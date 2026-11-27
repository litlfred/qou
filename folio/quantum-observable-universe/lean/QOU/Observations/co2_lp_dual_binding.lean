import Mathlib.Order.Defs.PartialOrder
import Mathlib.Tactic.NormNum

/-!
# QOU.Molecular.co2_lp_dual_binding

**Proposition (conditional on [`conj:q-integer-mass-formula`])**
([`prop:co2-lp-dual-binding`](../../../quantum-observable-universe/molecular-construction/co2-lp-dual-binding.md)):
*The LP dual of the CO₂ molecular braid selects the symmetric linear
arrangement O=C=O with two double bonds `(k₁, k₂) = (2, 2)` as the
ground state, subject to carbon valence `k₁ + k₂ ≤ 4`; the molecule
uses 66 strands.*

## Disposition (integrity)

All three conjuncts of the resolving declaration are now **derived**;
none is a projected conclusion field (a previous revision carried an
opaque `co2_lp_dual_bound` and `impl_…` fields handing back the
conclusions, and a later revision still returned the `carbon_valence`
and `n_strands_def` fields verbatim in the conjunction — both the
self-assuming-projection shape forbidden by AGENTS.md §3b-cond item 5):

* **(1) Carbon-valence feasibility.** The bond orders of the symmetric
  candidate are *definitional geometry inputs* (`k1_def : k1 = 2`,
  `k2_def : k2 = 2` — a double bond to each oxygen). The valence bound
  `k₁ + k₂ ≤ 4` is **derived** as the arithmetic fact `2 + 2 ≤ 4`
  (`co2_carbon_valence_feasible`) — the LP primal-feasibility check of
  the candidate, mirroring how `computations/lp_dual_solver.py`
  separates feasibility (checkable) from optimality (the dual bound).
* **(2) Strand count.** The per-atom strand counts are definitional
  composition inputs (`strands_C = 6 + 6 + 6` protons/neutrons/
  electrons of carbon, `strands_O = 8 + 8 + 8` of oxygen) and the
  molecular total is *defined* as `strands_C + 2·strands_O`. The claim
  `n_strands = 66` is **derived** by evaluating `18 + 2·24`
  (`co2_strand_count`).
* **(3) Symmetric optimum beats both asymmetric alternatives.**
  Instantiating the §3b-cond ground-state-minimisation *hypothesis* at
  `(3,1)` and `(1,3)` yields `Φ₁(2,2) ≤ Φ₁(3,1)` and
  `Φ₁(2,2) ≤ Φ₁(1,3)` (`co2_symmetric_beats_asymmetric`) — the `.md`'s
  "wins over asymmetric alternatives (3,1) or (1,3)", obtained by
  *using* the quantified hypothesis at two points, not restating it.

The single irreducibly-conjectural input is the **LP-dual ground-state
selection** — the symmetric `(2,2)` configuration minimises `Φ₁` over
the carbon-valence-feasible configurations. It is carried by the
§3b-cond class `Co2SymmetricSelection` as a *quantified hypothesis* the
theorem instantiates, never restated verbatim in the conclusion.

## Base ring (§7c)

`Φ₁` is the LP objective functional on bond configurations and the only thing
done to its values is `≤`; the strand counts and valences are `ℕ`. Nothing is
measured and nothing is archimedean, so the `Φ₁` values live in a generic
ordered `R` (contrast `ch4_lp_dual_binding`, whose `E_bind_CH` is a measured
bond energy and is `ℝ` by meaning). The substrate evaluation is `R := ℝ`. -/

namespace QOU.Molecular

variable {R : Type*} [Preorder R]

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

/-- Data of the CO₂ LP-dual-binding claim. All fields are *inputs*
    (the symmetric candidate's bond orders, the molecular composition,
    and the `Φ₁`-functional); none is a conclusion. -/
class Co2LpDualBindingContext (R : Type*) [Preorder R] where
  /-- Bond order to the first oxygen atom in the symmetric candidate. -/
  k1 : ℕ
  /-- Bond order to the second oxygen atom in the symmetric candidate. -/
  k2 : ℕ
  /-- The symmetric candidate places a double bond to the first oxygen
      (definitional geometry input). -/
  k1_def : k1 = 2
  /-- The symmetric candidate places a double bond to the second oxygen
      (definitional geometry input). -/
  k2_def : k2 = 2
  /-- Strand count contributed by the carbon atom: 6 protons +
      6 neutrons + 6 electrons (definitional composition input). -/
  strands_C : ℕ
  /-- Carbon contributes `6 + 6 + 6 = 18` strands. -/
  strands_C_def : strands_C = 6 + 6 + 6
  /-- Strand count contributed by each oxygen atom: 8 protons +
      8 neutrons + 8 electrons (definitional composition input). -/
  strands_O : ℕ
  /-- Each oxygen contributes `8 + 8 + 8 = 24` strands. -/
  strands_O_def : strands_O = 8 + 8 + 8
  /-- The number of strands in the CO₂ molecular braid. -/
  n_strands : ℕ
  /-- The molecular strand count is the carbon contribution plus two
      oxygen contributions (definitional composition input). -/
  n_strands_def : n_strands = strands_C + 2 * strands_O
  /-- `Φ₁` of each carbon-valence-feasible bond configuration. -/
  Phi1_config : Co2Config → R

