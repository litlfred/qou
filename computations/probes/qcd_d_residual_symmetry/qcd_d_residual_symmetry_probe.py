#!/usr/bin/env python3
"""Residual symmetry of the convention-D colour twist: tests R1-R4 (bean qou-ni4b).

Pre-registration: PREREGISTRATION-d-residual-symmetry.md (commit 3f7b5b43e13).

Setting: (C^3)^(x)n with the Jimbo U_q(gl3) action, exactly as in
../qcd_colour_full_tower/qcd_colour_full_tower_probe.py (same R, same coproduct variant).
All arithmetic exact over Q(q) (sympy) or Q. No float. q0 not used.

Invariance of a twisted functional phi_C(Y) = tr(C Y) under the adjoint action is tested
through the dual action on C:  phi_C(ad_g Y) = phi_{ad*_g C}(Y), with (coproduct variant B,
Delta E = E(x)1 + K(x)E, Delta F = F(x)K^-1 + 1(x)F, S(E) = -K^-1 E, S(F) = -F K)
    ad*_E(C) = C E - K^-1 E C K,   ad*_F(C) = K C F - F K C,   ad*_K(C) = K^-1 C K - C.
For a product u = g h:  ad*_{gh} = ad*_h o ad*_g.  phi_C is u-invariant iff ad*_u(C) = 0
(all generators below have counit 0, or the K-form already subtracts eps).
"""
import itertools
import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "qcd_colour_full_tower"))
from qcd_colour_full_tower_probe import jimbo_R, kron, sigma_on, unit, partitions, schur  # noqa: E402

q = sp.symbols("q", positive=True)
h = q - 1 / q
Z_D = q**3 / (q**2 + 1)
CHECKS, OUT = [], {}


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "pass": bool(ok), "detail": str(detail)})
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + str(detail) if detail else ""))


def z0(e):
    return sp.cancel(sp.together(e)) == 0


def mz(M):
    return all(z0(x) for x in M)


N = 3
I3 = sp.eye(N)
R = jimbo_R(N, True)            # T1 found upper=True with coproduct variant B
E = [unit(N, 0, 1), unit(N, 1, 2)]
F = [unit(N, 1, 0), unit(N, 2, 1)]
Kc = [sp.diag(q, 1 / q, 1), sp.diag(1, q, 1 / q)]
Kci = [sp.diag(1 / q, q, 1), sp.diag(1, 1 / q, q)]


def Delta(n, kind, i):
    """Iterated coproduct (variant B) of E_i / F_i / K_i on (C^3)^(x)n."""
    if kind == "K":
        return kron(*([Kc[i]] * n))
    if kind == "Ki":
        return kron(*([Kci[i]] * n))
    out = sp.zeros(N**n, N**n)
    for p in range(n):
        if kind == "E":     # E at p, K on factors < p, 1 after
            fac = [Kc[i]] * p + [E[i]] + [I3] * (n - p - 1)
        else:               # F at p, 1 before, K^-1 after
            fac = [I3] * p + [F[i]] + [Kci[i]] * (n - p - 1)
        out += kron(*fac)
    return out


def ad_star(n, gen):
    """Return the map C -> ad*_gen(C) on End((C^3)^(x)n). gen in E1,F1,E2,F2,K1,K2."""
    kind, i = gen[0], int(gen[1]) - 1
    Kd, Kdi = Delta(n, "K", i), Delta(n, "Ki", i)
    if kind == "E":
        X = Delta(n, "E", i)
        return lambda C: C * X - Kdi * X * C * Kd
    if kind == "F":
        X = Delta(n, "F", i)
        return lambda C: Kd * C * X - X * Kd * C
    return lambda C: Kdi * C * Kd - C


def ad_star_word(n, word):
    maps = [ad_star(n, g) for g in word]

    def f(C):
        for m in maps:      # ad*_{g1 g2 ... gk} = ad*_{gk} o ... o ad*_{g1}; apply g1 first
            C = m(C)
        return C
    return f


def twist(support):
    """The rank-2 Markov twist found by T1 for this support, scale s = 1 (out.json)."""
    vals = {(0, 1): [q**-3, q**-1, 0], (0, 2): [q**-3, 0, q**-1], (1, 2): [0, q**-3, q**-1]}[support]
    return sp.diag(*vals)


