#!/usr/bin/env python3
"""IDENTIFY the SL(3)-lift obstruction class [w] -- by descent to Q(zeta_3), not by search.

WHERE THIS STARTS.  ptolemy_sl3_lift_obstruction_class.py established that the lift
obstruction is a well-defined class [w] in K^x/(K^x)^3 (K = Q[T]/(f), degree 4) and that
it is NOT in <[u]> -- so it is an independent H^1(K, mu_3) class.  Naming it is the next
question, and the NO-FITTING directive bars the obvious move: picking a candidate
generator because it matches [w] is selection against the target.

THE DERIVED ROUTE.  Two facts, each read off the recorded data rather than guessed.

1. sigma_a and sigma_b agree EXACTLY on Q(zeta_3).  The witness records
   Gal(K/Q) = Z/2 x Z/2 with tau = sigma_a sigma_b fixing Q(zeta_3); since [K : Fix(tau)]
   = |<tau>| = 2 = [Q(zeta_3) : Q], Fix(tau) IS Q(zeta_3), and sigma_b^2 = 1 then gives
   sigma_a = sigma_b on it.  So a quantity is sigma-independent exactly when it lies in
   Q(zeta_3) -- which is why the scalar ansatz's obstructing_product is byte-identical
   for both sigma (same relation, c_0111_0 / c_0021_0).  That coincidence is a
   MEMBERSHIP statement, not a mystery.

2. If w lies in Q(zeta_3) then the cube question descends there.  Let F = Q(zeta_3), so
   [K : F] = 2.  If y in K has y^3 = w in F, then [F(y) : F] divides 3 (y is a root of
   Y^3 - w over F) and also divides 2 (F(y) <= K), hence y is in F.  So

       w is a cube in K   <=>   w is a cube in F.

   F is the Eisenstein field: class number 1, units {+-1, +-omega, +-omega^2}.  So the
   class of w in F^x/(F^x)^3 is DETERMINED by factorisation -- the valuation mod 3 at
   each Eisenstein prime, times a unit -- and is computed, never searched.

WHAT THIS FILE DOES.
  * tests w in F by solving w = a + b*u over Q (four equations, two unknowns: the
    over-determination IS the membership test, and an inconsistent system means w is not
    in F and the descent does not apply);
  * clears denominators to an Eisenstein integer and factors its norm
    N(a + b*omega) = a^2 - a*b + b^2 over Z, reporting the rational primes and their
    exponents mod 3;
  * reports the exponent pattern, which is what identifies the class.

It does NOT assert what the class "is" in framework terms.  Naming it as a Ptolemy
coordinate, a discriminant or a unit would require deriving that identification; this
file supplies the arithmetic invariant such a derivation would have to reproduce.

Exact throughout (sympy Rationals); no floats, no tolerances.
"""
import json
import sys
import warnings

warnings.filterwarnings('ignore')
import sympy as sp

T = sp.Symbol('T')
WIT = 'computations/ptolemy/ptolemy-duality-sigma-coboundary-test.witness.json'
PT = 'computations/ptolemy/L6a4-c1-ptolemy-in-K.json'


