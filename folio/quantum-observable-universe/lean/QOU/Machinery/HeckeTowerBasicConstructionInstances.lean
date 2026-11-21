import QOU.Machinery.HeckeTowerBasicConstruction
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# `JonesBasicConstruction` is mis-indexed: it forces `ε(e) = 1` on the Jones projection

The absorption field of `JonesBasicConstruction` reads
`e · y · e = ι(ε y) · e` for **every** `y : Hn1`, where the Jones projection
`e = jonesIdempotent q (σn1 n)` itself lies in `Hn1`. Taking `y = e` and using
`e² = e` gives `e = ι(ε e) · e`. In the Jones basic construction the relation
`e y e = E(y) e` is for `y` in the algebra *below* the one containing `e`
(`y ∈ H_{n+1}`, `e = e_{n+1} ∈ H_{n+2}`); with `y` allowed to be `e` the
relation pins `ε(e)` to act as `1` on `e`.

**What is proved (sorry-free).**
* `jonesProjection_eq_zero_of_scalar_expectation` — for any instance, if the
  generator `σn1 n` satisfies the Hecke quadratic, `q ≠ 0`, `q + q⁻¹ ≠ 0`, and
  `ε(e) = τ • 1` with `τ ≠ 1`, then `e = 0`. For a Markov conditional
  expectation `ε(e) = τ • 1` with `τ = (q − z)/(q + q⁻¹)`, so `τ ≠ 1` is every
  Markov parameter except `z = −q⁻¹`; and `e = 0` means `σn1 n = q • 1`. So the
  class cannot hold at a nondegenerate Markov trace with a genuine generator.
* A concrete refutation (`not_jonesBasicConstruction_halfTrace`): with
  `Hn = ℚ`, `Hn1 = M₂(ℚ)`, `σ = diag(2, −1/2)` (a genuine Hecke generator at
  `q = 2`, every rank), `ι` the unit map and `ε = ½·trace` (a conditional
  expectation), the class fails.
* A concrete inhabitant (`jonesBasicConstruction_corner`): the same data with
  `ε y = y₁₁` (compression to the `e`-corner) satisfies the class. So the class
  is satisfiable, but only for the degenerate `ε` with `ε(e) = 1`.

**What is not proved.** The genuine basic-construction relation for the Hecke
tower `H_n ⊂ H_{n+1} ⊂ H_{n+2}` (with `y ∈ H_{n+1}`, `e ∈ H_{n+2}`). Restating
the class with three levels is a refactor needing owner approval.

-- Ref: [leitner2026] QOU.Machinery.HeckeTowerBasicConstruction; [jones1983]
-- V. F. R. Jones, Index for subfactors, Invent. Math. 72 (1983), §3 (basic
-- construction, `e x e = E_N(x) e` for `x ∈ M`); [wenzl1988] §1.
-/

noncomputable section

namespace QOU.Machinery.HeckeTower.Instances

open QOU.Machinery.HeckeTower QOU.Machinery.HeckeBraidedCategory Matrix

/-- **Structural refutation at a scalar conditional expectation.** -/
theorem jonesProjection_eq_zero_of_scalar_expectation
    {R : Type*} [Field R] {q : R} {rank : ℕ}
    {Hn Hn1 : Type*} [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
    {σn1 : ℕ → Hn1} [HeckeBraidedPresentationOfRank q rank Hn1 σn1]
    {ι : Hn →ₐ[R] Hn1} {ε : Hn1 →ₗ[R] Hn}
    [HeckeConditionalExpectation R q rank Hn Hn1 σn1 ι ε] {n : ℕ}
    [hJ : JonesBasicConstruction R q rank Hn Hn1 σn1 ι ε n]
    (hq : q ≠ 0) (hd : q + q⁻¹ ≠ 0)
    (hs : σn1 n * σn1 n = (q - q⁻¹) • σn1 n + 1)
    (τ : R) (hτ : ε (jonesIdempotent q (σn1 n)) = τ • 1) (hτ1 : τ ≠ 1) :
    jonesIdempotent q (σn1 n) = 0 := by
  set e := jonesIdempotent q (σn1 n) with he
  have hidem : e * e = e := jonesIdempotent_mul_self q (σn1 n) hq hd hs
  have key := hJ.absorb e
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

/-- **Refutation**: half-trace conditional expectation violates absorption. -/
theorem not_jonesBasicConstruction_halfTrace (rank n : ℕ) :
    ¬ JonesBasicConstruction ℚ 2 rank ℚ (Matrix (Fin 2) (Fin 2) ℚ)
      (fun _ => σ2) ιQ halfTrace n := by
  intro h
  have key := h.absorb (jonesIdempotent (2 : ℚ) σ2)
  rw [jones_σ2, ιQ_apply] at key
  have := congrFun (congrFun key 1) 1
  simp [halfTrace, Matrix.trace_fin_two, Matrix.mul_apply, Fin.sum_univ_two] at this

/-- **Inhabitant**: the corner compression satisfies absorption. -/
theorem jonesBasicConstruction_corner (rank n : ℕ) :
    JonesBasicConstruction ℚ 2 rank ℚ (Matrix (Fin 2) (Fin 2) ℚ)
      (fun _ => σ2) ιQ corner n where
  absorb y := by
    rw [jones_σ2, ιQ_apply]
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [corner, Matrix.mul_apply, Fin.sum_univ_two, Matrix.vecMul, dotProduct]

end QOU.Machinery.HeckeTower.Instances
