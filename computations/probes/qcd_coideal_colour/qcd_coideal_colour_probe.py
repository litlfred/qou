#!/usr/bin/env python3
"""Coideal (quantum-symmetric-pair) colour on (C^3)^(x)n: tests Q1-Q4 (bean qou-ni4b).

Pre-registration: PREREGISTRATION-coideal-colour.md (commit 096d888f561, pushed before this file).

Setting identical to ../qcd_colour_full_tower and ../qcd_d_residual_symmetry:
  Jimbo U_q(gl3) on C^3, coproduct variant B (Kolb's convention)
      Delta E = E(x)1 + K(x)E,  Delta F = F(x)K^-1 + 1(x)F,  S(E) = -K^-1 E,  S(F) = -F K,
  R = jimbo_R(3, upper=True) (copied verbatim below).
Coideals (X = empty, s_i = 0), parameters c_i FREE symbols (never chosen against a target):
  AI   (gl3, so3):        B_i = F_i - c_i E_i K_i^-1,                 i = 1,2
  AIII (gl3, gl2+gl1):    B_1 = F_1 - c_1 E_2 K_1^-1,  B_2 = F_2 - c_2 E_1 K_2^-1,  H = K_1 K_2^-1
Exact sympy over Q(q, c1, c2) (DomainMatrix over the fraction field for the big linear systems).
No float. q0 not used.

Dual adjoint action on a twist C (functional phi_C(Y) = tr(C Y)):
  ad*_E(C) = C E - K^-1 E C K,  ad*_F(C) = K C F - F K C,  ad*_K(C) = K^-1 C K,  ad*_{K^-1}(C) = K C K^-1,
  ad*_{gh} = ad*_h o ad*_g.  phi_C is B-invariant iff ad*_b(C) = eps(b) C for the generators b.
"""
import json
import sys
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

q = sp.symbols("q", positive=True)
c1, c2 = sp.symbols("c1 c2")
al, be = sp.symbols("alpha beta")
h = q - 1 / q
Z_D = q**3 / (q**2 + 1)
Z_3 = q**5 / (q**4 + q**2 + 1)
Z_1 = q
CHECKS, OUT, ACCEPT = [], {}, {}
HERE = Path(__file__).resolve().parent


def check(name, ok, detail="", kind="prereg"):
    CHECKS.append({"name": name, "pass": bool(ok), "detail": str(detail), "kind": kind})
    print(("PASS " if ok else "FAIL ") + ("[posthoc] " if kind == "posthoc" else "") + name
          + ("  -- " + str(detail) if detail else ""), flush=True)


def z0(e):
    return sp.cancel(sp.together(e)) == 0


def mz(M):
    return all(z0(x) for x in M)


def unit(N, a, b):
    M = sp.zeros(N, N)
    M[a, b] = 1
    return M


def jimbo_R(N, upper=True):
    """Copied from qcd_colour_full_tower_probe.jimbo_R."""
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


N = 3
I3 = sp.eye(N)
R = jimbo_R(N, True)
E = [unit(N, 0, 1), unit(N, 1, 2)]
F = [unit(N, 1, 0), unit(N, 2, 1)]
Kc = [sp.diag(q, 1 / q, 1), sp.diag(1, q, 1 / q)]
Kci = [sp.diag(1 / q, q, 1), sp.diag(1, 1 / q, q)]
PIV = sp.diag(q**-4, q**-2, 1)


def sigma(n, i):
    return kron(*([I3] * i + [R] + [I3] * (n - i - 2)))


def Delta(n, kind, i):
    if kind == "K":
        return kron(*([Kc[i]] * n))
    if kind == "Ki":
        return kron(*([Kci[i]] * n))
    out = sp.zeros(N**n, N**n)
    for p in range(n):
        if kind == "E":
            fac = [Kc[i]] * p + [E[i]] + [I3] * (n - p - 1)
        else:
            fac = [I3] * p + [F[i]] + [Kci[i]] * (n - p - 1)
        out += kron(*fac)
    return out


