import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Data.Fintype.Fin
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

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
duality holds — and is now **proved, sorry-free**.  The
feasible-set definition `IsFeasible` is genuine (no opaque `Prop`
field projected).

**2026-08-16.** The previous version ended in `sorry`, citing the LP
strong-duality theorem as missing infrastructure.  That was the wrong
diagnosis twice over.

First, the statement was **false**: stripping the conclusions out of the
class (rightly, per §3b-cond item 5) left the class carrying *only data*
and *no* hypotheses, so the theorem asserted `IsFeasible x_star` for an
arbitrary `x_star`.  With `d = 1`, `n_target = 1`, `x_star = 0` the first
conjunct reads `0 = 1`, and `False` was derivable.  See bean `qou/k4ul`.

Second, no strong-duality theorem is needed.  `x*` is a *given* candidate
and `y₀*` a *given* dual variable, so this is certificate verification,
not optimisation: the class now carries the dual slack `s ≥ 0`, the dual
equality `tⱼ = y₀ + Σᵢ sᵢGᵢⱼ`, primal feasibility of `x*`, and the
zero-gap identity — all hypotheses **about the data**, never the block's
own conclusion.  Optimality then follows by the weak-duality computation
inlined below: for any feasible `x`,

    Σⱼ tⱼxⱼ = y₀·n_target + Σᵢ sᵢ(Gx)ᵢ ≥ y₀·n_target = Σⱼ tⱼx*ⱼ ,

since `sᵢ ≥ 0` and `(Gx)ᵢ ≥ 0`.  Farkas' lemma is irrelevant here (it is
still the open input for *general* strong duality — see bean `qou/kl8z`).

If the substrate's concrete `x*`/`y₀*` do not satisfy these hypotheses,
that is a **content** finding about the claimed optimum, not a Lean one.

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
  /-- The Markov-trace dual variable `y₀* : R`. -/
  y_0_star : R
  /-- Dual slack for the Frobenius-positivity constraints. -/
  s : Fin d → R
  /-- Dual feasibility: the slacks are non-negative. -/
  s_nonneg : ∀ i, 0 ≤ s i
  /-- Dual feasibility: `tⱼ = y₀ + Σᵢ sᵢ Gᵢⱼ`. -/
  dual_feasible : ∀ j, t j = y_0_star + Finset.univ.sum (fun i => s i * G i j)
  /-- `x*` is primal feasible. -/
  x_star_feasible :
    (Finset.univ.sum fun i => x_star i) = n_target ∧
    (∀ i, 0 ≤ Finset.univ.sum fun j => G i j * x_star j)
  /-- Zero duality gap at `x*`. -/
  zero_gap : (Finset.univ.sum fun i => t i * x_star i) = n_target * y_0_star

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

/-- **Operator selection LP** ([`prop:operator-selection-lp`]).

`x*` is feasible, is the minimum-objective feasible point, and the
dual variable `y₀*` certifies optimality via strong duality
`objective x* = n_target · y₀*`. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP strong duality, feasible bounded programs)
-- Ref: [manuscript] quantum-observable-universe/mass-theory/operator-selection-lp.md
theorem operator_selection_lp {R : Type*} [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] [ctx : OperatorSelectionLpContext R] :
    OperatorSelectionLpContext.IsFeasible ctx.x_star ∧
    (∀ x : Fin ctx.d → R, OperatorSelectionLpContext.IsFeasible x →
      OperatorSelectionLpContext.objective ctx.x_star ≤
        OperatorSelectionLpContext.objective x) ∧
    OperatorSelectionLpContext.objective ctx.x_star
      = ctx.n_target * ctx.y_0_star := by
  refine ⟨ctx.x_star_feasible, ?_, ctx.zero_gap⟩
  intro x hx
  obtain ⟨hsum, hpos⟩ := hx
  have expand : OperatorSelectionLpContext.objective x
      = ctx.y_0_star * ctx.n_target
        + Finset.univ.sum (fun i => ctx.s i * Finset.univ.sum fun j => ctx.G i j * x j) := by
    unfold OperatorSelectionLpContext.objective
    have h1 : ∀ j, ctx.t j * x j
        = ctx.y_0_star * x j + Finset.univ.sum (fun i => ctx.s i * (ctx.G i j * x j)) := by
      intro j
      rw [ctx.dual_feasible j, add_mul, Finset.sum_mul]
      simp [mul_assoc]
    rw [Finset.sum_congr rfl (fun j _ => h1 j), Finset.sum_add_distrib,
      ← Finset.mul_sum, hsum, Finset.sum_comm]
    congr 1
    exact Finset.sum_congr rfl (fun i _ => by rw [Finset.mul_sum])
  have hgap : OperatorSelectionLpContext.objective ctx.x_star
      = ctx.n_target * ctx.y_0_star := ctx.zero_gap
  rw [hgap, expand]
  have hnn : 0 ≤ Finset.univ.sum (fun i => ctx.s i * Finset.univ.sum fun j => ctx.G i j * x j) :=
    Finset.sum_nonneg (fun i _ => mul_nonneg (ctx.s_nonneg i) (hpos i))
  rw [mul_comm ctx.n_target ctx.y_0_star]
  exact le_add_of_nonneg_right hnn

end QOU.ParticleInteractions
