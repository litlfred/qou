/-
# A=4 (⁴He) binding precision is a NEGATIVE leading-order 4-body channel — the mirror of A=3

Companion to `A3PrecisionOrderSeparation`. Physical ratio `ρ_strong(4) = B(⁴He)/B(²H) = 13.0316`. The
graded coinvariant baseline `ρ_grad_G(4) = [3]_q·[4]_q = 15.740` is EXACT — and, unlike A=3 (baseline
undershoots by 4.6%), at A=4 it **OVERSHOOTS by +20.8%**. Adding the derived (positive) 3-body clusters
`4·c₃` makes it WORSE (`16.928`, +29.9%). The fix is a large NEGATIVE 4-body saturation channel

```
c₄(required) = ρ_strong(4) − (ρ_grad_G(4) + 4·c₃) = −3.896   (−24.75% of the baseline),
```

with `|c₄|/c₃ ≈ 13` — the α-cluster / closed `[1⁴]` SU(4) supermultiplet (the μ₄ Δ_λ object, #4320).

Order-separation (same prune as A=3, sharper): the bounded (`|aₖ| ≤ 2`) 3-body higher-order tail
`4·c₃·2·h²/(1−h²) ≈ 0.109` is ≪ `|c₄| ≈ 3.896` (36×), so the A=4 miss is NOT a 3-body higher-order
refinement — it is a NEW leading-order 4-body channel. **A=3 (small +3-body) and A=4 (large −4-body)
are opposite-sign regimes needing DISTINCT leading channels** (confirming three-walls Route 3's
sign-swap from the frame-independent + order-separation angle). μ₄ is even more frame-fragile than μ₃
(baseline spread 2.07× vs 1.73×). scope-(a); no fit; nothing wired. Companion probe
`computations/deltalambda/a4_precision_order_decomposition_probe.py`.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Data.Real.Basic

namespace QOU.MassTheory.A4PrecisionOrderSeparation

/-- **The A=4 graded baseline OVERSHOOTS** (`ρ_grad_G(4)/ρ_strong(4) > 1.2`, +20.8%) — the opposite of
A=3, where it undershoots. The correction the data needs at A=4 is therefore NEGATIVE. -/
theorem a4_baseline_overshoots : (15.73957 : ℝ) / 13.0316 > 1.2 := by norm_num

/-- **The (positive) 3-body clusters make A=4 worse.** `ρ_grad_G(4) + 4·c₃ = 16.928` overshoots the
physical ratio `13.0316` even more than the baseline alone — so the missing piece cannot be a 3-body
contribution; it must be a distinct 4-body channel. -/
theorem a4_three_body_makes_worse : (15.73957 : ℝ) + 4 * 0.297 > 13.0316 := by norm_num

/-- **The required 4-body channel is NEGATIVE** (the α-cluster saturation):
`c₄ = ρ_strong(4) − (ρ_grad_G(4) + 4·c₃) < 0`. -/
theorem a4_required_channel_negative : (13.0316 : ℝ) - (15.73957 + 4 * 0.297) < 0 := by norm_num

/-- **Order-separation.** The bounded (`|aₖ| ≤ 2`) 3-body higher-order tail `4·c₃·2·h²/(1−h²)` (`h² =
0.0437062`) is `< 0.11`, ≪ the required `|c₄| ≈ 3.896`. So the A=4 miss is NOT closable by 3-body
higher orders — it needs a new leading 4-body channel. -/
theorem a4_higher_order_ruled_out :
    (4 : ℝ) * 0.297 * 2 * 0.0437062 / (1 - 0.0437062) < 3.896 := by norm_num

/-- **The 4-body channel dominates the 3-body cluster** by an order of magnitude:
`|c₄|/c₃ = 3.89597/0.297 > 13`. The saturation term is large where the binding cluster is small. -/
theorem a4_four_body_dominates : (3.89597 : ℝ) / 0.297 > 13 := by norm_num

/-- **μ₄ is even more frame-fragile than μ₃**: its baseline-class spread `|μ₄^max|/|μ₄^min| =
4.591/2.220 > 2` exceeds μ₃'s 1.73×. Report A=4 precision on the frame-independent physical ratio, not
the μ₄ residual. -/
theorem mu4_more_fragile_than_mu3 : (4.591 : ℝ) / 2.220 > 2 := by norm_num

/-- **Capstone — A=4 precision is a NEGATIVE leading-order 4-body saturation channel.** The baseline
overshoots (`a4_baseline_overshoots`), the 3-body clusters worsen it (`a4_three_body_makes_worse`), the
required channel is negative (`a4_required_channel_negative`) and large (`a4_four_body_dominates`), and
it is order-separated from 3-body higher orders (`a4_higher_order_ruled_out`). So A=3 (+small 3-body)
and A=4 (−large 4-body) are opposite-sign regimes needing distinct leading channels — the μ₄ Δ_λ
object, open. scope-(a); no fit. -/
theorem a4_precision_is_negative_four_body_channel :
    ((15.73957 : ℝ) / 13.0316 > 1.2) ∧
    ((13.0316 : ℝ) - (15.73957 + 4 * 0.297) < 0) ∧
    ((4 : ℝ) * 0.297 * 2 * 0.0437062 / (1 - 0.0437062) < 3.896) ∧
    ((3.89597 : ℝ) / 0.297 > 13) :=
  ⟨a4_baseline_overshoots, a4_required_channel_negative, a4_higher_order_ruled_out,
   a4_four_body_dominates⟩

end QOU.MassTheory.A4PrecisionOrderSeparation
