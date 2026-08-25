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

**The 5₂ sum rule is PROVED**: `FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.

-- Ref: [neumann2004] library/0307092v2/0307092v2.pdf, Prop 2.5 (Rogers `R`, and `R(z;p,q)`)
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

/-! ## Pinning a branch integer by a window

Route 58's remaining links all have the same shape: an algebraic identity such as
`a₃³·y₁ = −y₃` gives `3·log a₃ + log y₁ = log(−y₃) + 2πik`, and the work is
showing `k = 0`. The window that does it need not be tight — the arguments
involved live in `(0, π)` and `(0, π/2)`, so the sum lands in `(0, 5π/2)`, and
the only value there congruent to `π` mod `2π` is `π` itself.

`Archimedean/BranchIntegerPinning.lean` pins such an integer along a *continuous
family*; this is the single-point version, and it is what the saddle needs. -/

/-- If `exp u = c` and `Im u` lies in `(−π, π]`, then `u` **is** `log c`. -/
theorem clog_eq_of_exp_eq {u c : ℂ} (h : Complex.exp u = c)
    (hlo : -Real.pi < u.im) (hhi : u.im ≤ Real.pi) : Complex.log c = u := by
  rw [← h, Complex.log_exp hlo hhi]

/-- **The window lemma.** `exp u` a *negative real* forces `Im u ≡ π (mod 2π)`;
a window of width less than `2π` containing `π` then pins it. `(0, 3π)` is the
window the saddle supplies, and it is far from tight. -/
theorem im_eq_pi_of_exp_eq_neg_ofReal {u : ℂ} {t : ℝ} (ht : 0 < t)
    (h : Complex.exp u = ((-t : ℝ) : ℂ)) (hlo : -Real.pi < u.im) (hhi : u.im < 3 * Real.pi) :
    u.im = Real.pi := by
  have hpi : (0 : ℝ) < Real.pi := Real.pi_pos
  have hbase : Complex.exp (((Real.log t : ℝ) : ℂ) + (Real.pi : ℂ) * Complex.I)
      = ((-t : ℝ) : ℂ) := by
    rw [Complex.exp_add, Complex.exp_pi_mul_I, ← Complex.ofReal_exp, Real.exp_log ht]
    push_cast
    ring
  obtain ⟨n, hn⟩ := Complex.exp_eq_exp_iff_exists_int.mp (h.trans hbase.symm)
  have him : u.im = Real.pi + n * (2 * Real.pi) := by
    rw [hn]
    simp [Complex.add_im, Complex.mul_im, Complex.ofReal_im, Complex.ofReal_re]
  rw [him] at hlo hhi
  have hn0 : n = 0 := by
    have h1 : (-1 : ℝ) < n := by nlinarith [hlo, hpi]
    have h2 : (n : ℝ) < 1 := by nlinarith [hhi, hpi]
    have hl : (-1 : ℤ) < n := by exact_mod_cast h1
    have hr : n < (1 : ℤ) := by exact_mod_cast h2
    omega
  rw [him, hn0]
  push_cast
  ring

/-- **The saddle's log identity, from the window.** If `a³·b = −t` with `t > 0`
and the two arguments sit in `[0, π/2]` and `[0, π]`, then

    3·log a + log b = log t + iπ

with no branch correction: the sum of arguments lands in `[0, 5π/2] ⊂ (−π, 3π)`,
and `π` is the only value there congruent to `π` mod `2π`. The window is not
tight, which is the point — the bounds needed are crude sign conditions.

Applied to `a₃³·y₁ = −y₃` (`FiveTwoComplexPentagon.saddle_arg_cube'`) this is
the angle identity Route 58's link G3 rests on. -/
theorem clog_cube_mul {a b : ℂ} {t : ℝ} (ha : a ≠ 0) (hb : b ≠ 0) (ht : 0 < t)
    (h : a ^ 3 * b = ((-t : ℝ) : ℂ))
    (ha1 : 0 ≤ a.arg) (ha2 : a.arg ≤ Real.pi / 2) (hb1 : 0 ≤ b.arg) :
    3 * Complex.log a + Complex.log b
      = ((Real.log t : ℝ) : ℂ) + (Real.pi : ℂ) * Complex.I := by
  have hpi : (0 : ℝ) < Real.pi := Real.pi_pos
  set u : ℂ := 3 * Complex.log a + Complex.log b with hu
  have hexp : Complex.exp u = ((-t : ℝ) : ℂ) := by
    rw [hu, Complex.exp_add, show (3 : ℂ) * Complex.log a = Complex.log a + Complex.log a
      + Complex.log a by ring, Complex.exp_add, Complex.exp_add,
      Complex.exp_log ha, Complex.exp_log hb, ← h]
    ring
  have huim : u.im = 3 * a.arg + b.arg := by
    simp [hu, Complex.add_im, Complex.mul_im, Complex.log_im]
  have hlo : -Real.pi < u.im := by rw [huim]; nlinarith [Complex.arg_le_pi b]
  have hhi : u.im < 3 * Real.pi := by
    rw [huim]; nlinarith [Complex.arg_le_pi b]
  have him := im_eq_pi_of_exp_eq_neg_ofReal ht hexp hlo hhi
  have hlog : Complex.log ((-t : ℝ) : ℂ) = u := by
    rw [← hexp, Complex.log_exp (by rw [him]; linarith) (le_of_eq him)]
  have hneg : ((-t : ℝ) : ℂ) = -((t : ℝ) : ℂ) := by push_cast; ring
  rw [hneg, log_neg_ofReal ht] at hlog
  rw [← hlog]


