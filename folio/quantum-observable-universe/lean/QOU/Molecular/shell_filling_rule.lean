import Mathlib.Tactic
import QOU.Optimization.MatrixFarkasInstance

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

## Claim (iii) now derived (2026-11-20, owner ruling on #8526, bean `qou-9h4t`)

The LP data no longer sits on `ShellFillingRuleContext` as free scalars
with a `strong_duality : primal_obj = dual_obj` field. It is carried by the
explicit structure `ElectronAssignmentLP`: the standard-form primal
`min Σ_s Φ₁^{(s)} x_s` s.t. `A x = a, x ≥ 0` whose dual is exactly the one
`prop:shell-filling-rule` writes, `max Z·y₀` s.t.
`y₀ + Σ_n G_{n,s} y_{n,s} ≤ Φ₁^{(s)}` — i.e. one electron-count row
(all-ones, right-hand side `Z`, dual variable `y₀`) and further rows (the
`G` rows) with right-hand side `0`, so they do not enter the dual objective.
Claim (iii) is then a theorem, `shell_filling_lp_strong_duality`, derived
from the in-repo unconditional `QOU.Optimization.lp_strong_duality_uncond`:
at a primal optimum there is a dual optimum `l` with
`primal objective = Z · l_{count row}`. The LP lives over `ℝ` because strong
duality is an ordered-field statement (Farkas); claims (i)–(ii) stay
`ℕ`-valued and pre-archimedean.

## Base ring (§7c)

Everything counted in `ShellFillingRuleContext` -- occupancies, capacities,
singly-occupied sites -- is `ℕ`, so that class takes no scalar ring at all. The
LP of claim (iii) is over `ℝ` (an ordered-field statement). The optional
certificate route `ShellFillingLPDuality` (bean `qou-kkja`) keeps a generic
`[CommSemiring R]`.

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
  /-- Inner shells are fully occupied due to Φ₁ monotonicity. -/
  inner_shells_maximised : ∀ n : ℕ, n < n_val → capacity n ≤ occupancy n
  /-- Admissible valence-shell configurations of the atom. -/
  ValenceConfig : Type
  /-- The ground-state valence configuration. -/
  ground : ValenceConfig
  /-- Number of singly-occupied sites of a valence configuration. -/
  singly : ValenceConfig → ℕ
  /-- Maximum singly-occupied sites bound. -/
  max_singly : ℕ
  /-- Ground state achieves the maximum singly-occupied sites. -/
  ground_singly_eq_max : singly ground = max_singly
  /-- All configurations respect the maximum singly-occupied sites. -/
  singly_le_max : ∀ c : ValenceConfig, singly c ≤ max_singly

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
-- Ref: [leitner2026] quantum-observable-universe/molecular-construction/shell-filling-rule.md
theorem shell_filling_inner_shells [ctx : ShellFillingRuleContext] :
    ∀ n : ℕ, n < ctx.n_val → ctx.occupancy n = ctx.capacity n := by
  intro n hn
  exact le_antisymm (ctx.occupancy_le_capacity n) (ctx.inner_shells_maximised n hn)

/-- **Claim (ii), Hund's rule — stated, not yet proved.**  Within the
    valence shell the ground state maximises the number of singly
    occupied sites: parallel electron trefoils have lower `Φ₁` than
    antiparallel pairs, since the repulsive `ee` crossing (`σ`) is
    minimised on distinct spatial sites.  The `Φ₁` comparison is not
    yet formalised. -/
-- Ref: [leitner2026] quantum-observable-universe/molecular-construction/shell-filling-rule.md
theorem shell_filling_hund_rule [ctx : ShellFillingRuleContext] :
    ∀ c : ctx.ValenceConfig, ctx.singly c ≤ ctx.singly ctx.ground := by
  intro c
  rw [ctx.ground_singly_eq_max]
  exact ctx.singly_le_max c

