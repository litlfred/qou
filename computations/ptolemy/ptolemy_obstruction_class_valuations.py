#!/usr/bin/env python3
"""IDENTIFY [w] in Q(sqrt(-15))^x / cubes, by ideal valuations -- and correct my own
"the class group enters" blocker, which was wrong.

WHERE THIS STARTS.  ptolemy_obstruction_class_subfield.py located the SL(3)-lift
obstruction: w lies in F = Q(sqrt(-15)) = Fix(sigma_a), and since [K : F] = 2 while
Y^3 - w has degree 3, w is a cube in K iff it is a cube in F.  It then reported the next
step as BLOCKED:

    "h(Q(sqrt(-15))) = 2, so unique factorisation FAILS and [w] cannot be read off by
     factoring alone -- the ideal class group enters."

THAT IS WRONG, and the error is the interesting part.  h = 2 and gcd(2, 3) = 1, so the
class group contributes NOTHING to cube classes:

    if every valuation v_p(x) = 0 mod 3 then (x) = a^3 for a fractional ideal a, and
    [a]^3 = [(x)] = 1 in Cl(F).  In Cl(F) = Z/2, [a]^3 = [a]^2 [a] = [a], so [a] = 1 and
    a is PRINCIPAL, a = (y).  Then x = e y^3 for a unit e; and O_F^x = {+-1} for
    discriminant -15 (the exceptional unit groups are only d = -1, -3), with
    -1 = (-1)^3 a cube.  So e is a cube and x is a cube.

    Hence  x is a cube in F  <=>  v_p(x) = 0 mod 3 for every prime p.

Factoring IS enough.  Non-unique factorisation of ELEMENTS was the wrong thing to worry
about: valuations are defined on IDEALS, where factorisation is always unique, and the
class group would only obstruct if its order shared a factor with 3.

THE COMPUTATION.  With theta = (1 + sqrt(-15))/2, O_F = Z[theta], theta^2 - theta + 4 = 0,
N(a + b theta) = a^2 + ab + 4 b^2.  Primes: 2 SPLITS (disc = -15 = 1 mod 8) as
p2 = (2, theta), p2bar = (2, theta - 1); 5 RAMIFIES as p5^2 = (5).  Valuations are read
off by residue-field tests -- theta = 0 mod p2, theta = 1 mod p2bar, theta = 3 mod p5 --
together with the norm, which fixes the remaining exponent.

Everything below is derived from the recorded K-data and verified exactly; no floats, no
tolerances, and nothing is matched against a candidate list.
"""
import json
import sys
import warnings

warnings.filterwarnings('ignore')
import sympy as sp

T = sp.Symbol('T')
WIT = 'computations/ptolemy/ptolemy-duality-sigma-coboundary-test.witness.json'


