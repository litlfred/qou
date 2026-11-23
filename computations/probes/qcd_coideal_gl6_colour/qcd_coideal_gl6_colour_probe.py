#!/usr/bin/env python3
"""The (gl6, gl3+gl3) quantum-symmetric-pair coideal as colour on colour(x)flavour (C^3(x)C^2)^(x)n.

Bean qou-ni4b.  Pre-registration: PREREGISTRATION-gl6-coideal-colour.md (pushed before this file).

Setting (as ../qcd_coideal_colour): Jimbo U_q(gl6) on C^6, coproduct variant B (Kolb)
    Delta E = E(x)1 + K(x)E,  Delta F = F(x)K^-1 + 1(x)F,  Delta K = K(x)K,
R = jimbo_R(6, upper=True) (same function as the sibling probe).
Satake AIII quasi-split, X = empty, tau(i) = 6 - i, s_3 = 0:
    B_i = F_i - c_i E_tau(i) K_i^-1  (i = 1..5),  T_j = K_eps_j K_eps_(7-j)  (j = 1,2,3)
c1, c2, c3 FREE symbols; c4 = c2, c5 = c1 (Kolb admissibility, checked at q = 1 in Q2).
Labelling v1..v6 = (1u)(2u)(3u)(3d)(2d)(1d)  (the tau-orbit structure).
Colour candidate B^col = <B1, B2, B4, B5, T1, T2, T3> (node 3 removed).

Exact: sparse matrices with entries in QQ(q, c1, c2, c3, a, b). No float. q0 not used.
"""
import itertools
import json
import sys
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

q, c1, c2, c3, fa, fb = sp.symbols("q c1 c2 c3 a b")
DOM = sp.QQ.frac_field(q, c1, c2, c3, fa, fb)
Q = DOM.from_sympy(q)
ONE, ZERO = DOM.one, DOM.zero
H = Q - 1 / Q
CS = {1: DOM.from_sympy(c1), 2: DOM.from_sympy(c2), 3: DOM.from_sympy(c3), 4: DOM.from_sympy(c2),
      5: DOM.from_sympy(c1)}
HERE = Path(__file__).resolve().parent
CHECKS, OUT = [], {}
N = 6


def check(name, ok, detail="", kind="prereg"):
    CHECKS.append({"name": name, "pass": bool(ok), "detail": str(detail), "kind": kind})
    print(("PASS " if ok else "FAIL ") + ("[posthoc] " if kind == "posthoc" else "") + name
          + ("  -- " + str(detail) if detail else ""), flush=True)


def S(x):
    return sp.factor(DOM.to_sympy(x))


# ---------------------------------------------------------------- sparse matrices over DOM
class M:
    __slots__ = ("d", "e")

    def __init__(self, d, e=None):
        self.d = d
        self.e = e or {}

    @staticmethod
    def eye(d):
        return M(d, {(i, i): ONE for i in range(d)})

    @staticmethod
    def diag(vals):
        return M(len(vals), {(i, i): v for i, v in enumerate(vals) if v != ZERO})

    @staticmethod
    def unit(d, a, b):
        return M(d, {(a, b): ONE})

    def __add__(self, o):
        e = dict(self.e)
        for k, v in o.e.items():
            w = e.get(k, ZERO) + v
            if w == ZERO:
                e.pop(k, None)
            else:
                e[k] = w
        return M(self.d, e)

    def scale(self, s):
        if s == ZERO:
            return M(self.d)
        return M(self.d, {k: v * s for k, v in self.e.items()})

    def __sub__(self, o):
        return self + o.scale(-ONE)

    def __matmul__(self, o):
        rows = {}
        for (i, k), v in self.e.items():
            rows.setdefault(k, []).append((i, v))
        e = {}
        for (k, j), w in o.e.items():
            for i, v in rows.get(k, ()):
                key = (i, j)
                x = e.get(key, ZERO) + v * w
                if x == ZERO:
                    e.pop(key, None)
                else:
                    e[key] = x
        return M(self.d, e)

    def kron(self, o):
        e = {}
        for (i, j), v in self.e.items():
            for (k, l), w in o.e.items():
                e[(i * o.d + k, j * o.d + l)] = v * w
        return M(self.d * o.d, e)

    def iszero(self):
        return not self.e

    def tr(self):
        return sum((v for (i, j), v in self.e.items() if i == j), ZERO)

    def subs_q1(self):
        """entrywise q -> 1 (entries are polynomial/rational without pole at q = 1 here)."""
        out = {}
        for k, v in self.e.items():
            x = sp.cancel(DOM.to_sympy(v).subs(q, 1))
            if x != 0:
                out[k] = x
        return out

    def dense(self):
        A = sp.zeros(self.d, self.d)
        for (i, j), v in self.e.items():
            A[i, j] = DOM.to_sympy(v)
        return A


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = out.kron(m)
    return out


def comm(A, B):
    return A @ B - B @ A


I6 = M.eye(N)
E = [M.unit(N, i, i + 1) for i in range(5)]
F = [M.unit(N, i + 1, i) for i in range(5)]


def Keps(j, p=1):
    v = [ONE] * N
    v[j] = Q ** p
    return M.diag(v)


def Kroot(i, p=1):
    v = [ONE] * N
    v[i] = Q ** p
    v[i + 1] = Q ** (-p)
    return M.diag(v)


