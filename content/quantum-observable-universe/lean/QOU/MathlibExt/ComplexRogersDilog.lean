/-
# The Rogers dilogarithm on `ℂ`, and its derivative

`cRogersL z = Li₂(z) + ½·log z·log(1−z)`, built on the corpus's own
`cLiTwoExt` — the integral continuation of `Li₂` off the unit disc — rather
than on a series, so it is defined on all of `notCut = ℂ ∖ [1,∞)`.

## Why this module exists

The five-term (pentagon) identity for a complex dilogarithm is the analytic
input the 5₂ sum-rule lane is missing (bean `qou-xblo`). Its standard proof is:
differentiate in one variable, show the derivative vanishes identically, then
pin the constant. The algebraic half of step one is
`QOU.QBeta.FiveTwo.pentagon_deriv_x_eq_zero`; **this module supplies the
analytic half**, namely that `cRogersL` really has the derivative that lemma
assumes:

    L′(z) = −½·( log(1−z)/z + log z/(1−z) )

Everything here is unconditional given its hypotheses — no branch choice is
smuggled in. The hypotheses are exactly the four the pieces need: `z ∈ notCut`
and `z ≠ 0` for `cLiTwoExt`, and `z`, `1−z ∈ slitPlane` for the two logarithms.

## ⚠ What this does NOT do

It does not prove the five-term identity. Assembling it still needs the
chain-rule bookkeeping at the three composite pentagon arguments and — the
delicate part — the **branch conditions** under which
`log a₃ = log(1−x) − log(1−xy)` and its two companions hold. Those expansions
are where flattening enters, so that is Neumann's `ker ν` again, not a
formality.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

-- Ref: [neumann2004] uploads/0307092v2.pdf, Prop 2.5 (Rogers `R`, and `R(z;p,q)`)
-/
import QOU.MathlibExt.ComplexDilogarithmDeriv

namespace QOU.MathlibExt

open Complex

/-- The **Rogers dilogarithm** on `ℂ`, built on the integral continuation
`cLiTwoExt` so that it is defined off `[1,∞)` rather than only on the disc.

Neumann writes `R(z) = ½·log z·log(1−z) − ∫₀^z log(1−t)/t dt`; the integral is
`−Li₂(z)`, so this is the same function. -/
noncomputable def cRogersL (z : ℂ) : ℂ :=
  cLiTwoExt z + Complex.log z * Complex.log (1 - z) / 2

/-- `1 − z ≠ 0` from `1 − z ∈ slitPlane`. -/
theorem one_sub_ne_zero_of_mem_slitPlane {z : ℂ} (h : (1 : ℂ) - z ∈ slitPlane) :
    (1 : ℂ) - z ≠ 0 :=
  Complex.slitPlane_ne_zero h

/-- **The derivative of the Rogers dilogarithm.**

    L′(z) = −½·( log(1−z)/z + log z/(1−z) )

The `Li₂` term contributes `−log(1−z)/z` and the `½·log·log` term contributes
`½·log(1−z)/z − ½·log z/(1−z)`; the two `log(1−z)/z` pieces combine to halve it.
This is exactly the `rogersDeriv` that
`QOU.QBeta.FiveTwo.pentagon_deriv_x_eq_zero` takes as given. -/
theorem hasDerivAt_cRogersL {z : ℂ} (hz : z ∈ notCut) (hz0 : z ≠ 0)
    (hs : z ∈ slitPlane) (hs1 : (1 : ℂ) - z ∈ slitPlane) :
    HasDerivAt cRogersL
      (-(1 / 2) * (Complex.log (1 - z) / z + Complex.log z / (1 - z))) z := by
  have h1z : (1 : ℂ) - z ≠ 0 := one_sub_ne_zero_of_mem_slitPlane hs1
  have hli : HasDerivAt cLiTwoExt (-(Complex.log (1 - z) / z)) z :=
    hasDerivAt_cLiTwoExt' hz hz0
  have hlog : HasDerivAt Complex.log z⁻¹ z := Complex.hasDerivAt_log hs
  have hinner : HasDerivAt (fun w : ℂ => 1 - w) (-1) z := by
    simpa using (hasDerivAt_const z (1 : ℂ)).sub (hasDerivAt_id z)
  have hlog1 : HasDerivAt (fun w : ℂ => Complex.log (1 - w)) (-((1 - z)⁻¹)) z := by
    simpa using (Complex.hasDerivAt_log hs1).comp z hinner
  have hprod : HasDerivAt (fun w : ℂ => Complex.log w * Complex.log (1 - w) / 2)
      ((z⁻¹ * Complex.log (1 - z) + Complex.log z * -((1 - z)⁻¹)) / 2) z :=
    (hlog.mul hlog1).div_const 2
  have hsum := hli.add hprod
  convert hsum using 1
  field_simp
  ring

