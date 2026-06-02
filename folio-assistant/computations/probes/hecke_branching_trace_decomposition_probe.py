#!/usr/bin/env python3
"""Probe: hecke-branching-trace-decomposition
(`prop:hecke-branching-trace-decomposition`).

The proposition states that, under the Wenzl 1988 LR decomposition
`V_λ ↓_{H_{n_1}(q) ⊗ H_{n_2}(q)} = ⊕_(μ,ν) c^λ_{μ,ν} V_μ ⊗ V_ν`,
the trace satisfies

    χ^λ(β_1 · I · β_2)
      = Σ_(μ,ν) Tr_{V_μ ⊗ V_ν}(
            A^λ_{μ,ν}(I) · (ρ_μ(β_1) ⊗ ρ_ν(β_2))
        ).

For the special case `I = 𝟙` (no boundary interface), `A^λ_{μ,ν}(𝟙)`
is the identity on each multiplicity copy, so the identity collapses
to the closed Littlewood-Richardson form

    χ^λ(β_1 · β_2) = Σ_(μ,ν) c^λ_{μ,ν} · χ_μ(β_1) · χ_ν(β_2)

for `β_1 ∈ H_{n_1}(q), β_2 ∈ H_{n_2}(q)` acting on disjoint strand
groups inside `H_{n_1 + n_2}(q)`.

This probe verifies the closed form for n_1 = n_2 = 3, λ ∈ {(3,3),
(4,2), (5,1), (6), (1^6)} ⊢ 6, with β_1 = β_2 = β_{4_1} (figure-
eight) at q = q_0.  The H_6 left-hand side is computed directly
via canonical Hoefsmit; the right-hand side is computed from
single-component H_3 characters of β_{4_1} via LR coefficients.
Equality to ~1e-50 witnesses the trace-decomposition identity for
each tested λ.

This probe complements the existing
`sublemma-2-1-A-operator-extract.witness.json` (which extracts the
`A^λ_{μ,ν}(I)` operator-valued blocks via bilinear inversion across
144 (β_1, β_2) test pairs for the deuteron interface
`I = σ_2 − h/2`).  Here we run the closed-form (I = 𝟙) case for a
different value of `β`, providing an independent path that bypasses
the operator-extraction machinery.

Emits `hecke-branching-trace-decomposition-probe.witness.json`.
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
from probe_staircase_ew_k3_categorical import build_hoefsmit_mpfr  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402


# β_{4_1} = σ_1 σ_2⁻¹ σ_1 σ_2⁻¹  in B_3 (1-indexed → 0-indexed below)
BETA_4_1_WORD = [(0, +1), (1, -1), (0, +1), (1, -1)]

# β_Bor_2 = β_{4_1}^(1,2,3) · β_{4_1}^(4,5,6) ∈ B_6
# (σ_3 absent — disjoint-union separator).
BETA_BOR2_WORD = [
    (0, +1), (1, -1), (0, +1), (1, -1),
    (3, +1), (4, -1), (3, +1), (4, -1),
]

# Littlewood-Richardson coefficients c^λ_{μ,ν} for λ ⊢ 6 and
# μ, ν ⊢ 3.  Computed from standard LR rule (verified by hand;
# dim checks below confirm Σ c^λ_{μν} dim(μ) dim(ν) = dim(λ)).
# Partition keys use tuple form.
P3 = [(3,), (2, 1), (1, 1, 1)]
DIM_3 = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}

LR_COEFFS = {
    (6,): {
        ((3,), (3,)): 1,  # only fully-symmetric x fully-symmetric
    },
    (5, 1): {
        ((3,), (3,)): 1,
        ((3,), (2, 1)): 1,
        ((2, 1), (3,)): 1,
    },
    (4, 2): {
        ((3,), (3,)): 1,
        ((3,), (2, 1)): 1,
        ((2, 1), (3,)): 1,
        ((2, 1), (2, 1)): 1,
    },
    (3, 3): {
        ((3,), (3,)): 1,
        ((2, 1), (2, 1)): 1,
    },
    (1, 1, 1, 1, 1, 1): {
        ((1, 1, 1), (1, 1, 1)): 1,
    },
}

# Dimensions of H_6 irreps (= number of SYT of shape λ).
DIM_H6 = {
    (6,): 1,
    (5, 1): 5,
    (4, 2): 9,
    (3, 3): 5,
    (1, 1, 1, 1, 1, 1): 1,
}


def trace_of_word(shape: tuple[int, ...], word: list[tuple[int, int]]) -> "mp.mpf":
    """Compute Tr ρ_shape(braid word) at q = Q_MP via canonical Hoefsmit."""
    sigmas, dim = build_hoefsmit_mpfr(shape, Q_MP)
    M = mp.eye(dim)
    for idx, sgn in word:
        g = sigmas[idx] if sgn > 0 else sigmas[idx] ** (-1)
        M = M * g
    return sum(M[i, i] for i in range(dim))


def main() -> int:
    builder = WitnessBuilder(
        "hecke-branching-trace-decomposition-probe",
        engine="mpmath",
    )
    mp.dps = 50

    # Single-component H_3 characters of β_{4_1} at q_0.
    chi_single: dict[tuple[int, ...], "mp.mpf"] = {}
    for mu in P3:
        chi_single[mu] = trace_of_word(mu, BETA_4_1_WORD)

    # For each tested λ ⊢ 6, compute LHS (direct H_6 Hoefsmit trace)
    # and RHS (LR-branching prediction), then assert match.
    results: list[dict] = []
    for lam in [(6,), (5, 1), (4, 2), (3, 3), (1, 1, 1, 1, 1, 1)]:
        # LHS: direct H_6 Hoefsmit trace.
        lhs = trace_of_word(lam, BETA_BOR2_WORD)
        # RHS: Σ_{μ,ν ⊢ 3} c^λ_{μν} · χ_μ(β_{4_1}) · χ_ν(β_{4_1}).
        rhs = mp.mpf(0)
        for (mu, nu), c in LR_COEFFS[lam].items():
            rhs += mp.mpf(c) * chi_single[mu] * chi_single[nu]
        # Dim check on the branching: Σ c^λ_{μν} dim_μ dim_ν = dim_λ.
        dim_check = sum(
            c * DIM_3[mu] * DIM_3[nu]
            for (mu, nu), c in LR_COEFFS[lam].items()
        )
        residue = float(mp.fabs(lhs - rhs))
        results.append({
            "lambda": str(lam),
            "dim_H6": DIM_H6[lam],
            "dim_check_branching_sum": dim_check,
            "dim_check_match": dim_check == DIM_H6[lam],
            "lhs_h6_direct_trace": float(lhs),
            "rhs_lr_branching_sum": float(rhs),
            "residue": residue,
        })

    (
        builder
        .set_description(
            "I1 probe for prop:hecke-branching-trace-decomposition.  "
            "Verifies the closed-form (I = 𝟙) branching identity "
            "χ^λ(β_1 · β_2) = Σ_(μ,ν) c^λ_{μ,ν} χ_μ(β_1) χ_ν(β_2) "
            "for β_1 = β_2 = β_{4_1} on disjoint strand groups, "
            "λ ∈ {(6), (5,1), (4,2), (3,3), (1^6)} ⊢ 6 (n_1 = n_2 = 3).  "
            "LHS computed directly via canonical H_6 Hoefsmit-seminormal "
            "matrices (mpmath, 50 dps); RHS computed from H_3 single-"
            "component characters via Wenzl-1988 LR coefficients.  "
            "Equality witnesses Wenzl 1988 Thm 3.4 + Hoefsmit 1974 "
            "matrix-element formulas on a concrete instance, "
            "independent of the operator-extraction path in "
            "`sublemma_2_1_A_operator_extract.py`."
        )
        .set_content_block("prop:hecke-branching-trace-decomposition")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("chi_3_single", float(chi_single[(3,)]))
        .add_parameter("chi_21_single", float(chi_single[(2, 1)]))
        .add_parameter("chi_111_single", float(chi_single[(1, 1, 1)]))
        .add_data("per_partition_results", results)
        .add_data("methodology", {
            "left_hand_side": (
                "Trace of ρ_λ(β_Bor_2) ∈ End(V_λ) where "
                "β_Bor_2 = σ_1 σ_2⁻¹ σ_1 σ_2⁻¹ · σ_4 σ_5⁻¹ σ_4 σ_5⁻¹ "
                "is the disjoint product of two figure-eights in B_6.  "
                "ρ_λ is the canonical H_6 Hoefsmit-seminormal rep "
                "(satisfies Hecke quadratic AND braid relation; "
                "verified to ~1e-50 in PR #818 follow-up)."
            ),
            "right_hand_side": (
                "Σ_{μ,ν ⊢ 3} c^λ_{μ,ν} · χ_μ(β_{4_1}) · χ_ν(β_{4_1}), "
                "where c^λ_{μ,ν} are Littlewood-Richardson coefficients "
                "(table inlined in source, verified by dimension check "
                "Σ c^λ_{μν} dim_μ dim_ν = dim_λ).  Single-component "
                "characters χ_μ(β_{4_1}) computed via canonical H_3 "
                "Hoefsmit."
            ),
        })
    )

    for r in results:
        builder.add_assertion(
            name=f"branching_decomposition_lambda_{r['lambda'].replace(' ', '').replace('(', '').replace(')', '').replace(',', '_').rstrip('_')}",
            computed=r["residue"],
            expected=0.0,
            tolerance=1e-40,
            unit=(
                f"|tr_H6 ρ_{r['lambda']}(β_Bor_2) − "
                f"Σ_(μ,ν) c^{r['lambda']}_{{μν}} χ_μ χ_ν|"
            ),
            source=(
                f"Closed-form (I=𝟙) branching for λ={r['lambda']} ⊢ 6, "
                f"dim {r['dim_H6']}.  "
                f"Direct trace ≈ {r['lhs_h6_direct_trace']:.6f}; "
                f"LR prediction ≈ {r['rhs_lr_branching_sum']:.6f}."
            ),
        )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"{'λ':<25} {'dim':<5} {'LHS':<25} {'RHS':<25} {'residue':<12}")
    for r in results:
        print(f"  {r['lambda']:<23} {r['dim_H6']:<5} "
              f"{r['lhs_h6_direct_trace']:<25.15f} "
              f"{r['rhs_lr_branching_sum']:<25.15f} "
              f"{r['residue']:.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
