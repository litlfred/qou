import QOU.QBeta.FiveTwoBranchPinnedB

/-!
# `S(φ)` in Lean, and `S(π) − S(0) = π²`

Bean `qou-trns`. Everything the envelope step needs was proved; what was missing
was the object it is about. `S(φ) = Σⱼ Re V(x φ, yⱼ φ)` had never been written
down as a Lean function, so `envelope_integrate` had nothing to be applied to.
This file writes it and applies it.

## What is defined

`arcX φ = exp(iφ)`, and

    envelopeS Y₁ Y₂ Y₃ φ = Σⱼ Re (V (arcX φ, Yⱼ φ)) .

The three root-paths are **parameters**, not constructed. Constructing a global
differentiable labelling is a monodromy question — the discriminant vanishes at
`φ₀` and two branches collide there — and `exists_hasDerivAt_root` gives one only
*locally*. Taking the labelling as a hypothesis is the honest factoring: it is
what the IFT supplies on each side of `φ₀`, and `envelope_integrate` is built to
tolerate exactly one exceptional point.

**Why one exceptional point is enough, and not a fudge.** `S` is a *symmetric*
function of the roots, so as a function of `φ` it needs no labelling at all — it
is well defined and continuous across `φ₀`, where the individual branches
collide and swap. Route 31 measures this: the symmetric sum satisfies
`S(φ) − S(0) = φ²` on both sides of `φ₀` and at `φ₀` itself, and `dS/dφ = 2φ` to
working precision. The labelling is needed only to *differentiate term by term*,
which is a local operation — hence a hypothesis, and hence one exceptional
point.

## The chain, and where each link comes from

| step | theorem |
|---|---|
| `d/dφ Re V(x φ, Yⱼ φ) = Re(∂V/∂x · i·x)` | `hasDerivAt_re_deformedV_envelope` |
| `Σⱼ ∂V/∂x = −2·log x / x` | `sum_dVdx_of_pinned`, fed by `logSumA_eq_log` and `logSumB_eq_neg_log` |
| `(−2 log x/x)·(i·x) = 2φ` | `envelope_value`, using `log(exp(iφ)) = iφ` |
| `S′ = 2φ` off one point ⟹ `S φ = S 0 + φ²` | `envelope_integrate` |

so `S(π) − S(0) = π²`, which is what the transport wants.

## ⚠ Two hypotheses that were nearly fatal

Both were caught by Route 31 G4, the non-vacuity gate, and both would have made
this file's main theorem true-but-empty.

**`−y ∈ slitPlane` is not in `VSide`.** An earlier draft had it, and it can
*never* hold at the positive real root — `−t` is a negative real. On this arc
one of the three roots is real and positive at every `φ`, so the theorem would
have been vacuous at all 199 sampled points. The `log(−y)` derivative is now
passed in, by `hasDerivAt_log_neg_of_slitPlane` off the cut or
`hasDerivAt_log_neg_ofReal` on it.

## ⚠ Read the hypothesis on `∂V/∂y` carefully

It is `Re(∂V/∂y · Yⱼ′) = 0`, **not** `∂V/∂y = 0`. The stronger form is *false*
at the positive real root, where `∂V/∂y = 2πi/t` because `−t` sits on `log`'s
cut — see `FiveTwoEnvelopeWiring`'s docstring and Route 30 G2. The weaker form
holds at all three roots, and real parts are all `S` ever sees.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Real Complex Set QOU.MathlibExt

/-! ### 1. The arc -/

/-- The transport path `x(φ) = e^{iφ}`. -/
noncomputable def arcX (φ : ℝ) : ℂ := Complex.exp ((φ : ℂ) * Complex.I)

theorem arcX_ne_zero (φ : ℝ) : arcX φ ≠ 0 := Complex.exp_ne_zero _

theorem hasDerivAt_arcX (φ : ℝ) : HasDerivAt arcX (Complex.I * arcX φ) φ := by
  have hlin : HasDerivAt (fun s : ℝ => (s : ℂ) * Complex.I) Complex.I φ := by
    simpa using (Complex.ofRealCLM.hasDerivAt (x := φ)).mul_const Complex.I
  have h := hlin.cexp
  unfold arcX
  rw [mul_comm Complex.I]
  exact h

theorem arcX_re (φ : ℝ) : (arcX φ).re = Real.cos φ := by
  simp [arcX, Complex.exp_mul_I, Complex.cos_ofReal_re]

