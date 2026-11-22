#!/usr/bin/env python3
"""Does the hbar^2 F-term of the Borromean core V^3 = (s0 s1^-1)^3 give a beta0-like number?

Pre-registered in PREREGISTRATION-beta0-from-braid.md (committed before this file, 78a5efe3447).
Three candidate maps, hit rules fixed there:
  (i)   r = X_ff / X_loop: G-coefficient of W4 = (s0 s1^-1 s2)^4 vs the Omega-coefficient of the
        strand-3 closure of V^3 (L1 sl3 quantum partial trace, L2 convention-D E_D); hit |r| = 33/2,
        same hbar order, opposite sign.
  (ii)  hbar^2 relative corrections b, b' of the F- and H3-commutator coefficients of V^3; hit in S.
  (iii) Casimir slope of [hbar^2] Haar(V^3) on the channels 10, 8, 8, 1 of V^(x)3; hit in S.
Exact arithmetic only (sympy rationals / Fraction series in hbar, q = e^hbar). No float. Machinery
(colour tensors, Jimbo R, commutant projection) copied from mn_three_gluon_vertex_probe.py (section 49).
Algebra only; no gluon is selected, nothing is wired.
"""
from __future__ import annotations

import itertools
import json
import os
from fractions import Fraction

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
I = sp.I
q = sp.Symbol("q", positive=True)
hb = sp.Symbol("hbar")
S_SET = [sp.Rational(x) for x in ("11", "11/3", "22/3", "11/2", "11/6", "22", "11/12")]
HIT_RATIO = sp.Rational(33, 2)


# ---------------- sparse linear algebra (dict {(r,c): v}) ----------------
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


# ---------------- colour tensors ----------------
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
f = {}
for a, b, c in itertools.product(range(8), repeat=3):
    fv = sp.nsimplify(sp.expand(-2 * I * ((T[a] * T[b] - T[b] * T[a]) * T[c]).trace()))
    if fv != 0:
        f[(a, b, c)] = fv
Ts = [{(i, j): sp.nsimplify(sp.expand(t[i, j])) for i in range(3) for j in range(3) if sp.expand(t[i, j]) != 0} for t in T]


def realify(A):
    out = {}
    for k, v in A.items():
        v = sp.nsimplify(sp.expand(v))
        assert sp.im(v) == 0
        v = sp.nsimplify(sp.re(v))
        assert v.is_Rational
        if v != 0:
            out[k] = Fraction(int(v.p), int(v.q))
    return out


def op_slots(ops, n):
    A, dim = {(0, 0): 1}, 1
    for s in range(n):
        A = kron(A, dim, ops.get(s, ident(3)), 3)
        dim *= 3
    return A


def omega(i, j, n):
    tot = {}
    for a in range(8):
        tot = madd((1, tot), (1, op_slots({i: Ts[a], j: Ts[a]}, n)))
    return realify(tot)


F_ = {}
for (a, b, c), v in f.items():
    F_ = madd((1, F_), (I * v, op_slots({0: Ts[a], 1: Ts[b], 2: Ts[c]}, 3)))
F = realify(F_)
K = []
for e in range(8):
    acc = {}
    for (a, b, c), v in f.items():
        if c == e:
            acc = madd((1, acc), (v, op_slots({0: Ts[a], 1: Ts[b]}, 2)))
    K.append(acc)
G_ = {}
for e in range(8):
    G_ = madd((1, G_), (1, kron(K[e], 9, K[e], 9)))
G = realify(G_)


# ---------------- permutations / commutant ----------------
def ncycles(p):
    seen, c = set(), 0
    for s in range(len(p)):
        if s not in seen:
            c += 1
            while s not in seen:
                seen.add(s); s = p[s]
    return c


def compose(a, b):
    return tuple(a[b[s]] for s in range(len(a)))


def inverse(a):
    inv = [0] * len(a)
    for s, t in enumerate(a):
        inv[t] = s
    return tuple(inv)


