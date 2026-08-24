#!/usr/bin/env python3
"""Witnesses that publish LP-dual field NAMES with no values behind them.

Bean `qou-cds2` (found while reviving `confinement-operator-selection.py`).

## What this measures

AGENTS.md makes the LP/SDP primal-dual block first-class: every
operator-selection compute "MUST emit BOTH primal and dual variables in its
witness JSON", because the dual variables *are* the binding-energy shadow
prices. `lp_dual_witness_validator.py` enforces it.

That validator flags a witness only when BOTH hold:

  1. its filename or description carries an LP/SDP hint, AND
  2. its sibling `.py` actually imports an LP/SDP solver.

Step 2 is a deliberate false-positive filter, documented in that file as
excluding "precomputed shadow prices". It works: measured here, every flagged
witness carrying dual fields carries them **fully populated, zero nulls**.

The gap is on the other side of the filter. A witness can carry all six dual
field names — `y0_star`, `y_star`, `active_set`, `primal_obj`, `dual_obj`,
`duality_gap` — with **every value `None`**, from a producer that solves no LP,
and the validator never looks at it. To a reader, to a grep, and to anything
that checks field PRESENCE rather than field CONTENT, such a witness is
indistinguishable from one carrying real shadow prices.

This is NOT a claim that the validator is wrong; it does what it documents.
It is a claim that presence of the names is not evidence of duals, and that
the population where the names appear without values is worth knowing.

## The case that prompted it

`confinement-operator-selection.witness.json` carries all six as `None`, plus
three `*_status` fields reading "STUB -- re-run script through
lp_dual_solver.py to populate". Its producer has no LP at all: the three
`RANKING` passes are sorts, not optimisations, so there is no primal to take a
dual of. The stub note asks for a wiring step that is not posed.

Two of the others are *named* for the thing they do not contain
(`shadow-price-c-321-q0`, `paper-six-term-shadow-price-sweep`).

## Verdicts

  STUB      every dual field present is `None` — names, no values
  PARTIAL   some present, some `None`
  POPULATED all present fields carry values

Exit 1 under `--strict` if any STUB witness is found. Advisory by default:
this reports a naming/labelling hazard, not a wrong number, and a gate red on
arrival gets skipped.

Usage:
    python3 computations/audits/lp_dual_stub_field_audit.py
    python3 computations/audits/lp_dual_stub_field_audit.py --strict
"""

from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent

#: The six names AGENTS.md requires of an operator-selection witness.
DUAL_FIELDS = (
    "y0_star",
    "y_star",
    "active_set",
    "primal_obj",
    "dual_obj",
    "duality_gap",
)


def _load_validator():
    """Import `lp_dual_witness_validator` by path (its name is not a module)."""
    path = COMPUTATIONS / "lp_dual_witness_validator.py"
    # It does a bare `from lp_dual_solver import ...`, so `computations/`
    # has to be importable before the module body runs.
    if str(COMPUTATIONS) not in sys.path:
        sys.path.insert(0, str(COMPUTATIONS))
    spec = importlib.util.spec_from_file_location("_lpv", path)
    if spec is None or spec.loader is None:
        return None
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as exc:  # noqa: BLE001 — report, do not die
        print(f"  (note: lp_dual_witness_validator unavailable: {exc};"
              f" the flagged/unflagged split is omitted)")
        return None
    return mod


def _occurrences(obj, key: str, out: list) -> None:
    """EVERY occurrence of `key`, at any depth, including inside lists.

    An earlier version of this audit recorded only the FIRST occurrence
    (dict `setdefault`, and only the head of each list). That is a
    false-positive generator, and `e-0-lp-dual-h3.witness.json` is the shape
    that exposes it: a top-level `y0_star: None` sitting above eight
    per-target result blocks whose `y_star` / `active_set` / `primal_obj` /
    `dual_obj` are all real. First-occurrence would read the top-level null
    and could call such a witness STUB while it carries genuine duals.

    Re-measured across all nine affected files when this was fixed: ZERO
    verdicts changed -- each of the eight STUB witnesses has exactly one
    occurrence of each field and it is null. The fix removes a latent
    misclassification, it did not correct a reported one.
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                out.append(v)
            _occurrences(v, key, out)
    elif isinstance(obj, list):
        for x in obj:
            _occurrences(x, key, out)


def dual_readers(stems: list[str]) -> list[tuple[str, list[str], list[str]]]:
    """Python files that name one of `stems` AND touch a dual field name.

    This answers the question the STUB list raises but does not settle: is it
    safe to DROP the null fields, or does something read them?

    Deliberately over-reports -- it is a textual co-occurrence scan, so a file
    that reads duals from a *different* witness while merely mentioning one of
    these counts as a hit. That is the safe direction: the caller adjudicates
    each hit at the call site, and a scan that under-reported would licence a
    deletion that breaks a reader.

    Measured on 2026-08-24 over 3737 files: three hits, all adjudicated as
    NOT reading duals from a stub witness --
      * `onepb_status_dashboard.py` loads the confinement witness for its Gram
        matrix; its dual reads come from `lp-confinement-nf-forcing`.
      * `deuteron_from_scratch_ledger.py` lists the confinement witness in
        `PRODUCTION_WITNESSES`; its dual reads come from `deuteron-real-sdp`.
      * `lp_dual_solver.py` names it in prose.
    So no reader consumes a null dual, and dropping the names breaks nothing.
    Re-run rather than trusting that sentence -- it ages with the tree.
    """
    import re

    repo = COMPUTATIONS.parent
    out: list[tuple[str, list[str], list[str]]] = []
    for f in sorted(repo.glob("**/*.py")):
        parts = set(f.parts)
        if "_deprecated" in parts or "_internal" in parts or ".git" in parts:
            continue
        if f.name == Path(__file__).name:
            continue  # this audit names every stem by construction
        try:
            text = f.read_text(errors="ignore")
        except OSError:
            continue
        ws = [w for w in stems if w in text]
        if not ws:
            continue
        ds = [d for d in DUAL_FIELDS
              if re.search(r"""["']""" + d + r"""["']""", text)
              or re.search(r"\." + d + r"\b", text)]
        if ds:
            out.append((str(f.relative_to(repo)), ws, ds))
    return out