theorem arcX_im (φ : ℝ) : (arcX φ).im = Real.sin φ := by
  simp [arcX, Complex.exp_mul_I, Complex.sin_ofReal_re]

theorem arcX_normSq (φ : ℝ) : (arcX φ).re ^ 2 + (arcX φ).im ^ 2 = 1 := by
  rw [arcX_re, arcX_im]
  nlinarith [Real.sin_sq_add_cos_sq φ]

/-- `log(e^{iφ}) = iφ` on the principal branch, for `φ ∈ (−π, π]`. -/
theorem log_arcX {φ : ℝ} (hlo : -π < φ) (hhi : φ ≤ π) :
    Complex.log (arcX φ) = (φ : ℂ) * Complex.I := by
  rw [arcX, Complex.log_exp] <;> simpa using ‹_›

theorem arcX_arg {φ : ℝ} (hlo : -π < φ) (hhi : φ ≤ π) : (arcX φ).arg = φ := by
  have := congrArg Complex.im (log_arcX hlo hhi)
  simpa [Complex.log_im] using this

/-! ### 2. `S(φ)` -/

/-- **`S(φ) = Σⱼ Re V(x φ, yⱼ φ)`.** The three root-paths are parameters; see
the module docstring for why they are not constructed here. -/
noncomputable def envelopeS (Y₁ Y₂ Y₃ : ℝ → ℂ) (φ : ℝ) : ℝ :=
  (deformedV (arcX φ, Y₁ φ)).re + (deformedV (arcX φ, Y₂ φ)).re
    + (deformedV (arcX φ, Y₃ φ)).re

/-- The side conditions under which `V` is differentiable at `(x, y)`: each
`Li₂` argument off the cut `[1,∞)` and nonzero. Bundled so the main statement
stays readable.

⚠ `−y ∈ slitPlane` is deliberately **absent**. An earlier draft included it, and
Route 31 G4 showed that made the whole statement **vacuous at the positive real
root** — which on this arc is one of the three roots at every `φ`. The `log(−y)`
derivative is passed separately instead, by whichever of
`hasDerivAt_log_neg_of_slitPlane` / `hasDerivAt_log_neg_ofReal` applies.

## ⚠⚠ `VSide` is FALSE at `φ = π`. Prove it over `Ico 0 π`, never `Icc 0 π`.

Route 36 G7. At the endpoint `x = −1` the three roots are the level-7 roots and
are **all real**, so for each of them `Im(x·y) = y·sin φ` vanishes — every
imaginary part goes at once. Two are still carried by `Re < 1`; the third,
`y = −2.2469796`, gives `x·y = +2.2469796`, real with `Re ≥ 1`. That is exactly
Li₂'s cut, so `hc₂` and `hc₃` fail there. Attempting `VSide` on the closed
interval is attempting something false.

The transport is **unaffected**, and it is worth seeing why rather than
assuming it: `envelopeS_total` asks for `ContinuousOn … (Icc 0 π)` but for
`HasDerivAt` only on `Ico 0 π`. The endpoint needs a *value*, not
differentiability — and `sum_re_deformedV_at_neg_one` already supplies that
value at `x = −1`, with no differentiability hypothesis anywhere in it. So the
two results meet exactly at the point where this one has to stop.

`hasDerivAt_envelopeS` below carries `hhi : φ ≤ π` for `arcX_arg`'s principal
range. That is not wrong — the theorem holds — but at `φ = π` its `VSide`
hypotheses cannot be met by the actual roots, so it has no instance there.

⚠ And this is invisible to a naive check. `exp(I * π)` evaluates to
`−1 + 4.1e-43·I`, and that spurious imaginary part satisfies `notCut`'s first
disjunct, so a numerical probe reports the endpoint as fine. Route 36 G7 builds
`x = −1` exactly for that reason — the same trap `root_mem_notCut` documents,
in a second place. -/
structure VSide (x y : ℂ) : Prop where
  hy0 : y ≠ 0
  hc₁ : y ∈ notCut
  hc₂ : x * y ∈ notCut
  hc₃ : y / x ∈ notCut
  hn₂ : x * y ≠ 0
  hn₃ : y / x ≠ 0

/-! ### 2b. `VSide`, discharged from the curve alone

`VSide` is the hypothesis that was once **vacuous**, so the order of work here was
deliberate: Route 36 measured it *before* any of this was written, and found all
six conditions holding simultaneously at all 597 interior checks (199 arc points
× 3 roots) — and **failing at `φ = π`**, which is why every statement below
carries `x.im ≠ 0`. Only then was proving them worth anything.

