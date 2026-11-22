#!/usr/bin/env python3
"""Braid-level analogue of the QCD three-gluon (and four-gluon) colour vertex.

Pre-registered in PREREGISTRATION-three-gluon-vertex.md (committed before this file).

V = C^3, T^a = lambda^a/2, Omega = sum_a T^a (x) T^a.  Jimbo braided R-matrix of U_q(sl3)
on V (x) V in the convention of NucleonWeightSpaceTraces.lean, R = P Rc.  Everything exact:
Gaussian rationals for the colour tensors (imaginary parts asserted zero), sympy rational
functions in q for the all-q measurements, Fraction power series in hbar (q = e^hbar) for the
expansions.  mpmath only for a final read-out at the proton pin q0.  No float anywhere.

Measurements M1..M5 as in the pre-registration.  Algebra only; no gluon is selected.
"""
from __future__ import annotations

import itertools
import json
import os
from fractions import Fraction

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
N = 3
I = sp.I
q = sp.Symbol("q", positive=True)

# ---------------------------------------------------------------------------
# generic small sparse linear algebra: matrices are dict {(r, c): value}
# ---------------------------------------------------------------------------


def mmul(A, B):
    Bc = {}
    for (r, c), v in B.items():
        Bc.setdefault(r, []).append((c, v))
    out = {}
    for (r, k), a in A.items():
        for c, b in Bc.get(k, ()):
            out[(r, c)] = out.get((r, c), 0) + a * b
    return {k: v for k, v in out.items() if v != 0}


def madd(*terms):
    out = {}
    for coef, A in terms:
        for k, v in A.items():
            out[k] = out.get(k, 0) + coef * v
    return {k: v for k, v in out.items() if v != 0}


def comm(A, B):
    return madd((1, mmul(A, B)), (-1, mmul(B, A)))


def kron(A, da, B, db):
    out = {}
    for (r1, c1), a in A.items():
        for (r2, c2), b in B.items():
            out[(r1 * db + r2, c1 * db + c2)] = a * b
    return out


def ident(d, one=1):
    return {(i, i): one for i in range(d)}


def msimp(A):
    out = {}
    for k, v in A.items():
        v = sp.nsimplify(v) if isinstance(v, sp.Basic) else v
        v = sp.simplify(v) if isinstance(v, sp.Basic) else v
        if v != 0:
            out[k] = v
    return out


def is_zero(A):
    return all((sp.simplify(v) == 0) if isinstance(v, sp.Basic) else v == 0 for v in A.values())


# ---------------------------------------------------------------------------
# colour tensors
# ---------------------------------------------------------------------------


def gell_mann():
    L = [sp.zeros(3) for _ in range(8)]
    L[0][0, 1] = L[0][1, 0] = 1
    L[1][0, 1] = -I; L[1][1, 0] = I
    L[2][0, 0] = 1; L[2][1, 1] = -1
    L[3][0, 2] = L[3][2, 0] = 1
    L[4][0, 2] = -I; L[4][2, 0] = I
    L[5][1, 2] = L[5][2, 1] = 1
    L[6][1, 2] = -I; L[6][2, 1] = I
    L[7][0, 0] = L[7][1, 1] = 1 / sp.sqrt(3); L[7][2, 2] = -2 / sp.sqrt(3)
    return [m / 2 for m in L]


T = gell_mann()
# f, d from tr: f^{abc} = -2i tr([Ta,Tb]Tc), d^{abc} = 2 tr({Ta,Tb}Tc)
f = {}
d = {}
for a, b, c in itertools.product(range(8), repeat=3):
    fv = sp.nsimplify(sp.expand(-2 * I * ((T[a] * T[b] - T[b] * T[a]) * T[c]).trace()))
    dv = sp.nsimplify(sp.expand(2 * ((T[a] * T[b] + T[b] * T[a]) * T[c]).trace()))
    if fv != 0:
        f[(a, b, c)] = fv
    if dv != 0:
        d[(a, b, c)] = dv
for a, b in itertools.product(range(8), repeat=2):  # sanity: commutator closes with f
    lhs = T[a] * T[b] - T[b] * T[a]
    rhs = sum((I * f.get((a, b, c), 0) * T[c] for c in range(8)), sp.zeros(3))
    assert sp.simplify(lhs - rhs) == sp.zeros(3)


