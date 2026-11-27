import QOU.FluidDynamics.q_ns_component_lap

/-!
# QOU.FluidDynamics.q_ns_component_lap_quadrants — `L = X₊X₋` on the other quadrants

Thread "Audit the q-Bessel special-function dictionary" (2026-11-27), Peter–Weyl step 2c.
`q_ns_component_lap` treats the components `α^a β^m K[ζ]`. This file treats `α^a γ^m K[ζ]`.

## Results

Over a commutative ring `R`, `q : Rˣ`, `ζ = βγ`, `[n]_x = 1 + x + ⋯ + x^{n-1}`:

* `fieldPlus_alpha_gamma`: `X₊(α^a γ^m) = 0`.
* `lap_alpha_gamma`: `L(α^a γ^m) = [a+m]_{q⁻²} · α^a γ^m`.
* `lap_ag_zeta_pow`: for every `a, m, k`,
  `L(α^a γ^m ζ^{k+1}) = q [m+k+1]_{q⁻²} [k+1]_{q²} · α^a γ^m ζ^k
      + [a+m+k+1]_{q⁻²} [k+2]_{q²} · α^a γ^m ζ^{k+1}`.

So `L` is lower bidiagonal on `α^a γ^m R[ζ]`, with diagonal `[a+m+k]_{q⁻²} [k+1]_{q²}`. That is
the diagonal `cdiag (a+m) 0 k` of the first quadrant, so over a field with `q²` not a root of
unity it is injective in `k` and `L` has an eigenbasis on the component (`compPolyAG`).

The closed forms were first checked in exact rational arithmetic (sympy, the PBW model) for
`a, m, k ≤ 3`.

## Not established

* The components `δ^a β^m K[ζ]` and `δ^a γ^m K[ζ]` (same bidiagonal shape in the model).
* Haar orthogonality between a component and its dual.

No empirical value enters any proof. Sorry-free.
-/

namespace QOU.FluidDynamics.ComponentLap

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2 QOU.FluidDynamics.HaarFieldInvariance
  QOU.FluidDynamics.HaarCoproductInvariance

section QuadrantAG

variable {R : Type*} [CommRing R] (q : Rˣ)

local notation "qi" => (((q⁻¹ : Rˣ) : R))
local notation "tw" => torusScaleAlgHom q q⁻¹ q⁻¹⁻¹

/-! ### Commutation -/

theorem gamma_zeta : Commute (γ (R := R) q) (zetaB q) := by
  show γ q * zetaB q = zetaB q * γ q
  unfold zetaB
  calc γ q * (β q * γ q) = (γ q * β q) * γ q := by rw [mul_assoc]
    _ = β q * γ q * γ q := by rw [← rel_bg]

theorem gamma_pow_alpha (m : ℕ) : γ (R := R) q ^ m * α q = qi ^ m • (α q * γ q ^ m) :=
  skew_pow_left (gamma_alpha_skew q) m

theorem tw_gamma_pow (m : ℕ) : tw (γ (R := R) q ^ m) = qi ^ m • γ q ^ m := by
  rw [map_pow, (field_twist_generators q).2.2.1, smul_pow]

theorem delta_alpha : δ (R := R) q * α q = 1 + qi • zetaB q := by
  have := rel_det_right (R := R) q
  unfold zetaB; rw [← this]; abel

/-- `(q⁻²)^n [n+1]_{q²} = [n+1]_{q⁻²}`. -/
theorem jk_rev' (n : ℕ) :
    (qi * qi) ^ n * jk ((q : R) * q) (n + 1) = jk (qi * qi) (n + 1) :=
  jk_reverse (by linear_combination (qi * (q : R) + 1) * qi_mul_q q) n

/-! ### Normal forms -/

/-- `α^a β γ^m · ζ^k αγ = q^{-(m+1)} q^{-2k} α^{a+1} γ^m ζ^{k+1}`. -/
theorem nf_ag_beta (a m k : ℕ) :
    α (R := R) q ^ a * β q * γ q ^ m * (zetaB q ^ k * (α q * γ q)) =
      (qi ^ (m + 1) * (qi * qi) ^ k) • (α q ^ (a + 1) * γ q ^ m * zetaB q ^ (k + 1)) := by
  have hbg : β (R := R) q * γ q ^ m = γ q ^ m * β q := ((show Commute (β (R := R) q) (γ q) from rel_bg q).pow_right m).eq
  have hbz : β (R := R) q * zetaB q ^ k = zetaB q ^ k * β q := by
    simpa using beta_pow_zeta_pow q 1 k
  have hrest : β (R := R) q * γ q ^ m * zetaB q ^ k * γ q = γ q ^ m * zetaB q ^ (k + 1) := by
    calc β q * γ q ^ m * zetaB q ^ k * γ q = γ q ^ m * ((β q * zetaB q ^ k) * γ q) := by
          rw [hbg]; simp only [mul_assoc]
      _ = γ q ^ m * (zetaB q ^ k * zetaB q) := by rw [hbz, mul_assoc]; rfl
      _ = γ q ^ m * zetaB q ^ (k + 1) := by rw [← pow_succ]
  calc α q ^ a * β q * γ q ^ m * (zetaB q ^ k * (α q * γ q))
      = α q ^ a * (β q * (γ q ^ m * ((zetaB q ^ k * α q) * γ q))) := by simp only [mul_assoc]
    _ = (qi * qi) ^ k • (α q ^ a * (β q * ((γ q ^ m * α q) * (zetaB q ^ k * γ q)))) := by
        rw [zeta_pow_alpha, smul_mul_assoc, mul_smul_comm, mul_smul_comm, mul_smul_comm]
        simp only [mul_assoc]
    _ = ((qi * qi) ^ k * qi ^ m) • (α q ^ a * ((β q * α q) * (γ q ^ m * zetaB q ^ k * γ q))) := by
        rw [gamma_pow_alpha, smul_mul_assoc, mul_smul_comm, mul_smul_comm, smul_smul]
        simp only [mul_assoc]
    _ = ((qi * qi) ^ k * qi ^ m * qi) •
          ((α q ^ a * α q) * (β q * γ q ^ m * zetaB q ^ k * γ q)) := by
        rw [beta_alpha_skew, smul_mul_assoc, mul_smul_comm, smul_smul]; simp only [mul_assoc]
    _ = _ := by
        rw [hrest, ← pow_succ]
        congr 1
        · ring
        · simp only [mul_assoc]

