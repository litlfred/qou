#!/usr/bin/env python3
"""M4 — is the Wigner SU(4) `[1^n]` supermultiplet sign-capable at 3-body?

WHY THIS TEST AND NOT ANOTHER.  Two assemblies in the corpus are now *proved*
incapable of the measured connected three-body cumulant, and between them they
cover everything the framework currently uses:

  * multiplicative / Mayer `W = 1 - prod f`  =>  b3 > 0 needs f_pn > 2/3, and
    every measured bond factor is below it
    (`QOU.MassTheory.MayerThreeBodySign.lt_of_b3_pos`, sorry-free);
  * pairwise-additive `B = sum_bonds f(mu)`  =>  b3 = 0 identically, for EVERY
    bond functional f, the s10a Cauchy-forced logarithm included
    (`QOU.Mass.PairwiseCumulantVanishing.b3_eq_zero_ofBondFunctional`,
    sorry-free, this branch).

The `gap2_he4_borromean_mu_bar` exclusion (Milnor mu-bar indeterminacy on a
max-contact cluster) leaves exactly one named candidate standing for the
super-pairwise content: the **non-link-invariant** Wigner SU(4) `[1^n]`
supermultiplet antisymmetriser, whose dimension is `C(4, n)` and which vanishes
for `n > 4` (`QOU.MassTheory.SU4SupermultipletGate`, sorry-free).

So the first question to ask of it is not "does it hit 9.24 MeV" but the one
that killed its two predecessors: **can it produce a positive b3 at all, and
with what per-order energies?**  This unit asks only that.

WHAT IS COMPUTED.  The AME2020 Ursell inversion (a body-order *definition* of a
binding map, not a fit), then the ratios a zero-parameter SU(4)-dimension
weighting predicts, then the per-order energies the measurement actually
requires under that weighting.

  B(A) = C(A,2) b2 + C(A,3) b3 + C(A,4) b4
  b2 = B(D);  b3 = Bbar(3) - 3 b2;  b4 = B(4He) - 6 b2 - 4 b3

DISCIPLINE.  mpmath end to end at 60 dps; `float()` appears nowhere; AME values
come from the canonical `ame_2020_binding_energies` table, not from literals.
Nothing here is wired, nothing is fitted, and the required-energy column is a
DIAGNOSTIC (reading it off the anchors would be the anchor inversion the
Delta_lambda gate forbids).  Beans qou-u8mu; parent qou-m2ay.
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
    """AME2020 binding in MeV, carried as mpf from the canonical exact table."""
    return mp.mpf(str(ame._binding_mev_exact(Z, A)))


def main() -> int:
    B_D = _B(1, 2)
    B_T = _B(1, 3)
    B_He3 = _B(2, 3)
    B_He4 = _B(2, 4)
    B_3 = (B_T + B_He3) / 2  # isospin average, as the corpus inversion uses

    b2 = B_D
    b3 = B_3 - 3 * b2
    b4 = B_He4 - 6 * b2 - 4 * b3

    print("== AME2020 Ursell cumulants (MeV) ==")
    for name, v in (("b2", b2), ("b3", b3), ("b4", b4)):
        print(f"  {name} = {mp.nstr(v, 12)}")
    closure = 6 * b2 + 4 * b3 + b4
    print(f"  closure check 6b2+4b3+b4 = {mp.nstr(closure, 15)}"
          f"  vs B(4He) = {mp.nstr(B_He4, 15)}")
    assert abs(closure - B_He4) < mp.mpf("1e-40"), "inversion is not an identity"

    print()
    print("== SU(4) supermultiplet dimensions dim[1^n] = C(4,n) ==")
    dims = {n: comb(4, n) for n in range(1, 6)}
    for n, d in dims.items():
        print(f"  n={n}: C(4,n) = {d}")
    print("  (vanishes for n>4 — the A=4 locality, SU4SupermultipletGate)")

    print()
    print("== LEG 1 — SIGN CAPABILITY (the question that killed both assemblies) ==")
    # Under B = sum_n e_n * C(A,n) * dim[1^n] with a COMMON POSITIVE e, every
    # connected cumulant inherits the sign of dim[1^n] = C(4,n) > 0 for n<=4.
    all_pos = all(dims[n] > 0 for n in (2, 3, 4))
    print(f"  dim[1^n] > 0 for n = 2,3,4 : {all_pos}")
    print(f"  measured sign of b3        : {'+' if b3 > 0 else '-'}")
    print("  The SU(4) weighting is SIGN-CAPABLE at 3-body.")
    print()
    print("  🛑 CORRECTED — read this before quoting the line above.")
    print("  Sign-capability here is ANALYTIC: it is `C(4,n) > 0` for n<=4,")
    print("  binomial arithmetic, and it holds for ANY object with positive")
    print("  per-order weights whether or not it has anything to do with")
    print("  binding. So it DISCRIMINATES NOTHING, and calling SU(4) 'the")
    print("  first sign-capable candidate' overstates it — every")
    print("  positive-weight assembly is sign-capable.")
    print()
    print("  What is NOT shared, and is the real reason SU(4) is the named")
    print("  survivor, is structural rather than numerical: it is a")
    print("  NON-LINK-INVARIANT, non-pairwise object, so the Milnor mu-bar")
    print("  indeterminacy exclusion (gap2_he4_borromean_mu_bar) does not")
    print("  reach it, and the pairwise-additivity theorem")
    print("  (PairwiseCumulantVanishing) does not either. Cite the")
    print("  exclusions it survives, never its positivity.")
    print()
    print("  This is the failure mode bean qou-04ub AMENDMENT 1 records")
    print("  against the SAME object one step over: a choice-free candidate")
    print("  whose definite prediction is ANALYTIC rather than synthetic.")
    print("  Their question is the one to ask of any such claim — could the")
    print("  prediction have come out otherwise, given the specification?")
    print("  For positivity of C(4,n): no. See")
    print("  computations/meson/prereg_su4_prediction_is_analytic_probe.py")

    print()
    print("== LEG 2 — ZERO-PARAMETER RATIO TEST (one common scale, no fit) ==")
    # If b_n = e * dim[1^n] with a single common e, the ratios are forced.
    pred_32 = mp.mpf(dims[3]) / mp.mpf(dims[2])
    pred_42 = mp.mpf(dims[4]) / mp.mpf(dims[2])
    meas_32 = b3 / b2
    meas_42 = b4 / b2
    err_32 = (meas_32 - pred_32) / pred_32 * 100
    err_42 = (meas_42 - pred_42) / pred_42 * 100
    print(f"  b3/b2  predicted C(4,3)/C(4,2) = {mp.nstr(pred_32, 12)}"
          f"   measured {mp.nstr(meas_32, 12)}   err {mp.nstr(err_32, 6)} %")
    print(f"  b4/b2  predicted C(4,4)/C(4,2) = {mp.nstr(pred_42, 12)}"
          f"   measured {mp.nstr(meas_42, 12)}   err {mp.nstr(err_42, 6)} %")
    print("  READING: 3-body lands within a few percent of the forced 2/3 with")
    print("  ZERO parameters; 4-body misses by more than an order of magnitude.")
    print("  NEAR-MATCH TIER for the 3-body ratio, NOT derived and NOT wired.")
    print("  A single common scale is REFUTED by the b4 row — scope (a).")

    print()
    print("== LEG 3 — GENERICITY CONTROL (is the 2/3 agreement cheap?) ==")
    # NORMALISATION: the miss in LEG 2 is normalised by the PREDICTION, so the
    # window must be too, or the control answers a different question than the
    # one the number came from. (Getting this backwards is the normalisation
    # trap AGENTS.md records for the c_3 3.47 % / 3.35 % pair.)
    tol = abs(err_32) / 100
    print(f"  relative tolerance set by the measured miss : {mp.nstr(tol, 6)}")
    print("  (normalised by the CANDIDATE, matching LEG 2)")
    # Dedupe by VALUE in lowest terms: 4/6 and 6/9 are the same number as 2/3,
    # and counting them separately inflates the window several-fold.
    from fractions import Fraction
    for qmax in (4, 6, 9, 12):
        window = sorted({Fraction(p, q) for q in range(1, qmax + 1)
                         for p in range(1, 4 * q)
                         if abs(mp.mpf(p) / q - meas_32) / (mp.mpf(p) / q) <= tol
                         and Fraction(p, q).denominator <= qmax})
        vals = [f"{f.numerator}/{f.denominator}" for f in window]
        print(f"  q <= {qmax:2d}: {len(window):2d} distinct values inside -> {vals}")
    print("  READING: 2/3 is alone only at q <= 6; at q <= 9 it is joined by 5/8")
    print("  and at q <= 12 by 7/11. So the 3.83 % agreement discriminates WEAKLY")
    print("  — it is not a coincidence-free identification, and it must not be")
    print("  reported as one. What survives LEG 2 is the SIGN result of LEG 1,")
    print("  which is structural; the 3.83 % is near-match tier at best.")

    print()
    print("== LEG 4 — REQUIRED PER-ORDER ENERGIES (DIAGNOSTIC, NOT A DERIVATION) ==")
    print("  Reading these off the anchors and wiring them would be the anchor")
    print("  inversion the Delta_lambda gate forbids. They are printed so the")
    print("  keystone has a falsifiable target, exactly as qou-i5yp is stated.")
    for n, bn in ((2, b2), (3, b3), (4, b4)):
        e_n = bn / mp.mpf(dims[n])
        print(f"  e_{n} = b{n}/C(4,{n}) = {mp.nstr(e_n, 12)} MeV")
    e2 = b2 / dims[2]
    print(f"  ratios e2:e3:e4 = 1 : {mp.nstr((b3 / dims[3]) / e2, 8)}"
          f" : {mp.nstr((b4 / dims[4]) / e2, 8)}")
    print("  Compare the multiplicative model's required a2:a3:a4 =")
    print("  1 : -0.519787 : +4.45038 (qou-i5yp). The SU(4) weighting removes")
    print("  the SIGN ALTERNATION — its required ratios are all positive — and")
    print("  keeps a large 4-body enhancement. The sign alternation was the part")
    print("  no Gauss-Manin recurrence was expected to supply.")

    print()
    print("== VERDICT ==")
    print("  scope-(a) throughout. Established: a single common scale for the")
    print("  SU(4) weighting is REFUTED by the 4-body row, and the b3/b2 ratio")
    print("  agreement discriminates weakly. NOT established: any closure, any")
    print("  value, any derivation of the per-order energies -- and NOT that")
    print("  SU(4) is distinguished by sign-capability, which is analytic and")
    print("  shared by every positive-weight assembly (LEG 1 correction).")
    print("  The magnitude gate is OPEN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
