/-
Copyright (c) 2026 QOU contributors. All rights reserved.

Photons that are braid monomials, and the six-strand γγ lepton pair as two photons.

The ruled photon on two adjacent generators s = σᵢ, t = σᵢ₊₁ is
  γ(a, b, c) = 1 + a·s + b·t + c·s·t⁻¹,
with the larger letter inverted (owner rulings 2026-11-20 and 2026-11-22). In the Hecke
algebra σ² = h·σ + 1, so σ⁻¹ = σ − h, h = q − q⁻¹.

Results (generic: any field k and k-algebra A, with h ≠ 0; no ordering, no ℝ):
* `photon_neg_crossing`: γ(0, −h⁻¹, 0) = −h⁻¹·t⁻¹, a single negative crossing.
* `photon_hopf`: γ(0, −h⁻¹, −1) = −h⁻¹·s²·t⁻¹. The braid s²t⁻¹ on three strands closes to
  the Hopf link, so the electron's link is the closure of one photon.
* `pair_word_reduces`: the γγ word V₀V₁V₂V₀V₃ (Vᵢ = σᵢσᵢ₊₁⁻¹) equals σ₀²σ₁⁻¹σ₄⁻¹.
* `pair_word_two_photons`: V₀V₁V₂V₀V₃ = h²·γ₀(0, −h⁻¹, −1)·γ₃(0, −h⁻¹, 0).

The closure of V₀V₁V₂V₀V₃ is e⁻ ⊔ ν̄ ⊔ loop (probe
`computations/probes/six_strand_photon_pair/`, invariant at q = 2, 3); that link
identification is computational evidence and is not part of this file.
-/
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.FieldSimp

namespace QOU.MassTheory.PhotonCrossingMonomials

variable {k A : Type*} [Field k] [Ring A] [Algebra k A]

/-- The scalar `h` inside `A`. -/
abbrev hb (h : k) : A := algebraMap k A h

/-- The Hecke inverse `σ⁻¹ = σ − h`. -/
def hinv (h : k) (x : A) : A := x - hb h

/-- The ruled photon `1 + a·s + b·t + c·s·t⁻¹` on adjacent generators `s, t`. -/
def photon (h a b c : k) (s t : A) : A :=
  1 + a • s + b • t + c • (s * hinv h t)

lemma hb_mul (h : k) (x : A) : hb h * x = h • x := (Algebra.smul_def h x).symm

lemma mul_hb (h : k) (x : A) : x * hb h = h • x := by
  rw [← Algebra.commutes, hb_mul]

/-- `σ⁻¹ = σ − h` is a left inverse when `σ² = hσ + 1`. -/
theorem hinv_mul (h : k) (x : A) (hx : x * x = h • x + 1) : hinv h x * x = 1 := by
  unfold hinv
  rw [sub_mul, hx, hb_mul]; abel

/-- `σ⁻¹ = σ − h` is a right inverse when `σ² = hσ + 1`. -/
theorem mul_hinv (h : k) (x : A) (hx : x * x = h • x + 1) : x * hinv h x = 1 := by
  unfold hinv
  rw [mul_sub, hx, mul_hb]; abel

/-- A photon with weights `(0, −h⁻¹, 0)` is the single negative crossing `−h⁻¹·t⁻¹`. -/
theorem photon_neg_crossing (h : k) (hh : h ≠ 0) (s t : A) :
    photon h 0 (-h⁻¹) 0 s t = (-h⁻¹) • hinv h t := by
  unfold photon hinv
  have : h⁻¹ • hb (A := A) h = 1 := by
    rw [hb, Algebra.smul_def, ← map_mul, inv_mul_cancel₀ hh, map_one]
  rw [smul_sub, neg_smul, neg_smul, this]
  simp only [zero_smul, add_zero]
  abel

/-- A photon with weights `(0, −h⁻¹, −1)` is the braid monomial `−h⁻¹·s²·t⁻¹`. -/
theorem photon_hopf (h : k) (hh : h ≠ 0) (s t : A) (hs : s * s = h • s + 1) :
    photon h 0 (-h⁻¹) (-1) s t = (-h⁻¹) • (s * s * hinv h t) := by
  have h1 : h⁻¹ • hb (A := A) h = 1 := by
    rw [hb, Algebra.smul_def, ← map_mul, inv_mul_cancel₀ hh, map_one]
  have key : (-h⁻¹) • (s * s * hinv h t) = (-h⁻¹) • (h • s * hinv h t) + (-h⁻¹) • hinv h t := by
    rw [hs, add_mul, one_mul, smul_add]
  rw [key, smul_mul_assoc, smul_smul, neg_mul, inv_mul_cancel₀ hh]
  unfold photon hinv
  rw [smul_sub (-h⁻¹) t (hb h), neg_smul, neg_smul h⁻¹ (hb h), h1]
  simp only [zero_smul, add_zero, neg_smul, one_smul]
  abel

