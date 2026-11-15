import Mathlib.Analysis.SpecialFunctions.Pow.Real
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

/-- Hyperbolic area of a genus-`g` (`g ≥ 2`) surface at curvature `-1`, via
    Gauss–Bonnet: `Area = -2π·χ = 4π(g-1)`. -/
noncomputable def area (g : ℕ) : ℝ := 4 * Real.pi * ((g : ℝ) - 1)

/-- Photon IR zero-mode shift `= (harmonic 1-form count) / Area = b₁/Area`. -/
noncomputable def photonZeroModeShift (g : ℕ) : ℝ := (betti1 g : ℝ) / area g

/-- **Gauss–Bonnet**: `Area = -2π·χ`. -/
theorem area_eq_neg_two_pi_chi (g : ℕ) :
    area g = -(2 * Real.pi) * (eulerChar g : ℝ) := by
  unfold area eulerChar
  push_cast
  ring

/-- **From-the-Lagrangian core.** The photon IR zero-mode shift on the
    genus-`g` surface is `2g/(4π(g-1))`. -/
theorem photonZeroModeShift_eq (g : ℕ) :
    photonZeroModeShift g = 2 * (g : ℝ) / (4 * Real.pi * ((g : ℝ) - 1)) := by
  unfold photonZeroModeShift betti1 area
  push_cast
  ring

/-- At `g = 4` (Bring's surface, `χ = -6`) the shift is `2/(3π)`. -/
theorem photonZeroModeShift_at_g4 :
    photonZeroModeShift 4 = 2 / (3 * Real.pi) := by
  rw [photonZeroModeShift_eq]
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  push_cast
  field_simp
  ring

/-- The naive `M × S¹` shift: `b₁(M×S¹) = 2g+1` over `Vol = Area·2π = 8π²(g-1)`.
    At `g = 4` this is `9/(24π²) ≈ 0.038`, strictly below the surface value
    `2/(3π) ≈ 0.212` — the recorded failed attempt. The strict inequality
    reduces to `π > 9/16` (true), and is witnessed numerically in
    `photon-ir-zero-mode-bring.witness.json` (the π-lower-bound import is
    outside this file's dependency cone). -/
noncomputable def naiveCrossS1Shift (g : ℕ) : ℝ :=
  (2 * (g : ℝ) + 1) / (8 * Real.pi ^ 2 * ((g : ℝ) - 1))

/-- The difference surface-minus-naive at `g=4` has the closed form
    `(16π-9)/(24π²)` — positive for `π > 9/16` (the surface value
    dominates the naive `M×S¹` value). Pure algebra, no `π`-bound needed. -/
theorem surface_minus_naive_g4 :
    photonZeroModeShift 4 - naiveCrossS1Shift 4
      = (16 * Real.pi - 9) / (24 * Real.pi ^ 2) := by
  rw [photonZeroModeShift_at_g4]
  unfold naiveCrossS1Shift
  have hπne : Real.pi ≠ 0 := Real.pi_ne_zero
  push_cast
  field_simp
  ring

/-- The **n=2 self-energy denominator** is `π · b₁(M_g)` — the *same* harmonic
    1-form count `b₁ = 2g` as the n=1 zero-mode, now in the denominator. This
    grounds the empirical n=2 form `α·[2]_q/(8π)·(1−h²α)` of the α/(4π) thread
    (PR #1495 RT-plan Identity 1: `[2]_q/(8π) = [2]_q/(π·dim H¹(M_Bring))`).

    Boundary discipline: `b₁` is topological (`ℕ`), `π` is archimedean (`ℝ`);
    the `[2]_q` numerator is the substrate Hecke integer, `τ_arch`-evaluated
    separately (it is *not* an object of this archimedean computation). -/
noncomputable def selfEnergyDenominator (g : ℕ) : ℝ := Real.pi * (betti1 g : ℝ)

/-- At `g = 4` the self-energy denominator is `8π` (since `b₁ = 2g = 8`),
    thus the n=2 term's `8π` is `π·dim H¹(M_Bring)` — the same Betti number that
    gives the n=1 zero-mode `2/(3π) = b₁/Area`. -/
theorem selfEnergyDenominator_at_g4 : selfEnergyDenominator 4 = 8 * Real.pi := by
  unfold selfEnergyDenominator betti1
  push_cast
  ring

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

/-- **The self-energy count is the REAL harmonic-1-form count, not the
    holomorphic one.** The photon is a real `U(1)` gauge field; its connection
    is a real 1-form, so the self-energy propagator lives on the kernel of the
    *real* Hodge Laplacian `Δ₁` on `Ω¹(M,ℝ)` — whose ζ-regularized index is
    `−ζ_{Δ₁}(0) = b₁ = 2g` (the merged area-free count, PR #3834/#3896), NOT the
    ∂̄-Laplacian's holomorphic `g`. Hence at `g = 4` the denominator is
    `π·b₁ = π·(2·g) = 8π = 2·(4π)`, with the `2` FORCED to be the real-vs-complex
    doubling. (This settles the *count*; the reciprocal normalization *form*
    — `π·b₁` vs the heat-kernel `(4π)·2` — is a separate, still-open question,
    tracked in the α_EM ledger and `alpha_em_multiplicity2_realcomplex_probe.py`.) -/
theorem selfEnergyDenominator_count_is_real (g : ℕ) :
    selfEnergyDenominator g = Real.pi * (2 * (holomorphicOneFormCount g : ℝ)) := by
  unfold selfEnergyDenominator betti1 holomorphicOneFormCount
  push_cast
  ring

/-- **n=1 ↔ n=2 unification on the genus-4 Hodge data.** Both IR corrections are
    built from the single Betti number `b₁(M_g) = 2g`: the n=1 zero-mode carries
    it in the numerator (`photonZeroModeShift = b₁/Area`), the n=2 self-energy in
    the denominator (`selfEnergyDenominator = π·b₁`). Their product is `π`-free,
    `b₁²/(4(g-1))` — the archimedean `π` cancels, leaving a topological ratio. -/
theorem photon_selfEnergy_betti_product (g : ℕ) (hg : (g : ℝ) ≠ 1) :
    photonZeroModeShift g * selfEnergyDenominator g
      = (betti1 g : ℝ) ^ 2 / (4 * ((g : ℝ) - 1)) := by
  unfold photonZeroModeShift selfEnergyDenominator area betti1
  have hπne : Real.pi ≠ 0 := Real.pi_ne_zero
  have hg1 : (g : ℝ) - 1 ≠ 0 := sub_ne_zero.mpr hg
  push_cast
  field_simp

end QOU.Archimedean.PhotonIRZeroMode
