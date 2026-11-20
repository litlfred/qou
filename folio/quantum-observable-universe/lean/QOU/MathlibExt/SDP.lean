import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic
import QOU.MathlibExt.PosSemidefTraceZero

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

variable [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] [StarRing R]

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
theorem feasible_of_strictlyFeasible
    (sdp : SDPPrimal n R ι) (h : sdp.IsStrictlyFeasible) :
    ∃ Φ, sdp.IsFeasible Φ := by
  obtain ⟨Φ, hPD, hConstr⟩ := h
  exact ⟨Φ, hPD.posSemidef, hConstr⟩

/-- **Empty-constraint feasibility** — proved theorem. With no
    equality constraints, every PSD matrix is feasible. -/
theorem isFeasible_of_emptyConstraints
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

/-! ## §2.1  Dual slack matrix

The dual slack `S(y) := T - Σ y_i A_i` is the matrix whose
positive-semidefiniteness encodes dual feasibility.  For a dual-
optimal `y*`, `S(y*)` is PSD and `tr(S(y*) · Φ) = primal_obj(Φ) -
Σ y*_i b_i = primal_obj(Φ) - dual_obj(y*)`.  This is the core
algebraic identity bridging primal/dual via complementary
slackness. -/

variable [Fintype ι]

/-- **Dual slack matrix** `S(y) := T - Σ_i y_i · A_i`. -/
def SDPPrimal.dualSlack (sdp : SDPPrimal n R ι) (y : ι → R) :
    Matrix (Fin n) (Fin n) R :=
  sdp.cost - ∑ i, y i • sdp.constraint i

/-- **Dual objective value** at a dual point `y`: `Σ_i y_i · b_i`. -/
def SDPPrimal.dualObjAt (sdp : SDPPrimal n R ι) (y : ι → R) : R :=
  ∑ i, y i * sdp.rhs i

/-- **Key algebraic identity**: `tr(S(y) · Φ) = objAt Φ -
    dualObjAt y` for any feasible `Φ`.  Combines
    `Matrix.trace_add` / `_smul` / `_sub` with feasibility
    (`tr(A_i · Φ) = b_i`).

    PROOF: linearity of trace + feasibility constraints. -/
theorem SDPPrimal.dualSlack_trace_eq (sdp : SDPPrimal n R ι)
    (y : ι → R) (Φ : Matrix (Fin n) (Fin n) R)
    (h_feas : sdp.IsFeasible Φ) :
    (sdp.dualSlack y * Φ).trace = sdp.objAt Φ - sdp.dualObjAt y := by
  unfold SDPPrimal.dualSlack SDPPrimal.objAt SDPPrimal.dualObjAt
  -- tr((T - Σ y_i A_i) · Φ) = tr(T · Φ) - Σ y_i · tr(A_i · Φ)
  --                        = objAt Φ - Σ y_i · b_i
  -- (using feasibility tr(A_i · Φ) = b_i for the second equality).
  rw [Matrix.sub_mul, Matrix.trace_sub]
  congr 1
  -- Σ_i y_i · tr(A_i · Φ) = Σ_i y_i · b_i
  rw [Matrix.sum_mul]
  rw [Matrix.trace_sum]
  apply Finset.sum_congr rfl
  intro i _
  rw [Matrix.smul_mul, Matrix.trace_smul]
  congr 1
  exact h_feas.2 i

/-! ## §2  Strong duality (Boyd-Vandenberghe Theorem 5.5)

The headline result: if the primal SDP `(P)` is Slater-strictly
feasible, then strong duality holds:
`inf{ ⟨T, Φ⟩ : Φ ⪰ 0, A_i Φ = b_i } = sup{ Σ b_i y_i : T - Σ y_i A_i ⪰ 0 }`.

The full proof requires convex-cone separation in
`Matrix.PosSemidef`, KKT conditions for matrix-cone constraints,
and value-function continuity. We package the conclusion as a
typeclass; concrete instances are the conjectural input. -/

/-- **Strong-duality pair** at an optimum.

    A primal point `Φstar`, a dual point `ystar`, and the two facts that
    make them a primal-dual optimal pair: `Φstar` is primal-feasible,
    the dual slack `S(ystar) = T - Σ ystar_i A_i` is PSD (dual
    feasibility), and the two objectives agree (zero duality gap).

    Until 2026-11-15 the last two fields were `True`, on the stated
    ground that PSD-ness "cannot be expressed without `[Fintype ι]` and
    `R := ℝ`".  Only the first half of that was right: `Matrix.PosSemidef`
    is defined over any `CommRing R` with `PartialOrder` and `StarRing`,
    which this file already assumes for `IsFeasible`.  `[Fintype ι]` is
    the only extra input, and it is carried here.  `RealStrongDualityPair`
    (`QOU.MathlibExt.SDPRealUniqueness`) states the same two fields at
    `R := ℝ`; see `StrongDualityPair.toReal`. -/
-- Ref: [boyd-vandenberghe-2004] §5.2.3, §5.3 (dual of an SDP, duality gap).
structure StrongDualityPair (sdp : SDPPrimal n R ι) where
  /-- Primal-optimal point. -/
  Φstar : Matrix (Fin n) (Fin n) R
  /-- Dual-optimal point. -/
  ystar : ι → R
  /-- Primal feasibility witness. -/
  primal_feas : sdp.IsFeasible Φstar
  /-- Dual feasibility: the dual slack `T - Σ ystar_i A_i` is PSD. -/
  dual_feas : (sdp.dualSlack ystar).PosSemidef
  /-- Zero duality gap: primal and dual objectives agree. -/
  obj_eq : sdp.objAt Φstar = sdp.dualObjAt ystar

