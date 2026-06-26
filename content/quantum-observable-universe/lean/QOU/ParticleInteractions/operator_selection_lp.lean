import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Data.Fintype.Fin

/-!
# QOU.ParticleInteractions.operator_selection_lp

**Proposition** ([`prop:operator-selection-lp`](../../../quantum-observable-universe/mass-theory/operator-selection-lp.md)):
*Knot operator selection as a linear program with LP duality.*

The knot operator `Φ = Σᵢ xᵢ bᵢ ∈ Hₙ(q)` for a target interaction
with net value `n_target` is the optimum of

  minimise   Σᵢ tᵢ xᵢ
  subject to Σᵢ xᵢ = n_target           (net constraint)
             Σⱼ G_{ij} xⱼ ≥ 0  ∀ i      (Frobenius positivity)
             xᵢ ≥ -M          ∀ i       (boundedness),

and the dual certificate `(y₀*, y*)` satisfies strong duality
`Σᵢ tᵢ xᵢ* = n_target · y₀*` and complementary slackness.

## Disposition (integrity)

The class below carries only the **LP data** — the cost vector `t`,
the Frobenius Gram matrix `G`, a candidate `x*`, the target
`n_target`, and the dual variable `y₀*`.  It does **not** carry the
optimality / strong-duality conclusions as fields (the previous
version did, then projected them — a self-assuming projection
forbidden by AGENTS.md §3b-cond item 5).

`operator_selection_lp` states the genuine conclusion — `x*` is
primal-feasible AND optimal among all feasible points AND strong
duality holds — and ends in `sorry` (disposition B): proving it
requires the LP strong-duality theorem for feasible bounded programs,
which is not yet available in the `QOU` library / Mathlib.  The
feasible-set definition `IsFeasible` is genuine (no opaque `Prop`
field projected). -/

namespace QOU.ParticleInteractions

/-- Data of the operator-selection LP: the cost vector `t`, the
    Frobenius Gram matrix `G`, the target net value `n_target`, a
    candidate primal point `x*`, and the net-constraint dual variable
    `y₀*`.  These are *inputs*; nothing here asserts the conclusion. -/
class OperatorSelectionLpContext where
  /-- The strand number `n ≥ 2`. -/
  n : ℕ
  /-- The basis cardinality `d = n!`. -/
  d : ℕ
  /-- The target net value `n_target ∈ ℝ_{>0}`. -/
  n_target : ℝ
  /-- The Markov-trace cost coefficients `t : Fin d → ℝ`. -/
  t : Fin d → ℝ
  /-- The Frobenius Gram matrix `G : Fin d → Fin d → ℝ`. -/
  G : Fin d → Fin d → ℝ
  /-- The candidate primal point `x* : Fin d → ℝ`. -/
  x_star : Fin d → ℝ
  /-- The Markov-trace dual variable `y₀* : ℝ`. -/
  y_0_star : ℝ

namespace OperatorSelectionLpContext

variable [ctx : OperatorSelectionLpContext]

/-- A vector `x : Fin d → ℝ` is LP-feasible: it satisfies the net
    constraint and Frobenius positivity. (Boundedness `xᵢ ≥ -M` is
    absorbed into the existence of a large `M`; we keep the two
    binding constraints, which are the ones that select the optimum.)

    This is a genuine predicate on the data, not a projected field. -/
def IsFeasible (x : Fin ctx.d → ℝ) : Prop :=
  (Finset.univ.sum fun i : Fin ctx.d => x i) = ctx.n_target ∧
  (∀ i : Fin ctx.d, 0 ≤ (Finset.univ.sum fun j : Fin ctx.d => ctx.G i j * x j))

/-- The objective value `Σᵢ tᵢ xᵢ` of a candidate `x`. -/
def objective (x : Fin ctx.d → ℝ) : ℝ :=
  Finset.univ.sum fun i : Fin ctx.d => ctx.t i * x i

end OperatorSelectionLpContext

/-- **Operator selection LP** ([`prop:operator-selection-lp`]).

`x*` is feasible, is the minimum-objective feasible point, and the
dual variable `y₀*` certifies optimality via strong duality
`objective x* = n_target · y₀*`. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP strong duality, feasible bounded programs)
-- Ref: [manuscript] quantum-observable-universe/mass-theory/operator-selection-lp.md
theorem operator_selection_lp [ctx : OperatorSelectionLpContext] :
    OperatorSelectionLpContext.IsFeasible ctx.x_star ∧
    (∀ x : Fin ctx.d → ℝ, OperatorSelectionLpContext.IsFeasible x →
      OperatorSelectionLpContext.objective ctx.x_star ≤
        OperatorSelectionLpContext.objective x) ∧
    OperatorSelectionLpContext.objective ctx.x_star
      = ctx.n_target * ctx.y_0_star := by
  -- Missing infra: the LP strong-duality theorem (no duality gap for
  -- feasible, bounded linear programs) and the simplex/vertex
  -- optimality argument selecting x*. Not yet formalised in QOU/Mathlib.
  sorry

end QOU.ParticleInteractions