def main():
    wit = json.load(open(WIT))
    pt = json.load(open(PT))
    f = sp.expand(sp.sympify(wit['field']['min_poly'].replace('t', 'T')))
    red = lambda e: sp.expand(sp.rem(sp.expand(e), f, T))
    S = lambda s: sp.expand(sp.sympify(s.replace('t', 'T')))

    u = S(pt['ptolemy']['u'])
    assert red(u ** 2 + u + 1) == 0, "u is not a primitive cube root of unity"
    w = S(wit['results']['sigma_b']['B_torus']['w_eq_r_of_3e0'])
    print(f"w = {w}", flush=True)

    # ---- 1. the Galois fact, verified rather than quoted -----------------------
    sa = S(wit['sigma']['sigma_a'])
    sb = S(wit['sigma']['sigma_b'])
    app = lambda g, x: red(sp.expand(x.subs(T, g)))
    tau = lambda x: app(sa, app(sb, x))
    print(f"tau = sigma_a sigma_b fixes u: {red(tau(u) - u) == 0}", flush=True)

    # ---- 2. is w in F = Q(u)?  Solve w = a + b*u over Q ------------------------
    a, b = sp.symbols('a b', rational=True)
    resid = sp.Poly(sp.expand(a + b * u - w), T)
    eqs = [sp.Eq(c, 0) for c in resid.all_coeffs()]
    print(f"membership system: {len(eqs)} equations in 2 unknowns "
          f"(over-determined -- consistency IS the test)", flush=True)
    sol = sp.solve(eqs, [a, b], dict=True)
    if not sol:
        print("\nw is NOT in Q(zeta_3): the system is inconsistent.")
        print("The descent does not apply and the class must be computed in K directly.")
        print("That is a real finding -- record it and stop, do not force the route.")
        return 1
    A, B = sp.nsimplify(sol[0][a]), sp.nsimplify(sol[0][b])
    assert red(A + B * u - w) == 0, "reconstruction failed"
    print(f"\nw IS in Q(zeta_3):   w = ({A}) + ({B})*u", flush=True)
    print(f"   cross-check, tau(w) = w: {red(tau(w) - w) == 0}", flush=True)

    # ---- 3. clear denominators, factor the Eisenstein norm ---------------------
    den = sp.lcm(sp.denom(A), sp.denom(B))
    Ai, Bi = sp.Integer(A * den), sp.Integer(B * den)
    print(f"\nw = (Ai + Bi*omega)/den   with  Ai = {Ai}, Bi = {Bi}, den = {den}",
          flush=True)
    # N(x + y*omega) = x^2 - x*y + y^2  for omega a primitive cube root of unity
    nz = sp.Integer(Ai ** 2 - Ai * Bi + Bi ** 2)
    print(f"N(Ai + Bi*omega) = {nz}", flush=True)
    print(f"N(den)           = {sp.Integer(den ** 2)}", flush=True)

    def show(n, label):
        n = sp.Integer(n)
        if n == 0:
            print(f"   {label}: ZERO -- w would not be a unit; impossible here")
            return {}
        fac = sp.factorint(abs(n))
        print(f"   {label} = {sp.factorint(abs(n))}"
              f"{'  (sign -1)' if n < 0 else ''}", flush=True)
        return fac

    print("\nfactorisations:", flush=True)
    fn = show(nz, 'N(numerator)')
    fd = show(den ** 2, 'N(den)')

    print("\nexponents mod 3 (a prime with exponent = 0 mod 3 contributes nothing "
          "to the class):", flush=True)
    allp = sorted(set(fn) | set(fd))
    live = []
    for p in allp:
        e = fn.get(p, 0) - fd.get(p, 0)
        tag = 'TRIVIAL' if e % 3 == 0 else f'LIVE (e = {e} = {e % 3} mod 3)'
        print(f"   p = {p:>12}   exponent {e:>4}   {tag}", flush=True)
        if e % 3:
            live.append((p, e % 3))

    print()
    if live:
        print(f"[w] is supported on {len(live)} rational prime(s): "
              f"{[p for p, _ in live]}")
        print("Those valuations are the arithmetic invariant of the obstruction.  Any")
        print("proposed identification of [w] -- a Ptolemy coordinate, a discriminant, a")
        print("unit of O_K -- must REPRODUCE this exponent pattern; matching it by")
        print("search would be selection against the target and is barred.")
    else:
        print("every exponent vanishes mod 3, so the class is carried by a UNIT of")
        print("Z[omega] alone -- the unit group is {+-1, +-omega, +-omega^2}, and the")
        print("previous probe already refuted w, w*u and w*u^2 as cubes.")
        print("NOTE: -1 = (-1)^3 IS a cube, so the only non-trivial unit classes are")
        print("[omega] and [omega^2] -- both already excluded.  If this branch is")
        print("reached the two measurements are INCONSISTENT and one of them is wrong;")
        print("report that, do not reconcile it.")
    print("\nScope: this point, this class.  Nothing here bears on whether")
    print("rho -> rho^{-T} induces sigma_b as a map on the variety (qou-qjhc, open).")
    return 0


if __name__ == '__main__':
    sys.exit(main())
