#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.

═══════════════════════════════════════════════════════════════

Audit the calibration constant E_0 (CAL-3, free-neutron β-decay
Q-value) used across the QOU witness pipeline.

Per `prop:three-calibration-inputs` (CAL-3), every mass prediction
in the paper traces back to the hadronic energy scale

    E_0 = Q_β(n) / |Δ(net)|

with Q_β(n) the free-neutron β-decay Q-value. The paper pins
Q_β(n) = 0.78233341 MeV (PDG 2022, derived from m_n − m_p − m_e),
so E_0 inherits the PDG precision floor of ~7.7×10⁻⁷ relative.

This audit:
  1. Scans every `*.py` in `computations/` for
     E_0-related literals: `0.782`, `0.78233341`, `Q_BETA*`,
     `E_0_CALIBRATION_MEV`, etc.
  2. Categorises each occurrence by (file, anchor, sig-figs).
  3. Flags inconsistencies — multiple values for what should be
     the same constant, or pinnings other than Q_β(n) (e.g.
     proton-mass-anchored E_0, which is a forbidden second
     pinning per CAL-3).
  4. Computes the achievable precision floor from the PDG
     uncertainty budget on m_n, m_p, m_e and reports the
     downstream cap on every E_0-dependent quantity.

Output: `e0-calibration-audit.witness.json`

Usage:
    python3 computations/e0_calibration_audit.py
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp, mpf, sqrt

mp.dps = 30

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
OUT = HERE / "e0-calibration-audit.witness.json"

# ── PDG / CODATA 2022 inputs — centralised in codata_constants ──
from codata_constants import (
    M_N_MEV_VALIDATION as M_N_MEV,
    M_P_MEV_VALIDATION as M_P_MEV,
    M_E_MEV,
    Q_BETA_MEV as Q_BETA_N,
    M_N_MEV_VALIDATION_ERR as M_N_ERR,
    M_P_MEV_VALIDATION_ERR as M_P_ERR,
    M_E_MEV_ERR as M_E_ERR,
)
# All m_p, m_n imports above are validation-only comparators (audit script).
# Combined uncertainty (uncorrelated for atomic masses; this is an
# upper bound — neutron and proton mass measurements share some
# systematic anchors, so the true σ is slightly smaller).
Q_BETA_N_ERR = sqrt(M_N_ERR**2 + M_P_ERR**2 + M_E_ERR**2)
Q_BETA_N_REL = Q_BETA_N_ERR / Q_BETA_N

# Patterns to scan
PATTERNS = {
    "literal_0_782":          re.compile(r"\b0\.782\b(?!\d)"),
    "literal_0_78233341":     re.compile(r"\b0\.78233341\b"),
    "literal_0_78233":        re.compile(r"\b0\.78233\b(?!3)"),
    "E_0_CALIBRATION_MEV":    re.compile(r"E_0_CALIBRATION_MEV"),
    "Q_BETA_MEV":             re.compile(r"Q_BETA_MEV|Q_BETA_N|Q_b_codata"),
    "proton_mass_anchor":     re.compile(r"938\.272[0-9]*\s*/\s*\w*proton"),
}

# Files that ARE the canonical reference (excluded from
# "inconsistency" reporting; they are expected to mention E_0).
CANONICAL_REFS = {
    "e0_calibration_audit.py",  # this file
}


def _classify_line(line: str) -> str:
    """Classify a line as 'active' (code) or 'doc' (comment / string).

    Heuristic: ignore lines starting with `#`, or inside a triple-
    quoted block. Lines that are pure print-format strings are also
    treated as 'doc' for drift detection.
    """
    s = line.strip()
    if s.startswith("#"):
        return "doc"
    # Crude: print/string lines where the literal is inside quotes
    if (s.startswith(("print(", "print ", "raise ", "msg =",
                       'f"', "f'", '"', "'", "_msg")) or
            "f\"" in s and "0.782" in s and "{" not in s.split("0.782")[1][:5]):
        return "doc"
    return "active"


