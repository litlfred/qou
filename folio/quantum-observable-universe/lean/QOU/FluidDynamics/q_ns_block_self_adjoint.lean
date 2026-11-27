import QOU.FluidDynamics.q_ns_block_pairing_nondegenerate
import QOU.FluidDynamics.q_ns_block_weight_lap
import QOU.FluidDynamics.q_ns_block_ladder_negative
import QOU.FluidDynamics.q_ns_haar_field_invariance_full

/-!
# QOU.FluidDynamics.q_ns_block_self_adjoint — `L` is self-adjoint on every weight block

(docstring filled in below)
-/

namespace QOU.FluidDynamics.BlockLadder

open Polynomial QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2 QOU.FluidDynamics.BlockLadderNeg

section Left

variable {K : Type*} [Field K] (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))

/-- `tw(βδ) = q² βδ`. -/
theorem tw_betaDelta :
    torusScaleAlgHom (R := K) q q⁻¹ q⁻¹⁻¹ (β q * δ q) = ((q : K) * q) • (β q * δ q) := by
  obtain ⟨-, hb, -, hd⟩ := field_twist_generators (R := K) q
  rw [map_mul, hb, hd, smul_mul_smul_comm]

theorem tw_betaDelta_pow (r : ℕ) :
    torusScaleAlgHom (R := K) q q⁻¹ q⁻¹⁻¹ ((β q * δ q) ^ r) =
      ((q : K) * q) ^ r • (β q * δ q) ^ r := by
  rw [map_pow, tw_betaDelta, smul_pow]

/-- `(βδ)^n ζ = q^{-2n} ζ (βδ)^n`. -/
theorem betaDelta_pow_zeta (n : ℕ) :
    (β (R := K) q * δ q) ^ n * zetaB q = (qi * qi) ^ n • (zetaB q * (β q * δ q) ^ n) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, mul_assoc, betaDelta_zeta, mul_smul_comm, ← mul_assoc, ih, smul_mul_assoc,
      smul_smul, mul_assoc (zetaB q), ← pow_succ]
    congr 1; ring

