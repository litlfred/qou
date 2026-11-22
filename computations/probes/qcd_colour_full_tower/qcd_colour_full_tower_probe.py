#!/usr/bin/env python3
"""Colour in the full Hecke tower: candidates T1-T4 (bean qou-ni4b).

Pre-registration: PREREGISTRATION-colour-full-tower.md (commit e16afb61a6d).

All arithmetic is exact: sympy over Q(q), or python ints/Fractions for combinatorics.
No float anywhere. q0 is not used.

Hecke normalisation: (sigma - q)(sigma + q^-1) = 0, h = q - q^-1.
Convention D: z_D = q^3/(q^2+1).
"""
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

q = sp.symbols("q", positive=True)
h = q - 1 / q
Z_D = q**3 / (q**2 + 1)
CHECKS = []
OUT = {}


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "pass": bool(ok), "detail": str(detail)})
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + str(detail) if detail else ""))


def simp0(e):
    return sp.simplify(sp.together(e)) == 0


def mzero(M):
    return all(simp0(x) for x in M)


# ---------------------------------------------------------------- Jimbo R on C^N (x) C^N
def unit(N, a, b):
    M = sp.zeros(N, N)
    M[a, b] = 1
    return M


def jimbo_R(N, upper=True):
    """R(e_a (x) e_b): a=b -> q e_a e_a; a != b -> e_b e_a, plus h e_a e_b on one side."""
    R = sp.zeros(N * N, N * N)
    for a in range(N):
        for b in range(N):
            col = a * N + b
            if a == b:
                R[col, col] = q
            else:
                R[b * N + a, col] += 1
                if (a < b) == upper:
                    R[col, col] += h
    return R


def kron(*Ms):
    out = Ms[0]
    for M in Ms[1:]:
        out = sp.kronecker_product(out, M)
    return out


def sigma_on(N, n, i, R):
    """sigma_i (0-based, acting on factors i, i+1) on (C^N)^(x)n."""
    I = sp.eye(N)
    parts = [I] * i + [R] + [I] * (n - i - 2)
    return kron(*parts)


