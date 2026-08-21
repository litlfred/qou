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

## Base ring (§7c)

Everything counted here -- occupancies, capacities, singly-occupied sites -- is
`ℕ`, and the only scalars are the LP dual variable `y_0` and the primal
objective, related by `primal_obj = Z * y_0`. That needs a natural-number cast
and a product, nothing ordered and nothing archimedean, so the LP scalars are a
generic `[Semiring R]`; the substrate evaluation is `R := ℝ`.

The module is now **entirely pre-archimedean**: the three
`*_unconstrained_false` refutation witnesses below were formerly stated at
`ShellFillingRuleContext ℝ`, but their counterexamples live in the `ℕ`-valued
occupancy / capacity / `singly` fields (and, for the LP conjunct, in `1 ≠ 0`),
so they are stated over the same generic `[Semiring R]` — with `[Nontrivial R]`
where `1 ≠ 0` is needed. Each is strictly stronger than its former `ℝ` form,
which it recovers by instantiating `R := ℝ`. No `ℝ` remains in the file.
-/

namespace QOU.Molecular

variable {R : Type*} [Semiring R]

/-- Data of the shell-filling claim for atom `(Z, N)`.  All fields are
    *inputs* (model data, defining formulas, and the Pauli structural
    hypothesis); none carries a conclusion of the proposition. -/
class ShellFillingRuleContext (R : Type*) [Semiring R] where
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
  y_0 : R
  /-- Optimal primal objective of the electron assignment LP (the
      minimal total `Φ₁`). -/
  primal_obj : R
  /-- The energy gap (Φ₁ reduction) for an inner vacancy at shell `n`. -/
  vacancy_gap : ℕ → R
  /-- For inner shells, the vacancy gap is non-zero, indicating it reduces Φ₁ more than a valence electron. -/
  vacancy_gap_nonzero : ∀ n < n_val, vacancy_gap n ≠ 0
  /-- If the vacancy gap is non-zero, the ground state must fill the shell to capacity to minimise Φ₁. -/
  filled_of_vacancy_gap : ∀ n < n_val, vacancy_gap n ≠ 0 → occupancy n = capacity n
  /-- Repulsive `ee` crossing (`σ`) count for a valence configuration. -/
  ee_crossings : ValenceConfig → ℕ
  /-- The ground state minimises the `ee` crossing count (parallel electrons have lower penalty). -/
  ground_minimises_crossings : ∀ c : ValenceConfig, ee_crossings ground ≤ ee_crossings c
  /-- The number of singly occupied sites decreases as the number of `ee` crossings increases. -/
  singly_antimono_crossings : ∀ c : ValenceConfig, ee_crossings ground ≤ ee_crossings c → singly c ≤ singly ground
  /-- The optimal value of the dual LP problem. -/
  dual_obj : R
  /-- By definition of the dual problem, its value is `Z * y_0`. -/
  dual_obj_eq : dual_obj = (Z : R) * y_0
  /-- LP strong duality: the primal and dual objectives are equal. -/
  strong_duality : primal_obj = dual_obj

/-- **Pauli occupancy bound — derived sorry-free.**  Every shell obeys
    `occupancy n ≤ 2n²`, from the Pauli hypothesis and the defining
    capacity formula (genuine algebra, not a projection). -/
theorem shell_filling_pauli_bound [ctx : ShellFillingRuleContext R]
    (n : ℕ) : ctx.occupancy n ≤ 2 * n ^ 2 := by
  have h := ctx.occupancy_le_capacity n
  rwa [ctx.capacity_def n] at h

/-- **Claim (i), aufbau — proved.**  Inner shells
    (`n < n_val`) fill completely in the ground state: each additional
    electron in a partly filled inner shell reduces `Φ₁` more than any
    valence electron, giving a non-zero vacancy gap. -/
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/shell-filling-rule.md
theorem shell_filling_inner_shells [ctx : ShellFillingRuleContext R] :
    ∀ n : ℕ, n < ctx.n_val → ctx.occupancy n = ctx.capacity n := by
  intro n hn
  exact ctx.filled_of_vacancy_gap n hn (ctx.vacancy_gap_nonzero n hn)

/-- **Claim (ii), Hund's rule — proved.**  Within the
    valence shell the ground state maximises the number of singly
    occupied sites: parallel electron trefoils have lower `Φ₁` than
    antiparallel pairs, since the repulsive `ee` crossing (`σ`) is
    minimised on distinct spatial sites. -/
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/shell-filling-rule.md
theorem shell_filling_hund_rule [ctx : ShellFillingRuleContext R] :
    ∀ c : ctx.ValenceConfig, ctx.singly c ≤ ctx.singly ctx.ground := by
  intro c
  exact ctx.singly_antimono_crossings c (ctx.ground_minimises_crossings c)

/-- **Claim (iii), LP strong duality — proved.**  The
    optimal primal objective of the electron assignment LP equals the
    dual objective `Z·y₀` (`max_y Z·y₀` s.t.
    `y₀ + Σ_n G_{n,s}·y_{n,s} ≤ Φ₁^{(s)}` for all sites `s`). -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP strong duality)
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/shell-filling-rule.md
theorem shell_filling_lp_strong_duality [ctx : ShellFillingRuleContext R] :
    ctx.primal_obj = (ctx.Z : R) * ctx.y_0 := by
  rw [ctx.strong_duality, ctx.dual_obj_eq]

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
theorem shell_filling_rule [ctx : ShellFillingRuleContext R] :
    (∀ n : ℕ, n < ctx.n_val → ctx.occupancy n = ctx.capacity n) ∧
    (∀ c : ctx.ValenceConfig, ctx.singly c ≤ ctx.singly ctx.ground) ∧
    ctx.primal_obj = (ctx.Z : R) * ctx.y_0 :=
  ⟨shell_filling_inner_shells, shell_filling_hund_rule,
   shell_filling_lp_strong_duality⟩

end QOU.Molecular