TAU = [4, 3, 2, 1, 0]                                   # 0-indexed node i -> tau(i)


def jimbo_R(Nn, upper=True):
    """Copied in form from qcd_coideal_colour_probe.jimbo_R (entries now in DOM)."""
    e = {}
    for a in range(Nn):
        for b in range(Nn):
            col = a * Nn + b
            if a == b:
                e[(col, col)] = Q
            else:
                e[(b * Nn + a, col)] = ONE
                if (a < b) == upper:
                    e[(col, col)] = e.get((col, col), ZERO) + H
    return M(Nn * Nn, e)


R = jimbo_R(N)


def sigma(n, i, Rm=R, d=N):
    return kron(*([M.eye(d)] * i + [Rm] + [M.eye(d)] * (n - i - 2)))


# ---------------------------------------------------------------- coproducts
def Dlet(n, kind, i):
    """Delta^n of a letter. kind in E,F,K,Ki (simple root i) or Ke,Kei (eps_j)."""
    if kind == "K":
        return kron(*([Kroot(i)] * n))
    if kind == "Ki":
        return kron(*([Kroot(i, -1)] * n))
    if kind == "Ke":
        return kron(*([Keps(i)] * n))
    if kind == "Kei":
        return kron(*([Keps(i, -1)] * n))
    out = M(N ** n)
    for p in range(n):
        if kind == "E":
            fac = [Kroot(i)] * p + [E[i]] + [I6] * (n - p - 1)
        else:
            fac = [I6] * p + [F[i]] + [Kroot(i, -1)] * (n - p - 1)
        out = out + kron(*fac)
    return out


def word_mat(n, word):
    out = M(N ** n)
    for coef, letters in word:
        X = M.eye(N ** n)
        for kind, i in letters:
            X = X @ Dlet(n, kind, i)
        out = out + X.scale(coef)
    return out


def Bword(i):            # 0-indexed node
    return [(ONE, (("F", i),)), (-CS[i + 1], (("E", TAU[i]), ("Ki", i)))]


def Tword(j, p=1):
    if p == 1:
        return [(ONE, (("Ke", j), ("Ke", 5 - j)))]
    return [(ONE, (("Kei", j), ("Kei", 5 - j)))]


GENS_B = {f"B{i + 1}": Bword(i) for i in range(5)}
GENS_B.update({f"T{j + 1}": Tword(j) for j in range(3)})
COL_NAMES = ["B1", "B2", "B4", "B5", "T1", "T2", "T3"]
EPS = {k: (ONE if k.startswith("T") else ZERO) for k in GENS_B}
_cache = {}


def G(n, name):
    key = (n, name)
    if key not in _cache:
        _cache[key] = word_mat(n, GENS_B[name])
    return _cache[key]


def nullspace(rows, nvars):
    if not rows:
        return [[ONE if j == k else ZERO for j in range(nvars)] for k in range(nvars)]
    A = DomainMatrix(rows, (len(rows), nvars), DOM)
    ns = A.nullspace()
    if ns.shape[0] == 0:
        return []
    return [list(r) for r in ns.to_list()]


# ================================================================ Q0 calibration
def Q0():
    ok = True
    for i in range(5):
        for kind in ("E", "F", "K"):
            X = Dlet(2, kind, i)
            ok &= comm(R, X).iszero()
    for j in range(6):
        ok &= comm(R, Dlet(2, "Ke", j)).iszero()
    check("Q0 R commutes with Delta(E_i), Delta(F_i), Delta(K_i), Delta(K_eps_j) on V(x)V (variant B)", ok)
    Id = M.eye(36)
    hk = ((R - Id.scale(Q)) @ (R + Id.scale(1 / Q))).iszero()
    s1, s2 = sigma(3, 0), sigma(3, 1)
    br = (s1 @ s2 @ s1 - s2 @ s1 @ s2).iszero()
    check("Q0/(c) Hecke (sigma-q)(sigma+q^-1)=0 on V(x)V and braid relation on V^(x)3", hk and br)
    return hk and br


# ================================================================ Q1 coideal
def Q1():
    ok = True
    torus_in_B = True
    for i in range(5):
        t = TAU[i]
        lhs = G(2, f"B{i + 1}")
        first = Kroot(t) @ Kroot(i, -1)
        rhs = (G(1, f"B{i + 1}").kron(Kroot(i, -1)) + I6.kron(F[i])
               - first.kron(E[t] @ Kroot(i, -1)).scale(CS[i + 1]))
        ok &= (lhs - rhs).iszero()
        # first leg = K_tau(i) K_i^-1 must be a monomial in T1,T2,T3 (theta-fixed torus)
        d = [first.e.get((k, k), ONE) for k in range(N)]
        torus_in_B &= all(d[k] == d[5 - k] for k in range(N))
    check("Q1a Delta(B_i) = B_i(x)K_i^-1 + 1(x)F_i - c_i K_tau(i)K_i^-1 (x) E_tau(i)K_i^-1 on V(x)V, i=1..5", ok)
    check("Q1a first legs K_tau(i)K_i^-1 are theta-fixed (diag symmetric under j <-> 7-j), so lie in <T1,T2,T3>"
          " -- B and B^col are right coideals", torus_in_B)
    okb = True
    for n in (2, 3):
        sig = [sigma(n, i) for i in range(n - 1)]
        for name in GENS_B:
            X = G(n, name)
            for s in sig:
                okb &= comm(s, X).iszero()
    check("Q1b/(b) every Delta^n(generator of B) commutes with every sigma_i, n = 2,3 (structural: B in U_q(gl6))",
          okb)
    P = {}
    for a in range(N):
        for b in range(N):
            P[(b * N + a, a * N + b)] = 1
    tr = R.subs_q1() == P
    check("Q1c/(f) transport: R|_(q=1) = P on C^6(x)C^6 = P_c (x) P_f", tr)
    return okb, tr


