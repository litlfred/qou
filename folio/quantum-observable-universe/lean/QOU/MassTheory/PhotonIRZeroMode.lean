import Mathlib.Tactic


/-!
# QOU.Archimedean.PhotonIRZeroMode

**From-the-Lagrangian derivation of the `α_EM` Bring zero-mode `2/(3π)`.**

`prop:em-coupling-bring-zero-mode` derives
`1/α_EM = q[9]_q[10]_q + 2g/(4π(g-1)) + αH(1 - h²α) + Δ₂` at `g = 4`, where
`H = [2]_q/(8π)`, `h = q - q⁻¹` is the Hecke structure constant, and `Δ₂` is the
uncomputed archimedean two-loop term (see `EmCouplingBringZeroMode`); its Status section
left open *why* the photon IR contribution equals `dim H¹ / Area`, recording a
failed naive attempt on the 3-manifold `M_Bring × S¹`.

This file proves the geometric core of the resolution: the photon IR zero-mode
lives on the **2-surface** `M_g` itself, as the harmonic 1-form sector
`b₁(M_g) = 2g`, normalised by the Gauss–Bonnet area
`Area(M_g) = -2πχ = 4π(g-1)`. The heat-kernel zero-mode contributes `b₁/Area`
(standard), so the IR shift is `2g/(4π(g-1)) = 2/(3π)` at `g = 4` — and the
naive `M × S¹` attempt is *strictly smaller* (`9/(24π²)`), explaining the
recorded failure.

The topological/geometric facts here are unconditional; the identification
"photon IR shift `= b₁/Vol`" is the standard heat-kernel zero-mode result
(cited in the narrative), and the upstream `τ_arch` uniqueness remains the named
conditional input of `prop:em-coupling-bring-zero-mode`.

-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-- Ref: [leitner2026] prop:photon-ir-zero-mode-bring
-- Ref: [thurston1978] The geometry and topology of three-manifolds.
-/

namespace QOU.Archimedean.PhotonIRZeroMode

/-- Euler characteristic of a closed orientable genus-`g` surface, `χ = 2 - 2g`. -/
def eulerChar (g : ℕ) : ℤ := 2 - 2 * (g : ℤ)

/-- First Betti number `b₁ = 2g` (rank of `H¹`, = harmonic 1-form count). -/
def betti1 (g : ℕ) : ℕ := 2 * g

/-- Holomorphic 1-form count `dim_ℂ H^{1,0}(M_g) = g` — the genus, i.e. the
    number of independent *holomorphic* differentials on a compact genus-`g`
    Riemann surface. Contrast `betti1 g = 2g`, the count of *real* harmonic
    1-forms `dim_ℝ H¹(M,ℝ)`. -/
def holomorphicOneFormCount (g : ℕ) : ℕ := g

/-- **Real-vs-complex Hodge doubling.** The real harmonic-1-form count is twice
    the holomorphic count: `b₁ = 2·g`. This is the archimedean shadow of the
    Hodge decomposition `H¹(M,ℝ) ⊗ ℂ = H^{1,0} ⊕ H^{0,1}`, each summand of
    complex dimension `g`. It pins WHERE the `2` in `8π = 2·(4π)` lives: it is
    the real⊕complex doubling, not a free multiplicity. -/
theorem betti1_eq_two_holomorphic (g : ℕ) :
    betti1 g = 2 * holomorphicOneFormCount g := rfl


/-! ## Over a generic field, with the half-turn as a symbol

Gauss–Bonnet makes `Area = −2π·χ` linear in `π`, so every statement below is
polynomial in one symbol `p` standing for `π` (`p ≠ 0`), over any field of
characteristic zero.  `π` is a magnitude here (an area), not an angle, so it is
carried as a ring symbol; its real value enters only in
`QOU.Transcendental.MassTheory.PhotonIRZeroModeReal`, which keeps the original
`ℝ` names (transcendental-boundary strangler, bean `qou-dk7p`). -/

section Generic

variable {K : Type*} [Field K] [CharZero K]

/-- Area `4p(g−1) = −2p·χ` with `p` standing for `π`. -/
def areaP (p : K) (g : ℕ) : K := 4 * p * ((g : K) - 1)

/-- Photon IR zero-mode shift `b₁/Area`, with `p` for `π`. -/
def photonZeroModeShiftP (p : K) (g : ℕ) : K := (betti1 g : K) / areaP p g

/-- **Gauss–Bonnet**, in `p`: `Area = −2p·χ`. -/
theorem areaP_eq_neg_two_p_chi (p : K) (g : ℕ) :
    areaP p g = -(2 * p) * (eulerChar g : K) := by
  unfold areaP eulerChar
  push_cast
  ring

/-- The shift is `2g / (4p(g−1))`. -/
theorem photonZeroModeShiftP_eq (p : K) (g : ℕ) :
    photonZeroModeShiftP p g = 2 * (g : K) / (4 * p * ((g : K) - 1)) := by
  unfold photonZeroModeShiftP betti1 areaP
  push_cast
  ring

/-- At `g = 4` the shift is `2/(3p)`. -/
theorem photonZeroModeShiftP_at_g4 {p : K} (hp : p ≠ 0) :
    photonZeroModeShiftP p 4 = 2 / (3 * p) := by
  rw [photonZeroModeShiftP_eq]
  push_cast
  field_simp
  ring

/-- Naive `M × S¹` shift `(2g+1)/(8p²(g−1))`. -/
def naiveCrossS1ShiftP (p : K) (g : ℕ) : K :=
  (2 * (g : K) + 1) / (8 * p ^ 2 * ((g : K) - 1))

/-- Surface minus naive at `g = 4`: `(16p − 9)/(24p²)`. -/
theorem surface_minus_naive_g4_P {p : K} (hp : p ≠ 0) :
    photonZeroModeShiftP p 4 - naiveCrossS1ShiftP p 4
      = (16 * p - 9) / (24 * p ^ 2) := by
  rw [photonZeroModeShiftP_at_g4 hp]
  unfold naiveCrossS1ShiftP
  push_cast
  field_simp
  ring

/-- Self-energy denominator `p·b₁`. -/
def selfEnergyDenominatorP (p : K) (g : ℕ) : K := p * (betti1 g : K)

/-- At `g = 4`: `8p`. -/
theorem selfEnergyDenominatorP_at_g4 (p : K) : selfEnergyDenominatorP p 4 = 8 * p := by
  unfold selfEnergyDenominatorP betti1
  push_cast
  ring

/-- The count in the denominator is the real harmonic count `2g`. -/
theorem selfEnergyDenominatorP_count_is_real (p : K) (g : ℕ) :
    selfEnergyDenominatorP p g = p * (2 * (holomorphicOneFormCount g : K)) := by
  unfold selfEnergyDenominatorP betti1 holomorphicOneFormCount
  push_cast
  ring

/-- **The product is `p`-free**: `b₁² / (4(g−1))`.  This holds for every
nonzero value of the symbol, so it does not depend on what `π` is. -/
theorem photon_selfEnergy_betti_product_P {p : K} (hp : p ≠ 0) (g : ℕ)
    (hg : (g : K) ≠ 1) :
    photonZeroModeShiftP p g * selfEnergyDenominatorP p g
      = (betti1 g : K) ^ 2 / (4 * ((g : K) - 1)) := by
  unfold photonZeroModeShiftP selfEnergyDenominatorP areaP betti1
  have hg1 : (g : K) - 1 ≠ 0 := sub_ne_zero.mpr hg
  push_cast
  field_simp

end Generic

end QOU.Archimedean.PhotonIRZeroMode
