import QOU.QBeta.FiveTwoRootLabelling
import QOU.QBeta.FiveTwoTransport
import QOU.QBeta.FiveTwoPairSaddle

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

**The 5₂ sum rule remains verified to 80 dps, unproved.**
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

end QOU.QBeta.FiveTwoDeformedSaddle
