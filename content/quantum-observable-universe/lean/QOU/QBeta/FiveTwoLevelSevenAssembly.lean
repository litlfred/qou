import QOU.QBeta.FiveTwoEnvelopeWiring
import QOU.QBeta.FiveTwoLevelSevenBridge
import QOU.QBeta.FiveTwoExtendIdentification
import QOU.QBeta.FiveTwoAbelFiveTerm

/-!
# `S(π) = −π²/2`, assembled — bean `qou-asem`

Four proved pieces, composed:

| piece | statement |
|---|---|
| `extended_sum` | `Σₖ (2·extend L(wₖ) + extend L(−wₖ)) = π²/2` |
| `extend_eq_re_cRogersL` | `extend = Re` of the **analytic** Rogers `L` (`qou-rstq` item 4) |
| `levelSeven_orbit_data` | the `wₖ` are the level-7 roots, negated |
| `corr_sum_eq_neg_pi_sq` | `Σⱼ corr yⱼ = −π²` |

giving `Σⱼ Re V(−1, yⱼ) = π²/2 − π² = −π²/2`.

## Why this could not be written before today

`extended_sum` is about the corpus's **piecewise** `extend`; `deformedV` is built
from the **analytic** `cLiTwoExt`. Until `extend_eq_re_cRogersL` (item 4) those
were different objects and the composition did not typecheck, let alone hold.
Route 32 G9 existed precisely to assert that gap, and is now rewritten.

## ⚠ What this is NOT

`S(0) = −3π²/2` **is** the 5₂ sum rule; `S(π) = −π²/2` is its value at the other
endpoint, and `S(0) = 3·S(π)`. So this assembles one endpoint of a transport
that **reformulates** the sum rule rather than approaching it. It is a
composition of proved parts, and the parts were the work.

Still open and untouched here: **Gap A** (`qou-glbl`), the globally
differentiable root labelling — the one remaining hypothesis in the transport
that would connect `S(π)` to `S(0)`.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoLevelSevenAssembly

open QOU.MathlibExt QOU.QBeta.FiveTwoDeformedSaddle
open QOU.QBeta.FiveTwoExtendIdentification
open QOU.QBeta.FiveTwoRogersExtend QOU.QBeta.FiveTwoRogersReflection
open QOU.QBeta.FiveTwoAbelFiveTerm

/-- **`V` at `x = −1` splits into two Rogers `L`s and the correction.**

`V(−1, y) = cLiTwoExt y + 2·cLiTwoExt(−y) + log(−y)²`, and subtracting
`2·L(−y) + L(y)` leaves exactly `corr`'s integrand. An identity in `ℂ`, before
any real part is taken. -/
theorem deformedV_neg_one_eq (y : ℂ) :
    deformedV (-1, y)
      = (cRogersL (-y) + cRogersL (-y) + cRogersL y)
        + (Complex.log (-y) ^ 2 - Complex.log (-y) * Complex.log (1 + y)
            - Complex.log y * Complex.log (1 - y) / 2) := by
  simp only [deformedV, cRogersL]
  have h1 : ((-1 : ℂ)) * y = -y := by ring
  have h2 : y / ((-1 : ℂ)) = -y := by ring
  have h3 : (1 : ℂ) - (-y) = 1 + y := by ring
  rw [h1, h2, h3]
  ring

/-- The real part of the split — `corr` is by definition the real part of the
bracket above. -/
theorem re_deformedV_neg_one (y : ℝ) :
    (deformedV (-1, ((y : ℝ) : ℂ))).re
      = 2 * (cRogersL (-((y : ℝ) : ℂ))).re + (cRogersL ((y : ℝ) : ℂ)).re + corr y := by
  rw [deformedV_neg_one_eq, corr]
  simp only [Complex.add_re, Complex.sub_re]
  ring

/-- **`Σⱼ Re V(−1, yⱼ) = −π²/2`** — the assembly.

