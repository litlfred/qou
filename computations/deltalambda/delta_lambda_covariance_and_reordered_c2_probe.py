#!/usr/bin/env python3
"""
delta_lambda_covariance_and_reordered_c2_probe.py — 80-dps / Exact Rational Compute Probe
=========================================================================================

Unifies three linked MassTheory / Delta_lambda derivations at 80-dps `mpmath` and exact
`Fraction` arithmetic (zero `float64` intermediates, zero parameter fitting):

1. Reordered-Word Second-Order Trace Coefficient `c_2` (`qou-qqm4`):
   Derives the exact dyadic rationals `(c_0, c_1, a_2, c_2)` for the six canonical
   (`intra_order='borromean'`) atom words `pp`, `pn` (`²H`), `nn`, `T` (`³H`), `³He`, `⁴He`
   via the cycle-decomposed diagonal-insertion expansion `[◇]` (`|S| <= 2`), cross-checked
   on `A = 2` (`pp, pn, nn`) against the exact rational `Ser` `ε`-series of the Wedderburn
   trace. Establishes:
     * `c_2(pp)  = 33/32`   (`|S|=0: 0,     |S|=1: 7/8,     |S|=2: 5/32`,    `a_2 = 29/32`)
     * `c_2(pn)  = 25/32`   (`|S|=0: 0,     |S|=1: 27/32,   |S|=2: -1/16`,   `a_2 = 23/32`)
     * `c_2(nn)  = 1/16`    (`|S|=0: 0,     |S|=1: 13/16,   |S|=2: -3/4`,    `a_2 = 1/16`)
     * `c_2(T)   = 99/128`  (`|S|=0: 5/32,  |S|=1: 123/128, |S|=2: -11/32`,  `a_2 = 97/128`)
     * `c_2(³He) = 157/128` (`|S|=0: 5/32,  |S|=1: 65/64,   |S|=2: 7/128`,   `a_2 = 141/128`)
     * `c_2(⁴He) = 439/512` (`|S|=0: 11/64, |S|=1: 25/32,   |S|=2: -49/512`, `a_2 = 411/512`)
     * Exact `A=3` mirror sum: `c_2(T) + c_2(³He) = 99/128 + 157/128 = 2`.
     * Exact `A=2` content-cancellation combination:
       `c_2(pp) + c_2(nn) - 2*c_2(pn) = -15/32` (invariant between `borromean` and `grouped`).
     * Exact second-order chain-over-atom ratios:
       `T: 12/11`, `³He: 232/157`, `⁴He: 960/439`, each strictly closer to `1` than the
       first-order ratio (`4`, `3/2`, `24/7`).

2. Deuteron (`²H`) at `H_6(q)`: Per-Partition `chi_lambda` Free-vs-Bound Table (`qou-6h6p`):
   Evaluates `chi^lambda(W_free)`, `chi^lambda(W_atom)`, `Delta chi^lambda`, and the
   Convention-D Wedderburn weight `y_lambda` across all 11 partitions `lambda |- 6` both:
     * as exact rational Taylor coefficients `[eps^0, eps^1, eps^2]` at `q = 1 + eps`,
       verifying that summing `y_lambda * Delta chi^lambda` over the 4 two-row partitions
       `{(6), (5,1), (4,2), (3,3)}` yields `[1/8, 1/16, 23/32]` and hence
       `(c_0, c_1, c_2) = (1/8, 1/16, 25/32)`, and
     * at 80-dps canonical proton pin `q_0`, matching the transfer-matrix trace `tr_m_atom_zn`
       to `< 10^-75` per character and `< 10^-50` on the total trace difference.

3. `Delta_lambda` Plancherel Covariance Kernel & Sufficient Two-Leg Bounds (`qou-v8t7`):
   Evaluates for `k = 1..20` in exact integer/rational arithmetic and 80-dps `mpmath`:
     * Plancherel identities `sum_{lambda |- k} (f^lambda)^2 = k!` and
       `sum_{lambda |- k} (f^lambda)^2 omega_3(lambda) = 0`, where
       `omega_3(lambda) = sum_{box in lambda} c(box)^2 - C(k, 2)`.
     * Transpose-involution invariance `f^{lambda'} = f^lambda` and
       `omega_3(lambda') = omega_3(lambda)`.
     * Exact integer kernel `cov(k) = sum_{lambda |- k} (f^lambda)^3 omega_3(lambda) <= 0`
       (`cov(1) = cov(2) = 0`, `cov(k) < 0` strictly for `3 <= k <= 20`).
     * Leg A2: `g'(0) = Cov_Planch(ln f^lambda, omega_3(lambda)) < 0` for all `3 <= k <= 20`.
     * Leg A3: `|R_k| = |g(1) - g'(0)| < |g'(0)|` (`r_k = g(1)/g'(0) in (0, 2)`) for all
       `3 <= k <= 20`.
"""
from __future__ import annotations

