import QOU.Nuclear.FiveTwoDeformedSaddle
import Mathlib.Analysis.Complex.Basic
import Mathlib.Topology.Order.IntermediateValue

/-!
# The real unit cubic of the deformed 5₂ curve on `|x| = 1`

Algebraic half of `QOU.Transcendental.Nuclear.FiveTwoRootStructure`, split off
on the transcendental boundary (epic `qou-dk7p`, strangler onto `[Coev E]`).

On `|x| = 1` the `y`-cubic of the deformed curve is real,

    p(Y) = Y³ − 2c·Y² + (2c+1)·Y − 1,     c = cos φ,

and this file holds everything about it that is real polynomial algebra plus
one application of the intermediate value theorem:

* `unitCubic`, `curve_eq_unitCubic`, `exists_root_mem_Ioo` — a root in `(0,1)`;
* `unitCubic_root_lt_one` — no real root reaches `1`;
* `beta_rel`, `gamma_rel`, `two_fifths_lt`, `W_nonneg_of_disc_nonneg`,
  `real_root_neg_of_ne` — the relations that carry the sign argument;
* `unitCubic_deriv_mul`, `unitCubic_deriv_ge`, `unitCubic_deriv_ne_zero` —
  `∂p/∂y ≥ 7/4` at the real root.

The explicit other two roots (`otherRoots`, built with `Real.sqrt`), their
continuity, and the `Im(x·y)` sign lemmas stay in the Transcendental module.
Declaration names and namespace are unchanged by the split.

-- Ref: [leitner2026] bean qou-trns
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Set

/-! ### 1. The real cubic, and a root in `(0,1)` -/

/-- The `y`-cubic of the deformed curve on `|x| = 1`, monic, with `c = cos φ`. -/
noncomputable def unitCubic (c t : ℝ) : ℝ := t ^ 3 - 2 * c * t ^ 2 + (2 * c + 1) * t - 1

/-- **`2·(Re x)·x = x² + 1` on `|x| = 1`** — which is `x·conj x = 1` in disguise.

Extracted as a theorem rather than left inside `curve_eq_unitCubic`, because it is
also the *minimal polynomial* of a non-real `x` on the circle over `ℝ`, and that
is what reduces any polynomial in `x` to something linear with real
coefficients — used by `quintic_of_mul_real` in `FiveTwoTransport`. -/
theorem unitCircle_quadratic {x : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) :
    2 * (x.re : ℂ) * x = x ^ 2 + 1 := by
  have h : ((2 * x.re : ℝ) : ℂ) * x = x ^ 2 + 1 := by
    apply Complex.ext <;>
      simp only [pow_two, Complex.mul_re, Complex.mul_im, Complex.add_re, Complex.add_im,
        Complex.ofReal_re, Complex.ofReal_im, Complex.one_re, Complex.one_im] <;>
      nlinarith [hx]
  push_cast at h
  linear_combination h

/-- **On `|x| = 1` the deformed curve's `y`-cubic IS `unitCubic (Re x)`.**

Checked rather than asserted: the reduction rests on `2·Re x·x = x² + 1`, which
is `x·conj x = 1` in disguise. Without this, everything below would be a correct
theorem about the wrong polynomial — the failure mode this lane has hit nine
times. -/
theorem curve_eq_unitCubic {x : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) (y : ℂ) :
    x * y ^ 3 - (x ^ 2 + 1) * y ^ 2 + (x ^ 2 + x + 1) * y - x
      = x * (y ^ 3 - 2 * (x.re : ℂ) * y ^ 2 + (2 * (x.re : ℂ) + 1) * y - 1) := by
  linear_combination (y ^ 2 - y) * unitCircle_quadratic hx

theorem unitCubic_zero (c : ℝ) : unitCubic c 0 = -1 := by unfold unitCubic; ring

/-- `p(1) = 1` **identically in `c`** — the `2c` terms cancel. This is why the
root in `(0,1)` costs nothing. -/
theorem unitCubic_one (c : ℝ) : unitCubic c 1 = 1 := by unfold unitCubic; ring

