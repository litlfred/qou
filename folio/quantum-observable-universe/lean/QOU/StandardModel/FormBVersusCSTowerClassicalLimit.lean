/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic
import Mathlib.Topology.Order.IntermediateValue

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

Two further results (2026-11-21, owner request):

* `formB_existsUnique_small` / `isFormB_existsUnique_small` — for `T > 0`, `q > 0`
  and `2·c·h² ≤ T + 2/(3π)`, the Form-B equation (Form A at `c = 0`) has exactly
  one solution `α ∈ (0, 1/(T + 2/(3π))]`; any other positive solution has
  `c·h²·α > 1` (`formB_large_root`).  So "the Form-B coupling" is a well-defined
  function of `q`, not an assumed one.
* `kappa_one` — the CS Gram ratio `κ = det G_cl / det G_q` equals `1` at `q = 1`
  (`G_q(1) = G_cl`, `det G_cl = π⁴·45375/72900 ≠ 0`), so the tower has no pole
  there.

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

/-! ## Forms A and B each define a unique small coupling

The fixed-point equations are stated with `S = T + 2/(3π)`, `H > 0` and the
Schwinger strength `k = c·h² ≥ 0`.  Form A is `k = 0`. -/

/-- The cleared form `α·(S + α·H·(1 − k·α))` of the Form-B equation. -/
def formBG (S H k α : ℝ) : ℝ := α * (S + α * H * (1 - k * α))

theorem formBG_strictMonoOn (S H k : ℝ) (hS : 0 < S) (hH : 0 < H)
    (h2k : 2 * k ≤ S) : StrictMonoOn (formBG S H k) (Set.Icc 0 (1 / S)) := by
  intro a ha b hb hab
  obtain ⟨ha0, ha1⟩ := ha
  obtain ⟨hb0, hb1⟩ := hb
  have hbS : b * S ≤ 1 := by rwa [le_div_iff₀ hS] at hb1
  have hkab : k * (a + b) ≤ 1 := by nlinarith
  have hsq : k * (a ^ 2 + a * b + b ^ 2) ≤ a + b := by nlinarith
  have key : formBG S H k b - formBG S H k a
      = (b - a) * (S + H * (a + b) - H * k * (a ^ 2 + a * b + b ^ 2)) := by
    unfold formBG; ring
  have hpos : 0 < S + H * (a + b) - H * k * (a ^ 2 + a * b + b ^ 2) := by nlinarith
  nlinarith

/-- **Form B has exactly one solution in `(0, 1/S]`** when `2·c·h² ≤ S`
    (Form A, `k = 0`, included). -/
theorem formB_existsUnique_small (S H k : ℝ) (hS : 0 < S) (hH : 0 < H)
    (h2k : 2 * k ≤ S) :
    ∃! α, α ∈ Set.Ioc 0 (1 / S) ∧ 1 / α = S + α * H * (1 - k * α) := by
  have hcont : ContinuousOn (formBG S H k) (Set.Icc 0 (1 / S)) := by
    unfold formBG; fun_prop
  have h0 : formBG S H k 0 = 0 := by simp [formBG]
  have hend : 1 ≤ formBG S H k (1 / S) := by
    unfold formBG
    have : 1 / S * (S + 1 / S * H * (1 - k * (1 / S)))
        = 1 + H / S ^ 2 * (1 - k / S) := by field_simp
    rw [this]
    have hk' : k / S ≤ 1 := by rw [div_le_one hS]; linarith
    have : 0 ≤ H / S ^ 2 * (1 - k / S) := by
      apply mul_nonneg (by positivity); linarith
    linarith
  have hle : (0 : ℝ) ≤ 1 / S := by positivity
  obtain ⟨α, hαI, hα⟩ := intermediate_value_Icc hle hcont ⟨by rw [h0]; norm_num, hend⟩
  have hα0 : α ≠ 0 := by rintro rfl; rw [h0] at hα; norm_num at hα
  have hαpos : 0 < α := lt_of_le_of_ne hαI.1 (Ne.symm hα0)
  have iff_eq : ∀ β, 0 < β → (1 / β = S + β * H * (1 - k * β) ↔ formBG S H k β = 1) := by
    intro β hβ
    unfold formBG
    constructor
    · intro h; rw [← h]; field_simp
    · intro h; field_simp; linarith
  refine ⟨α, ⟨⟨hαpos, hαI.2⟩, (iff_eq α hαpos).2 hα⟩, ?_⟩
  rintro β ⟨⟨hβ0, hβ1⟩, hβ⟩
  have hβg := (iff_eq β hβ0).1 hβ
  exact (formBG_strictMonoOn S H k hS hH h2k).injOn ⟨hβ0.le, hβ1⟩ hαI (hβg.trans hα.symm)

