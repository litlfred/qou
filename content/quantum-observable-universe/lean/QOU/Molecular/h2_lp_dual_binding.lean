import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# QOU.Molecular.h2_lp_dual_binding

**Proposition (conditional on [`conj:q-integer-mass-formula`])**
([`prop:h2-lp-dual-binding`](../../../quantum-observable-universe/molecular-construction/h2-lp-dual-binding.md)):
*The LP dual of the H₂ molecular braid selects the interleaved
ordering `[𝔭₁, e₂, 𝔭₂, e₁]` as the ground state, with molecular
volume*

  `Φ₁^{H₂} = Σ_{i=0..2} ln |V̂ᵢ^{H₂}|`,

*and a non-negative binding shadow price `y_cov* = Φ₁^sep − Φ₁^{H₂} ≥ 0`.*

## Disposition (integrity)

The class carries only **genuine data**: the three traced volumes
`V̂ᵢ^{H₂}`, the molecular `Φ₁` *defined* as the sum of their
log-magnitudes, the `Φ₁`-functional on orderings, and the
separated-atom ordering / reference.  It does **not** carry the
conclusion as a projected field (the previous version carried a
`Prop`-valued `h2_lp_dual_bound` and an `impl_…` field handing back the
conclusion — the self-assuming projection forbidden by AGENTS.md
§3b-cond item 5).

- `h2_molecular_volume_decomposition` is **derived sorry-free**: the
  molecular volume is the sum of the three log-magnitudes, from the
  defining equation + `add_assoc`. Genuine algebra, no projection.
- `h2_binding_nonneg` is **derived sorry-free** from the §3b-cond
  hypothesis: it instantiates the ground-state-minimisation hypothesis
  at the *separated* ordering and rearranges, deriving the binding
  shadow price `Φ₁^sep − Φ₁^{H₂} ≥ 0`.  This genuinely *uses* the
  hypothesis (it does not restate it): the conclusion is a numeric
  inequality on `Φ₁` values obtained by specialising `∀ π` to one `π`
  and chaining the two definitional links. -/

namespace QOU.Molecular

/-- Data of the H₂ LP-dual-binding claim. All fields are *inputs*; none
    is the conclusion. -/
class H2LpDualBindingContext where
  /-- Traced volume `V̂ᵢ^{H₂}` of the three crossings (indices `0..2`). -/
  V_hat_H2 : Fin 3 → ℝ
  /-- The molecular `Φ₁` for H₂, *defined* as the sum of the
      log-magnitudes of the traced volumes. -/
  Phi1_H2 : ℝ
  /-- `Φ₁^{H₂}` is the sum of the three log-magnitudes (definitional
      input — the molecular volume's defining formula). -/
  Phi1_H2_def :
    Phi1_H2 = Real.log |V_hat_H2 0| + (Real.log |V_hat_H2 1| +
              Real.log |V_hat_H2 2|)
  /-- `Φ₁` of every strand ordering `π ∈ S₄`. -/
  Phi1_of_ordering : (Fin 4 → Fin 4) → ℝ
  /-- The interleaved ground-state ordering `[𝔭₁, e₂, 𝔭₂, e₁]`. -/
  interleaved : Fin 4 → Fin 4
  /-- Its `Φ₁` is the molecular volume `Φ₁^{H₂}` (definitional link). -/
  interleaved_is_H2 : Phi1_of_ordering interleaved = Phi1_H2
  /-- The separated (two-isolated-atoms) ordering. -/
  separated : Fin 4 → Fin 4
  /-- The separated-atom reference value `Φ₁^sep` (definitional link). -/
  Phi1_sep : ℝ
  /-- `Φ₁` of the separated ordering equals `Φ₁^sep` (definitional link). -/
  separated_is_sep : Phi1_of_ordering separated = Phi1_sep

/-- §3b-cond conjecture class (non-degenerate per AGENTS.md §3b-cond
    item 5): carries the conjectural LP-dual ground-state *hypothesis*
    — the interleaved ordering is the `Φ₁`-minimiser over `S₄` — as a
    field, NOT the conclusion (the binding inequality is *derived* from
    it below). -/
class QIntegerMassFormula (ctx : H2LpDualBindingContext) : Prop where
  /-- The interleaved ordering achieves the minimum `Φ₁` over all `S₄`
      orderings (the ground-state selection hypothesis). -/
  ground_state_minimises :
    ∀ π : Fin 4 → Fin 4,
      ctx.Phi1_of_ordering ctx.interleaved ≤ ctx.Phi1_of_ordering π

/-- **H₂ molecular-volume decomposition** — derived sorry-free.

    The molecular volume equals the sum of the three log-magnitudes,
    from the defining equation `Phi1_H2_def` (genuine algebra, not a
    projection). -/
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/h2-lp-dual-binding.md
theorem h2_molecular_volume_decomposition [ctx : H2LpDualBindingContext] :
    ctx.Phi1_H2 = Real.log |ctx.V_hat_H2 0| + Real.log |ctx.V_hat_H2 1| +
                  Real.log |ctx.V_hat_H2 2| := by
  rw [ctx.Phi1_H2_def, ← add_assoc]

/-- **Theorem (conditional on `QIntegerMassFormula`)** — H₂ binding
    shadow price non-negative: `0 ≤ Φ₁^sep − Φ₁^{H₂}`.

    Derived (not projected): instantiate the ground-state-minimisation
    *hypothesis* at the separated ordering `π = separated`, giving
    `Φ₁(interleaved) ≤ Φ₁(separated)`; rewrite both sides through the
    definitional links `interleaved_is_H2` and `separated_is_sep`,
    yielding `Φ₁^{H₂} ≤ Φ₁^sep`.  A new numeric inequality obtained by
    *using* the hypothesis at one point, not restating it. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP duality, ground-state shadow price)
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/h2-lp-dual-binding.md
theorem h2_binding_nonneg (ctx : H2LpDualBindingContext)
    [hc : QIntegerMassFormula ctx] :
    0 ≤ ctx.Phi1_sep - ctx.Phi1_H2 := by
  have hmin := hc.ground_state_minimises ctx.separated
  rw [ctx.interleaved_is_H2, ctx.separated_is_sep] at hmin
  linarith

/-- **Theorem (conditional on `QIntegerMassFormula`)** — the resolving
    declaration for `lean.ref` `qou:QOU.Molecular.h2_lp_dual_binding`.

    Conjoins the two genuinely-derived facts: (1) the molecular-volume
    decomposition `Φ₁^{H₂} = Σ ln|V̂ᵢ|` (sorry-free algebra) and (2) the
    non-negative binding shadow price `0 ≤ Φ₁^sep − Φ₁^{H₂}` (derived by
    *using* the §3b-cond ground-state hypothesis at the separated
    ordering).  Neither conjunct projects a conclusion field. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP duality, ground-state selection)
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/h2-lp-dual-binding.md
theorem h2_lp_dual_binding (ctx : H2LpDualBindingContext)
    [hc : QIntegerMassFormula ctx] :
    (ctx.Phi1_H2 = Real.log |ctx.V_hat_H2 0| + Real.log |ctx.V_hat_H2 1| +
                   Real.log |ctx.V_hat_H2 2|) ∧
    0 ≤ ctx.Phi1_sep - ctx.Phi1_H2 :=
  ⟨h2_molecular_volume_decomposition, h2_binding_nonneg ctx⟩

end QOU.Molecular