/-- **There is a real root in `(0,1)`.** `p(0) = −1 < 0 < 1 = p(1)`, then IVT. -/
theorem exists_root_mem_Ioo (c : ℝ) : ∃ t ∈ Ioo (0 : ℝ) 1, unitCubic c t = 0 := by
  have hcont : ContinuousOn (unitCubic c) (Icc 0 1) := by unfold unitCubic; fun_prop
  have hmem : (0 : ℝ) ∈ Ioo (unitCubic c 0) (unitCubic c 1) := by
    rw [unitCubic_zero, unitCubic_one]; constructor <;> norm_num
  obtain ⟨t, ht, hft⟩ := intermediate_value_Ioo (by norm_num : (0 : ℝ) ≤ 1) hcont hmem
  exact ⟨t, ht, hft⟩

/-! ### 1b. No real root reaches `1` — a uniform `Re < 1`

`real_root_neg_of_ne` already says the roots *other* than a distinguished
`t ∈ (0,1)` are negative, which bounds them below `1` — but only once such a `t`
is in hand. The lemmas here bound **every** real root below `1` directly from
`c ≤ 1`, with no distinguished root and no case analysis, which is what `notCut`
membership wants: `notCut = {w | Im w ≠ 0 ∨ Re w < 1}`, and a real root has to
take the second disjunct.

Route 36 G5 is why this is stated for all roots rather than for one. On the arc
there are **291** real roots over 199 points, not 199: the cubic has real
coefficients, the arc crosses the discriminant at `c* = −0.74221766588`, and at
46 of those points all three roots are real. A bound covering one distinguished
root would leave two thirds of the real roots there unhandled. -/

/-- **`p(1+s) = 1 + (4−2c)s + (3−2c)s² + s³`** — an identity in `c` and `s`.

The whole content of this subsection. Expanded about `t = 1` every coefficient is
positive as soon as `c ≤ 1`, so positivity for `s ≥ 0` is immediate; expanded
about `t = 0` the signs are mixed and nothing is immediate. -/
theorem unitCubic_shift (c s : ℝ) :
    unitCubic c (1 + s) = 1 + (4 - 2 * c) * s + (3 - 2 * c) * s ^ 2 + s ^ 3 := by
  unfold unitCubic; ring

/-- **`p(t) > 0` for every `t ≥ 1`, whenever `c ≤ 1`** — at least `1`, in fact. -/
theorem unitCubic_pos_of_one_le {c t : ℝ} (hc : c ≤ 1) (ht : 1 ≤ t) : 0 < unitCubic c t := by
  have hs : 0 ≤ t - 1 := by linarith
  have hid : unitCubic c t
      = 1 + (4 - 2 * c) * (t - 1) + (3 - 2 * c) * (t - 1) ^ 2 + (t - 1) ^ 3 := by
    unfold unitCubic; ring
  have h1 : 0 ≤ (4 - 2 * c) * (t - 1) := mul_nonneg (by linarith) hs
  have h2 : 0 ≤ (3 - 2 * c) * (t - 1) ^ 2 := mul_nonneg (by linarith) (sq_nonneg _)
  have h3 : 0 ≤ (t - 1) ^ 3 := pow_nonneg hs 3
  rw [hid]; linarith

/-- **No real root of `unitCubic c` reaches `1`**, for every `c ≤ 1`.

The measured max over the arc is `0.80193` (Route 36 G5), so the bound is true
but not tight. It does not need to be — `notCut` only asks for `< 1`. -/
theorem unitCubic_root_lt_one {c t : ℝ} (hc : c ≤ 1) (hp : unitCubic c t = 0) : t < 1 := by
  by_contra h
  push_neg at h
  have hpos := unitCubic_pos_of_one_le hc h
  rw [hp] at hpos
  exact lt_irrefl 0 hpos

/-- **`|x| = 1 → Re x ≤ 1`** — the hypothesis `c ≤ 1` above, supplied on the arc. -/
theorem re_le_one_of_normSq_eq_one {x : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) : x.re ≤ 1 := by
  nlinarith [sq_nonneg x.im, sq_nonneg (x.re - 1)]

/-! ### 2. The two relations that carry the argument -/

/-- `2c·t(t−1) = t³ + t − 1`, i.e. `p(t) = 0` solved for the `c`-terms. -/
theorem two_c_rel {c t : ℝ} (hp : unitCubic c t = 0) :
    2 * c * (t * (t - 1)) = t ^ 3 + t - 1 := by unfold unitCubic at hp; linear_combination -hp

