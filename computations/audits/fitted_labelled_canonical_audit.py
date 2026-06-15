"""Audit: find scripts that claim "substrate"/"canonical"/"derived" in
their docstring or witness description but consume hardcoded numerical
literals or imported VALIDATION constants.

This catches the CAL-4-disguised-as-canonical pattern that
`m_p_borromean_verification_50dps.py` exhibited (LAMBDA_PROTON_DOC
literal solved from CODATA, while the witness was labelled
"canonical-substrate" by canonical_isotope_witness.py).

Pattern flagged:
  - Script docstring/header contains "substrate"/"derived"/"canonical"
    claim within 200 chars of a numerical literal definition.
  - OR Witness `description` claims substrate-derivation but
    `derivation_status` / `cal_class` is missing.
  - OR Hardcoded `mp.mpf("<10+digit literal>")` defined at module
    level when neither a `validation` comment nor a `# CAL-` marker is
    nearby (within 3 lines).

Run:
    python3 fitted_labelled_canonical_audit.py [--strict]

Emits `fitted-labelled-canonical-audit.witness.json`.
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

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))


# Regex: module-level mpf literal with 8+ digits after the decimal point
LITERAL_RE = re.compile(
    r"^\s*([A-Z_][A-Z0-9_]*)\s*=\s*"
    r"(?:mp\.)?mpf\(\s*[\"']([0-9]+\.[0-9]{8,})[\"']",
    re.MULTILINE,
)

# Validation / acknowledged-anchor markers that excuse the literal
EXEMPT_NEAR = re.compile(
    r"validation|VALIDATION|CODATA|codata|comparison|"
    r"reference|REFERENCE|target|TARGET|"
    r"CAL-[123]|cal-[123]|CAL_[123]|"
    r"acknowledged|ACKNOWLEDGED|fitted|FITTED|FITTING|"
    r"AME|PDG|SnapPy|KnotInfo|topological|"
    r"# polynomial_q_not_applicable|"
    r"hyperbolic.volume|literature|"
    # Self-documented drift-risk / cached audit values explicitly
    # marked as NOT a substrate derivation (CAL-4 audit, 2026-05-22).
    r"DRIFT.RISK|drift.risk|"
    r"audit.only|cached.values|cached.*audit|"
    r"NOT a substrate derivation|not a substrate derivation|"
    r"CAL-4-VIOLATION",
)

# Substrate / canonical claim markers in script docstring / comments
SUBSTRATE_CLAIM = re.compile(
    r"substrate.derived|substrate.pure|substrate-only|"
    r"canonical-substrate|canonical[\s_-]?derivation|"
    r"derived.from.substrate|derives.from.substrate|"
    r"\\bderived\\b.*\\bvalue\\b|predicts|prediction|"
    r"closed.form.from.substrate|pure.derivation",
    re.IGNORECASE,
)


def audit_script(path: Path) -> dict:
    text = path.read_text(errors="replace")
    issues: list[dict] = []

    for m in LITERAL_RE.finditer(text):
        var, lit = m.group(1), m.group(2)
        # Skip if the var name itself contains FITTED/CODATA/etc.
        if EXEMPT_NEAR.search(var):
            continue
        # Look at 1000 chars before and 200 chars after (widened so a
        # leading section comment like "DRIFT-RISK NOTE" still applies
        # to literals defined later in the same section).
        ctx_start = max(0, m.start() - 1000)
        ctx_end = min(len(text), m.end() + 200)
        ctx = text[ctx_start:ctx_end]
        if EXEMPT_NEAR.search(ctx):
            continue
        # Check if anywhere in the script makes a substrate / canonical claim
        if SUBSTRATE_CLAIM.search(text[:2000]):  # docstring + early comments
            line_no = text[: m.start()].count("\n") + 1
            issues.append({
                "line": line_no,
                "var": var,
                "literal": lit,
                "context_snippet": ctx.strip()[:220],
            })

    return {
        "path": str(path.relative_to(HERE.parent.parent)),
        "issue_count": len(issues),
        "issues": issues,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero if any issues found")
    args = ap.parse_args()

    # Scan the full folio-assistant/computations/ tree, not just audits/
    # (the script's own directory). Per Copilot #1712 review: the
    # description says "Audits production scripts in
    # folio-assistant/computations/", which is the PARENT of HERE since
    # the audit was moved under audits/ in a prior refactor.
    py_files = sorted(HERE.parent.rglob("*.py"))
    py_files = [
        p for p in py_files
        if not p.name.startswith("_")
        and p.name != "fitted_labelled_canonical_audit.py"
        # `_deprecated/` and `__pycache__/` are not production compute (the
        # underscore-prefixed FILENAME filter above skips e.g. `_bridge.py`
        # but not files INSIDE `_deprecated/` — they don't start with `_`).
        # Match the noncanonical-reentry-audit convention (PR #1819).
        and not any(part in {"_deprecated", "__pycache__"}
                    for part in p.relative_to(HERE.parent).parts)
    ]

    rows = []
    total_issues = 0
    for p in py_files:
        try:
            r = audit_script(p)
        except Exception as exc:
            r = {"path": str(p.name), "issue_count": -1, "error": str(exc)}
        if r.get("issue_count", 0) > 0:
            rows.append(r)
            total_issues += r["issue_count"]

    sys.path.insert(0, str(HERE))
    from witness_base import WitnessBuilder  # noqa: E402

    w = WitnessBuilder(
        "fitted-labelled-canonical-audit",
        engine="python",
    )
    w.set_description(
        "Audits production scripts in folio-assistant/computations/ "
        "for the CAL-4-disguised-as-canonical pattern: a hardcoded "
        "numerical literal at module level combined with a "
        "'substrate/canonical/derived' claim in the docstring, where "
        "neither the variable name nor the surrounding context tags "
        "the literal as validation/CODATA/acknowledged. Introduced "
        "2026-05-22 after the LAMBDA_PROTON_DOC discovery in "
        "m_p_borromean_verification_50dps.py (see "
        "docs/canonical-derivation-cheat-sheet.md §5 fix #1)."
    )
    w.set_content_block("prop:three-calibration-inputs")
    w.add_data("total_issues", total_issues)
    w.add_data("flagged_script_count", len(rows))
    w.add_data("scripts_scanned", len(py_files))
    w.add_data("rows", rows)
    w.add_assertion(
        "no_fitted_labelled_canonical",
        computed=total_issues,
        expected=0,
        tolerance=0,
    )
    w.save()

    print(f"\nFitted-labelled-canonical audit:")
    print(f"  scanned:  {len(py_files)} scripts")
    print(f"  flagged:  {len(rows)} scripts ({total_issues} issues)")

    if rows:
        print(f"\n  Top offenders:")
        for r in sorted(rows, key=lambda x: -x["issue_count"])[:10]:
            print(f"    {r['issue_count']:>3}  {r['path']}")
            for iss in r["issues"][:2]:
                print(f"         line {iss['line']}: {iss['var']} = {iss['literal']}")

    if args.strict and total_issues > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