def to_sparse(M):
    return {(i, j): sp.nsimplify(sp.expand(M[i, j])) for i in range(M.rows) for j in range(M.cols) if sp.expand(M[i, j]) != 0}


Ts = [to_sparse(t) for t in T]


def realify(A, name):
    out = {}
    for k, v in A.items():
        v = sp.nsimplify(sp.expand(v))
        assert sp.im(v) == 0, (name, k, v)
        v = sp.nsimplify(sp.re(v))
        assert v.is_Rational, (name, k, v)
        if v != 0:
            out[k] = Fraction(int(v.p), int(v.q))
    return out


def op_slots(ops, n):
    """tensor product of single-site ops (dict slot->sparse 3x3) on V^{(x)n}"""
    A = {(0, 0): 1}
    dim = 1
    for s in range(n):
        B = ops.get(s, ident(3))
        A = kron(A, dim, B, 3)
        dim *= 3
    return A


def omega(i, j, n):
    tot = {}
    for a in range(8):
        tot = madd((1, tot), (1, op_slots({i: Ts[a], j: Ts[a]}, n)))
    return realify(tot, f"Omega{i}{j}")


# F, D on V^3 ; G on V^4
F_ = {}
for (a, b, c), v in f.items():
    F_ = madd((1, F_), (I * v, op_slots({0: Ts[a], 1: Ts[b], 2: Ts[c]}, 3)))
F = realify(F_, "F")
D_ = {}
for (a, b, c), v in d.items():
    D_ = madd((1, D_), (v, op_slots({0: Ts[a], 1: Ts[b], 2: Ts[c]}, 3)))
D = realify(D_, "D")
K = []  # K_e = f^{abe} T^a (x) T^b  on V^2
for e in range(8):
    acc = {}
    for (a, b, c), v in f.items():
        if c == e:
            acc = madd((1, acc), (v, op_slots({0: Ts[a], 1: Ts[b]}, 2)))
    K.append(acc)
G_ = {}
for e in range(8):
    G_ = madd((1, G_), (1, kron(K[e], 9, K[e], 9)))
G = realify(G_, "G")

# ---------------------------------------------------------------------------
# permutation operators and commutant projection
# ---------------------------------------------------------------------------


def perm_op(sigma, n):
    """P_sigma e_{i_0..i_{n-1}} = e_{j} with j_{sigma(s)} = i_s"""
    out = {}
    for idx in itertools.product(range(3), repeat=n):
        j = [0] * n
        for s in range(n):
            j[sigma[s]] = idx[s]
        c = sum(x * 3 ** (n - 1 - k) for k, x in enumerate(idx))
        r = sum(x * 3 ** (n - 1 - k) for k, x in enumerate(j))
        out[(r, c)] = Fraction(1)
    return out


def ncycles(p):
    seen, c = set(), 0
    for s in range(len(p)):
        if s not in seen:
            c += 1
            while s not in seen:
                seen.add(s); s = p[s]
    return c


def compose(a, b):  # (a∘b)(s) = a(b(s))
    return tuple(a[b[s]] for s in range(len(a)))


def inverse(a):
    inv = [0] * len(a)
    for s, t in enumerate(a):
        inv[t] = s
    return tuple(inv)


def hs_with_perm(X, sigma, n):
    # tr(P_sigma^T X) = sum_c X[P_sigma(c), c]
    tot = 0
    for idx in itertools.product(range(3), repeat=n):
        j = [0] * n
        for s in range(n):
            j[sigma[s]] = idx[s]
        c = sum(x * 3 ** (n - 1 - k) for k, x in enumerate(idx))
        r = sum(x * 3 ** (n - 1 - k) for k, x in enumerate(j))
        tot += X.get((r, c), 0)
    return tot


def commutant_coords(X, perms, n):
    """coordinates c with Proj(X) = sum c_s P_s; perms must be a basis of the commutant image"""
    Gm = sp.Matrix(len(perms), len(perms), lambda i, j: sp.Integer(3) ** ncycles(compose(inverse(perms[i]), perms[j])))
    b = sp.Matrix([sp.nsimplify(hs_with_perm(X, p, n)) if not isinstance(hs_with_perm(X, p, n), sp.Basic) else hs_with_perm(X, p, n) for p in perms])
    sol = Gm.LUsolve(b)
    return [sp.simplify(s) for s in sol]


