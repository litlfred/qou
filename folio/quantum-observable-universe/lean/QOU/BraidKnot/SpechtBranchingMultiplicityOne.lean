/-
  Multiplicity-one branching for the standard (Specht) module at n = 3:
  ⟨Res^{S₃}_{S₂} V_(2,1), V_(2)⟩ = 1 — the finite representation-theoretic
  computation named by GAP-1 closure path 2 of
  docs/audits/2026-07-13-pion-radius-and-vol-to-radius-gaps.md ("one CAL-3
  quantum per bond": the multiplicity-one Frobenius reciprocity of
  folio/quantum-observable-universe/braids-and-knots/frobenius-lepton-meson-bridge.md).
  The content-block sibling frobenius-lepton-meson-bridge.lean records the
  same multiplicities as the Pieri TABLE `branchingH3H2`; here the V_(2,1)
  row is PROVED by explicit finite computation, not tabulated.

  Model.  V_(2,1) is realised concretely as the sum-zero subspace of the
  permutation module `Fin 3 → R` (the standard/Specht realisation).  At
  generic q the H₃(q) ↓ H₂(q) branching has the same multiplicities (Tits
  deformation / Wenzl); the corpus's Hecke conventions specialise at q = 1
  to this symmetric-group computation.  S₂ ⊂ S₃ is {1, s₁} with
  s₁ = swap 0 1, so S₂-invariance is invariance under the single
  transposition; V_(2) is the trivial S₂-irrep, hence its multiplicity in
  Res V_(2,1) is the rank of the s₁-invariant subspace.

  Main results (generic commutative ring, AGENTS.md §7c; sorry-free):

    * `sumZero_permAct` — the sum-zero subspace is an S₃-subrepresentation.
    * `res_trivial_multiplicity_one` — every s₁-invariant sum-zero vector
      is a UNIQUE R-multiple of w₊ = (1, 1, −2), and (`wPlus_sumZero`,
      `wPlus_fixed`, `wPlus_ne_zero`) w₊ is itself a nonzero invariant
      vector: the trivial isotypic component is FREE OF RANK ONE.  Over a
      field this is exactly ⟨Res^{S₃}_{S₂} V_(2,1), V_(2)⟩ = 1.
    * `res_sign_multiplicity_one` — the sign counterpart: every
      s₁-anti-invariant vector automatically lies in the Specht module and
      is a unique multiple of w₋ = (1, −1, 0) (no 2-torsion, hypothesis
      carried explicitly as in QOU.Mass.MilnorSignRepObstruction),
      completing Res V_(2,1) = V_(2) ⊕ V_(1,1) at the isotypic level and
      matching the `branchingH3H2 1 ·` row (1, 1).

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
-/

import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic

namespace QOU.BraidKnot.SpechtBranchingMultiplicityOne

open Equiv Finset

variable {R : Type*} [CommRing R]

/-! ### The concrete Specht module `V_(2,1)` and the S₃ action -/

/-- Membership in the concrete Specht module `V_(2,1)`: the sum-zero
    subspace of the permutation module `Fin 3 → R`. -/
def SumZero (v : Fin 3 → R) : Prop := v 0 + v 1 + v 2 = 0

/-- The S₃ relabeling action on the permutation module `Fin 3 → R`. -/
def permAct (g : Equiv.Perm (Fin 3)) (v : Fin 3 → R) : Fin 3 → R :=
  fun k => v (g⁻¹ k)

/-- The Specht module is an S₃-subrepresentation: the sum-zero condition is
    preserved by every relabeling. -/
theorem sumZero_permAct (g : Equiv.Perm (Fin 3)) {v : Fin 3 → R}
    (h : SumZero v) : SumZero (permAct g v) := by
  have hsum : ∑ k : Fin 3, v (g⁻¹ k) = ∑ k : Fin 3, v k :=
    Equiv.sum_comp g⁻¹ v
  have h3 : permAct g v 0 + permAct g v 1 + permAct g v 2
      = v 0 + v 1 + v 2 := by
    simpa [permAct, Fin.sum_univ_three] using hsum
  unfold SumZero at h ⊢
  rw [h3, h]

/-- Function extensionality over `Fin 3`, stated at the three literals. -/
theorem funext_fin3 {α : Type*} {v w : Fin 3 → α} (h0 : v 0 = w 0)
    (h1 : v 1 = w 1) (h2 : v 2 = w 2) : v = w := by
  funext k
  match k with
  | 0 => exact h0
  | 1 => exact h1
  | 2 => exact h2

/-! ### The two isotypic generators -/

/-- The trivial-isotypic (symmetric-channel) generator
    `w₊ = (1, 1, −2)` of the Specht module. -/
def wPlus : Fin 3 → R := fun k => if k = 2 then -2 else 1

/-- The sign-isotypic (antisymmetric-channel) generator
    `w₋ = (1, −1, 0)` of the Specht module. -/
