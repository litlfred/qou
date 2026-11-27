import QOU.FluidDynamics.q_ns_haar_coproduct_invariance
import CompactQuantumMetrics.OqSU2BudgetLittleQJacobi

/-!
# QOU.FluidDynamics.q_ns_component_lap — `L = X₊X₋` on every torus-weight component `α^a β^m K[ζ]`

Thread "Audit the q-Bessel special-function dictionary" (2026-11-27), Peter–Weyl step 2.

## Results (over a commutative ring `R`, `q : Rˣ`, `ζ = βγ`)

* `lap_mono`: `L(α^a β^m) = [a]_{q⁻²} [m+1]_{q²} · α^a β^m`.
* `lap_mono_zeta_pow`: for every `a, m, k`,
  `L(α^a β^m ζ^{k+1}) = q [k+1]_{q⁻²} [m+k+1]_{q²} · α^a β^m ζ^k
      + [a+k+1]_{q⁻²} [m+k+2]_{q²} · α^a β^m ζ^{k+1}`.

So `L` maps the component `α^a β^m K[ζ]` into itself and is lower bidiagonal there, with
diagonal `[a+k]_{q⁻²} [m+k+1]_{q²}` on `α^a β^m ζ^k`. The subdiagonal does not depend on `a`.

All identities were checked first in exact rational arithmetic (sympy, the PBW model).

No empirical value enters any proof. Sorry-free.
-/

namespace QOU.FluidDynamics.ComponentLap

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2 QOU.FluidDynamics.HaarFieldInvariance
  QOU.FluidDynamics.HaarCoproductInvariance

section Ring

variable {R : Type*} [CommRing R] (q : Rˣ)

local notation "qi" => (((q⁻¹ : Rˣ) : R))
local notation "tw" => torusScaleAlgHom q q⁻¹ q⁻¹⁻¹

/-! ### Commutation with `ζ` -/

theorem beta_zeta : β (R := R) q * zetaB q = zetaB q * β q := by
  unfold zetaB
  calc β q * (β q * γ q) = β q * (γ q * β q) := by rw [rel_bg]
    _ = β q * γ q * β q := by simp only [mul_assoc]

theorem beta_pow_zeta_pow (m k : ℕ) :
    β (R := R) q ^ m * zetaB q ^ k = zetaB q ^ k * β q ^ m :=
  ((Commute.pow_pow (beta_zeta q) m k)).eq

theorem zeta_pow_alpha (k : ℕ) :
    zetaB (R := R) q ^ k * α q = (qi * qi) ^ k • (α q * zetaB q ^ k) := by
  rw [skew_pow_right (alpha_zeta q), smul_smul, ← mul_pow,
    show qi * qi * ((q : R) * q) = 1 by
      linear_combination (qi * (q : R) + 1) * qi_mul_q q, one_pow, one_smul]

theorem zeta_delta : zetaB (R := R) q * δ q = ((q : R) * q) • (δ q * zetaB q) := by
  unfold zetaB
  calc β q * γ q * δ q = β q * (γ q * δ q) := by rw [mul_assoc]
    _ = (q : R) • ((β q * δ q) * γ q) := by
        rw [rel_gd, mul_smul_comm]; simp only [mul_assoc]
    _ = ((q : R) * q) • (δ q * (β q * γ q)) := by
        rw [rel_bd, smul_mul_assoc, smul_smul]; simp only [mul_assoc]

theorem zeta_pow_delta (k : ℕ) :
    zetaB (R := R) q ^ k * δ q = ((q : R) * q) ^ k • (δ q * zetaB q ^ k) :=
  skew_pow_left (zeta_delta q) k

theorem beta_pow_alpha (m : ℕ) : β (R := R) q ^ m * α q = qi ^ m • (α q * β q ^ m) :=
  skew_pow_left (beta_alpha_skew q) m

theorem alpha_beta_pow (m : ℕ) : α (R := R) q * β q ^ m = (q : R) ^ m • (β q ^ m * α q) :=
  skew_pow_right (rel_ab q) m

/-! ### The fields on `α^a β^m` -/

