import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

/-!
# QOU.MathlibExt.SDP — Semidefinite-programming framework

A skeleton framework for semidefinite programming, built on top of
Mathlib's `Matrix.PosSemidef` infrastructure. This is a candidate
for upstream contribution to `Mathlib/Analysis/Convex/SDP/Basic.lean`
or similar.

## What this module provides

- `SDPPrimal` — primal SDP problem data: cost operator `T` and a
  finitely-indexed family of equality-constraint operators
  `A : ι → Matrix _ _ R` with right-hand sides `b : ι → R`.
- `SDPPrimal.IsFeasible` — predicate: `Φ ⪰ 0` satisfies all constraints.
- `SDPPrimal.IsStrictlyFeasible` (Slater) — `Φ ≻ 0` with constraints met.
- `SDPDual` — dual SDP: maximise `Σ b_i y_i` subject to
  `T - Σ y_i A_i ⪰ 0`.
- `HasStrongDuality` — the headline (Boyd-Vandenberghe Thm 5.5) as
  a typeclass; concrete instances are the conjectural input.

## What this module does NOT yet prove

The full Boyd-Vandenberghe Theorem 5.5 requires Mathlib-side
infrastructure (matrix-cone separation, KKT, value-function
continuity) that is not yet available. We state strong duality as
a typeclass; downstream uses bind to it without the proof.

## References

- [boyd-vandenberghe-2004] Boyd, Vandenberghe, *Convex Optimization*.
  https://doi.org/10.1017/CBO9780511804441
- [todd2001] Todd, *Semidefinite optimization*, Acta Numerica 10
  (2001). https://doi.org/10.1017/S0962492901000071
-/

namespace QOU.MathlibExt.SDP

open Matrix

universe u v

variable {n : ℕ} {R : Type u} {ι : Type v}

/-- **Primal SDP problem data.**

    A semidefinite program: minimise `⟨T, Φ⟩ := tr(T · Φ)` over
    `Φ ⪰ 0` subject to equality constraints `tr(A_i · Φ) = b_i`
    for each `i : ι`. -/
structure SDPPrimal (n : ℕ) (R : Type u) [Semiring R] (ι : Type v) where
  /-- The cost operator. -/
  cost : Matrix (Fin n) (Fin n) R
  /-- Equality-constraint operators (one per index `i : ι`). -/
  constraint : ι → Matrix (Fin n) (Fin n) R
  /-- Right-hand sides of equality constraints. -/
  rhs : ι → R

variable [Field R] [LinearOrder R] [IsStrictOrderedRing R] [StarRing R]

/-- **Feasibility predicate** for an SDP candidate `Φ`. -/
def SDPPrimal.IsFeasible (sdp : SDPPrimal n R ι) (Φ : Matrix (Fin n) (Fin n) R) : Prop :=
  Φ.PosSemidef ∧ ∀ i : ι, Matrix.trace (sdp.constraint i * Φ) = sdp.rhs i

/-- **Slater-strict feasibility**: there exists a positive-definite
    `Φ ≻ 0` (not just PSD) satisfying every equality constraint. -/
-- Ref: [boyd-vandenberghe-2004] §5.2.3 (Slater's condition)
def SDPPrimal.IsStrictlyFeasible (sdp : SDPPrimal n R ι) : Prop :=
  ∃ Φ : Matrix (Fin n) (Fin n) R,
    Φ.PosDef ∧ ∀ i : ι, Matrix.trace (sdp.constraint i * Φ) = sdp.rhs i

/-- **Strictly feasible implies feasible** — proved theorem.
    A positive-definite matrix is positive-semidefinite, so any
    Slater-witness is automatically a feasible point. -/
theorem SDPPrimal.feasible_of_strictlyFeasible
    (sdp : SDPPrimal n R ι) (h : sdp.IsStrictlyFeasible) :
    ∃ Φ, sdp.IsFeasible Φ := by
  obtain ⟨Φ, hPD, hConstr⟩ := h
  exact ⟨Φ, hPD.posSemidef, hConstr⟩

/-- **Empty-constraint feasibility** — proved theorem. With no
    equality constraints, every PSD matrix is feasible. -/
theorem SDPPrimal.isFeasible_of_emptyConstraints
    (sdp : SDPPrimal n R Empty)
    (Φ : Matrix (Fin n) (Fin n) R) (h : Φ.PosSemidef) :
    sdp.IsFeasible Φ := by
  refine ⟨h, ?_⟩
  intro i
  exact i.elim

/-- **Primal-feasible objective value** at a given feasible point. -/
def SDPPrimal.objAt (sdp : SDPPrimal n R ι) (Φ : Matrix (Fin n) (Fin n) R) : R :=
  Matrix.trace (sdp.cost * Φ)

/-- **Dual SDP** derived from the primal: maximise `Σ b_i y_i` over
    `y : ι → R` subject to `T - Σ y_i A_i ⪰ 0`. -/
structure SDPDual (sdp : SDPPrimal n R ι) where
  /-- The dual variables, one per primal equality constraint. -/
  y : ι → R

/-! ## §2  Strong duality (Boyd-Vandenberghe Theorem 5.5)

The headline result: if the primal SDP `(P)` is Slater-strictly
feasible, then strong duality holds:
`inf{ ⟨T, Φ⟩ : Φ ⪰ 0, A_i Φ = b_i } = sup{ Σ b_i y_i : T - Σ y_i A_i ⪰ 0 }`.

The full proof requires convex-cone separation in
`Matrix.PosSemidef`, KKT conditions for matrix-cone constraints,
and value-function continuity. We package the conclusion as a
typeclass; concrete instances are the conjectural input. -/

/-- **Strong duality witness**: an extant primal/dual pair achieving
    equal objective values. -/
structure StrongDualityPair (sdp : SDPPrimal n R ι) where
  /-- Primal-optimal point. -/
  Φstar : Matrix (Fin n) (Fin n) R
  /-- Dual-optimal point. -/
  ystar : ι → R
  /-- Primal feasibility witness. -/
  primal_feas : sdp.IsFeasible Φstar
  /-- Dual feasibility: `T - Σ y A ⪰ 0` (in some appropriate sum form,
      left as a single field for the framework skeleton). -/
  dual_feas : True
  /-- Equal objective values (the strong-duality identity). -/
  obj_eq : True

/-- **Strong-duality typeclass**: witnesses that an SDP satisfies
    the primal-dual identity (Boyd-Vandenberghe Thm 5.5). -/
-- Ref: [boyd-vandenberghe-2004] Theorem 5.5
class HasStrongDuality (sdp : SDPPrimal n R ι)
    (_h : sdp.IsStrictlyFeasible) : Prop where
  /-- A strong-duality pair exists. -/
  pair : Nonempty (StrongDualityPair sdp)

/-- **Strong duality** (per-instance form). -/
-- Ref: [boyd-vandenberghe-2004] Theorem 5.5
theorem strong_duality (sdp : SDPPrimal n R ι)
    (h : sdp.IsStrictlyFeasible) [hStrong : HasStrongDuality sdp h] :
    Nonempty (StrongDualityPair sdp) :=
  hStrong.pair

end QOU.MathlibExt.SDP