def perm_op(sigma, n):
    out = {}
    for idx in itertools.product(range(3), repeat=n):
        j = [0] * n
        for s in range(n):
            j[sigma[s]] = idx[s]
        c = sum(x * 3 ** (n - 1 - k) for k, x in enumerate(idx))
        r = sum(x * 3 ** (n - 1 - k) for k, x in enumerate(j))
        out[(r, c)] = Fraction(1)
    return out


def hs_with_perm(X, sigma, n):
    tot = 0
    for idx in itertools.product(range(3), repeat=n):
        j = [0] * n
        for s in range(n):
            j[sigma[s]] = idx[s]
        c = sum(x * 3 ** (n - 1 - k) for k, x in enumerate(idx))
        r = sum(x * 3 ** (n - 1 - k) for k, x in enumerate(j))
        tot += X.get((r, c), 0)
    return tot


def fr(x):
    return sp.Rational(x.numerator, x.denominator) if isinstance(x, Fraction) else x


def commutant_coords(X, perms, n):
    Gm = sp.Matrix(len(perms), len(perms), lambda i, j: sp.Integer(3) ** ncycles(compose(inverse(perms[i]), perms[j])))
    b = sp.Matrix([fr(hs_with_perm(X, p, n)) if not isinstance(hs_with_perm(X, p, n), sp.Basic) else hs_with_perm(X, p, n) for p in perms])
    return [sp.simplify(s) for s in Gm.LUsolve(b)]


# ---------------- Jimbo R ----------------
def Rc_matrix(qv):
    hv = qv - 1 / qv
    M = {}
    for i in range(3):
        for j in range(3):
            col = 3 * i + j
            if i == j:
                M[(col, col)] = qv
            else:
                M[(3 * j + i, col)] = 1
                if i > j:
                    M[(col, col)] = hv
    return M


def emb2(A2, i, n):
    left, right = 3 ** i, 3 ** (n - i - 2)
    return kron(kron(ident(left), left, A2, 9), left * 9, ident(right), right)


hq = q - 1 / q
Rc_q = Rc_matrix(q)
Rc_inv = madd((1, Rc_q), (-hq, ident(9)))
assert all(sp.simplify(v) == 0 for v in madd((1, mmul(Rc_q, Rc_inv)), (-1, ident(9))).values())

# ---------------- hbar series (Laurent polys in q -> Fraction coefficients) ----------------
ORD = 6


def laurent_series(expr, ordn=ORD):
    expr = sp.expand(expr)
    coeffs = [Fraction(0)] * ordn
    for term in sp.Add.make_args(expr):
        c, rest = term.as_coeff_Mul()
        if rest == 1:
            k = sp.Integer(0)
        else:
            base, k = rest.as_base_exp()
            assert base == q, term
        k = Fraction(int(sp.Rational(k).p), int(sp.Rational(k).q))
        c = Fraction(int(sp.Rational(c).p), int(sp.Rational(c).q))
        tn = Fraction(1)
        for nn in range(ordn):
            coeffs[nn] += c * tn
            tn = tn * k / (nn + 1)
    return coeffs


def op_series(A, ordn=ORD):
    S = [dict() for _ in range(ordn)]
    for kk, v in A.items():
        for nn, cv in enumerate(laurent_series(v, ordn)):
            if cv != 0:
                S[nn][kk] = cv
    return S


def ser_mul(S1, S2):
    n = len(S1)
    S = [dict() for _ in range(n)]
    for i in range(n):
        for j in range(n - i):
            S[i + j] = madd((1, S[i + j]), (1, mmul(S1[i], S2[j])))
    return S


out = {"probe": "mn_beta0_from_braid_probe", "prereg": "PREREGISTRATION-beta0-from-braid.md (78a5efe3447)",
       "target": {"beta0": "11 - (2/3) n_f = (11/3) C_A - (4/3) T_F n_f",
                  "hit_ratio_(i)": "33/2", "S": [str(s) for s in S_SET]}}

