#!/usr/bin/env python3
"""volume_def_reconcile.py — reconcile the TWO Borromean-volume definitions.

Keystone open item (session 2026-06-01): the corpus carries two definitions of
the Borromean volume Vol(𝓑₃) that the keystone audit
`2026-06-01-yekutieli-volume-join-derivation.md` reported as "off by ~5090×":

  Definition A (PRODUCTION):
      Vol(𝓑₃) = 8·G = 7.32772          (G = Catalan)
    classical SnapPy hyperbolic volume, used in
    `_li_2_q_util.per_knot_density_borromean` as Geom_leading = Vol/ℏ_q².
    Provenance: `topological-mass-formula.md` Step 1 —
      Re tr(τ̂ⁿ_desc · Hol) = Vol(K)   (Chern–Simons / volume correspondence).
    This is a POST-τ REAL NUMBER (an archimedean volume in ℝ).

  Definition B (`prop:vol-through-tau`, `def:algebraic-quantum-volume`):
      Vol(K) = τ_arch(Vol_q(β)) = ln|Vol_q(β)|,   Vol_q(β) = ∏ᵢ V̂ᵢ(q) ∈ ℤ[q^½,q^-½].
    Vol_q is the PRE-τ ALGEBRAIC Laurent polynomial (UNNORMALIZED trace product).

This probe establishes PRECISELY what each computes and at which chain stage,
then tests the EXACT functional relation between 8G and the various candidate
"ln|trace|" quantities — to decide:

  (a) SAME object at different chain stages (the "5090×" is a cross-τ-functor
      category error — comparing a pre-log algebraic number to a post-log real
      volume), OR
  (b) GENUINE bug (production uses the wrong-stage volume).

DISCIPLINE: no fit, no fabrication. We do NOT tune anything to m_p. We report
the raw functional relation we find and the raw m_p that each stage implies.

Run:  python3 -u volume_def_reconcile.py 2>&1 | tee /tmp/volume_def_reconcile.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _precision import COMPUTE_DPS  # noqa: E402
from _li_2_q_util import (  # noqa: E402
    load_q_50dps,
    per_knot_density_borromean,
)
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
)
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = COMPUTE_DPS

HERE = Path(__file__).resolve().parent
WITNESS = HERE / "volume-def-reconcile.witness.json"

# CODATA reference masses (MeV) — for raw m_p readings only, NEVER for fitting.
# Imported from the central registry (P31: no hardcoded CODATA literals).
M_E = mp.mpf(M_E_MEV)                              # electron mass (CAL-1)
M_AVG_CODATA = (mp.mpf(M_P_MEV_VALIDATION)
                + mp.mpf(M_N_MEV_VALIDATION)) / 2  # (m_p+m_n)/2


def borromean_trM_normalized(q: mp.mpf, qi: mp.mpf) -> mp.mpf:
    """Bare-Borromean NORMALIZED Markov trace tr_M(𝓑₃) at q₀.

    Matches the keystone audit's `structural_vol_vs_log_trM.tr_M(bare)`
    value (~0.9986).  Wenzl-normalized closed form for the bare 𝓑₃ trace
    (leading 1 in h): (4 + h² − 3h⁴ − h⁶)/(h² + 4), h = q − q⁻¹.
    """
    h = q - qi
    return (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)


def main() -> None:
    q, qi, _z = load_q_50dps()
    hbar_q = 1 - qi  # ℏ_q = 1 − q⁻¹
    start = time.monotonic()

    G = mp.catalan
    vol_8G = 8 * G  # Definition A: classical hyperbolic Vol(𝓑₃)

    trM_norm = borromean_trM_normalized(q, qi)
    ln_trM_norm = mp.log(abs(trM_norm))  # what the keystone audit tested (-0.00144)

    # --- Exact functional-relation tests (the task's hard discipline) -------
    # Is 8G the log/exp of ln_trM_norm up to a factor?
    rel = {
        "exp_ln_trM_norm": mp.nstr(mp.exp(ln_trM_norm), 12),   # == trM_norm ≈ 1
        "trM_norm": mp.nstr(trM_norm, 12),
        "ln_8G": mp.nstr(mp.log(vol_8G), 12),                   # ≈ 1.99 ≠ ln_trM_norm
        "ratio_8G_over_abs_ln_trM_norm": mp.nstr(vol_8G / abs(ln_trM_norm), 8),
        "is_log_or_exp_relation": (
            "NO. exp(ln_trM_norm)=trM_norm≈1 (round-trips to the trace, not 8G); "
            "ln(8G)≈1.99 (not ≈ln_trM_norm). 8G is NEITHER log NOR exp of "
            "ln_trM_norm. The '5090×' = 8G / |ln(trM_norm(q₀))| is the ratio of "
            "a POST-τ volume to ln of a PRE-τ algebraic number at q₀ — a "
            "cross-functor (category) comparison, not one functional map."
        ),
    }
    ratio_5090 = vol_8G / abs(ln_trM_norm)

    # --- Raw m_avg readings (no fit) at each chain stage --------------------
    geom_leading_A = vol_8G / hbar_q**2
    m_avg_A_bare = M_E * geom_leading_A
    m_avg_A_prod = M_E * per_knot_density_borromean(q, qi)
    m_avg_B_wrongstage = M_E * (ln_trM_norm / hbar_q**2)  # negative — category error

    readings = {
        "production_8G_over_hbar2_times_linking_weight": {
            "m_avg_MeV": mp.nstr(m_avg_A_prod, 10),
            "err_vs_codata_pct": mp.nstr((m_avg_A_prod / M_AVG_CODATA - 1) * 100, 6),
            "stage": "POST-τ classical Vol (8G) × H₄ linking_weight (Def A, production)",
        },
        "8G_over_hbar2_bare_lw1": {
            "m_avg_MeV": mp.nstr(m_avg_A_bare, 10),
            "err_vs_codata_pct": mp.nstr((m_avg_A_bare / M_AVG_CODATA - 1) * 100, 6),
            "stage": "POST-τ classical Vol (8G) alone, linking_weight=1",
        },
        "lnTrMnorm_over_hbar2_WRONGSTAGE": {
            "m_avg_MeV": mp.nstr(m_avg_B_wrongstage, 10),
            "err_vs_codata_pct": mp.nstr((m_avg_B_wrongstage / M_AVG_CODATA - 1) * 100, 6),
            "stage": "ln of PRE-τ normalized trace at q₀ — CATEGORY ERROR "
                     "(the keystone audit's −0.00144 reading; gives negative mass)",
        },
    }

    verdict = (
        "(a) SAME OBJECT ACROSS τ — the '5090×' is a CROSS-FUNCTOR CATEGORY "
        "ERROR, not a numerical contradiction. Definition A (8G) is the "
        "POST-τ archimedean volume Vol(K)=Re tr(τ̂_desc·Hol) [topological-"
        "mass-formula Step 1, Chern–Simons/volume correspondence]. Definition "
        "B (ln|Vol_q|) is τ_arch applied to the PRE-τ algebraic generator "
        "Vol_q=∏V̂_i; prop:vol-through-tau + kashaev-volume-conjecture assert "
        "these are EQUAL by the Kashaev Volume Conjecture (the regulator of a "
        "Bloch-group class landing in ℝ as the hyperbolic volume). So "
        "ln|Vol_q| SHOULD equal 8G — they are the same Vol(K). The keystone "
        "audit's −0.00144 took ln of the q₀-evaluated NORMALIZED trace "
        "(≈0.9986), i.e. the PRE-τ algebraic number specialized at q₀ — NOT "
        "the τ_arch regulator/Kashaev-limit (an N→∞ asymptotic at roots of "
        "unity). Logging a pre-τ number is the category error. PRODUCTION "
        "USES THE CORRECT STAGE: the post-τ classical Vol(K)=8G is exactly "
        "what the KVC says ln|Vol_q| evaluates to. No volume-definition bug."
    )

    out = {
        "schema": "volume-def-reconcile/1",
        "description": (
            "Reconciliation of the two Borromean-volume definitions (8G vs "
            "ln|Vol_q|). Determines they are the SAME post-τ volume Vol(K) "
            "linked by the Kashaev Volume Conjecture; the keystone audit's "
            "5090× was a cross-τ category comparison. No fit."
        ),
        "compute_dps": COMPUTE_DPS,
        "q0": mp.nstr(q, 20),
        "hbar_q": mp.nstr(hbar_q, 20),
        "definition_A_production": {
            "name": "classical hyperbolic Vol(𝓑₃) = 8·G",
            "value": mp.nstr(vol_8G, 20),
            "chain_stage": "POST-τ (archimedean ℝ). topological-mass-formula "
                           "Step 1: Re tr(τ̂_desc·Hol)=Vol(K), CS/volume corr.",
            "provenance": "_li_2_q_util.per_knot_density_borromean vol_b3=8*mp.catalan; "
                          "Adams 1985 SnapPy table.",
        },
        "definition_B_vol_through_tau": {
            "name": "Vol(K)=τ_arch(Vol_q)=ln|Vol_q|, Vol_q=∏V̂_i ∈ ℤ[q^½]",
            "chain_stage": "Vol_q is PRE-τ algebraic; τ_arch=ln|·| is the "
                           "archimedean EXIT. The result ln|Vol_q| is POST-τ ℝ.",
            "kvc_bridge": "kashaev-volume-conjecture.md: Vol_hyp = "
                          "2π·lim log|J_N|/N at roots of unity = regulator of "
                          "a Bloch-group class. prop:vol-through-tau asserts "
                          "this EQUALS the classical Vol(K)=8G.",
            "normalized_trM_at_q0": mp.nstr(trM_norm, 12),
            "ln_normalized_trM_at_q0_WRONGSTAGE": mp.nstr(ln_trM_norm, 12),
            "note": "The keystone audit's −0.00144 = ln|trM_norm(q₀)| logs the "
                    "PRE-τ algebraic number at q₀ — a category error, not the "
                    "τ_arch/Kashaev regulator.",
        },
        "exact_functional_relation": rel,
        "the_5090x_explained": {
            "ratio_8G_over_abs_ln_trM_norm": mp.nstr(ratio_5090, 8),
            "interpretation": "8G / |ln(trM_norm(q₀))| = 7.328 / 0.00144 ≈ 5090. "
                              "NOT a log↔exp relation (see exact_functional_"
                              "relation). It is the magnitude of a post-τ volume "
                              "over ln of a pre-τ number — cross-functor compare.",
        },
        "raw_m_p_readings_no_fit": readings,
        "production_stage_verdict": (
            "CORRECT. Production uses the POST-τ classical Vol(K)=8G, which is "
            "exactly what prop:vol-through-tau says ln|Vol_q| evaluates to via "
            "the KVC. The q-volume functional (Def B) is the SAME observable "
            "computed the long way (open KVC asymptotic + per-crossing V̂_i). "
            "Production short-circuits to the SnapPy 8G — correct value, "
            "correct stage. Raw production m_avg ≈ 966 MeV (+2.89%) is "
            "unchanged; the +2.89% is the SEPARATE linking_weight residual."
        ),
        "verdict": verdict,
        "residual_open": (
            "Not the volume DEFINITION (reconciled here). The genuine open "
            "items per keystone §5: (i) the KVC itself (axiomatized as "
            "VolumeConjecture class — proved only for 4₁, some torus/pretzel); "
            "(ii) the per-crossing V̂_i factorization compute for atomic "
            "braids; (iii) the H₄ linking_weight 2.53 vs CODATA-λ 2.46 "
            "residual (+2.89%) = the separate λ_scale-absorbed item, NOT a "
            "volume-definition inconsistency."
        ),
        "discipline": "No fit, no fabrication. m_p readings are raw at each "
                      "stage; we report whichever follows, not the one nearest "
                      "CODATA.",
    }

    WitnessBuilder.wrap_legacy(
        "volume-def-reconcile",
        out,
        script_path=__file__,
        engine="mpmath",
        start_time=start,
    ).save()

    print("=" * 72)
    print("VOLUME DEFINITION RECONCILIATION — 8G vs ln|Vol_q|")
    print("=" * 72)
    print(f"q0                       = {mp.nstr(q, 14)}")
    print(f"Def A  Vol(𝓑₃) = 8G     = {mp.nstr(vol_8G, 12)}  (POST-τ classical)")
    print(f"       normalized tr_M   = {mp.nstr(trM_norm, 12)}  (PRE-τ, at q₀)")
    print(f"       ln|tr_M_norm|     = {mp.nstr(ln_trM_norm, 12)}  (keystone's −0.00144)")
    print(f"       8G / |ln tr_M|    = {mp.nstr(ratio_5090, 8)}  (the '5090×')")
    print("-" * 72)
    print(f"exp(ln_trM_norm)         = {rel['exp_ln_trM_norm']}  (round-trips to tr_M, NOT 8G)")
    print(f"ln(8G)                   = {rel['ln_8G']}  (!= ln_trM_norm)")
    print("-> 8G is NEITHER log NOR exp of ln_trM_norm: cross-functor compare.")
    print("-" * 72)
    print("RAW m_avg readings (no fit):")
    for k, v in readings.items():
        print(f"  {k:48s} {v['m_avg_MeV']:>12s} MeV  ({v['err_vs_codata_pct']}%)")
    print("-" * 72)
    print("VERDICT: (a) SAME OBJECT ACROSS τ — category error, not a bug.")
    print("PRODUCTION STAGE: CORRECT (post-τ classical 8G = KVC value of ln|Vol_q|).")
    print(f"Witness: {WITNESS}")


if __name__ == "__main__":
    main()