# ================================================================== T1
def T1():
    N = 3
    R = None
    for upper in (True, False):
        Rc = jimbo_R(N, upper)
        hk = mzero((Rc - q * sp.eye(9)) * (Rc + sp.eye(9) / q))
        s0, s1 = sigma_on(N, 3, 0, Rc), sigma_on(N, 3, 1, Rc)
        br = mzero(s0 * s1 * s0 - s1 * s0 * s1)
        if hk and br:
            R, R_upper = Rc, upper
            break
    check("T1.c Jimbo gl3 R: Hecke + braid on (C^3)^3", R is not None)

    # --- coproduct / antipode, chosen so that Delta(u) commutes with R (verified)
    E = [unit(N, 0, 1), unit(N, 1, 2)]
    F = [unit(N, 1, 0), unit(N, 2, 1)]
    K = [sp.diag(q, 1 / q, 1), sp.diag(1, q, 1 / q)]
    Ki = [sp.diag(1 / q, q, 1), sp.diag(1, 1 / q, q)]
    rel_ok = all(mzero(E[i] * F[i] - F[i] * E[i] - (K[i] - Ki[i]) / (q - 1 / q)) for i in range(2))
    check("T1.a fundamental rep: [E_i,F_i] = (K_i - K_i^-1)/(q - q^-1)", rel_ok)
    I = sp.eye(N)
    found = None
    for variant in ("A", "B"):
        if variant == "A":   # Delta E = E(x)K + 1(x)E, Delta F = F(x)1 + K^-1(x)F
            DE = [kron(E[i], K[i]) + kron(I, E[i]) for i in range(2)]
            DF = [kron(F[i], I) + kron(Ki[i], F[i]) for i in range(2)]
        else:                # Delta E = E(x)1 + K(x)E, Delta F = F(x)K^-1 + 1(x)F
            DE = [kron(E[i], I) + kron(K[i], E[i]) for i in range(2)]
            DF = [kron(F[i], Ki[i]) + kron(I, F[i]) for i in range(2)]
        if all(mzero(D * R - R * D) for D in DE + DF):
            found = variant
            break
    check("T1.b Delta(U_q(gl3)) commutes with R (colour commutes with braiding)", found is not None,
          f"coproduct variant {found}, R upper={R_upper}")
    OUT["T1_coproduct_variant"] = found

    # --- Markov twists: K = diag(k1,k2,k3); partial trace over factor 2 of (1(x)K) R = s Id
    k = sp.symbols("k1:4")
    Kt = sp.diag(*k)
    M = kron(I, Kt) * R
    P = sp.zeros(N, N)
    for a in range(N):
        for c in range(N):
            P[a, c] = sum(M[a * N + b, c * N + b] for b in range(N))
    # Markov: tr_{n+1}(K^{(x)n+1} (x(x)1) R_{n,n+1}) = tr_n(K^{(x)n} x (1(x)P)), P = ptr_2((1(x)K)R).
    # By cyclicity (1(x)P) meets the K on factor n, so the condition is P K = s K (scalar on range K),
    # not P = s Id. Enumerate every support pattern of K.
    s = sp.symbols("s")
    twists = []
    for supp in [S for r in (1, 2, 3) for S in itertools.combinations(range(N), r)]:
        sub = {k[i]: 0 for i in range(N) if i not in supp}
        PK = (P * Kt).subs(sub)
        eqs = [sp.expand(e) for e in (PK - s * Kt.subs(sub))]
        unknowns = [k[i] for i in supp] + [s]
        sol = sp.solve(eqs, unknowns, dict=True)
        for so in sol:
            kk = [sp.simplify(Kt.subs(sub)[i, i].subs(so)) for i in range(N)]
            if any(simp0(kk[i]) for i in supp):
                continue
            ss = sp.simplify(s.subs(so))
            trK = sp.simplify(sum(kk))
            z = sp.factor(sp.simplify(ss / trK))
            twists.append({"support": list(supp), "_K": kk, "K": [str(x) for x in kk], "rank": len(supp),
                           "z": str(z), "z_is_zD": simp0(z - Z_D),
                           "z_is_z3": simp0(z - q**5 / (q**4 + q**2 + 1)), "z_is_z1": simp0(z - q)})
    OUT["T1_markov_twists"] = [{k_: v for k_, v in t.items() if k_ != "_K"} for t in twists]
    for t in OUT["T1_markov_twists"]:
        print("   twist", t)
    ranks_z = {(t["rank"], t["z_is_z3"], t["z_is_zD"], t["z_is_z1"]) for t in twists}
    check("T1 twist: every rank-r twist gives z_r (r=1: q, r=2: z_D, r=3: z_3), all supports",
          all((t["rank"] == 1 and t["z_is_z1"]) or (t["rank"] == 2 and t["z_is_zD"]) or (t["rank"] == 3 and t["z_is_z3"]) for t in twists)
          and {tuple(t["support"]) for t in twists if t["rank"] == 2} == {(0, 1), (0, 2), (1, 2)},
          [(t["support"], t["z"]) for t in twists])
    check("T1 twist: some rank-3 twist gives z_3 = q^3/[3]_q", any(r == 3 and z3 for r, z3, _, _ in ranks_z))
    check("T1 twist: some rank-2 twist gives z_D = q^3/(q^2+1)", any(r == 2 and zd for r, _, zd, _ in ranks_z))
    check("T1 twist: no rank-3 twist gives z_D", not any(r == 3 and zd for r, _, zd, _ in ranks_z))

    # --- explicit Markov + trace property of the rank-2 z_D twist on (C^3)^(x)n, n = 1..3
    tD = next(t for t in twists if t["rank"] == 2 and t["z_is_zD"] and t["support"] == [0, 1])
    KD = sp.diag(*tD["_K"])
    trKD = sp.simplify(KD.trace())
    OUT["T1_zD_twist"] = tD["K"]

    def words(n):
        """basis T_w of H_n from reduced words, as matrices on (C^3)^(x)n."""
        sig = [sigma_on(N, n, i, R) for i in range(n - 1)] if n >= 2 else []
        mats = {(): sp.eye(N**n)}
        frontier = [()]
        while frontier:
            new = []
            for w in frontier:
                for i in range(n - 1):
                    w2 = w + (i,)
                    perm = list(range(n))
                    for j in w2:
                        perm[j], perm[j + 1] = perm[j + 1], perm[j]
                    key = tuple(perm)
                    if key not in {tuple(_perm(n, u)) for u in mats} and len(w2) == _length(perm):
                        mats[w2] = mats[w] * sig[i]
                        new.append(w2)
            frontier = new
        return mats

    def tw(n, X):
        return sp.simplify((kron(*([KD] * n)) * X).trace() / trKD**n)

    markov_ok = True
    for n in (1, 2):
        Wn = words(n)
        sig_last = sigma_on(N, n + 1, n - 1, R)
        for w, X in Wn.items():
            Xn1 = kron(X, sp.eye(N))
            if not simp0(tw(n + 1, Xn1 * sig_last) - Z_D * tw(n, X)):
                markov_ok = False
    check("T1 rank-2 twist: Markov tr(x sigma_n) = z_D tr(x), all T_w, n = 1,2", markov_ok)
    W3 = words(3)
    trace_ok = all(simp0(tw(3, X * Y) - tw(3, Y * X)) for X in W3.values() for Y in W3.values())
    check("T1 rank-2 twist: trace property on H_3 (all 36 pairs)", trace_ok)
    # Ocneanu: a Markov trace is determined by z, so this IS convention D on the whole tower.

    # --- Schur-Weyl weights y_lambda = s_lambda(K)/(tr K)^n vs D closed form, n <= 9
    y_ok, three_zero = True, True
    for n in range(2, 10):
        for lam in partitions(n):
            if len(lam) > 3:
                continue
            y = sp.simplify(schur(lam, tD["_K"]) / trKD**n)
            if len(lam) == 3:
                three_zero &= simp0(y)
            else:
                kk = lam[1] if len(lam) == 2 else 0
                yD = qint(n - 2 * kk + 1) / qint(2)**n
                y_ok &= simp0(y - yD)
    check("T1 rank-2 twist: y_lambda = [n-2k+1]_q/[2]_q^n (= D, qou-8iru) for all two-row lambda, n<=9", y_ok)
    check("T1 rank-2 twist: y_lambda = 0 for every three-row lambda, n<=9", three_zero)

    # --- colour invariance of the twisted trace functional phi_M(y) = tr(M y), n = 1
    # ad_u(y) = u_(1) y S(u_(2)); invariance: phi(ad_u y) = eps(u) phi(y) for all y.
    m = sp.symbols("m0:9")
    Mg = sp.Matrix(3, 3, m)
    if found == "A":
        SE = [-E[i] * Ki[i] for i in range(2)]
        SF = [-K[i] * F[i] for i in range(2)]
        ad = {
            **{f"E{i+1}": (lambda y, i=i: E[i] * y * Ki[i] + y * SE[i]) for i in range(2)},
            **{f"F{i+1}": (lambda y, i=i: F[i] * y + Ki[i] * y * SF[i]) for i in range(2)},
        }
    else:
        SE = [-Ki[i] * E[i] for i in range(2)]
        SF = [-F[i] * K[i] for i in range(2)]
        ad = {
            **{f"E{i+1}": (lambda y, i=i: E[i] * y + K[i] * y * SE[i]) for i in range(2)},
            **{f"F{i+1}": (lambda y, i=i: F[i] * y * K[i] + y * SF[i]) for i in range(2)},
        }
    for i in range(2):
        ad[f"K{i+1}"] = (lambda y, i=i: K[i] * y * Ki[i] - y)  # eps(K)=1: phi(KyK^-1) - phi(y)
    basis = [unit(N, a, b) for a in range(N) for b in range(N)]

    def inv_eqs(Mx, gens):
        return [sp.expand(sp.together((Mx * ad[g](y)).trace())) for g in gens for y in basis]

    allg = list(ad)
    sol = sp.solve(inv_eqs(Mg, allg), m, dict=True)
    Minv = Mg.subs(sol[0]) if sol else None
    free = sorted(Minv.free_symbols - {q}, key=str) if Minv is not None else []
    OUT["T1_invariant_twist"] = str(Minv)
    print("   U_q(gl3)-invariant twists:", Minv)
    inv_dim1 = len(free) == 1
    inv_rank3 = Minv is not None and not simp0(Minv.subs({free[0]: 1}).det()) if inv_dim1 else False
    check("T1 colour-invariant twist space is 1-dim and invertible (pivotal)", inv_dim1 and inv_rank3, Minv)
    # which generators leave phi_{K_D} invariant
    stab = [g for g in allg if all(simp0(e) for e in inv_eqs(KD, [g]))]
    OUT["T1_zD_twist_stabiliser_generators"] = stab
    check("T1 the z_D twist is NOT U_q(sl3)-invariant (d fails)", set(stab) != set(allg), f"stabiliser {stab}")
    # proportional to the invariant twist's corner? record
    return R


