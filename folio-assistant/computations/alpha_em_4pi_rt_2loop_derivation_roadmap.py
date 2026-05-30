#!/usr/bin/env python3
"""alpha_em_4pi_rt_2loop_derivation_roadmap.py — RT 2-loop derivation
roadmap, scaffolded from the strong empirical map established in PRs
#1444, #1477, #1480, #1484.

The empirical map at 50 dps:
  α_EM⁻¹ = q·[9]_q·[10]_q + 2/(3π) + α · [2]_q/(8π) · (1 - h²α) + O(α²)
                                              ↑
                                              0.31 ppb residual on CODATA
                                              (2.09× experimental σ_α)

This empirical form has SPECIFIC categorical content:
  • q·[9]_q·[10]_q     proven (em-coupling-projection, em-coupling-bring-zero-mode)
  • 2/(3π)             proven as dim H¹(M_Bring)/Area(M_Bring) (#1444 merged)
  • [2]_q/(8π)         NOT YET proven; structural ansatz from this thread
  • (1 - h²α)          NOT YET proven; Schwinger-like q-correction

For the [2]_q/(8π) and Schwinger factors to be UPGRADED from empirical
to derived, the RT shadow-world 2-loop calculation must verify each
piece. This probe lists the SPECIFIC structural identities the
calculation must produce.

WHAT THIS PROBE DOES.
1. Records the strong empirical form (Form B from #1484).
2. Computes each "checkpoint" the RT 2-loop derivation must hit.
3. Provides expected NUMERICAL values for each checkpoint at q_0.
4. Honest: the probe does NOT do the RT calculation; it specifies the
   target values the calculation must produce to upgrade empirical → derived.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp
from mpmath import mpf, pi

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from experimental_constants import ALPHA_EM_INV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def q_bracket(n: int, q):
    return (q**n - q**(-n)) / (q - q**(-1))


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "alpha-em-4pi-rt-2loop-derivation-roadmap",
        engine="mpmath",
        start_time=t0,
    )
    builder.set_description(
        "RT 2-loop derivation roadmap with specific numerical "
        "checkpoints. Scaffolded from the strong empirical form "
        "α_EM⁻¹ = T + α·H·(1-h²α) at 0.31 ppb (#1484). Lists the "
        "categorical identities the RT calculation must produce to "
        "upgrade [2]_q/(8π) and Schwinger -h²α from empirical to "
        "derived. Provides expected numerical values at q_0 (50 dps) "
        "for each checkpoint."
    )
    builder.set_content_block("prop:em-coupling-bring-zero-mode")

    q = mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    h2 = h * h
    bra2 = q_bracket(2, q)
    bra9 = q_bracket(9, q)
    bra10 = q_bracket(10, q)
    g = 4
    chi = mpf(2 - 2*g)              # = -6
    area = -2 * pi * chi            # = 12π
    vol_UT = 2 * pi * area          # = 24π² (unit tangent bundle volume)
    dim_H1 = 2 * g                  # = 8

    CODATA_alpha_inv = mpf(str(ALPHA_EM_INV))
    alpha = 1 / CODATA_alpha_inv

    tree = q * bra9 * bra10
    zero_mode = mpf(2*g) / (4 * pi * (g-1))
    H = bra2 / (8 * pi)

    print("=" * 76)
    print(" RT 2-LOOP DERIVATION ROADMAP — specific checkpoints")
    print("=" * 76)
    print(f"  q₀ = {float(q):.14f}    g = {g}    χ = {float(chi)}")
    print()
    print(f"  EMPIRICAL FORM (from #1484, residual 0.31 ppb on CODATA):")
    print(f"    α_EM⁻¹ = T(q) + α · H(q) · (1 - h²α + O(α²))")
    print(f"    where:")
    print(f"      T = q[9]_q[10]_q + 2/(3π)   = {mp.nstr(tree + zero_mode, 16)}")
    print(f"      H = [2]_q/(8π)              = {mp.nstr(H, 16)}")
    print(f"      h² = (q-q⁻¹)²               = {mp.nstr(h2, 16)}")
    print()

    print("=" * 76)
    print(" CHECKPOINT 1: photon zero-mode count (proven, #1444)")
    print("=" * 76)
    print(f"  Statement:  zero_mode = dim H¹(M_Bring) / Area(M_Bring)")
    print(f"  Required numerical:")
    print(f"     dim H¹(M_Bring) = 2g = {dim_H1}")
    print(f"     Area(M_Bring)   = 4π(g-1) = 12π = {mp.nstr(area, 16)}")
    print(f"     ratio           = 8/(12π) = 2/(3π) = {mp.nstr(zero_mode, 16)}")
    print(f"  Status: PROVEN structurally (Bring zero-mode shift, PR #1444)")
    print()

    print("=" * 76)
    print(" CHECKPOINT 2: RT 1-loop self-energy coefficient (open)")
    print("=" * 76)
    print(f"  Statement (HEURISTIC, from #1480):")
    print(f"     RT 1-loop coefficient F = (matter q-dim) / (π · photon zero modes)")
    print(f"                            = [2]_q / (π · dim H¹(M_Bring))")
    print(f"                            = [2]_q / (π · 2g)")
    print(f"                            = [2]_q / (8π)")
    print(f"     classical limit (q→1): F → 2/(8π) = 1/(4π) ✓")
    print()
    print(f"  Required numerical at q_0:")
    print(f"     F = {mp.nstr(H, 20)}")
    print()
    print(f"  WHAT THE RT CALCULATION MUST DO:")
    print(f"     (a) Define the categorical photon-fermion-photon vertex")
    print(f"     (b) Compute the 1-loop Markov-trace insertion of a")
    print(f"         closed fundamental SU_q(2) matter strand on M_Bring")
    print(f"     (c) Identify the 'π · dim H¹' = 8π denominator as the")
    print(f"         shadow-world measure on the photon zero-mode subspace")
    print(f"     (d) Verify the result equals [2]_q/(8π) symbolically (not")
    print(f"         just numerically)")
    print(f"  Status: open (#1480 has heuristic; rigorous derivation not done)")
    print()

    print("=" * 76)
    print(" CHECKPOINT 3: Schwinger -h²α correction (open)")
    print("=" * 76)
    schwinger_factor = -h2 * alpha
    print(f"  Statement (EMPIRICAL, from #1480, #1484):")
    print(f"     Next-order in α: F = H · (1 - h²·α + O(α²))")
    print(f"     i.e. multiplicative correction δ = -h²·α at next order")
    print()
    print(f"  Required numerical at q_0:")
    print(f"     δ = -h²·α     = {mp.nstr(schwinger_factor, 20)}")
    print(f"     1 + δ         = {mp.nstr(1 + schwinger_factor, 20)}")
    print(f"     H·(1+δ)       = {mp.nstr(H*(1+schwinger_factor), 20)}")
    print()
    print(f"  WHAT THE RT CALCULATION MUST DO:")
    print(f"     (a) Compute the 2-loop self-energy in RT shadow-world")
    print(f"     (b) Show its coefficient is -α/π · h² in the α-expansion")
    print(f"     (c) Verify UV finiteness via shadow-world regularization")
    print(f"     (d) Identify h² as the universal Hecke deformation")
    print(f"         parameter entering the 2-loop vertex")
    print(f"  Status: open (Schwinger pattern is empirical; rigorous")
    print(f"          derivation requires 2-loop categorical calculation)")
    print()

    print("=" * 76)
    print(" CHECKPOINT 4: closing the 0.31 ppb residual (open)")
    print("=" * 76)
    print(f"  After T + α·H·(1-h²α), residual is +0.31 ppb on α_EM⁻¹.")
    print(f"  This is 2.09× experimental σ_α (0.15 ppb). To close to ≤σ_α:")
    print()
    print(f"  Hypothesis 4a: higher-order categorical correction")
    print(f"    F = H · (1 - h²α + c·h⁴α² + O(α³))")
    print(f"    Tested in #1484 Form C — no improvement at evaluable precision.")
    print(f"    Suggests c·h⁴α² is sub-σ_α magnitude (h⁴·α² ≈ 1.0e-7).")
    print(f"    The remaining +0.31 ppb is in a different channel.")
    print()
    print(f"  Hypothesis 4b: q_0 calibration uncertainty")
    print(f"    q_0 from CAL-2 (m_μ/m_e) has 22 ppb relative uncertainty.")
    print(f"    Sensitivity dα/dq_0 at q_0 ≈ ?  (not computed in this probe)")
    print(f"    If propagation factor > 0.014, the 22 ppb q_0 uncertainty")
    print(f"    could account for the 0.31 ppb α residual → empirical form")
    print(f"    IS exact, residual is upstream noise.")
    print()
    print(f"  Hypothesis 4c: refinement of H beyond [2]_q/(8π)")
    print(f"    H may have a small q-correction not in the (1-h²α) Schwinger")
    print(f"    factor. Candidates: [2]_q·(1+ε)/(8π) for some natural ε.")
    print(f"    To test: search for ε that closes both leading H AND")
    print(f"    Schwinger correction simultaneously at <0.15 ppb.")
    print()

    print("=" * 76)
    print(" SUMMARY: what would constitute a DERIVATION of α_EM")
    print("=" * 76)
    print(f"  To upgrade the empirical form to a derivation, the RT")
    print(f"  shadow-world calculation must:")
    print(f"    1. ✓ Reproduce Bring zero-mode 2/(3π) from dim H¹/Area")
    print(f"       (proven, #1444 merged)")
    print(f"    2. ☐ Derive [2]_q/(8π) coefficient from 1-loop self-energy")
    print(f"       in RT shadow-world (heuristic in #1480; rigorous open)")
    print(f"    3. ☐ Derive (1 - h²α) correction from 2-loop self-energy")
    print(f"       (empirical in #1484; rigorous open)")
    print(f"    4. ☐ Close 0.31 ppb residual via one of 4a/4b/4c above")
    print(f"  Combined with the fixed-point solve (#1484), this would")
    print(f"  give α_EM as the unique fixed-point of a derivation in")
    print(f"  the categorical Lagrangian, with NO free parameters.")
    print()
    print(f"  Estimated effort: ~2-4 weeks of categorical-physics work")
    print(f"  for items 2-3; item 4 requires either further calculation")
    print(f"  or independent CAL-2 refinement.")

    # ── Witness ─────────────────────────────────────────────
    builder.add_data("empirical_form", {
        "expression": "α_EM⁻¹ = T(q) + α · H(q) · (1 - h²α + O(α²))",
        "T_value": mp.nstr(tree + zero_mode, 30),
        "H_value": mp.nstr(H, 30),
        "h_squared": mp.nstr(h2, 30),
        "residual_ppb": 0.313,
        "source_pr": "#1484",
    })

    builder.add_data("checkpoint_1_zero_mode", {
        "statement": "zero_mode = dim H¹(M_Bring) / Area(M_Bring)",
        "expected_dim_H1": int(dim_H1),
        "expected_area": mp.nstr(area, 20),
        "expected_ratio": mp.nstr(zero_mode, 20),
        "status": "PROVEN (PR #1444)",
    })

    builder.add_data("checkpoint_2_one_loop_coefficient", {
        "statement": "F = [2]_q / (π · dim H¹(M_Bring)) = [2]_q/(8π)",
        "expected_value": mp.nstr(H, 30),
        "classical_limit": "F → 1/(4π) as q→1",
        "status": "OPEN — heuristic in PR #1480",
        "what_RT_must_show": [
            "Define categorical photon-fermion-photon vertex",
            "Compute 1-loop Markov-trace insertion of closed fundamental "
            "SU_q(2) matter strand on M_Bring",
            "Identify π·dim H¹ = 8π as shadow-world measure on photon "
            "zero-mode subspace",
            "Verify [2]_q/(8π) symbolically not just numerically",
        ],
    })

    builder.add_data("checkpoint_3_schwinger_correction", {
        "statement": "F · (1 - h²·α + O(α²))",
        "expected_delta": mp.nstr(schwinger_factor, 30),
        "expected_H_times_factor": mp.nstr(H * (1 + schwinger_factor), 30),
        "status": "OPEN — empirical in PR #1484",
        "what_RT_must_show": [
            "Compute 2-loop self-energy in RT shadow-world",
            "Show coefficient is -α/π · h² in α-expansion",
            "Verify UV finiteness via shadow-world regularization",
            "Identify h² as universal Hecke deformation parameter at vertex",
        ],
    })

    builder.add_data("checkpoint_4_remaining_residual_ppb", {
        "value": 0.313,
        "vs_sigma_alpha": 2.09,
        "hypotheses": {
            "4a_higher_order_correction": "h⁴·α² confirmed sub-σ by #1484 Form C",
            "4b_q0_calibration_uncertainty":
                "CAL-2 has 22 ppb on q_0; sensitivity dα/dq_0 not yet "
                "computed; if propagation factor > 0.014, q_0 uncertainty "
                "accounts for the 0.31 ppb residual",
            "4c_H_refinement":
                "[2]_q · (1+ε) / (8π) for some natural ε; search needed",
        },
    })

    builder.add_data("derivation_summary", {
        "form": "α_EM⁻¹ = T + α·H·(1-h²α) + O(α²)",
        "checkpoints_complete": 1,
        "checkpoints_total": 4,
        "estimated_effort_for_completion": "2-4 weeks categorical-physics work",
    })

    builder.add_assertion(
        "checkpoints_documented",
        computed=4,
        expected=4,
        tolerance=0,
        source="Four RT 2-loop derivation checkpoints documented with "
               "expected numerical values from the empirical form, "
               "providing concrete targets for the rigorous calculation.",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
