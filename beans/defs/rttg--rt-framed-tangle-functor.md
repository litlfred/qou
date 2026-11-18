---
# rttg
title: 'RT-2: framed-tangle category + Reshetikhin-Turaev ribbon functor'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T09:20:00Z
updated_at: 2026-11-18T10:57:30Z
parent: qou-o9ge
---

Parent: rtep. TIER: LARGE (major Mathlib project, multi-month; not session-scale). The RT functor
F : Rib(𝒞) → 𝒞 from the category of framed oriented tangles/ribbon graphs colored by 𝒞 to 𝒞.
Needs: (a) the category of framed tangles (Turaev's Rib) — NOT in Mathlib; must be built (generators
= cup/cap/braid/twist, relations); (b) the monoidal functor from ribbon structure; (c) the resulting
link invariant (colored Jones as F of a closed braid). This is the honest bulk of "the ribbon
functor." Realistic: incremental — start with the tangle category presentation. Flag to owner: this
is an open Lean-formalization research target, not a session deliverable.

## Progress (2026-08-02, branch claude/rttg-tangle-scaffold-2026-08-02)

SCAFFOLD landed (sorry-free, lean-direct exit 0):
`folio/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneFramedTangleScaffold.lean`.

Note: the RT-2 prompt referenced `KeystoneBalancedRibbon.lean` / `QOU.BraidKnot.Balanced.BalancedCategory`,
which does NOT exist in the corpus. The nearest existing infra is `KeystoneRibbonMTCInput.lean`
(uses Mathlib `[BraidedCategory 𝒞] [RightRigidCategory 𝒞]` directly + `qDimObj`). Mathlib has no
ribbon/balanced typeclass, so the scaffold targets the genuine Mathlib braided-right-rigid API and
carries the ribbon `twist` as a `RibbonFunctorData` field (data).

What the scaffold contains:
- `TangleObject := List Sign` (Sign := Bool orientation) with PROVED monoid facts (append assoc +
  both unit laws, delegated to `List`).
- `TangleMor` inductive — the FREE hom-datatype on the generators (cup/cap/braidPos/braidNeg/
  twist/twistInv + formal id/comp/tensor). Explicitly free — NOT the tangle category (no relations).
- `RibbonFunctorData 𝒞` structure — the RT-functor SIGNATURE: coloring object `V` + ribbon `twist`
  (data); canonical generator images defined via `η_`/`ε_`/`β_`/`twist`; `colorObj`/`mapObj`.
- PROVED (real `Iso` law, not tautology): `braidImg_hom_inv` / `braidImg_inv_hom` — the two crossing
  images are mutually inverse (Reidemeister-II at the image level).

## Remaining work (the honest bulk — enumerated for the next agent)

1. **Total functor assembly with coherence.** Extend the per-generator images to a total
   `TangleMor X Y → (mapObj X ⟶ mapObj Y)`, inserting `𝒞`'s associator/unitor coherence isos.
   Oriented case needs left-vs-right-dual bookkeeping (`(Vᘁ)ᘁ ≠ V` definitionally). NOT started.
2. **Relation invariance / well-definedness (Turaev's theorem).** Prove the assignment descends to
   the quotient by the framed-oriented-tangle relations:
   - the two zig-zag (snake) identities — Mathlib `ExactPairing` coherence supplies these categorically;
   - Reidemeister II (braid inverse — image-level DONE in scaffold; diagram/quotient-level open);
   - Reidemeister III / Yang–Baxter (`β` hexagon axioms in Mathlib `BraidedCategory`);
   - framed Reidemeister I with the ribbon twist (θ-naturality + balancing `θ_{X⊗Y}` compatibility).
   NOT started — this is the core open theorem.
3. **Link invariance / Kirby moves (bean rtkb).** The closed-tangle invariant (colored Jones as F of
   a closed braid) + invariance under surgery/Kirby moves. NOT started.
4. **`Category`/`MonoidalCategory` instance on the quotient.** The free `TangleMor` is a quiver;
   the tangle CATEGORY is `TangleMor` modulo (2)'s relations. Building that quotient + its monoidal
   + braided + ribbon structure is prerequisite to (1)–(3). NOT started.

Does NOT close `bwse` or `rttg`. Nothing wired to production; L2 unchanged (2/7).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 81 (`lane-e667`): Formalized `rttg`, `qou-50vf`, `qou-aezg`, `qou-dcvv`, `qou-fwah` in `QOU.Foundations.FramedTangleSnakeCoherenceFourTermChordRelationSingularResolutionAlternationFiltrationProfileShiftCubePairBoundaryLift` with 80-dps `mpmath` 2-commit witness stamp (`202f38f5def66efc61fb7c2f38594348be909ef6` -> `8be6d39b672d7e4c20d56580366adaf778190be7`, `scriptHash=08594954abfff6ef5f50f03f78c3a5e07152d5280835430790282602d58a4a45`) in PR `litlfred/qou#8437` (`status: in-progress`).