# ---------------------------------------------------------------- coideal data
# a coideal generator is a list of (coef, word) with word a tuple of letters (kind, i)
TYPES = {
    "AI": {"tau": [0, 1], "gens": {"B1": [(1, (("F", 0),)), (-c1, (("E", 0), ("Ki", 0)))],
                                   "B2": [(1, (("F", 1),)), (-c2, (("E", 1), ("Ki", 1)))]},
           "eps": {"B1": 0, "B2": 0}},
    "AIII": {"tau": [1, 0], "gens": {"B1": [(1, (("F", 0),)), (-c1, (("E", 1), ("Ki", 0)))],
                                     "B2": [(1, (("F", 1),)), (-c2, (("E", 0), ("Ki", 1)))],
                                     "H": [(1, (("K", 0), ("Ki", 1)))]},
             "eps": {"B1": 0, "B2": 0, "H": 1}},
}


def gen_mat(n, gen):
    out = sp.zeros(N**n, N**n)
    for coef, word in gen:
        M = sp.eye(N**n)
        for kind, i in word:
            M = M * Delta(n, kind, i)
        out += coef * M
    return out


def ad_letter(n, kind, i):
    Kd, Kdi = Delta(n, "K", i), Delta(n, "Ki", i)
    if kind == "E":
        X = Delta(n, "E", i)
        return lambda C: C * X - Kdi * X * C * Kd
    if kind == "F":
        X = Delta(n, "F", i)
        return lambda C: Kd * C * X - X * Kd * C
    if kind == "K":
        return lambda C: Kdi * C * Kd
    return lambda C: Kd * C * Kdi            # K^-1


def ad_gen(n, gen):
    terms = [(coef, [ad_letter(n, k, i) for k, i in word]) for coef, word in gen]

    def f(C):
        out = sp.zeros(*C.shape)
        for coef, maps in terms:
            D = C
            for m in maps:      # word g1 g2 ... : apply ad*_{g1} first
                D = m(D)
            out += coef * D
        return out
    return f


DOM = sp.QQ.frac_field(q, c1, c2)


def nullspace_exact(rows, nvars):
    """Exact nullspace over Q(q,c1,c2) of the linear system given as a list of sympy row-lists."""
    if not rows:
        return [sp.Matrix([1 if j == k else 0 for j in range(nvars)]) for k in range(nvars)]
    M = DomainMatrix([[DOM.from_sympy(sp.together(x)) for x in r] for r in rows], (len(rows), nvars), DOM)
    ns = M.nullspace()
    return [sp.Matrix([DOM.to_sympy(x) for x in row]) for row in ns.to_Matrix().tolist()] if ns.shape[0] else []


def linear_rows(exprs, syms):
    rows = []
    for e in exprs:
        e = sp.together(e)
        num = sp.numer(e)
        num = sp.expand(num)
        if num == 0:
            continue
        rows.append([sp.diff(num, s) for s in syms])
    return rows


def commutant(mats, dim):
    xs = sp.symbols(f"x0:{dim * dim}")
    X = sp.Matrix(dim, dim, xs)
    eqs = []
    for M in mats:
        eqs += list(X * M - M * X)
    rows = linear_rows(eqs, xs)
    ns = nullspace_exact(rows, dim * dim)
    return [sp.Matrix(dim, dim, list(v)) for v in ns]


def invariant_twists(n, typ):
    dim = N**n
    xs = sp.symbols(f"y0:{dim * dim}")
    C = sp.Matrix(dim, dim, xs)
    eqs = []
    for name, gen in TYPES[typ]["gens"].items():
        eqs += list(ad_gen(n, gen)(C) - TYPES[typ]["eps"][name] * C)
    rows = linear_rows(eqs, xs)
    ns = nullspace_exact(rows, dim * dim)
    return [sp.Matrix(dim, dim, list(v)) for v in ns]


def invariant_vectors(n, typ):
    dim = N**n
    mats = []
    for name, gen in TYPES[typ]["gens"].items():
        mats.append(gen_mat(n, gen) - TYPES[typ]["eps"][name] * sp.eye(dim))
    A = sp.Matrix.vstack(*mats)
    ns = nullspace_exact(A.tolist(), dim)
    return ns


# ================================================================ calibration
def calibration():
    ok = all(mz(sigma(2, 0) * Delta(2, k, i) - Delta(2, k, i) * sigma(2, 0)) for k in "EFK" for i in (0, 1))
    check("CAL R commutes with Delta(E_i), Delta(F_i), Delta(K_i) (variant B) on V(x)V", ok)
    ok = all(mz(ad_letter(1, k, i)(PIV) - (PIV if k in ("K", "Ki") else sp.zeros(3, 3))) for k in ("E", "F", "K", "Ki") for i in (0, 1))
    check("CAL gl3 pivotal diag(q^-4,q^-2,1) is ad*-invariant (reproduces T1)", ok)