/-! ## The pentagon's log expansions, on the positive real region

Assembling the five-term identity needs the three expansions

    log a₃ = log(1−x) − log(1−xy),   log(1−a₃) = log x + log(1−y) − log(1−xy)
    log(1−a₄) = log x + log y

and their `a₅` companions. These are **branch conditions**, not identities: they
are exactly where flattening enters, and Route 45 measured the pentagon sum
drifting once one of them fails.

On the positive real square `0 < x, y < 1` every pentagon argument is a positive
real, so all logarithms are real and the expansions hold outright. That is the
base region from which analytic continuation carries the identity outward — the
same shape as the `Landen` proof already in the corpus, which pins its constant
on a real interval and continues.

⚠ This does **not** give the expansions anywhere else. Off the real square they
can and do fail, which is the whole content of Routes 45–46. -/

/-- `log(ab) = log a + log b` for positive reals, as complex logarithms. -/
theorem clog_mul_of_pos {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    Complex.log ((a : ℂ) * (b : ℂ)) = Complex.log (a : ℂ) + Complex.log (b : ℂ) := by
  rw [← Complex.ofReal_mul, ← Complex.ofReal_log ha.le, ← Complex.ofReal_log hb.le,
    ← Complex.ofReal_log (mul_pos ha hb).le, Real.log_mul ha.ne' hb.ne']
  push_cast
  ring

/-- `log(a/b) = log a − log b` for positive reals, as complex logarithms. -/
theorem clog_div_of_pos {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    Complex.log ((a : ℂ) / (b : ℂ)) = Complex.log (a : ℂ) - Complex.log (b : ℂ) := by
  rw [← Complex.ofReal_div, ← Complex.ofReal_log ha.le, ← Complex.ofReal_log hb.le,
    ← Complex.ofReal_log (div_pos ha hb).le, Real.log_div ha.ne' hb.ne']
  push_cast
  ring

/-- **On `0 < x, y < 1` every pentagon argument is a positive real.**

The five are `x`, `y`, `(1−x)/(1−xy)`, `1−xy`, `(1−y)/(1−xy)`, and the two
`1 − aᵢ` that the Rogers derivative also needs are `x(1−y)/(1−xy)` and
`y(1−x)/(1−xy)`. Positivity of all of them is what makes the log expansions
unconditional there. -/
theorem pentagon_args_pos {x y : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hy0 : 0 < y) (hy1 : y < 1) :
    0 < 1 - x * y ∧ 0 < (1 - x) / (1 - x * y) ∧ 0 < (1 - y) / (1 - x * y)
      ∧ 0 < x * (1 - y) / (1 - x * y) ∧ 0 < y * (1 - x) / (1 - x * y) := by
  have hxy : x * y < 1 := by nlinarith
  have h0 : 0 < 1 - x * y := by linarith
  refine ⟨h0, div_pos (by linarith) h0, div_pos (by linarith) h0,
    div_pos (by nlinarith) h0, div_pos (by nlinarith) h0⟩

/-- **The three log expansions hold on the positive real square.**

Stated for the two that carry the pentagon's `a₃` term; `a₅`'s companions follow
by the `x ↔ y` symmetry, which is the reflection of §7g's `Z/2`. -/
theorem clog_pentagon_expansions {x y : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hy0 : 0 < y) (hy1 : y < 1) :
    Complex.log (((1 - x : ℝ) : ℂ) / ((1 - x * y : ℝ) : ℂ))
        = Complex.log ((1 - x : ℝ) : ℂ) - Complex.log ((1 - x * y : ℝ) : ℂ)
      ∧ Complex.log (((x : ℝ) : ℂ) * ((y : ℝ) : ℂ))
        = Complex.log ((x : ℝ) : ℂ) + Complex.log ((y : ℝ) : ℂ) := by
  have hxy : x * y < 1 := by nlinarith
  exact ⟨clog_div_of_pos (by linarith) (by linarith), clog_mul_of_pos hx0 hy0⟩

end QOU.MathlibExt