/-- **`X₊` on `(βδ)^{r+1}`.**
`X₊((βδ)^{r+1}) = q[r+1]_{q²} (βδ)^r + (q²+1) q^{2r} [r+1]_{q⁻⁴} ζ (βδ)^r`. -/
theorem fieldPlus_betaDelta_pow (r : ℕ) :
    fieldPlus q ((β (R := K) q * δ q) ^ (r + 1)) =
      ((q : K) * jk ((q : K) * q) (r + 1)) • (β q * δ q) ^ r +
        (((q : K) * q + 1) * (((q : K) * q) ^ r * jk ((qi * qi) * (qi * qi)) (r + 1))) •
          (zetaB q * (β q * δ q) ^ r) := by
  induction r with
  | zero => simp [fieldPlus_betaDelta]
  | succ r ih =>
    have hz := betaDelta_pow_zeta q (r + 1)
    rw [pow_succ, field_leibniz, ih, tw_betaDelta, fieldPlus_betaDelta, add_mul, mul_add,
      smul_mul_assoc, smul_mul_assoc, mul_smul_comm, mul_smul_comm, mul_smul_comm, mul_one,
      ← pow_succ, mul_assoc (zetaB q), ← pow_succ, mul_smul_comm, hz]
    rw [jk_succ' ((q : K) * q) (r + 1), jk_succ _ (r + 1)]
    have hq0 : (q : K) ≠ 0 := q.ne_zero
    have h : ((q : K) * q) ^ (r + 1) * (((q : K)⁻¹ * (q : K)⁻¹) * ((q : K)⁻¹ * (q : K)⁻¹)) ^ (r + 1)
        = ((q : K)⁻¹ * (q : K)⁻¹) ^ (r + 1) := by
      rw [← mul_pow]; congr 1; field_simp
    match_scalars <;> first | ring1 | linear_combination (-((q : K) * q + 1)) * h

/-- `X₊(ζ^k) βδ = q⁻¹[k]_{q²} (q² ζ^k + q³ ζ^{k+1})`, including `k = 0`. -/
theorem fieldPlus_zeta_pow_mul_betaDelta (k : ℕ) :
    fieldPlus q (zetaB (R := K) q ^ k) * (β q * δ q) =
      (qi * jk ((q : K) * q) k) •
        (((q : K) * q) • zetaB q ^ k + ((q : K) * q * q) • zetaB q ^ (k + 1)) := by
  cases k with
  | zero => simp [field_one]
  | succ k =>
    rw [fieldPlus_zeta_pow, smul_mul_assoc, mul_assoc, alphaGamma_betaDelta, mul_add,
      mul_smul_comm, mul_smul_comm, ← pow_succ, ← mul_assoc, ← pow_succ, ← pow_succ]

/-- **`X₊` on the dual block.**
`X₊(ζ^k (βδ)^{r+1}) = c₁ ζ^k (βδ)^r + c₂ ζ^{k+1} (βδ)^r`. -/
theorem fieldPlus_zeta_pow_betaDelta_pow (k r : ℕ) :
    fieldPlus q (zetaB (R := K) q ^ k * (β q * δ q) ^ (r + 1)) =
      (((q : K) * q) ^ (r + 1) * (qi * jk ((q : K) * q) k) * ((q : K) * q) +
          (q : K) * jk ((q : K) * q) (r + 1)) • (zetaB q ^ k * (β q * δ q) ^ r) +
        (((q : K) * q) ^ (r + 1) * (qi * jk ((q : K) * q) k) * ((q : K) * q * q) +
          ((q : K) * q + 1) * (((q : K) * q) ^ r * jk ((qi * qi) * (qi * qi)) (r + 1))) •
          (zetaB q ^ (k + 1) * (β q * δ q) ^ r) := by
  have hb : (β (R := K) q * δ q) ^ (r + 1) = (β q * δ q) * (β q * δ q) ^ r := pow_succ' _ _
  rw [field_leibniz, tw_betaDelta_pow, fieldPlus_betaDelta_pow, mul_smul_comm, hb, ← mul_assoc,
    fieldPlus_zeta_pow_mul_betaDelta, mul_add, mul_smul_comm, mul_smul_comm, ← mul_assoc,
    pow_succ (zetaB q) k]
  simp only [add_mul, smul_mul_assoc, mul_assoc]
  module

/-- `X₋(ζ^{k+1} (βδ)^r) = [k+1]_{q⁻²} q^{2r} ζ^k (βδ)^{r+1}`. -/
theorem fieldMinus_zeta_pow_betaDelta_pow (k r : ℕ) :
    fieldMinus q (zetaB (R := K) q ^ (k + 1) * (β q * δ q) ^ r) =
      (jk (qi * qi) (k + 1) * ((q : K) * q) ^ r) • (zetaB q ^ k * (β q * δ q) ^ (r + 1)) := by
  rw [field_leibniz, fieldMinus_betaDelta_pow, mul_zero, add_zero, fieldMinus_zeta_pow,
    tw_betaDelta_pow, smul_mul_assoc, mul_smul_comm, smul_smul, mul_assoc, ← pow_succ']

/-- `X₋((βδ)^r) = 0`, in the form `X₋(ζ⁰ (βδ)^r) = 0`. -/
theorem fieldMinus_zeta_zero_betaDelta_pow (r : ℕ) :
    fieldMinus q (zetaB (R := K) q ^ 0 * (β q * δ q) ^ r) = 0 := by
  rw [pow_zero, one_mul, fieldMinus_betaDelta_pow]

end Left

/-! ## `L` on the block `B_{r+1}`, transported to `K[X]` -/

section Coord

variable {K : Type*} [Field K] (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))

/-- `L(A^{r+1} ζ^n)`, read in the coordinate `ζ`: the columns of `lap_alphaGamma_pow` and
`lap_block`. -/
noncomputable def blapX (r : ℕ) : ℕ → K[X]
  | 0 => C (qi * (((q : K) + qi) * jk ((qi * qi) * (qi * qi)) (r + 1)))
  | k + 1 =>
    C ((jk (qi * qi) (r + 1) + jk (qi * qi) (k + 1) * (((q : K) * q) ^ k * ((q : K) * q))) *
        (qi * jk (qi * qi) (k + 1))) * X ^ k +
      C ((((q : K) + qi) * jk ((qi * qi) * (qi * qi)) (r + 1) +
          jk (qi * qi) (k + 1) * (((q : K) * q) ^ k * ((q : K) * q * q))) *
        (qi * jk (qi * qi) (k + 2))) * X ^ (k + 1)

/-- `L` on `B_{r+1}`, transported to `K[X]` through `Q ↦ (αγ)^{r+1} Q(ζ)`. -/
noncomputable def Lb (r : ℕ) : K[X] →ₗ[K] K[X] :=
  lsum fun n => LinearMap.smulRight LinearMap.id (blapX q r n)

theorem Lb_monomial (r n : ℕ) (c : K) : Lb q r (monomial n c) = c • blapX q r n := by
  simp [Lb, lsum_apply, sum_monomial_index]

theorem ev_X_pow (n : ℕ) : ev q (X ^ n : K[X]) = zetaB q ^ n := by
  rw [map_pow, ev, aeval_X]

theorem ev_C (c : K) : ev q (C c) = c • (1 : OqSU2 K q) := by
  rw [ev, aeval_C, Algebra.algebraMap_eq_smul_one]

theorem ev_C_mul (c : K) (P : K[X]) : ev q (C c * P) = c • ev q P := by
  rw [map_mul, ev_C, smul_mul_assoc, one_mul]

/-- Right side: `L((αγ)^{r+1} ζ^n) = (αγ)^{r+1} · (blapX r n)(ζ)`. -/
theorem lap_alphaGamma_pow_zeta_pow (r n : ℕ) :
    lap q ((α (R := K) q * γ q) ^ (r + 1) * zetaB q ^ n) =
      (α q * γ q) ^ (r + 1) * ev q (blapX q r n) := by
  cases n with
  | zero => rw [pow_zero, mul_one, lap_alphaGamma_pow, blapX, ev_C, mul_smul_comm, mul_one]
  | succ k =>
    rw [lap_block, blapX, map_add, ev_C_mul, ev_C_mul, ev_X_pow, ev_X_pow, mul_add, mul_smul_comm,
      mul_smul_comm]

theorem lap_alphaGamma_pow_ev (r : ℕ) (Q : K[X]) :
    lap q ((α (R := K) q * γ q) ^ (r + 1) * ev q Q) = (α q * γ q) ^ (r + 1) * ev q (Lb q r Q) := by
  induction Q using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => simp only [map_add, mul_add, h₁, h₂]
  | monomial n c =>
    rw [Lb_monomial, ev_monomial, mul_smul_comm, map_smul, lap_alphaGamma_pow_zeta_pow, map_smul,
      mul_smul_comm]

end Coord
