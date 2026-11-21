/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

/-!
# Form B and the Chern–Simons tower part at the classical point `q = 1`

Bean `qou-aemx` ("which α_em functional is canonical").  The two live
constructions of `1/α_em` share the tree term `T(q) = q·[9]_q·[10]_q` and differ
in what they add to it:

```
Form B   1/α = T + 2/(3π) + α·H(q)·(1 − c·h(q)²·α),   H = [2]_q/(8π),  h = q − q⁻¹
CS tower 1/α = T·(1 + c₁/(1 − c₁κ)),   T·c₁ = π²·(98/45)·([2]_q/2)·(1 − q⁻¹)²
```

Form A is Form B with `c = 0`.  Each form carries one open parameter: the
Schwinger coefficient `c` (Form B, `c = 1` is motivated, not derived) and the
Gram ratio `κ = det G_cl / det G_q` (CS tower; `G_q` is a parameter of
`ChernSimonsCorrectionConjecture`, no instance, bean `qou-gbsa`).

This file proves that the two constructions are different functions of `q`,
**uniformly in both open parameters and in the shared tree value**, by
evaluating at the classical point `q = 1`, where `[2]_q = 2`, `h = 0` and
`1 − q⁻¹ = 0`:

* `csTower_at_one` — the CS tower is `T` at `q = 1`, for every `κ`;
* `formB_at_one_gt` — every positive solution `α` of the Form-B equation at
  `q = 1` has `1/α > T + 2/(3π)`, for every `c`;
* `formB_ne_csTower_at_one` — so no choice of `c`, `κ` or `T` makes them agree
  at `q = 1`.

Both right-hand sides are rational in `q` with no pole at `q = 1` (`H` and the
CS shift contain `q + q⁻¹` and `1 − q⁻¹`, never `1/(q − q⁻¹)`), so the value at
`q = 1` is also the `q → 1` limit (`csShift_tendsto_zero`).

**What this decides and what it does not.**  It decides that neither form is a
truncation, resummation or reparametrisation of the other: the CS correction is
a pure `ℏ_q`-effect that switches off classically, while Form B keeps a
topological shift `2/(3π) = b₁/Area` and a one-loop term `α/(4π)` at `q = 1`.
It does **not** say which is right.  That is a choice of axiom: whether the
correction to the tree term must vanish in the classical limit.  No measured
value enters this file.

-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-- Ref: [leitner2026] rem:em-coupling-chern-simons
-/

namespace QOU.AlphaEM.ClassicalLimit

open Filter Topology

noncomputable section

/-- The Bring zero-mode shift of Form B, `2/(3π) = 2g/(4π(g−1))` at `g = 4`. -/
def zeroMode : ℝ := 2 / (3 * Real.pi)

/-- Form-B one-loop normalisation `H(q) = [2]_q/(8π)`, `[2]_q = q + q⁻¹`. -/
def formBH (q : ℝ) : ℝ := (q + q⁻¹) / (8 * Real.pi)

/-- The Hecke structure constant `h(q) = q − q⁻¹`. -/
def hecke (q : ℝ) : ℝ := q - q⁻¹

/-- Form B as a relation between the tree value `T`, the Schwinger coefficient
    `c`, the deformation parameter `q` and the coupling `α`.  Form A is `c = 0`. -/
def IsFormB (T c q α : ℝ) : Prop :=
  1 / α = T + zeroMode + α * formBH q * (1 - c * hecke q ^ 2 * α)

/-- The first-order Chern–Simons shift `T·c₁ = π²·(98/45)·([2]_q/2)·(1 − q⁻¹)²`,
    with `98/45 = 10/9 + 16/15` the CS invariants of `T(2,9)` and `T(3,5)`
    divided by `π²`. -/
def csShift (q : ℝ) : ℝ :=
  Real.pi ^ 2 * (98 / 45) * ((q + q⁻¹) / 2) * (1 - q⁻¹) ^ 2

/-- The exactly resummed Chern–Simons tower `T·(1 + c₁/(1 − c₁κ))` with
    `c₁ = csShift q / T`.  `κ` is left free. -/
def csTower (T κ q : ℝ) : ℝ :=
  T * (1 + (csShift q / T) / (1 - (csShift q / T) * κ))

/-- The CS shift vanishes at the classical point. -/
theorem csShift_one : csShift 1 = 0 := by
  simp [csShift]

/-- The CS shift tends to `0` as `q → 1`. -/
theorem csShift_tendsto_zero : Tendsto csShift (𝓝 1) (𝓝 0) := by
  have hc : ContinuousAt csShift 1 := by
    unfold csShift
    have hinv : ContinuousAt (fun q : ℝ => q⁻¹) 1 :=
      continuousAt_inv₀ one_ne_zero
    fun_prop (disch := exact one_ne_zero)
  simpa [csShift_one] using hc.tendsto

/-- **The CS tower is the bare tree at `q = 1`, for every `κ` and every `T`.** -/
theorem csTower_at_one (T κ : ℝ) : csTower T κ 1 = T := by
  simp [csTower, csShift_one]

/-- `H(1) = 1/(4π)`. -/
theorem formBH_one : formBH 1 = 1 / (4 * Real.pi) := by
  unfold formBH
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp
  norm_num

/-- `h(1) = 0`: the Schwinger factor is invisible at `q = 1`. -/
theorem hecke_one : hecke 1 = 0 := by simp [hecke]

/-- At `q = 1` the Form-B relation no longer depends on `c`. -/
theorem isFormB_one_iff (T c α : ℝ) :
    IsFormB T c 1 α ↔ 1 / α = T + zeroMode + α / (4 * Real.pi) := by
  unfold IsFormB
  rw [hecke_one, formBH_one]
  constructor <;> intro h <;> (rw [h]; ring)

theorem zeroMode_pos : 0 < zeroMode := by
  unfold zeroMode; have := Real.pi_pos; positivity

/-- **Every positive Form-B coupling at `q = 1` has `1/α > T + 2/(3π)`**, for
    every Schwinger coefficient `c`. -/
theorem formB_at_one_gt (T c α : ℝ) (hα : 0 < α) (h : IsFormB T c 1 α) :
    T + zeroMode < 1 / α := by
  rw [isFormB_one_iff] at h
  rw [h]
  have : 0 < α / (4 * Real.pi) := by have := Real.pi_pos; positivity
  linarith

/-- **Form B and the CS tower disagree at `q = 1`, whatever `c`, `κ` and `T`.**
    A positive Form-B coupling `α` at `q = 1` never has `1/α` equal to the CS
    tower's value there. -/
theorem formB_ne_csTower_at_one (T c κ α : ℝ) (hα : 0 < α)
    (h : IsFormB T c 1 α) : 1 / α ≠ csTower T κ 1 := by
  rw [csTower_at_one]
  have := formB_at_one_gt T c α hα h
  have := zeroMode_pos
  intro heq
  linarith

/-- **Form A and Form B coincide at `q = 1`.**  The Schwinger coefficient is the
    only thing separating them, and it multiplies `h² = 0` there.  So A and B are
    one construction; the CS tower is another. -/
theorem formA_iff_formB_at_one (T c α : ℝ) :
    IsFormB T 0 1 α ↔ IsFormB T c 1 α := by
  rw [isFormB_one_iff, isFormB_one_iff]

end

end QOU.AlphaEM.ClassicalLimit
