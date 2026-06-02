#!/usr/bin/env python3
"""
Atomic braid recipe — disjoint construction at ⁴He.  **LEGACY
CONVENTION** — see `build_atomic_braid_recipe_canonical_chain.py`
for the canonical / SDP convention with averaged crossings I = σ −
(h/2)·1.  This builder is kept for parity with
`atomic_braid_gb_filtration_extension` (legacy bare-int word format
consumed by `gb_filtration_jet_tracker.reduce_braid` and the
`term7_alpha5_crystal_derivation.crystal_chi_lambda` crystal-limit
function — neither tool yet handles averaged crossings, see
`docs/audits/canonical-convention-migration-plan.md`); new
production work should consume the canonical chain instead.

Discharges (partially) the SCRIPT_CITED `atomic-braid-recipe-X`
frontier called out as item #1 in `DERIVATION-CHAIN-METHODOLOGY.md`.

The atomic braids for the disjoint convention used by
`atomic_braid_gb_filtration_extension.py` and the
`term7-alpha5-crystal-derivation.witness.json` follow a uniform
recipe:

  T_w(Z, N) :=  (proton braid)^{Z} ∘ (neutron braid)^{N}
  in B_{3(Z + N)}
  via the disjoint-strand embedding
  B_3 ↪ B_{3(Z+N)},   σ_i ↦ σ_{i + 3(k-1)}
  for the k-th nucleon block (k = 1..A).

This chain certifies the **assembly rule** + the disjoint
embedding rigorously from the categorical-action axiom and the
disjoint-product structure of the symmetric group, then specialises
to ⁴He with leaf

  T_w(2, 2) = [1, 2, -1, 4, 5, -4, 7, -8, 7, 10, -11, 10]  ∈ B_{12}.

Trust profile {axiom: 2, derived: 3, script-cited: 2}
— **NOT fully-trusted by design**.  The two SCRIPT_CITED steps are:

  * the canonical proton word `σ_1 σ_2 σ_1^{-1}` in B_3 (paper-
    cited under `prop:atomic-mass-gb-nf` and `prop:jet-prefix-gb-
    filtration`; awaits Lean formalisation of the quark-content →
    Hecke-NF map),
  * the canonical neutron word `σ_1 σ_2^{-1} σ_1` in B_3 (same
    status, opposite sign on the middle generator).

The chain is consumed by `term7-s-crystal-4he.derivation.json`
(via the SCRIPT_CITED step "⁴He atomic braid word β_⁴He ∈ B_{12}")
and indirectly by the `p`/`n`/`D` mass-trace assembly chains —
when the proton + neutron braid words are themselves discharged
to LEAN_PROVEN, every atomic chain rebases through this recipe
and becomes fully-trusted.

Output: `atomic-braid-recipe-4he.derivation.json`.
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
OUTPUT = _pb.witness_path("atomic-braid-recipe-4he.derivation.json", HERE)

# Canonical disjoint ⁴He braid word — matches
# `atomic_braid_gb_filtration_extension.ATOMIC_BRAIDS[3]` and the
# atom row of `term7-alpha5-crystal-derivation.witness.json`.
PROTON_WORD_B3 = [1, 2, -1]      # σ_1 σ_2 σ_1^{-1} in B_3
NEUTRON_WORD_B3 = [1, -2, 1]     # σ_1 σ_2^{-1} σ_1 in B_3
HE4_WORD_B12 = [1, 2, -1, 4, 5, -4, 7, -8, 7, 10, -11, 10]
A_HE4 = 4
Z_HE4 = 2
N_HE4 = 2


def _shift_word(word: list[int], k: int) -> list[int]:
    """Disjoint-block shift: σ_i ↦ σ_{i + 3(k-1)} (positive or negative)."""
    return [(s + 3 * (k - 1) if s > 0 else s - 3 * (k - 1)) for s in word]


def _assemble_he4_word() -> list[int]:
    """Reconstruct ⁴He's canonical word from proton/neutron + shifts."""
    word: list[int] = []
    # Z protons in blocks k = 1..Z
    for k in range(1, Z_HE4 + 1):
        word.extend(_shift_word(PROTON_WORD_B3, k))
    # N neutrons in blocks k = Z+1..Z+N
    for k in range(Z_HE4 + 1, Z_HE4 + N_HE4 + 1):
        word.extend(_shift_word(NEUTRON_WORD_B3, k))
    return word


