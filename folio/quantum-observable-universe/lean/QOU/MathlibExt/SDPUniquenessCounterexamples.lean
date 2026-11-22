/-
# SDP uniqueness: explicit counterexamples

Five axioms in the `QOU.MathlibExt` SDP ladder assert that a primal
optimum is unique given strict complementarity.  **All five statements
are false**, and this file proves it — not by exhibiting a proof from
the axioms, but by refuting the propositions outright, so the results
survive deletion of the axioms and prevent the statements from being
restated.

## The mathematics

Alizadeh–Haeberly–Overton 1997 does not say that strict complementarity
implies a unique primal optimum.  It says the primal optimum is unique
**iff the dual is nondegenerate**, given strict complementarity.  None of
the five axioms carried a nondegeneracy hypothesis, so each asserted a
strictly stronger — and false — proposition than the paper it cited.

## The two counterexamples

* `zeroSDP` — `n = 1`, no constraints, **zero cost**.  Every PSD matrix
  is feasible, the objective is identically `0`, and the dual slack
  `S = cost - Σ yᵢ Aᵢ` is the **zero matrix**.  So `Φ⋆ = 0` and `Φ' = 1`
  are both optimal.  Crucially the complementarity-difference hypotheses
  (`S * (Φ' - Φ⋆) = 0`) hold *vacuously*, because `S = 0` has full
  kernel — they look like a guard and constrain nothing.

* `rankSDP` — `n = 2`, no constraints, `cost = diag(1,0)`.  This one
  additionally satisfies the rank guard `rank Φ⋆ + rank S = n`
  (`1 + 1 = 2`), which `zeroSDP` fails, and is needed to refute
  `affine_slater_rigidity`.

Both are Slater-strictly-feasible (the identity is positive-definite and
there are no constraints to violate), so no Slater hypothesis rules them
out either.

-- Ref: [alizadeh-haeberly-overton-1997] §3 (uniqueness requires dual
--      nondegeneracy, not strict complementarity alone)
-- Ref: [boyd-vandenberghe-2004] §5.5.2
-/
import QOU.MathlibExt.SDPRankEquality

set_option autoImplicit false

namespace QOU.MathlibExt.SDPUniquenessCounterexamples

open Matrix QOU.MathlibExt.SDP QOU.MathlibExt.SDPRealUniqueness

/-! ## Positive-(semi)definiteness helpers

`Matrix.PosDef.one` and `Matrix.posSemidef_diagonal_iff` both require a
`StarOrderedRing ℝ` instance, so these are proved by hand. -/

/-- The identity matrix is positive-definite over `ℝ`. -/
theorem posdef_one (n : ℕ) : (1 : Matrix (Fin n) (Fin n) ℝ).PosDef := by
  constructor
  · simp [Matrix.IsHermitian]
  · intro x hx
    have ⟨i, hi⟩ : ∃ i, x i ≠ 0 := by
      by_contra h; push_neg at h; exact hx (funext h)
    simp only [Matrix.one_mulVec, dotProduct, Pi.star_apply, star_trivial]
    exact Finset.sum_pos' (fun j _ => mul_self_nonneg _)
      ⟨i, Finset.mem_univ i, mul_self_pos.mpr hi⟩

/-- A real diagonal matrix with non-negative entries is PSD. -/
theorem psd_diag {n : ℕ} (w : Fin n → ℝ) (hw : ∀ i, 0 ≤ w i) :
    (Matrix.diagonal w).PosSemidef := by
  constructor
  · exact Matrix.isHermitian_diagonal_iff.mpr (fun i => star_trivial _)
  · intro x
    simp only [dotProduct, Matrix.mulVec_diagonal, Pi.star_apply, star_trivial]
    refine Finset.sum_nonneg fun i _ => ?_
    have h : x i * (w i * x i) = w i * (x i * x i) := by ring
    rw [h]; exact mul_nonneg (hw i) (mul_self_nonneg _)