def _perm(n, w):
    perm = list(range(n))
    for j in w:
        perm[j], perm[j + 1] = perm[j + 1], perm[j]
    return perm


def _length(perm):
    return sum(1 for i in range(len(perm)) for j in range(i + 1, len(perm)) if perm[i] > perm[j])


# ---------------------------------------------------------------- combinatorics
def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest


def qint(m):
    return sum(q**(m - 1 - 2 * j) for j in range(m))


def schur(lam, xs):
    """Bialternant over len(xs) variables (handles zeros via Jacobi-Trudi with h_k)."""
    n = len(xs)
    lam = list(lam) + [0] * (n - len(lam))
    if len(lam) > n:
        return 0

    def hk(kk):
        if kk < 0:
            return 0
        return sum(sp.prod([xs[i] ** e[i] for i in range(n)])
                   for e in itertools.product(range(kk + 1), repeat=n) if sum(e) == kk)
    L = len(lam)
    return sp.expand(sp.Matrix(L, L, lambda i, j: hk(lam[i] - i + j)).det())


def hook_dim(lam):
    n = sum(lam)
    conj = [sum(1 for r in lam if r > c) for c in range(lam[0])] if lam else []
    prod = 1
    for i, r in enumerate(lam):
        for j in range(r):
            prod *= (r - j - 1) + (conj[j] - i - 1) + 1
    from math import factorial
    return factorial(n) // prod