# ================================================================ Q2 classical fixed algebra
def lie_closure_dim(mats, dom):
    """dimension of the Lie algebra generated by sympy 6x6 matrices, exact over `dom`."""
    vecs = []

    def rank(vs):
        if not vs:
            return 0
        return DomainMatrix([[dom.from_sympy(sp.together(x)) for x in v] for v in vs], (len(vs), 36), dom).rank()
    basis = []
    for X in mats:
        if rank([list(Y) for Y in basis + [X]]) > len(basis):
            basis.append(X)
    changed = True
    while changed:
        changed = False
        for A in list(basis):
            for B in list(basis):
                C = sp.expand(A * B - B * A)
                if any(x != 0 for x in C) and rank([list(Y) for Y in basis + [C]]) > len(basis):
                    basis.append(C)
                    changed = True
    return len(basis), basis


def classical_gen(name, cvals=None):
    X = G(1, name)
    if name.startswith("T"):
        A = X.dense()
        return sp.diff(A, q).subs(q, 1)
    A = X.dense().subs(q, 1)
    if cvals is not None:
        A = A.subs(cvals)
    return A


def colour_op_on_v(X3):
    """X (3x3 colour) (x) 1_flavour in the v-labelling (1u)(2u)(3u)(3d)(2d)(1d)."""
    A = sp.zeros(6, 6)
    for a in range(3):
        for b in range(3):
            A[a, b] = X3[a, b]
            A[5 - a, 5 - b] = X3[a, b]
    return A


def Q2():
    domc = sp.QQ.frac_field(c1, c2, c3)
    cl = [classical_gen(nm) for nm in GENS_B]
    dimB, _ = lie_closure_dim(cl, domc)
    OUT["Q2_classical_lie_dim_B"] = dimB
    check("Q2 q->1 Lie closure of B has dim 18 = dim(gl3+gl3) (c1,c2,c3 symbolic)", dimB == 18, f"dim {dimB}")
    # unconstrained c4, c5 (specialised rational point; rank is lower semicontinuous so this bounds generic dim)
    c4u, c5u = sp.Rational(3), sp.Rational(7)
    cl_u = []
    for i in range(5):
        ci = {1: sp.Rational(2), 2: sp.Rational(5), 3: sp.Rational(11), 4: c4u, 5: c5u}[i + 1]
        A = (F[i].dense() - ci * E[TAU[i]].dense()).subs(q, 1)
        cl_u.append(A)
    cl_u += [classical_gen(f"T{j + 1}") for j in range(3)]
    dimU, _ = lie_closure_dim(cl_u, sp.QQ)
    OUT["Q2_classical_lie_dim_B_unconstrained_c(2,5,11,3,7)"] = dimU
    check("Q2 with c4 != c2, c5 != c1 (rational point c=(2,5,11,3,7)) the q->1 closure is larger than 18, so"
          " Kolb's c_i = c_tau(i) is forced by the classical limit, not chosen", dimU > 18, f"dim {dimU}")
    clc = [classical_gen(nm) for nm in COL_NAMES]
    dimC, basisC = lie_closure_dim(clc, domc)
    OUT["Q2_classical_lie_dim_Bcol"] = dimC
    check("Q2 q->1 Lie closure of B^col has dim 9 (gl3: colour sl3 plus colour Cartan incl. centre)", dimC == 9,
          f"dim {dimC}")
    # explicit colour form after d-block rescaling D = diag(1, -1/c1, 1/(c1 c2)) on colours of the d-block
    Dd = [1, -1 / c1, 1 / (c1 * c2)]
    Phi = sp.diag(1, 1, 1, Dd[2], Dd[1], Dd[0])        # v4=(3d), v5=(2d), v6=(1d)
    targets = {"B1": colour_op_on_v(sp.Matrix(3, 3, lambda a, b: 1 if (a, b) == (1, 0) else 0)),
               "B2": colour_op_on_v(sp.Matrix(3, 3, lambda a, b: 1 if (a, b) == (2, 1) else 0)),
               "B5": colour_op_on_v(sp.Matrix(3, 3, lambda a, b: -c1 if (a, b) == (0, 1) else 0)),
               "B4": colour_op_on_v(sp.Matrix(3, 3, lambda a, b: -c2 if (a, b) == (1, 2) else 0))}
    ok = True
    for nm, T in targets.items():
        ok &= sp.simplify(Phi * classical_gen(nm) * Phi.inv() - T) == sp.zeros(6, 6)
    for j in range(3):
        X3 = sp.zeros(3, 3)
        X3[j, j] = 1
        ok &= sp.simplify(classical_gen(f"T{j + 1}") - colour_op_on_v(X3)) == sp.zeros(6, 6)
    check("Q2 after the d-block colour rescaling diag(1,-1/c1,1/(c1c2)) the classical B^col generators are exactly"
          " sl3/gl3 (x) 1_flavour: f_i -> E_(i+1,i)(x)1, e_i -> -c_i E_(i,i+1)(x)1", ok)
    # the node-3 generator classically: E33 (x) (flavour mixing)
    B3 = classical_gen("B3")
    OUT["Q2_classical_B3"] = str(B3)
    mix = (B3[2, 3] != 0 and B3[3, 2] != 0)
    check("Q2 the removed node-3 generator is the only flavour-mixing one: B3|_(q=1) = E^c_33 (x) [[0,-c3],[1,0]]"
          " (u<->d at colour 3)", mix and sp.simplify(B3 - sp.Matrix(6, 6, lambda r, s: (1 if (r, s) == (3, 2)
                                                                                      else (-c3 if (r, s) == (2, 3)
                                                                                            else 0)))) == sp.zeros(6, 6),
          str(B3))


