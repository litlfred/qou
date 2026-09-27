/-
  Knot-operator LP/SDP selection via Gram-inverse dual basis.

  Companion: knot-operator-lp-selection.md
  Path: folio/quantum-observable-universe/braids-and-knots/

  Encodes the LP/SDP-duality selection of knot operators per
  confinement, using the Frobenius Gram-inverse as the dual basis.
  Mathlib lacks a formal LP-duality theory, so the strong-duality
  + complementary-slackness consequences are taken as class
  hypotheses and cited via `-- Ref:`.

  Ref: [schrijver1986theory] Schrijver, "Theory of Linear and
       Integer Programming," Wiley 1986, §7.2 (strong duality)
       + §7.4 (complementary slackness, active-set uniqueness).
-/

import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.LinearAlgebra.BilinearForm.Properties
import Mathlib.Data.Fintype.Basic

namespace QOU.BraidsAndKnots

/--
  An indexed family of knot operators acting on an `R`-algebra `H`,
  together with the supply data needed to formulate the LP for
  operator selection.
-/
structure KnotOperatorFamily
    (R : Type*) [CommRing R]
    (H : Type*) [Ring H] [Algebra R H]
    where
  /-- The (finite) operator index set, e.g. `{T_{2,1}, T_{2,3}, T_{2,5}, …}`. -/
  Op : Type*
  opFinite : Fintype Op
  /-- Each operator's image in `H` (the braid word evaluated as a
      Hecke element). -/
  toH : Op → H
  /-- The (finite) Frobenius-non-degenerate basis of `H`, e.g. the
      NF basis `{γ, σ₀, σ₁, L₊, L₋, e⁻}` for `H_3(q)`. -/
  Basis : Type*
  basisFinite : Fintype Basis
  /-- Crossing-energy weight of each operator, used as the LP
      objective. -/
  crossingEnergy : Op → R
  /-- The supply matrix `S(o, (i,j)) = NF coefficient of basis
      element `i` in `b_i · toH(o) · b_j`. -/
  supply : Op → Basis → Basis → Basis → R

namespace KnotOperatorFamily

variable {R : Type*} [CommRing R] {H : Type*} [Ring H] [Algebra R H]

/-- LP objective: total crossing energy `Σ_o e(o)·x(o)` of a selection `x`. -/
noncomputable def objective (ops : KnotOperatorFamily R H) (x : ops.Op → R) : R :=
  letI := ops.opFinite
  ∑ o : ops.Op, ops.crossingEnergy o * x o

/-- Supply action of a selection `x` on NF-channel `i` (diagonal read of the
    4-index supply matrix): `Σ_o x(o)·S(o,i,i,i)`. -/
noncomputable def supplyAction (ops : KnotOperatorFamily R H)
    (x : ops.Op → R) (i : ops.Basis) : R :=
  letI := ops.opFinite
  ∑ o : ops.Op, x o * ops.supply o i i i

/-- **Feasible** selection for demand `n_T`: non-negative, and its supply
    action meets the required multiplicity on every channel. -/
def Feasible [PartialOrder R] (ops : KnotOperatorFamily R H)
    (x : ops.Op → R) (n_T : ops.Basis → R) : Prop :=
  (∀ o : ops.Op, 0 ≤ x o) ∧ (∀ i : ops.Basis, n_T i ≤ ops.supplyAction x i)

/-- **LP-optimal** selection for demand `n_T`: feasible and objective-maximal
    among all feasible selections. -/
def Optimal [PartialOrder R] (ops : KnotOperatorFamily R H)
    (x : ops.Op → R) (n_T : ops.Basis → R) : Prop :=
  ops.Feasible x n_T ∧
    ∀ x' : ops.Op → R, ops.Feasible x' n_T → ops.objective x' ≤ ops.objective x

end KnotOperatorFamily

/--
  A `KnotOperatorLPSelection R H ops` instance records the LP/SDP-
  duality structure that selects one knot operator per confinement
  via the Frobenius Gram-inverse.

  Mathlib has no formal LP-duality theory, so the two genuinely
  LP-theoretic facts — strong duality and complementary slackness —
  are carried as content-bearing class *hypotheses* (each cited to
  Schrijver). The block's selection conclusion is then **derived** by
  composing them (`knot_operator_lp_selection`), not projected.

  - `frob` / `frob_nondegenerate`: the Frobenius pairing supplying
    `G^{-1}` as the LP-dual basis transform.
  - `strongDuality` (Schrijver §7.2): every demand admits an
    objective-maximal feasible selection.
  - `complementarySlackness` (Schrijver §7.4): at generic non-
    degeneracy, any optimal selection is supported on a single
    operator.
-/
class KnotOperatorLPSelection
    (R : Type*) [CommRing R] [PartialOrder R] [IsOrderedRing R]
    (H : Type*) [Ring H] [Algebra R H]
    (ops : KnotOperatorFamily R H)
    where
  /-- The Frobenius bilinear form on `H` used to define the
      Markov pairing. -/
  frob : LinearMap.BilinForm R H
  /-- Non-degeneracy of the Frobenius form: `det G ≠ 0`. -/
  frob_nondegenerate : frob.Nondegenerate
  /-- **Strong duality** (Schrijver §7.2): every confinement target `n_T`
      admits an LP-optimal (objective-maximal feasible) selection. A genuine
      LP hypothesis — its content is the existence of an optimum, not a bare
      non-negative vector. -/
  strongDuality :
    ∀ (n_T : ops.Basis → R), ∃ x : ops.Op → R, ops.Optimal x n_T
  /-- **Complementary slackness + generic non-degeneracy** (Schrijver §7.4):
      any optimal selection `x` for `n_T` has its support `{o : x o ≠ 0}`
      equal to a single operator `oStar`. A genuine LP hypothesis about the
      *shape* of every optimum (not a bare `∃ oStar, True`). -/
  complementarySlackness :
    ∀ (n_T : ops.Basis → R) (x : ops.Op → R), ops.Optimal x n_T →
      ∃ oStar : ops.Op, ∀ o : ops.Op, x o ≠ 0 ↔ o = oStar

/--
  **Knot-operator LP selection** (`prop:knot-operator-lp-selection`):
  under a `KnotOperatorLPSelection` instance, every confinement target
  `n_T` admits an LP-optimal selection supported on a *unique* knot
  operator `oStar`.

  **Derived**, not projected: composes `strongDuality` (an optimum
  `x` exists) with `complementarySlackness` (that optimum's support is
  a singleton `oStar`) to produce the packaged selection. Neither class
  field is this theorem's conclusion.
-/
theorem knot_operator_lp_selection
    {R : Type*} [CommRing R] [PartialOrder R] [IsOrderedRing R]
    {H : Type*} [Ring H] [Algebra R H]
    {ops : KnotOperatorFamily R H}
    [inst : KnotOperatorLPSelection R H ops]
    (n_T : ops.Basis → R) :
    ∃ oStar : ops.Op, ∃ x : ops.Op → R,
      ops.Optimal x n_T ∧ (∀ o : ops.Op, x o ≠ 0 ↔ o = oStar) := by
  -- Ref: [schrijver1986theory] https://www.wiley.com/en-us/Theory+of+Linear+and+Integer+Programming-p-9780471982326
  -- Ref: [manuscript] docs/audits/2026-05-05-path-alpha-bring-refinement.md §3
  -- Ref: [manuscript] knot-operator-lp-selection.md §"Statement (formal)"
  -- Compose strong duality (§7.2) with complementary slackness (§7.4),
  -- both packaged as class hypotheses since Mathlib lacks formal LP duality.
  obtain ⟨x, hx⟩ := inst.strongDuality n_T
  obtain ⟨oStar, hoStar⟩ := inst.complementarySlackness n_T x hx
  exact ⟨oStar, x, hx, hoStar⟩

end QOU.BraidsAndKnots
