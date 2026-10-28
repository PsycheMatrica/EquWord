#!/usr/bin/env python3
"""Verify accepted release bytes and build EquWord.zip using only Python's standard library."""

import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import stat
import sys
from zipfile import ZipFile, ZipInfo, ZIP_STORED


PACKAGE_FILES = {
    "CITATION.cff",
    "LICENSE.txt",
    "README.txt",
    "ResearchEquationFormatter.dotm",
    "Tutorial/REF_Practice.docx",
    "Tutorial/Research_Equation_Formatter_Quick_Start.pdf",
}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def is_link_or_reparse_point(path):
    info = path.lstat()
    return (stat.S_ISLNK(info.st_mode)
            or bool(getattr(info, "st_file_attributes", 0) & 0x400))


def package_paths(package):
    require(not is_link_or_reparse_point(package) and package.is_dir(),
            "package/ must be a real directory, without a link or reparse point.")
    paths = []
    pending = [package]
    while pending:
        for path in sorted(pending.pop().iterdir()):
            # Inspect before descending, including on Python versions without
            # Path.is_junction(), so junction cycles cannot be traversed.
            require(not is_link_or_reparse_point(path),
                    "Links and reparse points are not permitted in package/: " + str(path))
            require(path.is_file() or path.is_dir(), "Unsupported package entry: " + str(path))
            paths.append(path)
            if path.is_dir():
                pending.append(path)
    return paths


def verify_package(root):
    manifest = json.loads((root / "RELEASE_MANIFEST.json").read_text(encoding="utf-8"))
    require(manifest.get("schema_version") == 1, "Unsupported release manifest schema.")
    expected = manifest["files"]
    require(set(expected) == PACKAGE_FILES, "Manifest must list exactly the six approved package files.")
    package = root / "package"
    paths = package_paths(package)
    actual = {p.relative_to(package).as_posix() for p in paths if p.is_file()}
    require(actual == PACKAGE_FILES,
            "Package file list differs: missing={}, extra={}. No source exports or raw test files are allowed."
            .format(sorted(PACKAGE_FILES - actual), sorted(actual - PACKAGE_FILES)))
    require(all(p.is_file() or p.is_dir() for p in paths), "Unsupported filesystem entry in package/.")
    files = {name: (package / name).read_bytes() for name in sorted(PACKAGE_FILES)}
    for name, data in files.items():
        entry = expected[name]
        require(len(data) == entry["bytes"], "Size mismatch: " + name)
        require(sha256(data) == entry["sha256"], "SHA-256 mismatch: " + name)
    require((root / "CITATION.cff").read_bytes() == files["CITATION.cff"],
            "Root and package CITATION.cff must be identical.")
    require((root / "LICENSE.txt").read_bytes() == files["LICENSE.txt"],
            "Root and package LICENSE.txt must be identical.")
    version = manifest["version"]
    require(isinstance(version, str) and version, "Manifest version must be a nonempty string.")
    cff = files["CITATION.cff"].decode("utf-8")
    cff_version = re.search(r"^version:\s*[\"']?([^\"'\r\n]+)[\"']?\s*$", cff, re.MULTILINE)
    require(cff_version is not None and cff_version.group(1).strip() == version,
            "CITATION.cff version differs from the release manifest.")
    candidate = manifest["verified_template"]
    require(candidate["filename"] == "ResearchEquationFormatter.dotm",
            "Unexpected verified template filename.")
    require(candidate["version"] == version, "Verified template version differs from release version.")
    require(candidate["sha256"] == sha256(files[candidate["filename"]]),
            "Verified native-test candidate differs from the package template.")
    timestamp = tuple(manifest["zip_timestamp"])
    require(timestamp == (2026, 10, 27, 0, 0, 0),
            "The reproducible ZIP timestamp must remain 2026-10-27 00:00:00.")
    return manifest, files, timestamp


def make_archive(files, timestamp):
    buffer = io.BytesIO()
    with ZipFile(buffer, "w", compression=ZIP_STORED) as archive:
        for name, data in sorted(files.items()):
            entry = ZipInfo(name, timestamp)
            entry.compress_type = ZIP_STORED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, data)
    result = buffer.getvalue()
    with ZipFile(io.BytesIO(result)) as archive:
        require(archive.testzip() is None, "Generated ZIP failed CRC verification.")
        require(archive.namelist() == sorted(files), "Generated ZIP member list differs.")
        require(all(archive.read(name) == data for name, data in files.items()),
                "Generated ZIP member bytes differ.")
    return result


def write_new_or_identical(output_dir, outputs):
    require(not output_dir.exists() or output_dir.is_dir(), "Output location is not a directory.")
    for filename, data in outputs.items():
        path = output_dir / filename
        require(not path.is_symlink(), "Refusing linked output file: " + str(path))
        require(not path.exists() or (path.is_file() and path.read_bytes() == data),
                "Refusing to overwrite a different existing asset: " + str(path)
                + ". Choose a new --output-dir.")
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, data in outputs.items():
        path = output_dir / filename
        if not path.exists():
            # Exclusive creation also prevents a file appearing after the preflight
            # checks from being overwritten.
            with path.open("xb") as handle:
                handle.write(data)
        require(path.read_bytes() == data, "Output verification failed: " + str(path))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path,
                        help="Absolute output directory; default: the ignored dist/ directory.")
    parser.add_argument("--verify-only", action="store_true", help="Verify package bytes without writing files.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest, files, timestamp = verify_package(root)
    archive_bytes = make_archive(files, timestamp)
    checksum = sha256(archive_bytes)
    if args.verify_only:
        print("Verified EquWord {}: six package files; candidate {}; ZIP SHA-256 {}"
              .format(manifest["version"], manifest["verified_template"]["sha256"], checksum))
        return
    if args.output_dir is not None:
        require(args.output_dir.is_absolute(), "--output-dir must be an absolute path.")
    output_dir = (args.output_dir or root / "dist").resolve()
    # In-repository build products belong only in the ignored dist/ tree.
    if output_dir == root or root in output_dir.parents:
        dist = root / "dist"
        require(output_dir == dist or dist in output_dir.parents,
                "An output directory inside the repository must be dist/ or a child of dist/.")
    require(".git" not in output_dir.parts, "Refusing output inside .git/.")
    require(output_dir not in root.parents, "Refusing to write release assets into a repository ancestor.")
    outputs = {
        "EquWord.zip": archive_bytes,
        "EquWord.zip.sha256": (checksum + "  EquWord.zip\n").encode("ascii"),
    }
    write_new_or_identical(output_dir, outputs)
    print("Verified and built EquWord {}: {} bytes\n{}\nSHA-256 {}"
          .format(manifest["version"], len(archive_bytes), output_dir / "EquWord.zip", checksum))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("Release build refused: " + str(error), file=sys.stderr)
        sys.exit(1)
