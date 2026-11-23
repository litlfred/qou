#!/usr/bin/env python3
"""Is Gresnigt's Clifford braid representation a Hecke representation in disguise?

Issue #9096. Pre-registration: PREREG.md in this directory (committed first).

Source matrices: library/arxiv-1901.01312v1 (Gresnigt, "Braided fermions from Hurwitz
algebras") §4.2 pp.4-5 (Kauffman-Lomonaco sigma_k = (1 + e_{k+1} e_k)/sqrt2 in Cl(n,0))
and §4.3 pp.5-6 (C rep of B_2, H rep of B_3^c). arxiv-1711.09011v1, named in the task, is
NOT held in library/.

Repo Hecke convention: T^2 = (q - q^-1) T + 1. Exact arithmetic only (sympy, Q(zeta_8));
every check is an exact zero test. No floats anywhere. The point q = zeta_8 is FIXED BY
GRESNIGT'S CONSTRUCTION; it is a specialisation of our formal q, not a q0 candidate.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import sympy as sp
from sympy import I, Matrix, Rational, eye, sqrt, zeros

HERE = Path(__file__).resolve().parent
ZETA = (1 + I) / sqrt(2)  # zeta_8 = e^{i pi/4}
CHECKS: list[tuple[str, bool, str]] = []


def z0(expr) -> bool:
    """Exact zero test in Q(zeta_8) (expand + nsimplify-free)."""
    e = sp.nsimplify(sp.expand(sp.simplify(expr)), rational=False)
    return sp.simplify(e) == 0


def mz(M: Matrix) -> bool:
    return all(z0(x) for x in M)


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def s(x) -> str:
    return str(sp.simplify(x))


# ---------------------------------------------------------------- matrices
# Quaternions in M_2(C): I_q = diag(i,-i), J_q = [[0,1],[-1,0]], K_q = I_q J_q.
Iq = Matrix([[I, 0], [0, -I]])
Jq = Matrix([[0, 1], [-1, 0]])
Kq = Iq * Jq
E2 = eye(2)
quat_sigma = [(E2 + Iq) / sqrt(2), (E2 + Jq) / sqrt(2), (E2 + Kq) / sqrt(2)]

# Complex rep of B_2: sigma = (1+i)/sqrt2. As a REAL 2x2 matrix (C = Cl(0,1)) and over C.
cplx_sigma_real = Matrix([[1, -1], [1, 1]]) / sqrt(2)
cplx_sigma_1d = Matrix([[ZETA]])

# Cl(4,0) gamma matrices, e_k^2 = 1, anticommuting.
px = Matrix([[0, 1], [1, 0]])
py = Matrix([[0, -I], [I, 0]])
pz = Matrix([[1, 0], [0, -1]])
kron = sp.kronecker_product
e = [kron(px, E2), kron(py, E2), kron(pz, px), kron(pz, py)]
E4 = eye(4)
cl4_sigma = [(E4 + e[k + 1] * e[k]) / sqrt(2) for k in range(3)]  # B_4 (non-circular)
cl4_sigma_circ = (E4 + e[0] * e[3]) / sqrt(2)                     # sigma_4 of B_4^c


def braid(a: Matrix, b: Matrix) -> Matrix:
    return a * b * a - b * a * b


# ---------------------------------------------------------------- C1 / C2
def c1_c2() -> dict:
    out = {}
    for k in range(4):
        for l in range(4):
            if k != l:
                check(f"Cl4 anticomm e{k+1}e{l+1}", mz(e[k] * e[l] + e[l] * e[k]))
        check(f"Cl4 e{k+1}^2=1", mz(e[k] ** 2 - E4))
    allgens = {
        "C_real": [cplx_sigma_real], "C_1d": [cplx_sigma_1d],
        "H": quat_sigma, "Cl4": cl4_sigma + [cl4_sigma_circ],
    }
    for name, gens in allgens.items():
        for j, g in enumerate(gens):
            n = g.shape[0]
            if name != "C_1d":
                check(f"C1 {name} sigma{j+1}: s^2 - sqrt2 s + 1 = 0",
                      mz(g * g - sqrt(2) * g + eye(n)))
            check(f"C1 {name} sigma{j+1}: order 8 (s^4=-1)",
                  mz(g ** 4 + eye(n)) and mz(g ** 8 - eye(n)))
    ev = sorted(map(s, cplx_sigma_real.eigenvals().keys()))
    out["eigenvalues_sigma"] = ev
    check("C1 eigenvalues are zeta8^{+-1}",
          set(cplx_sigma_real.eigenvals()) and all(
              z0(x - ZETA) or z0(x - sp.conjugate(ZETA))
              for x in quat_sigma[0].eigenvals()), str(ev))
    # braid relations
    a, b, c = quat_sigma
    for (u, v, nm) in [(a, b, "12"), (b, c, "23"), (c, a, "31")]:
        check(f"C2 H B3^c braid {nm}", mz(braid(u, v)))
    s1, s2, s3 = cl4_sigma
    check("C2 Cl4 B4 braid 12", mz(braid(s1, s2)))
    check("C2 Cl4 B4 braid 23", mz(braid(s2, s3)))
    check("C2 Cl4 B4 far-commute 13", mz(s1 * s3 - s3 * s1))
    check("C2 Cl4 B4^c braid 34", mz(braid(s3, cl4_sigma_circ)))
    check("C2 Cl4 B4^c braid 41", mz(braid(cl4_sigma_circ, s1)))
    check("C2 Cl4 B4^c far-commute 24", mz(s2 * cl4_sigma_circ - cl4_sigma_circ * s2))
    return out


# ---------------------------------------------------------------- C3 / C4
def c3_c4() -> dict:
    """Enumerate all scalars c, q with (c sigma)^2 = (q - q^-1)(c sigma) + 1.

    sigma (in every rep of dim >= 2 here) is diagonalisable with DISTINCT eigenvalues
    zeta, zeta^-1, so tau = c sigma satisfies a monic quadratic x^2 - h x - 1 iff
    {c zeta, c zeta^-1} is its root set: product c^2 = -1, sum c sqrt2 = h = q - q^-1.
    """
    c, q = sp.symbols("c q")
    csol = sp.solve(sp.Eq(c ** 2, -1), c)
    rows = []
    for cv in csol:
        h = sp.simplify(cv * sqrt(2))
        qs = sp.solve(sp.Eq(q - 1 / q, h), q)
        qs_nf = []
        for qv in qs:
            # identify as power of zeta8
            k = [m for m in range(8) if z0(qv - ZETA ** m)]
            qs_nf.append({"q": s(qv), "zeta8_power": k[0] if k else None})
        rows.append({"c": s(cv), "q_minus_qinv": s(h), "q_solutions": qs_nf})
        # verify on actual matrices, all generators
        for qd in qs:
            hh = qd - 1 / qd
            ok = True
            for g in quat_sigma + cl4_sigma + [cl4_sigma_circ, cplx_sigma_real]:
                t = cv * g
                ok &= mz(t * t - hh * t - eye(g.shape[0]))
            check(f"C3 c={s(cv)} q={s(qd)}: Hecke on all generators", ok)
    check("C3 c=1 (no rescale) is NOT Hecke on 2-dim reps (eigenvalue product 1 != -1)",
          not mz(quat_sigma[0] ** 2 - (ZETA - 1 / ZETA) * quat_sigma[0] - E2))
    check("C3 c real impossible (c^2=-1 has no real root)", all(not sp.im(x) == 0 for x in csol))
    # 1-dim complex rep: any c works (tau = q or tau = -q^-1)
    one_d = {"note": "1-dim rep sigma=zeta8: for any c != 0, tau=c*zeta8 is the trivial rep "
                     "with q = c*zeta8, or the sign rep with q = -1/(c*zeta8). With c=1: "
                     "q = zeta8 (trivial) or q = zeta8^3 (sign). The quadratic s^2 - sqrt2 s + 1 "
                     "is the minimal polynomial over R (C as the real algebra Cl(0,1))."}
    # C4: braid relation with per-generator scalars c_i requires c_i = c_{i+1}
    c1, c2 = sp.symbols("c1 c2", nonzero=True)
    lhs = c1 ** 2 * c2
    rhs = c1 * c2 ** 2
    sol = sp.solve(sp.Eq(lhs, rhs), c2)
    check("C4 c1^2 c2 = c1 c2^2 (nonzero) forces c2 = c1", sol == [c1], str(sol))
    for cv in csol:
        tg = [cv * g for g in quat_sigma]
        check(f"C4 tau=({s(cv)})sigma keeps H B3^c braid relations",
              all(mz(braid(u, v)) for u, v in [(tg[0], tg[1]), (tg[1], tg[2]), (tg[2], tg[0])]))
    return {"rescalings": rows, "one_dim": one_d}


# ---------------------------------------------------------------- Hecke algebra tools
def qint(k, q):
    return sp.simplify((q ** k - q ** (-k)) / (q - 1 / q))


def reduced_word(perm):
    """Bubble-sort reduced word (1-indexed simple transpositions) for a permutation tuple."""
    p = list(perm)
    word = []
    n = len(p)
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                word.append(i + 1)
                changed = True
    return list(reversed(word))


def T_w(gens, word, n):
    M = eye(n)
    for i in word:
        M = M * gens[i - 1]
    return M


def standard_tableaux(shape):
    n = sum(shape)
    cells = [(r, c) for r, L in enumerate(shape) for c in range(L)]
    res = []
    for perm in itertools.permutations(range(1, n + 1)):
        t = dict(zip(cells, perm))
        ok = all(t[(r, c)] < t[(r, c + 1)] for (r, c) in cells if (r, c + 1) in t) and \
             all(t[(r, c)] < t[(r + 1, c)] for (r, c) in cells if (r + 1, c) in t)
        if ok:
            res.append({v: k for k, v in t.items()})
    return res


def seminormal(shape, q):
    """Young seminormal form for T^2 = (q - q^-1)T + 1 over generic q."""
    tabs = standard_tableaux(shape)
    n = sum(shape)
    d = len(tabs)
    idx = {tuple(sorted(t.items())): k for k, t in enumerate(tabs)}
    gens = []
    for i in range(1, n):
        M = zeros(d, d)
        for k, t in enumerate(tabs):
            (r1, c1), (r2, c2) = t[i], t[i + 1]
            if r1 == r2:
                M[k, k] = q
            elif c1 == c2:
                M[k, k] = -1 / q
            else:
                ax = (c2 - r2) - (c1 - r1)
                M[k, k] = q ** ax / qint(ax, q)
                t2 = dict(t)
                t2[i], t2[i + 1] = t[i + 1], t[i]
                k2 = idx[tuple(sorted(t2.items()))]
                # pair (k,k2): put b=1 above, c = 1 - 1/[ax]^2 below (det -1)
                if k < k2:
                    M[k, k2] = 1
                else:
                    M[k, k2] = 1 - 1 / qint(ax, q) ** 2
        gens.append(M)
    return gens


def partitions(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for p in partitions(n - k, k):
            yield (k,) + p


# ---------------------------------------------------------------- C5 / C6 / C7
def c5_c6_c7() -> dict:
    qs = sp.Symbol("q")
    out = {}
    # q-integers at zeta8 for both labellings
    for lab, qv in [("q=zeta8", ZETA), ("q=zeta8^3", ZETA ** 3)]:
        out[f"qints_{lab}"] = {k: s(qint(k, qs).subs(qs, qv)) for k in range(1, 5)}
        fac = {n: s(sp.prod([qint(k, qs).subs(qs, qv) for k in range(1, n + 1)])) for n in range(1, 5)}
        out[f"qfactorial_{lab}"] = fac
    check("C5 [4]_q = 0 at zeta8 (H_4 non-semisimple)", z0(qint(4, qs).subs(qs, ZETA)))
    check("C5 [3]_q! != 0 at zeta8 (H_3 semisimple)",
          not z0(sp.prod([qint(k, qs).subs(qs, ZETA) for k in (1, 2, 3)])))

    results = {}
    for lab, qv, cv in [("q=zeta8,c=i", ZETA, I), ("q=zeta8^3,c=i", ZETA ** 3, I)]:
        R = {}
        # Specht characters of H_3, H_4 on all T_w, generic seminormal form then specialise
        for n in (3, 4):
            perms = list(itertools.permutations(range(1, n + 1)))
            words = [reduced_word(p) for p in perms]
            chars = {}
            for lam in partitions(n):
                g = seminormal(lam, qs)
                for i in range(len(g) - 1):
                    assert mz(braid(g[i], g[i + 1])), lam
                chars[lam] = [sp.simplify(T_w(g, w, g[0].shape[0] if g else 1).trace().subs(qs, qv))
                              if g else 1 for w in words]
            # our modules
            if n == 3:
                mods = {"H(quaternion) dim2": [cv * quat_sigma[0], cv * quat_sigma[1]]}
            else:
                mods = {"Cl4 dim4": [cv * x for x in cl4_sigma]}
            for mname, gens in mods.items():
                dim = gens[0].shape[0]
                chi = [sp.simplify(T_w(gens, w, dim).trace()) for w in words]
                # express chi as integer combination of Specht characters (solve exactly)
                lams = list(chars)
                a = sp.symbols(f"a0:{len(lams)}")
                eqs = [sum(a[j] * chars[lams[j]][k] for j in range(len(lams))) - chi[k]
                       for k in range(len(words))]
                sol = sp.solve([sp.expand(x) for x in eqs], a, dict=True)
                R[f"n{n} {mname} specht-character solutions"] = [
                    {str(lams[j]): s(sl.get(a[j], a[j])) for j in range(len(lams))} for sl in sol]
                # TL: kill x_- = sum (-q^-1)^l T_w and x_+ = sum q^l T_w on 3 strands
                p3 = list(itertools.permutations(range(1, 4)))
                w3 = [reduced_word(p) for p in p3]
                for shift in range(n - 2):
                    gg = gens[shift:shift + 2]
                    xm = sum((T_w(gg, w, dim) * (-1 / qv) ** len(w) for w in w3), zeros(dim, dim))
                    xp = sum((T_w(gg, w, dim) * qv ** len(w) for w in w3), zeros(dim, dim))
                    R[f"n{n} {mname} strands{shift+1}-{shift+3} kills x_minus"] = mz(xm)
                    R[f"n{n} {mname} strands{shift+1}-{shift+3} kills x_plus"] = mz(xp)
                # Markov property of normalised trace on H_{n-1} subset H_n
                t = lambda M: M.trace() / dim  # noqa: E731
                z = sp.simplify(t(gens[n - 2]))
                pm = list(itertools.permutations(range(1, n)))
                ok = all(z0(t(T_w(gens, reduced_word(p), dim) * gens[n - 2])
                             - z * t(T_w(gens, reduced_word(p), dim))) for p in pm)
                zD = sp.simplify(qv ** 3 / (qv ** 2 + 1))
                R[f"n{n} {mname} normalised-trace z=t(T_(n-1))"] = s(z)
                R[f"n{n} {mname} Markov property on H_(n-1) subset H_n"] = ok
                R[f"n{n} z_D=q^3/(q^2+1) at {lab}"] = s(zD)
                R[f"n{n} z == z_D"] = z0(z - zD)
                # Markov trace at z_D: Ocneanu weights via Markov recursion on S_n basis
            # submodules of Cl4: chirality halves gamma = e1e2e3e4
            if n == 4:
                gam = e[0] * e[1] * e[2] * e[3]
                Rh = {}
                for sign in (1, -1):
                    P = (E4 + sign * gam) / 2
                    cols = P.columnspace()
                    B = Matrix.hstack(*cols)
                    Binv = (B.H * B).inv() * B.H
                    gens_h = [sp.simplify(Binv * (cv * x) * B) for x in cl4_sigma]
                    for x in cl4_sigma:
                        assert mz((E4 - P) * (cv * x) * P)
                    chi = [sp.simplify(T_w(gens_h, w, 2).trace()) for w in words]
                    lams = list(chars)
                    a = sp.symbols(f"b0:{len(lams)}")
                    eqs = [sum(a[j] * chars[lams[j]][k] for j in range(len(lams))) - chi[k]
                           for k in range(len(words))]
                    sol = sp.solve([sp.expand(x) for x in eqs], a, dict=True)
                    tau1, tau3 = gens_h[0], gens_h[2]
                    Rh[f"gamma={sign:+d}"] = {
                        "specht_character_solutions": [
                            {str(lams[j]): s(sl.get(a[j], a[j])) for j in range(len(lams))} for sl in sol],
                        "tau3 == tau1": mz(tau3 - tau1),
                        "tau3 == -tau1^-1": mz(tau3 + tau1.inv()),
                        "irreducible(tau1,tau2 commute?)": not mz(gens_h[0] * gens_h[1] - gens_h[1] * gens_h[0]),
                        "trace tau1": s(tau1.trace()),
                        "trace tau1 tau3": s((tau1 * tau3).trace()),
                    }
                R["Cl4 chirality halves"] = Rh
                # Specht chars on T1, T1T3 at this q for reference
                w13 = [1, 3]
                R["specht chi(T1), chi(T1T3)"] = {
                    str(l): [s(chars[l][words.index([1])]),
                             s(chars[l][words.index(w13)] if w13 in words else chars[l][words.index([3, 1])])]
                    for l in chars}
        results[lab] = R
    out["per_labelling"] = results
    return out


def main() -> int:
    rec = {"source": "library/arxiv-1901.01312v1 sec 4.2 (pp.4-5), sec 4.3 (pp.5-6)",
           "task_named_source_held": False,
           "hecke_convention": "T^2 = (q - q^-1) T + 1",
           "q_status": "zeta8 fixed by Gresnigt's construction; specialisation of formal q; NOT q0",
           "q0Anchor": "independent",
           "q0AnchorReason": "zeta8 fixed by Gresnigt's construction; formal q specialisation only, q0 never read"}
    rec["C1_C2"] = c1_c2()
    rec["C3_C4"] = c3_c4()
    rec["C5_C6_C7"] = c5_c6_c7()
    for lab, R in rec["C5_C6_C7"]["per_labelling"].items():
        print("==", lab)
        for k, v in R.items():
            print("  ", k, ":", v)
    rec["checks"] = [{"name": n, "pass": p, "detail": d} for n, p, d in CHECKS]
    rec["n_pass"] = sum(p for _, p, _ in CHECKS)
    rec["n_fail"] = sum(not p for _, p, _ in CHECKS)
    (HERE / "gresnigt-hecke.witness.json").write_text(json.dumps(rec, indent=1, default=str) + "\n")
    print(f"{rec['n_pass']} pass / {rec['n_fail']} fail")
    return 0 if rec["n_fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
