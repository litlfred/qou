#!/usr/bin/env python3
"""
probe_trace_convention_production_impact.py — what would switching the
Borromean pipeline trace from convention D (TL/Jones, current) to
convention C (canonical Jones–Markov = Wenzl z-trace) do to production?

Input facts (Lean-proved + probe-verified, PR #3261):
  * D ≠ C exactly at β_Bor; D − C ≈ 1.9554e-4 at q₀ (relative ≈ 1.958e-4).
  * Production `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³` uses the D closed form
    (`m_p_substrate_identity_50dps.trM_borromean`).

Scenarios quantified here (exact mpmath, 50 dps; NO wiring change):

  S1 — MUON anchor (canonical 3-CAL): q₀ unchanged (F_Bor-independent);
       the m_p PREDICTION shifts by 2·m_μ·ΔF_Bor.
  S2 — PROTON anchor (live precision layer): q₀ re-pins by solving
       m_p(q₀; F_Bor^C) = m_p_CODATA; all q₀-downstream predictions
       shift — quantified for m_μ (the μ–p tension) and Q_β.
  S3 — Binding tower: τ^C vs τ^D per-nucleon relative shift (context:
       the 9b gap is 2.3×, so this is noise there).

Output: probe-trace-convention-production-impact.witness.json
Decision package: docs/audits/2026-07-03-trace-convention-decision-package.md
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from knot_volumes import VOL_4_1_MPF  # noqa: E402
from m_p_substrate_identity_50dps import F_Bor, qfact_three  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

M_P_CODATA = "938.27208816"    # MeV (CODATA 2018, as used by the q0 pin)
M_MU_CODATA = "105.6583755"    # MeV


def trC_borromean(q):
    """Convention C (canonical Jones–Markov = Wenzl z-trace) at β_Bor,
    from the Lean-proved closed form in BorromeanTraceConventionSplit
    (rational function in t = √q)."""
    t = mp.sqrt(q)
    num = (1 - t - t**2 + t**3 - 4*t**4 + 2*t**5 + 4*t**6 - t**7 + 6*t**8
           - t**9 - 6*t**10 - t**11 - 4*t**12 + 2*t**13 + 4*t**14 + t**15
           + t**16 - t**17 - t**18)
    return num / t**9


def F_Bor_C(q):
    """F_Bor with the convention-C trace substituted."""
    return abs(trC_borromean(q)) * qfact_three(q) / q**3


def m_p_pure_q(q, m_e, fbor_fn):
    """Pure-q proton mass: m_p = 2·(m_e·Vol(4₁)/ℏ_q²·F_Bor − 6·m_e)."""
    hbar_q_sq = ((q - 1) / q) ** 2
    return 2 * (m_e * VOL_4_1_MPF / hbar_q_sq * fbor_fn(q) - 6 * m_e)


def main() -> int:
    q0 = mp.mpf(Q_50_DIGIT_STR)
    m_e = mp.mpf(M_E_MEV)
    m_p_codata = mp.mpf(M_P_CODATA)
    m_mu_codata = mp.mpf(M_MU_CODATA)

    tau_D = F_Bor(q0) * q0**3 / qfact_three(q0)
    tau_C = abs(trC_borromean(q0))
    rel = (tau_D - tau_C) / tau_C

    # S1 — muon anchor: q0 fixed, m_p prediction shifts
    mp_D = m_p_pure_q(q0, m_e, F_Bor)
    mp_C = m_p_pure_q(q0, m_e, F_Bor_C)
    d_mp = mp_C - mp_D
    d_mp_ppm = d_mp / mp_D * mp.mpf(10)**6

    # S2 — proton anchor: re-pin q0 under BOTH conventions so the
    # m_mu-tension comparison is internal (same anchor on both sides).
    q0_Dp = mp.findroot(lambda q: m_p_pure_q(q, m_e, F_Bor) - m_p_codata, q0)
    q0_C = mp.findroot(lambda q: m_p_pure_q(q, m_e, F_Bor_C) - m_p_codata, q0)
    dq0 = q0_C - q0

    def m_mu_pred(q):
        return m_e * VOL_4_1_MPF / (((q - 1) / q) ** 2)

    # NOTE: Q_50_DIGIT_STR (identical in q_parameter AND
    # qou_substrate.constants — checked) is the MUON-pinned canonical
    # string: m_mu at it is near-tautological (~1.4 ppb). The proton
    # pin lives in the q_at() SOLVER, not in this constant. Both
    # proton-anchored baselines are therefore computed explicitly.
    mmu_at_q0 = m_mu_pred(q0)      # at the muon-pinned canonical q0
    mmu_Dp = m_mu_pred(q0_Dp)      # proton re-pin, convention D (status quo)
    mmu_C = m_mu_pred(q0_C)        # proton re-pin, convention C
    tension_D_ppb = (mmu_at_q0 - m_mu_codata) / m_mu_codata * mp.mpf(10)**9
    tension_Dp_ppb = (mmu_Dp - m_mu_codata) / m_mu_codata * mp.mpf(10)**9
    tension_C_ppb = (mmu_C - m_mu_codata) / m_mu_codata * mp.mpf(10)**9
    ratio_C_over_Dp = tension_C_ppb / tension_Dp_ppb

    def q_beta(q):
        return m_e * abs(q**2 - 2*q - 1) * (q + 1) / (2 * q**3)

    qb_D, qb_C = q_beta(q0), q_beta(q0_C)

    print(f"tau_D = {mp.nstr(tau_D, 20)}   tau_C = {mp.nstr(tau_C, 20)}")
    print(f"rel gap (D-C)/C          = {mp.nstr(rel, 8)}")
    print(f"S1 muon-anchor:  m_p(D) = {mp.nstr(mp_D, 15)}  m_p(C) = {mp.nstr(mp_C, 15)}")
    print(f"                 shift  = {mp.nstr(d_mp, 8)} MeV = {mp.nstr(d_mp_ppm, 6)} ppm")
    print(f"S2 proton-anchor re-pin: q0  = {mp.nstr(q0, 20)}")
    print(f"                         q0' = {mp.nstr(q0_C, 20)}  (dq0 = {mp.nstr(dq0, 8)})")
    print(f"   m_mu pred:  muon q0     {mp.nstr(mmu_at_q0, 15)} ({mp.nstr(tension_D_ppb, 6)} ppb)")
    print(f"               D proton-pin {mp.nstr(mmu_Dp, 15)} ({mp.nstr(tension_Dp_ppb, 6)} ppb)")
    print(f"               C proton-pin {mp.nstr(mmu_C, 15)} ({mp.nstr(tension_C_ppb, 6)} ppb)")
    print(f"               C/D same-anchor tension ratio = {mp.nstr(ratio_C_over_Dp, 6)}x")
    print(f"   Q_beta:     D-pin {mp.nstr(qb_D, 10)}  C-pin {mp.nstr(qb_C, 10)} MeV")
    print(f"S3 binding tower: per-nucleon tau ratio shift = {mp.nstr(rel, 6)} "
          f"(A=16 compound ~ {mp.nstr(16*rel, 6)}) — noise vs the 2.3x 9b gap")

    wb = WitnessBuilder("probe-trace-convention-production-impact",
                        engine="mpmath", output_dir=HERE)
    wb.set_description(
        "Impact of switching the Borromean pipeline from trace convention "
        "D (TL/Jones, production) to C (canonical Jones-Markov / Wenzl "
        "z-trace): muon-anchor m_p shift, proton-anchor q0 re-pin + "
        "m_mu/Q_beta prediction shifts, binding-tower noise floor. "
        "Decision package input; no production wiring changed.")
    wb.add_data("tau_D_at_q0", mp.nstr(tau_D, 50))
    wb.add_data("tau_C_at_q0", mp.nstr(tau_C, 50))
    wb.add_data("rel_gap_D_minus_C_over_C", mp.nstr(rel, 15))
    wb.add_data("S1_muon_anchor_m_p_shift_MeV", mp.nstr(d_mp, 15))
    wb.add_data("S1_muon_anchor_m_p_shift_ppm", mp.nstr(d_mp_ppm, 10))
    wb.add_data("S2_q0_current_muon_pinned", mp.nstr(q0, 50))
    wb.add_data("S2_q0_C_repin", mp.nstr(q0_C, 50))
    wb.add_data("S2_m_mu_tension_at_muon_q0_ppb", mp.nstr(tension_D_ppb, 10))
    wb.add_data("S2_m_mu_tension_D_proton_repin_ppb", mp.nstr(tension_Dp_ppb, 10))
    wb.add_data("S2_m_mu_tension_C_proton_repin_ppb", mp.nstr(tension_C_ppb, 10))
    wb.add_data("S2_tension_ratio_C_over_D_same_anchor", mp.nstr(ratio_C_over_Dp, 10))
    wb.add_data("S2_Q_beta_at_current_q0_MeV", mp.nstr(qb_D, 15))
    wb.add_data("S2_Q_beta_C_repin_MeV", mp.nstr(qb_C, 15))
    wb.add_assertion(
        "rel_gap_matches_registry", float(rel), 1.958e-4, tolerance=2e-6,
        source="the D-C gap at q0 must reproduce the registry figure")
    wb.add_assertion(
        "proton_repin_solves", float(m_p_pure_q(q0_C, m_e, F_Bor_C) - m_p_codata),
        0.0, tolerance=1e-30,
        source="the C-convention re-pinned q0 reproduces m_p CODATA")
    path = wb.save()
    print(f"witness: {path}")
    ok = abs(rel - mp.mpf("1.958e-4")) < mp.mpf("2e-6") and \
        abs(m_p_pure_q(q0_C, m_e, F_Bor_C) - m_p_codata) < mp.mpf("1e-30")
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