# ================================================================ Q1
def Q1(typ):
    t = TYPES[typ]
    tau = t["tau"]
    # (Q1a) coproduct formula on V(x)V
    ok_all = True
    for idx, name in enumerate(["B1", "B2"]):
        i, j = idx, tau[idx]
        ci = [c1, c2][idx]
        lhs = gen_mat(2, t["gens"][name])
        first_leg = Kc[j] * Kci[i]
        rhs = (kron(gen_mat(1, t["gens"][name]), Kci[i]) + kron(I3, F[i])
               - ci * kron(first_leg, E[j] * Kci[i]))
        ok = mz(lhs - rhs)
        ok_all &= ok
        # first leg in B: identity (AI) or H^-1 (AIII)
        if typ == "AI":
            inB = first_leg == I3
        else:
            Hm = gen_mat(1, t["gens"]["H"])
            inB = mz(first_leg - Hm) or mz(first_leg * Hm - I3)      # H or H^-1
        ok_all &= inB
    check(f"Q1a [{typ}] Delta(B_i) = B_i(x)K_i^-1 + 1(x)F_i - c_i K_tau(i)K_i^-1(x)E_tau(i)K_i^-1, first legs in B "
          f"(right/'left' coideal Delta(B) in B(x)U, convention of the prereg)", ok_all)
    # (Q1b) commutes with sigma_i, n = 2,3
    ok = True
    for n in (2, 3):
        for name, gen in t["gens"].items():
            G = gen_mat(n, gen)
            for i in range(n - 1):
                ok &= mz(sigma(n, i) * G - G * sigma(n, i))
    ACC_B[typ] = ok
    check(f"Q1b [{typ}] every Delta^n(B generator) commutes with every sigma_i, n = 2,3 (structural: B in U)", ok)
    # (Q1c) transport
    P = sp.zeros(9, 9)
    for a in range(3):
        for b in range(3):
            P[b * 3 + a, a * 3 + b] = 1
    ACC_F[typ] = mz(R.subs(q, 1) - P)
    check(f"Q1c [{typ}] transport: R|_(q=1) = P (colour moves with the strand)", ACC_F[typ])


