import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.Mass.SelectionRuleQuantumIntegerForm — the `[2]_q` assembly of the lever-1 trace τ

This file completes the **categorical `[2]_q` derivation** of the lever-1 binding-kernel trace,
joining the two ends already in the corpus:

* `HeckeStokesEigenvalues` — the quantum integer `[2]_q = q + q⁻¹` is the *gap* `λ₊ − λ₋` between
  the two Hecke / non-abelian-Stokes eigenvalues `λ₊ = q`, `λ₋ = −q⁻¹`;
* `TauQuantumIntegerForm` (#2774) — `τ = 3(3[2]² + 2)/(4([2] + 2))` is a function of `[2]_q`.

The middle of the chain is the **selection-rule mean quantum dimensions** `lw(c)` (the anchors
`a_D^(c+1)`). They are proved in the corpus in `q`-form / `h`-form (`h = q − q⁻¹`, bar-odd):
`lw(1)=1`, `lw(2)=([2]_q+2)/3` (`selection-rule-c2-prediction`, the sum-form), and
`lw(3) = 5/2 + (3/4)(q − q⁻¹)²` (`selection-rule-anchors-c1-c3`). This file adds the two missing
links: `lw(3)` in the bar-**even** `[2]_q = q + q⁻¹` form, and the **explicit assembly**
`τ = (lw(1) + lw(3))/lw(2)` landing on `TauQuantumIntegerForm`'s closed form — so the whole
trace is visibly built from the single quantum integer `[2]_q`.

Ground ring `ℝ` (the selection-rule anchors live there, `q₀`-evaluable; matches the c1–c3 files).
Pure field algebra (`field_simp; ring`). This does **not** touch the open keystone (the
geometric↔categorical identity `a_D^(n) = ∮ λ_SW^(n) = lw(n−1)`); it formalises the categorical
half, `lw → τ`, in `[2]_q`.

**Scope — the depth-2 form is the `n ≤ 4` germ, NOT the period recurrence** (fork verdict,
coordination on #2795; companion Lean lemma `QOU.Mass.sl2Invariant_eq_zeroth` /
`prop:sl2-period-conserved-quantity`). The `τ` assembled here reproduces the anchors `a_D^(2..4)`,
to which `τ` is fit, and the depth-2 SL₂ recurrence `a_D^(n+2) = τ·a_D^(n+1) − a_D^(n)` conserves the
first integral `H_n = a(n+1)² − τ·a(n+1)·a(n) + a(n)²`. The true SW period `a_D^(n) = ∮ λ_SW^(n)`
grows *super-exponentially* for `n ≥ 6` (a q-Bessel-class residue sum `Σ_λ dim_q`, since the contour
encircles the color-cubic branch points), so it conserves no such `H_n` and satisfies **no** depth-2
recurrence. Hence `tau_from_quantum_integer_anchors` is exact as the anchor germ and must **not** be
extrapolated as the geometric period recurrence; the period proper is the q-Bessel kernel of
`prop:binding-genfun-qdifference`.
-/

namespace QOU.Mass

/-- **`lw(3)` (the Family-A / proton anchor) in bar-even `[2]_q` form:**
`(3q² + 4 + 3q⁻²)/4 = (3[2]_q² − 2)/4` with `[2]_q = q + q⁻¹`. The corpus's `h`-form uses the
bar-odd `h = q − q⁻¹` via `(q−q⁻¹)² = [2]_q² − 4`; this is the bar-even quantum-integer form that
matches `TauQuantumIntegerForm`. -/
theorem selection_rule_c3_quantum_integer (q : ℝ) (hq : 0 < q) :
    (3 * q ^ 2 + 4 + 3 * q⁻¹ ^ 2) / 4 = (3 * (q + q⁻¹) ^ 2 - 2) / 4 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  field_simp
  ring

/-- **The τ assembly from the three `[2]_q` anchors.** With the mean quantum dimensions
`lw(1) = 1`, `lw(2) = (b + 2)/3`, `lw(3) = (3b² − 2)/4` (here `b = [2]_q`), the kernel trace
`τ = (lw(1) + lw(3))/lw(2)` equals `3(3b² + 2)/(4(b + 2))` — `TauQuantumIntegerForm`'s closed form.
Stated for a generic `b` with `b + 2 ≠ 0`. -/
theorem tau_from_quantum_integer_anchors (b : ℝ) (hb : b + 2 ≠ 0) :
    (1 + (3 * b ^ 2 - 2) / 4) / ((b + 2) / 3) = 3 * (3 * b ^ 2 + 2) / (4 * (b + 2)) := by
  field_simp
  ring

/-- **The categorical `[2]_q` derivation, assembled.** Substituting `b = [2]_q = q + q⁻¹` into the
anchor assembly gives `τ` directly in the quantum integer:
`(1 + lw(3))/lw(2) = 3(3[2]² + 2)/(4([2] + 2))`. This is the `lw → τ` half of the keystone,
entirely a function of the Hecke eigenvalue gap `[2]_q`. -/
theorem tau_anchors_assemble_quantum_integer (q : ℝ) (hq : 0 < q) :
    (1 + (3 * (q + q⁻¹) ^ 2 - 2) / 4) / (((q + q⁻¹) + 2) / 3)
      = 3 * (3 * (q + q⁻¹) ^ 2 + 2) / (4 * ((q + q⁻¹) + 2)) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hb : (0 : ℝ) < q + q⁻¹ + 2 := by positivity
  have hb0 : q + q⁻¹ + 2 ≠ 0 := ne_of_gt hb
  field_simp
  ring

/-- Vanishing difference form of `tau_from_quantum_integer_anchors`. -/
theorem tau_from_quantum_integer_anchors_sub_eq_zero (b : ℝ) (hb : b + 2 ≠ 0) :
    (1 + (3 * b ^ 2 - 2) / 4) / ((b + 2) / 3) - 3 * (3 * b ^ 2 + 2) / (4 * (b + 2)) = 0 := by
  rw [tau_from_quantum_integer_anchors b hb, sub_self]

end QOU.Mass
