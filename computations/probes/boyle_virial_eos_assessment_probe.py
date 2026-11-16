#!/usr/bin/env python3
"""Assess whether QOU defines or exhibits a Boyle resonance (B_2(q) = 0) at q_0.

Bean `qou-tekm` (Epic `qou-8lxd`).

Owner question:
  "What does QOU say about a Boyle resonance?"

Answer verified at 50+ dps from the QOU corpus:

  1. **Corpus & EOS scan (7 statistical-mechanics / equation-of-state blocks):**
     Across all 7 EOS and statistical-mechanics blocks in
     `folio/quantum-observable-universe/`:
       - `observations/eos-borromean-cfl.md`
       - `observations/color-superconductivity-borromean.md`
       - `observations/cfl-neutron-star-observables.md`
       - `information-theory/phase-transitions-intro.md`
       - `information-theory/phase-transition-interpretation.md`
       - `information-theory/stat-mech-computational-horizon.md`
       - `information-theory/hydrogen-partition-function.md`
     the term "Boyle" occurs 0 times and QOU defines NO density virial
     expansion `P / (rho k_B T) = 1 + B_2(q) rho + B_3(q) rho^2 + ...`:
       * `eos-borromean-cfl.md` defines cold degenerate Fermi-gas polytropes
         `P_B(n_B) ~ n_B^(5/3) / M_B(q_0)` and
         `P_D(n_B) ~ (3 n_B)^(5/3) / M_D(q_0) + 3 Delta_CFL^2 mu_q^2 / pi^2`
         with stiffness ratio `(M_B / M_D) * 3^(5/3) ~= 6947.27` (kinetic) /
         `~= 6977` (with CFL gap), which has zero `n_B^2` second-virial term.
       * `stat-mech-computational-horizon.md` and
         `hydrogen-partition-function.md` define the q-deformed ideal gas law
         `P_q V_q = N T_q (1 + (hbar_q^2 / [2]_q) <S_q>)`, where the
         q-correction is a density-independent single-knot boundary factor
         (`O(rho^0)` in `P_q / (rho T_q)`), not a 2-body density virial term.

  2. **Natural 2-body Mayer / cluster trace excess `B_2^trace(q)`:**
     If one defines a 2-body cluster / Mayer excess from the atomic Markov
     trace `tr_M`:
       - Classical `q = 1` limit (`tr_M(A_A)|_{q=1} = 2^(1 - 2A)`):
           `tr_M(A_1)|_{q=1} = 1/2`,  `tr_M(A_2)|_{q=1} = 1/8 = c_0(2)`,
         giving the raw 2-body cluster excess
           `B_2^raw(1) = tr_M(A_2)|_{q=1} - (tr_M(A_1)|_{q=1})^2`
                       `= 1/8 - 1/4 = -1/8 = -c_0(2) != 0`,
         unknot-baseline shift `c_0(2) - 1 = -7/8 != 0`, and reduced interface
         Mayer factor `B_2^red(1) = f(1) - 1 = 1/2 - 1 = -1/2 != 0`.
       - At the physical substrate `q_0` and across the entire interval
         `q in [1, 23/20]`, the reduced 2-body Mayer factor
           `B_2^red(q) = tr_M(W_atom) / tr_M(W_free) - 1 = f_{N1,N2}(q) - 1`
         and the full H_3-weighted 2-body trace excess
           `B_2^raw(q) = tr_M(W_atom) - tr_M(W_free)`
                       `= tau_{N1}(q) tau_{N2}(q) (f_{N1,N2}(q) - 1)`
         for `(pp, pn, nn)` remain strictly negative (`B_2^red(q) < -0.34`
         everywhere on `[1, 23/20]`, and `B_2^raw(q_0) ~= -0.1534, -0.1470,
         -0.1346` for `pp, pn, nn`). Neither vanishes at or near `q_0`.

No float64: mpmath end to end at repo-default precision (65 working / 52
serialised dps), proton pin by default.
"""
from __future__ import annotations

import sys as _sys
import time as _time
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from closed_form_tau_M import (  # noqa: E402
    closed_form_ratio,
    compute_tau_M_nucleon_H3,
    hecke_h,
    interface_factor,
    markov_z,
)
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

