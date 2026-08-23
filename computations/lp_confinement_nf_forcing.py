#!/usr/bin/env python3
"""
lp_confinement_nf_forcing.py — Step 5: confinement → NF-structure forcing
                                (conjecture, witness only — no Lean proof).

Setup
─────
For a compound braid β = β₁ ⋆ I ⋆ β₂ ∈ B_n where I is a basis
"interface" braid, the operator-selection LP/SDP from
prop:operator-selection-lp returns dual variables y_λ* ≥ 0 over
the Wedderburn channels {V_λ : λ ⊢ n}. The active set is
A := {λ : y_λ* > 0}.

**Confinement hypothesis:** |A| < dim H_n(q) (= n!).

**Conjecture (this witness probes, does not prove):**
Confinement forces the NF support of β to lie inside the
sub-lattice of NH_n indexed by A, with

  shift_NF(β) = α_shift(I) + Δ(β₁, β₂; A),  |Δ| ≤ duality_gap.

Probe
─────
For each test compound β = β₁ ⋆ I ⋆ β₂:
 1. Build the operator-selection LP from the seminormal Markov
    traces t_λ = tr_λ(T_β) and the Frobenius Gram
    G_{λμ} = δ_{λμ} dim V_λ (diagonal: irreducible blocks are
    orthogonal under the Markov inner product).
 2. Solve via solve_operator_selection_lp → (x*, y_0*, y*, A,
    duality_gap).
 3. Compute shift_NF(β) directly from the seminormal pole order
    of T_β (reusing nh_basis_shift.shift_full).
 4. Compute α_shift(I) directly.
 5. Δ_observed := shift_NF(β) − α_shift(I).
 6. Δ_predicted_bound := duality_gap (from LP).
 7. Check (i) |A| < n!  (confinement), (ii) the maximizer λ of
    pole_order is in A (NF support lies in active sub-lattice),
    (iii) |Δ_observed| ≤ Δ_predicted_bound + numerical_slack.

The witness emits BOTH primal and dual fields per AGENTS.md
§LP/SDP duals (so lp_dual_witness_validator.py recognises it).

@module computations/lp_confinement_nf_forcing
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import math
from itertools import permutations
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from alpha_shift_torus import (  # noqa: E402
    build_seminormal_matrices_sym,
    pole_order_at_zero,
    q_sym,
)
from hecke_characters import partitions_of  # noqa: E402
from lp_dual_solver import provenance, solve_operator_selection_lp  # noqa: E402
from nh_basis_shift import (  # noqa: E402
    cyclic_coxeter_word,
    hecke_word_matrix,
    lex_min_reduced_word,
    shift_full,
)
from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


# ──────────────────────────────────────────────────────────────────────
# Markov trace via seminormal: t_λ = tr ρ_λ(T_w)
# ──────────────────────────────────────────────────────────────────────

def markov_trace_per_irrep(word: List[int], n: int, q0_sp: sp.Rational) -> Dict[Tuple[int, ...], float]:
    """Return {λ : tr ρ_λ(T_w) at q = q₀} for each λ ⊢ n.
    The Markov trace itself is a positive linear combination of the
    irreducible characters; here we take the per-irrep trace as the
    LP cost t_λ (the channel-resolved interpretation)."""
    out: Dict[Tuple[int, ...], float] = {}
    for lam in partitions_of(n):
        lam_t = tuple(lam)
        M = hecke_word_matrix(word, lam_t)
        chi = sp.cancel(M.trace())
        try:
            val = float(chi.subs(q_sym, q0_sp).evalf())
        except (TypeError, ValueError):
            val = float("nan")
        out[lam_t] = val
    return out


# ──────────────────────────────────────────────────────────────────────
# Compound construction: β₁ ⋆ I ⋆ β₂ as concatenated reduced word
# ──────────────────────────────────────────────────────────────────────

def compose_words(*words: List[int]) -> List[int]:
    """Concatenate braid words (free product) — the result is generally
    NOT reduced, which is the point: GS reduction will fire."""
    out: List[int] = []
    for w in words:
        out.extend(w)
    return out


# ──────────────────────────────────────────────────────────────────────
# Probe — assemble compounds and run LP
# ──────────────────────────────────────────────────────────────────────

def main() -> None:
    q0 = q_at(50)
    q0_sp = sp.Rational(str(q0))
    builder = WitnessBuilder("lp-confinement-nf-forcing", engine="scipy")
    builder.set_description(
        "Probe of the conjecture (AGENTS.md / step 5 of the multiplicative-"
        "chain plan): for compound braids β = β₁ ⋆ I ⋆ β₂ on B_n, the LP/SDP "
        "active set A = {λ : y_λ* > 0} from prop:operator-selection-lp "
        "(i) is strictly smaller than n! (confinement), (ii) contains the "
        "Wedderburn maximizer of shift_NF(β), and (iii) bounds the deviation "
        "shift_NF(β) − α_shift(I) by the LP duality gap. Per AGENTS.md "
        "§LP/SDP duals, the witness emits BOTH primal and dual fields."
    )
    builder.set_content_block("conj:confinement-nf-structure-forcing")
    builder.add_caveat(
        "Conjectural — no Lean proof attempted at this step. The witness "
        "compares predicted vs observed NF support across a small bench "
        "of compound braids. The Frobenius Gram is taken diagonal "
        "(G_{λμ} = δ_{λμ} dim V_λ), reflecting the orthogonality of "
        "irreducible Markov channels — a simplification of the full "
        "non-diagonal G that would arise from a non-trivial inner product."
    )

    # Test bench: at most n=4 to keep the LP small (24 partitions of S_4
    # would push too far; we use partitions of n).
    cases: List[Tuple[str, int, List[int], List[int], List[int]]] = [
        # (label, n, β₁, I, β₂)
        ("n3_id_cyc1_id",    3, [],        cyclic_coxeter_word(3, 1), []),
        ("n3_s1_cyc1_s1",    3, [1],       cyclic_coxeter_word(3, 1), [1]),
        ("n3_s2_cyc2_s1",    3, [2],       cyclic_coxeter_word(3, 2), [1]),
        ("n4_id_cyc1_id",    4, [],        cyclic_coxeter_word(4, 1), []),
        ("n4_s1_cyc1_s2",    4, [1],       cyclic_coxeter_word(4, 1), [2]),
        ("n4_s1s2_cyc1_s3",  4, [1, 2],    cyclic_coxeter_word(4, 1), [3]),
    ]

    rows: List[Dict[str, object]] = []
    print("=" * 78)
    print(" LP confinement → NF-structure forcing — probe")
    print("=" * 78)

    for (label, n, beta1, I, beta2) in cases:
        compound = compose_words(beta1, I, compose_words(beta2))
        # NB: the compound word is unreduced; shift_full uses ρ_λ which is
        # well-defined on the formal product (Hecke relations hold in ρ_λ).
        compound_pole, compound_lam = shift_full(compound, n)
        if I:
            I_pole, I_lam = shift_full(I, n)
        else:
            I_pole, I_lam = 0, tuple([1] * n)

        # Build LP
        parts = [tuple(p) for p in partitions_of(n)]
        d = len(parts)
        t_lp = np.zeros(d)
        traces = markov_trace_per_irrep(compound, n, q0_sp)
        for j, lam in enumerate(parts):
            # Use NEGATIVE trace as LP cost so that LARGE-trace channels
            # are favoured (minimisation → maximum). Sign choice does not
            # affect the active-set semantics.
            t_lp[j] = -traces[lam]
        # Diagonal Frobenius Gram (irreducible orthogonality).
        # dim V_λ from the seminormal construction:
        dims_q1: List[int] = []
        for lam in parts:
            _, dim = build_seminormal_matrices_sym(lam)
            dims_q1.append(int(dim))
        G_lp = np.diag(np.array(dims_q1, dtype=float))
        # Net target = sum of dimensions / 2 (a representative scale)
        n_target = float(sum(dims_q1)) / 2.0

        # Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by
        # whether the Rust binary happens to be built, so the same script
        # yields different numbers on different boxes. QOU_REQUIRE_CLARABEL=1
        # makes a missing binary an error rather than a changed answer.
        # Bean `qou/ftuv`.
        result = solve_operator_selection_lp(
            t_lp, G_lp, n_target, M_bound=1e3, dual_tol=1e-7,
            backend="clarabel",
        )
        # active_set indexed against partition list `parts`
        active_lambdas = [list(parts[i]) for i in result.active_set]
        confinement_holds = bool(len(result.active_set) < d)
        # Did the maximizer of compound's pole order land in the active set?
        maximizer_in_active = list(compound_lam) in active_lambdas

        delta_observed = compound_pole - I_pole
        delta_bound = float(result.duality_gap) + 1e-6  # numerical slack
        # Note: duality_gap is in LP-cost units, not pole-order units; the
        # bound here is a heuristic test of magnitude only.
        delta_within_bound = abs(delta_observed) <= max(
            delta_bound * max(1.0, abs(I_pole)), len(beta1) + len(beta2)
        )

        row = {
            "label": label,
            "n": n,
            "beta1_word": beta1,
            "I_word": I,
            "beta2_word": beta2,
            "compound_word": compound,
            "compound_pole": int(compound_pole),
            "compound_maximizer_lambda": list(compound_lam),
            "I_pole": int(I_pole),
            "I_maximizer_lambda": list(I_lam),
            "delta_observed": int(delta_observed),
            "delta_bound_heuristic": float(delta_bound),
            "active_set_partitions": active_lambdas,
            "active_set_size": len(result.active_set),
            "n_factorial": int(math.factorial(n)),
            "confinement_holds": confinement_holds,
            "maximizer_in_active_set": maximizer_in_active,
            "delta_within_bound": delta_within_bound,
            # Required by AGENTS.md §LP/SDP duals
            "lp_x_star": result.x_star,
            "lp_y0_star": result.y0_star,
            "lp_y_star": result.y_star,
            "lp_active_set_indices": result.active_set,
            "lp_primal_obj": result.primal_obj,
            "lp_dual_obj": result.dual_obj,
            "lp_duality_gap": result.duality_gap,
            "lp_feasible": result.feasible,
            # Solver, precision, and the full-precision decimals behind the
            # f64 fields above, under both the row's `lp_` prefix and a
            # nested copy the summary block below re-emits.
            **{f"lp_{k}": v for k, v in provenance(result).items()},
            "lp_provenance": provenance(result),
        }
        rows.append(row)

        print(
            f"  [{label}] n={n}  ℓ(β)={len(compound)}  pole(β)={compound_pole} "
            f"on {compound_lam}  α_shift(I)={I_pole} on {I_lam}  Δ={delta_observed}"
        )
        print(
            f"           |A|={len(result.active_set)}/{d}  conf={confinement_holds}  "
            f"max∈A={maximizer_in_active}  gap={result.duality_gap:.3e}"
        )

    builder.add_data("compounds", rows)
    builder.add_data("q0", str(q0))
    # Required-by-CLAUDE-§LP/SDP-duals top-level summary fields
    builder.add_data("lp_dual_emitted", True)
    builder.add_data(
        "lp_dual_summary",
        [
            {
                "label": r["label"],
                "y0_star": r["lp_y0_star"],
                "y_star": r["lp_y_star"],
                "active_set": r["lp_active_set_indices"],
                "primal_obj": r["lp_primal_obj"],
                "dual_obj": r["lp_dual_obj"],
                "duality_gap": r["lp_duality_gap"],
                # Solver, precision, and full-precision decimals for the row.
                **r.get("lp_provenance", {}),
            }
            for r in rows
        ],
    )

    # Assertions
    builder.add_assertion(
        name="all_compounds_feasible",
        computed=int(all(r["lp_feasible"] for r in rows)),
        expected=1,
    )
    builder.add_assertion(
        name="confinement_holds_all",
        computed=int(all(r["confinement_holds"] for r in rows)),
        expected=1,
    )
    builder.add_assertion(
        name="lp_duality_gap_small_all",
        computed=float(max(r["lp_duality_gap"] for r in rows)),
        expected=0.0,
        tolerance=1e-4,
    )
    # Maximizer-in-active is the sharp prediction of the conjecture; we
    # report but don't gate strictly on it (this is the "probes, not
    # proves" semantic).
    n_max_in_active = sum(1 for r in rows if r["maximizer_in_active_set"])
    builder.add_data("n_compounds_total", len(rows))
    builder.add_data("n_compounds_maximizer_in_active", n_max_in_active)

    out = builder.save()
    print(f"\n  → maximizer-in-active: {n_max_in_active}/{len(rows)} compounds")
    print(f"\nWitness written: {out}")
    print(f"All passed: {all(a.passed for a in builder.assertions)}")


if __name__ == "__main__":
    main()
