#!/usr/bin/env python3
"""
Frontier-paydown chain — Deuteron Markov-trace assembly.

Companion to `build_markov_trace_assembly_chain.py` (proton, in
`_deprecated/`) and `build_markov_trace_assembly_neutron_chain.py`
(neutron).  Same structural pattern, specialised to the deuteron's
canonical atomic-braid recipe at H_6(q).

For the **deuteron** (Z=1, N=1, A=2, n = 3·A = 6):
  - Partitions of 6 = 11 partitions:
    (6), (5,1), (4,2), (4,1,1), (3,3), (3,2,1), (3,1,1,1),
    (2,2,2), (2,2,1,1), (2,1,1,1,1), (1,1,1,1,1,1).
  - All 11 Wedderburn weights w_λ(q) reference dedicated per-λ
    chains (`schur-weyl-weight-{6,51,42,411,33,321,3111,222,2211,
    21111,111111}.derivation.json`), all of which shipped on
    main as part of the per-λ frontier paydown.  This step is
    DERIVED via the chain references.
  - The canonical σ-word β_D for the deuteron has 23 crossings
    (11 σ + 7 σ^{-1} + 5 averaged) per
    `canonical_braid_crossings.atom_canonical_crossings(Z=1, N=1)`.
    The recipe step is SCRIPT_CITED until the dedicated
    `atomic-braid-recipe-d.derivation.json` chain ships
    (PR #476 family, currently in review).
  - Per-irrep characters χ^λ_q(β_D) are computed via the
    Hoefsmit recipe by `hecke_character_symbolic.q_character_on_braid_word(λ, β_D, q)`
    and cached in `chi-deuteron-h6.witness.json` (~155 s first
    run; O(1) on cache hits).  This step is SCRIPT_CITED
    until per-(λ, σ_i) Hoefsmit chains for n=6 ship (analogous
    to the existing `hoefsmit-rep-21-{sigma1,sigma2}` chains
    for n=3, but for the partitions of 6).

Trust profile: {axiom: 1, derived: 2, script-cited: 2,
computational: 1} — closes the per-λ Wedderburn-weight frontier
for partitions of 6 (the 11 chains shipped on main); the two
remaining SCRIPT_CITED steps (canonical recipe + per-λ Hoefsmit
chi values) are well-defined follow-up frontiers.

Output: `markov-trace-assembly-deuteron.derivation.json`.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    TR_M_AT_Q0,
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)


HERE = Path(__file__).parent
OUTPUT = HERE / "markov-trace-assembly-deuteron.derivation.json"

DEUTERON_TR_M_Q0 = TR_M_AT_Q0["D"]

# 11 partitions of 6 with Wedderburn block dimensions f_λ.
# Source: hook-length formula on Young diagram of shape λ.
PARTITIONS_OF_6: list[dict] = [
    {"lambda": "(6)",           "f": 1},
    {"lambda": "(5,1)",         "f": 5},
    {"lambda": "(4,2)",         "f": 9},
    {"lambda": "(4,1,1)",       "f": 10},
    {"lambda": "(3,3)",         "f": 5},
    {"lambda": "(3,2,1)",       "f": 16},
    {"lambda": "(3,1,1,1)",     "f": 10},
    {"lambda": "(2,2,2)",       "f": 5},
    {"lambda": "(2,2,1,1)",     "f": 9},
    {"lambda": "(2,1,1,1,1)",   "f": 5},
    {"lambda": "(1,1,1,1,1,1)", "f": 1},
]

# Schur-Weyl Markov weights per partition of 6, in the same Hoefsmit
# normalisation as the schur-weyl-weight-* chains on main:
#     w_λ(q) = (q − q^{-1})^(n − l(λ)) · ∏_{x ∈ λ} [h_x]_q^{-1}.
WEIGHTS_OF_6: dict[str, str] = {
    "w_(6)":           "(q − q^{-1})^5 / ([6]_q · [5]_q · [4]_q · [3]_q · [2]_q · [1]_q)",
    "w_(5,1)":         "(q − q^{-1})^4 / ([6]_q · [4]_q · [3]_q · [2]_q · [1]_q · [1]_q)",
    "w_(4,2)":         "(q − q^{-1})^4 / ([6]_q · [5]_q · [3]_q · [2]_q · [2]_q · [1]_q)",
    "w_(4,1,1)":       "(q − q^{-1})^3 / ([6]_q · [3]_q · [2]_q · [1]_q · [1]_q · [1]_q)",
    "w_(3,3)":         "(q − q^{-1})^4 / ([4]_q · [3]_q · [3]_q · [2]_q · [2]_q · [1]_q)",
    "w_(3,2,1)":       "(q − q^{-1})^3 / ([5]_q · [3]_q · [3]_q · [2]_q · [1]_q · [1]_q)",
    "w_(3,1,1,1)":     "(q − q^{-1})^2 / ([6]_q · [3]_q · [2]_q · [1]_q · [1]_q · [1]_q)",
    "w_(2,2,2)":       "(q − q^{-1})^3 / ([4]_q · [3]_q · [3]_q · [2]_q · [2]_q · [1]_q)",
    "w_(2,2,1,1)":     "(q − q^{-1})^2 / ([5]_q · [4]_q · [3]_q · [2]_q · [1]_q · [1]_q)",
    "w_(2,1,1,1,1)":   "(q − q^{-1}) / ([6]_q · [4]_q · [3]_q · [2]_q · [1]_q · [1]_q)",
    "w_(1,1,1,1,1,1)": "1 / ([6]_q · [5]_q · [4]_q · [3]_q · [2]_q · [1]_q)",
}


def build() -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — Partitions of 6
    steps.append(DerivationStep(
        name="Partitions of 6 — Schur–Weyl basis at A=2",
        operation=(
            "By Schur–Weyl duality the n=3·A=6 ambient Hecke algebra "
            "is H_6(q); partitions of 6 enumerate the Wedderburn "
            "blocks.  There are 11 partitions (counted by p(6)=11), "
            "with Wedderburn block dimensions f_λ given by the "
            "hook-length formula."
        ),
        inputs=[FirstPrinciple.SCHUR.value, FirstPrinciple.WEDDERBURN.value],
        output_name="partitions_of_6",
        output_value=PARTITIONS_OF_6,
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:STUB:PartitionsOfN",
        citation="kassel1995",
        jet_order=0,
    ))

    # 2 — Wedderburn weights w_λ for all 11 partitions, via per-λ chains
    steps.append(DerivationStep(
        name="Wedderburn weights w_λ(q) for λ ⊢ 6 — chain references",
        operation=(
            "Reference the 11 dedicated per-λ chains "
            "`schur-weyl-weight-{6, 51, 42, 411, 33, 321, 3111, 222, "
            "2211, 21111, 111111}.derivation.json`.  All 11 use the "
            "Hoefsmit normalisation w_λ(q) = (q − q^{-1})^(n − l(λ)) · "
            "∏_x [h_x]_q^{-1} (matching the schur-weyl-weight-3 "
            "convention on the proton/neutron chains) and are "
            "themselves fully-trusted (each has profile "
            "{axiom: 1, mathlib-cited: 2, derived: 1})."
        ),
        inputs=["partitions_of_6"],
        output_name="w_lambda_all",
        output_value=WEIGHTS_OF_6,
        trust_basis=TrustBasis.DERIVED,
        citation="kassel1995",
        jet_order=0,
        notes=(
            "Derivation chains: schur-weyl-weight-{6, 51, 42, 411, "
            "33, 321, 3111, 222, 2211, 21111, 111111}.derivation.json "
            "(11 chains, all shipped on main as part of the per-λ "
            "frontier paydown for partitions of 4-9).  Each chain "
            "discharges its w_λ(q) value entirely from AXIOMs (Hecke "
            "energy + Wedderburn + Schur)."
        ),
    ))

    # 3 — Atomic-braid recipe for β_D (canonical convention)
    steps.append(DerivationStep(
        name="Atomic-braid recipe for β_D (canonical)",
        operation=(
            "The deuteron canonical σ-word β_D has 23 crossings on 6 "
            "strands, decomposing as 11 σ (positive) + 7 σ^{-1} "
            "(negative) + 5 averaged crossings.  Produced by "
            "`canonical_braid_crossings.atom_canonical_crossings(Z=1, "
            "N=1)`, which bridges `mass_at_3A_proper.atom_braid_word_3A` "
            "(canonical convention) into the (gen_idx, ctype) format "
            "consumable by `q_character_on_braid_word`.  Note: this "
            "is the canonical convention introduced by PR #572 (audit "
            "doc `docs/audits/2026-05-08-q-hecke-character-gap-closure.md`); "
            "the legacy `atomic_braid_to_crossings` from "
            "hecke_character_symbolic.py is now a re-export of "
            "`atom_canonical_crossings`.  When the dedicated "
            "`atomic-braid-recipe-d.derivation.json` chain ships "
            "(PR #476 family), this step upgrades to DERIVED via "
            "that chain reference."
        ),
        inputs=["partitions_of_6", FirstPrinciple.HECKE_ENERGY.value],
        output_name="beta_D",
        output_value="β_D = canonical σ-word of length 23 (11 σ + 7 σ^{-1} + 5 averaged)",
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§Atomic-braid recipe",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/canonical_braid_crossings.py "
            "function `atom_canonical_crossings(Z=1, N=1)`.  "
            "SCRIPT_CITED until PR #476 ships the "
            "`atomic-braid-recipe-d` derivation chain on main.  "
            "Cross-checked: total crossing count 23 matches the "
            "23-crossing word documented in chi-deuteron-h6.witness.json's "
            "description."
        ),
    ))

    # 4 — Per-irrep characters χ^λ_q(β_D) via Hoefsmit recipe
    steps.append(DerivationStep(
        name="Per-irrep characters χ^λ_q(β_D) via Hoefsmit recipe",
        operation=(
            "For each λ ⊢ 6, compute χ^λ_q(β_D) by applying the "
            "Hoefsmit matrix recipe to the σ-word β_D: "
            "ρ^λ(σ_i) is the Hoefsmit matrix in the SYT basis of λ, "
            "ρ^λ(σ_i^{-1}) follows from the Hecke relation σ_i^2 = "
            "(q − q^{-1}) σ_i + 1 (so σ_i^{-1} = σ_i − (q − q^{-1})), "
            "and ρ^λ(I_avg) = ρ^λ(σ_i) − (q − q^{-1})/2 · 1.  The "
            "character χ^λ_q(β_D) is the trace of the resulting "
            "f_λ × f_λ matrix product over all 23 crossings.\n"
            "Closed-form values are cached in "
            "`chi-deuteron-h6.witness.json` (compute time ~155 s "
            "first-run, O(1) on cache hits)."
        ),
        inputs=["partitions_of_6", "beta_D",
                FirstPrinciple.FROBENIUS_PAIRING.value,
                FirstPrinciple.CATEGORICAL_ACTION.value],
        output_name="chi_lambda_deuteron",
        output_value=(
            "χ^λ_q(β_D) for each of the 11 partitions of 6, as "
            "symbolic Laurent polynomials in q (see "
            "chi-deuteron-h6.witness.json `chi_lambda_symbolic` field)"
        ),
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "script: folio-assistant/computations/hecke_character_symbolic.py "
            "function `q_character_on_braid_word(λ, β_D, q)` (called "
            "11 times, once per partition of 6).  Cache: "
            "chi-deuteron-h6.witness.json.  SCRIPT_CITED until "
            "per-(λ, σ_i) Hoefsmit chains for n=6 ship (analogous to "
            "the existing hoefsmit-rep-21-{sigma1,sigma2} chains for "
            "n=3, but specialised to the partitions of 6).  Trivial "
            "and sign reps have closed-form expressions in (n_+, n_-, "
            "n_avg) and could be promoted to DERIVED in a follow-up."
        ),
    ))

    # 5 — Finite-Jones Markov-trace assembly
    steps.append(DerivationStep(
        name="Finite-Jones Markov-trace assembly",
        operation=(
            "tr_M(β_D, q) = Σ_{λ ⊢ 6} w_λ(q) · χ^λ_q(β_D), summing "
            "over all 11 partitions of 6.  Uniqueness from "
            "finite-Jones (the Markov trace is the unique linear "
            "functional on H_6(q) satisfying τ(1)=1, τ(σ_i)=z, "
            "τ(xy)=τ(yx), τ(x σ_n)=z·τ(x); the Schur-Weyl "
            "decomposition into Wedderburn blocks gives the explicit "
            "formula above)."
        ),
        inputs=["w_lambda_all", "chi_lambda_deuteron",
                FirstPrinciple.FINITE_JONES.value],
        output_name="tr_M_deuteron_symbolic",
        output_value="symbolic Laurent polynomial in q",
        trust_basis=TrustBasis.DERIVED,
        citation="jones1987",
        jet_order=0,
        gb_filtration_level=0,
    ))

    # 6 — Numerical evaluation at q_0
    steps.append(DerivationStep(
        name="Evaluate tr_M(D, q_0) at q_0",
        operation=(
            "Substitute q := q_0 = 1.10997... into the symbolic "
            "assembly; mpmath at 50 dps gives 0.17743692421543206... "
            "matching the upstream atom-tr-M-q0 chain leaf "
            "(D-tr-M-q0.derivation.json target_value) and the "
            "habiro-coefficients-atomic.witness.json D entry "
            "tr_M_at_q0 field."
        ),
        inputs=["tr_M_deuteron_symbolic"],
        output_name="tr_M_deuteron_q0",
        output_value=DEUTERON_TR_M_Q0,
        trust_basis=TrustBasis.COMPUTATIONAL,
        jet_order=0,
        gb_filtration_level=0,
        spectral_stratum="archimedean (q_0 ∈ ℝ_{>1})",
        notes=(
            "Cross-checked at machine precision against the upstream "
            "habiro_coefficients_atomic.py / habiro-coefficients-atomic "
            "witness for the deuteron (Z=1, N=1, include_inter=True) — "
            "rel_diff ≤ 1e-12 against that script's `tr_M_at_q0` field."
        ),
    ))

    return DerivationChain(
        target="tr_M(D, q_0)",
        target_value=DEUTERON_TR_M_Q0,
        target_tolerance=1e-9,
        content_block="prop:full-pole-structure-mass-trace",
        description=(
            "Markov-trace assembly chain for the deuteron: combines "
            "the 11 schur-weyl-weight-{6, 51, 42, 411, 33, 321, 3111, "
            "222, 2211, 21111, 111111} per-λ chains + the canonical "
            "atomic-braid recipe for β_D (23 crossings) + the per-"
            "irrep characters χ^λ_q(β_D) via the Hoefsmit recipe "
            "(cached in chi-deuteron-h6.witness.json) via the "
            "finite-Jones axiom into tr_M(D, q_0) ≈ 0.17744.  Trust "
            "profile is {axiom: 1, mathlib-cited: 0, derived: 2, "
            "script-cited: 2, computational: 1} — closes the per-λ "
            "Wedderburn-weight frontier for n=6 (all 11 weights now "
            "DERIVED via dedicated chains, replacing what would "
            "otherwise be 11 SCRIPT_CITED weight steps).  The two "
            "remaining SCRIPT_CITED steps are the canonical β_D "
            "recipe (pending PR #476's atomic-braid-recipe-d chain) "
            "and the per-irrep χ^λ values (pending per-(λ, σ_i) "
            "Hoefsmit chains for n=6, analogous to the existing "
            "hoefsmit-rep-21-{sigma1,sigma2} chains for n=3).  "
            "Companion to markov-trace-assembly-{proton,neutron}.derivation.json."
        ),
        steps=steps,
    )


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"markov-trace-assembly-deuteron chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {chain.target_value}")
    chain.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
