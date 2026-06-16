#!/usr/bin/env python3
"""Witness assertion gate — the VALUE complement to the staleness check.

Staleness detection (witness_dependency_drift.py) tells you a witness is
out of date; it does NOT tell you whether the value is *right*. A blind
"regenerate the stale witness" can therefore launder a regression — or
keep advertising a retired fit (see the hadron ⁴He case,
docs/audits/2026-06-16-hadron-knot-table-stale-witness-regression.md).

Every WitnessBuilder witness carries `assertions` (computed vs expected vs
tolerance) and `allPassed`. This gate scans for witnesses whose assertions
FAIL (`allPassed == false`), separating:

  - auditOnly / exploratory witnesses (failing assertions are EXPECTED —
    they record an open gap honestly), and
  - production witnesses (a failing assertion is actionable: a regression
    or a value that should not be committed).

Intended use on the regenerate path: after re-running a producer, run this
gate; block the refresh/PR if a PRODUCTION witness's `allPassed` flips to
false. As a standalone CI step it surfaces the current failing set.

Usage:
    python3 computations/witness_assertion_gate.py           # report; warn
    python3 computations/witness_assertion_gate.py --strict  # exit 1 on
                                                             # production fails
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _is_audit_only(w: dict, name: str) -> bool:
    """A witness is exploratory/audit-only (failing assertions expected) if
    it self-declares so, or its name marks it a probe/prototype."""
    if w.get("auditOnly") is True or w.get("audit_only") is True:
        return True
    if w.get("auditOnlyDoc") or w.get("audit_only_doc"):
        return True
    low = name.lower()
    return any(tag in low for tag in ("probe", "prototype", "-probe-", "exploratory"))


def scan(witness_path: Path) -> dict | None:
    """Return a record if the witness has failing assertions, else None."""
    try:
        w = json.loads(witness_path.read_text())
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None
    if not isinstance(w, dict):
        return None
    if w.get("allPassed") is not False:
        return None  # no assertions, or all passed
    asserts = w.get("assertions") or []
    failing = [a for a in asserts
               if isinstance(a, dict) and a.get("passed") is False]
    return {
        "witness": witness_path.name,
        "audit_only": _is_audit_only(w, witness_path.name),
        "n_failing": len(failing),
        "first_failing": (failing[0].get("name") if failing else None),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any PRODUCTION witness has failing assertions")
    args = ap.parse_args()

    prod_fail: list[dict] = []
    audit_fail: list[dict] = []
    n = 0
    for wp in sorted(HERE.rglob("*.witness.json")):
        n += 1
        rec = scan(wp)
        if rec is None:
            continue
        (audit_fail if rec["audit_only"] else prod_fail).append(rec)

    print(f"Checked {n} witnesses for assertion failures (allPassed=false).")
    print(f"  production (actionable): {len(prod_fail)}")
    print(f"  audit-only/exploratory (expected): {len(audit_fail)}")
    if prod_fail:
        print("\nProduction witnesses with FAILING assertions:")
        for r in prod_fail[:50]:
            print(f"  - {r['witness']}: {r['n_failing']} failing "
                  f"(first: {r['first_failing']})")
        if len(prod_fail) > 50:
            print(f"  ... and {len(prod_fail) - 50} more")
    return 1 if (prod_fail and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
