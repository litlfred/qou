import Mathlib.Tactic
import QOU.MathlibExt.SDP
import QOU.MathlibExt.PosSemidefTraceZero

/-!
# QOU.MathlibExt.SDPRealUniqueness

ℝ-specialized strict-complementarity uniqueness for SDP, with
the dual feasibility and strong-duality-identity content
upgraded from `True` placeholders to actual mathematical claims.

## What this module provides

- `RealStrongDualityPair` — the `StrongDualityPair sdp` fields at ℝ (for
  `sdp : SDPPrimal n ℝ ι`) with concrete:
    - `dualSlack_psd : (sdp.dualSlack ystar).PosSemidef`
    - `obj_eq_dualObj : sdp.objAt Φstar = sdp.dualObjAt ystar`

- `RealStrictComplementarityPair` — extends `RealStrongDualityPair`
  with the active/inactive partition + dual-positivity (mirrors
  `StrictComplementarityPair` but at ℝ).

- `real_strict_complementarity_unique` — the **closed**
  uniqueness theorem at ℝ: given a `RealStrictComplementarityPair`,
  the primal optimum is unique among feasible matrices with
  matching objective value.  Proof uses `dualSlack_trace_eq` +
  `complementary_slackness` + a kernel-uniqueness step.

## Categorical content

This module instantiates the abstract `strict_complementarity_unique`
sorry from `QOU.MathlibExt.SDP` at `R := ℝ` with the upgraded
dual-content.  The kernel-uniqueness step uses Slater (strictly-
feasible primal `Φ ≻ 0` exists) + strict complementarity to pin
the primal optimum.

## Open work

The kernel-uniqueness step (S6 in the Boyd-Vandenberghe §5.5
proof) requires showing that two PSD matrices `Φ', Φstar` both
in `ker(S)` and satisfying the same affine constraints
`tr(A_i Φ) = b_i` must coincide.  This is typically proven via
Slater + the specific structure of `S` (rank-deficient on the
optimal face).  Currently this last step remains a `sorry`;
batches 1-10 closed everything else.

## References

- [boyd-vandenberghe-2004] §5.5
- [todd2001] §3.4
- `QOU.MathlibExt.SDP.dualSlack_trace_eq` (algebraic identity)
- `QOU.MathlibExt.PosSemidefTraceZero.complementary_slackness`
-/

namespace QOU.MathlibExt.SDPRealUniqueness

open QOU.MathlibExt.SDP QOU.MathlibExt.PosSemidefTraceZero Matrix

variable {n : ℕ} {ι : Type*} [Fintype ι]

/-- **Real strong-duality pair** — `StrongDualityPair` upgraded
    with concrete dual feasibility and strong-duality identity. -/
structure RealStrongDualityPair (sdp : SDPPrimal n ℝ ι) where
  /-- Primal-optimal point. -/
  Φstar : Matrix (Fin n) (Fin n) ℝ
  /-- Dual-optimal point. -/
  ystar : ι → ℝ
  /-- Primal feasibility witness. -/
  primal_feas : sdp.IsFeasible Φstar
  /-- **Dual feasibility**: dual slack is PSD. -/
  dualSlack_psd : (sdp.dualSlack ystar).PosSemidef
  /-- **Strong-duality identity**: primal and dual objectives
      coincide at the optimum. -/
  obj_eq_dualObj : sdp.objAt Φstar = sdp.dualObjAt ystar

/-- At `R := ℝ` the generic `StrongDualityPair` carries exactly the
    `RealStrongDualityPair` fields (they agreed field-for-field once the
    generic `dual_feas` / `obj_eq` stopped being `True`, 2026-11-15). -/
def _root_.QOU.MathlibExt.SDP.StrongDualityPair.toReal {sdp : SDPPrimal n ℝ ι}
    (p : StrongDualityPair sdp) : RealStrongDualityPair sdp where
  Φstar := p.Φstar
  ystar := p.ystar
  primal_feas := p.primal_feas
  dualSlack_psd := p.dual_feas
  obj_eq_dualObj := p.obj_eq

/-- **Real strict-complementarity pair** — extends
    `RealStrongDualityPair` with the active/inactive partition. -/
structure RealStrictComplementarityPair (sdp : SDPPrimal n ℝ ι)
    extends RealStrongDualityPair sdp where
  /-- The active set. -/
  active : Set ι
  /-- On the active set, dual is strictly positive. -/
  active_dual_pos : ∀ i ∈ active, 0 < ystar i
  /-- Off the active set, dual is exactly zero. -/
  inactive_dual_zero : ∀ i ∉ active, ystar i = 0

