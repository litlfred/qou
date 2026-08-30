#!/usr/bin/env python3
"""The Phi_2 / Phi_3 derivations are IDENTITIES IN q, not anchor coincidences.

(bean qou-1jw9 — hardening phi_allpairs_reconstruction.py)

Both derivations were validated by matching carried values recorded at a SINGLE
anchor (q0 = 1.10998). 19/19 is strong, but a match at one q is not proof that
the algebra is right -- it could in principle be a numerical accident there.
This checks the per-pair contributions SYMBOLICALLY, so the question is settled
without reference to any anchor.

RESULT -- all three hold exactly, for symbolic q:

  1. All six Table-1 chirality ratios lam_sym/lam_alt are exact:
         pp, ee -> -q^2      nn, pe -> -q^-2      pn -> -1      ne -> +1
     so Phi_3's quantisation in ln q is an IDENTITY.

  2. det T is +-1 for every crossing EXCEPT pn, where
         det_pn = -(q^2+1)^2 / (4q^2)   and   |det_pn| = 1 + h^2/4 exactly,
     so Phi_2 = Z*N*ln(1 + h^2/4) is an IDENTITY.

     And it has a cleaner form in the repo's own notation: (q^2+1)/q = [2]_q,
     so |det_pn| = ([2]_q/2)^2 and

         Phi_2 = 2 * Z * N * ln( [2]_q / 2 ).

  3. The counting identity 2[2C(Z,2) - C(N,2) - Z^2] = -2Z - N(N-1) holds for
     all Z, N.

So neither result depends on the anchor, and neither depends on the convention
(no z appears in either). Both survive the q0 pin and the C->D excision
unchanged -- which is what makes "the excision's blast radius is exactly one
invariant" a statement about the algebra rather than about one evaluation.

Symbolic throughout: sympy exact rationals, no floating point anywhere, so the
NO-FLOAT64 discipline is satisfied by construction rather than by care.
"""
from __future__ import annotations

import sympy as sp

q = sp.symbols('q', positive=True)
h = q - 1 / q

# Table 1, with the pn coefficient in the UN-DOUBLED form (1, -h/2) that Phi_2
# discriminates in favour of (phi2_pn_coefficient_probe.py).
TBL = {"pp": (1, sp.Integer(0)), "nn": (1, -h), "pn": (1, -h / 2),
       "pe": (1, -h),            "ne": (0, sp.Integer(1)), "ee": (1, sp.Integer(0))}

CLAIMED_RATIO = {"pp": -q**2, "ee": -q**2, "nn": -1 / q**2, "pe": -1 / q**2,
                 "pn": sp.Integer(-1), "ne": sp.Integer(1)}


def main() -> int:
    print("=" * 78)
    print("PHI_3 -- per-pair chirality ratio lam_sym/lam_alt, symbolically in q")
    print("=" * 78)
    print(f"{'pair':>5} {'lam_sym':>20} {'lam_alt':>20} {'ratio':>14} {'claim':>8}")
    print("-" * 72)
    allok = True
    for k, (c, d) in TBL.items():
        ls = sp.simplify(c * q + d)
        la = sp.simplify(-sp.Rational(c, 1) / q + d)
        r = sp.simplify(ls / la)
        ok = sp.simplify(r - CLAIMED_RATIO[k]) == 0
        allok &= ok
        print(f"{k:>5} {str(ls):>20} {str(la):>20} {str(r):>14} "
              f"{'OK' if ok else 'MISMATCH':>8}")
    print(f"\n  all six ratios exact in q: {allok}")
    print("  => Phi_3's quantisation in ln q is an IDENTITY, not an anchor accident.")

    print("\n" + "=" * 78)
    print("PHI_2 -- per-pair det T, symbolically")
    print("=" * 78)
    for k, (c, d) in TBL.items():
        det = sp.simplify((c * h + d) * d - sp.Integer(c) ** 2)
        print(f"{k:>5}  det T = {sp.factor(det)}")
    det_pn = sp.simplify((1 * h - h / 2) * (-h / 2) - 1)
    same = sp.simplify(-det_pn - (1 + h**2 / 4)) == 0
    print(f"\n  only pn differs from +-1:  det_pn = {sp.factor(det_pn)}")
    print(f"  |det_pn| == 1 + h^2/4 exactly: {same}")
    two_q = q + 1 / q
    cleaner = sp.simplify(-det_pn - (two_q / 2) ** 2) == 0
    print(f"  and |det_pn| == ([2]_q / 2)^2 exactly: {cleaner}")
    print("  => Phi_2 = Z*N*ln(1 + h^2/4) = 2*Z*N*ln([2]_q/2), an IDENTITY in q.")

    print("\n" + "=" * 78)
    print("PHI_3 -- the counting identity")
    print("=" * 78)
    Z, N = sp.symbols('Z N', integer=True, nonnegative=True)
    lhs = 2 * (2 * sp.binomial(Z, 2) - sp.binomial(N, 2) - Z**2)
    rhs = -2 * Z - N * (N - 1)
    diff = sp.simplify(sp.expand_func(lhs) - rhs)
    print(f"  2[2C(Z,2) - C(N,2) - Z^2] - (-2Z - N(N-1)) = {diff}")
    print(f"  holds for all Z, N: {diff == 0}")

    ok = allok and same and cleaner and diff == 0
    print(f"\n  ALL THREE IDENTITIES VERIFIED: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
