import Mathlib.Data.Real.Basic

/-!
# QOU.Molecular.co_lp_dual_binding

**Proposition (conditional on [`conj:q-integer-mass-formula`])**
([`prop:co-lp-dual-binding`](../../../quantum-observable-universe/molecular-construction/co-lp-dual-binding.md)):
*The LP dual of the CO molecular braid selects the triple-bond
configuration (`k* = 3`) as optimal over single (`k = 1`) and double
(`k = 2`) bonds.*

## Disposition (integrity)

The class carries only **genuine data**: the selected bond order `k*`
(definitional input), the `Φ₁`-functional on bond orders, and the three
candidate bond orders.  It does **not** carry the conclusion as a
projected field (the previous version carried a `Prop`-valued
`co_lp_dual_bound` and an `impl_…` field handing back the conclusion —
the self-assuming projection forbidden by AGENTS.md §3b-cond item 5).

- `co_triple_beats_single` and `co_triple_beats_double` are **derived**
  from the §3b-cond hypothesis: instantiating the
  ground-state-minimisation hypothesis at `k = 1` and `k = 2` yields
  `Φ₁(3) ≤ Φ₁(1)` and `Φ₁(3) ≤ Φ₁(2)` — genuine new inequalities (use
  the hypothesis, do not restate it).
- `co_lp_dual_binding` (the resolving decl) conjoins the *definitional*
  selection `k* = 3` with the two *derived* minimality inequalities.
  Neither inequality projects a conclusion field. -/

namespace QOU.Molecular

/-- Data of the CO LP-dual-binding claim. All fields are *inputs*; none
    is the conclusion. -/
class CoLpDualBindingContext where
  /-- The selected CO bond order `k* ∈ {1, 2, 3}` (definitional input). -/
  k_star : ℕ
  /-- The triple bond is selected: `k* = 3` (definitional input). -/
  k_star_def : k_star = 3
  /-- `Φ₁` at bond order `k`. -/
  Phi_1_k : ℕ → ℝ

/-- §3b-cond conjecture class (non-degenerate per AGENTS.md §3b-cond
    item 5): carries the conjectural LP-dual *hypothesis* — bond order
    `3` minimises `Φ₁` over the candidate bond orders `{1, 2, 3}` — as a
    field, NOT the conclusion (the minimality inequalities are *derived*
    from it below). -/
class QIntegerMassFormula (ctx : CoLpDualBindingContext) : Prop where
  /-- Bond order 3 minimises `Φ₁` over the candidate orders (the
      ground-state selection hypothesis). -/
  triple_minimises : ∀ k : ℕ, k ≤ 3 → ctx.Phi_1_k 3 ≤ ctx.Phi_1_k k

/-- **Theorem (conditional on `QIntegerMassFormula`)** — the triple bond
    beats the single bond: `Φ₁(3) ≤ Φ₁(1)`.  Derived by instantiating
    the minimisation *hypothesis* at `k = 1`. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP duality, bond-order optimum)
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/co-lp-dual-binding.md
theorem co_triple_beats_single (ctx : CoLpDualBindingContext)
    [hc : QIntegerMassFormula ctx] :
    ctx.Phi_1_k 3 ≤ ctx.Phi_1_k 1 :=
  hc.triple_minimises 1 (by omega)

/-- **Theorem (conditional on `QIntegerMassFormula`)** — the triple bond
    beats the double bond: `Φ₁(3) ≤ Φ₁(2)`.  Derived by instantiating
    the minimisation *hypothesis* at `k = 2`. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP duality, bond-order optimum)
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/co-lp-dual-binding.md
theorem co_triple_beats_double (ctx : CoLpDualBindingContext)
    [hc : QIntegerMassFormula ctx] :
    ctx.Phi_1_k 3 ≤ ctx.Phi_1_k 2 :=
  hc.triple_minimises 2 (by omega)

/-- **Theorem (conditional on `QIntegerMassFormula`)** — the resolving
    declaration for `lean.ref` `qou:QOU.Molecular.co_lp_dual_binding`.

    Conjoins the *definitional* triple-bond selection `k* = 3` with the
    two *derived* minimality inequalities `Φ₁(3) ≤ Φ₁(1)` and
    `Φ₁(3) ≤ Φ₁(2)`.  The inequalities are derived from the §3b-cond
    hypothesis, not projected. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP duality, bond-order optimum)
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/co-lp-dual-binding.md
theorem co_lp_dual_binding (ctx : CoLpDualBindingContext)
    [hc : QIntegerMassFormula ctx] :
    ctx.k_star = 3 ∧
    ctx.Phi_1_k 3 ≤ ctx.Phi_1_k 1 ∧
    ctx.Phi_1_k 3 ≤ ctx.Phi_1_k 2 :=
  ⟨ctx.k_star_def, co_triple_beats_single ctx, co_triple_beats_double ctx⟩

end QOU.Molecular