/-- **Strong-duality typeclass**: witnesses that an SDP satisfies
    the primal-dual identity (Slater's condition + strong duality
    for convex problems, Boyd-Vandenberghe §5.2.3 + §5.3). -/
-- Ref: [boyd-vandenberghe-2004] §5.2.3 + §5.3 (Slater's condition
--      implies strong duality for convex problems).
--      Note: Boyd doesn't number theorems; "Theorem 5.5" was a
--      misattribution — the result is stated in §5.2.3 and proved
--      in §5.3.2.
-- NOTE (2026-11-20): primal strict feasibility ALONE does not give a pair.
--      `QOU.Mathlib.SDPStrongDuality.not_forall_hasStrongDuality` proves a
--      1×1 counterexample (cost −1, no constraints: strictly feasible,
--      unbounded below). For `R = ℝ` the class is proved under the extra
--      hypotheses symmetric data, linearly independent constraints and dual
--      Slater: `QOU.Mathlib.SDPStrongDuality.hasStrongDuality_of_slater`.
class HasStrongDuality (sdp : SDPPrimal n R ι)
    (_h : sdp.IsStrictlyFeasible) : Prop where
  /-- A strong-duality pair exists. -/
  pair : Nonempty (StrongDualityPair sdp)

/-- **Strong duality** (per-instance form).

    **Assumed, not derived here** — the body projects `HasStrongDuality.pair`
    verbatim, so existence of a strong-duality pair is carried by the
    context-class axiom (§3b-conditional, derivation pending) rather than
    proved from `sdp.IsStrictlyFeasible` below. Boyd–Vandenberghe is cited for
    the external convex-optimisation theorem motivating the class, not for a
    proof performed in this file. -/
-- Ref: [boyd-vandenberghe-2004] §5.2.3 + §5.3
--      (Slater's condition implies strong duality for convex problems;
--      Boyd doesn't number theorems — "Theorem 5.5" was a misattribution.)
theorem strong_duality (sdp : SDPPrimal n R ι)
    (h : sdp.IsStrictlyFeasible) [hStrong : HasStrongDuality sdp h] :
    Nonempty (StrongDualityPair sdp) :=
  hStrong.pair

/-! ## §3  Strict complementarity → primal-optimum uniqueness

The Boyd-Vandenberghe §5.5 strict-complementarity condition refines
the strong-duality witness with active/inactive partition data.
Under this strengthening, the primal optimum is *unique* (cf.
Todd 2001 §3.4).  We package both the certificate and the
uniqueness conclusion so downstream consumers (`QOU.BraidKnot.*`)
can apply them directly. -/

/-- **Strict-complementarity certificate.**

    Strengthens `StrongDualityPair` with the active/inactive
    partition of the constraint indices.  An index `i` is "active"
    iff its dual variable `ystar i` is strictly positive (constraint
    is binding); otherwise it is "inactive" with `ystar i = 0`.

    Concrete fields:
    * `active : Set ι` — the active set
    * `active_dual_pos` — `∀ i ∈ active, 0 < ystar i`
    * `inactive_dual_zero` — `∀ i ∉ active, ystar i = 0`

    The "strict" qualifier means the dichotomy is sharp: there is
    no ambiguous case where both `ystar i > 0` and the slack is
    positive.  This is the Todd 2001 §3.4 / Boyd-Vandenberghe §5.5
    formulation. -/
-- Ref: [boyd-vandenberghe-2004] §5.5 ("Strict complementarity")
-- Ref: [todd2001] §3.4
structure StrictComplementarityPair (sdp : SDPPrimal n R ι)
    extends StrongDualityPair sdp where
  /-- The active set: indices where the dual variable is positive. -/
  active : Set ι
  /-- On the active set, the dual variable is strictly positive. -/
  active_dual_pos : ∀ i ∈ active, 0 < ystar i
  /-- Off the active set, the dual variable is exactly zero. -/
  inactive_dual_zero : ∀ i ∉ active, ystar i = 0

/-! ## Primal-optimum uniqueness — REMOVED (it was false)

This module used to carry `strict_complementarity_unique_axiom` and two
theorems consuming it: `strict_complementarity_unique` and
`strict_complementarity_optimum_subsingleton`.

**All three asserted false propositions and have been deleted.**  The
refutation is `QOU.MathlibExt.SDPUniquenessCounterexamples.not_strict_complementarity_unique`
(sorry-free, depending on no QOU axiom): take `n = 1`, no constraints and
**zero cost**.  Every PSD matrix is then feasible with the same objective, so
`Φ⋆ = 0` and `Φ' = 1` both satisfy every hypothesis and the conclusion gives
`1 = 0`.

Alizadeh-Haeberly-Overton 1997 requires **dual nondegeneracy** for primal
uniqueness, not strict complementarity alone; the deleted statement omitted it
and was therefore strictly stronger than the theorem it cited.

**Where uniqueness now lives.**  Uniqueness is an ordered-field fact and is not
available over the generic `R` of this module, so it belongs downstream at `ℝ`:

* `QOU.MathlibExt.SDPRealUniqueness.real_strict_complementarity_unique_of_dualSlack_posDef`
  — the interior case, fully proved, hypothesis `(sdp.dualSlack sc.ystar).PosDef`.
* `QOU.MathlibExt.SDPRealUniqueness.SDPSlaterUniqueness` — the §3b-cond
  conditional class, with proven instances for the interior and
  active-empty-plus-cost-PosDef cases.

Every live QOU consumer has `cost = 1` and no constraints, hence
`dualSlack = 1`, which is positive-definite — so all of them satisfy the
interior hypothesis and lose nothing by the change.

Tracked in bean `qou-i6u4`.
-/

end QOU.MathlibExt.SDP