PIV = sp.diag(q**-4, q**-2, 1)      # gl3 pivotal (unique invariant twist, T1)


def basis_words(n):
    """T_w as matrices on (C^3)^(x)n (reduced words by BFS)."""
    sig = [sigma_on(N, n, i, R) for i in range(n - 1)]
    mats, seen, frontier = {(): sp.eye(N**n)}, {tuple(range(n))}, [()]
    while frontier:
        new = []
        for w in frontier:
            for i in range(n - 1):
                perm = list(range(n))
                for j in w + (i,):
                    perm[j], perm[j + 1] = perm[j + 1], perm[j]
                if tuple(perm) in seen:
                    continue
                inv = sum(1 for a in range(n) for b in range(a + 1, n) if perm[a] > perm[b])
                if inv == len(w) + 1:
                    seen.add(tuple(perm))
                    mats[w + (i,)] = mats[w] * sig[i]
                    new.append(w + (i,))
        frontier = new
    return mats


# ============================================================ calibration
def calibration():
    ok = all(mz(ad_star(1, g)(PIV)) for g in ["E1", "F1", "E2", "F2", "K1", "K2"])
    check("CAL ad* convention: gl3 pivotal diag(q^-4,q^-2,1) is invariant under all generators (reproduces T1)", ok)
    KD = twist((0, 1))
    stab = [g for g in ["E1", "F1", "E2", "F2", "K1", "K2"] if mz(ad_star(1, g)(KD))]
    check("CAL support-{1,2} twist stabiliser = {E1,F1,K1,K2} (reproduces T1)", stab == ["E1", "F1", "K1", "K2"], stab)