Four fields fall out of `curve x y = 0` and `|x| = 1` with no root structure at
all; the other two follow in §2c. The bean expected those two to need the
labelling and a case analysis over `y₂`, `y₃` and the sign of `c`. They did not —
the route through the crossing is uniform in the root, so `hc₂` is one theorem
and `hc₃` is an involution. -/

/-- **No root of the curve vanishes**, for `x ≠ 0`: `curve x 0 = −x`. -/
theorem root_ne_zero {x y : ℂ} (hx0 : x ≠ 0) (hc : curve x y = 0) : y ≠ 0 := by
  rintro rfl
  refine hx0 (neg_eq_zero.mp ?_)
  rw [← hc]; unfold curve; ring

/-- **Every root of the curve on `|x| = 1` lies in `notCut`** — the real/complex
case split, discharged.

`notCut = {w | Im w ≠ 0 ∨ Re w < 1}`. A root with `Im ≠ 0` takes the first
disjunct outright. A **real** root takes the second: on `|x| = 1` the `y`-cubic
is `unitCubic (Re x)` with real coefficients, and no real root of that reaches
`1` when `Re x ≤ 1` (`unitCubic_root_lt_one`).

⚠ Both branches are live on the arc, so neither is defensive. Route 36 G5: the
arc crosses the discriminant at `c* = −0.74221766588`, giving **three** real
roots at 46 of 199 sampled points and one real plus a conjugate pair at the other
153. That is also why the real branch leans on `unitCubic_root_lt_one` — which
bounds *every* real root — rather than on `exists_pinning_data`'s distinguished
`t ∈ (0,1)`, which would leave two of the three unhandled at those 46 points.

⚠ And the disjunct attribution here is the *exact* one, not the numerical one.
`polyroots` returns `|Im| ~ 2.6e-41` for the real root at one arc point, so a
split driven by a floating `Im ≠ 0` test would route that root through the first
disjunct — which is false in exact arithmetic, and is the branch this proof
cannot take. Route 36 G2 classifies by root type for that reason.

⚠ **`hx` is load-bearing — do not weaken it.** The statement reads as though it
might hold for general `x`, and it does not. The curve is *quadratic* in `x`, so
fixing a bad `y` and solving produces a counterexample outright: at `y = 2` it is
`2x² − 9x + 2 = 0`, giving `x = (9 ± √65)/4`, both real and neither on the unit
circle, with `y = 2` real and `Re y ≥ 1` — so `y ∉ notCut`. Route 36 G6 carries
it exactly. `hx` is used twice and essentially: once for `curve_eq_unitCubic`,
once for `Re x ≤ 1`. -/
theorem root_mem_notCut {x y : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) (hx0 : x ≠ 0)
    (hc : curve x y = 0) : y ∈ notCut := by
  rcases eq_or_ne y.im 0 with him | him
  · -- a REAL root: `Im = 0`, so only `Re < 1` can carry it
    refine Or.inr ?_
    have hy : y = ((y.re : ℝ) : ℂ) := by
      apply Complex.ext <;> simp [him]
    have hcu : x * (y ^ 3 - 2 * (x.re : ℂ) * y ^ 2 + (2 * (x.re : ℂ) + 1) * y - 1) = 0 := by
      rw [← curve_eq_unitCubic hx y]; unfold curve at hc; exact hc
    have hbr : y ^ 3 - 2 * (x.re : ℂ) * y ^ 2 + (2 * (x.re : ℂ) + 1) * y - 1 = 0 :=
      (mul_eq_zero.mp hcu).resolve_left hx0
    rw [hy] at hbr
    have hreal : unitCubic x.re y.re = 0 := by
      have hcast : ((unitCubic x.re y.re : ℝ) : ℂ) = 0 := by
        rw [← hbr]; unfold unitCubic; push_cast; ring
      exact_mod_cast hcast
    exact unitCubic_root_lt_one (re_le_one_of_normSq_eq_one hx) hreal
  · exact Or.inl him

/-- `x·y ≠ 0` at a root — `VSide.hn₂`. -/
theorem mul_root_ne_zero {x y : ℂ} (hx0 : x ≠ 0) (hc : curve x y = 0) : x * y ≠ 0 :=
  mul_ne_zero hx0 (root_ne_zero hx0 hc)

/-- `y/x ≠ 0` at a root — `VSide.hn₃`. -/
theorem div_root_ne_zero {x y : ℂ} (hx0 : x ≠ 0) (hc : curve x y = 0) : y / x ≠ 0 :=
  div_ne_zero (root_ne_zero hx0 hc) hx0

