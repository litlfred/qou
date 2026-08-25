import QOU.MathlibExt.ComplexDilogarithmOnCut
import QOU.Archimedean.LiTwoNegOne
import Mathlib.Analysis.Convex.PathConnected
import Mathlib.Analysis.Complex.Convex

/-!
# `Re Li₂` is continuous **across** the cut `(1,∞)` — Route 36 G11, closed

Bean `qou-glbl`, obligation (2). `envelope_integrate` wants
`ContinuousOn S (Icc 0 π)` — the **closed** interval — and at `φ = π` two of the
three `Li₂` arguments land exactly on the cut, at `w₀ = 1 + 2cos(2π/7) =
2.2469796`. So the transport needs `Li₂` continuous *at a point of its own cut*.

    continuousAt_re_cLiTwoExt (hx : 1 < x) :
      ContinuousAt (fun w : ℂ => (cLiTwoExt w).re) (x : ℂ)

## ⚠ The recorded next step was not merely unpriced — it could not work

G11 left the residue as "**dominated convergence alone** — a uniform integrable
bound for `‖log(1−wt)/t‖` near `w₀`". **No such bound exists.** The integrand's
logarithmic singularity sits at `t = 1/w` and *moves with `w`*: for every `t`
near `1/w₀` the point `w = 1/t` is real, lies in the approach set, and makes
`|log(1−wt)|` infinite. So the pointwise supremum over any neighbourhood is `+∞`
at a whole interval of `t`, and a `w`-independent dominating function is not
available at any strength. Vitali / uniform integrability would do it; Mathlib
does not have it in a usable shape.

Route 37 G11-successor records this. It is the difference between "not yet
priced" and "priced wrong": the previous revision named a *technique*, and the
technique was the thing that was false.

## What replaces it, and why it is cheap

The **inversion formula** on `ℂ ∖ [0,∞)`:

    Li₂(w) + Li₂(1/w) + ½·log(−w)² = −π²/6

Read as `Li₂(w) = −π²/6 − Li₂(1/w) − ½·log(−w)²`, every term on the right is
harmless at `w₀`:

* `1/w₀ = 0.445` is an **interior** point of `ℂ ∖ [1,∞)`, where `cLiTwoExt` is
  already known analytic (`analyticOnNhd_cLiTwoExt`), hence continuous;
* `log(−w)²` is **elementary**, and its only discontinuity at `w₀` is in the
  imaginary part.

`envelopeS` takes `.re` of every term, and `Re log(−w)²` is continuous across
the positive reals — `arg(−w)` jumps by `2π` there but

    Re(log(−w)²) = (log‖w‖)² − (|arg w| − π)²                 `re_log_neg_sq`

and `|arg w|` does not jump. That single rewrite is what carries the theorem.

## The four pieces

| piece | why it is not free |
|---|---|
| `invDomain = ℂ ∖ [0,∞)` is **connected** | the constant is pinned at `−1`, an interior point; on a half plane the only computable base point is on the boundary |
| `log(1−1/w) + log(−w) = log(1−w)` | needs `arg(1−1/w) + arg(−w) ∈ (−π,π]`, which is **false on `(0,1)`** |
| `invCombo` is constant | `IsOpen.is_const_of_fderiv_eq_zero`, with the derivative cancelling by the line above |
| the value on the cut itself | `re_inversion_identity` — already proved, for real `x ≥ 1` only, which is why only `.re` is claimed there |

The real-part restriction is not a convenience. `cLiTwoExt` **jumps** by
`2πi·log x` across the cut (Route 37 G4 measures it, ≈ 9.45 at `x = 4.5`), so a
statement about `cLiTwoExt` unqualified would be false.

## ⚠ Which boundary value Lean's branch computes