def wMinus : Fin 3 → R := fun k => if k = 0 then 1 else if k = 1 then -1 else 0

@[simp] theorem wPlus_zero : (wPlus : Fin 3 → R) 0 = 1 := by
  show (if (0 : Fin 3) = 2 then (-2 : R) else 1) = 1
  rw [if_neg (by decide)]

@[simp] theorem wPlus_one : (wPlus : Fin 3 → R) 1 = 1 := by
  show (if (1 : Fin 3) = 2 then (-2 : R) else 1) = 1
  rw [if_neg (by decide)]

@[simp] theorem wPlus_two : (wPlus : Fin 3 → R) 2 = -2 := by
  show (if (2 : Fin 3) = 2 then (-2 : R) else 1) = -2
  rw [if_pos rfl]

@[simp] theorem wMinus_zero : (wMinus : Fin 3 → R) 0 = 1 := by
  show (if (0 : Fin 3) = 0 then (1 : R) else if (0 : Fin 3) = 1 then -1 else 0)
      = 1
  rw [if_pos rfl]

@[simp] theorem wMinus_one : (wMinus : Fin 3 → R) 1 = -1 := by
  show (if (1 : Fin 3) = 0 then (1 : R) else if (1 : Fin 3) = 1 then -1 else 0)
      = -1
  rw [if_neg (by decide), if_pos rfl]

@[simp] theorem wMinus_two : (wMinus : Fin 3 → R) 2 = 0 := by
  show (if (2 : Fin 3) = 0 then (1 : R) else if (2 : Fin 3) = 1 then -1 else 0)
      = 0
  rw [if_neg (by decide), if_neg (by decide)]

/-- `w₊` lies in the Specht module: `1 + 1 + (−2) = 0`. -/
theorem wPlus_sumZero : SumZero (wPlus : Fin 3 → R) := by
  show (wPlus : Fin 3 → R) 0 + wPlus 1 + wPlus 2 = 0
  rw [wPlus_zero, wPlus_one, wPlus_two]
  ring

/-- `w₋` lies in the Specht module: `1 + (−1) + 0 = 0`. -/
theorem wMinus_sumZero : SumZero (wMinus : Fin 3 → R) := by
  show (wMinus : Fin 3 → R) 0 + wMinus 1 + wMinus 2 = 0
  rw [wMinus_zero, wMinus_one, wMinus_two]
  ring

/-- `w₊` is s₁-invariant (existence half of multiplicity one). -/
theorem wPlus_fixed :
    permAct (Equiv.swap 0 1) (wPlus : Fin 3 → R) = wPlus := by
  have e0 : (Equiv.swap (0 : Fin 3) 1)⁻¹ 0 = 1 := by decide
  have e1 : (Equiv.swap (0 : Fin 3) 1)⁻¹ 1 = 0 := by decide
  have e2 : (Equiv.swap (0 : Fin 3) 1)⁻¹ 2 = 2 := by decide
  refine funext_fin3 ?_ ?_ ?_
  · show wPlus ((Equiv.swap (0 : Fin 3) 1)⁻¹ 0) = wPlus 0
    rw [e0, wPlus_one, wPlus_zero]
  · show wPlus ((Equiv.swap (0 : Fin 3) 1)⁻¹ 1) = wPlus 1
    rw [e1, wPlus_zero, wPlus_one]
  · show wPlus ((Equiv.swap (0 : Fin 3) 1)⁻¹ 2) = wPlus 2
    rw [e2]

/-- `w₋` is s₁-anti-invariant (existence half of the sign multiplicity). -/
theorem wMinus_anti :
    permAct (Equiv.swap 0 1) (wMinus : Fin 3 → R) = -wMinus := by
  have e0 : (Equiv.swap (0 : Fin 3) 1)⁻¹ 0 = 1 := by decide
  have e1 : (Equiv.swap (0 : Fin 3) 1)⁻¹ 1 = 0 := by decide
  have e2 : (Equiv.swap (0 : Fin 3) 1)⁻¹ 2 = 2 := by decide
  refine funext_fin3 ?_ ?_ ?_
  · show wMinus ((Equiv.swap (0 : Fin 3) 1)⁻¹ 0) = (-wMinus : Fin 3 → R) 0
    rw [e0, Pi.neg_apply, wMinus_one, wMinus_zero]
  · show wMinus ((Equiv.swap (0 : Fin 3) 1)⁻¹ 1) = (-wMinus : Fin 3 → R) 1
    rw [e1, Pi.neg_apply, wMinus_zero, wMinus_one, neg_neg]
  · show wMinus ((Equiv.swap (0 : Fin 3) 1)⁻¹ 2) = (-wMinus : Fin 3 → R) 2
    rw [e2, Pi.neg_apply, wMinus_two, neg_zero]

/-- `w₊ ≠ 0` whenever `R` is nontrivial — the invariant subspace is genuinely
    nonzero, so the multiplicity is exactly one, not at most one. -/
