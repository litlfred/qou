/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import QOU.QBeta.FlavourWeightSplit
import QOU.Braiding.ColourFlavourMirror

/-!
# Pivotal Quantum-Trace Identity and Skew-Howe Mirror Invariance of `epsFlavourV3` (`qou-pdio`)

Formalizes the second half of `NF-P2` (bean `qou-pdio`) over a generic field `R` (§7c, zero `ℝ`,
zero empirical literals, zero `sorry`):

1. **Exact Reshetikhin–Turaev Pivotal Quantum-Trace Identity.**
   On `(R²)^{⊗ 3}` (`0 = u`, `1 = d`), the single-strand Cartan pivotal element `diag(q, q⁻¹)` has
   tensor-cube weight `pivotalCubeWeight q b₀ b₁ b₂`:
   - On all three `uud` (`T₃ = +1/2`) basis states `(0,0,1), (0,1,0), (1,0,0)`, `K^{⊗ 3}` acts by
     scalar `q` (`pivotalCubeWeight_uud`).
   - On all three `udd` (`T₃ = -1/2`) basis states `(0,1,1), (1,0,1), (1,1,0)`, `K^{⊗ 3}` acts by
     scalar `q⁻¹` (`pivotalCubeWeight_udd`).
   - Consequently, the normalized Reshetikhin–Turaev pivotal trace differences on `V³` satisfy
     `(trace (Kn q * borromeanV3B q) - trace (Kp q * borromeanV3A q)) / (q + q⁻¹)³ = epsFlavourV3 q`
     and `(q⁻¹ * trace (borromeanV3B q) - q * trace (borromeanV3A q)) / (q + q⁻¹)³ = epsFlavourV3 q`
     (`pivotal_trace_diff_eq_epsFlavourV3`, `pivotal_proton_minus_neutron_eq_neg_epsFlavourV3`),
     identifying `FlavourWeightSplit` directly with the pivotal/Nakayama quantum trace.

2. **Exact Skew-Howe Colour-Singlet Mirror Antisymmetry (`q ↦ -q⁻¹`).**
   In `ColourFlavourMirror` (`singlet_exterior_iff`), restricting `X = Ř_colour ⊗ B` to the `U_q(𝔤𝔩₃)`
   colour singlet `ε_q` induces the scalar twist `-q⁻¹ • B`, corresponding to the parameter mirror
   `q ↦ -q⁻¹` (which preserves `h = q - q⁻¹` while exchanging `(3) ↔ (1³)`). Because `fV3` depends
   only on `q²` and `q⁴`, `epsFlavourV3 (-q⁻¹) = epsFlavourV3 (q⁻¹) = -epsFlavourV3 q`
   (`epsFlavourV3_skewHowe_mirror`, `epsFlavourV3_sq_skewHowe_invariant`,
   `abs_epsFlavourV3_skewHowe_invariant`), leaving `|epsFlavourV3|` invariant.

-- Ref: [leitner2026] beans qou-pdio, qou-qzvs
-- Ref: [turaev2016] Quantum Invariants of Knots and 3-Manifolds, De Gruyter (pivotal quantum trace)
-/

namespace QOU.QBeta.FlavourWeightSplitPivotalSkewHowe

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.QBeta.FlavourWeightSplit
open QOU.Braiding.ColourFlavourMirror
open QOU.Braiding.JimboGl3Singlet

section GenericField

variable {R : Type*} [Field R]

/-- Single-strand pivotal Cartan weight `K = diag(q, q⁻¹)` on `Fin 2` (`0 = u`, `1 = d`). -/
def pivotalStrandWeight (q : R) (b : Fin 2) : R :=
  if b = 0 then q else q⁻¹

/-- Three-strand tensor-product pivotal weight `K^{⊗ 3}` on `(b₀, b₁, b₂) : Fin 2 × Fin 2 × Fin 2`. -/
def pivotalCubeWeight (q : R) (b₀ b₁ b₂ : Fin 2) : R :=
  pivotalStrandWeight q b₀ * pivotalStrandWeight q b₁ * pivotalStrandWeight q b₂

/-- **On all three `uud` (`T₃ = +1/2`) basis states, `K^{⊗ 3}` acts by scalar `q`.** -/
theorem pivotalCubeWeight_uud (q : R) (hq : q ≠ 0) :
    pivotalCubeWeight q 0 0 1 = q ∧
      pivotalCubeWeight q 0 1 0 = q ∧
      pivotalCubeWeight q 1 0 0 = q := by
  refine ⟨?_, ?_, ?_⟩ <;>
    simp [pivotalCubeWeight, pivotalStrandWeight, hq]

/-- **On all three `udd` (`T₃ = -1/2`) basis states, `K^{⊗ 3}` acts by scalar `q⁻¹`.** -/
theorem pivotalCubeWeight_udd (q : R) (hq : q ≠ 0) :
    pivotalCubeWeight q 0 1 1 = q⁻¹ ∧
      pivotalCubeWeight q 1 0 1 = q⁻¹ ∧
      pivotalCubeWeight q 1 1 0 = q⁻¹ := by
  refine ⟨?_, ?_, ?_⟩ <;>
    simp [pivotalCubeWeight, pivotalStrandWeight, hq]

/-- **`Tr(K^{⊗ 3} M)` on `W_p` equals `q · tr_{W_p}(M)`.** -/
theorem trace_Kp_mul (q : R) (M : Matrix (Fin 3) (Fin 3) R) :
    trace (Kp q * M) = q * trace M := by
  simp [Kp, trace_smul, smul_eq_mul]

/-- **`Tr(K^{⊗ 3} M)` on `W_n` equals `q⁻¹ · tr_{W_n}(M)`.** -/
theorem trace_Kn_mul (q : R) (M : Matrix (Fin 3) (Fin 3) R) :
    trace (Kn q * M) = q⁻¹ * trace M := by
  simp [Kn, trace_smul, smul_eq_mul]

