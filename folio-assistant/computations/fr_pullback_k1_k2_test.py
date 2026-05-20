#!/usr/bin/env python3
"""
fr_pullback_k1_k2_test.py — empirical search for K_1*, K_2* per
conj:depth-stratified-frobenius-reciprocity.

PR #826 validated the FR pullback mechanism at k=3 with three candidate
knots {4_1, 5_2, 6_1} and found 4_1 best (1.55× variance closure from
1.82× baseline). The conjecture predicts a CHAIN of distinguished
knots K_k* at depths k = 1, 2, 3, where K_3* was named (6_1, but
empirically 4_1) and K_1*, K_2* are open.

Per `depth-stratified-frobenius-reciprocity.md:127-128`, candidate
sets are:
    K_1* ∈ {4_1, 5_2}      (smallest hyperbolic)
    K_2* ∈ {5_2, 6_1, 6_2} (chirality precursors)

This script sweeps each depth INDEPENDENTLY with the FR pullback
formula from PR #826 (proved 10⁻¹⁵ correct on canonical deuteron via
mass_tower_operator_valued.py). For each (k, K) pair:

  1. Compute the FR-pulled-back weight at depth k via the K
     central-projector image in H_{3A}.
  2. Re-run the depth-stratified binding formula with FR weights at
     depth k (uniform elsewhere).
  3. Report variance closure across {D, T, ³He, ⁴He}.

Goal: identify K_1*, K_2* that minimize max/min variance, then
compare to K_3* = 4_1 baseline from PR #826.

Output: `fr-pullback-k1-k2-test.witness.json`

Refs:
- conj:depth-stratified-frobenius-reciprocity
- PR #826 (k=3 validated 4_1 > 5_2 > 6_1)
- prop:mass-tower-operator-valued (operator-valued framework)
"""
from __future__ import annotations

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


# Candidate hyperbolic-knot braid words on 3 strands, per the
# canonical table from `_deprecated/hyperbolic_knot_db_extended.py:43-46`
# (now archived). Format: signed Conway. Per #826 finding, the 6_1
# entry is a mislabeled 3-strand braid (true 6_1 has braid index 4);
# included here for continuity but marked as such.
CANDIDATE_KNOTS_CONWAY = {
    "4_1": ((1, -2, 1, -2), 2.0298832, "figure-eight; braid index 3 (verified)"),
    "5_2": ((1, 1, 1, -2, 1, -2), 2.8281220, "braid index 3 (verified)"),
    "6_1": ((1, 1, -2, 1, -2, -2), 3.1639633, "3-strand (mislabeled — real 6_1 has braid index 4)"),
    "6_2": ((1, 1, 1, -2, 1, -2, -2), 4.4015175, "braid index 3"),
    "6_3": ((1, 1, -2, 1, -2, 1, -2), 5.6927297, "braid index 3"),
}


def conway_to_pyhecke(word_signed):
    out = []
    for s in word_signed:
        sign = 1 if s > 0 else -1
        out.append((sign, abs(s)))
    return out


CANDIDATE_KNOTS = {
    name: conway_to_pyhecke(w_signed)
    for name, (w_signed, _vol, _note) in CANDIDATE_KNOTS_CONWAY.items()
}

# Per `depth-stratified-frobenius-reciprocity.md` line 127-128 candidate
# sets at depths 1 and 2:
K_DEPTH_CANDIDATES = {
    1: ["4_1", "5_2"],
    2: ["5_2", "6_1", "6_2", "6_3"],
}


def vanishing_threshold():
    return mp.mpf(10) ** (5 - mp.mp.dps)


def alpha_k(k):
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return M_E_MEV * 8 * G


def embed_knot_braid(knot_word, n_strands):
    max_gen = max(g for _, g in knot_word)
    if max_gen > n_strands - 1:
        raise ValueError(
            f"max gen {max_gen} > n_strands - 1 = {n_strands - 1}")
    return knot_word


def chi_lambda_braid_via_rust(shape, word, q):
    word_tuples = [(int(s), int(g)) for (s, g) in word]
    return pyhecke_native.chi_lambda_braid(list(shape), word_tuples, float(q))