# ================================================================ Q3 relations of B^col at generic q
def Q3():
    res = {}
    allok = True
    for n in (1, 2, 3):
        e = {1: G(n, "B5"), 2: G(n, "B4")}
        f = {1: G(n, "B1"), 2: G(n, "B2")}
        T = [G(n, f"T{j + 1}") for j in range(3)]
        Ti = [word_mat(n, Tword(j, -1)) for j in range(3)]
        k = {1: T[0] @ Ti[1], 2: T[1] @ Ti[2]}
        ki = {1: Ti[0] @ T[1], 2: Ti[1] @ T[2]}
        Cart = [[2, -1], [-1, 2]]
        # weights
        w_ok = True
        for i in (1, 2):
            for j in (1, 2):
                a = Cart[i - 1][j - 1]
                w_ok &= (k[i] @ e[j] @ ki[i] - e[j].scale(Q ** a)).iszero()
                w_ok &= (k[i] @ f[j] @ ki[i] - f[j].scale(Q ** (-a))).iszero()
        # [e_i, f_i] = -c_i (k_i - k_i^-1)/(q - q^-1)
        ef_ok = True
        for i in (1, 2):
            lhs = comm(e[i], f[i])
            rhs = (k[i] - ki[i]).scale(-CS[i] / H)
            ef_ok &= (lhs - rhs).iszero()
        # Serre
        two = Q + 1 / Q
        se_ok = True
        for X in (f, e):
            for i, j in ((1, 2), (2, 1)):
                Y = X[i] @ X[i] @ X[j] - (X[i] @ X[j] @ X[i]).scale(two) + X[j] @ X[i] @ X[i]
                se_ok &= Y.iszero()
        # mixed: e1 f2 - q^m f2 e1
        mixed = {}
        for (i, j) in ((1, 2), (2, 1)):
            found = None
            for m in (0, 1, -1, 2, -2):
                if (e[i] @ f[j] - (f[j] @ e[i]).scale(Q ** m)).iszero():
                    found = m
                    break
            mixed[f"e{i}f{j}"] = found
        res[n] = {"weights": w_ok, "ef": ef_ok, "serre": se_ok, "mixed_q_power": mixed}
        allok &= w_ok and ef_ok and se_ok and all(v == 0 for v in mixed.values())
        print(f"   n={n}: {res[n]}", flush=True)
    OUT["Q3_relations"] = {str(k): v for k, v in res.items()}
    check("Q3/(a) on V^(x)n, n=1,2,3: with e_i = B_tau(i), f_i = B_i, k_1 = T1/T2, k_2 = T2/T3 the U_q(sl3) relations"
          " hold exactly with [e_i,f_i] = -c_i (k_i - k_i^-1)/(q-q^-1), q-Serre, and [e_i,f_j] = 0 (i != j)",
          allok, res)
    nz = all(not G(n, nm).iszero() for n in (1, 2, 3) for nm in ("B1", "B2", "B4", "B5"))
    check("Q3/(a) generators nonzero on every V^(x)n", nz)
    return allok and nz


