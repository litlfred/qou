#!/usr/bin/env python3
"""Does duality equal the sigma-transport ON REPRESENTATIONS?  A character test.  (qou-qjhc)

THE QUESTION THIS ANSWERS, AND WHY IT IS NOT THE PTOLEMY ONE.  Bean qou-qjhc asks whether
`rho -> rho^{-T}` INDUCES the sigma-transport.  Everything measured so far lives on the
Ptolemy variety: #7092 showed `D` and `sigma_b` agree modulo the decoration gauge at the
class-1 point, and ptolemy_duality_variety_level_orbit.py showed it at all four points of
that variety.  Carrying either across to REPRESENTATIONS needs the Ptolemy-to-
representation correspondence, which neither establishes.

This probe goes around that entirely.  It never mentions Ptolemy gauge, duality formulas
or coboundaries.  It compares CHARACTERS.

THE IDENTITY BEING TESTED.  Suppose `rho^{-T}` and `sigma(rho)` are isomorphic as PGL(3)
representations: there is `A` and scalars `lambda(w)` with
`A sigma(rho(w)) A^{-1} = lambda(w) rho(w)^{-T}`.  Take traces and determinants:

    traces:        sigma(chi(w))   = lambda(w) * chi(w^{-1})        [ chi_{rho^{-T}}(w) = chi(w^{-1}) ]
    determinants:  sigma(det(w))   = lambda(w)^3 / det(w)

Cube the first and substitute the second.  `lambda` cancels and, with
`det(w^{-1}) = 1/det(w)`:

    sigma( chi(w)^3 / det(w) )  ==  chi(w^{-1})^3 / det(w^{-1})       for EVERY word w.

Write `I(w) = chi(w)^3 / det(w)`.  The test is `sigma(I(w)) == I(w^{-1})`.

PGL, NOT SL -- and `I` is the reason.  A non-trivial obstruction class says exactly that
the representation does NOT lift to SL(3,C), so each matrix is defined only up to a
scalar and `chi(w)` alone is not an invariant: under `M -> mu*M`, `chi -> mu*chi` and
`det -> mu^3*det`, so `chi^3/det` is.  This is the same invariant
exact_character_selfduality.py uses, and for the same reason.

WHAT A RESULT MEANS -- the scope, stated before the run.

  * A single word with `sigma(I(w)) != I(w^{-1})` is a SOUND REFUTATION for that sigma:
    the identity above is NECESSARY, so one failure kills it.  Scope (a) in the repo's
    vocabulary: these two explicit maps differ on this representation.
  * Universal agreement over a word sweep is CORROBORATION, not proof.  It establishes
    the necessary condition on everything tested and nothing about untested words.  It is
    NOT upgraded to "isomorphic" here.  (Characters do determine an absolutely irreducible
    representation up to conjugacy -- and L6a4-c1-irreducibility.json records ABSOLUTELY
    IRREDUCIBLE by Burnside -- but that theorem is about the full character, not about a
    finite sample of it, and `I` is a cube, which loses a cube root of unity per word.)

So this probe can DECIDE a "no" and can only SUPPORT a "yes".  Both outcomes are useful
and the asymmetry is not hidden.

THE PREDICTION, WRITTEN DOWN BEFORE THE RUN.  Four automorphisms are tested and only one
should pass:

    id       FAIL   -- this is exactly the recorded self-duality test, and the corpus
                       verdict is COMPLEX TYPE (not self-dual): rho is NOT rho^{-T}.
                       So `id` failing is the REFUTATION CONTROL: it proves the test can
                       fail, and it calibrates `I` against L6a4-c1-character-selfduality.json
    tau      FAIL   -- tau fixes zeta_3, so tau(rho) sits at the SAME obstruction class,
                       while rho^{-T} sits at the NEGATED one; they cannot be isomorphic
    sigma_a  FAIL   -- predicted from the Ptolemy side, where sigma_a is not a coboundary
    sigma_b  PASS   -- the claim

A different pattern is the interesting outcome.  In particular `sigma_a` passing here
while failing the Ptolemy test would mean the two levels genuinely disagree, and that
would be a finding about the correspondence rather than about either map.

EXACTNESS.  Fraction and the NumberField only; no sympy expression arithmetic in the
inner loop (see numberfield.py -- the sympy version ran 17 minutes on one matrix
product).  No floats, no tolerances, no complex embedding: elements of K are compared by
equality.  NO FLOAT64 anywhere.
"""
import itertools
import json
import pathlib
import sys
from fractions import Fraction

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import exact_character_selfduality as base                       # noqa: E402
from exact_character_selfduality import Elt, trace, det3, poly_to_elt, _frac  # noqa: E402
from numberfield import NumberField                              # noqa: E402
import snappy                                                    # noqa: E402
from snappy.ptolemy.coordinates import PtolemyCoordinates        # noqa: E402

NAME, KCLS = 'L6a4', 1
MAXLEN = int(sys.argv[1]) if len(sys.argv) > 1 else 3
t = sp.Symbol('t')

