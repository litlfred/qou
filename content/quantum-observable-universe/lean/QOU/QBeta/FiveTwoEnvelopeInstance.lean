import QOU.QBeta.FiveTwoRootLabelling
import QOU.QBeta.FiveTwoTransport
import QOU.QBeta.FiveTwoPairSaddle
import QOU.MathlibExt.ComplexDilogarithmInversion

/-!
# The transport's hypotheses, discharged at the *concrete* labelling — `qou-glbl`

`FiveTwoRootLabelling` builds `Y₁ Y₂ Y₃` and proves them differentiable and
curve-solving. `FiveTwoTransport` states `hasDerivAt_envelopeS`, whose hypotheses
are about an arbitrary labelling. This file joins them: every hypothesis that can
be discharged pointwise from the construction, discharged.

## Why a separate module

`VSide` is declared in `FiveTwoTransport`, and `Yreal`/`Ypair` in
`FiveTwoRootLabelling`; neither imports the other, and neither should — the
labelling is about the real cubic and the transport is about `V`. This is the
join, and it is the first place the two can be spoken of together.

## What is discharged here

| hypothesis of `hasDerivAt_envelopeS` | supplied by |
|---|---|
| `hY₁ hY₂ hY₃` — differentiability | `hasDerivAt_Yreal`, `hasDerivAt_Ypair_fst/snd` |
| `hs₁ hs₂ hs₃` — `VSide` | `vSide_Yreal`, `vSide_Ypair_fst/snd` (below) |
| `hl₁` — `log(−Y₁)′`, **route 2** | `hasDerivAt_log_neg_Yreal` (below) |
| `hl₂ hl₃` — `log(−Y₂,₃)′`, **route 1** | `hasDerivAt_log_neg_Ypair_*` (below) |
| `hA` — `Σ log(1 − x·Yⱼ) = log x` | `logSumA_concrete` (below) |
| `hB` — `Σ log(1 − Yⱼ/x) = −log x` | `logSumB_concrete` (below) |

and the routing is not a choice: `log_neg_route` says `−y ∈ slitPlane` fails
*precisely* at a positive real root, `Y₁` is that root at every `φ` (Route 36 G8
measures exactly one per arc point), and `Y₂ Y₃` are non-real wherever
`pairDisc φ < 0`. So `Y₁` must take route 2 and the pair must take route 1 — one
lemma each, no case analysis.

## ⚠ Two hypotheses, two different arcs

* `sin φ ≠ 0` — the **open** arc. `VSide` is FALSE at `φ = π` (Route 36 G7), so
  this is not a convenience; it is the largest set on which these statements are
  true at all.
* `pairDisc φ < 0` — off the **collision**. This is the exceptional point
  `envelopeS_total` tolerates, and Route 36 G12 measures it holding at 153 of 199
  arc points, so the pair statements are non-vacuous rather than merely typed.

## ⚠ `hA` and `hB` are not symmetric, and Lean found it

`logSumA_concrete` needs **no** off-collision hypothesis; `logSumB_concrete` does.
`pairDisc φ < 0` was written into both and the linter flagged it unused in the
first. That is structure, not a slip: `logSumA`'s signs are `Im(x·y)` facts proved
straight from the root structure, while `logSumB`'s come through the conjugacy
`Im(y/x) = −Im(x·conj y)`, and the pair is conjugate only where `pairDisc φ < 0`.
Past the discriminant flip they are two distinct reals — each its own conjugate,
neither the other's. So `hA` survives the collision and `hB` does not.

## What is NOT here

`heⱼ` for the pair — it needs `k = 0`, and Route 36 G13 shows no term-by-term
bound on the four `arg`s reaches it (they sum to 11.857 > 2π). And `hcont` at
`φ = π` (Route 36 G11) — `envelopeS_total` wants continuity on the **closed**
interval, the `Li₂` argument sits on the cut there, and nothing has discharged it.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Real Complex Set QOU.MathlibExt

/-! ### 1. `VSide` at the concrete branches -/

theorem vSide_Yreal {φ : ℝ} (h : Real.sin φ ≠ 0) : VSide (arcX φ) (Yreal φ) :=
  vSide_of_root (arcX_normSq φ) (by rw [arcX_im]; exact h)
    (curve_Yreal (arcX_normSq φ) (arcX_re φ))

theorem vSide_Ypair_fst {φ : ℝ} (h : Real.sin φ ≠ 0) : VSide (arcX φ) (Ypair φ).1 :=
  vSide_of_root (arcX_normSq φ) (by rw [arcX_im]; exact h)
    (curve_Ypair (arcX_normSq φ) (arcX_re φ)).1

theorem vSide_Ypair_snd {φ : ℝ} (h : Real.sin φ ≠ 0) : VSide (arcX φ) (Ypair φ).2 :=
  vSide_of_root (arcX_normSq φ) (by rw [arcX_im]; exact h)
    (curve_Ypair (arcX_normSq φ) (arcX_re φ)).2

/-! ### 1b. `hA` and `hB` at the concrete labelling

`logSumA_eq_log` / `logSumB_eq_neg_log` take eleven hypotheses each. Every one is
now available: Vieta from `vieta_hv1/hv2/e3`, the four signs from
`im_mul_Ypair_*` / `im_div_Ypair_*`, the `≠ 0`s from `VSide` (below), and the arc
facts from `arcX_*`. This is the assembly. -/

/-- `w ∈ notCut → 1 − w ≠ 0`. `notCut` excludes `w = 1` — that point has `Im = 0`
and `Re = 1`, failing both disjuncts — so the nonvanishing `logSumA`/`logSumB`
want comes free from `VSide`. -/
theorem one_sub_ne_zero_of_mem_notCut {w : ℂ} (h : w ∈ notCut) : (1 : ℂ) - w ≠ 0 := by
  intro hz
  have hw : w = 1 := by linear_combination -hz
  rw [hw] at h
  rcases h with h | h <;> simp at h

/-- **`hA` at the concrete labelling — and it needs NO off-collision hypothesis.**

Lean flagged `pairDisc φ < 0` as unused here, and that is a real asymmetry rather
than a slip. `logSumA`'s signs are `Im(x·y)` facts, which `im_mul_otherRoots_*`
prove straight from the root structure. `logSumB`'s come *via conjugacy*
(`im_div_eq_neg_im_mul_conj`), and the pair is only conjugate where
`pairDisc φ < 0` — past the discriminant flip they are two distinct reals, each
its own conjugate but not each other's. So `hA` survives the collision and `hB`
does not. -/
theorem logSumA_concrete {φ : ℝ} (hsin : 0 < Real.sin φ)
    (hφ0 : 0 ≤ φ) (hφπ : φ < π) :
    Complex.log (1 - arcX φ * Yreal φ) + Complex.log (1 - arcX φ * (Ypair φ).1)
      + Complex.log (1 - arcX φ * (Ypair φ).2) = Complex.log (arcX φ) := by
  have hxim : 0 < (arcX φ).im := by rw [arcX_im]; exact hsin
  have hxre : (arcX φ).re = Real.cos φ := arcX_re φ
  have hsne : Real.sin φ ≠ 0 := ne_of_gt hsin
  exact logSumA_eq_log (arcX_ne_zero φ)
    (one_sub_ne_zero_of_mem_notCut (vSide_Yreal hsne).hc₂)
    (one_sub_ne_zero_of_mem_notCut (vSide_Ypair_fst hsne).hc₂)
    (one_sub_ne_zero_of_mem_notCut (vSide_Ypair_snd hsne).hc₂)
    (vieta_hv1 (arcX_normSq φ) hxre) (vieta_hv2 (arcX_normSq φ) hxre) (vieta_e3 φ)
    hxim (arcX_normSq φ) (realRootPath_pos φ) (realRootPath_lt_one φ)
    (im_mul_Ypair_snd_neg hxre hxim (arcX_normSq φ)).le
    (fun hb => (im_mul_Ypair_fst_neg
      (Real.cos_neg_of_pi_div_two_lt_of_lt hb (by linarith [Real.pi_pos])) hxre hxim
      (arcX_normSq φ)).le)
    hφ0 hφπ (arcX_arg (by linarith [Real.pi_pos]) (le_of_lt hφπ))

/-- **`hB` at the concrete labelling.** -/
theorem logSumB_concrete {φ : ℝ} (hsin : 0 < Real.sin φ) (hd : pairDisc φ < 0)
    (hφ0 : 0 ≤ φ) (hφπ : φ < π) :
    Complex.log (1 - Yreal φ / arcX φ) + Complex.log (1 - (Ypair φ).1 / arcX φ)
      + Complex.log (1 - (Ypair φ).2 / arcX φ) = -Complex.log (arcX φ) := by
  have hxim : 0 < (arcX φ).im := by rw [arcX_im]; exact hsin
  have hxre : (arcX φ).re = Real.cos φ := arcX_re φ
  have hsne : Real.sin φ ≠ 0 := ne_of_gt hsin
  exact logSumB_eq_neg_log (arcX_ne_zero φ)
    (one_sub_ne_zero_of_mem_notCut (vSide_Yreal hsne).hc₃)
    (one_sub_ne_zero_of_mem_notCut (vSide_Ypair_fst hsne).hc₃)
    (one_sub_ne_zero_of_mem_notCut (vSide_Ypair_snd hsne).hc₃)
    (vieta_hv1 (arcX_normSq φ) hxre) (vieta_hv2 (arcX_normSq φ) hxre) (vieta_e3 φ)
    hxim (arcX_normSq φ) (realRootPath_pos φ) (realRootPath_lt_one φ)
    (im_div_Ypair_fst_pos hd hxre hxim (arcX_normSq φ))
    (fun hb => im_div_Ypair_snd_pos hd
      (Real.cos_neg_of_pi_div_two_lt_of_lt hb (by linarith [Real.pi_pos])) hxre hxim
      (arcX_normSq φ))
    hφ0 hφπ (arcX_arg (by linarith [Real.pi_pos]) (le_of_lt hφπ))

/-! ### 2. The `log(−y)` derivatives, one route each -/

/-- **`Y₁` takes route 2**, and needs no hypothesis at all.

