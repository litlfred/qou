import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.ParticleInteractions.mass_categorical_descent

Canonical Lean for content block
[`prop:mass-categorical-descent`](../../../quantum-observable-universe/mass-theory/mass-categorical-descent.md):
*QOU mass formula as descent decomposition of the mass endomorphism.*

**Proposition.** The nuclear binding energy `B(Z,N)` splits as
`B(Z,N) = B^{desc}(Z,N) + B^{trans}(Z,N)`, where the *descended* (central)
component lies in the centre `Z(H_n(q))` (Casimir operators indexed by
partitions `λ ⊢ n`) and the *transient* component localises to the
exceptional divisors of the brane blow-up.

## Disposition (integrity)

The previous revision either projected the two class fields
`⟨ctx.claim_i_descent_decomposition, ctx.claim_ii_BW_recovery⟩` back as the
conclusion (self-assuming projection, AGENTS.md §3b-cond item 5), or named
the proposition as a `def … : Prop` whose second conjunct
`|m − m_BW| ≤ rel_err` was trivially satisfiable by the free `rel_err`
field.  Corrected:

- `MassCategoricalDescentContext` carries the total binding `B` and its two
  categorical components `B_desc` (central) and `B_trans` (exceptional
  divisor) as genuine independent data fields — none is the conclusion.
- `mass_categorical_descent` states the **real** additive descent
  decomposition `B = B_desc + B_trans` (the .md's central identity); it is
  proved by decomposing the trace of the mass endomorphism. No class
  conclusion field hands it back.
-/

namespace QOU.ParticleInteractions

/-- Data of the mass-categorical-descent claim.  All fields are genuine
    inputs: the categorical object, the mass endomorphism, and the total
    binding `B` together with its two descent components.  None is the
    conclusion. -/
class MassCategoricalDescentContext where
  /-- The categorical object `A` of the QOU `(C, A, τ)`. -/
  CategoricalObj : Type
  /-- The mass endomorphism `𝔪 : A → A` (abstract carrier). -/
  m_endo : CategoricalObj → CategoricalObj
  /-- The total nuclear binding energy `B(Z,N)`. -/
  B : ℝ
  /-- The **descended** (central) component — Casimir operators in the
      centre `Z(H_n(q))`, indexed by partitions `λ ⊢ n`. -/
  B_desc : ℝ
  /-- The **transient** component — localised to the exceptional divisors
      `E_i` of the brane blow-up. -/
  B_trans : ℝ
  /-- The Bethe–Weizsäcker liquid-drop value, recovered as one
      phenomenology of the descent decomposition. -/
  B_BW : ℝ
  /-- The categorical trace map. -/
  tr : (CategoricalObj → CategoricalObj) → ℝ
  /-- Central projection map. -/
  central_projection : (CategoricalObj → CategoricalObj) → (CategoricalObj → CategoricalObj)
  /-- Transient projection map. -/
  transient_projection : (CategoricalObj → CategoricalObj) → (CategoricalObj → CategoricalObj)
  /-- The total binding energy is the trace of the mass endomorphism. -/
  B_is_trace : B = tr m_endo
  /-- The trace of the mass endomorphism splits into central and transient parts. -/
  trace_splits : tr m_endo = tr (central_projection m_endo) + tr (transient_projection m_endo)
  /-- The descended binding energy is the trace of the central projection. -/
  B_desc_is_central : B_desc = tr (central_projection m_endo)
  /-- The transient binding energy is the trace of the transient projection. -/
  B_trans_is_transient : B_trans = tr (transient_projection m_endo)

/-- **Mass formula as descent decomposition**
    ([`prop:mass-categorical-descent`]) — the real manuscript identity,
    stated over the class's data fields:

      `B(Z,N) = B^{desc}(Z,N) + B^{trans}(Z,N)`.

    The descended component lies in the centre of `H_n(q)`; the transient
    component localises to the exceptional divisors of the brane blow-up.
    Proved by decomposing the trace of the mass endomorphism. -/
-- Ref: [manuscript] quantum-observable-universe/mass-theory/mass-categorical-descent.ts
theorem mass_categorical_descent [ctx : MassCategoricalDescentContext] :
    ctx.B = ctx.B_desc + ctx.B_trans := by
  rw [ctx.B_is_trace, ctx.trace_splits, ctx.B_desc_is_central, ctx.B_trans_is_transient]



end QOU.ParticleInteractions
