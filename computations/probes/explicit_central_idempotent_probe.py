#!/usr/bin/env python3
"""Probe: explicit-central-idempotent
(`prop:explicit-central-idempotent`).

The proposition gives an explicit Lagrange-interpolation formula
for the central primitive idempotents of H_n(q):

    e_λ  =  Σ_{T ∈ SYT(λ)}  Π_{k=1}^n  Π_{□ ∈ λ, □ ≠ T(k)}
              (J_k − c(□; q)) / (c(T(k); q) − c(□; q))

where c(□; q) = q^{2(j − i)} for cell □ = (i, j).

In the Hoefsmit-seminormal basis, the JM element J_k acts diagonally
on v_{T'} (T' ∈ SYT(μ)) with eigenvalue q^{2c(T'(k))}.  Substituting
this into the Lagrange product gives a SCALAR for each pair (T, T'),
and the proposition predicts the result of e_λ acting on v_{T'} is:

    e_λ · v_{T'}  =  δ_{λ, μ}  ·  v_{T'}    (μ = shape(T'))

i.e., e_λ is the orthogonal projector onto the λ-isotypic block.

This probe verifies, for n = 3 across all (λ, μ) ∈ {(3), (2,1),
(1^3)}² and all T' ∈ SYT(μ):

  (1) e_λ on v_{T'} = 1 when λ = μ  (idempotent value 1 on its
      own block).
  (2) e_λ on v_{T'} = 0 when λ ≠ μ  (orthogonality between blocks).
  (3) Σ_λ e_λ on any v_{T'} = 1 (completeness).

All residues at ~1e-50.

Emits `explicit-central-idempotent-probe.witness.json`.
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
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from mpmath import mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from hecke_character_symbolic import standard_young_tableaux  # noqa: E402


def _e_lambda_eigenvalue_on_syt(lam, mu, T_prime, q,
                                 union_contents=None):
    """Compute e_λ acting on the Hoefsmit basis vector v_{T'} for
    T' ∈ SYT(μ).  T_prime is a dict {entry → cell_idx_in_μ}.

    Returns the scalar that e_λ multiplies v_{T'} by, via the
    Lagrange-interpolation formula with JM eigenvalues substituted.

    `union_contents` is a list of integer cell contents over which
    the Lagrange product ranges.  Two regimes:

      · `union_contents = None` — use ONLY the cells of λ (the
        proposition's literal statement).  This is the regime in
        which the formula has a known issue: the off-block
        projection does NOT vanish, because the JM eigenvalue
        q^{2c(T'(k))} for T' ∈ SYT(μ ≠ λ) typically does not
        match any cell of λ.

      · `union_contents = <list of all distinct cell contents
        across every partition μ ⊢ n>` — the CORRECTED Lagrange
        product.  This is the form that actually gives the central
        idempotent projector onto V_λ.
    """
    syts_lam, _, contents_lam = standard_young_tableaux(lam)
    if not syts_lam:
        return mp.mpf(0)

    n = sum(lam)
    _syts_mu, _cells_mu, contents_mu = standard_young_tableaux(mu)
    jm_eigs = [
        q ** (2 * contents_mu[T_prime[k]])
        for k in range(1, n + 1)
    ]

    if union_contents is None:
        # Literal proposition: project over cells of λ only.
        # Inner product factor list per k is "cells of λ excluding
        # T(k)" — referenced by cell index.
        lam_cells_indices = list(range(n))

        def factor_contents_for_k(T, k):
            return [contents_lam[box] for box in lam_cells_indices
                     if box != T[k]]
    else:
        # Corrected: project over the UNION of all distinct contents
        # across every partition of n.  Excluded value is the
        # specific content c(T(k); q).
        def factor_contents_for_k(T, k):
            c_T_k = contents_lam[T[k]]
            return [c for c in union_contents if c != c_T_k]

    total = mp.mpf(0)
    for T in syts_lam:
        product_over_k = mp.mpf(1)
        for k in range(1, n + 1):
            t_k_content = contents_lam[T[k]]
            num = mp.mpf(1)
            den = mp.mpf(1)
            for box_content in factor_contents_for_k(T, k):
                num *= jm_eigs[k - 1] - q ** (2 * box_content)
                den *= (q ** (2 * t_k_content)
                          - q ** (2 * box_content))
            product_over_k *= num / den
        total += product_over_k
    return total


def _union_contents_for_n(shapes, n):
    """All distinct cell contents across every partition of n."""
    contents_set: set[int] = set()
    for shape in shapes:
        _, _, contents = standard_young_tableaux(shape)
        contents_set.update(contents)
    return sorted(contents_set)


def main() -> int:
    builder = WitnessBuilder(
        "explicit-central-idempotent-probe",
        engine="mpmath",
    )
    mp.dps = 50

    q = Q_MP
    SHAPES = [(3,), (2, 1), (1, 1, 1)]
    n = 3

    union_contents = _union_contents_for_n(SHAPES, n)

    def _run_pass(union_arg):
        per_rows = []
        max_own_block_resid = mp.mpf(0)
        max_off_block_resid = mp.mpf(0)
        max_complete_resid = mp.mpf(0)
        for mu in SHAPES:
            syts_mu, _, _ = standard_young_tableaux(mu)
            for T_idx, T_prime in enumerate(syts_mu):
                row_data = {
                    "mu": str(mu),
                    "T_prime_index": T_idx,
                    "e_lambda_values": {},
                }
                sum_over_lambda = mp.mpf(0)
                for lam in SHAPES:
                    val = _e_lambda_eigenvalue_on_syt(
                        lam, mu, T_prime, q,
                        union_contents=union_arg)
                    row_data["e_lambda_values"][str(lam)] = float(val)
                    sum_over_lambda += val
                    if lam == mu:
                        residue = mp.fabs(val - 1)
                        max_own_block_resid = max(
                            max_own_block_resid, residue)
                    else:
                        residue = mp.fabs(val)
                        max_off_block_resid = max(
                            max_off_block_resid, residue)
                row_data["sum_over_lambda"] = float(sum_over_lambda)
                completeness_residue = mp.fabs(sum_over_lambda - 1)
                max_complete_resid = max(max_complete_resid,
                                          completeness_residue)
                row_data["completeness_residue"] = float(
                    completeness_residue)
                per_rows.append(row_data)
        return (per_rows,
                float(max_own_block_resid),
                float(max_off_block_resid),
                float(max_complete_resid))

    # Pass 1 — literal proposition formula (cells of λ only).
    literal_rows, lit_own, lit_off, lit_complete = _run_pass(None)

    # Pass 2 — corrected formula (cells over union of all μ ⊢ n).
    corrected_rows, cor_own, cor_off, cor_complete = _run_pass(
        union_contents)

    max_idempotent_value_residue = mp.mpf(cor_own)
    max_off_block_residue = mp.mpf(cor_off)
    max_completeness_residue = mp.mpf(cor_complete)
    per_lambda_mu = corrected_rows

    (
        builder
        .set_description(
            "I1 probe for prop:explicit-central-idempotent.  "
            "Verifies the Lagrange-interpolation formula for the "
            "central primitive idempotents e_λ in H_3(q) — with a "
            "scope correction surfaced by the probe.  The "
            "proposition's literal statement has the inner product "
            "range over cells of λ only; with that scope, the "
            "off-block projection does NOT vanish (off-block residue "
            f"~{lit_off:.2e}).  The CORRECTED formula ranges the "
            "inner product over the UNION of cell contents across "
            "every μ ⊢ n (= {-2, -1, 0, 1, 2} for n = 3), and "
            "gives the actual central idempotent structure: e_λ on "
            "v_{T'} = δ_{λ,μ}, with completeness Σ_λ e_λ = 1, both "
            "to ~1e-50 numerical precision.  Surfacing the "
            "correction is a paper-level note flagged via the "
            "small-moderate-fix-rides-on-active-PR rule."
        )
        .set_content_block("prop:explicit-central-idempotent")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("num_syts_tested", sum(
            len(standard_young_tableaux(mu)[0]) for mu in SHAPES))
        .add_parameter("max_idempotent_value_residue",
                       float(max_idempotent_value_residue))
        .add_parameter("max_off_block_residue",
                       float(max_off_block_residue))
        .add_parameter("max_completeness_residue",
                       float(max_completeness_residue))
        .add_data("per_lambda_mu_T_prime_corrected_formula",
                  per_lambda_mu)
        .add_data("per_lambda_mu_T_prime_literal_formula",
                  literal_rows)
        .add_data("formula_scope_correction_note", {
            "literal_proposition_scope":
                "Inner Lagrange product ranges over cells of λ only.",
            "literal_off_block_residue": lit_off,
            "literal_completeness_residue": lit_complete,
            "corrected_scope": (
                "Inner Lagrange product ranges over the UNION of "
                "distinct cell contents across all μ ⊢ n.  For "
                "n = 3 this is {-2, -1, 0, 1, 2}."
            ),
            "corrected_off_block_residue": cor_off,
            "corrected_completeness_residue": cor_complete,
            "interpretation": (
                "The proposition's literal formula projects within "
                "the JM-eigenvalue lattice of λ but does not "
                "automatically vanish on off-block JM eigenvalues "
                "drawn from cells of distinct partitions.  The "
                "standard literature formula extends the inner "
                "product over the full distinct-content set so that "
                "the Lagrange factor (J_k - q^{2c(T'(k))}) appears "
                "literally when T' ∈ SYT(μ ≠ λ), forcing off-block "
                "vanishing.  Recommendation: update the proposition "
                "to make the inner-product scope explicit."
            ),
        })
        .add_assertion(
            name="e_lambda_eigenvalue_1_on_own_block",
            computed=float(max_idempotent_value_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over (λ ⊢ 3, T' ∈ SYT(λ)) of |e_λ · v_{T'} − 1|"
            ),
            source=(
                "Lagrange interpolation gives the unique projector "
                "with eigenvalue 1 on the desired tableau slot."
            ),
        )
        .add_assertion(
            name="e_lambda_orthogonality_off_block",
            computed=float(max_off_block_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over (λ ⊢ 3, μ ⊢ 3 with μ ≠ λ, T' ∈ SYT(μ)) "
                "of |e_λ · v_{T'} − 0|"
            ),
            source=(
                "Cells of distinct partitions have distinct content "
                "multisets in this regime; the Lagrange product "
                "vanishes when JM eigenvalues for T' miss the cell "
                "set of λ."
            ),
        )
        .add_assertion(
            name="completeness_sum_e_lambda_equals_1",
            computed=float(max_completeness_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over T' ∈ ∪_μ SYT(μ) of |Σ_λ e_λ · v_{T'} − 1|"
            ),
            source=(
                "Σ_λ e_λ = 1 in H_n(q) — partition into Wedderburn "
                "blocks is complete."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print("e_λ eigenvalue on v_{T'}, per (μ, T'_index) row:")
    print(f"{'μ':<12} {'T_idx':<5} {'e_(3) value':<15} "
          f"{'e_(2,1) value':<15} {'e_(1^3) value':<15} {'Σ':<8}")
    for r in per_lambda_mu:
        e3 = r['e_lambda_values'].get('(3,)', 0.0)
        e21 = r['e_lambda_values'].get('(2, 1)', 0.0)
        e111 = r['e_lambda_values'].get('(1, 1, 1)', 0.0)
        print(f"  {r['mu']:<10} {r['T_prime_index']:<5} "
              f"{e3:<15.10e} {e21:<15.10e} {e111:<15.10e} "
              f"{r['sum_over_lambda']:.6f}")
    print()
    print(f"max own-block residue:   "
          f"{float(max_idempotent_value_residue):.2e}")
    print(f"max off-block residue:   "
          f"{float(max_off_block_residue):.2e}")
    print(f"max completeness residue: "
          f"{float(max_completeness_residue):.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
