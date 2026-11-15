import QOU.QBeta.FiveTwoEnvelopeWiring

/-!
# `∂V/∂y = 0` at the pair — pinning `k = 0` by an argument bound

Bean `qou-glbl`, obligation (1), the last one open in Gap A.

`exists_int_dVdy_mul` says `∂V/∂y · y = −k·2πi` at *every* point of the curve,
with `k` an integer nobody has pinned. At the positive real root `k = ∓1` and it
does not matter (`re_dVdy_mul_eq_zero_of_real`: a real `Y′` sees only the real
part). At the **pair** `arg y` moves, so `heⱼ` needs `k = 0` outright.

    dVdy_eq_zero_of_argSum_bound … (hb : |argSum x y| < 2π) : dVdy x y = 0

where `argSum x y = arg(1−y) + arg(1−xy) + arg(1−y/x) − 2·arg(−y)`. Taking
imaginary parts in `exists_int_dVdy_mul` turns it into `argSum = k·2π`, so **any**
bound under `2π` forces `k = 0`. This file supplies that bound in four regimes.

## ⚠ The obvious route is FALSE, not merely insufficient

`argSum = 0` is *equivalent* to three `Complex.log_mul` splits holding at once:

    (i)   log(1−xy) + log(1−y/x) = log((1−xy)(1−y/x))
    (ii)  log(1−y)  + log(that)  = log(y²)
    (iii) 2·log(−y)              = log(y²)

and **(iii) needs `Re y ≤ 0`**, which fails at the pair — `Re y` reaches `+0.7848`
(Route 38 G2, at 320 of 800 checks, all with the pair genuinely complex). Route
38 measures each wrap integer separately: `n₁ ≡ 0`, and `n₂ = n₃ ∈ {−1,0,1}`. So
`argSum = 0` holds by **wrap cancellation**, and a proof that performs the three
splits unconditionally is proving something false. The bound below never needs
them.

## The four regimes, and what supplies the missing `π/2` in each

Write `A = arg(1−y)`, `a₁ = arg(1−xy)`, `a₂ = arg(1−y/x)`, `C = 2·arg(−y)`. Two
components are free everywhere: `A ∈ (−π/2, 0)` from `Re y < 1` and `Im y > 0`,
and `a₂ ∈ (−π, 0)` from `Im(y/x) > 0`. The regimes differ only in `a₁` and `C`.

| regime | supplies the bound | interval | Route 38 |
|---|---|---|---|
| `Re y > 0` | forces `cos φ > 0`, so every term of `Im(xy)` carries the sign of `Im y` | `(−3π/2, 2π)` | G9, 160 checks |
| `Re y ≤ 0`, `cos φ ≤ 0` | both terms of `Im(xy)` flip | `(−3π/2, 2π)` | G10, 107 |
| `Re y ≤ 0`, `cos φ > 0` | **an identity, not a sign**: `Re(xy) + Re(y/x) = 2cos φ·Re y ≤ 0` | `(−2π, 2π)` | G11, 40 |
| the real pair | both roots negative, so `A = C = 0` | `(−π, π)` | G12, 186 |

Every regime is non-empty. Regime 3 is the smallest and the only one no sign
argument reaches — it is where a proof that assumed the signs were uniform would
silently be assuming something false.

⚠ **The tree's four sign facts are really two inequalities.** With `y = p+qi`,
`x = c+si`: `cq − sp > 0` (unconditional) *is* both `im_div_Ypair_fst_pos` and
`im_mul_Ypair_snd_neg`; `cq + sp < 0` (needs `c < 0`) *is* both
`im_mul_Ypair_fst_neg` and `im_div_Ypair_snd_pos`. Route 38's first draft of the
regime gates mirrored each inequality branch-by-branch with a sign factor and
**failed**: `Im(x·y)` for one branch pairs with `Im(y/x)` for the *other*, not
with itself. Conjugation is the only correct symmetry, and it is why only
`Im y > 0` is treated here.

⚠ **`im_mul_Ypair_fst_neg`'s `cos φ < 0` is not a gap to be filled.** Route 38 G3
measures that it genuinely fails at 181 of 400 arc points, all at `cos φ > 0` —
and that failure region *is* regime 1, where the **opposite** sign supplies the
bound.

