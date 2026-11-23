/-
# On the short nucleon difference, every Q_β functional reads one number

Bean `qou-99qc` (which functional is `ε` in `Q_β = |ε(Δ)|·E₀`). Mass-pipeline gap 5.

## Setting

The block model of `RightLineTraceObstruction.lean`: `Blk K = K × Mat₂(K) × K` holds the
trivial, `(2,1)` and sign blocks of `H₃(q)`, with generator images `S1`, `S2`. A
block-weighted trace is `τ_y = y₃·χ₍₃₎ + y₂₁·χ₍₂,₁₎ + y₁₁₁·χ₍₁³₎`. Put `h = q − q⁻¹`.

The short nucleon elements are the corpus's typed-crossing products
(`neutron-qvalue-symbolic`, `c5-involution-leibniz-decomposition-proof` §Step 2):

* proton  `𝓑_p = σ₁·(σ₂ − h/2)`,
* neutron `𝓑_n = (σ₁ − h/2)·(σ₂ − h)`,

and `Δ_S := 𝓑_n − 𝓑_p`.

## What this file proves

* `deltaS_eq`: `Δ_S = (h²/2)·1 − (h/2)(σ₁ + σ₂)`, the normal-form vector the census uses.
* Cited, not re-proved: `DeltaSIsWeakVertexSum.deltaS_eq_grading_sum` (PR #8068) gives
  `Δ_S = −(h[2]/4)(J₁ + J₂)` with `Jᵢ = (σᵢ + σᵢ⁻¹)/[2] = P_L − P_R`, and
  `deltaS_eq_weakVertex_sum` gives `Δ_S = −(q·h·[2]/4)(W₁ + W₂)` in any algebra. This file
  adds what those do not: the block characters and the trace reduction.
* `chi21_deltaS`: `χ₍₂,₁₎(Δ_S) = 0`, and `deltaS_sign`: the sign-block value is minus the
  trivial-block value.
* `tau_deltaS`: for EVERY block-weighted trace, `τ(Δ_S) = −(h[2]/2)·(y₃ − y₁₁₁)`.
* `tau_J1`, `tau_J2`: `τ(Jᵢ) = y₃ − y₁₁₁`. So `τ(Δ_S) = −(h[2]/2)·τ(J)`: on `Δ_S` the
  functional enters only through its chirality expectation `τ(P_L) − τ(P_R)`.
* `tau_deltaS_conventionD`: at the convention-D weights, `τ(J) = (q⁴+1)/(q²+1)²`.
* `abs_tau_deltaS_le`: over an ordered field, for every normalised trace with
  `y₁₁₁ = 0` and non-negative weights, `|τ(Δ_S)| ≤ |h[2]/2|`; the bound is the
  augmentation's value (`tau_deltaS_augmentation`).

Nothing here chooses a functional. The file shows that, on `Δ_S`, choosing `ε` is choosing
one number, `y₃ = τ(J)`, and that the two derived principles on record give `y₃ = 1`
(left-line support, `normalised_eq_augmentation`) and `y₃ = (q⁴+1)/(q²+1)²` (Markov at
`z_D`). Base ring (§7c): generic `[Field K]`; an ordered field only for the bound.
No `ℝ`. No `sorry`, no axiom.
-/
import QOU.QuarkState.RightLineTraceObstruction
import Mathlib.Algebra.Order.Field.Basic

namespace QOU.QuarkState.QBetaChiralityReduction

open QOU.QuarkState.RightLineTraceObstruction Matrix

section Field

variable {K : Type*} [Field K] {q : K}

/-- `h = q − q⁻¹`. -/
def hh (q : K) : K := q - q⁻¹

/-- `[2]_q = q + q⁻¹`. -/
def b2 (q : K) : K := q + q⁻¹

/-- The scalar `c·1` in the block ring. -/
def sc (c : K) : Blk K := (c, c • (1 : Matrix (Fin 2) (Fin 2) K), c)

/-- Proton, short model: `σ₁·(σ₂ − h/2)`. -/
noncomputable def Bp (q : K) : Blk K := S1 q * (S2 q - sc (hh q / 2))

/-- Neutron, short model: `(σ₁ − h/2)·(σ₂ − h)`. -/
noncomputable def Bn (q : K) : Blk K := (S1 q - sc (hh q / 2)) * (S2 q - sc (hh q))

/-- `Δ_S = 𝓑_n − 𝓑_p`. -/
noncomputable def deltaS (q : K) : Blk K := Bn q - Bp q

/-- The chirality grading of `σ₁`: `(σ₁ + σ₁⁻¹)/[2] = (2σ₁ − h)/[2]`. -/
noncomputable def J1 (q : K) : Blk K := (b2 q)⁻¹ • (2 • S1 q - sc (hh q))

/-- The chirality grading of `σ₂`. -/
noncomputable def J2 (q : K) : Blk K := (b2 q)⁻¹ • (2 • S2 q - sc (hh q))

theorem deltaS_eq (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) :
    deltaS q = sc (hh q ^ 2 / 2) - (hh q / 2) • (S1 q + S2 q) := by
  unfold deltaS Bn Bp sc S1 S2
  refine Prod.ext ?_ (Prod.ext ?_ ?_)
  · simp; field_simp; ring
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply, Matrix.vecMul, dotProduct] <;>
      field_simp <;> ring
  · simp; field_simp; ring

