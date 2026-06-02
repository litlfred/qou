#!/usr/bin/env python3
"""qbeta_half_fill_probe.py — combinatorial probe of the half-fill
hypothesis for the averaging-resonance rule (prop:averaging-resonance-rule).

The half-fill hypothesis says: for a typed-B_n braid recipe with
n_avg ≥ 2 averaged crossings out of n_total = n_σ + n_σ⁻¹ + n_avg
total crossings, the **unique averaging-resonant rung** in the
precision-ladder expansion of τ_M(β) is

    k_outlier  =  ⌊ n_total / 2 ⌋ .

The proton typed-B_3 recipe (n_σ=6, n_σ⁻¹=3, n_avg=2, n_total=11)
has k_outlier = 5, matching the empirical c_5 = -11/8 outlier.

This probe is **combinatorial** — it does NOT extract c_k values
via SDP-T_β (that infrastructure lives on PR #814 / a future probe).
What it does:

  1. Enumerate typed distributions for n_total ∈ {9, ..., 15} with
     n_avg = 2 (matching the proton recipe's two-averaged-crossing
     pattern).
  2. For each distribution, compute the argmax-binomial heuristic
     m_k(d) for every k ∈ {2, ..., n_total - 1}.
  3. Compare against the half-fill prediction k* = ⌊n_total/2⌋.
  4. Identify the rungs where the half-fill rule and the
     argmax-binomial rule agree (both predict the same single
     outlier) vs. disagree.

The output is a side-by-side prediction table — running an actual
SDP-T_β extraction at these alternative n_total values is the next
step (not done here) for empirical falsification.

Status: experimental (probe).
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from math import comb
from pathlib import Path

# Reuse the canonical TypedB3Distribution from the sector classifier.
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from ck_sector_classifier import TypedB3Distribution  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def half_fill_rung(n_total: int) -> int:
    """The half-fill hypothesis: k_outlier = ⌊n_total/2⌋."""
    return n_total // 2


def argmax_m_k(dist: TypedB3Distribution, k: int) -> int:
    """The argmax-binomial m_k for rung k under distribution `dist`.

    Returns the largest m ∈ {0, 1, ..., n_avg} achieving
        w(m) = C(n_avg, m) * C(n_non_avg, k - m),
    with the `≥` tie-break matching averaging-resonance-rule.md.
    """
    n_avg, n_non_avg = dist.n_avg, dist.n_non_avg
    best_m, best_w = 0, comb(n_non_avg, k) if 0 <= k <= n_non_avg else 0
    for m in range(1, n_avg + 1):
        if 0 <= k - m <= n_non_avg:
            w = comb(n_avg, m) * comb(n_non_avg, k - m)
            if w >= best_w:
                best_m, best_w = m, w
    return best_m


def first_averaging_rung(dist: TypedB3Distribution, k_max: int) -> int | None:
    """The smallest k ∈ {2, ..., k_max} with argmax m_k ≥ 1."""
    for k in range(2, k_max + 1):
        if argmax_m_k(dist, k) >= 1:
            return k
    return None


def probe(n_total_range: range) -> list[dict]:
    """Enumerate typed-B_n distributions at varying n_total (fixed
    n_avg = 2) and compute half-fill vs argmax-binomial predictions."""
    rows: list[dict] = []
    for n_total in n_total_range:
        n_avg = 2  # fixed — matches proton/neutron typed-B_3 recipe
        n_non_avg = n_total - n_avg
        # Sample one representative split (skewed σ : σ⁻¹) matching
        # the proton (6:3) shape — for n_non_avg = 9 this is (6, 3);
        # we keep the same skewing ratio for other n_non_avg.
        n_sigma = (2 * n_non_avg + 2) // 3
        n_sigma_inv = n_non_avg - n_sigma
        dist = TypedB3Distribution(
            n_sigma=n_sigma, n_sigma_inv=n_sigma_inv, n_avg=n_avg
        )
        k_half = half_fill_rung(n_total)
        k_max = n_total - 1
        m_k_table = {k: argmax_m_k(dist, k) for k in range(2, k_max + 1)}
        averaging_predicted_rungs = [k for k, m in m_k_table.items() if m >= 1]
        first_avg = first_averaging_rung(dist, k_max)
        rows.append({
            "n_total": n_total,
            "n_sigma": n_sigma,
            "n_sigma_inv": n_sigma_inv,
            "n_avg": n_avg,
            "half_fill_predicted_k_outlier": k_half,
            "argmax_first_averaging_k": first_avg,
            "argmax_all_averaging_rungs": averaging_predicted_rungs,
            "m_k_table": m_k_table,
            "half_fill_in_argmax_set": k_half in averaging_predicted_rungs,
        })
    return rows


def build_witness(rows: list[dict]) -> WitnessBuilder:
    """Build the witness via the canonical WitnessBuilder so the output
    JSON follows the ComputationWitness shape (computedAt, commitSha,
    scriptHash, engineVersion, etc.) and drift detection works.
    """
    proton_row = next((r for r in rows if r["n_total"] == 11), None)
    anchor_match = (
        proton_row is not None
        and proton_row["half_fill_predicted_k_outlier"] == 5
    )
    w = WitnessBuilder(
        name="qbeta-half-fill-probe",
        engine="python",
        output_dir=HERE,
    )
    w.add_parameter("computation", "prop:averaging-resonance-rule")
    w.add_parameter("hypothesis", "k_outlier = floor(n_total / 2)")
    w.add_parameter("fixed_parameters", {"n_avg": 2, "skew_ratio": "2:1 σ:σ⁻¹"})
    w.add_data("rows", rows)
    w.add_data("anchor_row", proton_row)
    w.add_data("anchor_empirical_outlier", 5)
    # The half-fill prediction on the proton recipe (n_total = 11) must
    # equal the empirical outlier k = 5.
    w.add_assertion(
        name="half_fill_matches_empirical_proton_outlier",
        computed=proton_row["half_fill_predicted_k_outlier"] if proton_row else -1,
        expected=5,
        source="prop:averaging-resonance-rule",
    )
    return w


def main() -> None:
    rows = probe(range(9, 16))  # n_total ∈ {9, ..., 15}
    w = build_witness(rows)
    proton_row = next((r for r in rows if r["n_total"] == 11), None)
    print("=" * 78)
    print("Half-fill hypothesis combinatorial probe")
    print("=" * 78)
    print(f"Fixed: n_avg = 2, σ:σ⁻¹ skew ≈ 2:1 (matches proton recipe shape)")
    print()
    print(f"{'n_total':>8} | {'(n_σ, n_σ⁻¹, n_avg)':>20} | "
          f"{'k_half = ⌊n/2⌋':>15} | "
          f"{'first argmax avg-k':>20} | "
          f"{'argmax-avg rungs':>30}")
    print("-" * 110)
    for r in rows:
        triple = f"({r['n_sigma']}, {r['n_sigma_inv']}, {r['n_avg']})"
        print(f"{r['n_total']:>8} | {triple:>20} | "
              f"{r['half_fill_predicted_k_outlier']:>15} | "
              f"{str(r['argmax_first_averaging_k']):>20} | "
              f"{str(r['argmax_all_averaging_rungs']):>30}")
    print()
    print("Anchor check (proton typed-B_3, n_total = 11):")
    anchor = proton_row
    if anchor:
        agree = anchor["half_fill_predicted_k_outlier"] == 5
        print(f"  half-fill predicts k = {anchor['half_fill_predicted_k_outlier']}; "
              f"empirical c_5 outlier → {'AGREE ✓' if agree else 'DISAGREE ✗'}")
        print(f"  argmax-binomial predicts averaging at "
              f"{anchor['argmax_all_averaging_rungs']}; "
              f"empirical {{5}} only → "
              f"{'falsified at k ∉ {5}' if set(anchor['argmax_all_averaging_rungs']) != {5} else 'agrees'}")
    print()
    print("Half-fill prediction across n_total:")
    for r in rows:
        ok = "✓" if r["half_fill_in_argmax_set"] else "✗ (half-fill not in argmax avg-set)"
        print(f"  n_total = {r['n_total']:>2}: half-fill k* = "
              f"{r['half_fill_predicted_k_outlier']}  {ok}")
    print()
    print("NB: this probe is COMBINATORIAL — it tests whether the half-")
    print("    fill rung sits inside the argmax-binomial-predicted averaging")
    print("    set, but does NOT compute actual c_k values. Empirical")
    print("    falsification requires extending SDP-T_β extraction to")
    print("    non-n_total=11 braid recipes.")

    out = w.save()
    print()
    print(f"Witness emitted: {out.relative_to(HERE.parent.parent)}")


if __name__ == "__main__":
    main()