/-- §3b-cond conjecture class (non-degenerate per AGENTS.md §3b-cond
    item 5): carries the conjectural LP-dual *hypothesis* — the
    symmetric `(2,2)` configuration is the `Φ₁`-minimiser over all
    carbon-valence-feasible configurations — as a quantified field, NOT
    any conclusion of the theorems below. -/
class Co2SymmetricSelection (ctx : Co2LpDualBindingContext R) : Prop where
  /-- The symmetric configuration minimises `Φ₁` over all feasible
      configurations (the ground-state selection hypothesis). -/
  symmetric_minimises :
    ∀ c : Co2Config, ctx.Phi1_config Co2Config.sym ≤ ctx.Phi1_config c

/-- **Carbon-valence feasibility of the symmetric candidate — derived
    sorry-free.**  The symmetric double-bond configuration satisfies
    carbon's valence constraint: `k₁ + k₂ = 2 + 2 ≤ 4`.  The LP
    primal-feasibility check, computed from the definitional geometry
    inputs — not a projected hypothesis field. -/
-- Ref: [leitner2026] quantum-observable-universe/molecular-construction/co2-lp-dual-binding.md
theorem co2_carbon_valence_feasible (ctx : Co2LpDualBindingContext R) :
    ctx.k1 + ctx.k2 ≤ 4 := by
  norm_num [ctx.k1_def, ctx.k2_def]

/-- **CO₂ strand count — derived sorry-free.**  The molecular braid
    uses `18 + 2·24 = 66` strands, evaluated from the per-atom
    composition inputs — not a projected definitional field. -/
-- Ref: [leitner2026] quantum-observable-universe/molecular-construction/co2-lp-dual-binding.md
theorem co2_strand_count (ctx : Co2LpDualBindingContext R) :
    ctx.n_strands = 66 := by
  norm_num [ctx.n_strands_def, ctx.strands_C_def, ctx.strands_O_def]

/-- **Theorem (conditional on `Co2SymmetricSelection`)** — the symmetric
    double-bond configuration `(2,2)` has `Φ₁` no greater than either
    asymmetric alternative `(3,1)` or `(1,3)`.

    Derived (not projected): instantiate the minimisation *hypothesis*
    at `c = asym31` and `c = asym13`.  New inequalities on `Φ₁` values,
    obtained by using the quantified hypothesis at two points. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP duality, symmetric optimum)
-- Ref: [leitner2026] quantum-observable-universe/molecular-construction/co2-lp-dual-binding.md
theorem co2_symmetric_beats_asymmetric (ctx : Co2LpDualBindingContext R)
    [hc : Co2SymmetricSelection ctx] :
    ctx.Phi1_config Co2Config.sym ≤ ctx.Phi1_config Co2Config.asym31 ∧
    ctx.Phi1_config Co2Config.sym ≤ ctx.Phi1_config Co2Config.asym13 :=
  ⟨hc.symmetric_minimises Co2Config.asym31,
   hc.symmetric_minimises Co2Config.asym13⟩

/-- **Theorem (conditional on `Co2SymmetricSelection`)** — the resolving
    declaration for `lean.ref` `qou:QOU.Molecular.co2_lp_dual_binding`.

    Conjoins (1) the *derived* carbon-valence feasibility
    `k₁ + k₂ ≤ 4` of the symmetric candidate, (2) the *derived* strand
    count `n_strands = 66`, and (3) the *derived*
    symmetric-beats-asymmetric inequalities
    `Φ₁(2,2) ≤ Φ₁(3,1)` and `Φ₁(2,2) ≤ Φ₁(1,3)`.  Every conjunct is
    derived; the conjectural LP-dual selection enters only as the
    quantified `symmetric_minimises` hypothesis. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP duality, symmetric optimum)
-- Ref: [leitner2026] quantum-observable-universe/molecular-construction/co2-lp-dual-binding.md
theorem co2_lp_dual_binding (ctx : Co2LpDualBindingContext R)
    [hc : Co2SymmetricSelection ctx] :
    ctx.k1 + ctx.k2 ≤ 4 ∧
    ctx.n_strands = 66 ∧
    (ctx.Phi1_config Co2Config.sym ≤ ctx.Phi1_config Co2Config.asym31 ∧
     ctx.Phi1_config Co2Config.sym ≤ ctx.Phi1_config Co2Config.asym13) :=
  ⟨co2_carbon_valence_feasible ctx, co2_strand_count ctx,
   co2_symmetric_beats_asymmetric ctx⟩

end QOU.Molecular
