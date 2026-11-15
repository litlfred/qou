import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import QOU.KnotTheory


/-!
# QOU.Hadron — Composite localized knot (hadronic state)

A hadron is a finite collection of knots at a common base point,
bound by the Hopf link internal structure.  Baryons have three
constituent knots; mesons have two (knot–antiknot pair).

## References

- [leitner2026] §3 Lifting of Quantum Torsion
- [kock2004] https://doi.org/10.1017/CBO9780511615443

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- A hadron: a composite of knot types at a common point, with
    binding energy from the Hopf link structure. -/
structure Hadron where
  /-- Spherical coordinate θ of the common base point. -/
  theta : R_q
  /-- Spherical coordinate φ of the common base point. -/
  phi : R_q
  /-- The constituent knot types (valence quarks in the knot picture). -/
  constituents : List KnotTheory.BraidWord
  /-- A hadron must have at least 2 constituents. -/
  -- Ref: [leitner2026] §3, Definition: Hadron
  constituents_nonempty : constituents.length ≥ 2

/-! ## Classification -/

/-- A baryon is a hadron with exactly 3 constituents. -/
def Hadron.isBaryon (h : Hadron) : Prop := h.constituents.length = 3

/-- A meson is a hadron with exactly 2 constituents. -/
def Hadron.isMeson (h : Hadron) : Prop := h.constituents.length = 2

/-- Every hadron is either a meson, a baryon, or exotic (≥ 4 constituents). -/
-- Ref: [leitner2026] §3, Remark: Hadron classification
theorem Hadron.meson_or_baryon_or_exotic (h : Hadron) :
    h.isMeson ∨ h.isBaryon ∨ h.constituents.length ≥ 4 := by
  unfold isMeson isBaryon
  have h2 := h.constituents_nonempty
  omega

/-! ## Base point and constituent accessors -/

/-- The base point of a hadron on S². -/
def Hadron.basePoint (h : Hadron) : R_q × R_q :=
  (h.theta, h.phi)

/-- Number of constituents (valence quarks). -/
def Hadron.valence (h : Hadron) : ℕ :=
  h.constituents.length

/-- Total crossing number of all constituent knots. -/
def Hadron.totalCrossings (h : Hadron) : ℕ :=
  h.constituents.foldl (fun acc k => acc + k.crossingCount) 0

/-! ## Mass structure

The hadronic mass formula: m_H = Q(q) · M(L_Hopf) + Σᵢ M(Kᵢ)
where Q(q) encodes the q-deformed Skein polynomial of the binding link. -/

/-- Binding structure: the Hopf link and its Skein polynomial contribution. -/
-- Ref: [leitner2026] §3, Definition: Hadron mass
structure HadronBinding where
  /-- The q-deformation parameter (formal indeterminate of `R_q`). -/
  q : R_q
  /-- The binding link (Hopf link braid word). -/
  bindingLink : KnotTheory.BraidWord
  /-- The Skein polynomial evaluation Q(q) · M(L_Hopf), as an archimedean
      mass value in `ℝ` (post-wall numerical evaluation). -/
  bindingMass : ℝ
  -- Binding mass is non-negative (archimedean):
  --   bindingMass_nonneg : 0 ≤ bindingMass
  -- omitted here; the ordering lives in the archimedean evaluation layer.
  -- Ref: [leitner2026] §3

/-- Mass of a single constituent knot, given by its hyperbolic volume
    in the QOU framework.  Returns the volume value. -/
noncomputable def constituentMass (k : KnotTheory.BraidWord)
    (vol : KnotTheory.HyperbolicVolume) : ℝ :=
  vol.value

/-- The total mass of a hadron given a binding structure and constituent volumes.
    m_H = bindingMass + Σᵢ vol(Kᵢ) -/
-- Ref: [leitner2026] §3, Proposition: Terminal resolution
noncomputable def Hadron.mass (h : Hadron) (binding : HadronBinding)
    (volumes : List KnotTheory.HyperbolicVolume) : ℝ :=
  binding.bindingMass + volumes.foldl (fun acc v => acc + v.value) 0

/-! ## Hadron from localized knots -/

/-- A localized knot: a knot type placed at a point `(θ, φ)` on the base
    manifold `CP¹ ≅ S²`.  This mirrors `QOU.LocalizedKnot` (defined in
    `lifting-and-descent/localized-knot.lean`); it is restated locally
    because this standalone content sibling imports only `QOU.KnotTheory`
    and the `localized-knot` sibling is not part of that import closure. -/
-- Ref: [leitner2026] §3, Definition: Localized knot
structure LocalizedKnot where
  /-- Spherical coordinate θ ∈ [0, π] on CP¹ ≅ S². -/
  theta : R_q
  /-- Spherical coordinate φ ∈ [0, 2π) on CP¹ ≅ S². -/
  phi : R_q
  /-- The knot type at this point (given by its braid word). -/
  knot : KnotTheory.BraidWord

/-- The base point of a localized knot as a pair `(θ, φ)` on S². -/
def LocalizedKnot.basePoint (k : LocalizedKnot) : R_q × R_q :=
  (k.theta, k.phi)

/-- Construct a hadron from a list of co-located localized knots. -/
def Hadron.fromLocalizedKnots (knots : List LocalizedKnot)
    (h_len : knots.length ≥ 2)
    (h_coloc : ∀ k₁ k₂, k₁ ∈ knots → k₂ ∈ knots →
      k₁.basePoint = k₂.basePoint)
    (h_ne : knots ≠ []) : Hadron where
  theta := (knots.head h_ne).theta
  phi := (knots.head h_ne).phi
  constituents := knots.map LocalizedKnot.knot
  constituents_nonempty := by simp [List.length_map]; exact h_len

/-- A baryon has at least 2 constituents (follows from the hadron constraint). -/
theorem Hadron.baryon_ge_two (h : Hadron) (hb : h.isBaryon) :
    h.constituents.length ≥ 2 := by
  unfold isBaryon at hb; omega

/-- A meson has exactly the minimum number of constituents. -/
theorem Hadron.meson_is_minimal (h : Hadron) (hm : h.isMeson) :
    h.valence = 2 := hm

end

end QOU