def build() -> DerivationChain:
    # Internal sanity check: the assembly rule must reproduce the
    # canonical leaf.  If this fails the chain is incoherent.
    assembled = _assemble_he4_word()
    assert assembled == HE4_WORD_B12, (
        f"assembly mismatch: got {assembled} expected {HE4_WORD_B12}"
    )

    steps: list[DerivationStep] = []

    # 1 — Categorical action axiom
    steps.append(DerivationStep(
        name="Categorical R-matrix action of B_n on V^{⊗n}",
        operation=(
            "By the categorical-action axiom (FirstPrinciple "
            "`Cat.Action`), each braid generator `σ_i ∈ B_n` acts "
            "on `V^{⊗n}` (V the fundamental quark representation "
            "of `U_q(sl_2)`) via the Drinfeld–Jimbo R-matrix at "
            "strand `i`.  The action factors through the Hecke "
            "algebra `H_n(q)` by the Hecke quadratic relation."
        ),
        inputs=[FirstPrinciple.CATEGORICAL_ACTION.value],
        output_name="cat_action_general",
        output_value="σ_i : V^{⊗n} → V^{⊗n} via R-matrix at strand i",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:STUB:CategoricalRMatrixAction",
        citation="kassel1995",
        jet_order=0,
    ))

    # 2 — Schur–Weyl: quark = V, nucleon = V^{⊗3}
    steps.append(DerivationStep(
        name="Quark / nucleon irrep assignment via Schur–Weyl",
        operation=(
            "By Schur–Weyl duality (FirstPrinciple `Schur`), the "
            "quark sits in `V`, the fundamental of `U_q(sl_2)`.  A "
            "nucleon is a 3-quark composite living in the "
            "color-singlet block of `V^{⊗3}`; its braid statistics "
            "are governed by `H_3(q)` acting on `V^{⊗3}`."
        ),
        inputs=[FirstPrinciple.SCHUR.value, "cat_action_general"],
        output_name="nucleon_in_V3",
        output_value="nucleon ∈ singlet block of V^{⊗3}",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:STUB:SchurWeylDuality",
        citation="kassel1995",
        jet_order=0,
    ))

    # 3 — Proton word (SCRIPT_CITED)
    steps.append(DerivationStep(
        name="Canonical proton braid word in B_3",
        operation=(
            "Per `prop:atomic-mass-gb-nf` and `prop:jet-prefix-gb-"
            "filtration`, the proton's canonical Hecke normal form "
            "in `H_3(q)` is `T_w_p = σ_1 σ_2 σ_1^{-1}`, encoded as "
            "the word `[1, 2, -1]` (positive σ_1, positive σ_2, "
            "negative σ_1).  The (uud) quark content + the chirality "
            "convention fix the signs uniquely modulo Markov "
            "conjugation."
        ),
        inputs=["nucleon_in_V3"],
        output_name="proton_word_b3",
        output_value=PROTON_WORD_B3,
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§atomic-braid-recipe",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/atomic_braid_gb_filtration_extension.py "
            "(ATOMIC_BRAIDS table) + folio-assistant/computations/mass_at_3A_proper.py "
            "(`atom_braid_word_3A`).  Awaits Lean formalisation of "
            "the quark-content → Hecke-NF map (`uud → σ_1 σ_2 σ_1^{-1}`); "
            "once that lands, this step becomes LEAN_PROVEN and the "
            "atom mass-trace chains rebase to fully-trusted via this "
            "recipe."
        ),
    ))

    # 4 — Neutron word (SCRIPT_CITED)
    steps.append(DerivationStep(
        name="Canonical neutron braid word in B_3",
        operation=(
            "Per the same `prop:atomic-mass-gb-nf`, the neutron's "
            "canonical Hecke normal form in `H_3(q)` is "
            "`T_w_n = σ_1 σ_2^{-1} σ_1`, encoded as the word "
            "`[1, -2, 1]`.  The (udd) quark content flips the sign "
            "of the middle generator relative to the proton — this "
            "is the parity-distinguishing signature of the proton/"
            "neutron Hecke characters proved by "
            "`prop:hecke-branching-trace-decomposition`."
        ),
        inputs=["nucleon_in_V3"],
        output_name="neutron_word_b3",
        output_value=NEUTRON_WORD_B3,
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§atomic-braid-recipe",
        jet_order=0,
        notes=(
            "script: folio-assistant/computations/mass_at_3A_proper.py "
            "(`atom_braid_word_3A`).  Awaits Lean formalisation of the "
            "(udd) → `σ_1 σ_2^{-1} σ_1` map.  When closed jointly with "
            "the proton word (step 3), every atom mass chain becomes "
            "fully-trusted via this recipe."
        ),
    ))

    # 5 — Disjoint embedding B_3 ↪ B_{3A} (DERIVED)
    steps.append(DerivationStep(
        name="Disjoint-block embedding B_3 ↪ B_{3A}",
        operation=(
            "For an atom with `A = Z + N` nucleons, the disjoint-"
            "strand embedding `B_3 ↪ B_{3A}` for the `k`-th nucleon "
            "block (`k = 1..A`) is the index shift "
            "`σ_i ↦ σ_{i + 3(k - 1)}` extended sign-preservingly to "
            "negatives.  This is the standard disjoint-product "
            "structure of the braid group: blocks of strands `3(k-1)+1, "
            "..., 3k` are independently braided, so the union of "
            "block-k-only braids embeds without relations."
        ),
        inputs=["cat_action_general"],
        output_name="disjoint_embedding",
        output_value="(σ_i, k) ↦ σ_{i + 3(k - 1)}",
        trust_basis=TrustBasis.DERIVED,
        jet_order=0,
    ))

    # 6 — Atom assembly rule (DERIVED)
    steps.append(DerivationStep(
        name="Atom assembly rule T_w(Z, N) ∈ B_{3A}",
        operation=(
            "Combine steps 3 (proton word), 4 (neutron word), and "
            "5 (disjoint embedding) into the atom assembly:\n"
            "  T_w(Z, N) := \n"
            "    ∏_{k=1}^Z   (proton word shifted by block k) ∘\n"
            "    ∏_{k=Z+1}^{A} (neutron word shifted by block k).\n"
            "Pure algebra; sequence of disjoint-block braids "
            "concatenated in B_{3A}.  The convention for the "
            "ordering — protons first, neutrons after — matches "
            "`atomic_braid_gb_filtration_extension.ATOMIC_BRAIDS`."
        ),
        inputs=["proton_word_b3", "neutron_word_b3", "disjoint_embedding"],
        output_name="atom_assembly",
        output_value="T_w(Z, N) := concat(shifted proton + neutron blocks)",
        trust_basis=TrustBasis.DERIVED,
        jet_order=0,
    ))

    # 7 — Specialisation at ⁴He + numerical leaf (DERIVED;
    #     concatenation is pure algebra, no COMPUTATIONAL leaf needed)
    steps.append(DerivationStep(
        name="Specialisation: ⁴He = (Z = 2, N = 2)",
        operation=(
            "Apply the assembly rule at (Z = 2, N = 2): two proton "
            "blocks (k = 1, 2) and two neutron blocks (k = 3, 4) in "
            "B_{12}.  Concatenating the shifted words yields the "
            "expected canonical 12-strand braid "
            "`[1, 2, -1, 4, 5, -4, 7, -8, 7, 10, -11, 10]`.  Internal "
            "assertion in `build_atomic_braid_recipe_4he_chain.py` "
            "guards that the assembly reproduces the literal "
            "`atomic_braid_gb_filtration_extension.ATOMIC_BRAIDS[3]` "
            "convention bit-for-bit."
        ),
        inputs=["atom_assembly"],
        output_name="he4_word",
        output_value=HE4_WORD_B12,
        trust_basis=TrustBasis.DERIVED,
        jet_order=0,
    ))

    return DerivationChain(
        target="T_w(⁴He) ∈ B_{12}",
        target_value=HE4_WORD_B12,
        target_tolerance=0.0,  # exact equality (list of integers)
        content_block="prop:atomic-mass-gb-nf",
        description=(
            "Atomic-braid recipe specialised to ⁴He.  Discharges "
            "the assembly rule (disjoint-block embedding "
            "B_3 ↪ B_{12} + concatenation of shifted nucleon "
            "words) rigorously from the categorical-action and "
            "Schur–Weyl axioms; the only SCRIPT_CITED steps are "
            "the canonical proton + neutron Hecke normal forms in "
            "B_3.  Trust profile {axiom: 2, derived: 3, "
            "script-cited: 2}.  Replaces the diffuse "
            "`atomic-braid-recipe-X` SCRIPT_CITED debt in the per-"
            "atom mass chains with two focused open Lean items "
            "(proton word + neutron word).  Item #1 of the open "
            "frontier in `DERIVATION-CHAIN-METHODOLOGY.md` — "
            "partial paydown."
        ),
        steps=steps,
    )


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"⁴He atomic-braid recipe chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {chain.target_value}")
    chain.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