/-! ## Infrastructure: off-the-real-axis logarithms, and argument bounds

Every remaining evaluation in the 5₂ chain has the same two needs — move `log(−z)`
to `log z`, and bound an argument crudely enough to pin a branch integer. Both
are Mathlib-gap-shaped, so they live here rather than in the 5₂ modules. -/

/-- `arg z ≠ π` as soon as `z` is off the real axis. -/
theorem arg_ne_pi_of_im_ne_zero {z : ℂ} (h : z.im ≠ 0) : z.arg ≠ Real.pi := by
  intro hc
  exact h (Complex.arg_eq_pi_iff.mp hc).2

/-- `log(−z) = log z − iπ` above the real axis. -/
theorem clog_neg_of_im_pos {z : ℂ} (h : 0 < z.im) :
    Complex.log (-z) = Complex.log z - (Real.pi : ℂ) * Complex.I := by
  rw [Complex.log, Complex.log, Complex.arg_neg_eq_arg_sub_pi_of_im_pos h, norm_neg]
  push_cast
  ring

/-- `log(−z) = log z + iπ` below the real axis. -/
theorem clog_neg_of_im_neg {z : ℂ} (h : z.im < 0) :
    Complex.log (-z) = Complex.log z + (Real.pi : ℂ) * Complex.I := by
  rw [Complex.log, Complex.log, Complex.arg_neg_eq_arg_add_pi_of_im_neg h, norm_neg]
  push_cast
  ring

/-- `0 ≤ arg z` from `0 ≤ Im z`. Named for readability at the use sites, where
the whole point is that the bound needed is a crude sign condition. -/
theorem arg_nonneg_of_im_nonneg {z : ℂ} (h : 0 ≤ z.im) : 0 ≤ z.arg :=
  Complex.arg_nonneg_iff.mpr h

/-- `arg z ≤ π/2` from `0 ≤ Re z`. -/
theorem arg_le_pi_div_two_of_re_nonneg {z : ℂ} (h : 0 ≤ z.re) : z.arg ≤ Real.pi / 2 :=
  Complex.arg_le_pi_div_two_iff.mpr (Or.inl h)

/-- A point off the real axis is in `invDomain`. -/
theorem mem_invDomain_of_im_ne_zero {z : ℂ} (h : z.im ≠ 0) : z ∈ invDomain :=
  mem_invDomain_iff.mpr (Or.inr h)

/-- **Rogers inversion, with the `log(−z)` eliminated.**

    L(z) + L(1/z) = π²/3 + (iπ/2)·log z          for `Im z > 0`