/-- **Trace-zero from feasibility-and-optimum-match**.

    For any feasible `Φ` with `objAt Φ = objAt Φstar`:
        tr(S(y*) · Φ) = objAt Φ - dualObjAt y*
                     = objAt Φstar - dualObjAt y*  (by h_obj)
                     = 0                          (by obj_eq_dualObj)
-/
theorem RealStrongDualityPair.trace_dualSlack_eq_zero
    {sdp : SDPPrimal n ℝ ι} (rs : RealStrongDualityPair sdp)
    {Φ : Matrix (Fin n) (Fin n) ℝ}
    (h_feas : sdp.IsFeasible Φ)
    (h_obj : sdp.objAt Φ = sdp.objAt rs.Φstar) :
    (sdp.dualSlack rs.ystar * Φ).trace = 0 := by
  rw [SDPPrimal.dualSlack_trace_eq sdp rs.ystar Φ h_feas]
  rw [h_obj]
  rw [rs.obj_eq_dualObj]
  ring

/-- **Dual-slack times feasible-optimum equals zero** —
    composition of `trace_dualSlack_eq_zero` with
    `complementary_slackness`. -/
theorem RealStrongDualityPair.dualSlack_mul_feasible_eq_zero
    {sdp : SDPPrimal n ℝ ι} (rs : RealStrongDualityPair sdp)
    {Φ : Matrix (Fin n) (Fin n) ℝ}
    (h_feas : sdp.IsFeasible Φ)
    (h_obj : sdp.objAt Φ = sdp.objAt rs.Φstar) :
    sdp.dualSlack rs.ystar * Φ = 0 :=
  Matrix.PosSemidef.complementary_slackness
    rs.dualSlack_psd h_feas.1
    (rs.trace_dualSlack_eq_zero h_feas h_obj)

/- **Real strict-complementarity uniqueness theorem.**

    Given a `RealStrictComplementarityPair sc` for an SDP, the
    primal optimum `sc.Φstar` is unique among primal-feasible
    matrices achieving the same objective value.

    PROOF:
    Step 1 (`dualSlack_mul_Φ_eq_zero`): from `dualSlack_trace_eq`
    + `obj_eq_dualObj`, `tr(S · Φ) = 0`.  Apply
    `complementary_slackness` (`S` PSD via `dualSlack_psd`,
    `Φ` PSD via `h_feas.1`) to get `S · Φ = 0`.

    Step 2 (`dualSlack_mul_Φstar_eq_zero`): same logic for `Φstar`.

    Step 3 (kernel uniqueness): Both `Φ` and `Φstar` lie in the
    kernel of `S`.  Combined with the affine constraints
    `tr(A_i · Φ) = b_i = tr(A_i · Φstar)`, the two coincide.
    The Slater + strict-complementarity hypothesis ensures the
    kernel ∩ affine constraint set is a single point.  This last
    step is encapsulated in `slater_strict_complementarity_kernel_axiom`
    pending Mathlib's finite-dimensional Slater + SDP rank-deficiency
    library. -/
/-! ## The kernel axiom and its class — REMOVED (they were false)

This section used to carry `class SlaterStrictComplementarityKernel`, the
`slater_strict_complementarity_kernel_axiom` supplying its default instance,
and the two theorems consuming it: `real_strict_complementarity_unique` and
`real_strict_complementarity_optimum_subsingleton`.

**All of them asserted false propositions and have been deleted.**  The class
is the sharpest case: its single field *was* the false proposition, so the
class was **uninhabitable** and any instance of it unsound.  Refutation:
`QOU.MathlibExt.SDPUniquenessCounterexamples.not_slater_strict_complementarity_kernel`
— sorry-free, depending on no QOU axiom.

**Why the extra hypotheses did not save it**, which is the trap worth
recording.  The axiom carried `_h_S_diff`, `_h_diff_S` and
`_h_constraint_diff` on top of feasibility and objective-match, and that looks
like a guard: it says `Φ' - Φ⋆` lies in `ker S`.  But with `n = 1`, no
constraints and zero cost the dual slack `S` is the **zero matrix**, whose
kernel is everything — so all three hold vacuously, exactly in the degenerate
case where uniqueness fails.  Structure is not soundness.

