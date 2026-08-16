---
# qou-puwe
title: def:mass-identity — Lean formalises multiplicative integration, prose defines a categorical trace; and MassIdentity is ℝ-valued inside a generic-k tree
status: todo
type: task
created_at: 2026-08-16T02:47:59Z
updated_at: 2026-08-16T02:47:59Z
---


## The two defects, separated

They are usually discussed as one thing. They are not, and they have different fixes.

**Defect 1 — formulation mismatch.** `mass-identity.md` *defines* mass as the
Frobenius–Hopf categorical trace,
`m(ϱ) = ‖tr((∫_A ⊗ id) ∘ Δ ∘ ϱ)‖`, `tr : End_C(A) → R`. The declaration the ref
points at, `QOU.Torsion.MassIdentity` (`QOU/Torsion/MassIdentity.lean:17`),
formalises **nonabelian multiplicative integration** — its own docstring says
`m = ‖MI∫_Σ (∇_A q, L ∧ F⁺)‖ = ‖Hol_{∇_A}(γ; 𝔊)‖`. Neither text mentions the
other's formula. The ref is correct (it carries the block's `\label`), the
*mathematics* is a different object.

**Defect 2 — wall side.** `GroundRingAnnotations.lean` lists `Torsion/` as
**generic `k`, formal chain ✓**. `MassIdentity` sits in `Torsion/` and is ℝ-valued.
That is an in-tree contradiction, not an inference.

## The two archimedean anchors, and how deep each goes

| field | anchor | removable? |
|---|---|---|
| `sp : SubstrateParameter M` | `SubstrateParameter.field : M → ℝ` with `field_pos`, `field_ge_one`, `not_root_of_unity` — irreducibly ordered and archimedean | **yes, trivially** — nothing in the tree ever reads `MassIdentity.sp` (verified by grep; the `.sp` hits are `Symplectic.sp`, `cr.sp`, `eigenvalue.sp` on unrelated structures). It is an inert field. |
| `integrand_nonneg : 0 ≤ connectionGradient p * leviCurvatureCoupling p` | an **order** on the codomain | no — but it belongs in the archimedean layer, which is where its only consumer already is |
| `connectionGradient`, `leviCurvatureCoupling : M → ℝ` | none — never ordered, never normed, never fed to a real-analytic function inside this file | **yes** → `M → R` |

`vortexCycle : Set M` / `cycle_nonempty` are ring-free.

## Blast radius — small, and the archimedean consumer already exists

Consumers of `QOU.Torsion.MassIdentity`, exhaustively:

- `QOU/Torsion/TopologicalMass.lean:63` — `TopologicalMassDecomposition.mi`. That
  structure is thoroughly ℝ already (`baselineHolonomy : ℝ`,
  `exceptionalContribution : Fin n → ℝ`, `totalMass : ℝ`, three `0 ≤ _`
  hypotheses). It **is** the archimedean layer; it just is not labelled as one.
- `QOU/Torsion/TopologicalMass.lean:214` — `mass_dim_zero_pointwise`, whose entire
  body is `mi.integrand_nonneg p hp`.
- `QOU/Torsion/MassIdentity.lean:28` — `MassIdentityC extends MassIdentity`.
  **Zero consumers anywhere in the tree.**
- Four `.ts` blocks: `mass-identity`, `mass-identity-C`, `mass-identity-exists`,
  `mass-identity-unique`. The last two point at `QOU.MassIdentity.exists` /
  `.unique`, **neither of which exists** — they are `qou-2u26` backlog. So only two
  live refs constrain any rename.

## The pattern to copy is already in this namespace

`QOU/Torsion/HeckeMassElement.lean` does exactly what the owner asked for, in the
same directory, and nothing here needs inventing:

- `structure HeckeMassElement (R : Type u) [CommRing R]` — generic;
- `def frobeniusMassSquared … : R` — "Valued in `R` (no Archimedean norm)";
- `noncomputable def HeckeMassElement.mass {R} [NormedCommRing R] : ℝ := ‖…‖` —
  docstring: "**Post-Arch** … lives downstream of the formal chain. Per
  `QOU.GroundRingAnnotations`, this is **not** part of the pre-Arch chain."

Generic core → `[NormedCommRing R]` evaluation at the wall. That is the template.

## Prior bean 8jaf was closed on the prose alone

`8jaf` ("wall-side §7c: mass-identity — acknowledge (R-valued trace over generic
R)", completed 2026-07-05) is **title-only** — no body. What exists is the
"Archimedean specialisation" paragraph in `mass-identity.md`, which names two
identifiers, `frobeniusMass` (generic `R`) and `scalarMass` (the `R → ℝ`
realisation). **Neither exists in the Lean tree**; the closest is
`frobeniusMassSquared` in `HeckeMassElement.lean`. The acknowledgement was
written into the prose and the Lean was never touched. (The shallow clone here
cannot show the commit that closed 8jaf, so this is a stated correlation, not a
proved causal link.)

This is the same failure mode as the five cluster beans triaged in #5113: an
empty bean marked done, with the real gap surviving it.

## Options (for owner decision — not yet chosen)

1. **Generalise in place, split at the wall.** Follow `HeckeMassElement`: generic
   `MassIdentity (R) [CommRing R]` with `sp` dropped and `integrand_nonneg`
   moved out; an archimedean specialisation carries `sp` + the ordering, and
   `TopologicalMassDecomposition` consumes *that*. Fixes defect 2 only.
2. **Write the prose's declarations.** Add `frobeniusMass` (generic `R`) and
   `scalarMass` (`R → ℝ`), repoint `def:mass-identity` at `frobeniusMass`. Fixes
   defect 1, but leaves the existing structure carrying a `\label` it would no
   longer own, and with no block of its own.
3. **Treat the block as an identity, not a definition.** The label says
   *identity*; the Lean docstring is a chain of `=`. Define mass once
   (categorical trace, generic `R`) and carry "multiplicative integration agrees
   with it" as a §3b-conditional class field, since it is asserted and unproved.
   Fixes both, and is the only option that makes the docstring's own `=` chain
   auditable.
4. **Record only.** Status quo; `qou-qc6s` already records it.

Options 1 and 2 compose (1 then 2). Option 3 subsumes both but is the largest.
