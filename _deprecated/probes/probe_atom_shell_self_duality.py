#!/usr/bin/env python3
"""Probe — categorical magic via shell-self-duality on atom braids.

Per content/quantum-observable-universe/braids-and-knots/shell-schur-weyl-self-duality.md:

  Shell-operator self-duality:  x_λ(β) = x_{λ*}(β)  for all λ ⊢ A_magic
  ⇔  GL_k-charge-conjugate invariance under Schur-Weyl transport

For each atom β = atom_braid_word_3A(Z, N), this probe:

  1. Iterates partitions λ ⊢ 3A
  2. Computes χ_λ(β) at q_0 via Hoefsmit seminormal form
  3. Computes χ_{λ*}(β) for the transpose partition λ*
  4. Tests whether x_λ = x_{λ*} (categorical magic condition)
  5. Computes y_λ-weighted Markov trace tr_M(β) = Σ y_λ · χ_λ /dim(λ)

NO Vol_hyp.  NO knot identification.  NO census search.  Purely
algebraic in ℚ(q^{1/2}) at q = q_0.

Predictions (from charge-conjugation symmetry under u↔d):

  - Z = N atoms (D, ⁴He, ⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca):
    invariant under p↔n exchange ⇒ self-dual ⇒ MAGIC
  - Z ≠ N atoms (T, ³He, ⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹⁴N, ¹⁹F):
    not invariant under p↔n ⇒ NOT self-dual ⇒ non-magic

If non-self-dual, the FULL Wedderburn sum is required (not just
the chi-sym-alt pair).

Output: probe-atom-shell-self-duality.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV
from light_isotope_sweep import (
    atomic_braid_to_crossings,
    chi_lambda_numeric,
    dim_q,
    partitions_of,
    qfac,
)
from q_parameter import Q as Q_0
from witness_base import WitnessBuilder


# Atoms to probe — restricted to A ≤ 3 for tractable Hoefsmit at f64.
# A = 4 (⁴He) at H_12 has 77 partitions and times out.
# Higher A requires either MPFR optimisation or cached Hoefsmit data.
ATOMS = [
    ("D",   1, 1, "magic? (Z=N=1, p↔n self-dual)"),
    ("T",   1, 2, "non-magic (Z=1, N=2)"),
    ("3He", 2, 1, "non-magic (Z=2, N=1; dual of T)"),
]


def transpose_partition(shape):
    """Return the conjugate (transpose) of a partition shape."""
    if not shape:
        return ()
    n_cols = max(shape)
    return tuple(
        sum(1 for part in shape if part > col)
        for col in range(n_cols)
    )


def test_self_duality(Z, N, max_partitions=None):
    """Compute χ_λ and χ_{λ*} for each partition λ ⊢ 3A.

    Returns:
      rows: list of {shape, shape_star, chi, chi_star, equal, ratio}
      tr_M: full Markov trace
      summary: counts of self-dual partitions, total partitions
    """
    A = Z + N
    n_strands = 3 * A
    crossings = atomic_braid_to_crossings(Z, N, include_inter=True)
    nfac = qfac(n_strands)

    rows = []
    seen_pairs = set()  # avoid double-counting (λ, λ*) pairs
    self_dual_count = 0
    self_dual_partitions = 0   # λ = λ* (self-conjugate)
    pair_dual_count = 0        # λ ≠ λ*, χ_λ = χ_{λ*}
    not_dual_count = 0
    tr_M_total = 0.0

    n_partitions = sum(1 for _ in partitions_of(n_strands))
    if max_partitions and n_partitions > max_partitions:
        print(f"  WARNING: {n_partitions} partitions > {max_partitions}; "
              f"truncating (results will be partial)")

    for shape in partitions_of(n_strands):
        shape_star = transpose_partition(shape)
        # Compute chi_lambda
        try:
            chi, d = chi_lambda_numeric(shape, crossings)
        except (IndexError, ValueError):
            continue
        if d == 0:
            continue
        # Markov trace contribution
        d_q = float(dim_q(shape))
        y_lambda = float(d_q ** 2 / nfac)
        tr_M_total += y_lambda * chi / d

        # Compute chi_lambda_star (only if λ ≠ λ*)
        is_self_conjugate = (shape == shape_star)
        if is_self_conjugate:
            chi_star = chi
            d_star = d
        else:
            try:
                chi_star, d_star = chi_lambda_numeric(shape_star, crossings)
            except (IndexError, ValueError):
                continue

        # Skip the dual pair if we've seen (λ*, λ) already
        sorted_pair = tuple(sorted([shape, shape_star]))
        if sorted_pair in seen_pairs:
            continue
        seen_pairs.add(sorted_pair)

        equal = abs(chi - chi_star) < 1e-9
        ratio = chi / chi_star if chi_star != 0 else None

        if is_self_conjugate:
            self_dual_partitions += 1
            self_dual_count += 1
        elif equal:
            pair_dual_count += 1
            self_dual_count += 1
        else:
            not_dual_count += 1

        rows.append({
            "shape": list(shape),
            "shape_star": list(shape_star),
            "is_self_conjugate": is_self_conjugate,
            "dim": d,
            "chi_lambda": chi,
            "chi_lambda_star": chi_star,
            "y_lambda": y_lambda,
            "equal_within_1e-9": equal,
            "ratio_chi_to_chi_star": ratio,
        })

    summary = {
        "n_strands": n_strands,
        "n_distinct_partitions_total": n_partitions,
        "n_dual_pairs_examined": len(rows),
        "self_conjugate_count": self_dual_partitions,
        "pair_dual_count": pair_dual_count,
        "not_dual_count": not_dual_count,
        "all_dual": (not_dual_count == 0),
        "tr_M_total": tr_M_total,
        "B_term1_pred_MeV": M_E_MEV * abs(tr_M_total),
    }
    return rows, summary


def main():
    print("=" * 78)
    print("Probe — categorical magic via shell-self-duality")
    print("=" * 78)
    print(f"q_0 = {Q_0}")
    print()
    print("Test: χ_λ(β) = χ_{λ*}(β) for all partition pairs (λ, λ*) ⊢ 3A")
    print()

    out_atoms = []
    for sym, Z, N, label in ATOMS:
        A = Z + N
        n_strands = 3 * A
        print(f"━━ {sym} (Z={Z}, N={N}, A={A}, H_{n_strands}) — {label}")
        rows, summary = test_self_duality(
            Z, N, max_partitions=300 if n_strands <= 12 else 50
        )
        print(f"    {summary['n_dual_pairs_examined']} (λ, λ*) pairs examined")
        print(f"    self-conjugate (λ = λ*): {summary['self_conjugate_count']}")
        print(f"    dual-pair (χ_λ = χ_{{λ*}}): {summary['pair_dual_count']}")
        print(f"    NOT dual (χ_λ ≠ χ_{{λ*}}): {summary['not_dual_count']}")
        print(f"    all-dual (= categorically magic): {summary['all_dual']}")
        print(f"    tr_M(β) at q_0 = {summary['tr_M_total']:+.6f}")
        print(f"    B_term1_pred = m_e · |tr_M| = {summary['B_term1_pred_MeV']:.6f} MeV")
        print()
        out_atoms.append({
            "sym": sym, "Z": Z, "N": N, "A": A,
            "n_strands": n_strands,
            "label": label,
            "summary": summary,
            "rows": rows,
        })

    # Summary by Z=N vs Z≠N
    print("=" * 78)
    print("SUMMARY — categorical magic predicted vs observed")
    print("=" * 78)
    print(f"{'sym':<6} {'Z':>3} {'N':>3} {'pred':<12} {'observed':<25} {'verdict'}")
    print("-" * 78)
    for r in out_atoms:
        pred = "magic" if r["Z"] == r["N"] else "non-magic"
        observed = "all-dual" if r["summary"]["all_dual"] else "not-all-dual"
        match = (pred == "magic") == (r["summary"]["all_dual"])
        verdict = "✓ matches" if match else "✗ mismatch"
        print(f"{r['sym']:<6} {r['Z']:>3} {r['N']:>3} "
              f"{pred:<12} {observed:<25} {verdict}")
    print()

    # Build witness
    w = (
        WitnessBuilder("probe-atom-shell-self-duality", engine="python")
        .set_description(
            "Probe of the categorical magic condition (shell-self-duality) "
            "on atom braids. For each (Z, N), tests whether x_λ(β) = "
            "x_{λ*}(β) for every partition pair (λ, λ*) ⊢ 3A in the "
            "Wedderburn decomposition of H_{3A}(q) at q_0. NO Vol_hyp, "
            "NO knot identification, NO census search. Purely algebraic. "
            "Predicts: Z=N atoms are categorically magic (all dual pairs); "
            "Z≠N atoms are non-magic (some pairs not dual)."
        )
        .set_content_block("prop:shell-schur-weyl-self-duality")
        .add_parameter("q_0", Q_0)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_data("atoms", out_atoms)
        .add_caveat(
            "For atoms with n_strands ≥ 12 (A ≥ 4), the partition count "
            "grows rapidly. ⁴He at H_12 has 77 partitions; ⁸Be at H_24 "
            "has thousands. Currently probing only A ≤ 4 to keep wall-time "
            "manageable."
        )
        .add_caveat(
            "Equality test uses 1e-9 tolerance against the float64 "
            "Hoefsmit pipeline. MPFR precision would tighten this to "
            "~10⁻⁵⁰ if needed."
        )
    )
    out_path = w.save()
    print(f"Witness: {out_path.name}")


if __name__ == "__main__":
    main()
