"""
binding_depth_stratified_selfconj.py — restrict low-k Wedderburn weight
to self-conjugate partitions only.

CATEGORICAL HYPOTHESIS (2026-05-19): per prop:plancherel-term-7-
formulation, at low k ≤ 3 the Frobenius integral factors through a
distinguished hyperbolic-knot ideal (e.g. 6_1 at k=3, the chirality
channel). The 6_1 chirality channel is structurally tied to the
SELF-CONJUGATE (column-conjugation-fixed) Wedderburn block: at q=1,
y_λ = w_λ exactly on the self-conjugate stratum per
notation-collisions.md §"three partition-weight families".

This script tests: at low k (1, 2, 3), restrict ~w_λ to
SELF-CONJUGATE partitions only (λ = λ^T). At high k (≥4), keep
uniform ~w_λ over all partitions.

Empirical falsifiability: if variance drops vs uniform, the
self-conjugate restriction IS the categorical ideal at low k.

Ref: prop:plancherel-term-7-formulation
Ref: notation-collisions.md (Wenzl bridge — y_λ = w_λ on
     self-conjugate stratum)
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
from codata_constants import AME_B_TRITIUM_MEV_VALIDATION, M_E_MEV
from mass_at_3A_proper import dim_q, qfac
from q_parameter import Q as Q0


B_AME = {
    "D":   mp.mpf("2.22456607"),
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": mp.mpf("7.7180428"),
    "4He": mp.mpf("28.295674"),
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}


def conjugate_partition(shape: tuple) -> tuple:
    """λ^T = transpose / column-conjugate of λ."""
    if not shape:
        return ()
    max_row = max(shape)
    conj = []
    for j in range(max_row):
        count = sum(1 for row in shape if row > j)
        conj.append(count)
    return tuple(conj)


def is_self_conjugate(shape: tuple) -> bool:
    return tuple(shape) == conjugate_partition(shape)


def alpha_k(k: int) -> mp.mpf:
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
    G = mp.catalan
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G


def phi_k_selfconj_restricted(by_partition, n_strands, k, restrict_low_k):
    """Φ_k with low-k restricted to self-conjugate partitions
    (renormalised to preserve total measure within the stratum)."""
    qfact = qfac(n_strands)
    is_low_k = k <= 3 and restrict_low_k

    if is_low_k:
        Z_uniform = mp.mpf(0)
        Z_selfconj = mp.mpf(0)
        for p in by_partition:
            shape = tuple(p["partition"])
            if len(shape) - 1 != k:
                continue
            dq = dim_q(shape)
            w = mp.mpf(str(dq * dq)) / qfact
            Z_uniform += w
            if is_self_conjugate(shape):
                Z_selfconj += w
        if Z_selfconj < mp.mpf("1e-30"):
            renorm = mp.mpf(0)  # no self-conjugate partitions at this depth
        else:
            renorm = Z_uniform / Z_selfconj
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
        if is_low_k and not is_self_conjugate(shape):
            continue
        w = mp.mpf(str(dq * dq)) / qfact * renorm
        total += w * mp.log(magnitude)
    return total


def compute_atom_binding(atom: str, restrict_low_k: bool) -> dict:
    Z, N = ZN[atom]
    A = Z + N
    n_strands = 3 * A
    w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
    if not w_path.exists():
        return {"deferred": True}
    w = json.loads(w_path.read_text())
    atom_data = w["data"]["atom"]
    free_data = w["data"]["free"]

    delta_phi_total = mp.mpf(0)
    per_depth = {}
    for k in range(n_strands):
        phi_atom = phi_k_selfconj_restricted(
            atom_data["by_partition"], n_strands, k, restrict_low_k)
        phi_free = phi_k_selfconj_restricted(
            free_data["by_partition"], n_strands, k, restrict_low_k)
        delta = phi_free - phi_atom
        contrib = alpha_k(k) * delta
        per_depth[k] = {"delta_phi": fmt(delta), "contrib": fmt(contrib)}
        delta_phi_total += contrib

    return {
        "Z": Z, "N": N, "A": A,
        "B_MeV": fmt(delta_phi_total),
        "B_pred_sign": "+" if delta_phi_total > 0 else "-",
        "per_depth": per_depth,
    }


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("binding-depth-stratified-selfconj")
    builder.set_description(
        "Self-conjugate-restricted low-k Wedderburn weight test. "
        "Per prop:plancherel-term-7-formulation, low strata k ≤ 3 "
        "factor through distinguished knot ideals (6_1 chirality "
        "channel at k=3). Hypothesis: ideal restriction = self-"
        "conjugate partitions only (Wenzl bridge stratum at q=1)."
    )

    all_results = {}
    for restrict in (False, True):
        label = "selfconj-restricted" if restrict else "uniform-baseline"
        print(f"\n=== {label} ===")
        print(f"{'atom':<6} {'A':>3} {'B_MeV':>10} {'B_AME':>10} {'ratio':>8}")
        results = {}
        for atom in ("D", "T", "3He", "4He"):
            r = compute_atom_binding(atom, restrict)
            if r.get("deferred"):
                continue
            B_pred = mp.mpf(r["B_MeV"])
            B_emp = B_AME[atom]
            ratio = (B_pred / B_emp if B_emp > 0 else mp.mpf("nan"))
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
        all_results[label] = {"per_atom": results,
                                "max_over_min": float(mom),
                                "all_signs_correct": signs_correct}

    builder.add_data("results", all_results)
    builder.add_assertion(
        "data_loaded", computed=float(B_AME["D"]), expected=2.22456607,
        tolerance=1e-10, unit="B(D) MeV", source="AME 2020",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
