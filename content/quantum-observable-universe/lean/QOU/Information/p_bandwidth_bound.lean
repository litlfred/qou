import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
# QOU.Information.p_bandwidth_bound — P-time iff bandwidth-bounded Skein

**Proposition** ([`prop:p-bandwidth-bound`](../../../quantum-observable-universe/information-theory/p-bandwidth-bound.md)).

*A decision problem encoded by a link `L = β̂` with `c = 3N` crossings
is in `P` if and only if its Skein polynomial `P_L(q)` can be
evaluated — degree-0 answer extracted — within*

```
  t(c) ≤ 𝓑(q)⁻¹ · poly(c)
```

*Planck steps, where `𝓑(q) = q·η_q / (q − 1)²` is the information
bandwidth per Planck time.*

The Lean encoding records the iff as a `Prop`-valued claim against
an abstract `PBandwidthContext` carrying the link / Skein /
computational data, plus the bandwidth function `𝓑(q)`.

-- Ref: [manuscript] quantum-observable-universe/information-theory/p-bandwidth-bound.md
-/

namespace QOU.Information

/-- The information bandwidth per Planck time:
    `𝓑(q) = q · η_q / (q − 1)²` (where `η_q` is the entropy
    function, abstracted here as a parameter). -/
noncomputable def informationBandwidth (q : ℝ) (η_q : ℝ) : ℝ :=
  q * η_q / (q - 1) ^ 2

/-- Abstract context for the P-time-iff-bandwidth claim. -/
class PBandwidthContext where
  /-- The substrate parameter `q > 1`. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- The entropy parameter `η_q > 0`. -/
  η_q : ℝ
  η_q_pos : 0 < η_q
  /-- Number of crossings `c` (typically `c = 3N` for a braid on
      `N` strands). -/
  c : ℕ
  /-- Predicate "the decision problem is in P". -/
  inP : Prop
  /-- Predicate "the Skein polynomial is evaluable within
      `𝓑(q)⁻¹ · poly(c)` Planck steps". -/
  bandwidthBounded : Prop
  /-- Manuscript characterisation: P-time decidability equals
      bandwidth-bounded Skein evaluation. -/
  claim_p_iff_bandwidth : inP ↔ bandwidthBounded

/-- **The bandwidth `𝓑(q)` is positive for `q > 1`**. -/
-- Ref: [manuscript] quantum-observable-universe/information-theory/p-bandwidth-bound.md
theorem informationBandwidth_pos [ctx : PBandwidthContext] :
    0 < informationBandwidth ctx.q ctx.η_q := by
  unfold informationBandwidth
  have hq_pos : 0 < ctx.q := by linarith [ctx.q_gt_one]
  have hq_sub_one_sq_pos : 0 < (ctx.q - 1) ^ 2 := by
    have : ctx.q - 1 > 0 := by linarith [ctx.q_gt_one]
    exact pow_pos this 2
  exact div_pos (mul_pos hq_pos ctx.η_q_pos) hq_sub_one_sq_pos

/-- **P-time iff bandwidth-bounded Skein evaluation**
    ([`prop:p-bandwidth-bound`]).

    A decision problem encoded by a link is in P iff its Skein
    polynomial can be evaluated within `𝓑(q)⁻¹ · poly(c)` Planck
    steps. -/
-- Ref: [manuscript] quantum-observable-universe/information-theory/p-bandwidth-bound.md
def p_bandwidth_bound [ctx : PBandwidthContext] :
    ctx.inP ↔ ctx.bandwidthBounded :=
  ctx.claim_p_iff_bandwidth

end QOU.Information