def scan() -> dict:
    py_files = sorted(
        (HERE).glob("*.py")
    )
    findings: list[dict] = []
    for f in py_files:
        if f.name in CANONICAL_REFS:
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        # Pre-compute docstring blocks (lines inside triple-quoted
        # blocks at module / function scope).
        in_doc = False
        doc_lines: set[int] = set()
        for ln, raw in enumerate(text.splitlines(), 1):
            tcount = raw.count(chr(34)*3) + raw.count(chr(39)*3)
            if in_doc:
                doc_lines.add(ln)
            if tcount % 2 == 1:
                in_doc = not in_doc
                if in_doc:
                    doc_lines.add(ln)
        for label, pat in PATTERNS.items():
            for m in pat.finditer(text):
                line_no = text[:m.start()].count("\n") + 1
                line = text.splitlines()[line_no - 1]
                kind = "doc" if line_no in doc_lines else _classify_line(line)
                findings.append({
                    "file": str(f.relative_to(ROOT)),
                    "line": line_no,
                    "pattern": label,
                    "match": m.group(),
                    "context": line.strip()[:160],
                    "kind": kind,
                })
    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="Exit 1 if inconsistencies are found")
    args = ap.parse_args()

    findings = scan()

    # Categorise
    by_pattern: dict[str, list] = {}
    for f in findings:
        by_pattern.setdefault(f["pattern"], []).append(f)

    # Inconsistencies are based on ACTIVE-code findings only;
    # docstring / comment / print-string mentions are documentary
    # and don't affect numerical results.
    def _active(label: str) -> list:
        return [f for f in by_pattern.get(label, [])
                if f.get("kind") == "active"]

    has_low_precision = bool(_active("literal_0_782"))
    has_high_precision = bool(_active("literal_0_78233341"))
    has_proton_anchor = bool(_active("proton_mass_anchor"))

    inconsistencies: list[str] = []
    if has_low_precision and has_high_precision:
        inconsistencies.append(
            "Mixed precision: same codebase uses both 0.782 (3 sig "
            "figs, ~4e-4 relative) and 0.78233341 (8 sig figs, "
            "~10⁻⁸ relative) for E_0 / Q_β(n)."
        )
    if has_proton_anchor:
        inconsistencies.append(
            "Proton-mass-anchored E_0 detected — this is a forbidden "
            "second pinning per CAL-3 (`prop:three-calibration-"
            "inputs`). E_0 must trace back to Q_β(n) only."
        )

    # Print summary
    print("=" * 72)
    print("E_0 calibration audit — CAL-3 (free-neutron β-decay Q-value)")
    print("=" * 72)
    print()
    print("Reference values (CODATA 2022):")
    print(f"  m_n           = {M_N_MEV} ± {M_N_ERR} MeV")
    print(f"  m_p           = {M_P_MEV} ± {M_P_ERR} MeV")
    print(f"  m_e           = {M_E_MEV} ± {M_E_ERR} MeV")
    print(f"  Q_β(n)        = {mp.nstr(Q_BETA_N, 12)} "
          f"± {mp.nstr(Q_BETA_N_ERR, 3)} MeV")
    print(f"  Q_β(n) rel    = {mp.nstr(Q_BETA_N_REL, 3)} "
          f"({mp.nstr(Q_BETA_N_REL * mpf(1e9), 3)} ppb)")
    print()
    print(f"Files scanned: {len(set(f['file'] for f in findings))}")
    print(f"Total matches: {len(findings)}")
    print()
    for label in PATTERNS:
        hits = by_pattern.get(label, [])
        active = [h for h in hits if h.get("kind") == "active"]
        print(f"  {label:<30} {len(hits):>3} total ({len(active)} active)")
    print()

    if inconsistencies:
        print("INCONSISTENCIES FOUND:")
        for issue in inconsistencies:
            print(f"  - {issue}")
        print()

    # Show the low-precision sites — these are the ones the user
    # may want to upgrade.
    if by_pattern.get("literal_0_782"):
        print("Sites using low-precision 0.782 (consider upgrading to")
        print("0.78233341 — same constant, 5 more sig figs):")
        for hit in by_pattern["literal_0_782"]:
            print(f"  {hit['file']}:{hit['line']}")
            print(f"    {hit['context']}")

    out = {
        "auditOnly": "docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md",
        "computation": "e0-calibration-audit",
        "description": (
            "Audit of E_0 / Q_β(n) calibration constants across "
            "computations. Reports value-precision "
            "drift, anchor-of-pinning violations vs CAL-3, and the "
            "PDG-derived uncertainty floor on every E_0-dependent "
            "quantity."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "reference_blocks": [
            "prop:three-calibration-inputs",
            "rem:calibration-inputs",
        ],
        "pdg_inputs_2022": {
            "m_n_MeV": str(M_N_MEV),
            "m_n_err_MeV": str(M_N_ERR),
            "m_p_MeV": str(M_P_MEV),
            "m_p_err_MeV": str(M_P_ERR),
            "m_e_MeV": str(M_E_MEV),
            "m_e_err_MeV": str(M_E_ERR),
        },
        "Q_beta_n": {
            "value_MeV": str(Q_BETA_N),
            "abs_err_MeV": str(Q_BETA_N_ERR),
            "rel_err": str(Q_BETA_N_REL),
            "rel_err_ppb": str(Q_BETA_N_REL * mpf(1e9)),
        },
        "precision_floor": (
            f"Every E_0-dependent quantity inherits a relative "
            f"uncertainty floor of {mp.nstr(Q_BETA_N_REL, 3)} "
            f"(~{mp.nstr(Q_BETA_N_REL * mpf(1e9), 3)} ppb). 1 ppb is "
            "NOT physically achievable on these quantities without "
            "a tighter Q_β(n) measurement."
        ),
        "findings_by_pattern": {
            label: by_pattern.get(label, []) for label in PATTERNS
        },
        "inconsistencies": inconsistencies,
        "achievable_precision_floor_ppb": str(
            Q_BETA_N_REL * mpf(1e9)
        ),
    }
    # Content-diff-aware write: preserve on-disk file if the new witness
    # differs only in ephemeral meta fields (commitSha, computedAt,
    # durationMs, scriptCommitSha). See witness_base._witnesses_substantively_equal.
    from witness_base import _witnesses_substantively_equal
    new_bytes = json.dumps(out, indent=2, ensure_ascii=False)
    if OUT.exists():
        try:
            existing = json.loads(OUT.read_text())
            if _witnesses_substantively_equal(existing, out):
                print("(witness unchanged — preserving on-disk commitSha for staleness)")
                print()
                # fall through to the existing post-write code path without
                # actually rewriting the file
            else:
                OUT.write_text(new_bytes)
        except (json.JSONDecodeError, OSError):
            OUT.write_text(new_bytes)
    else:
        OUT.write_text(new_bytes)
    print()
    print(f"  Witness: {OUT.name}")

    if args.strict and inconsistencies:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