# =====================================================================================
# (i-a) X_ff: G-coefficient of W4 = (s0 s1^-1 s2)^4, leading hbar order
# =====================================================================================
S4 = [tuple(p) for p in itertools.permutations(range(4))]
basis4 = [p for p in S4 if p != (1, 2, 3, 0)]
O4 = {(i, j): omega(i, j, 4) for i, j in itertools.combinations(range(4), 2)}


def coords4(X):
    return [sp.nsimplify(x) for x in commutant_coords(X, basis4, 4)]


cG = coords4(G)
monos = [ident(81, Fraction(1))] + list(O4.values()) + [mmul(a, b) for a in O4.values() for b in O4.values()]
Mspan = sp.Matrix([coords4(m) for m in monos]).T
rank_span = Mspan.rank()
MspanG = Mspan.row_join(sp.Matrix(cG))
assert MspanG.rank() == rank_span + 1


def g_coef_mod_span(X):
    cc = sp.Matrix(coords4(X))
    if MspanG.row_join(cc).rank() != MspanG.rank():
        return None
    sol, params = MspanG.gauss_jordan_solve(cc)
    return sp.simplify(sol[-1].subs({p: 0 for p in params}))


# check the pure-braid rule: underlying permutation of s0 s1^-1 s2 at q=1 and its order
p_letter = compose(compose((1, 0, 2, 3), (0, 2, 1, 3)), (0, 1, 3, 2))
order = next(k for k in range(1, 10) if (lambda p: all(p[i] == i for i in range(4)))(
    (lambda k: [p := p_letter] and [p := compose(p, p_letter) for _ in range(k - 1)] and p)(k) if k > 1 else p_letter))
assert order == 4, order
L0 = op_series(emb2(Rc_q, 0, 4)); L1i = op_series(emb2(Rc_inv, 1, 4)); L2 = op_series(emb2(Rc_q, 2, 4))
letter4 = ser_mul(ser_mul(L0, L1i), L2)
W4 = letter4
for _ in range(3):
    W4 = ser_mul(W4, letter4)
assert W4[0] == ident(81, Fraction(1)), "W4 at q=1 is not the identity (not pure)"
w4_orders = {}
X_ff, ord_ff = None, None
for nn in range(1, ORD):
    g = g_coef_mod_span(W4[nn])
    w4_orders[f"hbar^{nn}"] = "outside span+G" if g is None else str(g)
    if X_ff is None and g is not None and g != 0:
        X_ff, ord_ff = g, nn
out["i_ff"] = {"word": "W4 = (s0 s1^-1 s2)^4 (permutation order of the letter = 4, W4(q=1) = 1 checked)",
               "rank_deg<=2_Omega_span": int(rank_span),
               "G_coef_mod_span_by_order": w4_orders, "X_ff": str(X_ff), "order": ord_ff,
               "reading": "G-coefficient 0 where defined (hbar^1, hbar^2); undefined from hbar^3 (outside span+G)"}

# =====================================================================================
# V^3 exactly on V^(x)3
# =====================================================================================
Rc12 = emb2(Rc_q, 0, 3); Rc23 = emb2(Rc_q, 1, 3)
letter = mmul(Rc12, emb2(Rc_inv, 1, 3))
V3 = mmul(mmul(letter, letter), letter)
V3 = {k: sp.factor(sp.expand(v)) for k, v in V3.items() if sp.expand(v) != 0}


def series_rat(expr, n=ORD):
    """exact Taylor coefficients in hbar of a rational function of q at q = e^hbar"""
    e = sp.series(sp.sympify(expr).subs(q, sp.exp(hb)), hb, 0, n).removeO()
    return [sp.nsimplify(sp.expand(e).coeff(hb, k)) for k in range(n)]


