"""Candidate-specific packaging policy regressions; these do not execute Word."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("build_release", Path(__file__).with_name("build_release.py"))
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)
ROOT = Path(__file__).resolve().parents[1]


class EvidencePolicyTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((ROOT / "RELEASE_MANIFEST.json").read_text(encoding="utf-8"))
        # Synthetic hashes only exercise the gate; this fixture is never written
        # into the release manifest or represented as native evidence.
        self.fixed = dict(BUILDER.MAC_FOCUSED_WINDOWS_ACCEPTANCE)
        self.fixed.update(candidate_sha256="1" * 64, audit_sha256="2" * 64)
        readiness = self.manifest["release_readiness"]
        acceptance = readiness["mac_focused_windows_acceptance"]
        acceptance.update(self.fixed)
        acceptance["preservation"] = dict.fromkeys(BUILDER.FOCUSED_WINDOWS_PRESERVATION, True)
        readiness["source_audit"] = {
            "status": "PASS_BOUNDED_CHECKS_WITH_RETAINED_RAW_FAILURES",
            "audit_sha256": self.fixed["audit_sha256"],
            "baseline_sha256": self.fixed["processing_baseline_sha256"],
            "candidate_sha256": self.fixed["candidate_sha256"],
            "strict_raw_failures_retained": True,
            "audit_or_runtime_guards_weakened": False,
            **dict.fromkeys(BUILDER.FOCUSED_WINDOWS_PRESERVATION, True),
        }
        for platform, test in readiness["native_tests"].items():
            test.update(version="1.0.2", template_sha256=self.fixed["candidate_sha256"],
                        status="PASS" if platform == "windows" else "UNVERIFIED")
        readiness["native_tests"]["windows"]["evidence"] = ["Synthetic unit fixture; not a native runtime receipt"]
        readiness["native_tests"]["windows"]["receipt_sha256"] = self.fixed["native_receipt_sha256"]

    def accepted(self, manifest=None):
        with patch.object(BUILDER, "MAC_FOCUSED_WINDOWS_ACCEPTANCE", self.fixed):
            return BUILDER.accepted_mac_focused_windows_basis(
                manifest or self.manifest, self.fixed["candidate_sha256"])

    def test_complete_scoped_fixture_is_eligible_without_claiming_mac_pass(self):
        self.assertTrue(self.accepted())
        self.assertEqual(self.manifest["release_readiness"]["native_tests"]["mac"]["status"], "UNVERIFIED")

    def test_altered_candidate_or_focused_receipt_is_rejected(self):
        for location, key in (("mac_focused_windows_acceptance", "candidate_sha256"),
                              ("focused", "receipt_sha256")):
            candidate = copy.deepcopy(self.manifest)
            readiness = candidate["release_readiness"]
            target = readiness["predecessor_tests"]["Focused_Script_Tokens"] if location == "focused" else readiness[location]
            target[key] = "3" * 64
            with self.subTest(location=location), self.assertRaises(ValueError):
                self.accepted(candidate)

    def test_failed_or_blocked_mac_cannot_be_waived(self):
        for status in ("FAIL", "BLOCKED"):
            candidate = copy.deepcopy(self.manifest)
            candidate["release_readiness"]["native_tests"]["mac"]["status"] = status
            with self.subTest(status=status), self.assertRaises(ValueError):
                self.accepted(candidate)

    def test_each_source_guard_designer_and_author_decision_is_required(self):
        for key in BUILDER.FOCUSED_WINDOWS_PRESERVATION:
            candidate = copy.deepcopy(self.manifest)
            candidate["release_readiness"]["source_audit"][key] = False
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.accepted(candidate)
        for key in ("accepted", "mac_rerun_not_required_for_this_candidate"):
            candidate = copy.deepcopy(self.manifest)
            candidate["release_readiness"]["mac_focused_windows_acceptance"]["author_decision"][key] = False
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.accepted(candidate)

    def test_pending_identity_and_incomplete_probe_count_are_rejected(self):
        pending = dict(self.fixed, candidate_sha256="PENDING_FINAL_TEMPLATE")
        candidate = copy.deepcopy(self.manifest)
        candidate["release_readiness"]["mac_focused_windows_acceptance"].update(pending)
        with patch.object(BUILDER, "MAC_FOCUSED_WINDOWS_ACCEPTANCE", pending), self.assertRaises(ValueError):
            BUILDER.accepted_mac_focused_windows_basis(candidate, pending["candidate_sha256"])
        candidate = copy.deepcopy(self.manifest)
        candidate["release_readiness"]["predecessor_tests"]["Focused_Script_Tokens"]["style_probes"] = 32
        with self.assertRaises(ValueError):
            self.accepted(candidate)

    def test_missing_native_evidence_or_suppressed_raw_failures_are_rejected(self):
        for target, key, value in (("native", "evidence", []),
                                   ("audit", "strict_raw_failures_retained", False),
                                   ("audit", "audit_or_runtime_guards_weakened", True)):
            candidate = copy.deepcopy(self.manifest)
            readiness = candidate["release_readiness"]
            record = readiness["native_tests"]["windows"] if target == "native" else readiness["source_audit"]
            record[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.accepted(candidate)

    def test_historical_101_exact_acceptance_still_validates(self):
        historical = self.manifest["release_readiness"]["predecessor_tests"]["Published_1_0_1"]
        frozen = {
            "version": "1.0.1",
            "release_readiness": {
                "native_tests": copy.deepcopy(historical["native_tests"]),
                "source_audit": copy.deepcopy(historical["source_audit"]),
                "mac_version_only_acceptance": copy.deepcopy(historical["mac_version_only_acceptance"]),
                "predecessor_tests": {"Final_1_0_0": self.manifest["release_readiness"]["predecessor_tests"]["Final_1_0_0"]},
            },
        }
        self.assertTrue(BUILDER.accepted_mac_version_only_basis(frozen, historical["template_sha256"]))
        frozen["version"] = "1.0.2"
        with self.assertRaises(ValueError):
            BUILDER.accepted_mac_version_only_basis(frozen, historical["template_sha256"])


if __name__ == "__main__":
    unittest.main()