S3 = [tuple(p) for p in itertools.permutations(range(3))]
ID3 = (0, 1, 2); P12 = (1, 0, 2); P23 = (0, 2, 1); P13 = (2, 1, 0)
C = compose(P12, P23)
C2 = compose(P23, P12)
basis_names = ["1", "P12", "P13", "P23", "C=P12P23", "C2=P23P12"]
basis3 = [ID3, P12, P13, P23, C, C2]
# adapted basis (conjugation-isotypic): 1, St, Sc, A, E1, E2
adapted = sp.Matrix([
    [1, 0, 0, 0, 0, 0],      # 1
    [0, 1, 1, 1, 0, 0],      # St = P12+P13+P23
    [0, 0, 0, 0, 1, 1],      # Sc = C+C2
    [0, 0, 0, 0, 1, -1],     # A = C - C2
    [0, 1, 0, -1, 0, 0],     # E1 = P12 - P23
    [0, 1, -2, 1, 0, 0],     # E2 = P12 - 2 P13 + P23
]).T  # columns = adapted vectors in basis3 coords
adapted_names = ["1", "St", "Sc", "A=C-C2", "E1", "E2"]


def adapted_coords(c):
    return list(adapted.LUsolve(sp.Matrix(c)))


def fr(x):
    return sp.Rational(x.numerator, x.denominator) if isinstance(x, Fraction) else x


def sym(A):
    return {k: fr(v) for k, v in A.items()}


def to_frac_op(A):
    return {k: Fraction(v) if not isinstance(v, Fraction) else v for k, v in A.items()}


out = {"probe": "mn_three_gluon_vertex_probe", "prereg": "PREREGISTRATION-three-gluon-vertex.md",
       "conventions": {"T": "lambda/2", "F": "i f^{abc} T^a T^b T^c", "D": "d^{abc} T^a T^b T^c",
                       "G": "f^{abe} f^{cde} T^a T^b T^c T^d",
                       "Rc": "Rc(ii)=q ii; i<j: Rc(ij)=ji, Rc(ji)=ij+h ji; R=P Rc",
                       "perm": "P_sigma moves slot s to slot sigma(s); C = P12 P23"}}

# ---------------- M1 ----------------
O12, O23, O13 = omega(0, 1, 3), omega(1, 2, 3), omega(0, 2, 3)
P12op = perm_op(P12, 3)
assert O12 == madd((Fraction(1, 2), P12op), (Fraction(-1, 6), ident(27, Fraction(1)))), "Omega != (P - 1/3)/2"
cF = adapted_coords(commutant_coords(sym(F), basis3, 3))
cD = adapted_coords(commutant_coords(sym(D), basis3, 3))
assert all(sp.simplify(x) == 0 for x in (cF[0], cF[1], cF[2], cF[4], cF[5])), cF
kF = cF[3]  # F = kF * A
assert all(sp.simplify(x) == 0 for x in (cD[3], cD[4], cD[5])), cD
c12_23 = comm(O12, O23)
coef_comm = adapted_coords(commutant_coords(sym(c12_23), basis3, 3))
assert all(sp.simplify(x) == 0 for x in (coef_comm[0], coef_comm[1], coef_comm[2], coef_comm[4], coef_comm[5]))
ratio_M1 = sp.simplify(coef_comm[3] / kF)  # [O12,O23] = ratio * F
# check operator identity directly
assert madd((1, c12_23), (-Fraction(int(ratio_M1.p), int(ratio_M1.q)), F)) == {}
out["M1"] = {
    "Omega_eq_(P-1/3)/2": True,
    "F_in_adapted_basis": {"A=C-C2": str(kF), "others": "0"},
    "D_in_adapted_basis": dict(zip(adapted_names[:3], map(str, cD[:3]))),
    "[Omega12,Omega23]_over_F": str(ratio_M1),
    "[Omega12,Omega23]_D_component": "0 (D lies in span{1,St,Sc}; the commutator has only A)",
    "reading": "[Omega12,Omega23] = c * i f^{abc} T^a T^b T^c exactly, and F = kF (C - C^2): the f-structure "
               "IS the antisymmetrised 3-cycle on V^3 (standard sl3 algebra).",
}

# ---------------- R-matrices ----------------


def Rc_matrix(qv):
    hv = qv - 1 / qv
    M = {}
    for i in range(3):
        for j in range(3):
            col = 3 * i + j
            if i == j:
                M[(col, col)] = qv
            elif i < j:
                M[(3 * j + i, col)] = 1
            else:
                M[(3 * j + i, col)] = 1
                M[(col, col)] = hv
    return M