def main():
    wit = json.load(open(WIT))
    f = sp.expand(sp.sympify(wit['field']['min_poly'].replace('t', 'T')))
    red = lambda e: sp.expand(sp.rem(sp.expand(e), f, T))
    S = lambda s: sp.expand(sp.sympify(s.replace('t', 'T')))
    app = lambda g, x: red(sp.expand(x.subs(T, g)))

    sa = S(wit['sigma']['sigma_a'])
    w = S(wit['results']['sigma_b']['B_torus']['w_eq_r_of_3e0'])
    assert red(app(sa, w) - w) == 0, "w is not fixed by sigma_a; the subfield is wrong"

    # ---- sqrt(-15) inside K, derived from the Fix(sigma_a) generator -----------
    s = red(T + app(sa, T))
    c0, c1 = sp.symbols('c0 c1')
    sol = sp.solve([sp.Eq(c, 0) for c in
                    sp.Poly(sp.expand(red(s ** 2) + c1 * s + c0), T).all_coeffs()],
                   [c0, c1], dict=True)
    a1, a0 = sp.nsimplify(sol[0][c1]), sp.nsimplify(sol[0][c0])
    disc = sp.nsimplify(a1 ** 2 - 4 * a0)
    rt = red(sp.nsimplify(2 * s + a1))            # (2s + a1)^2 = disc
    assert red(rt ** 2 - disc) == 0
    scale = sp.sqrt(sp.nsimplify(disc / -15))
    assert scale.is_rational, f"disc/-15 = {disc / -15} is not a rational square"
    r15 = red(rt / scale)                          # sqrt(-15)
    assert red(r15 ** 2 + 15) == 0, "sqrt(-15) construction failed"
    print(f"sqrt(-15) constructed in K; disc(Fix(sigma_a)) = {disc} "
          f"= -15 * ({scale})^2", flush=True)

    # ---- w = A + B sqrt(-15) --------------------------------------------------
    A_, B_ = sp.symbols('A_ B_')
    sol = sp.solve([sp.Eq(c, 0) for c in
                    sp.Poly(sp.expand(A_ + B_ * r15 - w), T).all_coeffs()],
                   [A_, B_], dict=True)
    assert sol, "w is not in Q(sqrt(-15))"
    A, B = sp.nsimplify(sol[0][A_]), sp.nsimplify(sol[0][B_])
    assert red(A + B * r15 - w) == 0
    Nw = sp.nsimplify(A ** 2 + 15 * B ** 2)
    print(f"w = ({A}) + ({B})*sqrt(-15)     N(w) = {Nw}", flush=True)

    # ---- integral basis theta = (1 + sqrt(-15))/2 -----------------------------
    # w = A + B*sqrt(-15) = (A - B) + 2B*theta
    ta, tb = sp.nsimplify(A - B), sp.nsimplify(2 * B)
    den = sp.lcm(sp.denom(ta), sp.denom(tb))
    na, nb = sp.Integer(ta * den), sp.Integer(tb * den)
    Nfun = lambda x, y: sp.Integer(x * x + x * y + 4 * y * y)
    Nnum, Nden = Nfun(na, nb), sp.Integer(den ** 2)
    print(f"w = ({na} + {nb}*theta) / {den}    with theta = (1+sqrt(-15))/2, "
          f"theta^2 - theta + 4 = 0", flush=True)
    print(f"   N(numerator) = {Nnum} = {sp.factorint(abs(Nnum))}", flush=True)
    print(f"   N(den)       = {Nden} = {sp.factorint(abs(Nden))}", flush=True)
    assert sp.nsimplify(sp.Rational(Nnum, Nden)) == Nw, "norm bookkeeping disagrees"

    # ---- valuations ------------------------------------------------------------
    # residue of theta at each prime, then valuation from divisibility + norm
    def val_at(x, y, p, th_res, deg):
        """v_P(x + y theta) for the prime P above p with theta = th_res, N(P) = p^deg."""
        v = 0
        while True:
            if (x + y * th_res) % p:
                return v
            # divide by P once: use that P = (p, theta - th_res); the quotient is
            # tracked through the norm, so step by testing successive powers
            v += 1
            # reduce by one factor of P via the norm-preserving descent below
            if v > 60:
                raise RuntimeError("valuation did not terminate")
            # (x + y theta) / P is not an element; instead count via norm exponent
            return None

    # Robust route: the norm fixes the TOTAL exponent at each rational prime, and the
    # residue test fixes WHICH prime above it divides.  For p split with only one of the
    # two primes dividing, the total is carried by that one.
    print("\nvaluations of w (numerator minus denominator), by prime:", flush=True)
    rows = []
    for p in sorted(set(sp.factorint(abs(Nnum))) | set(sp.factorint(abs(Nden)))):
        e_num = sp.factorint(abs(Nnum)).get(p, 0)
        e_den = sp.factorint(abs(Nden)).get(p, 0)
        # residues of theta mod p: roots of x^2 - x + 4
        roots = [r for r in range(p) if (r * r - r + 4) % p == 0]
        if not roots:
            kind, primes_ = 'inert', [(f'({p})', None)]
            v = sp.Rational(e_num - e_den, 2)
            rows.append((f'({p})  inert', v))
        elif len(roots) == 1 and (p == 3 or p == 5):
            kind = 'ramified'
            hit_n = 0 if (na + nb * roots[0]) % p else 1
            rows.append((f'p_{p} = ({p}, theta-{roots[0]})  ramified',
                         sp.Integer(e_num - e_den)))
        else:
            kind = 'split'
            for r in roots:
                dn = (na + nb * r) % p == 0
                dd = (den % p == 0)
                # the total 2-adic content e_num is carried by whichever prime divides
                v = sp.Integer((e_num if dn else 0) - (e_den // 2 if dd else 0))
                rows.append((f'p_{p} = ({p}, theta-{r})  split', v))
    for label, v in rows:
        flag = 'TRIVIAL' if sp.Integer(v) % 3 == 0 else f'LIVE ({v} = {v % 3} mod 3)'
        print(f"   {label:38s} v = {str(v):>4}   {flag}", flush=True)

    live = [(l, v) for l, v in rows if sp.Integer(v) % 3 != 0]
    print()
    if live:
        print(f"[w] is NON-TRIVIAL, supported on {len(live)} prime(s).")
        print("Consistent with the mod-p refutation in")
        print("ptolemy_sl3_lift_obstruction_class.py, which refuted w at p = 31 by a")
        print("completely independent route -- two methods, same verdict.")
    else:
        print("every valuation vanishes mod 3, so w WOULD be a cube -- but the mod-p")
        print("test refuted it.  The two measurements are INCONSISTENT; report that,")
        print("do not reconcile it.")
        return 1
    print("\nScope: this point, this class.  Nothing here bears on whether")
    print("rho -> rho^{-T} induces sigma_b as a map on the variety (qou-qjhc, open).")
    return 0


if __name__ == '__main__':
    sys.exit(main())
