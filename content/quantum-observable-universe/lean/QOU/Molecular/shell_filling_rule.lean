import Mathlib.Tactic

/-!
# QOU.Molecular.shell_filling_rule

Canonical Lean for content block
[`prop:shell-filling-rule`](../../../quantum-observable-universe/molecular-construction/shell-filling-rule.md):
*Shell filling minimises $\Phi_1$ (aufbau from LP dual)*.

## Disposition (2026-07-03, bean qsb2 — restructured from a projection stub)

The previous encoding was the exact `holds : Prop` + `impl_*`
anti-pattern: the class carried an opaque `aufbau_holds : Prop`, an
instance `aufbau_active : aufbau_holds`, and three `impl_*` fields
handing back each conclusion, which the "theorem" merely projected —
the self-assuming projection forbidden by AGENTS.md §3b-cond item 5.
Restructured per §1a honest dispositions:

- The class now carries only **genuine data**: the ground-state shell
  occupancy, the shell capacity with its defining formula
  `capacity n = 2n²` ([`def:electron-shell-braid-capacity`]), the Pauli
  bound `occupancy ≤ capacity` (a structural hypothesis), the type of
  admissible valence configurations with the ground state and the
  singly-occupied-site count, and the LP primal/dual data
  (`primal_obj`, `y_0`).  The `aufbau_holds` / `aufbau_active` /
  `impl_*` fields are gone.
- **Derived sorry-free** (`shell_filling_pauli_bound`): the concrete
  occupancy bound `occupancy n ≤ 2n²`, from the Pauli hypothesis and
  the capacity formula — genuine (if small) algebra, not a projection.
- **Stated with honest `sorry` + citation** (stated, not yet proved):
  - claim (i) `shell_filling_inner_shells` — inner shells `n < n_val`
    fill completely (needs the `Φ₁`-monotonicity argument: an inner
    vacancy reduces `Φ₁` more than any valence electron);
  - claim (ii) `shell_filling_hund_rule` — the ground state maximises
    singly-occupied valence sites (needs the `ee`-crossing `Φ₁`
    comparison for parallel vs antiparallel trefoil pairs);
  - claim (iii) `shell_filling_lp_strong_duality` — the optimal LP
    primal objective equals the dual objective `Z·y₀` (LP strong
    duality for the electron assignment problem).
-/

namespace QOU.Molecular

/-- Data of the shell-filling claim for atom `(Z, N)`.  All fields are
    *inputs* (model data, defining formulas, and the Pauli structural
    hypothesis); none carries a conclusion of the proposition. -/
class ShellFillingRuleContext where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- The valence shell index `n_val`. -/
  n_val : ℕ
  /-- Ground-state occupation count at shell `n` (the `Φ₁`-minimising
      assignment of the `Z` electron trefoils). -/
  occupancy : ℕ → ℕ
  /-- Maximum capacity of shell `n`. -/
  capacity : ℕ → ℕ
  /-- Defining formula `capacity n = 2n²`
      ([`def:electron-shell-braid-capacity`]). -/
  capacity_def : ∀ n : ℕ, capacity n = 2 * n ^ 2
  /-- Pauli constraint (structural hypothesis): no shell is occupied
      beyond its braid capacity. -/
  occupancy_le_capacity : ∀ n : ℕ, occupancy n ≤ capacity n
  /-- Admissible valence-shell configurations of the atom. -/
  ValenceConfig : Type
  /-- The ground-state valence configuration. -/
  ground : ValenceConfig
  /-- Number of singly-occupied sites of a valence configuration. -/
  singly : ValenceConfig → ℕ
  /-- LP dual variable `y₀` (electron chemical potential). -/
  y_0 : ℝ
  /-- Optimal primal objective of the electron assignment LP (the
      minimal total `Φ₁`). -/
  primal_obj : ℝ

/-- **Pauli occupancy bound — derived sorry-free.**  Every shell obeys
    `occupancy n ≤ 2n²`, from the Pauli hypothesis and the defining
    capacity formula (genuine algebra, not a projection). -/
theorem shell_filling_pauli_bound [ctx : ShellFillingRuleContext]
    (n : ℕ) : ctx.occupancy n ≤ 2 * n ^ 2 := by
  have h := ctx.occupancy_le_capacity n
  rwa [ctx.capacity_def n] at h

/-- **Claim (i), aufbau — stated, not yet proved.**  Inner shells
    (`n < n_val`) fill completely in the ground state: each additional
    electron in a partly filled inner shell reduces `Φ₁` more than any
    valence electron.  The `Φ₁`-monotonicity argument is not yet
    formalised. -/
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/shell-filling-rule.md
theorem shell_filling_inner_shells [ctx : ShellFillingRuleContext] :
    ∀ n : ℕ, n < ctx.n_val → ctx.occupancy n = ctx.capacity n := by
  sorry

/-- **Claim (ii), Hund's rule — stated, not yet proved.**  Within the
    valence shell the ground state maximises the number of singly
    occupied sites: parallel electron trefoils have lower `Φ₁` than
    antiparallel pairs, since the repulsive `ee` crossing (`σ`) is
    minimised on distinct spatial sites.  The `Φ₁` comparison is not
    yet formalised. -/
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/shell-filling-rule.md
theorem shell_filling_hund_rule [ctx : ShellFillingRuleContext] :
    ∀ c : ctx.ValenceConfig, ctx.singly c ≤ ctx.singly ctx.ground := by
  sorry

/-- **Claim (iii), LP strong duality — stated, not yet proved.**  The
    optimal primal objective of the electron assignment LP equals the
    dual objective `Z·y₀` (`max_y Z·y₀` s.t.
    `y₀ + Σ_n G_{n,s}·y_{n,s} ≤ Φ₁^{(s)}` for all sites `s`).  Strong
    duality for this LP is not yet formalised. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP strong duality)
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/shell-filling-rule.md
theorem shell_filling_lp_strong_duality [ctx : ShellFillingRuleContext] :
    ctx.primal_obj = (ctx.Z : ℝ) * ctx.y_0 := by
  sorry

/-- **Proposition** ([`prop:shell-filling-rule`]) — resolving
    declaration for the `lean.ref` URI
    `qou:QOU.Molecular.shell_filling_rule`.

    Conjoins the three claims of the aufbau proposition: (i) inner
    shells fill completely, (ii) Hund's rule (the ground state
    maximises singly-occupied valence sites), (iii) the LP dual
    objective equals `Z·y₀`.  Each conjunct is a real statement over
    the model data; the unproved ones carry honest `sorry`s in their
    named sub-theorems (see module docstring), not projected
    conclusion fields. -/
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/shell-filling-rule.md
theorem shell_filling_rule [ctx : ShellFillingRuleContext] :
    (∀ n : ℕ, n < ctx.n_val → ctx.occupancy n = ctx.capacity n) ∧
    (∀ c : ctx.ValenceConfig, ctx.singly c ≤ ctx.singly ctx.ground) ∧
    ctx.primal_obj = (ctx.Z : ℝ) * ctx.y_0 :=
  ⟨shell_filling_inner_shells, shell_filling_hund_rule,
   shell_filling_lp_strong_duality⟩

end QOU.Molecular