P2 = perm_op((1, 0), 2)
Rc_q = Rc_matrix(q)
R_q = mmul(P2, Rc_q)


def emb2(A2, i, n):
    """embed a 2-site op on adjacent sites (i,i+1) into V^{(x)n}"""
    left = 3 ** i
    right = 3 ** (n - i - 2)
    X = kron(ident(left), left, A2, 9)
    return kron(X, left * 9, ident(right), right)


def conj(P, X):
    return mmul(mmul(P, X), P)  # P is an involution here


R12 = emb2(R_q, 0, 3); R23 = emb2(R_q, 1, 3)
P23op = perm_op(P23, 3)
R13 = conj(sym(P23op), R12)
ybe = madd((1, mmul(mmul(R12, R13), R23)), (-1, mmul(mmul(R23, R13), R12)))
assert is_zero(ybe), "YBE fails"
Rc12 = emb2(Rc_q, 0, 3); Rc23 = emb2(Rc_q, 1, 3)
braid = madd((1, mmul(mmul(Rc12, Rc23), Rc12)), (-1, mmul(mmul(Rc23, Rc12), Rc23)))
assert is_zero(braid), "braid relation fails"
hecke = madd((1, mmul(Rc_q, Rc_q)), (-(q - 1 / q), Rc_q), (-1, ident(9)))
assert is_zero(hecke), "Hecke relation fails"

# ---------------- hbar series ----------------
ORD = 4  # keep hbar^0..hbar^3


def laurent_series(expr):
    """expr = Laurent polynomial in q (times q^(rational)); return [c0..c_{ORD-1}] of expr(e^hbar)"""
    expr = sp.expand(expr)
    coeffs = [Fraction(0)] * ORD
    for term in sp.Add.make_args(expr):
        c, rest = term.as_coeff_Mul()
        if rest == 1:
            k = sp.Integer(0)
        else:
            base, k = rest.as_base_exp()
            assert base == q, term
        k = Fraction(int(sp.Rational(k).p), int(sp.Rational(k).q))
        c = Fraction(int(sp.Rational(c).p), int(sp.Rational(c).q))
        term_n = Fraction(1)
        for nn in range(ORD):
            coeffs[nn] += c * term_n
            term_n = term_n * k / (nn + 1)
    return coeffs


def op_series(A):
    S = [dict() for _ in range(ORD)]
    for kk, v in A.items():
        for nn, cval in enumerate(laurent_series(v)):
            if cval != 0:
                S[nn][kk] = cval
    return S


def ser_mul(S1, S2):
    S = [dict() for _ in range(ORD)]
    for i in range(ORD):
        for j in range(ORD - i):
            S[i + j] = madd((1, S[i + j]), (1, mmul(S1[i], S2[j])))
    return S


Rt_q = {k: v * q ** sp.Rational(-1, 3) for k, v in R_q.items()}  # normalised R~ = q^{-1/3} R
Rt_ser2 = op_series(Rt_q)
r = Rt_ser2[1]
assert Rt_ser2[0] == ident(9, Fraction(1))
Om2 = omega(0, 1, 2)
P2f = to_frac_op(P2)
r21 = mmul(mmul(P2f, r), P2f)
r_a = madd((1, r), (-2, Om2))
assert madd((1, r), (1, r21)) == madd((4, Om2)), "r + r21 != 4 Omega"
assert madd((1, r_a), (1, mmul(mmul(P2f, r_a), P2f))) == {}, "r_a not antisymmetric"


def emb_ser(S, i, n):
    return [emb2(x, i, n) for x in S]


# ---------------- M2: YBE at order hbar^2 = CYBE(r) ----------------
def emb13(A2):
    return conj(to_frac_op(P23op), emb2(A2, 0, 3))


ra12, ra23, ra13 = emb2(r_a, 0, 3), emb2(r_a, 1, 3), emb13(r_a)
O = {"12": O12, "23": O23, "13": O13}
A_ = {"12": ra12, "23": ra23, "13": ra13}


def cybe(X12, X13, X23, Y12=None, Y13=None, Y23=None):
    Y12 = Y12 or X12; Y13 = Y13 or X13; Y23 = Y23 or X23
    return madd((1, comm(X12, Y13)), (1, comm(X12, Y23)), (1, comm(X13, Y23)))


