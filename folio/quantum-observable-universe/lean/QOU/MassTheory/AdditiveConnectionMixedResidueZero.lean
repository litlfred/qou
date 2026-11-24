/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import HeckeTemperleyLieb.HeckeStokesEigenvalues
import Mathlib.RingTheory.TensorProduct.Basic
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Additive Colour–Flavour Zero Mixed Residue & Bridge B Tensor-Square Stokes Discriminant (`qou-pdio`)

Formalizes two structural pillars of `NF-P2` (bean `qou-pdio`, also discharging the algebraic core
of `qou-et5f`) over generic commutative rings and fields (§7c, zero `ℝ`, zero empirical literals,
zero `sorry`):

1. **Zero Mixed Residue & Commuting Holonomy of Additive Colour–Flavour Connections.**
   For any additive logarithmic collision residue `Ω_{ab} = Ω_{ab}^{(c)} ⊗ 1 + 1 ⊗ Ω_{ab}^{(f)}`
   in `End_c ⊗_R End_f` (arising from `∇ = ∇_c ⊗ 1 + 1 ⊗ ∇_f` with zero direct colour–flavour
   gauge vertex):
   - For **any** `R`-linear projections `π_c : End_c →ₗ[R] M_c` and `π_f : End_f →ₗ[R] M_f` that
     annihilate the identity (`π_c(1) = 0`, `π_f(1) = 0`, e.g. traceless `𝔰𝔩_{N_c}` and `𝔰𝔩_{N_f}`
     projectors), the mixed bilinear projection `(π_c ⊗ π_f)(Ω_{ab})` vanishes identically
     (`mixedResidueProj_additive_eq_zero`), and the `P_c ⊗ₖ P_f` Schur–Weyl coefficient is `0`
     (`schurWeyl_additive_mixedCoeff_zero`).
   - The colour and flavour summands commute (`commute_inl_inr`, `commute_kronecker_additive`), so
     every truncated holonomy series factorises into `(∑ c_k Ω_c^k) ⊗ (∑ d_m Ω_f^m)`
     (`holonomy_series_factorizes`).

2. **Bridge B Rank-4 Tensor-Square KZ / Stokes Spectrum & Confluent Discriminant.**
   Whereas the single rank-2 Hecke/KZ quadratic `X² - (q - q⁻¹)X - 1 = (X - q)(X + q⁻¹)` has
   discriminant `Δ₁(q) = (q + q⁻¹)² = [2]_q²` (`Δ₁(1) = 4 ≠ 0`), the rank-4 tensor-square
   monodromy `(q, -q⁻¹)^{⊗ 2}` has eigenvalues `(q², -1, -1, q⁻²)` factoring as
   `(X + 1)² (X² - (q² + q⁻²)X + 1)` (`tensorSquare_charpoly_factors`):
   - Its inner `-1` block (hosting skew-Howe `(1³)_c ⊗ (3)_f` and `(3)_c ⊗ (1³)_f`) has
     discriminant `0` identically;
   - Its outer block `(q², q⁻²)` has confluent Stokes discriminant
     `Δ₂(q) = (q² + q⁻²)² - 4 = (q² - q⁻²)² = (q - q⁻¹)² · Δ₁(q)`
     (`tensorSquare_outer_discriminant`, `tensorSquare_discriminant_eq_h_sq_mul_hecke`), vanishing
     to order `2` in `h = q - q⁻¹` at `q = 1`.

-- Ref: [leitner2026] beans qou-pdio, qou-et5f, qou-qzvs
-- Ref: [kohno1987] Ann. Inst. Fourier 37 (1987) (holonomy of logarithmic connections)
-/

namespace QOU.Mass.AdditiveConnectionMixedResidueZero

open TensorProduct
open Matrix
open scoped Kronecker

/-! ## Section 1: Additive Colour–Flavour Zero Mixed Residue & Holonomy Factorisation -/

section AdditiveResidue

variable {R : Type*} [CommRing R]

section TensorAlgebra

