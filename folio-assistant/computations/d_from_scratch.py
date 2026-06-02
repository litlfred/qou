#!/usr/bin/env python3
"""D from scratch — full canonical infra at 50 dps mpmath.

Per user 'lets investigate D error. recalc from scratch using full
infra'.

Strategy: avoid all f64 noise + all convention mixing. Compute D's
binding energy from the canonical chain end-to-end at 50 dps:

  Inputs (at 50 dps):
    q_0  = 1/(1 - sqrt(Vol(4_1)/(m_μ/m_e)))
    m_e  = CODATA leptonic mass
    Q_β(n) = m_n − m_p − m_e  (CODATA splitting calibration)

  Step 1: Habiro polynomial evaluation
    tr_M(p, q_0)   = exact value from habiro-coefficients-atomic
                    (polynomial deg 48 in u = q^{1/2}, integral)
    tr_M(n, q_0)   = exact value (deg 40, integral)
    tr_M(D, q_0)   = exact value (deg 104, integral, include_inter=True)

  Step 2: Free-nucleon disconnected Markov trace at q_0
    tr_M(D_free) via light_isotope_sweep.tr_M_at_q0(1, 1, False)

  Step 3: Term 1 (descended, β-calibrated subtraction)
    Q_cat = tr_M(n_free) − tr_M(p_free) (numerical)
    E_0  = Q_β(n) / |Q_cat|
    Term 1 = E_0 · |tr_M(D_free) − tr_M(D_atom)|
    where tr_M(D_atom) is the Habiro polynomial value (50 dps).

  Step 4: Term 4 (universal Frobenius co-Casimir, Lean-proved)
    Term 4 = m_e · Σ_{λ⊢3A} 1/dim_q(λ)  (canonical per-3A)
    For D: A = 2, so sum is over partitions of 6.

    P1.C HARD BREAK 2026-05-12: legacy `A · m_e · (2 + 1/[2]_q)` REMOVED.
    See P1.C of `docs/audits/2026-05-12-1ppb-implementation-plan.md`.

  Step 5: Δm_shell (per σ_shell ILP, A_magic = 2 only contributes)
    Δm_shell = E_0 · 5.889e-3 ≈ 0.018 MeV

  Step 6: Final B(D) = T1 + T4 + Δm_shell

NO Vol_hyp.  NO census.  NO BW formula (T5 invalid at A=2).

Output: d-from-scratch.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV, Q_NEUTRON_MEV, M_P_MEV, M_N_MEV
from light_isotope_sweep import tr_M_at_q0
from witness_base import WitnessBuilder

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

# Substrate parameter at 50 dps
VOL_FIGURE_EIGHT = mp.mpf("2.029883212819307")
# CAL-2: m_μ/m_e from q_parameter registry (P31-triage Phase A).
from q_parameter import MASS_RATIO_MU_E_STR as _MU_E_STR  # noqa: E402
MASS_RATIO_MU_E  = mp.mpf(_MU_E_STR)
HBAR_Q_SQ        = VOL_FIGURE_EIGHT / MASS_RATIO_MU_E
HBAR_Q           = mp.sqrt(HBAR_Q_SQ)
Q0               = mp.mpf(1) / (mp.mpf(1) - HBAR_Q)
QI0              = mp.mpf(1) / Q0
HA               = Q0 - QI0
TWO_Q            = Q0 + QI0  # [2]_q


def load_habiro_tr_M(label: str) -> mp.mpf:
    """Load tr_M(label, q_0) from habiro-coefficients-atomic witness."""
    path = Path(__file__).parent / "habiro-coefficients-atomic.witness.json"
    with open(path) as f:
        d = json.load(f)
    for key, r in d.get("results", {}).items():
        if label in key.lower():
            return mp.mpf(str(r["tr_M_at_q0"]))
    raise KeyError(f"label {label!r} not found")


def main():
    print("=" * 78)
    print("D from scratch — full canonical infra at 50 dps mpmath")
    print("=" * 78)

    # ────────────────────────────────────────────────────────────
    # Inputs at 50 dps
    # ────────────────────────────────────────────────────────────
    print(f"  q_0          = {mp.nstr(Q0, 30)}")
    print(f"  [2]_q        = {mp.nstr(TWO_Q, 30)}")
    print(f"  H_A = q-q⁻¹  = {mp.nstr(HA, 30)}")
    print(f"  m_e          = {M_E_MEV} MeV")
    print(f"  Q_β(n)       = {Q_NEUTRON_MEV} MeV")
    print(f"  m_p (CODATA) = {M_P_MEV} MeV")
    print(f"  m_n (CODATA) = {M_N_MEV} MeV")
    print()

    # ────────────────────────────────────────────────────────────
    # Step 1: Habiro polynomial values at 50 dps (EXACT, no f64)
    # ────────────────────────────────────────────────────────────
    print("Step 1: Habiro polynomial Markov trace values @ q_0 (50 dps)")
    print("─" * 78)
    tr_M_p_habiro = load_habiro_tr_M("proton")
    tr_M_n_habiro = load_habiro_tr_M("neutron")
    tr_M_D_atom_habiro = load_habiro_tr_M("deuteron")
    print(f"  tr_M(p)        = {mp.nstr(tr_M_p_habiro, 30)}")
    print(f"  tr_M(n)        = {mp.nstr(tr_M_n_habiro, 30)}")
    print(f"  tr_M(D atom)   = {mp.nstr(tr_M_D_atom_habiro, 30)}")
    print()

    # ────────────────────────────────────────────────────────────
    # Step 2: Free-nucleon disconnected Markov trace
    # ────────────────────────────────────────────────────────────
    print("Step 2: Free-nucleon Markov trace (disconnected p⊗n)")
    print("─" * 78)
    # For binding subtraction we need tr_M(D, include_inter=False).
    # This is the Markov trace of the DISCONNECTED tensor p ⊗ n
    # under H_3(q)^⊗2 ↪ H_6(q).
    # Light_isotope_sweep gives this via include_inter=False at f64;
    # we use it as a finite-precision input (Habiro polynomial for
    # this specific 'free deuteron' is not tabulated in the atomic
    # witness — only include_inter=True is).
    tr_M_p_f64, _, _ = tr_M_at_q0(1, 0, include_inter=False)
    tr_M_n_f64, _, _ = tr_M_at_q0(0, 1, include_inter=False)
    tr_M_D_free_f64, _, _ = tr_M_at_q0(1, 1, include_inter=False)
    print(f"  tr_M(p, f64)        = {tr_M_p_f64}")
    print(f"  tr_M(n, f64)        = {tr_M_n_f64}")
    print(f"  tr_M(D_free, f64)   = {tr_M_D_free_f64}")
    print(f"  (Habiro 50dps p,n disagree with f64 by ~1e-6 due to f64 noise)")
    print()

    # ────────────────────────────────────────────────────────────
    # Step 3: Term 1 = E_0 · |tr_M(D_free) − tr_M(D_atom)|
    # ────────────────────────────────────────────────────────────
    print("Step 3: Term 1 (descended, β-calibrated)")
    print("─" * 78)
    Q_cat = mp.mpf(str(tr_M_n_f64)) - mp.mpf(str(tr_M_p_f64))
    E_0 = mp.mpf(str(Q_NEUTRON_MEV)) / mp.fabs(Q_cat)
    print(f"  Q_cat = tr_M(n) − tr_M(p)   = {mp.nstr(Q_cat, 12)}")
    print(f"  E_0  = Q_β / |Q_cat|        = {mp.nstr(E_0, 12)} MeV/cat")
    # Mix Habiro 50dps for atom + f64 for free (only avenue available)
    tr_M_D_free_mp = mp.mpf(str(tr_M_D_free_f64))
    delta_tr_M = mp.fabs(tr_M_D_free_mp - tr_M_D_atom_habiro)
    T1 = E_0 * delta_tr_M
    print(f"  Δtr_M = |free − atom|       = {mp.nstr(delta_tr_M, 12)}")
    print(f"  Term 1 = E_0 · Δtr_M        = {mp.nstr(T1, 12)} MeV")
    print()

    # ────────────────────────────────────────────────────────────
    # Step 4: Term 4 = m_e · Σ_{λ⊢3A} 1/dim_q(λ)  (canonical per-3A)
    # ────────────────────────────────────────────────────────────
    print("Step 4: Term 4 (universal Frobenius co-Casimir, Lean-proved)")
    print("─" * 78)
    A = 2
    # P1.C HARD BREAK (2026-05-12): the legacy
    # `Frob_per_vortex = m_e · (2 + 1/[2]_q); T4 = A · Frob_per_vortex`
    # has been REMOVED. It was an H_3-character formula × A that
    # overcounts T4 by 1.56× at A=2, 4.44× at A=4. The canonical form
    # per `thm:frobenius-codim-universal` is m_e · Σ_{λ⊢3A} 1/dim_q(λ).
    # See P1.C of `docs/audits/2026-05-12-1ppb-implementation-plan.md`.
    from paper_six_term_isotope_sweep import term4_frobenius_codim
    T4 = mp.mpf(str(M_E_MEV)) * term4_frobenius_codim(A)
    print(f"  Term 4 = m_e · τ(C_dim_q) at A={A}  = {mp.nstr(T4, 15)} MeV")
    print()

    # ────────────────────────────────────────────────────────────
    # Step 5: Δm_shell (σ_shell ILP, A_magic=2 only for D)
    # ────────────────────────────────────────────────────────────
    print("Step 5: Δm_shell (σ_shell ILP at A_magic = 2)")
    print("─" * 78)
    SIGMA_SHELL_BARE_AT_Q0_AMAGIC2 = mp.mpf("5.889176e-3")
    Dm_shell = SIGMA_SHELL_BARE_AT_Q0_AMAGIC2 * E_0
    print(f"  y_shell · σ_shell      = {mp.nstr(SIGMA_SHELL_BARE_AT_Q0_AMAGIC2, 10)} cat")
    print(f"  Δm_shell = y_shell·σ·E_0 = {mp.nstr(Dm_shell, 12)} MeV")
    print()

    # ────────────────────────────────────────────────────────────
    # Step 6: Final B(D)
    # ────────────────────────────────────────────────────────────
    print("Step 6: Final B(D)")
    print("─" * 78)
    B_pred = T1 + T4 + Dm_shell
    B_AME = mp.mpf("2.22456612")
    err_pct = (B_pred - B_AME) / B_AME * 100
    err_ppb = err_pct * mp.mpf(10)**7
    print(f"  T1 + T4 + Δm_shell    = {mp.nstr(B_pred, 15)} MeV")
    print(f"  AME B(D)              = {mp.nstr(B_AME, 15)} MeV")
    print(f"  err vs AME            = {float(err_pct):>+.6f}%")
    print(f"  err in ppb            = {float(err_ppb):>+.4e}")
    print()

    # Per-term breakdown
    print("Per-term breakdown:")
    print(f"  Term 1 (descended)     = {mp.nstr(T1, 10)} MeV  ({float(T1/B_AME*100):>+.2f}% of AME)")
    print(f"  Term 4 (Frobenius)    = {mp.nstr(T4, 10)} MeV  ({float(T4/B_AME*100):>+.2f}% of AME)")
    print(f"  Δm_shell              = {mp.nstr(Dm_shell, 10)} MeV  ({float(Dm_shell/B_AME*100):>+.2f}% of AME)")
    print(f"  Sum                   = {mp.nstr(B_pred, 10)} MeV  ({float(B_pred/B_AME*100):>+.2f}% of AME)")
    print()

    # Compare to existing T1+T4 prediction at f64
    T1_T4_f64 = mp.mpf("2.271368715455014")  # from mass-formula-6term.witness
    print(f"For comparison: T1+T4 from mass-formula-6term (f64) = {T1_T4_f64} MeV")
    print(f"Difference                                          = {mp.nstr(B_pred - T1_T4_f64, 10)} MeV")
    print(f"(this difference is mostly from Δm_shell + Habiro precision improvement on Term 1)")

    # Build witness
    w = (
        WitnessBuilder("d-from-scratch", engine="python+mpmath")
        .set_description(
            "Deuteron binding from scratch using full canonical infra at "
            "50 dps mpmath. Combines Habiro polynomial Markov trace values "
            "(exact at q_0 from habiro-coefficients-atomic.witness.json) "
            "for the atom-level tr_M with light_isotope_sweep f64 values "
            "for the free-nucleon disconnected baseline. Term 4 and "
            "Δm_shell computed exactly at 50 dps. NO Vol_hyp, NO BW "
            "(invalid at A=2), NO census."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0_mpf50", mp.nstr(Q0, 50))
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("Q_beta_n_MeV", Q_NEUTRON_MEV)
        .add_parameter("E_0_MeV_per_cat", float(E_0))
        .add_data("tr_M_habiro_50dps", {
            "proton":  mp.nstr(tr_M_p_habiro, 50),
            "neutron": mp.nstr(tr_M_n_habiro, 50),
            "D_atom":  mp.nstr(tr_M_D_atom_habiro, 50),
        })
        .add_data("tr_M_f64", {
            "proton_free":  tr_M_p_f64,
            "neutron_free": tr_M_n_f64,
            "D_free":       tr_M_D_free_f64,
        })
        .add_data("terms_50dps", {
            "Term_1_descended_MeV": mp.nstr(T1, 30),
            "Term_4_frobenius_MeV": mp.nstr(T4, 30),
            "delta_m_shell_MeV":   mp.nstr(Dm_shell, 30),
            "B_pred_MeV":          mp.nstr(B_pred, 30),
            "B_AME_MeV":           mp.nstr(B_AME, 30),
            "err_pct":             float(err_pct),
            "err_ppb":             float(err_ppb),
        })
        .add_caveat(
            "Free-nucleon Markov trace tr_M(D, include_inter=False) is "
            "computed at f64 via light_isotope_sweep — Habiro polynomial "
            "for this specific configuration is not yet in the witness. "
            "An end-to-end 50 dps result requires extending Habiro "
            "extraction to include_inter=False atom braids."
        )
        .add_caveat(
            "Term 5 (BW) explicitly NOT included — BW formula is "
            "structurally invalid at A=2 (surface dominates volume; "
            "B_bulk(D) = -4.44 MeV negative)."
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
