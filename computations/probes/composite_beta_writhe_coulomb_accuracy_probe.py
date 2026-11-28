#!/usr/bin/env python3
"""
composite_beta_writhe_coulomb_accuracy_probe.py — pre-registered 80-dps proton-pinned
benchmark of composite beta-minus Q-values across all 1,009 AME2020 transitions
(ACCURACY.md Table 3.4b; beans qou-f3hr, qou-tcl2, qou-tcl3, epic qou-myts).

WHAT IS FORMALIZED (Lean, QOU/Nuclear/IsobaricBetaWritheCoulombStep.lean, 0 sorry)
---------------------------------------------------------------------------------
Across an interior composite beta-minus step (Z, N_p) -> (Z + 1, N_p - 1) at fixed
mass number A = Z + N_p (Z >= 1, N_p >= 2):

1. The T_z-even ruled log-law chain baseline (mass_table_comprehensive.py PR #9675)
   cancels identically (ruledTzEvenChainBinding_interior_eq), leaving the flat
   nucleus-independent baseline Q_n = m_n - m_p - m_e = +0.325434 MeV on all 1,009
   composite transitions (92.7% median error).
2. Under QOU/Nuclear/IsospinTwistWrithe (#9747: 2691446b388, bb1d29c6df6), a braid
   word of writhe e on 3A quark strands contributes the lowest-block T(T+1) step
       Delta B_writhe(Z, N_p) = + kappa * e * ttStepInt(N_p - Z) / (3A(3A - 1)),
   where kappa = 2 * alpha * ln(q_0), alpha = 8 * G * m_e, and ttStepInt(d) = d for
   d >= 2 (Wigner linear cusp +1 on top of the quadratic step d - 1), 0 at d = 1
   (mirror doublet inside T = 1/2), and d - 2 for d <= 0. On a gamma-gamma-selected
   word (bb1d29c6df6), e = 0 so Delta B_writhe = 0 identically.
3. Under QOU/Nuclear/IsospinWeightMultiplicity (#9747: d7c7d1081ba, 9e6eb1efd6e),
   the T_z-sector state count C(3A, Z + 2 N_p) steps by the exact ratio
   C(3A, Z + 2 N_p - 1) / C(3A, Z + 2 N_p) = (Z + 2 N_p) / (2Z + N_p + 1)
   (downQuarkWeight_beta_step); under the conditional counting energy map
   B_mult = +alpha * ln C(3A, n_d), Delta B_mult = alpha * ln((Z + 2 N_p)/(2Z + N_p + 1)).
4. Under QOU/Nuclear/CoulombIsospinChannel + docs/audits/2026-11-28-coulomb-cell-radius.md
   (#9699 + #9866, owner ruling 2026-11-28), the isobaric Coulomb step is -Z * eps_c(A)
   (coulombBinding_isobaric_step), evaluated on BOTH open labelled cell-radius arms:
   - Arm A (c = 1): R = lambda_bar_pi * A^{1/3}, derived shape f (q-Hankel for A <= 4,
     uniform ball for A >= 5; coulomb_energy.coulomb_energy_mev),
   - Arm B (c^3 = 3/2): strand-volume ratio c = (3/2)^{1/3}, satisfying
     3 * (Delta B_EM,B)^3 = 2 * (Delta B_EM,A)^3 (coulomb_step_armA_armB_cubic),
   plus a cross-check arm reproducing mass_table_comprehensive.py's m_ruled_em_MeV
   (coulomb_isospin_channel.em_energy_mev with q-Hankel f across all A).

ANTI-FIT & PIN DISCIPLINE
-------------------------
- Strictly proton-pinned (q_at(80), q0Anchor = "proton", physical_proton in
  q0_anchor_manifest.json; zero muon-pin evaluation per 2026-11-28 owner ruling).
- Zero free or fitted parameters (CAL-1 m_e, CAL-2 proton q_0, CAL-3 m_pi only).
- AME2020 enters strictly at the comparison boundary; no arm is selected on its numbers,
  and mass_table_comprehensive.py is untouched pending owner card selection.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
REPO = COMP.parent
for _p in (COMP / "substrate", COMP):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import _path_bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from canonical_mass import proton_neutron_mass_mev  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
import coulomb_energy as ce  # noqa: E402
import coulomb_isospin_channel as cic  # noqa: E402
from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def _configure_precision() -> int:
    set_compute_dps(80)
    mp.mp.dps = max(int(mp.mp.dps), 80)
    return int(mp.mp.dps)


def casimir_four(t: int) -> int:
    """4 * T(T + 1) = t * (t + 2) for t = 2T (Lean: casimirFour)."""
    return t * (t + 2)


def tt_step_int(d: int) -> int:
    """Exact integer step T_p(T_p + 1) - T_d(T_d + 1) for d = N_parent - Z
    (Lean: ttStepInt)."""
    if d >= 2:
        return d
    if d == 1:
        return 0
    return d - 2


def strand_pair_denom(A: int) -> int:
    """Murphy-product letter count 3A(3A - 1) on 3A strands (Lean: strandPairDenom)."""
    return (3 * A) * (3 * A - 1)


def _comb_int(n: int, k: int) -> int:
    """Exact arbitrary-precision integer binomial C(n, k) using pure int arithmetic."""
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    acc = 1
    for i in range(1, k + 1):
        acc = (acc * (n - k + i)) // i
    return acc


def _mean(xs: list[mp.mpf]) -> mp.mpf:
    return mp.fsum(xs) / mp.mpf(len(xs))


def _median(xs: list[mp.mpf]) -> mp.mpf:
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / mp.mpf(2)


def _band_stats(records: list[dict]) -> dict:
    rels = [r["rel_err"] for r in records]
    qs = [r["q_pred"] for r in records]
    exo = sum(1 for r in records if r["q_pred"] > 0)
    med_rel = _median(rels)
    mean_rel = _mean(rels)
    hundred = mp.mpf(100)
    ten_15 = mp.mpf(10) ** 15
    return {
        "n_transitions": len(records),
        "exothermic_count": exo,
        "exothermic_ratio": f"{exo}/{len(records)}",
        "mean_rel_err_pct": fmt(mean_rel * hundred),
        "median_rel_err_pct": fmt(med_rel * hundred),
        "median_ppQ": fmt(med_rel * ten_15),
        "median_Q_pred_MeV": fmt(_median(qs)),
        "min_Q_pred_MeV": fmt(min(qs)),
        "max_Q_pred_MeV": fmt(max(qs)),
    }


def _load_table_3_4b_transitions(m_e: mp.mpf) -> tuple[list[dict], dict]:
    """Load the exact 1,010 transitions (1 free neutron + 1,009 composite) using
    scripts/generate-accuracy-scorecard.py's Table 3.4b filter."""
    mt_path = COMP / "mass-table-comprehensive.witness.json"
    ame_path = COMP / "data" / "ame2020.json"
    mt_raw = json.loads(mt_path.read_text())
    mt_by_zn = {(int(r["Z"]), int(r["N"])): r for r in mt_raw["data"]["rows"]}
    ame_raw = json.loads(ame_path.read_text())
    ame_entries = (
        ame_raw
        if isinstance(ame_raw, list)
        else next(v for v in ame_raw.values() if isinstance(v, list))
    )

    kilo = mp.mpf(1000)
    threshold_mev = mp.mpf("0.01")
    transitions: list[dict] = []
    for e in ame_entries:
        z, n, a = int(e["Z"]), int(e["N"]), int(e["A"])
        if e.get("beta_decay_energy_estimated") or e.get("beta_decay_energy_keV") is None:
            continue
        q_exp = mp.mpf(str(e["beta_decay_energy_keV"])) / kilo
        if q_exp <= threshold_mev:
            continue
        par = mt_by_zn.get((z, n))
        dau = mt_by_zn.get((z + 1, n - 1))
        if par is None or dau is None:
            continue
        mk = "m_ruled_MeV" if par.get("m_ruled_MeV") else "m_symbolic_MeV"
        if not dau.get(mk):
            continue
        q_witness_ruled = mp.mpf(str(par[mk])) - mp.mpf(str(dau[mk])) - m_e
        q_witness_ruled_em = (
            mp.mpf(str(par["m_ruled_em_MeV"])) - mp.mpf(str(dau["m_ruled_em_MeV"])) - m_e
            if par.get("m_ruled_em_MeV") and dau.get("m_ruled_em_MeV")
            else None
        )
        transitions.append(
            {
                "Z": z,
                "N": n,
                "A": a,
                "element": str(e.get("element", "")),
                "q_exp_MeV": q_exp,
                "q_witness_ruled_MeV": q_witness_ruled,
                "q_witness_ruled_em_MeV": q_witness_ruled_em,
            }
        )
    return transitions, mt_by_zn


