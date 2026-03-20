---
name: formalizer
description: >
  Lean 4 Formalizer — translates the logical skeleton of narrative mathematical
  proofs into Lean 4 tactic blocks.  Uses the Ontologist's glossary to resolve
  types, maps narrative proof phrases to Lean tactics, and generates sorry-bridged
  partial proofs that compile.
allowed-tools: Read Write Edit Bash Grep Glob
---

# Lean 4 Formalizer (Narrative to Proof)

## Overview

This skill translates the **logical skeleton** of the paper into Lean 4
tactic blocks.  It depends on the Ontologist skill having already produced
a resolved glossary — every term used in theorems must have a unique type
assignment before formalization can proceed.

## When to Use This Skill

- After the Ontologist has produced `glossary.json` and `Glossary.lean`
- When translating theorem statements from LaTeX to Lean
- When filling `sorry` placeholders with actual proofs
- When `lake build` succeeds but there are remaining `sorry` warnings

## Workflow

### 1. Library synthesis

The Formalizer identifies required Mathlib imports from the glossary:

```bash
PYTHONPATH=.github/scripts python .github/scripts/formalizer.py synthesize-imports
```

Reads `glossary.json` and outputs the import block for each chapter file.

### 2. Generate theorem stubs

```bash
PYTHONPATH=.github/scripts python .github/scripts/formalizer.py generate-theorems
```

Creates Lean theorem declarations with `sorry` bodies, using the glossary
types for the statement signatures.

### 3. Tactic translation

The Formalizer maps narrative proof phrases to Lean tactics:

| Narrative Phrase                    | Primary Tactic          | Fallbacks                       |
|-------------------------------------|-------------------------|---------------------------------|
| "By calculation"                    | `ring`                  | `field_simp`, `polyrith`        |
| "Clearly follows from..."          | `aesop`                 | `linarith`, `omega`             |
| "By induction on n..."             | `induction n with`      | `cases n`                       |
| "By the universal property of..."  | `Limits.IsLimit.lift`   | `Limits.IsLimit.hom_ext`        |
| "Diagram commutes" / "naturality"  | `aesop_cat`             | `slice_lhs`, `slice_rhs`        |
| "By contradiction"                 | `by_contra`             | `exfalso`                       |
| "By definition"                    | `rfl`                   | `unfold`, `simp only`           |

### 4. The "Sorry" Bridge

When a narrative step is too complex for immediate formalization:

1. Extract the logical structure of the proof
2. Create a `lemma` for each non-trivial step
3. Fill each lemma body with `sorry`
4. **Add a `-- Ref: [key] url` comment** before each `sorry` linking
   to the foundational reference that would resolve the gap
5. Ensure the file remains syntactically correct
6. Track the sorry count in `proof-objects.json`

```lean
/-- Intermediate step: torsion lifts through jet prolongation.
    TODO: formalize using the Frobenius-Hopf structure. -/
lemma torsion_lifts_jet (A : FrobeniusHopfAlgebra) :
    JetProlongation A → TorsionLifting A := by
  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
  sorry
```

**Rule**: Every `sorry` must have a `-- Ref:` annotation.  The `key`
must match an entry in `references.bib` exactly (case-sensitive).  If no
published reference exists, use `[manuscript]` and cite the chapter/section.
This is enforced by the axiom report's Theoretical Gap Report (§8).

## Library Synthesis Rules

Based on the glossary types, import the correct Mathlib modules:

| Glossary Type             | Required Mathlib Import                              |
|---------------------------|------------------------------------------------------|
| `TopologicalSpace`        | `Mathlib.Topology.Basic`                             |
| `SmoothManifold`          | `Mathlib.Geometry.Manifold.SmoothManifoldWithCorners`|
| `Category`                | `Mathlib.CategoryTheory.Category.Basic`              |
| `MonoidalCategory`        | `Mathlib.CategoryTheory.Monoidal.Basic`              |
| `Functor`                 | `Mathlib.CategoryTheory.Functor.Basic`               |
| `NatTrans`                | `Mathlib.CategoryTheory.NatTrans`                    |
| `Limits.IsLimit`          | `Mathlib.CategoryTheory.Limits.IsLimit`              |
| `Group`                   | `Mathlib.Algebra.Group.Basic`                        |
| `Ring`                    | `Mathlib.Algebra.Ring.Basic`                         |
| `Module`                  | `Mathlib.Algebra.Module.Basic`                       |
| `FundamentalGroupoid`     | `Mathlib.Topology.AlgebraicTopology.FundamentalGroupoid` |
| `ModuleCat`               | `Mathlib.Algebra.Category.ModuleCat`                 |

## Proof State Export

The Formalizer can export the current goal state at any `sorry` site:

```bash
PYTHONPATH=.github/scripts python .github/scripts/formalizer.py export-proof-state \
  --file lean/QOU/Torsion.lean --line 42
```

Output follows the `ProofStateExport` schema in `schemas/qou-types.ts`.

## Integration with Ontologist

