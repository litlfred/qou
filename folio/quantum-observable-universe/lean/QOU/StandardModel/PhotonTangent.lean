/-
  The photons as a tangent space, and what that buys downstream.

  `def:photon` is `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` (owner ruling 2026-11-18/20).
  Write `W = span{σ₀, σ₁, V}`, `V = σ₀σ₁⁻¹`. Owner ruling 2026-11-25 ("W is tangent = y"):
  state in Lean that `W` is the tangent space at `1` of the photon family.

  1. **Infinitesimal photons add** (`photon_mul_photon_of_sq_eq_zero`). Over a base ring
     with a scalar `ε`, `ε² = 0` (e.g. the dual numbers `R[ε]`), the product of the
     photons with weights `ε•φ` and `ε•ψ` is the photon with weights `ε•(φ + ψ)`. So on the
     first-order neighbourhood of the bare photon the γγ product is addition of colour
     weights: `W` with addition is the tangent group of the photon family at `1`. The
     statement is false without `ε² = 0`: the two-photon term `w_φ w_ψ` is what it drops.
  2. **Collinear factorisation is forced** (`collinear_photon_factorisation`). Photons on
     one tangent line `R·V` are `1 + a•V`. If `1, V, V²` are linearly independent and
     `V³ = (1 + a₀•V)(1 + b₀•V)`, then every factorisation `V³ = (1 + a•V)(1 + b•V)` over a
     domain has `{a, b} = {a₀, b₀}`. Applied to the Borromean core `V³ = β_Bor` with the
     corpus factorisation `γ(0,0,qh)·γ(0,0,−q⁻¹h)`
     (`QOU.Mass.BorromeanPhotonFactorisation.borromean_eq_two_photons`), this says the
     weights `qh, −q⁻¹h` are the only weights on the line `R·V`: they are forced by the
     minimal polynomial of `V`, not chosen. The independence of `1, V, V²` in `H₃(q)` is a
     hypothesis here; it is measured exactly (rank 3 over `ℚ(q)`) in
     `computations/probes/photon_jet_spectral/tangent_followups_probe.py`, not proved in Lean.

  Generic commutative ring `R` (§7c).

  -- Ref: [leitner2026] predicted-spectra, def:photon
-/
import QOU.StandardModel.Photon
import QOU.MassTheory.BorromeanPhotonFactorisation
import Mathlib.LinearAlgebra.LinearIndependent.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Module

namespace QOU.PhotonTangent

open QOU.Photon

section Infinitesimal

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- Colour weights scaled by a scalar. -/
def Colour.smul (ε : R) (c : Colour R) : Colour R := ⟨ε * c.phi0, ε * c.phi1, ε * c.phi01⟩

/-- Colour weights added. -/
def Colour.add (c d : Colour R) : Colour R := ⟨c.phi0 + d.phi0, c.phi1 + d.phi1, c.phi01 + d.phi01⟩

/-- **Infinitesimal photons add.** If `ε² = 0`, then
`γ(ε•φ) · γ(ε•ψ) = γ(ε•(φ + ψ))`. -/
theorem photon_mul_photon_of_sq_eq_zero (σ₀ : A) (σ₁ : Aˣ) {ε : R} (hε : ε * ε = 0)
    (φ ψ : Colour R) :
    photon σ₀ σ₁ (Colour.smul ε φ) * photon σ₀ σ₁ (Colour.smul ε ψ)
      = photon σ₀ σ₁ (Colour.smul ε (Colour.add φ ψ)) := by
  have key : ∀ (a b : R) (x y : A), ((ε * a) • x) * ((ε * b) • y) = 0 := by
    intro a b x y
    rw [smul_mul_smul_comm]
    have : ε * a * (ε * b) = (ε * ε) * (a * b) := by ring
    rw [this, hε, zero_mul, zero_smul]
  simp only [photon, Colour.smul, Colour.add, add_mul, mul_add, one_mul, mul_one, key,
    add_zero]
  module

end Infinitesimal

section Collinear

variable {R A : Type*} [CommRing R] [IsDomain R] [Ring A] [Algebra R A]

omit [IsDomain R] in
/-- Two photons on the line `R·V` multiply to `1 + (a+b)•V + (ab)•V²`. -/
theorem collinear_mul (V : A) (a b : R) :
    (1 + a • V) * (1 + b • V) = 1 + (a + b) • V + (a * b) • (V * V) := by
  simp only [add_mul, mul_add, one_mul, mul_one, smul_mul_smul_comm, add_smul]
  abel

/-- **Collinear factorisation is forced.** If `1, V, V²` are linearly independent and
`(1 + a•V)(1 + b•V) = (1 + a₀•V)(1 + b₀•V)`, then `a + b = a₀ + b₀` and `ab = a₀b₀`;
over a domain, `a = a₀ ∧ b = b₀` or `a = b₀ ∧ b = a₀`. -/
theorem collinear_photon_factorisation {V : A}
    (hli : LinearIndependent R ![(1 : A), V, V * V]) {a b a₀ b₀ : R}
    (h : (1 + a • V) * (1 + b • V) = (1 + a₀ • V) * (1 + b₀ • V)) :
    (a = a₀ ∧ b = b₀) ∨ (a = b₀ ∧ b = a₀) := by
  rw [collinear_mul, collinear_mul] at h
  have hcoef := (Fintype.linearIndependent_iff.mp hli)
    ![0, (a + b) - (a₀ + b₀), a * b - a₀ * b₀] (by
      simp only [Fin.sum_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one,
        Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, zero_smul, zero_add,
        sub_smul]
      linear_combination (norm := module) h)
  have hs : a + b = a₀ + b₀ := sub_eq_zero.mp (by simpa using hcoef 1)
  have hp : a * b = a₀ * b₀ := sub_eq_zero.mp (by simpa using hcoef 2)
  -- `a` is a root of `(x - a₀)(x - b₀)`
  have hroot : (a - a₀) * (a - b₀) = 0 := by
    have hb : b = a₀ + b₀ - a := by linear_combination hs
    rw [hb] at hp
    linear_combination -hp
  rcases mul_eq_zero.mp hroot with h1 | h1
  · left; refine ⟨sub_eq_zero.mp h1, ?_⟩
    linear_combination hs - h1
  · right; refine ⟨sub_eq_zero.mp h1, ?_⟩
    linear_combination hs - h1

open QOU.Mass.BorromeanPhotonFactorisation in
/-- **The Borromean photon weights are forced.** In any algebra satisfying the `H₃(q)`
relations, if `1, V, V²` are linearly independent (true in `H₃(q)` over `ℚ(q)`, measured),
then the only factorisation of `β_Bor = V³` into two photons on the line `R·V` is the
corpus one, `γ(0,0,qh)·γ(0,0,−q⁻¹h)`, up to order. -/
theorem borromean_weights_forced {h : R} {a b : A} (H : HeckeH3Rel h a b) {q q' : R}
    (hh : q - q' = h) (hq : q * q' = 1)
    (hli : LinearIndependent R ![(1 : A), vertex h a b, vertex h a b * vertex h a b])
    {x y : R}
    (hxy : (1 + x • vertex h a b) * (1 + y • vertex h a b)
      = vertex h a b * vertex h a b * vertex h a b) :
    (x = q * h ∧ y = -(q' * h)) ∨ (x = -(q' * h) ∧ y = q * h) := by
  rw [borromean_eq_two_photons H hh hq, photonPlus, photonMinus, sub_eq_add_neg,
    ← neg_smul] at hxy
  exact collinear_photon_factorisation hli hxy

end Collinear

end QOU.PhotonTangent
