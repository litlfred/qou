/-
  The Borromean braid is a product of two photons in `H₃(q)`.

  Let `A` be an algebra over a commutative ring `R`, and let `a b : A`
  (the images of `σ₀, σ₁`) satisfy the defining relations of `H₃(q)` with
  `h = q − q⁻¹`:

      a² = h·a + 1,   b² = h·b + 1,   aba = bab.

  Then `b` is invertible with `b⁻¹ = b − h`, and with `V := a·b⁻¹ = ab − h·a`:

  * `V³ = 1 + h²·V − h²·V²`, i.e. `(V − 1)(V² + (1 + h²)V + 1) = 0`
    (`borromean_cube_reduce`);
  * if `q, q' ∈ R` satisfy `q − q' = h` and `q·q' = 1` (so `q' = q⁻¹`), then

      β_Bor = (σ₀σ₁⁻¹)³ = (1 + q h V)(1 − q⁻¹ h V)

    (`borromean_eq_two_photons`).

  Each factor is a photon `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` in the sense of
  `def:photon` (`QOU.Photon.photon`, imported, not redefined here), with
  `σ₁` promoted to the unit `HeckeH3Rel.unitB` (inverse `b − h`), and with
  only its last term:

      1 + q h V    = γ(0, 0, q h),
      1 − q⁻¹ h V  = γ(0, 0, −q⁻¹ h)

  (`photonPlus_eq`, `photonMinus_eq`), and the two factors commute
  (`photonPlus_photonMinus_comm`). Before the 2026-11-18 owner ruling on the
  photon's last term (bean `qou-99qc`), the photon's last term was `σ₀σ₁` and
  the same two elements carried the weights `(−q h², 0, q h)` and
  `(q⁻¹ h², 0, −q⁻¹ h)`; the elements are unchanged, only their coordinates.

  The statement is about any algebra satisfying the relations, so it holds in
  `H₃(q)` itself and in every representation of it. No division, no ordering,
  no numerical value of `q` is used.

  -- Ref: [iwahori1964] https://doi.org/10.15083/00039809
  -- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9
-/
import QOU.Photon
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Tactic.Module
import Mathlib.Tactic.NoncommRing

namespace QOU.Mass.BorromeanPhotonFactorisation

open QOU.Photon (photon Colour)

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- The relations of `H₃(q)` on two elements `a = σ₀`, `b = σ₁`, with
    `h = q − q⁻¹`. -/
structure HeckeH3Rel (h : R) (a b : A) : Prop where
  quad_a : a * a = h • a + 1
  quad_b : b * b = h • b + 1
  braid : a * b * a = b * a * b

variable {h : R} {a b : A}

/-- `b − h` is a two-sided inverse of `b`. -/
theorem HeckeH3Rel.mul_inv (H : HeckeH3Rel h a b) : b * (b - h • 1) = 1 := by
  rw [mul_sub, mul_smul_comm, mul_one, H.quad_b]; abel

theorem HeckeH3Rel.inv_mul (H : HeckeH3Rel h a b) : (b - h • 1) * b = 1 := by
  rw [sub_mul, smul_mul_assoc, one_mul, H.quad_b]; abel

/-- `b` as a unit of `A`, with inverse `b − h`. -/
def HeckeH3Rel.unitB (H : HeckeH3Rel h a b) : Aˣ := ⟨b, b - h • 1, H.mul_inv, H.inv_mul⟩

@[simp] theorem HeckeH3Rel.unitB_val (H : HeckeH3Rel h a b) : (H.unitB : A) = b := rfl

@[simp] theorem HeckeH3Rel.unitB_inv (H : HeckeH3Rel h a b) : ((H.unitB⁻¹ : Aˣ) : A) = b - h • 1 :=
  rfl

/-- `V = σ₀σ₁⁻¹ = ab − h·a`. -/
def vertex (h : R) (a b : A) : A := a * (b - h • 1)

theorem vertex_eq (h : R) (a b : A) : vertex h a b = a * b - h • a := by
  simp [vertex, mul_sub, mul_smul_comm]

/-! ### Reduction rules (right-associated words). -/

section Reduce
variable (H : HeckeH3Rel h a b)
include H

theorem red_aa (x : A) : a * (a * x) = h • (a * x) + x := by
  rw [← mul_assoc, H.quad_a, add_mul, smul_mul_assoc, one_mul]

theorem red_bb (x : A) : b * (b * x) = h • (b * x) + x := by
  rw [← mul_assoc, H.quad_b, add_mul, smul_mul_assoc, one_mul]

theorem red_bab (x : A) : b * (a * (b * x)) = a * (b * (a * x)) := by
  have := congrArg (· * x) H.braid
  simp only [mul_assoc] at this
  exact this.symm

theorem red_bab' : b * (a * b) = a * (b * a) := by
  have := H.braid; simp only [mul_assoc] at this; exact this.symm

/-- Normal form of `V²`. -/
theorem vertex_sq :
    vertex h a b * vertex h a b
      = b * a - (h ^ 2) • (a * b) - h • b + (h ^ 3) • a + (h ^ 2) • (1 : A) := by
  rw [vertex_eq]
  simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, smul_sub, mul_assoc,
    red_aa H, red_bb H, red_bab H, red_bab' H, smul_add, mul_add, add_mul, mul_one,
    H.quad_a, smul_smul]
  module

