#!/usr/bin/env python3
"""80-dps mpmath + exact rational Q-Drain-4 / PR #8154 verification probe.

Verifies the Lean-backed theorems across:
  1. `qou-sbn9` (`QOU.MassTheory.H4GPMTCumulantRatio`):
     - Exact rational and 80-dps evaluation of the per-partition H_4(q) GPMT
       cumulant ratio `mu4GPMT_H4(q) / mu3GPMT_H4(q) =
       -(q^8 + 2 q^6 - 2 q^4 + 2 q^2 + 1) / ((q^2 + 1)^2 (q^4 + 1))` and its
       strictly positive magnitude `|mu_4 / mu_3|` at `q_0`, cross-checked
       against `computations/canonical_mass.py`.
  2. `qou-ndsa` (`QOU.Interactions.ConfinementLPHomogeneity`, salvaged from #8154):
     - Exact Q(q) verification on H_3(q) that `<t_M, v> = 0` forces `y_0 = 0`
       for any Gram annihilating the sign-block radical `v`, whereas a
       radical-coupled cost `t^alpha = t_M + alpha * e_5` forces a unique
       non-zero shadow price `y_0 = alpha / <1, v>`.
  3. `qou-s7ld` + `qou-brfy` (`QOU.Hecke.LevelLocalPathSumSupport`, salvaged from #8154):
     - Exact verification that all 32 `(intra_order, include_inter, isotope)`
       binding producer words from `atom_braid_word_3A` across `A = 1..6` are
       level-local with segment counts `2A - 1` (`borromean` `W_atom`), `A`
       (`borromean` `W_free`), `3A - 1` (`grouped` `W_atom`), `2A` (`grouped`
       `W_free`), chain `T_w`-support `6^A < (3A)!`, interface-parity classical
       floor `c_0(A, O) = 2^{-A}(1 - 2^{-O})`, and Bring `{5,4}` `2^30`
       quadrangulation diagonal refinements.
"""

from __future__ import annotations

import sys
import time
from fractions import Fraction
from pathlib import Path

THIS = Path(__file__).resolve()
ROOT = THIS.parents[2]
for _rel in (
    "computations",
    "computations/substrate",
    "tools/pyhecke/python",
    "tools/qou-substrate/python",
    "schemas/witness-schema/python",
):
    if str(ROOT / _rel) not in sys.path:
        sys.path.insert(0, str(ROOT / _rel))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from canonical_mass import gpmt_three_row_cumulants  # noqa: E402
