#!/usr/bin/env python3
"""M6 — the A>=5 tower blow-up is a MULTIPLICITY failure, not only a period-growth one.

WHAT THE CORPUS CURRENTLY SAYS, AND WHY IT MISLEADS.
`binding_wn_multianchor_tower_refute.py` records the full-tower refutation
(6Li ~ +920 %, 7Li ~ +3000 %, 9Be ~ +3e4 %, 12C ~ +2e6 %) and gives this
structural reason, verbatim from its docstring:

    "Structural reason (precision-independent): a_D^(n) grows super-exponentially
     [vs] B/A -> const."

That reason is TRUE and it is NOT THE WHOLE CAUSE. A reader takes from it that
taming the period growth would tame the blow-up. This unit measures that
counterfactual directly and finds it false.

THE COUNTERFACTUAL. Replace the super-exponentially growing per-order energies
with the AME2020 Ursell cumulants themselves -- b2 = 2.2246, b3 = 1.4262,
b4 = 9.2434 MeV. These are BOUNDED, they do not grow at all beyond n = 4, and
they are by construction exactly right at A <= 4 (the inversion is an identity
there, asserted below). They are the most favourable per-order energies the
body-order tower can possibly have.

The tower still blows up. So super-exponential a_D^(n) is SUFFICIENT for the
A>=5 failure but NOT NECESSARY: the C(A,n) all-subsets multiplicities do it on
their own.

WHY THIS MATTERS BEYOND BOOKKEEPING. It ties the A>=5 failure to
`QOU.Mass.CoordinationSaturation.complete_graph_no_saturation` (sorry-free):
the complete graph's C(A,2) bonds per nucleus give an unbounded B/A, so no
finite plateau exists. That result is stated at 2-body. This unit shows the
same defect is already fatal with the 3- and 4-body orders included and with
every per-order energy pinned at its best possible value -- i.e. the
saturation obstruction is not a large-A asymptotic curiosity, it bites at A=6.

Consequence for the SU(4) [1^n] route (bean qou-u8mu): that route supplies
per-order ENERGIES (dim [1^n] = C(4,n)) and leaves the MULTIPLICITIES as
C(A,n). It therefore inherits this failure untouched. Any SU(4)-weighted
assembly must also replace the multiplicities with saturating (bounded-degree)
counts, or it fails at 6Li for a reason that has nothing to do with SU(4).

DISCIPLINE. mpmath end to end at 60 dps; no float() outside display; AME from
the canonical `ame_2020_binding_energies` table, not literals. No fit -- the
cumulants are an inversion of A <= 4 and are then used UNCHANGED at A >= 5, so
A >= 5 is held out. No witness, nothing wired. scope-(a) throughout: this
constrains the all-subsets multiplicity, and excludes no ingredient.
Beans qou-x5bv; parent qou-y2l3.
"""
from __future__ import annotations

import sys
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import mpmath as mp  # noqa: E402

import ame_2020_binding_energies as ame  # noqa: E402

mp.mp.dps = 60


def _B(Z: int, A: int) -> mp.mpf:
    return mp.mpf(str(ame._binding_mev_exact(Z, A)))


def main() -> int:
    # --- the cumulants, inverted from A <= 4 only -------------------------
    b2 = _B(1, 2)
    b3 = (_B(1, 3) + _B(2, 3)) / 2 - 3 * b2
    b4 = _B(2, 4) - 6 * b2 - 4 * b3

    print("== per-order energies: the AME Ursell cumulants (A <= 4 only) ==")
    for n, v in ((2, b2), (3, b3), (4, b4)):
        print(f"  b{n} = {mp.nstr(v, 12)} MeV")
    print("  BOUNDED -- no super-exponential growth anywhere in this column.")
    ratio_max = max(abs(b3 / b2), abs(b4 / b3))
    print(f"  largest successive ratio |b_(n+1)/b_n| = {mp.nstr(ratio_max, 8)}")

    # --- the identity at A <= 4 (an assertion, not a claim) ---------------
    closure = 6 * b2 + 4 * b3 + b4
    assert abs(closure - _B(2, 4)) < mp.mpf("1e-40"), "inversion is not an identity"
    print("  inversion is an identity at A=4 (asserted, < 1e-40)")

    # --- held out: A >= 5, energies unchanged -----------------------------
    print()
    print("== held-out A >= 5, SAME bounded energies, C(A,n) multiplicities ==")
    rows = [("4He", 2, 4), ("6Li", 3, 6), ("7Li", 3, 7), ("9Be", 4, 9)]
    worst = mp.mpf(0)
    for lab, Z, A in rows:
        tower = comb(A, 2) * b2 + comb(A, 3) * b3 + comb(A, 4) * b4
        meas = _B(Z, A)
        r = tower / meas
        held = "(anchor)" if A <= 4 else "HELD OUT"
        print(f"  {lab:5s} A={A}: tower {mp.nstr(tower, 8):>10s}  AME {mp.nstr(meas, 8):>9s}"
              f"  ratio {mp.nstr(r, 6):>8s}x  {held}")
        if A >= 5:
            worst = max(worst, r)

    print()
    print("== VERDICT ==")
    print("  The energies are bounded and optimal, and the tower still")
    print(f"  over-predicts by up to {mp.nstr(worst, 6)}x from A=6 on.")
    print("  So super-exponential a_D^(n) is SUFFICIENT for the A>=5 failure")
    print("  but NOT NECESSARY. The C(A,n) all-subsets multiplicity does it")
    print("  alone. binding_wn_multianchor_tower_refute's stated structural")
    print("  reason is true but incomplete, and taming the period growth")
    print("  would NOT fix 6Li.")
    print()
    print("  Ties to CoordinationSaturation.complete_graph_no_saturation")
    print("  (sorry-free): the complete graph cannot saturate. That is stated")
    print("  at 2-body; this shows it is already fatal at A=6 with the 3- and")
    print("  4-body orders included and every energy at its best value.")
    print()
    print("  scope-(a). No ingredient is excluded -- in particular the SU(4)")
    print("  [1^n] route is not refuted here. It is shown to INHERIT this")
    print("  failure, because it supplies energies and leaves multiplicities")
    print("  as C(A,n); it must also replace those to survive A >= 5.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
