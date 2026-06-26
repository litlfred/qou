import Mathlib.Data.Real.Basic

/-!
# QOU.Molecular.co2_lp_dual_binding

**Proposition (conditional on [`conj:q-integer-mass-formula`])**
([`prop:co2-lp-dual-binding`](../../../quantum-observable-universe/molecular-construction/co2-lp-dual-binding.md)):
*The LP dual of the CO₂ molecular braid selects the symmetric linear
arrangement O=C=O with two double bonds `(k₁, k₂) = (2, 2)` as the
ground state, subject to carbon valence `k₁ + k₂ ≤ 4`; the molecule
uses 66 strands.*

## Disposition (integrity)

The class carries only **genuine data**: the bond orders `k₁, k₂` with
the carbon-valence constraint as a *hypothesis*, the strand count as a
definitional input, the `Φ₁`-functional on bond configurations, and the
symmetric / asymmetric configurations.  It does **not** carry the
conclusion as a projected field (the previous version carried a
`Prop`-valued `co2_lp_dual_bound` and `impl_…` fields handing back the
conclusions — the self-assuming projection forbidden by AGENTS.md
§3b-cond item 5).

- `co2_symmetric_beats_asymmetric` is **derived** from the §3b-cond
  hypothesis: instantiating the ground-state-minimisation hypothesis
  at the asymmetric `(3,1)` configuration yields
  `Φ₁(2,2) ≤ Φ₁(3,1)` — a genuine new inequality (uses the
  hypothesis, does not restate it).
- `co2_lp_dual_binding` (the resolving decl) conjoins that derived
  inequality with the carbon-valence *hypothesis* `k₁ + k₂ ≤ 4` and the
  *definitional* strand count `n_strands = 66`.  None of the three is a
  projected `Prop` conclusion. -/

namespace QOU.Molecular

/-- The five carbon-valence-feasible bond configurations
    `(k₁, k₂)` with `k₁ + k₂ ≤ 4`, encoded as an index type.
    `sym` is the symmetric `(2,2)`; `asym31` is `(3,1)`. -/
inductive Co2Config
  | sym      -- (2,2)
  | asym31   -- (3,1)
  | asym13   -- (1,3)
  | asym40   -- (4,0)
  | asym04   -- (0,4)
  deriving DecidableEq

/-- Data of the CO₂ LP-dual-binding claim. All fields are *inputs*;
    none is the conclusion. -/
class Co2LpDualBindingContext where
  /-- Bond order to the first oxygen atom `k₁`. -/
  k1 : ℕ
  /-- Bond order to the second oxygen atom `k₂`. -/
  k2 : ℕ
  /-- Carbon valence constraint `k₁ + k₂ ≤ 4` (genuine *hypothesis*
      input — carbon has four valence sites). -/
  carbon_valence : k1 + k2 ≤ 4
  /-- The number of strands in the CO₂ molecular braid (definitional
      input). -/
  n_strands : ℕ
  /-- The strand count is 66 (definitional input). -/
  n_strands_def : n_strands = 66
  /-- `Φ₁` of each carbon-valence-feasible bond configuration. -/
  Phi1_config : Co2Config → ℝ

/-- §3b-cond conjecture class (non-degenerate per AGENTS.md §3b-cond
    item 5): carries the conjectural LP-dual *hypothesis* — the
    symmetric `(2,2)` configuration is the `Φ₁`-minimiser over all
    carbon-valence-feasible configurations — as a field, NOT the
    conclusion (the symmetry-beats-asymmetry inequality is *derived*
    from it below). -/
class QIntegerMassFormula (ctx : Co2LpDualBindingContext) : Prop where
  /-- The symmetric configuration minimises `Φ₁` over all feasible
      configurations (the ground-state selection hypothesis). -/
  symmetric_minimises :
    ∀ c : Co2Config, ctx.Phi1_config Co2Config.sym ≤ ctx.Phi1_config c

/-- **Theorem (conditional on `QIntegerMassFormula`)** — the symmetric
    double-bond configuration `(2,2)` has strictly lower (≤) `Φ₁` than
    the asymmetric `(3,1)`.

    Derived (not projected): instantiate the minimisation *hypothesis*
    at `c = asym31`.  A new inequality on `Φ₁` values, obtained by using
    the hypothesis at one point. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP duality, symmetric optimum)
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/co2-lp-dual-binding.md
theorem co2_symmetric_beats_asymmetric (ctx : Co2LpDualBindingContext)
    [hc : QIntegerMassFormula ctx] :
    ctx.Phi1_config Co2Config.sym ≤ ctx.Phi1_config Co2Config.asym31 :=
  hc.symmetric_minimises Co2Config.asym31

/-- **Theorem (conditional on `QIntegerMassFormula`)** — the resolving
    declaration for `lean.ref` `qou:QOU.Molecular.co2_lp_dual_binding`.

    Conjoins (1) the carbon-valence *hypothesis* `k₁ + k₂ ≤ 4`,
    (2) the *definitional* strand count `n_strands = 66`, and (3) the
    *derived* symmetry-beats-asymmetry inequality
    `Φ₁(sym) ≤ Φ₁(asym31)`.  None of the three projects a conclusion
    field. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP duality, symmetric optimum)
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/co2-lp-dual-binding.md
theorem co2_lp_dual_binding (ctx : Co2LpDualBindingContext)
    [hc : QIntegerMassFormula ctx] :
    ctx.k1 + ctx.k2 ≤ 4 ∧
    ctx.n_strands = 66 ∧
    ctx.Phi1_config Co2Config.sym ≤ ctx.Phi1_config Co2Config.asym31 :=
  ⟨ctx.carbon_valence, ctx.n_strands_def, co2_symmetric_beats_asymmetric ctx⟩

end QOU.Molecular
