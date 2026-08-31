#!/usr/bin/env python3
"""Is the corpus's DERIVED N=2 factor `1 - u^2` bar-invariant under convention D?

Bean `qou-cds1`.  Follow-up to PR #6282, and a CORRECTION to its Result 2.

#6282 argued: `c_2 = -1` is a rational constant, hence bar-weight 0; the forced
D-frame expansion variable `X = u*Vhat` requires `w(c_k) = 0`; therefore the
corpus's one derived rung is CONSISTENT with the forced form.

That argument assumes the derived value `-1` attaches to whatever the expansion
variable turns out to be.  AGENTS.md ties it to `u` SPECIFICALLY:

    "`1 - b^2*hbar^4 = 1 - (b*hbar^2)^2`, a one-line `ring` identity: it proves
     only that re-reading the N=2 factor in the ansatz form yields `-1`."

So the object the corpus derives is `1 - u^2`, in the variable `u`.  This file
asks the question #6282 skipped: is THAT object bar-invariant under D?

  NO CLAIM about convention C.  Under C the bar action is affine and weights are
  not its grading, so none of this applies there.

Exact sympy end to end; no float64; no mpf(str(<f64>)); emits no witness.
"""
import sys

import sympy as sp

q = sp.symbols("q", positive=True)


def bar(expr):
    """The bar involution q -> 1/q, as an exact rational-function map."""
    return sp.simplify(expr.subs(q, 1 / q))


def weight(expr):
    """Return w with bar(expr)/expr == q**w, or None if the ratio is not a power."""
    ratio = sp.simplify(bar(expr) / expr)
    for w in range(-12, 13):
        if sp.simplify(ratio - q**w) == 0:
            return w
    return None


