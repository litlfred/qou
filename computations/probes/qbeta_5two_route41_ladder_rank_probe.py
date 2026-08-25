#!/usr/bin/env python3
"""Route 41 -- the five-term / Bloch-group ladder search on the 5_2 orbit, and
two corrections to claims made while running it.

Bean `qou-0yqu`.  Follows Route 40, which narrowed the search alphabet from
"the y_j" to the powers `c^m` of a single generator (`c` the real root of
`X^3+X^2-1`, `c = 1/rho`, rho the plastic number).

WHAT THIS SETTLES
-----------------
Nothing about the sum rule itself.  It bounds a second family, records a
general fact that explains why this family keeps not closing, and retracts two
things this session got wrong.

1. CORRECTION -- the Li2-form five-term RHS used in a first draft is WRONG.
   The argument set `[x, y, (1-x)/(1-xy), 1-xy, (1-y)/(1-xy)]` is right (it is
   the Rogers-L pentagon), but the identity is a statement about **Rogers L**,
   `L(z) = Li2(z) + log(z)log(1-z)/2`, summing to `pi^2/2` -- not the Li2 +
   log-product expression first written.  G1 gates both: the correct form to
   40 dps, and the wrong one FAILING at the same generic real points.  It was
   caught by evaluating off the configuration it was going to be used on.

2. CORRECTION -- "sum_sigma D(sigma x) = 0 is a feature of the disc -23 field"
   is WRONG; it is general.  `D(conj z) = -D(z)`, complex embeddings come in
   conjugate pairs, and real embeddings give `D = 0`, so the Bloch-Wigner
   regulator vanishes on a Galois sum in EVERY number field.  G2 gates it in
   the disc -23 cubic and in a quartic.  The intended "negative control"
   refused to be one, and that is what revealed the fact was general.

   This is worth recording because it explains the whole pattern: the Bloch
   group / ladder machinery computes an invariant that is **identically zero**
   on a Galois-summed dilogarithm.  Routes 1-5 and 40 were not unlucky.

3. THE RANK RESULT.  Over a set `S` of Galois orbits in `K = Q(c)` closed under
   `x -> 1-x` and `x -> 1/x`, with every Euler-reflection, inversion, and
   pentagon relation that closes in `S`, the functional reading off
   `A = sum Li2(y_j)` is NOT in the row space (G3).  Measured at two sizes:

       |S| = 82  orbits,  55 relations, rank 46  -> 47 with target stacked
       |S| = 168 orbits, 316 relations, rank 153 -> 154 with target stacked

   The gap stays exactly 1 as `S` doubles.

⚠ AND A LIMIT ON G3 THAT MUST NOT BE GLOSSED
--------------------------------------------
The rows above are correct as **Bloch-group** statements (relations modulo
torsion).  Converting one into a statement about `sum Li2` needs the pentagon
summed over the three embeddings to have an elementary right-hand side, and
G4 measures that it does NOT come out to `3*pi^2/2`: at `x = y = c` the sum is
`8.3326...` against `14.8044...`, off by `6.4718...`.  The pentagon's validity
region is the real one; the two complex embeddings carry branch corrections
that are not accounted for here.  So G3 bounds the family only up to that
bookkeeping, and this probe does not claim otherwise.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib
from fractions import Fraction as Fr
from itertools import product

import sympy as sp
from mpmath import arg, fabs, im, log, mp, mpc, mpf, nstr, pi, polylog, polyroots, quad
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

x = sp.symbols('x')

# ---- exact arithmetic in K = Q(c), c^3 = 1 - c^2 ---------------------------
ZERO = (Fr(0),) * 3
ONE = (Fr(1), Fr(0), Fr(0))
GEN = (Fr(0), Fr(1), Fr(0))


def kmul(u, v):
    p = [Fr(0)] * 5
    for i in range(3):
        for j in range(3):
            p[i + j] += u[i] * v[j]
    a0, a1, a2, a3, a4 = p
    a0 += a3
    a2 -= a3                       # c^3 = 1 - c^2
    a0 -= a4
    a1 += a4
    a2 += a4                       # c^4 = -1 + c + c^2
    return (a0, a1, a2)


def ksub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def kinv(u):
    if u == ZERO:
        return None
    cols = [kmul(u, ONE), kmul(u, GEN), kmul(u, kmul(GEN, GEN))]
    M = [[cols[j][i] for j in range(3)] + [Fr(1) if i == 0 else Fr(0)] for i in range(3)]
    for i in range(3):
        piv = next((r for r in range(i, 3) if M[r][i] != 0), None)
        if piv is None:
            return None
        M[i], M[piv] = M[piv], M[i]
        pv = M[i][i]
        M[i] = [a / pv for a in M[i]]
        for r in range(3):
            if r != i and M[r][i] != 0:
                f = M[r][i]
                M[r] = [a - f * b for a, b in zip(M[r], M[i])]
    return (M[0][3], M[1][3], M[2][3])


def kpow(m):
    r = ONE
    for _ in range(m):
        r = kmul(r, GEN)
    return r


def kminpoly(u):
    B, cur = [ONE], ONE
    for _ in range(3):
        cur = kmul(cur, u)
        B.append(cur)
    def rat(t):
        return sp.Rational(t.numerator, t.denominator)
    Mx = sp.Matrix(3, 3, lambda i, j: rat(B[j][i]))
    rhs = sp.Matrix([rat(B[3][i]) for i in range(3)])
    if Mx.det() != 0:
        co = Mx.solve(rhs)
        return sp.expand(x ** 3 - co[2] * x ** 2 - co[1] * x - co[0])
    return sp.expand(x - rat(u[0]))


def build(max_pow, depth):
    S = set()
    for m in range(1, max_pow + 1):
        p = kpow(m)
        S.add(p)
        S.add(tuple(-t for t in p))
    for _ in range(depth):
        new = set()
        for u in list(S):
            a = ksub(ONE, u)
            if a != ZERO:
                new.add(a)
            b = kinv(u)
            if b:
                new.add(b)
        S |= new
    return {u for u in S if u != ZERO and ksub(ONE, u) != ZERO}


def rank_report(max_pow, depth):
    S = build(max_pow, depth)
    key = {u: str(kminpoly(u)) for u in S}
    orbits = sorted(set(key.values()))
    idx = {o: i for i, o in enumerate(orbits)}
    deg = {o: sp.Poly(sp.sympify(o), x).degree() for o in orbits}

    def add(v, u):
        o = key[u]
        v[idx[o]] += 1 if deg[o] == 3 else 3      # Galois sum over 3 embeddings

    rows = set()
    for u in S:                                   # Euler reflection [u] + [1-u]
        a = ksub(ONE, u)
        if a in key:
            v = [0] * len(orbits); add(v, u); add(v, a); rows.add(tuple(v))
    for u in S:                                   # inversion [u] + [1/u]
        b = kinv(u)
        if b is not None and b in key:
            v = [0] * len(orbits); add(v, u); add(v, b); rows.add(tuple(v))
    Sl = list(S)
    for u, y in product(Sl, repeat=2):            # Rogers-L pentagon
        xy = kmul(u, y)
        d = ksub(ONE, xy)
        if d == ZERO:
            continue
        i4 = kinv(d)
        if i4 is None:
            continue
        args = [u, y, kmul(ksub(ONE, u), i4), d, kmul(ksub(ONE, y), i4)]
        if any(a not in key or a == ZERO or ksub(ONE, a) == ZERO for a in args):
            continue
        v = [0] * len(orbits)
        for a in args:
            add(v, a)
        rows.add(tuple(v))
    tgt_o = str(sp.expand(x ** 3 - 2 * x ** 2 + 3 * x - 1))
    assert tgt_o in idx, "the 5_2 orbit is not in S -- the search would be vacuous"
    t = [0] * len(orbits)
    t[idx[tgt_o]] = 1
    A = sp.Matrix(sorted(rows))
    r1 = A.rank()
    r2 = A.col_join(sp.Matrix([t])).rank()
    return len(orbits), len(rows), int(r1), int(r2)


def BW(z):
    z = mpc(z)
    if fabs(im(z)) < mpf(10) ** -35:
        return mpf(0)
    return im(polylog(2, z)) + arg(1 - z) * log(abs(z))


def rogersL(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def pentagon(X, Y):
    XY = X * Y
    return [X, Y, (1 - X) / (1 - XY), 1 - XY, (1 - Y) / (1 - XY)]


def galois_sum_li2(co):
    def f(z):
        if z == 0:
            return mpf(co[1])
        return log(sum(co[k] * z ** k for k in range(len(co)))) / z
    return -quad(f, [0, 1])


def main() -> int:
    set_compute_dps()
    gates = []
    rc = polyroots([1, 1, 0, -1], maxsteps=500, extraprec=1500)

    # ---- G1: the pentagon form, and the wrong form failing -------------------
    pts = [(mpf(3) / 10, mpf(4) / 10), (mpf(1) / 7, mpf(2) / 9), (mpf(3) / 5, mpf(1) / 4)]
    good = mpf(0)
    bad = mpf(10) ** 9
    for X, Y in pts:
        args = pentagon(X, Y)
        good = max(good, fabs(sum(rogersL(a) for a in args) - pi ** 2 / 2))
        wrong_lhs = sum(polylog(2, a) for a in args)
        wrong_rhs = (pi ** 2 / 6 - log(X) * log(1 - X) - log(Y) * log(1 - Y)
                     + log(args[2]) * log(args[4]))
        bad = min(bad, fabs(wrong_lhs - wrong_rhs))
    gates.append({
        "gate": "G1",
        "claim": "the five-term identity on this argument set is a ROGERS-L statement -- "
                 "sum of L over the five pentagon arguments is pi^2/2, exact at generic real "
                 "points. The second half is the negative control: the Li2-plus-log-product RHS "
                 "written in a first draft FAILS at the same points, by an amount that varies "
                 "with the point, so it is not a constant offset but a wrong identity",
        "worst_residual_rogersL_form": nstr(good, 10),
        "smallest_residual_of_the_WRONG_form": nstr(bad, 10),
        "pass": bool(good < mpf(10) ** -30 and bad > mpf(1)),
    })

    # ---- G2: the Bloch-Wigner regulator vanishes on Galois sums, generally ---
    worst_cubic = mpf(0)
    for co in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, -3), (2, -1, 5), (-3, 1, 1), (7, -2, 4)]:
        worst_cubic = max(worst_cubic,
                          fabs(sum(BW(co[0] + co[1] * r + co[2] * r ** 2) for r in rc)))
    rq = polyroots([1, 0, 0, -1, -1], maxsteps=500, extraprec=1500)
    worst_quartic = mpf(0)
    for co in [(0, 1, 0, 0), (1, 2, -3, 1), (2, -1, 5, 0)]:
        worst_quartic = max(worst_quartic, fabs(sum(
            BW(co[0] + co[1] * r + co[2] * r ** 2 + co[3] * r ** 3) for r in rq)))
    gates.append({
        "gate": "G2",
        "claim": "the Bloch-Wigner regulator is IDENTICALLY ZERO on a Galois sum -- in the "
                 "disc -23 cubic and equally in a quartic, because D(conj z) = -D(z), complex "
                 "embeddings come in conjugate pairs, and real embeddings give D = 0. This was "
                 "written as a feature of the 5_2 field; it is general, and the quartic was "
                 "meant to be a negative control and refused to be one. It is why Bloch-group "
                 "machinery cannot see A: the invariant it computes vanishes here by symmetry",
        "worst_in_disc_-23_cubic": nstr(worst_cubic, 10),
        "worst_in_quartic": nstr(worst_quartic, 10),
        "pass": bool(worst_cubic < mpf(10) ** -30 and worst_quartic < mpf(10) ** -30),
    })

    # ---- G3: the ladder rank test -------------------------------------------
    n_orb, n_rel, r1, r2 = rank_report(10, 2)
    gates.append({
        "gate": "G3",
        "claim": "over a set of Galois orbits in Q(c) closed under x -> 1-x and x -> 1/x, with "
                 "EVERY Euler-reflection, inversion and pentagon relation that closes in it, the "
                 "functional reading off A is NOT in the row space -- the rank rises by one when "
                 "it is stacked on. Recomputed here at the smaller size; the larger run "
                 "(168 orbits, 316 relations) gave rank 153 -> 154, the same gap of exactly one",
        "orbits": n_orb, "relations": n_rel,
        "rank": r1, "rank_with_target": r2,
        "A_determined": bool(r1 == r2),
        "larger_run": {"orbits": 168, "relations": 316, "rank": 153, "rank_with_target": 154},
        "pass": bool(r1 == r2 - 1),
    })

    # ---- G4: the limit on G3 -- branch corrections are real and unaccounted --
    tot = sum(sum(rogersL(a) for a in pentagon(r, r)) for r in rc)
    gap = fabs(tot - 3 * pi ** 2 / 2)
    gates.append({
        "gate": "G4",
        "claim": "THE LIMIT ON G3, gated so it cannot be glossed. Turning a pentagon row into a "
                 "statement about sum Li2 needs the pentagon summed over the three embeddings to "
                 "be elementary, and it does NOT come out to 3*pi^2/2: at x = y = c the sum is "
                 "8.3326 against 14.8044. The pentagon's validity region is the real one and the "
                 "two complex embeddings carry branch corrections not accounted for. G3 bounds "
                 "the family only up to that bookkeeping",
        "sum_over_three_embeddings": nstr(tot, 25),
        "three_halves_pi_squared": nstr(3 * pi ** 2 / 2, 25),
        "unaccounted_gap": nstr(gap, 15),
        "pass": bool(gap > mpf(1)),
    })

    # ---- G5: the target is unmoved ------------------------------------------
    A = galois_sum_li2([1, -2, 3, -1])
    C1, C2 = galois_sum_li2([1, 1, 0, -1]), galois_sum_li2([1, -1, 2, -1])
    gates.append({
        "gate": "G5",
        "claim": "the target is unmoved. A = sum Li2(y_j) over the roots of y^3-2y^2+3y-1 is "
                 "still exactly what the sum rule needs and still has no proof. This gate exists "
                 "so nothing above can be misread as progress toward it",
        "A": nstr(A, 30), "C_1": nstr(C1, 25), "C_2 (= B)": nstr(C2, 25),
        "pass": bool(fabs(A - mpf("0.9717306814686482591277741699")) < mpf(10) ** -25),
    })

    out = {
        "probe": "qbeta_5two_route41_ladder_rank",
        "bean": "qou-0yqu", "dps": mp.dps,
        "follows": "Route 40 (qbeta_5two_route40_distribution_factors_probe.py)",
        "retracts": [
            "the Li2-form five-term RHS used in a first draft of this search (G1) -- the "
            "argument set is right, the identity is Rogers-L, not Li2 plus a log product",
            "'sum_sigma D(sigma x) = 0 is a feature of the disc -23 field' (G2) -- it is "
            "general, true in every number field, by conjugate symmetry",
        ],
        "gates": gates,
        "verdict": {
            "measured": "the reflection + inversion + pentagon system over an (x -> 1-x, "
                        "x -> 1/x)-closed set of Galois orbits does not determine A: rank rises "
                        "by exactly one when the target functional is stacked, at both sizes "
                        "tried (82 and 168 orbits).",
            "why": "the Bloch-Wigner regulator vanishes identically on a Galois sum, so the "
                   "invariant the ladder machinery computes carries no information about A. "
                   "That is general, not special to this field.",
            "limit": "the rows are Bloch-group statements. Converting one into a statement "
                     "about sum Li2 needs branch bookkeeping over the complex embeddings that "
                     "is NOT done here, and G4 measures a 6.4718 gap where an elementary right- "
                     "hand side was assumed. The bound on the family is only as good as that.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route41-ladder-rank.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:76]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "the ladder family does not determine A over the orbit sets tried, and the Bloch-Wigner "
        "regulator vanishes identically on Galois sums so the machinery cannot see A at all -- "
        "but G4 records that the rows are not yet Li2 statements. The 5_2 sum rule remains "
        "verified to 80 dps, unproved." if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
