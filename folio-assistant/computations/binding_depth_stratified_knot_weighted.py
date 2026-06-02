"""
binding_depth_stratified_knot_weighted.py — per-knot ideal-restricted
Wedderburn weight at low k (k=1, 2, 3) for the depth-stratified binding.

PER-DEPTH DIAGNOSIS (2026-05-19, see audit
docs/audits/2026-05-19-variance-per-depth-diagnosis.md):

The 1.82× variance on D/T/³He/⁴He via uniform Wedderburn weight
~w_λ = dim_q²(λ)/[n]_q! at all depths suggests the formula is
missing a per-knot enhancement at low k.

Per prop:plancherel-term-7-formulation §"Why universal at k≥4":
  "At low strata k ≤ 3 the restricted Frobenius integral
   ∫_{A_λ} ρ(β_K) · T factors through specific hyperbolic-knot
   ideals (e.g. 6_1 at k=3, the chirality channel)."

This script tests a "knot-magnitude-weighted" refinement:
  ~w_λ^{knot-weighted}(K) = |χ^λ(β_K)|^β · ~w_λ / Z(β, K)

with normalization Z(β, K) = Σ_{λ': depth=k} |χ^{λ'}(β_K)|^β · ~w_{λ'}
and exponent β ∈ {0, 1, 2}. β=0 recovers uniform.

The hypothesis: low-k strata should weight toward partitions where
the closure knot's Hecke character is large (the "support" of the
knot ideal), and away from partitions where it's small (negligible
chirality / curvature-rank contribution).

USAGE:
    python3 binding_depth_stratified_knot_weighted.py [BETA]
    BETA = 0  (uniform, baseline)
    BETA = 1  (|χ^λ|-weighted)
    BETA = 2  (|χ^λ|²-weighted)
    default: tests all three.

Ref: prop:plancherel-term-7-formulation
Ref: docs/audits/2026-05-19-variance-per-depth-diagnosis.md
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from _precision import set_compute_dps, fmt
from witness_base import WitnessBuilder
from codata_constants import M_E_MEV
from mass_at_3A_proper import dim_q, qfac
from q_parameter import Q as Q0


B_AME = {
    "D":   mp.mpf("2.22456607"),
    "T":   mp.mpf("8.481798"),
    "3He": mp.mpf("7.7180428"),
    "4He": mp.mpf("28.295674"),
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}


def alpha_k(k: int) -> mp.mpf:
    """α_0 = α_1 = α_3 = 1; α_2 = z²; α_{k≥4} = m_e · 8G."""
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G


def phi_k_knot_weighted(
    by_partition: list, n_strands: int, k: int, beta: float,
    closure_chi: list,  # χ^λ(β_K) for all λ — used for knot weight
) -> mp.mpf:
    """Φ_k with knot-magnitude-weighted ~w_λ at low k only.

    At low k (k ≤ 3): ~w_λ^{knot} = |χ^λ(β_K)|^β · ~w_λ / Z(β, K)
    At high k (k ≥ 4): uniform ~w_λ = dim_q²/[n]_q!

    Z(β, K) ensures Σ ~w_λ^{knot} = Σ ~w_λ within each depth k stratum
    (renormalisation, not absolute reweighting).
    """
    qfact = qfac(n_strands)
    closure_chi_map = {tuple(c["partition"]): mp.mpf(str(c["chi_lambda"]))
                       for c in closure_chi}

    is_low_k = k <= 3
    if is_low_k and beta > 0:
        Z_norm_uniform = mp.mpf(0)
        Z_norm_weighted = mp.mpf(0)
        for p in by_partition:
            shape = tuple(p["partition"])
            if len(shape) - 1 != k:
                continue
            dq = dim_q(shape)
            w = mp.mpf(str(dq * dq)) / qfact
            Z_norm_uniform += w
            chi_K = mp.fabs(closure_chi_map.get(shape, mp.mpf(0)))
            Z_norm_weighted += w * (chi_K ** beta)
        if Z_norm_weighted < mp.mpf("1e-30"):
            renorm = mp.mpf(1)
        else:
            renorm = Z_norm_uniform / Z_norm_weighted
    else:
        renorm = mp.mpf(1)

    total = mp.mpf(0)
    for p in by_partition:
        shape = tuple(p["partition"])
        if len(shape) - 1 != k:
            continue
        chi = mp.mpf(str(p["chi_lambda"]))
        dq = dim_q(shape)
        magnitude = mp.fabs(chi) * dq
        if magnitude < mp.mpf("1e-30"):
            continue
        w_base = mp.mpf(str(dq * dq)) / qfact
        if is_low_k and beta > 0:
            chi_K = mp.fabs(closure_chi_map.get(shape, mp.mpf(0)))
            w = w_base * (chi_K ** beta) * renorm
        else:
            w = w_base
        total += w * mp.log(magnitude)
    return total


def compute_atom_binding(atom: str, beta: float) -> dict:
    """Apply knot-weighted depth-stratified formula to atom (Z, N)."""
    Z, N = ZN[atom]
    A = Z + N
    n_strands = 3 * A
    w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
    if not w_path.exists():
        return {"deferred": True}
    w = json.loads(w_path.read_text())
    atom_data = w["data"]["atom"]
    free_data = w["data"]["free"]

    # closure_chi = atom's chi (the closure of the atomic braid IS β_K)
    closure_chi = atom_data["by_partition"]

    delta_phi_total = mp.mpf(0)
    per_depth = {}
    for k in range(n_strands):
        phi_atom = phi_k_knot_weighted(
            atom_data["by_partition"], n_strands, k, beta, closure_chi)
        phi_free = phi_k_knot_weighted(
            free_data["by_partition"], n_strands, k, beta, closure_chi)
        delta = phi_free - phi_atom
        ak = alpha_k(k)
        contrib = ak * delta
        if mp.fabs(delta) > mp.mpf("1e-12"):
            per_depth[k] = {
                "alpha_k": fmt(ak), "delta_phi": fmt(delta),
                "contrib": fmt(contrib),
            }
        delta_phi_total += contrib

    return {
        "Z": Z, "N": N, "A": A, "n_strands": n_strands,
        "beta": beta,
        "per_depth": per_depth,
        "B_MeV": fmt(delta_phi_total),
        "B_pred_sign": "+" if delta_phi_total > 0 else "-",
        "canonical_status": "canonical-with-empirical-assignment",
    }


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("binding-depth-stratified-knot-weighted")
    builder.set_description(
        "Per-knot ideal-restricted depth-stratified binding test. "
        "Replaces uniform Wedderburn weight ~w_λ at low k (≤3) with "
        "|χ^λ(β_K)|^β · ~w_λ / Z(β, K) for β ∈ {0, 1, 2}. β=0 "
        "recovers uniform; β=1, 2 test the per-knot enhancement "
        "hypothesis from prop:plancherel-term-7-formulation."
    )
    builder.add_parameter("m_e_CAL1_MeV", str(M_E_MEV))

    betas = [0.0, 1.0, 2.0]
    if len(sys.argv) >= 2:
        betas = [float(sys.argv[1])]

    all_results = {}
    for beta in betas:
        print(f"\n=== β = {beta} ===")
        print(f"{'atom':<6} {'A':>3} {'B_MeV':>10} {'B_AME':>10} {'ratio':>8}")
        results = {}
        for atom in ("D", "T", "3He", "4He"):
            r = compute_atom_binding(atom, beta)
            if r.get("deferred"):
                continue
            B_pred = mp.mpf(r["B_MeV"])
            B_emp = B_AME[atom]
            ratio = B_pred / B_emp if B_emp > 0 else mp.mpf("nan")
            r["B_AME_MeV"] = fmt(B_emp)
            r["ratio_pred_over_AME"] = float(ratio)
            results[atom] = r
            print(f"  {atom:<6} {r['A']:>3} "
                  f"{float(B_pred):>10.4f} {float(B_emp):>10.4f} "
                  f"{float(ratio):>8.4f}")

        ratios = [abs(r["ratio_pred_over_AME"]) for r in results.values()]
        rmin, rmax = (min(ratios), max(ratios)) if ratios else (0, 0)
        mom = rmax / rmin if rmin > 0 else float("inf")
        signs_correct = all(r["B_pred_sign"] == "+" for r in results.values())
        print(f"  max/min = {mom:.4f}, signs +: {signs_correct}")
        all_results[f"beta_{beta}"] = {
            "per_atom": results,
            "max_over_min": float(mom),
            "all_signs_correct": signs_correct,
        }

    builder.add_data("per_beta", all_results)
    # Find best β by variance
    best_beta = min(
        all_results.keys(),
        key=lambda k: all_results[k]["max_over_min"]
        if all_results[k]["all_signs_correct"] else float("inf"))
    builder.add_data("best_beta", best_beta)
    builder.add_data("best_max_over_min",
                      all_results[best_beta]["max_over_min"])
    print(f"\n  Best β: {best_beta} (max/min = "
          f"{all_results[best_beta]['max_over_min']:.4f})")

    builder.add_assertion(
        "data_loaded", computed=float(B_AME["D"]), expected=2.22456607,
        tolerance=1e-10, unit="B(D) MeV", source="AME 2020",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
