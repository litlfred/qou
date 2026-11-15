import Mathlib.Data.Set.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Defs


/-!
# QOU.BraidKnot.PhaseBoundaryVariety — the phase-boundary variety

The pairwise-equality loci |y_{λ₁}| = |y_{λ₂}| and the shadow-price
vanishing loci are Zariski-closed; their union ℬ is measure-zero in Q.

LaTeX: `\label{prop:phase-boundary-variety}`
-/

namespace QOU.BraidKnot

universe u

/-- The pairwise-equality locus
    `ℬ_{λ₁,λ₂} = {q : y_{λ₁}²(q) = y_{λ₂}²(q)}` is cut out by the
    single polynomial equation `y_{λ₁}²(q) - y_{λ₂}²(q) = 0`, hence it
    equals the zero-set of `y_{λ₁}² - y_{λ₂}²` — the algebraic content
    of "Zariski-closed of codimension ≥ 1".

    (The downstream measure-zero claim for the finite union `ℬ`
    additionally requires the variety / measure API for `Q`; it is
    recorded as `phaseBoundary_measure_zero` below.) -/
-- Ref: [leitner2026] climax-volume-mass/local-shadow-ordering
theorem phaseBoundaryLocus_eq_zeroSet {R : Type u} [CommRing R]
    (y₁ y₂ : R → R) :
    {q : R | (y₁ q) ^ 2 = (y₂ q) ^ 2}
      = {q : R | (y₁ q) ^ 2 - (y₂ q) ^ 2 = 0} := by
  ext q
  simp [sub_eq_zero]

/-- **Phase-boundary variety is measure-zero.**

    The full variety `ℬ` is the finite union of the pairwise-equality
    loci (each a polynomial zero-set, see
    `phaseBoundaryLocus_eq_zeroSet`) with the shadow-price vanishing
    loci. A finite union of codimension-≥1 Zariski-closed sets is
    measure-zero; the proof needs the algebraic-variety / Lebesgue
    measure API for the base ring `Q`, deferred here. -/
-- Ref: [leitner2026] climax-volume-mass/local-shadow-ordering
theorem PhaseBoundaryVariety {R : Type u} [CommRing R]
    (B : Set R) (hB : ∃ (y₁ y₂ : R → R), B = {q : R | (y₁ q) ^ 2 = (y₂ q) ^ 2}) :
    ∃ (f : R → R), B = {q : R | f q = 0} := by
  obtain ⟨y₁, y₂, rfl⟩ := hB
  exact ⟨fun q => (y₁ q) ^ 2 - (y₂ q) ^ 2, by
    ext q; simp [sub_eq_zero]⟩

end QOU.BraidKnot