`hasDerivAt_log_neg_ofReal` is stated for a path of the form
`fun u => ((t u : ℝ) : ℂ)`; `Yreal` is *definitionally* that, which is the whole
reason it was built as the complexification of a real function rather than as a
`ℂ`-valued function that happens to be real. `log_neg_route` says route 1 is
**impossible** here — `−Y₁` is a negative real, squarely on `log`'s cut. -/
theorem hasDerivAt_log_neg_Yreal (φ : ℝ) :
    HasDerivAt (fun u => Complex.log (-Yreal u))
      (((realRootPath' φ : ℝ) : ℂ) / ((realRootPath φ : ℝ) : ℂ)) φ :=
  hasDerivAt_log_neg_ofReal (hasDerivAt_realRootPath' φ) (realRootPath_pos φ)

/-- The pair is genuinely non-real off the collision — which is what puts `−Y₂`
and `−Y₃` in `slitPlane` and so selects route 1. -/
theorem pair_im_ne_zero {φ : ℝ} (h : pairDisc φ < 0) :
    ((Ypair φ).1).im ≠ 0 ∧ ((Ypair φ).2).im ≠ 0 := by
  have hneg : 0 < pairNegDisc φ := by rw [pairNegDisc_eq_neg]; linarith
  have hpos : 0 < pairIm φ := by
    unfold pairIm
    exact div_pos (Real.sqrt_pos.mpr hneg) (by norm_num)
  rw [Ypair_of_disc_neg h]
  constructor
  · simpa using hpos.ne'
  · simpa using hpos.ne'

theorem neg_Ypair_mem_slitPlane {φ : ℝ} (h : pairDisc φ < 0) :
    -(Ypair φ).1 ∈ Complex.slitPlane ∧ -(Ypair φ).2 ∈ Complex.slitPlane := by
  obtain ⟨h1, h2⟩ := pair_im_ne_zero h
  exact ⟨Or.inr (by simpa using h1), Or.inr (by simpa using h2)⟩

/-- **`Y₂` takes route 1.** -/
theorem hasDerivAt_log_neg_Ypair_fst {φ : ℝ} (hd : pairDisc φ < 0) (hs : Real.sin φ ≠ 0) :
    HasDerivAt (fun u => Complex.log (-(Ypair u).1))
      ((((-(realRootPath' φ + 2 * Real.sin φ) / 2 : ℝ) : ℂ)
        + ((pairNegDisc' φ / (2 * Real.sqrt (pairNegDisc φ)) / 2 : ℝ) : ℂ) * Complex.I)
        / (Ypair φ).1) φ :=
  hasDerivAt_log_neg_of_slitPlane (hasDerivAt_Ypair_fst hd)
    (vSide_Ypair_fst hs).hy0 (neg_Ypair_mem_slitPlane hd).1

/-- **`Y₃` takes route 1.** -/
theorem hasDerivAt_log_neg_Ypair_snd {φ : ℝ} (hd : pairDisc φ < 0) (hs : Real.sin φ ≠ 0) :
    HasDerivAt (fun u => Complex.log (-(Ypair u).2))
      ((((-(realRootPath' φ + 2 * Real.sin φ) / 2 : ℝ) : ℂ)
        - ((pairNegDisc' φ / (2 * Real.sqrt (pairNegDisc φ)) / 2 : ℝ) : ℂ) * Complex.I)
        / (Ypair φ).2) φ :=
  hasDerivAt_log_neg_of_slitPlane (hasDerivAt_Ypair_snd hd)
    (vSide_Ypair_snd hs).hy0 (neg_Ypair_mem_slitPlane hd).2


/-! ## `heⱼ` at the pair — the four regime bounds, instantiated

`FiveTwoPairSaddle` reduces `heⱼ` at the pair to `|argSum x y| < 2π` and proves
that bound in four regimes, for an abstract `(x, y)` with `Im y > 0`. This
section supplies the regime hypotheses from the concrete labelling.

The dispatch is on `Re y = cos φ − t/2` (`re_Ypair_eq`) and the sign of `cos φ`,
and it is *exhaustive by construction* rather than by inspection: `t > 0` makes
`Re y > 0` force `cos φ > 0`, which is what collapses what looks like four cases
into three.

⚠ `sin φ ≥ 0` is not enough for the divisor sign fact. `im_div_Ypair_fst_pos`
carries `0 < x.im`, i.e. **strictly** `sin φ > 0`, and `envelopeS_total` needs the
derivative on `Ico 0 π`, which contains `φ = 0`. The endpoint is handled
separately: `sin φ = 0` with `0 ≤ φ < π` forces `φ = 0`, where `x = 1` and the
fact is `Im y > 0` outright. Dropping the `Ico` hypothesis and working on the
open interval would have left a hole exactly at the point the transport starts
from. -/

theorem pairIm_pos {φ : ℝ} (h : pairDisc φ < 0) : 0 < pairIm φ := by
  have hd : 0 < pairNegDisc φ := by rw [pairNegDisc_eq_neg]; linarith
  exact div_pos (Real.sqrt_pos.2 hd) two_pos

theorem im_Ypair_fst_pos {φ : ℝ} (h : pairDisc φ < 0) : 0 < ((Ypair φ).1).im := by
  rw [Ypair_of_disc_neg h]
  simpa using pairIm_pos h

theorem normSq_arcX (φ : ℝ) : Complex.normSq (arcX φ) = 1 := by
  have h := arcX_normSq φ
  simp only [Complex.normSq_apply]
  nlinarith [h]

/-- `Im(x·y) = cos φ·Im y + sin φ·Re y` on the arc. -/
theorem im_arcX_mul (φ : ℝ) (y : ℂ) :
    (arcX φ * y).im = Real.cos φ * y.im + Real.sin φ * y.re := by
  rw [Complex.mul_im, arcX_re, arcX_im]

/-- `Im(y/x) = cos φ·Im y − sin φ·Re y` on the arc — the *other* combination, and
the reason the two branches are not related by flipping one sign. -/
theorem im_arcX_div (φ : ℝ) (y : ℂ) :
    (y / arcX φ).im = Real.cos φ * y.im - Real.sin φ * y.re := by
  rw [Complex.div_im, normSq_arcX, arcX_re, arcX_im]; ring

/-- **The identity regime 3 runs on**: `Re(x·y) + Re(y/x) = 2cos φ·Re y`. No sign
of an imaginary part appears in it, which is the point — regime 3 is where
neither `Im` argument is available. -/
theorem re_arcX_mul_add_div (φ : ℝ) (y : ℂ) :
    (arcX φ * y).re + (y / arcX φ).re = 2 * Real.cos φ * y.re := by
  rw [Complex.mul_re, Complex.div_re, normSq_arcX, arcX_re, arcX_im]; ring

/-- The divisor sign fact, extended to the closed left endpoint. -/
theorem im_div_Ypair_fst_pos' {φ : ℝ} (h : pairDisc φ < 0) (hlo : 0 ≤ φ)
    (hhi : φ < Real.pi) : 0 < ((Ypair φ).1 / arcX φ).im := by
  have hs : 0 ≤ Real.sin φ :=
    Real.sin_nonneg_of_nonneg_of_le_pi hlo hhi.le
  rcases eq_or_lt_of_le hs with hs0 | hs0
  · -- `sin φ = 0` on `[0, π)` forces `φ = 0`, where `x = 1`
    have hφ : φ = 0 :=
      (Real.sin_eq_zero_iff_of_lt_of_lt (by linarith [Real.pi_pos]) hhi).1 hs0.symm
    subst hφ
    rw [im_arcX_div]
    simpa using im_Ypair_fst_pos h
  · exact im_div_Ypair_fst_pos h (arcX_re φ) (by rw [arcX_im]; exact hs0) (arcX_normSq φ)

/-- **`|argSum| < 2π` at the pair's first branch**, by the three-way dispatch.

`Re y = cos φ − t/2` with `t > 0`, so `Re y > 0` *forces* `cos φ > 0` — that is
what makes the case split three-way rather than four-way, and it is also why
`im_mul_Ypair_fst_neg`'s `cos φ < 0` is not a gap: its failure region is exactly
regime 1, where the opposite sign is what supplies the bound. -/
theorem abs_argSum_Ypair_fst {φ : ℝ} (h : pairDisc φ < 0) (hlo : 0 ≤ φ)
    (hhi : φ < Real.pi) :
    |argSum (arcX φ) ((Ypair φ).1)| < 2 * Real.pi := by
  have hyim : 0 < ((Ypair φ).1).im := im_Ypair_fst_pos h
  have hy1 : ((Ypair φ).1).re < 1 := (re_Ypair_lt_one h).1
  have hdiv : 0 < ((Ypair φ).1 / arcX φ).im := im_div_Ypair_fst_pos' h hlo hhi
  have hre : ((Ypair φ).1).re = Real.cos φ - realRootPath φ / 2 := (re_Ypair_eq h).1
  have ht : 0 < realRootPath φ := realRootPath_pos φ
  have hs : 0 ≤ Real.sin φ := Real.sin_nonneg_of_nonneg_of_le_pi hlo hhi.le
  rcases lt_or_ge 0 ((Ypair φ).1).re with hp | hp
  · -- regime 1: `Re y > 0`, hence `cos φ > 0`, hence `Im(x·y) > 0`
    have hc : 0 < Real.cos φ := by rw [hre] at hp; linarith
    have hmul : 0 < (arcX φ * (Ypair φ).1).im := by
      rw [im_arcX_mul]
      have : 0 ≤ Real.sin φ * ((Ypair φ).1).re := mul_nonneg hs hp.le
      nlinarith
    exact abs_argSum_lt_of_re_pos hy1 hyim hp hmul hdiv
  · rcases le_or_gt (Real.cos φ) 0 with hc | hc
    · -- regime 2: both terms of `Im(x·y)` carry the opposite sign
      have hmul : (arcX φ * (Ypair φ).1).im ≤ 0 := by
        rw [im_arcX_mul]
        have h1 : Real.cos φ * ((Ypair φ).1).im ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hc hyim.le
        have h2 : Real.sin φ * ((Ypair φ).1).re ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hs hp
        linarith
      exact abs_argSum_lt_of_im_mul_nonpos hy1 hyim hp hmul hdiv
    · -- regime 3: no `Im` sign is available; the identity supplies the disjunction
      have hsum : (arcX φ * (Ypair φ).1).re + ((Ypair φ).1 / arcX φ).re ≤ 0 := by
        rw [re_arcX_mul_add_div]
        nlinarith
      have hor : (arcX φ * (Ypair φ).1).re ≤ 0 ∨ ((Ypair φ).1 / arcX φ).re ≤ 0 := by
        by_contra hcon
        push_neg at hcon
        linarith [hcon.1, hcon.2]
      exact abs_argSum_lt_of_re_mul_or_div_nonpos hy1 hyim hp hor hdiv

/-- `arcX 0 = 1`. Needed because the transport starts at `φ = 0`, where `VSide`
is unavailable (`vSide_of_root` carries `x.im ≠ 0`) and every `x`-dependent
quantity collapses. -/
theorem arcX_zero : arcX 0 = 1 := by simp [arcX]

/-- `sin φ = 0` on `[0, π)` pins `φ = 0` — the one place the `Ico` endpoint has
to be argued rather than inherited. -/
theorem eq_zero_of_sin_eq_zero {φ : ℝ} (hlo : 0 ≤ φ) (hhi : φ < Real.pi)
    (hs : Real.sin φ = 0) : φ = 0 :=
  (Real.sin_eq_zero_iff_of_lt_of_lt (by linarith [Real.pi_pos]) hhi).1 hs

/-- The three non-vanishing side conditions `dVdy_eq_zero_of_argSum_bound` needs,
on the **closed** left endpoint. Off `φ = 0` they come from `VSide`; at `φ = 0`
all three collapse to `1 − y ≠ 0`, because `arcX 0 = 1`. -/
theorem one_sub_ne_zero_Ypair_fst {φ : ℝ} (h : pairDisc φ < 0) (hlo : 0 ≤ φ)
    (hhi : φ < Real.pi) :
    (1 : ℂ) - (Ypair φ).1 ≠ 0 ∧ (1 : ℂ) - arcX φ * (Ypair φ).1 ≠ 0
      ∧ (1 : ℂ) - (Ypair φ).1 / arcX φ ≠ 0 := by
  have hy : (1 : ℂ) - (Ypair φ).1 ≠ 0 :=
    Complex.slitPlane_ne_zero (one_sub_Ypair_mem_slitPlane h).1
  rcases eq_or_lt_of_le (Real.sin_nonneg_of_nonneg_of_le_pi hlo hhi.le) with hs0 | hs0
  · have hφ : φ = 0 := eq_zero_of_sin_eq_zero hlo hhi hs0.symm
    subst hφ
    refine ⟨hy, ?_, ?_⟩ <;> simpa [arcX_zero] using hy
  · have hv := vSide_Ypair_fst (φ := φ) (ne_of_gt hs0)
    exact ⟨hy, one_sub_ne_zero_of_mem_notCut hv.hc₂,
      one_sub_ne_zero_of_mem_notCut hv.hc₃⟩

/-- **`∂V/∂y = 0` at the pair's first branch** — the last hypothesis
`hasDerivAt_envelopeS` was still taking on faith.

`exists_int_dVdy_mul` leaves an unpinned integer `k`; the four regime bounds pin
it to `0`, and with `k = 0` the derivative vanishes outright rather than merely
being annihilated by `Y′`. Stated on `Ico 0 π`, which is exactly what
`envelopeS_total` consumes — and no wider: at `φ = π` this is **false**
(`argSum = 2π`, Route 38 G15), for the same reason `VSide` fails there. -/
theorem dVdy_Ypair_fst_eq_zero {φ : ℝ} (h : pairDisc φ < 0) (hlo : 0 ≤ φ)
    (hhi : φ < Real.pi) : dVdy (arcX φ) ((Ypair φ).1) = 0 := by
  obtain ⟨h1, h2, h3⟩ := one_sub_ne_zero_Ypair_fst h hlo hhi
  refine dVdy_eq_zero_of_argSum_bound (arcX_ne_zero φ) ?_ h1 h2 h3
    ((curve_Ypair (arcX_normSq φ) (arcX_re φ)).1) (abs_argSum_Ypair_fst h hlo hhi)
  intro hz
  have := im_Ypair_fst_pos h
  rw [hz] at this
  simp at this

/-! ### The conjugate branch, for free

`Ypair.2 = conj Ypair.1` (`Ypair_conj`), and on `|x| = 1` conjugation **swaps**
`x·y` with `y/x` (`one_sub_mul_conj` / `one_sub_div_conj`), so `argSum` merely
changes sign. The second branch therefore needs no regime analysis of its own —
which is the point: mirroring the inequalities branch-by-branch does **not**
work, because `Im(x·y)` for one branch pairs with `Im(y/x)` for the *other*
(Route 38 G14). -/

/-- The three `notCut` memberships, on the **closed** left endpoint. Off `φ = 0`
they are `VSide`'s; at `φ = 0` all three collapse to `y ∈ notCut`, because
`arcX 0 = 1`. `VSide` itself is unavailable there (`vSide_of_root` carries
`x.im ≠ 0`), which is why this is not just `vSide_Ypair_fst`. -/
theorem notCut_Ypair_fst {φ : ℝ} (h : pairDisc φ < 0) (hlo : 0 ≤ φ)
    (hhi : φ < Real.pi) :
    (Ypair φ).1 ∈ notCut ∧ arcX φ * (Ypair φ).1 ∈ notCut
      ∧ (Ypair φ).1 / arcX φ ∈ notCut := by
  have hy : (Ypair φ).1 ∈ notCut := Or.inr (re_Ypair_lt_one h).1
  rcases eq_or_lt_of_le (Real.sin_nonneg_of_nonneg_of_le_pi hlo hhi.le) with hs0 | hs0
  · have hφ : φ = 0 := eq_zero_of_sin_eq_zero hlo hhi hs0.symm
    subst hφ
    refine ⟨hy, ?_, ?_⟩ <;> simpa [arcX_zero] using hy
  · have hv := vSide_Ypair_fst (φ := φ) (ne_of_gt hs0)
    exact ⟨hv.hc₁, hv.hc₂, hv.hc₃⟩

/-- `arg(−y) ≠ π` at the pair — `−y` has non-zero imaginary part, and
`arg_eq_pi_iff` needs it to vanish. One of `argSum_conj`'s four side conditions,
and the only one not coming from `notCut`. -/
theorem arg_neg_Ypair_fst_ne_pi {φ : ℝ} (h : pairDisc φ < 0) :
    (-(Ypair φ).1).arg ≠ Real.pi := by
  intro hpi
  have him := (Complex.arg_eq_pi_iff.1 hpi).2
  simp only [Complex.neg_im] at him
  exact absurd (neg_eq_zero.1 him) (ne_of_gt (im_Ypair_fst_pos h))

theorem abs_argSum_Ypair_snd {φ : ℝ} (h : pairDisc φ < 0) (hlo : 0 ≤ φ)
    (hhi : φ < Real.pi) :
    |argSum (arcX φ) ((Ypair φ).2)| < 2 * Real.pi := by
  obtain ⟨hc1, hc2, hc3⟩ := notCut_Ypair_fst h hlo hhi
  rw [← Ypair_conj h]
  exact abs_argSum_conj (arcX_normSq φ) (arg_one_sub_ne_pi hc1) (arg_one_sub_ne_pi hc2)
    (arg_one_sub_ne_pi hc3) (arg_neg_Ypair_fst_ne_pi h) (abs_argSum_Ypair_fst h hlo hhi)

theorem dVdy_Ypair_snd_eq_zero {φ : ℝ} (h : pairDisc φ < 0) (hlo : 0 ≤ φ)
    (hhi : φ < Real.pi) : dVdy (arcX φ) ((Ypair φ).2) = 0 := by
  obtain ⟨h1, h2, h3⟩ := one_sub_ne_zero_Ypair_fst h hlo hhi
  have hconj : ∀ w : ℂ, w ≠ 0 → (starRingEnd ℂ) w ≠ 0 := by
    intro w hw hz
    exact hw (by simpa using congrArg (starRingEnd ℂ) hz)
  have hy2 : ((Ypair φ).2).im < 0 := by
    rw [← Ypair_conj h]
    simpa using im_Ypair_fst_pos h
  refine dVdy_eq_zero_of_argSum_bound (arcX_ne_zero φ) ?_ ?_ ?_ ?_
    ((curve_Ypair (arcX_normSq φ) (arcX_re φ)).2) (abs_argSum_Ypair_snd h hlo hhi)
  · intro hz
    rw [hz] at hy2
    simp at hy2
  · exact one_sub_ne_zero_of_mem_notCut (Or.inr (re_Ypair_lt_one h).2)
  · rw [← Ypair_conj h, one_sub_mul_conj (arcX_normSq φ)]
    exact hconj _ h3
  · rw [← Ypair_conj h, one_sub_div_conj (arcX_normSq φ)]
    exact hconj _ h2

/-- **`heⱼ` at BOTH pair branches, for every `Y′`.**

`∂V/∂y` is zero there, so the envelope condition holds outright rather than by
`Y′` being annihilated — stronger than `hasDerivAt_envelopeS` asks for, and
strictly easier to use. Together with `re_dVdy_mul_eq_zero_of_real` at the real
branch, this discharges all three of `he₁ he₂ he₃`.

⚠ `Ico 0 π`, never `Icc`. At `φ = π` this is **FALSE** — `argSum = 2π` there
(Route 38 G15), for exactly the reason `VSide` fails: `x·y = 2.2469796` lands on
Li₂'s cut, so `arg(1−xy)` and `arg(1−y/x)` are both `π` instead of cancelling. -/
theorem he_Ypair {φ : ℝ} (h : pairDisc φ < 0) (hlo : 0 ≤ φ) (hhi : φ < Real.pi)
    (Y' : ℂ) :
    (dVdy (arcX φ) ((Ypair φ).1) * Y').re = 0
      ∧ (dVdy (arcX φ) ((Ypair φ).2) * Y').re = 0 := by
  constructor
  · rw [dVdy_Ypair_fst_eq_zero h hlo hhi, zero_mul, Complex.zero_re]
  · rw [dVdy_Ypair_snd_eq_zero h hlo hhi, zero_mul, Complex.zero_re]

/-! ## The real-pair regime, past the collision

`pairDisc φ > 0` is `Ioo φ₀ π`, where the pair is real. Everything the transport
needs there is the mirror of the complex case, and the two facts it turns on are
`pairGamma = 1/t > 0` (from `gamma_rel`) and `pairBeta > 0`.

⚠ `pairBeta > 0` is not "obvious from the picture". It is what says both real
roots are **negative** — and if it failed, both would be positive, contradicting
Route 36 G8's measurement that exactly one root per arc point is positive real.
It is proved here from `pairDisc > 0` alone, by an inequality rather than by
appealing to where `φ₀` sits. -/

theorem pairGamma_pos (φ : ℝ) : 0 < pairGamma φ := by
  have hγ : realRootPath φ * pairGamma φ = 1 := by
    have h := gamma_rel (unitCubic_realRootPath φ)
    unfold pairGamma
    linarith [h]
  have ht : 0 < realRootPath φ := realRootPath_pos φ
  nlinarith [hγ, ht]

/-- **`β > 0` past the collision**, hence both real roots negative.

If `β ≤ 0` then `2c ≥ t > 0`, so `β² = (2c−t)² ≤ (2−t)²` using `c ≤ 1`; and
`4γ = 4/t > 4 > (2−t)²` for `t ∈ (0,1)`. So `pairDisc = β² − 4γ < 0`, against the
hypothesis. No fact about where the discriminant crossing sits is used. -/
theorem pairBeta_pos {φ : ℝ} (h : 0 ≤ pairDisc φ) : 0 < pairBeta φ := by
  by_contra hb
  push_neg at hb
  have hγ : realRootPath φ * pairGamma φ = 1 := by
    have hg := gamma_rel (unitCubic_realRootPath φ)
    unfold pairGamma
    linarith [hg]
  have ht0 : 0 < realRootPath φ := realRootPath_pos φ
  have ht1 : realRootPath φ < 1 := realRootPath_lt_one φ
  have hc : Real.cos φ ≤ 1 := Real.cos_le_one φ
  have hbe : pairBeta φ = realRootPath φ - 2 * Real.cos φ := rfl
  have hd : pairDisc φ = pairBeta φ ^ 2 - 4 * pairGamma φ := rfl
  rw [hd] at h
  nlinarith [hγ, ht0, ht1, hc, hb, hbe, sq_nonneg (realRootPath φ - 1)]

theorem re_Ypair_neg_of_disc_pos {φ : ℝ} (h : 0 ≤ pairDisc φ) :
    ((Ypair φ).1).re < 0 ∧ ((Ypair φ).2).re < 0 ∧
      ((Ypair φ).1).im = 0 ∧ ((Ypair φ).2).im = 0 := by
  have hb : 0 < pairBeta φ := pairBeta_pos h
  have hγ : 0 < pairGamma φ := pairGamma_pos φ
  have hlt : Real.sqrt (pairDisc φ) < pairBeta φ := by
    have hle : pairDisc φ < pairBeta φ ^ 2 := by
      have : pairDisc φ = pairBeta φ ^ 2 - 4 * pairGamma φ := rfl
      linarith
    calc Real.sqrt (pairDisc φ) < Real.sqrt (pairBeta φ ^ 2) := by
          exact Real.sqrt_lt_sqrt h hle
      _ = pairBeta φ := by rw [Real.sqrt_sq hb.le]
  have hnn : 0 ≤ Real.sqrt (pairDisc φ) := Real.sqrt_nonneg _
  rw [Ypair_of_disc_pos h]
  refine ⟨?_, ?_, ?_, ?_⟩ <;> simp <;> linarith

/-- The two `Im(y/x)` sign facts on the real branch — proved directly, not
through the conjugacy `Ypair.2 = conj Ypair.1`, which is a complex-branch fact. -/
theorem im_div_Ypair_pos_of_disc_pos {φ : ℝ} (h : 0 < pairDisc φ)
    (hsin : 0 < Real.sin φ) :
    0 < ((Ypair φ).1 / arcX φ).im ∧ 0 < ((Ypair φ).2 / arcX φ).im := by
  obtain ⟨hp1, hp2, hi1, hi2⟩ := re_Ypair_neg_of_disc_pos h.le
  refine ⟨?_, ?_⟩
  · rw [im_arcX_div, hi1]
    nlinarith [mul_pos hsin (neg_pos.mpr hp1)]
  · rw [im_arcX_div, hi2]
    nlinarith [mul_pos hsin (neg_pos.mpr hp2)]

theorem im_mul_Ypair_neg_of_disc_pos {φ : ℝ} (h : 0 < pairDisc φ)
    (hsin : 0 < Real.sin φ) :
    (arcX φ * (Ypair φ).1).im < 0 ∧ (arcX φ * (Ypair φ).2).im < 0 := by
  obtain ⟨hp1, hp2, hi1, hi2⟩ := re_Ypair_neg_of_disc_pos h.le
  refine ⟨?_, ?_⟩
  · rw [im_arcX_mul, hi1]
    nlinarith [mul_pos hsin (neg_pos.mpr hp1)]
  · rw [im_arcX_mul, hi2]
    nlinarith [mul_pos hsin (neg_pos.mpr hp2)]

/-- **`heⱼ` on the real branch** — regime 4 of `FiveTwoPairSaddle`, where
`arg(1−y)` and `arg(−y)` are both `0` outright and the whole quantity collapses
to `arg(1−xy) + arg(1−y/x) ∈ (−π, π)`. -/
theorem he_Ypair_real {φ : ℝ} (h : 0 < pairDisc φ) (hsin : 0 < Real.sin φ)
    (Y' : ℂ) :
    (dVdy (arcX φ) ((Ypair φ).1) * Y').re = 0
      ∧ (dVdy (arcX φ) ((Ypair φ).2) * Y').re = 0 := by
  obtain ⟨hp1, hp2, hi1, hi2⟩ := re_Ypair_neg_of_disc_pos h.le
  obtain ⟨hd1, hd2⟩ := im_div_Ypair_pos_of_disc_pos h hsin
  obtain ⟨hm1, hm2⟩ := im_mul_Ypair_neg_of_disc_pos h hsin
  have hv := vSide_Ypair_fst (φ := φ) (ne_of_gt hsin)
  have hw := vSide_Ypair_snd (φ := φ) (ne_of_gt hsin)
  have hz1 : dVdy (arcX φ) ((Ypair φ).1) = 0 :=
    dVdy_eq_zero_of_argSum_bound (arcX_ne_zero φ) hv.hy0
      (one_sub_ne_zero_of_mem_notCut hv.hc₁) (one_sub_ne_zero_of_mem_notCut hv.hc₂)
      (one_sub_ne_zero_of_mem_notCut hv.hc₃)
      ((curve_Ypair (arcX_normSq φ) (arcX_re φ)).1)
      (abs_argSum_lt_of_real_neg hi1 hp1 hm1 hd1)
  have hz2 : dVdy (arcX φ) ((Ypair φ).2) = 0 :=
    dVdy_eq_zero_of_argSum_bound (arcX_ne_zero φ) hw.hy0
      (one_sub_ne_zero_of_mem_notCut hw.hc₁) (one_sub_ne_zero_of_mem_notCut hw.hc₂)
      (one_sub_ne_zero_of_mem_notCut hw.hc₃)
      ((curve_Ypair (arcX_normSq φ) (arcX_re φ)).2)
      (abs_argSum_lt_of_real_neg hi2 hp2 hm2 hd2)
  exact ⟨by rw [hz1, zero_mul, Complex.zero_re],
    by rw [hz2, zero_mul, Complex.zero_re]⟩

/-- `hB` on the real branch — identical to `logSumB_concrete` except that the two
`Im(y/x)` sign facts come from `re_Ypair_neg_of_disc_pos` rather than from the
conjugacy, which does not hold here. -/
theorem logSumB_concrete_real {φ : ℝ} (hsin : 0 < Real.sin φ) (hd : 0 < pairDisc φ)
    (hφ0 : 0 ≤ φ) (hφπ : φ < π) :
    Complex.log (1 - Yreal φ / arcX φ) + Complex.log (1 - (Ypair φ).1 / arcX φ)
      + Complex.log (1 - (Ypair φ).2 / arcX φ) = -Complex.log (arcX φ) := by
  have hxim : 0 < (arcX φ).im := by rw [arcX_im]; exact hsin
  have hxre : (arcX φ).re = Real.cos φ := arcX_re φ
  have hsne : Real.sin φ ≠ 0 := ne_of_gt hsin
  obtain ⟨hp1, hp2⟩ := im_div_Ypair_pos_of_disc_pos hd hsin
  exact logSumB_eq_neg_log (arcX_ne_zero φ)
    (one_sub_ne_zero_of_mem_notCut (vSide_Yreal hsne).hc₃)
    (one_sub_ne_zero_of_mem_notCut (vSide_Ypair_fst hsne).hc₃)
    (one_sub_ne_zero_of_mem_notCut (vSide_Ypair_snd hsne).hc₃)
    (vieta_hv1 (arcX_normSq φ) hxre) (vieta_hv2 (arcX_normSq φ) hxre) (vieta_e3 φ)
    hxim (arcX_normSq φ) (realRootPath_pos φ) (realRootPath_lt_one φ)
    hp1 (fun _ => hp2)
    hφ0 hφπ (arcX_arg (by linarith [Real.pi_pos]) (le_of_lt hφπ))

/-! ## The assembly — `hasDerivAt_envelopeS` at the concrete labelling

Every hypothesis of `hasDerivAt_envelopeS` is now a theorem about `Yreal` and
`Ypair`, so the transport's derivative follows with no hypothesis about the
labelling left for a caller to supply. -/

/-- `Yreal`'s derivative in the form the transport consumes — the same statement
as `hasDerivAt_Yreal`, with the value written as `realRootPath'` rather than
expanded, so it matches `hasDerivAt_log_neg_Yreal`'s numerator on the nose. -/
theorem hasDerivAt_Yreal' (φ : ℝ) :
    HasDerivAt Yreal (((realRootPath' φ : ℝ) : ℂ)) φ :=
  (hasDerivAt_realRootPath' φ).ofReal_comp

/-- **`heⱼ` at the real branch.** No `k`-pinning is needed here and that is not an
accident: `arg y ≡ 0` along a real branch, so the `2πi·k` leak is annihilated by
`Y′` being real whatever `k` is. It is the pair, where `arg y` moves, that forced
`k = 0`. -/
theorem he_Yreal {φ : ℝ} (hs : Real.sin φ ≠ 0) :
    (dVdy (arcX φ) (Yreal φ) * ((realRootPath' φ : ℝ) : ℂ)).re = 0 := by
  have hv := vSide_Yreal hs
  exact re_dVdy_mul_eq_zero_of_real (arcX_ne_zero φ) (ne_of_gt (realRootPath_pos φ))
    (one_sub_ne_zero_of_mem_notCut hv.hc₁) (one_sub_ne_zero_of_mem_notCut hv.hc₂)
    (one_sub_ne_zero_of_mem_notCut hv.hc₃) (curve_Yreal (arcX_normSq φ) (arcX_re φ))

/-- **`S′ = 2φ` at the concrete labelling.**

`hasDerivAt_envelopeS` took fourteen hypotheses about an arbitrary labelling;
all fourteen are now theorems about `Yreal` / `Ypair`, and this is what closes
Gap A's construction half.

⚠ **`Ioo 0 π`, and the two ends fail for different reasons.** At `φ = π` `VSide`
is FALSE (`x·y = 2.2469796` on Li₂'s cut, Route 36 G7) and so is `heⱼ`
(`argSum = 2π`, Route 38 G15) — that end is genuinely out of reach and
`envelopeS_total` is built not to need it. At `φ = 0` the *statement* is fine —
`arcX 0 = 1`, so `hA` and `hB` reduce to `∏(1−yⱼ) = 1` and the conjugate pair's
arguments cancel — but three inputs (`vSide_*`, `logSumA_concrete`,
`logSumB_concrete`) carry `sin φ ≠ 0` and do not reach it. That is a gap in the
*route*, not in the mathematics, and it is the one thing between this and
`envelopeS_total`. -/
theorem hasDerivAt_envelopeS_concrete {φ : ℝ} (hd : pairDisc φ < 0)
    (hlo : 0 < φ) (hhi : φ < π) :
    HasDerivAt (envelopeS Yreal (fun u => (Ypair u).1) (fun u => (Ypair u).2))
      (2 * φ) φ := by
  have hsin : 0 < Real.sin φ := Real.sin_pos_of_pos_of_lt_pi hlo hhi
  have hsn : Real.sin φ ≠ 0 := ne_of_gt hsin
  exact hasDerivAt_envelopeS (by linarith [Real.pi_pos]) hhi.le
    (hasDerivAt_Yreal' φ) (hasDerivAt_Ypair_fst hd) (hasDerivAt_Ypair_snd hd)
    (vSide_Yreal hsn) (vSide_Ypair_fst hsn) (vSide_Ypair_snd hsn)
    (hasDerivAt_log_neg_Yreal φ) (hasDerivAt_log_neg_Ypair_fst hd hsn)
    (hasDerivAt_log_neg_Ypair_snd hd hsn)
    (he_Yreal hsn) (he_Ypair hd hlo.le hhi _).1 (he_Ypair hd hlo.le hhi _).2
    (logSumA_concrete hsin hlo.le hhi) (logSumB_concrete hsin hd hlo.le hhi)

/-- On the real branch `−y` is a **positive real**, so it is in `slitPlane` by
`Re > 0` rather than by `Im ≠ 0` — the opposite disjunct from the complex case. -/
theorem neg_Ypair_mem_slitPlane_of_disc_pos {φ : ℝ} (h : 0 < pairDisc φ) :
    -(Ypair φ).1 ∈ Complex.slitPlane ∧ -(Ypair φ).2 ∈ Complex.slitPlane := by
  obtain ⟨hp1, hp2, _, _⟩ := re_Ypair_neg_of_disc_pos h.le
  exact ⟨Or.inl (by simpa using hp1), Or.inl (by simpa using hp2)⟩

theorem hasDerivAt_log_neg_Ypair_fst_real {φ : ℝ} (hd : 0 < pairDisc φ)
    (hs : Real.sin φ ≠ 0) :
    HasDerivAt (fun u => Complex.log (-(Ypair u).1))
      ((((-(realRootPath' φ + 2 * Real.sin φ)
          + -pairNegDisc' φ / (2 * Real.sqrt (pairDisc φ))) / 2 : ℝ) : ℂ)
        / (Ypair φ).1) φ :=
  hasDerivAt_log_neg_of_slitPlane (hasDerivAt_Ypair_fst_real hd)
    (vSide_Ypair_fst hs).hy0 (neg_Ypair_mem_slitPlane_of_disc_pos hd).1

theorem hasDerivAt_log_neg_Ypair_snd_real {φ : ℝ} (hd : 0 < pairDisc φ)
    (hs : Real.sin φ ≠ 0) :
    HasDerivAt (fun u => Complex.log (-(Ypair u).2))
      ((((-(realRootPath' φ + 2 * Real.sin φ)
          - -pairNegDisc' φ / (2 * Real.sqrt (pairDisc φ))) / 2 : ℝ) : ℂ)
        / (Ypair φ).2) φ :=
  hasDerivAt_log_neg_of_slitPlane (hasDerivAt_Ypair_snd_real hd)
    (vSide_Ypair_snd hs).hy0 (neg_Ypair_mem_slitPlane_of_disc_pos hd).2

/-- **`S′ = 2φ` on the real-pair regime `Ioo φ₀ π`.** The mirror of
`hasDerivAt_envelopeS_concrete`, with `pairDisc φ < 0` replaced by `0 < pairDisc φ`
throughout. Together the two cover `Ioo 0 π` minus the collision, which is
exactly what `envelopeS_total_of_ioo` consumes. -/
theorem hasDerivAt_envelopeS_concrete_real {φ : ℝ} (hd : 0 < pairDisc φ)
    (hlo : 0 < φ) (hhi : φ < π) :
    HasDerivAt (envelopeS Yreal (fun u => (Ypair u).1) (fun u => (Ypair u).2))
      (2 * φ) φ := by
  have hsin : 0 < Real.sin φ := Real.sin_pos_of_pos_of_lt_pi hlo hhi
  have hsn : Real.sin φ ≠ 0 := ne_of_gt hsin
  exact hasDerivAt_envelopeS (by linarith [Real.pi_pos]) hhi.le
    (hasDerivAt_Yreal' φ) (hasDerivAt_Ypair_fst_real hd) (hasDerivAt_Ypair_snd_real hd)
    (vSide_Yreal hsn) (vSide_Ypair_fst hsn) (vSide_Ypair_snd hsn)
    (hasDerivAt_log_neg_Yreal φ) (hasDerivAt_log_neg_Ypair_fst_real hd hsn)
    (hasDerivAt_log_neg_Ypair_snd_real hd hsn)
    (he_Yreal hsn) (he_Ypair_real hd hsin _).1 (he_Ypair_real hd hsin _).2
    (logSumA_concrete hsin hlo.le hhi) (logSumB_concrete_real hsin hd hlo.le hhi)

/-- **`S′ = 2φ` on all of `Ioo 0 π` except the collision.**

The two regimes joined. `pairDisc φ ≠ 0` is exactly "not at the collision", and
it is the *only* hypothesis left besides being in the open interval — the
labelling, the branch routing, the envelope condition and both log sums are all
discharged. -/
theorem hasDerivAt_envelopeS_concrete_of_ne {φ : ℝ} (hd : pairDisc φ ≠ 0)
    (hlo : 0 < φ) (hhi : φ < π) :
    HasDerivAt (envelopeS Yreal (fun u => (Ypair u).1) (fun u => (Ypair u).2))
      (2 * φ) φ := by
  rcases hd.lt_or_gt with h | h
  · exact hasDerivAt_envelopeS_concrete h hlo hhi
  · exact hasDerivAt_envelopeS_concrete_real h hlo hhi

/-! ## `Ioo`, not `Ico` — the `φ = 0` endpoint dissolves

`envelopeS_total` asks for the derivative on `Ico 0 π`, i.e. **including** the
left endpoint. That is stronger than the mathematics needs, and it was the one
thing standing between `hasDerivAt_envelopeS_concrete` and the transport: three
of its inputs (`vSide_*`, `logSumA_concrete`, `logSumB_concrete`) carry
`sin φ ≠ 0`, which fails at `φ = 0`.

Mathlib's `intervalIntegral.integral_eq_sub_of_hasDerivAt_of_le` wants the
derivative only on the **open** interval, with continuity on the closed one — so
splitting at the exceptional point handles `φ₀` and the two endpoints in one
stroke, and no endpoint derivative is needed at all.

⚠ Worth stating plainly: this is not a workaround for a hard step, it is a
hypothesis that was too strong to begin with. The `Ico` form was written when
the exceptional point was the only endpoint anyone was thinking about. -/

theorem total_of_deriv_on_ioo {f : ℝ → ℝ} {b c : ℝ} (hc0 : 0 < c) (hcb : c < b)
    (hcont : ContinuousOn f (Set.Icc 0 b))
    (hderiv : ∀ φ ∈ Set.Ioo (0 : ℝ) b, φ ≠ c → HasDerivAt f (2 * φ) φ) :
    f b = f 0 + b ^ 2 := by
  have hint : ∀ u v : ℝ, IntervalIntegrable (fun φ : ℝ => 2 * φ) MeasureTheory.volume u v :=
    fun u v => (continuous_const.mul continuous_id).intervalIntegrable u v
  have hval : ∀ u v : ℝ, (∫ φ in u..v, 2 * φ) = v ^ 2 - u ^ 2 := by
    intro u v
    rw [intervalIntegral.integral_const_mul, integral_id]
    ring
  -- left piece `[0, c]`
  have hleft := intervalIntegral.integral_eq_sub_of_hasDerivAt_of_le hc0.le
    (hcont.mono (Set.Icc_subset_Icc le_rfl hcb.le))
    (fun φ hφ => hderiv φ ⟨hφ.1, lt_trans hφ.2 hcb⟩ (ne_of_lt hφ.2)) (hint 0 c)
  -- right piece `[c, b]`
  have hright := intervalIntegral.integral_eq_sub_of_hasDerivAt_of_le hcb.le
    (hcont.mono (Set.Icc_subset_Icc hc0.le le_rfl))
    (fun φ hφ => hderiv φ ⟨lt_trans hc0 hφ.1, hφ.2⟩ (ne_of_gt hφ.1)) (hint c b)
  rw [hval] at hleft hright
  linarith

/-- **The transport, with the endpoint hypothesis removed.** Same conclusion as
`envelopeS_total`, with `Ico` weakened to `Ioo`. -/
theorem envelopeS_total_of_ioo {Y₁ Y₂ Y₃ : ℝ → ℂ} {c : ℝ} (hc0 : 0 < c) (hcπ : c < π)
    (hcont : ContinuousOn (envelopeS Y₁ Y₂ Y₃) (Set.Icc 0 π))
    (hderiv : ∀ φ ∈ Set.Ioo (0 : ℝ) π, φ ≠ c →
      HasDerivAt (envelopeS Y₁ Y₂ Y₃) (2 * φ) φ) :
    envelopeS Y₁ Y₂ Y₃ π = envelopeS Y₁ Y₂ Y₃ 0 + π ^ 2 :=
  total_of_deriv_on_ioo hc0 hcπ hcont hderiv

/-- **The transport, reduced to continuity alone.**

Given a collision point `c` and continuity of `S` on the closed interval, the
whole of `S(π) − S(0) = π²` follows. Every other hypothesis
`hasDerivAt_envelopeS` and `envelopeS_total` between them asked for is now a
theorem about the concrete labelling.

⚠ What is *not* here: `hcont`. Its hard point is `φ = π`, where two of the `Li₂`
arguments land on the cut — the `Li₂` half of that is proved
(`continuousAt_re_cLiTwoExt`, 2-D), but composing it along the arc is not
written. -/
theorem envelopeS_total_concrete {c : ℝ} (hc0 : 0 < c) (hcπ : c < π)
    (hcoll : ∀ φ ∈ Set.Ioo (0 : ℝ) π, φ ≠ c → pairDisc φ ≠ 0)
    (hcont : ContinuousOn (envelopeS Yreal (fun u => (Ypair u).1) (fun u => (Ypair u).2))
      (Set.Icc 0 π)) :
    envelopeS Yreal (fun u => (Ypair u).1) (fun u => (Ypair u).2) π
      = envelopeS Yreal (fun u => (Ypair u).1) (fun u => (Ypair u).2) 0 + π ^ 2 :=
  envelopeS_total_of_ioo hc0 hcπ hcont
    (fun φ hφ hne => hasDerivAt_envelopeS_concrete_of_ne (hcoll φ hφ hne) hφ.1 hφ.2)

/-! ## `hcont`: the composition lemmas

`envelopeS` is `Re` of three copies of `deformedV`, and `deformedV` is three
`cLiTwoExt`s and one `log(−y)²`. Each of those is continuous along a continuous
path under one condition, and the conditions are exactly the two cases the cut
admits: **off** it, or **strictly inside** it.

That second case is what `continuousAt_re_cLiTwoExt` buys. Without it there would
be no `Icc 0 π` statement at all — at `φ = π` two of the nine `Li₂` arguments
land on `[1,∞)`. -/

/-- `Re ∘ cLiTwoExt ∘ g` is continuous at `φ` when `g φ` is off the cut, or is a
real number **strictly** greater than 1. The branch point `1` itself is in
neither case, and is not covered — deliberately, since `cLiTwoExt` is genuinely
singular in its derivative there. -/
theorem continuousAt_re_cLiTwoExt_comp {g : ℝ → ℂ} {φ : ℝ} (hg : ContinuousAt g φ)
    (h : g φ ∈ notCut ∨ ∃ r : ℝ, 1 < r ∧ g φ = (r : ℂ)) :
    ContinuousAt (fun u => (cLiTwoExt (g u)).re) φ := by
  rcases h with h | ⟨r, hr, hgr⟩
  · exact (Complex.continuous_re.continuousAt.comp
      (((analyticOnNhd_cLiTwoExt _ h).continuousAt).comp hg))
  · have hc : ContinuousAt (fun w : ℂ => (cLiTwoExt w).re) (g φ) := by
      rw [hgr]; exact continuousAt_re_cLiTwoExt hr
    exact hc.comp hg

/-- `Re ∘ (log(−·)²) ∘ g`, likewise. `−g φ ∈ slitPlane` is the ordinary case;
`0 < Re (g φ)` is the one where `−g φ` sits **on** log's cut and only the real
part of the square survives (`re_log_neg_sq`). The real branch `Yreal > 0` is
always in the second case, and never in the first. -/
theorem continuousAt_re_log_neg_sq_comp {q : ℝ → ℂ} {φ : ℝ} (hq : ContinuousAt q φ)
    (h : -q φ ∈ Complex.slitPlane ∨ 0 < (q φ).re) :
    ContinuousAt (fun u => (Complex.log (-q u) ^ 2).re) φ := by
  rcases h with h | h
  · -- pin `f`: bare `.comp` lets unification pick `Neg.neg` as the inner map
    have hlog : ContinuousAt (fun u : ℝ => Complex.log (-q u)) φ :=
      ContinuousAt.comp (f := fun u : ℝ => -q u) (continuousAt_clog h) hq.neg
    exact Complex.continuous_re.continuousAt.comp (hlog.pow 2)
  · exact (continuousAt_re_log_neg_sq h).comp hq

/-- **`Re deformedV` along a path**, under the four conditions its four terms
need. Stated for arbitrary `X Y` so it can be applied at each of the three
branches without repetition. -/
theorem continuousAt_re_deformedV_comp {X Y : ℝ → ℂ} {φ : ℝ}
    (hX : ContinuousAt X φ) (hY : ContinuousAt Y φ) (hX0 : X φ ≠ 0)
    (h1 : Y φ ∈ notCut ∨ ∃ r : ℝ, 1 < r ∧ Y φ = (r : ℂ))
    (h2 : X φ * Y φ ∈ notCut ∨ ∃ r : ℝ, 1 < r ∧ X φ * Y φ = (r : ℂ))
    (h3 : Y φ / X φ ∈ notCut ∨ ∃ r : ℝ, 1 < r ∧ Y φ / X φ = (r : ℂ))
    (h4 : -Y φ ∈ Complex.slitPlane ∨ 0 < (Y φ).re) :
    ContinuousAt (fun u => (deformedV (X u, Y u)).re) φ := by
  have hmul : ContinuousAt (fun u => X u * Y u) φ := hX.mul hY
  have hdiv : ContinuousAt (fun u => Y u / X u) φ := hY.div hX hX0
  have e1 := continuousAt_re_cLiTwoExt_comp hY h1
  have e2 := continuousAt_re_cLiTwoExt_comp hmul h2
  have e3 := continuousAt_re_cLiTwoExt_comp hdiv h3
  have e4 := continuousAt_re_log_neg_sq_comp hY h4
  have hsum := ((e1.add e2).add e3).add e4
  refine hsum.congr ?_
  filter_upwards with u
  simp [deformedV, Complex.add_re]

/-! ### The endpoint `φ = π`, from the cubic alone

Everything needed at `φ = π` follows from `t³ + 2t² − t − 1 = 0` and `0 < t < 1`
by pure algebra — **no numeric bound on `t = 2cos(π/7) − 1 = 0.8019…` is used**,
which matters: that value is measured, and a proof leaning on the decimal would
be leaning on a measurement. -/

theorem realRootPath_pi_cubic : realRootPath π ^ 3 + 2 * realRootPath π ^ 2
    - realRootPath π - 1 = 0 := by
  have h := unitCubic_realRootPath π
  unfold unitCubic at h
  rw [Real.cos_pi] at h
  linarith [h]

/-- `t² + t − 1 > 0` at `φ = π`, i.e. `t > (√5−1)/2`. If `t² ≤ 1 − t` then
`t³ ≤ t − t²`, while the cubic gives `t³ = 1 + t − 2t²`; together they force
`t² ≥ 1`, against `t < 1`. -/
theorem realRootPath_pi_gt : 0 < realRootPath π ^ 2 + realRootPath π - 1 := by
  have hc := realRootPath_pi_cubic
  have ht0 : 0 < realRootPath π := realRootPath_pos π
  have ht1 : realRootPath π < 1 := realRootPath_lt_one π
  nlinarith [hc, ht0, ht1]

theorem pairBeta_pi : pairBeta π = realRootPath π + 2 := by
  unfold pairBeta
  rw [Real.cos_pi]
  ring

theorem pairGamma_pi_rel : realRootPath π * pairGamma π = 1 := by
  have hg := gamma_rel (unitCubic_realRootPath π)
  unfold pairGamma
  linarith [hg]

/-- `pairDisc π > 0`: the pair is REAL at the endpoint. `t·(t+2)² − 4 = 2t² + 5t − 3`
after substituting the cubic, and that is positive for `t > 1/2`, which
`realRootPath_pi_gt` supplies. -/
theorem pairDisc_pi_pos : 0 < pairDisc π := by
  have hc := realRootPath_pi_cubic
  have ht0 : 0 < realRootPath π := realRootPath_pos π
  have hgt := realRootPath_pi_gt
  have hγ := pairGamma_pi_rel
  have hd : pairDisc π = pairBeta π ^ 2 - 4 * pairGamma π := rfl
  rw [hd, pairBeta_pi]
  nlinarith [hc, ht0, hgt, hγ]

/-- The endpoint values, bracketed. `Ypair.2 π < −1` is `β > 2`, i.e. `t > 0`.
`Ypair.1 π > −1` is the one that needs the cubic: it is `√d > t`, i.e.
`t² + t − 1 > 0`. -/
theorem Ypair_pi_bracket :
    ((Ypair π).1).re > -1 ∧ ((Ypair π).2).re < -1 ∧
      ((Ypair π).1).im = 0 ∧ ((Ypair π).2).im = 0 := by
  have hd := pairDisc_pi_pos
  have ht0 : 0 < realRootPath π := realRootPath_pos π
  have hgt := realRootPath_pi_gt
  have hγ := pairGamma_pi_rel
  have hcub := realRootPath_pi_cubic
  have hb : pairBeta π = realRootPath π + 2 := pairBeta_pi
  have hsq : Real.sqrt (pairDisc π) ^ 2 = pairDisc π := Real.sq_sqrt hd.le
  have hnn : 0 ≤ Real.sqrt (pairDisc π) := Real.sqrt_nonneg _
  have hdd : pairDisc π = pairBeta π ^ 2 - 4 * pairGamma π := rfl
  -- `√d > t` ⟺ `d > t²` ⟺ `t² + t − 1 > 0`
  have hlow : realRootPath π < Real.sqrt (pairDisc π) := by
    nlinarith [hsq, hnn, hdd, hb, hγ, ht0, hgt]
  rw [Ypair_of_disc_pos hd.le]
  refine ⟨?_, ?_, ?_, ?_⟩ <;> simp <;> nlinarith [hb, ht0, hnn, hlow]

/-! ### `hcont`, assembled -/

theorem arcX_pi : arcX π = -1 := by
  simp [arcX]

/-- The `snd` analogue of `notCut_Ypair_fst`, and the same for the real branch —
both on the **closed** left endpoint, where `VSide` is unavailable. -/
theorem notCut_Ypair_snd {φ : ℝ} (h : pairDisc φ < 0) (hlo : 0 ≤ φ)
    (hhi : φ < π) :
    (Ypair φ).2 ∈ notCut ∧ arcX φ * (Ypair φ).2 ∈ notCut
      ∧ (Ypair φ).2 / arcX φ ∈ notCut := by
  have hy : (Ypair φ).2 ∈ notCut := Or.inr (re_Ypair_lt_one h).2
  rcases eq_or_lt_of_le (Real.sin_nonneg_of_nonneg_of_le_pi hlo hhi.le) with hs0 | hs0
  · have hφ : φ = 0 := eq_zero_of_sin_eq_zero hlo hhi hs0.symm
    subst hφ
    refine ⟨hy, ?_, ?_⟩ <;> simpa [arcX_zero] using hy
  · have hv := vSide_Ypair_snd (φ := φ) (ne_of_gt hs0)
    exact ⟨hv.hc₁, hv.hc₂, hv.hc₃⟩

theorem notCut_Yreal {φ : ℝ} (hlo : 0 ≤ φ) (hhi : φ < π) :
    Yreal φ ∈ notCut ∧ arcX φ * Yreal φ ∈ notCut ∧ Yreal φ / arcX φ ∈ notCut := by
  have hy : Yreal φ ∈ notCut := Or.inr (by
    simpa [Yreal] using realRootPath_lt_one φ)
  rcases eq_or_lt_of_le (Real.sin_nonneg_of_nonneg_of_le_pi hlo hhi.le) with hs0 | hs0
  · have hφ : φ = 0 := eq_zero_of_sin_eq_zero hlo hhi hs0.symm
    subst hφ
    refine ⟨hy, ?_, ?_⟩ <;> simpa [arcX_zero] using hy
  · have hv := vSide_Yreal (φ := φ) (ne_of_gt hs0)
    exact ⟨hv.hc₁, hv.hc₂, hv.hc₃⟩

/-- `−Ypair ∈ slitPlane` on the whole arc: by `Im ≠ 0` before the collision, by
`Re < 0` at and after it. The two disjuncts, and neither covers both regimes. -/
theorem neg_Ypair_mem_slitPlane_all (φ : ℝ) :
    -(Ypair φ).1 ∈ Complex.slitPlane ∧ -(Ypair φ).2 ∈ Complex.slitPlane := by
  rcases lt_or_ge (pairDisc φ) 0 with h | h
  · exact neg_Ypair_mem_slitPlane h
  · obtain ⟨h1, h2, _, _⟩ := re_Ypair_neg_of_disc_pos h
    exact ⟨Or.inl (by simpa using h1), Or.inl (by simpa using h2)⟩

/-- At `φ = 0` the pair is complex: `β = t − 2 < 0`, and `pairBeta_pos` says that
forces `pairDisc < 0`. Needed because the real-branch statements would otherwise
have to be argued at a point where they are false. -/
theorem pairDisc_zero_neg : pairDisc 0 < 0 := by
  by_contra hcon
  push_neg at hcon
  have hb := pairBeta_pos hcon
  have : pairBeta 0 = realRootPath 0 - 2 := by unfold pairBeta; rw [Real.cos_zero]; ring
  linarith [realRootPath_lt_one 0, this, hb]

theorem continuousAt_Yreal (φ : ℝ) : ContinuousAt Yreal φ :=
  (hasDerivAt_Yreal' φ).continuousAt

theorem continuousAt_arcX (φ : ℝ) : ContinuousAt arcX φ := (hasDerivAt_arcX φ).continuousAt

/-- **`hcont`.** `envelopeS` is continuous at every point of `Icc 0 π`, endpoint
included — which is where `continuousAt_re_cLiTwoExt` earns its place: at `φ = π`
the arguments `x·Ypair.2` and `Ypair.2/x` are both `−Ypair.2 π > 1`, sitting
**on** Li₂'s cut, and no continuity statement about `cLiTwoExt` itself is true
there. -/
theorem continuousAt_envelopeS_concrete {φ : ℝ} (hlo : 0 ≤ φ) (hhi : φ ≤ π) :
    ContinuousAt (envelopeS Yreal (fun u => (Ypair u).1) (fun u => (Ypair u).2)) φ := by
  have hX := continuousAt_arcX φ
  have hX0 := arcX_ne_zero φ
  have hslit := neg_Ypair_mem_slitPlane_all φ
  have hYr := continuousAt_Yreal φ
  have hY1 : ContinuousAt (fun u => (Ypair u).1) φ := continuous_Ypair.fst.continuousAt
  have hY2 : ContinuousAt (fun u => (Ypair u).2) φ := continuous_Ypair.snd.continuousAt
  have hrpos : 0 < (Yreal φ).re := by simpa [Yreal] using realRootPath_pos φ
  -- `sin φ > 0` whenever the pair is NOT complex: `pairDisc 0 < 0` rules out `φ = 0`
  have hsin_of : 0 ≤ pairDisc φ → φ < π → 0 < Real.sin φ := by
    intro hd hπ
    rcases eq_or_lt_of_le hlo with h0 | h0
    · rw [← h0] at hd; linarith [pairDisc_zero_neg]
    · exact Real.sin_pos_of_pos_of_lt_pi h0 hπ
  rcases eq_or_lt_of_le hhi with hπ | hπ
  · -- the endpoint: `arcX π = −1`, so `x·y` and `y/x` are both `−y`
    subst hπ
    obtain ⟨hb1, hb2, hi1, hi2⟩ := Ypair_pi_bracket
    have hcut : ∀ y : ℂ, y.im = 0 → -1 < y.re → y.re < 1 →
        (y ∈ notCut ∧ arcX π * y ∈ notCut ∧ y / arcX π ∈ notCut) := by
      intro y hyi h1 h2
      rw [arcX_pi]
      refine ⟨Or.inr h2, Or.inr ?_, Or.inr ?_⟩
      · simp [Complex.neg_re]; linarith
      · simp [Complex.div_re, Complex.normSq_apply, hyi]; linarith
    have hn1 : ((Ypair π).1).re < 0 := (re_Ypair_neg_of_disc_pos pairDisc_pi_pos.le).1
    refine ContinuousAt.add (ContinuousAt.add ?_ ?_) ?_
    · obtain ⟨n1, n2, n3⟩ := hcut (Yreal π) (by simp [Yreal])
        (by simpa [Yreal] using lt_trans (by norm_num) (realRootPath_pos π))
        (by simpa [Yreal] using realRootPath_lt_one π)
      exact continuousAt_re_deformedV_comp hX hYr hX0 (Or.inl n1) (Or.inl n2)
        (Or.inl n3) (Or.inr hrpos)
    · obtain ⟨n1, n2, n3⟩ := hcut _ hi1 hb1 (by linarith)
      exact continuousAt_re_deformedV_comp hX hY1 hX0 (Or.inl n1) (Or.inl n2)
        (Or.inl n3) (Or.inl hslit.1)
    · have hpos : (1 : ℝ) < -((Ypair π).2).re := by linarith
      have hval : arcX π * (Ypair π).2 = ((-((Ypair π).2).re : ℝ) : ℂ) := by
        rw [arcX_pi]; apply Complex.ext <;> simp [hi2]
      have hval' : (Ypair π).2 / arcX π = ((-((Ypair π).2).re : ℝ) : ℂ) := by
        rw [arcX_pi]; apply Complex.ext <;>
          simp [Complex.div_re, Complex.div_im, Complex.normSq_apply, hi2]
      exact continuousAt_re_deformedV_comp hX hY2 hX0
        (Or.inl (Or.inr (by linarith))) (Or.inr ⟨_, hpos, hval⟩)
        (Or.inr ⟨_, hpos, hval'⟩) (Or.inl hslit.2)
  · refine ContinuousAt.add (ContinuousAt.add ?_ ?_) ?_
    · obtain ⟨n1, n2, n3⟩ := notCut_Yreal hlo hπ
      exact continuousAt_re_deformedV_comp hX hYr hX0 (Or.inl n1) (Or.inl n2)
        (Or.inl n3) (Or.inr hrpos)
    · rcases lt_or_ge (pairDisc φ) 0 with hd | hd
      · obtain ⟨n1, n2, n3⟩ := notCut_Ypair_fst hd hlo hπ
        exact continuousAt_re_deformedV_comp hX hY1 hX0 (Or.inl n1) (Or.inl n2)
          (Or.inl n3) (Or.inl hslit.1)
      · have hv := vSide_Ypair_fst (ne_of_gt (hsin_of hd hπ))
        exact continuousAt_re_deformedV_comp hX hY1 hX0 (Or.inl hv.hc₁)
          (Or.inl hv.hc₂) (Or.inl hv.hc₃) (Or.inl hslit.1)
    · rcases lt_or_ge (pairDisc φ) 0 with hd | hd
      · obtain ⟨n1, n2, n3⟩ := notCut_Ypair_snd hd hlo hπ
        exact continuousAt_re_deformedV_comp hX hY2 hX0 (Or.inl n1) (Or.inl n2)
          (Or.inl n3) (Or.inl hslit.2)
      · have hv := vSide_Ypair_snd (ne_of_gt (hsin_of hd hπ))
        exact continuousAt_re_deformedV_comp hX hY2 hX0 (Or.inl hv.hc₁)
          (Or.inl hv.hc₂) (Or.inl hv.hc₃) (Or.inl hslit.2)

/-- **`hcont`** — the last hypothesis of `envelopeS_total_concrete`. -/
theorem continuousOn_envelopeS_concrete :
    ContinuousOn (envelopeS Yreal (fun u => (Ypair u).1) (fun u => (Ypair u).2))
      (Set.Icc 0 π) := fun _ hφ =>
  (continuousAt_envelopeS_concrete hφ.1 hφ.2).continuousWithinAt

/-! ## `hcoll` — the collision is the only zero of `pairDisc`

Route 32 located the crossing by scanning `φ`. That is a claim about how many
zeros something has, backed by samples, and this lane has retracted two of those.
The algebra replaces it: `pairDisc` depends on `φ` **only** through
`t = realRootPath φ`, and

    pairDisc φ · t² · (t−1)²  =  E t,     E t = t⁴ − 2t³ + 7t² − 6t + 1

so `hcoll` is a statement about a **quartic**. Two facts finish it, and both are
already in the tree or one factorisation away:

* `E′ t = 2(2t−1)(t² − t + 3)` with the quadratic factor positive (discriminant
  `−11`), so `E` is strictly increasing above `t = 1/2` — one minimum, no
  root-locating;
* `pairDisc ≥ 0` forces `t² + t − 1 ≥ 0` (`W_nonneg_of_disc_nonneg`, **already
  proved**, for a different purpose), i.e. `t ≥ (√5−1)/2 > 1/2`.

⚠ `E` has a **second** root in `(0,1)`, at `t = 0.2192` (Route 39 G4). It is out
of range — `two_fifths_lt` gives `t > 2/5` — but an argument that forgot it would
be proving something false. -/

/-- `E t = t⁴ − 2t³ + 7t² − 6t + 1`, the quartic `pairDisc` reduces to. -/
noncomputable def collQuartic (t : ℝ) : ℝ := t ^ 4 - 2 * t ^ 3 + 7 * t ^ 2 - 6 * t + 1

/-- **The reduction.** A consequence of `unitCubic c t = 0` alone — Route 39 G1
checks it at five values of `c` *outside* `[−1,1]`, so nothing about the arc is
smuggled in. -/
theorem pairDisc_mul_eq_collQuartic (φ : ℝ) :
    pairDisc φ * realRootPath φ ^ 2 * (realRootPath φ - 1) ^ 2
      = collQuartic (realRootPath φ) := by
  have hp := unitCubic_realRootPath φ
  unfold unitCubic at hp
  have hd : pairDisc φ = pairBeta φ ^ 2 - 4 * pairGamma φ := rfl
  unfold pairBeta pairGamma at hd
  rw [hd, collQuartic]
  -- quotient of `LHS − RHS` by the cubic, computed rather than guessed
  linear_combination (-2 * Real.cos φ * realRootPath φ ^ 2
    + 2 * Real.cos φ * realRootPath φ - 3 * realRootPath φ ^ 3
    + 6 * realRootPath φ ^ 2 - 5 * realRootPath φ + 1) * hp

theorem hasDerivAt_collQuartic (t : ℝ) :
    HasDerivAt collQuartic (2 * (2 * t - 1) * (t ^ 2 - t + 3)) t := by
  have h1 : HasDerivAt (fun x : ℝ => x ^ 4) ((4 : ℕ) * t ^ 3) t := hasDerivAt_pow 4 t
  have h2 : HasDerivAt (fun x : ℝ => 2 * x ^ 3) (2 * ((3 : ℕ) * t ^ 2)) t :=
    (hasDerivAt_pow 3 t).const_mul 2
  have h3 : HasDerivAt (fun x : ℝ => 7 * x ^ 2) (7 * ((2 : ℕ) * t ^ 1)) t :=
    (hasDerivAt_pow 2 t).const_mul 7
  have h4 : HasDerivAt (fun x : ℝ => 6 * x) (6 * 1) t := (hasDerivAt_id t).const_mul 6
  have h := (((h1.sub h2).add h3).sub h4).add_const 1
  have heq : collQuartic = fun x : ℝ => x ^ 4 - 2 * x ^ 3 + 7 * x ^ 2 - 6 * x + 1 := rfl
  rw [heq]
  convert h using 1
  push_cast
  ring

/-- `E` is strictly increasing above `1/2`. The quadratic factor `t² − t + 3` has
discriminant `−11`, so it never vanishes and never changes the sign. -/
theorem strictMonoOn_collQuartic : StrictMonoOn collQuartic (Set.Ici (1 / 2 : ℝ)) := by
  refine strictMonoOn_of_deriv_pos (convex_Ici _)
    (fun t _ => (hasDerivAt_collQuartic t).continuousAt.continuousWithinAt) ?_
  intro t ht
  rw [interior_Ici] at ht
  rw [(hasDerivAt_collQuartic t).deriv]
  have hq : 0 < t ^ 2 - t + 3 := by nlinarith [sq_nonneg (t - 1 / 2)]
  have h2 : 0 < 2 * t - 1 := by simp only [Set.mem_Ioi] at ht; linarith
  positivity

/-- **`t` is strictly increasing in `φ` on `[0,π]`**, which is what turns
uniqueness in `t` into uniqueness in `φ`. Two signs: `dt/dc < 0` (numerator
`−2t(1−t) < 0` over a denominator `≥ 7/4`) and `dc/dφ = −sin φ < 0`. -/
theorem strictMonoOn_realRootPath : StrictMonoOn realRootPath (Set.Icc 0 π) := by
  refine strictMonoOn_of_deriv_pos (convex_Icc _ _)
    (fun φ _ => (hasDerivAt_realRootPath' φ).continuousAt.continuousWithinAt) ?_
  intro φ hφ
  rw [interior_Icc] at hφ
  rw [(hasDerivAt_realRootPath' φ).deriv, realRootPath']
  have ht0 : 0 < realRoot (Real.cos φ) := realRoot_pos _
  have ht1 : realRoot (Real.cos φ) < 1 := realRoot_lt_one _
  have hden : 7 / 4 ≤ 3 * realRoot (Real.cos φ) ^ 2
      - 4 * Real.cos φ * realRoot (Real.cos φ) + (2 * Real.cos φ + 1) :=
    unitCubic_deriv_ge ht0 ht1 (unitCubic_realRoot _)
  have hsin : 0 < Real.sin φ := Real.sin_pos_of_pos_of_lt_pi hφ.1 hφ.2
  have hnum : -(-2 * realRoot (Real.cos φ) ^ 2 + 2 * realRoot (Real.cos φ)) < 0 := by
    nlinarith [ht0, ht1]
  have hd : 0 < 3 * realRoot (Real.cos φ) ^ 2 - 4 * Real.cos φ * realRoot (Real.cos φ)
      + 2 * Real.cos φ + 1 := by linarith
  have hfrac : -(-2 * realRoot (Real.cos φ) ^ 2 + 2 * realRoot (Real.cos φ))
      / (3 * realRoot (Real.cos φ) ^ 2 - 4 * Real.cos φ * realRoot (Real.cos φ)
        + 2 * Real.cos φ + 1) < 0 := div_neg_of_neg_of_pos hnum hd
  nlinarith [hfrac, hsin]

/-- **`hcoll`, proved.** At most one zero of `pairDisc` on `Icc 0 π`, hence on
the open arc. -/
theorem pairDisc_eq_zero_unique {φ₁ φ₂ : ℝ} (h1 : φ₁ ∈ Set.Icc 0 π)
    (h2 : φ₂ ∈ Set.Icc 0 π) (hz1 : pairDisc φ₁ = 0) (hz2 : pairDisc φ₂ = 0) :
    φ₁ = φ₂ := by
  have key : ∀ φ : ℝ, pairDisc φ = 0 →
      collQuartic (realRootPath φ) = 0 ∧ (1 / 2 : ℝ) ≤ realRootPath φ := by
    intro φ hz
    have hq : collQuartic (realRootPath φ) = 0 := by
      have := pairDisc_mul_eq_collQuartic φ
      rw [hz] at this
      linarith [this]
    refine ⟨hq, ?_⟩
    -- `pairDisc ≥ 0` forces `t² + t − 1 ≥ 0`, i.e. `t ≥ (√5−1)/2 > 1/2`
    have hW := W_nonneg_of_disc_nonneg (Real.cos_le_one φ) (realRootPath_pos φ)
      (realRootPath_lt_one φ) (unitCubic_realRootPath φ) (by
        have : pairDisc φ = (realRootPath φ - 2 * Real.cos φ) ^ 2
            - 4 * (realRootPath φ ^ 2 - 2 * Real.cos φ * realRootPath φ
              + 2 * Real.cos φ + 1) := rfl
        rw [← this, hz])
    nlinarith [hW, realRootPath_pos φ]
  obtain ⟨hq1, hh1⟩ := key φ₁ hz1
  obtain ⟨hq2, hh2⟩ := key φ₂ hz2
  have heq : realRootPath φ₁ = realRootPath φ₂ :=
    strictMonoOn_collQuartic.injOn hh1 hh2 (by rw [hq1, hq2])
  exact strictMonoOn_realRootPath.injOn h1 h2 heq

/-- **The transport at the concrete labelling, with continuity supplied.**

`S(π) − S(0) = π²` now rests on exactly one thing: that the collision `φ₀` is the
**only** zero of `pairDisc` on the open arc. That is a statement about a quartic
in `cos φ` — Route 32 measures its unique root at `c* = −0.7422176659` — and it
is carried as a hypothesis rather than assumed, because measuring the number of
roots of a quartic on a grid is exactly the shape of argument this lane has had
to retract twice. -/
theorem envelopeS_total_concrete_of_unique_collision {c : ℝ} (hc0 : 0 < c) (hcπ : c < π)
    (hcoll : ∀ φ ∈ Set.Ioo (0 : ℝ) π, φ ≠ c → pairDisc φ ≠ 0) :
    envelopeS Yreal (fun u => (Ypair u).1) (fun u => (Ypair u).2) π
      = envelopeS Yreal (fun u => (Ypair u).1) (fun u => (Ypair u).2) 0 + π ^ 2 :=
  envelopeS_total_concrete hc0 hcπ hcoll continuousOn_envelopeS_concrete

/-- **The collision EXISTS**, by the intermediate value theorem — and both ends
are already theorems: `pairDisc 0 < 0` (the pair is complex at `φ = 0`) and
`pairDisc π > 0` (it is real at `φ = π`, from the cubic). Nothing numeric. -/
theorem exists_collision : ∃ c ∈ Set.Ioo (0 : ℝ) π, pairDisc c = 0 := by
  have hsub := intermediate_value_Ioo Real.pi_pos.le
    (continuous_pairDisc.continuousOn (s := Set.Icc 0 π))
  have hmem : (0 : ℝ) ∈ Set.Ioo (pairDisc 0) (pairDisc π) :=
    ⟨pairDisc_zero_neg, pairDisc_pi_pos⟩
  obtain ⟨c, hc, hcz⟩ := hsub hmem
  exact ⟨c, hc, hcz⟩

/-- **The transport, unconditionally.**

    envelopeS Yreal Ypair.1 Ypair.2 π = envelopeS Yreal Ypair.1 Ypair.2 0 + π²

Gap A, closed. Every hypothesis is discharged: the labelling is constructed, its
branch routing settled, `VSide` and the two log sums proved at it, `heⱼ` pinned by
`k = 0` in four regimes, continuity carried across the cut at `φ = π` by
`continuousAt_re_cLiTwoExt`, and the collision both located (IVT) and shown
unique (a quartic with one minimum).

⚠ **This is not the sum rule.** `S(0) = −3π²/2` *is* the 5₂ sum rule and
`S(0) = 3·S(π)`, so `S(π) − S(0) = π²` **reformulates** it. Closing Gap A moves a
named gap inside a proved chain; it does not move the headline.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. -/
theorem envelopeS_total_concrete_final :
    envelopeS Yreal (fun u => (Ypair u).1) (fun u => (Ypair u).2) π
      = envelopeS Yreal (fun u => (Ypair u).1) (fun u => (Ypair u).2) 0 + π ^ 2 := by
  obtain ⟨c, hc, hcz⟩ := exists_collision
  refine envelopeS_total_concrete_of_unique_collision hc.1 hc.2 ?_
  intro φ hφ hne hz
  exact hne (pairDisc_eq_zero_unique ⟨hφ.1.le, hφ.2.le⟩ ⟨hc.1.le, hc.2.le⟩ hz hcz)

end QOU.QBeta.FiveTwoDeformedSaddle
