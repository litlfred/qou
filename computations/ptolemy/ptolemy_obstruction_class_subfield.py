#!/usr/bin/env python3
"""WHERE the SL(3)-lift obstruction class lives: w is in Q(sqrt(-15)), not Q(zeta_3).

WHERE THIS STARTS.  ptolemy_sl3_lift_obstruction_class.py established that the lift
obstruction is a well-defined class [w] in K^x/(K^x)^3 and is NOT in <[u]> -- an
independent H^1(K, mu_3) class.  Locating it is the next step, and the NO-FITTING
directive bars the obvious move: picking a candidate generator because it matches [w] is
selection against the target.  So this file derives the field [w] lives in and stops
there, rather than proposing a name for it.

THE DESCENT, and it applies to whichever quadratic subfield contains w.  Let F be a
subfield with [K : F] = 2 and w in F.  If y in K has y^3 = w, then [F(y) : F] divides 3
(y is a root of Y^3 - w over F) and divides 2 (F(y) <= K), so y is in F:

    w is a cube in K   <=>   w is a cube in F.

MY OWN PREMATURE NEGATIVE, CORRECTED.  The first version of this file tested membership
in Q(zeta_3) ALONE, found it fails, and concluded "the descent does not apply".  That is
scoped to one subfield and was stated as though general.  Gal(K/Q) = Z/2 x Z/2 has THREE
quadratic subfields, and w lies in one of them -- just not that one.

WHAT IS DERIVED HERE, all exact.

  * The three subfields, from the generators sigma_a, sigma_b recorded in the witness,
    via s = T + sigma(T) and its quadratic minimal polynomial:

        Fix(sigma_a) = Q(sqrt(-15))     Fix(sigma_b) = Q(sqrt(5))
        Fix(tau)     = Q(sqrt(-3)) = Q(zeta_3)          (tau = sigma_a sigma_b)

    so K = Q(sqrt(-3), sqrt(5)) is biquadratic.  Fix(tau) = Q(zeta_3) independently
    reproduces the witness's own galois_group annotation, which is a cross-check on both.

  * w is FIXED BY sigma_a, hence lies in Q(sqrt(-15)), explicitly
    w = 4/3 - (4/1875) s with 8 s^2 - 11875 s + 5000000 = 0.  So the obstruction
    descends -- to Q(sqrt(-15)).

  * The recorded trace field of this point is ALL of K (span_dimension 4,
    equals_ptolemy_field true, L6a4-c1-trace-field.json).  So Q(sqrt(-15)) is a PROPER
    subfield of the trace field: the obstruction does not live in the trace field, it
    lives in one specific quadratic piece of it.  That is a negative, and it is reported
    as one -- comparing two independently computed corpus quantities is a cross-check,
    not a search for a match.

  * Whether the CLASS [w] is Galois-stable, which is NOT the same question as whether the
    element is.  sigma(w)/w being a cube is what fixes the class, and an element can move
    by a cube.  Both are measured, and the sigma_a row is flagged VACUOUS: it fixes w
    outright, so its ratio is 1 and "1 is a cube" is an identity, not evidence.

NOT DONE, and named so it is not mistaken for done.  Q(sqrt(-15)) has class number 2, so
unique factorisation FAILS there and the class cannot be read off by factoring alone --
the ideal class group enters.  Identifying [w] as a specific element of
Q(sqrt(-15))^x / cubes is the open next step.

Exact throughout (sympy Rationals; cube tests by reduction mod primes).  No floats.
"""
import json
import sys
import warnings

warnings.filterwarnings('ignore')
import sympy as sp

T = sp.Symbol('T')
WIT = 'computations/ptolemy/ptolemy-duality-sigma-coboundary-test.witness.json'
PT = 'computations/ptolemy/L6a4-c1-ptolemy-in-K.json'
TRACE = 'computations/ptolemy/L6a4-c1-trace-field.json'


def squarefree(d):
    """Squarefree part of a rational, as an integer (n/d ~ n*d modulo squares)."""
    n_, d_ = sp.fraction(sp.nsimplify(d))
    core = sp.Integer(n_ * d_)
    out = 1
    for p, e in sp.factorint(abs(core)).items():
        if e % 2:
            out *= p
    return -out if core < 0 else out


