#!/usr/bin/env python3
"""single_level_binding_gg_probe.py — the corpus single-level binding sum on γγ candidate words.

Issue #8983. Recipe: PREREGISTRATION.md in this directory (committed before this file).

    Binding(K) = m_e Σ_{λ ⊢ 3A} y_λ χ^λ(β_K) Δ_λ,   Δ_λ = (−1)^{n(λ)} f^λ,
    y_λ = convention-D Markov weight (SU(2) hook-content, y_lambda_su_n(n, q, 2)), proton pin.

Words: nucleon V(3j)^m (m in {3,6}), bond V(s_j)^k (k in {1,2,3}) at the two vertices that
straddle each inter-nucleon cut, chain layout, both bond orders; free word k = 0. V(s) = σ_s σ_{s+1}^{-1}.
Two-row characters from the Rust MPFR kernel (pyhecke_native.lp_accumulator_step_traces_mpfr)
and from an mpmath Young seminormal representation built here (also used for reading 3 at every
level). mpmath 70 dps throughout; floats only in display strings. AME2020 only as a final column.

-- Ref: [leitner2026] mass-endomorphism/recomputed-low-isotope-mass-table (direct binding form);
   QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional; QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows
"""
from __future__ import annotations

import itertools
import json
import multiprocessing as mpc
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

DPS = 70
mp.mp.dps = DPS
HERE = Path(__file__).resolve().parent
COMP = HERE.parent.parent
for p in (COMP, COMP / "substrate"):
    sys.path.insert(0, str(p))

import pyhecke_native as phn  # noqa: E402
from qou_substrate.constants import q_at, M_E_MEV_STR  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402

T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:8.1f}s] {msg}", flush=True)


Q = q_at(DPS + 10)
mp.mp.dps = DPS
Q = +Q
QS = mp.nstr(Q, DPS + 5, strip_zeros=False)
ME = mp.mpf(M_E_MEV_STR)
TOL = mp.mpf(10) ** (-40)


def setq(qv):
    global Q, QS
    Q = mp.mpf(qv)
    QS = mp.nstr(Q, DPS + 5, strip_zeros=False)


def H():
    return Q - 1 / Q


def qint(r):
    if Q == 1:
        return mp.mpf(r)
    return (Q ** r - Q ** (-r)) / (Q - 1 / Q)


# ── partitions, f^λ, Δ_λ, y_λ ──────────────────────────────────────────────

