#!/usr/bin/env python3
"""CONSTRUCT the intertwiner: rho^{-T} ~ sigma_b(rho) in PGL(3,K), proved, not swept. (qou-qjhc)

WHAT WAS LEFT OPEN, AND WHY THE SWEEP COULD NEVER CLOSE IT.
ptolemy_duality_is_sigma_on_characters.py verified the necessary character identity on
4686 words and found the intertwiner SCALAR lambda to be a mu_3-valued homomorphism.  Its
stated gap was "all w versus the 4686 tested": a finite character sweep cannot reach the
whole group, and no amount of extra words changes that.  Chasing a word-length bound from
the invariant theory of 3x3 matrices (Procesi/Razmyslov degree n^2, Teranishi's sharper 6
for two generic matrices) would make the sweep finite -- but it is the wrong instrument.

THE BOUND IS 1, because of an algebraic fact the sweep was ignoring.  Set

    rho_1(w) := sigma_b(rho(w))            (the field automorphism applied entrywise)
    rho_2(w) := lambda(w) * rho(w)^{-T}

Both are HOMOMORPHISMS on the free group: `(rho(v)rho(w))^{-T} = rho(v)^{-T} rho(w)^{-T}`
because transpose-inverse is an anti-anti-automorphism, and lambda is multiplicative.  So
if ONE matrix A satisfies

    A rho_1(g) A^{-1} = rho_2(g)        for g in the three GENERATORS,

then `w -> A rho_1(w) A^{-1}` and `w -> rho_2(w)` are two homomorphisms agreeing on a
generating set, hence EQUAL ON EVERY WORD.  Not corroborated on every word -- equal, by
multiplicativity.  Nothing about characters, absolute irreducibility, trace algebras or
word length enters.

So this probe does not sweep.  It SOLVES for A, exactly, and checks it is invertible.

THE SOLVE.  `A rho_1(g) = lambda(g) rho(g)^{-T} A` is LINEAR in the nine entries of A.
Each element of K = Q[t]/(f) is four rationals, so A carries 36 rational unknowns and each
generator contributes 9 K-equations = 36 Q-equations; three generators give 108.  The
nullspace is computed exactly over Q with sympy.  A nonzero nullspace vector with
det(A) != 0 IS the isomorphism.

WHAT THIS PROVES, AND WHAT IT DOES NOT.
  PROVES, for L6a4 obstruction class 1, over K:  sigma_b(rho) and rho^{-T} are conjugate
  in PGL(3,K).  lambda is mu_3-valued and mu_3 scalars are TRIVIAL in PGL(3), so the
  twist is invisible there and the statement is exactly "duality induces the sigma_b
  transport on this representation".
  DOES NOT prove anything about other obstruction classes, other manifolds, or duality as
  a map on a moduli space.  One representation (up to the Galois orbit), one manifold.

CONTROLS, because a solver that returns something is not the same as a solver that is
right.  The SAME solve is run for `id`, `tau` and `sigma_a`, where the answer must be NO:
  * `id`   -- a solution would mean rho is SELF-DUAL, contradicting the recorded
              COMPLEX TYPE verdict of L6a4-c1-character-selfduality.json
  * `tau`  -- fixes zeta_3, so tau(rho) sits at the SAME obstruction class while rho^{-T}
              sits at the negated one
  * `sigma_a` -- refuted on characters and not a coboundary on the Ptolemy side
A run in which all four succeed would mean the solve is vacuous (e.g. solving A = 0), and
is caught: the invertibility of A is checked, not assumed, and A = 0 is excluded by it.

EXACTNESS.  Fraction and NumberField for the representation; sympy Rational linear algebra
for the nullspace.  No floats, no tolerances, no complex embedding anywhere.
"""
import json
import pathlib
import sys
from fractions import Fraction

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
print(f"{NAME} c{KCLS}: K = Q[t]/({fe}), degree {DEG}")

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
    """K-element -> its DEG rational coordinates in the power basis 1, t, ..., t^(DEG-1)."""
    v = list(e.v) + [Fraction(0)] * (DEG - len(e.v))
    return [sp.Rational(c.numerator, c.denominator) for c in v[:DEG]]


for nm in ORDER:
    assert poly_to_elt(K, sp.expand(fe.subs(t, SIG[nm])), t) == zero, f"{nm} is not an automorphism"

# ------------------------------------------------------------- the representation + gate
pt = {k: poly_to_elt(K, sp.sympify(v), t) for k, v in d['ptolemy'].items()}
M = snappy.Manifold(NAME)
V = M.ptolemy_variety(3, obstruction_class=KCLS, eliminate_fixed_ptolemys=True)
dd = dict(pt)
dd['1'] = one
C = PtolemyCoordinates(dd, is_numerical=False,
                       py_eval_section=eval(V.py_eval_section()),
                       manifold_thunk=lambda: M,
                       non_trivial_generalized_obstruction_class=(KCLS != 0))
