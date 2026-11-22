/-
Copyright (c) 2026 litlfred. All rights reserved.

# The colored Lawrence–Rozansky bare amplitude, as a real trigonometric theorem

Archimedean companion to
[`KeystoneLRModulusFold.lean`](KeystoneLRModulusFold.lean) (PR #3822), the W_λ
keystone's last open piece (targets m_p / m_μ, Subgoal-2). That file proves the
**algebraic core** of the modulus identity over a generic field, carrying the
trigonometric value `sin²(mπ/5) = (10∓2√5)/16` only as a *rational-in-`s`
surrogate* (`(10−2s)/16`, `s² = 5`) — the real amplitude
`A_m(1) = (2/√5)·sin(mπ/5)` was explicitly "not a Lean theorem" (machine-evidence
only).

This file discharges exactly that gap — the step flagged **Lean-ready** in
[`docs/audits/2026-07-18-lr-modulus-bare-amplitude-exact.md`](../../../../../docs/audits/2026-07-18-lr-modulus-bare-amplitude-exact.md):
promote the bare-amplitude identity from a comment to a proved theorem about the
actual `Real.sin`. It closes the `loc_matches` / `bwS0_eq_hecke` gate's
bare-amplitude *precondition* (not the keystone; the archimedean q₀-continuation
of the folded root identity, #3652/#3681, remains open).

Genuinely archimedean (`Real.sin`, `Real.sqrt`, `Real.pi`) ⇒ base ring `ℝ`
(§7c: the archimedean specialisation lives in a separate file from the
generic-field algebraic core).

## Results (sorry-free)

* `sin_sq_pi_div_five` : `sin²(π/5) = (10 − 2√5)/16` — the first flat connection.
* `sin_sq_two_pi_div_five` : `sin²(2π/5) = (10 + 2√5)/16` — the Galois conjugate.
* `amplitude_first` : `A₁(1)² = ((2/√5)·sin(π/5))² = 4/(10 + 2√5) = 4/D²(ζ¹)`.
* `amplitude_second` : `A₂(1)² = ((2/√5)·sin(2π/5))² = 4/(10 − 2√5) = 4/D²(ζ²)`.
* `sin_sq_three_pi_div_five`, `sin_sq_four_pi_div_five` : the reflected node values
  (`sin(3π/5)=sin(2π/5)`, `sin(4π/5)=sin(π/5)`).
* `colored_modulus_phi_node` : the **colored (α ≥ 2)** amplitude at a `[α]=φ` Ê₈ node
  (marks 2, 3), `A₁(α)²·D²(ζ¹) = 4·φ²`, `φ = (1+√5)/2` — with `amplitude_first`
  (`[α]=1` nodes) and `qi φ 5 = 0` this closes `A₁(α)²·D²(ζ¹) = 4·[α]²` at every
  Ê₈ node, i.e. `W_λ ∝ [mark λ]²`.
* `phi_node_is_qi_two` : the `φ`-node value is the companion's fold integer `qi φ 2`.

The `4/(10 ± 2√5)` right-hand sides are `4/D²(ζ^m)` for the Ê₈ fold normalizers
`D²(ζ¹) = 10 + 2√5`, `D²(ζ²) = 10 − 2√5` proved in the companion
(`D2_E8_first_fold`, `D2_E8_second_fold` at `φ = (1+√5)/2`). So `A_m(1)` is the
vacuum modular-S element `S_{00}(ζ^m) = 2/D(ζ^m)` — derived from established exact
quantities, not extracted.

**Honest scope.** Closes the bare-amplitude precondition only. No `c_k` value; no
fit; nothing wired; L2 unchanged (2/7); the q₀-continuation gate stays open.

-- Ref: [leitner2026] docs/audits/2026-07-18-lr-modulus-bare-amplitude-exact.md
-- Ref: [hikami2005brieskorn] https://doi.org/10.1142/S0129167X05003004
-/
import QOU.BraidKnot.KeystoneLRModulusFold
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.BraidKnot.KeystoneLRAmplitudeReal

open Real

/-- `√5 ^ 2 = 5`. -/
private lemma sq_sqrt5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)

/-- `0 < √5`. -/
private lemma sqrt5_pos : (0 : ℝ) < Real.sqrt 5 := Real.sqrt_pos.mpr (by norm_num)

/-- **First flat connection**: `sin²(π/5) = (10 − 2√5)/16`.  Via
`cos(π/5) = (1+√5)/4` (Mathlib) and the Pythagorean identity. -/
theorem sin_sq_pi_div_five :
    Real.sin (π / 5) ^ 2 = (10 - 2 * Real.sqrt 5) / 16 := by
  have hcos : Real.cos (π / 5) = (1 + Real.sqrt 5) / 4 := Real.cos_pi_div_five
  have hpyth : Real.sin (π / 5) ^ 2 + Real.cos (π / 5) ^ 2 = 1 :=
    Real.sin_sq_add_cos_sq (π / 5)
  have hsin : Real.sin (π / 5) ^ 2 = 1 - Real.cos (π / 5) ^ 2 := by linarith
  rw [hsin, hcos]
  linear_combination (-1 / 16 : ℝ) * sq_sqrt5

/-- **Second flat connection** (Galois conjugate): `sin²(2π/5) = (10 + 2√5)/16`.
Via the sine double angle `sin(2π/5) = 2·sin(π/5)·cos(π/5)` and
`cos(π/5) = (1+√5)/4`. -/
theorem sin_sq_two_pi_div_five :
    Real.sin (2 * π / 5) ^ 2 = (10 + 2 * Real.sqrt 5) / 16 := by
  have hangle : (2 : ℝ) * π / 5 = 2 * (π / 5) := by ring
  have hcos : Real.cos (π / 5) = (1 + Real.sqrt 5) / 4 := Real.cos_pi_div_five
  have hdbl : Real.sin (2 * (π / 5)) = 2 * Real.sin (π / 5) * Real.cos (π / 5) :=
    Real.sin_two_mul (π / 5)
  have hexpand : Real.sin (2 * (π / 5)) ^ 2
      = 4 * Real.sin (π / 5) ^ 2 * Real.cos (π / 5) ^ 2 := by rw [hdbl]; ring
  rw [hangle, hexpand, sin_sq_pi_div_five, hcos]
  linear_combination (-(Real.sqrt 5 - 3) / 32) * sq_sqrt5

/-- **Bare amplitude, first flat connection**: `((2/√5)·sin(π/5))² = 4/(10 + 2√5)`
— i.e. `A₁(1)² = 4/D²(ζ¹)`, the vacuum modular-S element `S_{00}(ζ¹)`.  Reduces to
the companion's proved `vacuum_modulus_identity_first`. -/
theorem amplitude_first :
    ((2 / Real.sqrt 5) * Real.sin (π / 5)) ^ 2 = 4 / (10 + 2 * Real.sqrt 5) := by
  have hd : (10 + 2 * Real.sqrt 5) ≠ 0 := by positivity
  have hvac := KeystoneLRModulusFold.vacuum_modulus_identity_first (Real.sqrt 5) sq_sqrt5
  rw [mul_pow, div_pow, sin_sq_pi_div_five, sq_sqrt5, eq_div_iff hd]
  linear_combination hvac

/-- **Bare amplitude, second flat connection**: `((2/√5)·sin(2π/5))² = 4/(10 − 2√5)`
— i.e. `A₂(1)² = 4/D²(ζ²)`, the Galois-conjugate vacuum modular-S element.  Reduces
to the companion's proved `vacuum_modulus_identity_second`. -/
theorem amplitude_second :
    ((2 / Real.sqrt 5) * Real.sin (2 * π / 5)) ^ 2 = 4 / (10 - 2 * Real.sqrt 5) := by
  have hd : (10 - 2 * Real.sqrt 5) ≠ 0 := by
    have hpos : (0 : ℝ) < 10 - 2 * Real.sqrt 5 := by
      nlinarith [sq_sqrt5, sq_nonneg (Real.sqrt 5 - 3)]
    exact hpos.ne'
  have hvac := KeystoneLRModulusFold.vacuum_modulus_identity_second (Real.sqrt 5) sq_sqrt5
  rw [mul_pow, div_pow, sin_sq_two_pi_div_five, sq_sqrt5, eq_div_iff hd]
  linear_combination hvac

/-! ## The colored amplitude at the remaining Ê₈ nodes (first flat connection)

The colored Lawrence–Rozansky amplitude at node `λ` (mark `α`) is
`A_m(α) = (2/√5)·sin(αmπ/5)`, factoring as `|A_m(α)| = |A_m(1)|·|[α]_{ζ^m}|` with
the color character `[α]_{ζ¹} = sin(απ/5)/sin(π/5)` (= the Chebyshev-folded
quantum integer `qi φ α`, `φ = (1+√5)/2`).  At `m = 1` the node's `sin²(απ/5)`
reduces by the reflection `sin(π − x) = sin x` to one of the two vacuum values:
`α ∈ {1,4}` (marks with `[α] = 1`) → `(10−2√5)/16`; `α ∈ {2,3}`
(marks with `[α] = φ`) → `(10+2√5)/16`; `α = 5` → `0`.  So the full colored
amplitude closes at every Ê₈ node from the two `sin²` values already proved. -/

/-- `sin²(3π/5) = (10 + 2√5)/16` — by reflection `sin(3π/5) = sin(2π/5)`
(the mark-3 node, `[3] = φ`). -/
theorem sin_sq_three_pi_div_five :
    Real.sin (3 * π / 5) ^ 2 = (10 + 2 * Real.sqrt 5) / 16 := by
  have h : (3 : ℝ) * π / 5 = π - 2 * π / 5 := by ring
  rw [h, Real.sin_pi_sub]; exact sin_sq_two_pi_div_five

/-- `sin²(4π/5) = (10 − 2√5)/16` — by reflection `sin(4π/5) = sin(π/5)`
(the mark-4 node, `[4] = 1`). -/
theorem sin_sq_four_pi_div_five :
    Real.sin (4 * π / 5) ^ 2 = (10 - 2 * Real.sqrt 5) / 16 := by
  have h : (4 : ℝ) * π / 5 = π - π / 5 := by ring
  rw [h, Real.sin_pi_sub]; exact sin_sq_pi_div_five

/-- **Colored modulus identity at a `[α] = φ` node** (marks 2, 3; first flat
connection): `A₁(α)²·D²(ζ¹) = 4·φ²`, `φ = (1+√5)/2 = [2]_{ζ¹} = qi φ 2`.  Together
with `amplitude_first` (the `[α] = 1` nodes, `A₁²·D² = 4`) and `qi φ 5 = 0`, this
closes the colored amplitude at every Ê₈ node: `A₁(α)²·D²(ζ¹) = 4·[α]²_{ζ¹}`,
i.e. `W_λ ∝ [mark λ]²`. -/
theorem colored_modulus_phi_node :
    ((2 / Real.sqrt 5) * Real.sin (2 * π / 5)) ^ 2 * (10 + 2 * Real.sqrt 5)
      = 4 * ((1 + Real.sqrt 5) / 2) ^ 2 := by
  rw [mul_pow, div_pow, sin_sq_two_pi_div_five, sq_sqrt5]
  linear_combination (-4 / 5 : ℝ) * sq_sqrt5

/-- The `φ`-node quantum dimension is the companion's Chebyshev fold value
`qi φ 2 = φ`: the `((1+√5)/2)` in `colored_modulus_phi_node` is exactly the
mark-2 quantum integer at the first fold. -/
theorem phi_node_is_qi_two :
    KeystoneLRModulusFold.qi ((1 + Real.sqrt 5) / 2) 2 = (1 + Real.sqrt 5) / 2 :=
  KeystoneLRModulusFold.qi_two _

end QOU.BraidKnot.KeystoneLRAmplitudeReal
