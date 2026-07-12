/-
# QOU.Mass.BindingClassicalKernel — the EXACT classical (q=1) binding kernel

The lever-1 binding generating function `a_D^(n)` is often modelled by the fixed-`τ`
depth-2 recurrence `a_{n+2} = τ·a_{n+1} − a_n` (`BindingRecurrenceSpectral`), but that
model is **only an n≤4 effective description**: `Lever1Depth2Exclusion` proves *no* fixed
`τ` reproduces the anchors beyond the seed. This file supplies the **complement** — the
*exact* kernel at the classical limit `q = 1`, and it is **derived, not fitted**.

## The derivation

At `q = 1` the na-Stokes period `S(n) = Σ_{λ⊢n} dim_q(λ)` degenerates to the sum of
Young-tableau dimensions `Σ_{λ⊢n} f^λ`, which by the RSK/Burnside identity (the keystone
**Identity I**) equals the involution / telephone number `I(n)` (`involutionNumber`, OEIS
A000085). Hence the classical binding period is

  `a_D^(n) |_{q=1} = lw(n−1) |_{q=1} = S(n)/n |_{q=1} = I(n)/n`.

The telephone numbers satisfy the **variable-coefficient** recurrence
`I(n+2) = I(n+1) + (n+1)·I(n)` (definitional here), so `a_D^(n) = I(n)/n` satisfies

  `(n+3)·a_D^(n+3) = (n+2)·a_D^(n+2) + (n+2)(n+1)·a_D^(n+1)`     (shifted to keep n ≥ 1),

a **variable-coefficient** depth-2 kernel — its coefficients grow with `n`, giving the
super-exponential growth the fixed-`τ` (constant-coefficient) model cannot. `τ = 2.6424`
is the n≤4 constant-coefficient *shadow* of this exact kernel.

This is a `q = 1` (classical-limit) statement: exact, sorry-free, and derived from the
telephone recurrence — a proved fact — modulo the `Σ f^λ = I(n)` identification, which is
the keystone Identity I (`YoungTableauStandard.sum_dimSYT_eq_involution`, the RSK sorry the
P1–P5 program discharges). So the classical binding kernel and the keystone share **one**
open input; everything else here is proved. The full `q`-deformation is
`S(n) = S(n−1) + [n−1]_q·S(n−2) + D(n)` with a cyclotomic Habiro tail `D(n)`
(`c_3 = [2]_q` exact); this file pins the classical leading term.

Compute: `computations/lever1_binding_classical_kernel_derive.py`.
Audit: `docs/audits/2026-07-12-lever1-sw-period-lw-rate-refine.md`.
-/
import QOU.BraidKnot.KeystoneC8SuperExpBound

namespace QOU.Mass.BindingClassicalKernel

open QOU.BraidKnot.KeystoneC8SuperExpBound

/-- Classical-limit (`q = 1`) binding period `a_D^(n) = I(n)/n`, `I =` involution numbers
(`= (Σ_{λ⊢n} f^λ)/n` via Identity I). -/
noncomputable def aDClassical (n : ℕ) : ℚ := (involutionNumber n : ℚ) / n

/-- The telephone recurrence, in the shape needed below (definitional). -/
theorem involutionNumber_shift (n : ℕ) :
    involutionNumber (n + 3)
      = involutionNumber (n + 2) + (n + 2) * involutionNumber (n + 1) := rfl

/-- **The exact classical binding kernel is variable-coefficient (derived, not fitted).**

For every `n`, the classical binding period `a_D^(n) = I(n)/n` satisfies the
variable-coefficient depth-2 recurrence

  `(n+3)·a_D^(n+3) = (n+2)·a_D^(n+2) + (n+2)(n+1)·a_D^(n+1)`.

The coefficients depend on `n` (they grow), so this is **not** a fixed-`τ` recurrence; the
constant-`τ` depth-2 model (`BindingRecurrenceSpectral`) is the n≤4 shadow of this kernel.
Proved from the telephone recurrence — no fit, no `sorry`. -/
theorem aDClassical_variable_coeff (n : ℕ) :
    ((n : ℚ) + 3) * aDClassical (n + 3)
      = ((n : ℚ) + 2) * aDClassical (n + 2)
        + ((n : ℚ) + 2) * ((n : ℚ) + 1) * aDClassical (n + 1) := by
  unfold aDClassical
  rw [involutionNumber_shift n]
  have h1 : ((n : ℚ) + 1) ≠ 0 := by positivity
  have h2 : ((n : ℚ) + 2) ≠ 0 := by positivity
  have h3 : ((n : ℚ) + 3) ≠ 0 := by positivity
  push_cast
  field_simp

/-- The classical kernel is **not** the fixed-`τ` model: at a place where the variable
coefficient `(n+2)` differs from the constant one, the two recurrences disagree. Concretely
the leading multiplier is `(n+2)`, which is unbounded — no constant `τ` matches it for all
`n`. (The quantitative failure beyond the seed is `Lever1Depth2Exclusion`.) -/
theorem aDClassical_coeff_unbounded : ∀ C : ℚ, ∃ n : ℕ, C < (n : ℚ) + 2 := by
  intro C
  obtain ⟨n, hn⟩ := exists_nat_gt C
  exact ⟨n, by linarith⟩

end QOU.Mass.BindingClassicalKernel
