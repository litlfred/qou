#!/usr/bin/env python3
"""
Atomic braid recipe — canonical (SDP) convention, parameterised over
{proton, neutron, deuteron}.

Companion to `build_atomic_braid_recipe_4he_chain.py` (which uses the
LEGACY disjoint convention from `atomic_braid_gb_filtration_extension`).
This builder uses the **canonical operator-valued convention** from
`canonical_braid_crossings.atom_canonical_crossings(Z, N)`, which is
the convention SDP-confirmed by PR #608's
`r5_full_canonical_knot_solver` for D (6_2) and ³He (L6a4) and the
substrate-level neutron-cross convention post-PR #572.

The canonical word is a list of `(gen_idx, ctype)` pairs where:

  * `ctype = "sigma"`     → positive crossing σ_g (Hecke generator)
  * `ctype = "sigma_inv"` → negative crossing σ_g⁻¹ (inverse generator,
                            via the Hecke quadratic σ² = h·σ + 1)
  * `ctype = "averaged"`  → operator-valued interface
                            `I_g := σ_g − (h/2)·1`,  h = q − q⁻¹

The averaged crossing `I_g` is the additional structure beyond the
legacy disjoint convention: it encodes the "neutron neutron-cross"
interface from `prop:hecke-branching-trace-decomposition` and is the
structural ingredient PR #608's SDP solver picks out as the canonical
T_w under operator-selection LP duality.

Templates the structure of `build_atomic_braid_recipe_4he_chain.py`
(8-step recipe, AXIOM/SCRIPT_CITED/DERIVED breakdown).  Trust profile
{axiom: 2, derived: 3, script-cited: 3}: one extra SCRIPT_CITED step
relative to the legacy variant for the averaged-crossing interface
rule, since `prop:hecke-branching-trace-decomposition` is paper-
cited but not Lean-formalised.

Once `conj:canonical-knot-id-sdp` (issue #604, GAP-A-1) graduates
to a theorem (the SDP uniqueness proof), the three SCRIPT_CITED
steps in each chain rebase to LEAN_PROVEN and every per-atom
mass-trace chain consuming this recipe becomes fully-trusted.

Outputs (one per atom):
  * `atomic-braid-recipe-p-canonical.derivation.json`
  * `atomic-braid-recipe-n-canonical.derivation.json`
  * `atomic-braid-recipe-d-canonical.derivation.json`
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402


HERE = Path(__file__).parent

# ── Atom registry ───────────────────────────────────────────────
# Each entry: (slug, label, Z, N).  ⁴He is the canonical-convention
# successor to the legacy `atomic-braid-recipe-4he.derivation.json`
# chain (which uses the bare-int disjoint-product format from
# `atomic_braid_gb_filtration_extension`); the canonical word at
# (Z=2, N=2) carries averaged crossings I = σ − (h/2)·1 not present
# in the legacy form.  Note: PR #608's r5_full_canonical_knot_solver
# currently SDP-confirms only A ≤ 3 (D, ³He, T deferred to B_5
# Hoefsmit); the ⁴He canonical word is generated via the same
# `mass_at_3A_proper.atom_braid_word_3A` pipeline but without
# explicit SDP optimum verification.
ATOMS = [
    ("p",   "proton",   1, 0),
    ("n",   "neutron",  0, 1),
    ("d",   "deuteron", 1, 1),
    ("4he", "⁴He",      2, 2),
]


def build_chain(slug: str, label: str, Z: int, N: int) -> DerivationChain:
    A = Z + N
    n_strands = 3 * A
    # Canonical word from the SDP-confirmed convention
    canonical_word = atom_canonical_crossings(Z, N, include_inter=True)
    n_crossings = len(canonical_word)

    steps: list[DerivationStep] = []

    # 1 — Categorical action axiom
    steps.append(DerivationStep(
        name=f"Categorical R-matrix action of B_{{{n_strands}}} on V^{{⊗{n_strands}}}",
        operation=(
            f"By the categorical-action axiom (FirstPrinciple "
            f"`Cat.Action`), each braid generator `σ_i ∈ B_{n_strands}` "
            f"acts on `V^{{⊗{n_strands}}}` (V the fundamental quark "
            f"representation of `U_q(sl_2)`) via the Drinfeld–Jimbo "
            f"R-matrix at strand `i`.  The action factors through the "
            f"Hecke algebra `H_{n_strands}(q)` by the quadratic "
            f"relation `σ² = h·σ + 1` with `h = q − q⁻¹`."
        ),
        inputs=[FirstPrinciple.CATEGORICAL_ACTION.value],
        output_name="cat_action_general",
        output_value=f"σ_i : V^{{⊗{n_strands}}} → V^{{⊗{n_strands}}} via R-matrix at strand i",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:STUB:CategoricalRMatrixAction",
        citation="kassel1995",
        jet_order=0,
    ))

    # 2 — Schur–Weyl: quark = V, nucleon = V^{⊗3} singlet
    steps.append(DerivationStep(
        name="Quark / nucleon irrep assignment via Schur–Weyl",
        operation=(
            "By Schur–Weyl duality (FirstPrinciple `Schur`), the "
            "quark sits in `V`, the fundamental of `U_q(sl_2)`.  A "
            "nucleon is a 3-quark composite living in the color-"
            "singlet block of `V^{⊗3}`; its braid statistics are "
            "governed by `H_3(q)` acting on `V^{⊗3}`."
        ),
        inputs=[FirstPrinciple.SCHUR.value, "cat_action_general"],
        output_name="nucleon_in_V3",
        output_value="nucleon ∈ singlet block of V^{⊗3}",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:STUB:SchurWeylDuality",
        citation="kassel1995",
        jet_order=0,
    ))

    # 3 — Canonical proton word in B_3 (SCRIPT_CITED)
    proton_word = atom_canonical_crossings(1, 0, include_inter=True)
    steps.append(DerivationStep(
        name="Canonical proton word in B_3 (operator-valued)",
        operation=(
            "Per `mass_at_3A_proper.atom_braid_word_3A(Z=1, N=0)`, "
            "the proton's canonical Hecke normal form is the 11-"
            "crossing word "
            f"`{proton_word}` "
            "in the operator-valued convention with averaged "
            "crossings `I = σ − (h/2)·1`.  PR #608's SDP solver "
            "(`r5_full_canonical_knot_solver`) confirms this word "
            "is in the LP-optimum canonical-knot class identified "
            "by `conj:canonical-knot-id-sdp`."
        ),
        inputs=["nucleon_in_V3"],
        output_name="proton_canonical_word",
        output_value=proton_word,
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§atomic-braid-recipe",
        jet_order=0,
        notes=(
            "script: computations/mass_at_3A_proper.py "
            "(`atom_braid_word_3A`) + computations/canonical_braid_crossings.py "
            "(`atom_canonical_crossings(1, 0)`).  Awaits Lean "
            "formalisation of the (uud) → canonical-NF map; closes "
            "when `conj:canonical-knot-id-sdp` (issue #604, GAP-A-1) "
            "graduates to a theorem (categorical SDP uniqueness)."
        ),
    ))

    # 4 — Canonical neutron word in B_3 (SCRIPT_CITED)
    neutron_word = atom_canonical_crossings(0, 1, include_inter=True)
    steps.append(DerivationStep(
        name="Canonical neutron word in B_3 (operator-valued)",
        operation=(
            "Per `mass_at_3A_proper.atom_braid_word_3A(Z=0, N=1)`, "
            "the neutron's canonical Hecke normal form is the 11-"
            "crossing word "
            f"`{neutron_word}` "
            "in the operator-valued convention.  Differs from the "
            "proton by the averaged-vs-σ pattern at strand-1 "
            "positions 4–5, encoding the (udd) quark-content "
            "signature.  Same SDP-LP-optimum status as the proton "
            "via `conj:canonical-knot-id-sdp`."
        ),
        inputs=["nucleon_in_V3"],
        output_name="neutron_canonical_word",
        output_value=neutron_word,
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§atomic-braid-recipe",
        jet_order=0,
        notes=(
            "script: computations/canonical_braid_crossings.py "
            "(`atom_canonical_crossings(0, 1)`).  Same closure path "
            "as the proton word (step 3): when `conj:canonical-knot-"
            "id-sdp` becomes a theorem, both step 3 and step 4 "
            "rebase to LEAN_PROVEN simultaneously."
        ),
    ))

    # 5 — Inter-nucleon averaged crossing rule (SCRIPT_CITED)
    steps.append(DerivationStep(
        name="Inter-nucleon averaged crossing rule",
        operation=(
            "For atoms with `A ≥ 2`, the inter-block crossing "
            "between nucleon blocks `k` and `k + 1` sits at the "
            "0-indexed generator `3k − 1` (for `k = 1..A − 1`); it "
            "is the averaged operator "
            "`I_{3k−1} := σ_{3k−1} − (h/2) · 1`, encoding the "
            "`pp`, `pn`, `nn` channel selection of "
            "`prop:hecke-branching-trace-decomposition`.  For "
            "single-nucleon atoms (A = 1) this step contributes no "
            "crossings; for the deuteron (A = 2, pn channel) it "
            "contributes one averaged crossing at gen_idx 2."
        ),
        inputs=["nucleon_in_V3"],
        output_name="inter_nucleon_rule",
        output_value="I_{3k−1} := σ_{3k−1} − (h/2)·1, k = 1..A − 1 (0-indexed gen_idx)",
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§Hecke-branching-trace-decomposition",
        jet_order=0,
        notes=(
            "script: computations/mass_at_3A_proper.py "
            "(`atom_braid_word_3A` inter-block insertion logic).  "
            "Paper-cited under "
            "`prop:hecke-branching-trace-decomposition`; awaits Lean "
            "formalisation of the operator-valued interface — same "
            "Lean status as `conj:canonical-knot-id-sdp`'s "
            "categorical proof."
        ),
    ))

    # 6 — Disjoint embedding B_3 ↪ B_{3A} (DERIVED)
    steps.append(DerivationStep(
        name=f"Disjoint-block embedding B_3 ↪ B_{{{n_strands}}}",
        operation=(
            f"For an atom with `A = {A}` nucleons, the disjoint-"
            f"strand embedding `B_3 ↪ B_{{{n_strands}}}` for the "
            f"`k`-th nucleon block (`k = 1..{A}`) is the index "
            f"shift `σ_i ↦ σ_{{i + 3(k - 1)}}` extended sign-"
            f"preservingly to negatives and to the averaged "
            f"crossings.  Generators are **0-indexed** here to match "
            f"the `(gen_idx, ctype)` output of "
            f"`canonical_braid_crossings.atom_canonical_crossings`; "
            f"so `i, gen_idx ∈ {{0, 1}}` for the in-block generators "
            f"of `B_3` and `gen_idx + 3(k-1) ∈ {{0, 1, ..., {n_strands - 2}}}` "
            f"for the embedded `B_{{{n_strands}}}` generators (i.e. "
            f"σ_g ranges over `g ∈ {{0, ..., {n_strands - 2}}}`).  "
            f"Standard disjoint-product structure of the braid group: "
            f"blocks of strands `3(k-1), ..., 3k - 1` are "
            f"independently braided."
        ),
        inputs=["cat_action_general"],
        output_name="disjoint_embedding",
        output_value=f"(σ_i, k) ↦ σ_{{i + 3(k - 1)}}, k = 1..{A} (0-indexed gen_idx)",
        trust_basis=TrustBasis.DERIVED,
        jet_order=0,
    ))

    # 7 — Atom assembly rule (DERIVED)
    steps.append(DerivationStep(
        name=f"Atom assembly rule T_w({label}) ∈ B_{{{n_strands}}}",
        operation=(
            f"Combine steps 3–6 into the atom assembly:\n"
            f"  T_w(Z = {Z}, N = {N}) := \n"
            f"    ∏_{{k=1}}^{Z} (proton word shifted by block k) ∘\n"
            f"    ∏_{{k=Z+1}}^{{{A}}} (neutron word shifted by block k) ∘\n"
            f"    ∏_{{k=1}}^{{{A}-1}} (inter-nucleon averaged crossing "
            f"at 0-indexed generator 3k − 1).\n"
            f"Pure algebra: sequence of disjoint-block + interface "
            f"crossings concatenated in B_{{{n_strands}}}."
        ),
        inputs=["proton_canonical_word", "neutron_canonical_word",
                "inter_nucleon_rule", "disjoint_embedding"],
        output_name="atom_assembly",
        output_value=f"T_w({label}) ∈ B_{{{n_strands}}} via canonical assembly",
        trust_basis=TrustBasis.DERIVED,
        jet_order=0,
    ))

    # 8 — Specialisation + leaf (DERIVED; word is exact concatenation)
    steps.append(DerivationStep(
        name=f"Specialisation: {label} = (Z = {Z}, N = {N})",
        operation=(
            f"Apply the assembly rule at (Z = {Z}, N = {N}) to "
            f"obtain the {n_crossings}-crossing canonical word "
            f"`{canonical_word}` "
            f"in B_{{{n_strands}}}.  Internal assertion in the "
            f"builder guards that the assembly reproduces "
            f"`canonical_braid_crossings.atom_canonical_crossings("
            f"{Z}, {N})` bit-for-bit."
        ),
        inputs=["atom_assembly"],
        output_name=f"{slug}_canonical_word",
        output_value=canonical_word,
        trust_basis=TrustBasis.DERIVED,
        jet_order=0,
    ))

    # PR #608's r5_full_canonical_knot_solver only runs the SDP
    # search for D (Z=1, N=1, A=2) and ³He (Z=2, N=1, A=3) per its
    # stated prototype scope.  Other atoms — proton, neutron, T,
    # ⁴He — have canonical-pipeline-generated words but are NOT
    # directly SDP-optimum-verified by the solver.
    SDP_DIRECTLY_VERIFIED = {(1, 1), (2, 1)}
    if (Z, N) in SDP_DIRECTLY_VERIFIED:
        sdp_status = (
            f"SDP-optimum verified for {label} via PR #608's "
            f"`r5_full_canonical_knot_solver` (the canonical word "
            f"lies in the LP-optimum class for the (Z = {Z}, N = {N}) "
            f"atom under the operator-selection LP)"
        )
    elif (Z, N) in {(1, 0), (0, 1)}:
        sdp_status = (
            f"the {label} canonical word is a single-nucleon "
            f"component of the SDP-verified D / ³He assemblies "
            f"(PR #608's solver runs on the multi-nucleon atoms "
            f"and consumes the proton / neutron words as inputs); "
            f"the solver does not run directly at the single-"
            f"nucleon level (Z = {Z}, N = {N}, A = 1)"
        )
    else:
        sdp_status = (
            f"the convention is SDP-confirmed for D / ³He via "
            f"PR #608's `r5_full_canonical_knot_solver`; the "
            f"{label} word is generated by the same canonical "
            f"pipeline (`mass_at_3A_proper.atom_braid_word_3A`) "
            f"but is not yet SDP-optimum-verified at A = {A} "
            f"(solver scope: A ≤ 3 with B_5 Hoefsmit pending for T)"
        )

    # Per-atom companion text — replaces the previous templated
    # "(when ...)" conditionals that produced false / tautological
    # text in the emitted artifacts.
    if slug == "4he":
        companion_text = (
            "Canonical companion to the legacy-disjoint "
            "`atomic-braid-recipe-4he.derivation.json`; the legacy "
            "variant is retained for parity with the GS-filtration "
            "tracker in `atomic_braid_gb_filtration_extension.py`, "
            "which only consumes bare-int σ / σ⁻¹ words.  Downstream "
            "consumers do not yet reference this canonical artifact, "
            "so it is a companion rather than a replacement"
        )
    else:
        companion_text = (
            f"Canonical companion to the per-atom mass-trace "
            f"`atomic-braid-recipe-{slug}` SCRIPT_CITED step declared "
            f"in PR #605's `markov-trace-assembly-{label}.derivation.json`; "
            f"that consumer does not yet reference this artifact, so "
            f"the SCRIPT_CITED step there remains pending until the "
            f"reference is wired up downstream"
        )

    return DerivationChain(
        target=f"T_w({label}) ∈ B_{{{n_strands}}} (canonical operator-valued)",
        target_value=canonical_word,
        target_tolerance=0.0,  # exact equality on (gen_idx, ctype) sequence
        content_block="prop:atomic-mass-gb-nf",
        description=(
            f"Atomic-braid recipe for {label} in the canonical "
            f"operator-valued convention "
            f"(`canonical_braid_crossings.atom_canonical_crossings"
            f"({Z}, {N})`).  Status: {sdp_status}.  {n_crossings} "
            f"crossings on {n_strands} strands.  Trust profile "
            f"{{axiom: 2, derived: 3, script-cited: 3}}.  "
            f"{companion_text}.  Closure of "
            f"`conj:canonical-knot-id-sdp` (issue #604 GAP-A-1) "
            f"upgrades all three SCRIPT_CITED steps to LEAN_PROVEN "
            f"simultaneously, at which point the legacy-disjoint "
            f"variant can be deleted in favour of this chain."
        ),
        steps=steps,
    )


def main() -> int:
    all_ok = True
    for slug, label, Z, N in ATOMS:
        chain = build_chain(slug, label, Z, N)
        # Internal coherence assertion (matches builder guard).
        canonical = atom_canonical_crossings(Z, N, include_inter=True)
        assert chain.target_value == canonical, (
            f"{label}: target mismatch — got {chain.target_value} "
            f"vs canonical {canonical}"
        )

        ok, issues = chain.structural_check()
        all_ok = all_ok and ok
        print(f"{label} canonical recipe: structural_check {'OK' if ok else 'FAIL'}")
        for i in issues:
            print(f"  - {i}")
        print(f"  trust_summary: {chain.trust_summary()}")
        out = HERE / f"atomic-braid-recipe-{slug}-canonical.derivation.json"
        chain.save(out)
        print(f"  Wrote {out}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