from chi_path_sum_seminormal import segments_of  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from operator_selection_lp_symbolic_qq import (  # noqa: E402
    ONE,
    TR_M,
    ZERO,
    dot,
    gram_h3,
    kernel,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 80
set_compute_dps(DPS)
mp.mp.dps = DPS


def _cycle_count(n: int, gens_zero_based: list[int]) -> int:
    perm = list(range(n))
    for g in gens_zero_based:
        perm[g], perm[g + 1] = perm[g + 1], perm[g]
    visited = [False] * n
    cycles = 0
    for i in range(n):
        if not visited[i]:
            cycles += 1
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cur = perm[cur]
    return cycles


def main() -> int:
    t0 = time.time()
    set_compute_dps(DPS)
    mp.mp.dps = DPS

    q0 = mp.mpf(Q_50_DIGIT_STR)

    # 1. qou-sbn9: Exact symbolic + 80-dps verification of |mu_4 / mu_3|
    qs = sp.Symbol("q", positive=True)
    d111_s = -(qs**3) / ((qs**2 + 1) * (qs**4 + qs**2 + 1))
    d211_s = -(qs**3) * (qs**4 + qs**2 + 1) / ((qs**2 + 1) ** 3 * (qs**4 + 1))
    d1111_s = (qs**7) / ((qs**2 + 1) ** 3 * (qs**4 + 1) * (qs**4 + qs**2 + 1))
    mu3_s = -d111_s
    srow3_4_s = -3 * d211_s + d1111_s
    mu4_s = sp.simplify(srow3_4_s - 4 * mu3_s)
    ratio_closed_s = -(qs**8 + 2 * qs**6 - 2 * qs**4 + 2 * qs**2 + 1) / (
        (qs**2 + 1) ** 2 * (qs**4 + 1)
    )
    sym_ratio_ok = sp.simplify(mu4_s / mu3_s - ratio_closed_s) == 0

    gpmt = gpmt_three_row_cumulants(q0)
    mu3_q0 = mp.mpf(str(gpmt["mu3GPMT"]))
    mu4_q0 = mp.mpf(str(gpmt["mu4GPMT_H4"]))
    ratio_direct = mu4_q0 / mu3_q0
    ratio_closed = -(q0**8 + 2 * q0**6 - 2 * q0**4 + 2 * q0**2 + 1) / (
        (q0**2 + 1) ** 2 * (q0**4 + 1)
    )
    ratio_abs_err = abs(ratio_direct - ratio_closed)
    abs_ratio_q0 = abs(ratio_direct)

    # 2. qou-ndsa: Exact Q(q) radical pairing & converse non-degeneracy
    G = gram_h3()
    v = kernel(G)[0]
    one_dot_v = sum((v[i] for i in range(6)), ZERO)
    t_markov = list(TR_M)
    t_perturbed = [t_markov[i] + (ONE if i == 5 else ZERO) for i in range(6)]
    pairing_markov = dot(t_markov, v)
    pairing_perturbed = dot(t_perturbed, v)
    y0_perturbed = pairing_perturbed / one_dot_v
    ndsa_ok = bool(
        pairing_markov.is_zero()
        and pairing_perturbed == ONE
        and not one_dot_v.is_zero()
        and not y0_perturbed.is_zero()
    )

    # 3. qou-s7ld: All 32 binding producer words level-local + 6^A < (3A)!
    level_local_ok = True
    for order in ("borromean", "grouped"):
        for inc in (True, False):
            for Z_i, N_i in [
                (1, 0),
                (0, 1),
                (1, 1),
                (1, 2),
                (2, 1),
                (2, 2),
                (3, 2),
                (3, 3),
            ]:
                A_i = Z_i + N_i
                triples = atom_braid_word_3A(
                    Z_i, N_i, include_inter=inc, intra_order=order
                )
                word = [(1 if c >= 0 else -1, g + 1) for (c, _d, g) in triples]
                segs = segments_of(word)
                expected_len = (12 * A_i - 1) if inc else (11 * A_i)
                if order == "borromean":
                    expected_segs = (2 * A_i - 1) if inc else A_i
                    expected_max_span = 2
                else:
                    expected_segs = (3 * A_i - 1) if inc else (2 * A_i)
                    expected_max_span = 1
                max_span = max((sg["gens"][-1] - sg["gens"][0] + 1) for sg in segs)
                if (
                    len(word) != expected_len
                    or len(segs) != expected_segs
                    or max_span != expected_max_span
                ):
                    level_local_ok = False

    support_ratios = {}
    support_ok = True
    for A_i in range(2, 7):
        chain_sup = 6**A_i
        sym_card = int(sp.factorial(3 * A_i))
        if not (chain_sup < sym_card and sym_card % chain_sup == 0):
            support_ok = False
        support_ratios[f"A={A_i}"] = str(sym_card // chain_sup)
    if support_ratios["A=5"] != "168168000" or support_ratios["A=6"] != "137225088000":
        support_ok = False

    # 4. Interface-parity classical floor + Bring {5,4} diagonal refinements
    parity_ok = True
    for A_i in range(2, 7):
        n_s = 3 * A_i
        free_triples = atom_braid_word_3A(
            A_i, 0, include_inter=False, intra_order="borromean"
        )
        c_free = _cycle_count(n_s, [g for (_c, _d, g) in free_triples])
        if c_free != 2 * A_i:
            parity_ok = False
        for O_i in range(0, A_i):
            bond_gens: list[int] = []
            for k in range(A_i - 1):
                g_bond = 3 * k + 2
                mult = 1 if k < O_i else 2
                bond_gens.extend([g_bond] * mult)
            c_atom = _cycle_count(
                n_s, [g for (_c, _d, g) in free_triples] + bond_gens
            )
            floor_from_cycles = Fraction(1, 2 ** (n_s - c_free)) - Fraction(
                1, 2 ** (n_s - c_atom)
            )
            floor_formula = Fraction(1, 2**A_i) * (1 - Fraction(1, 2**O_i))
            if c_atom != 2 * A_i - O_i or floor_from_cycles != floor_formula:
                parity_ok = False

    V_b, E_b, F_b = 24, 60, 30
    brfy_ok = bool(
        4 * F_b == 2 * E_b
        and 5 * V_b == 2 * E_b
        and 3 * (2 * F_b) == 2 * (E_b + F_b)
        and V_b - (E_b + F_b) + 2 * F_b == 2 - 2 * 4
        and 2**F_b == 1073741824
    )

    wb = WitnessBuilder(
        "h4-gpmt-cumulant-ratio-and-lp-support",
        engine="mpmath+sympy",
        output_dir=THIS.parent,
        start_time=t0,
    )
    wb.set_description(
        "80-dps mpmath + exact rational verification for Q-Drain-4 & PR #8154: "
        "H_4(q) GPMT cumulant ratio |mu_4 / mu_3| (qou-sbn9), confinement-LP "
        "radical pairing & converse shadow-price criterion (qou-ndsa), and "
        "level-local path-sum segmentation + 6^A vs (3A)! support bounds (qou-s7ld, qou-brfy)."
    )
    wb.add_parameter("workdps", DPS)
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_data(
        "h4_gpmt_cumulant_ratio",
        {
            "mu3GPMT_H4_q0": fmt(mu3_q0, 50),
            "mu4GPMT_H4_q0": fmt(mu4_q0, 50),
            "mu4_div_mu3_q0": fmt(ratio_direct, 50),
            "abs_mu4_div_mu3_q0": fmt(abs_ratio_q0, 50),
            "closed_form_abs_err": fmt(ratio_abs_err, 12),
        },
    )
    wb.add_data(
        "lp_radical_and_path_sum_support",
        {
            "ndsa_one_dot_v": repr(one_dot_v),
            "ndsa_perturbed_y0": repr(y0_perturbed),
            "sym_group_over_6_pow_A_ratios": support_ratios,
            "bring_diagonal_refinements": 2**F_b,
        },
    )

    wb.add_assertion(
        "qou_sbn9_h4_gpmt_mu4_over_mu3_closed_form_exact",
        computed=bool(
            sym_ratio_ok
            and ratio_abs_err < mp.mpf("1e-70")
            and abs_ratio_q0 > mp.mpf(0)
            and ratio_direct < mp.mpf(0)
        ),
        expected=True,
        source="QOU.MassTheory.H4GPMTCumulantRatio.mu4GPMT_H4_div_mu3GPMT_H4 + abs_mu4GPMT_H4_div_mu3GPMT_H4",
    )
    wb.add_assertion(
        "qou_ndsa_markov_orthogonal_and_converse_radical_pairing",
        computed=ndsa_ok,
        expected=True,
        source="QOU.Interactions.ConfinementLPHomogeneity.radical_pairing_ne_zero_of_shadow_price_ne_zero",
    )
    wb.add_assertion(
        "qou_s7ld_all_32_producer_words_level_local_and_6_pow_A_lt_fact_3A",
        computed=bool(level_local_ok and support_ok),
        expected=True,
        source="QOU.Hecke.LevelLocalPathSumSupport.twChainSupport_lt_fullSymGroupCard_of_two_le",
    )
    wb.add_assertion(
        "qou_zrx2_brfy_interface_parity_and_bring_quadrangulation_split",
        computed=bool(parity_ok and brfy_ok),
        expected=True,
        source="QOU.Hecke.LevelLocalPathSumSupport.quadrangulation_diagonal_split_preserves_euler",
    )

    out_path = wb.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})
    print(f"Saved witness: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