/-- The six-strand γγ word `V₀V₁V₂V₀V₃` reduces to `σ₀²σ₁⁻¹σ₄⁻¹` in any algebra where the
generators satisfy the Hecke relation and the far-commutation relations used. -/
theorem pair_word_reduces (h : k) (s0 s1 s2 s3 s4 : A)
    (h1 : s1 * s1 = h • s1 + 1) (h2 : s2 * s2 = h • s2 + 1) (h3 : s3 * s3 = h • s3 + 1)
    (c30 : s3 * s0 = s0 * s3) (c31 : s3 * s1 = s1 * s3) :
    (s0 * hinv h s1) * (s1 * hinv h s2) * (s2 * hinv h s3) * (s0 * hinv h s1) *
        (s3 * hinv h s4) = s0 * s0 * hinv h s1 * hinv h s4 := by
  have i1 := hinv_mul h s1 h1
  have i2 := hinv_mul h s2 h2
  have i3 := hinv_mul h s3 h3
  -- hinv s3 commutes with s0 and with hinv s1
  have d30 : hinv h s3 * s0 = s0 * hinv h s3 := by
    unfold hinv; rw [sub_mul, mul_sub, c30, hb_mul, mul_hb]
  have d31 : hinv h s3 * hinv h s1 = hinv h s1 * hinv h s3 := by
    unfold hinv
    simp only [sub_mul, mul_sub, c31, hb_mul, mul_hb, smul_sub]
    abel
  calc (s0 * hinv h s1) * (s1 * hinv h s2) * (s2 * hinv h s3) * (s0 * hinv h s1) *
          (s3 * hinv h s4)
      = s0 * (hinv h s1 * s1) * (hinv h s2 * s2) * (hinv h s3 * s0) * hinv h s1 * s3 *
          hinv h s4 := by noncomm_ring
    _ = s0 * (s0 * hinv h s3) * hinv h s1 * s3 * hinv h s4 := by rw [i1, i2, d30]; noncomm_ring
    _ = s0 * s0 * (hinv h s3 * hinv h s1) * s3 * hinv h s4 := by noncomm_ring
    _ = s0 * s0 * hinv h s1 * (hinv h s3 * s3) * hinv h s4 := by rw [d31]; noncomm_ring
    _ = s0 * s0 * hinv h s1 * hinv h s4 := by rw [i3]; noncomm_ring

/-- **The six-strand γγ lepton-pair word is a product of two photons**:
`V₀V₁V₂V₀V₃ = h²·γ₀(0, −h⁻¹, −1)·γ₃(0, −h⁻¹, 0)`. -/
theorem pair_word_two_photons (h : k) (hh : h ≠ 0) (s0 s1 s2 s3 s4 : A)
    (h0 : s0 * s0 = h • s0 + 1) (h1 : s1 * s1 = h • s1 + 1) (h2 : s2 * s2 = h • s2 + 1)
    (h3 : s3 * s3 = h • s3 + 1)
    (c30 : s3 * s0 = s0 * s3) (c31 : s3 * s1 = s1 * s3) :
    (s0 * hinv h s1) * (s1 * hinv h s2) * (s2 * hinv h s3) * (s0 * hinv h s1) *
        (s3 * hinv h s4) =
      (h ^ 2) • (photon h 0 (-h⁻¹) (-1) s0 s1 * photon h 0 (-h⁻¹) 0 s3 s4) := by
  rw [pair_word_reduces h s0 s1 s2 s3 s4 h1 h2 h3 c30 c31, photon_hopf h hh s0 s1 h0,
    photon_neg_crossing h hh s3 s4, smul_mul_smul_comm, smul_smul]
  have : h ^ 2 * (-h⁻¹ * -h⁻¹) = 1 := by field_simp
  rw [this, one_smul]

end QOU.MassTheory.PhotonCrossingMonomials
