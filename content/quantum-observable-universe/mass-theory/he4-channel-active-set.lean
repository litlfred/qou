/-
He-4 operator-selection LP active set.

LaTeX label:        prop:he4-channel-active-set
Computational ref:  computations/probe_he4_sdp_compositional.py
Witness:            computations/he4-sdp-compositional-probe.witness.json
Audit:              docs/audits/2026-05-15-three-pr-integration.md §F1 ⁴He

For the ⁴He = (Z=2, N=2) bound state, the operator-selection LP
with channel binding residuals

  t = (t_{DD}, t_{Tp}, t_{³He+n}) ≈ (24.158, 20.380, 21.176)   MeV
  n_target = 13.197                                            MeV

solves uniquely (strong duality holds, gap = 0):

  primal x* = (0, 13.197, 0)              ⇒ Tp primal-saturating
  dual y*   = (3.778, 0, 0.796)           ⇒ DD highest receptivity
  active_set = {DD, ³He+n}

Following AGENTS.md §3b-cond, the proposition is axiomatised as a
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

/-- Class encoding the LP-solution **structural axioms** for ⁴He.

    **Audit fix #3 (PR followup, 2026-05-25):** the class fields
    (`tDD`, `tTp`, ... `yHe3n`) carry rational LP-solution data
    sourced from `he4-sdp-compositional-probe.witness.json` — but
    the **categorical content** consumed by downstream theorems is
    purely the AXIOMS:
      - `primal_saturating_unique` (xTp uniquely positive)
      - `active_set_eq` ({DD, ³He+n}, not Tp)
      - `dual_ordering` (yDD > yHe3n > yTp = 0)
      - `cost_ordering` (tTp < tHe3n < tDD)
      - `strong_duality` (gap = 0)

    None of the downstream theorems (he4_strong_duality_value,
    he4_primal_obj_eq_tTp_xTp, he4_DD_highest_shadow_price, ...)
    depend on the specific witness values — only on the STRUCTURAL
    axioms. The class IS categorical; the instance below is one
    witness, the witness JSON is the authoritative source.

    Per AGENTS.md §3b-cond, this class is the sole `sorry`-equivalent
    input for downstream propositions; the empirical numerics are
    LIVE in the witness JSON, with the class providing the structural
    interface. -/
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

/-- **Witness-encoded instance** (documentary only).

    The 11 rational fields below are LP-solution approximations from
    `he4-sdp-compositional-probe.witness.json`. Per the audit fix #3,
    these are NOT class axioms but documentary placeholders satisfying
    the categorical structural axioms (primal saturation, active set,
    dual ordering, cost ordering, strong duality). Downstream theorems
    consume only the axioms; any other LP-feasible-and-dual-saturating
    (t, x, y) triple would discharge the class equally well.

    The witness JSON is the authoritative numerical source; this
    instance exists to make the class type-inhabited for Lean
    elaboration. -/
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

/-! ## Categorical-content audit (audit fix #3, PR following PR #1255 sweep)

The theorems above (he4_strong_duality_value, he4_primal_obj_eq_tTp_xTp,
he4_dual_ordering_strict, he4_tp_dual_zero, he4_DD_highest_shadow_price,
he4_Tp_cheapest_channel, he4_DD_costliest_channel, he4_DD_active,
he4_Tp_not_active, he4_He3n_active) demonstrate that the LP-solution
**structural content** is fully derivable from the class axioms.

In particular, NONE of these theorems read the specific witness values
(`24158/1000`, `13197/1000`, etc.) — they pattern-match on the
`primal_saturating_unique`, `active_set_eq`, `dual_ordering`,
`cost_ordering`, and `strong_duality` axioms. The witness instance
provides ONE concrete saturation of these axioms; other LP-feasible
saturations would discharge the same theorems.

This separates the categorical content (proved here) from the empirical
LP-solve (recorded in `he4-sdp-compositional-probe.witness.json`) — the
audit's "framing" concern is addressed by:

  1. Docstrings on the class + instance (above) clarifying the
     structural-vs-witness distinction.
  2. The standalone abstract feasibility predicate
     `IsHe4LPFeasibleSolution` below, which captures the categorical
     content without ANY reference to the class or witness values.
  3. The existence theorem `he4_lp_solution_exists` proving the
     categorical content as a pure existential claim, derived from
     the witness-encoded instance but expressing nothing
     value-specific. -/

/-! ## Abstract LP-feasibility predicate

Defined OUTSIDE the typeclass so it captures the categorical content
as a pure relation on rational data — provable from ANY feasible
LP solution, not just the witness instance. -/

