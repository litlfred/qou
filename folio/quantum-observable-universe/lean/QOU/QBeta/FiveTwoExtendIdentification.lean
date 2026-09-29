import QOU.QBeta.FiveTwoRogersExtend
import QOU.QBeta.FiveTwoRogersReflection
import QOU.Archimedean.ComplexDilogBridge
import QOU.MathlibExt.ComplexDilogarithmLanden
import QOU.MathlibExt.ComplexDilogarithmBoundary
import QOU.MathlibExt.ComplexDilogarithmOnCut

/-!
# `extend` **is** `Re` of the analytic Rogers `L` — **`qou-rstq` item 4, closed**

    extend_eq_re_cRogersL (hx0 : x ≠ 0) (hx1 : x ≠ 1) :
      extend (π²/6) rogersL x = Re (cLiTwoExt x + log x · log(1−x) / 2)

for **every** real `x ≠ 0, 1` — all three regimes, hence all six arguments
`extended_sum` uses, none of which is `0` or `1`.

Route 33 measured this identification at `1e-50` and named what Lean was missing
per regime. All of it is now proved. The three regimes needed three different
things:

| regime | what it needed |
|---|---|
| `0 < x < 1` | nothing — the series converges, `cLiTwo_ofReal` bridges |
| `x < 0` | Landen's identity, `landenCombo_ofReal_eq_zero` |
| `x > 1` | the inversion identity **on the cut**, `re_inversion_identity` — which needed integrability of `cLiTwoExt`'s integrand at `x > 1`, and the branch-point value `cLiTwoExt 1 = π²/6` |

## The statement, per regime

The left side is the corpus's **piecewise** extension, built on the real `LiTwo`
(a `tsum`, hence the junk value `0` outside its disc of convergence). The right
side is `Re` of the **analytic** Rogers `L`, principal branches throughout.
`extended_sum` is stated for the left; the level-7 bridge computes with the
right. Identifying them is what item 4 asks for.

## Why Landen is exactly the input

Write `u = x/(x−1)`. For `x < 0` that lands in `(0,1)`, where the series
converges and `cLiTwo_ofReal` bridges `LiTwo` to `cLiTwo`. Two log identities
then do all the bookkeeping:

    log(1−u) = −log(1−x)          because `1 − u = 1/(1−x)`
    log u    = log(−x) − log(1−x) because `u = (−x)/(1−x)`

so that

    rogersL u = Li₂ u − ½·log(−x)·log(1−x) + ½·log(1−x)²

and Landen — `Li₂ x + Li₂ u + ½·log(1−x)² = 0` — replaces `Li₂ u`, leaving

    rogersL u = −Li₂ x − ½·log(−x)·log(1−x) = −Re L(x)

since `Re log x = log(−x)` for `x < 0` (the `iπ` in `log x` meets a *real*
`log(1−x)`, so it contributes nothing to the real part). Then
`extend x = −rogersL u = Re L(x)`.

The `iπ` not contributing is worth stating rather than passing over: it is the
same `−t`-on-log's-cut phenomenon that produced corrections 5 and 6 in the
transport lane. Here it is harmless, and *because* the partner factor is real —
not because the cut was avoided.

## Scope — what this closes, and what it does NOT

**Closed:** `qou-rstq` item 4. `extended_sum` is stated for the piecewise
`extend`; the level-7 bridge computes with the analytic `Re L`. This is the
identification that lets them talk to each other, and it now covers every
argument either of them uses.

**NOT closed, and unchanged by this file:**

* the **5₂ sum rule** itself — item 4 was one input to the level-7 bridge, not
  the sum rule;
* **Gap A**, the globally differentiable root labelling (`qou-glbl`), still the
  one open hypothesis in the transport;
* **assembling** `S(π)` and wiring `corr_sum_eq_neg_pi_sq` to `extended_sum`
  (`qou-asem`) — that composition is now unblocked but is not written.

An earlier draft of this file said the inversion regime "needs a genuine
boundary value rather than a constant of integration". **That was wrong** —
Route 35 showed `Re L` is continuous across the cut, so there was no limit to
take. The correction is recorded in `qou-invr` rather than quietly deleted.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoExtendIdentification

open QOU.MathlibExt QOU.Archimedean QOU.QBeta.FiveTwoRogersExtend
open QOU.QBeta.FiveTwoRogersReflection