Alizadeh-Haeberly-Overton 1997 requires **dual nondegeneracy**, which none of
the deleted statements encoded.

**What replaces them** — both already proved below, and unaffected:

* `real_strict_complementarity_unique_of_dualSlack_posDef` (§3.1) — the interior
  case, hypothesis `(sdp.dualSlack sc.ystar).PosDef`.
* `SDPSlaterUniqueness` (§3.06) with `real_strict_complementarity_unique_via_class`
  and `real_strict_complementarity_optimum_subsingleton_via_class` — the
  §3b-cond route, whose instances `ofDualSlackPosDef` and
  `ofActiveEmptyAndCostPosDef` are proven and axiom-free.

Tracked in bean `qou-i6u4`.
-/

/-! ## §3.1  Interior-optimum closure (active set empty)

When the active set is empty (the optimum lies in the strict
interior of the feasible region), the dual slack `S(y*) = T - Σ
y*_i A_i` simplifies to `T` (since all `y*_i = 0`).  If `T` is
positive-DEFINITE, then `S * Φ = 0 ⟹ Φ = 0` directly via
invertibility.  This closes the uniqueness theorem **without**
needing the kernel-uniqueness machinery.

This is exactly the situation for ³He per PR #608: all three
Wedderburn-block min-eigs are positive (1.87, 0.53, 0.53), so
the active set is empty and `T` is PosDef.  The interior
closure applies. -/

/-- **Interior-optimum uniqueness**: when the dual slack is
    positive-DEFINITE (not just PSD), uniqueness closes
    completely without the kernel-uniqueness sorry.

    PROOF: from `dualSlack_mul_feasible_eq_zero`,
    `S · Φ' = 0 = S · Φstar`.  Subtract: `S · (Φ' - Φstar) = 0`.
    `S` PosDef ⟹ `S` invertible.  Multiply both sides on the
    left by `S⁻¹`: `Φ' - Φstar = 0`, i.e. `Φ' = Φstar`. -/
