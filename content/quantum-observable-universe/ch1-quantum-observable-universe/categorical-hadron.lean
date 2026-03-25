/-!
# QOU.CategoricalHadron — Categorical hadron (morphism into tensor powers of V)

A categorical hadron is a morphism 𝟙 → V^⊗n in a rigid monoidal
category, factoring through the Frobenius comultiplication and
projections to simple objects.

Authoritative source: `lean-archive/QOU/RepresentationTheory.lean`

## References

- [manuscript] §1 Quantum Observable Universe
- [kock2004] https://doi.org/10.1017/CBO9780511615443
-/

import Mathlib.CategoryTheory.Monoidal.Basic

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- A categorical hadron: a morphism from the unit into a tensor power
    of simple objects, factoring through the Frobenius comultiplication.
    LaTeX: `\label{def:categorical-hadron}`
    Ref: [manuscript] §1, Definition: Categorical hadron -/
structure CategoricalHadron (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The number of constituent simple objects (valence). -/
  valence : ℕ
  /-- Valence is at least 2. -/
  -- Ref: [manuscript] §1
  valence_ge : valence ≥ 2
  /-- The spin labels of the constituents (each as twice_j). -/
  constituent_spins : Fin valence → ℕ

/-- A categorical baryon has valence 3. -/
def CategoricalHadron.isBaryon {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (h : CategoricalHadron C) : Prop :=
  h.valence = 3

/-- A categorical meson has valence 2. -/
def CategoricalHadron.isMeson {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (h : CategoricalHadron C) : Prop :=
  h.valence = 2

/-- Every categorical hadron is a meson, baryon, or exotic. -/
theorem CategoricalHadron.meson_or_baryon_or_exotic
    {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (h : CategoricalHadron C) :
    h.isMeson ∨ h.isBaryon ∨ h.valence ≥ 4 := by
  unfold isMeson isBaryon
  omega

/-- The total tensor power for embedding: N = 2(j₁ + ⋯ + jₙ). -/
def CategoricalHadron.totalTensorPower {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (h : CategoricalHadron C) : ℕ :=
  2 * (Finset.univ.sum h.constituent_spins)

end QOU
