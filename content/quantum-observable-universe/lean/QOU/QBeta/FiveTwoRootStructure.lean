import QOU.QBeta.FiveTwoArgSector
import Mathlib.Topology.Order.IntermediateValue

/-!
# The root structure — the last open input to the branch pinning, closed

Bean `qou-trns`. `FiveTwoArgSector` reduced the branch pinning to two facts about
the roots of the deformed curve on `|x| = 1`, and stated them as hypotheses:

* there is a **real** root `t` with `0 < t < 1`;
* of the other two, one has `Im(x·y) ≤ 0`, and when `φ > π/2` both do.

This file proves them. On `|x| = 1` the `y`-cubic is real,

    p(Y) = Y³ − 2c·Y² + (2c+1)·Y − 1,     c = cos φ,

so everything below is real algebra plus one application of the intermediate
value theorem. No continuity in `φ`, no root tracking, no base point.

## The three steps

**1. `t ∈ (0,1)` exists.** `p(0) = −1 < 0 < 1 = p(1)`, so IVT
(`exists_root_mem_Ioo`). That `p(1) = 1` identically in `c` is what makes this
free — the `2c` terms cancel.

**2. Factor out `(Y − t)`.** The remaining quadratic is `Y² + βY + γ` with
`β = t − 2c` and `γ = t² − 2ct + 2c + 1`, and `t·γ = 1` (that *is* `p(t) = 0`).
Two consequences carry the whole argument:

    (t − 2c)·t(1−t) = t² + t − 1 =: W       (`beta_rel`)
    c ≤ 1  ⟹  t > 2/5                       (`two_fifths_lt`)

**3. Split on the quadratic's discriminant.**

*Real roots* (`β² ≥ 4γ`). Then `W ≥ 0` — `W_nonneg_of_disc_nonneg`, the one
step with content. Suppose not; `β² ≥ 4γ` rearranges to `W² ≥ 4t(1−t)²`, while
`W < 0` bounds `t` above by the golden section and `c ≤ 1` bounds it below by
`2/5`, and on that interval `4t(1−t)² − W²` is positive. With `W ≥ 0` we get
`β ≥ 0`, and `γ = 1/t > 0`, so **both roots are negative** and
`Im(x·y) = y·sin φ < 0` for each — the conjugate-pair inequality is not needed
here at all.

*Conjugate pair* (`β² < 4γ`). Then `y = a ± b i` with `a = −β/2`, `b > 0`, and
`a² + b² = γ`. The hypotheses of `sa_lt_cb` hold — `h1` is an identity given
`t·γ = 1`, and `h2` is `beta_rel` — so `Im(x·ȳ) = s·a − c·b < 0`. When `c < 0`
the other member follows, since `c·b < 0 < −c·b`.

## What this closes

The hypotheses `ht0`, `ht1`, `h3` and `hbig` of
`branchInt_eq_zero_of_roots` are now theorems, assembled in
`exists_pinning_data`, which also returns the factorisation
`p(Y) = (Y − t)(Y − y₂)(Y − y₃)` so that a consumer holding Vieta data can match
its roots against these.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
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

/-! ### 3. The other two roots, constructed -/

/-- The two roots of `Y² + βY + γ`, written down: a real pair when
`β² ≥ 4γ`, a conjugate pair otherwise. Explicit rather than abstract, because
the whole point is to read off the sign of `Im(x·y)`. -/
noncomputable def otherRoots (β γ : ℝ) : ℂ × ℂ :=
  if 0 ≤ β ^ 2 - 4 * γ then
    ((((-β + Real.sqrt (β ^ 2 - 4 * γ)) / 2 : ℝ) : ℂ),
     (((-β - Real.sqrt (β ^ 2 - 4 * γ)) / 2 : ℝ) : ℂ))
  else
    (((-β / 2 : ℝ) : ℂ) + ((Real.sqrt (4 * γ - β ^ 2) / 2 : ℝ) : ℂ) * Complex.I,
     ((-β / 2 : ℝ) : ℂ) - ((Real.sqrt (4 * γ - β ^ 2) / 2 : ℝ) : ℂ) * Complex.I)

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

/-- **`otherRoots` is continuous — including THROUGH the collision.**

