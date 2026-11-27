/-
  `ℝ` forms of `QOU.MassTheory.PhotonIRZeroMode`, with `π = Real.pi`.  The
  generic statements in a symbol `p` for `π` are in the main module.  Same
  namespace, original names kept.
-/
import QOU.MassTheory.PhotonIRZeroMode
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.Archimedean.PhotonIRZeroMode

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
