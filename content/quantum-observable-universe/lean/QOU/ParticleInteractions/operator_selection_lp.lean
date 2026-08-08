import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Data.Fintype.Fin
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

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
`n_target`, and the duals `y₀*`, `y*`.  It does **not** carry the
optimality / strong-duality conclusions as fields (an earlier version
did, then projected them — a self-assuming projection forbidden by
AGENTS.md §3b-cond item 5).

`operator_selection_lp` is now **proved sorry-free** as the genuine LP
**weak-duality** theorem: given a dual certificate — primal feasibility,
`y* ≥ 0`, stationarity `t = y₀*·1 + Gᵀy*`, complementary slackness
`⟨y*, Gx*⟩ = 0` — it *derives* that `x*` is feasible, optimal among all
feasible points, and that strong duality `objective x* = n_target·y₀*`
holds.  The certificate is the LP *input* (a solver emits `y₀*`, `y*`,
the active set); the optimality/strong-duality *conclusions* are derived,
not assumed.  No full simplex/LP-strong-duality theorem is needed — weak
duality plus the certificate suffice.  `IsFeasible` is a genuine
predicate on the data (no opaque `Prop` field projected).

## Base ring (§7c)

Nothing in the program is archimedean: feasibility, optimality and
strong duality are statements about `Finset.sum`, `*` and `≤`, and a
linear program makes sense over any ordered commutative ring.  The
scalars are therefore a generic `R`, and the substrate evaluation is
the instantiation `R := ℝ`. -/

namespace QOU.ParticleInteractions

/-- Data of the operator-selection LP: the cost vector `t`, the
    Frobenius Gram matrix `G`, the target net value `n_target`, a
    candidate primal point `x*`, and the net-constraint dual variable
    `y₀*`.  These are *inputs*; nothing here asserts the conclusion. -/
class OperatorSelectionLpContext (R : Type*) [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] where
  /-- The strand number `n ≥ 2`. -/
  n : ℕ
  /-- The basis cardinality `d = n!`. -/
  d : ℕ
  /-- The target net value `n_target`. -/
  n_target : R
  /-- The Markov-trace cost coefficients `t : Fin d → R`. -/
  t : Fin d → R
  /-- The Frobenius Gram matrix `G : Fin d → Fin d → R`. -/
  G : Fin d → Fin d → R
  /-- The candidate primal point `x* : Fin d → R`. -/
  x_star : Fin d → R
  /-- The net-constraint dual variable `y₀* : R`. -/
  y_0_star : R
  /-- The Frobenius-positivity dual vector `y* : Fin d → R` (the certificate
      requires `y* ≥ 0`; carried as data, its sign is a theorem hypothesis). -/
  y_star : Fin d → R

namespace OperatorSelectionLpContext

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
variable [ctx : OperatorSelectionLpContext R]

/-- A vector `x : Fin d → R` is LP-feasible: it satisfies the net
    constraint and Frobenius positivity. (Boundedness `xᵢ ≥ -M` is
    absorbed into the existence of a large `M`; we keep the two
    binding constraints, which are the ones that select the optimum.)

    This is a genuine predicate on the data, not a projected field. -/
def IsFeasible (x : Fin (ctx.d) → R) : Prop :=
  (Finset.univ.sum fun i : Fin ctx.d => x i) = ctx.n_target ∧
  (∀ i : Fin ctx.d, 0 ≤ (Finset.univ.sum fun j : Fin ctx.d => ctx.G i j * x j))

/-- The objective value `Σᵢ tᵢ xᵢ` of a candidate `x`. -/
def objective (x : Fin (ctx.d) → R) : R :=
  Finset.univ.sum fun i : Fin ctx.d => ctx.t i * x i

end OperatorSelectionLpContext

