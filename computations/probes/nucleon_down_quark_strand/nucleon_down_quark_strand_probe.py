#!/usr/bin/env python3
"""What γγ production says about the up and down strands, full tower; down-strand candidates.

Pre-registration: PREREGISTRATION.md (committed before this ran). Beans qou-myts, qou-99qc.
Lean: QOU.Nuclear.NucleonDownQuarkStrand.

Part A (exact): one-dimensional characters of H_n on every γγ word; for n = 3..6, every γγ word
of up to K vertices, whether it is a pure braid and the signed crossing count of each strand.
Part B (exact, symbolic q): z̄_D = z_D − (q − q⁻¹), the ratio and bar swap; the K-weighted partial
trace of Ř and Ř⁻¹ (the corpus braiding of NucleonSplitFullTower).
Part C (mpmath, proton q0): Δm = E·log(f_u/f_d) for the enumerated candidates, both E₀.
No candidate is selected by CODATA; CODATA appears only as a comparison column.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)

import itertools  # noqa: E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from mpmath import mpf  # noqa: E402

mp.mp.dps = max(mp.mp.dps, 80)

from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta import qbeta_e0  # noqa: E402

DPS = 80
M_E = mpf(_codata.codata("electron mass energy equivalent in MeV").value_str)
DM_NP_EXP = (mpf(_codata.codata("neutron mass energy equivalent in MeV").value_str)
             - mpf(_codata.codata("proton mass energy equivalent in MeV").value_str))

q = sp.symbols("q", positive=True)


# ---------------------------------------------------------------- Part A
def vertex(i):
    return [(i, True), (i + 1, False)]


def gg_words(n, kmax):
    idx = range(n - 2)  # vertex i uses generators i, i+1 <= n-2
    for k in range(1, kmax + 1):
        for seq in itertools.product(idx, repeat=k):
            w = []
            for i in seq:
                w += vertex(i)
            yield seq, w


def strand_data(n, w):
    st = list(range(n))
    inv = [0] * n
    link = {}
    for g, pos in w:
        a, b = st[g], st[g + 1]
        s = 1 if pos else -1
        inv[a] += s
        inv[b] += s
        key = (min(a, b), max(a, b))
        link[key] = link.get(key, 0) + s
        st[g], st[g + 1] = b, a
    return st == list(range(n)), inv, link


def one_dim_chars(w):
    triv = sp.Integer(1)
    sgn = sp.Integer(1)
    for _, pos in w:
        triv *= q if pos else 1 / q
        sgn *= (-1 / q) if pos else (-q)
    return sp.simplify(triv), sp.simplify(sgn)


def part_a():
    out = {}
    chars_ok = True
    for n, kmax in ((3, 6), (4, 4), (5, 4), (6, 3)):
        n_words = n_pure = 0
        pure_inv_patterns = set()
        split_examples = []
        for seq, w in gg_words(n, kmax):
            n_words += 1
            t, s = one_dim_chars(w)
            chars_ok &= (t == 1 and s == 1)
            pure, inv, link = strand_data(n, w)
            if pure:
                n_pure += 1
                pat = tuple(sorted(inv))
                pure_inv_patterns.add(pat)
                if any(x > 0 for x in inv) and any(x < 0 for x in inv) and len(split_examples) < 3:
                    split_examples.append({"vertices": list(seq), "strand_signed_count": inv,
                                           "linking": {f"{a}{b}": v // 2 for (a, b), v in link.items()}})
        out[f"n{n}"] = {"max_vertices": kmax, "gg_words": n_words, "pure": n_pure,
                        "pure_strand_count_patterns": sorted(list(p) for p in pure_inv_patterns),
                        "pure_with_opposite_orientation_strands": split_examples}
        print(f"  [A] n={n} k<= {kmax}: {n_words} words, {n_pure} pure, patterns "
              f"{sorted(pure_inv_patterns)}")
    return out, chars_ok


# ---------------------------------------------------------------- Part B
def part_b():
    h = q - 1 / q
    zD = q**3 / (q**2 + 1)
    zbar = zD - h
    checks = {
        "zbarD_eq_1_over_q_q2p1": sp.simplify(zbar - 1 / (q * (q**2 + 1))) == 0,
        "zD_eq_q4_zbarD": sp.simplify(zD - q**4 * zbar) == 0,
        "bar_swaps_zD_zbarD": sp.simplify(zD.subs(q, 1 / q) - zbar) == 0,
        "vertex_curls_bar_even": sp.simplify((zD * zbar).subs(q, 1 / q) - zD * zbar) == 0,
    }
    # corpus braiding (NucleonSplitFullTower): basis index 2*i + k, u = 0, d = 1
    R = sp.zeros(4, 4)
    R[0, 0] = q              # u⊗u -> q u⊗u
    R[2, 1] = 1              # u⊗d -> d⊗u
    R[1, 2] = 1              # d⊗u -> u⊗d + h d⊗u
    R[2, 2] = h
    R[3, 3] = q              # d⊗d -> q d⊗d
    K = sp.diag(q**2, 1) / (q**2 + 1)   # Markov-forced weight, normalised ptr(1) = 1

    def ptr(X):
        M = sp.zeros(2, 2)
        for i in range(2):
            for j in range(2):
                M[i, j] = sum(K[k, k] * X[2 * i + k, 2 * j + k] for k in range(2))
        return M.applyfunc(sp.simplify)

    checks["ptrK_R_eq_zD"] = (ptr(R) - zD * sp.eye(2)).applyfunc(sp.simplify) == sp.zeros(2, 2)
    checks["ptrK_Rinv_eq_zbarD"] = (ptr(R.inv()) - zbar * sp.eye(2)).applyfunc(sp.simplify) == sp.zeros(2, 2)
    for k, v in checks.items():
        print(f"  [B] {k}: {'PASS' if v else 'FAIL'}")
    return checks


# ---------------------------------------------------------------- Part C
def part_c(q0):
    E0 = qbeta_e0.order_zero(q=q0, m_e=M_E)
    E0t = qbeta_e0.canonical(q=q0, m_e=M_E)
    zD = q0**3 / (q0**2 + 1)
    zbar = zD - (q0 - 1 / q0)
    cands = {
        "C0_same_object": mpf(1),
        "CT_through_parity_q_over_qinv": q0 / (1 / q0),
        "CM_markov_curl_zD_over_zbarD": zD / zbar,
    }
    rows = {}
    for name, ratio in cands.items():
        for tag, E in (("E0_order_zero", E0), ("E0_tower", E0t)):
            v = E * mp.log(ratio)
            rows[f"{name}|{tag}"] = {"MeV": fmt(v), "ratio_to_codata_comparison_only": fmt(v / DM_NP_EXP)}
            print(f"  [C] {name:34s} {tag:14s} {mp.nstr(v, 12):>16s} MeV  (/CODATA {mp.nstr(v / DM_NP_EXP, 6)})")
    meta = {"q0": fmt(q0), "E0_order_zero": fmt(E0), "E0_tower": fmt(E0t),
            "zD": fmt(zD), "zbarD": fmt(zbar)}
    curl_ok = mp.almosteq(zD / zbar, q0**4, mpf(10) ** (-70))
    return meta, rows, curl_ok


def main():
    wb = WitnessBuilder("nucleon-down-quark-strand", engine="sympy+mpmath")
    wb.set_description(
        "What γγ production says about the up and down strands, full tower (n = 3..6), and the "
        "enumerated down-strand candidates (same object / through-parity / Markov curl) with the "
        "Gibbs split at the proton q0 for both E0. No candidate selected by CODATA "
        "(QOU.Nuclear.NucleonDownQuarkStrand)."
    )
    a, chars_ok = part_a()
    print(f"  [A] one-dim characters of H_n equal 1 on every gg word: {'PASS' if chars_ok else 'FAIL'}")
    b = part_b()
    q0 = mpf(q_at(DPS))
    print(f"\n[C] proton q0 = {mp.nstr(q0, 20)}")
    meta, rows, curl_ok = part_c(q0)
    ok = chars_ok and all(b.values()) and curl_ok
    wb.add_data("lean_module", "QOU.Nuclear.NucleonDownQuarkStrand")
    wb.add_data("beans_referenced", ["qou-myts", "qou-99qc", "qou-ales"])
    wb.add_data("gg_full_tower", a)
    wb.add_data("one_dim_chars_trivial_on_gg", bool(chars_ok))
    wb.add_data("exact_checks", {k: bool(v) for k, v in b.items()})
    wb.add_data("anchor", meta)
    wb.add_data("candidates", rows)
    wb.add_data("codata_comparison_only", {"dm_np_MeV": fmt(DM_NP_EXP)})
    path = wb.save({"q0Anchor": "proton"})
    print(f"\nwitness: {path}\nALL CHECKS {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
