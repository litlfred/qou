#!/usr/bin/env python3
"""Find carriers whose fields are FREE PROPOSITIONAL VARIABLES.

## The shape

    class HabiroFlowSolution where
      expQ_solves_base_reeb      : Prop      -- <- a variable, not a claim
      fourier_diagonalises_qheat : Prop
      liTwoQ_volumetric          : Prop
      all_hold : expQ_solves_base_reeb ∧ fourier_diagonalises_qheat
                  ∧ liTwoQ_volumetric

Each docstring promises a named mathematical fact. The Lean says only "there
exist three propositions, and they hold" — so `instance : HabiroFlowSolution :=
⟨True, True, True, ⟨trivial, trivial, trivial⟩⟩` discharges it, and a downstream
`[HabiroFlowSolution] → P` is just `P`. This is the §3b-tax
`proof-claims-unencoded` failure mode: the docstring enumerates properties the
fields do not encode.

## Why a separate script

The existing detector keys `proof-claims-unencoded` on docstrings enumerating
>= 2 named properties, and on a field typed literally `: True`. A field typed
`: Prop` is neither, so this class is invisible to it — measured, **0 of these
carriers appear in the vacuity ledger under any criterion**.

## Not every free `Prop` field is a defect — that is what `--pinned` reports

A free `P : Prop` is harmless when another field PINS it:

    regular      : Prop
    regular_iff  : regular ↔ (0 < x)        -- pinned: `True` is now refutable

It is NOT pinned by a field that merely asserts it (`hP : P`) or uses it as an
antecedent (`impl : P → X`) — both survive `P := True`. The antecedent case is
its own, weaker defect: the carrier's *conditionality* is fake (the consequents
must hold outright) while the consequents themselves may still carry content.
So three buckets, reported separately:

    UNPINNED-EMPTY   no field constrains P, and no consequent survives  -> carrier asserts nothing
    UNPINNED-FAKE-IF P only appears as an antecedent -> conditionality is fake, consequents stand
    PINNED           some field ties P to real content -> not a defect

Usage:
    python3 scripts/free-prop-field-audit.py
    python3 scripts/free-prop-field-audit.py --show 20 --json out.json
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
# The type may be empty here: a field whose type starts on the NEXT line is
# written `name :` with nothing after the colon. An earlier version required
# >= 1 character and so DROPPED those fields entirely — which silently inflated
# UNPINNED-EMPTY, because the dropped field is very often the `impl_… : P → X`
# that makes the free `P` a fake-conditional rather than an empty one.
FIELD = re.compile(r"^\s+([A-Za-z_][A-Za-z0-9_']*)\s*:(.*?)\s*$")
FREE_PROP = re.compile(r"^\s+([A-Za-z_][A-Za-z0-9_']*)\s*:\s*Prop\s*$")
CARRIER = re.compile(r"^(class|structure)\s+([A-Za-z_][A-Za-z0-9_'.]*)")


def carriers(path: pathlib.Path):
    """Yield (name, decl_line, [(field, type, line)]) for each carrier."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    i = 0
    while i < len(lines):
        m = CARRIER.match(lines[i])
        if not m:
            i += 1
            continue
        name, start = m.group(2), i
        fields, j = [], i + 1
        while j < len(lines):
            ln = lines[j]
            if ln.strip() and not ln.startswith((" ", "\t")):
                break
            fm = FIELD.match(ln)
            if fm and not ln.lstrip().startswith(("--", "/-", "-/", "|")):
                ftype = fm.group(2)
                indent = len(ln) - len(ln.lstrip())
                k = j + 1
                while k < len(lines):
                    nxt = lines[k]
                    if not nxt.strip():
                        break
                    nind = len(nxt) - len(nxt.lstrip())
                    # A continuation is indented deeper than the field name, or
                    # (when the type began on the next line) at least as deep
                    # and not itself a new field.
                    if nind <= indent and ftype:
                        break
                    if FIELD.match(nxt) and nind <= indent:
                        break
                    if nxt.lstrip().startswith(("--", "/-", "-/")):
                        break
                    ftype += (" " if ftype else "") + nxt.strip()
                    k += 1
                fields.append((fm.group(1), ftype.strip(), j + 1))
            j += 1
        yield name, start + 1, fields
        i = j