/-- The **analytic** Rogers `L`, principal branches. -/
noncomputable def cRogersL (z : ℂ) : ℂ :=
  cLiTwoExt z + Complex.log z * Complex.log (1 - z) / 2

/-- For `x < 0` the Landen argument lands strictly inside `(0,1)`. -/
theorem landenArg_mem_Ioo {x : ℝ} (hx : x < 0) : 0 < x / (x - 1) ∧ x / (x - 1) < 1 := by
  have hden : x - 1 < 0 := by linarith
  constructor
  · exact div_pos_of_neg_of_neg hx hden
  · rw [div_lt_one_of_neg hden]; linarith

/-- `1 − x/(x−1) = 1/(1−x)`. -/
theorem one_sub_landenArg {x : ℝ} (hx : x < 0) : 1 - x / (x - 1) = 1 / (1 - x) := by
  have hden : x - 1 ≠ 0 := by intro h; linarith
  have hden' : (1 : ℝ) - x ≠ 0 := by intro h; linarith
  field_simp
  ring

/-- `x/(x−1) = (−x)/(1−x)`. -/
theorem landenArg_eq {x : ℝ} (hx : x < 0) : x / (x - 1) = (-x) / (1 - x) := by
  have hden : x - 1 ≠ 0 := by intro h; linarith
  have hden' : (1 : ℝ) - x ≠ 0 := by intro h; linarith
  field_simp
  ring

/-- **`LiTwo` on `(0,1)` is `Re` of the continuation.** The corpus's `LiTwo` is a
`tsum`; inside the disc it agrees with `cLiTwo`, which agrees with `cLiTwoExt`. -/
theorem liTwo_eq_re_cLiTwoExt {u : ℝ} (h0 : 0 < u) (h1 : u < 1) :
    QOU.QPochhammer.LiTwo u = (cLiTwoExt (u : ℂ)).re := by
  have hnorm : ‖(u : ℂ)‖ < 1 := by
    simpa [Complex.norm_real, Real.norm_eq_abs, abs_of_pos h0] using h1
  rw [cLiTwoExt_eq_cLiTwo hnorm, cLiTwo_ofReal, Complex.ofReal_re]

/-- **The real part of `log x · log(1−x)` for `x < 0`.** The `iπ` in `log x`
meets a *real* `log(1−x)`, so it drops out of the real part — harmlessly, and
because the partner is real, not because the cut was avoided. -/
theorem re_log_mul_log_one_sub {x : ℝ} (hx : x < 0) :
    (Complex.log (x : ℂ) * Complex.log (1 - (x : ℂ))).re
      = Real.log (-x) * Real.log (1 - x) := by
  have h1x : (0 : ℝ) < 1 - x := by linarith
  have hcast : (1 : ℂ) - (x : ℂ) = (((1 - x : ℝ)) : ℂ) := by push_cast; ring
  rw [hcast, ← Complex.ofReal_log h1x.le, mul_comm, Complex.re_ofReal_mul,
    Complex.log_re, Complex.norm_real, Real.norm_eq_abs, abs_of_neg hx]
  ring

/-- `Re` of the analytic Rogers `L` at a negative real, in real terms. -/
theorem re_cRogersL_of_neg {x : ℝ} (hx : x < 0) :
    (cRogersL (x : ℂ)).re
      = (cLiTwoExt (x : ℂ)).re + Real.log (-x) * Real.log (1 - x) / 2 := by
  have hhalf : ∀ w : ℂ, w / 2 = ((((1 : ℝ) / 2) : ℝ) : ℂ) * w := by
    intro w; push_cast; ring
  rw [cRogersL, Complex.add_re, hhalf, Complex.re_ofReal_mul,
    re_log_mul_log_one_sub hx]
  ring

/-- **`extend` IS `Re` of the analytic Rogers `L`, on `x < 0`.**

