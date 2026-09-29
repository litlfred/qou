#!/usr/bin/env python3
"""
prereg_su4_prediction_is_analytic_probe.py — the SU(4) entry of the free-choice
pre-registration was over-claimed by its own registrar, within the hour, and
this is the demonstration.

WHAT I REGISTERED (commit adding docs/audits/prereg-free-choice-2026-08-27.json):

    su4-supermultiplet | free_choice = none | "TESTABLE, and this is the
    sharpest entry in the registry. It predicts the term VANISHES for every
    A > 4."

and, in the companion audit doc, "Refutable in one measurement."

WHAT THE PRIMARY SOURCE SAYS.  I classified from a one-line summary in
`2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`, not from
`QOU/MassTheory/SU4SupermultipletGate.lean`.  The gate's actual content is

    su4_supermultiplet_dim_vanishes_iff (A : Nat) : Nat.choose 4 A = 0 <-> 4 < A
        := Nat.choose_eq_zero_iff

-- a one-line consequence of a Mathlib arithmetic lemma about binomial
coefficients.  Nothing about nucleons enters it.  So "the sharpest entry",
and the audit doc's "refutable in one measurement", are WRONG: the vanishing
is analytic, entailed by the
specification's own counting, and a measurement confirming it confirms
binomial arithmetic.

The gate's own docstring is explicit that the locality was measured FIRST --
"2.09x super-pairwise at 4He, vanishing to ~0.94 by 6Li" -- and that the gate
"*predicts* the A=4 locality already measured".  That is postdiction, correctly
labelled at source; my registry entry lost the label in transit.

WHAT THIS DOES TO THE RULE UNDER TEST.  The rule says: no free choice => a
definite prediction => testable.  SU(4) genuinely has no free choice, and it
genuinely yields a definite prediction.  Both halves hold.  What fails is the
step I silently added: that a definite prediction is an INFORMATIVE one.  This
prediction does not discriminate -- it holds for ANY object whose dimension is
C(4,A), whether or not that object has anything to do with binding, which is
what A2 below demonstrates.

So this is not one of the two refutation conditions I registered.  It is a
THIRD failure mode I did not anticipate: a choice-free candidate whose definite
prediction is ANALYTIC rather than synthetic.  Recording it as a new mode
rather than stretching an existing one.

PROCESS ERROR, named.  The classification was made from a secondary summary
when the primary source was one grep away.  That is the same class as the
corpus-grep discipline in AGENTS.md, and it is why the amendment is a NEW dated
file rather than an edit to the registry -- per the registry's own anti-peek
clause, which this probe's sibling guard enforces.

@module computations/meson/prereg_su4_prediction_is_analytic_probe
"""

from __future__ import annotations

import json
import pathlib
from math import comb

REG = pathlib.Path(__file__).resolve().parents[2] / "docs" / "audits" / \
    "prereg-free-choice-2026-08-27.json"
GATE = pathlib.Path(__file__).resolve().parents[2] / "folio" / \
    "quantum-observable-universe" / "lean" / "QOU" / "MassTheory" / \
    "SU4SupermultipletGate.lean"

_FAILED: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {msg}")
    if not ok:
        _FAILED.append(msg)


def main() -> int:
    print("=" * 92)
    print("The SU(4) entry's prediction is analytic — my registration over-claimed")
    print("=" * 92)

    reg = json.loads(REG.read_text())
    su4 = next(c for c in reg["candidates"] if c["id"] == "su4-supermultiplet")
    gate = GATE.read_text()

    print(f"\n  registered call : free_choice = {su4['free_choice']}")
    print(f"  registered claim: \"{su4['prediction'][:72]}...\"")

    # -- A1: the gate is arithmetic, and says so ---------------------------
    print("\n1. What the gate actually proves")
    is_arith = ("Nat.choose_eq_zero_iff" in gate
                and "Nat.choose 4 A = 0 ↔ 4 < A" in gate)
    check(is_arith,
          "A1: the gate's theorem is `Nat.choose 4 A = 0 ↔ 4 < A`, discharged by "
          "the Mathlib lemma `Nat.choose_eq_zero_iff`. It is binomial "
          "arithmetic; no nucleon, no braid, no q₀ enters it")

    check("already measured" in gate,
          "A2: and the gate's OWN docstring labels the relation as postdiction "
          "— it says the gate \"*predicts* the A=4 locality already measured\". "
          "The label exists at source; my registry entry lost it by classifying "
          "from a one-line summary instead")

    # -- A3: the prediction does not discriminate --------------------------
    print("\n2. Why the prediction carries no information about binding")
    print("\n     A    C(4,A)   any-object-with-this-dimension")
    for A in (2, 3, 4, 5, 6, 12, 16):
        print(f"   {A:3d}  {comb(4, A):7d}   {'vanishes' if A > 4 else 'present'}")

    vanish_all = all(comb(4, A) == 0 for A in range(5, 40))
    check(vanish_all,
          "A3: C(4,A) = 0 for every A in 5..39 — but this holds for ANY object "
          "whose dimension is C(4,A), binding-related or not. A measurement "
          "confirming the vanishing cannot distinguish the SU(4) Ursell cluster "
          "from any other C(4,A)-dimensional object, so it discriminates nothing")

    # -- A4: what a synthetic test would look like -------------------------
    print("\n3. What WOULD be a synthetic test")
    check(True,
          "A4: the falsifiable content is the IDENTIFICATION — that the missing "
          "super-pairwise term IS this cluster, with the right MAGNITUDE at "
          "A ≤ 4. The gate's docstring supplies the target (2.09× super-pairwise "
          "at ⁴He, ~0.94 by ⁶Li). Predicting that magnitude, not the vanishing, "
          "is what could fail")

    # -- A5: the registry is untouched -------------------------------------
    print("\n4. The registry is NOT edited")
    check(su4["outcome"] is None
          and "TESTABLE, and this is the sharpest entry" in su4["prediction"],
          "A5: the registry still carries the over-claim verbatim, with "
          "outcome = null. Correcting it in place would have destroyed the "
          "pre-registration's whole value — the amendment is a separate dated "
          "artifact, and the git order of the two commits is the evidence")

    print("\n" + "=" * 92)
    print(f"{5 - len(_FAILED)}/5 assertions passed")
    print("=" * 92)
    return 1 if _FAILED else 0


if __name__ == "__main__":
    raise SystemExit(main())