/-- The zero matrix is PSD over `ℝ`. -/
theorem psd_zero (n : ℕ) : (0 : Matrix (Fin n) (Fin n) ℝ).PosSemidef := by
  constructor
  · simp [Matrix.IsHermitian]
  · intro x; simp [dotProduct]

/-! ## Counterexample 1 — `n = 1`, no constraints, zero cost -/

/-- One dimension, no constraints, **zero** cost: every PSD matrix is
    optimal and the dual slack is the zero matrix. -/
def zeroSDP : SDPPrimal 1 ℝ Empty where
  cost := 0
  constraint := fun i => i.elim
  rhs := fun i => i.elim

theorem zeroSDP_dualSlack (y : Empty → ℝ) : zeroSDP.dualSlack y = 0 := by
  simp [SDPPrimal.dualSlack, zeroSDP]

theorem zeroSDP_strictlyFeasible : zeroSDP.IsStrictlyFeasible :=
  ⟨1, posdef_one 1, fun i => i.elim⟩

theorem zeroSDP_feasible_one : zeroSDP.IsFeasible 1 :=
  ⟨(posdef_one 1).posSemidef, fun i => i.elim⟩

theorem zeroSDP_feasible_zero : zeroSDP.IsFeasible 0 :=
  ⟨psd_zero 1, fun i => i.elim⟩

/-- The generic strict-complementarity pair at `Φ⋆ = 0`.  The dual
    slack of `zeroSDP` is `0`, so dual feasibility and the zero gap hold
    for the same reason as in `rsc` below. -/
def scPair : StrictComplementarityPair zeroSDP where
  Φstar := 0
  ystar := fun i => i.elim
  primal_feas := zeroSDP_feasible_zero
  dual_feas := by
    rw [zeroSDP_dualSlack]; exact psd_zero 1
  obj_eq := by simp [SDPPrimal.objAt, SDPPrimal.dualObjAt, zeroSDP]
  active := ∅
  active_dual_pos := fun i hi => hi.elim
  inactive_dual_zero := fun i _ => i.elim

/-- The ℝ-layer strict-complementarity pair at `Φ⋆ = 0`.  Unlike
    `scPair` this one discharges *genuine* `dualSlack_psd` and
    `obj_eq_dualObj` fields — the extra structure does not help,
    because the dual slack is zero. -/
def rsc : RealStrictComplementarityPair zeroSDP where
  Φstar := 0
  ystar := fun i => i.elim
  primal_feas := zeroSDP_feasible_zero
  dualSlack_psd := by
    rw [zeroSDP_dualSlack]; exact psd_zero 1
  obj_eq_dualObj := by simp [SDPPrimal.objAt, SDPPrimal.dualObjAt, zeroSDP]
  active := ∅
  active_dual_pos := fun i hi => hi.elim
  inactive_dual_zero := fun i _ => i.elim

theorem one_ne_zero_matrix : (1 : Matrix (Fin 1) (Fin 1) ℝ) ≠ 0 := by
  intro h
  have h00 := congrFun (congrFun h 0) 0
  simp at h00

/-! ## Counterexample 2 — `n = 2`, no constraints, `cost = diag(1,0)`

This one additionally meets the rank guard `rank Φ⋆ + rank S = n`. -/

/-- Two dimensions, no constraints, `cost = diag(1,0)`. -/
def rankSDP : SDPPrimal 2 ℝ Empty where
  cost := Matrix.diagonal ![1, 0]
  constraint := fun i => i.elim
  rhs := fun i => i.elim

theorem rankSDP_dualSlack (y : Empty → ℝ) :
    rankSDP.dualSlack y = Matrix.diagonal ![1, 0] := by
  simp [SDPPrimal.dualSlack, rankSDP]

/-- `Φ⋆ = diag(0,1)`: PSD, feasible, and objective-matching, since
    `tr(diag(1,0) * diag(0,1)) = 0`. -/
