import QOU.MassTheory.PhotonCrossingMonomials

/-!
# Two more two-photon γγ words: the 5-vertex words with an idle strand

The ruled photon is `γ(a, b, c) = 1 + a·s + b·t + c·s·t⁻¹` on adjacent generators `s = σᵢ`,
`t = σᵢ₊₁` (`PhotonCrossingMonomials.photon`; owner rulings 2026-11-20 and 2026-11-22). In the
Hecke algebra `σ² = h·σ + 1`, `σ⁻¹ = σ − h`, `h = q − q⁻¹`.

The six-strand pair test of PR #9050 checked two photons on 68 words (the 3-vertex matches and the
5-vertex matches with no idle strand). The generated `PhotonPairNoFactor.lean` covers 88 words; the
20 extra ones are 5-vertex matches that leave one strand idle. Among them two words ARE two-photon
products, in six (word, i, j) cells. This file proves those identities.

* `photon_twist_s`, `photon_twist_t`: `γ(h, 0, 0) = s²` and `γ(0, h, 0) = t²` (a full twist).
* `photon_neg_pair`: `γ(0, −h⁻¹, h⁻²) = h⁻²·s⁻¹t⁻¹`, two negative crossings.
* `word_V0V1V0V1V2`: `V₀V₁V₀V₁V₂ = σ₀²σ₂⁻¹σ₃⁻¹`, so
  `V₀V₁V₀V₁V₂ = h²·γ₀(h,0,0)·γ₂(0,−h⁻¹,h⁻²) = h²·γ₂(0,−h⁻¹,h⁻²)·γ₀(h,0,0)` (cells (0,2), (2,0)).
* `word_V1V2V1V2V3`: `V₁V₂V₁V₂V₃ = σ₁²σ₃⁻¹σ₄⁻¹`, so it is `h²·γ₀(0,h,0)·γ₃(0,−h⁻¹,h⁻²)` and
  `h²·γ₁(h,0,0)·γ₃(0,−h⁻¹,h⁻²)`, in either order (cells (0,3), (1,3), (3,0), (3,1)).

Generic: any field `k` and `k`-algebra `A`, with `h ≠ 0`; the Hecke and far-commutation relations
are hypotheses on the generators. That these are the only two-photon cells among the 88 words is
`PhotonPairNoFactor` (1370 cells) plus `PhotonPairNoFactorSector` (the other 19).

-- Ref: [leitner2026] computations/probes/six_strand_photon_pair/six_strand_pair_probe.py
-/

namespace QOU.MassTheory.PhotonPairIdleFactor

open QOU.MassTheory.PhotonCrossingMonomials

variable {k A : Type*} [Field k] [Ring A] [Algebra k A]

/-- `γ(h, 0, 0) = s²`: the full twist. -/
theorem photon_twist_s (h : k) (s t : A) (hs : s * s = h • s + 1) :
    photon h h 0 0 s t = s * s := by
  unfold photon; rw [hs]; simp only [zero_smul, add_zero]; abel

/-- `γ(0, h, 0) = t²`: the full twist on the second generator. -/
theorem photon_twist_t (h : k) (s t : A) (ht : t * t = h • t + 1) :
    photon h 0 h 0 s t = t * t := by
  unfold photon; rw [ht]; simp only [zero_smul, add_zero]; abel

/-- `γ(0, −h⁻¹, h⁻²) = h⁻²·s⁻¹t⁻¹`: two negative crossings. -/
theorem photon_neg_pair (h : k) (hh : h ≠ 0) (s t : A) :
    photon h 0 (-h⁻¹) (h⁻¹ ^ 2) s t = (h⁻¹ ^ 2) • (hinv h s * hinv h t) := by
  unfold photon hinv
  have e1 : ∀ x : A, hb h * x = h • x := hb_mul h
  have e2 : (h⁻¹ ^ 2) • (hb (A := A) h * hb h) = 1 := by
    rw [hb, ← map_mul, Algebra.smul_def, ← map_mul]
    rw [show h⁻¹ ^ 2 * (h * h) = 1 by field_simp, map_one]
  have e3 : (h⁻¹ ^ 2) • (h • t) = h⁻¹ • t := by
    rw [smul_smul, show h⁻¹ ^ 2 * h = h⁻¹ by field_simp]
  simp only [sub_mul, mul_sub, smul_sub, e1, e3, zero_smul, add_zero, neg_smul]
  rw [show (h⁻¹ ^ 2) • (h • hb (A := A) h) = 1 by
    rw [← e2, e1]]
  abel

