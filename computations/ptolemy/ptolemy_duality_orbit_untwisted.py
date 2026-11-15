#!/usr/bin/env python3
"""Does the GL(3,K) UNTWISTED duality survive the Galois orbit? (qou-qjhc)

ptolemy_duality_lambda_class_rigidity.py proved, at ONE point of the L6a4 class-1 variety,
that lambda == 1 and hence  A sigma_b(rho(w)) A^{-1} = rho(w)^{-T}  exactly in GL(3,K).
That is a statement about one representation.  This probe asks whether it is a statement
about the CLASS: does it hold at every point of the variety, and with the SAME sigma_b?

THE PREDICTION, WRITTEN BEFORE THE RUN.  At the conjugate point x_g = g(x) the
representation is rho_g = g(rho) (Galois acts on the Ptolemy coordinates).  So

    sigma(rho_g) = sigma(g(rho)) = (sigma . g)(rho)

while applying g to the base intertwining  A sigma_b(rho) A^{-1} = rho^{-T}  gives

    g(A) . (g . sigma_b)(rho) . g(A)^{-1} = g(rho^{-T}) = rho_g^{-T}.

Matching the two needs  sigma . g = g . sigma_b,  i.e.  sigma = g sigma_b g^{-1}.  Gal(K/Q)
is KLEIN FOUR -- measured, not assumed -- hence ABELIAN, so that conjugate is sigma_b
itself.  PREDICTION: sigma_b works at all four points with lambda == 1, id/tau/sigma_a fail
at all four, and the intertwiner at x_g is exactly g(A).

This is the representation-level twin of the variety-level "exists sigma, for all x" of
#7290 section 1, and it is the concrete instance of QOU/Eightfold/GaloisOrbitTransport.lean
-- whose sharpness theorem `exists_not_forall_eq_of_not_central` says commutativity is
exactly what cannot be dropped.  If the prediction FAILS, that Lean module's hypothesis is
not met by this situation and the abelian measurement is wrong; so this is a real test.

WHAT IS MEASURED
  1. each conjugate point is a genuine variety point -- the relator gate (every relator maps
     to a SCALAR) re-run at all four, before any character or intertwiner is read;
  2. the full 4 points x 4 automorphisms table, solving for an invertible A with lambda
     PINNED TO 1 -- so a success is an untwisted GL(3,K) conjugacy, not a projective one;
  3. whether the intertwiner found at x_g equals g(A), the transported one, up to the
     K-scalar Schur allows;
  4. det rho_g(g) == 1 at every point, so the SL(3) normalisation (which is what forces
     lambda into mu_3 in the first place) is not an artifact of the base point.

Exact in K throughout: Fraction and NumberField, sympy Rational nullspace.  No floats.
"""
import json
import pathlib
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from exact_character_selfduality import Elt, trace, det3, poly_to_elt, _frac  # noqa: E402
from numberfield import NumberField                                          # noqa: E402
import snappy                                                                # noqa: E402
from snappy.ptolemy.coordinates import PtolemyCoordinates                    # noqa: E402

NAME, KCLS = 'L6a4', 1
t = sp.Symbol('t')
T = sp.Symbol('T')
SIGMA_SRC = {
    'sigma_a': "-64*T**3/101015625 - T + 760000/1293",
    'sigma_b': "-T**3/625000 + 19*T**2/8000 - 1293*T/512 + 11875/8",
}

d = json.loads((HERE / f'{NAME}-c{KCLS}-ptolemy-in-K.json').read_text())
fe = sp.sympify(d['field']['min_poly'])
fp = sp.Poly(sp.expand(fe), t)
K = NumberField([_frac(c) for c in reversed(fp.all_coeffs())])
DEG = K.deg
print(f"{NAME} c{KCLS}: K = Q[t]/({fe}), degree {DEG}\n")

SIG = {k: sp.sympify(v).subs(T, t) for k, v in SIGMA_SRC.items()}
SIG['tau'] = sp.expand(SIG['sigma_a'].subs(t, SIG['sigma_b']))
SIG['id'] = t
ORDER = ['id', 'tau', 'sigma_a', 'sigma_b']
zero, one = Elt(K, K.zero()), Elt(K, K.one())


def elt_to_expr(e):
    return sum(sp.Rational(c.numerator, c.denominator) * t ** i for i, c in enumerate(e.v))