def main():
    wit = json.load(open(WIT))
    pt = json.load(open(PT))
    f = sp.expand(sp.sympify(wit['field']['min_poly'].replace('t', 'T')))
    red = lambda e: sp.expand(sp.rem(sp.expand(e), f, T))
    S = lambda s: sp.expand(sp.sympify(s.replace('t', 'T')))
    app = lambda g, x: red(sp.expand(x.subs(T, g)))

    u = S(pt['ptolemy']['u'])
    sa, sb = S(wit['sigma']['sigma_a']), S(wit['sigma']['sigma_b'])
    w = S(wit['results']['sigma_b']['B_torus']['w_eq_r_of_3e0'])
    tau = lambda x: app(sa, app(sb, x))
    print(f"w = {w}\n", flush=True)

    # ---- the three quadratic subfields, derived ------------------------------
    subs = {}
    for name, g in (('Fix(sigma_a)', lambda x: app(sa, x)),
                    ('Fix(sigma_b)', lambda x: app(sb, x)),
                    ('Fix(tau)', tau)):
        s = red(T + g(T))
        c0, c1 = sp.symbols('c0 c1')
        expr = red(s ** 2) + c1 * s + c0
        sol = sp.solve([sp.Eq(c, 0) for c in sp.Poly(sp.expand(expr), T).all_coeffs()],
                       [c0, c1], dict=True)
        assert sol, f"{name}: trace generator is degenerate"
        a1, a0 = sp.nsimplify(sol[0][c1]), sp.nsimplify(sol[0][c0])
        d = squarefree(a1 ** 2 - 4 * a0)
        subs[name] = (s, d, a1, a0)
        print(f"{name:14s} s^2 + ({a1})s + ({a0})   ->  Q(sqrt({d}))", flush=True)
    assert subs['Fix(tau)'][1] == -3, "Fix(tau) should be Q(zeta_3); witness disagrees"
    print("   Fix(tau) = Q(sqrt(-3)) = Q(zeta_3) reproduces the witness's own "
          "galois_group annotation", flush=True)
    print(f"   => K = Q(sqrt(-3), sqrt(5)), biquadratic", flush=True)

    # ---- which subfield holds w? --------------------------------------------
    print("\nwhich subfield contains w?", flush=True)
    home = None
    for name, (s, d, _, _) in subs.items():
        g = {'Fix(sigma_a)': lambda x: app(sa, x),
             'Fix(sigma_b)': lambda x: app(sb, x),
             'Fix(tau)': tau}[name]
        fixed = red(g(w) - w) == 0
        print(f"   {name:14s} fixes w: {fixed}", flush=True)
        if fixed:
            home = (name, s, d)
    if home is None:
        print("\nw lies in NO quadratic subfield -- it generates K.  The descent does not")
        print("apply at all, and the class must be handled in K directly.  Report as is.")
        return 1
    name, s, d = home
    a, b = sp.symbols('a b')
    sol = sp.solve([sp.Eq(c, 0) for c in
                    sp.Poly(sp.expand(a + b * s - w), T).all_coeffs()], [a, b], dict=True)
    assert sol, "w is fixed but not expressible in the trace generator; inconsistent"
    A, B = sp.nsimplify(sol[0][a]), sp.nsimplify(sol[0][b])
    assert red(A + B * s - w) == 0
    print(f"\nw lies in {name} = Q(sqrt({d})):   w = ({A}) + ({B})*s", flush=True)
    print(f"   so by the degree argument, w is a cube in K iff it is a cube in "
          f"Q(sqrt({d}))", flush=True)

    # ---- against the recorded trace field ------------------------------------
    tf = json.load(open(TRACE))
    span = tf['trace_field']['span_dimension']
    print(f"\nrecorded trace field of this point: span_dimension {span}, "
          f"equals_ptolemy_field {tf['trace_field']['equals_ptolemy_field']}", flush=True)
    if span == 4:
        print(f"   so Q(sqrt({d})) is a PROPER subfield of the trace field.  The")
        print( "   obstruction does not live in the trace field; it lives in one")
        print( "   quadratic piece of it.  Negative, reported as such.")
    else:
        print(f"   trace field is not all of K -- compare directly before concluding.")

    # ---- is the CLASS Galois-stable?  (not the same as the element) ----------
    print("\nGalois stability of the CLASS [w] -- distinct from the element", flush=True)
    fp = sp.Poly(f, T)
    cf = [sp.Integer(sp.nsimplify(c)) for c in fp.all_coeffs()]
    primes, pr = [], 5
    while len(primes) < 40 and pr < 200000:
        pr = sp.nextprime(pr)
        if pr % 3 != 1 or pr % 9 == 1 or int(cf[0]) % pr == 0:
            continue
        for x in range(pr):
            if sum(int(c) * pow(x, len(cf) - 1 - i, pr) for i, c in enumerate(cf)) % pr == 0:
                primes.append((pr, x))
                break

    def reduce_at(v, pr, th):
        v = red(v)
        co = sp.Poly(v, T).all_coeffs()[::-1] if v.free_symbols else [v]
        acc = 0
        for i, c in enumerate(co):
            n_, d_ = sp.fraction(sp.nsimplify(c))
            if int(d_) % pr == 0:
                return None
            acc += int(n_) * pow(int(d_), -1, pr) % pr * pow(th, i, pr)
        return acc % pr

    def refuted(v):
        for pr, th in primes:
            vb = reduce_at(v, pr, th)
            if vb is None or vb == 0:
                continue
            if pow(vb, (pr - 1) // 3, pr) != 1:
                return pr
        return None

    if refuted(red((2 + T) ** 3)) is not None or refuted(red((2 + T) ** 3 * u)) is None:
        print("   CONTROL FAILED: the cube test is not separating.  Aborting.")
        return 1
    inv = lambda v: red(sp.invert(red(v), f, T))
    for nm, g in (('sigma_a', lambda x: app(sa, x)),
                  ('sigma_b', lambda x: app(sb, x)),
                  ('tau', tau)):
        gw = g(w)
        if red(gw - w) == 0:
            print(f"   {nm:8s} VACUOUS -- fixes w outright, so the ratio is 1 and "
                  f"'1 is a cube' is an identity, not evidence", flush=True)
            continue
        pr = refuted(red(gw * inv(w)))
        print(f"   {nm:8s} element moves; sigma(w)/w "
              + (f"NOT a cube (refuted at p = {pr}) -> class MOVES" if pr else
                 "unrefuted as a cube over all 40 primes -> class plausibly FIXED "
                 "(NOT proved: reduction cannot prove a cube)"), flush=True)

    # class number of Q(sqrt(d)), COUNTED rather than quoted: reduced binary quadratic
    # forms a x^2 + b xy + c y^2 of discriminant D, with |b| <= a <= c and b >= 0 when
    # |b| = a or a = c.
    D = sp.Integer(d if d % 4 == 1 else 4 * d)
    forms = []
    amax = sp.integer_nthroot(int(abs(D)) // 3, 2)[0] + 1
    for A_ in range(1, amax + 1):
        for B_ in range(-A_, A_ + 1):
            num = B_ * B_ - int(D)
            if num % (4 * A_):
                continue
            C_ = num // (4 * A_)
            if C_ < A_:
                continue
            if (abs(B_) == A_ or A_ == C_) and B_ < 0:
                continue
            forms.append((A_, B_, C_))
    h = len(forms)
    print(f"\nclass number of Q(sqrt({d})), disc {D}: h = {h}   {forms}", flush=True)
    print("\nOPEN, and named so it is not mistaken for done:", flush=True)
    if h == 1:
        print(f"   h = 1, so Q(sqrt({d})) is a UFD and [w] can be read off by factoring.")
        print( "   That step is not done here.")
    else:
        print(f"   h = {h} > 1, so unique factorisation FAILS in Q(sqrt({d})) and [w]")
        print( "   cannot be read off by factoring alone -- the ideal class group enters.")
        print( "   Identifying [w] in the cube-class group is the next step.")
    print("\nScope: this point, this class.  Nothing here bears on whether")
    print("rho -> rho^{-T} induces sigma_b as a map on the variety (qou-qjhc, open).")
    return 0


if __name__ == '__main__':
    sys.exit(main())
