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
import QOU.MathlibExt.ComplexDilogarithmInversion

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

/-! ## The domain, and the chain rule

`hasDerivAt_cRogersL` takes four hypotheses, but only two of them are
independent: `1 − z ∈ slitPlane` says exactly `z ∉ [1,∞)`, which is `notCut`,
and `z ∈ slitPlane` already gives `z ≠ 0`. So the domain is the plane with
**both** real cuts removed, and that is what `rogersDomain` names. -/

/-- `1 − z ∈ slitPlane ↔ z ∈ notCut` — both say `z ∉ [1,∞)`. -/
theorem one_sub_mem_slitPlane_iff {z : ℂ} : (1 : ℂ) - z ∈ slitPlane ↔ z ∈ notCut := by
  rw [Complex.mem_slitPlane_iff, mem_notCut_iff]
  simp only [Complex.sub_re, Complex.one_re, Complex.sub_im, Complex.one_im, zero_sub,
    neg_ne_zero, sub_pos]
  exact or_comm

/-- **The domain of `cRogersL`**: `ℂ` with both real cuts `(−∞,0]` and `[1,∞)`
removed. `slitPlane` handles `log z`, `notCut` handles both `cLiTwoExt` and
`log (1−z)`. -/
def rogersDomain : Set ℂ := Complex.slitPlane ∩ notCut

theorem isOpen_rogersDomain : IsOpen rogersDomain :=
  Complex.isOpen_slitPlane.inter isOpen_notCut

theorem ne_zero_of_mem_rogersDomain {z : ℂ} (hz : z ∈ rogersDomain) : z ≠ 0 :=
  Complex.slitPlane_ne_zero hz.1

theorem one_sub_ne_zero_of_mem_rogersDomain {z : ℂ} (hz : z ∈ rogersDomain) :
    (1 : ℂ) - z ≠ 0 :=
  Complex.slitPlane_ne_zero (one_sub_mem_slitPlane_iff.mpr hz.2)

/-- A real point of `(0,1)` is in the domain — the base region the pentagon is
continued from. -/
theorem ofReal_mem_rogersDomain {t : ℝ} (h0 : 0 < t) (h1 : t < 1) :
    (t : ℂ) ∈ rogersDomain :=
  ⟨Complex.ofReal_mem_slitPlane.2 h0, Or.inr (by simpa using h1)⟩

/-- `hasDerivAt_cRogersL`, with the four hypotheses collapsed to membership of
`rogersDomain`. -/
theorem hasDerivAt_cRogersL_of_mem {z : ℂ} (hz : z ∈ rogersDomain) :
    HasDerivAt cRogersL
      (-(1 / 2) * (Complex.log (1 - z) / z + Complex.log z / (1 - z))) z :=
  hasDerivAt_cRogersL hz.2 (ne_zero_of_mem_rogersDomain hz) hz.1
    (one_sub_mem_slitPlane_iff.mpr hz.2)

/-- **The chain rule for `cRogersL`.** This is what assembling the pentagon
needs: each of its five arguments is a rational function of the differentiation
variable, and the composite's derivative is `L′` at the argument times the
argument's own derivative. -/
theorem hasDerivAt_cRogersL_comp {f : ℂ → ℂ} {f' z : ℂ} (hf : HasDerivAt f f' z)
    (hz : f z ∈ rogersDomain) :
    HasDerivAt (fun w => cRogersL (f w))
      (-(1 / 2) * (Complex.log (1 - f z) / f z + Complex.log (f z) / (1 - f z)) * f') z :=
  (hasDerivAt_cRogersL_of_mem hz).comp z hf

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

/-- **The one move every branch condition on the real square makes**: a complex
expression that happens to equal a *positive real* has complex logarithm the cast
of the real logarithm. Everything else is then `Real.log_mul` / `Real.log_div`,
with no branch left to choose. -/
theorem clog_of_eq_ofReal {a : ℝ} (ha : 0 < a) {z : ℂ} (hz : z = (a : ℂ)) :
    Complex.log z = ((Real.log a : ℝ) : ℂ) := by
  rw [hz, ← Complex.ofReal_log ha.le]

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

/-! ## Rogers inversion

The `Li₂` inversion `Li₂(z) + Li₂(1/z) + ½log(−z)² = −π²/6` is already proved in
`ComplexDilogarithmInversion`. Adding the two Rogers half-`log·log` terms, the
`log z · log(1−z)` pieces cancel against each other through
`log(1−1/z) + log(−z) = log(1−z)`, and what is left is quadratic in `log(−z)` but
**not** in `log z` alone.

That is why an inversion pair evaluates to `π²` plus `π` times an *angle* rather
than to a `log²` — the shape Route 58's link G3 needs. -/

/-- **Rogers inversion on `ℂ ∖ [0,∞)`.**

    L(z) + L(1/z) = −π²/6 − ½·log(−z)² + ½·log z·log(−z)

`z ∈ invDomain` is what both `cLiTwoExt` terms and `log(−z)` need; `arg z ≠ π`
is what `log(1/z) = −log z` needs, and it excludes exactly the negative reals,
where `invDomain` alone would not suffice. -/
theorem cRogersL_add_inv {z : ℂ} (hz : z ∈ invDomain) (harg : z.arg ≠ Real.pi) :
    cRogersL z + cRogersL z⁻¹
      = -((Real.pi ^ 2 / 6 : ℝ) : ℂ) - Complex.log (-z) ^ 2 / 2
        + Complex.log z * Complex.log (-z) / 2 := by
  have hcomb := invCombo_eq hz
  have hlog := log_one_sub_inv_add_log_neg hz
  have hinv : Complex.log z⁻¹ = -Complex.log z := Complex.log_inv z harg
  unfold invCombo at hcomb
  unfold cRogersL
  rw [hinv]
  linear_combination hcomb - (Complex.log z / 2) * hlog

end QOU.MathlibExt