# ============================================================ R1
def R1():
    KD = twist((0, 1))
    M = sp.simplify(PIV.inv() * KD)
    OUT["R1_M_support12"] = str(M)
    check("R1(b) K_D = g * M with M = q * P_12 (projector off colour 3)", mz(M - q * sp.diag(1, 1, 0)), M)

    # gl2 pivotal on the doublet: invariant twist for U_q(gl2) = <E1, F1, K1, gl2 centre> on C^2
    m = sp.symbols("m0:4")
    C2 = sp.Matrix(2, 2, m)
    e, f = unit(2, 0, 1), unit(2, 1, 0)
    k, ki = sp.diag(q, 1 / q), sp.diag(1 / q, q)
    eqs = list(C2 * e - ki * e * C2 * k) + list(k * C2 * f - f * k * C2) + list(ki * C2 * k - C2)
    sol = sp.solve(eqs, m, dict=True)[0]
    G2 = C2.subs(sol)
    free = sorted(G2.free_symbols - {q}, key=str)
    G2n = G2.subs({free[0]: 1}) if len(free) == 1 else None
    OUT["R1_gl2_invariant_twist"] = str(G2)
    restr = KD[:2, :2]
    prop = G2n is not None and mz(restr * G2n[0, 0] - G2n * restr[0, 0])
    check("R1(b) K_D restricted to the doublet is proportional to the U_q(gl2) pivotal (1-dim invariant space)",
          len(free) == 1 and prop, f"gl2 invariant twists {G2}, K_D|C2 = {restr}")

    # (C^2)^(x)n is R-stable and R restricted = gl2 Jimbo R (same convention)
    R2 = jimbo_R(2, True)
    sub2 = [a * N + b for a in range(2) for b in range(2)]
    out2 = [i for i in range(N * N) if i not in sub2]
    stable = all(z0(R[o, s]) for o in out2 for s in sub2)
    same = mz(R.extract(sub2, sub2) - R2)
    check("R1(b) C^2(x)C^2 is R-stable and R|_{C^2(x)C^2} = the gl2 Jimbo R", stable and same)

    # twisted trace == gl2 quantum trace on (C^2)^(x)n, every T_w, n <= 3, and Markov z_D
    allok = True
    for n in (1, 2, 3):
        Wn = basis_words(n)
        sub = [sum(c * N**(n - 1 - p) for p, c in enumerate(cs)) for cs in itertools.product(range(2), repeat=n)]
        Kn = kron(*([KD] * n))
        g2n = kron(*([restr] * n))
        for w, X in Wn.items():
            t3 = (Kn * X).trace()
            t2 = (g2n * X.extract(sub, sub)).trace()
            allok &= z0(t3 - t2)
    check("R1(b) tr_{(C^3)^n}(K_D^n X) = tr_{(C^2)^n}(g2^n X|) for every T_w, n <= 3", allok)

    # (c) U(1)s commuting with the residual gl2 inside the gl3 Cartan
    a = sp.symbols("a0:3")
    Hd = sp.diag(*a)
    eqs = list(Hd * E[0] - E[0] * Hd) + list(Hd * F[0] - F[0] * Hd)
    sol = sp.solve(eqs, a, dict=True)[0]
    comm = Hd.subs(sol)
    fr = sorted(comm.free_symbols, key=str)
    OUT["R1_cartan_commutant_of_gl2"] = str(comm)
    check("R1(c) Cartan elements commuting with gl2_{12}: 2-dim, span{diag(1,1,0), diag(0,0,1)}",
          len(fr) == 2 and z0(comm[0, 0] - comm[1, 1]), comm)
    # forced selection rule: K_D^(x)n * N3 = 0
    sel = True
    for n in (1, 2, 3):
        N3 = sum((kron(*([I3] * p + [unit(N, 2, 2)] + [I3] * (n - p - 1))) for p in range(n)), sp.zeros(N**n, N**n))
        sel &= mz(kron(*([KD] * n)) * N3)
    check("R1(c) forced datum: K_D^(x)n * N3 = 0, n <= 3 (D sees only the N3 = 0 sector)", sel)
    # traceless representative (a convention, not derived)
    trl = sp.solve([comm.trace()], fr[0], dict=True)
    Yt = comm.subs(trl[0]) if trl else None
    OUT["R1_traceless_u1_rep"] = str(Yt)
    check("R1(c) traceless (sl3) representative of the U(1) is proportional to diag(1,1,-2) [convention]",
          Yt is not None and z0(Yt[2, 2] + 2 * Yt[0, 0]) and z0(Yt[0, 0] - Yt[1, 1]), Yt)

    # (d) orientation against OverStrandWeight (h on e2 e1 = lower)
    res = {}
    for upper in (True, False):
        Rc = jimbo_R(2, upper)
        d = sp.symbols("d0:2")
        s = sp.symbols("s")
        P = sp.Matrix(2, 2, lambda A, Cc: sum(d[b] * Rc[A * 2 + b, Cc * 2 + b] for b in range(2)))
        sl = sp.solve(list(P - s * sp.eye(2)), list(d) + [s], dict=True)
        sols = [(sp.simplify(sl_[d[0]] / sl_[d[1]]) if d[1] in sl_ and d[0] in sl_ else None) for sl_ in sl]
        sols = [x for x in sols if x is not None and not z0(x)]
        if not sols:     # one variable free
            sols = [sp.simplify((d[0] / d[1]).subs(sl_)) for sl_ in sl]
        res[upper] = [str(x) for x in sols]
    OUT["R1_doublet_twist_ratio_d1_over_d2"] = {"h_on_e1e2 (T1 R)": res[True], "h_on_e2e1 (OverStrandWeight R)": res[False]}
    okd = res[True] == [str(q**-2)] and res[False] == [str(q**2)]
    check("R1(d) doublet twist d1/d2 = q^-2 under the T1 R, = q^2 under the OverStrandWeight R (orientation is Ř-convention-tied)",
          okd, res)