twoO = {k: madd((2, v)) for k, v in O.items()}
cy_OO = cybe(twoO["12"], twoO["13"], twoO["23"])
cy_aa = cybe(A_["12"], A_["13"], A_["23"])
cy_mix = madd((1, cybe(twoO["12"], twoO["13"], twoO["23"], A_["12"], A_["13"], A_["23"])),
              (1, cybe(A_["12"], A_["13"], A_["23"], twoO["12"], twoO["13"], twoO["23"])))
total = madd((1, cy_OO), (1, cy_aa), (1, cy_mix))
assert total == {}, "CYBE(r) != 0"
Ff = F


def f_multiple(X):
    """return c if X == c F exactly, else None"""
    if not X:
        return Fraction(0)
    k0 = next(iter(Ff))
    c = Fraction(X.get(k0, 0)) / Ff[k0]
    return c if madd((1, X), (-c, Ff)) == {} else None


def proj_F_D(X):
    cc = adapted_coords(commutant_coords(sym(X), basis3, 3))
    return {"F_coef": str(sp.simplify(cc[3] / kF)), "adapted": dict(zip(adapted_names, [str(sp.simplify(x)) for x in cc]))}


out["M2"] = {
    "YBE_R12R13R23=R23R13R12_exact": True, "braid_relation_exact": True, "Hecke_relation_exact": True,
    "r_decomposition": "r = 2 Omega + r_a, r + r21 = 4 Omega, r_a antisymmetric (exact)",
    "CYBE(2Omega)_over_F": str(f_multiple(cy_OO)),
    "CYBE(r_a)_over_F": str(f_multiple(cy_aa)),
    "mixed_terms_exact_zero": cy_mix == {},
    "mixed_terms_projection": proj_F_D(cy_mix) if cy_mix else "0",
    "CYBE(r)_total": "0 exactly",
    "reading": "The YBE at order hbar^2 is CYBE(r)=0; the Omega-Omega part is a nonzero multiple of F and is "
               "cancelled by CYBE(r_a) (modified CYBE). F appears in the braid relation only as a cancellation.",
}

# ---------------- M3: order hbar^2 of R~12 R~23 and of Rc12 Rc23 Rc12 ----------------
S12 = emb_ser(Rt_ser2, 0, 3); S23 = emb_ser(Rt_ser2, 1, 3)
prod = ser_mul(S12, S23)
m3 = {}
for nn in range(ORD):
    m3[f"hbar^{nn}"] = proj_F_D(prod[nn])
half_comm = madd((Fraction(1, 2), comm(emb2(r, 0, 3), emb2(r, 1, 3))))
m3["(1/2)[r12,r23]_projection"] = proj_F_D(half_comm)
# exact-q projection of R12 R23 (normalised q^{-2/3}) and of Rc12 Rc23 Rc12
R12R23 = mmul(R12, R23)
m3["R12R23_exact_q_projection(unnormalised)"] = proj_F_D(R12R23)
rc_long = mmul(mmul(Rc12, Rc23), Rc12)
m3["Rc12Rc23Rc12_exact_q_projection"] = proj_F_D(rc_long)
two_comm = madd((2, comm(O12, O23)))  # (1/2)[2 Omega12, 2 Omega23]
m3["(1/2)[2Omega12,2Omega23]_over_F"] = str(f_multiple(two_comm))
m3["r_a_contribution_to_hbar2_F_coef"] = str(sp.Rational(-8, 3) - sp.Rational(str(f_multiple(two_comm))))
out["M3"] = m3

# ---------------- M4: photon chiral letter and Borromean core ----------------
hq = q - 1 / q
Rc_inv = madd((1, Rc_q), (-hq, ident(9)))
assert is_zero(madd((1, mmul(Rc_q, Rc_inv)), (-1, ident(9))))
letter = mmul(Rc12, emb2(Rc_inv, 1, 3))          # sigma0 sigma1^{-1}
letter_rev = mmul(emb2(Rc_inv, 1, 3), Rc12)      # sigma1^{-1} sigma0
V3 = mmul(mmul(letter, letter), letter)
V3 = {k: sp.factor(sp.expand(v)) for k, v in V3.items() if sp.expand(v) != 0}

# abstract H3 coordinates via the (faithful) rep on V^3
hb = [ident(27, sp.Integer(1)), Rc12, Rc23, mmul(Rc12, Rc23), mmul(Rc23, Rc12), rc_long]
hb_names = ["1", "s0", "s1", "s0s1", "s1s0", "s0s1s0"]