Bean `qou-glbl` part (b). The formula is piecewise on the sign of `β² − 4γ`, and
that is exactly where the two roots collide. It is nonetheless continuous, for
the reason that makes Gap A tractable at all: at `β² − 4γ = 0` **both branches
give `(−β/2, −β/2)`** — `Real.sqrt 0 = 0` on one side, and the imaginary part
vanishes on the other.

So the *labelling* is continuous across the collision even though it is not
differentiable there. That is the asymmetry `qou-glbl` turns on: continuity
survives exactly what differentiability does not. -/
theorem continuous_otherRoots :
    Continuous (fun p : ℝ × ℝ => otherRoots p.1 p.2) := by
  unfold otherRoots
  have hsq : Continuous Real.sqrt := Real.continuous_sqrt
  refine Continuous.if_le ?_ ?_ continuous_const (by fun_prop) ?_
  · exact Continuous.prodMk (by fun_prop) (by fun_prop)
  · exact Continuous.prodMk (by fun_prop) (by fun_prop)
  · intro q hq
    -- on the boundary `0 = β² − 4γ`, both branches are `(−β/2, −β/2)`
    have h1 : q.1 ^ 2 - 4 * q.2 = 0 := hq.symm
    have h2 : 4 * q.2 - q.1 ^ 2 = 0 := by linarith
    simp [h1, h2, Real.sqrt_zero]

theorem otherRoots_sum (β γ : ℝ) : (otherRoots β γ).1 + (otherRoots β γ).2 = -β := by
  unfold otherRoots
  split_ifs <;> · push_cast; ring

theorem otherRoots_prod (β γ : ℝ) : (otherRoots β γ).1 * (otherRoots β γ).2 = γ := by
  unfold otherRoots
  split_ifs with h
  · have hs := Real.sq_sqrt h
    have hreal : ((-β + Real.sqrt (β ^ 2 - 4 * γ)) / 2) * ((-β - Real.sqrt (β ^ 2 - 4 * γ)) / 2)
        = γ := by linear_combination (-1 / 4 : ℝ) * hs
    rw [← Complex.ofReal_mul, hreal]
  · have h' : (0 : ℝ) ≤ 4 * γ - β ^ 2 := by linarith
    have hs := Real.sq_sqrt h'
    have hreal : (-β / 2) ^ 2 + (Real.sqrt (4 * γ - β ^ 2) / 2) ^ 2 = γ := by
      linear_combination (1 / 4 : ℝ) * hs
    have hc : ((-β / 2 : ℝ) : ℂ) ^ 2 + ((Real.sqrt (4 * γ - β ^ 2) / 2 : ℝ) : ℂ) ^ 2 = (γ : ℂ) := by
      exact_mod_cast congrArg (fun x : ℝ => (x : ℂ)) hreal
    linear_combination hc - ((Real.sqrt (4 * γ - β ^ 2) / 2 : ℝ) : ℂ) ^ 2 * Complex.I_sq

/-- The quadratic really does factor through these two. -/
theorem otherRoots_factor (β γ : ℝ) (Y : ℂ) :
    Y ^ 2 + β * Y + γ = (Y - (otherRoots β γ).1) * (Y - (otherRoots β γ).2) := by
  have hs := otherRoots_sum β γ
  have hp := otherRoots_prod β γ
  linear_combination (Y : ℂ) * hs - hp

/-! ### 4. The sign of `Im(x · y)` for the two extra roots -/

/-- **The lower extra root is pushed into the open lower half plane.**