⚠⚠ **This is FALSE at `φ = π`**, on the branch reaching `−2.2469796`: there
`argSum = 2π` and `k = ±1` (Route 38 G15). The cause is identical to `VSide`'s
endpoint failure — `x·y = 2.2469796` lands ON Li₂'s cut, so `a₁ = a₂ = π` instead
of cancelling. Benign because `envelopeS_total` needs `HasDerivAt` only on
`Ico 0 π`, but every statement here must carry a hypothesis that excludes it.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Complex Real QOU.MathlibExt

/-- The quantity `exists_int_dVdy_mul` pins to `2πℤ`: the imaginary part of
`−∂V/∂y · y`, written out. -/
noncomputable def argSum (x y : ℂ) : ℝ :=
  (1 - y).arg + (1 - x * y).arg + (1 - y / x).arg - 2 * (-y).arg

/-- **The reduction: any bound under `2π` gives `∂V/∂y = 0`.**

`exists_int_dVdy_mul` gives `∂V/∂y·y = −k·2πi`; its imaginary part is
`−argSum x y = −k·2π`. So `argSum` is an integer multiple of `2π`, and a strict
bound by `2π` forces the integer to be `0`. -/
theorem dVdy_eq_zero_of_argSum_bound {x y : ℂ} (hx : x ≠ 0) (hy : y ≠ 0)
    (h1 : (1 : ℂ) - y ≠ 0) (h2 : (1 : ℂ) - x * y ≠ 0) (h3 : (1 : ℂ) - y / x ≠ 0)
    (hc : curve x y = 0) (hb : |argSum x y| < 2 * Real.pi) :
    dVdy x y = 0 := by
  obtain ⟨k, hk⟩ := exists_int_dVdy_mul hx hy h1 h2 h3 hc
  -- the same product, written out
  have hexp : dVdy x y * y =
      -Complex.log (1 - y) - Complex.log (1 - x * y) - Complex.log (1 - y / x)
        + 2 * Complex.log (-y) := by
    rw [dVdy, div_mul_cancel₀ _ hy]
  -- imaginary parts
  have hL : -(1 - y).arg - (1 - x * y).arg - (1 - y / x).arg + 2 * (-y).arg
      = -((k : ℝ) * (2 * Real.pi)) := by
    have h := congrArg Complex.im (hexp.symm.trans hk)
    simpa [Complex.log_im, Complex.sub_im, Complex.add_im, Complex.neg_im,
      Complex.mul_im, Complex.mul_re, Complex.I_im, Complex.I_re,
      Complex.intCast_im, Complex.intCast_re, Complex.ofReal_im,
      Complex.ofReal_re] using h
  have hS : argSum x y = (k : ℝ) * (2 * Real.pi) := by
    simp only [argSum]
    linarith
  -- an integer multiple of `2π` that is smaller than `2π` in absolute value
  have hpi : (0 : ℝ) < 2 * Real.pi := by positivity
  have hk0 : k = 0 := by
    by_contra hne
    have h1k : (1 : ℝ) ≤ |(k : ℝ)| := by
      have : (1 : ℤ) ≤ |k| := Int.one_le_abs (by exact_mod_cast hne)
      calc (1 : ℝ) ≤ ((|k| : ℤ) : ℝ) := by exact_mod_cast this
        _ = |(k : ℝ)| := by push_cast [Int.cast_abs]; rfl
    rw [hS, abs_mul, abs_of_pos hpi] at hb
    nlinarith
  rw [hk0] at hk
  simp only [Int.cast_zero, zero_mul, neg_zero] at hk
  exact (mul_eq_zero.1 hk).resolve_right hy

/-! ## The two components that are free in every regime -/