/-- `V₀V₁V₀V₁V₂ = σ₀²σ₂⁻¹σ₃⁻¹`. -/
theorem word_V0V1V0V1V2_reduces (h : k) (s0 s1 s2 s3 : A)
    (h1 : s1 * s1 = h • s1 + 1) (h2 : s2 * s2 = h • s2 + 1) (c20 : s2 * s0 = s0 * s2) :
    (s0 * hinv h s1) * (s1 * hinv h s2) * (s0 * hinv h s1) * (s1 * hinv h s2) *
        (s2 * hinv h s3) = s0 * s0 * hinv h s2 * hinv h s3 := by
  have i1 := hinv_mul h s1 h1
  have i2 := hinv_mul h s2 h2
  have d20 : hinv h s2 * s0 = s0 * hinv h s2 := by
    unfold hinv; rw [sub_mul, mul_sub, c20, hb_mul, mul_hb]
  calc (s0 * hinv h s1) * (s1 * hinv h s2) * (s0 * hinv h s1) * (s1 * hinv h s2) *
          (s2 * hinv h s3)
      = s0 * (hinv h s1 * s1) * (hinv h s2 * s0) * (hinv h s1 * s1) * (hinv h s2 * s2) *
          hinv h s3 := by noncomm_ring
    _ = s0 * s0 * hinv h s2 * hinv h s3 := by rw [i1, i2, d20]; noncomm_ring

/-- `V₀V₁V₀V₁V₂ = h²·γ₀(h,0,0)·γ₂(0,−h⁻¹,h⁻²)` (cell (0, 2)). -/
theorem word_V0V1V0V1V2_two_photons (h : k) (hh : h ≠ 0) (s0 s1 s2 s3 : A)
    (h0 : s0 * s0 = h • s0 + 1) (h1 : s1 * s1 = h • s1 + 1) (h2 : s2 * s2 = h • s2 + 1)
    (c20 : s2 * s0 = s0 * s2) :
    (s0 * hinv h s1) * (s1 * hinv h s2) * (s0 * hinv h s1) * (s1 * hinv h s2) *
        (s2 * hinv h s3) =
      (h ^ 2) • (photon h h 0 0 s0 s1 * photon h 0 (-h⁻¹) (h⁻¹ ^ 2) s2 s3) := by
  rw [word_V0V1V0V1V2_reduces h s0 s1 s2 s3 h1 h2 c20, photon_twist_s h s0 s1 h0,
    photon_neg_pair h hh s2 s3, mul_smul_comm, smul_smul,
    show h ^ 2 * h⁻¹ ^ 2 = 1 by field_simp, one_smul]
  noncomm_ring

/-- `V₀V₁V₀V₁V₂ = h²·γ₂(0,−h⁻¹,h⁻²)·γ₀(h,0,0)` (cell (2, 0)): the two photons commute. -/
theorem word_V0V1V0V1V2_two_photons' (h : k) (hh : h ≠ 0) (s0 s1 s2 s3 : A)
    (h0 : s0 * s0 = h • s0 + 1) (h1 : s1 * s1 = h • s1 + 1) (h2 : s2 * s2 = h • s2 + 1)
    (c20 : s2 * s0 = s0 * s2) (c30 : s3 * s0 = s0 * s3) :
    (s0 * hinv h s1) * (s1 * hinv h s2) * (s0 * hinv h s1) * (s1 * hinv h s2) *
        (s2 * hinv h s3) =
      (h ^ 2) • (photon h 0 (-h⁻¹) (h⁻¹ ^ 2) s2 s3 * photon h h 0 0 s0 s1) := by
  rw [word_V0V1V0V1V2_reduces h s0 s1 s2 s3 h1 h2 c20, photon_twist_s h s0 s1 h0,
    photon_neg_pair h hh s2 s3, smul_mul_assoc, smul_smul,
    show h ^ 2 * h⁻¹ ^ 2 = 1 by field_simp, one_smul]
  have d2 : hinv h s2 * s0 = s0 * hinv h s2 := by
    unfold hinv; rw [sub_mul, mul_sub, c20, hb_mul, mul_hb]
  have d3 : hinv h s3 * s0 = s0 * hinv h s3 := by
    unfold hinv; rw [sub_mul, mul_sub, c30, hb_mul, mul_hb]
  have hc : Commute (hinv h s2 * hinv h s3) (s0 * s0) :=
    (((Commute.mul_right d2 d2)).mul_left (Commute.mul_right d3 d3))
  rw [mul_assoc (s0 * s0), ← hc.eq]

/-- `V₁V₂V₁V₂V₃ = σ₁²σ₃⁻¹σ₄⁻¹`. -/
theorem word_V1V2V1V2V3_reduces (h : k) (s1 s2 s3 s4 : A)
    (h2 : s2 * s2 = h • s2 + 1) (h3 : s3 * s3 = h • s3 + 1) (c31 : s3 * s1 = s1 * s3) :
    (s1 * hinv h s2) * (s2 * hinv h s3) * (s1 * hinv h s2) * (s2 * hinv h s3) *
        (s3 * hinv h s4) = s1 * s1 * hinv h s3 * hinv h s4 :=
  word_V0V1V0V1V2_reduces h s1 s2 s3 s4 h2 h3 c31

