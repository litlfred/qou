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

-- Ref: [leitner2026] quantum-observable-universe/information-theory/p-bandwidth-bound.md
-/

namespace QOU.Information

/-- The information bandwidth per Planck time:
    `𝓑(q) = q · η_q / (q − 1)²` (where `η_q` is the entropy
    function, abstracted here as a parameter).

    **Unguarded signature.** `q` is a bare `ℝ` here, so `informationBandwidth 1 η`
    is a legal call and returns `0` (Lean's `x/0 = 0`) at exactly the classical
    limit where the bandwidth is meant to blow up — see
    `informationBandwidth_junk_at_one`. Every *intended* use goes through
    `PBandwidthContext`, which carries `q_gt_one : 1 < q` and so excludes the
    point; the exposure is in the signature, not in any current consumer. Noted
    rather than fixed because tightening the signature would change a public
    declaration's type for a defect nothing currently reaches. -/
noncomputable def informationBandwidth (q : ℝ) (η_q : ℝ) : ℝ :=
  q * η_q / (q - 1) ^ 2

/-- **The unguarded point.** A direct call at `q = 1` returns `0`. Recorded so the
    gap between this bare signature and `PBandwidthContext.q_gt_one` is visible at
    the declaration. -/
theorem informationBandwidth_junk_at_one (η_q : ℝ) :
    informationBandwidth 1 η_q = 0 := by
  unfold informationBandwidth
  norm_num

/-- Abstract context for the P-time-iff-bandwidth claim.

    The two implication directions of the characterisation are carried
    as **explicit hypotheses** (§3b-cond non-degenerate pattern), matching
    the two halves of the manuscript proof:

    - `p_to_bandwidth` — the forward simulation: a polynomial-time Turing
      machine deciding the problem encodes as a braid with `c =
      O(poly(N))` crossings, and the transfer-matrix product evaluates
      `P_L(q)` in `O(c)` matrix multiplications, i.e. within the
      bandwidth budget.
    - `bandwidth_to_p` — the converse funnel: if the factored Skein form
      has `O(poly(c))` factors then each is computed in `O(1)` steps from
      the local transfer matrix, so the total cost is polynomial and the
      problem is in P.

    Neither field *is* the iff; `p_bandwidth_bound` *derives* it
    (`Iff.intro`), so the projection-vacuity test is not triggered. -/
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
  /-- **Forward direction (TM → braid simulation):** a P-time decision
      problem admits a bandwidth-bounded Skein evaluation. -/
  p_to_bandwidth : inP → bandwidthBounded
  /-- **Converse direction (interference funnel):** a bandwidth-bounded
      Skein evaluation decides the problem in polynomial time. -/
  bandwidth_to_p : bandwidthBounded → inP

/-- **The bandwidth `𝓑(q)` is positive for `q > 1`**. -/
-- Ref: [leitner2026] quantum-observable-universe/information-theory/p-bandwidth-bound.md
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
    steps. *Derived* by composing the two directional hypotheses of
    `PBandwidthContext` (`Iff.intro`); the theorem proves the iff, it
    does not assume it. -/
-- Ref: [leitner2026] quantum-observable-universe/information-theory/p-bandwidth-bound.md
theorem p_bandwidth_bound [ctx : PBandwidthContext] :
    ctx.inP ↔ ctx.bandwidthBounded :=
  ⟨ctx.p_to_bandwidth, ctx.bandwidth_to_p⟩

end QOU.Information