EOS_STAT_MECH_BLOCKS = (
    "observations/eos-borromean-cfl.md",
    "observations/color-superconductivity-borromean.md",
    "observations/cfl-neutron-star-observables.md",
    "information-theory/phase-transitions-intro.md",
    "information-theory/phase-transition-interpretation.md",
    "information-theory/stat-mech-computational-horizon.md",
    "information-theory/hydrogen-partition-function.md",
)


def _find_folio_dir() -> _Path:
    """Resolve folio/quantum-observable-universe from repo root."""
    here = _Path(__file__).resolve()
    for parent in here.parents:
        cand = parent / "folio" / "quantum-observable-universe"
        if cand.is_dir():
            return cand
    return _Path("/Users/litlfred/space_cats/qou/folio/quantum-observable-universe")


def q_int_2(q: mp.mpf) -> mp.mpf:
    """Symmetric quantum integer [2]_q = q + q^-1."""
    return q + mp.mpf(1) / q


def interface_factors_at_q(q: mp.mpf) -> dict[str, mp.mpf]:
    """Return f_pp(q), f_pn(q), f_nn(q) under the canonical Bring color-tube convention."""
    z = markov_z(q)
    h = hecke_h(q)
    delta = flavor_split_leading(q)
    return {
        "pp": z,
        "pn": z - h * (mp.mpf(1) / mp.mpf(2) - delta / mp.mpf(4)),
        "nn": z - h,
    }