/-- **Reshetikhin–Turaev pivotal quantum-trace identity (`udd - uud`):**
`(Tr_{W_n}(K^{⊗ 3} V³) - Tr_{W_p}(K^{⊗ 3} V³)) / (q + q⁻¹)³ = epsFlavourV3 q`. -/
theorem pivotal_trace_diff_eq_epsFlavourV3 (q : R) :
    (trace (Kn q * borromeanV3B q) - trace (Kp q * borromeanV3A q)) / (q + q⁻¹) ^ 3 =
      epsFlavourV3 q := by
  rw [trace_Kn_mul, trace_Kp_mul]
  unfold epsFlavourV3 epsN epsP qd2
  ring

/-- **Reshetikhin–Turaev pivotal quantum-trace identity (`uud - udd` sign convention):**
`(q · tr_{W_p}(V³) - q⁻¹ · tr_{W_n}(V³)) / (q + q⁻¹)³ = -epsFlavourV3 q`, and
`(q⁻¹ · tr_{W_n}(V³) - q · tr_{W_p}(V³)) / (q + q⁻¹)³ = epsFlavourV3 q`. -/
theorem pivotal_proton_minus_neutron_eq_neg_epsFlavourV3 (q : R) :
    (q * trace (borromeanV3A q) - q⁻¹ * trace (borromeanV3B q)) / (q + q⁻¹) ^ 3 =
      -epsFlavourV3 q ∧
    (q⁻¹ * trace (borromeanV3B q) - q * trace (borromeanV3A q)) / (q + q⁻¹) ^ 3 =
      epsFlavourV3 q := by
  unfold epsFlavourV3 epsN epsP qd2
  exact ⟨by ring, by ring⟩

/-- Skew-Howe parameter mirror `q ↦ -q⁻¹` preserves the Hecke linear parameter `h = q - q⁻¹`. -/
theorem heckeH_skewHowe_invariant (q : R) :
    (-q⁻¹) - (-q⁻¹)⁻¹ = q - q⁻¹ := by
  rw [inv_neg, inv_inv]
  ring

/-- Link to `ColourFlavourMirror`: on the colour singlet `pure (eps q) f`, the composite crossing
`X12 q B` acts on the flavour factor by `(-q⁻¹) • B f`. -/
theorem skewHowe_singlet_scalar_twist (q : R) (hq : q ≠ 0)
    {M : Type*} [AddCommGroup M] [Module R M] (B : M →ₗ[R] M) (f : M) :
    X12 q B (pure (eps q) f) = pure (eps q) ((-q⁻¹) • B f) :=
  X12_singlet q hq B f

/-- `polyP` is even, so `polyP (-q) = polyP q`. -/
theorem polyP_neg_arg (q : R) : polyP (-q) = polyP q := by
  unfold polyP
  ring

/-- `fV3` is even in the sign of its argument: `fV3 (-q) = fV3 q`. -/
theorem fV3_neg_arg (q : R) : fV3 (-q) = fV3 q := by
  unfold fV3
  rw [polyP_neg_arg]
  have h2 : (-q) ^ 2 = q ^ 2 := by ring
  have h4 : (-q) ^ 4 = q ^ 4 := by ring
  rw [h2, h4]

/-- **Skew-Howe colour-singlet mirror identity on `fV3`:** `fV3 (-q⁻¹) = -fV3 q`. -/
theorem fV3_skewHowe_mirror (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    fV3 (-q⁻¹) = -fV3 q := by
  rw [fV3_neg_arg, fV3_bar_odd q hq hq2]

/-- **Exact skew-Howe colour-singlet mirror antisymmetry (`q ↦ -q⁻¹`) on `epsFlavourV3`:**
`epsFlavourV3 (-q⁻¹) = -epsFlavourV3 q` over any field. -/
theorem epsFlavourV3_skewHowe_mirror (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    epsFlavourV3 (-q⁻¹) = -epsFlavourV3 q := by
  have hq' : -q⁻¹ ≠ 0 := neg_ne_zero.mpr (inv_ne_zero hq)
  have hq2' : (-q⁻¹) ^ 2 + 1 ≠ 0 := by
    intro h
    apply hq2
    have e : q ^ 2 * ((-q⁻¹) ^ 2 + 1) = 1 + q ^ 2 := by field_simp
    rw [h, mul_zero] at e
    linear_combination -e
  rw [epsFlavour_V3_eq (-q⁻¹) hq' hq2', epsFlavour_V3_eq q hq hq2, fV3_skewHowe_mirror q hq hq2]

/-- **Magnitude-squared invariance of `epsFlavourV3` under `q ↦ -q⁻¹` over any field.** -/
theorem epsFlavourV3_sq_skewHowe_invariant (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    epsFlavourV3 (-q⁻¹) ^ 2 = epsFlavourV3 q ^ 2 := by
  rw [epsFlavourV3_skewHowe_mirror q hq hq2, neg_sq]

end GenericField

section OrderedField

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Absolute-value invariance `|epsFlavourV3 (-q⁻¹)| = |epsFlavourV3 q|` over any ordered field.** -/
theorem abs_epsFlavourV3_skewHowe_invariant (q : K) (hq : q ≠ 0) :
    |epsFlavourV3 (-q⁻¹)| = |epsFlavourV3 q| := by
  have hq2 : q ^ 2 + 1 ≠ 0 := by
    have hsq : 0 ≤ q ^ 2 := sq_nonneg q
    linarith
  rw [epsFlavourV3_skewHowe_mirror q hq hq2, abs_neg]

end OrderedField

end QOU.QBeta.FlavourWeightSplitPivotalSkewHowe
