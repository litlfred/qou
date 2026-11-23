/-
# What fixes the photon's colour weights `φ₀, φ₁`?

Bean `qou-99qc` (entry 2026-11-20). `def:photon` is
`γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` (`QOU.Photon.photon`). The corpus fixes only
the vertex weights of the Borromean pair, `β_Bor = V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)`
(`prop:borromean-two-photon-factorisation`). This file tests, in the normal-form
algebra of `H₃(q)` over a generic commutative ring, which candidate constraints
force `φ₀, φ₁`. Coordinates are those of `pairNFChiral_eq`: basis
`1, σ₀, σ₁, L₋ = σ₁σ₀, L₊ = σ₀σ₁, e⁻ = σ₀σ₁σ₀`; the first photon has weights
`(a0, a1, a2) = (φ₀, φ₁, φ₀₁)`, the second `(b0, b1, b2) = (ψ₀, ψ₁, ψ₀₁)`.

## Results

* `borromean_pair_nf`: `NF(β_Bor) = [1 − h⁴, −h³ − h⁵, h³, −h², h² + h⁴, 0]`.
  Its `e⁻` coordinate is `0`, so **every** factorisation `γ(φ)γ(ψ) = β_Bor` has
  zero electron channel `φ₀₁ψ₀ + φ₁ψ₀₁` (`FactorsBorromean.eChannel_eq_zero`).
  A γγ → e⁻ amplitude cannot come from a factorisation of `β_Bor`, whatever `φ`.
* **(d) The factorisation alone does not force `φ₀ = φ₁ = 0`.** The system is six
  equations in six unknowns. Measured (not proved here, see
  `computations/probes/photon_colour_weights_solution_set_probe.py`): at
  `h = 1/2` and `h = 2/9` it has 8 solutions over `ℂ`; 2 are the Borromean pair in
  its two orders, 6 have `φ₀, φ₁ ≠ 0`. What is proved: inside the solution set,
  `φ₁ = 0 ⟺ ψ₀ = 0` (`FactorsBorromean.phi1_eq_zero_iff`), and either one forces
  the Borromean pair exactly (`FactorsBorromean.borromean_of_phi1_eq_zero`,
  `…vertex_weights`).
* **Bar-closure forces the Borromean pair** (`borromean_of_barClosed`). If both
  photons satisfy `φ₀ + φ₁ = 0`, the factorisation forces `φ₀ = φ₁ = ψ₀ = ψ₁ = 0`
  and `{φ₀₁, ψ₀₁} = {qh, −q⁻¹h}` (needs `h ≠ 0`, `h² + 2 ≠ 0`, a domain).
  The condition `φ₀ + φ₁ = 0` is exactly what makes the bar image
  `1 + φ̄₀σ₀⁻¹ + φ̄₁σ₁⁻¹ + φ̄₀₁σ₀⁻¹σ₁` of a photon a photon again
  (`barImage_isPhoton_iff`), and also what makes the image under
  `σ₀ ↦ σ₁⁻¹, σ₁ ↦ σ₀⁻¹` (which fixes `V`) a photon (`thetaImage_isPhoton_iff`).
  Whether "the bar image of a photon is a photon" is a corpus premise is an owner
  decision (bean `qou-99qc`). Under it the `e⁻` channel of two photons is the
  determinant `φ₀₁ψ₀ − φ₀ψ₀₁` (`eChannel_barClosed`).
* **(b) Flip symmetry kills the vertex.** Conjugation by `Δ = σ₀σ₁σ₀` swaps
  `σ₀ ↔ σ₁` (`delta_mul_s0`, `delta_mul_s1`). The flip image of `γ(φ)` is a photon
  iff `φ₀₁ = 0` (`flipImage_isPhoton_iff`), and two three-term photons
  (`φ₀₁ = ψ₀₁ = 0`) never factor `β_Bor` (`not_factors_of_threeTerm`, certificate
  `h²(h² + 2) = 0`). So flip-closure is incompatible with the Borromean pair.
* **(c) Neutral in both one-dimensional blocks kills the vertex.** On a photon the
  trivial character is `1 + q(φ₀ + φ₁) + φ₀₁` and the sign character
  `1 − q⁻¹(φ₀ + φ₁) + φ₀₁` (`charTriv_photon`, `charSign_photon`). Both equal to
  `1` forces `φ₀₁ = 0` and `φ₀ + φ₁ = 0` (`neutral_forces`), hence again no
  factorisation of `β_Bor`.