Lean's `Complex.log` takes `arg = +π` on the negative reals, and for real
`x > 1` the integrand's `1 − x·t` is a negative real once `t > 1/x`. So
`cLiTwoExt x` is the boundary value from **below**, `Li₂(x − i0)`, with
`Im = −π·log x`. Route 37 G3 pins this against the independently known jump
`Li₂(x+i0) − Li₂(x−i0) = 2πi·log x`; getting it backwards flips the sign of the
`log(−w)²` correction while leaving every other check self-consistent.

Route 37, 11 gates, all pass. G0 is a regression gate on the quadrature split
(the reference integral is wrong without it, and this lane has shipped a partial
version of that fix before). G4 and G8 are gated on the **ratio** `gap/ε` over
six decades, not on a small residual at the finest sample.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.MathlibExt

open Complex Filter Topology

/-! ## The domain `ℂ ∖ [0,∞)` -/

/-- **`ℂ ∖ [0,∞)`**, the domain of the inversion formula: the slit plane
reflected through the origin. Taking it as `-slitPlane` rather than as a raw
`setOf` is what makes `starConvex_one_slitPlane.neg` apply, and connectedness is
the only nontrivial thing needed of it. -/
def invDomain : Set ℂ := -Complex.slitPlane

theorem mem_invDomain_iff {w : ℂ} : w ∈ invDomain ↔ (w.re < 0 ∨ w.im ≠ 0) := by
  simp only [invDomain, Set.mem_neg, Complex.mem_slitPlane_iff, Complex.neg_re,
    Complex.neg_im, neg_pos, neg_ne_zero]

theorem neg_mem_slitPlane_of_mem_invDomain {w : ℂ} (hw : w ∈ invDomain) :
    -w ∈ Complex.slitPlane := hw

theorem isOpen_invDomain : IsOpen invDomain :=
  Complex.isOpen_slitPlane.preimage continuous_neg

theorem neg_one_mem_invDomain : (-1 : ℂ) ∈ invDomain := by
  rw [mem_invDomain_iff]
  norm_num

/-- **`ℂ ∖ [0,∞)` is connected.** It is star-shaped about `−1`, being the image
of the slit plane — star-shaped about `1` — under negation. This is what lets
the constant be pinned at an *interior* point; on a half plane the only base
point where `invCombo` is computable sits on the boundary, and the constant
would have to be recovered by a limit. -/
theorem isPreconnected_invDomain : IsPreconnected invDomain :=
  ((Complex.starConvex_one_slitPlane.neg).isPathConnected
    neg_one_mem_invDomain).isConnected.isPreconnected

theorem ne_zero_of_mem_invDomain {w : ℂ} (hw : w ∈ invDomain) : w ≠ 0 := by
  rintro rfl
  rcases mem_invDomain_iff.1 hw with h | h <;> simp at h

theorem mem_notCut_of_mem_invDomain {w : ℂ} (hw : w ∈ invDomain) : w ∈ notCut := by
  rcases mem_invDomain_iff.1 hw with h | h
  · exact Or.inr (by linarith)
  · exact Or.inl h

theorem inv_mem_invDomain {w : ℂ} (hw : w ∈ invDomain) : w⁻¹ ∈ invDomain := by
  have hw0 : w ≠ 0 := ne_zero_of_mem_invDomain hw
  have hns : 0 < Complex.normSq w := Complex.normSq_pos.2 hw0
  rw [mem_invDomain_iff] at hw ⊢
  rcases hw with h | h
  · exact Or.inl (by rw [Complex.inv_re]; exact div_neg_of_neg_of_pos h hns)
  · refine Or.inr ?_
    rw [Complex.inv_im]
    exact div_ne_zero (neg_ne_zero.2 h) (ne_of_gt hns)