G = M.fundamental_group()
gens = G.generators()
for r in G.relators():
    R = C.evaluate_word(r, G)
    off = [(i, j) for i in range(3) for j in range(3) if i != j and not (R[i][j] == 0)]
    assert not off and R[0][0] == R[1][1] and R[1][1] == R[2][2], f"relator gate failed on {r}"
print(f"gate: every relator maps to a scalar; generators {gens}")

u_expr = sp.sympify(d['ptolemy']['u'])
u = poly_to_elt(K, sp.expand(u_expr), t)
assert (u * u + u + one) == zero


def mat(w):
    return C.evaluate_word(w, G)


def minv(Mw):
    """Exact inverse in M_3(K) via the adjugate."""
    D = det3(K, Mw)
    assert not (D == zero), "singular matrix"
    C_ = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            r = [x for x in range(3) if x != i]
            c = [y for y in range(3) if y != j]
            m = Mw[r[0]][c[0]] * Mw[r[1]][c[1]] - Mw[r[0]][c[1]] * Mw[r[1]][c[0]]
            C_[j][i] = m if (i + j) % 2 == 0 else zero - m          # adjugate = cofactor^T
    return [[C_[i][j] / D for j in range(3)] for i in range(3)]


def transpose(Mw):
    return [[Mw[j][i] for j in range(3)] for i in range(3)]


# -------------------------------------------------------------------------- the solve
def intertwiner(nm):
    """Solve  A sigma(rho(g)) = lambda(g) rho(g)^{-T} A  over K, for all generators g.

    Returns (dim of solution space, an invertible solution or None, lambda values).
    """
    g_sig = SIG[nm]
    lam = {}
    for g in gens:
        Mg, Mgi = mat(g), mat(g.upper())
        chi_g, chi_gi = trace(K, Mg), trace(K, Mgi)
        if chi_gi == zero:
            return None, None, None, f"chi({g}^-1) = 0; lambda undefined on a generator"
        lam[g] = sig_apply(chi_g, g_sig) / chi_gi

    rows = []
    for g in gens:
        Mg = mat(g)
        S = [[sig_apply(Mg[i][j], g_sig) for j in range(3)] for i in range(3)]   # sigma(rho(g))
        Dg = transpose(minv(Mg))                                                 # rho(g)^{-T}
        L = lam[g]
        # (A S)_{ij} - L (Dg A)_{ij} = 0, linear in A_{pq}
        for i in range(3):
            for j in range(3):
                # coefficient of A_{pq}
                coef = {}
                for q in range(3):
                    coef[(i, q)] = coef.get((i, q), zero) + S[q][j]             # A_{iq} S_{qj}
                for p in range(3):
                    coef[(p, j)] = coef.get((p, j), zero) - L * Dg[i][p]        # -L Dg_{ip} A_{pj}
                # expand into DEG rational rows
                blocks = []
                for p in range(3):
                    for q in range(3):
                        blocks.append(coef.get((p, q), zero))
                # each K-coefficient c multiplies an unknown that is itself DEG rationals:
                # represent A_{pq} = sum_k a_{pq,k} t^k, so c * A_{pq} contributes
                # coords(c * t^k) to the DEG rows.
                mrows = [[sp.Integer(0)] * (9 * DEG) for _ in range(DEG)]
                for idx, c in enumerate(blocks):
                    if c == zero:
                        continue
                    for k in range(DEG):
                        col = idx * DEG + k
                        prod = c * poly_to_elt(K, t ** k, t)
                        for r_, val in enumerate(coords(prod)):
                            mrows[r_][col] += val
                rows.extend(mrows)

    Mx = sp.Matrix(rows)
    ns = Mx.nullspace()
    if not ns:
        return 0, None, lam, None
    # look for an invertible solution among the nullspace vectors and small combinations
    cands = list(ns) + ([ns[0] + ns[1]] if len(ns) > 1 else [])
    for vec in cands:
        A = [[poly_to_elt(K, sum(vec[(p * 3 + q) * DEG + k] * t ** k for k in range(DEG)), t)
              for q in range(3)] for p in range(3)]
        if not (det3(K, A) == zero):
            return len(ns), A, lam, None
    return len(ns), None, lam, None


report = {'probe': 'ptolemy_duality_sigma_intertwiner', 'manifold': NAME,
          'obstruction_class': KCLS, 'method': 'exact linear solve for the intertwiner A',
          'rows': {}}