def classify_free(field: str, fields: list[tuple[str, str, int]]) -> str:
    """PINNED / UNPINNED-FAKE-IF / UNPINNED-EMPTY for one free Prop field."""
    tok = re.compile(r"\b" + re.escape(field) + r"\b")
    f = re.escape(field)
    # A pin requires the free field to be an OPERAND of the iff/eq. Scanning
    # for any `=` in a field type that mentions it is wrong: in
    #     impl : P → n_linking_ops = 2 ∧ …
    # the `=` belongs to the CONSEQUENT and pins nothing. (That bug called this
    # exact carrier PINNED.)
    pin = re.compile(r"(?:(?<![A-Za-z0-9_'])" + f + r"\s*(?:↔|(?<![<>=!])=(?!=))"
                     r"|(?:↔|(?<![<>=!])=(?!=))\s*" + f + r"(?![A-Za-z0-9_']))")
    ante = re.compile(r"(?<![A-Za-z0-9_'])" + f + r"\s*(?:→|->)")
    saw_antecedent = False
    for name, ftype, _ln in fields:
        if name == field or not tok.search(ftype):
            continue
        if pin.search(ftype):
            return "PINNED"
        if ante.search(ftype):
            saw_antecedent = True
        # A bare assertion `hP : field` (or a conjunction of such) is not a pin.
    return "UNPINNED-FAKE-IF" if saw_antecedent else "UNPINNED-EMPTY"


# Four hand-read carriers, two of each verdict. Both bugs this script shipped
# with — dropping fields whose type starts on the next line, and reading an `=`
# in a CONSEQUENT as a pin — are caught here, and each flipped a case below.
SELF_TEST = [
    ("lean/QOU/Torsion/KnotParticleGeneration.lean",
     "KnotParticleGenerationContext", "particle_spectrum_generated",
     "UNPINNED-FAKE-IF"),
    ("lean/QOU/Habiro/FlowSolution.lean",
     "HabiroFlowSolution", "expQ_solves_base_reeb", "UNPINNED-EMPTY"),
    ("stochastic-mechanics/classical-limit-functor.lean",
     "ClassicalLimitFunctor", "is_exact", "UNPINNED-EMPTY"),
    ("lean/QOU/FluidDynamics/core_levi_form.lean",
     "CoreLeviFormContext", "levi_form_regular", "UNPINNED-FAKE-IF"),
]


def self_test() -> int:
    base = REPO / "content/quantum-observable-universe"
    bad = 0
    for rel, car, fld, want in SELF_TEST:
        p = base / rel
        got = "(carrier not found)"
        if p.exists():
            for name, _line, fields in carriers(p):
                if name == car:
                    got = classify_free(fld, fields)
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'MISS'} {car}.{fld}: {got}"
              + ("" if ok else f"  (expected {want})"))
    print(f"self-test: {len(SELF_TEST) - bad}/{len(SELF_TEST)} passing")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--show", type=int, default=12)
    ap.add_argument("--json", type=pathlib.Path)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any UNPINNED-EMPTY carrier exists")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    rows = []
    for p in sorted(REPO.glob("content/**/*.lean")):
        for name, line, fields in carriers(p):
            free = [f for f in fields if FREE_PROP.match(f"  {f[0]} : {f[1]}")]
            for fname, _ft, fline in free:
                rows.append({
                    "file": str(p.relative_to(REPO)), "carrier": name,
                    "carrier_line": line, "field": fname, "field_line": fline,
                    "verdict": classify_free(fname, fields),
                })

    by = {}
    for r in rows:
        by.setdefault(r["verdict"], []).append(r)
    tot = len(rows)
    print(f"free `: Prop` fields: {tot} in "
          f"{len({(r['file'], r['carrier']) for r in rows})} carrier(s), "
          f"{len({r['file'] for r in rows})} file(s)\n")
    for v in ("UNPINNED-EMPTY", "UNPINNED-FAKE-IF", "PINNED"):
        n = len(by.get(v, []))
        print(f"  {v:<18} {n:>4}  ({100*n/tot:.0f}%)" if tot else v)
    print("\nUNPINNED-* is a CANDIDATE: the field is free, so `True` satisfies it.")
    print("Confirm per carrier before recording a verdict.\n")

    if args.show:
        worst = {}
        for r in by.get("UNPINNED-EMPTY", []):
            worst.setdefault((r["file"], r["carrier"]), []).append(r["field"])
        for (f, c), flds in sorted(worst.items(), key=lambda x: -len(x[1]))[:args.show]:
            print(f"  {c:<40} {len(flds):>2} free  {f}")

    if args.json:
        args.json.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n")
        print(f"\nwrote {args.json}")

    if args.strict and by.get("UNPINNED-EMPTY"):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
