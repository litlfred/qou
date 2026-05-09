/-!
# QOU.MathlibExt.SDPRealUniqueness

ℝ-specialized strict-complementarity uniqueness for SDP, with
the dual feasibility and strong-duality-identity content
upgraded from `True` placeholders to actual mathematical claims.

## What this module provides

- `RealStrongDualityPair` — extends `StrongDualityPair sdp` (for
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

import Mathlib.Tactic
import QOU.MathlibExt.SDP
import QOU.MathlibExt.PosSemidefTraceZero

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

/-- **Real strict-complementarity uniqueness theorem.**

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
    step requires a kernel-uniqueness lemma that depends on the
    specific SDP structure; left as `sorry` pending the
    finite-dimensional Slater argument. -/
theorem real_strict_complementarity_unique
    {sdp : SDPPrimal n ℝ ι}
    (sc : RealStrictComplementarityPair sdp)
    {Φ' : Matrix (Fin n) (Fin n) ℝ}
    (h_feas : sdp.IsFeasible Φ')
    (h_obj : sdp.objAt Φ' = sdp.objAt sc.Φstar) :
    Φ' = sc.Φstar := by
  -- Step 1 + 2: kernel containment via complementary slackness.
  have h_S_Φ' : sdp.dualSlack sc.ystar * Φ' = 0 :=
    sc.toRealStrongDualityPair.dualSlack_mul_feasible_eq_zero h_feas h_obj
  have h_S_Φstar : sdp.dualSlack sc.ystar * sc.Φstar = 0 :=
    sc.toRealStrongDualityPair.dualSlack_mul_feasible_eq_zero
      sc.primal_feas rfl
  -- Step 3: kernel uniqueness from Slater + strict comp.
  -- Subtract: `S · (Φ' - Φstar) = 0`.  Affine constraints match:
  -- `tr(A_i · (Φ' - Φstar)) = b_i - b_i = 0` for all i.
  -- Strict complementarity: on active i, ystar_i > 0; on
  -- inactive i, slacks differ.  Combined: Φ' - Φstar = 0.
  -- Full proof requires the kernel-uniqueness lemma.
  sorry

/-- **Subsingleton wrapper** for typeclass-friendly use. -/
theorem real_strict_complementarity_optimum_subsingleton
    {sdp : SDPPrimal n ℝ ι}
    (sc : RealStrictComplementarityPair sdp) :
    Subsingleton {Φ : Matrix (Fin n) (Fin n) ℝ //
      sdp.IsFeasible Φ ∧ sdp.objAt Φ = sdp.objAt sc.Φstar} := by
  refine ⟨fun ⟨Φ₁, h₁_feas, h₁_obj⟩ ⟨Φ₂, h₂_feas, h₂_obj⟩ => ?_⟩
  ext1
  rw [real_strict_complementarity_unique sc h₁_feas h₁_obj,
      real_strict_complementarity_unique sc h₂_feas h₂_obj]

end QOU.MathlibExt.SDPRealUniqueness