/-- `1 − 1/w` never lands on `log`'s cut when `w` avoids `[0,∞)`. Needed twice:
to know `log (1 − 1/w)` is not the junk value, and — through
`arg_nonpos_of_mem_slitPlane` — to bound its argument. -/
theorem one_sub_inv_mem_slitPlane {w : ℂ} (hw : w ∈ invDomain) :
    1 - w⁻¹ ∈ Complex.slitPlane := by
  have hw0 : w ≠ 0 := ne_zero_of_mem_invDomain hw
  have hns : 0 < Complex.normSq w := Complex.normSq_pos.2 hw0
  by_cases hi : w.im = 0
  · -- `w` is a negative real, so `1 − 1/w > 1`
    have hre : w.re < 0 := (mem_invDomain_iff.1 hw).resolve_right (by simpa using hi)
    refine Or.inl ?_
    have hsq : Complex.normSq w = w.re * w.re := by
      simp [Complex.normSq_apply, hi]
    have : (1 - w⁻¹).re = 1 - w.re / Complex.normSq w := by
      simp [Complex.sub_re, Complex.inv_re]
    rw [this, hsq]
    have : w.re / (w.re * w.re) < 0 := by
      rw [div_mul_eq_div_div_swap, div_self (ne_of_lt hre)]
      exact one_div_neg.2 hre
    linarith
  · refine Or.inr ?_
    have : (1 - w⁻¹).im = w.im / Complex.normSq w := by
      simp [Complex.sub_im, Complex.inv_im, neg_div]
    rw [this]
    exact div_ne_zero hi (ne_of_gt hns)

/-! ## The one non-formal step: `log (1 − 1/w) + log (−w) = log (1 − w)` -/

/-- On the slit plane, `arg ≤ 0` is equivalent to `Im ≤ 0` — the `Im = 0` case
being carried by `Re > 0`. **Off** the slit plane it is false (`arg = π` at a
negative real, whose imaginary part is `0`), which is exactly why `invDomain`
cannot be widened. -/
theorem arg_nonpos_of_mem_slitPlane {z : ℂ} (hz : z ∈ Complex.slitPlane)
    (him : z.im ≤ 0) : z.arg ≤ 0 := by
  rcases lt_or_eq_of_le him with h | h
  · exact (Complex.arg_neg_iff.2 h).le
  · have hre : 0 < z.re := hz.resolve_right (by simp [h])
    exact le_of_eq (Complex.arg_eq_zero_iff.2 ⟨hre.le, h⟩)

/-- **The additive law for the two logarithms in the inversion derivative.**

`(1 − 1/w)·(−w) = 1 − w` is algebra; that the *principal* logarithms add is not.
It needs `arg (1 − 1/w) + arg (−w) ∈ (−π, π]`, and the two arguments have
strictly **opposite** signs throughout `ℂ ∖ [0,∞)` — `Im (1 − 1/w) = Im w/‖w‖²`
against `Im (−w) = −Im w` — so the sum is trapped between them.