variable {Ec Ef Mc Mf : Type*}
  [Ring Ec] [Algebra R Ec] [Ring Ef] [Algebra R Ef]
  [AddCommGroup Mc] [Module R Mc] [AddCommGroup Mf] [Module R Mf]

/-- Additive logarithmic collision residue `Ω_c ⊗ 1 + 1 ⊗ Ω_f` in `Ec ⊗[R] Ef`. -/
def additiveResidue (Ωc : Ec) (Ωf : Ef) : Ec ⊗[R] Ef :=
  Ωc ⊗ₜ[R] (1 : Ef) + (1 : Ec) ⊗ₜ[R] Ωf

/-- Bilinear mixed-residue projection `π_c ⊗ π_f : Ec ⊗[R] Ef →ₗ[R] Mc ⊗[R] Mf`. -/
def mixedResidueProj (πc : Ec →ₗ[R] Mc) (πf : Ef →ₗ[R] Mf) :
    Ec ⊗[R] Ef →ₗ[R] Mc ⊗[R] Mf :=
  TensorProduct.map πc πf

/-- **Unconditional vanishing of the mixed residue:** if `π_c(1) = 0` and `π_f(1) = 0`
(traceless / `End_0` projections), then `(π_c ⊗ π_f)(Ω_c ⊗ 1 + 1 ⊗ Ω_f) = 0`. -/
theorem mixedResidueProj_additive_eq_zero
    (πc : Ec →ₗ[R] Mc) (πf : Ef →ₗ[R] Mf)
    (hπc : πc 1 = 0) (hπf : πf 1 = 0) (Ωc : Ec) (Ωf : Ef) :
    mixedResidueProj πc πf (additiveResidue Ωc Ωf) = 0 := by
  simp [mixedResidueProj, additiveResidue, hπc, hπf]

/-- **Conversational witness for a mixed term:** on a pure mixed tensor `X_c ⊗ X_f`,
`mixedResidueProj` evaluates to `π_c(X_c) ⊗ π_f(X_f)`. -/
theorem mixedResidueProj_tmul (πc : Ec →ₗ[R] Mc) (πf : Ef →ₗ[R] Mf) (Xc : Ec) (Xf : Ef) :
    mixedResidueProj πc πf (Xc ⊗ₜ[R] Xf) = πc Xc ⊗ₜ[R] πf Xf := rfl

/-- **Exact commutation of colour and flavour residue summands in `Ec ⊗[R] Ef`.** -/
theorem commute_inl_inr (Ωc : Ec) (Ωf : Ef) :
    Commute (Ωc ⊗ₜ[R] (1 : Ef)) ((1 : Ec) ⊗ₜ[R] Ωf) := by
  rw [Commute, SemiconjBy, Algebra.TensorProduct.tmul_mul_tmul,
    Algebra.TensorProduct.tmul_mul_tmul, mul_one, one_mul, one_mul, mul_one]

/-- Pure-power identity `(Ω_c ⊗ 1)^k = Ω_c^k ⊗ 1`. -/
theorem tmul_one_pow (Ωc : Ec) : ∀ k : ℕ, (Ωc ⊗ₜ[R] (1 : Ef)) ^ k = (Ωc ^ k) ⊗ₜ[R] (1 : Ef)
  | 0 => by rw [pow_zero, pow_zero, Algebra.TensorProduct.one_def]
  | k + 1 => by
    rw [pow_succ, pow_succ, tmul_one_pow Ωc k, Algebra.TensorProduct.tmul_mul_tmul, one_mul]

/-- Pure-power identity `(1 ⊗ Ω_f)^m = 1 ⊗ Ω_f^m`. -/
theorem one_tmul_pow (Ωf : Ef) : ∀ m : ℕ, ((1 : Ec) ⊗ₜ[R] Ωf) ^ m = (1 : Ec) ⊗ₜ[R] (Ωf ^ m)
  | 0 => by rw [pow_zero, pow_zero, Algebra.TensorProduct.one_def]
  | m + 1 => by
    rw [pow_succ, pow_succ, one_tmul_pow Ωf m, Algebra.TensorProduct.tmul_mul_tmul, one_mul]