/-- The trivial-block value is `−h[2]/2`. -/
theorem deltaS_trivial (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) :
    (deltaS q).1 = -(hh q * b2 q / 2) := by
  rw [deltaS_eq h2 hq]
  simp [sc, S1, S2, hh, b2]
  field_simp
  ring

/-- The sign block sees minus the trivial block. -/
theorem deltaS_sign (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) : (deltaS q).2.2 = -(deltaS q).1 := by
  rw [deltaS_eq h2 hq]
  simp [sc, S1, S2, hh]
  field_simp
  ring

/-- The standard block does not see `Δ_S`: `χ₍₂,₁₎(Δ_S) = 0`. -/
theorem chi21_deltaS (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) : trace (deltaS q).2.1 = 0 := by
  rw [deltaS_eq h2 hq]
  simp [sc, S1, S2, hh, trace_fin_two]
  field_simp
  ring

/-- **Every block-weighted trace on `Δ_S`.** -/
theorem tau_deltaS (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) (y3 y21 y111 : K) :
    tau y3 y21 y111 (deltaS q) = -(hh q * b2 q / 2) * (y3 - y111) := by
  unfold tau
  rw [chi21_deltaS h2 hq, deltaS_sign h2 hq, deltaS_trivial h2 hq]
  ring

theorem tau_J1 (hq : q ≠ 0) (hq2 : b2 q ≠ 0) (y3 y21 y111 : K) :
    tau y3 y21 y111 (J1 q) = y3 - y111 := by
  have hb : 1 + q ^ 2 ≠ 0 := by
    intro h; apply hq2; unfold b2; field_simp; linear_combination h
  simp [tau, J1, sc, S1, hh, b2, trace_fin_two]
  field_simp
  have hx : (1 + q ^ 2)⁻¹ * (1 + q ^ 2) = 1 := inv_mul_cancel₀ hb
  linear_combination (y3 - y111) * hx

theorem tau_J2 (hq : q ≠ 0) (hq2 : b2 q ≠ 0) (y3 y21 y111 : K) :
    tau y3 y21 y111 (J2 q) = y3 - y111 := by
  have hb : 1 + q ^ 2 ≠ 0 := by
    intro h; apply hq2; unfold b2; field_simp; linear_combination h
  simp [tau, J2, sc, S2, hh, b2, trace_fin_two]
  field_simp
  have hx : (1 + q ^ 2)⁻¹ * (1 + q ^ 2) = 1 := inv_mul_cancel₀ hb
  linear_combination (y3 - y111) * hx

/-- **The reduction.** On `Δ_S` a trace enters only through its chirality expectation
`τ(J) = τ(P_L) − τ(P_R)`. -/
theorem tau_deltaS_eq_tau_J (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) (hq2 : b2 q ≠ 0)
    (y3 y21 y111 : K) :
    tau y3 y21 y111 (deltaS q) = -(hh q * b2 q / 2) * tau y3 y21 y111 (J1 q) := by
  rw [tau_deltaS h2 hq, tau_J1 hq hq2]

/-- The augmentation (`y₃ = 1`, other weights `0`). -/
theorem tau_deltaS_augmentation (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) :
    tau 1 0 0 (deltaS q) = -(hh q * b2 q / 2) := by
  rw [tau_deltaS h2 hq]; ring

/-- Convention D: `y₃ = (q⁴+1)/(q²+1)²`, `y₂₁ = q²/(q²+1)²`, `y₁₁₁ = 0`. -/
theorem tau_deltaS_conventionD (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) :
    tau ((q ^ 4 + 1) / (q ^ 2 + 1) ^ 2) (q ^ 2 / (q ^ 2 + 1) ^ 2) 0 (deltaS q) =
      -(hh q * b2 q / 2) * ((q ^ 4 + 1) / (q ^ 2 + 1) ^ 2) := by
  rw [tau_deltaS h2 hq]; ring

/-- The convention-D weights are normalised: `y₃ + 2y₂₁ = 1`. -/
theorem conventionD_normalised (hq2' : q ^ 2 + 1 ≠ 0) :
    (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 + 2 * (q ^ 2 / (q ^ 2 + 1) ^ 2) = 1 := by
  field_simp; ring

end Field

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {q : K}

/-- **The augmentation is the ceiling.** For a normalised trace with `y₁₁₁ = 0` and
non-negative weights, `|τ(Δ_S)| ≤ |h[2]/2|`. -/
theorem abs_tau_deltaS_le (hq : q ≠ 0) {y3 y21 : K} (h3 : 0 ≤ y3) (h21 : 0 ≤ y21)
    (hn : y3 + 2 * y21 = 1) :
    |tau y3 y21 0 (deltaS q)| ≤ |hh q * b2 q / 2| := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  rw [tau_deltaS h2 hq, sub_zero, abs_mul, abs_neg, abs_of_nonneg h3]
  have : y3 ≤ 1 := by linarith
  calc |hh q * b2 q / 2| * y3 ≤ |hh q * b2 q / 2| * 1 :=
        mul_le_mul_of_nonneg_left this (abs_nonneg _)
    _ = |hh q * b2 q / 2| := mul_one _

end Ordered

end QOU.QuarkState.QBetaChiralityReduction
