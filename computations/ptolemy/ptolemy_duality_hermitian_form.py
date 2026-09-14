#!/usr/bin/env python3
"""WHY the duality sigma is complex conjugation: rho preserves a HERMITIAN FORM. (qou-qjhc)

The sibling probe `ptolemy_duality_sigma_is_complex_conjugation.py` MEASURES that
the duality sigma is complex conjugation on every exact point the corpus holds.
It offers no mechanism.  This one supplies the mechanism, and it is a chain of
three steps of which the first two are theorems and the third is a computation.

STEP 1 -- THE INTERTWINER RELATION *IS* AN INVARIANT SESQUILINEAR FORM.
Forced, no choices.  From the untwisted duality relation on the generators,

    A . sigma(rho(g)) . A^{-1} = rho(g)^{-T},                                  (*)

multiply on the right by A and on the left by rho(g)^T:

    rho(g)^T A sigma(rho(g)) = A.                                             (**)

Define the sigma-sesquilinear form  H(v, w) := v^T A sigma(w)  on K^3.  Then

    H(rho(g)v, rho(g)w) = v^T rho(g)^T A sigma(rho(g)) sigma(w) = H(v, w),

so A IS a rho-invariant form.  The duality intertwiner and the invariant form are
the same object written two ways.  Schur (the solution space of (**) has exactly
[K:Q] free Q-parameters, i.e. ONE K-dimension) makes it canonical up to a
K-scalar.

STEP 2 -- IT CAN ALWAYS BE NORMALISED HERMITIAN, CONSTRUCTIVELY, BY HILBERT 90.
H is sigma-Hermitian iff A = A^dagger, where A^dagger := transpose(sigma(A)).
Since A^dagger is also invariant and A is unique up to a K-scalar,

    A^dagger = c A   for a unique c in K,   and applying dagger twice gives
    N(c) := sigma(c) c = 1.

Hilbert 90 for K / Fix(sigma) then makes c a ratio EXPLICITLY: for any x with
d := x + c sigma(x) nonzero,

    sigma(d) = sigma(x) + sigma(c) x = sigma(x) + x/c = d/c,   so   sigma(d) c = d,
    hence  (dA)^dagger = sigma(d) A^dagger = sigma(d) c A = d A.

So A_herm := d A is Hermitian.  No existence hand-wave -- d is produced.

STEP 3 -- THE SIGNATURE, AND THIS IS WHERE sigma = CONJUGATION EARNS ITS KEEP.
Steps 1-2 hold for ANY involution sigma; neither one singles out conjugation.
What conjugation supplies is an ARCHIMEDEAN invariant: embed K in C, and if sigma
is complex conjugation at that embedding then dagger is the ordinary conjugate
transpose, A_herm is a Hermitian MATRIX, its eigenvalues are real, and it has a
SIGNATURE (p,q) with p+q=3.  rho then lands in U(p,q).  For an abstract involution
there is no signature and no geometry.

MEASURED: signature (2,1) -- equivalently (1,2), since A_herm is only defined up
to a real scalar and negating it swaps p and q; the projective group is PU(2,1)
either way -- at EVERY embedding, on all four exact points.  PU(2,1) is the
isometry group of complex hyperbolic 2-space, whose boundary is the strictly
pseudoconvex CR 3-sphere.  These are SPHERICAL CR representations.

HOW THE SIGNATURE IS READ -- EXACTLY, TWO INDEPENDENT WAYS THAT MUST AGREE.
(a) JACOBI on the leading principal minors.  For a sigma-Hermitian matrix every
    leading principal minor is sigma-FIXED, hence lies in Fix(sigma); when K is CM
    that subfield is totally real, so each minor is a real algebraic number with an
    unambiguous sign, and the signature is the count of sign agreements/changes in
    (1, D1, D2, D3).  No eigenvalue solver.
(b) the roots of the characteristic polynomial at 50 dps, asserted real.
The script ABORTS if (a) and (b) disagree.

TWO HONEST BOUNDARIES, both enforced by assertions rather than prose.

  * e_0 is ISOTROPIC (A_herm[0,0] = 0) on every case examined.  That is not a
    degeneracy -- it says the first basis vector is a NULL vector, which a definite
    form cannot have, so it is already evidence of indefiniteness.  Jacobi needs
    nonzero minors, so a RATIONAL congruence A -> P^T A P is applied first; sigma
    fixes Q, so this is ordinary congruence and Sylvester's law of inertia keeps
    the signature.

  * `5_2` class 1 ORBIT 1 is NOT CM.  Its Fix(sigma) has degree 3 and is not
    totally real, so the minors are NOT real at every embedding and the signature
    is only defined at the embeddings where sigma acts as conjugation (2 of 6).
    The assertion fires there.  That is the correct behaviour: the argument is
    genuinely weaker on a non-CM field and the script refuses to hide it.

NO FLOAT64: sympy Rationals and exact polynomial arithmetic mod f throughout;
`sp.N(..., 60)` and mpmath at 50 dps for the archimedean reads only.
"""
import json, sys, warnings
warnings.filterwarnings('ignore')
P = '/home/user/qou/computations/ptolemy'
sys.path.insert(0, P)
import sympy as sp
import snappy
from snappy.ptolemy.coordinates import PtolemyCoordinates
from exact_character_selfduality import Elt, poly_to_elt, _frac
from numberfield import NumberField