def partitions(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def flam(lam):
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    hp = 1
    for i, r in enumerate(lam):
        for j in range(r):
            hp *= (r - j - 1) + (conj[j] - i - 1) + 1
    return mp.factorial(n) / hp


def nlam(lam):
    return sum(i * r for i, r in enumerate(lam))


def delta(lam):
    return (-1) ** nlam(lam) * flam(lam)


def y2(lam):
    """Two-row convention-D weight [λ1−λ2+1]/[2]^n (balanced q-integers)."""
    lam = tuple(lam) + (0,) * (2 - len(lam))
    return qint(lam[0] - lam[1] + 1) / qint(2) ** (lam[0] + lam[1])


def two_row(n):
    return [l for l in partitions(n) if len(l) <= 2]


# ── words ──────────────────────────────────────────────────────────────────
# letter = (c, d, g): c·σ_g + d, g 0-based. σ^{-1} = σ − h.

def V(s):
    return [("1", "0", s), ("1", "-h", s + 1)]


def nucleon(j, m):
    return V(3 * j) * m


def bond(j, o, k):
    return V(3 * j + o) * k


def word_assembled(A, m, k, offs, order="asc"):
    w = []
    for j in range(A):
        w += nucleon(j, m)
    idx = list(range(A - 1))
    if order == "desc":
        idx.reverse()
    for j in idx:
        w += bond(j, offs[j], k) if k else []
    return w


def word_route(A, m, k, offs, route):
    if route == "sequential":   # N0 N1 K0 N2 K1 N3 K2
        w = nucleon(0, m)
        for j in range(1, A):
            w += nucleon(j, m) + bond(j - 1, offs[j - 1], k)
        return w
    if route == "DD":           # N0 N1 K0 N2 N3 K2 K1  (A = 4)
        return (nucleon(0, m) + nucleon(1, m) + bond(0, offs[0], k) + nucleon(2, m) + nucleon(3, m)
                + bond(2, offs[2], k) + bond(1, offs[1], k))
    raise ValueError(route)


def normal_form(word):
    """Lexicographic normal form in the partially commutative monoid (letters on generators
    with |g − g'| ≥ 2 commute). Equal normal forms ⇒ equal Hecke elements."""
    w = list(word)
    out = []
    while w:
        best = None
        for i, a in enumerate(w):
            if all(abs(a[2] - b[2]) >= 2 for b in w[:i]):
                if best is None or a < w[best]:
                    best = i
        out.append(w.pop(best))
    return tuple(out)


def realise(word):
    h = H()
    out = []
    for c, d, g in word:
        dv = mp.mpf(0) if d == "0" else -h
        out.append((mp.mpf(c), dv, g))
    return out


# ── kernel characters ──────────────────────────────────────────────────────

def chi_kernel(lam, word):
    h = H()
    with mp.workdps(DPS + 10):
        chain = [(c, "0" if d == "0" else mp.nstr(-h, DPS + 8, strip_zeros=False), g) for c, d, g in word]
    (t, l), = phn.lp_accumulator_step_traces_mpfr(list(lam), [chain], QS, DPS)[-1:]
    return mp.mpf(t) * mp.exp(mp.mpf(l))


# ── mpmath Young seminormal representation (two-row) ──────────────────────

_SYT = {}


def syt_rows(lam):
    """SYT of a two-row shape as tuples rows[e] (0/1) for e = 0..n−1."""
    lam = tuple(lam)
    if lam not in _SYT:
        n = sum(lam)
        top = lam[0]
        bot = lam[1] if len(lam) > 1 else 0
        out = []

        def rec(pre, a, b):
            if a + b == n:
                out.append(tuple(pre))
                return
            if a < top:
                rec(pre + [0], a + 1, b)
            if b < bot and b < a:
                rec(pre + [1], a, b + 1)
        rec([], 0, 0)
        _SYT[lam] = out
    return _SYT[lam]


def contents(rows):
    cnt = [0, 0]
    c = []
    for r in rows:
        c.append(cnt[r] - r)
        cnt[r] += 1
    return c


_GEN = {}


def gen_data(lam, g):
    """(diag vector d, partner index perm, off-diagonal b) for σ_g in the seminormal basis:
    σ v_T = d_T v_T + b_T v_{T'}; (M σ)[:, T] = d_T M[:, T] + b_T M[:, T']."""
    key = (tuple(lam), g, QS)
    if key not in _GEN:
        tabs = syt_rows(lam)
        index = {t: i for i, t in enumerate(tabs)}
        dim = len(tabs)
        d = np.empty(dim, dtype=object)
        b = np.empty(dim, dtype=object)
        perm = np.arange(dim)
        for i, t in enumerate(tabs):
            c = contents(t)
            r = c[g + 1] - c[g]
            d[i] = Q ** r / qint(r)
            if t[g] == t[g + 1]:
                b[i] = mp.mpf(0)
            else:
                s = list(t)
                s[g], s[g + 1] = s[g + 1], s[g]
                s = tuple(s)
                if s in index:
                    perm[i] = index[s]
                    b[i] = mp.mpf(1) if r > 0 else 1 - 1 / qint(r) ** 2
                else:
                    b[i] = mp.mpf(0)
        _GEN[key] = (d, perm, b)
    return _GEN[key]


def apply_word(M, lam, word):
    for c, dv, g in realise(word):
        d, perm, b = gen_data(lam, g)
        M = (M * (c * d + dv)) + (M[:, perm] * (c * b))
    return M


def identity(dim):
    M = np.empty((dim, dim), dtype=object)
    for i in range(dim):
        for j in range(dim):
            M[i, j] = mp.mpf(1) if i == j else mp.mpf(0)
    return M


def level_chars(diag, n):
    """{(m, μ): χ_μ(E_{n→m} W)} for two-row μ ⊢ m, m = 1..n, from the diagonals of W."""
    out = {}
    for m in range(1, n + 1):
        for mu in two_row(m):
            acc = mp.mpf(0)
            for lam, dg in diag.items():
                rows = syt_rows(lam)
                s = mp.fsum(v for v, r in zip(dg, rows) if (m - sum(r[:m]), sum(r[:m])) == tuple(mu) + (0,) * (2 - len(mu)))
                acc += y2(lam) / y2(mu) * s
            out[(m, mu)] = acc
    return out


# ── one row ────────────────────────────────────────────────────────────────

_PREFIX = {}


def nucleon_prefix(A, m, lam):
    key = (A, m, tuple(lam), QS)
    if key not in _PREFIX:
        w = []
        for j in range(A):
            w += nucleon(j, m)
        _PREFIX[key] = apply_word(identity(len(syt_rows(lam))), lam, w)
    return _PREFIX[key]


def evaluate_row(spec):
    A, m, k, offs, order = spec
    n = 3 * A
    word = word_assembled(A, m, k, offs, order)
    bonds = word[A * 2 * m:]
    diag, chi_py, chi_k = {}, {}, {}
    for lam in two_row(n):
        M = apply_word(nucleon_prefix(A, m, lam), lam, bonds)
        diag[lam] = [M[i, i] for i in range(M.shape[0])]
        chi_py[lam] = mp.fsum(diag[lam])
        chi_k[lam] = chi_kernel(lam, word)
    lc = level_chars(diag, n)
    return spec, word, chi_py, chi_k, lc


def fmt(x, d=30):
    return mp.nstr(x, d)


def row_specs(A):
    specs = []
    for m in (3, 6):
        specs.append((A, m, 0, (), "asc"))
        for k in (1, 2, 3):
            for offs in itertools.product((1, 2), repeat=A - 1):
                for order in ("asc", "desc"):
                    specs.append((A, m, k, offs, order))
    return specs


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name}: {src}")

    log(f"q0 (proton pin) = {mp.nstr(Q, 25)}, m_e = {M_E_MEV_STR} MeV, dps = {DPS}")
    h = H()
    zD = Q ** 3 / (Q ** 2 + 1)

    # C5: y_λ from y_lambda_su_n vs two-row formula; three-row y exactly 0
    worst5, three_zero = mp.mpf(0), True
    ysn = {}
    for n in (2, 3, 6, 9, 12):
        ys = y_lambda_su_n(n, Q, 2)
        ysn[n] = ys
        for lam, v in ys.items():
            if len(lam) >= 3:
                three_zero &= (v == 0)
            else:
                worst5 = max(worst5, abs(v - y2(lam)) / abs(v))
        norm = mp.fsum(v * flam(l) for l, v in ys.items())
        worst5 = max(worst5, abs(norm - 1))
    check("C5_y_two_row_formula_and_three_row_zero", worst5 < mp.mpf("1e-60") and three_zero,
          f"max rel diff {mp.nstr(worst5, 5)}; three-row y exactly 0: {three_zero}")

    # C3: tr_M(σ_0) = z_D at n = 2, 3, 6
    worst3 = mp.mpf(0)
    for n in (2, 3, 6):
        tr = mp.fsum(y2(l) * chi_kernel(l, [("1", "0", 0)]) for l in two_row(n))
        worst3 = max(worst3, abs(tr - zD))
    check("C3_markov_sigma0_equals_zD", worst3 < mp.mpf("1e-60"), f"max |tr(σ0) − z_D| {mp.nstr(worst3, 5)}")

    # C2: χ_(2,1)(V³) closed form
    cf = -(Q ** 4 - Q ** 2 + 1) * (Q ** 8 - 2 * Q ** 6 - 2 * Q ** 2 + 1) / Q ** 6
    c2k = chi_kernel((2, 1), V(0) * 3)
    c2p = mp.fsum(np.diag(apply_word(identity(2), (2, 1), V(0) * 3)))
    check("C2_chi21_V3_closed_form", abs(c2k - cf) < mp.mpf("1e-60") and abs(c2p - cf) < mp.mpf("1e-60"),
          f"kernel {mp.nstr(c2k, 25)}, mpmath {mp.nstr(c2p, 25)}, closed form {mp.nstr(cf, 25)}")

    # C0: braid + Hecke relations in the mpmath seminormal rep at n = 6
    worst0 = mp.mpf(0)
    for lam in two_row(6):
        dim = len(syt_rows(lam))
        I = identity(dim)
        for g in range(4):
            L = apply_word(I, lam, [("1", "0", g), ("1", "0", g + 1), ("1", "0", g)])
            R = apply_word(I, lam, [("1", "0", g + 1), ("1", "0", g), ("1", "0", g + 1)])
            worst0 = max(worst0, max(abs(x) for x in (L - R).ravel()))
        for g in range(5):
            S2 = apply_word(I, lam, [("1", "0", g), ("1", "0", g)])
            S1 = apply_word(I, lam, [("1", "0", g)])
            worst0 = max(worst0, max(abs(x) for x in (S2 - h * S1 - I).ravel()))
    check("C0_seminormal_braid_and_hecke_relations", worst0 < mp.mpf("1e-60"), f"max entry error {mp.nstr(worst0, 5)}")

    # C4: Markov property of the level-(n−1) restriction at n = 6
    xw = V(0) * 2 + [("1", "0", 3), ("1", "-h", 1), ("1", "0", 2)]
    diag_x, diag_xs = {}, {}
    for lam in two_row(6):
        Mx = apply_word(identity(len(syt_rows(lam))), lam, xw)
        Mxs = apply_word(Mx, lam, [("1", "0", 4)])
        diag_x[lam] = [Mx[i, i] for i in range(Mx.shape[0])]
        diag_xs[lam] = [Mxs[i, i] for i in range(Mxs.shape[0])]
    lx, lxs = level_chars(diag_x, 6), level_chars(diag_xs, 6)
    worst4 = max(abs(lxs[(5, mu)] - zD * lx[(5, mu)]) for mu in two_row(5))
    check("C4_markov_property_restriction", worst4 < mp.mpf("1e-60"), f"max |χ_μ(E(xσ4)) − z_D χ_μ(E x)| {mp.nstr(worst4, 5)}")

    # ── nucleon alone (A = 1) ──
    results = {"nucleon": {}}
    for m in (3, 6):
        w = nucleon(0, m)
        diag = {}
        blocks = {}
        for lam in partitions(3):
            ck = chi_kernel(lam, w)
            y = ysn[3][lam]
            blocks[str(lam)] = {"y": fmt(y), "chi": fmt(ck), "Delta": str(int(delta(lam))),
                                "term_MeV": fmt(ME * y * ck * delta(lam))}
            if len(lam) <= 2:
                M = apply_word(identity(len(syt_rows(lam))), lam, w)
                diag[lam] = [M[i, i] for i in range(M.shape[0])]
        lc = level_chars(diag, 3)
        fails = sorted({mm for (mm, mu), v in lc.items() if v < -TOL})
        binding = ME * mp.fsum(ysn[3][l] * chi_kernel(l, w) * delta(l) for l in two_row(3))
        results["nucleon"][f"V^{m}"] = {"Binding_MeV": fmt(binding), "reading3_every_level": not fails,
                                        "failing_levels": fails, "blocks": blocks}
        log(f"nucleon V^{m}: Binding = {mp.nstr(binding, 15)} MeV, reading3 pass={not fails}")

    # ── nuclei ──
    route_ok = True
    nf_ok = True
    nf_cover_ok = True       # every route equals the ascending OR the descending word
    route_mismatch = []      # routes whose normal form differs from the ascending word
    route_mismatch_numeric = {}
    py_vs_kernel = mp.mpf(0)
    nuclei = {2: [("2H", 1, 1)], 3: [("3H", 1, 2), ("3He", 2, 1)], 4: [("4He", 2, 2)]}
    for A in (2, 3, 4):
        specs = row_specs(A)
        log(f"A = {A}: {len(specs)} rows (n = {3 * A})")
        # dedup by commutation normal form
        nf_groups = {}
        for s in specs:
            nf_groups.setdefault(normal_form(word_assembled(*s)), []).append(s)
        unique = [g[0] for g in nf_groups.values()]
        log(f"  {len(unique)} distinct Hecke elements by commutation normal form")
        with mpc.Pool(4) as pool:
            out = []
            for i, r in enumerate(pool.imap(evaluate_row, unique)):
                out.append(r)
                log(f"  row {i + 1}/{len(unique)} {r[0]} done")
        byspec = {r[0]: r for r in out}
        free_binding = {}
        rows = []
        n = 3 * A
        for nf, group in nf_groups.items():
            spec, word, chi_py, chi_k, lc = byspec[group[0]]
            A_, m, k, offs, order = spec
            for lam in chi_py:
                py_vs_kernel = max(py_vs_kernel, abs(chi_py[lam] - chi_k[lam]) / max(1, abs(chi_k[lam])))
            terms = {lam: ME * ysn[n][lam] * chi_k[lam] * delta(lam) for lam in chi_k}
            binding = mp.fsum(terms.values())
            tr = mp.fsum(ysn[n][lam] * chi_k[lam] for lam in chi_k)
            fails = sorted({mm for (mm, mu), v in lc.items() if v < -TOL})
            neg = [f"{mm}:{mu}={mp.nstr(v, 8)}" for (mm, mu), v in sorted(lc.items()) if v < -TOL]
            if k == 0:
                free_binding[m] = (binding, tr)
            rows.append({"m": m, "k": k, "offsets": list(offs), "orders_in_class": [g[4] for g in group if g[1:4] == spec[1:4]],
                         "same_element_as": [f"m={g[1]},k={g[2]},offs={list(g[3])},{g[4]}" for g in group],
                         "Binding_MeV": binding, "trace": tr, "reading3_every_level": not fails,
                         "failing_levels": fails, "negative": neg[:12],
                         "blocks": {str(l): {"y": fmt(ysn[n][l]), "chi": fmt(chi_k[l]), "Delta": str(int(delta(l))),
                                             "term_MeV": fmt(terms[l])} for l in chi_k}})
        for r in rows:
            fb, ftr = free_binding[r["m"]]
            r["B_pred_MeV"] = fmt(-r["Binding_MeV"])
            r["B_bond_MeV"] = fmt(-(r["Binding_MeV"] - fb))
            r["trace_ratio_vs_free"] = fmt(r["trace"] / ftr)
            r["Binding_MeV"] = fmt(r["Binding_MeV"])
            r["trace"] = fmt(r["trace"])
        # formation routes: normal form + numeric match on every route row
        if A >= 3:
            routes = ["sequential"] + (["DD"] if A == 4 else [])
            for m in (3, 6):
                for k in (1, 2, 3):
                    for offs in itertools.product((1, 2), repeat=A - 1):
                        wa = word_assembled(A, m, k, offs, "asc")
                        for rt in routes:
                            wr = word_route(A, m, k, offs, rt)
                            nfr, nfa = normal_form(wr), normal_form(wa)
                            nfd = normal_form(word_assembled(A, m, k, offs, "desc"))
                            nf_ok &= nfr == nfa
                            nf_cover_ok &= nfr in (nfa, nfd)
                            if nfr != nfa:
                                route_mismatch.append({"A": A, "m": m, "k": k, "offsets": list(offs),
                                                       "route": rt, "equals_descending": nfr == nfd})
            if A == 4:   # numeric: is a mismatching route a genuinely different element?
                offs = (1, 2, 1)
                wa, wd, wr = (word_assembled(4, 3, 3, offs, "asc"), word_assembled(4, 3, 3, offs, "desc"),
                              word_route(4, 3, 3, offs, "DD"))
                for lam in two_row(n):
                    ca, cd, cr = chi_kernel(lam, wa), chi_kernel(lam, wd), chi_kernel(lam, wr)
                    route_mismatch_numeric[str(lam)] = {"asc": fmt(ca, 25), "desc": fmt(cd, 25), "DD": fmt(cr, 25),
                                                        "DD_minus_asc": fmt(cr - ca, 10), "DD_minus_desc": fmt(cr - cd, 10)}
            for rt in routes:   # numeric on one row per route
                offs = (2, 1) + ((2,) if A == 4 else ())
                wa, wr = word_assembled(A, 3, 3, offs, "asc"), word_route(A, 3, 3, offs, rt)
                for lam in two_row(n):
                    route_ok &= abs(chi_kernel(lam, wa) - chi_kernel(lam, wr)) < mp.mpf("1e-55") * max(1, abs(chi_kernel(lam, wa)))
        # three-row blocks (y = 0)
        three = {}
        sel = specs if A <= 3 else [(4, 3, 0, (), "asc"), (4, 3, 3, (1, 1, 1), "asc"), (4, 3, 3, (2, 2, 2), "asc")]
        for s in sel:
            w = word_assembled(*s)
            entry = {}
            for lam in partitions(n):
                if len(lam) >= 3:
                    ck = chi_kernel(lam, w)
                    entry[str(lam)] = {"chi": fmt(ck, 20), "y": str(ysn[n][lam]), "term_MeV": str(ME * ysn[n][lam] * ck * delta(lam))}
            three[f"m={s[1]},k={s[2]},offs={list(s[3])},{s[4]}"] = entry
            log(f"  three-row characters for {s} done")
        for label, Z, N in nuclei[A]:
            results[label] = {"Z": Z, "N": N, "n": n, "rows": rows, "three_row_blocks": three,
                              "AME2020_B_MeV": fmt(ame_binding_mev(Z, A))}
    check("C1_kernel_vs_mpmath_seminormal_two_row", py_vs_kernel < mp.mpf("1e-50"), f"max rel diff {mp.nstr(py_vs_kernel, 5)}")
    # C6 is the preregistered prediction, kept as written; it is FALSE (see route_mismatch).
    check("C6_formation_routes_equal_assembled", nf_ok and route_ok,
          f"normal forms equal to ascending: {nf_ok}; numeric (offs (2,1[,2])): {route_ok}; "
          f"{len(route_mismatch)} route rows differ from ascending")
    # Added after the preregistration, reported separately: every route lies in the enumeration.
    check("C6b_every_route_equals_an_enumerated_bond_order", nf_cover_ok,
          "each formation route has the normal form of the ascending or the descending word")

    # p–n at q = 1 and q0. In this family the proton and neutron are the SAME word V^m, so the
    # ³H and ³He words are built separately from p/n labels and compared as letter strings,
    # then as characters. The Rust kernel returns nan at q = 1 (h = 0), so q = 1 uses the
    # mpmath seminormal representation on the two-row blocks (the only blocks with y ≠ 0).
    def nucleus_word(labels, m=3, k=3, offs=(2, 1)):
        word_of = {"p": lambda j: nucleon(j, m), "n": lambda j: nucleon(j, m)}
        w = []
        for j, lab in enumerate(labels):
            w += word_of[lab](j)
        for j, o in enumerate(offs):
            w += bond(j, o, k)
        return w
    w3H, w3He = nucleus_word("pnn"), nucleus_word("ppn")
    pn_word_equal = (w3H == w3He)
    pn = {}
    q0 = Q
    for qv in (mp.mpf(1), q0):
        setq(qv)
        diffs = []
        for lam in two_row(9):
            dim = len(syt_rows(lam))
            a = apply_word(identity(dim), lam, w3H)
            b = apply_word(identity(dim), lam, w3He)
            diffs.append(abs(sum(a[i, i] for i in range(dim)) - sum(b[i, i] for i in range(dim))))
        pn[mp.nstr(qv, 12)] = max(diffs)
    kernel_q1 = None
    setq(mp.mpf(1))
    try:
        kernel_q1 = mp.nstr(chi_kernel((5, 4), w3H), 10)
    except Exception as e:  # recorded, not used
        kernel_q1 = f"raised {type(e).__name__}"
    setq(q0)
    check("C7_pn_difference_zero_at_q1_and_q0", pn_word_equal and all(v == 0 for v in pn.values()),
          f"words equal: {pn_word_equal}; max |χ(³H) − χ(³He)| over two-row λ ⊢ 9 (mpmath seminormal) {pn}; "
          f"kernel at q=1 gives {kernel_q1} (not used)")
    # Diagnostic (added after preregistration, reported, not used to choose anything):
    # the same sum on the IDENTITY element, χ^λ(1) = f^λ, i.e. the word-independent baseline
    # m_e Σ_{two-row λ ⊢ n} y_λ f^λ Δ_λ.
    identity_baseline = {}
    for nn in (3, 6, 9, 12):
        yy = y_lambda_su_n(nn, Q, 2)
        val = ME * sum(yy[l] * flam(l) * delta(l) for l in two_row(nn))
        identity_baseline[str(nn)] = {"Binding_MeV": fmt(val), "B_pred_MeV": fmt(-val)}
    log(f"identity-element baseline B_pred: { {k: mp.nstr(mp.mpf(v['B_pred_MeV']), 10) for k, v in identity_baseline.items()} }")

    ok_all = all(ok for _, ok, _ in checks)
    wb = WitnessBuilder("single-level-binding-gg", engine="mpmath", output_dir=HERE)
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 = qou_substrate.constants.q_at(80) (proton pin), passed to the kernel as a decimal string",
        "q0Value": mp.nstr(Q, 50),
        "description": "PROBE (issue #8983): corpus single-level binding Binding = m_e Σ_{λ⊢3A} y_λ χ^λ Δ_λ, "
                       "convention D, proton pin, on the PR #7741 γγ candidate words (nucleon V^m, m in {3,6}; "
                       "bond V^k, k in {1,2,3}, at straddling vertices; chain; both bond orders). Candidate words, "
                       "not ruled words; AME only as a comparison column; does not decide owner decision qou-8274.",
        "preregistration": "computations/probes/single_level_binding_gg/PREREGISTRATION.md",
        "results": results,
        "identity_element_baseline": identity_baseline,
        "formation_routes": {
            "preregistered_prediction": "every formation route equals the assembled ascending word (PREREGISTRATION §1)",
            "prediction_holds": nf_ok,
            "rows_differing_from_ascending": route_mismatch,
            "every_route_equals_ascending_or_descending": nf_cover_ok,
            "numeric_A4_m3_k3_offs_1_2_1": route_mismatch_numeric,
        },
    })
    log(f"witness {out}; checks {sum(ok for _, ok, _ in checks)}/{len(checks)}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