Base ring (§7c): generic `[CommRing R]`; the cancellation steps need
`[IsDomain R]`. No `ℝ`, no ordering.

-- Ref: [iwahori1964] https://doi.org/10.15083/00039809
-- Ref: [leitner2026] predicted-spectra, def:photon; prop:borromean-two-photon-factorisation
-/
import QOU.QuarkState.PhotonPairNormalForm

namespace QOU.QuarkState.PhotonColourWeights

open QOU.Machinery.H3
open QOU.QuarkState

variable {R : Type*} [CommRing R]

/-! ## The Borromean braid in normal form -/

/-- `NF(β_Bor)` with `β_Bor = (σ₀σ₁⁻¹)³`, as a function of `h` alone. -/
def borromeanNF (h : R) : Fin 6 → R := ![1 - h ^ 4, -h ^ 3 - h ^ 5, h ^ 3, -h ^ 2, h ^ 2 + h ^ 4, 0]

/-- The Borromean pair `γ(0,0,qh)·γ(0,0,−q⁻¹h)` has normal form `borromeanNF h`. -/
theorem borromean_pair_nf (h q q' : R) (hh : q - q' = h) (hq : q * q' = 1) :
    pairNFChiral h 0 0 (q * h) 0 0 (-(q' * h)) = borromeanNF h := by
  rw [pairNFChiral_eq]
  funext i
  fin_cases i <;> simp [borromeanNF]
  · linear_combination (-h ^ 4) * hq
  · linear_combination (-h ^ 2) * hh + (-h ^ 5) * hq
  · linear_combination (h ^ 3) * hq
  · linear_combination (h ^ 2) * hq
  · linear_combination h * hh + (h ^ 4) * hq

/-- The other order: the two Borromean photons commute. -/
theorem borromean_pair_nf_swap (h q q' : R) (hh : q - q' = h) (hq : q * q' = 1) :
    pairNFChiral h 0 0 (-(q' * h)) 0 0 (q * h) = borromeanNF h := by
  rw [pairNFChiral_eq]
  funext i
  fin_cases i <;> simp [borromeanNF]
  · linear_combination (-h ^ 4) * hq
  · linear_combination (-h ^ 2) * hh + (-h ^ 5) * hq
  · linear_combination (h ^ 3) * hq
  · linear_combination (h ^ 2) * hq
  · linear_combination h * hh + (h ^ 4) * hq

/-- `γ(φ)·γ(ψ) = β_Bor` in `H₃(q)`. -/
def FactorsBorromean (h a0 a1 a2 b0 b1 b2 : R) : Prop :=
  pairNFChiral h a0 a1 a2 b0 b1 b2 = borromeanNF h

variable {h a0 a1 a2 b0 b1 b2 : R}

/-- The six coordinate equations of a factorisation. -/
theorem FactorsBorromean.eqs (H : FactorsBorromean h a0 a1 a2 b0 b1 b2) :
    1 + a0 * b0 + a1 * b1 - h * (a0 * b2 + a2 * b0) + h ^ 2 * (a2 * b2) = 1 - h ^ 4 ∧
    a0 + b0 + h * a0 * b0 + a2 * b1 - h * (a2 + b2) - h ^ 2 * (a0 * b2 + a2 * b0)
      + h ^ 3 * (a2 * b2) = -h ^ 3 - h ^ 5 ∧
    a1 + b1 + h * a1 * b1 + a0 * b2 - h * (a2 * b2) = h ^ 3 ∧
    a1 * b0 + a2 * b2 - h * (a1 * b2) = -h ^ 2 ∧
    a2 + b2 + a0 * b1 + h * (a0 * b2) - h ^ 2 * (a2 * b2) = h ^ 2 + h ^ 4 ∧
    a2 * b0 + a1 * b2 = 0 := by
  have H' := congrFun H
  unfold FactorsBorromean at H
  rw [pairNFChiral_eq] at H'
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · simpa [borromeanNF] using H' 0
  · simpa [borromeanNF] using H' 1
  · simpa [borromeanNF] using H' 2
  · simpa [borromeanNF] using H' 3
  · simpa [borromeanNF] using H' 4
  · simpa [borromeanNF] using H' 5

/-- **No electron in any factorisation of `β_Bor`.** The `e⁻ = σ₀σ₁σ₀` coordinate
of `γ(φ)γ(ψ)` is `φ₀₁ψ₀ + φ₁ψ₀₁`, and `β_Bor` has none. -/
theorem FactorsBorromean.eChannel_eq_zero (H : FactorsBorromean h a0 a1 a2 b0 b1 b2) :
    a2 * b0 + a1 * b2 = 0 :=
  H.eqs.2.2.2.2.2

section Domain

variable [IsDomain R]

/-- Inside the solution set, `φ₁ = 0 ⟺ ψ₀ = 0`. -/
theorem FactorsBorromean.phi1_eq_zero_iff (hh0 : h ≠ 0)
    (H : FactorsBorromean h a0 a1 a2 b0 b1 b2) : a1 = 0 ↔ b0 = 0 := by
  obtain ⟨-, -, -, e3, -, e5⟩ := H.eqs
  have hh2 : h ^ 2 ≠ 0 := pow_ne_zero 2 hh0
  constructor
  · intro ha1
    subst ha1
    have ha2 : a2 ≠ 0 := by
      rintro rfl; apply hh2; linear_combination e3
    have : a2 * b0 = 0 := by linear_combination e5
    exact (mul_eq_zero.mp this).resolve_left ha2
  · intro hb0
    subst hb0
    have hb2 : b2 ≠ 0 := by
      rintro rfl; apply hh2; linear_combination e3
    have : a1 * b2 = 0 := by linear_combination e5
    exact (mul_eq_zero.mp this).resolve_right hb2

/-- **`φ₁ = 0` forces the Borromean pair.** With one weight of the first photon
zero, every other weight is fixed: `φ₀ = ψ₀ = ψ₁ = 0`, and the vertex weights are
the two roots of `t² − h²t − h² = 0`. -/
theorem FactorsBorromean.borromean_of_phi1_eq_zero (hh0 : h ≠ 0)
    (H : FactorsBorromean h a0 a1 a2 b0 b1 b2) (ha1 : a1 = 0) :
    a0 = 0 ∧ b0 = 0 ∧ b1 = 0 ∧ a2 + b2 = h ^ 2 ∧ a2 * b2 = -h ^ 2 := by
  have hb0 := (H.phi1_eq_zero_iff hh0).mp ha1
  obtain ⟨e0, -, e2, e3, e4, -⟩ := H.eqs
  subst ha1; subst hb0
  have hprod : a2 * b2 = -h ^ 2 := by linear_combination e3
  have hb2 : b2 ≠ 0 := by
    rintro rfl; apply pow_ne_zero 2 hh0; linear_combination hprod
  have h1 : h * (a0 * b2) = 0 := by linear_combination -e0 + h ^ 2 * hprod
  have ha0 : a0 = 0 :=
    (mul_eq_zero.mp ((mul_eq_zero.mp h1).resolve_left hh0)).resolve_right hb2
  subst ha0
  have hb1 : b1 = 0 := by linear_combination e2 + h * hprod
  subst hb1
  exact ⟨rfl, rfl, rfl, by linear_combination e4 + h ^ 2 * hprod, hprod⟩

/-- The vertex weights of `borromean_of_phi1_eq_zero` are `qh` and `−q⁻¹h`. -/
theorem FactorsBorromean.vertex_weights (hh0 : h ≠ 0) {q q' : R} (hh : q - q' = h)
    (hq : q * q' = 1) (H : FactorsBorromean h a0 a1 a2 b0 b1 b2) (ha1 : a1 = 0) :
    (a2 = q * h ∧ b2 = -(q' * h)) ∨ (a2 = -(q' * h) ∧ b2 = q * h) := by
  obtain ⟨-, -, -, hs, hp⟩ := H.borromean_of_phi1_eq_zero hh0 ha1
  have hb2 : b2 = h ^ 2 - a2 := by linear_combination hs
  have key : (a2 - q * h) * (a2 + q' * h) = 0 := by
    linear_combination a2 * hs - hp - (h * a2) * hh - h ^ 2 * hq
  rcases mul_eq_zero.mp key with k | k
  · left
    refine ⟨by linear_combination k, ?_⟩
    rw [hb2]; linear_combination -k - h * hh
  · right
    refine ⟨by linear_combination k, ?_⟩
    rw [hb2]; linear_combination -k - h * hh

end Domain

/-! ## Bar image and the `V`-fixing anti-involution -/

/-- `σ₀⁻¹σ₁ = σ₀σ₁ − hσ₁`. -/
theorem s0inv_mul_s1 (h : R) : mulNF h (s0 - h • e0) s1 = ![0, 0, -h, 0, 1, 0] := by
  funext i; fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, s0, s1, e0]

/-- `V = σ₀σ₁⁻¹ = σ₀σ₁ − hσ₀`. -/
theorem vertexNF (h : R) : mulNF h s0 (s1 - h • e0) = ![0, -h, 0, 0, 1, 0] := by
  funext i; fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, s0, s1, e0]

/-- An NF vector is a photon iff its support is in `{1, σ₀, σ₁, L₊}` and its unit
coordinate is `1`. -/
def IsPhoton (x : Fin 6 → R) : Prop := x 0 = 1 ∧ x 3 = 0 ∧ x 5 = 0

theorem isPhoton_iff_exists (h : R) (x : Fin 6 → R) :
    IsPhoton x ↔ ∃ c0 c1 c2 : R, x = photon h c0 c1 c2 := by
  constructor
  · rintro ⟨h0, h3, h5⟩
    refine ⟨x 1 + h * x 4, x 2, x 4, ?_⟩
    rw [photon_eq]; funext i; fin_cases i <;> simp [h0, h3, h5]
  · rintro ⟨c0, c1, c2, rfl⟩
    rw [photon_eq]; simp [IsPhoton]

/-- The bar image `1 + c₀σ₀⁻¹ + c₁σ₁⁻¹ + c₂σ₀⁻¹σ₁` of a photon, with `cᵢ` the
barred weights `φ̄ᵢ` (bar: `σᵢ ↦ σᵢ⁻¹`, `q ↦ q⁻¹`; a ring automorphism of the
ground ring, so `c₀ + c₁ = 0 ⟺ φ₀ + φ₁ = 0`). -/
def barImage (h c0 c1 c2 : R) : Fin 6 → R :=
  e0 + c0 • (s0 - h • e0) + c1 • (s1 - h • e0) + c2 • mulNF h (s0 - h • e0) s1

theorem barImage_eq (h c0 c1 c2 : R) :
    barImage h c0 c1 c2 = ![1 - h * (c0 + c1), c0, c1 - h * c2, 0, c2, 0] := by
  rw [barImage, s0inv_mul_s1]
  funext i; fin_cases i <;> simp [e0, s0, s1] <;> ring

/-- **Bar-closure.** The bar image of a photon is a photon iff `c₀ + c₁ = 0`
(`h` a non-zero-divisor). -/
theorem barImage_isPhoton_iff (h c0 c1 c2 : R) (hreg : ∀ x : R, h * x = 0 → x = 0) :
    IsPhoton (barImage h c0 c1 c2) ↔ c0 + c1 = 0 := by
  rw [barImage_eq]
  simp only [IsPhoton]
  constructor
  · rintro ⟨h0, -, -⟩
    exact hreg _ (by simpa using (by simpa using h0 : 1 - h * (c0 + c1) = 1))
  · intro hc; simp [hc]

/-- The image under the anti-involution `θ : σ₀ ↦ σ₁⁻¹, σ₁ ↦ σ₀⁻¹` (reversing
products, barring scalars), which fixes `V`: `θ(γ(φ)) = 1 + φ̄₀σ₁⁻¹ + φ̄₁σ₀⁻¹ + φ̄₀₁V`. -/
def thetaImage (h c0 c1 c2 : R) : Fin 6 → R :=
  e0 + c0 • (s1 - h • e0) + c1 • (s0 - h • e0) + c2 • mulNF h s0 (s1 - h • e0)

theorem thetaImage_eq (h c0 c1 c2 : R) :
    thetaImage h c0 c1 c2 = ![1 - h * (c0 + c1), c1 - h * c2, c0, 0, c2, 0] := by
  rw [thetaImage, vertexNF]
  funext i; fin_cases i <;> simp [e0, s0, s1] <;> ring

theorem thetaImage_isPhoton_iff (h c0 c1 c2 : R) (hreg : ∀ x : R, h * x = 0 → x = 0) :
    IsPhoton (thetaImage h c0 c1 c2) ↔ c0 + c1 = 0 := by
  rw [thetaImage_eq]
  simp only [IsPhoton]
  constructor
  · rintro ⟨h0, -, -⟩
    exact hreg _ (by simpa using (by simpa using h0 : 1 - h * (c0 + c1) = 1))
  · intro hc; simp [hc]

/-- On a pure-vertex photon `θ` acts by barring the vertex weight only:
`θ(γ(0,0,c)) = γ(0,0,c̄)`. With `c = qh`, `c̄ = q⁻¹(−h)`: `θ` swaps the two
Borromean photons. -/
theorem thetaImage_vertex (h c : R) : thetaImage h 0 0 c = photon h 0 0 c := by
  rw [thetaImage_eq, photon_eq]; funext i; fin_cases i <;> simp

/-- **Bar-closed pairs: the `e⁻` channel is a determinant.** -/
theorem eChannel_barClosed (h a0 a1 a2 b0 b1 b2 : R) (ha : a0 + a1 = 0)
    (hb : b0 + b1 = 0) :
    pairNFChiral h a0 a1 a2 b0 b1 b2 5 = a2 * b0 - a0 * b2 := by
  rw [pairNFChiral_eq]; simp
  linear_combination b2 * ha

/-- For two identical photons the `e⁻` channel is `φ₀₁(φ₀ + φ₁)`. -/
theorem eChannel_identical (h a0 a1 a2 : R) :
    pairNFChiral h a0 a1 a2 a0 a1 a2 5 = a2 * (a0 + a1) := by
  rw [pairNFChiral_eq]; simp; ring

/-- **Bar-closure + factorisation ⇒ the Borromean pair.** -/
theorem borromean_of_barClosed [IsDomain R] (hh0 : h ≠ 0) (hh2 : h ^ 2 + 2 ≠ 0)
    (H : FactorsBorromean h a0 a1 a2 b0 b1 b2) (ha : a0 + a1 = 0) (hb : b0 + b1 = 0) :
    a1 = 0 := by
  obtain ⟨e0, -, e2, e3, e4, e5⟩ := H.eqs
  have ha1 : a1 = -a0 := by linear_combination ha
  have hb1 : b1 = -b0 := by linear_combination hb
  subst ha1; subst hb1
  -- (h² + 2)·a0·(b0 − h·b2) = 0
  have key : (h ^ 2 + 2) * (a0 * (b0 - h * b2)) = 0 := by
    linear_combination e0 - h ^ 2 * e3 + h * e5
  rcases mul_eq_zero.mp ((mul_eq_zero.mp key).resolve_left hh2) with k | k
  · subst k; simp
  · have hb0 : b0 = h * b2 := by linear_combination k
    subst hb0
    have k2 : b2 * (h * a2 - a0) = 0 := by linear_combination e5
    rcases mul_eq_zero.mp k2 with k3 | k3
    · subst k3
      have : -a0 = (0 : R) := (H.phi1_eq_zero_iff hh0).mpr (by simp)
      simpa using this
    · have ha0 : a0 = h * a2 := by linear_combination -k3
      subst ha0
      exfalso
      have : h ^ 3 * (h ^ 2 + 2) = 0 := by
        linear_combination -e2 - h * e4
      rcases mul_eq_zero.mp this with k4 | k4
      · exact hh0 (pow_eq_zero_iff (by norm_num) |>.mp k4)
      · exact hh2 k4

/-! ## Flip symmetry `σ₀ ↔ σ₁` (conjugation by `Δ = σ₀σ₁σ₀`) -/

/-- `Δ = σ₀σ₁σ₀` as an NF vector. -/
def delta : Fin 6 → R := ![0, 0, 0, 0, 0, 1]

theorem delta_mul_s0 (h : R) : mulNF h delta s0 = mulNF h s1 delta := by
  funext i; fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, s0, s1, delta]

theorem delta_mul_s1 (h : R) : mulNF h delta s1 = mulNF h s0 delta := by
  funext i; fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, s0, s1, delta]

/-- The flip image `1 + φ₀σ₁ + φ₁σ₀ + φ₀₁σ₁σ₀⁻¹` of `γ(φ)`. -/
def flipImage (h a0 a1 a2 : R) : Fin 6 → R :=
  e0 + a0 • s1 + a1 • s0 + a2 • mulNF h s1 (s0 - h • e0)

theorem flipImage_eq (h a0 a1 a2 : R) :
    flipImage h a0 a1 a2 = ![1, a1, a0 - h * a2, a2, 0, 0] := by
  funext i; fin_cases i <;> simp [flipImage, mulNF, mulσ₀, mulσ₁, e0, s0, s1] <;> ring

/-- The flip image is a photon iff the vertex weight is zero. -/
theorem flipImage_isPhoton_iff (h a0 a1 a2 : R) :
    IsPhoton (flipImage h a0 a1 a2) ↔ a2 = 0 := by
  rw [flipImage_eq]; simp [IsPhoton]

/-- **Three-term photons never factor `β_Bor`** (`h ≠ 0`, `h² + 2 ≠ 0`). -/
theorem not_factors_of_threeTerm [IsDomain R] (hh0 : h ≠ 0) (hh2 : h ^ 2 + 2 ≠ 0) :
    ¬ FactorsBorromean h a0 a1 0 b0 b1 0 := by
  intro H
  obtain ⟨e0, e1, e2, e3, e4, -⟩ := H.eqs
  have : h ^ 2 * (h ^ 2 + 2) = 0 := by
    linear_combination (-a1) * e1 + a0 * e2 + (a0 * h + 1) * e3 + (-a1 * h - 1) * e4
      + 0 * e0
  rcases mul_eq_zero.mp this with k | k
  · exact hh0 (pow_eq_zero_iff (by norm_num) |>.mp k)
  · exact hh2 k

/-! ## Neutrality in the two one-dimensional blocks -/

/-- Trivial character on NF vectors: `σᵢ ↦ q`. -/
def charTriv (q : R) (x : Fin 6 → R) : R :=
  x 0 + q * (x 1 + x 2) + q ^ 2 * (x 3 + x 4) + q ^ 3 * x 5

/-- Sign character on NF vectors: `σᵢ ↦ −q⁻¹` (`q' = q⁻¹`). -/
def charSign (q' : R) (x : Fin 6 → R) : R :=
  x 0 - q' * (x 1 + x 2) + q' ^ 2 * (x 3 + x 4) - q' ^ 3 * x 5

theorem charTriv_photon {q q' : R} (hh : q - q' = h) (hq : q * q' = 1) (c0 c1 c2 : R) :
    charTriv q (photon h c0 c1 c2) = 1 + q * (c0 + c1) + c2 := by
  rw [photon_eq]; simp [charTriv]
  linear_combination (q * c2) * hh + c2 * hq

theorem charSign_photon {q q' : R} (hh : q - q' = h) (hq : q * q' = 1) (c0 c1 c2 : R) :
    charSign q' (photon h c0 c1 c2) = 1 - q' * (c0 + c1) + c2 := by
  rw [photon_eq]; simp [charSign]
  linear_combination (-(q' * c2)) * hh + c2 * hq

/-- **Neutral in both one-dimensional blocks ⇒ no vertex, and `φ₀ + φ₁ = 0`**
(`q + q⁻¹` a non-zero-divisor). -/
theorem neutral_forces {q q' : R} (hh : q - q' = h) (hq : q * q' = 1)
    (hreg : ∀ x : R, (q + q') * x = 0 → x = 0) (c0 c1 c2 : R)
    (ht : charTriv q (photon h c0 c1 c2) = 1) (hs : charSign q' (photon h c0 c1 c2) = 1) :
    c0 + c1 = 0 ∧ c2 = 0 := by
  rw [charTriv_photon hh hq] at ht
  rw [charSign_photon hh hq] at hs
  have hsum : c0 + c1 = 0 := hreg _ (by linear_combination ht - hs)
  exact ⟨hsum, by linear_combination ht - q * hsum⟩

end QOU.QuarkState.PhotonColourWeights