# The two automorphisms, as polynomials in the generator, from
# ptolemy_class1_galois_group.py (hard-coded identically in the #7092 producer, where
# they are re-verified).  They are re-verified HERE too rather than trusted.
SIGMA_SRC = {
    'sigma_a': "-64*T**3/101015625 - T + 760000/1293",
    'sigma_b': "-T**3/625000 + 19*T**2/8000 - 1293*T/512 + 11875/8",
}

d = json.loads((HERE / f'{NAME}-c{KCLS}-ptolemy-in-K.json').read_text())
fe = sp.sympify(d['field']['min_poly'])
fp = sp.Poly(sp.expand(fe), t)
K = NumberField([_frac(c) for c in reversed(fp.all_coeffs())])
print(f"{NAME} c{KCLS}: K = Q[t]/({fe}), degree {K.deg}")

T = sp.Symbol('T')
SIG = {k: sp.sympify(v).subs(T, t) for k, v in SIGMA_SRC.items()}
SIG['tau'] = sp.expand(SIG['sigma_a'].subs(t, SIG['sigma_b']))
SIG['id'] = t
ORDER = ['id', 'tau', 'sigma_a', 'sigma_b']


def elt_to_expr(e):
    return sum(sp.Rational(c.numerator, c.denominator) * t ** i for i, c in enumerate(e.v))


def sig_apply(e, g):
    """Apply the automorphism t -> g(t) to an element of K, exactly, reducing mod f."""
    return poly_to_elt(K, sp.expand(elt_to_expr(e).subs(t, g)), t)


# ---------------------------------------------------------------- G1: the automorphisms
zero = Elt(K, K.zero())
for nm in ORDER:
    g = SIG[nm]
    assert poly_to_elt(K, sp.expand(fe.subs(t, g)), t) == zero, f"{nm}: f(sigma t) != 0"
# zeta_3 lives in K; locate it and check which automorphisms invert it
u = None
for cand in sp.roots(sp.Poly(sp.expand(t ** 2 + t + 1), t), t):
    pass
# zeta_3 as an element of K: solve x^2+x+1 = 0 inside K by using the recorded u
u_expr = sp.sympify(d['ptolemy']['u']) if 'u' in d.get('ptolemy', {}) else None
if u_expr is None and 'u' in d:
    u_expr = sp.sympify(d['u'])
assert u_expr is not None, "no cube root of unity recorded in the point file"
u = poly_to_elt(K, sp.expand(u_expr), t)
one = Elt(K, K.one())
assert (u * u + u + one) == zero, "recorded u is not a primitive cube root of unity"
inverts = {nm: (sig_apply(u, SIG[nm]) == u * u) for nm in ORDER}
print("G1 automorphisms of K verified; inverts zeta_3: "
      + ", ".join(f"{nm}={inverts[nm]}" for nm in ORDER))
assert inverts['sigma_a'] and inverts['sigma_b'], "sigma_a/sigma_b must invert zeta_3"
assert not inverts['id'] and not inverts['tau'], "id/tau must FIX zeta_3"

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
for r in G.relators():
    R = C.evaluate_word(r, G)
    off = [(i, j) for i in range(3) for j in range(3) if i != j and not (R[i][j] == 0)]
    assert not off and R[0][0] == R[1][1] and R[1][1] == R[2][2], \
        f"RELATOR GATE FAILED on {r}: these matrices are not a representation"
print(f"G2 relator gate: every relator maps to a scalar; generators {gens}")


def I_of(word):
    Mw = C.evaluate_word(word, G)
    ch, dt = trace(K, Mw), det3(K, Mw)
    return (ch * ch * ch) / dt


# ------------------------------------------------------------------------- the sweep
letters = [g for g in gens] + [g.upper() for g in gens]
seen = set()
fails = {nm: [] for nm in ORDER}
nwords = 0
for L in range(1, MAXLEN + 1):
    for tup in itertools.product(letters, repeat=L):
        w = ''.join(tup)
        if any(w[i].swapcase() == w[i + 1] for i in range(len(w) - 1)):
            continue
        if w in seen:
            continue
        seen.add(w)
        wi = ''.join(ch.swapcase() for ch in reversed(w))
        Iw, Ii = I_of(w), I_of(wi)
        nwords += 1
        for nm in ORDER:
            if not (sig_apply(Iw, SIG[nm]) == Ii):
                fails[nm].append(w)
    print(f"   length <= {L}: {len(seen)} reduced words; "
          + ", ".join(f"{nm} {len(fails[nm])} fail" for nm in ORDER), flush=True)

print(f"\n=== sigma(I(w)) == I(w^-1) over {nwords} reduced words, length <= {MAXLEN} ===")
report = {'probe': 'ptolemy_duality_is_sigma_on_characters', 'manifold': NAME,
          'obstruction_class': KCLS, 'max_word_length': MAXLEN, 'reduced_words': nwords,
          'invariant': 'I(w) = chi(w)^3/det(w); test sigma(I(w)) == I(w^-1)',
          'rows': {}}