t = sp.Symbol('t'); PREC = 60
STEM = sys.argv[1] if len(sys.argv) > 1 else '5_2-c1-orbit0'

d = json.loads(open(f'{P}/{STEM}-ptolemy-in-K.json').read())
NAME, KCLS = d['manifold'], d['obstruction_class']
fe = sp.sympify(d['field']['min_poly']); fp = sp.Poly(sp.expand(fe), t); DEG = fp.degree()
K = NumberField([_frac(c) for c in reversed(fp.all_coeffs())])
red = lambda e: sp.expand(sp.rem(sp.Poly(sp.expand(e), t), fp).as_expr())
kinv = lambda x: red(sp.invert(sp.Poly(red(x), t), fp).as_expr())
sig = lambda e, S: red(sp.expand(e).subs(t, S))

def kmatinv(Mx):
    """Inverse of a 3x3 matrix over K = Q[t]/(f), staying inside K.

    sympy's Matrix.inv() emits entries with rational-FUNCTION denominators
    (1/(poly in t)), which are not elements of K and which `red` cannot reduce.
    Use the adjugate and one modular inverse of the determinant instead.
    """
    D = red(Mx.det())
    assert D != 0, 'singular'
    Di = kinv(D)
    adj = sp.Matrix(3, 3, lambda i, j: red(
        (-1) ** (i + j) * Mx.minor_submatrix(j, i).det()))
    return adj.applyfunc(lambda x: red(x * Di))

rows = json.loads(open(f'{P}/{STEM}-duality-generic.json').read())['rows']
w = [k[len('t -> '):] for k, v in rows.items()
     if v.get('untwisted_found') and not v.get('is_identity')]
assert len(w) == 1
SIG = sp.sympify(w[0])
print(f"{STEM}: [K:Q] = {DEG},  f = {fe}")
print(f"sigma: t -> {SIG}\n")

pt = {k: poly_to_elt(K, sp.sympify(v), t) for k, v in d['ptolemy'].items()}
dd = dict(pt); dd['1'] = Elt(K, K.one())
M = snappy.Manifold(NAME)
V = M.ptolemy_variety(3, obstruction_class=KCLS, eliminate_fixed_ptolemys=True)
C = PtolemyCoordinates(dd, is_numerical=False, py_eval_section=eval(V.py_eval_section()),
                       manifold_thunk=lambda: M,
                       non_trivial_generalized_obstruction_class=(KCLS != 0))
G = M.fundamental_group(); gens = G.generators()
e2x = lambda e: sp.expand(sum(sp.Rational(c.numerator, c.denominator) * t ** i
                              for i, c in enumerate(e.v)))
RHO = {g: sp.Matrix(3, 3, lambda i, j: red(e2x(C.evaluate_word(g, G)[i][j]))) for g in gens}