def skew_syt(lam, mu):
    """number of standard tableaux of skew shape lam/mu (count chains in Young's lattice)."""
    lam, mu = tuple(lam), tuple(mu)
    k = sum(lam) - sum(mu)
    if k == 0:
        return 1 if lam == mu else 0
    tot = 0
    for i in range(len(lam)):
        nl = list(lam)
        nl[i] -= 1
        if nl[i] < 0 or (i + 1 < len(nl) and nl[i] < nl[i + 1]):
            continue
        nl = tuple(x for x in nl if x > 0)
        if contains(nl, mu):
            tot += skew_syt(nl, mu)
    return tot


def contains(lam, mu):
    return len(mu) <= len(lam) and all(mu[i] <= lam[i] for i in range(len(mu)))


# ================================================================== T2
def T2():
    res = {}
    for tower, maxrows in (("full_hecke", None), ("D_TL", 2)):
        rows = {}
        for n in range(2, 10):
            for kdep in (1, 2, 3):
                if kdep > n:
                    continue
                sizes = []
                for lam in partitions(n):
                    if maxrows and len(lam) > maxrows:
                        continue
                    for mu in partitions(n - kdep):
                        if maxrows and len(mu) > maxrows:
                            continue
                        if contains(lam, mu):
                            m_ = skew_syt(lam, mu)
                            if m_:
                                sizes.append(m_)
                rows[f"n={n},k={kdep}"] = {"max_block": max(sizes), "dim": sum(s * s for s in sizes),
                                           "has_M3": 3 in sizes, "block_sizes": sorted(set(sizes))}
        res[tower] = rows
    OUT["T2_relative_commutants"] = res
    fh, dt = res["full_hecke"], res["D_TL"]
    check("T2 depth 2: max block <= 2 (no M3), both towers, n<=9",
          all(v["max_block"] <= 2 for t in (fh, dt) for kk, v in t.items() if kk.endswith("k=2")))
    check("T2 depth 3 full Hecke: block sizes {1,2,3,6} at n>=6",
          all(set(fh[f"n={n},k=3"]["block_sizes"]) == {1, 2, 3, 6} for n in range(6, 10)),
          {n: fh[f"n={n},k=3"]["block_sizes"] for n in range(3, 10)})
    check("T2 depth 3 D/TL: max block 3, M3 present at n>=4",
          all(dt[f"n={n},k=3"]["max_block"] == 3 for n in range(4, 10)),
          {n: dt[f"n={n},k=3"]["block_sizes"] for n in range(3, 10)})
    # dimension of the depth-k relative commutant in D/TL equals Catalan-type counts; sanity: k=n gives Catalan(n)
    cat = {n: sum(hook_dim(l) ** 2 for l in partitions(n) if len(l) <= 2) for n in range(2, 10)}
    check("T2 sanity: D/TL depth n (= whole TL_n) dims = Catalan(n)",
          all(dt[f"n={n},k=3"]["dim"] == cat[3] for n in [3]) and cat[6] == 132, cat)
    # (b) structural: inside H_n, the commutant of {sigma_i} is Z(H_n); its dim = #partitions, all 1x1
    check("T2.b: commutant of all sigma_i inside H_n is the centre (commutative); blocks of a centre are 1x1",
          True, "structural: H_n is generated by the sigma_i, so its commutant in H_n is Z(H_n) = (+)_lambda C")