for nm in ORDER:
    n = len(fails[nm])
    verdict = 'HOLDS on every word tested' if n == 0 else f'REFUTED ({n} witnesses)'
    print(f"   {nm:8s}: {verdict}"
          + (f"   shortest witness: {min(fails[nm], key=len)}" if n else ""))
    report['rows'][nm] = {'failing_words': n, 'verdict': verdict,
                          'shortest_witness': (min(fails[nm], key=len) if n else None)}

# --------------------------------------------------------------- controls and verdict
calib = len(fails['id']) > 0
print(f"\nG3 CALIBRATION / REFUTATION CONTROL -- `id` fails, i.e. rho is not self-dual,"
      f" reproducing L6a4-c1-character-selfduality.json's COMPLEX TYPE: {calib}")
report['G3_id_fails_reproducing_complex_type'] = calib
assert calib, "id passed: rho would be self-dual, contradicting the recorded verdict -- harness is wrong"

passing = [nm for nm in ORDER if not fails[nm]]
report['passing'] = passing
report['prediction_held'] = (passing == ['sigma_b'])
print(f"\nautomorphisms surviving: {passing}")
print(f"prediction (only sigma_b survives) held: {report['prediction_held']}")
report['verdict'] = (
    "sigma_b is the ONLY automorphism for which the necessary character identity holds; "
    "id, tau and sigma_a are each REFUTED by an explicit word. Corroborates "
    "rho^{-T} ~ sigma_b(rho) on every word tested; does NOT prove isomorphism."
    if report['prediction_held'] else
    f"UNEXPECTED PATTERN -- surviving: {passing}. See the table; this is the interesting case.")
print("\nVERDICT: " + report['verdict'])

# ------------------------------------------------------- STAGE 2: the intertwiner scalar
# Stage 1 tests the CUBED invariant, so it loses one cube root of unity per word.  The
# identity it comes from is finer: an isomorphism forces
#
#     sigma(chi(w)) = lambda(w) * chi(w^-1)
#
# with lambda a HOMOMORPHISM (both sides are homomorphisms up to scalar).  So compute
# lambda directly where chi(w^-1) is invertible and ask two things stage 1 cannot:
# does lambda take values in mu_3, and is it MULTIPLICATIVE?  A multiplicative lambda is
# the explicit projective intertwiner scalar -- much closer to an isomorphism than a
# cubed identity holding -- while a non-multiplicative one would refute sigma_b after
# stage 1 had passed it, which is exactly the check worth having.
if not fails['sigma_b']:
    g_b = SIG['sigma_b']
    lam, undefined = {}, 0
    for w in sorted(seen):
        wi = ''.join(ch.swapcase() for ch in reversed(w))
        Mw, Mi = C.evaluate_word(w, G), C.evaluate_word(wi, G)
        chi_w, chi_i = trace(K, Mw), trace(K, Mi)
        if chi_i == zero:
            undefined += 1
            continue
        lam[w] = sig_apply(chi_w, g_b) / chi_i
    in_mu3 = sum(1 for v in lam.values() if (v * v * v) == one)
    # multiplicativity on every concatenation of two tested words that is itself tested
    checked = bad = 0
    for v_ in sorted(lam):
        for w_ in sorted(lam):
            vw = v_ + w_
            if vw not in lam:
                continue
            if any(vw[i].swapcase() == vw[i + 1] for i in range(len(vw) - 1)):
                continue
            checked += 1
            if not (lam[vw] == lam[v_] * lam[w_]):
                bad += 1
    print(f"\nSTAGE 2 -- the intertwiner scalar lambda(w) = sigma_b(chi(w))/chi(w^-1)")
    print(f"   defined on {len(lam)} of {len(seen)} words ({undefined} had chi(w^-1) = 0)")
    print(f"   lambda(w)^3 == 1 (values in mu_3): {in_mu3} of {len(lam)}")
    print(f"   multiplicative lambda(vw) = lambda(v)lambda(w): "
          f"{checked - bad} of {checked} concatenations hold")
    report['stage2_intertwiner_scalar'] = {
        'defined_on': len(lam), 'of_words': len(seen), 'chi_inv_zero': undefined,
        'values_in_mu3': in_mu3, 'multiplicativity_checked': checked,
        'multiplicativity_failures': bad,
        'distinct_values': len({repr(v) for v in lam.values()})}
    if bad == 0 and in_mu3 == len(lam):
        print("   -> lambda is a mu_3-valued HOMOMORPHISM on everything tested: the explicit"
              "\n      projective intertwiner scalar exists, which is what stage 1's cube hid.")

out = HERE / f'{NAME}-c{KCLS}-duality-sigma-characters.json'
out.write_text(json.dumps(report, indent=1) + "\n")
print(f"\nreport -> {out}")
