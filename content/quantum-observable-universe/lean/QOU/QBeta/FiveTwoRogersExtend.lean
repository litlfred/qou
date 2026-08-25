import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Extending Rogers `L` off `[0,1]` — and why two ladder hypotheses were *false*

Bean `qou-rhyp`, item 2. This file discharges the inversion and Landen
hypotheses of `QOU/QBeta/FiveTwoLevelSevenLadder.lean`, and corrects the reason
they were open.

## The correction

`qou-rhyp` graded `hinv1` and `hlan1/2/3` as "real analysis, not yet in the
corpus — each is a one-variable identity provable the same way
`LiTwo_reflection'` is, so the corpus's existing proof is the template."

**That grading was wrong, in both directions.**

The corpus's dilogarithm is a bare power series,

    LiTwo x = ∑' k, x ^ (k + 1) / (k + 1) ^ 2      (`QOU/Archimedean/DilogarithmArchimedeanLimit.lean`)

which is summable exactly on `[-1, 1]`. Off that interval Lean's `tsum` returns
its **junk value `0`** (`tsum_eq_zero_of_not_summable`), and `Real.log` is
**even** (`Real.log_neg_eq_log`), so a Rogers `L` built directly on `LiTwo` is,
for `|x| > 1`, the function `log|x| · log|1 - x| / 2` — not the dilogarithm.

Two of the ladder's arguments sit exactly there. The ladder's `w₁` is the root
`2.2469796…` of `w³ - 2w² - w + 1`, so `hinv1` is evaluated at `w₁ > 1` and
`hlan1` at `-w₁ < -1`. Numerically (probe
`qbeta_5two_route13_rogers_extension_probe.py`, 60 dps) the two hypotheses fail
by

    hinv1 : residual  -2.4543…        hlan1 : residual  +1.5692…

while the other seven hold to `1e-61`. They were not hard; they were **false**.

## The repair, and what it costs

The fix is definitional, not analytic. The extended real Rogers dilogarithm
(Zagier, *The dilogarithm function*, §I.3) is **defined** off `[0,1]` by

    L x  :=  2·L 1 - L (1/x)        for x > 1
    L x  :=  -L (x/(x-1))           for x < 0

so inversion and Landen hold **by construction**. That is what `extend` below
does, and the four hypotheses become one-line consequences of `if`-unfolding
plus the two membership facts `1/x ∈ [0,1]` and `x/(x-1) ∈ [0,1]`.

The cost is honest and worth stating: the Lean object is then a piecewise
function, *not* proved equal to the analytic continuation of `Li₂`. It agrees
with it — the same probe confirms the extension reproduces the three level-7
numerators `(17, 5, -1)/7 · π²/6` to `1e-61` — but "agrees numerically" is not
"is". Anyone wanting the analytic identification must prove it separately.

## Net effect on `qou-rhyp`

Of the twelve hypotheses `numerators_original_form` takes, this file discharges
the four reduction ones (`hinv1`, `hlan1`, `hlan2`, `hlan3`) for any `f`
whatever, and `extend_reflection` transports reflection through the extension.
**The genuinely open input is now exactly the three five-term instances**
`hA`, `hB`, `hC`.

Everything here is generic in `f` and `c`: no dilogarithm is involved, so this
file builds off basic `Mathlib` order/field lemmas alone and does not wait on
the `DilogReflection` cone.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoRogersExtend

variable (c : ℝ) (f : ℝ → ℝ)

/-- Extend `f`, thought of as defined on `[0,1]`, to all of `ℝ` by the Rogers
recipe: inversion above `1`, Landen below `0`. `c` plays the role of `f 1`. -/
noncomputable def extend (x : ℝ) : ℝ :=
  if 1 < x then 2 * c - f (1 / x)
  else if x < 0 then -f (x / (x - 1))
  else f x

theorem extend_of_one_lt {x : ℝ} (hx : 1 < x) : extend c f x = 2 * c - f (1 / x) :=
  if_pos hx

