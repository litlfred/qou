#!/usr/bin/env python3
"""Is the mu_3 twist lambda CANONICAL, or an artifact of the decoration? (qou-qjhc)

ptolemy_duality_sigma_intertwiner.py PROVED, for L6a4 class 1, that an invertible A over K
satisfies  A sigma_b(rho(g)) A^{-1} = lambda(g) rho(g)^{-T}  on the generators, hence on
every word, with lambda valued in mu_3.  In PGL(3) the mu_3 scalars vanish, so that proof
does not care what lambda is.  The question left open is whether lambda MEANS anything:
is its class forced by the duality, or is it bookkeeping that a different choice of
decoration would wash out?

THE THREE CHOICES, AND WHICH ONE CAN MOVE LAMBDA.

  (i) THE INTERTWINER A.  Schur gives dim_K = 1 (measured: nullspace dim_Q 4 = [K:Q]), so A
      is unique up to a K-scalar, and a scalar cancels between A and A^{-1}.  lambda cannot
      depend on A.
  (ii) CONJUGATING rho by B in GL(3,K).  Take A' = B^{-T} A sigma_b(B)^{-1}; then
      A' sigma_b(BrhoB^{-1}) A'^{-1} = B^{-T}(A sigma_b(rho) A^{-1})B^{T}
                                     = lambda . (BrhoB^{-1})^{-T},
      with the SAME lambda.  Conjugation cannot move it either.
  (iii) THE LIFT.  rho is a matrix representation; the PGL(3) representation determines it
      only up to rho -> mu.rho for a homomorphism mu : F -> K*.  Then
      sigma_b(rho') = sigma_b(mu).sigma_b(rho) and rho'^{-T} = mu^{-1}.rho^{-T}, so

          lambda'(g) = lambda(g) . mu(g) . sigma_b(mu(g))        (*)

      THIS is the only freedom.  So lambda is canonical exactly when it is nontrivial in the
      cokernel of the twisted-norm map  N_b(mu) := mu . sigma_b(mu).

THE ARGUMENT, which the measurements below either establish or refute.

  If sigma_b is an INVOLUTION then N_b(m) = m.sigma_b(m) is sigma_b-FIXED:
      sigma_b(N_b(m)) = sigma_b(m).sigma_b^2(m) = sigma_b(m).m = N_b(m).
  So the entire image of N_b lies in the fixed field F_b = K^{sigma_b}.  If additionally
  sigma_b does NOT fix zeta_3 -- i.e. sigma_b(zeta_3) = zeta_3^2, which is exactly the
  condition that sigma_b NEGATES the obstruction class, the reason sigma_b is the
  automorphism that works at all -- then zeta_3 is not in F_b, hence

      zeta_3 is NOT in the image of N_b.

  A lambda taking a primitive cube root on some generator is then NOT a coboundary: no
  redecoration of any kind produces it or removes it.  THE CLASS IS CANONICAL.

  And under the SL(3) normalisation the rigidity is sharper still.  If the lift is required
  to have det 1 then mu(g)^3 = 1 pointwise, so mu is mu_3-valued, and
      N_b(mu) = mu . sigma_b(mu) = mu . mu^2 = mu^3 = 1
  IDENTICALLY.  lambda is then rigid POINTWISE, not merely rigid as a class.

WHAT IS MEASURED HERE (nothing above is assumed):
  1. the Galois group's multiplication table -- is sigma_b an involution?
  2. sigma(zeta_3) for all four automorphisms -- does sigma_b negate the obstruction class?
  3. det rho(g) -- is the lift SL(3), so that (*) is restricted to mu_3?
  4. lambda(a), lambda(b), lambda(c) as explicit powers of zeta_3 -- is lambda nontrivial
     at all?  MEASURED ANSWER: lambda == 1.  That does NOT make the question moot, because
     the rigidity analysis then says something stronger about the triviality itself; see
     the verdict block.
  5. whether lambda DESCENDS to pi_1: lambda(relator) must be 1, or lambda is a class on the
     free group only and "class in Hom(pi_1, mu_3)" is not a statement that type-checks.
  6. the transformation law (*) itself, by RE-SOLVING the intertwiner for a rescaled rho'
     rather than trusting the algebra -- with a deliberately WRONG lambda'' as the control,
     which must admit no invertible intertwiner.

Exact throughout: Fraction and NumberField, sympy Rational linear algebra.  No floats.
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


def sig_reduced(g):
    """Canonical form of an automorphism polynomial: reduce t -> g(t) modulo f."""
    return elt_to_expr(poly_to_elt(K, sp.expand(g), t))


def sig_name(g):
    r = sp.expand(sig_reduced(g))
    for nm in ORDER:
        if sp.expand(r - sig_reduced(SIG[nm])) == 0:
            return nm
    return '??'


for nm in ORDER:
    assert poly_to_elt(K, sp.expand(fe.subs(t, SIG[nm])), t) == zero, f"{nm} is not an automorphism"

report = {'probe': 'ptolemy_duality_lambda_class_rigidity', 'manifold': NAME,
          'obstruction_class': KCLS,
          'question': 'is the mu_3 twist lambda canonical, or an artifact of the decoration'}

# ----------------------------------------------------------------- 1. the Galois group
print("=== 1. Galois group multiplication table (sigma . sigma') ===")
table = {}
for x in ORDER:
    row = {}
    for y in ORDER:
        # (x after y) corresponds to substituting t -> x(t) into y's polynomial
        row[y] = sig_name(sp.expand(SIG[y].subs(t, SIG[x])))
    table[x] = row
    print(f"   {x:8s}: " + "  ".join(f"{y}->{row[y]}" for y in ORDER))
orders = {nm: (1 if nm == 'id' else (2 if table[nm][nm] == 'id' else 4)) for nm in ORDER}
sb_involution = (table['sigma_b']['sigma_b'] == 'id')
klein = all(table[nm][nm] == 'id' for nm in ORDER)
print(f"\n   element orders: {orders}")
print(f"   group is Klein four (every element an involution): {klein}")
print(f"   *** sigma_b is an INVOLUTION: {sb_involution} ***"
      f"   <- needed for N_b to land in the fixed field")
report['galois'] = {'table': table, 'orders': orders, 'klein_four': klein,
                    'sigma_b_is_involution': sb_involution}

# ------------------------------------------------------- 2. the action on zeta_3
u = poly_to_elt(K, sp.expand(sp.sympify(d['ptolemy']['u'])), t)
assert (u * u + u + one) == zero, "u is not a primitive cube root of unity"
u2 = u * u
print("\n=== 2. action on zeta_3 (u, with u^2+u+1 = 0) ===")
zact = {}
for nm in ORDER:
    su = sig_apply(u, SIG[nm])
    lab = 'u' if su == u else ('u^2 = -1-u' if su == u2 else '??')
    zact[nm] = lab
    print(f"   {nm:8s}(u) = {lab}")
sb_negates = (zact['sigma_b'] == 'u^2 = -1-u')
print(f"\n   *** sigma_b NEGATES the obstruction class (sigma_b(u) = u^2): {sb_negates} ***")
print(f"       so zeta_3 is NOT in the fixed field K^sigma_b: {sb_negates}")
report['zeta3_action'] = zact
report['sigma_b_negates_obstruction_class'] = sb_negates

# ------------------------------------------------------------ the representation + gate
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
rels = list(G.relators())
for r in rels:
    R = C.evaluate_word(r, G)
    off = [(i, j) for i in range(3) for j in range(3) if i != j and not (R[i][j] == 0)]
    assert not off and R[0][0] == R[1][1] and R[1][1] == R[2][2], f"relator gate failed on {r}"
print(f"\ngate: every relator maps to a scalar; generators {gens}, relators {rels}")


def mat(w):
    return C.evaluate_word(w, G)


def minv(Mw):
    D = det3(K, Mw)
    assert not (D == zero), "singular matrix"
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


# --------------------------------------------------------------- 3. is the lift SL(3)?
print("\n=== 3. det rho(g): is the lift SL(3), so that (*) is restricted to mu_3? ===")
dets = {}
for g in gens:
    D = det3(K, mat(g))
    lab = '1' if D == one else ('u' if D == u else ('u^2' if D == u2 else repr(D)))
    dets[g] = lab
    print(f"   det rho({g}) = {lab}")
cube = {g: det3(K, mat(g)) ** 3 if False else None for g in gens}
det_cubes_one = all((det3(K, mat(g)) * det3(K, mat(g)) * det3(K, mat(g))) == one for g in gens)
sl3 = all(dets[g] == '1' for g in gens)
print(f"   lift is SL(3) (all dets 1): {sl3}")
print(f"   all dets are cube roots of unity: {det_cubes_one}")
report['det_rho'] = dets
report['lift_is_SL3'] = sl3
report['dets_are_cube_roots_of_unity'] = det_cubes_one

# ------------------------------------------------------------------- 4/5. lambda itself
lam = {}
for g in gens:
    chi_g, chi_gi = trace(K, mat(g)), trace(K, mat(g.upper()))
    assert not (chi_gi == zero), f"chi({g}^-1) = 0"
    lam[g] = sig_apply(chi_g, SIG['sigma_b']) / chi_gi


def as_power_of_u(e):
    if e == one:
        return 0
    if e == u:
        return 1
    if e == u2:
        return 2
    return None


print("\n=== 4. lambda on the generators, as powers of zeta_3 ===")
lam_pow = {}
for g in gens:
    k = as_power_of_u(lam[g])
    lam_pow[g] = k
    print(f"   lambda({g}) = u^{k}" if k is not None else f"   lambda({g}) = {lam[g]}  NOT in mu_3")
nontrivial = any(k not in (0, None) for k in lam_pow.values())
print(f"\n   *** lambda is NONTRIVIAL (not identically 1): {nontrivial} ***")
if not nontrivial:
    print("       -> the class question is MOOT; lambda is the trivial homomorphism")
report['lambda_powers_of_zeta3'] = lam_pow
report['lambda_nontrivial'] = nontrivial


def lam_word(w):
    out = one
    for ch in w:
        out = out * (lam[ch] if ch.islower() else one / lam[ch.lower()])
    return out


print("\n=== 5. does lambda DESCEND to pi_1?  lambda(relator) must be 1 ===")
rel_lam = {}
for r in rels:
    lr = lam_word(r)
    k = as_power_of_u(lr)
    rel_lam[r] = k
    print(f"   lambda({r}) = u^{k}")
descends = all(k == 0 for k in rel_lam.values())
print(f"\n   *** lambda descends to pi_1 (trivial on every relator): {descends} ***")
if not descends:
    print("       -> lambda is a homomorphism on the FREE group only; 'class in Hom(pi_1, mu_3)'")
    print("          would not type-check, and must not be claimed")
report['lambda_on_relators'] = rel_lam
report['lambda_descends_to_pi1'] = descends

# ---------------------------------------------- the intertwiner solver (reused verbatim)
def coords(e):
    v = list(e.v) + [_frac(0)] * (DEG - len(e.v))
    return [sp.Rational(c.numerator, c.denominator) for c in v[:DEG]]


def solve_intertwiner(rho_gen, lam_gen, g_sig):
    """Solve  A sigma(rho(g)) = lam(g) rho(g)^{-T} A  over K, exactly, for all generators."""
    rows = []
    for g in gens:
        Mg = rho_gen[g]
        S = [[sig_apply(Mg[i][j], g_sig) for j in range(3)] for i in range(3)]
        Dg = transpose(minv(Mg))
        L = lam_gen[g]
        for i in range(3):
            for j in range(3):
                coef = {}
                for q_ in range(3):
                    coef[(i, q_)] = coef.get((i, q_), zero) + S[q_][j]
                for p_ in range(3):
                    coef[(p_, j)] = coef.get((p_, j), zero) - L * Dg[i][p_]
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


# ------------------------------- 6. the transformation law (*), MEASURED not assumed
print("\n=== 6. the transformation law  lambda' = lambda . mu . sigma_b(mu),")
print("       MEASURED by re-solving the intertwiner for a rescaled rho' ===")
rho0 = {g: mat(g) for g in gens}
dim0, A0 = solve_intertwiner(rho0, lam, SIG['sigma_b'])
print(f"   baseline (mu = 1): nullspace dim {dim0}, invertible A {'FOUND' if A0 else 'none'}")

MUS = [
    ('mu in mu_3   (a->u, b->1, c->u^2)', {gens[0]: u, gens[1]: one, gens[2]: u2}),
    ('mu rational  (a->2, b->3, c->1)', {gens[0]: poly_to_elt(K, sp.Integer(2), t),
                                         gens[1]: poly_to_elt(K, sp.Integer(3), t),
                                         gens[2]: one}),
    ('mu generic   (a->t, b->1, c->1)', {gens[0]: poly_to_elt(K, t, t),
                                         gens[1]: one, gens[2]: one}),
]
law_rows = []
for label, mu in MUS:
    rho1 = {g: [[mu[g] * rho0[g][i][j] for j in range(3)] for i in range(3)] for g in gens}
    pred = {g: lam[g] * mu[g] * sig_apply(mu[g], SIG['sigma_b']) for g in gens}
    dim_p, A_p = solve_intertwiner(rho1, pred, SIG['sigma_b'])
    # CONTROL: the same rescaled rho' against a deliberately WRONG lambda'' (predicted * u)
    wrong = {g: pred[g] * u for g in gens}
    dim_w, A_w = solve_intertwiner(rho1, wrong, SIG['sigma_b'])
    ok = (A_p is not None) and (A_w is None)
    unchanged = all(pred[g] == lam[g] for g in gens)
    print(f"   {label}")
    print(f"      predicted lambda' : nullspace dim {dim_p}, invertible A "
          f"{'FOUND' if A_p else 'none'}")
    print(f"      CONTROL (lambda'.u): nullspace dim {dim_w}, invertible A "
          f"{'FOUND -- BROKEN' if A_w else 'none (correct)'}")
    print(f"      law holds: {ok}    lambda' == lambda (unchanged): {unchanged}")
    law_rows.append({'mu': label, 'predicted_dim': dim_p, 'predicted_ok': A_p is not None,
                     'control_dim': dim_w, 'control_rejected': A_w is None,
                     'law_holds': ok, 'lambda_unchanged': unchanged})
report['transformation_law'] = law_rows
law_ok = all(r['law_holds'] for r in law_rows)
print(f"\n   *** transformation law (*) verified on every mu tested: {law_ok} ***")
report['transformation_law_verified'] = law_ok

# ------------------- 6b. SL(3) FORCES lambda into mu_3; and the GL(3) statement
print("\n=== 6b. the SL(3) normalisation FORCES lambda(g)^3 = 1 (determinants of both")
print("        sides of the intertwining), and lambda = 1 then lifts the theorem to GL(3) ===")
forced = []
for g in gens:
    Mg = rho0[g]
    lhs = det3(K, [[sig_apply(Mg[i][j], SIG['sigma_b']) for j in range(3)] for i in range(3)])
    rhs = det3(K, transpose(minv(Mg)))
    # det(lam . rho^-T) = lam^3 . det(rho^-T);  det(A X A^-1) = det X
    cube = lam[g] * lam[g] * lam[g]
    forced.append(bool((lhs == cube * rhs)))
    print(f"   {g}: det sigma_b(rho) = {'lambda^3 . det rho^-T' if forced[-1] else 'MISMATCH'}")
det_forcing = all(forced)
print(f"   *** lambda^3 = 1 is FORCED by det, not observed by luck: {det_forcing} ***")
report['mu3_forced_by_determinant'] = det_forcing

# With lambda == 1 the intertwining is an equality of GL(3) representations.  Re-solve with
# lambda identically 1 and check it on words, so the GL(3) claim is measured, not inferred.
lam_one = {g: one for g in gens}
dim1, A1 = solve_intertwiner(rho0, lam_one, SIG['sigma_b'])
print(f"   re-solve with lambda == 1 identically: nullspace dim {dim1}, invertible A "
      f"{'FOUND' if A1 else 'none'}")
gl3_words = []
if A1 is not None:
    for w in ['a', 'b', 'c', 'ab', 'abc', 'aBc', 'abcab', 'AB', 'aabbcc']:
        Mw = mat(w)
        S = [[sig_apply(Mw[i][j], SIG['sigma_b']) for j in range(3)] for i in range(3)]
        Dw = transpose(minv(Mw))
        lhs = [[sum((A1[i][k] * S[k][j] for k in range(3)), zero) for j in range(3)]
               for i in range(3)]
        rhs = [[sum((Dw[i][k] * A1[k][j] for k in range(3)), zero) for j in range(3)]
               for i in range(3)]
        gl3_words.append(all(lhs[i][j] == rhs[i][j] for i in range(3) for j in range(3)))
gl3 = (A1 is not None) and all(gl3_words)
print(f"   A sigma_b(rho(w)) A^-1 = rho(w)^-T  EXACTLY (no scalar) on {len(gl3_words)} words: "
      f"{all(gl3_words) if gl3_words else False}")
print(f"   *** the intertwining holds in GL(3,K), not merely PGL(3,K): {gl3} ***")
report['untwisted_in_GL3'] = gl3
report['untwisted_words_checked'] = len(gl3_words)

# -------------------------------------------------------------------- 7. the verdict
print("\n=== 7. VERDICT ===")
coboundaries_in_fixed_field = sb_involution
zeta3_not_a_coboundary = sb_involution and sb_negates
mu3_lifts_give_nothing = sb_negates       # N_b(mu) = mu.mu^2 = 1 for mu in mu_3
print(f"   N_b(m) = m.sigma_b(m) lands in the fixed field K^sigma_b: "
      f"{coboundaries_in_fixed_field}  (needs sigma_b^2 = id)")
print(f"   zeta_3 is not in K^sigma_b, hence not in the image of N_b: {zeta3_not_a_coboundary}")
print(f"   under an SL(3)/mu_3-restricted lift, N_b(mu) = mu.mu^2 = 1 identically: "
      f"{mu3_lifts_give_nothing}")
# lambda == 1 is RIGID, not merely trivial: under the SL(3) normalisation every
# redecoration has mu in mu_3, and N_b(mu) = mu.sigma_b(mu) = mu.mu^2 = 1 IDENTICALLY,
# so lambda' = lambda for EVERY admissible mu.  The untwistedness is a property of the
# representation, not of the decoration that was chosen.
trivial_and_rigid = bool((not nontrivial) and sl3 and mu3_lifts_give_nothing and law_ok)
canonical = bool(nontrivial and zeta3_not_a_coboundary and law_ok)
report['coboundaries_land_in_fixed_field'] = coboundaries_in_fixed_field
report['zeta3_not_a_coboundary'] = zeta3_not_a_coboundary
report['mu3_lift_gives_trivial_coboundary'] = mu3_lifts_give_nothing
report['lambda_class_is_canonical'] = canonical
report['lambda_trivial_and_rigid'] = trivial_and_rigid
report['verdict'] = (
    "UNTWISTED AND RIGID: lambda == 1 on every generator, so the intertwining is "
    "A sigma_b(rho(w)) A^-1 = rho(w)^-T EXACTLY -- an equality of GL(3,K) representations, "
    "strictly stronger than the PGL(3,K) statement. And the triviality is FORCED, not "
    "chosen: the lift is SL(3), so det forces lambda(g)^3 = 1, and any redecoration "
    "preserving SL(3) has mu in mu_3, where N_b(mu) = mu.sigma_b(mu) = mu.mu^2 = 1 "
    "IDENTICALLY because sigma_b(zeta_3) = zeta_3^2. So lambda' = lambda for EVERY "
    "admissible mu: no decoration could have made the twist nontrivial. The mu_3 twist "
    "does not merely vanish in PGL(3) -- it is absent."
    if trivial_and_rigid else
    ("CANONICAL: lambda is nontrivial and no choice of lift produces or removes it."
     if canonical else
     "NOT ESTABLISHED -- see the rows above for which hypothesis failed"))
print("\n" + report['verdict'])

out = HERE / f'{NAME}-c{KCLS}-duality-lambda-class-rigidity.json'
out.write_text(json.dumps(report, indent=1) + "\n")
print(f"\nreport -> {out}")
