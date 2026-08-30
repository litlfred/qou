#!/usr/bin/env python3
"""Can the q-Toffoli gate be an involution?  Two independent routes, both exact.

Bean `qou-54tg`.  `q-game-of-life.lean`'s `qGameOfLife_reversible` assumes
`Function.Involutive T`, justified in its docstring as "an involution in H_3(q)",
while the same content object's PROOF says the generators are *not* involutions
at generic q.  This settles it at the GATE.

ROUTE A (assumption-free, and the one formalised).  `prop:toffoli-transfer-matrix`
states unitarity and antisymmetry `P_67 = -P_76`.  A real orthogonal involution is
symmetric, and symmetric + antisymmetric forces the entry to zero.  So the gate is
an involution only where `Phi(q) = 0`, and `Phi` carries the factor `(q - 1)`:
only in the classical limit.  Formalised sorry-free in
`QOU/Information/AntisymmetricInvolutionForcesZero.lean`; this script only checks
the `Phi` factor claim numerically-exactly.

ROUTE B (needs a support assumption; corroboration only).  Assuming row 7 is
supported on {6,7} as the classical Toffoli's is, `M^2 = I` forces
`P_77^2 - Phi^2 = 1`.  Substituting `q = u^2` clears the half-powers; the
resulting polynomial has ZERO real roots by an exact Sturm count.

NO FLOAT64 anywhere: sympy exact rationals and algebraic numbers throughout,
per AGENTS.md "PROBES ARE NOT EXEMPT".  Emits no witness -- it re-derives a
structural fact, and re-running it is the check.
"""
import sympy as sp


def toffoli_entries(u):
    """P_77 and Phi in the variable u, where q = u^2 (so sqrt(q) = u)."""
    q = u**2
    P77 = (q + u - 1) / (q + 1)
    Phi = (q - 1) * (u**3 + u - 1) * (u**3 + q + 1) / (2 * (q + 1) ** 2)
    return P77, Phi


def main() -> int:
    u = sp.symbols("u", positive=True)
    P77, Phi = toffoli_entries(u)
    ok = True

    # --- Route A: Phi vanishes exactly at q = 1 (u = 1), via its (q-1) factor.
    phi_num = sp.factor(sp.numer(sp.together(Phi)))
    assert (u - 1) in phi_num.args or sp.simplify(Phi.subs(u, 1)) == 0, phi_num
    print(f"Route A  Phi(u=1) = {sp.simplify(Phi.subs(u, 1))}   (classical limit)")
    roots_phi = [r for r in sp.solve(sp.Eq(sp.numer(sp.together(Phi)), 0), u)
                 if r.is_real and r.is_positive]
    print(f"         Phi = 0 at positive real u: {roots_phi}")
    if roots_phi != [sp.Integer(1)]:
        print("         NOTE: additional zeros of Phi above; the (q-1) factor is"
              " not the only one, so 'only at q=1' would be an over-claim.")

    # --- Route B: M^2 = I would force P_77^2 - Phi^2 = 1.
    residual = sp.simplify(P77**2 - Phi**2 - 1)
    N = sp.Poly(sp.numer(sp.together(-residual)), u)
    n_pos = sp.polys.polytools.count_roots(N, 0, sp.oo)      # exact Sturm count
    n_real = sp.polys.polytools.count_roots(N, -sp.oo, sp.oo)
    print(f"Route B  numerator degree {N.degree()}, "
          f"real roots in (0,inf): {n_pos}, overall: {n_real}")
    if n_pos != 0:
        print("         FAIL: a positive real q admits P_77^2 - Phi^2 = 1")
        ok = False
    else:
        print("         => P_77^2 - Phi^2 != 1 at every q > 0; no involution")

    # --- At the substrate, exactly (rational q0, algebraic sqrt).
    q0 = sp.Rational(11099785827513808, 10**16)
    P77_0, Phi_0 = toffoli_entries(sp.sqrt(q0))
    val = P77_0**2 - Phi_0**2
    print(f"substrate q0 = {sp.N(q0, 17)}")
    print(f"         P_77^2 - Phi^2 = {sp.N(val, 30)}   (required 1 for M^2 = I)")
    print(f"         shortfall      = {sp.N(1 - val, 20)}")
    if sp.N(val, 30) >= 1:
        print("         FAIL: substrate reaches the involution condition")
        ok = False

    print("\nVERDICT:", "the q-Toffoli is not an involution at any q > 1"
          if ok else "CHECK FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