/-- **`β·t(1−t) = W`**, where `β = t − 2c` is the quadratic factor's linear
coefficient and `W = t² + t − 1`. Since `t(1−t) > 0` on `(0,1)`, `β` and `W`
have the same sign — which is how step 3 turns a statement about the
discriminant into a statement about the roots. -/
theorem beta_rel {c t : ℝ} (hp : unitCubic c t = 0) :
    (t - 2 * c) * (t * (1 - t)) = t ^ 2 + t - 1 := by
  unfold unitCubic at hp; linear_combination -hp

/-- `t·γ = 1` for the quadratic factor's constant term `γ = t² − 2ct + 2c + 1`. -/
theorem gamma_rel {c t : ℝ} (hp : unitCubic c t = 0) :
    t * (t ^ 2 - 2 * c * t + 2 * c + 1) = 1 := by unfold unitCubic at hp; linear_combination hp

/-- **`c ≤ 1` forces the root above `2/5`.**

`c ≤ 1` gives `t³ − 2t² + 3t − 1 ≥ 0` (multiplying by `t(t−1) < 0` flips), and
that cubic is strictly increasing with value `−7/125` at `2/5`. -/
theorem two_fifths_lt {c t : ℝ} (hc : c ≤ 1) (ht0 : 0 < t) (ht1 : t < 1)
    (hp : unitCubic c t = 0) : 2 / 5 < t := by
  have hneg : t * (t - 1) < 0 := by nlinarith
  have hcub : 0 ≤ t ^ 3 - 2 * t ^ 2 + 3 * t - 1 := by nlinarith [two_c_rel hp]
  nlinarith [sq_nonneg (t - 4 / 5), hcub]

/-- **If the other two roots are real, then `W ≥ 0`.**

The step with content. `hD` is the quadratic's discriminant, which is
nonnegative exactly when it has a real root. Rearranged it says
`W² ≥ 4t(1−t)²`; but `W < 0` caps `t` at the golden section while `c ≤ 1` floors
it at `2/5`, and on `(2/5, (√5−1)/2)` the quartic `4t(1−t)² − W²` is positive. -/
theorem W_nonneg_of_disc_nonneg {c t : ℝ} (hc : c ≤ 1) (ht0 : 0 < t) (ht1 : t < 1)
    (hp : unitCubic c t = 0)
    (hD : 0 ≤ (t - 2 * c) ^ 2 - 4 * (t ^ 2 - 2 * c * t + 2 * c + 1)) :
    0 ≤ t ^ 2 + t - 1 := by
  by_contra hcon
  push_neg at hcon
  have h25 : 2 / 5 < t := two_fifths_lt hc ht0 ht1 hp
  have hb := beta_rel hp
  have hconst := gamma_rel hp
  have ht1t : 0 < t * (1 - t) := by nlinarith
  have hpos : 0 < (t * (1 - t)) ^ 2 := pow_pos ht1t 2
  have hkey : 4 * t * (1 - t) ^ 2 ≤ (t ^ 2 + t - 1) ^ 2 := by
    nlinarith [mul_nonneg hD hpos.le, hb, hconst, sq_nonneg (t * (1 - t))]
  nlinarith [hkey, h25, hcon, sq_nonneg (t - 1 / 2)]

/-- **Every real root of the cubic other than `t` is negative.** A corollary of
the above, recorded because it is the statement one wants to quote. -/
theorem real_root_neg_of_ne {c t r : ℝ} (hc : c ≤ 1) (ht0 : 0 < t) (ht1 : t < 1)
    (hpt : unitCubic c t = 0) (hpr : unitCubic c r = 0) (hne : r ≠ t) : r < 0 := by
  have hq : r ^ 2 + (t - 2 * c) * r + (t ^ 2 - 2 * c * t + 2 * c + 1) = 0 := by
    have hfac : (r - t) * (r ^ 2 + (t - 2 * c) * r + (t ^ 2 - 2 * c * t + 2 * c + 1)) = 0 := by
      unfold unitCubic at hpt hpr; linear_combination hpr - hpt
    rcases mul_eq_zero.mp hfac with h | h
    · exact absurd (sub_eq_zero.mp h) hne
    · exact h
  have hconst := gamma_rel hpt
  have hconstpos : 0 < t ^ 2 - 2 * c * t + 2 * c + 1 := by nlinarith
  have hD : 0 ≤ (t - 2 * c) ^ 2 - 4 * (t ^ 2 - 2 * c * t + 2 * c + 1) := by
    nlinarith [sq_nonneg (2 * r + (t - 2 * c))]
  have hW := W_nonneg_of_disc_nonneg hc ht0 ht1 hpt hD
  have hb := beta_rel hpt
  have ht1t : 0 < t * (1 - t) := by nlinarith
  have hbeta : 0 ≤ t - 2 * c := by nlinarith
  by_contra hcon
  push_neg at hcon
  nlinarith

