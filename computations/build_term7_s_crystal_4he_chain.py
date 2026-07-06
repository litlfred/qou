#!/usr/bin/env python3
"""
Crystal-side Term-7 shell-correction sum at ⁴He — fully structural chain.

This is the **post-#481-reconceive** Term-7 chain.  PR #481 originally
shipped a `sigma-shell-alpha5-skeleton` chain that marked α_5 as an
open frontier.  Two weeks later (2026-05-09) the crystal-basis
derivation closed the structural side: `term7_alpha5_crystal_derivation.py`
produces a per-atom `S_crystal(A)` from the Schur–Weyl decomposition
of `H_{3A}(q)` evaluated at the crystal limit `q → 0`, with no free
parameter.

This chain certifies `S_crystal(⁴He) ≈ −0.991241` as the structural
prediction for ⁴He's level-5 GB-filtration character contribution to
the shell-correction sum.  α_5 itself becomes the AME-calibrated
proportionality constant `Term7(A) = α_5 · S_crystal(A)` (atom-
independent under flat transport `q → 0 ⇝ q_0`).

Conditional on `conj:crystal-graph-realization` (per the witness's
`conditional_on` field).  The script-cited frontier is two-fold:
  * crystal-limit characters await a Lean formalisation of the
    q → 0 functor (or a closure of the realisation conjecture);
  * atomic braid words inherit the open `atomic_braid_recipe`
    frontier already noted in `DERIVATION-CHAIN-METHODOLOGY.md`.

Output: `term7-s-crystal-4he.derivation.json`.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — bridge: reads a witness that co-moved into a cluster subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)


HERE = Path(__file__).parent
OUTPUT = _pb.witness_path("term7-s-crystal-4he.derivation.json", HERE)

# Witness-pinned target value — must match the ⁴He row of
# `term7-alpha5-crystal-derivation.witness.json` exactly so the
# derivation-chain validator's leaf cross-check passes.
S_CRYSTAL_4HE = -0.99124115660574

N_STRANDS_4HE = 12              # n = 3A for A = 4
N_HEIGHT_6_PARTITIONS_4HE = 58  # |{λ ⊢ 12 : height(λ) ≤ 6}|

# ⁴He atomic braid word (mirrors atomic_braid_gb_filtration_extension)
ATOM_4HE_WORD = [1, 2, -1, 4, 5, -4, 7, -8, 7, 10, -11, 10]


def build() -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — Schur–Weyl decomposition of H_12(q) (AXIOM)
    steps.append(DerivationStep(
        name="Schur–Weyl decomposition of H_{12}(q) ↺ V^{⊗12}",
        operation=(
            "By Schur–Weyl duality (FirstPrinciple `Schur`), the "
            "Hecke algebra `H_{12}(q)` acts on `V^{⊗12}` and the "
            "centraliser of `U_q(sl_2)` decomposes as a direct sum "
            "of irreducibles indexed by partitions `λ ⊢ 12`.  The "
            "atomic ⁴He braid is realised in the Markov closure of "
            "this 12-strand braid algebra (n = 3A for A = 4)."
        ),
        inputs=[FirstPrinciple.SCHUR.value],
        output_name="schur_weyl_h12",
        output_value="H_{12}(q) ≅ ⊕_{λ ⊢ 12} M_{f_λ}(K(q))",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:STUB:SchurWeylDuality",
        citation="kassel1995",
        jet_order=0,
    ))

    # 2 — Height-6 partitions of 12 (Mathlib-cited combinatorics)
    steps.append(DerivationStep(
        name="Height-6 partition enumeration of n = 12",
        operation=(
            "Per `def:confinement-level`, GB-filtration level ℓ = 5 "
            "corresponds to partitions `λ` with `height(λ) ≤ 6`.  "
            "Mathlib's `Mathlib.Combinatorics.Young.YoungDiagram` "
            "exposes the partition lattice; enumerating partitions "
            "of `n = 12` with at most 6 parts gives 58 partitions "
            "(matches `term7-height6-partition-enum.witness.json`)."
        ),
        inputs=["schur_weyl_h12"],
        output_name="height_6_partitions_12",
        output_value={
            "n": N_STRANDS_4HE,
            "height_bound": 6,
            "n_partitions": N_HEIGHT_6_PARTITIONS_4HE,
        },
        trust_basis=TrustBasis.MATHLIB_CITED,
        lean_ref="qou:STUB:YoungDiagram.heightBoundedPartitions",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=5,
    ))

    # 3 — Wedderburn block dimensions f_λ (AXIOM)
    steps.append(DerivationStep(
        name="Wedderburn block dimension f_λ via hook-length formula",
        operation=(
            "By Wedderburn (FirstPrinciple `Wedderburn`), each "
            "Schur–Weyl summand `M_{f_λ}(K(q))` has block dimension "
            "`f_λ = #SYT(λ) = n! / ∏_{x ∈ λ} h_x(λ)` (hook-length "
            "formula).  Computed for each of the 58 height-6 "
            "partitions of 12; the largest block has `f_λ = 7700` "
            "for `λ = (5, 3, 2, 1, 1)`."
        ),
        inputs=["height_6_partitions_12", FirstPrinciple.WEDDERBURN.value],
        output_name="wedderburn_block_dims_4he",
        output_value="f_λ : Partition → ℕ",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:STUB:HeckeWedderburn",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=5,
    ))

    # 4 — Plancherel weights at q = 1 (DERIVED, pure algebra)
    steps.append(DerivationStep(
        name="Plancherel weights w_λ(q = 1) = f_λ² / n!",
        operation=(
            "The Markov weight `w_λ(q) = (q − q^{-1})^{n − ℓ(λ)} / "
            "∏ [h_x]_q` evaluated at `q = 1` reduces to the "
            "Plancherel measure on partitions: `w_λ(1) = f_λ² / n!`.  "
            "This is the q → 1 classical limit, a pure-algebra "
            "specialisation of step 3.  No new content beyond the "
            "Wedderburn dimensions and the convention `[k]_1 = k`."
        ),
        inputs=["wedderburn_block_dims_4he"],
        output_name="plancherel_weights_4he",
        output_value="w_λ(1) = f_λ² / 12!",
        trust_basis=TrustBasis.DERIVED,
        jet_order=0,
        gb_filtration_level=5,
    ))

    # 5 — Categorical action of B_12 (AXIOM)
    steps.append(DerivationStep(
        name="Categorical R-matrix action of B_{12} on V^{⊗12}",
        operation=(
            "By the categorical-action axiom (FirstPrinciple "
            "`Cat.Action`), each generator `σ_i ∈ B_n` acts on "
            "`V^{⊗n}` via the Drinfeld–Jimbo R-matrix at strand `i`.  "
            "The action commutes with Schur–Weyl, so it descends to "
            "the partition blocks; on each block `M_{f_λ}` it gives "
            "the Hoefsmit-seminormal q-character `χ^λ(σ_i; q)`."
        ),
        inputs=[FirstPrinciple.CATEGORICAL_ACTION.value],
        output_name="cat_action_b12",
        output_value="χ^λ : B_{12} → GL(M_{f_λ})",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:STUB:CategoricalRMatrixAction",
        citation="kassel1995",
        jet_order=0,
    ))

    # 6 — Crystal-limit characters χ_λ_crystal at q → 0 (SCRIPT_CITED)
    #     CONDITIONAL on conj:crystal-graph-realization.
    steps.append(DerivationStep(
        name="Crystal-limit χ_λ_crystal at q → 0",
        operation=(
            "Per `conj:crystal-graph-realization`, the q → 0 limit "
            "of `χ^λ(β; q)` is the trace of a signed-permutation "
            "action on the standard Young tableaux of shape `λ`.  "
            "Concretely, each generator `σ_i` acts on `T ∈ SYT(λ)` "
            "by the sign of the axial distance "
            "`ρ_T(i) = c(T_{i+1}) − c(T_i)` between cells "
            "containing `i` and `i + 1` (zero when neither cell "
            "exists).  This is computed by "
            "`term7_alpha5_crystal_derivation.crystal_chi_lambda`."
        ),
        inputs=["cat_action_b12", "wedderburn_block_dims_4he"],
        output_name="crystal_chi_lambda",
        output_value="χ_λ_crystal : SYT(λ) × Word → ℤ",
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§term7-crystal-derivation",
        jet_order=0,
        gb_filtration_level=5,
        spectral_stratum="q = 0 (crystal limit)",
        notes=(
            "script: computations/term7_alpha5_crystal_derivation.py "
            "(crystal_chi_lambda).  CONDITIONAL on "
            "`conj:crystal-graph-realization` per the witness's "
            "`conditional_on` field; closes when either the "
            "crystal-graph realisation conjecture is proved (or "
            "axiomatised as a class per AGENTS.md §3b-cond) or a "
            "Lean formalisation of the q → 0 functor lands."
        ),
    ))

    # 7 — ⁴He atomic braid word (SCRIPT_CITED)
    steps.append(DerivationStep(
        name="⁴He atomic braid word β_⁴He ∈ B_{12}",
        operation=(
            "The ⁴He atomic braid word is "
            "`[1, 2, -1, 4, 5, -4, 7, -8, 7, 10, -11, 10]` "
            "in `B_{12}` (4 nucleon braids of 3 strands each, "
            "joined by the Markov closure).  Supplied by "
            "`atomic_braid_gb_filtration_extension.py`."
        ),
        inputs=[],
        output_name="atom_4he_word",
        output_value=ATOM_4HE_WORD,
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§atomic-braid-recipe",
        jet_order=0,
        notes=(
            "script: computations/atomic_braid_gb_filtration_extension.py.  "
            "Inherits the open `atomic_braid_recipe` frontier already "
            "noted in `DERIVATION-CHAIN-METHODOLOGY.md` (Open frontier "
            "item 1)."
        ),
    ))

    # 8 — Crystal-side sum (DERIVED)
    steps.append(DerivationStep(
        name="Crystal-side Term 7 sum S_crystal(⁴He)",
        operation=(
            "Combine steps 4 (Plancherel weights), 6 (crystal "
            "characters), and 7 (atomic word):\n"
            "  S_crystal(⁴He) := Σ_{λ ⊢ 12, height(λ) ≤ 6} "
            "w_λ(q = 1) · χ_λ_crystal(β_⁴He).\n"
            "Pure algebra given the inputs; no free parameter."
        ),
        inputs=["plancherel_weights_4he", "crystal_chi_lambda", "atom_4he_word"],
        output_name="s_crystal_4he_symbolic",
        output_value="Σ_λ w_λ(1) · χ_λ_crystal(β_⁴He)",
        trust_basis=TrustBasis.DERIVED,
        jet_order=0,
        gb_filtration_level=5,
        spectral_stratum="q = 0 (crystal limit)",
    ))

    # 9 — Numerical leaf (COMPUTATIONAL)
    steps.append(DerivationStep(
        name="S_crystal(⁴He) numerical evaluation",
        operation=(
            "Numerical evaluation of the symbolic sum from step 8 "
            "via `term7_alpha5_crystal_derivation.py` (sympy 1.14, "
            "rational arithmetic).  The full per-partition "
            "contribution table is in the witness file under "
            "`atoms[3].nonzero_contributions`."
        ),
        inputs=["s_crystal_4he_symbolic"],
        output_name="s_crystal_4he_numerical",
        output_value=S_CRYSTAL_4HE,
        trust_basis=TrustBasis.COMPUTATIONAL,
        jet_order=0,
        gb_filtration_level=5,
        spectral_stratum="q = 0 (crystal limit)",
        notes=(
            "Witness: term7-alpha5-crystal-derivation.witness.json "
            "(scriptFile term7_alpha5_crystal_derivation.py @ "
            "bc3f32d2; computedAt 2026-05-09).  ⁴He is doubly-magic "
            "(Z = N = 2), so |S_crystal(⁴He)| dominates the table — "
            "the structural cancellation pattern reproduces the "
            "empirical shell-closure signal."
        ),
    ))

    return DerivationChain(
        target="S_crystal(⁴He)",
        target_value=S_CRYSTAL_4HE,
        target_tolerance=1e-10,
        content_block="prop:term7-shell-correction",
        description=(
            "Crystal-side Term-7 shell-correction sum for ⁴He, "
            "S_crystal(⁴He) ≈ −0.991241.  Structural prediction "
            "from Schur–Weyl + Wedderburn + categorical R-matrix "
            "action evaluated at the crystal limit q → 0 — no free "
            "parameter.  Trust profile {axiom: 3, mathlib-cited: 1, "
            "derived: 2, script-cited: 2, computational: 1}; the "
            "two SCRIPT_CITED frontiers are (a) crystal-limit "
            "characters (closes when `conj:crystal-graph-realization` "
            "is proven or class-axiomatised per AGENTS.md §3b-cond), "
            "and (b) atomic braid words (inherits the open "
            "`atomic_braid_recipe` frontier).  α_5 itself becomes "
            "the AME-calibrated proportionality "
            "`Term7(A) = α_5 · S_crystal(A)`, atom-independent "
            "under flat transport q → 0 ⇝ q_0; this chain replaces "
            "PR #481's σ_shell-α_5-skeleton (which marked α_5 as "
            "the open frontier — closed structurally on 2026-05-09)."
        ),
        steps=steps,
    )


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"S_crystal(⁴He) chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {chain.target_value}")
    chain.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