/-- `V₁V₂V₁V₂V₃ = h²·γ₀(0,h,0)·γ₃(0,−h⁻¹,h⁻²)` (cell (0, 3)). -/
theorem word_V1V2V1V2V3_two_photons_03 (h : k) (hh : h ≠ 0) (s0 s1 s2 s3 s4 : A)
    (h1 : s1 * s1 = h • s1 + 1) (h2 : s2 * s2 = h • s2 + 1) (h3 : s3 * s3 = h • s3 + 1)
    (c31 : s3 * s1 = s1 * s3) :
    (s1 * hinv h s2) * (s2 * hinv h s3) * (s1 * hinv h s2) * (s2 * hinv h s3) *
        (s3 * hinv h s4) =
      (h ^ 2) • (photon h 0 h 0 s0 s1 * photon h 0 (-h⁻¹) (h⁻¹ ^ 2) s3 s4) := by
  rw [word_V1V2V1V2V3_reduces h s1 s2 s3 s4 h2 h3 c31, photon_twist_t h s0 s1 h1,
    photon_neg_pair h hh s3 s4, mul_smul_comm, smul_smul,
    show h ^ 2 * h⁻¹ ^ 2 = 1 by field_simp, one_smul]
  noncomm_ring

/-- `V₁V₂V₁V₂V₃ = h²·γ₁(h,0,0)·γ₃(0,−h⁻¹,h⁻²)` (cell (1, 3)). -/
theorem word_V1V2V1V2V3_two_photons_13 (h : k) (hh : h ≠ 0) (s1 s2 s3 s4 : A)
    (h1 : s1 * s1 = h • s1 + 1) (h2 : s2 * s2 = h • s2 + 1) (h3 : s3 * s3 = h • s3 + 1)
    (c31 : s3 * s1 = s1 * s3) :
    (s1 * hinv h s2) * (s2 * hinv h s3) * (s1 * hinv h s2) * (s2 * hinv h s3) *
        (s3 * hinv h s4) =
      (h ^ 2) • (photon h h 0 0 s1 s2 * photon h 0 (-h⁻¹) (h⁻¹ ^ 2) s3 s4) := by
  rw [word_V1V2V1V2V3_reduces h s1 s2 s3 s4 h2 h3 c31, photon_twist_s h s1 s2 h1,
    photon_neg_pair h hh s3 s4, mul_smul_comm, smul_smul,
    show h ^ 2 * h⁻¹ ^ 2 = 1 by field_simp, one_smul]
  noncomm_ring

/-- Cells (3, 0) and (3, 1): `σ₁²` commutes with `σ₃⁻¹σ₄⁻¹`, so the order of the photons can be
swapped. -/
theorem word_V1V2V1V2V3_two_photons_swap (h : k) (hh : h ≠ 0) (s1 s2 s3 s4 : A)
    (h1 : s1 * s1 = h • s1 + 1) (h2 : s2 * s2 = h • s2 + 1) (h3 : s3 * s3 = h • s3 + 1)
    (c31 : s3 * s1 = s1 * s3) (c41 : s4 * s1 = s1 * s4) (s0 : A) :
    (s1 * hinv h s2) * (s2 * hinv h s3) * (s1 * hinv h s2) * (s2 * hinv h s3) *
        (s3 * hinv h s4) =
      (h ^ 2) • (photon h 0 (-h⁻¹) (h⁻¹ ^ 2) s3 s4 * photon h 0 h 0 s0 s1) ∧
    (s1 * hinv h s2) * (s2 * hinv h s3) * (s1 * hinv h s2) * (s2 * hinv h s3) *
        (s3 * hinv h s4) =
      (h ^ 2) • (photon h 0 (-h⁻¹) (h⁻¹ ^ 2) s3 s4 * photon h h 0 0 s1 s2) := by
  have d3 : hinv h s3 * s1 = s1 * hinv h s3 := by
    unfold hinv; rw [sub_mul, mul_sub, c31, hb_mul, mul_hb]
  have d4 : hinv h s4 * s1 = s1 * hinv h s4 := by
    unfold hinv; rw [sub_mul, mul_sub, c41, hb_mul, mul_hb]
  have hc : Commute (hinv h s3 * hinv h s4) (s1 * s1) :=
    (((Commute.mul_right d3 d3)).mul_left (Commute.mul_right d4 d4))
  have key : s1 * s1 * hinv h s3 * hinv h s4 = hinv h s3 * hinv h s4 * (s1 * s1) := by
    rw [mul_assoc (s1 * s1), ← hc.eq]
  rw [word_V1V2V1V2V3_reduces h s1 s2 s3 s4 h2 h3 c31, photon_twist_t h s0 s1 h1,
    photon_twist_s h s1 s2 h1, photon_neg_pair h hh s3 s4, smul_mul_assoc, smul_smul,
    show h ^ 2 * h⁻¹ ^ 2 = 1 by field_simp, one_smul, key]
  exact ⟨rfl, rfl⟩

end QOU.MassTheory.PhotonPairIdleFactor