def main() -> int:
    os.environ["QOU_Q0_ANCHOR"] = "proton"
    dps = _configure_precision()

    q0 = q_at(dps)
    m_e = mp.mpf(str(M_E_MEV))
    m_p_pred, m_n_pred = proton_neutron_mass_mev()
    m_p = mp.mpf(str(m_p_pred))
    m_n = mp.mpf(str(m_n_pred))
    q_free_n = m_n - m_p - m_e

    alpha_cat = m_e * mp.mpf(8) * mp.catalan
    kappa_writhe = mp.mpf(2) * alpha_cat * mp.log(q0)

    # Arm B cell-radius scale c = (3/2)^{1/3} (#9866, owner ruling 2026-11-28)
    arm_b_c = (mp.mpf(3) / mp.mpf(2)) ** (mp.mpf(1) / mp.mpf(3))

    transitions, _ = _load_table_3_4b_transitions(m_e)
    composite = [t for t in transitions if t["A"] >= 2]

    benchmark_specs = [
        ("3H->3He", 1, 2),
        ("14C->14N", 6, 8),
        ("60Co->60Ni", 27, 33),
        ("90Sr->90Y", 38, 52),
        ("137Cs->137Ba", 55, 82),
        ("210Bi->210Po", 83, 127),
    ]

    # Precompute exact per-A Coulomb pair weights eps(A) at 80 dps so isobaric
    # steps -Z * eps(A) are evaluated once per A and cross-checked against
    # E_C(Z + 1, A) - E_C(Z, A).
    distinct_a = sorted(
        {t["A"] for t in composite} | {z + n for _, z, n in benchmark_specs}
    )
    eps_arm_a: dict[int, mp.mpf] = {}
    eps_arm_b: dict[int, mp.mpf] = {}
    eps_qhankel_c1: dict[int, mp.mpf] = {}
    a_hc = ce.alpha_em_hbar_c_mev_fm()
    sqrt_3_5 = mp.sqrt(mp.mpf(3) / mp.mpf(5))
    for A in distinct_a:
        r_rms_a = sqrt_3_5 * ce.nuclear_radius_fm(A)
        f_der = ce.shape_factor(A, "derived")
        ea = mp.mpf(2) * f_der * a_hc / r_rms_a
        eps_arm_a[A] = ea
        eps_arm_b[A] = ea / arm_b_c
        eps_qhankel_c1[A] = cic.pair_weight_mev(cic.r_rms_cal3_conditional(A))

    # Verify Lean algebraic identities across all 1,009 composite transitions + edge d's
    casimir_identity_ok = all(
        casimir_four(abs(d)) - casimir_four(abs(d - 2)) == 4 * tt_step_int(d)
        and casimir_four(abs(d)) == d * d + 2 * abs(d)
        for d in range(-12, 80)
    )
    all_composite_interior = all(t["Z"] >= 1 and t["N"] >= 2 for t in composite)
    casimir_on_corpus_ok = all(
        casimir_four(abs(t["N"] - t["Z"])) - casimir_four(abs((t["N"] - 2) - t["Z"]))
        == 4 * tt_step_int(t["N"] - t["Z"])
        for t in composite
    )
    binomial_step_ok = all(
        _comb_int(3 * t["A"], t["Z"] + 2 * t["N"] - 1) * (2 * t["Z"] + t["N"] + 1)
        == _comb_int(3 * t["A"], t["Z"] + 2 * t["N"]) * (t["Z"] + 2 * t["N"])
        for t in composite
    )
    max_markov_step_residual = max(
        abs(
            (
                mp.log(mp.mpf(_comb_int(3 * t["A"], t["Z"] + 2 * t["N"] - 1)))
                + mp.mpf((2 * t["Z"] + t["N"] + 1) - (t["Z"] + 2 * t["N"] - 1)) * mp.log(q0)
            )
            - (
                mp.log(mp.mpf(_comb_int(3 * t["A"], t["Z"] + 2 * t["N"])))
                + mp.mpf((2 * t["Z"] + t["N"]) - (t["Z"] + 2 * t["N"])) * mp.log(q0)
            )
            - (
                mp.log(mp.mpf(t["Z"] + 2 * t["N"]) / mp.mpf(2 * t["Z"] + t["N"] + 1))
                + mp.mpf(2) * mp.log(q0)
            )
        )
        for t in composite
    )

    max_coulomb_step_diff = mp.mpf(0)
    max_arm_cubic_residual = mp.mpf(0)
    max_witness_ruled_diff = mp.mpf(0)
    max_witness_ruled_em_diff = mp.mpf(0)

    for t in composite:
        z, n, A = t["Z"], t["N"], t["A"]
        step_direct = ce.coulomb_energy_mev(z + 1, A, "derived") - ce.coulomb_energy_mev(
            z, A, "derived"
        )
        step_pair = mp.mpf(z) * eps_arm_a[A]
        max_coulomb_step_diff = max(max_coulomb_step_diff, abs(step_direct - step_pair))

        da = -mp.mpf(z) * eps_arm_a[A]
        db = -mp.mpf(z) * eps_arm_b[A]
        max_arm_cubic_residual = max(
            max_arm_cubic_residual, abs(mp.mpf(3) * (db ** 3) - mp.mpf(2) * (da ** 3))
        )

        max_witness_ruled_diff = max(
            max_witness_ruled_diff, abs(q_free_n - t["q_witness_ruled_MeV"])
        )
        if t["q_witness_ruled_em_MeV"] is not None:
            q_em_analytic = q_free_n - mp.mpf(z) * eps_qhankel_c1[A]
            max_witness_ruled_em_diff = max(
                max_witness_ruled_em_diff,
                abs(q_em_analytic - t["q_witness_ruled_em_MeV"]),
            )

    def g2_step_mev(g2_arm: str, z: int, n: int, A: int) -> mp.mpf:
        if A < 2 or g2_arm == "G2_none_or_gg_e0":
            return mp.mpf(0)
        d = n - z
        denom = mp.mpf(strand_pair_denom(A))
        if g2_arm == "G2_writhe_chain":
            e = mp.mpf(A - 1)
            return kappa_writhe * e * mp.mpf(tt_step_int(d)) / denom
        if g2_arm == "G2_writhe_T3_valence":
            e = mp.mpf(3 * (A // 2))
            return kappa_writhe * e * mp.mpf(tt_step_int(d)) / denom
        if g2_arm == "G2_writhe_full_twist":
            return kappa_writhe * mp.mpf(tt_step_int(d))
        if g2_arm == "G2_weight_multiplicity":
            # Exact binomial step C(3A, n_d - 1) / C(3A, n_d) = (Z + 2N) / (2Z + N + 1)
            return alpha_cat * mp.log(mp.mpf(z + 2 * n) / mp.mpf(2 * z + n + 1))
        if g2_arm == "G2_block_twoRowDim":
            # Lowest two-row Hecke block dimension d(3A, k) = C(3A, k) - C(3A, k-1)
            n_str = 3 * A
            k_par = min(2 * z + n, z + 2 * n)
            k_dau = min(2 * (z + 1) + (n - 1), (z + 1) + 2 * (n - 1))
            d_par = _comb_int(n_str, k_par) - (
                _comb_int(n_str, k_par - 1) if k_par > 0 else 0
            )
            d_dau = _comb_int(n_str, k_dau) - (
                _comb_int(n_str, k_dau - 1) if k_dau > 0 else 0
            )
            return alpha_cat * mp.log(mp.mpf(d_dau) / mp.mpf(d_par))
        if g2_arm == "G2_markov_sector_raw":
            # Un-symmetrized Markov quantum-trace sector (9e6eb1efd6e):
            # ratio = ((Z + 2N) / (2Z + N + 1)) * q0^2 -> +kappa_writhe T_z-odd offset
            return (
                alpha_cat * mp.log(mp.mpf(z + 2 * n) / mp.mpf(2 * z + n + 1))
                + kappa_writhe
            )
        raise ValueError(f"unknown G2 arm: {g2_arm}")

    def g3_step_mev(g3_arm: str, z: int, A: int) -> mp.mpf:
        if A < 2 or g3_arm == "G3_none":
            return mp.mpf(0)
        if g3_arm == "G3_armA_c_eq_1":
            return -mp.mpf(z) * eps_arm_a[A]
        if g3_arm == "G3_armB_c3_eq_3_over_2":
            return -mp.mpf(z) * eps_arm_b[A]
        if g3_arm == "G3_qhankel_allA_c1":
            return -mp.mpf(z) * eps_qhankel_c1[A]
        raise ValueError(f"unknown G3 arm: {g3_arm}")

    g2_arms = [
        "G2_none_or_gg_e0",
        "G2_writhe_chain",
        "G2_writhe_T3_valence",
        "G2_weight_multiplicity",
        "G2_block_twoRowDim",
        "G2_markov_sector_raw",
        "G2_writhe_full_twist",
    ]
    g3_arms = [
        "G3_none",
        "G3_armA_c_eq_1",
        "G3_armB_c3_eq_3_over_2",
        "G3_qhankel_allA_c1",
    ]

    band_defs = [
        ("A_2_16", lambda a: 2 <= a <= 16),
        ("A_17_56", lambda a: 17 <= a <= 56),
        ("A_57_150", lambda a: 57 <= a <= 150),
        ("A_ge_151", lambda a: a >= 151),
    ]

    matrix_results: dict[str, dict] = {}
    print("=" * 108)
    print(
        "COMPOSITE BETA-MINUS ACCURACY MATRIX — 80-dps Proton Pin (1,009 Composite + 1 Free n)"
    )
    print(f"  q0 (proton)   = {mp.nstr(q0, 24)}")
    print(f"  Q_n baseline  = {mp.nstr(q_free_n, 15)} MeV  (flat ruled baseline)")
    print(f"  alpha_cat     = {mp.nstr(alpha_cat, 15)} MeV,  kappa = 2*alpha*ln(q0) = {mp.nstr(kappa_writhe, 15)} MeV")
    print(f"  Arm B c       = (3/2)^(1/3) = {mp.nstr(arm_b_c, 18)}")
    print("=" * 108)
    print(
        f"  {'G2 Arm':<24} {'G3 Coulomb Arm':<24} {'Exo (1009)':>12} "
        f"{'Mean |dQ|/Q':>13} {'Med |dQ|/Q':>12} {'Med Q_pred':>12}"
    )
    print("  " + "-" * 102)

    for g2 in g2_arms:
        for g3 in g3_arms:
            if g3 == "G3_qhankel_allA_c1" and g2 != "G2_none_or_gg_e0":
                continue
            key = f"{g2}__{g3}"
            eval_all: list[dict] = []
            for t in transitions:
                z, n, A = t["Z"], t["N"], t["A"]
                q_base = t["q_witness_ruled_MeV"] if A == 1 else q_free_n
                dq = g2_step_mev(g2, z, n, A) + g3_step_mev(g3, z, A)
                q_pred = q_base + dq
                rel_err = abs(q_pred - t["q_exp_MeV"]) / t["q_exp_MeV"]
                eval_all.append(
                    {
                        "Z": z,
                        "N": n,
                        "A": A,
                        "q_pred": q_pred,
                        "q_exp": t["q_exp_MeV"],
                        "rel_err": rel_err,
                    }
                )
            eval_comp = [r for r in eval_all if r["A"] >= 2]
            comp_stats = _band_stats(eval_comp)
            all_stats = _band_stats(eval_all)
            bands_out = {
                b_name: _band_stats([r for r in eval_comp if b_fn(r["A"])])
                for b_name, b_fn in band_defs
            }
            matrix_results[key] = {
                "g2_arm": g2,
                "g3_arm": g3,
                "composite_1009": comp_stats,
                "all_1010": all_stats,
                "bands": bands_out,
            }
            print(
                f"  {g2:<24} {g3:<24} {comp_stats['exothermic_ratio']:>12} "
                f"{mp.nstr(mp.mpf(comp_stats['mean_rel_err_pct']), 5) + '%':>13} "
                f"{mp.nstr(mp.mpf(comp_stats['median_rel_err_pct']), 5) + '%':>12} "
                f"{mp.nstr(mp.mpf(comp_stats['median_Q_pred_MeV']), 5) + ' MeV':>12}"
            )

    # Representative benchmark nuclides (3H mirror d=1, 14C, 60Co, 90Sr, 137Cs, 210Bi)
    ame_q_map = {(t["Z"], t["N"]): t["q_exp_MeV"] for t in composite}
    benchmark_rows: dict[str, dict] = {}
    for label, z, n in benchmark_specs:
        A = z + n
        benchmark_rows[label] = {
            "Z": z,
            "N": n,
            "A": A,
            "d_neutron_excess": n - z,
            "ttStepInt": tt_step_int(n - z),
            "Q_AME_MeV": fmt(ame_q_map[(z, n)]) if (z, n) in ame_q_map else None,
            "Q_ruled_flat_MeV": fmt(q_free_n),
            "dB_G2_chain_MeV": fmt(g2_step_mev("G2_writhe_chain", z, n, A)),
            "dB_G2_T3_valence_MeV": fmt(g2_step_mev("G2_writhe_T3_valence", z, n, A)),
            "dB_G2_weight_mult_MeV": fmt(g2_step_mev("G2_weight_multiplicity", z, n, A)),
            "dB_G3_armA_c1_MeV": fmt(g3_step_mev("G3_armA_c_eq_1", z, A)),
            "dB_G3_armB_c3_3_2_MeV": fmt(g3_step_mev("G3_armB_c3_eq_3_over_2", z, A)),
        }

    baseline_cell = matrix_results["G2_none_or_gg_e0__G3_none"]
    baseline_med_all = mp.mpf(baseline_cell["all_1010"]["median_rel_err_pct"])

    wb = WitnessBuilder("composite-beta-writhe-coulomb-accuracy", engine="mpmath")
    wb.set_description(
        "Pre-registered 80-dps proton-pinned benchmark of the derived G2 isospin step "
        "(IsospinTwistWrithe #9747 writhe arms e = 0, A-1, 3 floor(A/2), 3A(3A-1) and "
        "IsospinWeightMultiplicity down-quark weight count C(3A, Z+2N)) combined with the "
        "G3 Coulomb step (two labelled #9866 cell-radius arms c = 1 and c^3 = 3/2, derived "
        "#9699 shape factor) across all 1,009 composite AME2020 beta-minus transitions "
        "(ACCURACY.md Table 3.4b). Lean companion: QOU/Nuclear/IsobaricBetaWritheCoulombStep.lean. "
        "Zero free parameters; AME2020 comparison only; no arm selected."
    )
    wb.add_parameter("compute_dps", dps)
    wb.add_parameter("q0_anchor", "proton")
    wb.add_parameter("q0", fmt(q0))
    wb.add_parameter("lean_module", "QOU/Nuclear/IsobaricBetaWritheCoulombStep.lean")
    wb.add_parameter("n_composite_transitions", len(composite))
    wb.add_parameter("n_total_transitions", len(transitions))

    wb.add_data("q0_proton", fmt(q0))
    wb.add_data("m_e_MeV", fmt(m_e))
    wb.add_data("m_p_pred_MeV", fmt(m_p))
    wb.add_data("m_n_pred_MeV", fmt(m_n))
    wb.add_data("Q_free_neutron_baseline_MeV", fmt(q_free_n))
    wb.add_data("alpha_catalan_MeV", fmt(alpha_cat))
    wb.add_data("kappa_writhe_MeV", fmt(kappa_writhe))
    wb.add_data("coulomb_armB_c_factor", fmt(arm_b_c))
    wb.add_data("max_coulomb_step_vs_pair_formula_MeV", fmt(max_coulomb_step_diff))
    wb.add_data("max_armA_armB_cubic_residual_MeV3", fmt(max_arm_cubic_residual))
    wb.add_data("max_witness_m_ruled_diff_MeV", fmt(max_witness_ruled_diff))
    wb.add_data("max_witness_m_ruled_em_diff_MeV", fmt(max_witness_ruled_em_diff))
    wb.add_data("matrix", matrix_results)
    wb.add_data("benchmarks", benchmark_rows)
    wb.add_data(
        "structural_diagnosis",
        {
            "gamma_gamma_word_writhe": (
                "Identically 0 (IsospinTwistWrithe bb1d29c6df6), so the braid-channel "
                "log-determinant T(T+1) step vanishes on ruled gamma-gamma words."
            ),
            "mirror_doublet_d_eq_1": (
                "ttStepInt(1) = 0 and C(3A, n_d - 1) = C(3A, n_d) at N_parent = Z + 1 "
                "(e.g. 3H -> 3He), so every mirror beta-minus transition shifts purely by "
                "the Coulomb displacement -Z * eps_c(A)."
            ),
            "scale_mismatch_between_G2_and_G3": (
                "G2 writhe (chain e=A-1: <= 2*kappa/(9A) ~ 0.17/A MeV) and weight-multiplicity "
                "(~(alpha/6)(N-Z)^2/A ~ 0.624*(N-Z)^2/A MeV) sit at the 1D proxy scale "
                "alpha = 8*G*m_e (~37x below classical ~23 MeV symmetry energy), whereas G3 "
                "Coulomb (-Z*eps_c(A)) carries the full CAL-3 electromagnetic scale. Wiring G3 "
                "into mass_table_comprehensive without closing the strong/symmetry scale (G5) "
                "drives heavy beta-minus transitions endothermic; G2 weight-multiplicity alone "
                "keeps 1,009/1,009 exothermic and lowers median |dQ|/Q from 92.69% to 84.26%."
            ),
        },
    )

    assertions = [
        (
            "composite_transition_count_is_1009",
            len(composite) == 1009 and len(transitions) == 1010 and all_composite_interior,
            f"Table 3.4b filter selects 1,009 interior composite transitions (Z>=1, N>=2) + 1 free neutron = 1,010.",
        ),
        (
            "ruled_baseline_reproduces_scorecard_table_3_4b",
            baseline_cell["composite_1009"]["exothermic_count"] == 1009
            and max_witness_ruled_diff < mp.mpf("2e-6")
            and abs(baseline_med_all - mp.mpf("92.685")) < mp.mpf("0.05"),
            f"Reproduces mass-table-comprehensive m_ruled_MeV to {mp.nstr(max_witness_ruled_diff, 4)} MeV (< 2e-6 6-dp rounding) and Table 3.4b 92.7% median.",
        ),
        (
            "qhankel_c1_reproduces_mass_table_m_ruled_em_to_6dp",
            max_witness_ruled_em_diff < mp.mpf("2e-6"),
            f"Analytic Coulomb step -Z*eps_qhankel(A) matches mass-table-comprehensive m_ruled_em_MeV across all 1,009 rows to {mp.nstr(max_witness_ruled_em_diff, 4)} MeV.",
        ),
        (
            "lean_casimir4_step_and_wigner_cusp_verified",
            casimir_identity_ok and casimir_on_corpus_ok,
            "casimirFour(|d|) - casimirFour(|d-2|) == 4 * ttStepInt(d) verified across d in [-12, 79] and all 1,009 composite rows.",
        ),
        (
            "lean_down_quark_and_markov_sector_step_verified",
            binomial_step_ok and max_markov_step_residual < mp.mpf("1e-65"),
            f"Exact C(3A, Z+2N-1)*(2Z+N+1) == C(3A, Z+2N)*(Z+2N) and markovSectorWeight q^2 step residual {mp.nstr(max_markov_step_residual, 4)} (< 1e-65) across all 1,009 rows.",
        ),
        (
            "lean_coulomb_armA_armB_cubic_verified_80dps",
            max_coulomb_step_diff < mp.mpf("1e-65")
            and max_arm_cubic_residual < mp.mpf("1e-65"),
            f"coulombBinding_isobaric_step residual {mp.nstr(max_coulomb_step_diff, 4)} MeV and 3*(dB_B)^3 - 2*(dB_A)^3 residual {mp.nstr(max_arm_cubic_residual, 4)} MeV^3 (< 1e-65 at 80 dps).",
        ),
    ]

    all_ok = True
    print()
    for name, ok, detail in assertions:
        all_ok = all_ok and bool(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        wb.add_assertion(
            name=name,
            computed="PASS" if ok else "FAIL",
            expected="PASS",
            tolerance="0",
            source=detail,
        )

    out_path = wb.save()
    print(f"\n  witness -> {out_path}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