/-- For **real** `y ≠ 0` and `x` off the real axis, `Im(x·y) = Im x · Re y ≠ 0`.

This is what carries every *real* root on the **open** arc, with no case
analysis — and it is exactly what expires at `φ = π`, where `Im x = 0` and the
root `−2.2469796` is left with `Re(x·y) = 2.2469796` on the cut. See the `VSide`
docstring. -/
theorem mul_mem_notCut_of_real {x y : ℂ} (hxim : x.im ≠ 0) (hy : y.im = 0) (hy0 : y ≠ 0) :
    x * y ∈ notCut := by
  refine Or.inl ?_
  have hre : y.re ≠ 0 := fun h => hy0 (Complex.ext (by simpa using h) (by simpa using hy))
  simpa [Complex.mul_im, hy] using mul_ne_zero hxim hre

/-- The `y/x` counterpart: `Im(y/x) = −Re y · Im x / ‖x‖²`. -/
theorem div_mem_notCut_of_real {x y : ℂ} (hx0 : x ≠ 0) (hxim : x.im ≠ 0) (hy : y.im = 0)
    (hy0 : y ≠ 0) : y / x ∈ notCut := by
  refine Or.inl ?_
  have hre : y.re ≠ 0 := fun h => hy0 (Complex.ext (by simpa using h) (by simpa using hy))
  have hns : Complex.normSq x ≠ 0 := by
    simpa [Complex.normSq_eq_zero] using hx0
  have hval : (y / x).im = -(y.re * x.im) / Complex.normSq x := by
    rw [Complex.div_im, hy]; ring
  rw [hval]
  exact div_ne_zero (neg_ne_zero.mpr (mul_ne_zero hre hxim)) hns

/-- **If `x·y` is real on the arc, its value satisfies `r⁵ − r³ + 1 = 0`.**

This is the exact characterisation of Route 36 G3's crossing — the one the
retracted G3 asserted could not happen. The derivation needs no Vieta and no
root tracking:

* substituting `x·y = r` into `curve x y = 0` after multiplying by `x²` gives a
  **cubic in `x` with real coefficients** (`r` is real);
* on `|x| = 1` the quadratic `x² + 1 = 2·(Re x)·x` (`unitCircle_quadratic`) is
  the minimal polynomial of a non-real `x` over `ℝ`, so that cubic reduces to
  `α·x + β` with `α, β` **real** in `r` and `c = Re x`;
* `x.im ≠ 0` then forces `α = 0` *and* `β = 0` — two real equations;
* and `r⁵ − r³ + 1 = α + (r² + 2c)·β` identically.

`hxim` is doing real work at the third step: without it the two coefficients
could trade off against each other, and indeed at `φ = 0` and `φ = π` — the
exact points where `x.im = 0` — the conclusion fails, as it must, since `x·y` is
real there for *every* root. -/
theorem quintic_of_mul_real {x y : ℂ} {r : ℝ} (hx : x.re ^ 2 + x.im ^ 2 = 1)
    (hxim : x.im ≠ 0) (hc : curve x y = 0) (hxy : x * y = (r : ℂ)) :
    r ^ 5 - r ^ 3 + 1 = 0 := by
  set c : ℝ := x.re with hcdef
  -- the curve, cleared of `y` by `x·y = r`: a cubic in `x` with real coefficients
  have hA : (r : ℂ) ^ 3 - (x ^ 2 + 1) * (r : ℂ) ^ 2
      + x * (x ^ 2 + x + 1) * (r : ℂ) - x ^ 3 = 0 := by
    have hcc : x * y ^ 3 - (x ^ 2 + 1) * y ^ 2 + (x ^ 2 + x + 1) * y - x = 0 := by
      rw [← hc]; unfold curve; ring
    linear_combination x ^ 2 * hcc
      - ((r : ℂ) ^ 2 + (r : ℂ) * (x * y) + (x * y) ^ 2
          - (x ^ 2 + 1) * ((r : ℂ) + x * y) + x * (x ^ 2 + x + 1)) * hxy
  -- `x² − 2cx + 1 = 0`: the minimal polynomial of a non-real point of the circle
  have hg : x ^ 2 - 2 * (c : ℂ) * x + 1 = 0 := by
    have := unitCircle_quadratic hx
    rw [← hcdef] at this
    linear_combination -this
  -- reduce `hA` modulo `hg`: quotient `(r−1)(x + 2c − r)`, remainder `αx + β`
  have hsplit : ((-2 * c * r ^ 2 + 2 * c * (2 * c + 1) * r - (4 * c ^ 2 - 1) : ℝ) : ℂ) * x
      + ((r ^ 3 - (2 * c + 1) * r + 2 * c : ℝ) : ℂ) = 0 := by
    push_cast
    linear_combination hA - ((r : ℂ) - 1) * (x + 2 * (c : ℂ) - (r : ℂ)) * hg
  -- `α` and `β` are real and `x` is not, so both vanish
  have hα : -2 * c * r ^ 2 + 2 * c * (2 * c + 1) * r - (4 * c ^ 2 - 1) = 0 := by
    have him := congrArg Complex.im hsplit
    simp only [Complex.add_im, Complex.mul_im, Complex.ofReal_re, Complex.ofReal_im,
      zero_mul, add_zero, Complex.zero_im] at him
    exact (mul_eq_zero.mp him).resolve_right hxim
  have hβ : r ^ 3 - (2 * c + 1) * r + 2 * c = 0 := by
    rw [show ((-2 * c * r ^ 2 + 2 * c * (2 * c + 1) * r - (4 * c ^ 2 - 1) : ℝ) : ℂ) = 0 by
      rw [hα]; norm_num] at hsplit
    have h0 : (r : ℂ) ^ 3 - (2 * (c : ℂ) + 1) * (r : ℂ) + 2 * (c : ℂ) = 0 := by
      simpa using hsplit
    exact_mod_cast h0
  linear_combination hα + (r ^ 2 + 2 * c) * hβ