# ============================================================ R2
def R2():
    KD = twist((0, 1))
    trK = KD.trace()
    ok_comm, ok_tr, ok_cartan = True, True, True
    for n in (2, 3):
        N3 = sum((kron(*([I3] * p + [unit(N, 2, 2)] + [I3] * (n - p - 1))) for p in range(n)), sp.zeros(N**n, N**n))
        for i in range(n - 1):
            s = sigma_on(N, n, i, R)
            ok_comm &= mz(N3 * s - s * N3)
        for i in range(2):
            Kd = Delta(n, "K", i)
            ok_cartan &= all(mz(Kd * sigma_on(N, n, j, R) - sigma_on(N, n, j, R) * Kd) for j in range(n - 1))
        Kn = kron(*([KD] * n))
        for X in basis_words(n).values():
            ok_tr &= z0((Kn * (N3 * X - X * N3)).trace()) and z0((Kn * N3 * X).trace())
    check("R2(a) N3 commutes with every sigma_i on (C^3)^n, n = 2,3", ok_comm)
    check("R2(a) Delta(K1), Delta(K2) commute with every sigma_i, n = 2,3", ok_cartan)
    check("R2(b) tr(K_D^n [N3, T_w]) = 0 and tr(K_D^n N3 T_w) = 0 for every T_w, n = 2,3", ok_tr)
    # also: N3 commutes with the residual U_q(gl2) (Delta E1, Delta F1), n = 2
    N3_2 = kron(unit(N, 2, 2), I3) + kron(I3, unit(N, 2, 2))
    check("R2(a) N3 commutes with Delta(E1), Delta(F1) on (C^3)^2 (the U(1) is central in the residual)",
          mz(N3_2 * Delta(2, "E", 0) - Delta(2, "E", 0) * N3_2) and mz(N3_2 * Delta(2, "F", 0) - Delta(2, "F", 0) * N3_2))

    # (c) particle words on (C^3)^(x)3
    n = 3
    s0, s1 = sigma_on(N, n, 0, R), sigma_on(N, n, 1, R)
    s0i, s1i = s0 - h * sp.eye(N**n), s1 - h * sp.eye(N**n)
    check("R2 sanity: sigma_i^-1 = sigma_i - h", mz(s0 * s0i - sp.eye(N**n)))
    p0, p1, p01 = sp.symbols("phi0 phi1 phi01")
    words = {
        "photon 1+phi0 s0+phi1 s1+phi01 s0 s1^-1": sp.eye(N**n) + p0 * s0 + p1 * s1 + p01 * s0 * s1i,
        "electron s0 s1 s0 (Hopf closure)": s0 * s1 * s0,
        "electron backup trefoil s0^3 (in H_3)": s0 ** 3,
        "quark letter s0": s0, "quark letter s0^-1": s0i, "quark letter s1": s1, "quark letter s1^-1": s1i,
        "V^3 = (s0 s1^-1)^3 (Borromean core)": (s0 * s1i) ** 3,
    }
    N3 = sum((kron(*([I3] * p + [unit(N, 2, 2)] + [I3] * (n - p - 1))) for p in range(n)), sp.zeros(N**n, N**n))
    Kn = kron(*([KD] * n))
    charges, traces, allzero = {}, {}, True
    for name, X in words.items():
        c = N3 * X - X * N3
        zero = mz(c)
        allzero &= zero
        charges[name] = 0 if zero else "nonzero"
        traces[name] = str(sp.factor(sp.cancel((Kn * X).trace() / trK**n)))
    OUT["R2_word_adjoint_N3_charge"] = charges
    OUT["R2_word_D_trace_normalised"] = traces
    for k_, v in traces.items():
        print("   D-trace", k_, "=", v)
    check("R2(c) adjoint U(1) charge [N3, rho(w)] = 0 for photon, electron, trefoil, quark letters, V^3", allzero, charges)
    # D-trace cross-check: electron s0 s1 s0 normalised equals z_D^2 * tr(s0) ... Markov: tr(s0 s1 s0) = z * tr(s0^2)
    tD = lambda X: sp.cancel((Kn * X).trace() / trK**n)
    check("R2 D-trace sanity: tr(s0 s1 s0) = z_D tr(s0^2) (Markov on the electron word)",
          z0(tD(s0 * s1 * s0) - Z_D * tD(s0 * s0)))