/-- `X₋ α^{a+1} = [a+1]_{q⁻²} α^a β`. -/
theorem fieldMinus_alpha_pow_succ (a : ℕ) :
    fieldMinus q (α (R := R) q ^ (a + 1)) = jk (qi * qi) (a + 1) • (α q ^ a * β q) := by
  induction a with
  | zero => simp [(fieldMinus_generators q).1]
  | succ a ih =>
    rw [pow_succ, field_leibniz, ih, (field_twist_generators q).1, (fieldMinus_generators q).1,
      smul_mul_smul_comm, mul_assoc (α q ^ a), beta_alpha_skew, mul_smul_comm, smul_smul,
      ← mul_assoc, ← pow_succ, jk_succ' (qi * qi) (a + 1)]
    module

theorem tw_beta_pow (m : ℕ) : tw (β (R := R) q ^ m) = (q : R) ^ m • β q ^ m := by
  rw [map_pow, (field_twist_generators q).2.1, smul_pow]

/-- `X₋ (α^{a+1} β^m) = q^m [a+1]_{q⁻²} α^a β^{m+1}`. -/
theorem fieldMinus_mono_succ (a m : ℕ) :
    fieldMinus q (α (R := R) q ^ (a + 1) * β q ^ m) =
      ((q : R) ^ m * jk (qi * qi) (a + 1)) • (α q ^ a * β q ^ (m + 1)) := by
  rw [field_leibniz, fieldMinus_beta_pow, mul_zero, add_zero, fieldMinus_alpha_pow_succ,
    tw_beta_pow, smul_mul_smul_comm, mul_assoc, ← pow_succ', mul_comm ((q : R) ^ m)]

theorem fieldMinus_beta_pow' (m : ℕ) :
    fieldMinus q (α (R := R) q ^ 0 * β q ^ m) = 0 := by
  rw [pow_zero, one_mul, fieldMinus_beta_pow]

/-- `X₊ (α^a β^{m+1}) = q^m [m+1]_{q⁻²} α^{a+1} β^m`. -/
theorem fieldPlus_mono_succ (a m : ℕ) :
    fieldPlus q (α (R := R) q ^ a * β q ^ (m + 1)) =
      ((q : R) ^ m * jk (qi * qi) (m + 1)) • (α q ^ (a + 1) * β q ^ m) := by
  have h := fieldPlus_monoA q a m 0
  simp only [monoA, monoY, pow_zero, mul_one] at h
  exact h

theorem fieldPlus_alpha_pow' (a : ℕ) :
    fieldPlus q (α (R := R) q ^ a * β q ^ 0) = 0 := by
  rw [pow_zero, mul_one, fieldPlus_alpha_pow]

/-! ### `L` and the Leibniz rule -/

theorem tw_zeta_pow (k : ℕ) : tw (zetaB (R := R) q ^ k) = zetaB q ^ k := by
  rw [map_pow, tw_zeta]

/-- `L(f g) = L f · g + X₋f · X₊g + X₊f · R(X₋g) + f · L g` when the twist `R` fixes `g`. -/
theorem lap_mul_of_tw (f g : OqSU2 R q) (hg : tw g = g) :
    lap q (f * g) = lap q f * g + fieldMinus q f * fieldPlus q g +
      fieldPlus q f * tw (fieldMinus q g) + f * lap q g := by
  simp only [lap_apply, field_leibniz, map_add, hg]
  abel

/-- `(q²)^n [n+1]_{q⁻²} = [n+1]_{q²}`. -/
theorem jk_rev (n : ℕ) :
    ((q : R) * q) ^ n * jk (qi * qi) (n + 1) = jk ((q : R) * q) (n + 1) :=
  jk_reverse (by linear_combination ((q : R) * qi + 1) * q_mul_qi q) n

/-! ### The four terms -/

/-- `L(α^a β^m) = [a]_{q⁻²} [m+1]_{q²} α^a β^m`. -/
theorem lap_mono (a m : ℕ) :
    lap q (α (R := R) q ^ a * β q ^ m) =
      (jk (qi * qi) a * jk ((q : R) * q) (m + 1)) • (α q ^ a * β q ^ m) := by
  cases a with
  | zero => rw [lap_apply, fieldMinus_beta_pow', map_zero, jk_zero, zero_mul, zero_smul]
  | succ a =>
    rw [lap_apply, fieldMinus_mono_succ, map_smul, fieldPlus_mono_succ, smul_smul, ← jk_rev q m]
    congr 1
    ring

/-- Normal form for the second term. -/
theorem mono_mul_zeta_pow_alphaGamma (a n k : ℕ) :
    α (R := R) q ^ a * β q ^ (n + 1) * (zetaB q ^ k * (α q * γ q)) =
      ((qi * qi) ^ k * qi ^ (n + 1)) • (α q ^ (a + 1) * β q ^ n * zetaB q ^ (k + 1)) := by
  have hbz : β (R := R) q * zetaB q ^ k = zetaB q ^ k * β q := by
    simpa using beta_pow_zeta_pow q 1 k
  have hb : β (R := R) q ^ (n + 1) * zetaB q ^ k * γ q = β q ^ n * zetaB q ^ (k + 1) := by
    calc β q ^ (n + 1) * zetaB q ^ k * γ q = β q ^ n * ((β q * zetaB q ^ k) * γ q) := by
          rw [pow_succ]; simp only [mul_assoc]
      _ = β q ^ n * (zetaB q ^ k * zetaB q) := by rw [hbz, mul_assoc]; rfl
      _ = β q ^ n * zetaB q ^ (k + 1) := by rw [← pow_succ]
  calc α q ^ a * β q ^ (n + 1) * (zetaB q ^ k * (α q * γ q))
      = α q ^ a * (β q ^ (n + 1) * ((zetaB q ^ k * α q) * γ q)) := by simp only [mul_assoc]
    _ = (qi * qi) ^ k • (α q ^ a * ((β q ^ (n + 1) * α q) * (zetaB q ^ k * γ q))) := by
        rw [zeta_pow_alpha, smul_mul_assoc, mul_smul_comm, mul_smul_comm]; simp only [mul_assoc]
    _ = ((qi * qi) ^ k * qi ^ (n + 1)) •
          ((α q ^ a * α q) * (β q ^ (n + 1) * zetaB q ^ k * γ q)) := by
        rw [beta_pow_alpha, smul_mul_assoc, mul_smul_comm, smul_smul]; simp only [mul_assoc]
    _ = _ := by rw [hb, ← pow_succ]; simp only [mul_assoc]

/-- The second term: `X₋(α^a β^m) · X₊ζ^{k+1}`. -/
theorem fieldMinus_mono_mul_fieldPlus_zeta_pow (a m k : ℕ) :
    fieldMinus q (α (R := R) q ^ a * β q ^ m) * fieldPlus q (zetaB q ^ (k + 1)) =
      (jk (qi * qi) a * jk ((q : R) * q) (k + 1) * (qi * qi) ^ (k + 1)) •
        (α q ^ a * β q ^ m * zetaB q ^ (k + 1)) := by
  cases a with
  | zero => rw [fieldMinus_beta_pow', zero_mul, jk_zero, zero_mul, zero_mul, zero_smul]
  | succ a =>
    rw [fieldMinus_mono_succ, fieldPlus_zeta_pow, smul_mul_smul_comm,
      mono_mul_zeta_pow_alphaGamma, smul_smul]
    congr 1
    have hm : (q : R) ^ m * qi ^ m = 1 := by rw [← mul_pow, q_mul_qi, one_pow]
    linear_combination (jk (qi * qi) (a + 1) * jk ((q : R) * q) (k + 1) * (qi * qi) ^ k *
      qi * qi) * hm

/-- Normal form for the third term. -/
theorem mono_mul_zeta_pow_betaDelta (a n k : ℕ) :
    α (R := R) q ^ (a + 1) * β q ^ n * (zetaB q ^ k * (β q * δ q)) =
      (((q : R) * q) ^ k * (q : R) ^ (n + 1)) • (α q ^ a * β q ^ (n + 1) * zetaB q ^ k) +
      (((q : R) * q) ^ k * (q : R) ^ (n + 1) * q) •
        (α q ^ a * β q ^ (n + 1) * zetaB q ^ (k + 1)) := by
  have hzb : zetaB (R := R) q ^ k * β q = β q * zetaB q ^ k := by
    simpa using (beta_pow_zeta_pow q 1 k).symm
  calc α q ^ (a + 1) * β q ^ n * (zetaB q ^ k * (β q * δ q))
      = α q ^ (a + 1) * (β q ^ n * ((zetaB q ^ k * β q) * δ q)) := by simp only [mul_assoc]
    _ = α q ^ (a + 1) * (β q ^ (n + 1) * (zetaB q ^ k * δ q)) := by
        rw [hzb, pow_succ (β q) n]; simp only [mul_assoc]
    _ = ((q : R) * q) ^ k • (α q ^ a * ((α q * β q ^ (n + 1)) * δ q) * zetaB q ^ k) := by
        rw [zeta_pow_delta, mul_smul_comm, mul_smul_comm, pow_succ]; simp only [mul_assoc]
    _ = (((q : R) * q) ^ k * (q : R) ^ (n + 1)) •
          (α q ^ a * β q ^ (n + 1) * (α q * δ q) * zetaB q ^ k) := by
        rw [alpha_beta_pow, smul_mul_assoc, mul_smul_comm, smul_mul_assoc, smul_smul]
        simp only [mul_assoc]
    _ = _ := by
        rw [alpha_delta, mul_add, mul_one, add_mul, mul_smul_comm, smul_mul_assoc, smul_add,
          smul_smul]
        simp only [mul_assoc]
        rw [← pow_succ']

/-- The third term: `X₊(α^a β^m) · R(X₋ζ^{k+1})`. -/
theorem fieldPlus_mono_mul_tw_fieldMinus_zeta_pow (a m k : ℕ) :
    fieldPlus q (α (R := R) q ^ a * β q ^ m) * tw (fieldMinus q (zetaB q ^ (k + 1))) =
      ((q : R) * jk ((q : R) * q) m * jk (qi * qi) (k + 1) * ((q : R) * q) ^ (k + 1)) •
          (α q ^ a * β q ^ m * zetaB q ^ k) +
      ((q : R) * jk ((q : R) * q) m * jk (qi * qi) (k + 1) * ((q : R) * q) ^ (k + 1) * q) •
          (α q ^ a * β q ^ m * zetaB q ^ (k + 1)) := by
  cases m with
  | zero =>
    rw [fieldPlus_alpha_pow', zero_mul, jk_zero, mul_zero, zero_mul, zero_mul, zero_mul,
      zero_smul, zero_smul, add_zero]
  | succ n =>
    rw [fieldPlus_mono_succ, fieldMinus_zeta_pow, map_smul, map_mul, tw_zeta_pow, tw_betaDelta]
    simp only [mul_smul_comm, smul_mul_assoc, smul_smul]
    rw [mono_mul_zeta_pow_betaDelta, smul_add, smul_smul, smul_smul]
    have h := jk_rev q n
    match_scalars
    · linear_combination ((q : R) * jk (qi * qi) (k + 1) * ((q : R) * q) ^ (k + 1)) * h
    · linear_combination ((q : R) * jk (qi * qi) (k + 1) * ((q : R) * q) ^ (k + 1) * q) * h

/-! ### `L` on the component `α^a β^m R[ζ]` -/

/-- **`L` on `α^a β^m ζ^{k+1}`.** Lower bidiagonal in `k`:
`L(α^a β^m ζ^{k+1}) = q [k+1]_{q⁻²} [m+k+1]_{q²} α^a β^m ζ^k
  + [a+k+1]_{q⁻²} [m+k+2]_{q²} α^a β^m ζ^{k+1}`. -/
theorem lap_mono_zeta_pow (a m k : ℕ) :
    lap q (α (R := R) q ^ a * β q ^ m * zetaB q ^ (k + 1)) =
      ((q : R) * jk (qi * qi) (k + 1) * jk ((q : R) * q) (m + k + 1)) •
          (α q ^ a * β q ^ m * zetaB q ^ k) +
      (jk (qi * qi) (a + k + 1) * jk ((q : R) * q) (m + k + 2)) •
          (α q ^ a * β q ^ m * zetaB q ^ (k + 1)) := by
  rw [lap_mul_of_tw q _ _ (tw_zeta_pow q (k + 1)), lap_mono,
    fieldMinus_mono_mul_fieldPlus_zeta_pow, fieldPlus_mono_mul_tw_fieldMinus_zeta_pow,
    lap_zeta_pow, mul_add, mul_smul_comm, mul_smul_comm, smul_mul_assoc]
  set x : R := (q : R) * q
  set y : R := qi * qi
  have hA : jk y (a + k + 1) = jk y (k + 1) + y ^ (k + 1) * jk y a := by
    rw [show a + k + 1 = (k + 1) + a by omega]; exact jk_add _ _ _
  have hB : jk x (m + k + 2) = jk x (k + 1) + x ^ (k + 1) * jk x (m + 1) := by
    rw [show m + k + 2 = (k + 1) + (m + 1) by omega]; exact jk_add _ _ _
  have hB0 : jk x (m + k + 1) = jk x (k + 1) + x ^ (k + 1) * jk x m := by
    rw [show m + k + 1 = (k + 1) + m by omega]; exact jk_add _ _ _
  have hB' : jk x (k + 2) = jk x (k + 1) + x ^ (k + 1) := jk_succ _ _
  have hBm : jk x (m + 1) = 1 + x * jk x m := jk_succ' _ _
  have hxy : x ^ (k + 1) * y ^ (k + 1) = 1 := by
    rw [← mul_pow, show x * y = 1 by
      simp only [x, y]; linear_combination ((q : R) * qi + 1) * q_mul_qi q, one_pow]
  match_scalars
  · linear_combination (-jk x (m + k + 2)) * hA + (-(jk y (k + 1) + y ^ (k + 1) * jk y a)) * hB +
      jk y (k + 1) * hB' + (-(jk y a * jk x (m + 1))) * hxy +
      (-(jk y (k + 1) * x ^ (k + 1))) * hBm
  · linear_combination (-((q : R) * jk y (k + 1))) * hB0

/-- `L(α^a β^m ζ^0)`: the bottom of the component. -/
theorem lap_mono_zeta_pow_zero (a m : ℕ) :
    lap q (α (R := R) q ^ a * β q ^ m * zetaB q ^ 0) =
      (jk (qi * qi) (a + 0) * jk ((q : R) * q) (m + 0 + 1)) •
        (α q ^ a * β q ^ m * zetaB q ^ 0) := by
  simp only [pow_zero, mul_one, add_zero]
  exact lap_mono q a m

end Ring

end QOU.FluidDynamics.ComponentLap