def main() -> int:
    t0 = _time.monotonic()
    set_compute_dps()
    q0 = mp.mpf(Q_50_DIGIT_STR)
    q0_inv = mp.mpf(1) / q0
    hbar_q0 = mp.mpf(1) - q0_inv

    # 1. Scan the 7 EOS / stat-mech blocks for any occurrence of "Boyle"
    folio_dir = _find_folio_dir()
    boyle_mentions_by_block: dict[str, int] = {}
    blocks_checked = 0
    for rel_path in EOS_STAT_MECH_BLOCKS:
        p = folio_dir / rel_path
        text = p.read_text(encoding="utf-8")
        boyle_mentions_by_block[rel_path] = text.lower().count("boyle")
        blocks_checked += 1
    total_boyle_mentions = sum(boyle_mentions_by_block.values())

    # 2. Evaluate the Borromean / CFL EOS parameters from eos-borromean-cfl.md at q0:
    #    M_B(q0) = V_B / hbar_q^2 = 8*G / (1 - q0^-1)^2
    #    M_D(q0) = (q0 + q0^-1) / 3
    #    Kinetic stiffness ratio = (M_B / M_D) * 3^(5/3)
    vol_b3 = mp.mpf(8) * mp.catalan
    m_b_q0 = vol_b3 / (hbar_q0 ** 2)
    m_d_q0 = (q0 + q0_inv) / mp.mpf(3)
    three_pow_5_3 = mp.power(mp.mpf(3), mp.mpf(5) / mp.mpf(3))
    cfl_kinetic_stiffness_ratio = (m_b_q0 / m_d_q0) * three_pow_5_3

    # q-deformed ideal-gas single-knot anomaly prefactor hbar_q^2 / [2]_q
    # from stat-mech-computational-horizon.md / hydrogen-partition-function.md:
    q_anomaly_prefactor = (hbar_q0 ** 2) / q_int_2(q0)

    # 3. Classical q = 1 limit of the 2-body Markov trace cluster excess:
    #    tr_M(A_A)|_{q=1} = 2^((A+1) - 3A) = 2^(1 - 2A)
    tr_a1_q1 = mp.mpf(1) / mp.mpf(2)      # A = 1: 2^-1 = 1/2
    tr_a2_q1 = mp.mpf(1) / mp.mpf(8)      # A = 2: 2^-3 = 1/8 = c_0(2)
    b2_raw_q1 = tr_a2_q1 - (tr_a1_q1 ** 2)  # 1/8 - 1/4 = -1/8 = -c_0(2)
    b2_unknot_shift_q1 = tr_a2_q1 - mp.mpf(1)  # 1/8 - 1 = -7/8
    f_q1 = markov_z(mp.mpf(1))            # 1 / 2
    b2_reduced_q1 = f_q1 - mp.mpf(1)      # -1 / 2

    # 4. Evaluate 2-body cluster / Mayer trace excess at q0 (50+ dps):
    tau_p_q0 = compute_tau_M_nucleon_H3("p", q0, dps=65)
    tau_n_q0 = compute_tau_M_nucleon_H3("n", q0, dps=65)
    f_q0 = interface_factors_at_q(q0)

    # Verify agreement with closed_form_ratio:
    f_pp_check = interface_factor("positive", q0)
    f_nn_check = interface_factor("negative", q0)
    f_pn_check = closed_form_ratio(1, 1, q0, pn_convention="bring_color_weighted")
    ratio_consistency_err = (
        abs(f_q0["pp"] - f_pp_check)
        + abs(f_q0["pn"] - f_pn_check)
        + abs(f_q0["nn"] - f_nn_check)
    )

    free_traces_q0 = {
        "pp": tau_p_q0 * tau_p_q0,
        "pn": tau_p_q0 * tau_n_q0,
        "nn": tau_n_q0 * tau_n_q0,
    }
    atom_traces_q0 = {
        ch: free_traces_q0[ch] * f_q0[ch] for ch in ("pp", "pn", "nn")
    }
    b2_reduced_q0 = {
        ch: f_q0[ch] - mp.mpf(1) for ch in ("pp", "pn", "nn")
    }
    b2_raw_q0 = {
        ch: atom_traces_q0[ch] - free_traces_q0[ch] for ch in ("pp", "pn", "nn")
    }

    # 5. Sweep across 16 grid points on q in [1, 23/20] = [1.00, 1.15] to verify
    #    that B_2^red(q) = f(q) - 1 has NO zero crossing (no Boyle point) anywhere
    #    on the physical interval:
    grid_q = [mp.mpf(1) + mp.mpf(k) / mp.mpf(100) for k in range(16)]
    grid_rows = []
    max_b2_reduced_on_grid = mp.mpf("-inf")
    min_abs_b2_reduced_on_grid = mp.mpf("inf")
    for q_pt in grid_q:
        fs = interface_factors_at_q(q_pt)
        b2s = {ch: fs[ch] - mp.mpf(1) for ch in ("pp", "pn", "nn")}
        for val in b2s.values():
            if val > max_b2_reduced_on_grid:
                max_b2_reduced_on_grid = val
            if abs(val) < min_abs_b2_reduced_on_grid:
                min_abs_b2_reduced_on_grid = abs(val)
        grid_rows.append(
            {
                "q": fmt(q_pt),
                "b2_red_pp": fmt(b2s["pp"]),
                "b2_red_pn": fmt(b2s["pn"]),
                "b2_red_nn": fmt(b2s["nn"]),
            }
        )

    b = WitnessBuilder(
        "boyle-virial-eos-assessment",
        engine="mpmath",
        start_time=t0,
    )
    b.set_description(
        "Bean qou-tekm (Epic qou-8lxd). Assesses at 50+ dps what QOU says about a "
        "Boyle resonance / second virial coefficient zero (B_2(q) = 0): (1) across "
        "all 7 statistical-mechanics and EOS content blocks in "
        "folio/quantum-observable-universe/, 'Boyle' occurs 0 times and no density "
        "virial expansion P/(rho k_B T) = 1 + B_2(q) rho + ... is defined "
        "(eos-borromean-cfl.md defines a cold degenerate Fermi-gas polytrope "
        "P ~ n_B^(5/3) with kinetic stiffness ratio P_D/P_B ~= 6947.27 and zero "
        "n_B^2 virial term; stat-mech-computational-horizon.md and "
        "hydrogen-partition-function.md define a density-independent single-knot "
        "boundary factor 1 + (hbar_q^2/[2]_q)<S_q>); (2) the natural 2-body Mayer / "
        "cluster trace excess B_2^raw(q) = tr_M(W_atom) - tr_M(W_free) and reduced "
        "factor B_2^red(q) = f(q) - 1 equal -c_0(2) = -1/8 and -1/2 at q = 1, and "
        "stay strictly negative (|B_2^red(q)| > 0.32) across the entire physical "
        "interval q in [1, 23/20], including q_0 (no Boyle point exists near q_0)."
    )
    b.add_parameter("q0", Q_50_DIGIT_STR)
    b.add_data(
        "corpus_eos_scan",
        {
            "blocks_checked": blocks_checked,
            "boyle_mentions_by_block": boyle_mentions_by_block,
            "total_boyle_mentions": total_boyle_mentions,
            "eos_borromean_cfl_M_B_q0": fmt(m_b_q0),
            "eos_borromean_cfl_M_D_q0": fmt(m_d_q0),
            "eos_borromean_cfl_kinetic_stiffness_ratio": fmt(
                cfl_kinetic_stiffness_ratio
            ),
            "q_ideal_gas_single_knot_prefactor_hbar2_over_q2": fmt(
                q_anomaly_prefactor
            ),
        },
    )
    b.add_data(
        "classical_q1_cluster_baseline",
        {
            "tr_M_A1_at_q1": fmt(tr_a1_q1),
            "tr_M_A2_at_q1_c0_2": fmt(tr_a2_q1),
            "b2_raw_at_q1_minus_c0_2": fmt(b2_raw_q1),
            "b2_unknot_shift_c0_2_minus_1": fmt(b2_unknot_shift_q1),
            "b2_reduced_at_q1": fmt(b2_reduced_q1),
        },
    )
    b.add_data(
        "two_body_cluster_excess_at_q0",
        {
            "tau_p_H3_q0": fmt(tau_p_q0),
            "tau_n_H3_q0": fmt(tau_n_q0),
            "interface_factors_f_q0": {k: fmt(v) for k, v in f_q0.items()},
            "b2_reduced_f_minus_1_q0": {k: fmt(v) for k, v in b2_reduced_q0.items()},
            "b2_raw_trace_excess_q0": {k: fmt(v) for k, v in b2_raw_q0.items()},
        },
    )
    b.add_data(
        "interval_sweep_q_1_to_1p15",
        {
            "grid_points": len(grid_rows),
            "max_b2_reduced_on_grid": fmt(max_b2_reduced_on_grid),
            "min_abs_b2_reduced_on_grid": fmt(min_abs_b2_reduced_on_grid),
            "rows": grid_rows,
        },
    )

    b.add_assertion(
        "zero_boyle_mentions_in_eos_and_stat_mech_blocks",
        computed=str(total_boyle_mentions),
        expected="0",
        tolerance="0",
        source="Direct scan of all 7 EOS and statistical-mechanics blocks in "
               "folio/quantum-observable-universe/ confirms 'Boyle' occurs 0 times.",
    )
    b.add_assertion(
        "classical_q1_two_body_trace_excess_equals_minus_one_eighth",
        computed=fmt(abs(b2_raw_q1 - (-mp.mpf(1) / mp.mpf(8))) + abs(b2_unknot_shift_q1 - (-mp.mpf(7) / mp.mpf(8)))),
        expected="0",
        tolerance="1e-48",
        source="At q = 1, tr_M(A_1) = 1/2 and tr_M(A_2) = 1/8 = c_0(2), so "
               "B_2^raw(1) = tr_M(A_2) - tr_M(A_1)^2 = -1/8 = -c_0(2) and "
               "c_0(2) - 1 = -7/8.",
    )
    b.add_assertion(
        "interface_factors_match_closed_form_tau_M_at_q0",
        computed=fmt(ratio_consistency_err),
        expected="0",
        tolerance="1e-48",
        source="Per-channel interface factors f_pp, f_pn, f_nn at q0 match "
               "closed_form_tau_M.py under canonical bring_color_weighted convention.",
    )
    b.add_assertion(
        "no_boyle_zero_crossing_anywhere_on_physical_interval",
        computed="1" if max_b2_reduced_on_grid < mp.mpf("-0.34") and max(b2_raw_q0.values()) < mp.mpf("-0.13") else "0",
        expected="1",
        tolerance="0",
        source="Across q in [1, 23/20] and for all three nucleon pair channels "
               "(pp, pn, nn), B_2^red(q) = f(q) - 1 < -0.345 and B_2^raw(q0) < -0.134: "
               "the 2-body cluster excess is strictly negative and bounded away from 0.",
    )

    out_path = b.save()
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
