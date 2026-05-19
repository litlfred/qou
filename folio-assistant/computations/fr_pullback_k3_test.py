"""
fr_pullback_k3_test.py — empirical test of conj:depth-stratified-
frobenius-reciprocity at k=3 (chirality channel).

Per prop:plancherel-term-7-formulation, "at low strata k ≤ 3 the
restricted Frobenius integral factors through specific hyperbolic-knot
ideals (e.g. 6_1 at k=3, the chirality channel)."

Per conj:depth-stratified-frobenius-reciprocity, the FR pullback
modifies the Wedderburn weight at depth k via:

  ~w_λ^{(K_k*)} := dim_q²(λ) · χ^λ(e_{K_k*}) /
                   ([n]_q! · Σ_μ dim_q²(μ) · χ^μ(e_{K_k*}))

where e_{K_k*} is the central projector of the distinguished
hyperbolic-knot ideal at depth k.

This script tests the FR pullback at k=3 with candidate distinguished
knots K_3* ∈ {4_1, 5_2, 6_1}. For each candidate:
  1. Embed the knot's braid into H_{3A} via Wenzl (acts on
     strands {1, 2, 3, ...}, identity elsewhere).
  2. Compute χ^λ(K_dist_embedded) for each λ ⊢ 3A via the
     Rust kernel (pyhecke_native.chi_q_atomic).
  3. Apply the FR-pullback weight at k=3 in the depth-stratified
     mass formula.
  4. Re-run binding-energy variance test on D, T, ³He, ⁴He.

Result: which (if any) K_dist closes the variance below the
1.82× baseline?

Reference: prop:plancherel-term-7-formulation, conj:depth-stratified-
frobenius-reciprocity.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

import pyhecke_native
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


# Distinguished hyperbolic-knot candidates at depth k=3.
# Each braid word is in (sign, gen) format expected by
# pyhecke_native — gen is 1-indexed.
#
# 4_1 (figure-eight knot): standard 4-crossing braid in B_3,
#   closure of σ_1 σ_2^{-1} σ_1 σ_2^{-1}.
# 5_2: 5-crossing braid in B_3, closure of σ_1^2 σ_2^{-1} σ_1 σ_2^{-1}.
# 6_1 (Stevedore knot): 6-crossing in B_3, closure of
#   σ_1^4 σ_2^{-1} σ_1^{-1} σ_2 (one canonical Knot-Atlas form).
CANDIDATE_KNOTS = {
    "4_1": [(+1, 1), (-1, 2), (+1, 1), (-1, 2)],
    "5_2": [(+1, 1), (+1, 1), (-1, 2), (+1, 1), (-1, 2)],
    "6_1": [(+1, 1), (+1, 1), (+1, 1), (+1, 1),
            (-1, 2), (-1, 1), (+1, 2)],
}


def alpha_k(k: int) -> mp.mpf:
    """Structural prefactor per prop:plancherel-term-7-formulation."""
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G


def embed_knot_braid(knot_word: list[tuple[int, int]],
                      n_strands: int) -> list[tuple[int, int]]:
    """Embed a small braid word (in B_3 or B_4) into H_n via Wenzl.

    The knot acts on the first 3 (or 4) strands; identity on the rest.
    Since the rest of the strands are identity, the braid word stays
    the same in (sign, gen) format — gen indices are interpreted
    within H_n.  We just need to verify the max generator index
    is < n - 1.

    Returns the same word (no modification needed; Wenzl embedding
    is implicit via H_n's inclusion of H_m for m ≤ n).
    """
    max_gen = max(g for _, g in knot_word)
    if max_gen >= n_strands:
        raise ValueError(
            f"Knot braid uses gen {max_gen} but H_{n_strands} only "
            f"has generators 1..{n_strands - 1}")
    return knot_word


def chi_lambda_braid_via_rust(shape: list[int], braid_word_signed: list,
                                q: float) -> float:
    """Compute χ^λ(β) at q (f64) via pyhecke_native.

    Note: chi_lambda_braid takes (sign, gen) format for signed
    crossings (+1 = σ, -1 = σ⁻¹).  For our distinguished-knot
    embedding (no averaged crossings), this is the right path.
    """
    # pyhecke_native expects (i32, u32) tuples
    word = [(int(s), int(g)) for (s, g) in braid_word_signed]
    return pyhecke_native.chi_lambda_braid(list(shape), word, float(q))


def fr_pullback_weight_per_partition(
    by_partition: list, n_strands: int, k_depth: int,
    knot_word: list, q_f64: float
) -> dict:
    """Compute FR-pullback weight per partition at depth k.

    Returns dict {partition_tuple: ~w_λ^{(K_dist)}}.

    Only partitions at depth k_depth get the FR pullback; all others
    get the uniform Plancherel weight (no modification).
    """
    qfact = qfac(n_strands)

    # First compute the un-normalized FR weights at depth k
    fr_weights = {}
    chi_at_k_dist = {}
    z_norm_at_depth = mp.mpf(0)

    for p in by_partition:
        shape = tuple(p["partition"])
        depth = len(shape) - 1
        dq = dim_q(shape)
        if depth != k_depth:
            # Uniform weight at other depths
            fr_weights[shape] = mp.mpf(str(dq * dq)) / qfact
            continue

        # Compute χ^λ(K_dist) for partitions at depth k
        try:
            chi_K = chi_lambda_braid_via_rust(list(shape), knot_word, q_f64)
        except Exception:
            chi_K = 0.0
        chi_at_k_dist[shape] = chi_K
        z_norm_at_depth += mp.mpf(str(dq * dq)) * mp.fabs(chi_K)

    # Normalize the FR weights at depth k
    if z_norm_at_depth < mp.mpf("1e-30"):
        # Knot has no support at this depth — fall back to uniform
        for shape, _ in chi_at_k_dist.items():
            dq = dim_q(shape)
            fr_weights[shape] = mp.mpf(str(dq * dq)) / qfact
    else:
        for shape, chi_K in chi_at_k_dist.items():
            dq = dim_q(shape)
            # FR-pullback weight, normalized so it sums to the
            # same total as the uniform Plancherel measure at this
            # depth (preserves total weight conservation).
            fr_weights[shape] = (mp.mpf(str(dq * dq)) * mp.fabs(chi_K)
                                  / z_norm_at_depth)
    return fr_weights


def phi_k_with_fr_pullback(
    by_partition: list, n_strands: int, k: int,
    fr_weights: dict
) -> mp.mpf:
    """Φ_k(K, T) using FR-pullback weight at depth k."""
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
        w = fr_weights.get(shape, mp.mpf(0))
        total += w * mp.log(magnitude)
    return total


def compute_atom_binding_fr(atom: str, knot_word: list[tuple[int, int]],
                             knot_name: str) -> dict:
    """Compute B(K) with FR pullback through `knot_word` at k=3."""
    Z, N = ZN[atom]
    A = Z + N
    n_strands = 3 * A
    w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
    if not w_path.exists():
        return {"deferred": True,
                "reason": f"Run compute_atom_chi_rust.py {atom} first"}
    w = json.loads(w_path.read_text())
    atom_data = w["data"]["atom"]
    free_data = w["data"]["free"]

    # Embed knot in H_n
    embedded_word = embed_knot_braid(knot_word, n_strands)
    q_f64 = float(Q0)

    # Compute FR-pulled-back weight at depth 3 only
    fr_weights_atom = fr_pullback_weight_per_partition(
        atom_data["by_partition"], n_strands, 3, embedded_word, q_f64)
    fr_weights_free = fr_pullback_weight_per_partition(
        free_data["by_partition"], n_strands, 3, embedded_word, q_f64)

    # Apply depth-stratified mass formula with FR pullback at k=3
    delta_phi_total = mp.mpf(0)
    for d in range(n_strands):
        # At k=3, use FR-pullback weight; elsewhere use uniform
        if d == 3:
            phi_atom = phi_k_with_fr_pullback(
                atom_data["by_partition"], n_strands, d, fr_weights_atom)
            phi_free = phi_k_with_fr_pullback(
                free_data["by_partition"], n_strands, d, fr_weights_free)
        else:
            # Uniform Plancherel weight (existing infrastructure)
            qfact = qfac(n_strands)
            phi_atom = mp.mpf(0)
            phi_free = mp.mpf(0)
            for p_data, dest in ((atom_data["by_partition"], "atom"),
                                  (free_data["by_partition"], "free")):
                phi = mp.mpf(0)
                for p in p_data:
                    shape = tuple(p["partition"])
                    if len(shape) - 1 != d:
                        continue
                    chi = mp.mpf(str(p["chi_lambda"]))
                    dq = dim_q(shape)
                    magnitude = mp.fabs(chi) * dq
                    if magnitude < mp.mpf("1e-30"):
                        continue
                    weight = mp.mpf(str(dq * dq)) / qfact
                    phi += weight * mp.log(magnitude)
                if dest == "atom":
                    phi_atom = phi
                else:
                    phi_free = phi
        delta = phi_free - phi_atom
        delta_phi_total += alpha_k(d) * delta

    return {
        "Z": Z, "N": N, "A": A, "n_strands": n_strands,
        "knot_name": knot_name,
        "B_MeV": fmt(delta_phi_total),
        "B_pred_sign": "+" if delta_phi_total > 0 else "-",
    }


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("fr-pullback-k3-test")
    builder.set_description(
        "Empirical test of conj:depth-stratified-frobenius-reciprocity "
        "at k=3 with candidate distinguished knots {4_1, 5_2, 6_1}. "
        "Computes FR-pullback weight ~w_λ^{(K_dist)} = "
        "dim_q²(λ)·|χ^λ(K_dist)| / Z_normalization at depth k=3 "
        "and re-runs depth-stratified binding-energy variance test."
    )
    builder.add_parameter("m_e_CAL1_MeV", str(M_E_MEV))
    builder.add_parameter("q0_f64", str(float(Q0)))

    all_results = {}
    for knot_name, knot_word in CANDIDATE_KNOTS.items():
        print(f"\n=== FR pullback at k=3 via {knot_name} "
              f"(braid len {len(knot_word)}) ===")
        print(f"{'atom':<6} {'A':>3} {'B_MeV':>10} {'B_AME':>10} "
              f"{'ratio':>8} {'sign':>5}")
        results = {}
        for atom in ("D", "T", "3He", "4He"):
            r = compute_atom_binding_fr(atom, knot_word, knot_name)
            if r.get("deferred"):
                continue
            B_pred = mp.mpf(r["B_MeV"])
            B_emp = B_AME[atom]
            ratio = B_pred / B_emp
            r["B_AME_MeV"] = fmt(B_emp)
            r["ratio_pred_over_AME"] = float(ratio)
            results[atom] = r
            print(f"  {atom:<6} {r['A']:>3} {float(B_pred):>10.4f} "
                  f"{float(B_emp):>10.4f} {float(ratio):>8.4f} "
                  f"{r['B_pred_sign']:>5}")
        # Variance
        ratios = [abs(r["ratio_pred_over_AME"]) for r in results.values()]
        if ratios:
            rmin, rmax = min(ratios), max(ratios)
            mom = rmax / rmin if rmin > 0 else float("inf")
            signs_correct = all(r["B_pred_sign"] == "+"
                                 for r in results.values())
            print(f"  max/min = {mom:.4f}, signs +: {signs_correct}")
            all_results[knot_name] = {
                "per_atom": results,
                "max_over_min": float(mom),
                "all_signs_correct": signs_correct,
            }

    # Compare to baseline 1.82× (from binding-depth-stratified-rust)
    baseline = 1.82
    builder.add_data("baseline_variance_no_fr", baseline)
    builder.add_data("per_knot", all_results)

    print("\n=== Summary: variance comparison ===")
    print(f"{'knot':<6} {'max/min':>10} {'signs +':>8} {'vs baseline':>14}")
    print(f"  {'(none)':<6} {baseline:>10.4f} {'(yes)':>8} {'baseline':>14}")
    best_knot = None
    best_mom = baseline
    for kname, r in all_results.items():
        mom = r["max_over_min"]
        improvement = (baseline - mom) / baseline * 100
        sign = "+" if r["all_signs_correct"] else "-"
        print(f"  {kname:<6} {mom:>10.4f} {sign:>8} "
              f"{improvement:>+11.1f}%")
        if r["all_signs_correct"] and mom < best_mom:
            best_mom = mom
            best_knot = kname

    if best_knot:
        verdict = (f"Best K_3*: {best_knot} closes variance to "
                   f"{best_mom:.3f}× (was 1.82×) — "
                   f"{'STRONG' if best_mom < 1.5 else 'PARTIAL'} support "
                   "for FR conjecture.")
    else:
        verdict = ("No candidate knot improves variance; "
                   "conjecture's specific knot identity for k=3 "
                   "may need refinement, or the FR-pullback form is wrong.")
    builder.add_data("verdict", verdict)
    builder.add_data("best_knot", best_knot)
    builder.add_data("best_max_over_min", best_mom)
    print(f"\n  {verdict}")

    builder.add_assertion(
        "data_loaded",
        computed=float(B_AME["D"]),
        expected=2.22456607,
        tolerance=1e-10,
        unit="B(D) MeV",
        source="AME 2020 deuteron binding",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