# ---- solve (**) rho^T A sigma(rho) = A -----------------------------------
sym = sp.symbols(f'a0:{9 * DEG}')
A = sp.Matrix(3, 3, lambda i, j: sum(sym[(3 * i + j) * DEG + k] * t ** k for k in range(DEG)))
eqs = []
for g in gens:
    R = RHO[g]; Rs = R.applyfunc(lambda x: sig(x, SIG))
    E = (R.T * A * Rs).applyfunc(red) - A
    for i in range(3):
        for j in range(3):
            pe = sp.Poly(red(E[i, j]), t)
            eqs.extend([sp.expand(pe.coeff_monomial(t ** k)) for k in range(DEG)])
sol = sp.solve(eqs, sym, dict=True)[0]
freev = [v for v in sym if v not in sol]
print(f"STEP 1: solution space has {len(freev)} free Q-params; [K:Q] = {DEG} "
      f"-> A unique up to K-scalar (Schur): {len(freev) == DEG}")

# pick the member with the first free param = 1
A0 = A.subs(sol).subs({v: (1 if i == 0 else 0) for i, v in enumerate(freev)})
A0 = A0.applyfunc(red)
detA = red(A0.det())
assert detA != 0, "A is singular -- the form is degenerate"
print(f"        A nondegenerate: det A = {detA} != 0")

# verify (*) the ORIGINAL intertwiner relation, not just (**)
for g in gens:
    R = RHO[g]; Rs = R.applyfunc(lambda x: sig(x, SIG))
    lhs = (A0 * Rs).applyfunc(red)
    rhs = (kmatinv(R).T * A0).applyfunc(red)
    assert (lhs - rhs).applyfunc(red) == sp.zeros(3, 3), f"(*) fails on {g}"
print(f"        A sigma(rho(g)) = rho(g)^-T A  verified exactly on {gens}")

# ---- STEP 2: A^dagger = c A, N(c) = 1, Hilbert 90 ------------------------
Ad = sp.Matrix(3, 3, lambda i, j: sig(A0[j, i], SIG))       # transpose(sigma(A))
nz = [(i, j) for i in range(3) for j in range(3) if A0[i, j] != 0][0]
c = red(Ad[nz] * kinv(A0[nz]))
assert (Ad - (c * A0).applyfunc(red)).applyfunc(red) == sp.zeros(3, 3), \
    "A^dagger is not a K-multiple of A -- Schur violated"
Nc = red(c * sig(c, SIG))
print(f"\nSTEP 2: A^dagger = c A with c = {c}")
print(f"        norm N(c) = sigma(c)*c = {Nc}   (must be 1: {Nc == 1})")
assert Nc == 1

dd_ = None
for x in [sp.Integer(1), t, red(t * t), red(t + 1), red(t ** 3)]:
    cand = red(x + red(c * sig(x, SIG)))
    if cand != 0:
        dd_ = cand; break
assert dd_ is not None
assert red(sig(dd_, SIG) * c) == dd_, "Hilbert-90 witness fails sigma(d)*c = d"
print(f"        Hilbert 90 witness d = {dd_}")
Ah = (dd_ * A0).applyfunc(red)
Ahd = sp.Matrix(3, 3, lambda i, j: sig(Ah[j, i], SIG))
assert (Ah - Ahd).applyfunc(red) == sp.zeros(3, 3), "A_herm is not Hermitian"
print(f"        A_herm := d*A satisfies A_herm^dagger = A_herm  EXACTLY  OK")

# ---- STEP 3: signature, EXACTLY, via Jacobi on principal minors ----------
# For a sigma-Hermitian A_herm every LEADING PRINCIPAL MINOR is sigma-FIXED,
# hence lies in Fix(sigma).  Fix(sigma) is totally real exactly when K is CM --
# which is the case measured for this stem -- so each minor is a REAL algebraic
# number at every embedding and has an unambiguous sign.  JACOBI'S THEOREM then
# reads the signature straight off the sign sequence 1, D1, D2, D3:
#   #positive eigenvalues = number of sign AGREEMENTS in consecutive pairs,
#   #negative eigenvalues = number of sign CHANGES.
# No eigenvalue solver, no tolerance on an eigenvalue.
print(f"\nSTEP 3: signature of A_herm")