1. **Before formalization**: Ontologist runs, produces resolved `glossary.json`
2. **During formalization**: Formalizer checks every term against the glossary
3. **On type mismatch**: Formalizer reports back to Ontologist for re-evaluation
4. **After `lake build`**: If build fails, Ontologist re-scans for type conflicts

## Lean Output Structure

```
lean/
├── lakefile.lean
├── lean-toolchain
├── QOU.lean              ← Root import
└── QOU/
    ├── Basic.lean        ← Shared foundations
    ├── Glossary.lean     ← Ontologist output (central registry)
    ├── KnotTheory.lean   ← Knot combinatorics
    ├── MassDerivation.lean ← CODATA mass parameter derivation
    ├── QuantumObservableUniverse.lean  ← Chapter 1
    └── ...
```

## Proven Patterns

### Subsingleton as Categorical Vanishing

Use `Subsingleton` to model vanishing conditions (e.g., `H⁰(M, Ad(P)) = 0`)
without requiring `Preadditive` or `AddCommGroup` structure:

```lean
/-- All morphisms 𝟙 → Ad(A) are equal ⟺ Hom(𝟙, Ad(A)) = 0. -/
adjoint_vanishing : Subsingleton ((𝟙_ C) ⟶ adjointObj)

/-- All global adjoint sections are equal ⟺ H⁰(M, Ad(P)) = 0. -/
adjoint_cohomology_vanishes : Subsingleton adjointSections
```

**Why**: In a `k`-linear category, the zero morphism always exists, so
`Subsingleton` implies the only morphism is zero — equivalent to the hom-space
vanishing.  This avoids importing `Preadditive` just for a vanishing axiom.

### Irreducibility via Subsingleton Propagation

Prove irreducibility by propagating `Subsingleton` through an injective map:

```lean
theorem irreducible_connection (cqou : CQuantumObservableUniverse)
    (inst : InstantonConnection cqou.toCRManifoldData)
    (embed : inst.parallelAdjointSections → cqou.adjointSections)
    (h_inj : Function.Injective embed) :
    inst.IsIrreducible :=
  ⟨fun a b => h_inj (cqou.adjoint_cohomology_vanishes.allEq _ _)⟩
```

**Pattern**: Given `Subsingleton Y` and `f : X → Y` injective, conclude
`Subsingleton X` by `⟨fun a b => h_inj (inst.allEq _ _)⟩`.

### Coevaluation + Snake Identities for Exact Self-Pairing

Model non-degeneracy of a Frobenius form as a categorical self-duality
(exact pairing) using coevaluation and snake identities:

```lean
coevaluation : (𝟙_ C) ⟶ (obj ⊗ obj)
pairing_snake_left :
  (ρ_ obj).inv ≫ (obj ◁ coevaluation) ≫ (α_ obj obj obj).inv ≫
    ((mul ≫ frobeniusForm) ▷ obj) ≫ (λ_ obj).hom = 𝟙 obj
pairing_snake_right :
  (λ_ obj).inv ≫ (coevaluation ▷ obj) ≫ (α_ obj obj obj).hom ≫
    (obj ◁ (mul ≫ frobeniusForm)) ≫ (ρ_ obj).hom = 𝟙 obj
```

**Why**: Non-degeneracy of a bilinear form is hard to state categorically
without linear algebra.  The snake identities (`zig-zag`) are equivalent and
work in any monoidal category.

### Abstract Hodge Involution

Model the Hodge star as an involutive endomorphism — works at both the
categorical level and the concrete level:

```lean
-- Categorical level (any category with identity):
structure CatHodgeInvolution {C : Type u} [Category.{v} C] (X : C) where
  star : X ⟶ X
  star_sq : star ≫ star = 𝟙 X

-- Concrete level (Type):
structure HodgeInvolution (V : Type*) where
  star : V → V
  star_sq : ∀ v, star (star v) = v
```

Self-duality predicates follow as `f ≫ star = f` (categorical) or
`star v = v` (concrete).

## Blueprint Synchronization

The Formalizer must keep Lean declarations in sync with the blueprint:

1. Every Lean declaration referenced by `\lean{}` in
   `blueprint/src/content.tex` must exist in the Lean source
2. When a `sorry` is resolved, update the blueprint entry to add `\leanok`
3. When adding new theorems, add a corresponding entry to
   `blueprint/src/content.tex` with `\lean{}` and `\uses{}` edges
4. The `-- Ref: [key]` in Lean must match `\cite{key}` in the blueprint
   where applicable, ensuring bibliography consistency across both systems

## Checklist

- [ ] All theorem statements match the LaTeX originals
- [ ] Import blocks are minimal and correct
- [ ] Every `sorry` is tracked in `proof-objects.json`
- [ ] Every `sorry` has a `-- Ref: [key] url` comment (bibtex-linked)
- [ ] All `-- Ref:` keys exist in `references.bib`
- [ ] `lake build` succeeds (sorry warnings are expected)
- [ ] Tactic choices match the narrative proof strategy
- [ ] Proof state can be exported at every sorry site
- [ ] `blueprint/src/content.tex` entries match Lean declarations
- [ ] `\leanok` only on sorry-free declarations