/-- `arg (1−y) ∈ (−π/2, 0)` whenever `Re y < 1` and `Im y > 0`. -/
theorem arg_one_sub_mem {y : ℂ} (hre : y.re < 1) (him : 0 < y.im) :
    -(Real.pi / 2) < (1 - y).arg ∧ (1 - y).arg < 0 := by
  have hre' : 0 < ((1 : ℂ) - y).re := by simp [Complex.sub_re]; linarith
  have him' : ((1 : ℂ) - y).im < 0 := by simp [Complex.sub_im]; linarith
  have hlt : (1 - y).arg < 0 := Complex.arg_neg_iff.2 him'
  have habs : |(1 - y).arg| < Real.pi / 2 :=
    Complex.abs_arg_lt_pi_div_two_iff.2 (Or.inl hre')
  exact ⟨by rw [abs_lt] at habs; exact habs.1, hlt⟩

/-- `arg z ∈ (−π, 0)` whenever `Im z < 0`. -/
theorem arg_mem_neg {z : ℂ} (h : z.im < 0) : -Real.pi < z.arg ∧ z.arg < 0 :=
  ⟨Complex.neg_pi_lt_arg z, Complex.arg_neg_iff.2 h⟩

/-- `arg z ∈ (0, π]` whenever `Im z > 0`. -/
theorem arg_mem_pos {z : ℂ} (h : 0 < z.im) : 0 < z.arg ∧ z.arg ≤ Real.pi := by
  refine ⟨lt_of_le_of_ne (Complex.arg_nonneg_iff.2 h.le) ?_, Complex.arg_le_pi z⟩
  intro hz
  exact absurd (Complex.arg_eq_zero_iff.1 hz.symm).2 (ne_of_gt h)

/-- `arg z ∈ [0, π]` whenever `Im z ≥ 0`. -/
theorem arg_mem_nonneg {z : ℂ} (h : 0 ≤ z.im) : 0 ≤ z.arg ∧ z.arg ≤ Real.pi :=
  ⟨Complex.arg_nonneg_iff.2 h, Complex.arg_le_pi z⟩

/-- `|arg z| < π/2` whenever `Re z > 0` — the shape regime 3 needs, where the
`π/2` comes from `Re(x·y) ≤ 0` rather than from a sign of an imaginary part. -/
theorem abs_arg_lt_of_re_pos {z : ℂ} (h : 0 < z.re) : |z.arg| < Real.pi / 2 :=
  Complex.abs_arg_lt_pi_div_two_iff.2 (Or.inl h)

/-! ## `−C = 2π − 2·arg y` on the upper half plane, and its two ranges -/

/-- On `Im y > 0`, `arg(−y) = arg y − π`, so `−2·arg(−y) = 2π − 2·arg y`. -/
theorem two_pi_sub_two_arg {y : ℂ} (him : 0 < y.im) :
    -(2 * (-y).arg) = 2 * Real.pi - 2 * y.arg := by
  rw [Complex.arg_neg_eq_arg_sub_pi_of_im_pos him]; ring

/-- `Re y > 0` and `Im y > 0` put `arg y` in `(0, π/2)`, hence `−C ∈ (π, 2π)`. -/
theorem arg_mem_Ioo_of_re_pos {y : ℂ} (hre : 0 < y.re) (him : 0 < y.im) :
    0 < y.arg ∧ y.arg < Real.pi / 2 := by
  refine ⟨(arg_mem_pos him).1, ?_⟩
  have := abs_arg_lt_of_re_pos hre
  rw [abs_lt] at this
  exact this.2

/-- `Re y ≤ 0` and `Im y > 0` put `arg y` in `[π/2, π)`, hence `−C ∈ (0, π]`. -/
theorem arg_mem_Ico_of_re_nonpos {y : ℂ} (hre : y.re ≤ 0) (him : 0 < y.im) :
    Real.pi / 2 ≤ y.arg ∧ y.arg < Real.pi := by
  constructor
  · by_contra h
    push_neg at h
    have hy0 : y ≠ 0 := fun hz => by simp [hz] at him
    have habs : |y.arg| < Real.pi / 2 := by
      rw [abs_lt]
      exact ⟨by linarith [Complex.arg_nonneg_iff.2 him.le], h⟩
    rcases Complex.abs_arg_lt_pi_div_two_iff.1 habs with hr | hr
    · linarith
    · exact hy0 hr
  · rcases lt_or_eq_of_le (Complex.arg_le_pi y) with h | h
    · exact h
    · exact absurd (Complex.arg_eq_pi_iff.1 h).2 (ne_of_gt him)


/-! ## The four regime bounds

Each concludes `|argSum x y| < 2π`, which `dVdy_eq_zero_of_argSum_bound` turns
into `∂V/∂y = 0`. All four are stated for a root with `Im y > 0`; the conjugate
branch follows by conjugation (Route 38 G14) rather than by mirroring the
individual inequalities, which does **not** work — see the module docstring. -/

private theorem one_sub_im (z : ℂ) : ((1 : ℂ) - z).im = -z.im := by
  simp [Complex.sub_im]

private theorem one_sub_re (z : ℂ) : ((1 : ℂ) - z).re = 1 - z.re := by
  simp [Complex.sub_re]

/-- **Regime 1 — `Re y > 0`.** On the arc this forces `cos φ > 0`, and then every
term of `Im(x·y) = cos φ·Im y + sin φ·Re y` carries the sign of `Im y`, so
`arg(1−x·y) < 0`. That is exactly where `im_mul_Ypair_fst_neg` fails (Route 38
G3): the failure supplies the bound. Interval `(−3π/2, 2π)`. -/
theorem abs_argSum_lt_of_re_pos {x y : ℂ} (hy1 : y.re < 1) (hyim : 0 < y.im)
    (hyre : 0 < y.re) (hmul : 0 < (x * y).im) (hdiv : 0 < (y / x).im) :
    |argSum x y| < 2 * Real.pi := by
  obtain ⟨hA1, hA2⟩ := arg_one_sub_mem hy1 hyim
  obtain ⟨ha11, ha12⟩ := arg_mem_neg (z := 1 - x * y) (by rw [one_sub_im]; linarith)
  obtain ⟨ha21, ha22⟩ := arg_mem_neg (z := 1 - y / x) (by rw [one_sub_im]; linarith)
  obtain ⟨hy1', hy2'⟩ := arg_mem_Ioo_of_re_pos hyre hyim
  have hC := two_pi_sub_two_arg hyim
  have hpi := Real.pi_pos
  rw [abs_lt]
  constructor <;> · simp only [argSum]; linarith

/-- **Regime 2 — `Re y ≤ 0` and `cos φ ≤ 0`.** Both terms of `Im(x·y)` now flip,
so `arg(1−x·y) ≥ 0` instead. Interval `(−3π/2, 2π)`; the upper end is reached only
if `arg(1−y) = 0`, which `Im y > 0` forbids. -/
theorem abs_argSum_lt_of_im_mul_nonpos {x y : ℂ} (hy1 : y.re < 1) (hyim : 0 < y.im)
    (hyre : y.re ≤ 0) (hmul : (x * y).im ≤ 0) (hdiv : 0 < (y / x).im) :
    |argSum x y| < 2 * Real.pi := by
  obtain ⟨hA1, hA2⟩ := arg_one_sub_mem hy1 hyim
  obtain ⟨ha11, ha12⟩ := arg_mem_nonneg (z := 1 - x * y) (by rw [one_sub_im]; linarith)
  obtain ⟨ha21, ha22⟩ := arg_mem_neg (z := 1 - y / x) (by rw [one_sub_im]; linarith)
  obtain ⟨hy1', hy2'⟩ := arg_mem_Ico_of_re_nonpos hyre hyim
  have hC := two_pi_sub_two_arg hyim
  have hpi := Real.pi_pos
  rw [abs_lt]
  constructor <;> · simp only [argSum]; linarith

/-- **Regime 3a — `Re(x·y) ≤ 0`.** Neither `Im`-sign argument applies here; the
missing `π/2` comes from `Re(1 − x·y) ≥ 1 > 0` instead. Interval `(−2π, 3π/2)`. -/
theorem abs_argSum_lt_of_re_mul_nonpos {x y : ℂ} (hy1 : y.re < 1) (hyim : 0 < y.im)
    (hyre : y.re ≤ 0) (hmul : (x * y).re ≤ 0) (hdiv : 0 < (y / x).im) :
    |argSum x y| < 2 * Real.pi := by
  obtain ⟨hA1, hA2⟩ := arg_one_sub_mem hy1 hyim
  have ha1 : |((1 : ℂ) - x * y).arg| < Real.pi / 2 :=
    abs_arg_lt_of_re_pos (by rw [one_sub_re]; linarith)
  rw [abs_lt] at ha1
  obtain ⟨ha11, ha12⟩ := ha1
  obtain ⟨ha21, ha22⟩ := arg_mem_neg (z := 1 - y / x) (by rw [one_sub_im]; linarith)
  obtain ⟨hy1', hy2'⟩ := arg_mem_Ico_of_re_nonpos hyre hyim
  have hC := two_pi_sub_two_arg hyim
  have hpi := Real.pi_pos
  rw [abs_lt]
  constructor <;> · simp only [argSum]; linarith

/-- **Regime 3b — `Re(y/x) ≤ 0`,** the other half of regime 3. Which of the two
factors has non-positive real part is not determined by
`Re(x·y) + Re(y/x) = 2cos φ·Re y ≤ 0`, and does not need to be: the bound is
symmetric in them. Interval `(−2π, 2π)`. -/
theorem abs_argSum_lt_of_re_div_nonpos {x y : ℂ} (hy1 : y.re < 1) (hyim : 0 < y.im)
    (hyre : y.re ≤ 0) (hdivre : (y / x).re ≤ 0) (hdiv : 0 < (y / x).im) :
    |argSum x y| < 2 * Real.pi := by
  obtain ⟨hA1, hA2⟩ := arg_one_sub_mem hy1 hyim
  have ha11 : -Real.pi < ((1 : ℂ) - x * y).arg := Complex.neg_pi_lt_arg _
  have ha12 : ((1 : ℂ) - x * y).arg ≤ Real.pi := Complex.arg_le_pi _
  have ha2 : |((1 : ℂ) - y / x).arg| < Real.pi / 2 :=
    abs_arg_lt_of_re_pos (by rw [one_sub_re]; linarith)
  rw [abs_lt] at ha2
  obtain ⟨ha21, _⟩ := ha2
  have ha22 : ((1 : ℂ) - y / x).arg < 0 :=
    (arg_mem_neg (z := 1 - y / x) (by rw [one_sub_im]; linarith)).2
  obtain ⟨hy1', hy2'⟩ := arg_mem_Ico_of_re_nonpos hyre hyim
  have hC := two_pi_sub_two_arg hyim
  have hpi := Real.pi_pos
  rw [abs_lt]
  constructor <;> · simp only [argSum]; linarith

/-- **Regime 4 — the real pair.** Past the discriminant crossing both pair roots
are real and **negative**, so `arg(1−y) = 0` and `arg(−y) = 0` outright and the
whole quantity collapses to `arg(1−x·y) + arg(1−y/x)`, inside `(−π, π)` by the two
`Im` signs.

⚠ This is the regime that needs `sin φ > 0`, through `hmul`/`hdiv`, and it is the
one that breaks at `φ = π`: there `Im(x·y) = 0`, both arguments are `π`, and
`argSum = 2π` (Route 38 G15). -/
theorem abs_argSum_lt_of_real_neg {x y : ℂ} (hyim : y.im = 0) (hyre : y.re < 0)
    (hmul : (x * y).im < 0) (hdiv : 0 < (y / x).im) :
    |argSum x y| < 2 * Real.pi := by
  have hA : ((1 : ℂ) - y).arg = 0 := by
    refine Complex.arg_eq_zero_iff.2 ⟨?_, ?_⟩
    · rw [one_sub_re]; linarith
    · rw [one_sub_im, hyim]; ring
  have hC : (-y).arg = 0 := by
    refine Complex.arg_eq_zero_iff.2 ⟨?_, ?_⟩
    · simp [Complex.neg_re]; linarith
    · simp [Complex.neg_im, hyim]
  obtain ⟨ha11, ha12⟩ := arg_mem_pos (z := 1 - x * y) (by rw [one_sub_im]; linarith)
  obtain ⟨ha21, ha22⟩ := arg_mem_neg (z := 1 - y / x) (by rw [one_sub_im]; linarith)
  have hpi := Real.pi_pos
  rw [abs_lt]
  constructor <;> · simp only [argSum, hA, hC]; linarith

/-- **Regime 3, as one statement.** `Re(x·y) + Re(y/x) = 2cos φ·Re y ≤ 0` gives
the disjunction; either side lands inside `(−2π, 2π)`. -/
theorem abs_argSum_lt_of_re_mul_or_div_nonpos {x y : ℂ} (hy1 : y.re < 1)
    (hyim : 0 < y.im) (hyre : y.re ≤ 0)
    (hor : (x * y).re ≤ 0 ∨ (y / x).re ≤ 0) (hdiv : 0 < (y / x).im) :
    |argSum x y| < 2 * Real.pi := by
  rcases hor with h | h
  · exact abs_argSum_lt_of_re_mul_nonpos hy1 hyim hyre h hdiv
  · exact abs_argSum_lt_of_re_div_nonpos hy1 hyim hyre h hdiv

/-! ## The conjugate branch, for free

`Ypair.2 = conj Ypair.1`, and on `|x| = 1` conjugation **swaps** `x·y` with
`y/x` — because `conj x = x⁻¹` there. So `argSum x (conj y) = −argSum x y`: the
two middle terms exchange places and every term flips sign.

⚠ This is the ONLY correct symmetry between the branches. Route 38's first draft
of the regime gates tried to mirror each inequality separately with a sign
factor and failed: `Im(x·y)` for one branch pairs with `Im(y/x)` for the
**other**, not with itself.

⚠ And the four `arg ≠ π` side conditions are not decoration. `arg_conj` is
`if arg x = π then π else -arg x`, so a term sitting on `log`'s cut does **not**
flip — it would break the identity by `2π`, which is exactly the size of the
error that matters here. Each is discharged from `notCut` at the call site:
`w ∈ notCut` with `Im w = 0` forces `Re w < 1`, hence `Re (1 − w) > 0`, hence
`arg (1 − w) = 0`. -/

private theorem conj_ne_pi_aux {z : ℂ} (h : z.arg ≠ Real.pi) :
    ((starRingEnd ℂ) z).arg = -z.arg := by
  rw [Complex.arg_conj, if_neg h]

theorem conj_eq_inv_of_unit {x : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) :
    (starRingEnd ℂ) x = x⁻¹ := by
  have hx0 : x ≠ 0 := by
    intro hz
    rw [hz] at hx
    simp at hx
  have hns : Complex.normSq x = 1 := by
    simp only [Complex.normSq_apply]
    nlinarith [hx]
  field_simp
  rw [mul_comm, Complex.mul_conj]
  exact_mod_cast hns

/-- On `|x| = 1`, conjugation **swaps** the two mixed arguments. This is the one
fact the second branch rests on, and it is why mirroring the inequalities
branch-by-branch fails. -/
theorem one_sub_mul_conj {x y : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) :
    (1 : ℂ) - x * (starRingEnd ℂ) y = (starRingEnd ℂ) ((1 : ℂ) - y / x) := by
  have hx0 : x ≠ 0 := by
    intro hz
    rw [hz] at hx
    simp at hx
  rw [map_sub, map_one, map_div₀, conj_eq_inv_of_unit hx]
  field_simp

theorem one_sub_div_conj {x y : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) :
    (1 : ℂ) - (starRingEnd ℂ) y / x = (starRingEnd ℂ) ((1 : ℂ) - x * y) := by
  have hx0 : x ≠ 0 := by
    intro hz
    rw [hz] at hx
    simp at hx
  rw [map_sub, map_one, map_mul, conj_eq_inv_of_unit hx]
  field_simp

theorem argSum_conj {x y : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1)
    (h1 : ((1 : ℂ) - y).arg ≠ Real.pi) (h2 : ((1 : ℂ) - x * y).arg ≠ Real.pi)
    (h3 : ((1 : ℂ) - y / x).arg ≠ Real.pi) (h4 : (-y).arg ≠ Real.pi) :
    argSum x ((starRingEnd ℂ) y) = -argSum x y := by
  have e2 := one_sub_mul_conj (y := y) hx
  have e3 := one_sub_div_conj (y := y) hx
  have e1 : (1 : ℂ) - (starRingEnd ℂ) y = (starRingEnd ℂ) ((1 : ℂ) - y) := by
    rw [map_sub, map_one]
  have e4 : -(starRingEnd ℂ) y = (starRingEnd ℂ) (-y) := by rw [map_neg]
  simp only [argSum, e1, e2, e3, e4, conj_ne_pi_aux h1, conj_ne_pi_aux h2,
    conj_ne_pi_aux h3, conj_ne_pi_aux h4]
  ring

theorem abs_argSum_conj {x y : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1)
    (h1 : ((1 : ℂ) - y).arg ≠ Real.pi) (h2 : ((1 : ℂ) - x * y).arg ≠ Real.pi)
    (h3 : ((1 : ℂ) - y / x).arg ≠ Real.pi) (h4 : (-y).arg ≠ Real.pi)
    (hb : |argSum x y| < 2 * Real.pi) :
    |argSum x ((starRingEnd ℂ) y)| < 2 * Real.pi := by
  rw [argSum_conj hx h1 h2 h3 h4, abs_neg]
  exact hb

/-- `w ∈ notCut` ⟹ `arg (1 − w) ≠ π`: if `Im w ≠ 0` then `Im (1 − w) ≠ 0`, and
otherwise `Re w < 1` puts `1 − w` strictly in the right half plane. -/
theorem arg_one_sub_ne_pi {w : ℂ} (h : w ∈ notCut) : ((1 : ℂ) - w).arg ≠ Real.pi := by
  intro hpi
  obtain ⟨hre, him⟩ := Complex.arg_eq_pi_iff.1 hpi
  simp only [Complex.sub_re, Complex.one_re, Complex.sub_im, Complex.one_im] at hre him
  rcases h with h | h
  · exact h (by linarith)
  · linarith

end QOU.QBeta.FiveTwoDeformedSaddle