def hecke_coords(X):
    keys = sorted(set().union(*[set(b) for b in hb], set(X)))
    M = sp.Matrix([[b.get(k, 0) for b in hb] for k in keys])
    v = sp.Matrix([X.get(k, 0) for k in keys])
    sol, params = M.gauss_jordan_solve(v)
    assert not params.free_symbols - {q} or len(params) == 0
    return [sp.factor(sp.simplify(s)) for s in sol]


def hecke_report(X):
    c = hecke_coords(X)
    d_ = dict(zip(hb_names, c))
    return {"coords": {k: str(v) for k, v in d_.items()},
            "commutator_coef_(s0s1-s1s0)": str(sp.factor((d_["s0s1"] - d_["s1s0"]) / 2)),
            "flip_antisym_s0-s1_coef": str(sp.factor((d_["s0"] - d_["s1"]) / 2))}


import mpmath as mpm  # noqa: E402  read-out only
mpm.mp.dps = 40
try:
    from qou_substrate.constants import Q_50_DIGIT_STR as _Q0S
    q0 = mpm.mpf(_Q0S)
    q0_src = "qou_substrate.constants.Q_50_DIGIT_STR (proton pin)"
except ImportError as _e:  # pragma: no cover
    # No typed fallback: a 17-digit copy of the pin would publish a different
    # number silently (reference-literal ratchet, issue #9104).
    raise SystemExit(f"qou_substrate is required for the proton pin: {_e}")
Q0_RAT = sp.Rational(mpm.nstr(q0, 40))


def at_q0(s):
    e = sp.sympify(s, locals={"q": q})
    if not e.free_symbols:
        return str(e)
    v = sp.Rational(e.subs(q, Q0_RAT))  # exact rational evaluation, then one mpf division
    return mpm.nstr(mpm.mpf(v.p) / mpm.mpf(v.q), 20)


def report(X):
    pr = proj_F_D(X)
    hr = hecke_report(X)
    fc = sp.factor(sp.sympify(pr["F_coef"], locals={"q": q}))
    ser = sp.series(fc.subs(q, sp.exp(sp.Symbol("hbar"))), sp.Symbol("hbar"), 0, 3).removeO()
    return {"classical_commutant_projection": pr, "F_coef_factored": str(fc),
            "F_coef_series_hbar": str(sp.expand(ser)), "F_coef_at_q0": at_q0(fc),
            "H3": hr, "H3_commutator_coef_at_q0": at_q0(hr["commutator_coef_(s0s1-s1s0)"])}


out["M4"] = {"q0_source": q0_src,
             "sigma0_sigma1inv (photon chiral letter)": report(letter),
             "sigma1inv_sigma0 (reversed order)": report(letter_rev),
             "V3 = (sigma0 sigma1inv)^3 (Borromean core)": report(V3),
             "sigma0sigma1 (for comparison)": report(mmul(Rc12, Rc23))}

# ---------------- M5: four strands ----------------
S4 = [tuple(p) for p in itertools.permutations(range(4))]
# kernel of S4 -> End(V^4) for dim V = 3 is the antisymmetriser; drop one 4-cycle
drop = (1, 2, 3, 0)
basis4 = [p for p in S4 if p != drop]
O4 = {(i, j): omega(i, j, 4) for i, j in itertools.combinations(range(4), 2)}
nested = comm(comm(O4[(0, 1)], O4[(1, 2)]), O4[(2, 3)])
kG = None
k0 = next(iter(G))
kG = Fraction(nested.get(k0, 0)) / G[k0]
nested_is_multiple = madd((1, nested), (-kG, G)) == {}


def coords4(X):
    return [sp.nsimplify(x) for x in commutant_coords(sym(X), basis4, 4)]


cG = coords4(G)
# span of degree <=2 Omega monomials
monos = [ident(81, Fraction(1))] + list(O4.values()) + [mmul(a, b) for a in O4.values() for b in O4.values()]
Mspan = sp.Matrix([coords4(m) for m in monos]).T
rank_span = Mspan.rank()
aug_rank = Mspan.row_join(sp.Matrix(cG)).rank()
G_in_span = aug_rank == rank_span
# R~12 R~23 R~34 series, projected, and in/out of span per order
T12 = emb_ser(Rt_ser2, 0, 4); T23 = emb_ser(Rt_ser2, 1, 4); T34 = emb_ser(Rt_ser2, 2, 4)
chain = ser_mul(ser_mul(T12, T23), T34)
order_out = {}
for nn in range(ORD):
    cc = sp.Matrix(coords4(chain[nn]))
    order_out[f"hbar^{nn}"] = {"in_degree<=2_Omega_span": Mspan.row_join(cc).rank() == rank_span}