/-- `α^a δ γ^m · ζ^k αγ = q^{-m} q^{-2k} (α^a γ^{m+1} ζ^k + q⁻¹ α^a γ^{m+1} ζ^{k+1})`. -/
theorem nf_ag_delta (a m k : ℕ) :
    α (R := R) q ^ a * δ q * γ q ^ m * (zetaB q ^ k * (α q * γ q)) =
      (qi ^ m * (qi * qi) ^ k) • (α q ^ a * γ q ^ (m + 1) * zetaB q ^ k) +
      (qi ^ m * (qi * qi) ^ k * qi) • (α q ^ a * γ q ^ (m + 1) * zetaB q ^ (k + 1)) := by
  have hgz : γ (R := R) q ^ m * zetaB q ^ k = zetaB q ^ k * γ q ^ m :=
    ((gamma_zeta q).pow_pow m k).eq
  have hzg : zetaB (R := R) q ^ k * γ q = γ q * zetaB q ^ k := ((gamma_zeta q).pow_right k).eq.symm
  have hz : zetaB (R := R) q * (γ q ^ m * zetaB q ^ k * γ q) =
      γ q ^ (m + 1) * zetaB q ^ (k + 1) := by
    calc zetaB q * (γ q ^ m * zetaB q ^ k * γ q)
        = zetaB q * (γ q ^ m * (γ q * zetaB q ^ k)) := by rw [mul_assoc, hzg]
      _ = (zetaB q * γ q ^ (m + 1)) * zetaB q ^ k := by
          rw [← mul_assoc (γ q ^ m), ← pow_succ]; simp only [mul_assoc]
      _ = γ q ^ (m + 1) * zetaB q ^ (k + 1) := by
          rw [← ((gamma_zeta q).pow_left (m + 1)).eq, mul_assoc, ← pow_succ']
  have h1 : γ (R := R) q ^ m * zetaB q ^ k * γ q = γ q ^ (m + 1) * zetaB q ^ k := by
    rw [mul_assoc, hzg, ← mul_assoc, ← pow_succ]
  calc α q ^ a * δ q * γ q ^ m * (zetaB q ^ k * (α q * γ q))
      = α q ^ a * (δ q * (γ q ^ m * ((zetaB q ^ k * α q) * γ q))) := by simp only [mul_assoc]
    _ = (qi * qi) ^ k • (α q ^ a * (δ q * ((γ q ^ m * α q) * (zetaB q ^ k * γ q)))) := by
        rw [zeta_pow_alpha, smul_mul_assoc, mul_smul_comm, mul_smul_comm, mul_smul_comm]
        simp only [mul_assoc]
    _ = ((qi * qi) ^ k * qi ^ m) • (α q ^ a * ((δ q * α q) * (γ q ^ m * zetaB q ^ k * γ q))) := by
        rw [gamma_pow_alpha, smul_mul_assoc, mul_smul_comm, mul_smul_comm, smul_smul]
        simp only [mul_assoc]
    _ = _ := by
        rw [delta_alpha, add_mul, one_mul, smul_mul_assoc, hz, h1, mul_add, mul_smul_comm,
          smul_add, smul_smul]
        congr 1
        · rw [mul_comm ((qi * qi) ^ k)]; simp only [mul_assoc]
        · congr 1
          · ring
          · simp only [mul_assoc]

/-! ### The fields on `α^a γ^m` -/

theorem fieldPlus_alpha_gamma (a m : ℕ) : fieldPlus q (α (R := R) q ^ a * γ q ^ m) = 0 := by
  rw [field_leibniz, fieldPlus_alpha_pow, fieldPlus_gamma_pow, zero_mul, mul_zero, add_zero]

/-- First half of `X₊X₋(α^a γ^m)`. -/
theorem fieldPlus_minusAlpha_tw (a m : ℕ) :
    fieldPlus q (fieldMinus q (α (R := R) q ^ a) * tw (γ q ^ m)) =
      (jk (qi * qi) a * (qi * qi) ^ m) • (α q ^ a * γ q ^ m) := by
  cases a with
  | zero => rw [pow_zero, fieldMinus_one, zero_mul, map_zero, jk_zero, zero_mul, zero_smul]
  | succ a =>
    rw [fieldMinus_alpha_pow_succ, tw_gamma_pow, smul_mul_smul_comm, map_smul, field_leibniz,
      fieldPlus_gamma_pow, mul_zero, add_zero, field_leibniz, fieldPlus_alpha_pow, zero_mul,
      zero_add, (fieldPlus_generators q).2.1, tw_gamma_pow, mul_smul_comm, smul_smul, ← pow_succ,
      mul_pow]
    rw [mul_assoc]

/-- Second half of `X₊X₋(α^a γ^m)`. -/
theorem fieldPlus_alpha_minusGamma (a m : ℕ) :
    fieldPlus q (α (R := R) q ^ a * fieldMinus q (γ q ^ m)) =
      jk (qi * qi) m • (α q ^ a * γ q ^ m) := by
  cases m with
  | zero => rw [pow_zero, fieldMinus_one, mul_zero, map_zero, jk_zero, zero_smul]
  | succ m =>
    rw [fieldMinus_gamma_pow_succ, mul_smul_comm, map_smul, field_leibniz, fieldPlus_alpha_pow,
      zero_mul, zero_add, field_leibniz, (fieldPlus_generators q).2.2.2, fieldPlus_gamma_pow,
      mul_zero, add_zero, tw_gamma_pow, mul_smul_comm, mul_smul_comm, smul_smul, ← pow_succ',
      ← jk_rev' q m, mul_pow]
    congr 1
    ring

/-- `L(α^a γ^m) = [a+m]_{q⁻²} α^a γ^m`. -/
theorem lap_alpha_gamma (a m : ℕ) :
    lap q (α (R := R) q ^ a * γ q ^ m) = jk (qi * qi) (a + m) • (α q ^ a * γ q ^ m) := by
  rw [lap_apply, field_leibniz, map_add, fieldPlus_minusAlpha_tw, fieldPlus_alpha_minusGamma,
    ← add_smul, add_comm a m, jk_add]
  congr 1
  ring

/-- First half of `X₋(α^a γ^m) · ζ^k αγ`. -/
theorem minusAlpha_tw_mul (a m k : ℕ) :
    fieldMinus q (α (R := R) q ^ a) * tw (γ q ^ m) * (zetaB q ^ k * (α q * γ q)) =
      (jk (qi * qi) a * qi * (qi * qi) ^ m * (qi * qi) ^ k) •
        (α q ^ a * γ q ^ m * zetaB q ^ (k + 1)) := by
  cases a with
  | zero => rw [pow_zero, fieldMinus_one, zero_mul, zero_mul, jk_zero, zero_mul, zero_mul,
      zero_mul, zero_smul]
  | succ a =>
    rw [fieldMinus_alpha_pow_succ, tw_gamma_pow, smul_mul_smul_comm, smul_mul_assoc,
      nf_ag_beta, smul_smul]
    congr 1
    rw [pow_succ, mul_pow]; ring

/-- Second half of `X₋(α^a γ^m) · ζ^k αγ`. -/
theorem alpha_minusGamma_mul (a m k : ℕ) :
    α (R := R) q ^ a * fieldMinus q (γ q ^ m) * (zetaB q ^ k * (α q * γ q)) =
      ((qi * qi) ^ k * jk (qi * qi) m) • (α q ^ a * γ q ^ m * zetaB q ^ k) +
      (qi * (qi * qi) ^ k * jk (qi * qi) m) • (α q ^ a * γ q ^ m * zetaB q ^ (k + 1)) := by
  cases m with
  | zero => rw [pow_zero, fieldMinus_one, mul_zero, zero_mul, jk_zero, mul_zero, mul_zero,
      zero_smul, zero_smul, add_zero]
  | succ m =>
    rw [fieldMinus_gamma_pow_succ, mul_smul_comm, smul_mul_assoc,
      show α q ^ a * (δ q * γ q ^ m) * (zetaB q ^ k * (α q * γ q)) =
        α q ^ a * δ q * γ q ^ m * (zetaB q ^ k * (α q * γ q)) by simp only [mul_assoc],
      nf_ag_delta, smul_add, smul_smul, smul_smul, ← jk_rev' q m]
    congr 2
    · rw [mul_pow]; ring
    · rw [mul_pow]; ring

/-- `X₋(α^a γ^m) · ζ^k αγ`. -/
theorem fieldMinus_ag_mul (a m k : ℕ) :
    fieldMinus q (α (R := R) q ^ a * γ q ^ m) * (zetaB q ^ k * (α q * γ q)) =
      ((qi * qi) ^ k * jk (qi * qi) m) • (α q ^ a * γ q ^ m * zetaB q ^ k) +
      (qi * (qi * qi) ^ k * jk (qi * qi) (m + a)) • (α q ^ a * γ q ^ m * zetaB q ^ (k + 1)) := by
  rw [field_leibniz, add_mul, minusAlpha_tw_mul, alpha_minusGamma_mul, jk_add]
  rw [add_left_comm, ← add_smul]
  congr 2
  ring

/-! ### `L` on the component `α^a γ^m R[ζ]` -/

/-- **`L` on `α^a γ^m ζ^{k+1}`.** Lower bidiagonal in `k`:
`L(α^a γ^m ζ^{k+1}) = q [m+k+1]_{q⁻²} [k+1]_{q²} α^a γ^m ζ^k
  + [a+m+k+1]_{q⁻²} [k+2]_{q²} α^a γ^m ζ^{k+1}`. -/
theorem lap_ag_zeta_pow (a m k : ℕ) :
    lap q (α (R := R) q ^ a * γ q ^ m * zetaB q ^ (k + 1)) =
      ((q : R) * jk (qi * qi) (m + k + 1) * jk ((q : R) * q) (k + 1)) •
          (α q ^ a * γ q ^ m * zetaB q ^ k) +
      (jk (qi * qi) (a + m + k + 1) * jk ((q : R) * q) (k + 2)) •
          (α q ^ a * γ q ^ m * zetaB q ^ (k + 1)) := by
  rw [lap_mul_of_tw q _ _ (tw_zeta_pow q (k + 1)), lap_alpha_gamma, fieldPlus_alpha_gamma,
    zero_mul, add_zero, fieldPlus_zeta_pow, mul_smul_comm, fieldMinus_ag_mul, lap_zeta_pow,
    mul_add, mul_smul_comm, mul_smul_comm, smul_mul_assoc]
  have hA : jk (qi * qi) (a + m + k + 1) =
      jk (qi * qi) (k + 1) + (qi * qi) ^ (k + 1) * jk (qi * qi) (m + a) := by
    rw [show a + m + k + 1 = (k + 1) + (m + a) by omega]; exact jk_add _ _ _
  have hA' : jk (qi * qi) (m + k + 1) =
      jk (qi * qi) (k + 1) + (qi * qi) ^ (k + 1) * jk (qi * qi) m := by
    rw [show m + k + 1 = (k + 1) + m by omega]; exact jk_add _ _ _
  have hB : jk ((q : R) * q) (k + 2) = jk ((q : R) * q) (k + 1) + ((q : R) * q) ^ (k + 1) :=
    jk_succ _ _
  have hq : (q : R) * qi = 1 := q_mul_qi q
  have hxy : ((q : R) * q) ^ (k + 1) * (qi * qi) ^ (k + 1) = 1 := by
    rw [← mul_pow, show (q : R) * q * (qi * qi) = 1 by linear_combination ((q : R) * qi + 1) * hq,
      one_pow]
  have hAM : jk (qi * qi) (a + m) = jk (qi * qi) (m + a) := by rw [add_comm]
  match_scalars
  · linear_combination (-jk ((q : R) * q) (k + 2)) * hA +
      (-((qi * qi) ^ (k + 1) * jk (qi * qi) (m + a))) * hB + (-jk (qi * qi) (m + a)) * hxy + hAM
  · linear_combination (-((q : R) * jk ((q : R) * q) (k + 1))) * hA' +
      (-(jk ((q : R) * q) (k + 1) * (qi * qi) ^ k * jk (qi * qi) m * qi)) * hq

end QuadrantAG

/-! ## The quadrant `δ^a β^m R[ζ]` -/

section QuadrantDB

variable {R : Type*} [CommRing R] (q : Rˣ)

local notation "qi" => (((q⁻¹ : Rˣ) : R))
local notation "tw" => torusScaleAlgHom q q⁻¹ q⁻¹⁻¹

/-- `X₊ δ^{n+1} = [n+1]_{q²} δ^n γ`. -/
theorem fieldPlus_delta_pow_succ (n : ℕ) :
    fieldPlus q (δ (R := R) q ^ (n + 1)) = jk ((q : R) * q) (n + 1) • (δ q ^ n * γ q) := by
  induction n with
  | zero => simp [(fieldPlus_generators q).2.2.2]
  | succ n ih =>
    rw [pow_succ, field_leibniz, ih, (field_twist_generators q).2.2.2,
      (fieldPlus_generators q).2.2.2, smul_mul_smul_comm, mul_assoc (δ q ^ n), rel_gd,
      mul_smul_comm, smul_smul, ← mul_assoc, ← pow_succ, jk_succ' _ (n + 1)]
    module

theorem fieldMinus_delta_beta (a m : ℕ) : fieldMinus q (δ (R := R) q ^ a * β q ^ m) = 0 := by
  rw [field_leibniz, fieldMinus_delta_pow, fieldMinus_beta_pow, zero_mul, mul_zero, add_zero]

theorem lap_delta_beta (a m : ℕ) : lap q (δ (R := R) q ^ a * β q ^ m) = 0 := by
  rw [lap_apply, fieldMinus_delta_beta, map_zero]

/-- `δ^a γ β^m · ζ^k βδ = q^m q^{2(k+1)} δ^{a+1} β^m ζ^{k+1}`. -/
theorem nf_db_gamma (a m k : ℕ) :
    δ (R := R) q ^ a * γ q * β q ^ m * (zetaB q ^ k * (β q * δ q)) =
      ((q : R) ^ m * ((q : R) * q) ^ (k + 1)) • (δ q ^ (a + 1) * β q ^ m * zetaB q ^ (k + 1)) := by
  have hgb : γ (R := R) q * β q ^ m = β q ^ m * γ q :=
    ((show Commute (β (R := R) q) (γ q) from rel_bg q).pow_left m).eq.symm
  have hgz : γ (R := R) q * zetaB q ^ k = zetaB q ^ k * γ q := ((gamma_zeta q).pow_right k).eq
  have hin : γ (R := R) q * (β q ^ m * (zetaB q ^ k * β q)) = β q ^ m * zetaB q ^ (k + 1) := by
    rw [← mul_assoc, hgb, mul_assoc, ← mul_assoc (γ q), hgz, mul_assoc, gamma_beta_zetaB,
      ← pow_succ]
  calc δ q ^ a * γ q * β q ^ m * (zetaB q ^ k * (β q * δ q))
      = δ q ^ a * ((γ q * (β q ^ m * (zetaB q ^ k * β q))) * δ q) := by simp only [mul_assoc]
    _ = ((q : R) * q) ^ (k + 1) • (δ q ^ a * ((β q ^ m * δ q) * zetaB q ^ (k + 1))) := by
        rw [hin, mul_assoc, zeta_pow_delta, mul_smul_comm, mul_smul_comm]; simp only [mul_assoc]
    _ = _ := by
        rw [skew_pow_left (rel_bd q), smul_mul_assoc, mul_smul_comm, smul_smul,
          mul_comm (((q : R) * q) ^ (k + 1))]
        congr 1
        rw [pow_succ (δ q) a]; simp only [mul_assoc]

/-- `δ^a α β^m · ζ^k βδ = q^{m+1} q^{2k} (δ^a β^{m+1} ζ^k + q δ^a β^{m+1} ζ^{k+1})`. -/
theorem nf_db_alpha (a m k : ℕ) :
    δ (R := R) q ^ a * α q * β q ^ m * (zetaB q ^ k * (β q * δ q)) =
      ((q : R) ^ (m + 1) * ((q : R) * q) ^ k) • (δ q ^ a * β q ^ (m + 1) * zetaB q ^ k) +
      ((q : R) ^ (m + 1) * ((q : R) * q) ^ k * q) •
        (δ q ^ a * β q ^ (m + 1) * zetaB q ^ (k + 1)) := by
  have hzb : zetaB (R := R) q ^ k * β q = β q * zetaB q ^ k := by
    simpa using (beta_pow_zeta_pow q 1 k).symm
  have hzb' : zetaB (R := R) q * β q ^ (m + 1) = β q ^ (m + 1) * zetaB q :=
    by simpa using (beta_pow_zeta_pow q (m + 1) 1).symm
  calc δ q ^ a * α q * β q ^ m * (zetaB q ^ k * (β q * δ q))
      = δ q ^ a * (α q * (β q ^ (m + 1) * (zetaB q ^ k * δ q))) := by
        rw [show β q ^ (m + 1) * (zetaB q ^ k * δ q) = β q ^ m * ((zetaB q ^ k * β q) * δ q) by
          rw [hzb, pow_succ]; simp only [mul_assoc]]
        simp only [mul_assoc]
    _ = ((q : R) * q) ^ k • (δ q ^ a * ((α q * (β q ^ (m + 1) * δ q)) * zetaB q ^ k)) := by
        rw [zeta_pow_delta, mul_smul_comm, mul_smul_comm, mul_smul_comm]; simp only [mul_assoc]
    _ = (((q : R) * q) ^ k * (q : R) ^ (m + 1)) •
          (δ q ^ a * ((α q * δ q) * β q ^ (m + 1) * zetaB q ^ k)) := by
        rw [skew_pow_left (rel_bd q), mul_smul_comm, smul_mul_assoc, mul_smul_comm, smul_smul]
        simp only [mul_assoc]
    _ = _ := by
        rw [alpha_delta, add_mul, add_mul, one_mul, smul_mul_assoc, smul_mul_assoc]
        simp only [mul_assoc]
        rw [show zetaB q * (β q ^ (m + 1) * zetaB q ^ k) = β q ^ (m + 1) * zetaB q ^ (k + 1) by
            rw [← mul_assoc, hzb', mul_assoc, ← pow_succ'],
          mul_add, mul_smul_comm, smul_add, smul_smul]
        congr 1
        · rw [mul_comm]
        · congr 1
          ring

/-- First half of `X₊(δ^a β^m) · ζ^k βδ`. -/
theorem plusDelta_tw_mul (a m k : ℕ) :
    fieldPlus q (δ (R := R) q ^ a) * tw (β q ^ m) * (zetaB q ^ k * (β q * δ q)) =
      (jk ((q : R) * q) a * ((q : R) * q) ^ m * ((q : R) * q) ^ (k + 1)) •
        (δ q ^ a * β q ^ m * zetaB q ^ (k + 1)) := by
  cases a with
  | zero => rw [pow_zero, fieldPlus_one, zero_mul, zero_mul, jk_zero, zero_mul, zero_mul,
      zero_smul]
  | succ a =>
    rw [fieldPlus_delta_pow_succ, tw_beta_pow, smul_mul_smul_comm, smul_mul_assoc, nf_db_gamma,
      smul_smul]
    congr 1
    rw [mul_pow]; ring

/-- Second half of `X₊(δ^a β^m) · ζ^k βδ`. -/
theorem delta_plusBeta_mul (a m k : ℕ) :
    δ (R := R) q ^ a * fieldPlus q (β q ^ m) * (zetaB q ^ k * (β q * δ q)) =
      ((q : R) * ((q : R) * q) ^ k * jk ((q : R) * q) m) • (δ q ^ a * β q ^ m * zetaB q ^ k) +
      ((q : R) * q * ((q : R) * q) ^ k * jk ((q : R) * q) m) •
        (δ q ^ a * β q ^ m * zetaB q ^ (k + 1)) := by
  cases m with
  | zero => rw [pow_zero, fieldPlus_one, mul_zero, zero_mul, jk_zero, mul_zero, mul_zero,
      zero_smul, zero_smul, add_zero]
  | succ m =>
    rw [fieldPlus_beta_pow_succ, mul_smul_comm, smul_mul_assoc,
      show δ q ^ a * (α q * β q ^ m) * (zetaB q ^ k * (β q * δ q)) =
        δ q ^ a * α q * β q ^ m * (zetaB q ^ k * (β q * δ q)) by simp only [mul_assoc],
      nf_db_alpha, smul_add, smul_smul, smul_smul, ← jk_rev q m]
    congr 2
    · rw [mul_pow]; ring
    · rw [mul_pow]; ring

/-- `X₊(δ^a β^m) · ζ^k βδ`. -/
theorem fieldPlus_db_mul (a m k : ℕ) :
    fieldPlus q (δ (R := R) q ^ a * β q ^ m) * (zetaB q ^ k * (β q * δ q)) =
      ((q : R) * ((q : R) * q) ^ k * jk ((q : R) * q) m) • (δ q ^ a * β q ^ m * zetaB q ^ k) +
      (((q : R) * q) ^ (k + 1) * jk ((q : R) * q) (m + a)) •
        (δ q ^ a * β q ^ m * zetaB q ^ (k + 1)) := by
  rw [field_leibniz, add_mul, plusDelta_tw_mul, delta_plusBeta_mul, jk_add]
  rw [add_left_comm, ← add_smul]
  congr 2
  ring

/-- **`L` on `δ^a β^m ζ^{k+1}`.** Lower bidiagonal in `k`:
`L(δ^a β^m ζ^{k+1}) = q [k+1]_{q⁻²} [m+k+1]_{q²} δ^a β^m ζ^k
  + [k+1]_{q⁻²} [a+m+k+2]_{q²} δ^a β^m ζ^{k+1}`. -/
theorem lap_db_zeta_pow (a m k : ℕ) :
    lap q (δ (R := R) q ^ a * β q ^ m * zetaB q ^ (k + 1)) =
      ((q : R) * jk (qi * qi) (k + 1) * jk ((q : R) * q) (m + k + 1)) •
          (δ q ^ a * β q ^ m * zetaB q ^ k) +
      (jk (qi * qi) (k + 1) * jk ((q : R) * q) (a + m + k + 2)) •
          (δ q ^ a * β q ^ m * zetaB q ^ (k + 1)) := by
  rw [lap_mul_of_tw q _ _ (tw_zeta_pow q (k + 1)), lap_delta_beta, fieldMinus_delta_beta,
    zero_mul, zero_mul, zero_add, zero_add, fieldMinus_zeta_pow,
    map_smul (torusScaleAlgHom q q⁻¹ q⁻¹⁻¹), map_mul (torusScaleAlgHom q q⁻¹ q⁻¹⁻¹), tw_zeta_pow, tw_betaDelta]
  simp only [mul_smul_comm, smul_smul]
  rw [fieldPlus_db_mul, lap_zeta_pow]
  simp only [mul_add, mul_smul_comm, smul_add, smul_smul]
  have hB : jk ((q : R) * q) (m + k + 1) =
      jk ((q : R) * q) (k + 1) + ((q : R) * q) ^ (k + 1) * jk ((q : R) * q) m := by
    rw [show m + k + 1 = (k + 1) + m by omega]; exact jk_add _ _ _
  have hB' : jk ((q : R) * q) (a + m + k + 2) =
      jk ((q : R) * q) (k + 2) + ((q : R) * q) ^ (k + 2) * jk ((q : R) * q) (m + a) := by
    rw [show a + m + k + 2 = (k + 2) + (m + a) by omega]; exact jk_add _ _ _
  match_scalars
  · linear_combination (-(q : R) * jk (qi * qi) (k + 1)) * hB
  · linear_combination (-jk (qi * qi) (k + 1)) * hB'

end QuadrantDB

/-! ## The quadrant `δ^a γ^m R[ζ]` -/

section QuadrantDG

variable {R : Type*} [CommRing R] (q : Rˣ)

local notation "qi" => (((q⁻¹ : Rˣ) : R))
local notation "tw" => torusScaleAlgHom q q⁻¹ q⁻¹⁻¹

/-- `X₋(δ^a γ^{m+1}) = q^{-m} [m+1]_{q²} δ^{a+1} γ^m`. -/
theorem fieldMinus_delta_gamma_succ (a m : ℕ) :
    fieldMinus q (δ (R := R) q ^ a * γ q ^ (m + 1)) =
      (qi ^ m * jk ((q : R) * q) (m + 1)) • (δ q ^ (a + 1) * γ q ^ m) := by
  rw [field_leibniz, fieldMinus_delta_pow, zero_mul, zero_add, fieldMinus_gamma_pow_succ,
    mul_smul_comm, ← mul_assoc, ← pow_succ]

/-- `X₊(δ^{a+1} γ^m) = q^{-m} [a+1]_{q²} δ^a γ^{m+1}`. -/
theorem fieldPlus_delta_succ_gamma (a m : ℕ) :
    fieldPlus q (δ (R := R) q ^ (a + 1) * γ q ^ m) =
      (jk ((q : R) * q) (a + 1) * qi ^ m) • (δ q ^ a * γ q ^ (m + 1)) := by
  rw [field_leibniz, fieldPlus_gamma_pow, mul_zero, add_zero, fieldPlus_delta_pow_succ,
    tw_gamma_pow, smul_mul_smul_comm, mul_assoc, ← pow_succ']

/-- `L(δ^a γ^m) = [m]_{q⁻²} [a+1]_{q²} δ^a γ^m`. -/
theorem lap_delta_gamma (a m : ℕ) :
    lap q (δ (R := R) q ^ a * γ q ^ m) =
      (jk (qi * qi) m * jk ((q : R) * q) (a + 1)) • (δ q ^ a * γ q ^ m) := by
  cases m with
  | zero =>
    rw [pow_zero, mul_one, lap_apply, fieldMinus_delta_pow, map_zero, jk_zero, zero_mul,
      zero_smul]
  | succ m =>
    rw [lap_apply, fieldMinus_delta_gamma_succ, map_smul, fieldPlus_delta_succ_gamma, smul_smul,
      ← jk_rev' q m]
    congr 1
    rw [mul_pow]; ring

/-- `δ^{a+1} γ^m · ζ^k αγ = q^{-m} q^{-2k} (δ^a γ^{m+1} ζ^k + q⁻¹ δ^a γ^{m+1} ζ^{k+1})`. -/
theorem nf_dg_alpha (a m k : ℕ) :
    δ (R := R) q ^ (a + 1) * γ q ^ m * (zetaB q ^ k * (α q * γ q)) =
      (qi ^ m * (qi * qi) ^ k) • (δ q ^ a * γ q ^ (m + 1) * zetaB q ^ k) +
      (qi ^ m * (qi * qi) ^ k * qi) • (δ q ^ a * γ q ^ (m + 1) * zetaB q ^ (k + 1)) := by
  have h := nf_ag_delta q 0 m k
  simp only [pow_zero, one_mul] at h
  calc δ q ^ (a + 1) * γ q ^ m * (zetaB q ^ k * (α q * γ q))
      = δ q ^ a * (δ q * γ q ^ m * (zetaB q ^ k * (α q * γ q))) := by
        rw [pow_succ]; simp only [mul_assoc]
    _ = _ := by
        rw [h, mul_add, mul_smul_comm, mul_smul_comm]; simp only [mul_assoc]

/-- `δ^a γ^{m+1} · ζ^k βδ = q^m q^{2(k+1)} δ^{a+1} γ^m ζ^{k+1}`. -/
theorem nf_dg_beta (a m k : ℕ) :
    δ (R := R) q ^ a * γ q ^ (m + 1) * (zetaB q ^ k * (β q * δ q)) =
      ((q : R) ^ m * ((q : R) * q) ^ (k + 1)) • (δ q ^ (a + 1) * γ q ^ m * zetaB q ^ (k + 1)) := by
  have hgz : γ (R := R) q * zetaB q ^ k = zetaB q ^ k * γ q := ((gamma_zeta q).pow_right k).eq
  have hin : γ (R := R) q ^ (m + 1) * (zetaB q ^ k * β q) = γ q ^ m * zetaB q ^ (k + 1) := by
    rw [pow_succ, mul_assoc, ← mul_assoc (γ q), hgz, mul_assoc, gamma_beta_zetaB, ← pow_succ]
  calc δ q ^ a * γ q ^ (m + 1) * (zetaB q ^ k * (β q * δ q))
      = δ q ^ a * ((γ q ^ (m + 1) * (zetaB q ^ k * β q)) * δ q) := by simp only [mul_assoc]
    _ = ((q : R) * q) ^ (k + 1) • (δ q ^ a * ((γ q ^ m * δ q) * zetaB q ^ (k + 1))) := by
        rw [hin, mul_assoc, zeta_pow_delta, mul_smul_comm, mul_smul_comm]; simp only [mul_assoc]
    _ = _ := by
        rw [skew_pow_left (rel_gd q), smul_mul_assoc, mul_smul_comm, smul_smul,
          mul_comm (((q : R) * q) ^ (k + 1))]
        congr 1
        rw [pow_succ (δ q) a]; simp only [mul_assoc]

/-- `X₋(δ^a γ^m) · ζ^k αγ`. -/
theorem fieldMinus_dg_mul (a m k : ℕ) :
    fieldMinus q (δ (R := R) q ^ a * γ q ^ m) * (zetaB q ^ k * (α q * γ q)) =
      ((qi * qi) ^ k * jk (qi * qi) m) • (δ q ^ a * γ q ^ m * zetaB q ^ k) +
      ((qi * qi) ^ k * jk (qi * qi) m * qi) • (δ q ^ a * γ q ^ m * zetaB q ^ (k + 1)) := by
  cases m with
  | zero =>
    rw [pow_zero, mul_one, fieldMinus_delta_pow, zero_mul, jk_zero, mul_zero, zero_mul,
      zero_smul, zero_smul, add_zero]
  | succ m =>
    rw [fieldMinus_delta_gamma_succ, smul_mul_assoc, nf_dg_alpha, smul_add, smul_smul, smul_smul,
      ← jk_rev' q m]
    congr 2
    · rw [mul_pow]; ring
    · rw [mul_pow]; ring

/-- `X₊(δ^a γ^m) · ζ^k βδ`. -/
theorem fieldPlus_dg_mul (a m k : ℕ) :
    fieldPlus q (δ (R := R) q ^ a * γ q ^ m) * (zetaB q ^ k * (β q * δ q)) =
      (jk ((q : R) * q) a * ((q : R) * q) ^ (k + 1)) •
        (δ q ^ a * γ q ^ m * zetaB q ^ (k + 1)) := by
  cases a with
  | zero =>
    rw [pow_zero, one_mul, fieldPlus_gamma_pow, zero_mul, jk_zero, zero_mul, zero_smul]
  | succ a =>
    rw [fieldPlus_delta_succ_gamma, smul_mul_assoc, nf_dg_beta, smul_smul]
    congr 1
    have hq : qi * (q : R) = 1 := qi_mul_q q
    calc jk ((q : R) * q) (a + 1) * qi ^ m * ((q : R) ^ m * ((q : R) * q) ^ (k + 1))
        = jk ((q : R) * q) (a + 1) * (qi * q) ^ m * ((q : R) * q) ^ (k + 1) := by
          rw [mul_pow]; ring
      _ = _ := by rw [hq, one_pow, mul_one]

/-- **`L` on `δ^a γ^m ζ^{k+1}`.** Lower bidiagonal in `k`:
`L(δ^a γ^m ζ^{k+1}) = q [m+k+1]_{q⁻²} [k+1]_{q²} δ^a γ^m ζ^k
  + [m+k+1]_{q⁻²} [a+k+2]_{q²} δ^a γ^m ζ^{k+1}`. -/
theorem lap_dg_zeta_pow (a m k : ℕ) :
    lap q (δ (R := R) q ^ a * γ q ^ m * zetaB q ^ (k + 1)) =
      ((q : R) * jk (qi * qi) (m + k + 1) * jk ((q : R) * q) (k + 1)) •
          (δ q ^ a * γ q ^ m * zetaB q ^ k) +
      (jk (qi * qi) (m + k + 1) * jk ((q : R) * q) (a + k + 2)) •
          (δ q ^ a * γ q ^ m * zetaB q ^ (k + 1)) := by
  rw [lap_mul_of_tw q _ _ (tw_zeta_pow q (k + 1)), lap_delta_gamma, fieldPlus_zeta_pow,
    fieldMinus_zeta_pow, map_smul (torusScaleAlgHom q q⁻¹ q⁻¹⁻¹),
    map_mul (torusScaleAlgHom q q⁻¹ q⁻¹⁻¹), tw_zeta_pow, tw_betaDelta]
  simp only [mul_smul_comm, smul_smul]
  rw [fieldMinus_dg_mul, fieldPlus_dg_mul, lap_zeta_pow]
  simp only [mul_add, mul_smul_comm, smul_add, smul_smul, smul_mul_assoc]
  have hA : jk (qi * qi) (m + k + 1) =
      jk (qi * qi) (k + 1) + (qi * qi) ^ (k + 1) * jk (qi * qi) m := by
    rw [show m + k + 1 = (k + 1) + m by omega]; exact jk_add _ _ _
  have hB : jk ((q : R) * q) (a + k + 2) =
      jk ((q : R) * q) (k + 2) + ((q : R) * q) ^ (k + 2) * jk ((q : R) * q) a := by
    rw [show a + k + 2 = (k + 2) + a by omega]; exact jk_add _ _ _
  have hB2 : jk ((q : R) * q) (k + 2) = jk ((q : R) * q) (k + 1) + ((q : R) * q) ^ (k + 1) :=
    jk_succ _ _
  have hA1 : jk ((q : R) * q) (a + 1) = 1 + (q : R) * q * jk ((q : R) * q) a := jk_succ' _ _
  have hq : (q : R) * qi = 1 := q_mul_qi q
  have hxy : ((q : R) * q) ^ (k + 1) * (qi * qi) ^ (k + 1) = 1 := by
    rw [← mul_pow, show (q : R) * q * (qi * qi) = 1 by linear_combination ((q : R) * qi + 1) * hq,
      one_pow]
  match_scalars
  · linear_combination jk (qi * qi) m * hA1 +
      (-((qi * qi) ^ (k + 1) * jk (qi * qi) m)) * hB2 + (-jk ((q : R) * q) (a + k + 2)) * hA +
      (-(jk (qi * qi) (k + 1) + (qi * qi) ^ (k + 1) * jk (qi * qi) m)) * hB +
      (-(jk (qi * qi) m + (q : R) * q * jk (qi * qi) m * jk ((q : R) * q) a)) * hxy
  · linear_combination (-((q : R) * jk ((q : R) * q) (k + 1))) * hA +
      (-(jk ((q : R) * q) (k + 1) * jk (qi * qi) m * (qi * qi) ^ k * qi)) * hq

end QuadrantDG

/-! ## Bidiagonal maps on `K[X]` -/

section Bidiag

open Polynomial

variable {K : Type*} [Field K]

/-- The image of `X^n` under the lower bidiagonal map with diagonal `d` and subdiagonal `s`. -/
noncomputable def bidiagX (d s : ℕ → K) : ℕ → K[X]
  | 0 => C (d 0)
  | k + 1 => C (s k) * X ^ k + C (d (k + 1)) * X ^ (k + 1)

/-- The lower bidiagonal map with diagonal `d` and subdiagonal `s`. -/
noncomputable def bidiag (d s : ℕ → K) : K[X] →ₗ[K] K[X] :=
  lsum fun n => LinearMap.smulRight LinearMap.id (bidiagX d s n)

theorem bidiag_monomial (d s : ℕ → K) (n : ℕ) (c : K) :
    bidiag d s (monomial n c) = c • bidiagX d s n := by
  simp [bidiag, lsum_apply, sum_monomial_index]

theorem bidiag_tri (d s : ℕ → K) (n : ℕ) : bidiag d s (X ^ n) - d n • X ^ n ∈ degreeLT K n := by
  rw [← monomial_one_right_eq_X_pow, bidiag_monomial, one_smul, monomial_one_right_eq_X_pow]
  cases n with
  | zero => rw [bidiagX, smul_eq_C_mul, pow_zero, mul_one, sub_self]; exact Submodule.zero_mem _
  | succ k =>
    have : bidiagX d s (k + 1) - d (k + 1) • X ^ (k + 1) = C (s k) * X ^ k := by
      rw [bidiagX, smul_eq_C_mul]; ring
    rw [this]; exact CX_mem _ (by omega)

/-- If an operator acts on `u · Q(ζ)` monomial by monomial as the bidiagonal pattern, it acts on
`u · Q(ζ)` as `bidiag d s`. -/
theorem bidiag_transport {A : Type*} [Ring A] [Algebra K A] (L : A →ₗ[K] A) (e : K[X] →ₐ[K] A)
    (u : A) (d s : ℕ → K)
    (h0 : L (u * e (X ^ 0)) = d 0 • (u * e (X ^ 0)))
    (hs : ∀ k, L (u * e (X ^ (k + 1))) = s k • (u * e (X ^ k)) + d (k + 1) • (u * e (X ^ (k + 1))))
    (Q : K[X]) : L (u * e Q) = u * e (bidiag d s Q) := by
  induction Q using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => simp only [map_add, mul_add, h₁, h₂]
  | monomial n c =>
    have hC : ∀ x : K, ∀ P : K[X], e (C x * P) = x • e P := fun x P => by
      rw [← smul_eq_C_mul, map_smul]
    have hm : e (monomial n c) = c • e (X ^ n) := by rw [← C_mul_X_pow_eq_monomial, hC]
    rw [bidiag_monomial, map_smul e, hm, mul_smul_comm, mul_smul_comm, map_smul L]
    congr 1
    cases n with
    | zero =>
      rw [h0, bidiagX, ← mul_one (C _), ← pow_zero (X : K[X]), hC, mul_smul_comm]
    | succ k =>
      rw [hs, bidiagX, map_add e, hC, hC, mul_add, mul_smul_comm, mul_smul_comm]

end Bidiag

/-! ## The eigenbasis on `α^a γ^m K[ζ]` -/

section ComponentAG

open Polynomial

variable {K : Type*} [Field K] (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))

theorem ev_X_pow (n : ℕ) : ev q ((X : K[X]) ^ n) = zetaB q ^ n := by
  simp [ev]

/-- Subdiagonal entry on `α^a γ^m K[ζ]`: `q [m+k+1]_{q⁻²} [k+1]_{q²}`. -/
noncomputable def csubAG (m k : ℕ) : K := (q : K) * jk (qi * qi) (m + k + 1) * jk ((q : K) * q) (k + 1)

/-- `L` on `α^a γ^m K[ζ]`, transported to `K[X]`. -/
noncomputable def LcAG (a m : ℕ) : K[X] →ₗ[K] K[X] := bidiag (cdiag q (a + m) 0) (csubAG q m)

/-- **`L` preserves the component.** `L(α^a γ^m Q(ζ)) = α^a γ^m (LcAG a m Q)(ζ)`. -/
theorem lap_ag_ev (a m : ℕ) (Q : K[X]) :
    lap q (α (R := K) q ^ a * γ q ^ m * ev q Q) = α q ^ a * γ q ^ m * ev q (LcAG q a m Q) := by
  refine bidiag_transport (lap q) (ev q) _ _ _ ?_ ?_ Q
  · rw [ev_X_pow, pow_zero, mul_one, lap_alpha_gamma, cdiag]
    simp
  · intro k
    rw [ev_X_pow, ev_X_pow, lap_ag_zeta_pow, csubAG, cdiag,
      show a + m + (k + 1) = a + m + k + 1 by omega, show 0 + (k + 1) + 1 = k + 2 by omega]

/-- `LcAG a m` is lower triangular with diagonal `cdiag (a+m) 0`. -/
theorem LcAG_tri (a m n : ℕ) : LcAG q a m (X ^ n) - cdiag q (a + m) 0 n • X ^ n ∈ degreeLT K n :=
  bidiag_tri _ _ n

/-- `p^{(a,m),γ}_n`: the degree-`n` eigenpolynomial of `L` on `α^a γ^m K[ζ]`. -/
noncomputable def compPolyAG (a m n : ℕ) : K[X] := triPoly (LcAG q a m) (cdiag q (a + m) 0) n

/-- **Eigen-equation on the component.**
`L(α^a γ^m p_n(ζ)) = [a+m+n]_{q⁻²} [n+1]_{q²} · α^a γ^m p_n(ζ)`. -/
theorem lap_compPolyAG (a m n : ℕ) :
    lap q (α (R := K) q ^ a * γ q ^ m * ev q (compPolyAG q a m n)) =
      cdiag q (a + m) 0 n • (α q ^ a * γ q ^ m * ev q (compPolyAG q a m n)) := by
  rw [lap_ag_ev, compPolyAG, tri_triPoly _ _ (LcAG_tri q a m), map_smul, mul_smul_comm]

theorem compPolyAG_mem (a m n : ℕ) : compPolyAG q a m n ∈ degreeLT K (n + 1) :=
  triPoly_mem _ _ (LcAG_tri q a m) n

/-- **The eigenpolynomials span `K[X]`.** -/
theorem compPolyAG_span (hp : ∀ n : ℕ, ((q : K) * q) ^ (n + 1) ≠ 1) (a m : ℕ) :
    Submodule.span K (Set.range (compPolyAG q a m)) = ⊤ :=
  triPoly_span _ _ (LcAG_tri q a m) (cdiag_injective q hp (a + m) 0)

theorem coeff_compPolyAG_ne_zero (hp : ∀ n : ℕ, ((q : K) * q) ^ (n + 1) ≠ 1) (a m n : ℕ) :
    (compPolyAG q a m n).coeff n ≠ 0 :=
  coeff_triPoly_ne_zero _ _ (LcAG_tri q a m) (cdiag_injective q hp (a + m) 0) n

end ComponentAG

/-! ## The component `δ^a β^m K[ζ]` -/

section ComponentDB

open Polynomial

variable {K : Type*} [Field K] (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))

/-- `L` on `δ^a β^m K[ζ]`, transported to `K[X]`. -/
noncomputable def LcDB (a m : ℕ) : K[X] →ₗ[K] K[X] := bidiag (cdiag q 0 (a + m)) (csub q m)

/-- **`L` preserves the component.** `L(δ^a β^m Q(ζ)) = δ^a β^m (LcDB a m Q)(ζ)`. -/
theorem lap_db_ev (a m : ℕ) (Q : K[X]) :
    lap q (δ (R := K) q ^ a * β q ^ m * ev q Q) = δ q ^ a * β q ^ m * ev q (LcDB q a m Q) := by
  refine bidiag_transport (lap q) (ev q) _ _ _ ?_ ?_ Q
  · rw [ev_X_pow, pow_zero, mul_one, lap_delta_beta, cdiag]
    simp
  · intro k
    rw [ev_X_pow, ev_X_pow, lap_db_zeta_pow, csub, cdiag,
      show 0 + (k + 1) = k + 1 by omega, show a + m + (k + 1) + 1 = a + m + k + 2 by omega]

/-- `LcDB a m` is lower triangular with diagonal `cdiag 0 (a+m)`. -/
theorem LcDB_tri (a m n : ℕ) : LcDB q a m (X ^ n) - cdiag q 0 (a + m) n • X ^ n ∈ degreeLT K n :=
  bidiag_tri _ _ n

/-- `p^{(a,m),δβ}_n`: the degree-`n` eigenpolynomial of `L` on `δ^a β^m K[ζ]`. -/
noncomputable def compPolyDB (a m n : ℕ) : K[X] := triPoly (LcDB q a m) (cdiag q 0 (a + m)) n

/-- **Eigen-equation on the component.**
`L(δ^a β^m p_n(ζ)) = [n]_{q⁻²} [a+m+n+1]_{q²} · δ^a β^m p_n(ζ)`. -/
theorem lap_compPolyDB (a m n : ℕ) :
    lap q (δ (R := K) q ^ a * β q ^ m * ev q (compPolyDB q a m n)) =
      cdiag q 0 (a + m) n • (δ q ^ a * β q ^ m * ev q (compPolyDB q a m n)) := by
  rw [lap_db_ev, compPolyDB, tri_triPoly _ _ (LcDB_tri q a m), map_smul, mul_smul_comm]

theorem compPolyDB_mem (a m n : ℕ) : compPolyDB q a m n ∈ degreeLT K (n + 1) :=
  triPoly_mem _ _ (LcDB_tri q a m) n

/-- **The eigenpolynomials span `K[X]`.** -/
theorem compPolyDB_span (hp : ∀ n : ℕ, ((q : K) * q) ^ (n + 1) ≠ 1) (a m : ℕ) :
    Submodule.span K (Set.range (compPolyDB q a m)) = ⊤ :=
  triPoly_span _ _ (LcDB_tri q a m) (cdiag_injective q hp 0 (a + m))

theorem coeff_compPolyDB_ne_zero (hp : ∀ n : ℕ, ((q : K) * q) ^ (n + 1) ≠ 1) (a m n : ℕ) :
    (compPolyDB q a m n).coeff n ≠ 0 :=
  coeff_triPoly_ne_zero _ _ (LcDB_tri q a m) (cdiag_injective q hp 0 (a + m)) n

end ComponentDB

end QOU.FluidDynamics.ComponentLap