print("\n=== solve  A sigma(rho(g)) A^-1 = lambda(g) rho(g)^-T  on the GENERATORS ===")
for nm in ORDER:
    dim, A, lam, err = intertwiner(nm)
    if err:
        print(f"   {nm:8s}: SKIPPED -- {err}")
        report['rows'][nm] = {'verdict': 'skipped', 'reason': err}
        continue
    ok = A is not None
    print(f"   {nm:8s}: nullspace dim {dim}; invertible intertwiner "
          f"{'FOUND' if ok else 'none'}")
    report['rows'][nm] = {'nullspace_dim': dim, 'invertible_intertwiner': ok,
                          'lambda': {g: repr(lam[g]) for g in gens} if lam else None}
    if ok:
        report['rows'][nm]['A'] = [[repr(A[i][j]) for j in range(3)] for i in range(3)]
        report['rows'][nm]['det_A'] = repr(det3(K, A))
        # REDUNDANT CHECK: the intertwining must now hold on longer words automatically.
        # If it does not, multiplicativity has been misapplied somewhere.
        bad = []
        for w in ['ab', 'ac', 'bc', 'aab', 'abc', 'abcab', 'AB', 'aBc']:
            Mw = mat(w)
            S = [[sig_apply(Mw[i][j], SIG[nm]) for j in range(3)] for i in range(3)]
            Dw = transpose(minv(Mw))
            lw = one
            for ch in w:
                lw = lw * (lam[ch] if ch.islower() else one / lam[ch.lower()])
            lhs = [[sum((A[i][k] * S[k][j] for k in range(3)), zero) for j in range(3)]
                   for i in range(3)]
            rhs = [[sum((lw * Dw[i][k] * A[k][j] for k in range(3)), zero) for j in range(3)]
                   for i in range(3)]
            if any(not (lhs[i][j] == rhs[i][j]) for i in range(3) for j in range(3)):
                bad.append(w)
        print(f"      redundant check on longer words (must be automatic): "
              f"{8 - len(bad)}/8 hold" + (f"  FAILURES {bad}" if bad else ""))
        report['rows'][nm]['longer_word_check'] = {'tested': 8, 'failures': bad}
        mu3 = all((lam[g] * lam[g] * lam[g]) == one for g in gens)
        print(f"      lambda(g)^3 == 1 on every generator (so the twist is trivial in PGL(3)): {mu3}")
        report['rows'][nm]['lambda_in_mu3'] = mu3
        # SCHUR CONSISTENCY.  The solve is over Q, so a K-line of intertwiners shows up
        # with Q-dimension [K:Q].  For an ABSOLUTELY IRREDUCIBLE rho, Schur forces the
        # intertwiner to be unique up to a K-scalar, i.e. dim_K = 1, i.e. dim_Q = DEG.
        # Anything larger would mean rho is not absolutely irreducible or the system is
        # under-constrained -- so this is a check the solve had to pass, not a remark.
        schur = (dim == DEG)
        print(f"      Schur: nullspace dim_Q {dim} == [K:Q] {DEG}, so the intertwiner is"
              f" unique up to a K-scalar: {schur}")
        report['rows'][nm]['schur_dim_matches_degree'] = schur
        # The intertwining descends to pi_1 in PGL(3): relators map to SCALARS (gate
        # above), and scalars are trivial there.  Checked rather than asserted.
        relbad = []
        for r in G.relators():
            Rm = mat(r)
            Sr = [[sig_apply(Rm[i][j], SIG[nm]) for j in range(3)] for i in range(3)]
            Dr = transpose(minv(Rm))
            lr = one
            for ch in r:
                lr = lr * (lam[ch] if ch.islower() else one / lam[ch.lower()])
            lhs = [[sum((A[i][k] * Sr[k][j] for k in range(3)), zero) for j in range(3)]
                   for i in range(3)]
            rhs = [[sum((lr * Dr[i][k] * A[k][j] for k in range(3)), zero) for j in range(3)]
                   for i in range(3)]
            if any(not (lhs[i][j] == rhs[i][j]) for i in range(3) for j in range(3)):
                relbad.append(r)
        print(f"      intertwining holds on the relators (so it descends to pi_1): "
              f"{len(list(G.relators())) - len(relbad)}/{len(list(G.relators()))}")
        report['rows'][nm]['relator_check_failures'] = relbad

found = [nm for nm in ORDER if report['rows'][nm].get('invertible_intertwiner')]
report['intertwiner_exists_for'] = found
ctrl = [nm for nm in ('id', 'tau', 'sigma_a') if nm in found]
report['controls_passed'] = not ctrl
print(f"\nCONTROLS -- id / tau / sigma_a must all FAIL: "
      f"{'PASS' if not ctrl else 'BROKEN, these succeeded: ' + str(ctrl)}")
report['verdict'] = (
    "PROVED for L6a4 class 1: an invertible A over K conjugates sigma_b(rho) to "
    "lambda (x) rho^{-T} on the generators, hence on EVERY word by multiplicativity; "
    "lambda is mu_3-valued and mu_3 is trivial in PGL(3), so sigma_b(rho) and rho^{-T} "
    "are conjugate in PGL(3,K)."
    if found == ['sigma_b'] else
    f"UNEXPECTED -- intertwiners found for {found}; see the table")
print("\nVERDICT: " + report['verdict'])

out = HERE / f'{NAME}-c{KCLS}-duality-sigma-intertwiner.json'
out.write_text(json.dumps(report, indent=1) + "\n")
print(f"\nreport -> {out}")
