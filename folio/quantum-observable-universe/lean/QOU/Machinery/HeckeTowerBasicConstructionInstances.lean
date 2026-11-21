import QOU.Machinery.HeckeTowerBasicConstruction
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# `JonesBasicConstruction`: why the two-level form failed, and the three-level form

**History.** Until 2026-11-21 the class used two levels: the Jones projection
`e = jonesIdempotent q (σn1 n)` lay in `Hn1`, and absorption was required for
every `y : Hn1`, including `y = e`. With `e² = e` that forces `e = ι(ε e) · e`.
The class was restated with three levels (owner "Fix", bean `qou-c8p8`). The
defective two-level relation is kept here as the plain predicate
`SameLevelAbsorption`, so that the reason for the restatement stays checkable.

**What is proved (sorry-free).**
* `sameLevel_forces_e_eq_zero` — if same-level absorption holds, the generator
  satisfies the Hecke quadratic, `q ≠ 0`, `q + q⁻¹ ≠ 0`, and `ε(e) = τ • 1`
  with `τ ≠ 1`, then `e = 0`. A Markov conditional expectation has
  `τ = (q − z)/(q + q⁻¹)`, so `τ ≠ 1` holds at every Markov parameter except
  `z = −q⁻¹`.
* `not_sameLevel_halfTrace` / `sameLevel_corner` — a concrete model at `q = 2`
  in `M₂(ℚ)`. Same-level absorption fails for `ε = ½·trace` and holds only for
  the degenerate corner compression with `ε(e) = 1`.
* `jonesBasicConstruction_bottom` — the restated three-level class has a
  non-degenerate inhabitant at the bottom of the tower:
  `ℚ ⊂ ℚ ⊂ M₂(ℚ)`, `ε = id` (a genuine conditional expectation), and the genuine
  generator `σ = diag(2, −1/2)` on top, with `e = diag(0, 1) ≠ 0`.

**What is not proved.** The three-level relation for the Hecke tower
`H_n ⊂ H_{n+1} ⊂ H_{n+2}` at general `n`.

-- Ref: [leitner2026] QOU.Machinery.HeckeTowerBasicConstruction; [jones1983]
-- V. F. R. Jones, Index for subfactors, Invent. Math. 72 (1983), §3 (basic
-- construction, `e x e = E_N(x) e` for `x ∈ M`); [wenzl1988] §1.
-/

noncomputable section

namespace QOU.Machinery.HeckeTower.Instances

open QOU.Machinery.HeckeTower QOU.Machinery.HeckeBraidedCategory Matrix

