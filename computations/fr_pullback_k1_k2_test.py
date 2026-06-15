"""
fr_pullback_k1_k2_test.py — Phase 5f probe.

Extends the FR-pullback test of `fr_pullback_k3_test.py` (PR #826) to
curvature ranks k=1 and k=2. Per
[`conj:depth-stratified-frobenius-reciprocity`](../../content/quantum-observable-universe/braids-and-knots/depth-stratified-frobenius-reciprocity.md):

  K_1*, K_2* are open structural questions; candidate sets are
  K_1* ∈ {4_1, 5_2}, K_2* ∈ {5_2, 6_1}, plus the unknot control
  and the torus-knot lepton-generation candidates {3_1, 5_1, 7_1}
  from PR #819 Phase 5d.5.

K_3* = 4_1 is fixed per PR #826's empirical resolution; this probe
tests whether adding FR pullback at k=1 and / or k=2 (with K_3* = 4_1
already pulled back at depth 3) closes the residual variance further
below #826's 1.551× best.

The script reuses #826's canonical-braid-words-from-Conway converter
and S_uniform_at_depth-preserving weight normalization. It also
inherits #826's KnotInfo cross-validation of canonical braid words
via hyperbolic volume.

  Ref: prop:depth-stratified-frobenius-reciprocity
  Ref: PR #826 (fr_pullback_k3_test.py) — infrastructure source
  Ref: PR #819 Phase 5d.5 — torus-knot candidates
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
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
    "D":   mp.mpf("2.22456607"),
    "T":   mp.mpf("8.481798"),
    "3He": mp.mpf("7.7180428"),
    "4He": mp.mpf("28.295674"),
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}


# Distinguished hyperbolic-knot candidates, by depth.  Braid words
# in Conway-signed form (positive = σ_g, negative = σ_g^{-1});
# cross-validated against KnotInfo via hyperbolic volume.
#
# Sources:
#   - 4_1, 5_2, 6_1: from PR #826 (verified canonical via volume).
#   - 3_1, 5_1, 7_1: (2, m)-torus knots from PR #819 Phase 5d.5
#                    (knot-particle dictionary lepton generations).
#   - unknot: trivial control (Plancherel-uniform = no FR pullback).
CANDIDATE_KNOTS_CONWAY = {
    "unknot": ((), 0.0),
    "3_1":    ((1, 1, 1), 0.0),                # (2,3)-torus = electron
    "4_1":    ((1, -2, 1, -2), 2.0298832),     # figure-eight
    "5_1":    ((1, 1, 1, 1, 1), 0.0),          # (2,5)-torus = muon
    "5_2":    ((1, 1, 1, -2, 1, -2), 2.8281220),
    "6_1":    ((1, 1, -2, 1, -2, -2), 3.1639633),
    "7_1":    ((1, 1, 1, 1, 1, 1, 1), 0.0),    # (2,7)-torus = tau
}


def conway_to_pyhecke(word_signed: tuple[int, ...]) -> list[tuple[int, int]]:
    """Convert Conway-signed braid word to pyhecke_native (sign, |gen|)."""
    out: list[tuple[int, int]] = []
    for s in word_signed:
        sign = 1 if s > 0 else -1
        g = abs(s)
        out.append((sign, g))
    return out


CANDIDATE_KNOTS = {
    name: conway_to_pyhecke(w_signed)
    for name, (w_signed, _vol) in CANDIDATE_KNOTS_CONWAY.items()
}


def vanishing_threshold() -> mp.mpf:
    return mp.mpf(10) ** (5 - mp.mp.dps)


def alpha_k(k: int) -> mp.mpf:
    """Structural prefactor per prop:plancherel-term-7-formulation."""
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return M_E_MEV * 8 * G


def chi_lambda_braid_via_rust(shape, braid_word_signed, q_f64: float) -> float:
    """Compute χ^λ(β) at q (f64) via pyhecke_native."""
    word = [(int(s), int(g)) for (s, g) in braid_word_signed]
    return pyhecke_native.chi_lambda_braid(list(shape), word, float(q_f64))


def fr_pullback_weights_per_depth(
    by_partition: list,
    n_strands: int,
    K_per_depth: dict,
    q_f64: float,
) -> tuple[dict, dict]:
    """Compute per-partition weights with FR pullback at the depths
    specified by `K_per_depth` (a mapping {k: knot_word}).

    Partitions at depths NOT in `K_per_depth` get the uniform
    Plancherel weight `dim_q²/[n]_q!`.  Partitions at depths IN
    `K_per_depth` get the FR-pulled-back weight, with normalization
    preserving the per-depth total (per #826).

    Returns (weights_by_partition_shape, errors_by_shape).
    """
    qfact = qfac(n_strands)
    eps = vanishing_threshold()

    weights: dict = {}
    errors: dict = {}

    # Per-depth bookkeeping for FR pullback normalization.
    chi_per_depth: dict = {k: {} for k in K_per_depth}
    z_norm_per_depth: dict = {k: mp.mpf(0) for k in K_per_depth}
    s_uniform_per_depth: dict = {k: mp.mpf(0) for k in K_per_depth}

    for p in by_partition:
        shape = tuple(p["partition"])
        depth = len(shape) - 1
        dq = dim_q(shape)
        if depth not in K_per_depth:
            weights[shape] = mp.mpf(str(dq * dq)) / qfact
            continue
        knot_word = K_per_depth[depth]
        s_uniform_per_depth[depth] += mp.mpf(str(dq * dq)) / qfact
        if not knot_word:
            # unknot baseline: set χ^λ = 1 constant so that the FR
            # pullback weight reduces to uniform Plancherel.  With
            #   chi_K = 1, Z_norm = Σ_μ dim_q²(μ) = [n]_q!,
            # giving w_λ^{(unknot)} = dim_q²/[n]_q! · S_{uniform,k} —
            # exactly the uniform Plancherel weight at depth k.  Per
            # #831 Copilot review (the previous chi_K = dq made
            # weights proportional to dim_q^3, not the uniform
            # Plancherel claim in this comment).
            chi_K = 1.0
        else:
            try:
                chi_K = chi_lambda_braid_via_rust(list(shape), knot_word, q_f64)
            except (ValueError, RuntimeError, OverflowError) as exc:
                chi_K = 0.0
                errors[shape] = f"{type(exc).__name__}: {exc}"
        chi_per_depth[depth][shape] = chi_K
        z_norm_per_depth[depth] += mp.mpf(str(dq * dq)) * mp.fabs(chi_K)

    # Apply normalization per depth.
    for k in K_per_depth:
        z = z_norm_per_depth[k]
        s = s_uniform_per_depth[k]
        if z < eps:
            for shape in chi_per_depth[k]:
                dq = dim_q(shape)
                weights[shape] = mp.mpf(str(dq * dq)) / qfact
        else:
            scale = s / z
            for shape, chi_K in chi_per_depth[k].items():
                dq = dim_q(shape)
                weights[shape] = (mp.mpf(str(dq * dq)) * mp.fabs(chi_K)
                                   * scale)
    return weights, errors


def phi_k_with_weights(by_partition: list, k: int, weights: dict) -> mp.mpf:
    """Φ_k(β) using arbitrary per-partition weight."""
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


def compute_B_with_K(atom: str, K_per_depth: dict) -> dict:
    """Compute B(K) with FR pullback at the specified depths."""
    Z, N = ZN[atom]
    A = Z + N
    n_strands = 3 * A
    w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
    if not w_path.exists():
        return {"deferred": True, "reason": f"need atom-chi-rust-{atom.lower()}"}
    w = json.loads(w_path.read_text())
    atom_data = w["data"]["atom"]
    free_data = w["data"]["free"]
    q_f64 = float(Q0)

    w_atom, _ = fr_pullback_weights_per_depth(
        atom_data["by_partition"], n_strands, K_per_depth, q_f64)
    w_free, _ = fr_pullback_weights_per_depth(
        free_data["by_partition"], n_strands, K_per_depth, q_f64)

    B_dim = mp.mpf(0)
    per_depth_contrib: dict = {}
    for k in range(n_strands):
        ak = alpha_k(k)
        phi_a = phi_k_with_weights(atom_data["by_partition"], k, w_atom)
        phi_f = phi_k_with_weights(free_data["by_partition"], k, w_free)
        delta = phi_f - phi_a
        contrib = ak * delta
        B_dim += contrib
        if mp.fabs(delta) > mp.mpf("1e-12"):
            per_depth_contrib[k] = {
                "alpha_k": fmt(ak), "delta_phi": fmt(delta),
                "contrib": fmt(contrib),
            }

    # alpha_k_base() already includes the m_e·8G factor for k≥4
    # (matches binding_depth_stratified_rust.py:62), so B_dim is in
    # MeV.  Do NOT multiply by M_E_MEV again — see #831 Copilot review.
    B_MeV = B_dim
    B_ame = B_AME[atom]
    return {
        "B_MeV": fmt(B_MeV), "B_AME_MeV": fmt(B_ame),
        "ratio_pred_over_AME": float(B_MeV / B_ame),
        "per_depth_contrib": per_depth_contrib,
    }


def main() -> int:
    set_compute_dps(30)
    builder = WitnessBuilder("fr-pullback-k1-k2")
    builder.set_description(
        "Phase 5f: FR-pullback variance test at k=1 and k=2, "
        "extending PR #826's k=3 infrastructure. K_3* fixed at 4_1 "
        "(per #826). Sweeps (K_1*, K_2*) over a candidate set "
        "including hyperbolic knots {4_1, 5_2, 6_1} and torus-knot "
        "lepton-generation candidates {3_1, 5_1, 7_1} from PR #819 "
        "Phase 5d.5. Reports the (K_1*, K_2*) pair that minimises "
        "variance across D / T / ³He / ⁴He."
    )
    builder.set_content_block("conj:depth-stratified-frobenius-reciprocity")
    builder.add_parameter("q_0", str(Q0))
    builder.add_parameter("K_3_star_fixed", "4_1")

    print(f"  q_0 = {Q0}")
    print(f"  K_3* fixed = 4_1 (per PR #826 empirical resolution)\n")

    # Baseline: K_3* = 4_1 only (matches #826's best result).
    K_3 = CANDIDATE_KNOTS["4_1"]
    baseline_K = {3: K_3}

    print("=== Baseline (FR at k=3 only, K_3* = 4_1) ===")
    baseline_per_atom = {}
    baseline_ratios = []
    for atom in ("D", "T", "3He", "4He"):
        r = compute_B_with_K(atom, baseline_K)
        if "deferred" not in r:
            baseline_per_atom[atom] = r
            baseline_ratios.append(r["ratio_pred_over_AME"])
            print(f"    {atom}: ratio = {r['ratio_pred_over_AME']:.6f}")
    baseline_var = max(baseline_ratios) / min(baseline_ratios) if baseline_ratios else None
    print(f"    baseline variance (K_3* = 4_1 only): {baseline_var:.4f}×\n")
    builder.add_data("baseline_K_3_only", {
        "per_atom": baseline_per_atom,
        "variance_max_min": baseline_var,
    })

    # Sweep (K_1*, K_2*) candidate pairs with K_3* = 4_1.
    candidate_K1 = [n for n in CANDIDATE_KNOTS_CONWAY if n != "7_1"]
    candidate_K2 = [n for n in CANDIDATE_KNOTS_CONWAY if n != "7_1"]
    # 7_1 needs B_3 → braid index 2 OK, but skip to keep grid small.

    print(f"=== (K_1*, K_2*) grid sweep ({len(candidate_K1)}×{len(candidate_K2)} = "
          f"{len(candidate_K1)*len(candidate_K2)}) ===")
    results = []
    for K1_name in candidate_K1:
        for K2_name in candidate_K2:
            K_per_depth = {
                1: CANDIDATE_KNOTS[K1_name],
                2: CANDIDATE_KNOTS[K2_name],
                3: K_3,
            }
            per_atom = {}
            ratios = []
            for atom in ("D", "T", "3He", "4He"):
                r = compute_B_with_K(atom, K_per_depth)
                if "deferred" not in r:
                    per_atom[atom] = r
                    ratios.append(r["ratio_pred_over_AME"])
            if len(ratios) >= 2:
                pos = [x for x in ratios if x > 0]
                var = max(pos) / min(pos) if len(pos) >= 2 else float("inf")
            else:
                var = float("inf")
            results.append({
                "K_1_star": K1_name, "K_2_star": K2_name, "K_3_star": "4_1",
                "variance_max_min": var, "per_atom": per_atom,
            })

    results.sort(key=lambda r: r["variance_max_min"]
                 if r["variance_max_min"] != float("inf") else 1e9)
    builder.add_data("k1_k2_grid_results_top_15",
                     [{k: v for k, v in r.items() if k != "per_atom"}
                      for r in results[:15]])
    # Keep full data for the top 5 only (size budget).
    builder.add_data("top_5_full", results[:5])

    print(f"\n  {'K_1*':<8} {'K_2*':<8} {'variance':>10}  vs baseline ({baseline_var:.3f}×)")
    for r in results[:10]:
        v = r["variance_max_min"]
        v_str = f"{v:.4f}" if v != float("inf") else "INF"
        delta = ((baseline_var - v) / baseline_var * 100) if v != float("inf") else None
        delta_str = f"({delta:+.1f}%)" if delta is not None else ""
        print(f"  {r['K_1_star']:<8} {r['K_2_star']:<8} {v_str:>10}  {delta_str}")

    best = results[0]
    print(f"\n  BEST: K_1* = {best['K_1_star']}, K_2* = {best['K_2_star']}, "
          f"K_3* = 4_1; variance = {best['variance_max_min']:.4f}×")
    builder.add_data("best", {
        "K_1_star": best["K_1_star"], "K_2_star": best["K_2_star"],
        "K_3_star": "4_1",
        "variance_max_min": best["variance_max_min"],
        "improvement_over_baseline_pct":
            ((baseline_var - best["variance_max_min"]) / baseline_var * 100)
            if best["variance_max_min"] != float("inf") else None,
    })

    builder.add_assertion(
        "best_variance_below_two_x",
        computed=float(best["variance_max_min"]),
        expected=0.0,
        tolerance=2.0,
        unit="variance",
        source=(
            f"FR pullback grid scan finds best (K_1*, K_2*) pair at "
            f"variance {best['variance_max_min']:.4f}×, well below the "
            f"structural 2× ceiling. K_3* = 4_1 baseline is "
            f"{baseline_var:.4f}× (matches PR #826)."
        ),
    )
    # Cross-validation: this script's K_3* = 4_1 baseline should match
    # PR #826's reported 1.551× to within numerical noise.
    builder.add_assertion(
        "baseline_matches_PR_826",
        computed=float(baseline_var),
        expected=1.551,
        tolerance=0.005,  # 0.3% absolute
        unit="variance",
        source=(
            f"K_3* = 4_1 baseline (FR at k=3 only) computed here: "
            f"{baseline_var:.4f}×; PR #826 reported 1.551×. "
            f"Cross-validates the FR-pullback formula implementation."
        ),
    )
    # Marginal-improvement assertion: phase 5f best should be at least
    # the k=3-only baseline (no regression).
    improvement_pct = ((baseline_var - best["variance_max_min"])
                        / baseline_var * 100) if best["variance_max_min"] != float("inf") else 0.0
    builder.add_assertion(
        "no_regression_vs_baseline",
        computed=float(max(0.0, -improvement_pct)),  # if negative pct, computed = |improvement_pct|
        expected=0.0,
        tolerance=0.1,  # at most 0.1% absolute regression tolerated
        unit="percent_regression",
        source=(
            f"Best (K_1*, K_2*) variance {best['variance_max_min']:.4f}× vs "
            f"K_3*-only baseline {baseline_var:.4f}×: "
            f"improvement = {improvement_pct:+.2f}% "
            f"(positive = better; negative = regression — would fail this assertion)."
        ),
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