/-! ### Gap A (a): the IFT's non-degeneracy, PROVED rather than measured

`exists_hasDerivAt_root` gives a locally differentiable root labelling wherever
`curveDy ≠ 0`. Route 32 G8 *measured* `|∂p/∂y| ≥ 1.75` at the real root on the
arc; below it is proved, and the `1.75` turns out to be exactly `7/4` with a
closed-form source.

On `|x| = 1` the curve is `x · unitCubic c`, so `curveDy = x·(3t² − 4ct + 2c+1)`
and — `x ≠ 0` — the non-degeneracy is a statement about the real cubic alone.
-/

/-- The `y`-derivative of `unitCubic`, times `t(1−t)`, is a **`c`-free quartic**.
The root relation eliminates `c` entirely. -/
theorem unitCubic_deriv_mul {c t : ℝ} (hp : unitCubic c t = 0) :
    (3 * t ^ 2 - 4 * c * t + (2 * c + 1)) * (t * (1 - t))
      = -t ^ 4 + 2 * t ^ 3 + t ^ 2 - 2 * t + 1 := by
  unfold unitCubic at hp
  linear_combination (1 - 2 * t) * hp

/-- **`∂p/∂y ≥ 7/4` at the real root** — so the IFT applies, and the `1.75`
Route 32 G8 measured is exactly `7/4`.

Two exact facts do it: the quartic satisfies
`q(t) − 7/16 = (2t−1)²(9 + 4t − 4t²)/16 ≥ 0` on `(0,1)`, and `t(1−t) ≤ 1/4`.
Dividing, `∂p/∂y ≥ (7/16)/(1/4) = 7/4`. Equality would need `t = 1/2`, which is
excluded by `two_fifths_lt` only in the weak sense — the bound holds regardless. -/
theorem unitCubic_deriv_ge {c t : ℝ} (ht0 : 0 < t) (ht1 : t < 1)
    (hp : unitCubic c t = 0) :
    7 / 4 ≤ 3 * t ^ 2 - 4 * c * t + (2 * c + 1) := by
  have hmul := unitCubic_deriv_mul hp
  have h1t : (0 : ℝ) < 1 - t := by linarith
  have htt : (0 : ℝ) < t * (1 - t) := mul_pos ht0 h1t
  -- `q(t) ≥ 7/16`, from the exact factorisation
  have hq : (7 : ℝ) / 16 ≤ -t ^ 4 + 2 * t ^ 3 + t ^ 2 - 2 * t + 1 := by
    nlinarith [sq_nonneg (2 * t - 1), mul_pos ht0 h1t, sq_nonneg t]
  -- `t(1−t) ≤ 1/4`
  have hle : t * (1 - t) ≤ 1 / 4 := by nlinarith [sq_nonneg (2 * t - 1)]
  nlinarith [hmul, hq, hle, htt]

/-- **The IFT's hypothesis holds at the real root**, in the form
`exists_hasDerivAt_root` consumes: `3t² − 4ct + 2c+1 ≠ 0`. -/
theorem unitCubic_deriv_ne_zero {c t : ℝ} (ht0 : 0 < t) (ht1 : t < 1)
    (hp : unitCubic c t = 0) :
    3 * t ^ 2 - 4 * c * t + (2 * c + 1) ≠ 0 := by
  have := unitCubic_deriv_ge ht0 ht1 hp
  intro h
  rw [h] at this
  linarith

end QOU.QBeta.FiveTwoDeformedSaddle