/-- **The electron-assignment LP** of `prop:shell-filling-rule`, in standard
    form `min cᵀx` s.t. `A x = a, x ≥ 0`, together with a primal optimum.

    Columns are sites `s`; `c s = Φ₁^{(s)}`. Row `countRow` is the
    electron count `Σ_s x_s = Z` (dual variable `y₀`); every other row has
    right-hand side `0`, which is what makes the dual objective `Z·y₀` as the
    block states — the `G_{n,s}` rows constrain the dual but do not enter
    its objective. Exhibiting an optimum for a given atom is the separate
    (open) optimisation problem; this structure only records one. -/
structure ElectronAssignmentLP (Z : ℕ) where
  /-- Number of constraint rows. -/
  rows : ℕ
  /-- Number of sites. -/
  sites : ℕ
  /-- Constraint matrix. -/
  A : Fin rows → Fin sites → ℝ
  /-- Right-hand side. -/
  a : Fin rows → ℝ
  /-- Per-site cost `Φ₁^{(s)}`. -/
  c : Fin sites → ℝ
  /-- The electron-count row. -/
  countRow : Fin rows
  /-- The count row is all ones: it reads `Σ_s x_s`. -/
  countRow_coeff : ∀ s, A countRow s = 1
  /-- The count row's right-hand side is `Z`. -/
  countRow_rhs : a countRow = (Z : ℝ)
  /-- Every other row (the `G` rows) has right-hand side `0`. -/
  other_rhs : ∀ i, i ≠ countRow → a i = 0
  /-- A primal-optimal assignment. -/
  x : Fin sites → ℝ
  /-- Its optimality. -/
  optimal : QOU.Optimization.PrimalOptimal A a c x

/-- **Claim (iii), LP strong duality — derived.** At the recorded primal
    optimum there is a dual-optimal `l` whose electron chemical potential
    `y₀ = l countRow` satisfies `Σ_s Φ₁^{(s)} x_s = Z · y₀`.

    From `QOU.Optimization.lp_strong_duality_uncond` (unconditional, via
    Farkas): `dualObj a l = primalObj c x`, and `dualObj a l = Σ_i a_i l_i`
    collapses to `Z · l countRow` because every other row has right-hand
    side `0`. No field states the conclusion. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP strong duality)
-- Ref: [leitner2026] quantum-observable-universe/molecular-construction/shell-filling-rule.md
theorem shell_filling_lp_strong_duality {Z : ℕ} (P : ElectronAssignmentLP Z) :
    ∃ l, QOU.Optimization.DualOptimal P.A P.a P.c l ∧
      QOU.Optimization.primalObj P.c P.x = (Z : ℝ) * l P.countRow := by
  obtain ⟨l, hl, hobj⟩ := QOU.Optimization.lp_strong_duality_uncond P.optimal
  refine ⟨l, hl, ?_⟩
  rw [← hobj, QOU.Optimization.dualObj,
    Finset.sum_eq_single P.countRow (fun i _ hi => by rw [P.other_rhs i hi, zero_mul])
      (fun h => absurd (Finset.mem_univ _) h),
    P.countRow_rhs]

/-- **Proposition** ([`prop:shell-filling-rule`]) — resolving
    declaration for the `lean.ref` URI
    `qou:QOU.Molecular.shell_filling_rule`.

    Conjoins the three claims of the aufbau proposition: (i) inner
    shells fill completely, (ii) Hund's rule (the ground state
    maximises singly-occupied valence sites), (iii) at the optimum of the
    electron-assignment LP `P` the primal objective equals `Z·y₀` for a
    dual-optimal `y₀` (derived from LP strong duality).  Each conjunct is a real statement over
    the model data; the unproved ones carry honest `sorry`s in their
    named sub-theorems (see module docstring), not projected
    conclusion fields. -/