The corpus's piecewise extension and the analytic function agree on the whole
negative axis. Landen (`landenCombo_ofReal_eq_zero`) is the only analytic input;
everything else is log bookkeeping. -/
theorem extend_eq_re_cRogersL_of_neg {x : ℝ} (hx : x < 0) :
    extend (Real.pi ^ 2 / 6) rogersL x = (cRogersL (x : ℂ)).re := by
  obtain ⟨hu0, hu1⟩ := landenArg_mem_Ioo hx
  set u : ℝ := x / (x - 1) with hu
  have h1x : (0 : ℝ) < 1 - x := by linarith
  have hnegx : (0 : ℝ) < -x := by linarith
  -- the two log identities
  have hlog1u : Real.log (1 - u) = -Real.log (1 - x) := by
    rw [hu, one_sub_landenArg hx, one_div, Real.log_inv]
  have hlogu : Real.log u = Real.log (-x) - Real.log (1 - x) := by
    rw [hu, landenArg_eq hx, Real.log_div (by linarith) (by linarith)]
  -- Landen, with real parts taken
  have hlanden := landenCombo_ofReal_eq_zero hx
  rw [landenCombo] at hlanden
  have hcast : (x : ℂ) / ((x : ℂ) - 1) = (u : ℂ) := by
    rw [hu]; push_cast; ring
  rw [hcast] at hlanden
  have hre := congrArg Complex.re hlanden
  simp only [Complex.add_re, Complex.zero_re] at hre
  -- `log (1 - x)` is real, so its square contributes only its real part
  have hcast1 : (1 : ℂ) - (x : ℂ) = (((1 - x : ℝ)) : ℂ) := by push_cast; ring
  have hsq : (Complex.log (1 - (x : ℂ)) ^ 2 / 2).re = Real.log (1 - x) ^ 2 / 2 := by
    rw [hcast1, ← Complex.ofReal_log h1x.le]
    norm_cast
  rw [hsq, ← liTwo_eq_re_cLiTwoExt hu0 hu1] at hre
  -- assemble: linear in the atoms `LiTwo u`, `(cLiTwoExt x).re`,
  -- `log(1−x)²` and `log(−x)·log(1−x)`, so `linear_combination` closes it
  rw [extend_of_neg _ _ hx, ← hu, rogersL, hlogu, hlog1u, re_cRogersL_of_neg hx]
  linear_combination -hre

/-! ## The INVERSION regime, `x > 1` — the sixth and last argument -/

/-- `Re` of the analytic Rogers `L` at real `x > 1`. `log x` is real, so it
factors out of the real part; `log(1−x)` contributes only its own real part,
which `Real.log` being even renders as `log(x−1)`. -/
theorem re_cRogersL_of_one_lt {x : ℝ} (hx : 1 < x) :
    (cRogersL ((x : ℝ) : ℂ)).re
      = (cLiTwoExt ((x : ℝ) : ℂ)).re + Real.log x * Real.log (1 - x) / 2 := by
  have hx0 : (0 : ℝ) < x := lt_trans zero_lt_one hx
  have hlogx : Complex.log ((x : ℝ) : ℂ) = ((Real.log x : ℝ) : ℂ) :=
    (Complex.ofReal_log hx0.le).symm
  have hcast : (1 : ℂ) - ((x : ℝ) : ℂ) = (((1 - x : ℝ)) : ℂ) := by push_cast; ring
  have hhalf : ∀ w : ℂ, w / 2 = ((((1 : ℝ) / 2) : ℝ) : ℂ) * w := by
    intro w; push_cast; ring
  rw [cRogersL, Complex.add_re, hlogx, hcast, hhalf, Complex.re_ofReal_mul,
    Complex.re_ofReal_mul, re_log_ofReal]
  ring

/-- **`extend` IS `Re` of the analytic Rogers `L` on `x > 1`.**

The last of the three regimes. `re_inversion_identity` is the only analytic
input; the rest is the same log bookkeeping as the `x < 0` case. -/
theorem extend_eq_re_cRogersL_of_one_lt {x : ℝ} (hx : 1 < x) :
    extend (Real.pi ^ 2 / 6) rogersL x = (cRogersL ((x : ℝ) : ℂ)).re := by
  have hx0 : (0 : ℝ) < x := lt_trans zero_lt_one hx
  have hxne : x ≠ 0 := ne_of_gt hx0
  have hinv0 : (0 : ℝ) < 1 / x := by positivity
  have hinv1 : 1 / x < 1 := by rw [div_lt_one hx0]; exact hx
  have hx1 : (0 : ℝ) < x - 1 := by linarith
  -- the inversion identity, with `Re cLiTwoExt(1/x)` recognised as `LiTwo (1/x)`
  have hid := QOU.MathlibExt.re_inversion_identity (le_of_lt hx)
  rw [← liTwo_eq_re_cLiTwoExt hinv0 hinv1] at hid
  -- log bookkeeping
  have hloginv : Real.log (1 / x) = -Real.log x := by
    rw [one_div, Real.log_inv]
  have hlog1inv : Real.log (1 - 1 / x) = Real.log (x - 1) - Real.log x := by
    have h : (1 : ℝ) - 1 / x = (x - 1) / x := by field_simp
    rw [h, Real.log_div (ne_of_gt hx1) hxne]
  have hlog1x : Real.log (1 - x) = Real.log (x - 1) := by
    rw [← Real.log_neg_eq_log]; congr 1; ring
  -- assemble
  rw [extend_of_one_lt _ _ hx, rogersL, hloginv, hlog1inv,
    re_cRogersL_of_one_lt hx, hlog1x]
  linear_combination -hid

