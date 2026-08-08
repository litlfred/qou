import QOU.QBeta.FiveTwoRootLabelling
import QOU.QBeta.FiveTwoTransport

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

end QOU.QBeta.FiveTwoDeformedSaddle
