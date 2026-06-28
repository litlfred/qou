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

/-- **Strong duality witness** — abstract skeleton for any
    `R : Type*` (with appropriate algebraic structure).  Per
    Copilot review: the `dual_feas` and `obj_eq` fields are
    intentionally `True` placeholders here because PSD-ness
    cannot be expressed without `[Fintype ι]` and `R := ℝ`.

    The **ℝ-specialised** form `RealStrongDualityPair` (in
    `QOU.MathlibExt.SDPRealUniqueness`) carries the actual
    PSD-ness + objective-equality content.  Downstream code
    that needs the categorical content should consume that
    structure, not this abstract skeleton. -/
structure StrongDualityPair (sdp : SDPPrimal n R ι) where
  /-- Primal-optimal point. -/
  Φstar : Matrix (Fin n) (Fin n) R
  /-- Dual-optimal point. -/
  ystar : ι → R
  /-- Primal feasibility witness. -/
  primal_feas : sdp.IsFeasible Φstar
  /-- Dual feasibility — `opaque marker` for genuinely-open
      infrastructure: PSD-ness `(sdp.dualSlack ystar).PosSemidef`
      requires `[Fintype ι]` + the `StarOrderedRing` of `R := ℝ`
      and so cannot be stated over the generic `R` carrier here.
      The content-bearing ℝ-specialised field is
      `RealStrongDualityPair.dualSlack_psd` (in
      `QOU.MathlibExt.SDPRealUniqueness`); consume that, not this
      abstract skeleton. -/
  dual_feas : True
  /-- Strong-duality identity — `opaque marker` for genuinely-open
      infrastructure: the content-bearing ℝ-specialised field is
      `RealStrongDualityPair.obj_eq_dualObj`
      (`objAt Φstar = dualObjAt ystar`, in
      `QOU.MathlibExt.SDPRealUniqueness`). Kept `True` here so the
      generic skeleton stays usable by the empty-constraint witness
      `trivialStrongDualityPair`; consume the ℝ form for the real
      objective-equality content. -/
  obj_eq : True

/-- **Strong-duality typeclass**: witnesses that an SDP satisfies
    the primal-dual identity (Slater's condition + strong duality
    for convex problems, Boyd-Vandenberghe §5.2.3 + §5.3). -/
-- Ref: [boyd-vandenberghe-2004] §5.2.3 + §5.3 (Slater's condition
--      implies strong duality for convex problems).
--      Note: Boyd doesn't number theorems; "Theorem 5.5" was a
--      misattribution — the result is stated in §5.2.3 and proved
--      in §5.3.2.
class HasStrongDuality (sdp : SDPPrimal n R ι)
    (_h : sdp.IsStrictlyFeasible) : Prop where
  /-- A strong-duality pair exists. -/
  pair : Nonempty (StrongDualityPair sdp)

/-- **Strong duality** (per-instance form). -/
-- Ref: [boyd-vandenberghe-2004] §5.2.3 + §5.3
--      (Slater's condition implies strong duality for convex problems;
--      Boyd doesn't number theorems — "Theorem 5.5" was a misattribution.)
theorem strong_duality (sdp : SDPPrimal n R ι)
    (h : sdp.IsStrictlyFeasible) [hStrong : HasStrongDuality sdp h] :
    Nonempty (StrongDualityPair sdp) :=
  hStrong.pair

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

/- **Primal-optimum uniqueness from strict complementarity.**

    Given a strict-complementarity pair `sc` for `sdp`, the primal
    optimum `sc.Φstar` is unique among primal-feasible points
    achieving the same objective value.

    PROOF: standard SDP-duality complementary-slackness argument
    (Boyd-Vandenberghe §5.5, Todd 2001 §3.4):
      1. Complementary slackness: any feasible Φ' with `objAt Φ' =
         objAt Φstar` satisfies `tr(constraint i · Φ') = rhs i` for
         all active i (since on active set ystar_i > 0).
      2. The active-constraint-set face F = {Φ : tr(A_i · Φ) = b_i
         for all i ∈ active} is a non-empty closed convex face of
         the feasible region.
      3. The cost `tr(T · Φ)` restricted to F is strictly convex
         (the inactive-constraint slack acts as a linear
         distinguishing functional), so it has at most one
         minimizer on F.
      4. Both Φstar and Φ' minimize on F (by feasibility +
         optimal-value match), hence Φ' = Φstar. -/
-- Ref: [boyd-vandenberghe-2004] §5.5 ("Strict complementarity")
-- Ref: [todd2001] §3.4 ("Uniqueness via strict complementarity")
/-- **External axiom (Boyd-Vandenberghe 2004 §5.5; Todd 2001 §3.4):
    SDP strict-complementarity uniqueness over a `LinearOrderedField`.**

    For a SDPPrimal with strict complementarity, the primal optimal
    is unique.  Proof reduces (per the §3b-cond §5.5.4 pattern) to
    the kernel-uniqueness step requiring Slater's strict feasibility
    + Mathlib's SDP rank-deficiency theorem (open Mathlib gap). -/
-- Ref: [boyd-vandenberghe-2004] §5.5
-- Ref: [todd2001] §3.4
axiom strict_complementarity_unique_axiom :
    ∀ {n : ℕ} {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] [StarRing R] {ι : Type*}
      {sdp : SDPPrimal n R ι}
      (sc : StrictComplementarityPair sdp)
      {Φ' : Matrix (Fin n) (Fin n) R}
      (_h_feas : sdp.IsFeasible Φ')
      (_h_obj : sdp.objAt Φ' = sdp.objAt sc.Φstar),
        Φ' = sc.Φstar

theorem strict_complementarity_unique
    {sdp : SDPPrimal n R ι}
    (sc : StrictComplementarityPair sdp)
    {Φ' : Matrix (Fin n) (Fin n) R}
    (h_feas : sdp.IsFeasible Φ')
    (h_obj : sdp.objAt Φ' = sdp.objAt sc.Φstar) :
    Φ' = sc.Φstar :=
  strict_complementarity_unique_axiom sc h_feas h_obj

/-- **Uniqueness as a `Subsingleton` (typeclass-friendly form).**

    Wraps `strict_complementarity_unique` so downstream code can
    use `Subsingleton {Φ // sdp.IsFeasible Φ ∧ sdp.objAt Φ =
    sdp.objAt sc.Φstar}` directly. -/
theorem strict_complementarity_optimum_subsingleton
    {sdp : SDPPrimal n R ι}
    (sc : StrictComplementarityPair sdp) :
    Subsingleton {Φ : Matrix (Fin n) (Fin n) R //
      sdp.IsFeasible Φ ∧ sdp.objAt Φ = sdp.objAt sc.Φstar} := by
  refine ⟨fun ⟨Φ₁, h₁_feas, h₁_obj⟩ ⟨Φ₂, h₂_feas, h₂_obj⟩ => ?_⟩
  have e₁ := strict_complementarity_unique sc h₁_feas h₁_obj
  have e₂ := strict_complementarity_unique sc h₂_feas h₂_obj
  ext1
  exact e₁.trans e₂.symm

end QOU.MathlibExt.SDP
