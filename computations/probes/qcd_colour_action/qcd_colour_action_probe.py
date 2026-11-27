#!/usr/bin/env python3
"""qcd_colour_action_probe — colour action on the three-strand Hecke state module (bean qou-ni4b).

Pre-registration: PREREGISTRATION-colour-action.md (committed before this file). Constructions
K0-K4 and acceptance tests (a)-(f) are fixed there; every member is reported, none is selected.

Exact sympy over Q(q) (and Q(p,q)). No float64 anywhere. Operators are sparse column dicts on
W^{(x)n}; equalities are checked column by column with sympy.cancel.
Output: qcd_colour_action_probe.out.json (next to this file).
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

q, p = sp.symbols("q p", positive=True)
HERE = Path(__file__).resolve().parent
OUT: dict = {"checks": [], "constructions": {}}


def check(name, ok, detail=""):
    OUT["checks"].append({"name": name, "pass": bool(ok), "detail": str(detail)})
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    return bool(ok)


# ---------------------------------------------------------------- sparse operators
def mat_to_cols(M):
    cols = {}
    for j in range(M.shape[1]):
        col = {}
        for i in range(M.shape[0]):
            v = M[i, j]
            if v != 0:
                col[i] = v
        cols[j] = col
    return cols


class Op:
    """Linear operator on (C^d)^{(x)n}, stored as columns: basis tuple -> {tuple: coef}."""

    def __init__(self, d, n, cols):
        self.d, self.n, self.cols = d, n, cols

    @staticmethod
    def basis(d, n):
        return list(itertools.product(range(d), repeat=n))

    @classmethod
    def local(cls, d, n, M, sites):
        """M acts on the sites listed (1 or 2 consecutive sites); M is (d^k x d^k)."""
        k = len(sites)
        Mc = mat_to_cols(M)
        cols = {}
        for t in cls.basis(d, n):
            idx = 0
            for s in sites:
                idx = idx * d + t[s]
            col = {}
            for i, v in Mc[idx].items():
                digs = []
                r = i
                for _ in range(k):
                    digs.append(r % d)
                    r //= d
                digs = digs[::-1]
                tt = list(t)
                for s, g in zip(sites, digs):
                    tt[s] = g
                col[tuple(tt)] = col.get(tuple(tt), 0) + v
            cols[t] = col
        return cls(d, n, cols)

    @classmethod
    def identity(cls, d, n):
        return cls(d, n, {t: {t: sp.Integer(1)} for t in cls.basis(d, n)})

    def apply_vec(self, vec):
        out = {}
        for t, c in vec.items():
            for u, v in self.cols[t].items():
                out[u] = out.get(u, 0) + c * v
        return out

    def __matmul__(self, other):  # self after other
        return Op(self.d, self.n, {t: self.apply_vec(other.cols[t]) for t in other.cols})

    def lin(self, a, other, b):
        cols = {}
        for t in self.cols:
            col = {}
            for u, v in self.cols[t].items():
                col[u] = col.get(u, 0) + a * v
            for u, v in other.cols[t].items():
                col[u] = col.get(u, 0) + b * v
            cols[t] = col
        return Op(self.d, self.n, cols)

    def __add__(self, o):
        return self.lin(1, o, 1)

    def __sub__(self, o):
        return self.lin(1, o, -1)

    def scale(self, a):
        return Op(self.d, self.n, {t: {u: a * v for u, v in c.items()} for t, c in self.cols.items()})

    def is_zero(self, subs=None):
        for c in self.cols.values():
            for v in c.values():
                e = v if subs is None else v.subs(subs)
                if sp.cancel(sp.together(e)) != 0:
                    return False
        return True

    def first_nonzero(self):
        for t, c in self.cols.items():
            for u, v in c.items():
                e = sp.factor(sp.cancel(v))
                if e != 0:
                    return (t, u, e)
        return None


def comm(A, B):
    return A @ B - B @ A


# ---------------------------------------------------------------- building blocks
def E(n, i, j):
    M = sp.zeros(n, n)
    M[i, j] = 1
    return M


def jimbo(N, qq, order=None):
    """Jimbo gl_N R-check on C^N (x) C^N with the nucleon-matrix convention
    R(e_i e_i) = q e_i e_i; i<j: R(e_i e_j) = e_j e_i, R(e_j e_i) = e_i e_j + h e_j e_i.
    `order` maps basis index -> rank in the total order (default identity)."""
    rk = order or (lambda a: a)
    h = qq - 1 / qq
    M = sp.zeros(N * N, N * N)
    for a in range(N):
        for b in range(N):
            col = a * N + b
            if a == b:
                M[col, col] = qq
            elif rk(a) < rk(b):
                M[b * N + a, col] = 1
            else:
                M[b * N + a, col] = 1
                M[col, col] = h
    return M


def kron(*Ms):
    out = Ms[0]
    for M in Ms[1:]:
        out = sp.kronecker_product(out, M)
    return out


def swap_factors_2site(Mc, Mf, dc, df):
    """Two-site operator on (C^dc (x) C^df)^{(x)2} from colour op Mc on C^dc(x)C^dc and flavour op
    Mf on C^df(x)C^df. Strand basis index = c*df + f."""
    d = dc * df
    M = sp.zeros(d * d, d * d)
    for c1, f1, c2, f2 in itertools.product(range(dc), range(df), range(dc), range(df)):
        col = (c1 * df + f1) * d + (c2 * df + f2)
        for c1p, c2p in itertools.product(range(dc), range(dc)):
            a = Mc[c1p * dc + c2p, c1 * dc + c2]
            if a == 0:
                continue
            for f1p, f2p in itertools.product(range(df), range(df)):
                b = Mf[f1p * df + f2p, f1 * df + f2]
                if b == 0:
                    continue
                M[(c1p * df + f1p) * d + (c2p * df + f2p), col] += a * b
    return M


RF = jimbo(2, q)                       # nucleon matrix Rc (u = e1 over d)
assert RF == sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, q - 1 / q, 0], [0, 0, 0, q]])
RFinv = RF - (q - 1 / q) * sp.eye(4)
I4, I9 = sp.eye(4), sp.eye(9)
P3 = sp.zeros(9, 9)
for a, b in itertools.product(range(3), range(3)):
    P3[b * 3 + a, a * 3 + b] = 1
P2 = sp.zeros(4, 4)
for a, b in itertools.product(range(2), range(2)):
    P2[b * 2 + a, a * 2 + b] = 1
ZD = q**3 / (q**2 + 1)


# ---------------------------------------------------------------- generic tests
def hecke_braid(R2, d, qq=q, n=3):
    s1 = Op.local(d, n, R2, (0, 1))
    s2 = Op.local(d, n, R2, (1, 2))
    Id = Op.identity(d, n)
    hecke = ((s1 - Id.scale(qq)) @ (s1 + Id.scale(1 / qq))).is_zero()
    braid_op = s1 @ s2 @ s1 - s2 @ s1 @ s2
    braid = braid_op.is_zero()
    return s1, s2, hecke, braid, (None if braid else braid_op.first_nonzero())


def eigen_classes(R2):
    ev = sp.Matrix(R2).eigenvals()
    return sorted({sp.factor(k) for k in ev}, key=str)


def markov_z(R2, Kdiag, dstrand):
    """Partial quantum trace Tr_2((1(x)K) R) / Tr K; returns (is_scalar, z)."""
    d = dstrand
    T = sp.zeros(d, d)
    for a, b in itertools.product(range(d), range(d)):
        s = 0
        for c in range(d):
            s += R2[a * d + c, b * d + c] * Kdiag[c]
        T[a, b] = sp.cancel(s)
    scalar = all(T[a, b] == 0 for a in range(d) for b in range(d) if a != b) and \
        all(sp.cancel(T[a, a] - T[0, 0]) == 0 for a in range(d))
    z = sp.factor(sp.cancel(T[0, 0] / sum(Kdiag)))
    return scalar, z


def colour_gens_classical(dc, df, n, site_colour_index):
    """Classical gl3 E_ab acting on the colour factor of every strand (primitive coproduct)."""
    gens = {}
    for a, b in itertools.product(range(3), range(3)):
        M1 = kron(E(3, a, b), sp.eye(df)) if df > 1 else E(3, a, b)
        d = 3 * df
        tot = None
        for s in range(n):
            o = Op.local(d, n, M1, (s,))
            tot = o if tot is None else tot + o
        gens[(a, b)] = tot
    return gens


def su3_injective_and_brackets(gens):
    """(a) for classical colour: the eight traceless combinations are linearly independent operators
    and satisfy [E_ab, E_cd] = d_bc E_ad - d_da E_cb."""
    ok_br = True
    for (a, b), (c, d) in itertools.product(gens, gens):
        lhs = comm(gens[(a, b)], gens[(c, d)])
        rhs = None
        if b == c:
            rhs = gens[(a, d)]
        if d == a:
            rhs = gens[(c, b)].scale(-1) if rhs is None else rhs - gens[(c, b)]
        diff = lhs if rhs is None else lhs - rhs
        if not diff.is_zero():
            ok_br = False
            break
    # linear independence of the 8 sl3 operators: E_ab (a!=b), H1 = E00-E11, H2 = E11-E22
    ops = [gens[(a, b)] for a in range(3) for b in range(3) if a != b]
    ops += [gens[(0, 0)] - gens[(1, 1)], gens[(1, 1)] - gens[(2, 2)]]
    keys = sorted({(t, u) for o in ops for t, c in o.cols.items() for u in c})
    M = sp.Matrix([[o.cols[t].get(u, 0) for o in ops] for (t, u) in keys])
    rank = M.rank()
    return ok_br, rank


def uq_gens(pp, df, n, coprod):
    """U_p(gl3) Chevalley generators on the colour factor, through the coproduct `coprod`.
    coprod 'A': D(E)=E(x)K + 1(x)E, D(F)=F(x)1 + K^-1(x)F ; coprod 'B': D(E)=E(x)1 + K(x)E,
    D(F)=F(x)K^-1 + 1(x)F. K_i = diag on colour with p^{+1} at i, p^{-1} at i+1."""
    d = 3 * df
    Id1 = sp.eye(df)
    out = {}
    for i in (0, 1):
        Ei = kron(E(3, i, i + 1), Id1)
        Fi = kron(E(3, i + 1, i), Id1)
        Kd = [1, 1, 1]
        Kd[i], Kd[i + 1] = pp, 1 / pp
        Ki = kron(sp.diag(*Kd), Id1)
        Kinv = Ki.inv()
        one = sp.eye(d)

        def tens(ms):
            tot = None
            for s, m in enumerate(ms):
                o = Op.local(d, n, m, (s,))
                tot = o if tot is None else tot @ o
            return tot

        def coproduct_n(X, Kx, kind):
            # iterated coproduct of a skew-primitive: sum_s  [left factors] X_s [right factors]
            tot = None
            for s in range(n):
                ms = []
                for r in range(n):
                    if r == s:
                        ms.append(X)
                    elif kind == "XK":      # D(X) = X (x) K + 1 (x) X  -> left 1, right K
                        ms.append(Kx if r > s else one)
                    else:                   # D(X) = X (x) 1 + K (x) X  -> left K, right 1
                        ms.append(Kx if r < s else one)
                o = tens(ms)
                tot = o if tot is None else tot + o
            return tot
        if coprod == "A":
            Eo = coproduct_n(Ei, Ki, "XK")
            Fo = coproduct_n(Fi, Kinv, "KX")
        else:
            Eo = coproduct_n(Ei, Ki, "KX")
            Fo = coproduct_n(Fi, Kinv, "XK")
        Ko = tens([Ki] * n)
        Kio = tens([Kinv] * n)
        out[i] = (Eo, Fo, Ko, Kio)
    return out


def uq_relations(G, pp):
    ok = True
    for i in (0, 1):
        Ei, Fi, Ki, Kii = G[i]
        if not (comm(Ei, Fi) - (Ki - Kii).scale(1 / (pp - 1 / pp))).is_zero():
            ok = False
        for j in (0, 1):
            Ej, Fj, Kj, Kji = G[j]
            aij = 2 if i == j else -1
            if not (Ki @ Ej @ Kii - Ej.scale(pp**aij)).is_zero():
                ok = False
            if i != j and not comm(Ei, Fj).is_zero():
                ok = False
    # Serre: E1^2 E2 - [2] E1 E2 E1 + E2 E1^2 = 0
    for (i, j) in ((0, 1), (1, 0)):
        Ei, Ej = G[i][0], G[j][0]
        S = Ei @ Ei @ Ej - (Ei @ Ej @ Ei).scale(pp + 1 / pp) + Ej @ Ei @ Ei
        if not S.is_zero():
            ok = False
    nonzero = all(not G[i][0].is_zero() for i in (0, 1))
    return ok and nonzero


def commutes_all(ops, s1, s2):
    return all(comm(o, s).is_zero() for o in ops for s in (s1, s2))


def singlet_vector_classical():
    w = {}
    for perm in itertools.permutations(range(3)):
        sgn = sp.combinatorics.Permutation(list(perm)).signature()
        w[perm] = sp.Integer(sgn)
    return w


def colour_invariant_dim(gens_ops_colour_only):
    """Dimension of the common kernel of the given operators on (C^3)^{(x)3} (colour only)."""
    keys = Op.basis(3, 3)
    rows = []
    for o in gens_ops_colour_only:
        for u in keys:
            rows.append([o.cols[t].get(u, 0) for t in keys])
    M = sp.Matrix(rows)
    ns = M.nullspace()
    return len(ns), ns


def singlet_test(s_list, omega, df=2):
    """(d): for each flavour basis tuple g, sigma_i (omega (x) e_g) == omega (x) (R_f,i e_g)?
    W strand index = c*df + f. omega: dict colour-tuple -> coef."""
    n = 3
    sf1 = Op.local(df, n, RF, (0, 1))
    sf2 = Op.local(df, n, RF, (1, 2))
    ok = True
    for s, sf in zip(s_list, (sf1, sf2)):
        for g in Op.basis(df, n):
            vec = {tuple(c * df + f for c, f in zip(ct, g)): v for ct, v in omega.items()}
            got = s.apply_vec(vec)
            want = {}
            for g2, cf in sf.cols[g].items():
                for ct, v in omega.items():
                    k = tuple(c * df + f for c, f in zip(ct, g2))
                    want[k] = want.get(k, 0) + v * cf
            keys = set(got) | set(want)
            if any(sp.cancel(got.get(k, 0) - want.get(k, 0)) != 0 for k in keys):
                return False
    return ok


def limit_is_pm_perm(R2, d, subs):
    Pd = sp.zeros(d * d, d * d)
    for a, b in itertools.product(range(d), range(d)):
        Pd[b * d + a, a * d + b] = 1
    L = R2.subs(subs).applyfunc(sp.cancel)
    if L == Pd:
        return "+P"
    if L == -Pd:
        return "-P"
    return "neither"


def record(key, **kw):
    OUT["constructions"][key] = {k: (str(v) if not isinstance(v, (bool, int, list, dict)) else v)
                                 for k, v in kw.items()}


# ================================================================== K0
print("== K0 colour spectator at fixed position: R = 1_c (x) R_f, W = C^3 (x) C^2")
R0 = swap_factors_2site(I9, RF, 3, 2)
s1, s2, hk, br, wit = hecke_braid(R0, 6)
gens = colour_gens_classical(3, 2, 3, None)
br_ok, rank = su3_injective_and_brackets(gens)
comm_ok = commutes_all(list(gens.values()), s1, s2)
omega = singlet_vector_classical()
d_ok = singlet_test((s1, s2), omega)
scal, zK0 = markov_z(RF, [q, 1 / q], 2)
# (e) colour invariant dimension in (C^3)^{(x)3}
gc = colour_gens_classical(3, 1, 3, None)
inv_ops = [gc[(a, b)] for a in range(3) for b in range(3) if a != b] + \
    [gc[(0, 0)] - gc[(1, 1)], gc[(1, 1)] - gc[(2, 2)]]
edim, _ = colour_invariant_dim(inv_ops)
lim = limit_is_pm_perm(R0, 6, {q: 1})
check("K0 (a) su3 brackets hold and 8 operators independent", br_ok and rank == 8, f"rank={rank}")
check("K0 (b) colour commutes with sigma1, sigma2", comm_ok)
check("K0 (c) Hecke and braid", hk and br, wit)
check("K0 (d) singlet sector = flavour model; z = z_D", d_ok and scal and sp.cancel(zK0 - ZD) == 0, zK0)
check("K0 (e) colour invariants of (C^3)^3 one-dimensional", edim == 1, edim)
check("K0 (f) transport: q->1 limit is +-P on C^6(x)C^6 (predicted FAIL)", lim != "neither", lim)
record("K0", a=br_ok and rank == 8, b=comm_ok, c=hk and br, d=d_ok, e=edim == 1, f=lim,
       eigenvalues=[str(x) for x in eigen_classes(R0)])

# ================================================================== K1
print("\n== K1 colour strands only: Jimbo gl3 on C^3")
RC = jimbo(3, q)
s1, s2, hk, br, wit = hecke_braid(RC, 3)
coprod_used = None
for cp_kind in ("A", "B"):
    G = uq_gens(q, 1, 2, cp_kind)
    if all(comm(G[i][0], Op.local(3, 2, RC, (0, 1))).is_zero() and
           comm(G[i][1], Op.local(3, 2, RC, (0, 1))).is_zero() for i in (0, 1)):
        coprod_used = cp_kind
        break
check("K1 convention: a U_q(gl3) coproduct commuting with the Jimbo R exists", coprod_used is not None,
      f"coproduct {coprod_used}")
G = uq_gens(q, 1, 3, coprod_used)
a_ok = uq_relations(G, q)
b_ok = commutes_all([G[i][k] for i in (0, 1) for k in range(4)], s1, s2)
scal1, z3 = markov_z(RC, [q**2, 1, q**-2], 3)
ops_e = [G[i][0] for i in (0, 1)] + [G[i][1] for i in (0, 1)] + \
    [G[i][2] - Op.identity(3, 3) for i in (0, 1)]
edim1, ns1 = colour_invariant_dim(ops_e)
check("K1 (a) U_q(sl3) Chevalley-Serre relations on (C^3)^3, generators nonzero", a_ok)
check("K1 (b) commutes with sigma1, sigma2", b_ok)
check("K1 (c) Hecke and braid", hk and br, wit)
check("K1 (d) z equals z_D (predicted FAIL; no flavour in K1)",
      scal1 and sp.cancel(z3 - ZD) == 0, f"Markov scalar={scal1}, z3={z3}")
check("K1 z3 = q^3/[3]_q", sp.cancel(z3 - q**3 / (q**2 + 1 + q**-2)) == 0, z3)
check("K1 (e) U_q(sl3) invariants of (C^3)^3 one-dimensional", edim1 == 1, edim1)
record("K1", a=a_ok, b=b_ok, c=hk and br, d=False, e=edim1 == 1, f=limit_is_pm_perm(RC, 3, {q: 1}),
       z3=z3, coproduct=coprod_used)

# ================================================================== K2
print("\n== K2 flavour (x) colour = C^6, Jimbo gl6 (both lexicographic orders)")
for order_name in ("isospin-major", "colour-major"):
    # strand index s = c*2 + f (colour-major index); isospin-major rank = 3f + c
    if order_name == "isospin-major":
        rk = (lambda s: 3 * (s % 2) + s // 2)
    else:
        rk = (lambda s: s)
    R6 = jimbo(6, q, rk)
    s1, s2, hk, br, wit = hecke_braid(R6, 6)
    gens6 = colour_gens_classical(3, 2, 3, None)
    b_i = commutes_all(list(gens6.values()), s1, s2)
    # 2-site witness of non-commutation
    g2 = colour_gens_classical(3, 2, 2, None)
    r2 = Op.local(6, 2, R6, (0, 1))
    wit_b = next(((k, comm(g2[k], r2).first_nonzero()) for k in g2 if not comm(g2[k], r2).is_zero()), None)
    # (ii) q-coproduct of e_c = sum_f E_(f,c),(f,c+1) through U_q(gl6) Chevalley generators
    # Build on 2 sites: e = D(E_x) + D(E_y) where E_x, E_y are gl6 simple root vectors (if simple).
    # Test the U_q(sl3) relation [e,f] = (k - k^-1)/(q - q^-1) with k = product of the K's.
    viable = True
    reason = ""
    # gl6 simple root positions in the chosen order
    inv = {rk(s): s for s in range(6)}
    pairs = []
    for c in (0, 1):
        pr = []
        for f in (0, 1):
            a, b = c * 2 + f, (c + 1) * 2 + f
            if rk(b) - rk(a) != 1:
                viable = False
                reason = f"(f={f},c={c})->(c+1) is not a simple root in {order_name}"
            pr.append((a, b))
        pairs.append(pr)
    rel_ok = None
    if viable:
        def cop2(X, Kx, kind):
            o1 = Op.local(6, 2, X, (0,))
            if kind == "XK":
                return o1 @ Op.local(6, 2, Kx, (1,)) + Op.local(6, 2, X, (1,))
            return o1 + Op.local(6, 2, Kx, (0,)) @ Op.local(6, 2, X, (1,))
        rel_ok = True
        for pr in pairs:
            e = f = None
            kk = Op.identity(6, 2)
            for (a, b) in pr:
                Kd = [1] * 6
                Kd[a], Kd[b] = q, 1 / q
                K = sp.diag(*Kd)
                Ea, Fa = E(6, a, b), E(6, b, a)
                ee, ff = cop2(Ea, K, "XK"), cop2(Fa, K.inv(), "KX")
                e = ee if e is None else e + ee
                f = ff if f is None else f + ff
                kk = kk @ (Op.local(6, 2, K, (0,)) @ Op.local(6, 2, K, (1,)))
            kinv = Op(6, 2, {t: {u: 1 / v for u, v in c.items()} for t, c in kk.cols.items()})
            if not (comm(e, f) - (kk - kinv).scale(1 / (q - 1 / q))).is_zero():
                rel_ok = False
    check(f"K2[{order_name}] (c) Hecke and braid", hk and br, wit)
    check(f"K2[{order_name}] (i) classical colour commutes with sigma (predicted FAIL)", b_i,
          f"2-site witness {wit_b}")
    check(f"K2[{order_name}] (ii) summed q-Chevalley colour satisfies [e,f]=[k] (predicted FAIL)",
          bool(rel_ok), reason or f"relation holds={rel_ok}")
    scal6, z6 = markov_z(R6, [q**(5 - 2 * rk(s)) for s in range(6)], 6)
    check(f"K2[{order_name}] Markov z6 = q^6/[6]_q (reported)",
          scal6 and sp.cancel(z6 - q**6 / sum(q**(5 - 2 * k) for k in range(6))) == 0, z6)
    record(f"K2[{order_name}]", c=hk and br, b_classical=b_i, a_qsum=rel_ok, viable_qsum=viable,
           reason=reason, z6=z6)

# ================================================================== K3
print("\n== K3 R = R_f (x) P_c ; K3' R = R_f (x) R_c(gl3)")
R3 = swap_factors_2site(P3, RF, 3, 2)
R3p = swap_factors_2site(RC, RF, 3, 2)
for key, R in (("K3", R3), ("K3'", R3p)):
    ev = eigen_classes(R)
    _, _, hk, br, wit = hecke_braid(R, 6)
    check(f"{key} (c) Hecke relation (predicted FAIL)", hk, f"distinct eigenvalues {ev}; braid={br}")
    record(key, c=hk, braid=br, eigenvalues=[str(x) for x in ev])

# ================================================================== K4
print("\n== K4 colour-invariant class R = s_c (x) X + a_c (x) Y")
FL = {"q": q * I4, "-1/q": -I4 / q, "Rf": RF, "-Rf^-1": -RFinv}


def colour_projectors(pp):
    if pp == 1:
        return (sp.eye(9) + P3) / 2, (sp.eye(9) - P3) / 2
    Rc = jimbo(3, pp)
    s = ((Rc + sp.eye(9) / pp) / (pp + 1 / pp)).applyfunc(sp.cancel)
    a = ((pp * sp.eye(9) - Rc) / (pp + 1 / pp)).applyfunc(sp.cancel)
    return s, a


k4 = {}
for pname, pp in (("p=1", 1), ("p=q", q)):
    sC, aC = colour_projectors(pp)
    if pp == 1:
        cg = colour_gens_classical(3, 2, 3, None)
        col_ops = list(cg.values())
        omega_c = omega
    else:
        Gq = uq_gens(q, 2, 3, coprod_used)
        col_ops = [Gq[i][k] for i in (0, 1) for k in range(4)]
        Gc = uq_gens(q, 1, 3, coprod_used)
        _, nsq = colour_invariant_dim([Gc[i][0] for i in (0, 1)] + [Gc[i][1] for i in (0, 1)] +
                                      [Gc[i][2] - Op.identity(3, 3) for i in (0, 1)])
        vq = nsq[0]
        omega_c = {t: sp.cancel(vq[k]) for k, t in enumerate(Op.basis(3, 3)) if vq[k] != 0}
    for xn, yn in itertools.product(FL, FL):
        R = (swap_factors_2site(sC, FL[xn], 3, 2) + swap_factors_2site(aC, FL[yn], 3, 2)).applyfunc(sp.cancel)
        s1, s2, hk, br, wit = hecke_braid(R, 6)
        b_ok = commutes_all(col_ops, s1, s2) if (hk and br) else None
        d_ok = singlet_test((s1, s2), omega_c) if (hk and br) else None
        lim = limit_is_pm_perm(R, 6, {q: 1})
        key = f"K4[{pname}; X={xn}, Y={yn}]"
        k4[key] = dict(c_hecke=hk, c_braid=br, b=b_ok, d=d_ok, f=lim,
                       braid_witness=None if br else str(wit))
        print(f"  {key}: Hecke={hk} braid={br} b={b_ok} d={d_ok} f={lim}"
              + ("" if br else f"  witness {wit}"))
OUT["K4"] = {k: {kk: (vv if isinstance(vv, (bool, type(None))) else str(vv)) for kk, vv in v.items()}
             for k, v in k4.items()}

passing = [k for k, v in k4.items() if v["c_hecke"] and v["c_braid"]]
transported = [k for k, v in k4.items() if v["f"] != "neither"]
check("K4 transported members (q->1 limit +-P) are exactly X=Rf,Y=-Rf^-1 and X=-Rf^-1,Y=Rf",
      sorted(transported) == sorted([f"K4[{pn}; X=Rf, Y=-Rf^-1]" for pn in ("p=1", "p=q")] +
                                    [f"K4[{pn}; X=-Rf^-1, Y=Rf]" for pn in ("p=1", "p=q")]),
      transported)
check("K4 every transported member fails the braid relation at q != 1 (predicted)",
      all(not k4[k]["c_braid"] for k in transported), [(k, k4[k]["c_braid"]) for k in transported])
check("K4 members satisfying Hecke+braid (reported)", True, passing)

# symbolic p for the two transported members: residual of the braid relation as a function of p, q
print("\n== K4 transported members with symbolic colour parameter p")
sym = {}
for xn, yn in (("Rf", "-Rf^-1"), ("-Rf^-1", "Rf")):
    sC, aC = colour_projectors(p)
    R = (swap_factors_2site(sC, FL[xn], 3, 2) + swap_factors_2site(aC, FL[yn], 3, 2)).applyfunc(sp.cancel)
    s1 = Op.local(6, 3, R, (0, 1))
    s2 = Op.local(6, 3, R, (1, 2))
    D = s1 @ s2 @ s1 - s2 @ s1 @ s2
    nums = set()
    for c in D.cols.values():
        for v in c.values():
            nn = sp.factor(sp.numer(sp.together(sp.cancel(v))))
            if nn != 0:
                nums.add(nn)
    # common zero set of all residual numerators: lex Groebner basis in (p, q)
    G = sp.groebner([sp.expand(nn) for nn in nums], p, q, order="lex")
    gb = [sp.factor(x) for x in G.exprs]
    expected = [sp.factor((p**2 - 1)**2), sp.factor((q**2 - 1)**2)]
    sym[f"X={xn},Y={yn}"] = {"groebner_basis": [str(x) for x in gb], "n_distinct": len(nums)}
    check(f"K4 symbolic p, X={xn}, Y={yn}: braid holds iff p^2 = 1 and q^2 = 1 (Groebner basis)",
          [sp.expand(x) for x in gb] == [sp.expand(x) for x in expected], f"basis = {gb}")
OUT["K4_symbolic_p"] = sym

(HERE / "qcd_colour_action_probe.out.json").write_text(json.dumps(OUT, indent=1))
print(f"\n{sum(c['pass'] for c in OUT['checks'])}/{len(OUT['checks'])} checks PASS")