/-- The **defective two-level** absorption relation that the class carried until
2026-11-21: `e · y · e = ι (ε y) · e` for every `y` in the algebra containing
`e = jonesIdempotent q (σn1 n)`. Kept as a plain predicate, not a class. -/
def SameLevelAbsorption {R : Type*} [Field R] (q : R)
    {Hn Hn1 : Type*} [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
    (σn1 : ℕ → Hn1) (ι : Hn →ₐ[R] Hn1) (ε : Hn1 →ₗ[R] Hn) (n : ℕ) : Prop :=
  ∀ y : Hn1, jonesIdempotent q (σn1 n) * y * jonesIdempotent q (σn1 n) =
    ι (ε y) * jonesIdempotent q (σn1 n)

/-- **Same-level absorption kills `e` at a scalar conditional expectation.** -/
theorem sameLevel_forces_e_eq_zero
    {R : Type*} [Field R] {q : R}
    {Hn Hn1 : Type*} [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
    {σn1 : ℕ → Hn1} {ι : Hn →ₐ[R] Hn1} {ε : Hn1 →ₗ[R] Hn} {n : ℕ}
    (habs : SameLevelAbsorption q σn1 ι ε n)
    (hq : q ≠ 0) (hd : q + q⁻¹ ≠ 0)
    (hs : σn1 n * σn1 n = (q - q⁻¹) • σn1 n + 1)
    (τ : R) (hτ : ε (jonesIdempotent q (σn1 n)) = τ • 1) (hτ1 : τ ≠ 1) :
    jonesIdempotent q (σn1 n) = 0 := by
  set e := jonesIdempotent q (σn1 n) with he
  have hidem : e * e = e := jonesIdempotent_mul_self q (σn1 n) hq hd hs
  have key := habs e
  rw [hidem, hidem, hτ, map_smul, map_one, smul_mul_assoc, one_mul] at key
  -- key : e = τ • e
  have h1 : (1 - τ) • e = 0 := by
    rw [sub_smul, one_smul, ← key, sub_self]
  have hne : (1 - τ) ≠ 0 := sub_ne_zero.mpr (Ne.symm hτ1)
  calc e = (1 - τ)⁻¹ • ((1 - τ) • e) := by rw [smul_smul, inv_mul_cancel₀ hne, one_smul]
    _ = 0 := by rw [h1, smul_zero]

/-! ## Concrete model at `q = 2` over `ℚ` -/

/-- The diagonal Hecke generator `diag(2, −1/2)`. -/
def σ2 : Matrix (Fin 2) (Fin 2) ℚ := Matrix.of ![![2, 0], ![0, -(2 : ℚ)⁻¹]]

/-- The constant generator family satisfies the (unbounded, hence every-rank)
Hecke braided presentation: the quadratic is `heckeQuadratic_h2`, and braid /
far-commutation hold because all generators coincide. -/
instance presentation_σ2 (rank : ℕ) :
    HeckeBraidedPresentationOfRank (2 : ℚ) rank (Matrix (Fin 2) (Fin 2) ℚ)
      (fun _ => σ2) where
  hecke_quadratic _ _ := heckeQuadratic_h2 (2 : ℚ) (by norm_num)
  braid_adjacent _ _ := rfl
  far_commute _ _ _ _ := rfl

/-- The unit map `ℚ → M₂(ℚ)`. -/
def ιQ : ℚ →ₐ[ℚ] Matrix (Fin 2) (Fin 2) ℚ := Algebra.ofId ℚ _

/-- Half the trace. -/
def halfTrace : Matrix (Fin 2) (Fin 2) ℚ →ₗ[ℚ] ℚ := (2 : ℚ)⁻¹ • Matrix.traceLinearMap (Fin 2) ℚ ℚ

/-- Compression to the `(1,1)` corner. -/
def corner : Matrix (Fin 2) (Fin 2) ℚ →ₗ[ℚ] ℚ :=
  { toFun := fun y => y 1 1
    map_add' := fun _ _ => rfl
    map_smul' := fun _ _ => rfl }

theorem ιQ_apply (x : ℚ) : ιQ x = x • (1 : Matrix (Fin 2) (Fin 2) ℚ) := by
  simp [ιQ, Algebra.algebraMap_eq_smul_one]

instance condExp_halfTrace (rank : ℕ) :
    HeckeConditionalExpectation ℚ 2 rank ℚ (Matrix (Fin 2) (Fin 2) ℚ)
      (fun _ => σ2) ιQ halfTrace where
  retract x := by
    rw [ιQ_apply]; simp [halfTrace]
  bimodule x z y := by
    rw [ιQ_apply, ιQ_apply]
    simp [halfTrace, Matrix.trace_fin_two]; ring

instance condExp_corner (rank : ℕ) :
    HeckeConditionalExpectation ℚ 2 rank ℚ (Matrix (Fin 2) (Fin 2) ℚ)
      (fun _ => σ2) ιQ corner where
  retract x := by
    rw [ιQ_apply]; simp [corner]
  bimodule x z y := by
    rw [ιQ_apply, ιQ_apply]
    simp [corner]; ring

theorem jones_σ2 : jonesIdempotent (2 : ℚ) σ2 = Matrix.of ![![0, 0], ![0, (1 : ℚ)]] :=
  jonesIdempotent_h2 (2 : ℚ) (by norm_num)

/-- **Refutation**: half-trace conditional expectation violates same-level
absorption. -/
theorem not_sameLevel_halfTrace (n : ℕ) :
    ¬ SameLevelAbsorption (2 : ℚ) (fun _ => σ2) ιQ halfTrace n := by
  intro h
  have key := h (jonesIdempotent (2 : ℚ) σ2)
  simp only at key
  rw [jones_σ2, ιQ_apply] at key
  have := congrFun (congrFun key 1) 1
  simp [halfTrace, Matrix.trace_fin_two, Matrix.mul_apply, Fin.sum_univ_two] at this

/-- **Degenerate inhabitant**: the corner compression (`ε(e) = 1`) satisfies
same-level absorption. -/
theorem sameLevel_corner (n : ℕ) :
    SameLevelAbsorption (2 : ℚ) (fun _ => σ2) ιQ corner n := by
  intro y
  simp only
  rw [jones_σ2, ιQ_apply]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [corner, Matrix.mul_apply, Fin.sum_univ_two, Matrix.vecMul, dotProduct]

/-! ## The restated three-level class at the bottom of the tower -/

/-- One strand carries no generators, so any family presents rank 1. -/
instance presentation_rank_one (σ : ℕ → ℚ) :
    HeckeBraidedPresentationOfRank (2 : ℚ) 1 ℚ σ where
  hecke_quadratic i hi := absurd hi (by omega)
  braid_adjacent i hi := absurd hi (by omega)
  far_commute _ j _ hj := absurd hj (by omega)

/-- The identity is a conditional expectation `ℚ → ℚ`. -/
instance condExp_id :
    HeckeConditionalExpectation ℚ 2 1 ℚ ℚ (fun _ => 0) (AlgHom.id ℚ ℚ)
      LinearMap.id where
  retract _ := rfl
  bimodule _ _ _ := rfl

/-- **Non-degenerate inhabitant of the restated class**: `ℚ ⊂ ℚ ⊂ M₂(ℚ)`,
`ε = id`, top generator `diag(2, −1/2)`, `e = diag(0, 1) ≠ 0`. -/
theorem jonesBasicConstruction_bottom :
    JonesBasicConstruction ℚ 2 1 ℚ ℚ (Matrix (Fin 2) (Fin 2) ℚ)
      (fun _ => 0) (fun _ => σ2) (AlgHom.id ℚ ℚ) LinearMap.id ιQ 0 where
  compat i hi := absurd hi (by omega)
  absorb y := by
    simp only [AlgHom.id_apply, LinearMap.id_apply]
    rw [jones_σ2, ιQ_apply]
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_two]

/-- The Jones projection in that inhabitant is nonzero. -/
theorem jones_σ2_ne_zero : jonesIdempotent (2 : ℚ) σ2 ≠ 0 := by
  rw [jones_σ2]
  intro h
  have := congrFun (congrFun h 1) 1
  simp at this

end QOU.Machinery.HeckeTower.Instances
