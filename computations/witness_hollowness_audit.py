#!/usr/bin/env python3
"""Witness-hollowness audit — devil's-advocate class-3 checker.

Catches witnesses that pass *presence-only* CI checks while carrying no
real content — the failure class the devils-advocate watcher surfaced
three times (empty-assertion "verified" witnesses; LP/SDP witnesses with
the dual certificate emitted as null VALUES). Complements
`lp_dual_witness_validator.py` (which checks the dual KEYS are present)
by checking the values are non-null / non-empty.

Two offence kinds:

  (H1) hollow-verification — `assertions` is present-and-empty (`[]`)
       AND the witness claims success (`allPassed: true`, or
       `status`/`verdict` ~ "verified"/"pass"). A green status backed by
       an empty assertion array verifies nothing. (A witness with NO
       `assertions` key uses a different schema and is not flagged — only
       an explicitly empty array is hollow.)

  (H2) null-dual — an LP/SDP/operator-selection witness (by name or
       description) whose dual fields (`y0_star`, `y_star`,
       `active_set`, `duality_gap`, `primal_obj`, `dual_obj`) are present
       as keys but null/empty. `lp_dual_witness_validator.py` checks
       presence; this checks the shadow prices were actually computed.

Report-only by default (exit 0). `--strict` exits 1 if any offence is
found (for opt-in CI gating). No witness is emitted (avoids drift).

Usage:
  python3 computations/witness_hollowness_audit.py [--strict] [--json]
"""
from __future__ import annotations
import json, sys, glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# H2 trigger: witness file name or description signalling an LP/SDP /
# operator-selection compute (mirrors lp_dual_witness_validator's hints).
LP_HINTS = ("lp-dual", "lp_dual", "operator-selection", "operator_selection",
            "shadow-price", "shadow_price", "primal-dual", "primal_dual",
            "lp-duality", "confinement-sdp", "confinement_sdp",
            "operator-selection-lp", "sdp")
DUAL_FIELDS = ("y0_star", "y_star", "active_set", "duality_gap",
               "primal_obj", "dual_obj")
VERIFIED_RE = re.compile(r"\b(verified|passed|pass|ok|success)\b", re.I)


def _is_empty(v) -> bool:
    return v is None or v == [] or v == {} or v == ""


def _claims_success(w: dict) -> bool:
    if w.get("allPassed") is True:
        return True
    for k in ("status", "verdict", "result"):
        v = w.get(k)
        if isinstance(v, str) and VERIFIED_RE.search(v):
            return True
    # nested witness.* mirror
    inner = w.get("witness")
    if isinstance(inner, dict):
        return _claims_success(inner)
    return False


def _looks_lp(path: str, w: dict) -> bool:
    blob = (os.path.basename(path) + " " +
            str(w.get("description", "")) + " " +
            str(w.get("computation", "")) + " " +
            str((w.get("witness") or {}).get("description", ""))).lower()
    return any(h in blob for h in LP_HINTS)


def _find(w: dict, key: str):
    """Shallow lookup, then one level into witness.* and data.*"""
    if key in w:
        return w[key], True
    for sub in ("witness", "data", "result"):
        d = w.get(sub)
        if isinstance(d, dict) and key in d:
            return d[key], True
    return None, False


def audit_one(path: str) -> list[dict]:
    try:
        with open(path) as f:
            w = json.load(f)
    except Exception as e:
        return [{"path": path, "kind": "unparseable", "detail": str(e)}]
    if not isinstance(w, dict):
        return []
    offences = []

    # H1 — hollow verification: assertions key PRESENT and empty [], AND
    # no OTHER non-empty validation array carries the checks (else the
    # witness validates via a different field and is not hollow).
    assertions, has_a = _find(w, "assertions")
    if _claims_success(w) and has_a and assertions == []:
        other = False
        for alt in ("checks", "tests", "comparisons", "crossChecks",
                    "cross_checks", "results", "validations"):
            v, present = _find(w, alt)
            if present and isinstance(v, (list, dict)) and len(v) > 0:
                other = True
                break
        if not other:
            offences.append({"path": path, "kind": "hollow-verification",
                             "detail": "claims success but assertions array is "
                                       "empty [] and no other validation array present"})

    # H2 — null dual on an LP/SDP witness
    if _looks_lp(path, w):
        null_fields = []
        any_present = False
        for fld in DUAL_FIELDS:
            v, present = _find(w, fld)
            if present:
                any_present = True
                if _is_empty(v):
                    null_fields.append(fld)
        if any_present and null_fields:
            offences.append({"path": path, "kind": "null-dual",
                             "detail": "LP/SDP dual fields present but null/empty: "
                                       + ", ".join(null_fields)})
    return offences


def main() -> int:
    strict = "--strict" in sys.argv
    as_json = "--json" in sys.argv
    include_deprecated = "--include-deprecated" in sys.argv
    paths = sorted(glob.glob(os.path.join(ROOT, "**", "*.witness.json"),
                             recursive=True))
    if not include_deprecated:
        paths = [p for p in paths if "_deprecated" + os.sep not in p
                 and os.sep + "_deprecated" + os.sep not in p]
    all_off = []
    for p in paths:
        all_off.extend(audit_one(p))
    rel = lambda p: os.path.relpath(p, ROOT)
    if as_json:
        print(json.dumps([{**o, "path": rel(o["path"])} for o in all_off], indent=2))
    else:
        if not all_off:
            print(f"witness-hollowness: clean — {len(paths)} witnesses scanned.")
        else:
            print(f"witness-hollowness: {len(all_off)} offence(s) across "
                  f"{len(paths)} witnesses:\n")
            for o in all_off:
                print(f"  [{o['kind']}] {rel(o['path'])}\n      {o['detail']}")
    return 1 if (strict and all_off) else 0


if __name__ == "__main__":
    sys.exit(main())