/-- **No real root of `r⁵ − r³ + 1` reaches `1`** — because `r ≥ 1` forces
`r⁵ − r³ + 1 = r³(r² − 1) + 1 ≥ 1 > 0`.

This quintic is not decoration. Route 36 G3 originally claimed that `x·y` is
*never* real on the arc, so that `x·y ∈ notCut` would need no case split. That
was **false**, and the gate hid it by testing a grid minimum of `|Im(x·y)|`,
which is not a lower bound: refining the grid shrank the minimum like `1/N`,
the signature of a zero crossing. There is exactly one crossing on `(0,π)`.

At it, `x·y` is real with value `r = −1.2365057033914990243`, and `r` is exactly
the unique real root of this quintic — with `c = r(1+r)/2` and `t = 1/r²`,
matching to 20 digits. It falls out of Vieta: if `x·y₂ = r` is real with
`|x| = 1` then `y₂ = r·conj x`, so `y₃ = r·x`, and substituting into the curve
makes `x` a root of a cubic with **real** coefficients; `x` is non-real on the
open arc, so `conj x` is a root too and the third is `−r²`.

So `x·y ∈ notCut` at the crossing holds via `Re < 1` — the *opposite* disjunct
from the retracted claim — and this lemma is what supplies it. -/
theorem quintic_root_lt_one {r : ℝ} (h : r ^ 5 - r ^ 3 + 1 = 0) : r < 1 := by
  by_contra hle
  push_neg at hle
  have h3 : (1 : ℝ) ≤ r ^ 3 := one_le_pow₀ hle
  have h2 : (0 : ℝ) ≤ r ^ 2 - 1 := by nlinarith
  nlinarith [mul_nonneg (by linarith : (0:ℝ) ≤ r ^ 3) h2]

/-- **`VSide` reduced to its two genuinely root-dependent fields.**

Given the two `notCut` memberships that need the labelling, the other four are
supplied. Stated this way so the residue is visible in a signature rather than in
prose: what is left of `VSide` is `x·y` and `y/x` off the cut, nothing else.

Route 36 G3 measured both — they are carried by `Im ≠ 0` at every one of the 597
checks with `min |Im| = 0.00676`, a genuine margin and never a near-miss, so
neither needs a case split of its own. `exists_pinning_data` already supplies
part: `(x·y₃).im < 0`, and `(x·y₂).im < 0` once `c < 0`. -/
theorem vSide_of_notCut_mul_div {x y : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) (hx0 : x ≠ 0)
    (hc : curve x y = 0) (h₂ : x * y ∈ notCut) (h₃ : y / x ∈ notCut) : VSide x y :=
  { hy0 := root_ne_zero hx0 hc
    hc₁ := root_mem_notCut hx hx0 hc
    hc₂ := h₂
    hc₃ := h₃
    hn₂ := mul_root_ne_zero hx0 hc
    hn₃ := div_root_ne_zero hx0 hc }