/-- **Operator selection LP** ([`prop:operator-selection-lp`]), the genuine
    LP **weak-duality** result (sorry-free).

    Given a *dual certificate* — primal feasibility of `x*`, dual sign
    `y* ≥ 0`, stationarity `t = y₀*·1 + Gᵀy*`, and complementary slackness
    `⟨y*, G x*⟩ = 0` — the candidate `x*` is feasible, is the minimum-objective
    feasible point, and strong duality `objective x* = n_target · y₀*` holds.

    The certificate hypotheses are the LP *inputs* (a solver emits them: the
    active-set dual `y*`, the shadow price `y₀*`); the optimality and
    strong-duality *conclusions* are **derived** here by weak duality — not
    assumed.  This is the honest §3b-cond form (hypotheses in, conclusion
    out), replacing the earlier self-assuming projection. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP weak/strong duality)
-- Ref: [manuscript] quantum-observable-universe/mass-theory/operator-selection-lp.md
theorem operator_selection_lp {R : Type*} [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] [ctx : OperatorSelectionLpContext R]
    (hfeas : OperatorSelectionLpContext.IsFeasible ctx.x_star)
    (hdual : ∀ i : Fin ctx.d, 0 ≤ ctx.y_star i)
    (hstat : ∀ i : Fin ctx.d,
      ctx.t i = ctx.y_0_star + ∑ j : Fin ctx.d, ctx.G j i * ctx.y_star j)
    (hcs : (∑ i : Fin ctx.d,
      ctx.y_star i * (∑ j : Fin ctx.d, ctx.G i j * ctx.x_star j)) = 0) :
    OperatorSelectionLpContext.IsFeasible ctx.x_star ∧
    (∀ x : Fin ctx.d → R, OperatorSelectionLpContext.IsFeasible x →
      OperatorSelectionLpContext.objective ctx.x_star ≤
        OperatorSelectionLpContext.objective x) ∧
    OperatorSelectionLpContext.objective ctx.x_star
      = ctx.n_target * ctx.y_0_star := by
  -- Key identity (from stationarity): for ANY x,
  --   objective x = y₀*·(Σᵢ xᵢ) + Σᵢ y*ᵢ·(Σⱼ Gᵢⱼ xⱼ).
  have key : ∀ x : Fin ctx.d → R,
      OperatorSelectionLpContext.objective x
        = ctx.y_0_star * (∑ i, x i)
          + ∑ i, ctx.y_star i * (∑ j, ctx.G i j * x j) := by
    intro x
    calc OperatorSelectionLpContext.objective x
        = ∑ i, (ctx.y_0_star + ∑ j, ctx.G j i * ctx.y_star j) * x i := by
          simp only [OperatorSelectionLpContext.objective]
          exact Finset.sum_congr rfl (fun i _ => by rw [hstat i])
      _ = (∑ i, ctx.y_0_star * x i)
            + ∑ i, ∑ j, ctx.G j i * ctx.y_star j * x i := by
          rw [← Finset.sum_add_distrib]
          exact Finset.sum_congr rfl (fun i _ => by rw [add_mul, Finset.sum_mul])
      _ = ctx.y_0_star * (∑ i, x i)
            + ∑ j, ∑ i, ctx.G j i * ctx.y_star j * x i := by
          rw [Finset.mul_sum, Finset.sum_comm]
      _ = ctx.y_0_star * (∑ i, x i)
            + ∑ i, ctx.y_star i * (∑ j, ctx.G i j * x j) := by
          congr 1
          exact Finset.sum_congr rfl (fun i _ => by
            rw [Finset.mul_sum]
            exact Finset.sum_congr rfl (fun j _ => by ring))
  -- Strong duality: objective x* = y₀*·n_target (feasibility + comp. slack).
  have hsd : OperatorSelectionLpContext.objective ctx.x_star
      = ctx.n_target * ctx.y_0_star := by
    rw [key ctx.x_star, hfeas.1, hcs, add_zero, mul_comm]
  refine ⟨hfeas, ?_, hsd⟩
  -- Optimality: for feasible x, objective x ≥ y₀*·n_target = objective x*.
  intro x hx
  have hnn : 0 ≤ ∑ i, ctx.y_star i * (∑ j, ctx.G i j * x j) :=
    Finset.sum_nonneg (fun i _ => mul_nonneg (hdual i) (hx.2 i))
  rw [hsd, key x, hx.1]
  nlinarith [hnn]

end QOU.ParticleInteractions
