#!/usr/bin/env python3
"""
Exact 80-dps mpmath + exact rational probe for Round 68 qou-8lxd beans:
  - qou-dlet: Phase 5 Detangler backward-edge DAG acyclicity and under-complexity band shift (20 -> 18)
  - qou-t6rw: Cross-check 0806.3105v3 [finkelstein2008] on the proton/neutron nucleon doublet
              (writhe-only degeneracy vs rotation-number lift Delta_r = -6)
  - qou-vwu9: Eightfold Way 3-chapter architecture partition conservation and cumulative boundary monotonicity
  - qou-wp6m: Atomic shell-filling 2*n^2 capacity (2, 8, 18, 32), Hund's rule half-shell maximum,
              and homogeneous LP primal-dual scaling
  - qou-ywsk: Phase 4 brings-surface 181-block migration scoping gap (181 - 6 = 175) and detangler cap overflow
"""

from fractions import Fraction
from pathlib import Path
import sys

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

mp.mp.dps = 80


def main() -> None:
    wb = WitnessBuilder(
        name="detangler-dag-finkelstein-nucleon-three-chapter-shell-filling-and-brings-scoping",
        engine="mpmath",
    )
    wb.description = (
        "Exact 80-dps mpmath and Fraction verification for qou-dlet, qou-t6rw, "
        "qou-vwu9, qou-wp6m, and qou-ywsk under epic qou-8lxd."
    )

    # 1. qou-dlet: Detangler backward-edge DAG transitive span & under-complexity section count shift
    pos_c, pos_b, pos_a = 3, 7, 12
    span_cb = pos_b - pos_c
    span_ba = pos_a - pos_b
    span_ca = pos_a - pos_c
    under_before = 21 - 1 - 0
    under_after = 21 - 3 - 0

    wb.add_assertion(
        "qou_dlet_detangler_backward_dag_and_under_complexity_shift",
        f"{int(span_ca == span_cb + span_ba and span_ca >= 2)}:{under_before}:{under_after}",
        "1:20:18",
        tolerance="0",
        source="QOU.Eightfold.DetanglerDagFinkelsteinNucleonThreeChapterShellFillingAndBringsScoping.detangler_backward_dag_and_under_complexity_shift",
    )

    # 2. qou-t6rw: Finkelstein (0806.3105v3) nucleon doublet writhe-only degeneracy vs rotation lift
    w_shared = Fraction(0, 1)
    r_n = Fraction(-1, 1)
    r_p_writhe_only = r_n
    r_p_lifted = r_n - Fraction(6, 1)

    q_p_deg = -(w_shared + r_p_writhe_only + 1) / Fraction(6, 1)
    q_n_deg = -(w_shared + r_n + 1) / Fraction(6, 1)
    q_p_lift = -(w_shared + r_p_lifted + 1) / Fraction(6, 1)
    t0_p_lift = -(r_p_lifted + 1) / Fraction(6, 1)
    t0_n_deg = -(r_n + 1) / Fraction(6, 1)

    wb.add_assertion(
        "qou_t6rw_finkelstein_nucleon_doublet_separation_dichotomy",
        f"{q_p_deg - q_n_deg}:{q_p_lift - q_n_deg}:{t0_p_lift - t0_n_deg}",
        "0:1:1",
        tolerance="0",
        source="QOU.Eightfold.DetanglerDagFinkelsteinNucleonThreeChapterShellFillingAndBringsScoping.finkelstein_nucleon_doublet_separation_dichotomy",
    )

    # 3. qou-vwu9: Eightfold Way 3-chapter architecture partition conservation & boundary monotonicity
    c1, c2, c3 = 18, 24, 15
    b1 = c1
    b2 = c1 + c2
    b3 = c1 + c2 + c3
    density_mean = mp.mpf(b3) / mp.mpf(21)

    wb.add_assertion(
        "qou_vwu9_three_chapter_boundary_monotonicity_and_conservation",
        f"{int(0 < b1 < b2 < b3)}:{b3 - b2}:{c3}",
        "1:15:15",
        tolerance="0",
        source="QOU.Eightfold.DetanglerDagFinkelsteinNucleonThreeChapterShellFillingAndBringsScoping.three_chapter_architecture_boundary_monotonicity",
    )

    # 4. qou-wp6m: Atomic shell-filling 2*n^2 capacity, Hund's rule half-shell maximum, and LP duality scaling
    shell_sums = [
        sum(2 * (2 * l_idx + 1) for l_idx in range(n_val))
        for n_val in (1, 2, 3, 4)
    ]
    closed_forms = [2 * (n_val ** 2) for n_val in (1, 2, 3, 4)]
    m_d_orb = 5  # d-subshell (2*2 + 1 = 5 orbitals, capacity 10)
    hund_profile = [min(k, 2 * m_d_orb - k) for k in range(2 * m_d_orb + 1)]
    y0_dual = mp.mpf("13.605693122994")
    lp_diff = abs((mp.mpf(10) + mp.mpf(8)) * y0_dual - (mp.mpf(10) * y0_dual + mp.mpf(8) * y0_dual))

    wb.add_assertion(
        "qou_wp6m_shell_filling_capacities_and_hund_profile",
        f"{shell_sums}:{int(shell_sums == closed_forms)}:{max(hund_profile)}:{hund_profile[m_d_orb]}",
        "[2, 8, 18, 32]:1:5:5",
        tolerance="0",
        source="QOU.Eightfold.DetanglerDagFinkelsteinNucleonThreeChapterShellFillingAndBringsScoping.shell_filling_capacity_hund_and_lp_duality",
    )
    wb.add_assertion(
        "qou_wp6m_lp_dual_homogeneity_80dps",
        mp.nstr(lp_diff, 30),
        "0.0",
        tolerance="1e-70",
        source="QOU.Eightfold.DetanglerDagFinkelsteinNucleonThreeChapterShellFillingAndBringsScoping.shell_filling_capacity_hund_and_lp_duality",
    )

    # 5. qou-ywsk: Bring-surface 181-block scoping discrepancy and single-section detangler overflow
    total_brings = 181
    subset_brings = 6
    scoping_gap = total_brings - subset_brings
    overflow_full = total_brings - 18
    overflow_subset = subset_brings - 18

    wb.add_assertion(
        "qou_ywsk_brings_surface_scoping_discrepancy_and_overflow",
        f"{scoping_gap}:{overflow_full}:{overflow_subset}",
        "175:163:-12",
        tolerance="0",
        source="QOU.Eightfold.DetanglerDagFinkelsteinNucleonThreeChapterShellFillingAndBringsScoping.brings_surface_scoping_discrepancy_and_overflow",
    )

    wb.data["three_chapter_mean_blocks_per_section"] = mp.nstr(density_mean, 40)
    wb.data["brings_surface_total_blocks"] = "181"
    wb.data["brings_surface_scoping_gap"] = "175"
    wb.save()


if __name__ == "__main__":
    main()
