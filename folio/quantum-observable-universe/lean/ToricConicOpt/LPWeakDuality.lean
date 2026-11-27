import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Linear-programming weak duality (proved backing for the QOU LP/SDP dual witnesses)

Every QOU operator-selection / shadow-price compute emits a primal–dual pair in
its `*.witness.json` and asserts `duality_gap ≥ 0` (equivalently
`dual_obj ≤ primal_obj`) as a *numerical* check (see the LP/SDP-dual infra in
`AGENTS.md` and `computations/lp_dual_solver.py`). This file replaces that
numeric check with a **proved** statement: for any primal-feasible `x` and any
dual-feasible `λ`, the dual objective is a lower bound on the primal objective,
so the duality gap is non-negative. This is the *weak* duality half; it holds
for **any** feasible pair, requires no optimality, and needs only ordered-ring
structure — no analysis, no archimedean input.

## Formulation

For a constraint matrix `A : Fin m → Fin n → R`, right-hand side `a : Fin m → R`
and cost vector `c : Fin n → R`, over an ordered commutative ring `R`:

* **Primal feasibility** (`PrimalFeasible A a x`): `A x = a` (row-wise,
  `∀ i, ∑ j, A i j * x j = a i`) together with `x ≥ 0` (`∀ j, 0 ≤ x j`).
* **Dual feasibility** (`DualFeasible A c l`): `λᵀ A ≤ c`
  (`∀ j, ∑ i, l i * A i j ≤ c j`).

The primal is `min ∑ⱼ cⱼ xⱼ  s.t.  A x = a, x ≥ 0`; its Lagrangian dual is
`max ∑ᵢ aᵢ λᵢ  s.t.  λᵀ A ≤ c`. Weak duality is the inequality between the two
objectives at *any* feasible pair.

## Contents

* `lp_weak_duality` — `∑ᵢ aᵢ λᵢ ≤ ∑ⱼ cⱼ xⱼ` for feasible `x`, `λ`.
* `lp_duality_gap_nonneg` — the gap `primalObj − dualObj` is non-negative.

The base ring is a generic `{R : Type*}` with `[CommRing R] [LinearOrder R]
[IsStrictOrderedRing R]` — the substrate-side (§7c) statement of an inequality
that later specialises to `ℝ` at the numerical witnesses without any change to
the proof.

-- Ref: [rivin2003] Igor Rivin, "Combinatorial optimization in geometry",
--   Adv. Appl. Math. 31 (2003) 242–271, §3 (LP duality for the angle-structure
--   / metric programs); the abstract LP weak-duality inequality proved here.
-/

namespace QOU.Optimization

open scoped BigOperators

variable {m n : ℕ} {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Primal feasibility for the standard-form LP `min cᵀx  s.t.  A x = a, x ≥ 0`:
the equality constraints `A x = a` hold row-wise and `x` is non-negative. -/
structure PrimalFeasible (A : Fin m → Fin n → R) (a : Fin m → R) (x : Fin n → R) :
    Prop where
  /-- The equality constraints `A x = a`, one per row `i`. -/
  eq : ∀ i, ∑ j, A i j * x j = a i
  /-- Non-negativity of the primal variables. -/
  nonneg : ∀ j, 0 ≤ x j

/-- Dual feasibility for the Lagrangian dual `max aᵀλ  s.t.  λᵀ A ≤ c`:
the column constraint `λᵀ A ≤ c` holds column-wise. -/
structure DualFeasible (A : Fin m → Fin n → R) (c : Fin n → R) (l : Fin m → R) :
    Prop where
  /-- The dual inequality `λᵀ A ≤ c`, one per column `j`. -/
  le : ∀ j, ∑ i, l i * A i j ≤ c j

/-- The primal objective `∑ⱼ cⱼ xⱼ`. -/
def primalObj (c : Fin n → R) (x : Fin n → R) : R := ∑ j, c j * x j

/-- The dual objective `∑ᵢ aᵢ λᵢ`. -/
def dualObj (a : Fin m → R) (l : Fin m → R) : R := ∑ i, a i * l i

/-- The duality gap `primalObj − dualObj`. Its non-negativity is the content of
`lp_duality_gap_nonneg`; equality would be *strong* duality (not claimed here). -/
def dualityGap (c : Fin n → R) (x : Fin n → R) (a : Fin m → R) (l : Fin m → R) : R :=
  primalObj c x - dualObj a l

/-- **LP weak duality.** For any primal-feasible `x` and dual-feasible `λ`, the
dual objective bounds the primal objective from below:
`∑ᵢ aᵢ λᵢ ≤ ∑ⱼ cⱼ xⱼ`.

Proof: substitute `aᵢ = ∑ⱼ Aᵢⱼ xⱼ`, swap the order of summation, factor out `xⱼ`
to reach `∑ⱼ (∑ᵢ λᵢ Aᵢⱼ) xⱼ`, then bound each term using the dual inequality
`∑ᵢ λᵢ Aᵢⱼ ≤ cⱼ` and `xⱼ ≥ 0`. -/
theorem lp_weak_duality
    {A : Fin m → Fin n → R} {a : Fin m → R} {c : Fin n → R}
    {x : Fin n → R} {l : Fin m → R}
    (hp : PrimalFeasible A a x) (hd : DualFeasible A c l) :
    ∑ i, a i * l i ≤ ∑ j, c j * x j := by
  have key : ∑ i, a i * l i = ∑ j, (∑ i, l i * A i j) * x j := by
    calc
      ∑ i, a i * l i
          = ∑ i, (∑ j, A i j * x j) * l i := by
            refine Finset.sum_congr rfl (fun i _ => ?_)
            rw [hp.eq i]
      _ = ∑ i, ∑ j, A i j * x j * l i := by
            refine Finset.sum_congr rfl (fun i _ => ?_)
            rw [Finset.sum_mul]
      _ = ∑ j, ∑ i, A i j * x j * l i := Finset.sum_comm
      _ = ∑ j, (∑ i, l i * A i j) * x j := by
            refine Finset.sum_congr rfl (fun j _ => ?_)
            rw [Finset.sum_mul]
            refine Finset.sum_congr rfl (fun i _ => ?_)
            ring
  rw [key]
  refine Finset.sum_le_sum (fun j _ => ?_)
  exact mul_le_mul_of_nonneg_right (hd.le j) (hp.nonneg j)

/-- **The LP duality gap is non-negative.** For any primal-feasible `x` and
dual-feasible `λ`, `0 ≤ dualityGap c x a l = primalObj c x − dualObj a l`. This
is the proved statement standing behind the `duality_gap ≥ 0` assertion in every
QOU LP/SDP-dual witness. -/
theorem lp_duality_gap_nonneg
    {A : Fin m → Fin n → R} {a : Fin m → R} {c : Fin n → R}
    {x : Fin n → R} {l : Fin m → R}
    (hp : PrimalFeasible A a x) (hd : DualFeasible A c l) :
    0 ≤ dualityGap c x a l := by
  have h := lp_weak_duality hp hd
  simp only [dualityGap, primalObj, dualObj]
  linarith

end QOU.Optimization
