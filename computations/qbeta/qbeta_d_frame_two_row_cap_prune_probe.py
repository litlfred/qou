#!/usr/bin/env python3
"""Does the convention-D two-row cap supply the Q_β correction? No — by 13.6×.

BEAN `qou-cds1`. That bean's "Remaining piece" names exactly one input that had
landed but was never folded in:

    "The two-row cap. WenzlWeightVanishing.lean landed 2026-08-16 (sorry-free,
     all n; z_D is Wenzl level r=2 exactly) ... Under D the >=3-row blocks are
     annihilated, so chi_(1,1,1) drops from the H_3 decomposition. NOT folded
     in yet."

This probe folds it in, in the F coordinate the bean recommends
(`work in F, not alpha`), and the answer is a scope-(a) NEGATIVE.

WHAT IS BEING ASKED. The ladder needs a multiplicative correction

    F(q) := Q_beta(q) / Q_A(q),   with  1 - F(q0) = 1.6748e-3  (the target),

where Q_A = m_e*|q^2-2q-1|*(q+1)/(2q^3) carries NO z and NO trace, so the whole
convention dependence sits in the one factor cos(alpha - u/2), alpha=(z-1)h/2.

The structural candidate: D provably annihilates every partition with >= 3 rows,
so at n=3 the block (1,1,1) drops from the H_3 decomposition that C retains. If
the correction were "the part of the trace that D discards", it would equal the
C-frame weight of that block.

MEASURED (both anchors):

  * dim * y_(1,1,1) in convention C  =  0.0227449...   =  13.6x the target.
  * Both traces are SEPARATELY NORMALISED: sum_lambda dim_lambda * y_lambda = 1
    holds in C (three blocks) AND in D (two blocks). Each is a complete
    normalised trace on its own support.

So the cap does not leave a residue that could BE the correction: it is not a
1.7e-3 effect, it is a 2.3e-2 effect, and it is already absorbed by
renormalisation on each side. This prunes the class "F = the two-row
restriction fraction of the n=3 trace" WITHOUT running any search over it,
which is what the bean's Discipline section asks for.

SCOPE (a) — this is a scope-limited negative in the sense of AGENTS.md
"Before declaring refuted": it says THIS construction, alone, does not supply
the correction at the measured magnitude. It does NOT exclude the two-row cap
as an ingredient of some multi-term closure, and it proves no invariant that
would forbid one. Nothing here derives F; the re-derivation stays open.

Anchor: experimental (proton) pin per the 2026-08-07 owner directive; the muon
pin is carried alongside only as a cross-anchor stability check.
"""
from __future__ import annotations

import pathlib
import sys

import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations"))

import schur_principal_mpmath as S  # noqa: E402

mp.mp.dps = 50

# Substrate anchors (proton = experimental pin; muon = ideal CAL-2 pin).
ANCHORS = {
    "proton": mp.mpf("1.10997858275138080759166909561076887987449912187357873607281"),
    "muon": mp.mpf("1.10997859555418057528159407960950937799328227995868622546675"),
}
M_E = mp.mpf("0.51099895069")
Q_CODATA = mp.mpf("0.78233341")
DIM3 = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}


def q_a(q: mp.mpf) -> mp.mpf:
    """Q_A = m_e*|q^2-2q-1|*(q+1)/(2q^3) — no z, no trace."""
    return M_E * abs(q**2 - 2 * q - 1) * (q + 1) / (2 * q**3)


def main() -> int:
    ok = True
    for name, q in ANCHORS.items():
        target = 1 - Q_CODATA / q_a(q)
        yc = S.y_lambda_at_q0_mpmath_convention_C_HISTORICAL(3, q)
        yd = S.y_lambda_at_q0_mpmath(3, q)

        norm_c = sum(DIM3[l] * yc.get(l, mp.mpf(0)) for l in DIM3)
        norm_d = sum(DIM3[l] * yd.get(l, mp.mpf(0)) for l in DIM3)
        dropped = DIM3[(1, 1, 1)] * yc.get((1, 1, 1), mp.mpf(0))

        print(f"=== anchor: {name}   q0 = {mp.nstr(q, 14)}")
        print(f"  target  1 - F_required            = {mp.nstr(target, 12)}")
        print(f"  C weights: {[mp.nstr(yc.get(l, 0), 10) for l in DIM3]}")
        print(f"  D weights: {[mp.nstr(yd.get(l, 0), 10) for l in DIM3]}")
        print(f"  sum dim*y  (C) = {mp.nstr(norm_c, 12)}   (D) = {mp.nstr(norm_d, 12)}")
        print(f"  block D removes: dim*y_(1,1,1)|_C = {mp.nstr(dropped, 12)}")
        print(f"  ratio dropped/target              = {mp.nstr(dropped / target, 8)}")
        print()

        # Assertions: both traces normalised; the cap is an order too big.
        ok &= abs(norm_c - 1) < mp.mpf("1e-40")
        ok &= abs(norm_d - 1) < mp.mpf("1e-40")
        # D annihilates >=3 rows. Compared against a tolerance, not to exact 0:
        # the weights are built by mpmath arithmetic, so the vanishing block
        # lands on numerical zero (-2.6e-52 at the muon anchor), not on 0.0.
        # The Lean statement (conventionD_weight_eq_zero_iff_rowLens) is the
        # exact one; this is its floating-point shadow.
        ok &= abs(yd.get((1, 1, 1), mp.mpf(0))) < mp.mpf("1e-40")
        ok &= dropped / target > 10                       # not a 1.7e-3 effect

    print("VERDICT: the two-row cap does NOT supply the Q_beta correction.")
    print("  It is ~13.6x the required size, and both traces are separately")
    print("  normalised, so the cap leaves no residue to be the correction.")
    print("  Scope-(a): this construction alone; no invariant excludes the cap")
    print("  as one ingredient of a multi-term closure.")
    print()
    print("ASSERTIONS PASS" if ok else "ASSERTIONS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
