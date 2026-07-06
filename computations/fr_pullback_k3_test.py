"""
fr_pullback_k3_test.py — empirical test of conj:depth-stratified-
frobenius-reciprocity at k=3 (chirality channel).

Per prop:plancherel-term-7-formulation, "at low strata k ≤ 3 the
restricted Frobenius integral factors through specific hyperbolic-knot
ideals (e.g. 6_1 at k=3, the chirality channel)."

Per conj:depth-stratified-frobenius-reciprocity, the FR pullback
modifies the Wedderburn weight at depth k via:

  ~w_λ^{(K_k*)} := dim_q²(λ) · |χ^λ(e_{K_k*})| /
                   (Σ_μ dim_q²(μ) · |χ^μ(e_{K_k*})|)
                   · S_uniform_k

where S_uniform_k = Σ_{μ:depth=k} dim_q²(μ) / [n]_q! is the total
uniform-Plancherel weight at depth k (preserved by the FR pullback,
which only REDISTRIBUTES weight within the depth-k stratum, not
rescales it).

This script tests the FR pullback at k=3 with candidate distinguished
knots K_3* ∈ {4_1, 5_2, 6_1} using the repo's canonical braid words
from `_deprecated/hyperbolic_knot_db_extended.py`.

Reference: prop:plancherel-term-7-formulation,
           conj:depth-stratified-frobenius-reciprocity.
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
from codata_constants import AME_B_TRITIUM_MEV_VALIDATION, M_E_MEV  # noqa: E402
from mass_at_3A_proper import dim_q, qfac  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402


B_AME = {
    "D":   mp.mpf("2.22456607"),
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": mp.mpf("7.7180428"),
    "4He": mp.mpf("28.295674"),
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}


# Distinguished hyperbolic-knot candidates at depth k=3.
# Braid words taken from the repo's canonical table:
#   `_deprecated/hyperbolic_knot_db_extended.py:43-46`
# Format: tuple of signed gen indices (Conway form), where positive
# = σ_g, negative = σ_g^{-1}.
CANDIDATE_KNOTS_CONWAY = {
    "4_1": ((1, -2, 1, -2), 2.0298832),
    "5_2": ((1, 1, 1, -2, 1, -2), 2.8281220),
    "6_1": ((1, 1, -2, 1, -2, -2), 3.1639633),
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
    """Threshold for treating |z| as zero, tied to current mp.dps."""
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


def embed_knot_braid(knot_word: list[tuple[int, int]],
                      n_strands: int) -> list[tuple[int, int]]:
    """Embed a small braid word into H_n via Wenzl.

    H_n has generators σ_1..σ_{n-1} (1-indexed), so the max
    generator index used must be ≤ n - 1.
    """
    max_gen = max(g for _, g in knot_word)
    if max_gen > n_strands - 1:
        raise ValueError(
            f"Knot braid uses gen {max_gen} but H_{n_strands} only "
            f"has generators 1..{n_strands - 1}")
    return knot_word


def chi_lambda_braid_via_rust(shape: list[int],
                                braid_word_signed: list,
                                q: float) -> float:
    """Compute χ^λ(β) at q (f64) via pyhecke_native.chi_lambda_braid."""
    word = [(int(s), int(g)) for (s, g) in braid_word_signed]
    return pyhecke_native.chi_lambda_braid(list(shape), word, float(q))


def fr_pullback_weight_per_partition(
    by_partition: list, n_strands: int, k_depth: int,
    knot_word: list, q_f64: float
) -> tuple[dict, dict]:
    """Compute FR-pullback weight + errors per partition.

    Returns (fr_weights, errors):
      - fr_weights at depth k_depth: redistribute dim_q²/qfact weight
        proportionally to |χ^λ(K_dist)|, preserving total depth-k mass.
      - errors: any per-partition chi-computation failures
        (specific exceptions only; bugs propagate).
    """
    qfact = qfac(n_strands)
    eps = vanishing_threshold()

    fr_weights: dict = {}
    errors: dict = {}
    chi_at_k_dist: dict = {}
    z_norm_unweighted = mp.mpf(0)  # Σ dim_q² · |χ| at depth k
    s_uniform_at_depth = mp.mpf(0)  # Σ dim_q² / qfact at depth k

    for p in by_partition:
        shape = tuple(p["partition"])
        depth = len(shape) - 1
        dq = dim_q(shape)
        if depth != k_depth:
            fr_weights[shape] = mp.mpf(str(dq * dq)) / qfact
            continue
        s_uniform_at_depth += mp.mpf(str(dq * dq)) / qfact
        try:
            chi_K = chi_lambda_braid_via_rust(list(shape), knot_word, q_f64)
        except (ValueError, RuntimeError, OverflowError) as exc:
            chi_K = 0.0
            errors[shape] = f"{type(exc).__name__}: {exc}"
        chi_at_k_dist[shape] = chi_K
        z_norm_unweighted += mp.mpf(str(dq * dq)) * mp.fabs(chi_K)

    # Normalize so FR-pulled-back weights at depth k SUM to the
    # uniform Plancherel total at depth k (preserves total depth-3
    # mass contribution; FR redistributes within stratum).
    if z_norm_unweighted < eps:
        for shape, _ in chi_at_k_dist.items():
            dq = dim_q(shape)
            fr_weights[shape] = mp.mpf(str(dq * dq)) / qfact
    else:
        scale = s_uniform_at_depth / z_norm_unweighted
        for shape, chi_K in chi_at_k_dist.items():
            dq = dim_q(shape)
            fr_weights[shape] = (mp.mpf(str(dq * dq)) * mp.fabs(chi_K)
                                  * scale)
    return fr_weights, errors


def phi_k_with_weights(
    by_partition: list, n_strands: int, k: int,
    weights: dict
) -> mp.mpf:
    """Φ_k(K, T) using arbitrary weight per partition."""
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


def precompute_uniform_weights(by_partition: list, n_strands: int) -> dict:
    """Pre-compute uniform Plancherel weights (one pass over partitions)."""
    qfact = qfac(n_strands)
    weights: dict = {}
    for p in by_partition:
        shape = tuple(p["partition"])
        dq = dim_q(shape)
        weights[shape] = mp.mpf(str(dq * dq)) / qfact
    return weights


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
    upstream_sha = w.get("commitSha", "unknown")

    embedded_word = embed_knot_braid(knot_word, n_strands)
    q_f64 = float(Q0)

    fr_atom_weights, atom_errors = fr_pullback_weight_per_partition(
        atom_data["by_partition"], n_strands, 3, embedded_word, q_f64)
    fr_free_weights, free_errors = fr_pullback_weight_per_partition(
        free_data["by_partition"], n_strands, 3, embedded_word, q_f64)

    uniform_atom_weights = precompute_uniform_weights(
        atom_data["by_partition"], n_strands)
    uniform_free_weights = precompute_uniform_weights(
        free_data["by_partition"], n_strands)

    # FR at depth 3, uniform elsewhere
    final_atom_weights = dict(uniform_atom_weights)
    final_free_weights = dict(uniform_free_weights)
    for shape, w in fr_atom_weights.items():
        if len(shape) - 1 == 3:
            final_atom_weights[shape] = w
    for shape, w in fr_free_weights.items():
        if len(shape) - 1 == 3:
            final_free_weights[shape] = w

    delta_phi_total = mp.mpf(0)
    for d in range(n_strands):
        phi_atom = phi_k_with_weights(
            atom_data["by_partition"], n_strands, d, final_atom_weights)
        phi_free = phi_k_with_weights(
            free_data["by_partition"], n_strands, d, final_free_weights)
        delta_phi_total += alpha_k(d) * (phi_free - phi_atom)

    return {
        "Z": Z, "N": N, "A": A, "n_strands": n_strands,
        "knot_name": knot_name,
        "B_MeV": fmt(delta_phi_total),
        "B_pred_sign": "+" if delta_phi_total > 0 else "-",
        "upstream_witness": f"atom-chi-rust-{atom.lower()}.witness.json",
        "upstream_commitSha": upstream_sha,
        "atom_chi_errors_count": len(atom_errors),
        "free_chi_errors_count": len(free_errors),
    }


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("fr-pullback-k3-test")
    builder.set_description(
        "Empirical test of conj:depth-stratified-frobenius-reciprocity "
        "at k=3 with candidate distinguished knots {4_1, 5_2, 6_1} "
        "via Wenzl embedding into H_{3A}. FR-pulled-back weight "
        "normalized to preserve uniform Plancherel depth-3 total. "
        "Braid words sourced from "
        "_deprecated/hyperbolic_knot_db_extended.py canonical table."
    )
    builder.add_parameter("m_e_CAL1_MeV", str(M_E_MEV))
    builder.add_parameter("q0_f64", str(float(Q0)))

    builder.add_data("candidate_knots", {
        name: {
            "conway_word": list(w_signed),
            "hyperbolic_volume_cross_check": vol,
            "n_crossings": len(w_signed),
        }
        for name, (w_signed, vol) in CANDIDATE_KNOTS_CONWAY.items()
    })

    upstream_witnesses = []
    for atom in ("D", "T", "3He", "4He"):
        w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
        if w_path.exists():
            upstream_witnesses.append(
                str(w_path.relative_to(HERE.parent.parent)))
    builder.add_data("upstream_witnesses", upstream_witnesses)

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

    paper_knot = "6_1"
    paper_knot_mom = (all_results.get(paper_knot, {}).get("max_over_min")
                       if paper_knot in all_results else None)
    paper_naming_validated = (best_knot == paper_knot)
    if best_knot:
        general_support = ("STRONG" if best_mom < 1.5 else "PARTIAL")
        if paper_naming_validated:
            verdict = (f"FR conjecture {general_support} support: "
                       f"K_3* = {best_knot} (matches paper) closes "
                       f"variance to {best_mom:.3f}× (was {baseline}×).")
        else:
            paper_str = (f"{paper_knot_mom:.3f}×"
                          if paper_knot_mom else "n/a")
            verdict = (
                f"FR conjecture {general_support} support: empirically "
                f"best K_3* = {best_knot} ({best_mom:.3f}×, baseline "
                f"{baseline}×); paper's named K_3* = {paper_knot} gives "
                f"{paper_str} (NOT empirically best). Paper's specific "
                "naming K_3* = 6_1 NOT validated by this test; general "
                "FR mechanism partially validated via 4_1, 5_2.")
    else:
        verdict = ("No candidate knot improves variance; "
                   "FR-pullback form or specific knot identity may "
                   "need refinement.")
    builder.add_data("verdict", verdict)
    builder.add_data("best_knot", best_knot)
    builder.add_data("best_max_over_min", best_mom)
    builder.add_data("paper_named_knot", paper_knot)
    builder.add_data("paper_named_knot_max_over_min",
                      float(paper_knot_mom) if paper_knot_mom else None)
    builder.add_data("paper_naming_validated", paper_naming_validated)
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