/-- **Polynomial / truncated-exponential holonomy factorisation:** for any coefficient sequences
`c, d : ℕ → R` and truncation orders `N, M`, the product of the colour and flavour holonomy
series in `Ec ⊗[R] Ef` equals the tensor product of the individual series. -/
theorem holonomy_series_factorizes (Ωc : Ec) (Ωf : Ef) (c d : ℕ → R) (N M : ℕ) :
    (∑ k ∈ Finset.range N, c k • (Ωc ⊗ₜ[R] (1 : Ef)) ^ k) *
      (∑ m ∈ Finset.range M, d m • ((1 : Ec) ⊗ₜ[R] Ωf) ^ m) =
      (∑ k ∈ Finset.range N, c k • Ωc ^ k) ⊗ₜ[R] (∑ m ∈ Finset.range M, d m • Ωf ^ m) := by
  simp_rw [tmul_one_pow, one_tmul_pow]
  rw [Finset.sum_mul, TensorProduct.sum_tmul]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [Finset.mul_sum, TensorProduct.tmul_sum]
  refine Finset.sum_congr rfl fun m _ => ?_
  rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm, Algebra.TensorProduct.tmul_mul_tmul,
    mul_one, one_mul, TensorProduct.smul_tmul_smul, smul_smul]

end TensorAlgebra

section KroneckerMatrix

variable {a b : Type*} [Fintype a] [DecidableEq a] [Fintype b] [DecidableEq b]

/-- **Exact commutation of Kronecker colour and flavour matrices `Ω_c ⊗ₖ 1` and `1 ⊗ₖ Ω_f`.** -/
theorem commute_kronecker_additive (Ωc : Matrix a a R) (Ωf : Matrix b b R) :
    Commute (Ωc ⊗ₖ (1 : Matrix b b R)) ((1 : Matrix a a R) ⊗ₖ Ωf) := by
  rw [Commute, SemiconjBy, ← Matrix.mul_kronecker_mul, ← Matrix.mul_kronecker_mul,
    Matrix.mul_one, Matrix.one_mul, Matrix.one_mul, Matrix.mul_one]

/-- Normalized traceless matrix projector `M - (d⁻¹ · tr(M)) • 1`. -/
def tracelessMatrixProj (dInv : R) (M : Matrix a a R) : Matrix a a R :=
  M - (dInv * Matrix.trace M) • (1 : Matrix a a R)

/-- `tracelessMatrixProj` kills `1` whenever `dInv * card(a) = 1`. -/
theorem tracelessMatrixProj_one (dInv : R) (hd : dInv * (Fintype.card a : R) = 1) :
    tracelessMatrixProj dInv (1 : Matrix a a R) = 0 := by
  unfold tracelessMatrixProj
  rw [Matrix.trace_one, hd, one_smul, sub_self]

omit [Fintype a] [Fintype b] in
/-- **Schur–Weyl commutant decomposition of an additive pair residue:**
`(α_c • 1 + β_c • P_c) ⊗ₖ 1 + 1 ⊗ₖ (α_f • 1 + β_f • P_f)` expands in `{1 ⊗ₖ 1, P_c ⊗ₖ 1,
1 ⊗ₖ P_f, P_c ⊗ₖ P_f}` with **identically zero** `P_c ⊗ₖ P_f` coefficient. -/
theorem schurWeyl_additive_mixedCoeff_zero
    (αc βc αf βf : R) (Pc : Matrix a a R) (Pf : Matrix b b R) :
    (αc • (1 : Matrix a a R) + βc • Pc) ⊗ₖ (1 : Matrix b b R) +
      (1 : Matrix a a R) ⊗ₖ (αf • (1 : Matrix b b R) + βf • Pf) =
      (αc + αf) • ((1 : Matrix a a R) ⊗ₖ (1 : Matrix b b R)) +
        βc • (Pc ⊗ₖ (1 : Matrix b b R)) +
        βf • ((1 : Matrix a a R) ⊗ₖ Pf) +
        (0 : R) • (Pc ⊗ₖ Pf) := by
  simp only [Matrix.add_kronecker, Matrix.kronecker_add, Matrix.smul_kronecker,
    Matrix.kronecker_smul, add_smul, zero_smul, add_zero]
  abel