# ================================================================ Q2
def Q2(typ):
    t = TYPES[typ]
    gens1 = [gen_mat(1, g) for g in t["gens"].values()]
    com = commutant(gens1, 3)
    OUT[f"Q2a_{typ}_commutant_dim_on_V"] = len(com)
    OUT[f"Q2a_{typ}_commutant_basis_on_V"] = [str(sp.simplify(M)) for M in com]
    pred = 1 if typ == "AI" else 2
    check(f"Q2a [{typ}] commutant of B on C^3 has dim {pred} (prediction)", len(com) == pred, f"dim {len(com)}")
    res = {"type": typ, "J": None}
    if len(com) < 2:
        return res
    # pick the non-scalar direction J0 (orthogonal-ish to identity): any basis element not prop. to I
    J0 = None
    for M in com:
        if not mz(M - M[0, 0] * I3) or not all(z0(M[a, b]) for a in range(3) for b in range(3) if a != b):
            J0 = M
            break
    Jg = al * I3 + be * J0
    res["J0"] = J0
    OUT[f"Q2b_{typ}_J0"] = str(sp.simplify(J0))
    # eigenvalues / minimal polynomial of J0
    lam = sp.symbols("lam")
    cp = sp.factor(sp.cancel((J0 - lam * I3).det()))
    OUT[f"Q2b_{typ}_charpoly_J0"] = str(cp)
    ev = sp.roots(sp.Poly(sp.numer(sp.together((J0 - lam * I3).det())), lam))
    OUT[f"Q2b_{typ}_eigen_J0"] = {str(sp.simplify(k)): v for k, v in ev.items()}
    distinct = len(ev)
    # minimal polynomial degree: check whether (J0-a)(J0-b) = 0 for the distinct roots
    mp_deg2 = False
    if distinct == 2:
        r_ = list(ev.keys())
        mp_deg2 = mz((J0 - r_[0] * I3) * (J0 - r_[1] * I3))
    check(f"Q2b [{typ}] J0 has exactly 2 distinct eigenvalues and a quadratic minimal polynomial (type-B Hecke generator)",
          distinct == 2 and mp_deg2, f"charpoly {cp}; eigen {OUT[f'Q2b_{typ}_eigen_J0']}")
    # reflection equation for J = alpha I + beta J0
    T1 = kron(Jg, I3)
    RE = R * T1 * R * T1 - T1 * R * T1 * R
    nums = [sp.numer(sp.together(x)) for x in RE if not z0(x)]
    g = sp.factor(sp.gcd_list(nums)) if nums else 0
    OUT[f"Q2b_{typ}_RE_gcd_of_residuals"] = str(g)
    sol = sp.solve(nums, [al], dict=True) if nums else [{}]
    OUT[f"Q2b_{typ}_RE_solutions_alpha"] = [str(x) for x in sol]
    # the non-scalar solution line, normalised by beta = 1
    Jsol = None
    for sd in sol:
        if al in sd:
            Jsol = (Jg.subs(al, sd[al])).subs(be, 1)
    ok_inv = False
    if Jsol is not None:
        ok_inv = mz(Jsol * J0 - (Jsol * J0)[0, 0] * I3) and not z0((Jsol * J0)[0, 0])
        assert mz(R * kron(Jsol, I3) * R * kron(Jsol, I3) - kron(Jsol, I3) * R * kron(Jsol, I3) * R)
    res["Jsol"] = Jsol
    OUT[f"Q2b_{typ}_K_matrix"] = str(sp.simplify(Jsol)) if Jsol is not None else None
    check(f"Q2b [{typ}] the reflection equation has a non-scalar solution in the commutant pencil alpha*1 + beta*J0 "
          f"(prediction: J satisfies RE possibly after normalisation)", Jsol is not None,
          f"residual gcd {g}; solutions {sol}")
    check(f"Q2b [{typ}] the RE solution line is exactly J proportional to J0^-1", ok_inv, kind="posthoc")
    if Jsol is not None:
        lam = sp.symbols("lam")
        evs = sp.roots(sp.Poly(sp.numer(sp.together((Jsol - lam * I3).det())), lam))
        OUT[f"Q2b_{typ}_K_matrix_eigen"] = {str(sp.factor(k)): v for k, v in evs.items()}
        ks = list(evs.keys())
        if len(ks) == 2:
            OUT[f"Q2b_{typ}_K_eigen_ratio"] = str(sp.factor(ks[0] / ks[1]))
    # J (x) 1 (x) ... commutes with Delta^n(B)
    ok = True
    for n in (2, 3):
        Tn = kron(*([Jg] + [I3] * (n - 1)))
        for g in t["gens"].values():
            G = gen_mat(n, g)
            ok &= mz(Tn * G - G * Tn)
    check(f"Q2b [{typ}] J(x)1(x)..(x)1 commutes with Delta^n(B), n = 2,3 (cylinder: K on the first strand)", ok)
    # 1 (x) J does NOT (expected): record
    T2 = kron(I3, J0)
    okr = all(mz(T2 * gen_mat(2, g) - gen_mat(2, g) * T2) for g in t["gens"].values())
    check(f"Q2b [{typ}] 1(x)J0 does NOT commute with Delta(B) on V(x)V (the K-matrix belongs to the first strand only)",
          not okr, f"commutes={okr}")
    res["J"] = Jg
    return res


def markov_data(G1, G2, G3):
    """Normalised functional tr_n(x) = tr(G_n x)/tr(G_n) on H_n; returns (z, trace-property flag on H3,
    Markov flag on H2->H3, value on the (1^3) block)."""
    s1_2 = sigma(2, 0)
    s1, s2 = sigma(3, 0), sigma(3, 1)
    t1 = sp.cancel(G1.trace())
    t2 = sp.cancel((G2).trace())
    t3 = sp.cancel(G3.trace())
    z = sp.cancel((G2 * s1_2).trace() / t2) if not z0(t2) else None
    words = [sp.eye(27), s1, s2, s1 * s2, s2 * s1, s1 * s2 * s1]
    trace_ok = all(z0((G3 * (a * b - b * a)).trace()) for a in words for b in (s1, s2))
    # Markov: tr3(x s2) = z tr2(x) for x in H2 = span{1, s1}
    mk = None
    if z is not None and not z0(t3):
        mk = all(z0((G3 * x3 * s2).trace() / t3 - z * (G2 * x2).trace() / t2)
                 for x3, x2 in ((sp.eye(27), sp.eye(9)), (s1, s1_2)))
    # (1^3) block: rank-1 projector P = v u^T/(u^T v)
    A = sp.Matrix.vstack(s1 + sp.eye(27) / q, s2 + sp.eye(27) / q)
    v = A.nullspace()
    u = sp.Matrix.vstack((s1 + sp.eye(27) / q).T, (s2 + sp.eye(27) / q).T).nullspace()
    alt = None
    if len(v) == 1 and len(u) == 1:
        P = v[0] * u[0].T / (u[0].T * v[0])[0]
        alt = sp.factor(sp.cancel((G3 * P).trace() / t3)) if not z0(t3) else None
    return {"z": None if z is None else sp.factor(z), "trace_ok": trace_ok, "markov_ok": mk, "alt_weight": alt,
            "tr1": sp.factor(t1)}


