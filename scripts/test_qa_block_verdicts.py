#!/usr/bin/env python3
"""Unit and worked-case regression tests for scripts/qa-block-verdicts.py (bean qou-tv74)."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve().parent / "qa-block-verdicts.py"
spec = importlib.util.spec_from_file_location("qa_block_verdicts", SCRIPT_PATH)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class QaBlockVerdictsTests(unittest.TestCase):
    def test_uic_worked_case_from_qou_tv74(self) -> None:
        """Verify the exact worked case of bean qou-tv74 is surfaced by label and path."""
        stem = mod.resolve_block_stem("tbl:unified-iterative-correction-table-data")
        self.assertEqual(
            stem.as_posix(),
            "folio/quantum-observable-universe/mass-theory/unified-iterative-correction-table-data",
        )
        report = mod.collect_verdicts(stem, min_chars=400)
        self.assertGreaterEqual(report["count"], 1)
        trap_hits = [
            v for v in report["verdicts"]
            if v["criterion"] == "trap-superlative" and "fourth column" in v["text"]
        ]
        self.assertEqual(len(trap_hits), 1)
        self.assertEqual(trap_hits[0]["reviewer_kind"], "agent")

    def test_unions_all_three_stores_and_tags_freshness(self) -> None:
        """Verify deduplication and FRESH/STALE/UNHASHED tagging across all 3 QA stores."""
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            blk_dir = root / "folio" / "demo" / "ch1"
            att_dir = root / "test" / "attestations" / "block-qa" / "folio" / "demo" / "ch1"
            res_dir = root / "test" / "results" / "block-qa" / "folio" / "demo" / "ch1"
            blk_dir.mkdir(parents=True)
            att_dir.mkdir(parents=True)
            res_dir.mkdir(parents=True)

            md_bytes = b"Sample mathematical content.\n"
            (blk_dir / "sample.md").write_bytes(md_bytes)
            (blk_dir / "sample.ts").write_text('export default { label: "rem:sample" };\n', encoding="utf-8")
            live_hash = mod.sha12(md_bytes)

            shared_entry = {
                "field_hash": {"md": live_hash},
                "result": "pass",
                "reviewer": {"kind": "agent", "id": "agent:a1"},
                "reviewed_at": "2026-11-24T00:00:00Z",
                "evidence": "Fresh verdict shared across sibling and attestations.",
            }
            att_only_entry = {
                "field_hash": {"md": "000000000000"},
                "result": "warn",
                "reviewer": {"kind": "agent", "id": "agent:a2"},
                "reviewed_at": "2026-10-01T00:00:00Z",
                "evidence": "Prior analysis stored only in attestations.",
            }
            res_only_entry = {
                "result": "pass",
                "reviewer": {"kind": "human", "id": "litlfred"},
                "reviewed_at": "2026-11-20T00:00:00Z",
                "notes": "Unhashed human note in results tree.",
            }
            script_entry = {
                "field_hash": {"md": live_hash},
                "result": "pass",
                "reviewer": {"kind": "script", "id": "qa-sweep"},
            }

            (blk_dir / "sample.qa.json").write_text(
                json.dumps({"criteria": {"c1": [shared_entry, script_entry]}}),
                encoding="utf-8",
            )
            (att_dir / "sample.attestations.json").write_text(
                json.dumps({"criteria": {"c1": [shared_entry], "c2": [att_only_entry]}}),
                encoding="utf-8",
            )
            (res_dir / "sample.qa.json").write_text(
                json.dumps({"criteria": {"c3": [res_only_entry]}}),
                encoding="utf-8",
            )

            stem = mod.resolve_block_stem("rem:sample", repo_root=root)
            rep = mod.collect_verdicts(stem, repo_root=root)
            self.assertEqual(rep["count"], 3)
            by_crit = {v["criterion"]: v for v in rep["verdicts"]}
            self.assertEqual(by_crit["c1"]["freshness"], "FRESH")
            self.assertEqual(by_crit["c2"]["freshness"], "STALE")
            self.assertEqual(by_crit["c3"]["freshness"], "UNHASHED")


if __name__ == "__main__":
    unittest.main()