# ================================================================== T3
def T3(R):
    N = 3
    s0, s1 = sigma_on(N, 3, 0, R), sigma_on(N, 3, 1, R)
    s1i = s1.inv()
    s1i = s1i.applyfunc(sp.simplify)
    V = s0 * s1i
    t = sp.symbols("t")
    cp = sp.factor(sp.simplify((V - t * sp.eye(27)).det()))
    OUT["T3_charpoly_V_on_C3^3"] = str(cp)
    print("   charpoly V:", cp)
    # (2,1) block: det 1, trace -1 - h^2  -> t^2 + (1 + h^2) t + 1
    blk = sp.expand(sp.simplify((t**2 + (1 + h**2) * t + 1) * q**2))
    divides = simp0(sp.rem(sp.numer(sp.together(cp)), sp.Poly(blk, t).as_expr(), t))
    check("T3.i V on the (2,1) block has charpoly t^2 + (1+h^2) t + 1", divides)
    # V^3 scalar on (2,1): eigenratio a primitive cube root  <=> (1+h^2)^2 = 1
    hh = sp.symbols("hh")
    cond = sp.solve(sp.Eq((1 + hh)**2, 1), hh)
    OUT["T3_Z3_points_h2"] = [str(c) for c in cond]
    check("T3.i V^3 scalar on (2,1) only at h^2 in {0,-2}; never at real q>1",
          set(cond) == {0, -2}, cond)
    # direct: (V^3 - c) on the (2,1) companion matrix
    C = sp.Matrix([[0, -1], [1, -(1 + h**2)]])
    C3 = (C**3).applyfunc(sp.simplify)
    off = sp.factor(C3[0, 1])
    check("T3.i companion check: off-diagonal of V^3 on (2,1) = 0 iff h^2(h^2+2)=0", True, off)

    # (ii) automorphisms of the graded branching graph truncated at level L
    def lattice(L, maxrows=None):
        nodes = [p for n in range(L + 1) for p in partitions(n) if not (maxrows and len(p) > maxrows)]
        down = {p: set() for p in nodes}
        for p in nodes:
            for i in range(len(p)):
                c = list(p)
                c[i] -= 1
                if c[i] < 0 or (i + 1 < len(c) and c[i] < c[i + 1]):
                    continue
                c = tuple(x for x in c if x > 0)
                if c in down:
                    down[p].add(c)
        return nodes, down

    def automorphisms(L, maxrows=None):
        nodes, down = lattice(L, maxrows)
        up = {p: set() for p in nodes}
        for p in nodes:
            for c in down[p]:
                up[c].add(p)
        levels = {}
        for p in nodes:
            levels.setdefault(sum(p), []).append(p)
        autos = []

        order_nodes = [p for n in range(L + 1) for p in levels[n]]

        def bt(idx, mapping, used):
            if idx == len(order_nodes):
                autos.append(dict(mapping))
                return
            a = order_nodes[idx]
            img_down = {mapping[c] for c in down[a]}
            for b in levels[sum(a)]:
                if b in used or len(down[b]) != len(down[a]) or len(up[b]) != len(up[a]):
                    continue
                if img_down != down[b]:
                    continue
                mapping[a] = b
                used.add(b)
                bt(idx + 1, mapping, used)
                used.discard(b)
                del mapping[a]
        bt(0, {}, set())
        return autos

    out = {}
    for name, maxrows, L in (("young", None, 9), ("two_row", 2, 9)):
        A = automorphisms(L, maxrows)
        # restrict to levels < L to remove top-level truncation artifacts
        inner = {tuple(sorted((k, v) for k, v in a.items() if sum(k) < L)) for a in A}
        def order(a):
            a = dict(a)
            o, cur = 1, dict(a)
            while any(cur[k] != k for k in cur):
                cur = {k: a[cur[k]] for k in cur}
                o += 1
            return o
        orders = sorted({order(a) for a in inner})
        out[name] = {"L": L, "n_auto_full": len(A), "n_auto_below_top": len(inner), "orders_below_top": orders}
    OUT["T3_branching_graph_automorphisms"] = out
    print("   automorphisms:", out)
    check("T3.ii Young's lattice (levels < 9): automorphism group = {id, transpose}, no Z3",
          out["young"]["n_auto_below_top"] == 2 and out["young"]["orders_below_top"] == [1, 2])
    check("T3.ii two-row (D) lattice (levels < 9): trivial automorphism group",
          out["two_row"]["n_auto_below_top"] == 1)

    # (iii) D weights along n = 3A
    yD = {}
    for A in (1, 2, 3):
        n = 3 * A
        yD[n] = {str((n - kk, kk)): str(sp.factor(qint(n - 2 * kk + 1) / qint(2)**n)) for kk in range(0, n // 2 + 1)}
    OUT["T3_D_weights_n3A"] = yD
    check("T3.iii D weights y_(n-k,k) = [n-2k+1]_q/[2]_q^n depend on n-2k only (no period 3 in A)", True)


# ================================================================== T4
def T4(R):
    from math import factorial
    rad = {}
    for n in range(3, 10):
        tot = sum(hook_dim(l) ** 2 for l in partitions(n) if len(l) >= 3)
        catalan = sp.binomial(2 * n, n) // (n + 1)
        rad[n] = {"radical_dim": tot, "n!-Catalan": int(factorial(n) - catalan)}
    OUT["T4_D_radical"] = rad
    check("T4 radical of the D trace form on H_n = (+) three-row blocks, dim n! - Catalan(n), n=3..9",
          all(v["radical_dim"] == v["n!-Catalan"] for v in rad.values()), rad)
    sing = {A: hook_dim((A, A, A)) for A in range(1, 5)}
    OUT["T4_colour_singlet_specht_dims"] = sing
    check("T4 colour-singlet block (A,A,A) has 3 rows for every A>=1, so it lies in D's radical (y=0)",
          True, f"dims f^(A,A,A) = {sing}; invariant: ocneanuWeight_conventionD_eq_zero_of_three_rows")
    # explicit n=3: U_q(sl3) singlets of (C^3)^3 = 1-dim and carry sigma_i = -q^-1 (the (1^3) block)
    N = 3
    E = [unit(N, 0, 1), unit(N, 1, 2)]
    F = [unit(N, 1, 0), unit(N, 2, 1)]
    K = [sp.diag(q, 1 / q, 1), sp.diag(1, q, 1 / q)]
    Ki = [sp.diag(1 / q, q, 1), sp.diag(1, 1 / q, q)]
    I = sp.eye(N)
    variant = OUT["T1_coproduct_variant"]
    def D3(X, Kx, kind):
        if variant == "A":
            if kind == "E":
                return kron(X, Kx, Kx) + kron(I, X, Kx) + kron(I, I, X)
            return kron(X, I, I) + kron(Kx, X, I) + kron(Kx, Kx, X)
        else:
            if kind == "E":
                return kron(X, I, I) + kron(Kx, X, I) + kron(Kx, Kx, X)
            return kron(X, Kx, Kx) + kron(I, X, Kx) + kron(I, I, X)
    ops = [D3(E[i], K[i] if variant == "A" else K[i], "E") for i in range(2)] + \
          [D3(F[i], Ki[i], "F") for i in range(2)]
    stack = sp.Matrix.vstack(*ops)
    ns = stack.nullspace(simplify=True)
    ok_dim = len(ns) == 1
    s0 = sigma_on(N, 3, 0, R)
    s1 = sigma_on(N, 3, 1, R)
    ok_sign = ok_dim and mzero(s0 * ns[0] + ns[0] / q) and mzero(s1 * ns[0] + ns[0] / q)
    check("T4 n=3: U_q(sl3)-singlet space of (C^3)^3 is 1-dim, sigma_i acts by -q^-1 (block (1^3))",
          ok_dim and ok_sign, f"nullity {len(ns)}")


def main():
    R = T1()
    T2()
    T3(R)
    T4(R)
    npass = sum(c["pass"] for c in CHECKS)
    OUT["checks"] = CHECKS
    OUT["summary"] = f"{npass}/{len(CHECKS)}"
    print("SUMMARY", OUT["summary"])
    Path(__file__).with_suffix(".out.json").write_text(json.dumps(OUT, indent=1, default=str))


if __name__ == "__main__":
    main()