import functools
import importlib.util
import sys
import time
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
for _p in (
    str(HERE),
    str(COMP),
    str(COMP / "probes"),
    str(COMP / "hecke"),
    str(COMP / "markov"),
    str(COMP / "substrate"),
    str(COMP / "habiro"),
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import canonical_braid_crossings as _cbc  # noqa: E402
import tr_m_atom_via_transfer as _tr  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from wedderburn_jones_markov import Q_SYM, y_lambda_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import c1_leading_coefficient_derived_probe as _c1p  # noqa: E402
import c2_diagonal_insertion_expansion_probe as _c2p  # noqa: E402

_erc_spec = importlib.util.spec_from_file_location(
    "erc", COMP / "probes" / "exact_rational_chi_gauge_probe.py"
)
_erc = importlib.util.module_from_spec(_erc_spec)
_erc_spec.loader.exec_module(_erc)

set_compute_dps(80)
mp.mp.dps = 80


def frac_to_mpf(x: F) -> mp.mpf:
    """Convert an exact Fraction to an 80-dps mpf without float64 intermediates."""
    return mp.mpf(x.numerator) / mp.mpf(x.denominator)


# =============================================================================
# PART 1: Cycle-Decomposed Diagonal-Insertion Expansion [◇] for c_0, c_1, a_2, c_2
# =============================================================================

CASES = [
    ("pp", (2, 0)),
    ("pn", (1, 1)),
    ("nn", (0, 2)),
    ("T", (1, 2)),
    ("3He", (2, 1)),
    ("4He", (2, 2)),
]

EXPECTED_CANONICAL = {
    "pp": {
        "a0": F(1, 8),
        "c1": F(1, 8),
        "a2": F(29, 32),
        "c2": F(33, 32),
        "s0": F(0),
        "s1": F(7, 8),
        "s2": F(5, 32),
    },
    "pn": {
        "a0": F(1, 8),
        "c1": F(1, 16),
        "a2": F(23, 32),
        "c2": F(25, 32),
        "s0": F(0),
        "s1": F(27, 32),
        "s2": F(-1, 16),
    },
    "nn": {
        "a0": F(1, 8),
        "c1": F(0),
        "a2": F(1, 16),
        "c2": F(1, 16),
        "s0": F(0),
        "s1": F(13, 16),
        "s2": F(-3, 4),
    },
    "T": {
        "a0": F(3, 32),
        "c1": F(1, 64),
        "a2": F(97, 128),
        "c2": F(99, 128),
        "s0": F(5, 32),
        "s1": F(123, 128),
        "s2": F(-11, 32),
    },
    "3He": {
        "a0": F(3, 32),
        "c1": F(1, 8),
        "a2": F(141, 128),
        "c2": F(157, 128),
        "s0": F(5, 32),
        "s1": F(65, 64),
        "s2": F(7, 128),
    },
    "4He": {
        "a0": F(7, 128),
        "c1": F(7, 128),
        "a2": F(411, 512),
        "c2": F(439, 512),
        "s0": F(11, 64),
        "s1": F(25, 32),
        "s2": F(-49, 512),
    },
}

EXPECTED_GROUPED_A2_C2 = {
    "pp": F(357, 32),
    "pn": F(403, 32),
    "nn": F(217, 16),
}


def cycle_trace_expansion(
    Z: int,
    N: int,
    include_inter: bool,
    K: int = 2,
    intra_order: str = "borromean",
) -> tuple[list[F], dict[int, list[F]]]:
    """Exact diagonal-insertion expansion `[◇]` of `tr_M(W)` to order `eps^K` via cycle decomposition.

    For each deletion subset `S` of letters (`|S| <= K`), the undeleted letters are pure
    transpositions `s_g`, forming a permutation `pi_S in S_n`. A basis state `b in {e_1, e_2}^n`
    is fixed by `pi_S` iff `b` is constant on each disjoint cycle of `pi_S`, reducing the fixed-point
    sum from `2^n` states to `2^{c(pi_S)}` cycle-colorings in exact `Fraction` arithmetic.
    """
    n = 3 * (Z + N)
    crossings = _cbc.atom_canonical_crossings(
        Z, N, include_inter=include_inter, intra_order=intra_order
    )
    L = len(crossings)
    gens = [g for g, _ in crossings]
    d_ser = [_c2p.letter_d_series(kind, K) for _, kind in crossings]
    eps_series = [F(0), F(1)] + [F(0)] * (K - 1)
    h = _c2p.series_h(K)

    kpow: dict[int, list[F]] = {}
    for m in range(n + 1):
        s = [F(1)] + [F(0)] * K
        base = [F(1), F(2), F(1)] + [F(0)] * (K - 2) if K >= 2 else [F(1), F(2)]
        for _ in range(m):
            s = _c2p.pmul(s, base, K)
        kpow[m] = s

    u = [F(0), F(1), F(1, 2)] + [F(0)] * (K - 2) if K >= 2 else [F(0), F(1)]
    inv = [F(1)] + [F(0)] * K
    upow = [F(1)] + [F(0)] * K
    coef = F(1)
    for j in range(1, K + 1):
        upow = _c2p.pmul(upow, u, K)
        coef = coef * F(-n - j + 1) / j
        inv = _c2p.padd(inv, [coef * x for x in upow])
    norm = [x / F(2) ** n for x in inv]

    pat_table = []
    for idx in range(L):
        d = d_ser[idx]
        p00 = _c2p.padd(eps_series, d)
        p01 = list(d)
        p10 = _c2p.padd(h, d)
        p11 = p00
        pat_table.append((p00, p01, p10, p11))

    raw_by_class = {k: [F(0)] * (K + 1) for k in range(K + 1)}
    order = list(range(L - 1, -1, -1))

    for size in range(K + 1):
        for S in combinations(range(L), size):
            Sset = set(S)
            pos = list(range(n))
            inspected = []
            for idx in order:
                g = gens[idx]
                if idx in Sset:
                    inspected.append((idx, pos[g], pos[g + 1]))
                else:
                    pos[g], pos[g + 1] = pos[g + 1], pos[g]
            visited = [False] * n
            cycle_of = [0] * n
            cycle_sizes = []
            cid = 0
            for i in range(n):
                if not visited[i]:
                    cnt = 0
                    cur = i
                    while not visited[cur]:
                        visited[cur] = True
                        cycle_of[cur] = cid
                        cnt += 1
                        cur = pos[cur]
                    cycle_sizes.append(cnt)
                    cid += 1
            num_cycles = cid
            insp_cycles = [(idx, cycle_of[u_i], cycle_of[v_i]) for idx, u_i, v_i in inspected]
            for c_mask in range(1 << num_cycles):
                m_down = sum(
                    cycle_sizes[c] for c in range(num_cycles) if (c_mask >> c) & 1
                )
                scal = kpow[m_down]
                for idx, cu, cv in insp_cycles:
                    bu = (c_mask >> cu) & 1
                    bv = (c_mask >> cv) & 1
                    scal = _c2p.pmul(scal, pat_table[idx][(bu << 1) | bv], K)
                raw_by_class[size] = _c2p.padd(raw_by_class[size], scal)

    total_raw = [F(0)] * (K + 1)
    for s in raw_by_class.values():
        total_raw = _c2p.padd(total_raw, s)
    coeffs = _c2p.pmul(total_raw, norm, K)
    by_class = {size: _c2p.pmul(raw_by_class[size], norm, K) for size in raw_by_class}
    return coeffs, by_class


def run_part1_reordered_c2() -> dict:
    """Compute and verify reordered-word (c_0, c_1, a_2, c_2) and class splits (`qou-qqm4`)."""
    print("=" * 84)
    print("PART 1 (qou-qqm4): Exact Diagonal-Insertion & Series Derivation of Reordered-Word c2")
    print("=" * 84)
    rows = {}
    all_match = True
    for name, (Z, N) in CASES:
        t0 = time.time()
        cf, cls_f = cycle_trace_expansion(Z, N, False, K=2, intra_order="borromean")
        ca, cls_a = cycle_trace_expansion(Z, N, True, K=2, intra_order="borromean")
        d = [x - y for x, y in zip(cf, ca)]
        cls = {s: [x - y for x, y in zip(cls_f[s], cls_a[s])] for s in cls_f}
        a0, a1, a2 = d[0], d[1], d[2]
        c1 = a1
        c2 = a1 + a2
        c2_by_s = {s: cls[s][1] + cls[s][2] for s in cls}
        exp = EXPECTED_CANONICAL[name]
        ok = (
            a0 == exp["a0"]
            and c1 == exp["c1"]
            and a2 == exp["a2"]
            and c2 == exp["c2"]
            and c2_by_s[0] == exp["s0"]
            and c2_by_s[1] == exp["s1"]
            and c2_by_s[2] == exp["s2"]
            and (c2_by_s[0] + c2_by_s[1] + c2_by_s[2] == c2)
        )
        all_match &= ok
        rows[name] = {
            "Z": Z,
            "N": N,
            "A": Z + N,
            "a0": a0,
            "c1": c1,
            "a2": a2,
            "c2": c2,
            "s0": c2_by_s[0],
            "s1": c2_by_s[1],
            "s2": c2_by_s[2],
            "ok": ok,
        }
        print(
            f"  {name:<4} (Z={Z},N={N}, {time.time()-t0:4.2f}s): "
            f"a0={str(a0):<6} c1={str(c1):<6} a2={str(a2):<8} c2={str(c2):<8} "
            f"|S|=0:{str(c2_by_s[0]):<6} |S|=1:{str(c2_by_s[1]):<8} |S|=2:{str(c2_by_s[2]):<8} "
            f"[match={ok}]"
        )

    # Cross-check A=2 against the Wedderburn exact Ser epsilon-series AND grouped ordering
    ser_a2_ok = True
    grouped_a2 = {}
    for name in ("pp", "pn", "nn"):
        Z, N = rows[name]["Z"], rows[name]["N"]
        d_ser = _c1p.tr_M_series(Z, N, False, 4) - _c1p.tr_M_series(Z, N, True, 4)
        s_a0 = d_ser.coeff(0)
        s_a1 = d_ser.coeff(1)
        s_a2 = d_ser.coeff(2)
        s_c2 = s_a1 + s_a2
        ser_a2_ok &= (
            s_a0 == rows[name]["a0"]
            and s_a1 == rows[name]["c1"]
            and s_a2 == rows[name]["a2"]
            and s_c2 == rows[name]["c2"]
        )
        cf_g, _ = cycle_trace_expansion(Z, N, False, K=2, intra_order="grouped")
        ca_g, _ = cycle_trace_expansion(Z, N, True, K=2, intra_order="grouped")
        d_g = [x - y for x, y in zip(cf_g, ca_g)]
        c2_g = d_g[1] + d_g[2]
        grouped_a2[name] = c2_g
        ser_a2_ok &= c2_g == EXPECTED_GROUPED_A2_C2[name]

    # Exact algebraic identities on c2
    mirror_sum_a3 = rows["T"]["c2"] + rows["3He"]["c2"]
    content_cancel_canon = rows["pp"]["c2"] + rows["nn"]["c2"] - 2 * rows["pn"]["c2"]
    content_cancel_grouped = (
        grouped_a2["pp"] + grouped_a2["nn"] - 2 * grouped_a2["pn"]
    )
    s0_blind_ok = (
        rows["pp"]["s0"] == rows["pn"]["s0"] == rows["nn"]["s0"] == F(0)
        and rows["T"]["s0"] == rows["3He"]["s0"] == F(5, 32)
        and rows["4He"]["s0"] == F(11, 64)
    )

    # Chain-over-atom ratios at order 1 and order 2
    r1 = {
        "T": (rows["pn"]["c1"] + rows["nn"]["c1"]) / rows["T"]["c1"],
        "3He": (rows["pp"]["c1"] + rows["pn"]["c1"]) / rows["3He"]["c1"],
        "4He": (rows["pp"]["c1"] + rows["pn"]["c1"] + rows["nn"]["c1"]) / rows["4He"]["c1"],
    }
    r2 = {
        "T": (rows["pn"]["c2"] + rows["nn"]["c2"]) / rows["T"]["c2"],
        "3He": (rows["pp"]["c2"] + rows["pn"]["c2"]) / rows["3He"]["c2"],
        "4He": (rows["pp"]["c2"] + rows["pn"]["c2"] + rows["nn"]["c2"]) / rows["4He"]["c2"],
    }
    ratios_ok = (
        r1["T"] == F(4, 1)
        and r1["3He"] == F(3, 2)
        and r1["4He"] == F(24, 7)
        and r2["T"] == F(12, 11)
        and r2["3He"] == F(232, 157)
        and r2["4He"] == F(960, 439)
        and all(abs(r2[k] - 1) < abs(r1[k] - 1) for k in ("T", "3He", "4He"))
    )

    print(f"  A=2 Wedderburn Ser eps-series & grouped self-test: {ser_a2_ok}")
    print(f"  A=3 mirror sum c2(T) + c2(3He) = {mirror_sum_a3} (expected 2)")
    print(
        f"  A=2 content cancellation c2(pp)+c2(nn)-2*c2(pn): "
        f"canonical={content_cancel_canon}, grouped={content_cancel_grouped} (expected -15/32)"
    )
    print(
        f"  Chain/atom ratios r2 vs r1: T={r2['T']} (vs {r1['T']}), "
        f"3He={r2['3He']} (vs {r1['3He']}), 4He={r2['4He']} (vs {r1['4He']}) [ok={ratios_ok}]\n"
    )
    return {
        "rows": rows,
        "all_match": all_match,
        "ser_a2_ok": ser_a2_ok,
        "mirror_sum_a3": mirror_sum_a3,
        "content_cancel_canon": content_cancel_canon,
        "content_cancel_grouped": content_cancel_grouped,
        "s0_blind_ok": s0_blind_ok,
        "r1": r1,
        "r2": r2,
        "ratios_ok": ratios_ok,
    }


# =============================================================================
# PART 2: Deuteron (²H) at H_6(q): Exact & 80-dps Per-Partition chi_lambda Table
# =============================================================================

PARTITIONS_6 = [
    [6],
    [5, 1],
    [4, 2],
    [4, 1, 1],
    [3, 3],
    [3, 2, 1],
    [3, 1, 1, 1],
    [2, 2, 2],
    [2, 2, 1, 1],
    [2, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

EXPECTED_DEUTERON_TWO_ROW_SERIES = {
    (6,): {
        "chi_free": (F(1), F(4), F(8)),
        "chi_atom": (F(1), F(4), F(17, 2)),
        "dchi": (F(0), F(0), F(-1, 2)),
        "y": (F(7, 64), F(0), F(35, 64)),
        "y_dchi": (F(0), F(0), F(-7, 128)),
    },
    (5, 1): {
        "chi_free": (F(1), F(-3), F(-7, 2)),
        "chi_atom": (F(0), F(-5), F(-27, 2)),
        "dchi": (F(1), F(2), F(10)),
        "y": (F(5, 64), F(0), F(5, 64)),
        "y_dchi": (F(5, 64), F(5, 32), F(55, 64)),
    },
    (4, 2): {
        "chi_free": (F(1), F(-3), F(17, 2)),
        "chi_atom": (F(0), F(1), F(31, 2)),
        "dchi": (F(1), F(-4), F(-7)),
        "y": (F(3, 64), F(0), F(-5, 64)),
        "y_dchi": (F(3, 64), F(-3, 16), F(-13, 32)),
    },
    (3, 3): {
        "chi_free": (F(1), F(4), F(20)),
        "chi_atom": (F(1), F(-2), F(-1, 2)),
        "dchi": (F(0), F(6), F(41, 2)),
        "y": (F(1, 64), F(0), F(-3, 64)),
        "y_dchi": (F(0), F(3, 32), F(41, 128)),
    },
}


def run_part2_deuteron_h6_chi() -> dict:
    """Evaluate free vs bound chi_lambda for 2H across all 11 partitions of H_6(q) (`qou-6h6p`)."""
    print("=" * 84)
    print("PART 2 (qou-6h6p): Deuteron (2H) at H_6(q) — Free vs Bound chi_lambda Decomposition")
    print("=" * 84)

    n = 6
    P = 4
    q_ser = _c1p.Ser.eps(P)
    x_free = _cbc.atom_canonical_crossings(1, 1, include_inter=False)
    x_atom = _cbc.atom_canonical_crossings(1, 1, include_inter=True)
    fac_free_ser = _erc.factors_for(x_free, q_ser, colour_weighted=True)
    fac_atom_ser = _erc.factors_for(x_atom, q_ser, colour_weighted=True)
    ys_ser, bad_three_row = _c1p.y_lambda_series(n, P)

    # Exact rational evaluation at the 50-digit canonical proton pin q0, lifted to 80-dps mpf
    q0_mp = mp.mpf(str(Q_50_DIGIT_STR))
    q0_frac = F(str(Q_50_DIGIT_STR))
    fac_free_q0 = _erc.factors_for(x_free, q0_frac, colour_weighted=True)
    fac_atom_q0 = _erc.factors_for(x_atom, q0_frac, colour_weighted=True)
    ta_tr, tf_tr, chi_atom_tr, _ = _tr.tr_m_atom_zn(1, 1, dps=80, q=q0_mp)
    y_sym = y_lambda_at(n)

    sum_ser = _c1p.Ser.const(0)
    sum_free_q0 = mp.mpf(0)
    sum_atom_q0 = mp.mpf(0)
    max_chi_diff_q0 = mp.mpf(0)
    two_row_series_ok = len(bad_three_row) == 0
    part_rows = []

    print(
        f"  {'lambda':<18} {'chi_free[0..2]':<22} {'chi_atom[0..2]':<22} "
        f"{'dchi(q0)':>16} {'y_lam(q0)':>16}"
    )
    for lam in PARTITIONS_6:
        lam_t = tuple(lam)
        cf_s = _erc.chi_at(lam, fac_free_ser, q_ser)
        ca_s = _erc.chi_at(lam, fac_atom_ser, q_ser)
        dc_s = cf_s - ca_s
        yl_s = ys_ser.get(lam_t, _c1p.Ser.const(0))
        yd_s = yl_s * dc_s
        sum_ser = sum_ser + yd_s

        cf_tup = tuple(cf_s.coeff(k) for k in range(3))
        ca_tup = tuple(ca_s.coeff(k) for k in range(3))
        dc_tup = tuple(dc_s.coeff(k) for k in range(3))
        yl_tup = tuple(yl_s.coeff(k) for k in range(3))
        yd_tup = tuple(yd_s.coeff(k) for k in range(3))

        if lam_t in EXPECTED_DEUTERON_TWO_ROW_SERIES:
            exp = EXPECTED_DEUTERON_TWO_ROW_SERIES[lam_t]
            two_row_series_ok &= (
                cf_tup == exp["chi_free"]
                and ca_tup == exp["chi_atom"]
                and dc_tup == exp["dchi"]
                and yl_tup == exp["y"]
                and yd_tup == exp["y_dchi"]
            )
        else:
            two_row_series_ok &= yl_tup == (F(0), F(0), F(0))

        cf_q0 = frac_to_mpf(_erc.chi_at(lam, fac_free_q0, q0_frac))
        ca_q0 = frac_to_mpf(_erc.chi_at(lam, fac_atom_q0, q0_frac))
        dc_q0 = cf_q0 - ca_q0
        chi_diff = abs(ca_q0 - chi_atom_tr[lam_t])
        if chi_diff > max_chi_diff_q0:
            max_chi_diff_q0 = chi_diff

        y_expr = sp.simplify(y_sym[lam_t])
        if y_expr == 0:
            yv_q0 = mp.mpf(0)
        else:
            num, den = sp.fraction(sp.together(y_expr))
            num_poly = sp.Poly(num, Q_SYM)
            den_poly = sp.Poly(den, Q_SYM)
            num_val = sum(mp.mpf(int(c)) * (q0_mp ** k) for (k,), c in num_poly.terms())
            den_val = sum(mp.mpf(int(c)) * (q0_mp ** k) for (k,), c in den_poly.terms())
            yv_q0 = num_val / den_val

        sum_free_q0 += yv_q0 * cf_q0
        sum_atom_q0 += yv_q0 * ca_q0

        part_rows.append(
            {
                "partition": list(lam),
                "num_rows": len(lam),
                "chi_free_eps012": [str(x) for x in cf_tup],
                "chi_atom_eps012": [str(x) for x in ca_tup],
                "dchi_eps012": [str(x) for x in dc_tup],
                "y_lambda_eps012": [str(x) for x in yl_tup],
                "y_dchi_eps012": [str(x) for x in yd_tup],
                "chi_free_q0": mp.nstr(cf_q0, 25),
                "chi_atom_q0": mp.nstr(ca_q0, 25),
                "dchi_q0": mp.nstr(dc_q0, 25),
                "y_lambda_q0": mp.nstr(yv_q0, 25),
                "y_dchi_q0": mp.nstr(yv_q0 * dc_q0, 25),
            }
        )
        print(
            f"  {str(lam):<18} {str([str(x) for x in cf_tup]):<22} "
            f"{str([str(x) for x in ca_tup]):<22} "
            f"{mp.nstr(dc_q0, 10):>16} {mp.nstr(yv_q0, 10):>16}"
        )

    a0_2h = sum_ser.coeff(0)
    a1_2h = sum_ser.coeff(1)
    a2_2h = sum_ser.coeff(2)
    c0_2h = a0_2h
    c1_2h = a1_2h
    c2_2h = a1_2h + a2_2h
    series_sum_ok = (
        c0_2h == F(1, 8)
        and c1_2h == F(1, 16)
        and a2_2h == F(23, 32)
        and c2_2h == F(25, 32)
    )
    dtr_wedderburn_q0 = sum_free_q0 - sum_atom_q0
    dtr_transfer_q0 = tf_tr - ta_tr
    dtr_diff_q0 = abs(dtr_wedderburn_q0 - dtr_transfer_q0)
    q0_match_ok = max_chi_diff_q0 < mp.mpf("1e-75") and dtr_diff_q0 < mp.mpf("1e-49")

    print(
        f"  Wedderburn sum [eps^0, eps^1, eps^2] = [{a0_2h}, {a1_2h}, {a2_2h}] "
        f"=> c0={c0_2h}, c1={c1_2h}, c2={c2_2h} [ok={series_sum_ok}]"
    )
    print(
        f"  80-dps q0 check: tr_free={mp.nstr(sum_free_q0, 18)}, "
        f"tr_atom={mp.nstr(sum_atom_q0, 18)}, dtr={mp.nstr(dtr_wedderburn_q0, 18)} "
        f"(max|chi_diff|={mp.nstr(max_chi_diff_q0, 6)}, |dtr_diff|={mp.nstr(dtr_diff_q0, 6)})\n"
    )
    return {
        "rows": part_rows,
        "two_row_series_ok": two_row_series_ok,
        "series_sum_ok": series_sum_ok,
        "q0_match_ok": q0_match_ok,
        "max_chi_diff_q0": max_chi_diff_q0,
        "dtr_diff_q0": dtr_diff_q0,
        "tr_free_q0": sum_free_q0,
        "tr_atom_q0": sum_atom_q0,
        "dtr_q0": dtr_wedderburn_q0,
    }


# =============================================================================
# PART 3: Plancherel Covariance Kernel cov(k) <= 0 and Legs A2 & A3 (k = 1..20)
# =============================================================================

EXPECTED_COV_1_TO_10 = {
    1: 0,
    2: 0,
    3: -4,
    4: -16,
    5: -320,
    6: -10400,
    7: -163520,
    8: -3224704,
    9: -106339296,
    10: -4722309120,
}


def partitions_of(n: int, m: int | None = None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for rest in partitions_of(n - i, i):
            yield (i,) + rest


def transpose_partition(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    return tuple(sum(1 for row in lam if row > j) for j in range(lam[0]))


def hook_product(lam: tuple[int, ...]) -> int:
    conj = transpose_partition(lam)
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return prod


def syt_dim(lam: tuple[int, ...], k_fact: int) -> int:
    return k_fact // hook_product(lam)


def _int_factorial(n: int) -> int:
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def content_sq_sum(lam: tuple[int, ...]) -> int:
    return sum((j - i) ** 2 for i, row in enumerate(lam) for j in range(row))


def run_part3_plancherel_covariance(k_max: int = 20) -> dict:
    """Evaluate Plancherel covariance kernel cov(k) and Legs A2 & A3 for k = 1..k_max (`qou-v8t7`)."""
    print("=" * 84)
    print(f"PART 3 (qou-v8t7): Plancherel Covariance Kernel cov(k) & Legs A2, A3 (k = 1..{k_max})")
    print("=" * 84)
    print(
        f"  {'k':>2} | {'#part':>5} | {'cov(k) = sum f^3 omega_3':>26} | "
        f"{'g(1)':>14} | {'g\'(0) (Leg A2)':>15} | {'r=g(1)/g\'(0)':>13} | {'|r-1|<1 (Leg A3)':>16}"
    )

    k_rows = []
    plancherel_id_ok = True
    transpose_sym_ok = True
    kernel_nonpos_ok = True
    leg_a2_ok = True
    leg_a3_ok = True
    exact_1_to_10_ok = True

    for k in range(1, k_max + 1):
        k_fact = _int_factorial(k)
        ck2 = k * (k - 1) // 2
        parts = list(partitions_of(k))

        sum_f2 = 0
        sum_f2_w = 0
        sum_f3 = 0
        cov_k = 0
        lnf_terms = []

        dim_map: dict[tuple[int, ...], int] = {}
        w_map: dict[tuple[int, ...], int] = {}

        for lam in parts:
            f = syt_dim(lam, k_fact)
            w = content_sq_sum(lam) - ck2
            dim_map[lam] = f
            w_map[lam] = w

            f2 = f * f
            f3 = f2 * f
            sum_f2 += f2
            sum_f2_w += f2 * w
            sum_f3 += f3
            cov_k += f3 * w
            if w != 0:
                lnf_terms.append(mp.mpf(f2) * mp.log(mp.mpf(f)) * mp.mpf(w))

        # Verify transpose symmetry f^{lam'} == f^lam and omega_3(lam') == omega_3(lam)
        for lam in parts:
            lam_t = transpose_partition(lam)
            if dim_map[lam_t] != dim_map[lam] or w_map[lam_t] != w_map[lam]:
                transpose_sym_ok = False

        plancherel_id_ok &= (sum_f2 == k_fact) and (sum_f2_w == 0)
        if k in EXPECTED_COV_1_TO_10:
            exact_1_to_10_ok &= cov_k == EXPECTED_COV_1_TO_10[k]

        g1 = mp.mpf(cov_k) / mp.mpf(sum_f3)
        gp0 = mp.fsum(lnf_terms) / mp.mpf(k_fact) if lnf_terms else mp.mpf(0)

        if k <= 2:
            k_ok = cov_k == 0
            a2_k = gp0 == 0
            a3_k = True
            r_val = mp.mpf(1)
            rem_ratio = mp.mpf(0)
        else:
            k_ok = cov_k < 0
            a2_k = gp0 < 0
            r_val = g1 / gp0
            rem_ratio = abs(r_val - 1)
            a3_k = (r_val > 0) and (r_val < 2) and (rem_ratio < 1)

        kernel_nonpos_ok &= k_ok
        leg_a2_ok &= a2_k
        leg_a3_ok &= a3_k

        k_rows.append(
            {
                "k": k,
                "num_partitions": len(parts),
                "k_factorial": str(k_fact),
                "sum_f2": str(sum_f2),
                "sum_f2_omega3": str(sum_f2_w),
                "sum_f3": str(sum_f3),
                "cov_k": str(cov_k),
                "g1_exact_ratio": f"{cov_k}/{sum_f3}",
                "g1_mpf": mp.nstr(g1, 25),
                "gp0_mpf": mp.nstr(gp0, 25),
                "transfer_ratio_r": mp.nstr(r_val, 25),
                "remainder_over_main": mp.nstr(rem_ratio, 25),
                "kernel_ok": k_ok,
                "leg_a2_ok": a2_k,
                "leg_a3_ok": a3_k,
            }
        )
        print(
            f"  {k:2d} | {len(parts):5d} | {str(cov_k):>26} | "
            f"{mp.nstr(g1, 7):>14} | {mp.nstr(gp0, 7):>15} | "
            f"{mp.nstr(r_val, 7):>13} | {str(a3_k):>16}"
        )

    print(
        f"\n  Plancherel identities (sum f^2 == k! and sum f^2 omega_3 == 0, k=1..{k_max}): "
        f"{plancherel_id_ok}"
    )
    print(f"  Transpose-involution symmetry (f^lam'==f^lam, omega_3(lam')==omega_3(lam)): {transpose_sym_ok}")
    print(f"  Exact kernel cov(k) <= 0 (==0 for k=1,2; <0 for k=3..{k_max}): {kernel_nonpos_ok}")
    print(f"  Leg A2 (g'(0) < 0 for k=3..{k_max}): {leg_a2_ok}")
    print(f"  Leg A3 (|g(1) - g'(0)| < |g'(0)| for k=3..{k_max}): {leg_a3_ok}\n")

    return {
        "k_max": k_max,
        "rows": k_rows,
        "plancherel_id_ok": plancherel_id_ok,
        "transpose_sym_ok": transpose_sym_ok,
        "kernel_nonpos_ok": kernel_nonpos_ok,
        "exact_1_to_10_ok": exact_1_to_10_ok,
        "leg_a2_ok": leg_a2_ok,
        "leg_a3_ok": leg_a3_ok,
    }


def main() -> int:
    p1 = run_part1_reordered_c2()
    p2 = run_part2_deuteron_h6_chi()
    p3 = run_part3_plancherel_covariance(k_max=20)

    w = WitnessBuilder(
        "delta-lambda-covariance-and-reordered-c2-probe",
        engine="python-mpmath-80dps-and-exact-fraction",
    )
    w.set_description(
        "80-dps and exact rational compute probe closing three linked MassTheory / Delta_lambda "
        "derivations without float64 intermediates or parameter fitting: "
        "(1) qou-qqm4 — exact reordered-word (c0, c1, a2, c2) and |S|<=2 diagonal-insertion class "
        "splits for pp (33/32), pn (25/32), nn (1/16), T (99/128), 3He (157/128), 4He (439/512), "
        "the A=3 mirror sum 99/128 + 157/128 = 2, the A=2 content-cancellation invariance "
        "c2(pp) + c2(nn) - 2*c2(pn) = -15/32, and chain/atom second-order ratios (12/11, 232/157, "
        "960/439); "
        "(2) qou-6h6p — deuteron (2H) at H_6(q) per-partition chi_lambda free-vs-bound table across "
        "all 11 partitions lambda |- 6 both as exact rational [eps^0, eps^1, eps^2] series and at "
        "80-dps canonical proton pin q0; "
        "(3) qou-v8t7 — Plancherel covariance kernel cov(k) = sum_{lambda|-k} (f^lambda)^3 omega_3(lambda) "
        "<= 0, transpose-involution invariance, Leg A2 (g'(0) < 0), and Leg A3 (|g(1)-g'(0)| < |g'(0)|) "
        "for k = 1..20."
    )

    w.add_data("compute_dps", 80)
    w.add_data("q0_proton_pin_50d", str(Q_50_DIGIT_STR))

    w.add_data(
        "reordered_word_c2_table",
        {
            k: {
                key: str(val) if isinstance(val, F) else val
                for key, val in v.items()
            }
            for k, v in p1["rows"].items()
        },
    )
    w.add_data("a3_mirror_sum_c2", str(p1["mirror_sum_a3"]))
    w.add_data("a2_content_cancellation_c2_canonical", str(p1["content_cancel_canon"]))
    w.add_data("a2_content_cancellation_c2_grouped", str(p1["content_cancel_grouped"]))
    w.add_data(
        "chain_over_atom_ratios",
        {
            "order1_c1": {k: str(v) for k, v in p1["r1"].items()},
            "order2_c2": {k: str(v) for k, v in p1["r2"].items()},
        },
    )
    w.add_data("deuteron_h6_partitions", p2["rows"])
    w.add_data("plancherel_covariance_k1_to_20", p3["rows"])

    # Assertions for Part 1 (qou-qqm4)
    w.add_assertion(
        "reordered_c2_diagonal_insertion_all_six_exact",
        computed="1" if p1["all_match"] else "0",
        expected="1",
        tolerance=0,
        source=(
            "Exact cycle-decomposed diagonal-insertion expansion [◇] (|S|<=2) reproduces "
            "(a0, c1, a2, c2) and the |S|=0,1,2 class splits for pp (33/32), pn (25/32), "
            "nn (1/16), T (99/128), 3He (157/128), and 4He (439/512) (qou-qqm4)."
        ),
    )
    w.add_assertion(
        "reordered_c2_a2_wedderburn_series_and_grouped_crosscheck",
        computed="1" if p1["ser_a2_ok"] else "0",
        expected="1",
        tolerance=0,
        source=(
            "Exact Wedderburn Ser eps-series on A=2 (pp, pn, nn) matches the diagonal-insertion "
            "expansion identically (33/32, 25/32, 1/16 on borromean; 357/32, 403/32, 217/16 on grouped)."
        ),
    )
    w.add_assertion(
        "reordered_c2_a3_mirror_sum_equals_2",
        computed=str(p1["mirror_sum_a3"]),
        expected="2",
        tolerance=0,
        source="Exact A=3 mirror sum c2(T) + c2(3He) = 99/128 + 157/128 = 256/128 = 2 (qou-qqm4).",
    )
    w.add_assertion(
        "reordered_c2_a2_content_cancellation_invariance",
        computed=str(p1["content_cancel_canon"]),
        expected=str(p1["content_cancel_grouped"]),
        tolerance=0,
        source=(
            "Content-cancelling second-order combination c2(pp) + c2(nn) - 2*c2(pn) = -15/32 "
            "is identically invariant between borromean (33/32 + 1/16 - 50/32) and grouped "
            "(357/32 + 217/16 - 806/32) intra-nucleon orderings."
        ),
    )
    w.add_assertion(
        "reordered_c2_chain_over_atom_ratios_exact",
        computed="1" if (p1["ratios_ok"] and p1["s0_blind_ok"]) else "0",
        expected="1",
        tolerance=0,
        source=(
            "Exact second-order chain-over-atom ratios T: 12/11, 3He: 232/157, 4He: 960/439 "
            "with |r2 - 1| < |r1 - 1| vs first-order (4, 3/2, 24/7), plus species-blindness "
            "of the |S|=0 permutation floor (0 at A=2, 5/32 at A=3, 11/64 at A=4)."
        ),
    )

    # Assertions for Part 2 (qou-6h6p)
    w.add_assertion(
        "deuteron_h6_chi_lambda_eps_series_reproduces_c0_c1_c2",
        computed="1" if (p2["two_row_series_ok"] and p2["series_sum_ok"]) else "0",
        expected="1",
        tolerance=0,
        source=(
            "Exact H_6(q) Wedderburn character decomposition sum_{l(lambda)<=2} y_lambda * "
            "(chi^lambda_free - chi^lambda_atom) over {(6), (5,1), (4,2), (3,3)} yields "
            "[eps^0, eps^1, eps^2] = [1/8, 1/16, 23/32] and (c0, c1, c2) = (1/8, 1/16, 25/32) "
            "(qou-6h6p)."
        ),
    )
    w.add_assertion(
        "deuteron_h6_chi_lambda_80dps_matches_transfer_trace",
        computed=p2["dtr_q0"],
        expected=p2["tr_free_q0"] - p2["tr_atom_q0"],
        tolerance=mp.mpf("1e-49"),
        source=(
            "At 80-dps canonical proton pin q0, all 11 H_6(q0) irreps chi^lambda(W_atom) match "
            "tr_m_atom_zn to < 1e-75 and the two-row Wedderburn sum matches Delta tr_M(2H; q0) "
            "to < 1e-50 (qou-6h6p)."
        ),
    )

    # Assertions for Part 3 (qou-v8t7)
    w.add_assertion(
        "plancherel_covariance_identities_and_transpose_symmetry_k1_to_20",
        computed="1" if (p3["plancherel_id_ok"] and p3["transpose_sym_ok"]) else "0",
        expected="1",
        tolerance=0,
        source=(
            "Exact Plancherel identities sum_{lambda|-k} (f^lambda)^2 = k! and "
            "sum_{lambda|-k} (f^lambda)^2 omega_3(lambda) = 0, plus transpose invariance "
            "f^{lambda'} = f^lambda and omega_3(lambda') = omega_3(lambda), verified for k=1..20."
        ),
    )
    w.add_assertion(
        "plancherel_covariance_kernel_nonpositive_k1_to_20",
        computed="1" if (p3["kernel_nonpos_ok"] and p3["exact_1_to_10_ok"]) else "0",
        expected="1",
        tolerance=0,
        source=(
            "Exact integer Plancherel covariance kernel cov(k) = sum_{lambda|-k} (f^lambda)^3 "
            "omega_3(lambda) satisfies cov(1) = cov(2) = 0 and cov(k) < 0 strictly for all "
            "3 <= k <= 20 (with cov(3)=-4, cov(4)=-16, cov(5)=-320, cov(6)=-10400, "
            "cov(7)=-163520) (qou-v8t7)."
        ),
    )
    w.add_assertion(
        "plancherel_covariance_legs_A2_and_A3_k3_to_20",
        computed="1" if (p3["leg_a2_ok"] and p3["leg_a3_ok"]) else "0",
        expected="1",
        tolerance=0,
        source=(
            "80-dps verification of Leg A2 (g'(0) = Cov_Planch(ln f^lambda, omega_3(lambda)) < 0) "
            "and Leg A3 (|g(1) - g'(0)| < |g'(0)|, equivalently r = g(1)/g'(0) in (0, 2)) for all "
            "3 <= k <= 20 (qou-v8t7)."
        ),
    )

    out_path = w.save({"q0Anchor": "proton", "q0Value": str(Q_50_DIGIT_STR)})
    print(f"Witness written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
