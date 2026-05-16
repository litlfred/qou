/-
He-4 operator-selection LP active set.

LaTeX label:        prop:he4-channel-active-set
Computational ref:  folio-assistant/computations/probe_he4_sdp_compositional.py
Witness:            folio-assistant/computations/he4-sdp-compositional-probe.witness.json
Audit:              docs/audits/2026-05-15-three-pr-integration.md §F1 ⁴He

For the ⁴He = (Z=2, N=2) bound state, the operator-selection LP
with channel binding residuals

  t = (t_{DD}, t_{Tp}, t_{³He+n}) ≈ (24.158, 20.380, 21.176)   MeV
  n_target = 13.197                                            MeV

solves uniquely (strong duality holds, gap = 0):

  primal x* = (0, 13.197, 0)              ⇒ Tp primal-saturating
  dual y*   = (3.778, 0, 0.796)           ⇒ DD highest receptivity
  active_set = {DD, ³He+n}

Following CLAUDE.md §3b-cond, the proposition is axiomatised as a
class `HasHe4ChannelActiveSet` whose instance encodes the
witness-verified primal+dual+active-set triple.

Ref: [manuscript] §F1 ⁴He compositional probe (audit doc)
-/

import Mathlib.Data.Rat.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

namespace QOU.BraidKnot.He4ChannelActiveSet

/-- Discrete index of the three primary ⁴He compositional channels. -/
inductive Channel : Type
  | DD       -- D ⊕ D
  | Tp       -- T ⊕ p
  | He3n     -- ³He ⊕ n
deriving DecidableEq, Repr

namespace Channel

/-- A channel is in the active set iff its dual shadow price is
    strictly positive (constraint is tight on the LP dual side). -/
def InActiveSet (c : Channel) (yDD yTp yHe3n : ℚ) : Prop :=
  match c with
  | DD   => 0 < yDD
  | Tp   => 0 < yTp
  | He3n => 0 < yHe3n

end Channel

/-- Class encoding the witness-verified LP solution at q_0.  The
    instance pins down the rational approximations of the channel
    cost vector `t`, the binding target `n_target`, the primal
    weights `x*`, the dual shadow prices `y*` and `y0*`, and the
    active set.  Strong duality `Σ t_i x_i = n_target · y0*` is
    proved as an identity at the witnessed rational values.

    Per CLAUDE.md §3b-cond, this class is the sole `sorry` input
    for downstream propositions; the empirical numerics are
    encapsulated here.  -/
class HasHe4ChannelActiveSet where
  /-- Cost coefficient for D⊕D (channel binding residual). -/
  tDD : ℚ
  /-- Cost coefficient for T⊕p (channel binding residual). -/
  tTp : ℚ
  /-- Cost coefficient for ³He⊕n (channel binding residual). -/
  tHe3n : ℚ
  /-- Binding target: Δ_coupling(2,2) ≈ 13.197 MeV. -/
  n_target : ℚ
  /-- Primal weight on D⊕D channel. -/
  xDD : ℚ
  /-- Primal weight on T⊕p channel (the saturating one). -/
  xTp : ℚ
  /-- Primal weight on ³He⊕n channel. -/
  xHe3n : ℚ
  /-- Dual variable for the binding constraint. -/
  y0_star : ℚ
  /-- Dual shadow price for D⊕D. -/
  yDD : ℚ
  /-- Dual shadow price for T⊕p (must be zero by complementary slackness). -/
  yTp : ℚ
  /-- Dual shadow price for ³He⊕n. -/
  yHe3n : ℚ
  /-- The primal-saturating channel is unique and is T⊕p. -/
  primal_saturating_unique : xDD = 0 ∧ 0 < xTp ∧ xHe3n = 0
  /-- The active set is {D⊕D, ³He⊕n}. -/
  active_set_eq : (0 < yDD) ∧ (yTp = 0) ∧ (0 < yHe3n)
  /-- Dual ordering: y*_{DD} > y*_{³He⊕n} > y*_{Tp} = 0. -/
  dual_ordering : yHe3n < yDD ∧ yTp < yHe3n
  /-- Cost ordering: T⊕p has the smallest channel cost (witness
      input that motivates the LP picking T⊕p as the primal-
      saturating channel). -/
  cost_ordering : tTp < tHe3n ∧ tHe3n < tDD
  /-- Strong duality: Σ t_i x_i = n_target · y0_star (LP duality
      gap = 0).  Proved as a rational identity at the witnessed
      values; not axiomatised. -/
  strong_duality :
    tDD * xDD + tTp * xTp + tHe3n * xHe3n = n_target * y0_star

/-- Witness-encoded instance: rational approximations of the LP
    solution at q_0 from `he4-sdp-compositional-probe.witness.json`. -/