def Q2cde(typ):
    # (Q2c) invariant twists on V and V(x)V
    inv1 = invariant_twists(1, typ)
    OUT[f"Q2c_{typ}_invariant_twists_V_dim"] = len(inv1)
    OUT[f"Q2c_{typ}_invariant_twists_V"] = [str(sp.simplify(M)) for M in inv1]
    pred = 1 if typ == "AI" else 2
    check(f"Q2c [{typ}] B-invariant twists on V: dim {pred} (prediction)", len(inv1) == pred, f"dim {len(inv1)}")
    piv_in = mz(ad_gen(1, TYPES[typ]["gens"]["B1"])(PIV))
    check(f"Q2c [{typ}] the gl3 pivotal is among them (sanity: B in U)", piv_in)
    inv2 = invariant_twists(2, typ)
    OUT[f"Q2c_{typ}_invariant_twists_VV_dim"] = len(inv2)
    # product twists T(x)T with T = alpha*PIV + beta*Y in inv1 span
    others = [M for M in inv1 if not mz(M - M[2, 2] * PIV)] if len(inv1) > 1 else []
    if others:
        Y = others[0]
        T = al * PIV + be * Y
        TT = kron(T, T)
        eqs = []
        for name, gen in TYPES[typ]["gens"].items():
            eqs += [x for x in (ad_gen(2, gen)(TT) - TYPES[typ]["eps"][name] * TT) if not z0(x)]
        nums = sp.factor_list(sp.gcd_list([sp.numer(sp.together(e)) for e in eqs]))[1] if eqs else []
        sol = sp.solve([sp.numer(sp.together(e)) for e in eqs], [al, be], dict=True) if eqs else [{}]
        OUT[f"Q2c_{typ}_productTT_solutions"] = [str(s) for s in sol]
        only_piv = all(s.get(be, None) == 0 or (be in s and z0(s[be])) for s in sol) and len(sol) > 0
        check(f"Q2c [{typ}] only (pivotal)(x)(pivotal) among product twists T(x)T, T in the V-invariant span, is B-invariant on V(x)V",
              only_piv, f"solutions {sol}")
        # does T1 (x) PIV lie in inv2 for all T1 in inv1? (prediction: later strands pivotal)
        ok = True
        for M in inv1:
            G = kron(M, PIV)
            ok &= all(mz(ad_gen(2, gen)(G) - TYPES[typ]["eps"][name] * G) for name, gen in TYPES[typ]["gens"].items())
        check(f"Q2c [{typ}] T1(x)pivotal is B-invariant on V(x)V for every V-invariant T1 (cylinder-type product twist)", ok)
        # Q2d: product twist on H3
        G1 = T
        G2 = kron(T, PIV)
        G3 = kron(T, PIV, PIV)
        md = markov_data(G1, G2, G3)
        OUT[f"Q2d_{typ}_product_twist"] = {k: str(v) for k, v in md.items()}
        check(f"Q2d [{typ}] product twist T1(x)piv(x)piv: functional on H3 is a trace (alpha, beta free)", md["trace_ok"],
              md["trace_ok"])
        zval = md["z"]
        is_zD = zval is not None and z0(zval - Z_D)
        is_z3 = zval is not None and z0(zval - Z_3)
        check(f"Q2d [{typ}] its Markov parameter tr2(sigma) is NOT z_D identically in (alpha, beta)", not is_zD,
              f"z = {zval}")
        OUT[f"Q2d_{typ}_z_equals_z3"] = bool(is_z3)
        ACC_D[typ] = bool(is_zD)
        check(f"Q2d [{typ}] prediction: the type-A Markov parameter of the product twist is z3 = q^3/[3]_q for all (alpha, beta)",
              is_z3, f"z = {zval}")
        # solve z = z_D for beta/alpha (selection flag only)
        if zval is not None and not is_zD and not is_z3:
            s = sp.solve(sp.numer(sp.together(zval - Z_D)), be)
            OUT[f"Q2d_{typ}_beta_that_would_give_zD_SELECTION_ONLY"] = [str(sp.factor(x)) for x in s]
    if not others:
        md = markov_data(PIV, kron(PIV, PIV), kron(PIV, PIV, PIV))
        OUT[f"Q2d_{typ}_pivotal_twist"] = {k: str(v) for k, v in md.items()}
        ACC_D[typ] = md["z"] is not None and z0(md["z"] - Z_D)
        check(f"Q2d [{typ}] prediction: the only B-invariant twist is the pivotal, whose Markov parameter is z3 (not z_D)",
              md["z"] is not None and z0(md["z"] - Z_3) and md["trace_ok"], f"z = {md['z']}")
    # (Q2e) D twists
    supports = {(0, 1): [q**-3, q**-1, 0], (0, 2): [q**-3, 0, q**-1], (1, 2): [0, q**-3, q**-1]}
    stab = {}
    for S, vals in supports.items():
        TD = sp.diag(*vals)
        eqs = []
        for name, gen in TYPES[typ]["gens"].items():
            eqs += [sp.numer(sp.together(x)) for x in (ad_gen(1, gen)(TD) - TYPES[typ]["eps"][name] * TD) if not z0(x)]
        sol = sp.solve(eqs, [c1, c2], dict=True) if eqs else [{}]
        stab[str(S)] = [str(s) for s in sol]
    OUT[f"Q2e_{typ}_Dtwist_c_solutions"] = stab
    nontriv = any(("c1: 0" not in s or "c2: 0" not in s) for v in stab.values() for s in v)
    check(f"Q2e [{typ}] no c with c != 0 makes a rank-2 D twist B-invariant (any support)", not nontriv, stab)


