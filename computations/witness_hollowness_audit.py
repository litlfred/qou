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


def _occurrences(obj, key: str, out: list) -> None:
    """EVERY occurrence of `key`, at any depth, including inside lists.

    `_find` above is shallow by design -- top level, then one level into
    `witness`/`data`/`result`. That is enough for H1 but not for H2: a
    witness can nest its dual block per-target inside a list, where a
    shallow lookup cannot see it.

    Measured 2026-08-24: switching H2 to this walk gains two offences the
    shallow lookup missed -- `option-b-proton-mass-full-chain` and
    `r5-full-canonical-knot-solver`, both with an empty `active_set` nested
    past the head of a list.
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                out.append(v)
            _occurrences(v, key, out)
    elif isinstance(obj, list):
        for x in obj:
            _occurrences(x, key, out)


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
            # A field counts as POPULATED if ANY occurrence is non-empty --
            # one real nested value outweighs a top-level placeholder, which
            # is the only reading under which "this witness carries duals" is
            # true. `e-0-lp-dual-h3` is the shape that forces this: a
            # top-level `y0_star: None` above eight per-target blocks whose
            # other five fields are all real.
            occ: list = []
            _occurrences(w, fld, occ)
            present = bool(occ)
            v = next((x for x in occ if not _is_empty(x)), None)
            if present:
                any_present = True
                if all(_is_empty(x) for x in occ):
                    null_fields.append(fld)
        if any_present and null_fields:
            offences.append({"path": path, "kind": "null-dual",
                             "detail": "LP/SDP dual fields present but null/empty: "
                                       + ", ".join(null_fields)})
    return offences


def dual_readers(stems: list[str]) -> list[tuple[str, list[str], list[str]]]:
    """Python files that name one of `stems` AND touch a dual field name.

    Answers the question an H2 list raises but does not settle: is it safe to
    DROP the empty names, or does something read them?

    Deliberately OVER-reports -- textual co-occurrence, so a file reading
    duals from a *different* witness while merely mentioning one of these
    counts as a hit, and the caller adjudicates at the call site. A scan that
    under-reported would licence a deletion that breaks a reader, which is the
    expensive direction to be wrong in.

    Measured 2026-08-24 over ~3700 files: three hits on the confinement
    witness, all adjudicated as NOT reading duals from it --
      * `onepb_status_dashboard.py` loads it for its Gram matrix; its dual
        reads come from `lp-confinement-nf-forcing`.
      * `deuteron_from_scratch_ledger.py` lists it in `PRODUCTION_WITNESSES`;
        its dual reads come from `deuteron-real-sdp`.
      * `lp_dual_solver.py` names it in prose.
    Re-run rather than trusting that sentence -- it ages with the tree.
    """
    out: list[tuple[str, list[str], list[str]]] = []
    self_name = os.path.basename(__file__)
    for f in sorted(glob.glob(os.path.join(ROOT, "**", "*.py"), recursive=True)):
        parts = f.split(os.sep)
        if "_deprecated" in parts or "_internal" in parts or ".git" in parts:
            continue
        if os.path.basename(f) == self_name:
            continue  # names every stem by construction
        try:
            with open(f, errors="ignore") as fh:
                text = fh.read()
        except OSError:
            continue
        ws = [w for w in stems if w in text]
        if not ws:
            continue
        ds = [d for d in DUAL_FIELDS
              if re.search(r"""["']""" + d + r"""["']""", text)
              or re.search(r"\." + d + r"\b", text)]
        if ds:
            out.append((os.path.relpath(f, ROOT), ws, ds))
    return out


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
    nulls = [o for o in all_off if o["kind"] == "null-dual"]
    if nulls and not as_json:
        stems = [os.path.basename(o["path"]).replace(".witness.json", "")
                 for o in nulls]
        readers = dual_readers(stems)
        print()
        print("  Can the empty names simply be DROPPED? -- co-occurrence scan")
        print(f"    files naming a null-dual witness AND a dual field: "
              f"{len(readers)}")
        for f, ws, ds in readers:
            print(f"      {f}")
            print(f"          names: {', '.join(ws)}")
            print(f"          duals: {', '.join(ds)}")
        if readers:
            print("    Over-reports by design: a file reading duals from a")
            print("    DIFFERENT witness while mentioning one of these counts.")
            print("    Adjudicate each at the call site before deleting.")
        else:
            print("    Nothing reads a dual field anywhere near these.")

    return 1 if (strict and all_off) else 0


if __name__ == "__main__":
    sys.exit(main())