The `log²` terms cancel *completely* against the ones in `cRogersL_add_inv`, so
an inversion pair above the real axis is `π²` plus `π` times a single logarithm —
no quadratic term at all. This is the form Route 58's link G3 uses, and it is why
that link's value has no `log²` in it. -/
theorem cRogersL_add_inv_of_im_pos {z : ℂ} (h : 0 < z.im) :
    cRogersL z + cRogersL z⁻¹
      = ((Real.pi ^ 2 / 3 : ℝ) : ℂ) + ((Real.pi : ℂ) * Complex.I / 2) * Complex.log z := by
  have hne : z.im ≠ 0 := ne_of_gt h
  rw [cRogersL_add_inv (mem_invDomain_of_im_ne_zero hne) (arg_ne_pi_of_im_ne_zero hne),
    clog_neg_of_im_pos h]
  have hI : Complex.I ^ 2 = -1 := Complex.I_sq
  push_cast
  linear_combination (-((Real.pi : ℂ) ^ 2) / 2) * hI

/-- **Rogers inversion below the real axis.** The mirror of
`cRogersL_add_inv_of_im_pos`:

    L(z) + L(1/z) = π²/3 − (iπ/2)·log z          for `Im z < 0`

Same cancellation, opposite sign — the two together are the inversion half of the
anharmonic toolkit. -/
theorem cRogersL_add_inv_of_im_neg {z : ℂ} (h : z.im < 0) :
    cRogersL z + cRogersL z⁻¹
      = ((Real.pi ^ 2 / 3 : ℝ) : ℂ) - ((Real.pi : ℂ) * Complex.I / 2) * Complex.log z := by
  have hne : z.im ≠ 0 := ne_of_lt h
  rw [cRogersL_add_inv (mem_invDomain_of_im_ne_zero hne) (arg_ne_pi_of_im_ne_zero hne),
    clog_neg_of_im_neg h]
  have hI : Complex.I ^ 2 = -1 := Complex.I_sq
  push_cast
  linear_combination (-((Real.pi : ℂ) ^ 2) / 2) * hI

/-! ## The branch equation, from a multiplicative relation

`exp u = 1` puts `Im u` in `2πℤ`; a window of width `2π` pins which one. This is
the same window argument as `im_eq_pi_of_exp_eq_neg_ofReal`, in the form the
saddle branch equation needs. -/

/-- **A window pins the branch integer.** `exp u = 1` and
`Im u ∈ (2π(n−1), 2π(n+1))` force `u = n·2πi` — the window has width `4π` and
still contains only one multiple of `2π`, which is what makes the crude bounds
the saddle supplies sufficient. `Re u = 0` comes free; it is not a hypothesis. -/
theorem eq_intMul_two_pi_I_of_exp_eq_one {u : ℂ} {n : ℤ} (h : Complex.exp u = 1)
    (hlo : (2 * (n : ℝ) - 2) * Real.pi < u.im)
    (hhi : u.im < (2 * (n : ℝ) + 2) * Real.pi) :
    u = (n : ℂ) * (2 * (Real.pi : ℂ) * Complex.I) := by
  have hpi : (0 : ℝ) < Real.pi := Real.pi_pos
  obtain ⟨m, hm⟩ := Complex.exp_eq_one_iff.mp h
  have him : u.im = 2 * (m : ℝ) * Real.pi := by
    rw [hm]
    simp [Complex.mul_im, Complex.ofReal_im, Complex.ofReal_re]
    ring
  rw [him] at hlo hhi
  have hmn : m = n := by
    have h1 : (2 * (n : ℝ) - 2) < 2 * (m : ℝ) := by nlinarith
    have h2 : (2 * (m : ℝ)) < 2 * (n : ℝ) + 2 := by nlinarith
    have h1' : (2 * n - 2 : ℤ) < 2 * m := by exact_mod_cast h1
    have h2' : (2 * m : ℤ) < 2 * n + 2 := by exact_mod_cast h2
    omega
  rw [hm, hmn]