⚠ The hypothesis is load-bearing. On `(0,1)` both arguments are `+π` and the sum
is `2π`: Route 37 G5 checks that the law **fails** there, so dropping `invDomain`
gives a false lemma rather than a harder one. -/
theorem log_one_sub_inv_add_log_neg {w : ℂ} (hw : w ∈ invDomain) :
    Complex.log (1 - w⁻¹) + Complex.log (-w) = Complex.log (1 - w) := by
  have hw0 : w ≠ 0 := ne_zero_of_mem_invDomain hw
  have hns : 0 < Complex.normSq w := Complex.normSq_pos.2 hw0
  have hs1 : 1 - w⁻¹ ∈ Complex.slitPlane := one_sub_inv_mem_slitPlane hw
  have hs2 : -w ∈ Complex.slitPlane := neg_mem_slitPlane_of_mem_invDomain hw
  have hne1 : (1 : ℂ) - w⁻¹ ≠ 0 := Complex.slitPlane_ne_zero hs1
  have hne2 : (-w : ℂ) ≠ 0 := neg_ne_zero.2 hw0
  have him1 : (1 - w⁻¹).im = w.im / Complex.normSq w := by
    simp [Complex.sub_im, Complex.inv_im, neg_div]
  have him2 : (-w).im = -w.im := by simp
  have harg : (1 - w⁻¹).arg + (-w).arg ∈ Set.Ioc (-Real.pi) Real.pi := by
    constructor
    · rcases le_total 0 w.im with h | h
      · have h1 : 0 ≤ (1 - w⁻¹).arg :=
          Complex.arg_nonneg_iff.2 (by rw [him1]; positivity)
        have h2 : -Real.pi < (-w).arg := Complex.neg_pi_lt_arg _
        linarith
      · have h1 : -Real.pi < (1 - w⁻¹).arg := Complex.neg_pi_lt_arg _
        have h2 : 0 ≤ (-w).arg := Complex.arg_nonneg_iff.2 (by rw [him2]; linarith)
        linarith
    · rcases le_total 0 w.im with h | h
      · have h1 : (1 - w⁻¹).arg ≤ Real.pi := Complex.arg_le_pi _
        have h2 : (-w).arg ≤ 0 :=
          arg_nonpos_of_mem_slitPlane hs2 (by rw [him2]; linarith)
        linarith
      · have h1 : (1 - w⁻¹).arg ≤ 0 := by
          refine arg_nonpos_of_mem_slitPlane hs1 ?_
          rw [him1]
          exact div_nonpos_of_nonpos_of_nonneg h hns.le
        have h2 : (-w).arg ≤ Real.pi := Complex.arg_le_pi _
        linarith
  have hprod : ((1 : ℂ) - w⁻¹) * (-w) = 1 - w := by
    field_simp
    ring
  rw [← Complex.log_mul hne1 hne2 harg, hprod]

/-! ## The inversion combination and its constancy -/

/-- `invCombo w = Li₂(w) + Li₂(1/w) + ½·log(−w)²`. Constant on `ℂ ∖ [0,∞)`. -/
noncomputable def invCombo (w : ℂ) : ℂ :=
  cLiTwoExt w + cLiTwoExt w⁻¹ + Complex.log (-w) ^ 2 / 2

/-- **The derivative of the inversion combination vanishes on `ℂ ∖ [0,∞)`.**