def main() -> int:
    checks = []

    # --- the substrate quantities, exact -------------------------------------
    hbar_q = (q - 1) / q                       # hbar_q = 1 - 1/q
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)  # Hoefsmit b = sqrt([3]_{q^2})/[2]_q
    u = b * hbar_q**2
    h = q - 1 / q
    z_D = q**3 / (q**2 + 1)                    # convention D (canonical)
    Vhat_D = sp.simplify(z_D * h + 1)

    # 1. b is bar-invariant (so all of u's weight comes from hbar_q^2).
    checks.append(("b is bar-invariant", weight(b) == 0))

    # 2. hbar_q has weight 1 up to the sign: bar(hbar_q)/hbar_q = -q.
    checks.append(("bar(hbar_q)/hbar_q == -q",
                   sp.simplify(bar(hbar_q) / hbar_q + q) == 0))

    # 3. hence u has weight +2 (the sign squares away).
    checks.append(("w(u) == 2", weight(u) == 2))

    # 4. Vhat_D has weight -2, so u*Vhat_D is bar-invariant (PR #6244/#6282).
    checks.append(("w(Vhat_D) == -2", weight(Vhat_D) == -2))
    checks.append(("w(u*Vhat_D) == 0", weight(u * Vhat_D) == 0))

    # --- the actual question -------------------------------------------------
    # The corpus's DERIVED N=2 factor, in the variable it was derived in.
    N2_corpus = 1 - b**2 * hbar_q**4
    checks.append(("N2_corpus == 1 - u^2", sp.simplify(N2_corpus - (1 - u**2)) == 0))

    # 5. Is it bar-invariant?  bar(1 - u^2) = 1 - q^4 u^2.
    N2_defect = sp.simplify(bar(N2_corpus) - N2_corpus)
    checks.append(("N2_corpus is NOT bar-invariant", N2_defect != 0))
    checks.append(("the defect is exactly (1 - q^4)*u^2",
                   sp.simplify(N2_defect - (1 - q**4) * u**2) == 0))

    # 6. The factor written in the forced variable IS bar-invariant.
    N2_forced = 1 - (u * Vhat_D) ** 2
    checks.append(("1 - (u*Vhat_D)^2 IS bar-invariant",
                   sp.simplify(bar(N2_forced) - N2_forced) == 0))

    # 7. So the two are NOT the same object: they differ by Vhat_D^2.
    checks.append(("N2_forced != N2_corpus",
                   sp.simplify(N2_forced - N2_corpus) != 0))
    checks.append(("their u^2 coefficients differ by exactly Vhat_D^2",
                   sp.simplify(sp.expand(1 - N2_forced) / sp.expand(1 - N2_corpus)
                               - Vhat_D**2) == 0))

    # 8. Re-expressed in X = u*Vhat_D, the corpus's coefficient is NOT -1.
    #    1 - u^2 = 1 - X^2/Vhat_D^2, so c_2^{(X)} = -1/Vhat_D^2, of weight +4.
    c2_in_X = -1 / Vhat_D**2
    checks.append(("c_2 in the X variable is -1/Vhat_D^2, weight +4",
                   weight(c2_in_X) == 4))
    checks.append(("weight +4 != the weight 0 the forced form requires",
                   weight(c2_in_X) != 0))

    # --- report --------------------------------------------------------------
    print("q-symbolic, exact.  Convention D (canonical).\n")
    print(f"  hbar_q  = {hbar_q}")
    print(f"  u       = b*hbar_q^2,   w(u) = {weight(u)}")
    print(f"  Vhat_D  = {sp.simplify(Vhat_D)},   w = {weight(Vhat_D)}")
    print(f"  w(u*Vhat_D) = {weight(u * Vhat_D)}\n")

    print("The corpus's DERIVED N=2 factor, in its own variable:")
    print(f"  1 - b^2*hbar_q^4  =  1 - u^2")
    print(f"  bar(.) - (.)      =  (1 - q^4)*u^2   != 0   -> NOT bar-invariant\n")

    print("Re-expressed in the forced variable X = u*Vhat_D:")
    print(f"  1 - u^2  =  1 - X^2/Vhat_D^2   ->   c_2^(X) = -1/Vhat_D^2, weight +4")
    print(f"  the forced form requires weight 0   ->   INCONSISTENT\n")

    # numeric size of the discrepancy at the proton pin, for scale only
    from qou_substrate.constants import q_at
    import mpmath as mpm
    mpm.mp.dps = 40
    q0 = q_at(40)
    Vhat_val = sp.N(Vhat_D.subs(q, sp.Float(str(q0), 40)), 30)
    print(f"At the proton pin q0 = {mpm.nstr(q0, 15)}:")
    print(f"  Vhat_D    = {Vhat_val}")
    print(f"  Vhat_D^2  = {sp.N(Vhat_val**2, 30)}   <- the k=2 rung rescaling")

    print("\n--- checks ---")
    ok = True
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok = ok and bool(passed)
    print(f"\n{sum(1 for _, p in checks if p)}/{len(checks)}")

    print("""
CONCLUSION (scope (a) -- a scope-limited negative about ONE construction):

  The corpus's ONE derived rung does NOT carry to convention D as written.
  `1 - u^2` is not bar-invariant; its bar-defect is exactly `(1 - q^4)*u^2`.
  Re-expressed in the forced variable it carries coefficient `-1/Vhat_D^2`
  of weight +4, where the forced form requires weight 0.

  This CORRECTS PR #6282's Result 2.  That result read the value `-1` as a
  weight-0 rational constant and concluded it was CONSISTENT with `X = u*Vhat`.
  The value is indeed weight 0 -- but it is the coefficient of `u^2`, not of
  `X^2`, and the two differ by `Vhat_D^2`.  Result 2's weight argument tested
  a coefficient the corpus does not actually derive.

  NOT a claim that `c_2 = -1` is wrong.  It is correct in the frame it was
  derived in.  What fails is its TRANSPORT to D, which is the same failure
  #6244 established for `cos(alpha_eff)` and #6282 for the product form.
  All three legs of the C instrument fail to transport, for the one reason:
  D's grading is multiplicative and C's is affine.
""")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