def rsc2 : RealStrictComplementarityPair rankSDP where
  Φstar := Matrix.diagonal ![0, 1]
  ystar := fun i => i.elim
  primal_feas := ⟨psd_diag _ (by intro i; fin_cases i <;> norm_num), fun i => i.elim⟩
  dualSlack_psd := by
    rw [rankSDP_dualSlack]
    exact psd_diag _ (by intro i; fin_cases i <;> norm_num)
  obj_eq_dualObj := by
    simp [SDPPrimal.objAt, SDPPrimal.dualObjAt, rankSDP, Matrix.diagonal_mul_diagonal,
      Matrix.trace_diagonal, Fin.sum_univ_two]
  active := ∅
  active_dual_pos := fun i hi => hi.elim
  inactive_dual_zero := fun i _ => i.elim

theorem rank_d01 : (Matrix.diagonal ![(0:ℝ), 1]).rank = 1 := by
  rw [Matrix.rank_diagonal, Fintype.card_subtype]
  have h : (Finset.univ.filter (fun i : Fin 2 => ![(0:ℝ), 1] i ≠ 0)) = {1} := by
    ext i; fin_cases i <;> simp
  rw [h]; rfl

theorem rank_d10 : (Matrix.diagonal ![(1:ℝ), 0]).rank = 1 := by
  rw [Matrix.rank_diagonal, Fintype.card_subtype]
  have h : (Finset.univ.filter (fun i : Fin 2 => ![(1:ℝ), 0] i ≠ 0)) = {0} := by
    ext i; fin_cases i <;> simp
  rw [h]; rfl

/-- The rank guard `rank Φ⋆ + rank S = n` is **satisfied** here. -/
theorem rankSDP_rank_eq :
    rsc2.Φstar.rank + (rankSDP.dualSlack rsc2.ystar).rank = 2 := by
  rw [rankSDP_dualSlack]
  show (Matrix.diagonal ![(0:ℝ), 1]).rank + (Matrix.diagonal ![(1:ℝ), 0]).rank = 2
  rw [rank_d01, rank_d10]

/-! ## The five refutations

Each theorem below negates the proposition asserted by one of the five
SDP axioms.  They are stated at `ℝ`; for the two axioms quantified over
a general ordered `*`-ring, refuting the `ℝ` instance refutes the
general statement a fortiori. -/

/-- **`strict_complementarity_unique_axiom` is FALSE.**
    (`QOU/MathlibExt/SDP.lean`) -/
