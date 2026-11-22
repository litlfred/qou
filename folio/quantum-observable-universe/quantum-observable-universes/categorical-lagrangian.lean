import QOU.QuantumObservableUniverses.QDifferentialGeometry
import Mathlib.CategoryTheory.Linear.Basic


/-!
# QOU.CategoricalLagrangian

The categorical Lagrangian `ℒ_q(∇, ψ) = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ`,
an endomorphism of `A` encoding the full physics before tracing.

Stated over an `R`-linear monoidal category `C` (the `k`-linearity of the
`(𝐂, A, τ)` triple), so the sum of the two endomorphisms is expressible.
The matter term `ψ* ⊗ 𝒟_∇ψ` is the rank-one endomorphism
`A --ψ*--> 𝟙 --𝒟_∇ψ--> A`, i.e. `costate ≫ (state ≫ 𝒟_∇)`.

The authoritative, importable structure `QOU.CategoricalLagrangian` — the
target of this block's `lean.ref` (`qou:QOU.CategoricalLagrangian`) — lives
in the `QOU` Lake library at
[`QOU.QuantumObservableUniverses.QDifferentialGeometry`].  Its `lagrangian`
morphism is pinned by the `lagrangian_formula` law field to
`dirac.dirac ≫ dirac.dirac + costate ≫ state ≫ dirac.dirac`.  Rather than
re-declare a shadowing copy (forbidden by the no-shadowing-stub rule, and a
duplicate-declaration error against the import below), this display sibling
imports the real structure and pins down its identity with the
`re_export` definitional equation, so the narrative `.md` retains a
type-checked `.lean` sibling that genuinely refers to the library object.

LaTeX: `\label{def:categorical-lagrangian}`

Ref: [leitner2026] §1-quantum-observable-universe
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- The `def:categorical-lagrangian` block's structure is the library
    `QOU.CategoricalLagrangian`.  This abbreviation records that the display
    sibling's referent is precisely that importable structure (with its
    `lagrangian_formula` law field), without re-declaring it. -/
abbrev CategoricalLagrangian.re_export
    (R : Type*) [CommRing R]
    (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R C]
    (fh : FrobeniusHopfData C) : Type _ :=
  CategoricalLagrangian R C fh

end QOU