/-- `y² = (1−y)³` gives `exp(2·log y − 3·log(1−y)) = 1`. -/
theorem exp_branch_eq_one {y : ℂ} (hy : y ≠ 0) (h1y : (1 : ℂ) - y ≠ 0)
    (hsq : y ^ 2 = (1 - y) ^ 3) :
    Complex.exp (2 * Complex.log y - 3 * Complex.log (1 - y)) = 1 := by
  have e2 : Complex.exp (2 * Complex.log y) = y ^ 2 := by
    rw [two_mul, Complex.exp_add, Complex.exp_log hy]
    ring
  have e3 : Complex.exp (3 * Complex.log (1 - y)) = (1 - y) ^ 3 := by
    rw [show (3 : ℂ) = 1 + 1 + 1 by norm_num]
    rw [add_mul, add_mul, one_mul, Complex.exp_add, Complex.exp_add,
      Complex.exp_log h1y]
    ring
  rw [Complex.exp_sub, e2, e3, hsq, div_self (pow_ne_zero 3 h1y)]

/-- **The saddle branch equation, with its integer pinned by a window.**

    2·log y − 3·log(1−y) = ε·2πi

from `y² = (1−y)³` alone, plus a `2π`-wide window on the imaginary part. For the
5₂ cubic `y² = (1−y)³` **is** the cubic — `(1−y)³ − y² = −(y³−2y²+3y−1)`
identically — so this is the branch equation with nothing assumed about branches. -/
theorem branch_eq_of_window {y : ℂ} {n : ℤ} (hy : y ≠ 0) (h1y : (1 : ℂ) - y ≠ 0)
    (hsq : y ^ 2 = (1 - y) ^ 3)
    (hlo : (2 * (n : ℝ) - 2) * Real.pi
      < (2 * Complex.log y - 3 * Complex.log (1 - y)).im)
    (hhi : (2 * Complex.log y - 3 * Complex.log (1 - y)).im
      < (2 * (n : ℝ) + 2) * Real.pi) :
    2 * Complex.log y - 3 * Complex.log (1 - y)
      = 2 * (Real.pi : ℂ) * Complex.I * (n : ℂ) := by
  have h := eq_intMul_two_pi_I_of_exp_eq_one (exp_branch_eq_one hy h1y hsq) hlo hhi
  rw [h]
  ring

/-- The imaginary part of the branch expression is `2·arg y − 3·arg(1−y)`. -/
theorem branch_im {y : ℂ} :
    (2 * Complex.log y - 3 * Complex.log (1 - y)).im
      = 2 * y.arg - 3 * ((1 : ℂ) - y).arg := by
  simp [Complex.sub_im, Complex.mul_im, Complex.log_im, Complex.log_re]

/-- `Im(p/q) > 0` for a positive real `p` and a `q` below the axis. -/
theorem im_div_ofReal_pos {p : ℝ} (hp : 0 < p) {q : ℂ} (hq : q ≠ 0) (hqim : q.im < 0) :
    0 < ((p : ℂ) / q).im := by
  have hns : 0 < Complex.normSq q := Complex.normSq_pos.2 hq
  rw [Complex.div_im]
  simp only [Complex.ofReal_im, Complex.ofReal_re, zero_mul, zero_div, zero_sub, neg_pos]
  exact div_neg_of_neg_of_pos (mul_neg_of_pos_of_neg hp hqim) hns

/-- `Im(p/q) < 0` for a positive real `p` and a `q` above the axis. -/
theorem im_div_ofReal_neg {p : ℝ} (hp : 0 < p) {q : ℂ} (hq : q ≠ 0) (hqim : 0 < q.im) :
    ((p : ℂ) / q).im < 0 := by
  have hns : 0 < Complex.normSq q := Complex.normSq_pos.2 hq
  rw [Complex.div_im]
  simp only [Complex.ofReal_im, Complex.ofReal_re, zero_mul, zero_div, zero_sub,
    neg_lt_zero]
  exact div_pos (mul_pos hp hqim) hns

end QOU.MathlibExt
