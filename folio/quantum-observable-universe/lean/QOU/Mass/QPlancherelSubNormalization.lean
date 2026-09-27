import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

/-!
# QOU.Mass.QPlancherelSubNormalization — the q-Plancherel completeness defect

Formalize-first Lean record of the normalization leg of the W_λ keystone wall
(2026-07-17 audit `docs/audits/.../keystone-wlambda-unitarity-normalization-gate.md`,
Python probe `keystone_wlambda_unitarity_normalization_gate_probe.py`). The
q-deformed Plancherel weight of an irrep `λ ⊢ n` is
`W_λ(q) = d_q(λ)² / [n]_q!`, and its total mass is the **partition function**

`Z_n(q) := (Σ_{λ ⊢ n} d_q(λ)²) / [n]_q!`,

where `d_q(λ) = [n]_q! / ∏_{cells}[hook]_q` is the quantum hook-length dimension
and `[k]_q = (q^k − q^{−k})/(q − q^{−1})` is the **balanced** quantum integer.
At `q = 1` this is the classical Plancherel measure and `Z_n(1) = 1`
(RSK / Burnside: `Σ_λ (f^λ)² = n!`). The audit's finding — the content of this
file — is that for `q ≠ 1` the total mass is a **rational function of `q` that is
strictly less than 1**: `W_λ` is *sub-normalized*, so it is **not** the vacuum-row
probability measure of any unitary modular category at real `q ≠ 1`. The
"fibre → archimedean continuation" of the normalization is therefore trivial
(a rational function continues everywhere bar poles); the genuine wall is the
non-rational *amplitude* leg (the Lawrence–Rozansky front), not the normalization.

This file proves the two smallest cases explicitly, which is all that is needed to
witness both phenomena (rationality + strict sub-normalization at `q ≠ 1`):

* **n = 2** — `Z₂(q) = 2q/(q²+1)` (rational), `Z₂(1) = 1`, and `Z₂(q) < 1` for
  every real `q > 0`, `q ≠ 1` (the archimedean completeness defect);
* **n = 3** — `Z₃(q) = q(q⁴+4q²+1) / ((q²+1)(q⁴+q²+1))` (rational), `Z₃(1) = 1`.

Base ring: `ℝ` throughout (§7c). This is deliberate and justified — the load-bearing
result is the *archimedean* strict inequality `Z₂(q) < 1` (a `0 < (q−1)²` fact), which
lives past the substrate→archimedean wall; the companion rational-closed-form identities
are stated over `ℝ` so that `positivity` discharges the (positive) denominators without
threading nonvanishing hypotheses.

The small-`n` quantum dimensions are the hook-length values, computed by hand:
`d_q((2)) = d_q((1,1)) = 1`, `d_q((2,1)) = [2]_q`, `d_q((3)) = d_q((1,1,1)) = 1`
(hook multisets `{2,1}`, `{3,1,1}`, `{3,2,1}`), and `[2]_q! = [2]_q`,
`[3]_q! = [3]_q[2]_q`.

Ref: [macdonald1995] (symmetric functions; hook-length formula) —
`content/schema/references.ts`.
-/

namespace QOU.Mass.QPlancherelSubNormalization

/-- The balanced quantum integer `[2]_q = q + q⁻¹`. -/
noncomputable def bracket2 (q : ℝ) : ℝ := q + q⁻¹

/-- The balanced quantum integer `[3]_q = q² + 1 + q⁻²`. -/
noncomputable def bracket3 (q : ℝ) : ℝ := q ^ 2 + 1 + (q⁻¹) ^ 2

/-- **q-Plancherel partition function at `n = 2`.**
`Z₂(q) = (d_q(2)² + d_q(1,1)²)/[2]_q! = (1 + 1)/[2]_q = 2/[2]_q`. -/
noncomputable def Z2 (q : ℝ) : ℝ := 2 / bracket2 q

/-- **q-Plancherel partition function at `n = 3`.**
`Z₃(q) = (d_q(3)² + d_q(2,1)² + d_q(1,1,1)²)/[3]_q!
       = (1 + [2]_q² + 1)/([3]_q[2]_q)`. -/
noncomputable def Z3 (q : ℝ) : ℝ := (2 + bracket2 q ^ 2) / (bracket3 q * bracket2 q)

/-- **Rationality at `n = 2`.** `Z₂(q) = 2q/(q²+1)` — a rational function of `q`,
so the normalization's fibre→archimedean continuation is trivial. -/
theorem Z2_eq (q : ℝ) (hq : q ≠ 0) : Z2 q = 2 * q / (q ^ 2 + 1) := by
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hden : q + q⁻¹ ≠ 0 := by
    have h : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [h]; exact div_ne_zero hq2 hq
  unfold Z2 bracket2
  rw [div_eq_div_iff hden hq2]
  field_simp

/-- **Classical normalization.** `Z₂(1) = 1` (Plancherel at `q = 1`). -/
theorem Z2_at_one : Z2 1 = 1 := by
  unfold Z2 bracket2
  norm_num

/-- **Sub-normalization / completeness defect at `n = 2`.** For every real
`q > 0` with `q ≠ 1`, `Z₂(q) < 1`: the total q-Plancherel mass is strictly
below 1, so `W_λ` is not a unitary vacuum-row probability measure at `q ≠ 1`.
The obstruction is exactly `0 < (q−1)²`. -/
theorem Z2_sub_normalized (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1) : Z2 q < 1 := by
  have hne : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  have hbig : (2 : ℝ) < q + q⁻¹ := by
    rw [← sub_pos]
    have hstep : q + q⁻¹ - 2 = (q - 1) ^ 2 / q := by
      field_simp
      ring
    rw [hstep]
    positivity
  unfold Z2 bracket2
  rw [div_lt_one (by linarith)]
  linarith

/-- **Rationality at `n = 3`.**
`Z₃(q) = q(q⁴+4q²+1) / ((q²+1)(q⁴+q²+1))` — again a rational function of `q`. -/
theorem Z3_eq (q : ℝ) (hq : q ≠ 0) :
    Z3 q = q * (q ^ 4 + 4 * q ^ 2 + 1) / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have hb2 : q + q⁻¹ ≠ 0 := by
    have h : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [h]; exact div_ne_zero h1 hq
  have hb3 : q ^ 2 + 1 + (q⁻¹) ^ 2 ≠ 0 := by positivity
  unfold Z3 bracket3 bracket2
  rw [div_eq_div_iff (mul_ne_zero hb3 hb2) (mul_ne_zero h1 h2)]
  field_simp
  ring

/-- **Classical normalization at `n = 3`.** `Z₃(1) = 1`. -/
theorem Z3_at_one : Z3 1 = 1 := by
  unfold Z3 bracket3 bracket2
  norm_num

end QOU.Mass.QPlancherelSubNormalization