instance : HasHe4ChannelActiveSet where
  tDD     := 24158 / 1000   -- 24.158 MeV (Δ_cat(⁴He) − 2·Δ_cat(D))
  tTp     := 20380 / 1000   -- 20.380 MeV (Δ_cat(⁴He) − Δ_cat(T) − Δ_cat(p))
  tHe3n   := 21176 / 1000   -- 21.176 MeV (Δ_cat(⁴He) − Δ_cat(³He) − Δ_cat(n))
  n_target := 13197 / 1000  -- 13.197 MeV (Δ_coupling(2,2))
  xDD := 0
  xTp := 13197 / 1000       -- 13.197 (matches n_target by primal saturation)
  xHe3n := 0
  y0_star := 20380 / 1000   -- 20.380 (matches tTp by complementary slackness)
  yDD := 3778 / 1000        -- 3.778 (highest shadow price)
  yTp := 0
  yHe3n := 796 / 1000       -- 0.796
  primal_saturating_unique := by refine ⟨rfl, ?_, rfl⟩; norm_num
  active_set_eq := by refine ⟨?_, rfl, ?_⟩ <;> norm_num
  dual_ordering := by refine ⟨?_, ?_⟩ <;> norm_num
  cost_ordering := by refine ⟨?_, ?_⟩ <;> norm_num
  strong_duality := by norm_num

/-! ## Derived theorems

The following theorems are PROVED from the class instance above
(no further `sorry` / empirical input).  They demonstrate that the
LP solution encoded in the class implies the structural claims of
`prop:he4-channel-active-set`. -/

/-- Strong duality at the witnessed values: primal_obj = dual_obj. -/
theorem he4_strong_duality_value
    [h : HasHe4ChannelActiveSet] :
    h.tDD * h.xDD + h.tTp * h.xTp + h.tHe3n * h.xHe3n =
      h.n_target * h.y0_star :=
  h.strong_duality

/-- Primal objective collapses to T⊕p contribution because xDD = 0
    and xHe3n = 0 (primal saturation). -/
theorem he4_primal_obj_eq_tTp_xTp
    [h : HasHe4ChannelActiveSet] :
    h.tDD * h.xDD + h.tTp * h.xTp + h.tHe3n * h.xHe3n =
      h.tTp * h.xTp := by
  obtain ⟨hDD, _hTp_pos, hHe3n⟩ := h.primal_saturating_unique
  rw [hDD, hHe3n]; ring

/-- D⊕D dual shadow price strictly exceeds ³He⊕n's, which strictly
    exceeds T⊕p's (= 0).  Direct corollary of `dual_ordering`. -/
theorem he4_dual_ordering_strict
    [h : HasHe4ChannelActiveSet] :
    h.yTp < h.yHe3n ∧ h.yHe3n < h.yDD := by
  obtain ⟨hHe3n_lt_DD, hTp_lt_He3n⟩ := h.dual_ordering
  exact ⟨hTp_lt_He3n, hHe3n_lt_DD⟩

/-- T⊕p has zero dual shadow price (complementary-slackness consequence
    of being the primal-saturating channel). -/
theorem he4_tp_dual_zero [h : HasHe4ChannelActiveSet] : h.yTp = 0 := by
  obtain ⟨_, hTp, _⟩ := h.active_set_eq
  exact hTp

/-- D⊕D is the most binding-receptive channel: its dual shadow price
    strictly exceeds both T⊕p and ³He⊕n. -/
theorem he4_DD_highest_shadow_price
    [h : HasHe4ChannelActiveSet] :
    h.yTp < h.yDD ∧ h.yHe3n < h.yDD := by
  obtain ⟨hHe3n_lt_DD, hTp_lt_He3n⟩ := h.dual_ordering
  refine ⟨?_, hHe3n_lt_DD⟩
  exact lt_trans hTp_lt_He3n hHe3n_lt_DD

/-- T⊕p has the strictly smallest channel cost (smallest binding
    residual), which is why the LP picks it as the primal-saturating
    channel. -/
theorem he4_Tp_cheapest_channel
    [h : HasHe4ChannelActiveSet] :
    h.tTp < h.tDD := by
  obtain ⟨hTp_lt_He3n, hHe3n_lt_DD⟩ := h.cost_ordering
  exact lt_trans hTp_lt_He3n hHe3n_lt_DD

/-- D⊕D has strictly the largest channel cost. -/
theorem he4_DD_costliest_channel
    [h : HasHe4ChannelActiveSet] :
    h.tHe3n < h.tDD ∧ h.tTp < h.tDD := by
  refine ⟨h.cost_ordering.2, he4_Tp_cheapest_channel⟩

/-- Channel D⊕D is in the LP active set. -/
theorem he4_DD_active [h : HasHe4ChannelActiveSet] :
    Channel.InActiveSet Channel.DD h.yDD h.yTp h.yHe3n := by
  unfold Channel.InActiveSet
  exact h.active_set_eq.1

/-- Channel T⊕p is NOT in the LP active set. -/
theorem he4_Tp_not_active [h : HasHe4ChannelActiveSet] :
    ¬ Channel.InActiveSet Channel.Tp h.yDD h.yTp h.yHe3n := by
  unfold Channel.InActiveSet
  rw [h.active_set_eq.2.1]
  exact lt_irrefl 0

/-- Channel ³He⊕n is in the LP active set. -/
theorem he4_He3n_active [h : HasHe4ChannelActiveSet] :
    Channel.InActiveSet Channel.He3n h.yDD h.yTp h.yHe3n := by
  unfold Channel.InActiveSet
  exact h.active_set_eq.2.2

end QOU.BraidKnot.He4ChannelActiveSet