# ================================================================ Q3 / Q4
def lie_closure(mats):
    basis = []

    def indep(M, B):
        if not B:
            return not mz(M)
        A = sp.Matrix([list(x) for x in B] + [list(M)])
        return A.rank(simplify=True) > len(B)
    frontier = [M for M in mats]
    for M in mats:
        if indep(M, basis):
            basis.append(M)
    changed = True
    while changed:
        changed = False
        for a in list(basis):
            for b in list(basis):
                C = sp.expand(a * b - b * a)
                if indep(C, basis):
                    basis.append(C)
                    changed = True
    return basis


def Q3Q4(typ):
    t = TYPES[typ]
    # classical limit q -> 1 of the B generators (H -> derivative at q = 1)
    cl = []
    for name, g in t["gens"].items():
        M = gen_mat(1, g)
        if name == "H":
            cl.append(sp.diff(M, q).subs(q, 1))
        else:
            cl.append(M.subs(q, 1))
    L = lie_closure(cl)
    dimL = len(L)
    OUT[f"Q4_{typ}_classical_lie_dim"] = dimL
    # simple check: is L = sl3? (dim 8 required)
    pred = {"AI": 3, "AIII": 4}[typ]
    ACCEPT.setdefault(typ, {})["a_su3_dim8"] = (dimL == 8)
    ACCEPT[typ]["Q4_colour"] = (dimL == 8)
    check(f"Q3(a)/Q4 [{typ}] prediction: q->1 Lie closure of B has dim {pred}, not 8, so B is NOT colour "
          f"(acceptance (a) and Q4 FAIL as predicted)", dimL == pred, f"dim {dimL} (c1, c2 symbolic)")
    # Killing-form type: centre dimension of L
    xs = sp.symbols(f"w0:{dimL}")
    gen = sum((xs[k] * L[k] for k in range(dimL)), sp.zeros(3, 3))
    eqs = []
    for M in L:
        eqs += list(gen * M - M * gen)
    cen = sp.solve(eqs, xs, dict=True)
    OUT[f"Q4_{typ}_lie_basis"] = [str(M) for M in L]
    # B-commutant on V(x)V (U_q(gl3) would give 2)
    com2 = commutant([gen_mat(2, g) for g in t["gens"].values()], 9)
    OUT[f"Q3_{typ}_commutant_dim_VV"] = len(com2)
    check(f"Q3 [{typ}] commutant of B on V(x)V is larger than the Hecke image (dim 2), so B is a proper part of colour",
          len(com2) > 2, f"dim {len(com2)}")
    # (c) Hecke + braid
    s1, s2 = sigma(3, 0), sigma(3, 1)
    hk = mz((R - q * sp.eye(9)) * (R + sp.eye(9) / q))
    br = mz(s1 * s2 * s1 - s2 * s1 * s2)
    ACC_C[typ] = hk and br
    check(f"Q3(c) [{typ}] Hecke (sigma-q)(sigma+q^-1)=0 and braid relation on V^(x)3", hk and br)
    # (e) invariants
    inv2 = invariant_vectors(2, typ)
    inv3 = invariant_vectors(3, typ)
    OUT[f"Q3e_{typ}_B_invariants_dim_V2"] = len(inv2)
    OUT[f"Q3e_{typ}_B_invariants_dim_V3"] = len(inv3)
    ACCEPT[typ]["e_unique_singlet_V3"] = (len(inv3) == 1)
    ACCEPT[typ]["e_prime_no_singlet_V2"] = (len(inv2) == 0)
    if typ == "AI":
        check("Q3(e) [AI] prediction: dim 1 invariants in V^(x)3 AND dim 1 in V(x)V (so3 has a two-strand singlet)",
              len(inv3) == 1 and len(inv2) == 1, f"V3 {len(inv3)}, V2 {len(inv2)}")
    else:
        check("Q3(e) [AIII] prediction: dim > 1 invariants in V^(x)3 (classically 3)", len(inv3) > 1,
              f"V3 {len(inv3)}, V2 {len(inv2)}")
    # singlet-sector Hecke action
    if inv3:
        Vm = sp.Matrix.hstack(*inv3)
        acts = {}
        rows = []
        for k in range(27):
            if sp.Matrix([Vm.row(r) for r in rows + [k]]).rank() > len(rows):
                rows.append(k)
            if len(rows) == Vm.shape[1]:
                break
        Vsub = sp.Matrix([Vm.row(r) for r in rows])
        Vinv = Vsub.inv()
        for i, s in enumerate((s1, s2)):
            sol = Vinv * sp.Matrix([(s * Vm).row(r) for r in rows])
            sol = sol.applyfunc(lambda x: sp.factor(sp.cancel(x)))
            acts[f"sigma{i + 1}"] = str(sol)
            assert mz(Vm * sol - s * Vm)
        OUT[f"Q3d_{typ}_hecke_on_singlets"] = acts
        if len(inv3) == 1:
            ev = sp.cancel((s1 * Vm)[next(k for k in range(27) if not z0(Vm[k, 0])), 0]
                           / Vm[next(k for k in range(27) if not z0(Vm[k, 0])), 0])
            OUT[f"Q3d_{typ}_singlet_eigenvalue"] = str(sp.factor(ev))
    if inv2:
        Vm2 = sp.Matrix.hstack(*inv2)
        k0 = next(k for k in range(9) if not z0(Vm2[k, 0]))
        sol = sp.Matrix([[sp.cancel((R * Vm2)[k0, 0] / Vm2[k0, 0])]])
        assert mz(R * Vm2 - sol[0, 0] * Vm2)
        OUT[f"Q3e_{typ}_hecke_on_VV_singlets"] = str(sol.applyfunc(lambda x: sp.factor(sp.cancel(x))))


ACC_B, ACC_C, ACC_F, ACC_D = {}, {}, {}, {}


def main():
    calibration()
    for typ in ("AI", "AIII"):
        print(f"===== {typ}", flush=True)
        Q1(typ)
        Q2(typ)
        Q2cde(typ)
        Q3Q4(typ)
    npass = sum(c["pass"] for c in CHECKS)
    print(f"SUMMARY {npass}/{len(CHECKS)}")
    for typ in ACCEPT:
        ACCEPT[typ].update({"b_commutes": ACC_B[typ], "c_hecke_braid": ACC_C[typ], "f_transport": ACC_F[typ],
                            "d_zD_from_B_invariant_markov_twist": ACC_D[typ]})
    OUT["acceptance_a_to_f"] = ACCEPT
    OUT["checks"] = CHECKS
    OUT["summary"] = f"{npass}/{len(CHECKS)}"
    (HERE / "qcd_coideal_colour_probe.out.json").write_text(json.dumps(OUT, indent=1, default=str))
    sys.exit(0 if npass == len(CHECKS) else 1)


if __name__ == "__main__":
    main()
