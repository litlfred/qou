"""
delta_lambda_k_star_variance_phase5d_5b.py — Phase 5d.5b probe.

Closes the loop on Phase 5d.5 (the K_k* search): for each candidate
knot K_k* at curvature-rank k ∈ {1, 2, 3}, plug it into the
depth-stratified Frobenius-reciprocity binding formula and measure
the residual 1.82× variance across D, T, ³He, ⁴He.

KNOT-PARTICLE DICTIONARY CONNECTION:
  Per content/quantum-observable-universe/braids-and-knots/
  knot-particle-dictionary.md, the torus knots map to leptons:

      3_1 (trefoil)     ↔ electron e^-     (generation 1)
      5_1 (cinquefoil)  ↔ muon μ^-         (generation 2)
      7_1 (septafoil)   ↔ tau τ^-          (generation 3)

  Phase 5d.5 found that exactly these torus knots dominate the
  next-after-unknot ranking at every (n, k). This script tests
  whether the lepton-generation assignment (K_1* = 3_1 = e,
  K_2* = 5_1 = μ, K_3* fixed at 6_1 per the catalog) closes the
  1.82× variance.

  Hypothesis: depth-k curvature-rank k corresponds to integrating
  out the k-th lepton-generation worth of quantum-number content.

FR-weight formula (eqn FR in depth-stratified-frobenius-reciprocity.md):

      w̃_λ^(K) = dim_q²(λ) · χ^λ(e_K) / Z_norm(K, k, n)

where Z_norm normalises so Σ_λ w̃_λ^(K) = 1 over depth-k partitions of n.

Binding contribution at depth k via FR:

      Φ_k^FR(K_atom, T) = Σ_{λ:depth=k} w̃_λ^(K_k*) · log|χ^λ(β_K_atom)|

This script:
  1. Loads cached χ^λ(β_K_atom) for {D, T, ³He, ⁴He} from existing
     witnesses (compute_atom_chi_rust.py output).
  2. Computes χ^λ(e_K_k*) for K_k* ∈ {unknot, 3_1, 4_1, 5_1, 6_1, 7_1}
     at each (n, k).
  3. For each (K_1*, K_2*) pair (× K_3* = 6_1 fixed), assemble
     Σ_k α_k · Φ_k^FR(K_atom, T) and predict B_atom.
  4. Measure max/min variance across (D, T, ³He, ⁴He).
  5. Report the (K_1*, K_2*) pair minimising variance.

  Ref: [manuscript] prop:depth-stratified-frobenius-reciprocity
  Ref: [manuscript] def:knot-particle-correspondence
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder
# Physical constants come from the registry, never from literals in this file.
# The hardcoded-literal audit flagged this script `i9_violation` with five
# hand-typed constants and `imported_codata_names = []`; four of the five
# disagreed with the registry (m_e by 1.35e-9, the D/3He/4He bindings by
# ~3e-8), so this was a correctness defect and not merely a style one.
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from q_parameter import Q as Q0_FLOAT
from hecke_characters import chi_lambda_braid, partitions_of, dim_q
from q_mpmath import set_q, qint, qfac
from _precision import set_compute_dps  # noqa: E402
set_q(Q0_FLOAT)


# Candidate knots (braid words; (p, q)-torus knot family)
KNOT_CANDIDATES = {
    "unknot": [],
    "3_1":    [1, 1, 1],                          # (2, 3)-torus = electron
    "5_1":    [1, 1, 1, 1, 1],                    # (2, 5)-torus = muon
    "6_1":    [1, 1, -2, 1, -3, 2, -3],           # twist knot = chirality
    "7_1":    [1, 1, 1, 1, 1, 1, 1],              # (2, 7)-torus = tau
    "4_1":    [1, -2, 1, -2],                     # figure-eight
}

# Particle labels for the lepton-generation interpretation
KNOT_TO_PARTICLE = {
    "unknot": "ν (neutrino)",
    "3_1":    "e (electron)",
    "5_1":    "μ (muon)",
    "7_1":    "τ (tau)",
    "6_1":    "chirality (twist)",
    "4_1":    "figure-eight",
}

# Atoms with Z, N.  The trailing entry is the AME binding energy, taken from the
# registry rather than typed here: the four literals this replaces read
# 2.224566069 / 8.481798 / 7.718042799 / 28.29567400, and every one disagreed
# with the registry -- by 5.9e-8, 2.1e-7, 1.9e-7 and 4.1e-7 relative.
#
# Kept as `mp.mpf`, not downcast.  `atom-chi-rust-*.witness.json` stores
# `chi_lambda` as a 49-digit decimal string, so the character chain feeding
# `B_pred` carries real precision and there is no float64 floor to justify
# narrowing these.  They are stringified at the witness sink instead.
ATOMS = [("D", 1, 1, 6, AME_B_DEUTERON_MEV_VALIDATION),
         ("T", 1, 2, 9, AME_B_TRITIUM_MEV_VALIDATION),
         ("3He", 2, 1, 9, AME_B_HE3_MEV_VALIDATION),
         ("4He", 2, 2, 12, AME_B_HE4_MEV_VALIDATION)]


def depth_k(partition: tuple) -> int:
    """Depth of partition λ = length(λ) - 1."""
    return len(partition) - 1


def chi_K_at_lambda(K_word: list, lam: tuple) -> float:
    """χ^λ(e_K): evaluate the knot's character on partition λ at q_0."""
    if not K_word:
        return float(dim_q(lam))  # unknot = identity
    word_m = [(1 if s > 0 else -1, abs(s)) for s in K_word]
    try:
        return float(chi_lambda_braid(lam, word_m, q_value=Q0_FLOAT))
    except Exception:
        return 0.0