/-! ### 2c. The last two fields, and `VSide` in full on the open arc -/

/-- **`x ↦ x⁻¹` is an involution of the curve**: `curve x⁻¹ y · x² = curve x y`.

So `x·y` and `y/x` are the *same* `Li₂` argument, read at `x` and at `x⁻¹` —
and on `|x| = 1` the two points differ only by the sign of `Im x`. `hc₃` therefore
needs no argument of its own, and this is also why Route 36 G3 found the two
crossings at the same `φ` with the same value. -/
theorem curve_inv {x : ℂ} (hx0 : x ≠ 0) (y : ℂ) : curve x⁻¹ y * x ^ 2 = curve x y := by
  unfold curve
  field_simp
  ring

/-- **`x·y ∈ notCut` for every root on the open arc** — `VSide.hc₂`, in full.

The disjunction, used as a disjunction. If `x·y` has nonzero imaginary part the
first disjunct closes it. If it is real — which Route 36 G3 shows *does* happen,
exactly once on `(0,π)`, contrary to that gate's retracted claim — then
`quintic_of_mul_real` pins its value to a root of `r⁵ − r³ + 1` and
`quintic_root_lt_one` puts that below `1`, closing the second.

Note which fact does the work in each branch. For a *real* root the first
disjunct is elementary: `Im(x·y) = Im x · Re y`, nonzero on the open arc — and
that is exactly what expires at `φ = π`, taking `VSide` with it. The quintic is
needed only for the complex pair, at the one point where its `Im` vanishes. -/
theorem mul_mem_notCut {x y : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) (hxim : x.im ≠ 0)
    (hc : curve x y = 0) : x * y ∈ notCut := by
  rcases eq_or_ne (x * y).im 0 with him | him
  · refine Or.inr ?_
    have hxy : x * y = ((((x * y).re : ℝ)) : ℂ) := by
      apply Complex.ext <;> simp [him]
    exact quintic_root_lt_one (quintic_of_mul_real hx hxim hc hxy)
  · exact Or.inl him

/-- **`y/x ∈ notCut` for every root on the open arc** — `VSide.hc₃`, in full.

`mul_mem_notCut` at `x⁻¹`, via `curve_inv`. On `|x| = 1` the inverse has the same
real part and the negated imaginary part, so both hypotheses transport unchanged. -/
theorem div_mem_notCut {x y : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) (hxim : x.im ≠ 0)
    (hc : curve x y = 0) : y / x ∈ notCut := by
  have hx0 : x ≠ 0 := fun h => hxim (by rw [h]; simp)
  have hns : Complex.normSq x = 1 := by
    rw [Complex.normSq_apply]; nlinarith [hx]
  have hre : (x⁻¹).re = x.re := by rw [Complex.inv_re, hns, div_one]
  have him : (x⁻¹).im = -x.im := by rw [Complex.inv_im, hns, div_one]
  have hxi : (x⁻¹).re ^ 2 + (x⁻¹).im ^ 2 = 1 := by rw [hre, him]; nlinarith [hx]
  have hxiim : (x⁻¹).im ≠ 0 := by rw [him]; exact neg_ne_zero.mpr hxim
  have hci : curve x⁻¹ y = 0 := by
    have h2 : curve x⁻¹ y * x ^ 2 = 0 := by rw [curve_inv hx0, hc]
    exact (mul_eq_zero.mp h2).resolve_right (pow_ne_zero 2 hx0)
  simpa [inv_mul_eq_div] using mul_mem_notCut hxi hxiim hci

/-- **`VSide` in full, at every root of the curve on the OPEN arc.**

All six fields, no root structure, no labelling, no case analysis left to the
caller. `hxim : x.im ≠ 0` is the open-arc condition and it is load-bearing, not
decorative: at `φ = π` it is exactly what fails, and `VSide` fails with it
(Route 36 G7). Proving this over `Icc 0 π` would be proving something false. -/
theorem vSide_of_root {x y : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) (hxim : x.im ≠ 0)
    (hc : curve x y = 0) : VSide x y :=
  vSide_of_notCut_mul_div hx (fun h => hxim (by rw [h]; simp)) hc
    (mul_mem_notCut hx hxim hc) (div_mem_notCut hx hxim hc)

/-- **Every root takes exactly one of the two `log(−y)` routes, and which one is
decided by the root alone.**

