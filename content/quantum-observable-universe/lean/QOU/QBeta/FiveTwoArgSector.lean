import QOU.QBeta.FiveTwoBranchByArgument

/-!
# Pinning the branch integer by a SECTOR — Route 27's obligations, proved

Bean `qou-trns`. `FiveTwoBranchByArgument` traded `hcont` for three
real-algebraic inequalities *measured* along the arc (Route 27), with margins of
10% and 17% and no proof. This file discharges that trade: the obligations turn
out not to be needed in the measured form at all, because the bound they were
approximating is `φ`-dependent, and what is left is one inequality which is
proved here.

## Why the measured margins were an artefact

Route 27 confined `Σⱼ arg(1 − x·yⱼ)` to the *uniform* window `(−π, 2π)`, which
forces tight control on every individual argument — hence the tight margins. But
the window only has to exclude `φ ± 2π`, and it is free to depend on `φ`. With
`φ ∈ [0, π)` the window `(φ − 2π, φ + 2π)` suffices, and it is loose enough to be
reached from:

| input | source |
|---|---|
| `arg(1 − x·y₁) ∈ (−π/2, 0)`, `y₁` the positive real root | `‖x·y₁‖ = y₁ < 1`, so `Re(1 − x·y₁) > 0` |
| `arg(1 − x·y₃) ≥ 0` when `Im(x·y₃) ≤ 0` | `Complex.arg_nonneg_iff` |
| `arg(1 − x·y₂) ∈ (−π, π]` | free — `Complex.neg_pi_lt_arg`, `Complex.arg_le_pi` |
| and, **only** when `φ > π/2`, `arg(1 − x·y₂) ≥ 0` too | same as `y₃` |

`sum_window` turns those into `Σ ∈ (φ − 2π, φ + 2π)`, and
`branchInt_eq_zero_of_window` into `k = 0`. Two of the four inputs are free, and
the first needs only `0 < y₁ < 1` — which is `p(0) = −1 < 0 < 1 = p(1)` for the
monic cubic `Y³ − 2cY² + (2c+1)Y − 1`.

## The one real fact, and its proof

What is left is: *some* root has `Im(x·yⱼ) ≤ 0`, and when `φ > π/2`, *two* do. On
`|x| = 1` the cubic is real, so the roots are a real one plus either two reals or
a conjugate pair. Two reals: they are both **negative** (product `1`, sum
`2c < 0`), so `Im(x·y) = y·sin φ < 0` outright, and both qualify. A conjugate
pair `a ± b i`: the statement is

    s·a < c·b        (`sa_lt_cb`),   `c = cos φ`, `s = sin φ > 0`, `b > 0`

for the lower member, and when `c < 0` the upper member follows from it since
`c·b < 0 < −c·b`. That single inequality is Route 27's obligation — measured
there with `max(s·a − c·b) = −0.3365` and left open. It is proved here from two
Vieta consequences, `2cR = 1 + 2aR` and `2a(R−1) = R² − R − 1` with
`R = a² + b² = ‖y₂‖²`, by three sign certificates:

* `1 < R` (`one_lt_normSq`) — equivalently the real root is `< 1`. Otherwise
  `b² > 0` would force `4R(R−1)² > (R²−R−1)²`, impossible on `(0,1]` where the
  left side is at most `16/27` (certificate `(3R−1)²(4−3R) ≥ 0`) and the right
  side is at least `1`.
* `a > 0`: then `c > a > 0`, and `E := 1 + 4aR + 4a²R(R−1) > 0` termwise, giving
  `a² < c²R`.
* `a < 0 < −c`: then `E·(R−1) = R³(R−1)² − 1`, and
  `R³(R−1)² = (R³ − R²)·(R² − R)` is a product of **two factors in `(0,1)`** —
  the first below `1` because `c < 0`, the second because `a < 0` — so `E < 0`
  and `a² > c²R`.

`sq_gap` is the bridge: `(s·a)² − (c·b)² = a² − c²R` on the constraint set, so
the sign of `a² − c²R` decides the goal once the signs of `s·a` and `c·b` are
known.

## Status

This turns Route 27's three measured obligations into theorems, and removes the
margins from the argument entirely.

The remaining inputs — a real root in `(0,1)`, and the sign of `Im(x·yⱼ)` for the
other two — are stated as hypotheses here rather than assumed silently. They are
**proved** in `FiveTwoRootStructure` (`exists_pinning_data`), by IVT plus real
algebra; this file does not depend on that one, so the factoring stays honest.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Real Complex