theorem not_strict_complementarity_unique :
    ¬ (∀ {n : ℕ} {ι : Type} {sdp : SDPPrimal n ℝ ι} [Fintype ι]
        (sc : StrictComplementarityPair sdp)
        {Φ' : Matrix (Fin n) (Fin n) ℝ},
          sdp.IsFeasible Φ' → sdp.objAt Φ' = sdp.objAt sc.Φstar →
            Φ' = sc.Φstar) := by
  intro h
  refine one_ne_zero_matrix ?_
  exact h scPair zeroSDP_feasible_one
    (by simp [SDPPrimal.objAt, zeroSDP, scPair])

/-- **`slater_strict_complementarity_kernel_axiom` is FALSE** — the
    complementarity-difference hypotheses hold vacuously when `S = 0`.
    (`QOU/MathlibExt/SDPRealUniqueness.lean`) -/
theorem not_slater_strict_complementarity_kernel :
    ¬ (∀ {n : ℕ} {ι : Type} [Fintype ι] {sdp : SDPPrimal n ℝ ι}
        (sc : RealStrictComplementarityPair sdp)
        {Φ' : Matrix (Fin n) (Fin n) ℝ},
          sdp.IsFeasible Φ' →
          sdp.objAt Φ' = sdp.objAt sc.Φstar →
          (∀ i : ι, Matrix.trace (sdp.constraint i * (Φ' - sc.Φstar)) = 0) →
          sdp.dualSlack sc.ystar * (Φ' - sc.Φstar) = 0 →
          (Φ' - sc.Φstar) * sdp.dualSlack sc.ystar = 0 →
            Φ' = sc.Φstar) := by
  intro h
  refine one_ne_zero_matrix ?_
  exact h rsc zeroSDP_feasible_one
    (by simp [SDPPrimal.objAt, zeroSDP, rsc])
    (fun i => i.elim)
    (by rw [zeroSDP_dualSlack]; simp)
    (by rw [zeroSDP_dualSlack]; simp)

/-- **`SDPRankUniqueness` is FALSE** — Slater's condition holds too.
    (`QOU/MathlibExt/SDPRealUniqueness.lean`) -/
theorem not_SDPRankUniqueness :
    ¬ (∀ {n : ℕ} {ι : Type} [Fintype ι] (sdp : SDPPrimal n ℝ ι)
        (sc : RealStrictComplementarityPair sdp),
          sdp.IsStrictlyFeasible →
          ∀ {Φ' : Matrix (Fin n) (Fin n) ℝ},
            sdp.IsFeasible Φ' →
            sdp.dualSlack sc.ystar * (Φ' - sc.Φstar) = 0 →
            (∀ i : ι, Matrix.trace (sdp.constraint i * (Φ' - sc.Φstar)) = 0) →
              Φ' = sc.Φstar) := by
  intro h
  refine one_ne_zero_matrix ?_
  exact h zeroSDP rsc zeroSDP_strictlyFeasible zeroSDP_feasible_one
    (by rw [zeroSDP_dualSlack]; simp)
    (fun i => i.elim)

/-- **`strict_complementarity_kernel_disjoint` is FALSE** — with
    `Φ⋆ = 0` and `S = 0` every vector is in both kernels.
    (`QOU/MathlibExt/SDPRankEquality.lean`) -/
theorem not_strict_complementarity_kernel_disjoint :
    ¬ (∀ {n : ℕ} {ι : Type} [Fintype ι] {sdp : SDPPrimal n ℝ ι}
        (sc : RealStrictComplementarityPair sdp),
          sdp.IsStrictlyFeasible →
          ∀ v : Fin n → ℝ,
            sc.Φstar.mulVec v = 0 →
            (sdp.dualSlack sc.ystar).mulVec v = 0 →
              v = 0) := by
  intro h
  have hv := h rsc zeroSDP_strictlyFeasible (fun _ => (1 : ℝ))
    (by simp [rsc])
    (by rw [zeroSDP_dualSlack]; simp)
  have := congrFun hv 0
  simp at this

/-- **`affine_slater_rigidity` is FALSE** — and this refutation
    *satisfies* its rank guard `rank Φ⋆ + rank S = n`.
    (`QOU/MathlibExt/SDPRankEquality.lean`) -/
theorem not_affine_slater_rigidity :
    ¬ (∀ {n : ℕ} {ι : Type} [Fintype ι] {sdp : SDPPrimal n ℝ ι}
        (sc : RealStrictComplementarityPair sdp),
          sdp.IsStrictlyFeasible →
          sc.Φstar.rank + (sdp.dualSlack sc.ystar).rank = n →
          ∀ {D : Matrix (Fin n) (Fin n) ℝ},
            D.IsHermitian →
            sdp.dualSlack sc.ystar * D = 0 →
            (∀ i : ι, Matrix.trace (sdp.constraint i * D) = 0) →
              D = 0) := by
  intro h
  have hD : (Matrix.diagonal ![(0:ℝ), 1] : Matrix (Fin 2) (Fin 2) ℝ) = 0 :=
    h rsc2 ⟨1, posdef_one 2, fun i => i.elim⟩ rankSDP_rank_eq
      (Matrix.isHermitian_diagonal_iff.mpr (fun i => star_trivial _))
      (by rw [rankSDP_dualSlack, Matrix.diagonal_mul_diagonal]
          ext i j; fin_cases i <;> fin_cases j <;> simp)
      (fun i => i.elim)
  have := congrFun (congrFun hD 1) 1
  simp [Matrix.diagonal] at this

end QOU.MathlibExt.SDPUniquenessCounterexamples
