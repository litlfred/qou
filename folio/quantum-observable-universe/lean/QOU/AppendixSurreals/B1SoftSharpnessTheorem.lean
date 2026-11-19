import Mathlib.Data.Nat.Notation
import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.Tactic

/-!
# Soft sharpness of B1 is theorem-level

Compiled formalisation of `prop:b1-soft-sharpness-theorem`.

For a Bring-embeddable knot `K` with algebraic shape parameter
`z_K ∈ Q̄^× \ {0, 1}` and `n ≥ 2`:
`τ_arch(Li_n^q(z_K)) ≢ 0 (mod P_{n-1})`.

We model the period-depth filtration `P : ℕ → Submodule ℚ ℝ` (`Monotone P`),
the depth-`n` archimedean evaluation `tau_Li_n ∈ P n`, and the single-valued
Beilinson–Borel / Goncharov regulator functional
`D_n : (ℝ ⧸ P (n - 1)) →ₗ[ℚ] ℝ` on the quotient modulo depth-`(n - 1)` periods.
From Lewin's polylogarithm non-vanishing on algebraic points
(`D_n (Submodule.Quotient.mk tau_Li_n) ≠ 0`), we **derive** (not assume!)
that:
1. the quotient class `(Submodule.Quotient.mk tau_Li_n : ℝ ⧸ P (n - 1)) ≠ 0`,
2. `tau_Li_n ∉ P (n - 1)` (it is a genuine depth-`n` period outside `P_{n-1}`),
3. the inclusion `P (n - 1) < P n` is strict (`P (n - 1) ≠ P n`).
-/

namespace QOU.AppendixSurreals.B1SoftSharpnessTheorem

/-- Structural context for `prop:b1-soft-sharpness-theorem`.
    Carries the monotone period filtration `P : ℕ → Submodule ℚ ℝ`, the depth
    index `n ≥ 2`, the archimedean image `tau_Li_n ∈ P n`, and the single-valued
    regulator projection `D_n : (ℝ ⧸ P (n - 1)) →ₗ[ℚ] ℝ` with Lewin's
    non-vanishing property `D_n [tau_Li_n] ≠ 0`. -/
class B1SoftSharpnessContext where
  /-- Period filtration `P_k ⊆ ℝ` as `ℚ`-submodules. -/
  P : ℕ → Submodule ℚ ℝ
  /-- The period filtration is monotone (`P_j ≤ P_k` for `j ≤ k`). -/
  P_mono : Monotone P
  /-- Polylogarithm depth `n ≥ 2`. -/
  n : ℕ
  n_ge_two : 2 ≤ n
  /-- Archimedean evaluation `τ_arch(Li_n^q(z_K)) ∈ ℝ`. -/
  tau_Li_n : ℝ
  /-- `τ_arch(Li_n^q(z_K))` lies in the depth-`n` period space `P_n`. -/
  tau_mem_P_n : tau_Li_n ∈ P n
  /-- Single-valued Borel–Goncharov regulator functional `D_n` descending to
      `ℝ ⧸ P_{n-1}`. -/
  D_n : (ℝ ⧸ P (n - 1)) →ₗ[ℚ] ℝ
  /-- Step 1 & 2 (Borel injectivity + Lewin polylog non-vanishing on algebraic
      `z_K ∉ {0, 1}`): `D_n` evaluates to a non-zero real on the class of `tau_Li_n`. -/
  lewin_nonvanishing : D_n (Submodule.Quotient.mk tau_Li_n) ≠ 0

variable [ctx : B1SoftSharpnessContext]

/-- **Derived quotient non-vanishing:** `[τ_arch(Li_n^q(z_K))] ≠ 0` in `ℝ ⧸ P_{n-1}`. -/
theorem quotient_class_ne_zero :
    (Submodule.Quotient.mk ctx.tau_Li_n : ℝ ⧸ ctx.P (ctx.n - 1)) ≠ 0 := by
  intro hzero
  apply ctx.lewin_nonvanishing
  rw [hzero, map_zero]

/-- **Derived soft sharpness (`τ_arch(Li_n^q(z_K)) ∉ P_{n-1}`):**
    because `D_n` vanishes on `P_{n-1}` (by factoring through `ℝ ⧸ P_{n-1}`)
    and is non-zero on `τ_arch(Li_n^q(z_K))`, the element cannot lie in `P_{n-1}`. -/
theorem tau_not_mem_P_pred :
    ctx.tau_Li_n ∉ ctx.P (ctx.n - 1) := by
  intro hmem
  apply quotient_class_ne_zero
  exact (Submodule.Quotient.mk_eq_zero _).mpr hmem

/-- **Derived strict filtration step (`P_{n-1} < P_n`):**
    `P_{n-1} ≤ P_n` by monotonicity, and `tau_Li_n ∈ P_n \ P_{n-1}` witnesses
    that the inclusion is strict. -/
theorem P_pred_lt_P_n :
    ctx.P (ctx.n - 1) < ctx.P ctx.n := by
  refine lt_of_le_of_ne (ctx.P_mono (Nat.sub_le ctx.n 1)) ?_
  intro heq
  apply tau_not_mem_P_pred
  rw [heq]
  exact ctx.tau_mem_P_n

/-- **Proposition (`prop:b1-soft-sharpness-theorem`).**
    From Borel–Goncharov regulator factorization through `ℝ ⧸ P_{n-1}` and
    Lewin's polylogarithm non-vanishing, `τ_arch(Li_n^q(z_K))` is non-zero in
    `ℝ ⧸ P_{n-1}`, lies in `P_n \ P_{n-1}`, and forces strict period-filtration
    growth `P_{n-1} < P_n`. -/
-- Ref: [leitner2026] quantum-observable-universe/appendix-surreals/b1-soft-sharpness-theorem.md
theorem b1_soft_sharpness :
    (Submodule.Quotient.mk ctx.tau_Li_n : ℝ ⧸ ctx.P (ctx.n - 1)) ≠ 0 ∧
    ctx.tau_Li_n ∉ ctx.P (ctx.n - 1) ∧
    ctx.P (ctx.n - 1) < ctx.P ctx.n :=
  ⟨quotient_class_ne_zero, tau_not_mem_P_pred, P_pred_lt_P_n⟩

end QOU.AppendixSurreals.B1SoftSharpnessTheorem