/-- Any other positive Form-B solution lies beyond `1/k`: it needs `k·α > 1`. -/
theorem formB_large_root (S H k α : ℝ) (hS : 0 < S) (hH : 0 < H) (hα : 0 < α)
    (hlarge : 1 / S < α) (h : 1 / α = S + α * H * (1 - k * α)) : 1 < k * α := by
  have h1 : 1 / α < S := by
    rw [div_lt_iff₀ hα]; rw [div_lt_iff₀ hS] at hlarge; linarith
  have : α * H * (1 - k * α) < 0 := by linarith
  have hαH : 0 < α * H := mul_pos hα hH
  by_contra hc
  push_neg at hc
  nlinarith

/-- The Form-A/B equation at `q > 0` in the shape of `IsFormB`. -/
theorem isFormB_existsUnique_small (T c q : ℝ) (hT : 0 < T) (hq : 0 < q)
    (h2 : 2 * (c * hecke q ^ 2) ≤ T + zeroMode) :
    ∃! α, α ∈ Set.Ioc 0 (1 / (T + zeroMode)) ∧ IsFormB T c q α := by
  have hS : 0 < T + zeroMode := by have := zeroMode_pos; linarith
  have hH : 0 < formBH q := by unfold formBH; have := Real.pi_pos; positivity
  obtain ⟨α, hα, huniq⟩ := formB_existsUnique_small _ _ _ hS hH h2
  refine ⟨α, ⟨hα.1, by unfold IsFormB; rw [hα.2]⟩, ?_⟩
  rintro β ⟨hβ1, hβ2⟩
  exact huniq β ⟨hβ1, by unfold IsFormB at hβ2; rw [hβ2]⟩

/-! ## The CS Gram ratio is regular at `q = 1`

`κ(q) = det G_cl / det G_q`, with `G_q` the `q`-integer substitution used by
`meson_em_sinh_closed_form._alpha_em_inv_derived`.  At `q = 1` every `[n]_q`
is `n`, so `G_q(1) = G_cl` and `κ(1) = 1`; `det G_cl = π⁴·45375/72900 ≠ 0`. -/

/-- `[n]_q = Σ_{k<n} q^k (q⁻¹)^{n−1−k}`. -/
def qN (n : ℕ) (q : ℝ) : ℝ := ∑ k ∈ Finset.range n, q ^ k * q⁻¹ ^ (n - 1 - k)

theorem qN_one (n : ℕ) : qN n 1 = n := by simp [qN]

/-- Diagonal entry `CS(T(a,b)) + π²·sl²/(ab)²` with `q`-integers `a, b`. -/
def gramDiag (a b : ℝ) : ℝ :=
  Real.pi ^ 2 * (a ^ 2 - 1) * (b ^ 2 - 1) / (12 * a * b) +
    Real.pi ^ 2 * ((a - 1) * (b - 1)) ^ 2 / (a * b) ^ 2

/-- `det G_q`. -/
def detGq (q : ℝ) : ℝ :=
  gramDiag (qN 2 q) (qN 9 q) * gramDiag (qN 3 q) (qN 5 q) -
    (Real.pi ^ 2 * (qN 2 q * qN 5 q - qN 3 q * qN 9 q) ^ 2 /
      (qN 2 q * qN 9 q * qN 3 q * qN 5 q)) ^ 2

/-- `det G_cl` (classical CS invariants, self-linking 8, linking 17). -/
def detGcl : ℝ :=
  (Real.pi ^ 2 * (10 / 9) + Real.pi ^ 2 * 8 ^ 2 / 18 ^ 2) *
      (Real.pi ^ 2 * (16 / 15) + Real.pi ^ 2 * 8 ^ 2 / 15 ^ 2) -
    (Real.pi ^ 2 * 17 ^ 2 / (18 * 15)) ^ 2

theorem detGcl_eq : detGcl = Real.pi ^ 4 * (45375 / 72900) := by
  unfold detGcl; ring

theorem detGcl_ne_zero : detGcl ≠ 0 := by
  rw [detGcl_eq]; have := Real.pi_pos; positivity

/-- **`G_q(1) = G_cl`**: the `q`-deformed Gram determinant equals the classical one. -/
theorem detGq_one : detGq 1 = detGcl := by
  simp only [detGq, qN_one, gramDiag, detGcl]
  push_cast
  ring

/-- **`κ(1) = 1`.** -/
theorem kappa_one : detGcl / detGq 1 = 1 := by
  rw [detGq_one]; exact div_self detGcl_ne_zero

end

end QOU.AlphaEM.ClassicalLimit
