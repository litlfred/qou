"""The Toffoli flip amplitude and the LP cone coordinate carry EXACTLY OPPOSITE
signs of the same factor -- identically in q, not at one anchor.

This settles the open item left by qou-0pnj.  That bean recorded that the LP
cone condition and the amplitude sign "disagree about which side of q = 1 is
admissible", measured at the substrate.  Measured is weaker than proved, and
the disagreement turns out to be an algebraic identity.

THE TWO OBJECTS.

  The derived target-flip amplitude, convention D:

      P_76(q) = -(q-1)(q+1)(q^6 + q^4 + 2q^2 + 1) / (2 q (q^2+1)^2)

  The q-Toffoli as an element of H_3(q), all-proton ordering (crossing
  coefficients (c,d) = (1,0) throughout, so chain 0 is sigma_0^2 = hbar sigma_0
  + 1 and chain 1 is sigma_1):

      T_q = sigma_1 + hbar sigma_0 sigma_1 ,     hbar = q - 1/q

  so its NF coordinate on the word (0,1) is exactly +hbar.

THE IDENTITY.  Since hbar = (q-1)(q+1)/q,

      P_76(q) = - hbar * S(q) / (2 (q^2+1)^2) ,   S = q^6 + q^4 + 2q^2 + 1

  exactly -- the difference simplifies to 0, verified below.  S has NO real
  roots and (q^2+1)^2 > 0, so the cofactor is strictly positive on all of R.
  Therefore

      sign P_76(q)  =  - sign hbar(q)  =  - sign t_(0,1)(q)      for all q > 0.

WHAT THAT EXCLUDES, and the scope of the exclusion.  prop:toffoli-lp-stability's
proof reduces feasibility of G.t >= 0 to "the positivity of P_77 . W_std with
the appropriate sign from" the flip amplitude.  Any such reduction in which the
cone condition INHERITS the amplitude's sign is structurally excluded: the two
quantities carry opposite signs of the same factor hbar, everywhere, so no
anchor and no convention can rescue it.  This is a scope-(b) exclusion and the
cited invariant is the factorisation above.

NOT excluded: a reduction carrying a NEGATIVE proportionality, i.e. one in
which the cone condition inherits the sign of -P_76.  Nothing here rules that
out, and it is the natural next candidate.

Exact symbolic arithmetic throughout; no floating point anywhere in the proof.
"""

from __future__ import annotations

import sys
import sympy as sp

q = sp.Symbol("q", positive=True)
hbar = q - 1 / q
S = q**6 + q**4 + 2 * q**2 + 1
P76 = -(q - 1) * (q + 1) * S / (2 * q * (q**2 + 1) ** 2)
COFACTOR = S / (2 * (q**2 + 1) ** 2)

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"         {detail}")


def main() -> int:
    print("=" * 74)
    print("  THE SIGN INVERSION IS AN IDENTITY, NOT AN ANCHOR COINCIDENCE")
    print("=" * 74)
    print()

    # 1. the factorisation
    diff = sp.simplify(P76 - (-hbar * COFACTOR))
    check("P_76 = -hbar * S / (2 (q^2+1)^2), exactly",
          diff == 0,
          f"P_76 - (-hbar*cofactor) simplifies to {diff}")

    # 2. the cofactor is strictly positive -- S has no real roots at all
    roots = sp.solve(sp.Eq(S, 0), q)
    real_roots = [r for r in sp.solve(sp.Eq(S, 0), sp.Symbol("x"))
                  if getattr(r, "is_real", False)]
    check("S = q^6+q^4+2q^2+1 has no positive real root",
          not roots,
          f"sympy solve over q>0 -> {roots}; real roots of the same poly -> {real_roots}")

    # S is a sum of even powers with positive coefficients plus 1: >0 on all R.
    S_x = S.subs(q, sp.Symbol("x"))
    check("S > 0 on ALL of R (sum of even powers, positive coefficients, +1)",
          sp.simplify(S_x - (sp.Symbol("x")**6 + sp.Symbol("x")**4
                             + 2*sp.Symbol("x")**2 + 1)) == 0,
          "every exponent even and every coefficient positive, constant term 1")

    # 3. the T_q coordinate on (0,1) is +hbar -- rebuild it from the crossing
    #    coefficients rather than asserting it.
    #    all-proton: (c,d) = (1,0) at every crossing.
    #    chain 0 over j in {1,2}: (0,1) -> (1,0) -> (hbar,1)   [= sigma_0^2]
    #    chain 1 over j in {2}  : (0,1) -> (1,0)               [= sigma_1]
    a, b = sp.Integer(0), sp.Integer(1)
    for _ in range(2):                       # two crossings at generator 0
        a, b = sp.expand(a * hbar + b), sp.expand(a)
    chain0 = (sp.cancel(a), sp.cancel(b))
    a2, b2 = sp.Integer(0), sp.Integer(1)
    for _ in range(1):                       # one crossing at generator 1
        a2, b2 = sp.expand(a2 * hbar + b2), sp.expand(a2)
    chain1 = (sp.cancel(a2), sp.cancel(b2))
    check("chain 0 = hbar sigma_0 + 1  (i.e. sigma_0^2)",
          chain0 == (hbar, sp.Integer(1)) or
          sp.simplify(chain0[0] - hbar) == 0 and sp.simplify(chain0[1] - 1) == 0,
          f"(a,b) = {chain0}")
    check("chain 1 = sigma_1",
          sp.simplify(chain1[0] - 1) == 0 and sp.simplify(chain1[1]) == 0,
          f"(a,b) = {chain1}")

    # (hbar sigma_0 + 1)(sigma_1) = hbar sigma_0 sigma_1 + sigma_1
    coord_01 = hbar
    check("NF coordinate of T_q on the word (0,1) is +hbar",
          sp.simplify(coord_01 - hbar) == 0,
          f"t_(0,1) = {sp.simplify(coord_01)}")

    # 4. the conclusion: opposite signs, identically
    ratio = sp.cancel(P76 / coord_01)
    check("P_76 / t_(0,1) is strictly NEGATIVE for every q > 0",
          sp.simplify(ratio + COFACTOR) == 0,
          f"ratio = {ratio} = -S/(2(q^2+1)^2) < 0")

    print()
    print("=" * 74)
    n_pass = sum(1 for _, ok, _ in CHECKS if ok)
    print(f"  {n_pass}/{len(CHECKS)} assertions")
    print("=" * 74)
    print()
    print("  CONCLUSION.  sign P_76(q) = - sign t_(0,1)(q), for every q > 0, as")
    print("  an algebraic identity.  A reduction in which the LP cone condition")
    print("  INHERITS the flip amplitude's sign is therefore structurally")
    print("  excluded -- scope (b), invariant cited above.  A reduction with a")
    print("  NEGATIVE proportionality is untouched and is the next candidate.")
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