/-- Normal form of `V³`. -/
theorem vertex_cube :
    vertex h a b * vertex h a b * vertex h a b
      = -(h ^ 2) • (b * a) + (h ^ 3) • b + (1 - h ^ 4) • (1 : A)
        + (h ^ 4 + h ^ 2) • (a * b) - (h ^ 5 + h ^ 3) • a := by
  rw [vertex_sq H, vertex_eq]
  simp only [sub_mul, mul_sub, add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_sub,
    smul_add, mul_assoc, red_aa H, red_bb H, red_bab H, red_bab' H, mul_one, one_mul,
    H.quad_a, H.quad_b, smul_smul]
  module

end Reduce

/-- **Cubic relation of the vertex.** `V³ = 1 + h²V − h²V²`, equivalently
    `(V − 1)(V² + (1 + h²)V + 1) = 0`. -/
theorem borromean_cube_reduce (H : HeckeH3Rel h a b) :
    vertex h a b * vertex h a b * vertex h a b
      = 1 + (h ^ 2) • vertex h a b - (h ^ 2) • (vertex h a b * vertex h a b) := by
  rw [vertex_cube H, vertex_sq H, vertex_eq]
  module

theorem vertex_cubic_factor (H : HeckeH3Rel h a b) :
    (vertex h a b - 1) * (vertex h a b * vertex h a b + (1 + h ^ 2) • vertex h a b + 1) = 0 := by
  have hc := borromean_cube_reduce H
  set V := vertex h a b
  have : (V - 1) * (V * V + (1 + h ^ 2) • V + 1)
      = V * V * V - (1 + (h ^ 2) • V - (h ^ 2) • (V * V)) := by
    simp only [sub_mul, mul_add, mul_smul_comm, smul_mul_assoc, mul_one, one_mul, mul_assoc,
      add_smul, one_smul]
    module
  rw [this, hc, sub_self]

/-- `1 + q h V`. -/
def photonPlus (q h : R) (a b : A) : A := 1 + (q * h) • vertex h a b

/-- `1 − q⁻¹ h V`, with `q' = q⁻¹` supplied as an element. -/
def photonMinus (q' h : R) (a b : A) : A := 1 - (q' * h) • vertex h a b

/-- The photon's last term is this file's vertex: `σ₀ · (unitB)⁻¹ = V`. -/
theorem photon_vertex_eq (H : HeckeH3Rel h a b) :
    QOU.Photon.vertex a H.unitB = vertex h a b := rfl

theorem photonPlus_eq (H : HeckeH3Rel h a b) (q : R) :
    photonPlus q h a b = photon a H.unitB (⟨0, 0, q * h⟩ : Colour R) := by
  simp only [photonPlus, photon, photon_vertex_eq H, zero_smul, add_zero]

theorem photonMinus_eq (H : HeckeH3Rel h a b) (q' : R) :
    photonMinus q' h a b = photon a H.unitB (⟨0, 0, -(q' * h)⟩ : Colour R) := by
  simp only [photonMinus, photon, photon_vertex_eq H, zero_smul, add_zero, neg_smul,
    sub_eq_add_neg]

/-- The two photons commute (both are polynomials in `V`). -/
theorem photonPlus_photonMinus_comm (q q' h : R) (a b : A) :
    photonPlus q h a b * photonMinus q' h a b = photonMinus q' h a b * photonPlus q h a b := by
  simp only [photonPlus, photonMinus, add_mul, mul_add, sub_mul, mul_sub, one_mul, mul_one,
    smul_mul_smul_comm]
  module

/-- **The Borromean braid is a product of two photons.**
    If `q − q' = h` and `q q' = 1`, then
    `(σ₀σ₁⁻¹)³ = (1 + q h V)(1 − q⁻¹ h V)`. -/
theorem borromean_eq_two_photons (H : HeckeH3Rel h a b) {q q' : R}
    (hh : q - q' = h) (hq : q * q' = 1) :
    vertex h a b * vertex h a b * vertex h a b
      = photonPlus q h a b * photonMinus q' h a b := by
  rw [borromean_cube_reduce H]
  simp only [photonPlus, photonMinus, add_mul, mul_sub, one_mul, mul_one, smul_mul_smul_comm]
  have e1 : (q * h) • vertex h a b - (q' * h) • vertex h a b = (h ^ 2) • vertex h a b := by
    rw [← sub_smul]; congr 1; rw [← sub_mul, hh]; ring
  have e2 : (q * h * (q' * h)) = h ^ 2 := by
    calc q * h * (q' * h) = (q * q') * h ^ 2 := by ring
      _ = h ^ 2 := by rw [hq, one_mul]
  rw [e2, ← e1]
  abel

/-- The same statement with the photons written as `def:photon`:
    `β_Bor = γ(0, 0, q h) · γ(0, 0, −q⁻¹ h)`, each photon carrying only its
    vertex term. -/
theorem borromean_eq_photon_product (H : HeckeH3Rel h a b) {q q' : R}
    (hh : q - q' = h) (hq : q * q' = 1) :
    vertex h a b * vertex h a b * vertex h a b
      = photon a H.unitB (⟨0, 0, q * h⟩ : Colour R)
        * photon a H.unitB (⟨0, 0, -(q' * h)⟩ : Colour R) := by
  rw [← photonPlus_eq H, ← photonMinus_eq H, borromean_eq_two_photons H hh hq]

end QOU.Mass.BorromeanPhotonFactorisation