theorem extend_of_neg {x : ℝ} (hx : x < 0) : extend c f x = -f (x / (x - 1)) := by
  unfold extend
  rw [if_neg (not_lt.mpr (by linarith)), if_pos hx]

/-- On `[0,1]` the extension is the original function. -/
theorem extend_of_mem {x : ℝ} (h0 : 0 ≤ x) (h1 : x ≤ 1) : extend c f x = f x := by
  unfold extend
  rw [if_neg (not_lt.mpr h1), if_neg (not_lt.mpr h0)]

/-- Inversion lands in the unit interval: this is why `extend` closes up. -/
theorem inv_mem_unit {x : ℝ} (hx : 1 < x) : 0 ≤ 1 / x ∧ 1 / x ≤ 1 := by
  have hx0 : (0 : ℝ) < x := by linarith
  exact ⟨le_of_lt (by positivity), (div_le_one hx0).mpr (by linarith)⟩

/-- Landen lands in the unit interval, for *every* negative `x` — including
`x < -1`, which is exactly where the power series had nothing to say. -/
theorem landen_mem_unit {x : ℝ} (hx : x < 0) : 0 ≤ x / (x - 1) ∧ x / (x - 1) ≤ 1 := by
  have hd : x - 1 < 0 := by linarith
  refine ⟨le_of_lt (div_pos_of_neg_of_neg hx hd), ?_⟩
  have hne : x - 1 ≠ 0 := ne_of_lt hd
  have key : x / (x - 1) - 1 = 1 / (x - 1) := by
    field_simp
    ring
  have hneg : 1 / (x - 1) < 0 := div_neg_of_pos_of_neg one_pos hd
  linarith

/-- **Inversion**, by construction. -/
theorem extend_inversion {x : ℝ} (hx : 1 < x) :
    extend c f x + extend c f (1 / x) = 2 * c := by
  obtain ⟨h0, h1⟩ := inv_mem_unit hx
  rw [extend_of_one_lt c f hx, extend_of_mem c f h0 h1]
  ring

/-- **Landen**, by construction. -/
theorem extend_landen {x : ℝ} (hx : x < 0) :
    extend c f x + extend c f (x / (x - 1)) = 0 := by
  obtain ⟨h0, h1⟩ := landen_mem_unit hx
  rw [extend_of_neg c f hx, extend_of_mem c f h0 h1]
  ring

/-- Reflection survives the extension unchanged on `(0,1)`, since both `x` and
`1 - x` stay in the middle branch. This is what carries
`FiveTwoRogersReflection.rogersL_reflection` across. -/
theorem extend_reflection {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hrefl : f x + f (1 - x) = c) :
    extend c f x + extend c f (1 - x) = c := by
  rw [extend_of_mem c f (le_of_lt hx0) (le_of_lt hx1),
      extend_of_mem c f (by linarith) (by linarith)]
  exact hrefl

/-! ### The shapes `FiveTwoLevelSevenLadder.numerators_original_form` consumes

The ladder states its reduction hypotheses as equations `L x = …`, not as sums.
These are those forms. -/

/-- `hinv1`-shaped: `L x = 2·L1 - L (1/x)` for `x > 1`. -/
theorem extend_inv_eq {x : ℝ} (hx : 1 < x) :
    extend c f x = 2 * c - extend c f (1 / x) := by
  have h := extend_inversion c f hx
  linarith

/-- `hlan`-shaped: `L x = -L (x/(x-1))` for `x < 0`. -/
theorem extend_landen_eq {x : ℝ} (hx : x < 0) :
    extend c f x = -extend c f (x / (x - 1)) := by
  have h := extend_landen c f hx
  linarith

/-- `hrw`-shaped: `L (1 - x) = L1 - L x` for `x ∈ (0,1)`. -/
theorem extend_reflection_eq {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1)
    (hrefl : f x + f (1 - x) = c) :
    extend c f (1 - x) = c - extend c f x := by
  have h := extend_reflection c f hx0 hx1 hrefl
  linarith

end QOU.QBeta.FiveTwoRogersExtend
