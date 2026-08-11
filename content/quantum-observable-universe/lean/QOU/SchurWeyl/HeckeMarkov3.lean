import QOU.SchurWeyl.HoefsmitRep
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# QOU.SchurWeyl.HeckeMarkov3 — the weighted-character (Markov) trace on `H_3(q)` (SW-8, n=3)

Under the Wedderburn iso `H_3(q) ≅ ℝ × ℝ × M₂(ℝ)` (`HeckeWedderburn3`), any Markov
trace is a **weighted character sum** `tr_M = Σ_λ w_λ χ_λ` — the QOU Frobenius
pairing and the partition-function reading of the trace (R1).  Here we build that
functional concretely at `n = 3`,

  `markovTrace3 w₀ w₁ w₂ (x) = w₀·χ_{(3)}(x) + w₁·χ_{(1³)}(x) + w₂·χ_{(2,1)}(x)`,

with `χ_{(3)} = rhoTriv`, `χ_{(1³)} = rhoSign`, and `χ_{(2,1)} = trace ∘ seminormalRep21`,
and prove the two structural facts a Markov trace must have:

* **trace property** `markovTrace3 (x·y) = markovTrace3 (y·x)` (`markovTrace3_mul_comm`)
  — each summand is the character of a representation, and characters are class
  functions (`Matrix.trace_mul_comm` for the `(2,1)` block);
* **value at `1`** `markovTrace3 1 = w₀ + w₁ + 2 w₂ = Σ_λ w_λ d_λ` (`markovTrace3_one`)
  — the degeneracy-weighted block count (`d_{(2,1)} = 2`).

Plus the concrete `H_3(q)` character values on the generators
(`char21_σ`, `char21_σ0σ1`): `χ_{(2,1)}(σ_i) = q - q⁻¹` and `χ_{(2,1)}(σ₀σ₁) = -1`.

The canonical *Ocneanu/HOMFLY normalisation* of the weights `w_λ` (the choice of
Markov parameter fixing the 1-parameter family, giving the Jones polynomial) is a
separate normalisation step, tracked under `qou-tpl5`.

Base ring `ℝ` (the `(2,1)` seminormal rep is archimedean, §7c).

LaTeX label: `prop:hecke3-markov-weighted-character`
References: Jones (1987) `[jones1987]`, Wenzl (1988) `[wenzl1988]`.
-/

namespace QOU.SchurWeyl

open Hecke Matrix

section Markov3

variable (q : ℝ)

local notation3 "t₀" => σ ℝ q q⁻¹ 2 0
local notation3 "t₁" => σ ℝ q q⁻¹ 2 1

/-- The **weighted-character (Markov) trace** on `H_3(q)`: the block-weighted sum of
the three irreducible characters (trivial, sign, and the `(2,1)` seminormal). -/
noncomputable def markovTrace3 (hq : q ≠ 0) (w₀ w₁ w₂ : ℝ) (x : Hecke ℝ q q⁻¹ 2) : ℝ :=
  w₀ * rhoTriv ℝ q q⁻¹ 2 x + w₁ * rhoSign ℝ q q⁻¹ 2 x
    + w₂ * (seminormalRep21 q hq x).trace

/-- **Trace property**: `markovTrace3` is a class function, `tr_M(x·y) = tr_M(y·x)`.
Each summand is the character of a representation. -/
theorem markovTrace3_mul_comm (hq : q ≠ 0) (w₀ w₁ w₂ : ℝ) (x y : Hecke ℝ q q⁻¹ 2) :
    markovTrace3 q hq w₀ w₁ w₂ (x * y) = markovTrace3 q hq w₀ w₁ w₂ (y * x) := by
  simp only [markovTrace3, map_mul]
  rw [mul_comm (rhoTriv ℝ q q⁻¹ 2 x) (rhoTriv ℝ q q⁻¹ 2 y),
      mul_comm (rhoSign ℝ q q⁻¹ 2 x) (rhoSign ℝ q q⁻¹ 2 y),
      Matrix.trace_mul_comm]

/-- **Value at the identity**: `tr_M(1) = Σ_λ w_λ d_λ = w₀ + w₁ + 2 w₂`
(`d_{(3)} = d_{(1³)} = 1`, `d_{(2,1)} = 2`). -/
theorem markovTrace3_one (hq : q ≠ 0) (w₀ w₁ w₂ : ℝ) :
    markovTrace3 q hq w₀ w₁ w₂ 1 = w₀ + w₁ + 2 * w₂ := by
  simp only [markovTrace3, map_one, Matrix.trace_one, Fintype.card_fin]
  ring

/-- The `(2,1)` character of `σ₀`: `χ_{(2,1)}(σ₀) = tr(S0) = q - q⁻¹`. -/
theorem char21_σ0 (hq : q ≠ 0) :
    (seminormalRep21 q hq t₀).trace = q - q⁻¹ := by
  rw [seminormalRep21_σ0, Matrix.trace_fin_two]
  simp only [S0, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.of_apply]
  ring

/-- The `(2,1)` character of `σ₁`: `χ_{(2,1)}(σ₁) = tr(S1) = q - q⁻¹`.  (The two
seminormal generators are isospectral: same trace `q - q⁻¹`, same determinant `-1`.) -/
theorem char21_σ1 (hq : q ≠ 0) :
    (seminormalRep21 q hq t₁).trace = q - q⁻¹ := by
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq3q : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq (by positivity)
  rw [seminormalRep21_σ1, Matrix.trace_fin_two]
  simp only [S1, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.of_apply]
  field_simp
  ring

/-- The `(2,1)` character of the length-2 element `σ₀σ₁`: `χ_{(2,1)}(σ₀σ₁) = tr(S0·S1) = -1`. -/
theorem char21_σ0σ1 (hq : q ≠ 0) :
    (seminormalRep21 q hq (t₀ * t₁)).trace = -1 := by
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq3q : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq (by positivity)
  rw [map_mul, seminormalRep21_σ0, seminormalRep21_σ1, Matrix.trace_fin_two]
  simp only [S0, S1, Matrix.mul_apply, Fin.sum_univ_two, Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.of_apply]
  field_simp
  ring

/-- The Markov trace on a single generator: `tr_M(σ_i) = w₀ q - w₁ q⁻¹ + w₂ (q - q⁻¹)`
(the same for `σ₀` and `σ₁` — isospectrality). -/
theorem markovTrace3_σ0 (hq : q ≠ 0) (w₀ w₁ w₂ : ℝ) :
    markovTrace3 q hq w₀ w₁ w₂ t₀ = w₀ * q - w₁ * q⁻¹ + w₂ * (q - q⁻¹) := by
  rw [markovTrace3, rhoTriv_σ, rhoSign_σ, char21_σ0]
  ring

theorem markovTrace3_σ1 (hq : q ≠ 0) (w₀ w₁ w₂ : ℝ) :
    markovTrace3 q hq w₀ w₁ w₂ t₁ = w₀ * q - w₁ * q⁻¹ + w₂ * (q - q⁻¹) := by
  rw [markovTrace3, rhoTriv_σ, rhoSign_σ, char21_σ1]
  ring

end Markov3

end QOU.SchurWeyl