Both branches land here: a negative real root gives `Im(x·y) = y·sin φ < 0`
directly, and the conjugate pair gives it from `sa_lt_cb`. -/
theorem im_mul_otherRoots_snd_neg {c t : ℝ} (hc : c ≤ 1) (ht0 : 0 < t) (ht1 : t < 1)
    (hp : unitCubic c t = 0) {x : ℂ} (hxre : x.re = c) (hxim : 0 < x.im)
    (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) :
    (x * (otherRoots (t - 2 * c) (t ^ 2 - 2 * c * t + 2 * c + 1)).2).im < 0 := by
  set β := t - 2 * c with hβdef
  set γ := t ^ 2 - 2 * c * t + 2 * c + 1 with hγdef
  have hconst := gamma_rel hp
  have hγpos : 0 < γ := by rw [hγdef]; nlinarith
  unfold otherRoots
  split_ifs with h
  · -- real pair: `β > 0` and `γ > 0`, so both roots are negative
    have hW := W_nonneg_of_disc_nonneg hc ht0 ht1 hp h
    have hb := beta_rel hp
    have ht1t : 0 < t * (1 - t) := by nlinarith
    have hβ0 : 0 < β := by
      rcases lt_or_eq_of_le (by nlinarith : (0:ℝ) ≤ β) with hlt | heq
      · exact hlt
      · exfalso; rw [← heq] at h; nlinarith
    have hs := Real.sq_sqrt h
    have hsnn : 0 ≤ Real.sqrt (β ^ 2 - 4 * γ) := Real.sqrt_nonneg _
    have hroot : (-β - Real.sqrt (β ^ 2 - 4 * γ)) / 2 < 0 := by linarith
    simp only [Complex.mul_im, Complex.ofReal_re, Complex.ofReal_im, mul_zero, zero_add]
    exact mul_neg_of_pos_of_neg hxim hroot
  · -- conjugate pair: this is exactly `sa_lt_cb`
    have h' : (0 : ℝ) ≤ 4 * γ - β ^ 2 := by linarith
    set b := Real.sqrt (4 * γ - β ^ 2) / 2 with hbdef
    have hb0 : 0 < b := by
      rw [hbdef]
      have : 0 < 4 * γ - β ^ 2 := by linarith
      positivity
    have hbsq : b ^ 2 = (4 * γ - β ^ 2) / 4 := by
      rw [hbdef, div_pow, Real.sq_sqrt h']; norm_num
    have hR : γ = (-β / 2) ^ 2 + b ^ 2 := by rw [hbsq]; ring
    have h1 : 2 * c * γ = 1 + 2 * (-β / 2) * γ := by
      rw [hβdef]; linear_combination hconst
    have h2 : 2 * (-β / 2) * (γ - 1) = γ ^ 2 - γ - 1 := by
      have hb' := beta_rel hp
      rw [hβdef, hγdef] at *
      nlinarith [hconst, hb', sq_nonneg t]
    have hkey := sa_lt_cb hb0 hxim hR (hxre ▸ h1) h2 hxnorm
    simp only [Complex.mul_im, Complex.sub_re, Complex.sub_im, Complex.ofReal_re,
      Complex.ofReal_im, Complex.mul_re, Complex.mul_im, Complex.I_re, Complex.I_im]
    rw [hxre]
    nlinarith [hkey]

/-- **The upper extra root too, once `c < 0`** — i.e. once `φ > π/2`.

In the real branch both roots are negative anyway, so `c < 0` is not used there.
In the conjugate branch it is exactly what turns `s·a < c·b` into
`c·b + s·a < 2c·b < 0`. -/
theorem im_mul_otherRoots_fst_neg {c t : ℝ} (hc : c ≤ 1) (hcneg : c < 0)
    (ht0 : 0 < t) (ht1 : t < 1)
    (hp : unitCubic c t = 0) {x : ℂ} (hxre : x.re = c) (hxim : 0 < x.im)
    (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) :
    (x * (otherRoots (t - 2 * c) (t ^ 2 - 2 * c * t + 2 * c + 1)).1).im < 0 := by
  set β := t - 2 * c with hβdef
  set γ := t ^ 2 - 2 * c * t + 2 * c + 1 with hγdef
  have hconst := gamma_rel hp
  have hγpos : 0 < γ := by rw [hγdef]; nlinarith
  unfold otherRoots
  split_ifs with h
  · have hW := W_nonneg_of_disc_nonneg hc ht0 ht1 hp h
    have hb := beta_rel hp
    have ht1t : 0 < t * (1 - t) := by nlinarith
    have hβ0 : 0 < β := by
      rcases lt_or_eq_of_le (by nlinarith : (0:ℝ) ≤ β) with hlt | heq
      · exact hlt
      · exfalso; rw [← heq] at h; nlinarith
    have hlt : Real.sqrt (β ^ 2 - 4 * γ) < β := (Real.sqrt_lt' hβ0).mpr (by nlinarith)
    have hroot : (-β + Real.sqrt (β ^ 2 - 4 * γ)) / 2 < 0 := by linarith
    simp only [Complex.mul_im, Complex.ofReal_re, Complex.ofReal_im, mul_zero, zero_add]
    exact mul_neg_of_pos_of_neg hxim hroot
  · have h' : (0 : ℝ) ≤ 4 * γ - β ^ 2 := by linarith
    set b := Real.sqrt (4 * γ - β ^ 2) / 2 with hbdef
    have hb0 : 0 < b := by
      rw [hbdef]
      have : 0 < 4 * γ - β ^ 2 := by linarith
      positivity
    have hbsq : b ^ 2 = (4 * γ - β ^ 2) / 4 := by
      rw [hbdef, div_pow, Real.sq_sqrt h']; norm_num
    have hR : γ = (-β / 2) ^ 2 + b ^ 2 := by rw [hbsq]; ring
    have h1 : 2 * c * γ = 1 + 2 * (-β / 2) * γ := by rw [hβdef]; linear_combination hconst
    have h2 : 2 * (-β / 2) * (γ - 1) = γ ^ 2 - γ - 1 := by
      have hb' := beta_rel hp
      rw [hβdef, hγdef] at *
      nlinarith [hconst, hb', sq_nonneg t]
    have hkey := sa_lt_cb hb0 hxim hR (hxre ▸ h1) h2 hxnorm
    have hcb : c * b < 0 := mul_neg_of_neg_of_pos hcneg hb0
    simp only [Complex.mul_im, Complex.add_re, Complex.add_im, Complex.ofReal_re,
      Complex.ofReal_im, Complex.mul_re, Complex.mul_im, Complex.I_re, Complex.I_im]
    rw [hxre]
    nlinarith [hkey, hcb]

/-! ### 5. The bridge, assembled -/

/-- **Everything `branchInt_eq_zero_of_roots` assumed about the roots, supplied.**

Returns the real root `t ∈ (0,1)`, the other two roots as complex numbers, the
factorisation certifying that these three *are* the roots — so a consumer
holding only Vieta data can match against them — and the two sign facts. -/
theorem exists_pinning_data {c : ℝ} (hc : c ≤ 1) {x : ℂ}
    (hxre : x.re = c) (hxim : 0 < x.im) (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) :
    ∃ (t : ℝ) (y₂ y₃ : ℂ), 0 < t ∧ t < 1 ∧
      (∀ Y : ℂ, Y ^ 3 - 2 * (c : ℂ) * Y ^ 2 + (2 * (c : ℂ) + 1) * Y - 1
        = (Y - (t : ℂ)) * (Y - y₂) * (Y - y₃)) ∧
      (x * y₃).im < 0 ∧ (c < 0 → (x * y₂).im < 0) := by
  obtain ⟨t, ⟨ht0, ht1⟩, hp⟩ := exists_root_mem_Ioo c
  refine ⟨t, (otherRoots (t - 2 * c) (t ^ 2 - 2 * c * t + 2 * c + 1)).1,
    (otherRoots (t - 2 * c) (t ^ 2 - 2 * c * t + 2 * c + 1)).2, ht0, ht1, ?_, ?_, ?_⟩
  · intro Y
    have hfac2 := otherRoots_factor (t - 2 * c) (t ^ 2 - 2 * c * t + 2 * c + 1) Y
    have htγ : (t : ℂ) * ((t ^ 2 - 2 * c * t + 2 * c + 1 : ℝ) : ℂ) = 1 := by
      exact_mod_cast congrArg (fun r : ℝ => (r : ℂ)) (gamma_rel hp)
    push_cast at hfac2 htγ ⊢
    linear_combination htγ + (Y - (t : ℂ)) * hfac2
  · exact im_mul_otherRoots_snd_neg hc ht0 ht1 hp hxre hxim hxnorm
  · intro hcneg
    exact im_mul_otherRoots_fst_neg hc hcneg ht0 ht1 hp hxre hxim hxnorm

end QOU.QBeta.FiveTwoDeformedSaddle