Stated over the orbit of a root `x` of `x³ − 2x² − x + 1` in `(1/2, 1)`, which
is the shape `extended_sum` is stated in; `levelSeven_orbit_data` identifies the
negated orbit with the level-7 roots. -/
theorem sum_re_deformedV_at_neg_one {x : ℝ}
    (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0) (hlo : 1 / 2 < x) (hhi : x < 1) :
    (deformedV (-1, ((((1 - x) / x : ℝ)) : ℂ))).re
      + (deformedV (-1, ((((-(1 / (1 - x))) : ℝ)) : ℂ))).re
      + (deformedV (-1, (((-x : ℝ)) : ℂ))).re
      = -Real.pi ^ 2 / 2 := by
  obtain ⟨hr₁, hr₂, hr₃, hp0, hp1, hn₂, hn₃, hne₂, hne₃⟩ :=
    levelSeven_orbit_data hx hlo hhi
  have hx0 : (0 : ℝ) < x := by linarith
  have h1x : (0 : ℝ) < 1 - x := by linarith
  -- the correction sums to −π²
  have hcorr := corr_sum_eq_neg_pi_sq hr₁ hr₂ hr₃ hp0 hp1 hn₂ hn₃ hne₂ hne₃
  -- the cyclotomic identity, transported to the analytic `L` by item 4
  have hsum := extended_sum hx hlo hhi
  -- every `extend` becomes `Re cRogersL` — item 4, at all six arguments
  have key : ∀ z : ℝ, z ≠ 0 → z ≠ 1 →
      extend (Real.pi ^ 2 / 6) rogersL z = (cRogersL ((z : ℝ) : ℂ)).re :=
    fun z h0 h1 => extend_eq_re_cRogersL h0 h1
  have hw1 : (0 : ℝ) < 1 / (1 - x) := by positivity
  have hw3 : (x - 1) / x < 0 := div_neg_of_neg_of_pos (by linarith) hx0
  have e1 := key (1 / (1 - x)) (ne_of_gt hw1) (by
    intro h; rw [div_eq_one_iff_eq (ne_of_gt h1x)] at h; linarith)
  have e2 := key (-(1 / (1 - x))) (by linarith) (by intro h; linarith)
  have e3 := key x (ne_of_gt hx0) (ne_of_lt hhi)
  have e4 := key (-x) (by linarith) (by intro h; linarith)
  have e5 := key ((x - 1) / x) (ne_of_lt hw3) (by intro h; linarith)
  -- `−((x−1)/x) = (1−x)/x`, which is in `(0,1)`, so it is neither `0` nor `1`
  have hflip : -((x - 1) / x) = (1 - x) / x := by ring
  have e6 := key (-((x - 1) / x))
    (by rw [hflip]; exact ne_of_gt hp0)
    (by rw [hflip]; exact ne_of_lt hp1)
  rw [e1, e2, e3, e4, e5, e6] at hsum
  -- `−((x−1)/x)` and `(1−x)/x` are the same number; align them in `hsum`
  rw [hflip] at hsum
  -- the three `V` splits
  have v1 := re_deformedV_neg_one ((1 - x) / x)
  have v2 := re_deformedV_neg_one (-(1 / (1 - x)))
  have v3 := re_deformedV_neg_one (-x)
  -- align the casts: `−↑z = ↑(−z)`, and `−((x−1)/x) = (1−x)/x`
  have c1 : -((((1 - x) / x : ℝ)) : ℂ) = ((((x - 1) / x : ℝ)) : ℂ) := by
    push_cast; ring
  have c2 : -(((-(1 / (1 - x)) : ℝ)) : ℂ) = (((1 / (1 - x) : ℝ)) : ℂ) := by
    push_cast; ring
  have c3 : -(((-x : ℝ)) : ℂ) = ((x : ℝ) : ℂ) := by push_cast; ring
  rw [c1] at v1
  rw [c2] at v2
  rw [c3] at v3
  rw [v1, v2, v3]
  linear_combination hsum + hcorr

end QOU.QBeta.FiveTwoLevelSevenAssembly