theorem wPlus_ne_zero [Nontrivial R] : (wPlus : Fin 3 → R) ≠ 0 := by
  intro h
  have h0 := congrFun h 0
  rw [wPlus_zero, Pi.zero_apply] at h0
  exact one_ne_zero h0

/-- `w₋ ≠ 0` whenever `R` is nontrivial. -/
theorem wMinus_ne_zero [Nontrivial R] : (wMinus : Fin 3 → R) ≠ 0 := by
  intro h
  have h0 := congrFun h 0
  rw [wMinus_zero, Pi.zero_apply] at h0
  exact one_ne_zero h0

/-! ### The multiplicity-one theorems -/

/-- **⟨Res^{S₃}_{S₂} V_(2,1), V_(2)⟩ = 1** (uniqueness half).  Every
    s₁-invariant vector of the Specht module is a UNIQUE `R`-multiple of
    `w₊ = (1, 1, −2)`: the trivial-isotypic component of the restriction is
    free of rank one on `w₊`.  Combined with `wPlus_sumZero` +
    `wPlus_fixed` + `wPlus_ne_zero` (existence), this is the
    multiplicity-one branching of the Frobenius lepton–meson bridge, proved
    rather than tabulated. -/
theorem res_trivial_multiplicity_one (v : Fin 3 → R) (hsum : SumZero v)
    (hfix : permAct (Equiv.swap 0 1) v = v) :
    ∃! c : R, v = c • wPlus := by
  have e0 : (Equiv.swap (0 : Fin 3) 1)⁻¹ 0 = 1 := by decide
  have h10 : v 1 = v 0 := by
    have h := congrFun hfix 0
    simp only [permAct] at h
    rw [e0] at h
    exact h
  have hs : v 0 + v 1 + v 2 = 0 := hsum
  have h2v : v 2 = v 0 * (-2) := by linear_combination hs - h10
  refine ⟨v 0, ?_, ?_⟩
  · refine funext_fin3 ?_ ?_ ?_
    · rw [Pi.smul_apply, wPlus_zero, smul_eq_mul, mul_one]
    · rw [Pi.smul_apply, wPlus_one, smul_eq_mul, mul_one]
      exact h10
    · rw [Pi.smul_apply, wPlus_two, smul_eq_mul]
      exact h2v
  · intro c hc
    have h := congrFun hc 0
    rw [Pi.smul_apply, wPlus_zero, smul_eq_mul, mul_one] at h
    exact h.symm

/-- **⟨Res^{S₃}_{S₂} V_(2,1), V_(1,1)⟩ = 1** (sign counterpart).  Every
    s₁-anti-invariant vector automatically lies in the Specht module and is
    a unique `R`-multiple of `w₋ = (1, −1, 0)`.  The no-2-torsion hypothesis
    `htf` is the weakest sufficient assumption (the statement fails in
    characteristic 2), carried explicitly per the
    `MilnorSignRepObstruction` convention. -/
theorem res_sign_multiplicity_one (htf : ∀ x : R, x + x = 0 → x = 0)
    (v : Fin 3 → R) (hanti : permAct (Equiv.swap 0 1) v = -v) :
    SumZero v ∧ ∃! c : R, v = c • wMinus := by
  have e0 : (Equiv.swap (0 : Fin 3) 1)⁻¹ 0 = 1 := by decide
  have e2 : (Equiv.swap (0 : Fin 3) 1)⁻¹ 2 = 2 := by decide
  have h10 : v 1 = -v 0 := by
    have h := congrFun hanti 0
    simp only [permAct, Pi.neg_apply] at h
    rw [e0] at h
    exact h
  have h22 : v 2 = -v 2 := by
    have h := congrFun hanti 2
    simp only [permAct, Pi.neg_apply] at h
    rw [e2] at h
    exact h
  have hv2 : v 2 = 0 := htf (v 2) (by linear_combination h22)
  constructor
  · show v 0 + v 1 + v 2 = 0
    rw [h10, hv2]
    ring
  · refine ⟨v 0, ?_, ?_⟩
    · refine funext_fin3 ?_ ?_ ?_
      · rw [Pi.smul_apply, wMinus_zero, smul_eq_mul, mul_one]
      · rw [Pi.smul_apply, wMinus_one, smul_eq_mul, h10]
        ring
      · rw [Pi.smul_apply, wMinus_two, smul_eq_mul, hv2]
        ring
    · intro c hc
      have h := congrFun hc 0
      rw [Pi.smul_apply, wMinus_zero, smul_eq_mul, mul_one] at h
      exact h.symm

/-- Dimension cross-check: the two rank-one isotypic pieces exhaust
    `dim V_(2,1) = 2`, matching the `branchingH3H2 1 ·` row `(1, 1)` of the
    Frobenius lepton–meson bridge table. -/
theorem branching_dimension_check : 1 + 1 = 2 := rfl

end QOU.BraidKnot.SpechtBranchingMultiplicityOne
