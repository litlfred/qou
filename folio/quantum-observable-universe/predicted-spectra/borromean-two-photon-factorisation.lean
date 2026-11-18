/-
  prop:borromean-two-photon-factorisation

  In H₃(q) the Borromean element (σ₀σ₁⁻¹)³ is the product of two four-term
  photons (def:photon), each of the form 1 + ε·h·V with V = σ₀σ₁⁻¹ and ε one
  of the two eigenvalues q, −q⁻¹ of a generator.

  Stated over a generic commutative ring R and an R-algebra A (§7c): s₀, s₁
  satisfy the quadratic Hecke relations sᵢ² = h·sᵢ + 1 and the braid relation.
  No archimedean input; no value of q is used.

  -- Ref: [leitner2026] predicted-spectra, prop:borromean-two-photon-factorisation
-/
import Mathlib.Algebra.Algebra.Defs
import Mathlib.Tactic

namespace QOU.Photon.Borromean

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- Hecke data on three strands: two generators with the quadratic relation
`sᵢ² = h • sᵢ + 1` and the braid relation. -/
structure HeckeThree (R A : Type*) [CommRing R] [Ring A] [Algebra R A] where
  h : R
  s0 : A
  s1 : A
  quad0 : s0 * s0 = h • s0 + 1
  quad1 : s1 * s1 = h • s1 + 1
  braid : s1 * (s0 * s1) = s0 * (s1 * s0)

namespace HeckeThree

variable (H : HeckeThree R A)

/-- The inverse of `s₁`: `s₁ - h`. -/
def s1inv : A := H.s1 - H.h • (1 : A)

theorem s1_mul_s1inv : H.s1 * H.s1inv = 1 := by
  simp only [s1inv, mul_sub, mul_smul_comm, mul_one, H.quad1]
  abel

theorem s1inv_mul_s1 : H.s1inv * H.s1 = 1 := by
  simp only [s1inv, sub_mul, smul_mul_assoc, one_mul, H.quad1]
  abel

/-- The γγ vertex `V = σ₀σ₁⁻¹`. -/
def V : A := H.s0 * H.s1inv

theorem V_eq : H.V = H.s0 * H.s1 - H.h • H.s0 := by
  simp [V, s1inv, mul_sub]

/-! Right-associated rewriting rules (a confluent system for H₃). -/

theorem quad0' (x : A) : H.s0 * (H.s0 * x) = H.h • (H.s0 * x) + x := by
  rw [← mul_assoc, H.quad0, add_mul, smul_mul_assoc, one_mul]

theorem quad1' (x : A) : H.s1 * (H.s1 * x) = H.h • (H.s1 * x) + x := by
  rw [← mul_assoc, H.quad1, add_mul, smul_mul_assoc, one_mul]

theorem braid' (x : A) : H.s1 * (H.s0 * (H.s1 * x)) = H.s0 * (H.s1 * (H.s0 * x)) := by
  have := congrArg (· * x) H.braid
  simpa [mul_assoc] using this

/-- **The cubic relation.** `V³ + h²V² − h²V − 1 = 0`, i.e.
`(V − 1)(V² + (1 + h²)V + 1) = 0`. -/
theorem V_cubic :
    H.V ^ 3 + (H.h * H.h) • H.V ^ 2 - (H.h * H.h) • H.V - 1 = 0 := by
  rw [V_eq]
  simp only [pow_succ, pow_zero, one_mul, mul_sub, sub_mul, mul_add, add_mul,
    smul_mul_assoc, mul_smul_comm, mul_assoc, smul_sub, smul_add, smul_smul,
    mul_one, one_mul, H.quad0, H.quad1, H.braid, H.quad0']
  module

/-- **Two-photon factorisation of the Borromean element.** With `q * qi = 1`
and `h = q - qi`,
`(σ₀σ₁⁻¹)³ = (1 + (q·h)•V) * (1 - (qi·h)•V)`.
Both factors are photons in the sense of `def:photon`: `V = σ₀σ₁ - h·σ₀`. -/
theorem borromean_eq_two_photons (q qi : R) (hq : q * qi = 1) (hh : H.h = q - qi) :
    H.V ^ 3 = (1 + (q * H.h) • H.V) * (1 - (qi * H.h) • H.V) := by
  have hc := H.V_cubic
  have expand : (1 + (q * H.h) • H.V) * (1 - (qi * H.h) • H.V)
      = 1 + (q * H.h - qi * H.h) • H.V - ((q * qi) * (H.h * H.h)) • (H.V * H.V) := by
    simp only [add_mul, mul_sub, one_mul, mul_one, smul_mul_assoc, mul_smul_comm]
    module
  rw [expand, hq, one_mul, ← sub_mul, ← hh]
  have : H.V ^ 3 = 1 + (H.h * H.h) • H.V - (H.h * H.h) • H.V ^ 2 := by
    rw [← sub_eq_zero]
    rw [← hc]
    abel
  rw [this, sq]

end HeckeThree

end QOU.Photon.Borromean