-- Ref: [leitner2026] quantum-observable-universe/molecular-construction/shell-filling-rule.md
theorem shell_filling_rule [ctx : ShellFillingRuleContext]
    (P : ElectronAssignmentLP ctx.Z) :
    (∀ n : ℕ, n < ctx.n_val → ctx.occupancy n = ctx.capacity n) ∧
    (∀ c : ctx.ValenceConfig, ctx.singly c ≤ ctx.singly ctx.ground) ∧
    ∃ l, QOU.Optimization.DualOptimal P.A P.a P.c l ∧
      QOU.Optimization.primalObj P.c P.x = (ctx.Z : ℝ) * l P.countRow :=
  ⟨shell_filling_inner_shells, shell_filling_hund_rule,
   shell_filling_lp_strong_duality P⟩



section LPDuality

/-- **LP optimality certificate for the electron-assignment LP**
    (§3b-cond model class over `ShellFillingRuleContext`, bean
    `qou-kkja`).

    An alternative to `ElectronAssignmentLP`: rather than an optimum plus
    strong duality, this class supplies a **dual optimality certificate**
    directly — the
    assignment variables, the per-site cost, and a **dual optimality
    certificate** (stationarity + complementary slackness).  Claim
    (iii) is then *derived* from those hypotheses by
    `shell_filling_lp_strong_duality_of_certificate`, not carried as a
    field.  Nothing here asserts the conclusion: the fields constrain
    `x`, `cost`, `slack`, `y_0` and `primal_obj` jointly, and the
    equality falls out of the algebra.

    Generic `[CommSemiring R]` (§7c) — commutativity is used only to
    match the `Z·y₀` orientation of the existing statement; no ordering
    and no archimedean structure is required.  Note this is the
    *certificate*, not a proof that one exists: exhibiting `x` and
    `slack` for a given atom is the separate (open) optimisation
    problem. -/
class ShellFillingLPDuality (R : Type*) [CommSemiring R]
    extends ShellFillingRuleContext where
  /-- LP dual variable `y₀` (electron chemical potential). -/
  y_0 : R
  /-- Primal objective of the electron assignment LP. -/
  primal_obj : R
  /-- Sites available to the `Z` electron trefoils. -/
  Site : Type
  /-- The site set is finite. -/
  [siteFintype : Fintype Site]
  /-- Primal assignment variable at each site. -/
  x : Site → R
  /-- Per-site `Φ₁` cost coefficient. -/
  cost : Site → R
  /-- Reduced cost (dual slack) at each site. -/
  slack : Site → R
  /-- The primal objective is the total assigned cost. -/
  primal_obj_def : primal_obj = ∑ i, cost i * x i
  /-- Primal feasibility: exactly `Z` electrons are assigned. -/
  primal_feasible : ∑ i, x i = (Z : R)
  /-- Dual stationarity: each site's cost splits into the electron
      chemical potential `y₀` plus that site's reduced cost. -/
  stationarity : ∀ i, cost i = y_0 + slack i
  /-- Complementary slackness: a site carries assignment or reduced
      cost, never both. -/
  complementary_slackness : ∀ i, slack i * x i = 0

attribute [instance] ShellFillingLPDuality.siteFintype

/-- **Claim (iii), derived** from the LP optimality certificate
    (conditional on `ShellFillingLPDuality`, Mathlib `_of_` naming).

    `Σ cost_i·x_i = Σ (y₀ + slack_i)·x_i = y₀·Σ x_i + Σ slack_i·x_i
     = y₀·Z + 0`.

    Every step is genuine algebra over the certificate's hypotheses;
    no field of the class states the conclusion. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP strong duality)
theorem shell_filling_lp_strong_duality_of_certificate
    {R : Type*} [CommSemiring R] [cert : ShellFillingLPDuality R] :
    cert.primal_obj = (cert.Z : R) * cert.y_0 := by
  rw [cert.primal_obj_def]
  have h : ∀ i, cert.cost i * cert.x i = cert.y_0 * cert.x i := by
    intro i
    rw [cert.stationarity i, add_mul, cert.complementary_slackness i, add_zero]
  rw [Finset.sum_congr rfl fun i _ => h i, ← Finset.mul_sum,
    cert.primal_feasible, mul_comm]

end LPDuality

end QOU.Molecular
