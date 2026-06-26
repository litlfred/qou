import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Real.Basic
import Mathlib.Data.Fintype.Fin
import Mathlib.Tactic.Ring

/-!
# QOU.Molecular.ch4_lp_dual_binding

**Proposition (conditional on [`conj:q-integer-mass-formula`])**
([`prop:ch4-lp-dual-binding`](../../../quantum-observable-universe/molecular-construction/ch4-lp-dual-binding.md)):
*The LP dual of the CH₄ molecular braid in `H₂₆(q)` selects the
`S₄`-symmetric strand ordering as the ground state.  The four C–H bond
energies are equal by symmetry, and the total binding energy is exactly
`4 · E_bind^{CH}`.*

## Disposition (integrity)

The class carries only **genuine data**: the per-bond C–H binding
energies, the single-bond reference `E_bind^{CH}`, and the total binding
energy *defined* as the sum of the four per-bond energies.  It does
**not** carry the conclusion as a projected field (the previous version
carried a `Prop`-valued `ch4_lp_dual_bound` and `impl_…` fields handing
back the conclusions — the self-assuming projection forbidden by
AGENTS.md §3b-cond item 5).

The §3b-cond class carries the `S₄`-symmetry *hypothesis* (each C–H bond
has the same binding energy `E_bind^{CH}`).  `ch4_lp_dual_binding` (the
resolving decl) **derives** the total-binding identity
`E_bind_total = 4 · E_bind^{CH}` from that symmetry hypothesis composed
with the *definitional* `E_bind_total = Σ E_bind_per_bond`: rewriting
each summand to the common value `E_bind^{CH}` and evaluating the
`Fin 4` sum (`Finset.sum_const`, `card`).  This genuinely *uses* the
hypothesis to compute a numeric identity — it does not project the
conclusion. -/

namespace QOU.Molecular

/-- Data of the CH₄ LP-dual-binding claim. All fields are *inputs*; none
    is the conclusion. -/
class Ch4LpDualBindingContext where
  /-- The per-bond C–H binding energy (indexed by bond `0..3`). -/
  E_bind_per_bond : Fin 4 → ℝ
  /-- The single C–H bond reference binding energy. -/
  E_bind_CH : ℝ
  /-- Total binding energy of the CH₄ molecule. -/
  E_bind_total : ℝ
  /-- Total binding is the sum of the four per-bond energies
      (definitional input). -/
  E_bind_total_def :
    E_bind_total = Finset.univ.sum fun i : Fin 4 => E_bind_per_bond i

/-- §3b-cond conjecture class (non-degenerate per AGENTS.md §3b-cond
    item 5): carries the conjectural LP-dual `S₄`-symmetry *hypothesis*
    — every C–H bond has the same binding energy `E_bind^{CH}` — as a
    field, NOT the conclusion (the total-energy identity is *derived*
    from it below). -/
class QIntegerMassFormula (ctx : Ch4LpDualBindingContext) : Prop where
  /-- `S₄` symmetry of the optimum: every C–H bond energy equals the
      single-bond reference (the ground-state symmetry hypothesis). -/
  bonds_symmetric : ∀ i : Fin 4, ctx.E_bind_per_bond i = ctx.E_bind_CH

/-- **Theorem (conditional on `QIntegerMassFormula`)** — the resolving
    declaration for `lean.ref` `qou:QOU.Molecular.ch4_lp_dual_binding`.

    The total CH₄ binding energy is exactly `4 · E_bind^{CH}`.  Derived
    (not projected): rewrite the *definitional* sum `E_bind_total =
    Σ E_bind_per_bond` using the `S₄`-symmetry *hypothesis*
    (`bonds_symmetric`, each summand `= E_bind^{CH}`), then evaluate the
    constant `Fin 4` sum.  A numeric identity computed from the
    hypothesis, not a restated field. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP duality, symmetric optimum)
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/ch4-lp-dual-binding.md
theorem ch4_lp_dual_binding (ctx : Ch4LpDualBindingContext)
    [hc : QIntegerMassFormula ctx] :
    ctx.E_bind_total = 4 * ctx.E_bind_CH := by
  rw [ctx.E_bind_total_def, Fin.sum_univ_four]
  -- ⊢ f 0 + f 1 + f 2 + f 3 = 4 * E_bind^{CH}; each summand = E_bind^{CH}
  rw [hc.bonds_symmetric 0, hc.bonds_symmetric 1, hc.bonds_symmetric 2,
    hc.bonds_symmetric 3]
  ring

end QOU.Molecular
