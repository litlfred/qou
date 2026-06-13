"""
fr_pullback_cosh_h_test.py — Phase 5h probe.

Tests whether integrating the Phase 5b cosh(h) correction into the
depth-stratified FR-pullback formula closes the residual 1.54× variance
left over after PR #826's K_3* = 4_1 resolution and Phase 5f's
(K_1*, K_2*) sweep showed both are essentially flat.

Background:
  - PR #826 + Phase 5f (PR #831): K_3* = 4_1 brings variance from
    1.82× (uniform) to 1.551×; FR at k=1, 2 marginal (+0.5%).
  - Phase 5b (PR #819 conj:alpha-cosh-h-z-step-correction): at the
    |Δ_λ*| single-block level, α ≈ [3]_q² · cosh(h) to 0.022%.
  - Hypothesis: cosh(h) is a structural correction missing from the
    depth-stratified formula. The 1.54× variance is the *integrated*
    consequence of this missing correction.

This probe tests four injection points:

  Variant 1: α_2 → α_2 · cosh(h)              (z² Markov-skein layer)
  Variant 2: α_3 → α_3 · cosh(h)              (chirality layer)
  Variant 3: α_2 → α_2 · cosh(h), α_3 → α_3 · cosh(h)
  Variant 4: B_pred → B_pred · cosh(h)        (global gain)
  Variant 5: α_2 → α_2 / cosh(h)              (reciprocal check)
  Variant 6: dim_q² weight → dim_q² · cosh(h) (per-partition)

Each variant is tested against the K_3* = 4_1 baseline (variance 1.551×
from PR #826). Reports best variance + which variant.

  Ref: conj:alpha-cosh-h-z-step-correction
  Ref: prop:depth-stratified-frobenius-reciprocity
  Ref: PR #826, PR #819 Phase 5b, PR #831 Phase 5f
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

import pyhecke_native  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from mass_at_3A_proper import dim_q, qfac  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402


B_AME = {
    "D":   AME_B_DEUTERON_MEV_VALIDATION,
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}

# K_3* = 4_1 from PR #826 empirical resolution.
K_3_STAR_4_1_CONWAY = (1, -2, 1, -2)


def conway_to_pyhecke(word_signed):
    out = []
    for s in word_signed:
        sign = 1 if s > 0 else -1
        out.append((sign, abs(s)))
    return out


K_3_STAR_WORD = conway_to_pyhecke(K_3_STAR_4_1_CONWAY)


def vanishing_threshold() -> mp.mpf:
    return mp.mpf(10) ** (5 - mp.mp.dps)


def alpha_k_base(k: int) -> mp.mpf:
    """Base alpha_k per binding_depth_stratified_rust.py."""
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G


def chi_lambda_braid_via_rust(shape, braid_word_signed, q_f64):
    word = [(int(s), int(g)) for (s, g) in braid_word_signed]
    return pyhecke_native.chi_lambda_braid(list(shape), word, float(q_f64))


def fr_pullback_weights_k3(by_partition, n_strands, q_f64,
                            per_partition_cosh_multiplier=False,
                            h_val=None):
    """K_3* = 4_1 FR pullback at depth 3 only, with optional cosh(h)
    multiplier on the dim_q² weight (Variant 6)."""
    qfact = qfac(n_strands)
    eps = vanishing_threshold()
    weights = {}
    chi_at_3 = {}
    z_norm = mp.mpf(0)
    s_uniform = mp.mpf(0)
    cosh_h = mp.cosh(h_val) if (per_partition_cosh_multiplier and h_val is not None) else mp.mpf(1)
    for p in by_partition:
        shape = tuple(p["partition"])
        depth = len(shape) - 1
        dq = dim_q(shape)
        dq_sq = mp.mpf(str(dq * dq))
        if per_partition_cosh_multiplier:
            dq_sq = dq_sq * cosh_h
        if depth != 3:
            weights[shape] = dq_sq / qfact
            continue
        s_uniform += dq_sq / qfact
        try:
            chi_K = chi_lambda_braid_via_rust(list(shape), K_3_STAR_WORD, q_f64)
        except (ValueError, RuntimeError, OverflowError):
            chi_K = 0.0
        chi_at_3[shape] = chi_K
        z_norm += dq_sq * mp.fabs(chi_K)
    if z_norm < eps:
        for shape in chi_at_3:
            dq = dim_q(shape)
            dq_sq = mp.mpf(str(dq * dq)) * cosh_h
            weights[shape] = dq_sq / qfact
    else:
        scale = s_uniform / z_norm
        for shape, chi_K in chi_at_3.items():
            dq = dim_q(shape)
            dq_sq = mp.mpf(str(dq * dq)) * cosh_h
            weights[shape] = dq_sq * mp.fabs(chi_K) * scale
    return weights


def phi_k_with_weights(by_partition, k, weights):
    total = mp.mpf(0)
    eps = vanishing_threshold()
    for p in by_partition:
        shape = tuple(p["partition"])
        if len(shape) - 1 != k:
            continue
        chi = mp.mpf(str(p["chi_lambda"]))
        dq = dim_q(shape)
        magnitude = mp.fabs(chi) * dq
        if magnitude < eps:
            continue
        w = weights.get(shape, mp.mpf(0))
        total += w * mp.log(magnitude)
    return total


def compute_B_with_variant(atom, variant):
    """Compute B with one of the cosh(h)-injection variants."""
    Z, N = ZN[atom]
    A = Z + N
    n_strands = 3 * A
    w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
    if not w_path.exists():
        return {"deferred": True}
    w = json.loads(w_path.read_text())
    atom_data = w["data"]["atom"]
    free_data = w["data"]["free"]
    q_f64 = float(Q0)

    q_mp = mp.mpf(str(Q0))
    h_val = q_mp - 1 / q_mp
    cosh_h = mp.cosh(h_val)

    per_part_cosh = (variant == "v6_dim_q2_times_cosh_h")
    w_atom = fr_pullback_weights_k3(atom_data["by_partition"], n_strands, q_f64,
                                      per_part_cosh, h_val)
    w_free = fr_pullback_weights_k3(free_data["by_partition"], n_strands, q_f64,
                                      per_part_cosh, h_val)

    B_dim = mp.mpf(0)
    for k in range(n_strands):
        ak = alpha_k_base(k)
        # Apply variant-specific alpha multipliers
        if variant == "v1_alpha_2_x_cosh_h" and k == 2:
            ak = ak * cosh_h
        elif variant == "v2_alpha_3_x_cosh_h" and k == 3:
            ak = ak * cosh_h
        elif variant == "v3_alpha_2_and_3_x_cosh_h" and k in (2, 3):
            ak = ak * cosh_h
        elif variant == "v5_alpha_2_div_cosh_h" and k == 2:
            ak = ak / cosh_h
        # Variants v4 and v6 are applied outside the alpha loop
        phi_a = phi_k_with_weights(atom_data["by_partition"], k, w_atom)
        phi_f = phi_k_with_weights(free_data["by_partition"], k, w_free)
        B_dim += ak * (phi_f - phi_a)

    if variant == "v4_global_cosh_h":
        B_dim = B_dim * cosh_h

    # alpha_k_base() already includes the m_e·8G factor for k≥4
    # (matches binding_depth_stratified_rust.py:62), so B_dim is in
    # MeV.  Do NOT multiply by M_E_MEV again — see #831 Copilot review.
    B_MeV = B_dim
    B_ame = B_AME[atom]
    return {
        "B_MeV": fmt(B_MeV), "B_AME_MeV": fmt(B_ame),
        "ratio_pred_over_AME": float(B_MeV / B_ame),
    }


def main() -> int:
    set_compute_dps(30)
    builder = WitnessBuilder("fr-pullback-cosh-h")
    builder.set_description(
        "Phase 5h: probe whether injecting Phase 5b's cosh(h) correction "
        "into the depth-stratified FR-pullback formula closes the "
        "residual 1.54× variance left after PR #826's K_3* = 4_1 "
        "resolution. Tests 6 injection points: α_2·cosh(h), α_3·cosh(h), "
        "both, global·cosh(h), α_2/cosh(h), and per-partition dim_q² "
        "weight×cosh(h). K_3* = 4_1 fixed; baseline 1.551× (PR #826)."
    )
    builder.set_content_block("conj:alpha-cosh-h-z-step-correction")
    builder.add_parameter("q_0", str(Q0))
    builder.add_parameter("K_3_star", "4_1")

    q_mp = mp.mpf(str(Q0))
    h_val = q_mp - 1 / q_mp
    cosh_h = mp.cosh(h_val)
    builder.add_parameter("h", str(h_val))
    builder.add_parameter("cosh_h", str(cosh_h))
    print(f"  q_0 = {float(Q0):.6f}, h = {float(h_val):.6f}, cosh(h) = {float(cosh_h):.6f}\n")

    variants = [
        "baseline",
        "v1_alpha_2_x_cosh_h",
        "v2_alpha_3_x_cosh_h",
        "v3_alpha_2_and_3_x_cosh_h",
        "v4_global_cosh_h",
        "v5_alpha_2_div_cosh_h",
        "v6_dim_q2_times_cosh_h",
    ]

    results = {}
    for variant in variants:
        per_atom = {}
        ratios = []
        for atom in ("D", "T", "3He", "4He"):
            r = compute_B_with_variant(atom, variant)
            if "deferred" not in r:
                per_atom[atom] = r
                ratios.append(r["ratio_pred_over_AME"])
        pos = [x for x in ratios if x > 0]
        var = max(pos) / min(pos) if len(pos) >= 2 else float("inf")
        results[variant] = {"per_atom": per_atom, "variance_max_min": var}

    baseline_var = results["baseline"]["variance_max_min"]
    print(f"=== Variant comparison (vs K_3*=4_1 baseline, variance {baseline_var:.4f}×) ===\n")
    print(f"  {'variant':<32} {'variance':>10}  vs baseline")
    for variant in variants:
        v = results[variant]["variance_max_min"]
        delta = (baseline_var - v) / baseline_var * 100 if v != float("inf") else 0.0
        print(f"  {variant:<32} {v:>10.4f}  ({delta:+.2f}%)")

    # Find best non-baseline variant
    non_baseline_variants = [v for v in variants if v != "baseline"]
    best_variant = min(non_baseline_variants,
                       key=lambda v: results[v]["variance_max_min"])
    best_var = results[best_variant]["variance_max_min"]
    delta_pct = (baseline_var - best_var) / baseline_var * 100

    print(f"\n  BEST cosh(h)-injection variant: {best_variant}")
    print(f"  Variance: {best_var:.4f}× (vs baseline {baseline_var:.4f}×, {delta_pct:+.2f}%)")
    if delta_pct > 1.0:
        verdict = f"cosh(h)-injection HELPS at {best_variant}; +{delta_pct:.1f}%"
    elif delta_pct > -1.0:
        verdict = (f"cosh(h)-injection is NEUTRAL (best variant {best_variant} "
                   f"changes variance by {delta_pct:+.1f}% — within noise)")
    else:
        verdict = (f"cosh(h)-injection REGRESSES at every tested variant; "
                   f"best is still {best_variant} at {delta_pct:+.1f}%")
    builder.add_data("verdict", verdict)
    builder.add_data("results", results)
    builder.add_data("best_variant", best_variant)
    builder.add_data("best_variance", float(best_var))
    builder.add_data("improvement_pct_vs_baseline", float(delta_pct))
    print(f"\n  Verdict: {verdict}")

    builder.add_assertion(
        "best_variance_finite",
        computed=float(best_var) if best_var != float("inf") else 1e9,
        expected=0.0,
        tolerance=10.0,
        unit="variance",
        source=(
            f"cosh(h) injection probe — all 6 variants completed; "
            f"best variant '{best_variant}' at variance {best_var:.4f}×."
        ),
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