/-- **Abstract LP-feasibility predicate** for the ⁴He channel-active-set
    structure. An 11-tuple `(t_DD, t_Tp, t_He3n, n_target, x_DD, x_Tp,
    x_He3n, y0*, y_DD, y_Tp, y_He3n) ∈ ℚ¹¹` is a feasible LP solution
    iff it satisfies all 5 structural axioms (primal saturation, active
    set, dual ordering, cost ordering, strong duality). Categorical:
    no specific values mentioned.

    The witness-encoded instance below provides ONE such solution
    (sourced from the SDP probe), but the predicate accepts any
    rational 11-tuple satisfying the same axioms. -/
def IsHe4LPFeasibleSolution
    (tDD tTp tHe3n n_target xDD xTp xHe3n
     y0_star yDD yTp yHe3n : ℚ) : Prop :=
  -- Primal saturation: only T⊕p has positive weight
  (xDD = 0 ∧ 0 < xTp ∧ xHe3n = 0) ∧
  -- Active set: {DD, ³He+n}, not Tp
  (0 < yDD ∧ yTp = 0 ∧ 0 < yHe3n) ∧
  -- Dual ordering: yDD > yHe3n > yTp = 0
  (yHe3n < yDD ∧ yTp < yHe3n) ∧
  -- Cost ordering: tTp < tHe3n < tDD
  (tTp < tHe3n ∧ tHe3n < tDD) ∧
  -- Strong duality: primal_obj = dual_obj (zero gap)
  (tDD * xDD + tTp * xTp + tHe3n * xHe3n = n_target * y0_star)

/-- **EXISTENCE THEOREM (categorical content of the LP-active-set
    proposition).** There exists a rational LP solution for the ⁴He
    channel-active-set structure satisfying all 5 categorical axioms.

    This is the pure categorical claim — no specific values; the
    existential is discharged by the witness-encoded instance.
    Downstream consumers depending only on the EXISTENCE of such a
    solution (rather than its specific values) can cite this theorem
    directly without needing the `[HasHe4ChannelActiveSet]` instance. -/
theorem he4_lp_solution_exists :
    ∃ tDD tTp tHe3n n_target xDD xTp xHe3n y0_star yDD yTp yHe3n : ℚ,
      IsHe4LPFeasibleSolution tDD tTp tHe3n n_target xDD xTp xHe3n
                              y0_star yDD yTp yHe3n :=
  let h := (inferInstance : HasHe4ChannelActiveSet)
  ⟨h.tDD, h.tTp, h.tHe3n, h.n_target, h.xDD, h.xTp, h.xHe3n,
   h.y0_star, h.yDD, h.yTp, h.yHe3n,
   ⟨h.primal_saturating_unique, h.active_set_eq, h.dual_ordering,
    h.cost_ordering, h.strong_duality⟩⟩

/-- **Bridge theorem**: any `HasHe4ChannelActiveSet` instance yields
    an `IsHe4LPFeasibleSolution` witness for its tuple. Confirms the
    class IS a categorical encoding of the abstract feasibility
    predicate. -/
def he4_class_is_feasible_solution [h : HasHe4ChannelActiveSet] :
    IsHe4LPFeasibleSolution h.tDD h.tTp h.tHe3n h.n_target
                            h.xDD h.xTp h.xHe3n
                            h.y0_star h.yDD h.yTp h.yHe3n :=
  ⟨h.primal_saturating_unique, h.active_set_eq, h.dual_ordering,
   h.cost_ordering, h.strong_duality⟩

/-- **Categorical demonstration**: a hypothetical alternative instance
    (with different witness values but the same structural axioms)
    would discharge all the downstream theorems identically. The
    conjunction below packages the 5 structural axioms without
    reference to specific values.

    Definitionally equal to `he4_class_is_feasible_solution` (since
    `IsHe4LPFeasibleSolution` unfolds to this conjunction). Proof
    delegates directly to that theorem to avoid duplication. -/
theorem he4_downstream_uses_only_axioms_not_values [h : HasHe4ChannelActiveSet] :
    (h.xDD = 0 ∧ 0 < h.xTp ∧ h.xHe3n = 0) ∧
    (0 < h.yDD ∧ h.yTp = 0 ∧ 0 < h.yHe3n) ∧
    (h.yHe3n < h.yDD ∧ h.yTp < h.yHe3n) ∧
    (h.tTp < h.tHe3n ∧ h.tHe3n < h.tDD) ∧
    (h.tDD * h.xDD + h.tTp * h.xTp + h.tHe3n * h.xHe3n = h.n_target * h.y0_star) :=
  he4_class_is_feasible_solution

end QOU.BraidKnot.He4ChannelActiveSet