# ============================================================ R3
def R3():
    gens = ["E1", "F1", "E2", "F2", "K1", "K2"]
    c = sp.symbols("c")
    res = {}
    for supp in [(0, 1), (0, 2), (1, 2)]:
        KD = twist(supp)
        M = sp.simplify(PIV.inv() * KD)
        st1 = [g for g in gens if mz(ad_star(1, g)(KD))]
        st2 = [g for g in gens if mz(ad_star(2, g)(kron(KD, KD)))]
        # non-simple root vectors E13 = E1E2 - c E2E1, F13 = F2F1 - c F1F2 ; solve for c at n=1, test at n=2
        nonsimple = {}
        for nm, (w1, w2) in {"E13": (("E1", "E2"), ("E2", "E1")), "F13": (("F2", "F1"), ("F1", "F2"))}.items():
            A1 = ad_star_word(1, w1)(KD)
            B1 = ad_star_word(1, w2)(KD)
            eqs = [sp.numer(sp.together(x)) for x in (A1 - c * B1)]
            eqs = [x for x in eqs if not z0(x)]
            sol = sp.solve(eqs, c, dict=True) if eqs else [{}]
            if eqs and sol:
                cv = sp.simplify(sol[0][c])
                A2 = ad_star_word(2, w1)(kron(KD, KD))
                B2 = ad_star_word(2, w2)(kron(KD, KD))
                nonsimple[nm] = {"c": str(cv), "invariant_n1": True, "invariant_n2": mz(A2 - cv * B2)}
            elif not eqs:
                nonsimple[nm] = {"c": "any", "invariant_n1": True, "invariant_n2": None}
            else:
                nonsimple[nm] = {"c": None, "invariant_n1": False, "invariant_n2": False}
        res[str([s + 1 for s in supp])] = {"K": str(list(KD.diagonal())), "M=g^-1 K": str(list(M.diagonal())),
                                           "stabiliser_n1": st1, "stabiliser_n2": st2, "nonsimple": nonsimple}
        print("   support", [s + 1 for s in supp], res[str([s + 1 for s in supp])])
    OUT["R3_per_support"] = res
    r12, r13, r23 = res["[1, 2]"], res["[1, 3]"], res["[2, 3]"]
    check("R3(a) support {1,2}: stabiliser {E1,F1,K1,K2} at n=1 and n=2",
          r12["stabiliser_n1"] == r12["stabiliser_n2"] == ["E1", "F1", "K1", "K2"])
    check("R3(a) support {2,3}: stabiliser {E2,F2,K1,K2} at n=1 and n=2",
          r23["stabiliser_n1"] == r23["stabiliser_n2"] == ["E2", "F2", "K1", "K2"], r23["stabiliser_n1"])
    check("R3(a) support {1,3}: no simple root vector survives (Cartan K1,K2 only among Chevalley generators)",
          r13["stabiliser_n1"] == ["K1", "K2"], r13["stabiliser_n1"])
    ns13 = r13["nonsimple"]
    check("R3(a) support {1,3}: no E13/F13 of the form E1E2 - c E2E1 (resp. F2F1 - c F1F2) is invariant",
          not ns13["E13"]["invariant_n1"] and not ns13["F13"]["invariant_n1"], ns13)
    check("R3(a) support {1,3}: M = g^-1 K is not proportional to a projector (distinct eigenvalues q, 0, q^-1)",
          r13["M=g^-1 K"] == str([q, 0, 1 / q]), r13["M=g^-1 K"])
    # POST-HOC (added after the first run, which FAILED the pre-registered {1,3} prediction above):
    # are the surviving E13 = E1E2 - q E2E1, F13 = F2F1 - q^-1 F1F2 a q-sl2 for the root a1+a2?
    E13 = E[0] * E[1] - q * E[1] * E[0]
    F13 = F[1] * F[0] - F[0] * F[1] / q
    K13, K13i = Kc[0] * Kc[1], Kci[0] * Kci[1]
    lam = sp.symbols("lam")
    comm = E13 * F13 - F13 * E13
    rhs = (K13 - K13i) / (q - 1 / q)
    sol = sp.solve([sp.numer(sp.together(x)) for x in (comm - lam * rhs) if not z0(x)], lam, dict=True)
    OUT["R3_posthoc_E13_F13"] = {"E13": str(E13), "F13": str(F13), "[E13,F13]/((K13-K13^-1)/(q-q^-1))": str(sol)}
    check("R3 POST-HOC: E13 = E1E2 - qE2E1 = e_13, F13 = F2F1 - q^-1 F1F2 = e_31 up to sign/scale, and "
          "[E13,F13] is a nonzero multiple of (K1K2 - (K1K2)^-1)/(q - q^-1) on C^3: a root-(a1+a2) q-sl2 survives on {1,3}",
          bool(sol) and not z0(sol[0][lam]) and sum(1 for x in E13 if not z0(x)) == 1 and not z0(E13[0, 2])
          and sum(1 for x in F13 if not z0(x)) == 1 and not z0(F13[2, 0]), sol)
    # (b) identical trace on H_n: same eigenvalue multiset => identical Schur weights
    same = True
    for n in range(2, 7):
        for lam in partitions(n):
            if len(lam) > 3:
                continue
            vals = [schur(lam, list(twist(s).diagonal())) for s in [(0, 1), (0, 2), (1, 2)]]
            same &= z0(vals[0] - vals[1]) and z0(vals[0] - vals[2])
    check("R3(b) all three supports give identical y_lambda = s_lambda(K)/(trK)^n, n <= 6 (same eigenvalue multiset)", same)