`hasDerivAt_envelopeS` needs `d/du log(−Yⱼ u)` and offers two ways to get it:
`hasDerivAt_log_neg_of_slitPlane` when `−y` is off `log`'s cut, and
`hasDerivAt_log_neg_ofReal` when it is on it. `−y ∈ slitPlane` unfolds to
`Re y < 0 ∨ Im y ≠ 0`, so it fails **precisely** at a positive real `y`.

Neither route is redundant. On this arc exactly one root is positive real at
every `φ` (`exists_root_mem_Ioo` puts it in `(0,1)`), so route 2 is needed
everywhere and route 1 is impossible there — that is correction 6's fact, in the
form a caller can use. The other two roots take route 1 either because they are
genuinely complex or, at the 46 arc points where all three roots are real,
because they are negative (`real_root_neg_of_ne`).

⚠ **This settles the routing, not the derivative.** Route 2's lemma is stated
for a path of the form `fun u => ((t u : ℝ) : ℂ)` — it needs `Y` to be
*real-valued near `φ`*, not merely real *at* `φ`. That is a condition on the
labelling rather than on the root, so it belongs to the concrete `Y₁ Y₂ Y₃` still
open in `qou-glbl`. Stating the dichotomy here makes that the only thing left to
supply, instead of leaving both the routing and the path condition implicit. -/
theorem log_neg_route {x y : ℂ} (hx0 : x ≠ 0) (hc : curve x y = 0) :
    -y ∈ Complex.slitPlane ∨ (0 < y.re ∧ y.im = 0) := by
  rcases eq_or_ne y.im 0 with him | him
  · have hy0 : y ≠ 0 := root_ne_zero hx0 hc
    have hre : y.re ≠ 0 := fun h => hy0 (Complex.ext (by simpa using h) (by simpa using him))
    rcases hre.lt_or_gt with hneg | hpos
    · exact Or.inl (Or.inl (by simpa using hneg))
    · exact Or.inr ⟨hpos, him⟩
  · exact Or.inl (Or.inr (by simpa using him))

/-! ### 3. `S′(φ) = 2φ` -/

/-- **The transport's derivative.**