/-! ### 1. The window arithmetic -/

/-- **The branch integer is `0` as soon as the argument sum lies in a window of
radius `2π` about `φ`.**

Weaker than `branchInt_eq_zero_of_bounds`, which fixes the window at `(−π, 2π)`;
here it may follow `φ`, and that is the whole gain. -/
theorem branchInt_eq_zero_of_window {S φ : ℝ} {k : ℤ}
    (hlo : φ - 2 * π < S) (hhi : S < φ + 2 * π) (h : S = φ + 2 * π * k) : k = 0 := by
  have hpi : (0 : ℝ) < π := Real.pi_pos
  have hk : |(k : ℝ)| < 1 := by
    rw [abs_lt]
    constructor <;> nlinarith
  have hkz : |k| < 1 := by exact_mod_cast hk
  exact Int.abs_lt_one_iff.mp hkz

/-- **The window, from the sector data.**

`a₁` is the argument at the positive real root, confined to `(−π/2, 0)` because
that root has modulus `< 1`. `a₃` is nonnegative. `a₂` is free — except when
`φ > π/2`, which is exactly where the slack below `φ − 2π` runs out. -/
theorem sum_window {a₁ a₂ a₃ φ : ℝ} (hφ0 : 0 ≤ φ) (hφπ : φ < π)
    (h1lo : -(π / 2) < a₁) (h1hi : a₁ < 0)
    (h2lo : -π < a₂) (h2hi : a₂ ≤ π)
    (h3lo : 0 ≤ a₃) (h3hi : a₃ ≤ π)
    (hbig : π / 2 < φ → 0 ≤ a₂) :
    φ - 2 * π < a₁ + a₂ + a₃ ∧ a₁ + a₂ + a₃ < φ + 2 * π := by
  refine ⟨?_, by linarith⟩
  rcases le_or_gt φ (π / 2) with h | h
  · linarith
  · have := hbig h; linarith

/-- **The pinning, from the sector data.** Compare
`branchDiff_eq_zero_of_continuousOn`, which needs continuity plus a base point,
and `branchInt_eq_zero_of_arg_structure`, which needs Route 27's three
inequalities: this needs neither. -/
theorem branchInt_eq_zero_of_sector {a₁ a₂ a₃ φ : ℝ} {k : ℤ}
    (hφ0 : 0 ≤ φ) (hφπ : φ < π)
    (h1lo : -(π / 2) < a₁) (h1hi : a₁ < 0)
    (h2lo : -π < a₂) (h2hi : a₂ ≤ π)
    (h3lo : 0 ≤ a₃) (h3hi : a₃ ≤ π)
    (hbig : π / 2 < φ → 0 ≤ a₂)
    (h : a₁ + a₂ + a₃ = φ + 2 * π * k) : k = 0 :=
  let ⟨hlo, hhi⟩ := sum_window hφ0 hφπ h1lo h1hi h2lo h2hi h3lo h3hi hbig
  branchInt_eq_zero_of_window hlo hhi h

/-! ### 2. The two argument inputs -/

/-- **The positive real root lands in the open right half plane.**

If `y₁ = t` is real with `0 < t < 1` and `x` sits on the unit circle with
`Im x > 0`, then `1 − t·x` has positive real part — because `‖t·x‖ = t < 1` — and
negative imaginary part, so its argument lies in `(−π/2, 0)`.

This is the only use of `y₁ < 1`, and it is what replaces Route 27's measured
minimum `−1.4077` against `−π/2`. -/
theorem arg_pos_real_root {x : ℂ} {t : ℝ}
    (hxim : 0 < x.im) (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) (ht0 : 0 < t) (ht1 : t < 1) :
    -(π / 2) < (1 - (t : ℂ) * x).arg ∧ (1 - (t : ℂ) * x).arg < 0 := by
  have hxre : x.re ≤ 1 := by nlinarith
  have him : (1 - (t : ℂ) * x).im < 0 := by
    simp only [Complex.sub_im, Complex.one_im, Complex.mul_im, Complex.ofReal_re,
      Complex.ofReal_im, zero_mul, add_zero, zero_sub, neg_lt_zero]
    positivity
  have hre : 0 < (1 - (t : ℂ) * x).re := by
    simp only [Complex.sub_re, Complex.one_re, Complex.mul_re, Complex.ofReal_re,
      Complex.ofReal_im, zero_mul, sub_zero, sub_pos]
    nlinarith
  refine ⟨?_, Complex.arg_neg_iff.mpr him⟩
  exact (abs_lt.mp (Complex.abs_arg_lt_pi_div_two_iff.mpr (Or.inl hre))).1