MspanG = Mspan.row_join(sp.Matrix(cG))


def g_coef_mod_span(X):
    """if X in span(deg<=2 monomials, G), return the (unique) G coefficient, else None"""
    cc = sp.Matrix(coords4(X))
    if MspanG.row_join(cc).rank() != MspanG.rank():
        return None
    sol, params = MspanG.gauss_jordan_solve(cc)
    g = sol[-1]
    return str(sp.simplify(g.subs({p: 0 for p in params})))


for nn in range(ORD):
    order_out[f"hbar^{nn}"]["G_coef_mod_degree<=2_span"] = g_coef_mod_span(chain[nn])
ra4 = {(i, i + 1): emb2(r_a, i, 4) for i in range(3)}
order_out["r_a12*r_a34_G_coef_mod_span"] = g_coef_mod_span(mmul(ra4[(0, 1)], ra4[(2, 3)]))
order_out["r_a12*r_a23_G_coef_mod_span"] = g_coef_mod_span(mmul(ra4[(0, 1)], ra4[(1, 2)]))
order_out["r_a23*r_a34_G_coef_mod_span"] = g_coef_mod_span(mmul(ra4[(1, 2)], ra4[(2, 3)]))
order_out["quotient_dim_commutant/deg<=2_span"] = int(23 - rank_span)
order_out["G_coef_well_defined"] = bool(MspanG.rank() == rank_span + 1)
out["M5"] = {"commutant_basis": "S4 minus the 4-cycle (1,2,3,0) (antisymmetriser kernel for dim V=3)",
             "[[O12,O23],O34]_over_G": str(kG) if nested_is_multiple else "not a multiple of G",
             "nested_is_multiple_of_G": nested_is_multiple,
             "G_coords_nonzero": {"".join(map(str, p)): str(c) for p, c in zip(basis4, cG) if c != 0},
             "rank_degree<=2_Omega_span": int(rank_span),
             "G_in_degree<=2_span": G_in_span,
             "R12R23R34_orders": order_out}

out["verdict"] = {
    "M1": "[Omega12,Omega23] = -F exactly (F = i f^{abc}T^aT^bT^c = -(1/4)(C - C^2)); d-component 0. Standard sl3 algebra.",
    "M2": "YBE exact; order hbar^2 = CYBE(r) = 0 with CYBE(2 Omega) = +4F cancelled by CYBE(r_a) = -4F, mixed terms 0. "
          "The braid relation contains F only as a cancellation (modified CYBE).",
    "M3": "R~12R~23 at hbar^2: F-coef -8/3 = -2 (from (1/2)[2Omega12,2Omega23]) + -2/3 (from r_a, after Haar projection). "
          "Rc12Rc23Rc12: F-coef 0 at all q (prediction held).",
    "M4": "sigma0 sigma1^-1: F-coef -(q+1)^2/(2q) = -2 - hbar^2/2 (identical to sigma0 sigma1: the 3-cycle at q=1 carries F at hbar^0); "
          "H3 commutator coef exactly 1/2. V^3: F-coef -(q-1)^2(q+1)^4(q^4+1)/(2q^5) = -16 hbar^2 + ..., zero at q=1; "
          "H3 commutator coef (q-1)^2(q+1)^2(q^4+1)/(2q^4).",
    "M5": "[[O12,O23],O34] = -G exactly; G not in the degree<=2 Omega span (rank 18 of 23). PREDICTION FAILED for the "
          "R~ chain: the projected hbar^2 term already leaves the span, with G-coefficient -38/45 mod span, all of it from "
          "r_a12*r_a34 (Haar average of the non-invariant antisymmetric parts of two disjoint crossings).",
    "scope": "Projections are classical-SU(3) Haar averages; they are not U_q-covariant. No vertex, coupling or gluon is identified.",
}
with open(os.path.join(HERE, "mn_three_gluon_vertex_probe.out.json"), "w") as fh:
    json.dump(out, fh, indent=2, default=str)
print(json.dumps(out, indent=2, default=str))