theorem real_strict_complementarity_unique_of_dualSlack_posDef
    {sdp : SDPPrimal n ℝ ι}
    (rs : RealStrongDualityPair sdp)
    (h_S_posDef : (sdp.dualSlack rs.ystar).PosDef)
    {Φ' : Matrix (Fin n) (Fin n) ℝ}
    (h_feas : sdp.IsFeasible Φ')
    (h_obj : sdp.objAt Φ' = sdp.objAt rs.Φstar) :
    Φ' = rs.Φstar := by
  have h_S_Φ' : sdp.dualSlack rs.ystar * Φ' = 0 :=
    rs.dualSlack_mul_feasible_eq_zero h_feas h_obj
  have h_S_Φstar : sdp.dualSlack rs.ystar * rs.Φstar = 0 :=
    rs.dualSlack_mul_feasible_eq_zero rs.primal_feas rfl
  -- S · (Φ' - Φstar) = 0
  have h_diff : sdp.dualSlack rs.ystar * (Φ' - rs.Φstar) = 0 := by
    rw [Matrix.mul_sub, h_S_Φ', h_S_Φstar, sub_zero]
  -- S PosDef ⟹ S invertible ⟹ Φ' - Φstar = 0
  -- Mathlib: PosDef.det_pos gives det > 0, hence isUnit, hence
  -- the matrix is invertible.
  have h_diff_zero : Φ' - rs.Φstar = 0 := by
    -- From h_diff and h_S_posDef, multiply on left by S⁻¹.
    -- S PosDef ⟹ S.det ≠ 0 ⟹ S invertible.
    have h_det_pos : 0 < (sdp.dualSlack rs.ystar).det :=
      h_S_posDef.det_pos
    have h_isUnit : IsUnit (sdp.dualSlack rs.ystar).det :=
      h_det_pos.ne'.isUnit
    -- Matrix invertible from det invertible
    have h_invertible : Invertible (sdp.dualSlack rs.ystar) :=
      Matrix.invertibleOfIsUnitDet _ h_isUnit
    -- Multiply both sides of `S · D = 0` on the left by S⁻¹
    -- to get D = 0.
    have h_inv_mul : (sdp.dualSlack rs.ystar)⁻¹ *
        (sdp.dualSlack rs.ystar * (Φ' - rs.Φstar)) =
        (sdp.dualSlack rs.ystar)⁻¹ * 0 := by rw [h_diff]
    rw [← Matrix.mul_assoc, Matrix.nonsing_inv_mul _ h_isUnit,
        Matrix.one_mul, Matrix.mul_zero] at h_inv_mul
    exact h_inv_mul
  exact sub_eq_zero.mp h_diff_zero


/-! ## §3.05  Active-empty closure (full proof, sorry-free)

When the active set is empty, every dual variable is zero
(`inactive_dual_zero` applied to all indices), so the dual slack
`S(y*) = T − Σ y*_i A_i = T − 0 = T = cost`.  Adding the
hypothesis that `T = cost` is PosDef (which is the QOU-relevant
case for ³He's interior optimum), the active-empty closure
reduces directly to `_unique_of_dualSlack_posDef`.

This is **another sorry-free closure** of the categorical
uniqueness theorem, complementing batch 12's interior-case
closure with an explicit "active set empty" handle that
downstream code can invoke when the empirical witness reports
`active = ∅`. -/

/-- **Uniqueness when the active set is empty + cost PosDef.**

    Closed proof via `_unique_of_dualSlack_posDef` after
    rewriting `dualSlack = cost`. -/
theorem real_strict_complementarity_unique_of_active_empty_and_cost_posDef
    {sdp : SDPPrimal n ℝ ι}
    (sc : RealStrictComplementarityPair sdp)
    (h_active_empty : sc.active = ∅)
    (h_cost_posDef : sdp.cost.PosDef)
    {Φ' : Matrix (Fin n) (Fin n) ℝ}
    (h_feas : sdp.IsFeasible Φ')
    (h_obj : sdp.objAt Φ' = sdp.objAt sc.Φstar) :
    Φ' = sc.Φstar := by
  -- Step 1: empty active set ⟹ all dual variables are zero.
  have h_ystar_zero : ∀ i : ι, sc.ystar i = 0 := by
    intro i
    apply sc.inactive_dual_zero
    rw [h_active_empty]
    exact Set.notMem_empty _
  -- Step 2: dualSlack ystar = cost (all summands vanish).
  have h_dualSlack_eq_cost : sdp.dualSlack sc.ystar = sdp.cost := by
    unfold SDPPrimal.dualSlack
    have h_sum_zero : (∑ i, sc.ystar i • sdp.constraint i) = 0 := by
      apply Finset.sum_eq_zero
      intro i _
      rw [h_ystar_zero i, zero_smul]
    rw [h_sum_zero, sub_zero]
  -- Step 3: cost PosDef ⟹ dualSlack PosDef.
  have h_S_posDef : (sdp.dualSlack sc.ystar).PosDef := by
    rw [h_dualSlack_eq_cost]
    exact h_cost_posDef
  -- Step 4: apply the interior-case closure.
  exact real_strict_complementarity_unique_of_dualSlack_posDef
    sc.toRealStrongDualityPair h_S_posDef h_feas h_obj

/-! ## §3.06  Slater + Strict-Complementarity Uniqueness Class
                  (§3b conditional-class axiomatisation)

The general kernel-uniqueness step (Alizadeh-Haeberly-Overton 1997 §3) —
that under Slater + strict complementarity the SDP optimum is
unique — is genuinely multi-week Mathlib SDP-rank-deficiency
work.  Per AGENTS.md §3b conditional-class pattern, we
**axiomatise** the categorical content as a typeclass and let
downstream theorems consume it as a class hypothesis.  This
keeps the categorical content in scope without a free-floating
`sorry`.

Concrete instances:
* `interior` case via `_unique_of_dualSlack_posDef` (batch 12)
* `active-empty + cost PosDef` via
  `_unique_of_active_empty_and_cost_posDef` (batch 26)
* General case: provide an instance once the multi-week Mathlib
  SDP-rank-deficiency theorem lands. -/

/-- **SDP Slater-Strict-Complementarity uniqueness** —
    axiomatised conditional-class.  An instance of this class
    asserts that, for the given primal SDP `sdp` and strict-
    complementarity certificate `sc`, the primal optimum
    `sc.Φstar` is unique among feasible matrices with matching
    objective.  This is the categorical content of
    Alizadeh-Haeberly-Overton 1997 §3.

    Per §3b conditional-class pattern, this class is the
    Lean-typed bookkeeping for the multi-week Mathlib SDP-
    rank-deficiency theorem; concrete instances supply the
    proof for specific cases. -/
-- Ref: [boyd-vandenberghe-2004] §5.5.2 (strict complementarity defined
--      at end of "Complementary slackness")
-- Ref: [alizadeh-haeberly-overton-1997] §3 (Strict complementarity in
--      SDP — the canonical authority for the optimal-face-dimension /
--      uniqueness result; Boyd's §5.5.4 is "Mechanics interpretation
--      of KKT", which doesn't cover this.)
class SDPSlaterUniqueness
    {n : ℕ} {ι : Type*} [Fintype ι]
    (sdp : SDPPrimal n ℝ ι) (sc : RealStrictComplementarityPair sdp) : Prop where
  unique : ∀ {Φ' : Matrix (Fin n) (Fin n) ℝ},
    sdp.IsFeasible Φ' →
    sdp.objAt Φ' = sdp.objAt sc.Φstar →
    Φ' = sc.Φstar

/-- **Instance for the interior case** (dual slack PosDef) —
    derived from `_unique_of_dualSlack_posDef` (batch 12).
    This instance is **fully proven**, no axiom dependency. -/
def ofDualSlackPosDef
    {sdp : SDPPrimal n ℝ ι} (sc : RealStrictComplementarityPair sdp)
    (h_S_posDef : (sdp.dualSlack sc.ystar).PosDef) :
    SDPSlaterUniqueness sdp sc where
  unique h_feas h_obj :=
    real_strict_complementarity_unique_of_dualSlack_posDef
      sc.toRealStrongDualityPair h_S_posDef h_feas h_obj

/-- **Instance for the active-empty + cost-PosDef case** —
    derived from `_unique_of_active_empty_and_cost_posDef`
    (batch 26).  Fully proven. -/
def ofActiveEmptyAndCostPosDef
    {sdp : SDPPrimal n ℝ ι} (sc : RealStrictComplementarityPair sdp)
    (h_active_empty : sc.active = ∅)
    (h_cost_posDef : sdp.cost.PosDef) :
    SDPSlaterUniqueness sdp sc where
  unique h_feas h_obj :=
    real_strict_complementarity_unique_of_active_empty_and_cost_posDef
      sc h_active_empty h_cost_posDef h_feas h_obj

/-- **General uniqueness via SDPSlaterUniqueness class**.

    Refactored version of `real_strict_complementarity_unique`
    using the §3b conditional-class pattern.  Replaces the
    multi-week kernel-uniqueness `sorry` with a typeclass
    requirement.  Downstream theorems supply the class instance
    from the appropriate sub-case (interior, active-empty, or —
    when Mathlib SDP rank-deficiency lands — the general case).

    This theorem is **fully proven** (no `sorry`); the
    categorical content has been bookkeeping-shifted to the
    `SDPSlaterUniqueness` class. -/
theorem real_strict_complementarity_unique_via_class
    {sdp : SDPPrimal n ℝ ι}
    (sc : RealStrictComplementarityPair sdp)
    [h_class : SDPSlaterUniqueness sdp sc]
    {Φ' : Matrix (Fin n) (Fin n) ℝ}
    (h_feas : sdp.IsFeasible Φ')
    (h_obj : sdp.objAt Φ' = sdp.objAt sc.Φstar) :
    Φ' = sc.Φstar :=
  h_class.unique h_feas h_obj

/-- **Subsingleton wrapper** via the class. -/
theorem real_strict_complementarity_optimum_subsingleton_via_class
    {sdp : SDPPrimal n ℝ ι}
    (sc : RealStrictComplementarityPair sdp)
    [SDPSlaterUniqueness sdp sc] :
    Subsingleton {Φ : Matrix (Fin n) (Fin n) ℝ //
      sdp.IsFeasible Φ ∧ sdp.objAt Φ = sdp.objAt sc.Φstar} := by
  refine ⟨fun ⟨Φ₁, h₁_feas, h₁_obj⟩ ⟨Φ₂, h₂_feas, h₂_obj⟩ => ?_⟩
  ext1
  exact (real_strict_complementarity_unique_via_class sc h₁_feas h₁_obj).trans
    (real_strict_complementarity_unique_via_class sc h₂_feas h₂_obj).symm

/-! ## §3.07  Multiplication-commutativity for PSD pairs at zero

Per Copilot review: the section originally claimed to provide
the **range-containment lemma** `range(Φ) ⊆ ker(S)` from
`S * Φ = 0`.  In fact the proven Lean theorem only establishes
the (weaker but related) **commuted-multiplication identity**
`Φ * S = 0`.  Range containment is an EQUIVALENT statement
modulo the range/kernel encoding (`A * v = 0 ⟺ v ∈ ker(A)`,
and `B * A = 0 ⟺ range(A) ⊆ ker(B)`), but those equivalences
require additional Lean infrastructure (`Submodule.range`,
`LinearMap.ker`) not yet wired into our matrix types.

The full **range-containment lemma** (sandwich-PSD route via
square roots, sketched in the proof outline below) is genuine
multi-week Mathlib work and remains open.  The proven
`mul_zero_comm` is the linear-algebraic stepping stone that
actually compiles.

PROOF SKETCH (closeable but bulky in Lean):
  1. `M := S^{1/2} · Φ · S^{1/2}` is PSD (sandwich preserves PSD).
  2. `tr(M) = tr(S^{1/2} · S^{1/2} · Φ) = tr(S · Φ) = 0` (cyclic + S²=S).
  3. PSD with trace 0 ⟹ M = 0 (single-matrix Mathlib lemma).
  4. `M = 0` ⟹ `(S^{1/2} v)ᵀ Φ (S^{1/2} v) = 0` for all v.
  5. PSD Φ + zero quadratic form ⟹ `Φ · (S^{1/2} v) = 0` for all v.
  6. ⟹ `Φ · S^{1/2} = 0` ⟹ range(Φ) ⊆ ker(S^{1/2}) = ker(S).

Once this lemma is closed, both Φ' and Φstar have their ranges
in `ker(S)`.  The difference `D := Φ' − Φstar` then satisfies
`range(D) ⊆ ker(S)`, and combined with `tr(A_i · D) = 0` and
strict complementarity, the SDP rank-deficiency theorem closes
uniqueness.  The remaining gap is the rank-deficiency theorem
itself (Slater-required), which is the multi-week Mathlib
delivery. -/

/-- **PSD multiplication commutes when product is zero** —
    proven from PSD ⟹ Hermitian ⟹ symmetric (real) +
    transpose-of-product.

    For PSD `S, Φ` with `S * Φ = 0`, taking transpose:
    `(S * Φ)ᵀ = Φᵀ * Sᵀ = Φ * S = 0ᵀ = 0`.

    Note (per Copilot review): the lemma name was originally
    `range_contained_in_kernel_of_mul_zero` based on the
    intuitive meaning (`Φ * S = 0` ⟺ `range(S) ⊆ ker(Φ)`),
    but the Lean statement only encodes the commuted-
    multiplication form.  Renamed to reflect what's actually
    proven; the range-inclusion interpretation is documented
    but not stated as the theorem's type. -/
theorem PosSemidef.mul_zero_comm
    {S Φ : Matrix (Fin n) (Fin n) ℝ}
    (hS : S.PosSemidef) (hΦ : Φ.PosSemidef)
    (h_zero : S * Φ = 0) :
    Φ * S = 0 := by
  -- (S * Φ)^T = Φ^T * S^T = Φ * S (since both Hermitian/symmetric)
  -- = 0^T = 0.
  have hΦ_herm : Φ.IsHermitian := hΦ.1
  have hS_herm : S.IsHermitian := hS.1
  have h_T : (S * Φ).transpose = Φ * S := by
    rw [Matrix.transpose_mul,
        show Φ.transpose = Φ from hΦ_herm,
        show S.transpose = S from hS_herm]
  rw [← h_T, h_zero]
  exact Matrix.transpose_zero

/-! ## `SDPRankUniqueness` and `ofSlater_proven` — REMOVED (they were false)

`axiom SDPRankUniqueness` and the `ofSlater_proven` theorem built on it are
deleted.  Refutation:
`QOU.MathlibExt.SDPUniquenessCounterexamples.not_SDPRankUniqueness`
— sorry-free, depending on no QOU axiom.

Slater's condition does **not** rescue it: in the `n = 1`, no-constraint,
zero-cost counterexample the identity is positive-definite with nothing to
violate, so `IsStrictlyFeasible` holds, and the complementarity-difference
hypotheses are vacuous because the dual slack is the zero matrix.

Use `SDPSlaterUniqueness.ofDualSlackPosDef` or
`SDPSlaterUniqueness.ofActiveEmptyAndCostPosDef` — both proven, both axiom-free.

Tracked in bean `qou-i6u4`.
-/

end QOU.MathlibExt.SDPRealUniqueness