/-- **A root pushed into the closed lower half plane gives a nonnegative
argument.** -/
theorem arg_nonneg_of_im_nonpos {z : ℂ} (h : z.im ≤ 0) : 0 ≤ (1 - z).arg :=
  Complex.arg_nonneg_iff.mpr (by simpa using h)

/-! ### 3. The real-algebraic core -/

/-- The bridge: on the constraint set `(s·a)² − (c·b)² = a² − c²R`, so the sign of
`a² − c²R` decides `s·a` against `c·b` once their own signs are known. -/
theorem sq_gap {a b c s R : ℝ} (hR : R = a ^ 2 + b ^ 2) (hcs : c ^ 2 + s ^ 2 = 1) :
    (s * a) ^ 2 - (c * b) ^ 2 = a ^ 2 - c ^ 2 * R := by
  linear_combination a ^ 2 * hcs + c ^ 2 * hR

/-- From `v² < u²` with `u, v < 0`, conclude `u < v`. -/
theorem lt_of_sq_gt_of_neg {u v : ℝ} (hu : u < 0) (hv : v < 0) (h : v ^ 2 < u ^ 2) : u < v := by
  by_contra hcon
  push_neg at hcon
  nlinarith [mul_nonneg (neg_nonneg.mpr hu.le) (sub_nonneg.mpr hcon),
             mul_nonneg (neg_nonneg.mpr hv.le) (sub_nonneg.mpr hcon)]

/-- From `u² < v²` with `0 < u`, `0 < v`, conclude `u < v`. -/
theorem lt_of_sq_lt_of_pos {u v : ℝ} (hu : 0 < u) (hv : 0 < v) (h : u ^ 2 < v ^ 2) : u < v := by
  nlinarith

/-- **`‖y₂‖² > 1` for the conjugate pair** — equivalently, the real root `1/R` is
below `1`.

From the Vieta relation alone: `b² > 0` forces `4R(R−1)² > (R²−R−1)²`, and on
`(0,1]` the left side is at most `16/27` — certificate `(3R−1)²(4−3R) ≥ 0` —
while the right side is at least `1`. -/
theorem one_lt_normSq {a b R : ℝ} (hb : 0 < b) (hR : R = a ^ 2 + b ^ 2)
    (h2 : 2 * a * (R - 1) = R ^ 2 - R - 1) : 1 < R := by
  by_contra hcon
  push_neg at hcon
  have hRpos : 0 < R := by nlinarith [sq_nonneg a]
  rcases eq_or_lt_of_le hcon with h | hlt
  · rw [h] at h2; norm_num at h2
  · have hkey : (R ^ 2 - R - 1) ^ 2 < 4 * R * (R - 1) ^ 2 := by
      have hb2 : 0 < b ^ 2 := by positivity
      nlinarith [mul_pos hb2 (mul_pos (sub_pos.mpr hlt) (sub_pos.mpr hlt))]
    nlinarith [mul_nonneg (sq_nonneg (3 * R - 1)) (by linarith : (0:ℝ) ≤ 4 - 3 * R)]

/-- **Route 27's obligation, proved: `s·a < c·b`.**

`y₂ = a + b i` with `b > 0` is the upper member of the conjugate pair,
`R = ‖y₂‖²`, `c = cos φ`, `s = sin φ > 0`. The hypotheses are Vieta consequences:
`h1` is `e₁ = 2c` with the real root written as `1/R`, and `h2` is `e₂ − e₁ = 1`
cleared of denominators.