def omega_coef_2(X9):
    """X on V(x)V -> classical-commutant coords (a,b) for a*1 + b*P; Omega coefficient = 2b"""
    a, b = commutant_coords(X9, [(0, 1), (1, 0)], 2)
    return sp.factor(a), sp.factor(b), sp.factor(2 * b)


def leading(coefs):
    for k, c in enumerate(coefs):
        if c != 0:
            return k, c
    return None, 0


# ---------------- L1: sl3 quantum partial trace on strand 3 ----------------
def ptrace_last(X, n, w):
    """partial trace over the last of n slots with weights w[k]"""
    out_ = {}
    for (r, c), v in X.items():
        r0, rk = divmod(r, 3); c0, ck = divmod(c, 3)
        if rk == ck:
            out_[(r0, c0)] = out_.get((r0, c0), 0) + w[rk] * v
    return {k: sp.factor(sp.simplify(v)) for k, v in out_.items() if sp.simplify(v) != 0}


markov = {}
Kchoice = None
for name, w in (("diag(q^2,1,q^-2)", [q ** 2, 1, q ** -2]), ("diag(q^-2,1,q^2)", [q ** -2, 1, q ** 2])):
    tr = ptrace_last(Rc_q, 2, w)  # 3x3
    scalar = all(k[0] == k[1] for k in tr) and len({sp.simplify(v) for v in tr.values()}) == 1 and len(tr) == 3
    markov[name] = {"Tr_q,2(R) scalar": scalar, "value": str(sp.factor(tr.get((0, 0), 0))) if scalar else "not scalar"}
    if scalar and Kchoice is None:
        Kchoice = (name, w)
assert Kchoice is not None, "no Markov weight"
wK = Kchoice[1]
norm = sp.factor(sum(wK))
clos_L1 = {k: sp.factor(v / norm) for k, v in ptrace_last(V3, 3, wK).items()}
a1, b1, om1 = omega_coef_2(clos_L1)
ser_om1 = series_rat(om1)
ordL1, X_loop_L1 = leading(ser_om1)

# ---------------- L2: convention-D conditional expectation on H3 coords ----------------
hbasis = [ident(27, sp.Integer(1)), Rc12, Rc23, mmul(Rc12, Rc23), mmul(Rc23, Rc12), mmul(mmul(Rc12, Rc23), Rc12)]
hnames = ["1", "s0", "s1", "s0s1", "s1s0", "s0s1s0"]
keys = sorted(set().union(*[set(bb) for bb in hbasis], set(V3)))
Mh = sp.Matrix([[bb.get(k, 0) for bb in hbasis] for k in keys])
vh = sp.Matrix([V3.get(k, 0) for k in keys])
sol, params = Mh.gauss_jordan_solve(vh)
assert len(params) == 0
hc = dict(zip(hnames, [sp.factor(sp.simplify(s)) for s in sol]))
zD = q ** 3 / (q ** 2 + 1)
# E(1)=1, E(s0)=s0, E(s1)=z, E(s0 s1)=E(s1 s0)=z s0, E(s0 s1 s0)= z s0^2 = z (h s0 + 1)
alpha = sp.factor(hc["1"] + zD * hc["s1"] + zD * hc["s0s1s0"])
beta = sp.factor(hc["s0"] + zD * (hc["s0s1"] + hc["s1s0"]) + zD * hq * hc["s0s1s0"])
clos_L2 = madd((alpha, ident(9, sp.Integer(1))), (beta, Rc_q))
a2, b2, om2 = omega_coef_2(clos_L2)
ser_om2 = series_rat(om2)
ordL2, X_loop_L2 = leading(ser_om2)
# sanity: E_D(1) = 1 and E_D(V3) at q = 1 is 1
assert sp.simplify(alpha.subs(q, 1) - 1) == 0 and sp.simplify(beta.subs(q, 1)) == 0