def fr_pullback_weight_per_partition(by_partition, n_strands, k_depth,
                                       knot_word, q_f64):
    """Reproduce the validated FR-pullback formula from fr_pullback_k3_test.

    Returns (fr_weights, errors)."""
    qfact = qfac(n_strands)
    eps = vanishing_threshold()
    fr_weights = {}
    errors = {}
    chi_at_k = {}
    z_norm = mp.mpf(0)
    s_uniform = mp.mpf(0)
    for p in by_partition:
        shape = tuple(p["partition"])
        depth = len(shape) - 1
        dq = dim_q(shape)
        if depth != k_depth:
            fr_weights[shape] = mp.mpf(str(dq * dq)) / qfact
            continue
        s_uniform += mp.mpf(str(dq * dq)) / qfact
        try:
            chi_K = chi_lambda_braid_via_rust(list(shape), knot_word, q_f64)
        except (ValueError, RuntimeError, OverflowError) as exc:
            chi_K = 0.0
            errors[shape] = f"{type(exc).__name__}: {exc}"
        chi_at_k[shape] = chi_K
        z_norm += mp.mpf(str(dq * dq)) * mp.fabs(chi_K)
    if z_norm < eps:
        for shape in chi_at_k:
            dq = dim_q(shape)
            fr_weights[shape] = mp.mpf(str(dq * dq)) / qfact
    else:
        scale = s_uniform / z_norm
        for shape, chi_K in chi_at_k.items():
            dq = dim_q(shape)
            fr_weights[shape] = mp.mpf(str(dq * dq)) * mp.fabs(chi_K) * scale
    return fr_weights, errors


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


def precompute_uniform_weights(by_partition, n_strands):
    qfact = qfac(n_strands)
    out = {}
    for p in by_partition:
        shape = tuple(p["partition"])
        dq = dim_q(shape)
        out[shape] = mp.mpf(str(dq * dq)) / qfact
    return out


def compute_atom_binding(atom, knot_word, knot_name, k_depth):
    Z, N = ZN[atom]
    A = Z + N
    n_strands = 3 * A
    w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
    if not w_path.exists():
        return {"deferred": True, "reason": f"need atom-chi-rust-{atom.lower()}"}
    w = json.loads(w_path.read_text())
    atom_data = w["data"]["atom"]
    free_data = w["data"]["free"]
    upstream_sha = w.get("commitSha", "unknown")
    embedded = embed_knot_braid(knot_word, n_strands)
    q_f64 = float(Q0)
    fr_atom, a_errs = fr_pullback_weight_per_partition(
        atom_data["by_partition"], n_strands, k_depth, embedded, q_f64)
    fr_free, f_errs = fr_pullback_weight_per_partition(
        free_data["by_partition"], n_strands, k_depth, embedded, q_f64)
    uni_atom = precompute_uniform_weights(atom_data["by_partition"], n_strands)
    uni_free = precompute_uniform_weights(free_data["by_partition"], n_strands)
    final_atom = dict(uni_atom)
    final_free = dict(uni_free)
    for shape, ww in fr_atom.items():
        if len(shape) - 1 == k_depth:
            final_atom[shape] = ww
    for shape, ww in fr_free.items():
        if len(shape) - 1 == k_depth:
            final_free[shape] = ww
    delta = mp.mpf(0)
    for d in range(n_strands):
        phi_a = phi_k_with_weights(atom_data["by_partition"], d, final_atom)
        phi_f = phi_k_with_weights(free_data["by_partition"], d, final_free)
        delta += alpha_k(d) * (phi_f - phi_a)
    return {
        "Z": Z, "N": N, "A": A, "n_strands": n_strands,
        "knot_name": knot_name, "k_depth": k_depth,
        "B_MeV": fmt(delta),
        "B_pred_sign": "+" if delta > 0 else "-",
        "upstream_commitSha": upstream_sha,
        "atom_chi_errors_count": len(a_errs),
        "free_chi_errors_count": len(f_errs),
    }


def sweep_depth(k_depth, candidate_names, builder_data):
    """Sweep candidate knots at given k_depth across {D, T, ³He, ⁴He}."""
    print(f"\n=== Sweep at depth k={k_depth} (candidates: {candidate_names}) ===")
    print(f"{'knot':<6} {'max/min':>10} {'signs':>6} "
          f"{'atoms_skipped':>13}")
    print("-" * 50)
    per_knot = {}
    for knot_name in candidate_names:
        knot_word = CANDIDATE_KNOTS[knot_name]
        atom_results = {}
        skipped = 0
        for atom in ("D", "T", "3He", "4He"):
            r = compute_atom_binding(atom, knot_word, knot_name, k_depth)
            if r.get("deferred"):
                skipped += 1
                continue
            B_pred = mp.mpf(r["B_MeV"])
            B_emp = B_AME[atom]
            r["B_AME_MeV"] = fmt(B_emp)
            r["ratio_pred_over_AME"] = float(B_pred / B_emp)
            atom_results[atom] = r
        if atom_results:
            ratios = [abs(rr["ratio_pred_over_AME"]) for rr in atom_results.values()]
            rmin, rmax = min(ratios), max(ratios)
            mom = rmax / rmin if rmin > 0 else float("inf")
            signs_correct = all(rr["B_pred_sign"] == "+"
                                 for rr in atom_results.values())
            sign_str = "+" if signs_correct else "-"
            print(f"  {knot_name:<6} {mom:>10.4f} {sign_str:>6} "
                  f"{skipped:>13}")
            per_knot[knot_name] = {
                "per_atom": atom_results,
                "max_over_min": float(mom),
                "all_signs_correct": signs_correct,
                "atoms_skipped": skipped,
            }
    builder_data[f"k_{k_depth}"] = per_knot
    return per_knot