Three derivatives, each already in the tree or in Mathlib, whose sum is
`(−log(1−w) + log(1−1/w) + log(−w))/w`. The bracket vanishes by
`log_one_sub_inv_add_log_neg`, and that is the entire content. -/
theorem hasDerivAt_invCombo {w : ℂ} (hw : w ∈ invDomain) : HasDerivAt invCombo 0 w := by
  have hw0 : w ≠ 0 := ne_zero_of_mem_invDomain hw
  have hnc : w ∈ notCut := mem_notCut_of_mem_invDomain hw
  have hwi : w⁻¹ ∈ invDomain := inv_mem_invDomain hw
  have hnci : w⁻¹ ∈ notCut := mem_notCut_of_mem_invDomain hwi
  have hwi0 : w⁻¹ ≠ 0 := inv_ne_zero hw0
  have hs2 : -w ∈ Complex.slitPlane := neg_mem_slitPlane_of_mem_invDomain hw
  have d1 : HasDerivAt cLiTwoExt (-(Complex.log (1 - w) / w)) w :=
    hasDerivAt_cLiTwoExt' hnc hw0
  have d2 : HasDerivAt (fun z : ℂ => cLiTwoExt z⁻¹)
      (-(Complex.log (1 - w⁻¹) / w⁻¹) * -(w ^ 2)⁻¹) w :=
    (hasDerivAt_cLiTwoExt' hnci hwi0).comp w (hasDerivAt_inv hw0)
  have dneg : HasDerivAt (fun z : ℂ => -z) (-1 : ℂ) w := (hasDerivAt_id w).neg
  have dlog : HasDerivAt (fun z : ℂ => Complex.log (-z)) (-1 / -w) w := dneg.clog hs2
  have d3 : HasDerivAt (fun z : ℂ => Complex.log (-z) ^ 2 / 2)
      (2 * Complex.log (-w) ^ 1 * (-1 / -w) / 2) w := (dlog.pow 2).div_const 2
  have hval : -(Complex.log (1 - w) / w)
      + -(Complex.log (1 - w⁻¹) / w⁻¹) * -(w ^ 2)⁻¹
      + 2 * Complex.log (-w) ^ 1 * (-1 / -w) / 2 = 0 := by
    rw [← log_one_sub_inv_add_log_neg hw]
    field_simp
    ring
  have := (d1.add d2).add d3
  rwa [hval] at this

/-- **The inversion identity, as a full complex equation on `ℂ ∖ [0,∞)`.**

Route 37 G2 checks it at 16 points — both half planes, the negative reals, both
sides of the cut, near the branch point, and far out — all chosen *off* the 5₂
arc configuration, so nothing peculiar to that locus can be carrying it.

The base point is `−1`, where both dilogarithm terms are `cLiTwoExt (−1) =
−π²/12` (`cLiTwoExt_neg_one`) and `log 1 = 0` kills the third. -/
theorem invCombo_eq {w : ℂ} (hw : w ∈ invDomain) :
    invCombo w = -((Real.pi ^ 2 / 6 : ℝ) : ℂ) := by
  have hconst : invCombo w = invCombo (-1) := by
    refine isOpen_invDomain.is_const_of_fderiv_eq_zero isPreconnected_invDomain
      (fun z hz => ((hasDerivAt_invCombo hz).differentiableAt).differentiableWithinAt)
      (fun z hz => ?_) hw neg_one_mem_invDomain
    simp only [Pi.zero_apply]
    rw [(hasDerivAt_invCombo hz).hasFDerivAt.fderiv]
    ext
    simp
  rw [hconst]
  have hinv : (-1 : ℂ)⁻¹ = -1 := by norm_num
  have hlog : Complex.log (-(-1 : ℂ)) = 0 := by norm_num
  simp only [invCombo, hinv, hlog, QOU.Archimedean.cLiTwoExt_neg_one]
  push_cast
  ring

/-! ## The value on the cut itself, from `re_inversion_identity` -/

/-- `Complex.log` of a negative real, in the form the real part needs. -/
theorem log_neg_ofReal {x : ℝ} (hx : 0 < x) :
    Complex.log (-((x : ℝ) : ℂ)) = ((Real.log x : ℝ) : ℂ) + Real.pi * Complex.I := by
  have hneg : (-((x : ℝ) : ℂ)) = ((-x : ℝ) : ℂ) := by push_cast; ring
  have hnorm : ‖((-x : ℝ) : ℂ)‖ = x := by
    rw [Complex.norm_real, Real.norm_eq_abs,
      abs_of_neg (by linarith : (-x : ℝ) < 0), neg_neg]
  rw [Complex.log, hneg, Complex.arg_ofReal_of_neg (by linarith), hnorm]

/-- `(z / 2).re = z.re / 2`. Stated once rather than re-`simp`ed at each use. -/
theorem re_div_two (z : ℂ) : (z / 2).re = z.re / 2 := by simp

/-- **`Re (invCombo x) = −π²/6` for real `x ≥ 1`** — i.e. *on the cut*, where
`invCombo_eq` does not reach.

This is `re_inversion_identity` rearranged, and it is the reason only the real
part is claimed here: the imaginary part of `cLiTwoExt` on the cut is
`−π·log x`, which the tree does not prove. -/
theorem re_invCombo_ofReal {x : ℝ} (hx : 1 ≤ x) :
    (invCombo ((x : ℝ) : ℂ)).re = -(Real.pi ^ 2 / 6) := by
  have hx0 : (0 : ℝ) < x := lt_of_lt_of_le zero_lt_one hx
  have hinv : (((x : ℝ) : ℂ))⁻¹ = (((1 / x : ℝ)) : ℂ) := by
    rw [one_div, Complex.ofReal_inv]
  have hsq : (Complex.log (-((x : ℝ) : ℂ)) ^ 2).re = Real.log x ^ 2 - Real.pi ^ 2 := by
    rw [log_neg_ofReal hx0, pow_two, Complex.mul_re]
    simp [Complex.add_re, Complex.add_im]
    ring
  have hmain := re_inversion_identity hx
  simp only [invCombo, Complex.add_re, hinv, re_div_two, hsq]
  linarith

/-- **`Re (invCombo w) = −π²/6` on an open neighbourhood of the cut.**

The two clauses tile a full neighbourhood of any real `x > 1`: nearby points are
either off the real axis — where `invCombo_eq` applies — or real with real part
above `1`, where `re_invCombo_ofReal` does. That is what makes the continuity
below **two-sided** rather than one-sided; Route 37 G8 measures that the
transport needs both sides, `x·y` reaching `w₀` from below and `y/x` from above. -/
theorem re_invCombo_eq {w : ℂ} (hw : w.im ≠ 0 ∨ 1 < w.re) :
    (invCombo w).re = -(Real.pi ^ 2 / 6) := by
  by_cases him : w.im = 0
  · have h1 : 1 < w.re := hw.resolve_left (by simpa using him)
    have hw' : w = ((w.re : ℝ) : ℂ) := by
      apply Complex.ext <;> simp [him]
    rw [hw']
    exact re_invCombo_ofReal h1.le
  · rw [invCombo_eq (mem_invDomain_iff.2 (Or.inr him)), Complex.neg_re, Complex.ofReal_re]

/-! ## `Re log(−w)²` is continuous across the positive reals -/

/-- **The rewrite that carries the theorem.** `arg (−w)` jumps by `2π` across
the positive reals; `|arg w|` does not jump there at all, and

    Re(log(−w)²) = (log‖w‖)² − (|arg w| − π)²

holds for **every** `w ≠ 0`, including on both jump loci. Route 37 G6 checks it
*on* the positive and negative reals, not merely near them. -/
theorem re_log_neg_sq {w : ℂ} (hw : w ≠ 0) :
    (Complex.log (-w) ^ 2).re = Real.log ‖w‖ ^ 2 - (|Complex.arg w| - Real.pi) ^ 2 := by
  have hsq : (Complex.log (-w) ^ 2).re
      = (Complex.log (-w)).re ^ 2 - (Complex.log (-w)).im ^ 2 := by
    rw [pow_two, Complex.mul_re]; ring
  rw [hsq, Complex.log_re, norm_neg, Complex.log_im]
  congr 1
  rcases lt_trichotomy w.im 0 with h | h | h
  · rw [Complex.arg_neg_eq_arg_add_pi_of_im_neg h,
      abs_of_neg (Complex.arg_neg_iff.2 h)]
    ring
  · rcases lt_trichotomy w.re 0 with hr | hr | hr
    · have h1 : Complex.arg w = Real.pi := Complex.arg_eq_pi_iff.2 ⟨hr, h⟩
      have h2 : Complex.arg (-w) = 0 :=
        Complex.arg_eq_zero_iff.2 ⟨by simp; linarith, by simp [h]⟩
      rw [h1, h2, abs_of_nonneg Real.pi_pos.le]
      ring
    · exact absurd (Complex.ext hr h) hw
    · have h1 : Complex.arg w = 0 := Complex.arg_eq_zero_iff.2 ⟨hr.le, h⟩
      have h2 : Complex.arg (-w) = Real.pi :=
        Complex.arg_eq_pi_iff.2 ⟨by simp; linarith, by simp [h]⟩
      rw [h1, h2]
      simp
  · rw [Complex.arg_neg_eq_arg_sub_pi_of_im_pos h,
      abs_of_nonneg (Complex.arg_nonneg_iff.2 h.le)]

theorem continuousAt_re_log_neg_sq {w : ℂ} (hw : 0 < w.re) :
    ContinuousAt (fun z : ℂ => (Complex.log (-z) ^ 2).re) w := by
  have hslit : w ∈ Complex.slitPlane := Or.inl hw
  have hw0 : w ≠ 0 := Complex.slitPlane_ne_zero hslit
  have hcont : ContinuousAt
      (fun z : ℂ => Real.log ‖z‖ ^ 2 - (|Complex.arg z| - Real.pi) ^ 2) w := by
    refine ContinuousAt.sub (ContinuousAt.pow ?_ 2) (ContinuousAt.pow ?_ 2)
    · exact (Real.continuousAt_log (norm_ne_zero_iff.2 hw0)).comp
        continuous_norm.continuousAt
    · exact ((Complex.continuousAt_arg hslit).abs).sub continuousAt_const
  refine hcont.congr ?_
  filter_upwards [isOpen_ne.mem_nhds hw0] with z hz
  exact (re_log_neg_sq hz).symm

/-! ## The theorem -/

/-- **`Re Li₂` is continuous at every point of the cut `(1,∞)`.**

Two-sided, which is what the transport needs: at `φ = π` the argument `x·y`
reaches the cut point from below and `y/x` reaches the *same* point from above
(Route 37 G8), so a one-sided statement would have to be proved twice.

`cLiTwoExt` itself is **not** continuous there — it jumps by `2πi·log x` — so
the `.re` is load-bearing rather than cosmetic. `envelopeS` takes `.re` of every
term, which is exactly what makes the endpoint reachable. -/
theorem continuousAt_re_cLiTwoExt {x : ℝ} (hx : 1 < x) :
    ContinuousAt (fun w : ℂ => (cLiTwoExt w).re) ((x : ℝ) : ℂ) := by
  have hx0 : (0 : ℝ) < x := lt_trans zero_lt_one hx
  have hne : ((x : ℝ) : ℂ) ≠ 0 := Complex.ofReal_ne_zero.2 (ne_of_gt hx0)
  -- the open neighbourhood on which the inversion formula is available
  set U : Set ℂ := {z : ℂ | z.im ≠ 0} ∪ {z : ℂ | 1 < z.re} with hU
  have hUopen : IsOpen U :=
    (isOpen_ne.preimage Complex.continuous_im).union
      (isOpen_lt continuous_const Complex.continuous_re)
  have hmem : ((x : ℝ) : ℂ) ∈ U := Or.inr (by simpa using hx)
  -- the continuous replacement
  have hcont : ContinuousAt (fun z : ℂ => -(Real.pi ^ 2 / 6) - (cLiTwoExt z⁻¹).re
      - (Complex.log (-z) ^ 2).re / 2) ((x : ℝ) : ℂ) := by
    refine ContinuousAt.sub (ContinuousAt.sub continuousAt_const ?_) ?_
    · have hmemnc : ((x : ℝ) : ℂ)⁻¹ ∈ notCut := by
        refine Or.inr ?_
        rw [← Complex.ofReal_inv, Complex.ofReal_re, inv_lt_one₀ hx0]
        exact hx
      refine Complex.continuous_re.continuousAt.comp ?_
      exact ContinuousAt.comp (g := cLiTwoExt) (f := fun z : ℂ => z⁻¹)
        ((analyticOnNhd_cLiTwoExt _ hmemnc).continuousAt) (continuousAt_inv₀ hne)
    · exact (continuousAt_re_log_neg_sq (by simpa using hx0)).div_const 2
  refine hcont.congr ?_
  filter_upwards [hUopen.mem_nhds hmem] with z hz
  have hzc : z.im ≠ 0 ∨ 1 < z.re := hz
  have := re_invCombo_eq hzc
  simp only [invCombo, Complex.add_re, re_div_two] at this
  linarith

end QOU.MathlibExt