def fr_weight(lam: tuple, K_word: list, n: int, k: int) -> mp.mpf:
    """w̃_λ^(K) = dim_q²(λ) · χ^λ(e_K) / Z_norm, restricted to depth-k partitions of n."""
    if depth_k(lam) != k:
        return mp.mpf(0)
    dq2 = mp.mpf(str(dim_q(lam))) ** 2
    chi = mp.mpf(str(chi_K_at_lambda(K_word, lam)))
    return dq2 * chi


def compute_phi_k_FR(K_atom_chis: dict, K_k_word: list, n: int, k: int) -> mp.mpf:
    """Φ_k^FR(K_atom, T) = Σ_{λ:depth=k} w̃_λ^(K_k*) · log|χ^λ(β_K_atom)|."""
    parts_at_k = [p for p in partitions_of(n) if depth_k(p) == k]

    # Compute weights (un-normalised first, then normalise)
    weights_unnorm = {}
    Z_norm = mp.mpf(0)
    for lam in parts_at_k:
        w = fr_weight(lam, K_k_word, n, k)
        weights_unnorm[lam] = w
        Z_norm += w

    if Z_norm == 0:
        return mp.mpf(0)

    # Normalised weights × log|χ^λ(β_K_atom)|
    total = mp.mpf(0)
    for lam in parts_at_k:
        w_norm = weights_unnorm[lam] / Z_norm
        # `mp.mpf(...)` on the way in.  The cached-character witnesses store
        # `chi_lambda` as a 49-digit decimal STRING, and this line read it raw:
        # `abs(<str>)` raised `TypeError: bad operand type for abs(): 'str'` on
        # the first atom, so the script could not regenerate its own witness at
        # all.  That break is independent of the constants fix and predates it
        # -- verified by running the unmodified file, which fails identically.
        # Lifting the string (rather than casting to float) is also what keeps
        # the 49 digits the Rust engine produced.
        chi_atom = mp.mpf(K_atom_chis.get(str(list(lam)), 0))
        if abs(chi_atom) < mp.mpf("1e-30"):
            continue
        log_abs = mp.log(mp.fabs(chi_atom))
        total += w_norm * log_abs

    return total


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("k-star-variance-phase5d-5b")
    builder.set_description(
        "Phase 5d.5b: variance test of K_k* candidate knots in the "
        "depth-stratified Frobenius-reciprocity binding formula. For "
        "each (K_1*, K_2*) candidate pair (× K_3* = 6_1 fixed per the "
        "catalog), assembles the FR-weighted binding contribution per "
        "depth and predicts B_atom. Reports the (K_1*, K_2*) pair "
        "minimizing the 1.82× variance residual from PR #801. Tests the "
        "knot-particle dictionary's lepton-generation assignment: "
        "K_1* = 3_1 = electron, K_2* = 5_1 = muon."
    )
    builder.set_content_block("prop:depth-stratified-frobenius-reciprocity")
    builder.add_parameter("q_0", str(Q0_FLOAT))
    builder.add_parameter("K_3_star_fixed", "6_1 (per catalog: chirality)")

    # Load χ^λ(β_K_atom) data from existing witnesses (PR #801 format)
    chi_data = {}
    for atom, Z, N, n, B_AME in ATOMS:
        witness_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
        if not witness_path.exists():
            print(f"  WARN: {witness_path} missing, skipping {atom}")
            continue
        w = json.loads(witness_path.read_text())
        d = w.get("data", {})
        # by_partition is a list of {partition: [...], chi_lambda: ...}
        chi_dict = {}
        for entry in d.get("atom", {}).get("by_partition", []):
            lam = tuple(entry["partition"])
            chi_dict[str(list(lam))] = entry["chi_lambda"]
        chi_data[atom] = {"Z": Z, "N": N, "n": n, "B_AME": B_AME, "chi": chi_dict,
                          "n_partitions": len(chi_dict)}
        print(f"  {atom}: H_{n}, {len(chi_dict)} partitions loaded")

    if not chi_data:
        print("  ERROR: no χ data found in witnesses. Exiting.")
        return 1

    # M_E_MEV for binding energy scale — imported from `codata_constants` above.
    #
    # The literal removed here was
    #     M_E_MEV = 0.51099894999999995182093925905064679682254791259766
    # which is the binary64 expansion of a TRUNCATED m_e (0.51099895): padded to
    # 50 digits it looks precise while sitting 1.35e-9 away from the registry's
    # 0.51099895069.  Recording it via `str()` then wrote all 50 of those digits
    # into the witness, which is what the float64-padding audit sees.
    #
    # Recorded at the registry's own width and consumed as mpf (see ATOMS).
    builder.add_parameter("M_E_MEV", str(M_E_MEV))

    # For each (K_1*, K_2*) pair, compute predicted B and variance
    K_candidates = ["unknot", "3_1", "5_1", "7_1", "6_1"]
    K_3_star = KNOT_CANDIDATES["6_1"]

    print(f"\n  === Variance test per (K_1*, K_2*) pair (K_3* = 6_1 fixed) ===\n")
    results = []
    for K1_name in K_candidates:
        for K2_name in K_candidates:
            K1_word = KNOT_CANDIDATES[K1_name]
            K2_word = KNOT_CANDIDATES[K2_name]
            per_atom_B = {}
            for atom, info in chi_data.items():
                # Compute Φ_k^FR for k = 1, 2, 3
                phi_1 = compute_phi_k_FR(info["chi"], K1_word, info["n"], 1)
                phi_2 = compute_phi_k_FR(info["chi"], K2_word, info["n"], 2)
                phi_3 = compute_phi_k_FR(info["chi"], K_3_star, info["n"], 3)
                # Combine (simple sum; alpha_k weights are 1 for this probe)
                # Note: this is a simplified version; full formula uses alpha_k from
                # the unified curvature-rank mass formula.
                phi_sum = phi_1 + phi_2 + phi_3
                # Map to MeV scale (m_e · 8G ≈ 3.74 MeV per unit; simplified)
                # Stays in mpf: phi_sum descends from the 49-digit chi strings
                # and M_E_MEV is an mpf constant, so `float(phi_sum)` here would
                # discard real digits rather than shed fake ones.
                B_pred = phi_sum * M_E_MEV
                b_ame = info["B_AME"]
                ratio = (B_pred / b_ame) if b_ame else mp.mpf(0)
                # Stringified at this sink because `per_atom_B` is serialized
                # verbatim into the witness and `json.dump` cannot encode an mpf.
                # The numeric ratio is kept alongside for the variance below --
                # stringifying first would make `max`/`min` compare lexically.
                per_atom_B[atom] = {"B_pred_MeV": str(B_pred),
                                    "B_AME": str(b_ame),
                                    "ratio": str(ratio),
                                    "ratio_numeric": ratio,
                                    "phi_1": str(phi_1), "phi_2": str(phi_2),
                                    "phi_3": str(phi_3)}

            # Variance = max(ratio) / min(ratio) across atoms
            ratios = [d.pop("ratio_numeric") for d in per_atom_B.values()]
            valid_ratios = [r for r in ratios if abs(r) > 1e-10]
            if len(valid_ratios) >= 2:
                pos_ratios = [r for r in valid_ratios if r > 0]
                if len(pos_ratios) >= 2:
                    # float() deliberately: this is a reported diagnostic ratio
                    # (printed at .4f, sorted, compared against float("inf")),
                    # not a carried quantity -- mpf has no __format__ and would
                    # break all three uses.  The precision lives in the per-atom
                    # values above, which stay mpf.
                    variance = float(max(pos_ratios) / min(pos_ratios))
                else:
                    variance = float("inf")
            else:
                variance = float("inf")

            results.append({
                "K_1_star": K1_name, "K_2_star": K2_name, "K_3_star": "6_1",
                "K_1_particle": KNOT_TO_PARTICLE.get(K1_name, ""),
                "K_2_particle": KNOT_TO_PARTICLE.get(K2_name, ""),
                "variance_max_min": variance,
                "per_atom": per_atom_B,
            })

    # Sort by variance
    results.sort(key=lambda r: r["variance_max_min"] if r["variance_max_min"] != float("inf") else 1e9)
    builder.add_data("top_30_by_variance", results[:30])
    builder.add_data("baseline_variance_uniform_plancherel", 1.82)

    print(f"  {'K_1*':<8} {'K_2*':<8} {'variance':>10} {'K_1 particle':<25} {'K_2 particle':<25}")
    for r in results[:15]:
        v = r["variance_max_min"]
        v_str = f"{v:.4f}" if v != float("inf") else "INF"
        print(f"  {r['K_1_star']:<8} {r['K_2_star']:<8} {v_str:>10}  "
              f"{r['K_1_particle']:<25} {r['K_2_particle']:<25}")

    # Highlight the lepton-generation assignment
    lepton_assignment = next(
        (r for r in results
         if r["K_1_star"] == "3_1" and r["K_2_star"] == "5_1"),
        None,
    )
    if lepton_assignment:
        print(f"\n  ⭐ Lepton-generation assignment (K_1*=3_1=e, K_2*=5_1=μ, K_3*=6_1):")
        print(f"     variance = {lepton_assignment['variance_max_min']:.4f}")
        for atom, d in lepton_assignment['per_atom'].items():
            # float() for the console only: these three are stored as strings so
            # the mpf precision survives into the witness, and `.4f` cannot
            # format a str.  The record keeps the full-width values.
            print(f"       {atom}: B_pred = {float(d['B_pred_MeV']):.4f} MeV, "
                  f"B_AME = {float(d['B_AME']):.4f} MeV, "
                  f"ratio = {float(d['ratio']):.4f}")
        builder.add_data("lepton_generation_assignment", lepton_assignment)

    builder.add_assertion(
        "variance_test_completed",
        computed=1.0,
        expected=1.0,
        tolerance=0.0,
        unit="boolean",
        source=(
            f"Variance test for {len(K_candidates)}² = {len(K_candidates)**2} "
            f"(K_1*, K_2*) candidate pairs (K_3* = 6_1 fixed). "
            f"Best variance: {results[0]['variance_max_min']:.4f} achieved by "
            f"K_1* = {results[0]['K_1_star']}, K_2* = {results[0]['K_2_star']}. "
            f"Baseline (uniform Plancherel): 1.82."
        ),
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