def verdict_i(Xl, ol):
    if X_ff is None or Xl == 0:
        return {"r": None, "hit": False, "orders(ff,loop)": [ord_ff, ol],
                "reason": "MISS: X_ff is not defined. The G-coefficient of W4 is 0 at hbar^1, hbar^2 (where "
                          "'mod degree<=2 span' is defined) and from hbar^3 on the projection leaves span(deg<=2)+G, "
                          "so the pre-registered G-coefficient does not exist; G = -[[O12,O23],O34] is itself "
                          "degree 3, so taking it 'mod degree<=3' would be meaningless. X_loop is first nonzero at "
                          "hbar^%s; no scale-free ratio exists." % ol}
    r = sp.nsimplify(sp.Rational(X_ff) / Xl) if not isinstance(X_ff, sp.Basic) else sp.nsimplify(X_ff / Xl)
    same = (ol == ord_ff)
    opp = bool(sp.sign(X_ff) != sp.sign(Xl))
    hit = same and opp and abs(r) == HIT_RATIO
    return {"r": str(r), "same_hbar_order": same, "orders(ff,loop)": [ord_ff, ol], "opposite_sign": opp,
            "|r|==33/2": abs(r) == HIT_RATIO, "hit": hit,
            "reason": "MISS: orders differ, ratio carries hbar^%d (not scale-free)" % (ol - ord_ff) if not same else
                      ("HIT" if hit else "MISS: |r| != 33/2 or same sign")}


out["i_loop"] = {
    "L1_markov_weight_check": markov, "L1_weight_used": Kchoice[0],
    "L1_closure_(a,b)_in_a*1+b*P": [str(a1), str(b1)], "L1_Omega_coef": str(om1),
    "L1_Omega_coef_series": [str(x) for x in ser_om1], "L1_X_loop": str(X_loop_L1), "L1_order": ordL1,
    "V3_H3_coords": {k: str(v) for k, v in hc.items()},
    "L2_E_D(V3)_=alpha+beta*s0": [str(alpha), str(beta)], "L2_Omega_coef": str(om2),
    "L2_Omega_coef_series": [str(x) for x in ser_om2], "L2_X_loop": str(X_loop_L2), "L2_order": ordL2,
}
out["i_verdict"] = {"L1": verdict_i(X_loop_L1, ordL1), "L2": verdict_i(X_loop_L2, ordL2)}

# =====================================================================================
# (ii) hbar^2 relative corrections
# =====================================================================================
cF = -(q - 1) ** 2 * (q + 1) ** 4 * (q ** 4 + 1) / (2 * q ** 5)
cH = (q - 1) ** 2 * (q + 1) ** 2 * (q ** 4 + 1) / (2 * q ** 4)
sF, sH = series_rat(cF, 7), series_rat(cH, 7)
assert sF[0] == sF[1] == sF[3] == sF[5] == 0 and sH[1] == sH[3] == sH[5] == 0
b = sp.nsimplify(sF[4] / sF[2]); bp = sp.nsimplify(sH[4] / sH[2])
closed_F = sp.simplify(sp.expand(sp.sympify(cF).subs(q, sp.exp(hb)).rewrite(sp.exp)
                       - (-16 * sp.sinh(hb) ** 2 * sp.cosh(hb / 2) ** 2 * sp.cosh(2 * hb)).rewrite(sp.exp)))
cands_ii = {"b": b, "2b": 2 * b, "b'": bp, "2b'": 2 * bp}
out["ii"] = {"c_F_series": [str(x) for x in sF], "c_F_closed_form_-16sinh^2(h)cosh^2(h/2)cosh(2h)_check": str(closed_F),
             "H3_comm_series": [str(x) for x in sH],
             "values": {k: str(v) for k, v in cands_ii.items()},
             "in_S": {k: v in S_SET for k, v in cands_ii.items()},
             "hit": any(v in S_SET for v in cands_ii.values()),
             "disclosure": "b = 31/12 and b' = 7/3 were hand-computed before the run (prereg); recorded check, not a blind test"}