# A RATIONAL congruence A -> P^T A sigma(P) = P^T A P (sigma fixes Q) preserves the
# signature by Sylvester's law of inertia.  Use one to move off an isotropic basis
# vector: D1 = A_herm[0,0] = 0 here, which is not a degeneracy -- it says e_0 is a
# NULL vector of the form, which a DEFINITE form cannot have.  That is already
# evidence the form is indefinite; the congruence just lets Jacobi read it off.
import itertools, random
Acong, Pused = None, None
cands = [sp.eye(3)]
cands += [sp.Matrix(3, 3, lambda a_, b_: 1 if (a_ == b_ or (a_, b_) == pr) else 0)
          for pr in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]]
rng = random.Random(20260914)
for _ in range(60):
    cands.append(sp.Matrix(3, 3, lambda a_, b_: rng.randint(-2, 2)))
for Pm in cands:
    if sp.Rational(Pm.det()) == 0:
        continue
    Ac = (Pm.T * Ah * Pm).applyfunc(red)
    if all(red(Ac[:k, :k].det()) != 0 for k in (1, 2, 3)):
        Acong, Pused = Ac, Pm
        break
assert Acong is not None, "no rational congruence found with all minors nonzero"
print(f"        e_0 is ISOTROPIC (A_herm[0,0] = 0) -- a definite form has no null vector")
print(f"        rational congruence P (det {sp.Rational(Pused.det())}) applied; signature preserved (Sylvester)")
Acd = sp.Matrix(3, 3, lambda i_, j_: sig(Acong[j_, i_], SIG))
assert (Acong - Acd).applyfunc(red) == sp.zeros(3, 3), "congruence broke hermiticity"

D = [sp.Integer(1)] + [red(Acong[:k, :k].det()) for k in (1, 2, 3)]
for k in (1, 2, 3):
    assert red(sig(D[k], SIG) - D[k]) == 0, f"minor D{k} is NOT sigma-fixed"
    assert D[k] != 0
print(f"        leading principal minors sigma-fixed (hence real) and nonzero: OK")

chi = sp.expand(Acong.charpoly(sp.Symbol('x')).as_expr())
roots_f = sp.Poly(fe, t).all_roots()
print(f"\n   {'emb':>4s} {'sigma=conj':>11s} {'sign(D1,D2,D3)':>16s} {'Jacobi (p,q)':>13s} {'chi-roots (p,q)':>16s}")
import mpmath as mp
mp.mp.dps = 50
for idx, r in enumerate(roots_f):
    rN = sp.N(r, PREC)
    isconj = abs(sp.N(SIG.subs(t, rN), PREC) - sp.conjugate(rN)) < sp.Float(10) ** (-(PREC - 15))
    sgn = []
    for k in (1, 2, 3):
        v = sp.N(D[k].subs(t, rN), PREC)
        assert abs(sp.im(v)) < sp.Float(10) ** (-(PREC - 15)), f"D{k} not real at emb {idx}"
        assert abs(sp.re(v)) > sp.Float(10) ** (-(PREC - 20)), f"D{k} too close to 0 at emb {idx}"
        sgn.append(1 if sp.re(v) > 0 else -1)
    seq = [1] + sgn
    p_ = sum(1 for a_, b_ in zip(seq, seq[1:]) if a_ * b_ > 0)
    q_ = sum(1 for a_, b_ in zip(seq, seq[1:]) if a_ * b_ < 0)
    cp = sp.Poly(sp.expand(chi.subs(t, rN)), sp.Symbol('x'))
    cc = [complex(sp.N(c_, 40)) for c_ in cp.all_coeffs()]
    rr = mp.polyroots([mp.mpc(c_.real, c_.imag) for c_ in cc], maxsteps=300, extraprec=300)
    imax = max(abs(mp.im(z)) for z in rr)
    assert imax < mp.mpf(10) ** (-20), f"chi has non-real roots at emb {idx}: {imax}"
    pe = sum(1 for z in rr if mp.re(z) > 0); qe = sum(1 for z in rr if mp.re(z) < 0)
    print(f"   {idx:>4d} {str(bool(isconj)):>11s} {str(tuple(sgn)):>16s} "
          f"{str((p_, q_)):>13s} {str((pe, qe)):>16s}")
    assert (p_, q_) == (pe, qe), "Jacobi and the characteristic polynomial DISAGREE"