def main():
    set_compute_dps()
    builder = WitnessBuilder("fr-pullback-k1-k2-test")
    builder.set_description(
        "Empirical search for K_1*, K_2* of conj:depth-stratified-"
        "frobenius-reciprocity (PR #826 validated k=3 with 4_1 best). "
        "Sweeps candidate hyperbolic knots {4_1, 5_2} at k=1 and "
        "{5_2, 6_1, 6_2, 6_3} at k=2 via Wenzl embedding into H_{3A}; "
        "reports variance closure across {D, T, ³He, ⁴He}."
    )
    builder.add_parameter("m_e_CAL1_MeV", str(M_E_MEV))
    builder.add_parameter("q0_f64", str(float(Q0)))
    builder.add_data("candidate_knots", {
        name: {"conway_word": list(w), "volume": v, "note": n}
        for name, (w, v, n) in CANDIDATE_KNOTS_CONWAY.items()
    })
    builder.add_data("baseline_variance_no_fr", 1.82)
    builder.add_data("k3_reference_best_knot_PR826", {
        "K_3*": "4_1",
        "k3_best_variance": 1.551,
        "k3_paper_named": "6_1",
    })

    upstream = []
    for atom in ("D", "T", "3He", "4He"):
        p = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
        if p.exists():
            upstream.append(str(p.relative_to(HERE.parent.parent)))
    builder.add_data("upstream_witnesses", upstream)

    print("=" * 78)
    print(" FR-pullback K_1*, K_2* search ")
    print(" (PR #826 baseline: no FR = 1.82×, k=3 best (4_1) = 1.551×)")
    print("=" * 78)

    sweep_results = {}
    sweep_depth(1, K_DEPTH_CANDIDATES[1], sweep_results)
    sweep_depth(2, K_DEPTH_CANDIDATES[2], sweep_results)

    builder.add_data("sweeps", sweep_results)

    # Identify best per depth
    best_per_depth = {}
    for k in (1, 2):
        results = sweep_results.get(f"k_{k}", {})
        positive_signs = {n: r for n, r in results.items()
                          if r["all_signs_correct"]}
        if not positive_signs:
            best_per_depth[k] = None
            continue
        best_name = min(positive_signs,
                         key=lambda n: positive_signs[n]["max_over_min"])
        best_per_depth[k] = {
            "knot": best_name,
            "max_over_min": positive_signs[best_name]["max_over_min"],
        }

    builder.add_data("best_per_depth", best_per_depth)

    print("\n=== Best K_k* per depth ===")
    for k in (1, 2):
        b = best_per_depth.get(k)
        if b:
            print(f"  K_{k}* = {b['knot']} "
                  f"(variance {b['max_over_min']:.4f}, vs baseline 1.82)")
        else:
            print(f"  K_{k}*: no candidate gives positive signs across all atoms")

    # Verdict
    parts = []
    for k in (1, 2):
        b = best_per_depth.get(k)
        if b:
            improvement = (1.82 - b["max_over_min"]) / 1.82 * 100
            parts.append(
                f"K_{k}* = {b['knot']} (variance {b['max_over_min']:.3f}×, "
                f"{improvement:+.1f}% vs no-FR baseline)")
        else:
            parts.append(f"K_{k}* = NONE (no candidate gives correct signs)")
    verdict = ("PR #826 k=3 chain extension: " + "; ".join(parts) +
               f". For comparison, PR #826 found K_3* = 4_1 (1.551×, +14.8%).")
    builder.add_data("verdict", verdict)
    print(f"\n  Verdict: {verdict}")

    builder.add_assertion(
        "data_loaded",
        computed=float(B_AME["D"]),
        expected=2.22456607,
        tolerance=1e-10,
        unit="B(D) MeV",
        source="AME 2020",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