# =====================================================================================
# (iii) Casimir slope of [hbar^2] Haar(V^3) on 10, 8, 8, 1
# =====================================================================================
S3 = [tuple(p) for p in itertools.permutations(range(3))]
cS3 = commutant_coords(V3, S3, 3)
c2 = [series_rat(sp.factor(c), 3)[2] for c in cS3]
c0 = [series_rat(sp.factor(c), 3)[0] for c in cS3]


def sgn(p):
    return (-1) ** (3 - ncycles(p))


# standard 2-dim rep of S3 via the action on {x in Q^3 : sum x = 0} (basis e0-e1, e1-e2), permuting slots
def std_rep(p):
    basis = [sp.Matrix([1, -1, 0]), sp.Matrix([0, 1, -1])]
    B = sp.Matrix.hstack(*basis)
    imgs = []
    for v in basis:
        w = sp.zeros(3, 1)
        for s in range(3):
            w[p[s]] = v[s]
        imgs.append(w)
    return (B.T * B).inv() * B.T * sp.Matrix.hstack(*imgs)


lam10 = sp.nsimplify(sum(c2))
lam1 = sp.nsimplify(sum(c * sgn(p) for c, p in zip(c2, S3)))
M8 = sum((c * std_rep(p) for c, p in zip(c2, S3)), sp.zeros(2))
ev8 = [sp.nsimplify(e) for e in M8.eigenvals(multiple=True)]
a_C = lam1
beta_C = sp.nsimplify((lam10 - lam1) / 6)
pred8 = a_C + 3 * beta_C
consistent = all(sp.simplify(e - pred8) == 0 for e in ev8)
cands_iii = {"beta_C": beta_C, "beta_C*C_A": 3 * beta_C}
out["iii"] = {"Haar(V3)_hbar0_S3_coords": dict(zip(map(str, S3), map(str, c0))),
              "Haar(V3)_hbar2_S3_coords": dict(zip(map(str, S3), map(str, c2))),
              "eigenvalue_10_(C2=6)": str(lam10), "eigenvalue_1_(C2=0)": str(lam1),
              "eigenvalues_8_block_(C2=3)": [str(e) for e in ev8],
              "linear_in_C2_prediction_on_8": str(pred8), "single_Casimir_slope_consistent": consistent,
              "values": {k: str(v) for k, v in cands_iii.items()},
              "hit": bool(consistent and any(v in S_SET for v in cands_iii.values())),
              "structure": "[hbar^2] Haar(V3) = 4(C - C^2) = -16 F: the flip-odd 3-cycle difference, which is NOT "
                           "central in Q[S3] (a transposition swaps C and C^2). It is 0 on the 10 and the 1 and "
                           "acts on the 8 multiplicity block with eigenvalues +-4 sqrt(3) i; no function of C2 can "
                           "represent it.",
              "reason": "MISS by construction: no single Casimir slope" if not consistent else
                        ("HIT" if any(v in S_SET for v in cands_iii.values()) else "MISS: slope not in S")}

out["n_f"] = ("No flavour count exists: the three strands are the three quarks of one baryon; the closure "
              "closes one fixed strand. n_f-dependence of beta0 has no counterpart in the searched constructions.")
out["verdict"] = {"i_L1": out["i_verdict"]["L1"]["hit"], "i_L2": out["i_verdict"]["L2"]["hit"],
                  "ii": out["ii"]["hit"], "iii": out["iii"]["hit"],
                  "overall": "HIT somewhere (coincidence candidate only)" if any(
                      [out["i_verdict"]["L1"]["hit"], out["i_verdict"]["L2"]["hit"], out["ii"]["hit"], out["iii"]["hit"]])
                  else "MISS on all pre-registered candidates (scope a)"}
with open(os.path.join(HERE, "mn_beta0_from_braid_probe.out.json"), "w") as fh:
    json.dump(out, fh, indent=2, default=str)
print(json.dumps(out, indent=2, default=str))