/-! ## The identity regime `0 < x < 1`, and all three combined -/

/-- On `(0,1)` both logarithms are real, so `Re` passes straight through. -/
theorem re_cRogersL_of_mem {x : ℝ} (h0 : 0 < x) (h1 : x < 1) :
    (cRogersL ((x : ℝ) : ℂ)).re
      = (cLiTwoExt ((x : ℝ) : ℂ)).re + Real.log x * Real.log (1 - x) / 2 := by
  have h1x : (0 : ℝ) < 1 - x := by linarith
  have hlogx : Complex.log ((x : ℝ) : ℂ) = ((Real.log x : ℝ) : ℂ) :=
    (Complex.ofReal_log h0.le).symm
  have hcast : (1 : ℂ) - ((x : ℝ) : ℂ) = (((1 - x : ℝ)) : ℂ) := by push_cast; ring
  have hlog1x : Complex.log ((((1 - x : ℝ)) : ℂ)) = ((Real.log (1 - x) : ℝ) : ℂ) :=
    (Complex.ofReal_log h1x.le).symm
  rw [cRogersL, Complex.add_re, hlogx, hcast, hlog1x]
  norm_cast

/-- **`extend` IS `Re` of the analytic Rogers `L` on `(0,1)`** — where `extend`
is the identity and the series converges, so nothing analytic is needed. -/
theorem extend_eq_re_cRogersL_of_mem {x : ℝ} (h0 : 0 < x) (h1 : x < 1) :
    extend (Real.pi ^ 2 / 6) rogersL x = (cRogersL ((x : ℝ) : ℂ)).re := by
  rw [extend_of_mem _ _ h0.le h1.le, rogersL, re_cRogersL_of_mem h0 h1,
    liTwo_eq_re_cLiTwoExt h0 h1]

/-- **`qou-rstq` item 4, all three regimes at once.**

    extend (π²/6) rogersL x = Re (cLiTwoExt x + log x · log(1−x) / 2)

for every real `x ≠ 0, 1`. The corpus's **piecewise** extension and `Re` of the
**analytic** Rogers `L` are the same function.

`extended_sum` is stated for the left side; the level-7 bridge computes with the
right. This is the identification that lets them talk to each other, and it
covers **all six arguments** `extended_sum` uses — none of which is `0` or `1`.

The three regimes needed three different things:
* `x < 0` — Landen's identity (`landenCombo_ofReal_eq_zero`);
* `0 < x < 1` — nothing, the series converges;
* `x > 1` — the inversion identity **on the cut** (`re_inversion_identity`),
  which in turn needed integrability of `cLiTwoExt`'s integrand at `x > 1` and
  the branch-point value `cLiTwoExt 1 = π²/6`. -/
theorem extend_eq_re_cRogersL {x : ℝ} (hx0 : x ≠ 0) (hx1 : x ≠ 1) :
    extend (Real.pi ^ 2 / 6) rogersL x = (cRogersL ((x : ℝ) : ℂ)).re := by
  rcases lt_trichotomy x 0 with h | h | h
  · exact extend_eq_re_cRogersL_of_neg h
  · exact absurd h hx0
  · rcases lt_trichotomy x 1 with h1 | h1 | h1
    · exact extend_eq_re_cRogersL_of_mem h h1
    · exact absurd h1 hx1
    · exact extend_eq_re_cRogersL_of_one_lt h1

end QOU.QBeta.FiveTwoExtendIdentification