def sig_apply(e, g):
    return poly_to_elt(K, sp.expand(elt_to_expr(e).subs(t, g)), t)


def coords(e):
    v = list(e.v) + [_frac(0)] * (DEG - len(e.v))
    return [sp.Rational(c.numerator, c.denominator) for c in v[:DEG]]


for nm in ORDER:
    assert poly_to_elt(K, sp.expand(fe.subs(t, SIG[nm])), t) == zero, f"{nm} not an automorphism"

M = snappy.Manifold(NAME)
V = M.ptolemy_variety(3, obstruction_class=KCLS, eliminate_fixed_ptolemys=True)
PY_EVAL = eval(V.py_eval_section())
G = M.fundamental_group()
gens, rels = G.generators(), list(G.relators())
pt0 = {k: poly_to_elt(K, sp.sympify(v), t) for k, v in d['ptolemy'].items()}


def coords_at(gname):
    """The Ptolemy point conjugate to the base point by the automorphism `gname`."""
    return {k: sig_apply(v, SIG[gname]) for k, v in pt0.items()}


def rep_at(gname):
    dd = dict(coords_at(gname))
    dd['1'] = one
    return PtolemyCoordinates(dd, is_numerical=False, py_eval_section=PY_EVAL,
                              manifold_thunk=lambda: M,
                              non_trivial_generalized_obstruction_class=(KCLS != 0))


def minv(Mw):
    D = det3(K, Mw)
    assert not (D == zero), "singular"
    Cf = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            r_ = [x for x in range(3) if x != i]
            c_ = [y for y in range(3) if y != j]
            m = Mw[r_[0]][c_[0]] * Mw[r_[1]][c_[1]] - Mw[r_[0]][c_[1]] * Mw[r_[1]][c_[0]]
            Cf[j][i] = m if (i + j) % 2 == 0 else zero - m
    return [[Cf[i][j] / D for j in range(3)] for i in range(3)]


def transpose(Mw):
    return [[Mw[j][i] for j in range(3)] for i in range(3)]


def solve_untwisted(rho_gen, g_sig):
    """Solve  A sigma(rho(g)) = rho(g)^{-T} A  -- lambda PINNED TO 1 -- exactly over K."""
    rows = []
    for gg in gens:
        Mg = rho_gen[gg]
        S = [[sig_apply(Mg[i][j], g_sig) for j in range(3)] for i in range(3)]
        Dg = transpose(minv(Mg))
        for i in range(3):
            for j in range(3):
                coef = {}
                for q_ in range(3):
                    coef[(i, q_)] = coef.get((i, q_), zero) + S[q_][j]
                for p_ in range(3):
                    coef[(p_, j)] = coef.get((p_, j), zero) - Dg[i][p_]
                blocks = [coef.get((p_, q_), zero) for p_ in range(3) for q_ in range(3)]
                mrows = [[sp.Integer(0)] * (9 * DEG) for _ in range(DEG)]
                for idx, c in enumerate(blocks):
                    if c == zero:
                        continue
                    for k in range(DEG):
                        prod = c * poly_to_elt(K, t ** k, t)
                        for r_, val in enumerate(coords(prod)):
                            mrows[r_][idx * DEG + k] += val
                rows.extend(mrows)
    ns = sp.Matrix(rows).nullspace()
    if not ns:
        return 0, None
    cands = list(ns) + ([ns[0] + ns[1]] if len(ns) > 1 else [])
    for vec in cands:
        A = [[poly_to_elt(K, sum(vec[(p_ * 3 + q_) * DEG + k] * t ** k for k in range(DEG)), t)
              for q_ in range(3)] for p_ in range(3)]
        if not (det3(K, A) == zero):
            return len(ns), A
    return len(ns), None


report = {'probe': 'ptolemy_duality_orbit_untwisted', 'manifold': NAME,
          'obstruction_class': KCLS,
          'prediction': 'sigma_b at ALL FOUR points with lambda == 1; id/tau/sigma_a fail '
                        'at all four; intertwiner at x_g is g(A) up to a K-scalar',
          'points': {}}