# ============================================================ R4
def R4():
    # traceless U(1) commuting with the residual sl2, per support; charge ratio singlet/doublet
    ratios = {}
    for supp, (Ee, Ff) in {(0, 1): (E[0], F[0]), (1, 2): (E[1], F[1])}.items():
        a = sp.symbols("a0:3")
        Hd = sp.diag(*a)
        sol = sp.solve(list(Hd * Ee - Ee * Hd) + list(Hd * Ff - Ff * Hd) + [Hd.trace()], a, dict=True)[0]
        Y = Hd.subs(sol)
        fr = sorted(Y.free_symbols, key=str)
        Y = Y.subs({fr[0]: 1})
        sing = [i for i in range(3) if i not in supp][0]
        ratios[str([s + 1 for s in supp])] = {"Y": str(list(Y.diagonal())),
                                              "singlet/doublet": str(sp.nsimplify(Y[sing, sing] / Y[supp[0], supp[0]]))}
    OUT["R4_traceless_u1"] = ratios
    check("R4 traceless U(1): singlet/doublet charge ratio = -2 for both simple-root supports [forced by tracelessness only]",
          all(v["singlet/doublet"] == "-2" for v in ratios.values()), ratios)
    # without the traceless convention the ratio is free: Y = diag(1,1,0) + t*Id gives ratio t/(1+t)
    t = sp.symbols("t")
    Yt = sp.diag(1, 1, 0) + t * sp.eye(3)
    rr = sp.simplify(Yt[2, 2] / Yt[0, 0])
    OUT["R4_ratio_with_centre_shift"] = str(rr)
    check("R4 with the gl3 centre added (Y + t*Id) the ratio is t/(t+1): not normalisation-free", z0(rr - t / (t + 1)), rr)
    # mixing ratio: Tr(T3^2)/Tr(Y^2) on C^3 depends on Y's scale -> no parameter-free angle
    s_ = sp.symbols("s", positive=True)
    T3 = sp.diag(sp.Rational(1, 2), -sp.Rational(1, 2), 0)
    Ys = s_ * sp.diag(1, 1, -2)
    mix = sp.simplify((T3**2).trace() / ((T3**2).trace() + (Ys**2).trace()))
    OUT["R4_mixing_family"] = str(mix)
    check("R4 the would-be mixing Tr T3^2/(Tr T3^2 + Tr Y^2) depends on the free U(1) scale s: no Weinberg angle is forced",
          len(mix.free_symbols) == 1, mix)
    # the twist itself carries no relative coupling: the residual sl2 and U(1) commute and are orthogonal
    # under the trace form on C^3
    check("R4 Tr(T3 * Y) = 0: residual sl2 and traceless U(1) are trace-orthogonal (no forced mixing)",
          z0((T3 * sp.diag(1, 1, -2)).trace()))


def main():
    calibration()
    R1()
    R2()
    R3()
    R4()
    npass = sum(c["pass"] for c in CHECKS)
    OUT["checks"] = CHECKS
    OUT["summary"] = f"{npass}/{len(CHECKS)}"
    print("SUMMARY", OUT["summary"])
    Path(__file__).with_suffix(".out.json").write_text(json.dumps(OUT, indent=1, default=str))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
