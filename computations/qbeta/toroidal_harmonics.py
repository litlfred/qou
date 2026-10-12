#!/usr/bin/env python3
"""
Toroidal Harmonics Derivation Script (convention D)

`derive_bridge()`  — VERIFIED. The exact symbolic change of variables
    `x = 1/(2w) - 1` mapping the toroidal Legendre operator
    `(1 - x^2) y'' - 2x y' + (n^2 - 1/4) y` to the `w`-operator
    `(16 w^3 - 4 w^2) f'' + 16 w^2 f' + (4 n^2 - 1) f`. Genuine identity
    (SymPy `simplify` -> 0). It is a change of variables and holds for
    whatever `w` is later identified with.

    Identification of `w` (convention D, canonical since 2026-08-15):
    with `q = e^eta`, `z = q^3/(q^2+1)` and the negative loop value
    `z_- = z - (q - 1/q) = 1/(q(q^2+1))`, the bar-invariant product is
    `w = z z_- = 1/[2]_q^2 = 1/(2(cosh 2eta + 1))`, so `x = cosh 2eta`
    (checked symbolically in `check_D_identification`). The convention-C
    identity `w = z^2 = 1/(2(cosh eta + 1))` (with `z = sqrt(q)/(q+1)`) is
    excised; under D, `w = z^2` gives `x < 1` at the substrate and has no
    toroidal reading (also checked there).

    OPEN: whether `w = z z_-` is the right variable at all. The proved
    Markov-parameter recursion
    `4(n+1)a_{n+1} + 6n a_n + (2n-1)a_{n-1} = 0` is written in `q - 1`,
    a DIFFERENT variable, and no link from it to this `w`-ODE is
    established here. Nothing here makes any c_k exact. Bean qou-nxjw.

`evaluate_c_lambda()` — NEGATIVE / numerical-coincidence audit, NOT a
    derivation and NOT paper content. The comparison target c_lambda_exp
    = B_AME/E_gate contains the experimental binding (circular). Under the
    D identification x = cosh 2eta no "pretty" anchor matches it: the
    golden anchor q = 1/phi gives x = 3/2 and lands ~14.7% below. The
    former ~0.12% golden near-match came only from the excised C reading
    x = cosh eta and is printed once below as a labelled historical
    comparison. See docs/audits/2026-07-06-c3-not-exact-cross-anchor-verdict.md.

Precision: mpmath end to end (mp.dps = 50); Legendre functions via
mpmath.legenp (Ferrers type 2 for |x| < 1, type 3 for x > 1). Numbers are
displayed with mp.nstr; no float64 arithmetic.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 50

# Proton pin (owner directive 2026-08-07), carried as a decimal string so no
# float64 value enters the mpmath computation.
try:
    from qou_substrate.constants import Q_50_DIGIT_STR as _Q0_STR
    Q0 = mp.mpf(_Q0_STR)
except Exception:  # pragma: no cover - documented pin string
    Q0 = mp.mpf("1.1099785827513808")


def toroidal_harmonic_P(n, m, x):
    """Toroidal harmonic P_{n-1/2}^m(x); x = cosh(2 eta) under convention D.

    mpmath.legenp: type=2 (Ferrers, on the cut |x| < 1) or type=3
    (x outside [-1, 1]). For m = 0 the two agree on x > -1.
    """
    x = mp.mpf(x)
    v = mp.mpf(n) - mp.mpf(1) / 2
    typ = 2 if abs(x) < 1 else 3
    return mp.legenp(v, m, x, type=typ)


def x_of_q_D(q):
    """Convention D: x = cosh(2 ln q) = (q^2 + q^-2)/2."""
    q = mp.mpf(q)
    return (q**2 + q**-2) / 2


def q_of_x_D(x):
    """Inverse of x_of_q_D on the q > 1 branch (the q < 1 branch is 1/q)."""
    return mp.e ** (mp.acosh(x) / 2)


def check_D_identification():
    """Symbolic: w = z z_- gives x = cosh 2 eta; w = z^2 does not."""
    print("--- Convention-D identification of w ---")
    eta = sp.symbols('eta', real=True)
    q = sp.exp(eta)
    z = q**3 / (q**2 + 1)
    z_minus = sp.simplify(z - (q - 1 / q))
    print(f"  z_- = z - (q - 1/q) = {sp.factor(z_minus)}")
    w_prod = sp.simplify(z * z_minus)
    gap_prod = sp.simplify((1 / (2 * w_prod) - 1 - sp.cosh(2 * eta)).rewrite(sp.exp))
    print(f"  w = z z_- = {sp.factor(w_prod)};  1/(2w) - 1 - cosh(2 eta) = {gap_prod}")
    assert gap_prod == 0
    gap_sq = sp.simplify((1 / (2 * z**2) - 1 - sp.cosh(eta)).rewrite(sp.exp))
    print(f"  w = z^2 with x = cosh eta (the C identity): residual = {gap_sq}")
    assert gap_sq != 0, "C identity unexpectedly holds under D"
    zD = Q0**3 / (Q0**2 + 1)
    zm = zD - (Q0 - 1 / Q0)
    x_sq = 1 / (2 * zD**2) - 1
    x_pr = 1 / (2 * zD * zm) - 1
    print(f"  at q0 = {mp.nstr(Q0, 17)}: eta0 = ln q0 = {mp.nstr(mp.log(Q0), 12)}")
    print(f"    z^2   = {mp.nstr(zD**2, 12)} -> x = {mp.nstr(x_sq, 12)}  (< 1: not cosh of a real angle)")
    print(f"    z z_- = {mp.nstr(zD*zm, 12)} -> x = {mp.nstr(x_pr, 12)}"
          f"  = cosh(2 eta0) = {mp.nstr(mp.cosh(2*mp.log(Q0)), 12)}")
    print()


def derive_bridge():
    print("--- Deriving the Toroidal Harmonics Bridge ---\n")

    w, x = sp.symbols('w x', real=True)
    n = sp.Symbol('n', integer=True)

    # Change of variables x = 1/(2w) - 1 (convention-neutral). Under D the
    # toroidal reading is w = z z_-, x = cosh(2 eta); see check_D_identification.
    x_w = 1/(2*w) - 1
    print("Change of variables (w = z z_- under convention D):")
    print(f"  x(w) = {x_w}")

    v = n - sp.Rational(1, 2)
    eigenvalue = v * (v + 1)

    w_x = 1 / (2 * (x + 1))
    dw_dx = sp.diff(w_x, x)

    f = sp.Function('f')(w)
    df_dw = sp.diff(f, w)
    d2f_dw2 = sp.diff(df_dw, w)

    dy_dx = df_dw * dw_dx
    d2y_dx2 = d2f_dw2 * (dw_dx**2) + df_dw * sp.diff(dw_dx, x)

    legendre_ode_x = (1 - x**2) * d2y_dx2 - 2 * x * dy_dx + eigenvalue * f
    ode_w = legendre_ode_x.subs(x, x_w)
    ode_w_simplified = sp.simplify(ode_w)
    print("\nToroidal Legendre ODE transformed to w-domain:")
    print(f"  {ode_w_simplified} = 0")

    polynomial_ode = sp.simplify(ode_w_simplified * (4 * w**2))
    collected_ode = sp.collect(sp.expand(polynomial_ode), [d2f_dw2, df_dw, f])
    print("\nPolynomial ODE form:")
    print(f"  {collected_ode} = 0")

    canonical_ode = sp.simplify(collected_ode / (w**2))
    canonical_collected = sp.collect(sp.expand(canonical_ode), [d2f_dw2, df_dw, f])
    print("\nCanonical Normalized ODE (divided by w^2):")
    print(f"  {canonical_collected} = 0")

    c_d2f = canonical_collected.coeff(d2f_dw2)
    c_df = canonical_collected.coeff(df_dw)
    c_f = canonical_collected.coeff(f)
    print("\nCanonical Coefficients:")
    print(f"  w^2 * d^2f/dw^2 : {sp.factor(c_d2f) / w**2} * w^2")
    print(f"  w * df/dw       : {sp.factor(c_df) / w} * w")
    print(f"  f               : {sp.factor(c_f)}")

    print("\nVERIFIED: toroidal Legendre ODE <-> this w-ODE (change of variables).")
    print("OPEN: whether w = z z_- (convention D) is the right variable, and any")
    print("link to the Markov z-recursion, whose variable is q - 1 (a DIFFERENT")
    print("quantity). The z -> c_k f-map is unaffected; no c_k is made exact.\n")


def evaluate_c_lambda():
    """NEGATIVE / coincidence audit — NOT a derivation, NOT paper content.

    Under convention D (x = cosh 2 eta, q = e^eta) evaluates the ratio
    P_{-1/2}(x)/P_{1/2}(x) at three "pretty" anchors and at the substrate,
    against the circular target c_lambda_exp = B_AME/E_gate.
    """
    print("--- Delta_lambda anchor scan (A=4) — NEGATIVE / coincidence audit ---")
    print("    (convention D: x = cosh(2 ln q); not a derivation)")

    b_ame = mp.mpf("28.29566")  # AME2020 binding energy of 4He in MeV
    e_gate = mp.mpf("29.99")    # SU(4) Plancherel occupancy from B_gate
    c_lambda_exp = b_ame / e_gate
    print(f"c_lambda_exp = B_AME/E_gate = {mp.nstr(c_lambda_exp, 12)}  (CIRCULAR — contains B_AME)")

    def ratio(x):
        return toroidal_harmonic_P(0, 0, x) / toroidal_harmonic_P(1, 0, x)

    def report(label, x):
        r = ratio(x)
        off = (r - c_lambda_exp) / c_lambda_exp * 100
        print(f"  [{label:<28}] x = {mp.nstr(x, 12):<16} ratio = {mp.nstr(r, 12):<16} ({mp.nstr(off, 4)} %)")

    print("\n1. Anchors under convention D (x = cosh(2 ln q) = (q^2 + q^-2)/2):")
    # Galois q = e^{2 pi i/5}: x = cosh(2 ln q) = cos(4 pi/5) = -(1+sqrt5)/4
    report("Galois q=e^(2pi i/5)", mp.cos(4 * mp.pi / 5))
    phi = (1 + mp.sqrt(5)) / 2
    report("Silver q=sqrt2-1 (x=3)", x_of_q_D(mp.sqrt(2) - 1))
    report("Golden q=1/phi (x=3/2)", x_of_q_D(1 / phi))
    report("Substrate q0 (proton pin)", x_of_q_D(Q0))

    print("\n   Historical comparison only (excised convention C, x = cosh eta):")
    report("Golden, C reading x=sqrt5/2", mp.sqrt(5) / 2)
    print("   -> the ~0.1% golden near-match exists only under the excised C reading.")

    print("\n2. Inverting to the x that reproduces c_lambda_exp:")
    x_star = mp.findroot(lambda x: ratio(x) - c_lambda_exp,
                         (mp.mpf("1.01"), mp.mpf(10)), solver='anderson')
    q_star = q_of_x_D(x_star)
    print(f"  x* (= cosh 2 eta*) : {mp.nstr(x_star, 15)}")
    print(f"  w* = 1/(2(x*+1))   : {mp.nstr(1/(2*(x_star+1)), 15)}")
    print(f"  q* (D, q > 1)      : {mp.nstr(q_star, 15)}   (q < 1 branch: {mp.nstr(1/q_star, 15)})")
    print(f"  substrate q0       : {mp.nstr(Q0, 15)}")
    print("\nVERDICT: no parameter-free anchor. Under D the golden anchor misses by")
    print("~14.7% and the substrate by ~4.8%; the q that reproduces the (circular)")
    print("target matches no framework constant. Fails 3-CAL + Delta_lambda gate.")


if __name__ == "__main__":
    check_D_identification()
    derive_bridge()
    evaluate_c_lambda()