print("=== 1. relator gate + SL(3) check at each of the four orbit points ===")
reps, gates = {}, {}
for gname in ORDER:
    C = rep_at(gname)
    ok, dets_one = True, True
    for r in rels:
        R = C.evaluate_word(r, G)
        off = [(i, j) for i in range(3) for j in range(3) if i != j and not (R[i][j] == 0)]
        if off or not (R[0][0] == R[1][1]) or not (R[1][1] == R[2][2]):
            ok = False
    for gg in gens:
        if not (det3(K, C.evaluate_word(gg, G)) == one):
            dets_one = False
    reps[gname] = {gg: C.evaluate_word(gg, G) for gg in gens}
    gates[gname] = (ok, dets_one)
    print(f"   x_{gname:8s}: relators -> scalar {ok}   det rho(g) == 1 {dets_one}")
    report['points'][gname] = {'relator_gate': ok, 'sl3': dets_one}
assert all(a and b for a, b in gates.values()), "a conjugate point failed its gate"

print("\n=== 2. the 4 x 4 table: invertible A with lambda PINNED TO 1 ===")
print(f"   {'point':10s}" + "".join(f"{s:>12s}" for s in ORDER))
table = {}
for gname in ORDER:
    row = {}
    cells = []
    for s in ORDER:
        dim, A = solve_untwisted(reps[gname], SIG[s])
        row[s] = {'nullspace_dim': dim, 'found': A is not None}
        if A is not None:
            row[s]['A'] = [[repr(A[i][j]) for j in range(3)] for i in range(3)]
        cells.append(f"{'FOUND(' + str(dim) + ')' if A is not None else 'none(' + str(dim) + ')':>12s}")
    table[gname] = row
    report['points'][gname]['sigmas'] = row
    print(f"   x_{gname:8s}" + "".join(cells))

works = {g: [s for s in ORDER if table[g][s]['found']] for g in ORDER}
uniform = all(works[g] == ['sigma_b'] for g in ORDER)
print(f"\n   per-point working automorphisms: { {g: works[g] for g in ORDER} }")
print(f"   *** sigma_b works at ALL FOUR points and nothing else does: {uniform} ***")
report['uniform_sigma_b'] = uniform
report['works_per_point'] = works

print("\n=== 3. is the intertwiner at x_g the TRANSPORTED one, g(A)? ===")
_, A0 = solve_untwisted(reps['id'], SIG['sigma_b'])
transport = {}
for gname in ORDER:
    if not table[gname]['sigma_b']['found']:
        transport[gname] = None
        continue
    _, Ag = solve_untwisted(reps[gname], SIG['sigma_b'])
    gA = [[sig_apply(A0[i][j], SIG[gname]) for j in range(3)] for i in range(3)]
    # Schur: both span the same K-line, so compare up to a scalar
    piv = next(((i, j) for i in range(3) for j in range(3) if not (gA[i][j] == zero)), None)
    scal = Ag[piv[0]][piv[1]] / gA[piv[0]][piv[1]]
    same = all(Ag[i][j] == scal * gA[i][j] for i in range(3) for j in range(3))
    transport[gname] = same
    print(f"   x_{gname:8s}: A_g == g(A) up to a K-scalar: {same}")
report['intertwiner_is_transported'] = transport
all_transported = all(v for v in transport.values() if v is not None)

print("\n=== VERDICT ===")
verdict = (
    "SURVIVES THE ORBIT: the untwisted GL(3,K) duality holds at EVERY point of the L6a4 "
    "class-1 variety, with the SAME sigma_b, and the intertwiner at each point is the "
    "Galois transport g(A) of the base one. Since the orbit IS the whole variety (degree 4, "
    "four distinct reduced points), this upgrades the representation-level statement from "
    "one point to the whole class -- the representation-level twin of the variety-level "
    "'exists sigma, for all x'. It is the predicted consequence of Gal(K/Q) being ABELIAN, "
    "which is exactly the hypothesis GaloisOrbitTransport.lean cannot drop."
    if (uniform and all_transported) else
    "PREDICTION NOT MET -- see the table; if sigma_b is not uniform the abelian transport "
    "argument does not apply here and the measurement must be re-examined")
report['verdict'] = verdict
print(verdict)

out = HERE / f'{NAME}-c{KCLS}-duality-orbit-untwisted.json'
out.write_text(json.dumps(report, indent=1) + "\n")
print(f"\nreport -> {out}")