end KroneckerMatrix

end AdditiveResidue

/-! ## Section 2: Bridge B Rank-4 Tensor-Square KZ / Stokes Eigenvalues & Confluent Discriminant -/

section BridgeBTensorSquareStokes

variable {K : Type*} [Field K]

/-- Discriminant `(q - q⁻¹)² + 4` of the rank-2 Hecke monodromy quadratic `X² - (q - q⁻¹)X - 1`. -/
def heckeDiscriminant (q : K) : K := (q - q⁻¹) ^ 2 + 4

/-- Discriminant `(q² + q⁻²)² - 4` of the outer rank-2 block `X² - (q² + q⁻²)X + 1` of the
rank-4 tensor-square monodromy. -/
def tensorSquareOuterDiscriminant (q : K) : K := (q ^ 2 + q⁻¹ ^ 2) ^ 2 - 4

/-- **Rank-2 Hecke discriminant equals `[2]_q² = (q + q⁻¹)²`.** -/
theorem heckeDiscriminant_eq_qd2_sq (q : K) (hq : q ≠ 0) :
    heckeDiscriminant q = (q + q⁻¹) ^ 2 := by
  unfold heckeDiscriminant
  field_simp
  ring

/-- **Rank-4 tensor-square characteristic polynomial factorisation:**
the four tensor-product eigenvalues `(q², -1, -1, q⁻²)` of `(q, -q⁻¹)^{⊗ 2}` factor as the
degenerate inner `-1` block `(X + 1)²` times the outer Stokes quadratic `X² - (q² + q⁻²)X + 1`. -/
theorem tensorSquare_charpoly_factors (q : K) (hq : q ≠ 0) (X : K) :
    (X - q ^ 2) * (X + 1) * (X + 1) * (X - q⁻¹ ^ 2) =
      (X + 1) ^ 2 * (X ^ 2 - (q ^ 2 + q⁻¹ ^ 2) * X + 1) := by
  field_simp
  ring

/-- **Exact confluent factorisation of the outer tensor-square Stokes discriminant:**
`Δ₂(q) = (q² - q⁻²)² = (q - q⁻¹)² (q + q⁻¹)²`. -/
theorem tensorSquare_outer_discriminant (q : K) (hq : q ≠ 0) :
    tensorSquareOuterDiscriminant q = (q - q⁻¹) ^ 2 * (q + q⁻¹) ^ 2 := by
  unfold tensorSquareOuterDiscriminant
  field_simp
  ring

/-- **Bridge B Stokes discriminant identity:** `Δ₂(q) = (q - q⁻¹)² · Δ₁(q)`. -/
theorem tensorSquare_discriminant_eq_h_sq_mul_hecke (q : K) (hq : q ≠ 0) :
    tensorSquareOuterDiscriminant q = (q - q⁻¹) ^ 2 * heckeDiscriminant q := by
  rw [tensorSquare_outer_discriminant q hq, heckeDiscriminant_eq_qd2_sq q hq]

/-- **Classical `q = 1` dichotomy:** at `q = 1`, the rank-2 Hecke discriminant is `4` (non-confluent
eigenvalues `±1`), whereas the tensor-square outer Stokes discriminant vanishes (`0`, confluent
coalescence of `q²` and `q⁻²` at `+1` alongside the inner `-1` double root). -/
theorem hecke_vs_tensorSquare_discriminant_at_one :
    heckeDiscriminant (1 : K) = 4 ∧ tensorSquareOuterDiscriminant (1 : K) = 0 := by
  unfold heckeDiscriminant tensorSquareOuterDiscriminant
  norm_num

end BridgeBTensorSquareStokes

end QOU.Mass.AdditiveConnectionMixedResidueZero