Three envelope collapses, summed by `sum_dVdx_of_pinned`, evaluated by
`envelope_value`. The two pinned log-sums `hA` and `hB` are hypotheses here and
theorems elsewhere (`logSumA_eq_log`, `logSumB_eq_neg_log`); the `Re(∂V/∂y·Y′)`
conditions are the weakened envelope hypothesis, which is the one that is true
at all three roots. -/
theorem hasDerivAt_envelopeS {Y₁ Y₂ Y₃ : ℝ → ℂ} {Y₁' Y₂' Y₃' : ℂ} {φ : ℝ}
    (hlo : -π < φ) (hhi : φ ≤ π)
    (hY₁ : HasDerivAt Y₁ Y₁' φ) (hY₂ : HasDerivAt Y₂ Y₂' φ) (hY₃ : HasDerivAt Y₃ Y₃' φ)
    (hs₁ : VSide (arcX φ) (Y₁ φ)) (hs₂ : VSide (arcX φ) (Y₂ φ))
    (hs₃ : VSide (arcX φ) (Y₃ φ))
    (hl₁ : HasDerivAt (fun u => Complex.log (-Y₁ u)) (Y₁' / Y₁ φ) φ)
    (hl₂ : HasDerivAt (fun u => Complex.log (-Y₂ u)) (Y₂' / Y₂ φ) φ)
    (hl₃ : HasDerivAt (fun u => Complex.log (-Y₃ u)) (Y₃' / Y₃ φ) φ)
    (he₁ : (dVdy (arcX φ) (Y₁ φ) * Y₁').re = 0)
    (he₂ : (dVdy (arcX φ) (Y₂ φ) * Y₂').re = 0)
    (he₃ : (dVdy (arcX φ) (Y₃ φ) * Y₃').re = 0)
    (hA : Complex.log (1 - arcX φ * Y₁ φ) + Complex.log (1 - arcX φ * Y₂ φ)
      + Complex.log (1 - arcX φ * Y₃ φ) = Complex.log (arcX φ))
    (hB : Complex.log (1 - Y₁ φ / arcX φ) + Complex.log (1 - Y₂ φ / arcX φ)
      + Complex.log (1 - Y₃ φ / arcX φ) = -Complex.log (arcX φ)) :
    HasDerivAt (envelopeS Y₁ Y₂ Y₃) (2 * φ) φ := by
  have hx0 := arcX_ne_zero φ
  have hX := hasDerivAt_arcX φ
  -- the three envelope collapses
  have h₁ := hasDerivAt_re_deformedV_envelope (X := arcX) (Y := Y₁) hX hY₁
    hx0 hs₁.hy0 hs₁.hc₁ hs₁.hc₂ hs₁.hc₃ hs₁.hn₂ hs₁.hn₃ hl₁ he₁
  have h₂ := hasDerivAt_re_deformedV_envelope (X := arcX) (Y := Y₂) hX hY₂
    hx0 hs₂.hy0 hs₂.hc₁ hs₂.hc₂ hs₂.hc₃ hs₂.hn₂ hs₂.hn₃ hl₂ he₂
  have h₃ := hasDerivAt_re_deformedV_envelope (X := arcX) (Y := Y₃) hX hY₃
    hx0 hs₃.hy0 hs₃.hc₁ hs₃.hc₂ hs₃.hc₃ hs₃.hn₂ hs₃.hn₃ hl₃ he₃
  have hsum := (h₁.add h₂).add h₃
  -- the three `∂V/∂x` sum to `−2 log x / x`, and against `i·x` that is `2φ`
  have hcollect : dVdx (arcX φ) (Y₁ φ) + dVdx (arcX φ) (Y₂ φ) + dVdx (arcX φ) (Y₃ φ)
      = -2 * Complex.log (arcX φ) / arcX φ := by
    unfold dVdx
    exact sum_dVdx_of_pinned hx0 hA hB
  have hval : ((dVdx (arcX φ) (Y₁ φ) + dVdx (arcX φ) (Y₂ φ) + dVdx (arcX φ) (Y₃ φ))
      * (Complex.I * arcX φ)) = ((2 * φ : ℝ) : ℂ) := by
    rw [hcollect]
    exact envelope_value φ hx0 (log_arcX hlo hhi)
  have hre : (dVdx (arcX φ) (Y₁ φ) * (Complex.I * arcX φ)).re
      + (dVdx (arcX φ) (Y₂ φ) * (Complex.I * arcX φ)).re
      + (dVdx (arcX φ) (Y₃ φ) * (Complex.I * arcX φ)).re = 2 * φ := by
    have := congrArg Complex.re hval
    simpa [add_mul, Complex.add_re] using this
  unfold envelopeS
  rwa [hre] at hsum

/-! ### 4. `S(π) − S(0) = π²` -/

/-- **The transport's total.** `envelope_integrate` applied to `S`, tolerating
one exceptional point — which is `φ₀`, where the discriminant vanishes and no
differentiable root labelling exists (`exists_unit_circle_disc_zero`). -/
theorem envelopeS_total {Y₁ Y₂ Y₃ : ℝ → ℂ} {c : ℝ}
    (hcont : ContinuousOn (envelopeS Y₁ Y₂ Y₃) (Icc 0 π))
    (hderiv : ∀ φ ∈ Ico (0 : ℝ) π, φ ≠ c → HasDerivAt (envelopeS Y₁ Y₂ Y₃) (2 * φ) φ) :
    envelopeS Y₁ Y₂ Y₃ π = envelopeS Y₁ Y₂ Y₃ 0 + π ^ 2 :=
  envelope_integrate hcont (fun φ hφ hne => (hderiv φ hφ hne).hasDerivWithinAt) π
    ⟨Real.pi_pos.le, le_rfl⟩

/-! ### 5. Non-vacuity -/

/-- **Non-vacuity for `envelopeS_total`.** The conclusion is not a tautology
about an empty hypothesis set: a constant-plus-square `S` satisfies both
hypotheses and the conclusion reads `π² = 0 + π²`.

The check with real content is Route 30, which measures `S′ = 2φ` on the actual
arc — per root to `4.6e-41` and summed to `9.2e-41`. -/
theorem envelopeS_total_nonvacuous {c : ℝ} :
    ∀ S : ℝ → ℝ, (∀ φ, S φ = φ ^ 2) →
      ContinuousOn S (Icc 0 π) ∧
      (∀ φ ∈ Ico (0 : ℝ) π, φ ≠ c → HasDerivAt S (2 * φ) φ) ∧
      S π = S 0 + π ^ 2 := by
  intro S hS
  have hfun : S = fun φ => φ ^ 2 := funext hS
  subst hfun
  refine ⟨(continuous_pow 2).continuousOn, ?_, by simp⟩
  intro φ _ _
  simpa using hasDerivAt_pow 2 φ

end QOU.QBeta.FiveTwoDeformedSaddle