def classify(path: Path) -> tuple[str, list[str], list[str], dict] | None:
    """Verdict, plus the per-field occurrence counts the verdict rests on.

    A field counts as populated if ANY of its occurrences is non-null -- one
    real nested value outweighs a top-level placeholder, which is the only
    reading under which "this witness carries duals" is true.
    """
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError):
        return None

    counts: dict[str, tuple[int, int]] = {}
    for k in DUAL_FIELDS:
        occ: list = []
        _occurrences(data, k, occ)
        if occ:
            counts[k] = (len(occ), sum(1 for v in occ if v is not None))

    present = list(counts)
    if not present:
        return None
    nulls = [k for k, (_n, nonnull) in counts.items() if nonnull == 0]
    if not nulls:
        return "POPULATED", present, nulls, counts
    if len(nulls) == len(present):
        return "STUB", present, nulls, counts
    return "PARTIAL", present, nulls, counts


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any STUB witness is found")
    args = ap.parse_args(argv)

    validator = _load_validator()

    rows = []
    for f in sorted(glob.glob(str(COMPUTATIONS / "**" / "*.witness.json"),
                              recursive=True)):
        if "_deprecated" in f:
            continue
        p = Path(f)
        verdict = classify(p)
        if verdict is None:
            continue
        kind, present, nulls, counts = verdict
        flagged = False
        if validator is not None:
            try:
                flagged = bool(validator.is_lp_sdp_witness(p)[0])
            except Exception:  # noqa: BLE001 - a validator crash must not
                flagged = False  # take the audit down with it
        rows.append((p, kind, present, nulls, flagged, counts))

    stubs = [r for r in rows if r[1] == "STUB"]
    partial = [r for r in rows if r[1] == "PARTIAL"]
    populated = [r for r in rows if r[1] == "POPULATED"]

    print("=" * 72)
    print("  LP-dual field names carried without values")
    print("=" * 72)
    print(f"  witnesses carrying any dual field : {len(rows)}")
    print(f"    POPULATED                       : {len(populated)}")
    print(f"    PARTIAL                         : {len(partial)}")
    print(f"    STUB (names only, all None)     : {len(stubs)}")
    print()

    # The cross-tabulation is the point: it separates "the validator is
    # missing these" from "the validator is not looking at these".
    flagged_stub = [r for r in stubs if r[4]]
    print(f"  of the STUB witnesses, flagged by lp_dual_witness_validator: "
          f"{len(flagged_stub)}")
    print("    (a nonzero count here WOULD be a validator defect -- a null"
          " passing a presence check)")
    print()

    for label, sel in (("STUB", stubs), ("PARTIAL", partial)):
        if not sel:
            continue
        print(f"  {label}:")
        for p, _kind, present, nulls, flagged, counts in sel:
            rel = p.relative_to(COMPUTATIONS)
            mark = " [flagged]" if flagged else ""
            print(f"    {rel}{mark}")
            print(f"        present={len(present)} null={len(nulls)}: "
                  f"{', '.join(nulls)}")
            occ = ", ".join(f"{k}:{n}occ/{nn}nonnull"
                            for k, (n, nn) in sorted(counts.items()))
            print(f"        occurrences: {occ}")
        print()

    if stubs:
        print("  These are invisible to lp_dual_witness_validator BY DESIGN:")
        print("  its step 2 requires the sibling script to import an LP/SDP")
        print("  solver, and a producer that solves no LP does not. The names")
        print("  are still published. Presence of the names is not evidence")
        print("  of duals -- check a value before citing one.")

    if stubs:
        stems = [p.name.replace(".witness.json", "") for p, *_ in stubs]
        readers = dual_readers(stems)
        print()
        print("  Can the null names simply be DROPPED? -- co-occurrence scan")
        print(f"    files naming a STUB witness AND a dual field: {len(readers)}")
        for f, ws, ds in readers:
            print(f"      {f}")
            print(f"          names: {', '.join(ws)}")
            print(f"          duals: {', '.join(ds)}")
        if readers:
            print("    Over-reports by design: a file reading duals from a")
            print("    DIFFERENT witness while mentioning one of these counts.")
            print("    Adjudicate each at the call site before deleting.")
        else:
            print("    Nothing reads a dual field anywhere near these witnesses.")

    if args.strict and stubs:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