Route 27 measured `max(s·a − c·b) = −0.3365` over the arc and left this open.
Three sign certificates discharge it; see the module docstring. -/
theorem sa_lt_cb {a b c s R : ℝ} (hb : 0 < b) (hs : 0 < s)
    (hR : R = a ^ 2 + b ^ 2)
    (h1 : 2 * c * R = 1 + 2 * a * R)
    (h2 : 2 * a * (R - 1) = R ^ 2 - R - 1)
    (hcs : c ^ 2 + s ^ 2 = 1) :
    s * a < c * b := by
  have hR1 : 1 < R := one_lt_normSq hb hR h2
  have hRpos : 0 < R := by linarith
  have hR1' : 0 < R - 1 := sub_pos.mpr hR1
  have hgap := sq_gap hR hcs
  have hca : a < c := by
    have h : 2 * R * (c - a) = 1 := by linear_combination h1
    nlinarith
  -- `(2cR)² = (1+2aR)²` rewrites the sign of `a² − c²R` as the sign of `−E`.
  have hsqE : 4 * c ^ 2 * R ^ 2
      = 4 * a ^ 2 * R + (1 + 4 * a * R + 4 * a ^ 2 * R * (R - 1)) := by
    linear_combination (2 * c * R + 1 + 2 * a * R) * h1
  rcases le_or_gt a 0 with ha | ha
  · rcases le_or_gt 0 c with hc | hc
    · -- `s·a ≤ 0 ≤ c·b`, and they cannot both vanish: `a = 0` forces `c > 0`.
      rcases lt_or_eq_of_le ha with ha' | ha'
      · have h₁ : s * a < 0 := mul_neg_of_pos_of_neg hs ha'
        have h₂ : 0 ≤ c * b := mul_nonneg hc hb.le
        linarith
      · have hc0 : 0 < c := ha' ▸ hca
        have h₁ : s * a = 0 := by rw [ha']; ring
        have h₂ : 0 < c * b := mul_pos hc0 hb
        linarith
    · -- `a < 0 < −c`: `E < 0`, so `a² > c²R`, so `s·a < c·b` with both negative.
      have ha' : a < 0 := by
        rcases lt_or_eq_of_le ha with h | h
        · exact h
        · exfalso
          rw [h] at h1
          nlinarith [mul_neg_of_neg_of_pos hc hRpos]
      -- `R² − R < 1` because `a < 0`
      have hB : R ^ 2 - R < 1 := by nlinarith [mul_neg_of_neg_of_pos ha' hR1']
      -- `R³ − R² < 1` because `c < 0`
      have h2aR : 2 * a * R < -1 := by nlinarith [mul_neg_of_neg_of_pos hc hRpos]
      have h2Rid : 2 * a * R * (R - 1) = R ^ 3 - R ^ 2 - R := by linear_combination R * h2
      have hA : R ^ 3 - R ^ 2 < 1 := by nlinarith [mul_lt_mul_of_pos_right h2aR hR1']
      -- so `R³(R−1)² = (R³−R²)·(R²−R)` is a product of two factors in `(0,1)`
      have hApos : 0 < R ^ 3 - R ^ 2 := by nlinarith
      have hBpos : 0 < R ^ 2 - R := by nlinarith
      have hAB : R ^ 3 * (R - 1) ^ 2 < 1 := by
        have hfac : R ^ 3 * (R - 1) ^ 2 = (R ^ 3 - R ^ 2) * (R ^ 2 - R) := by ring
        rw [hfac]; nlinarith
      have hEid : (1 + 4 * a * R + 4 * a ^ 2 * R * (R - 1)) * (R - 1)
          = R ^ 3 * (R - 1) ^ 2 - 1 := by
        linear_combination (2 * R + R * (2 * a * (R - 1) + (R ^ 2 - R - 1))) * h2
      have hE : 1 + 4 * a * R + 4 * a ^ 2 * R * (R - 1) < 0 := by
        by_contra hcon
        push_neg at hcon
        nlinarith [mul_nonneg hcon hR1'.le]
      have hstep : 4 * c ^ 2 * R ^ 2 < 4 * a ^ 2 * R := by linarith
      have hc2R : c ^ 2 * R < a ^ 2 := by
        by_contra hcon
        push_neg at hcon
        nlinarith [mul_le_mul_of_nonneg_left hcon (by linarith : (0:ℝ) ≤ 4 * R)]
      exact lt_of_sq_gt_of_neg (mul_neg_of_pos_of_neg hs ha')
        (mul_neg_of_neg_of_pos hc hb) (by linarith)
  · -- `a > 0`: `c > a > 0`, and `E > 0` termwise.
    have hc0 : 0 < c := lt_trans ha hca
    have hE : 0 < 1 + 4 * a * R + 4 * a ^ 2 * R * (R - 1) := by
      have h₁ : 0 < 4 * a * R := by positivity
      have h₂ : 0 < 4 * a ^ 2 * R * (R - 1) := by positivity
      linarith
    have hstep : 4 * a ^ 2 * R < 4 * c ^ 2 * R ^ 2 := by linarith
    have hc2R : a ^ 2 < c ^ 2 * R := by
      by_contra hcon
      push_neg at hcon
      nlinarith [mul_le_mul_of_nonneg_left hcon (by linarith : (0:ℝ) ≤ 4 * R)]
    exact lt_of_sq_lt_of_pos (mul_pos hs ha) (mul_pos hc0 hb) (by linarith)

/-! ### 4. The complex-level wrappers -/

/-- **The lower member of the conjugate pair is pushed into the open lower half
plane**: `Im(x · conj y) < 0`. This is `sa_lt_cb` with the components named. -/
theorem im_mul_conj_root_neg {x y : ℂ} (hyim : 0 < y.im) (hxim : 0 < x.im)
    (hxnorm : x.re ^ 2 + x.im ^ 2 = 1)
    (h1 : 2 * x.re * (y.re ^ 2 + y.im ^ 2) = 1 + 2 * y.re * (y.re ^ 2 + y.im ^ 2))
    (h2 : 2 * y.re * ((y.re ^ 2 + y.im ^ 2) - 1)
      = (y.re ^ 2 + y.im ^ 2) ^ 2 - (y.re ^ 2 + y.im ^ 2) - 1) :
    (x * (starRingEnd ℂ) y).im < 0 := by
  have hcomp : (x * (starRingEnd ℂ) y).im = x.im * y.re - x.re * y.im := by
    simp [Complex.mul_im]; ring
  rw [hcomp, sub_neg]
  exact sa_lt_cb hyim hxim rfl h1 h2 hxnorm

/-- **The pinning, with the sector hypotheses discharged from the root data.**

`t` is the positive real root, `y₂` and `y₃` the other two. Only two facts about
them are used: `y₃` is pushed into the closed lower half plane by `x`, and — when
`φ > π/2` — so is `y₂`. -/
theorem branchInt_eq_zero_of_roots {x : ℂ} {t : ℝ} {y₂ y₃ : ℂ} {φ : ℝ} {k : ℤ}
    (hxim : 0 < x.im) (hxnorm : x.re ^ 2 + x.im ^ 2 = 1)
    (ht0 : 0 < t) (ht1 : t < 1)
    (h3 : (x * y₃).im ≤ 0)
    (hbig : π / 2 < φ → (x * y₂).im ≤ 0)
    (hφ0 : 0 ≤ φ) (hφπ : φ < π)
    (h : (1 - (t : ℂ) * x).arg + (1 - x * y₂).arg + (1 - x * y₃).arg = φ + 2 * π * k) :
    k = 0 := by
  obtain ⟨h1lo, h1hi⟩ := arg_pos_real_root hxim hxnorm ht0 ht1
  exact branchInt_eq_zero_of_sector hφ0 hφπ h1lo h1hi
    (Complex.neg_pi_lt_arg _) (Complex.arg_le_pi _)
    (arg_nonneg_of_im_nonpos h3) (Complex.arg_le_pi _)
    (fun hb => arg_nonneg_of_im_nonpos (hbig hb)) h

/-! ### 5. Non-vacuity -/

/-- **Non-vacuity for `sa_lt_cb`.** The hypotheses are satisfiable, and by a point
that is genuinely on the arc: `R = 2` lies inside the measured range
`[1.2821, 2.3247]` of `‖y₂‖²` over the complex-pair arc (Route 28). Solving the
two Vieta relations at `R = 2` gives `a = 1/2`, then `c = 3/4`, then
`b = √7/2`, `s = √7/4`, and the conclusion reads `√7/8 < 3√7/8`.

The check with real content is Route 28, which verifies both Vieta relations,
`1 < R`, and the conclusion at 700 points of the arc at 40 dps. -/
theorem sa_lt_cb_nonvacuous :
    ∃ a b c s R : ℝ, 0 < b ∧ 0 < s ∧ R = a ^ 2 + b ^ 2 ∧
      2 * c * R = 1 + 2 * a * R ∧ 2 * a * (R - 1) = R ^ 2 - R - 1 ∧
      c ^ 2 + s ^ 2 = 1 ∧ s * a < c * b := by
  refine ⟨1 / 2, Real.sqrt 7 / 2, 3 / 4, Real.sqrt 7 / 4, 2, ?_, ?_, ?_, by norm_num,
    by norm_num, ?_, ?_⟩
  · positivity
  · positivity
  · have : Real.sqrt 7 ^ 2 = 7 := Real.sq_sqrt (by norm_num)
    nlinarith [this]
  · have : Real.sqrt 7 ^ 2 = 7 := Real.sq_sqrt (by norm_num)
    nlinarith [this]
  · have h7 : 0 < Real.sqrt 7 := Real.sqrt_pos.mpr (by norm_num)
    nlinarith

end QOU.QBeta.FiveTwoDeformedSaddle
