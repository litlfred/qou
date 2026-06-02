#!/usr/bin/env python3
"""EXPLORATORY shape-probe (per user direction 2026-05-23 clarification:
"suggestions of empirical fits are OK for exploratory - what is the
shape type of questions. but never for PROD pipeline").

This probe is **exploratory shape-probing**, NOT for production. The
α = (3/4 + 1 − G) ≈ 0.834 h^4 coefficient it surfaces gives m_p to
22 ppm — a SHAPE HINT that the partition-algebra h^4 weight at H_4
might contain a "+1" leading term combined with canonical (+3/4) and
Yekutieli (−G) at h². But the "+1" lacks categorical derivation; it
cannot be promoted to production without one.

Status:
  - EXPLORATORY: yes — useful for hypothesis-generation about the
    h^4 categorical structure (is the leading +1 from second-order
    Yekutieli per-cell? from Φ_q pentagon h^4 remainder? from a
    crystal-graph contribution? — RULE 14 candidates).
  - PRODUCTION: no — the "+1" is fit, not derived. Production
    remains option (a) canonical alone (PR #895) until either the
    cell-↔-projection bijection (option b's load-bearing step) or
    the color-sheet ↔ flavor mapping (option c's load-bearing step)
    or a categorical derivation of the +1 coefficient closes.

Per RULE 14 (canonical-unification audit
docs/audits/2026-05-23-lambda-scale-canonical-unification.md
§"Rule 14"): if the "+1" coefficient can be derived from one of the
13 categorical drivers (Φ_q recursion, Rogers pentagon, Yang-Baxter,
hexagon, Frobenius reciprocity, 6j, modular dual, KLR, MacMahon,
Lobachevsky-Catalan, Chern-Simons-Ohtsuki, crystal-graph), then this
probe's shape-hint translates into a canonical refinement. If NOT,
the candidate must be escalated to the author for explicit
authorisation before production adoption.

Until that closure: framework canonical predictions are
  (a) canonical Wedderburn alone:         m_p ≈ 965 MeV  (+2.89%)
  (b) canonical + Yekutieli additive:     m_p ≈ 950 MeV  (+1.26%)
  (c) Bring color-tube (n=10 substrate):  m_p ≈ 938 MeV  (−670 ppm)

Each is conjecture-conditional but FITTING-FREE. This exploratory
probe sits above (c) as a shape-hint for future canonical derivation.

Refinement probe — h^4 correction to Bring color-tube (EXPLORATORY).

Observation (lambda_scale_refinements_composed_predictions.py):
Option (c) `λ = 1/(1 − h_q · q_0^10)` gives m_p = 937.6 MeV vs
CODATA 938.27 MeV → **−670 ppm UNDER**. The residual on λ:

  λ_target_with_flavor_split = m_p_CODATA · ℏ_q² / Vol(𝓑_3) / (1 − Δm/(2 M_N))
                             ≈ 2.4619
  λ_option_c                  = 1/(1 − h_q · q_0^10)
                             ≈ 2.4600
  residual                    = +0.00193

Striking: this residual ≈ h_q^4 (with coefficient ~1):

  h_q^4 = (q_0 − 1/q_0)^4  ≈  0.001910
  residual ≈ +0.00193 → coefficient ≈ +1.011 (= +1 + 1 % deviation)

If the structural form is

  λ_refined  =  1/(1 − h_q · q_0^10)  +  α · h_q^4   (α small integer)

then this is a TWO-MECHANISM substrate-pure candidate:
  - 1/(1−h_q·q_0^10) from Bring color-tube weighted averaging
    (Phase 5q, color-sheet ↔ quark-flavor mapping load-bearing)
  - α · h_q^4 from a higher-order Yekutieli per-cell contribution
    OR a Φ_q-pentagon h⁴ remainder (audit Step 4 R&D)

This probe:
  1. Computes the framework-correct λ target (with #942 flavor-split)
  2. Probes the h^4 coefficient α via direct algebraic identification
  3. Tests several small-integer / small-rational α values for best
     m_p / m_n match
  4. Documents which α gives the closest framework prediction
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # CODATA-2022 full precision

mp.mp.dps = 80


def main() -> int:
    Q0 = mp.mpf(Q_50_DIGIT_STR)
    h_q = Q0 - 1 / Q0
    h2 = h_q * h_q
    h4 = h2 * h2
    G = mp.catalan

    VOL_B3 = 8 * G
    HBAR_Q = (Q0 - 1) / Q0
    INV_HBAR2 = 1 / (HBAR_Q ** 2)

    # CODATA (Layer-2 substrate flavor-split per PR #942):
    M_E = M_E_MEV  # from codata_constants
    M_P_CODATA = mp.mpf("938.27208816")
    M_N_CODATA = mp.mpf("939.56542052")
    M_AVG_CODATA = (M_P_CODATA + M_N_CODATA) / 2

    bracket_2_q = Q0 + 1 / Q0
    delta_m_over_M_N = HBAR_Q ** 2 * h_q * bracket_2_q * (1 + HBAR_Q ** 3) / 3

    # Framework-correct λ target (after flavor-split layer):
    # m_p = m_e · Vol(𝓑_3)/ℏ_q² · λ · (1 - Δm/(2 M_N))
    # ⇒ λ = m_p_CODATA / (m_e · Vol(𝓑_3)/ℏ_q² · (1 - Δm/(2 M_N)))
    scale_constant = M_E * VOL_B3 * INV_HBAR2
    flavor_p_factor = 1 - delta_m_over_M_N / 2
    flavor_n_factor = 1 + delta_m_over_M_N / 2
    flavor_avg_factor = mp.mpf("1")

    lambda_target_for_m_p = M_P_CODATA / (scale_constant * flavor_p_factor)
    lambda_target_for_m_n = M_N_CODATA / (scale_constant * flavor_n_factor)
    lambda_target_for_m_avg = M_AVG_CODATA / (scale_constant * flavor_avg_factor)

    # Base form: Bring color-tube Φ_q pentagon
    lambda_bring = 1 / (1 - h_q * Q0 ** 10)

    # Residuals at λ-level
    residual_p = lambda_target_for_m_p - lambda_bring
    residual_n = lambda_target_for_m_n - lambda_bring
    residual_avg = lambda_target_for_m_avg - lambda_bring

    print(f"q_0           = {mp.nstr(Q0, 25)}")
    print(f"h_q           = {mp.nstr(h_q, 18)}")
    print(f"h_q^2         = {mp.nstr(h2, 18)}")
    print(f"h_q^4         = {mp.nstr(h4, 18)}")
    print(f"G (Catalan)   = {mp.nstr(G, 18)}")
    print()
    print(f"scale_constant     = m_e · Vol/ℏ_q² = {mp.nstr(scale_constant, 18)}")
    print(f"flavor_p_factor    = 1 − Δm/(2 M_N) = {mp.nstr(flavor_p_factor, 18)}")
    print(f"flavor_n_factor    = 1 + Δm/(2 M_N) = {mp.nstr(flavor_n_factor, 18)}")
    print()
    print("λ TARGETS (framework-correct, with flavor-split per PR #942):")
    print(f"  for m_p_CODATA  = {mp.nstr(lambda_target_for_m_p, 18)}")
    print(f"  for m_n_CODATA  = {mp.nstr(lambda_target_for_m_n, 18)}")
    print(f"  for m_avg_CODATA = {mp.nstr(lambda_target_for_m_avg, 18)}")
    print()
    print(f"Bring color-tube base:    λ = 1/(1 − h_q · q_0^10) = {mp.nstr(lambda_bring, 18)}")
    print()
    print(f"Residual vs m_p target:  {mp.nstr(residual_p, 12)}  → α = residual/h^4 = {mp.nstr(residual_p / h4, 12)}")
    print(f"Residual vs m_n target:  {mp.nstr(residual_n, 12)}  → α = residual/h^4 = {mp.nstr(residual_n / h4, 12)}")
    print(f"Residual vs m_avg target:{mp.nstr(residual_avg, 12)}  → α = residual/h^4 = {mp.nstr(residual_avg / h4, 12)}")
    print()

    # The framework prediction must give CONSISTENT m_p, m_n, m_avg
    # under ONE λ_scale (which is class-uniform per Family A).
    # So we use m_avg's target and use the flavor-split to derive m_p, m_n.
    print("Using m_avg-derived target (since λ_scale is class-uniform):")
    print(f"  α_m_avg = {mp.nstr(residual_avg / h4, 14)}")
    print()

    # Test candidate α values
    print("Candidate α values for refinement λ = 1/(1−h·q^10) + α·h^4:")
    candidates_alpha = [
        ("1", mp.mpf(1)),
        ("3/4", mp.mpf(3) / 4),
        ("1 + h²/12", 1 + h2 / 12),
        ("1 + G·h²", 1 + G * h2),
        ("[2]_q²/(2[3]_q)", (Q0 + 1/Q0) ** 2 / (2 * (Q0**2 + 1 + Q0**(-2)))),
        ("G/2", G / 2),
        ("(3/4 - G + 1)", mp.mpf("0.75") - G + 1),
    ]

    best_alpha_name = None
    best_alpha_val = None
    best_m_p_rel_ppm = mp.mpf("1e10")

    print(f"  {'alpha':<28s} {'value':>15s}  {'m_p pred':>14s}  {'rel ppm':>12s}")
    print(f"  {'-' * 28} {'-' * 15}  {'-' * 14}  {'-' * 12}")
    for name, alpha in candidates_alpha:
        lambda_refined = lambda_bring + alpha * h4
        m_avg_pred = scale_constant * lambda_refined
        m_p_pred = m_avg_pred * flavor_p_factor
        rel_ppm = (m_p_pred - M_P_CODATA) / M_P_CODATA * mp.mpf("1e6")
        marker = ""
        if abs(rel_ppm) < abs(best_m_p_rel_ppm):
            best_m_p_rel_ppm = rel_ppm
            best_alpha_name = name
            best_alpha_val = alpha
            marker = "  ←"
        print(f"  {name:<28s} {mp.nstr(alpha, 12):>15s}  {mp.nstr(m_p_pred, 12):>14s}  {mp.nstr(rel_ppm, 6):>12s}{marker}")

    print()
    print(f"BEST α = {best_alpha_name} ({mp.nstr(best_alpha_val, 14)})")
    print(f"  m_p prediction = {mp.nstr(scale_constant * (lambda_bring + best_alpha_val * h4) * flavor_p_factor, 18)} MeV")
    print(f"  vs CODATA       = {mp.nstr(M_P_CODATA, 18)} MeV")
    print(f"  rel diff        = {mp.nstr(best_m_p_rel_ppm, 8)} ppm")

    # Structural interpretation
    print()
    print("=" * 70)
    print("STRUCTURAL INTERPRETATION:")
    alpha_residual_m_avg = residual_avg / h4
    print(f"  α (empirical, m_avg-anchored) = {mp.nstr(alpha_residual_m_avg, 14)}")
    print(f"  Closest simple form: α ≈ 1.0  ⇒  refinement is +h_q^4")
    print()
    print("Possible categorical origins of +h^4 term:")
    print("  - SECOND-ORDER Yekutieli per-cell: per the audit Step 4 R&D")
    print("    open item, the next term in the q-expansion of the half-sym")
    print("    Markov trace should be derivable from the partition algebra")
    print("    at level n=4. If structurally derivable, this closes the")
    print("    Bring color-tube residual.")
    print("  - Φ_q pentagon h^4 remainder: the operator-theoretic Φ_q")
    print("    pentagon identity has h^4 contributions beyond the leading")
    print("    1/(1−h·q^10) = Φ_q(h·q^11)/Φ_q(h·q^10).")
    print("  - h^4 modular-dual q̃ contribution: q̃ = e^{2πi/τ} where")
    print("    τ = h_q · K (some modular-form quantity); h^4 may be the")
    print("    leading instanton.")
    print()
    print("OPEN: distinguish these mechanisms by checking the coefficient's")
    print("substrate-natural form. α ≈ 1 (vs h²-corrected forms) suggests")
    print("the term is a clean (h_q^4) without internal q-deformation —")
    print("more consistent with the partition-algebra origin than the")
    print("modular-dual origin (the latter would carry K-dependent factors).")
    print("=" * 70)

    w = WitnessBuilder(
        "lambda-scale-refinement-h4-correction-bring",
        engine="mpmath",
    )
    w.set_description(
        "Refinement probe: Bring color-tube Φ_q pentagon `1/(1−h_q·q_0^10)` "
        "+ α·h_q^4 correction, tested against the framework-correct λ target "
        "(m_p_CODATA back-solved through PR #942 flavor-split). Residual "
        "(m_avg target − Bring base) ≈ +1.011·h_q^4 — α ≈ 1 cleanly. "
        "Possible categorical origins: second-order Yekutieli per-cell "
        "(audit Step 4 R&D), Φ_q pentagon h^4 remainder, modular-dual "
        "instanton. Coefficient ≈ 1 (no internal q-deformation) most "
        "consistent with partition-algebra origin per audit hint."
    )
    w.set_content_block("conj:borromean-baryon-mass-formula")
    w.add_parameter("dps", 80)
    w.add_data("lambda_bring_color_tube_base", mp.nstr(lambda_bring, 25))
    w.add_data("lambda_target_for_m_p_codata", mp.nstr(lambda_target_for_m_p, 25))
    w.add_data("lambda_target_for_m_avg_codata", mp.nstr(lambda_target_for_m_avg, 25))
    w.add_data("alpha_empirical_m_avg_anchored", mp.nstr(alpha_residual_m_avg, 25))
    w.add_data("best_alpha_name", best_alpha_name)
    w.add_data("best_alpha_value", mp.nstr(best_alpha_val, 25))
    w.add_data("best_m_p_rel_diff_ppm", mp.nstr(best_m_p_rel_ppm, 18))
    w.add_data("h4_at_q0", mp.nstr(h4, 25))

    # Probe documents the +h^4 refinement candidate
    # Passes iff α ≈ 1 cleanly (within 2%) AND the resulting m_p
    # prediction is within 1000 ppm of CODATA
    alpha_close_to_one = abs(alpha_residual_m_avg - 1) < mp.mpf("0.02")
    m_p_close = abs(best_m_p_rel_ppm) < 1000
    h4_refinement_valid = int(bool(alpha_close_to_one and m_p_close))
    w.add_assertion(
        "h4_refinement_alpha_close_to_one_and_m_p_close",
        computed=h4_refinement_valid,
        expected=1,
        tolerance=None,
        source=(
            "Empirical α (= residual / h^4) ≈ 1 within 2%, and the "
            "refined λ = 1/(1-h_q·q^10) + h_q^4 gives m_p prediction "
            "within 1000 ppm of CODATA — a coherent +h^4 refinement "
            "candidate for the Bring color-tube form. Categorical "
            "origin of the +h^4 term (second-order Yekutieli per-cell "
            "vs Φ_q pentagon h^4 remainder vs modular dual) is the "
            "remaining R&D direction."
        ),
    )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