# ================================================================ Q4 commutants and K-matrix
def commutant(names, n=1):
    d = N ** n
    mats = [G(n, nm) for nm in names]
    # unknown X (d x d): equations (X A - A X)_{rs} = 0, linear in X entries; index var (r,s) -> r*d+s
    rows = []
    for A in mats:
        eqs = {}
        for (k, s), v in A.e.items():          # (X A)_{r s} += X_{r k} A_{k s}
            for r in range(d):
                eqs.setdefault((r, s), {})
                eqs[(r, s)][r * d + k] = eqs[(r, s)].get(r * d + k, ZERO) + v
        for (r, k), v in A.e.items():          # (A X)_{r s} -= A_{r k} X_{k s}
            for s in range(d):
                eqs.setdefault((r, s), {})
                eqs[(r, s)][k * d + s] = eqs[(r, s)].get(k * d + s, ZERO) - v
        for row in eqs.values():
            if any(x != ZERO for x in row.values()):
                rr = [ZERO] * (d * d)
                for kk, x in row.items():
                    rr[kk] = x
                rows.append(rr)
    ns = nullspace(rows, d * d)
    return [M(d, {(i // d, i % d): x for i, x in enumerate(v) if x != ZERO}) for v in ns]


def Q4():
    comB = commutant(list(GENS_B))
    OUT["Q4_commutant_B_on_V_dim"] = len(comB)
    check("Q4 commutant of B (full, gl3+gl3) on C^6 has dim 2: span{1, J_q}", len(comB) == 2, f"dim {len(comB)}")
    comC = commutant(COL_NAMES)
    OUT["Q4_commutant_Bcol_on_V_dim"] = len(comC)
    OUT["Q4_commutant_Bcol_on_V_basis"] = [str(X.dense()) for X in comC]
    check("Q4 commutant of B^col on C^6 has dim 4 (the flavour matrices, conjugated)", len(comC) == 4,
          f"dim {len(comC)}")
    # K-matrix for full B: reflection equation on alpha*1 + beta*J0
    J0 = next(X for X in comB if not (X - I6.scale(X.e.get((0, 0), ZERO))).iszero())
    J0d = J0.dense()
    OUT["Q4_J0"] = str(J0d)
    al, be = sp.symbols("alpha beta")
    Rd = R.dense()
    Jg = al * sp.eye(6) + be * J0d
    T1 = sp.kronecker_product(Jg, sp.eye(6))
    RE = Rd * T1 * Rd * T1 - T1 * Rd * T1 * Rd
    nums = [sp.numer(sp.together(x)) for x in RE if sp.cancel(x) != 0]
    sol = sp.solve(nums, [al], dict=True) if nums else [{}]
    OUT["Q4_RE_solutions_alpha"] = [str(s) for s in sol]
    nontriv = [s for s in sol if al in s]
    Ksol = None
    if nontriv:
        Ksol = sp.simplify(Jg.subs(al, nontriv[0][al]).subs(be, 1))
        OUT["Q4_K_matrix"] = str(Ksol)
        lam = sp.symbols("lam")
        ev = sp.roots(sp.Poly(sp.numer(sp.together((Ksol - lam * sp.eye(6)).det())), lam))
        OUT["Q4_K_matrix_eigen"] = {str(sp.factor(k)): v for k, v in ev.items()}
        # does it commute with B on strand 1 for n = 2?
        KK = M(36)
        Kd = sp.kronecker_product(Ksol, sp.eye(6))
        for r in range(36):
            for s in range(36):
                if Kd[r, s] != 0:
                    KK.e[(r, s)] = DOM.from_sympy(sp.together(Kd[r, s]))
        okc = all(comm(KK, G(2, nm)).iszero() for nm in GENS_B)
        OUT["Q4_K_on_strand1_commutes_with_Delta2_B"] = okc
    check("Q4 the reflection equation has a non-scalar solution on the B-commutant pencil (K-matrix)",
          Ksol is not None, OUT.get("Q4_RE_solutions_alpha"))
    return comC


# ================================================================ K4 question
def K4q():
    # 1_c (x) sigma_x and 1_c (x) sigma_z on one strand, v-labelling
    Sx = M(6, {(a, 5 - a): ONE for a in range(6)})
    Sz = M.diag([ONE, ONE, ONE, -ONE, -ONE, -ONE])
    res = {}
    for nm in ("B1", "B2", "B4", "B5"):
        X1 = G(1, nm)
        X2 = G(2, nm)
        res[nm] = {
            "strand1_commutes_1c_sz": comm(X1, Sz).iszero(),
            "V(x)V_commutes_1(x)(1c(x)sx)": comm(X2, I6.kron(Sx)).iszero(),
            "V(x)V_commutes_1(x)(1c(x)sz)": comm(X2, I6.kron(Sz)).iszero(),
            "V(x)V_commutes_(1c(x)sz)(x)1": comm(X2, Sz.kron(I6)).iszero(),
        }
        # at q = 1 does it commute with 1(x)(1c(x)sx)?  (classical Delta = x(x)1 + 1(x)x, flavour-blind up to c)
        C = comm(X2, I6.kron(Sx)).subs_q1()
        res[nm]["q=1_commutator_with_1(x)sx_entries_nonzero"] = len(C)
    OUT["K4_flavour_dependence"] = res
    # coideal coproduct of B1 on strand 2 acts with different first legs on u and d:
    #   1(x)F_1 (u-flavour, first leg 1)  vs  -c1 K5K1^-1 (x) E_5K1^-1 (d-flavour, first leg K5K1^-1 != 1)
    first_leg_d = Kroot(4) @ Kroot(0, -1)
    non_trivial = not (first_leg_d - I6).iszero()
    ok = non_trivial and all(not r["V(x)V_commutes_1(x)(1c(x)sx)"] for r in res.values())
    check("K4 at generic q, Delta^2(B_i) (i=1,2,4,5) does NOT commute with 1(x)(1_c(x)sigma_x): the colour action on"
          " strand 2 depends on its flavour (first leg 1 on u, K_tau(i)K_i^-1 != 1 on d), so it is not of the"
          " K4 form Delta_H(x)(x)1_flavour", ok, res)
    # at q = 1 with c = -1 the classical coproduct x(x)1 + 1(x)x of sl3(x)1 commutes with flavour
    Csp = {}
    for nm in ("B1", "B5"):
        X2 = G(2, nm).dense().subs({q: 1, c1: -1, c2: -1})
        Sxd = sp.kronecker_product(sp.eye(6), Sx.dense())
        Csp[nm] = sp.simplify(X2 * Sxd - Sxd * X2) == sp.zeros(36, 36)
    check("K4 at q = 1 and c = -1 the same operators commute with 1(x)(1_c(x)sigma_x) (classical colour sl3(x)1);"
          " the flavour dependence is a q != 1 effect", all(Csp.values()), Csp, kind="posthoc")


# ================================================================ Q5 singlets
COLOUR = [0, 1, 2, 2, 1, 0]
FLAV = [0, 0, 0, 1, 1, 1]


def idx(tup):
    r = 0
    for t in tup:
        r = r * N + t
    return r


def untup(r, n):
    out = []
    for _ in range(n):
        out.append(r % N)
        r //= N
    return tuple(reversed(out))


def singlets(n):
    cols = [idx(t) for t in itertools.product(range(N), repeat=n)
            if sorted(COLOUR[x] for x in t) == list(range(3)) * (n // 3)]
    if not cols:
        return [], cols
    colpos = {c: k for k, c in enumerate(cols)}
    rows = []
    for nm in ("B1", "B2", "B4", "B5"):
        X = G(n, nm)
        eqs = {}
        for (r, s), v in X.e.items():
            if s in colpos:
                eqs.setdefault(r, {})[colpos[s]] = v
        for row in eqs.values():
            rr = [ZERO] * len(cols)
            for k, v in row.items():
                rr[k] = v
            rows.append(rr)
    ns = nullspace(rows, len(cols))
    vecs = [{cols[k]: x for k, x in enumerate(v) if x != ZERO} for v in ns]
    return vecs, cols


def apply(X, vec):
    out = {}
    for (r, s), v in X.e.items():
        if s in vec:
            out[r] = out.get(r, ZERO) + v * vec[s]
    return {k: v for k, v in out.items() if v != ZERO}


def coords(vecs, target):
    """solve target = sum x_k vecs[k] exactly."""
    keys = sorted(set().union(*[set(v) for v in vecs]) | set(target))
    A = DomainMatrix([[v.get(k, ZERO) for v in vecs] + [target.get(k, ZERO)] for k in keys],
                     (len(keys), len(vecs) + 1), DOM)
    rref, piv = A.rref()
    assert len(vecs) not in piv, "not in span"
    x = [ZERO] * len(vecs)
    L = rref.to_list()
    for r, p in enumerate(piv):
        x[p] = L[r][len(vecs)]
    return x


def restrict(X, vecs):
    cols = [coords(vecs, apply(X, v)) for v in vecs]
    k = len(vecs)
    return sp.Matrix(k, k, lambda i, j: DOM.to_sympy(cols[j][i]))


def multiplicities(tr1, trs1, trs1s2):
    m3, m21, m111 = sp.symbols("m3 m21 m111")
    sol = sp.solve([m3 + 2 * m21 + m111 - tr1,
                    m3 * q + m21 * (q - 1 / q) - m111 / q - trs1,
                    m3 * q**2 - m21 + m111 / q**2 - trs1s2], [m3, m21, m111], dict=True)[0]
    return {k: sp.simplify(v) for k, v in sol.items()}, (m3, m21, m111)


def flavour_model(Rf):
    Rf3 = [kron(Rf, M.eye(2)), kron(M.eye(2), Rf)]
    s1, s2 = Rf3
    return (sp.Integer(8), S((s1).tr()), S((s1 @ s2).tr()))


def jimbo2(upper=True):
    e = {}
    for a in range(2):
        for b in range(2):
            col = a * 2 + b
            if a == b:
                e[(col, col)] = Q
            else:
                e[(b * 2 + a, col)] = ONE
                if (a < b) == upper:
                    e[(col, col)] = e.get((col, col), ZERO) + H
    return M(4, e)


def markov_z(Rf, K):
    d = 2
    T = sp.zeros(d, d)
    for a in range(d):
        for b in range(d):
            T[a, b] = sum(DOM.to_sympy(Rf.e.get((a * d + c, b * d + c), ZERO)) * K[c] for c in range(d))
    scal = sp.cancel(T[0, 1]) == 0 and sp.cancel(T[1, 0]) == 0 and sp.cancel(T[0, 0] - T[1, 1]) == 0
    return scal, sp.factor(sp.cancel(T[0, 0] / sum(K)))


def Q5Q6(dc):
    v2, _ = singlets(2)
    OUT["Q5_singlets_V2_dim"] = len(v2)
    check("Q5 no B^col-invariant vector in V(x)V (no colour-weight-zero states for two strands)", len(v2) == 0)
    vecs, cols = singlets(3)
    OUT["Q5_singlets_V3_dim"] = len(vecs)
    OUT["Q5_colour_weight_zero_states_V3"] = len(cols)
    e_ok = len(vecs) == 8
    check("Q5/(e) B^col-invariants in V^(x)3 have dim 8 = 1 colour singlet x 2^3 flavour states", e_ok,
          f"dim {len(vecs)}")
    # torus invariance of the singlets
    ki_ok = True
    for j in range(3):
        for v in vecs:
            w = apply(G(3, f"T{j + 1}"), v)
            ki_ok &= all(w.get(k, ZERO) == Q * v.get(k, ZERO) for k in set(w) | set(v))
    check("Q5 each T_j acts on the singlets by q (colour weight (1,1,1)), so k_1, k_2 act by 1", ki_ok)
    s1, s2 = sigma(3, 0), sigma(3, 1)
    A1, A2 = restrict(s1, vecs), restrict(s2, vecs)
    I8 = sp.eye(8)
    hk = sp.simplify((A1 - q * I8) * (A1 + I8 / q)) == sp.zeros(8, 8)
    br = sp.simplify(A1 * A2 * A1 - A2 * A1 * A2) == sp.zeros(8, 8)
    check("Q5 the singlet sector is an H3-module (Hecke + braid on the restriction)", hk and br)
    tr1, trs1, trs1s2 = sp.Integer(8), sp.factor(sp.cancel(A1.trace())), sp.factor(sp.cancel((A1 * A2).trace()))
    mult, (m3, m21, m111) = multiplicities(tr1, trs1, trs1s2)
    OUT["Q5_singlet_sector_characters"] = {"tr1": 8, "tr_s1": str(trs1), "tr_s1s2": str(trs1s2)}
    OUT["Q5_singlet_sector_multiplicities"] = {str(k): str(v) for k, v in mult.items()}
    pred = mult[m3] == 0 and mult[m21] == 2 and mult[m111] == 4
    check("Q5 singlet sector = S^(1^3) x4 + S^(2,1) x2 (prediction)", pred, mult)
    Rf = jimbo2(True)
    Rfp = (Rf.scale(-ONE)) + M.eye(4).scale(H)          # -Rf^-1 = -Rf + h
    chf = flavour_model(Rf)
    chp = flavour_model(Rfp)
    mf, _ = multiplicities(*chf)
    mp_, _ = multiplicities(*chp)
    OUT["Q5_flavour_model_Rf_multiplicities"] = {str(k): str(v) for k, v in mf.items()}
    OUT["Q5_fermionic_model_-Rf^-1_multiplicities"] = {str(k): str(v) for k, v in mp_.items()}
    d_iso = sp.cancel(chf[1] - trs1) == 0 and sp.cancel(chf[2] - trs1s2) == 0
    ferm_iso = sp.cancel(chp[1] - trs1) == 0 and sp.cancel(chp[2] - trs1s2) == 0
    check("Q5/(d) the singlet sector is NOT H3-isomorphic to the flavour model sigma -> R_f (prediction)",
          not d_iso, f"flavour model {mf}")
    check("Q5 the singlet sector IS H3-isomorphic to the fermionic flavour model sigma -> -R_f^-1", ferm_iso,
          f"fermionic {mp_}")
    # q -> 1 sign invariant
    t1 = sp.limit(trs1, q, 1)
    check("Q5 invariant: at q = 1, tr(sigma_1) on the singlet sector is -4, while the flavour model gives +4"
          " (S3 sign character of the colour singlet)", t1 == -4 and sp.limit(chf[1], q, 1) == 4, f"{t1}")
    # Q6(iii) flavour Markov parameters with the gl2 pivotal K (upper convention: diag(q^-1, q))
    Kf = [1 / q, q]
    sc, z_f = markov_z(Rf, Kf)
    sp_, z_p = markov_z(Rfp, Kf)
    ZD = q**3 / (q**2 + 1)
    OUT["Q6_flavour_Rf_markov"] = {"scalar": sc, "z": str(z_f)}
    OUT["Q6_fermionic_markov"] = {"scalar": sp_, "z": str(z_p)}
    check("Q6 calibration: R_f with K_f = gl2 pivotal is Markov with z = z_D = q^3/(q^2+1)",
          sc and sp.cancel(z_f - ZD) == 0, z_f)
    check("Q6/(d) the singlet sector's (fermionic) flavour model is Markov with z = z_D(-q^-1) = -1/(q(q^2+1)),"
          " not z_D", sp_ and sp.cancel(z_p - ZD.subs(q, -1 / q)) == 0 and sp.cancel(z_p - ZD) != 0, z_p)
    # Q6(ii) colour-blind flavour twist G = 1_c (x) diag(a,b) on the singlet sector
    Gm = M.diag([DOM.from_sympy(fa)] * 3 + [DOM.from_sympy(fb)] * 3)
    G3 = kron(Gm, Gm, Gm)
    comm_ok = all(comm(G3, G(3, nm)).iszero() for nm in COL_NAMES) and comm(G3, s1).iszero() \
        and comm(G3, s2).iszero()
    check("Q6 G^(x)3 = (1_c(x)diag(a,b))^(x)3 commutes with B^col and with sigma_1, sigma_2 on V^(x)3", comm_ok)
    Gs = restrict(G3, vecs)
    w1 = sp.factor(sp.cancel(Gs.trace()))
    ws1 = sp.factor(sp.cancel((Gs * A1).trace()))
    ws12 = sp.factor(sp.cancel((Gs * A1 * A2).trace()))
    wts, _ = multiplicities(w1, ws1, ws12)
    wts = {str(k): sp.factor(v) for k, v in wts.items()}
    OUT["Q6_trace_weights_on_singlet_sector_G=1c(x)diag(a,b)"] = {k: str(v) for k, v in wts.items()}
    w111 = wts["m111"]
    OUT["Q6_selection_flag_(a,b)_with_zero_weight_on_(1^3)_SELECTION_ONLY"] = str(sp.solve(sp.numer(w111), fb))
    check("Q6 the colour-blind twist puts nonzero weight on the S^(1^3) block for generic (a,b) (so it is not"
          " convention D, whose (1^3) weight is 0)", sp.cancel(w111) != 0, wts)
    return e_ok, d_iso


# ================================================================ Q6(i) product twists, Schur
def adstar(n, word):
    def let(kind, i):
        if kind in ("Ke", "Kei"):
            Ke, Kei = Dlet(n, "Ke", i), Dlet(n, "Kei", i)
            return (lambda C: Kei @ C @ Ke) if kind == "Ke" else (lambda C: Ke @ C @ Kei)
        Kd, Kdi = Dlet(n, "K", i), Dlet(n, "Ki", i)
        if kind == "E":
            X = Dlet(n, "E", i)
            return lambda C: C @ X - Kdi @ X @ C @ Kd
        if kind == "F":
            X = Dlet(n, "F", i)
            return lambda C: Kd @ C @ X - X @ Kd @ C
        if kind == "K":
            return lambda C: Kdi @ C @ Kd
        return lambda C: Kd @ C @ Kdi
    terms = [(coef, [let(k, i) for k, i in letters]) for coef, letters in word]

    def f(C):
        out = M(C.d)
        for coef, maps in terms:
            D = C
            for m in maps:
                D = m(D)
            out = out + D.scale(coef)
        return out
    return f


def invariant_twists_V(names):
    d = N
    basis = [M(d, {(r, s): ONE}) for r in range(d) for s in range(d)]
    imgs = {nm: [adstar(1, GENS_B[nm])(Bm) - Bm.scale(EPS[nm]) for Bm in basis] for nm in names}
    rows = []
    for nm in names:
        for r in range(d):
            for s in range(d):
                row = [im.e.get((r, s), ZERO) for im in imgs[nm]]
                if any(x != ZERO for x in row):
                    rows.append(row)
    ns = nullspace(rows, d * d)
    return [M(d, {(i // d, i % d): x for i, x in enumerate(v) if x != ZERO}) for v in ns]


def Q6i():
    PIV = M.diag([Q ** (-2 * (5 - j)) for j in range(6)])
    okp = all((adstar(1, [(ONE, ((k, i),))])(PIV) - (PIV if k in ("K",) else M(6))).iszero()
              for k in ("E", "F", "K") for i in range(5))
    check("Q6 calibration: gl6 pivotal diag(q^-10,...,1) is ad*-invariant under U_q(gl6)", okp)
    inv = invariant_twists_V(COL_NAMES)
    OUT["Q6_Bcol_invariant_twists_on_V_dim"] = len(inv)
    invB = invariant_twists_V(list(GENS_B))
    OUT["Q6_B_invariant_twists_on_V_dim"] = len(invB)
    s1_2 = sigma(2, 0)
    Z6 = q**6 * (q - 1 / q) / (q**6 - q**-6)
    zs = []
    trace_ok = True
    s1, s2 = sigma(3, 0), sigma(3, 1)
    for T in inv:
        G2 = T.kron(PIV)
        t2 = G2.tr()
        if t2 == ZERO:
            zs.append("tr=0")
            continue
        z = S((G2 @ s1_2).tr() / t2)
        zs.append(z)
        G3 = kron(T, PIV, PIV)
        for a in (M.eye(216), s1, s2, s1 @ s2):
            for b in (s1, s2):
                trace_ok &= (G3 @ comm(a, b)).tr() == ZERO
    OUT["Q6_product_twist_T1(x)piv_z_values"] = [str(z) for z in zs]
    allz6 = all(z == "tr=0" or sp.cancel(z - Z6) == 0 for z in zs)
    check(f"Q6(i) every B^col-invariant T1 on V ({len(inv)} of them) gives T1(x)piv a Markov parameter z6 = q^6/[6]_q"
          " (Schur: partial trace over later strands is a U_q(gl6)-scalar on irreducible C^6), never z_D",
          allz6 and trace_ok, zs)


def main():
    Q0()
    okb, tr = Q1()
    Q2()
    a_ok = Q3()
    Q4()
    K4q()
    e_ok, d_iso = Q5Q6(None)
    Q6i()
    npass = sum(c["pass"] for c in CHECKS)
    OUT["acceptance_a_to_f"] = {"a_Uq_sl3_relations": a_ok, "b_commutes": okb, "c_hecke_braid": True,
                                "d_singlet_sector_is_Rf_flavour_model_with_zD": d_iso,
                                "e_one_colour_singlet_per_flavour_state_dim8": e_ok, "f_transport": tr}
    OUT["checks"] = CHECKS
    OUT["summary"] = f"{npass}/{len(CHECKS)}"
    print(f"SUMMARY {npass}/{len(CHECKS)}")
    (HERE / "qcd_coideal_gl6_colour_probe.out.json").write_text(json.dumps(OUT, indent=1, default=str))
    sys.exit(0 if npass == len(CHECKS) else 1)


if __name__ == "__main__":
    main()
