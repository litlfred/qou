import QOU.FluidDynamics.q_ns_haar_coproduct_invariance
import CompactQuantumMetrics.OqSU2BudgetLittleQJacobi
import CompactQuantumMetrics.OqSU2LittleQJacobiBasis

/-!
# QOU.FluidDynamics.q_ns_component_lap — `L = X₊X₋` on every torus-weight component `α^a β^m K[ζ]`

Thread "Audit the q-Bessel special-function dictionary" (2026-11-27), Peter–Weyl step 2.

## Results

Over a commutative ring `R`, `q : Rˣ`, `ζ = βγ`, `[n]_x = 1 + x + ⋯ + x^{n-1}`:

* `lap_mono`: `L(α^a β^m) = [a]_{q⁻²} [m+1]_{q²} · α^a β^m`.
* `lap_mono_zeta_pow`: for every `a, m, k`,
  `L(α^a β^m ζ^{k+1}) = q [k+1]_{q⁻²} [m+k+1]_{q²} · α^a β^m ζ^k
      + [a+k+1]_{q⁻²} [m+k+2]_{q²} · α^a β^m ζ^{k+1}`.

So `L` maps the torus-weight component `α^a β^m R[ζ]` into itself and is lower bidiagonal
there, with diagonal `[a+k]_{q⁻²} [m+k+1]_{q²}` on `α^a β^m ζ^k`. The subdiagonal does not
depend on `a`. These components (`a, m ≥ 0`) are the PBW monomials `α^a β^b γ^c` with `b ≥ c`.

Over a field `K`:

* `triPoly`, `tri_triPoly`, `triPoly_span`: a generic lemma. A linear map on `K[X]` that is
  lower triangular in the monomial basis, with pairwise distinct diagonal, has one
  eigenpolynomial in each degree, and these span `K[X]`.
* `Lc a m`, `lap_mono_ev`: `L(α^a β^m Q(ζ)) = α^a β^m (Lc a m Q)(ζ)`.
* `cdiag_mul_eq`: with `x = q²`,
  `cdiag a m k · (x − 1)² · x^{a+k} = x (x^{a+k} − 1)(x^{m+k+1} − 1)`.
* `cdiag_injective`: for `q²` not a root of unity the diagonal is injective in `k`.
* `compPoly a m n`, `lap_compPoly`, `compPoly_span`: on every component `α^a β^m K[ζ]`, `L`
  has an eigenbasis `α^a β^m p^{(a,m)}_n(ζ)` with eigenvalue `[a+n]_{q⁻²} [m+n+1]_{q²}`.

All identities were checked first in exact rational arithmetic (sympy, the PBW model) for
`a ≤ 3`, `m ≤ 2`, `k ≤ 2`.

## Not established

* The other three quadrants: the components `α^a γ^m K[ζ]`, `δ^a β^m K[ζ]` and
  `δ^a γ^m K[ζ]`. The exact-arithmetic model shows the same bidiagonal shape there.
* Haar orthogonality between a component and its dual (Schur orthogonality), and so the
  orthogonality of the eigenbasis. The weight blocks `(αγ)^s K[ζ]` already have this
  (`q_ns_block_self_adjoint`).
* Identification of `p^{(a,m)}_n` with a named little q-Jacobi family.

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

/-! ## A lower-triangular operator on `K[X]` with distinct diagonal has an eigenbasis -/

section Triangular

open Polynomial Finset

variable {K : Type*} [Field K] (T : K[X] →ₗ[K] K[X]) (d : ℕ → K)
  (hT : ∀ n : ℕ, T (X ^ n) - d n • X ^ n ∈ degreeLT K n)

include hT

theorem tri_X_pow_mem (n : ℕ) : T (X ^ n) ∈ degreeLT K (n + 1) := by
  have h := Submodule.add_mem _ (degreeLT_mono (Nat.le_succ n) (hT n))
    (Submodule.smul_mem _ (d n) (X_pow_mem (K := K) (Nat.lt_succ_self n)))
  rwa [sub_add_cancel] at h

/-- `(T − d m)` maps degree `≤ m` into degree `< m`. -/
theorem tri_sub_mem (m : ℕ) {P : K[X]} (hP : P ∈ degreeLT K (m + 1)) :
    T P - d m • P ∈ degreeLT K m := by
  classical
  let M : K[X] →ₗ[K] K[X] := T - d m • LinearMap.id
  have hM : ∀ R, M R = T R - d m • R := fun R => rfl
  suffices h : degreeLT K (m + 1) ≤ (degreeLT K m).comap M by
    have := h hP; rwa [Submodule.mem_comap, hM] at this
  rw [degreeLT_eq_span_X_pow, Submodule.span_le]
  intro x hx
  simp only [coe_image, coe_range, Set.mem_image, Set.mem_Iio] at hx
  obtain ⟨k, hk, rfl⟩ := hx
  rw [SetLike.mem_coe, Submodule.mem_comap, hM]
  rcases Nat.lt_or_ge k m with hkm | hkm
  · exact Submodule.sub_mem _ ((degreeLT_mono hkm) (tri_X_pow_mem T d hT k))
      (Submodule.smul_mem _ _ (X_pow_mem hkm))
  · have hk' : k = m := by omega
    subst hk'
    exact hT k

omit hT in
theorem tri_aeval_X_sub_C (a : K) (P : K[X]) : aeval T (X - C a) P = T P - a • P := by
  simp [Algebra.algebraMap_eq_smul_one]

theorem tri_sub_coeff (m : ℕ) (a : K) {P : K[X]} (hP : P ∈ degreeLT K (m + 1)) :
    T P - a • P ∈ degreeLT K (m + 1) ∧ (T P - a • P).coeff m = (d m - a) * P.coeff m := by
  have h1 := tri_sub_mem T d hT m hP
  have hsplit : T P - a • P = (T P - d m • P) + (d m - a) • P := by rw [sub_smul]; abel
  refine ⟨?_, ?_⟩
  · rw [hsplit]
    exact Submodule.add_mem _ (degreeLT_mono (Nat.le_succ m) h1) (Submodule.smul_mem _ _ hP)
  · rw [hsplit, coeff_add, coeff_smul, smul_eq_mul]
    have : (T P - d m • P).coeff m = 0 :=
      coeff_eq_zero_of_degree_lt ((mem_degreeLT.mp h1).trans_le le_rfl)
    rw [this, zero_add]

/-- **Triangular Cayley–Hamilton.** -/
theorem tri_charPoly_annihilates (m : ℕ) {P : K[X]} (hP : P ∈ degreeLT K (m + 1)) :
    aeval T (∏ k ∈ range (m + 1), (X - C (d k))) P = 0 := by
  induction m generalizing P with
  | zero =>
    rw [prod_range_one, tri_aeval_X_sub_C T]
    exact eq_zero_of_mem_degreeLT_zero (tri_sub_mem T d hT 0 hP)
  | succ m ih =>
    rw [prod_range_succ, map_mul, Module.End.mul_apply, tri_aeval_X_sub_C T]
    exact ih (tri_sub_mem T d hT (m + 1) hP)

omit hT in
/-- `p_n = Π_{k<n} (T − d k) X^n`. -/
noncomputable def triPoly (n : ℕ) : K[X] := aeval T (∏ k ∈ range n, (X - C (d k))) (X ^ n)

theorem triPoly_aux (n j : ℕ) :
    aeval T (∏ k ∈ range j, (X - C (d k))) (X ^ n) ∈ degreeLT K (n + 1) ∧
      (aeval T (∏ k ∈ range j, (X - C (d k))) (X ^ n)).coeff n =
        ∏ k ∈ range j, (d n - d k) := by
  induction j with
  | zero => simp [X_pow_mem (Nat.lt_succ_self n)]
  | succ j ih =>
    rw [prod_range_succ, mul_comm, map_mul, Module.End.mul_apply, tri_aeval_X_sub_C T,
      prod_range_succ]
    obtain ⟨h1, h2⟩ := tri_sub_coeff T d hT n (d j) ih.1
    exact ⟨h1, by rw [h2, ih.2, mul_comm]⟩

theorem triPoly_mem (n : ℕ) : triPoly T d n ∈ degreeLT K (n + 1) := (triPoly_aux T d hT n n).1

/-- **Eigen-equation.** `T p_n = d n · p_n`. -/
theorem tri_triPoly (n : ℕ) : T (triPoly T d n) = d n • triPoly T d n := by
  have h := tri_charPoly_annihilates T d hT n (X_pow_mem (K := K) (Nat.lt_succ_self n))
  rw [prod_range_succ, mul_comm, map_mul, Module.End.mul_apply, tri_aeval_X_sub_C T] at h
  exact sub_eq_zero.mp h

theorem coeff_triPoly_ne_zero (hd : ∀ {k n : ℕ}, k < n → d n ≠ d k) (n : ℕ) :
    (triPoly T d n).coeff n ≠ 0 := by
  rw [show (triPoly T d n).coeff n = _ from (triPoly_aux T d hT n n).2, prod_ne_zero_iff]
  intro k hk
  exact sub_ne_zero.mpr (hd (mem_range.mp hk))

/-- **The eigenpolynomials span `K[X]`.** -/
theorem triPoly_span (hd : ∀ {k n : ℕ}, k < n → d n ≠ d k) :
    Submodule.span K (Set.range (triPoly T d)) = ⊤ := by
  classical
  set S := Submodule.span K (Set.range (triPoly T d))
  have hlt : ∀ n, degreeLT K n ≤ S := by
    intro n
    induction n with
    | zero => intro P hP; rw [eq_zero_of_mem_degreeLT_zero hP]; exact S.zero_mem
    | succ n ih =>
      rw [degreeLT_eq_span_X_pow, Submodule.span_le]
      intro x hx
      simp only [coe_image, coe_range, Set.mem_image, Set.mem_Iio] at hx
      obtain ⟨k, hk, rfl⟩ := hx
      rcases Nat.lt_or_ge k n with hkn | hkn
      · exact ih (X_pow_mem hkn)
      · have hk' : k = n := by omega
        subst hk'
        set c := (triPoly T d k).coeff k
        have hc : c ≠ 0 := coeff_triPoly_ne_zero T d hT hd k
        have hrest : triPoly T d k - c • X ^ k ∈ degreeLT K k := by
          rw [mem_degreeLT, degree_lt_iff_coeff_zero]
          intro m hm
          have hmem := mem_degreeLT.mp (triPoly_mem T d hT k)
          rcases Nat.lt_or_ge k m with h | h
          · rw [coeff_sub, coeff_smul, coeff_X_pow, if_neg (by omega), smul_zero, sub_zero]
            exact coeff_eq_zero_of_degree_lt (hmem.trans_le (by exact_mod_cast h))
          · have : m = k := by omega
            subst this
            rw [coeff_sub, coeff_smul, coeff_X_pow, if_pos rfl, smul_eq_mul, mul_one, sub_self]
        have hx : (X ^ k : K[X]) = c⁻¹ • (triPoly T d k - (triPoly T d k - c • X ^ k)) := by
          rw [sub_sub_cancel, smul_smul, inv_mul_cancel₀ hc, one_smul]
        rw [SetLike.mem_coe, hx]
        exact S.smul_mem _ (S.sub_mem (Submodule.subset_span ⟨k, rfl⟩) (ih hrest))
  rw [eq_top_iff]
  intro P _
  exact hlt (P.natDegree + 1)
    (mem_degreeLT.mpr (degree_le_natDegree.trans_lt (by exact_mod_cast Nat.lt_succ_self _)))

end Triangular

/-! ## The eigenbasis on each component `α^a β^m K[ζ]` -/

section Component

open Polynomial Finset

variable {K : Type*} [Field K] (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))

/-- Diagonal entry of `L` on `α^a β^m ζ^k`: `[a+k]_{q⁻²} [m+k+1]_{q²}`. -/
noncomputable def cdiag (a m k : ℕ) : K := jk (qi * qi) (a + k) * jk ((q : K) * q) (m + k + 1)

/-- Subdiagonal entry: the coefficient of `α^a β^m ζ^k` in `L(α^a β^m ζ^{k+1})`. -/
noncomputable def csub (m k : ℕ) : K := (q : K) * jk (qi * qi) (k + 1) * jk ((q : K) * q) (m + k + 1)

/-- `L(α^a β^m ζ^n)`, read in the coordinate `ζ`. -/
noncomputable def clapX (a m : ℕ) : ℕ → K[X]
  | 0 => C (cdiag q a m 0)
  | k + 1 => C (csub q m k) * X ^ k + C (cdiag q a m (k + 1)) * X ^ (k + 1)

/-- `L` on `α^a β^m K[ζ]`, transported to `K[X]` through `Q ↦ α^a β^m Q(ζ)`. -/
noncomputable def Lc (a m : ℕ) : K[X] →ₗ[K] K[X] :=
  lsum fun n => LinearMap.smulRight LinearMap.id (clapX q a m n)

theorem Lc_monomial (a m n : ℕ) (c : K) : Lc q a m (monomial n c) = c • clapX q a m n := by
  simp [Lc, lsum_apply, sum_monomial_index]

theorem Lc_X_pow (a m n : ℕ) : Lc q a m (X ^ n) = clapX q a m n := by
  rw [← monomial_one_right_eq_X_pow, Lc_monomial, one_smul]

theorem ev_C_mul_X_pow (c : K) (n : ℕ) : ev q (C c * X ^ n) = c • zetaB q ^ n := by
  rw [C_mul_X_pow_eq_monomial, ev_monomial]

theorem lap_mono_zeta_pow_ev (a m n : ℕ) :
    lap q (α (R := K) q ^ a * β q ^ m * zetaB q ^ n) =
      α q ^ a * β q ^ m * ev q (clapX q a m n) := by
  cases n with
  | zero =>
    rw [lap_mono_zeta_pow_zero, clapX, ← mul_one (C _), ← pow_zero (X : K[X]), ev_C_mul_X_pow,
      mul_smul_comm, cdiag]
  | succ k =>
    rw [lap_mono_zeta_pow, clapX, map_add, ev_C_mul_X_pow, ev_C_mul_X_pow, mul_add,
      mul_smul_comm, mul_smul_comm, csub, cdiag]
    rfl

/-- **`L` preserves the component.** `L(α^a β^m Q(ζ)) = α^a β^m (Lc a m Q)(ζ)`. -/
theorem lap_mono_ev (a m : ℕ) (Q : K[X]) :
    lap q (α (R := K) q ^ a * β q ^ m * ev q Q) = α q ^ a * β q ^ m * ev q (Lc q a m Q) := by
  induction Q using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => simp only [map_add, mul_add, h₁, h₂]
  | monomial n c =>
    rw [Lc_monomial, ev_monomial, mul_smul_comm, map_smul, lap_mono_zeta_pow_ev, map_smul,
      mul_smul_comm]

/-- `Lc a m` is lower triangular with diagonal `cdiag a m`. -/
theorem Lc_tri (a m n : ℕ) : Lc q a m (X ^ n) - cdiag q a m n • X ^ n ∈ degreeLT K n := by
  rw [Lc_X_pow]
  cases n with
  | zero => rw [clapX, smul_eq_C_mul, pow_zero, mul_one, sub_self]; exact Submodule.zero_mem _
  | succ k =>
    have : clapX q a m (k + 1) - cdiag q a m (k + 1) • X ^ (k + 1) = C (csub q m k) * X ^ k := by
      rw [clapX, smul_eq_C_mul]; ring
    rw [this]; exact CX_mem _ (by omega)

/-- `q^{2n} [n]_{q⁻²} = q² [n]_{q²}`. -/
theorem pow_mul_jk_inv (n : ℕ) :
    ((q : K) * q) ^ n * jk (qi * qi) n = (q : K) * q * jk ((q : K) * q) n := by
  cases n with
  | zero => simp
  | succ n => rw [← jk_rev q n, pow_succ]; ring

/-- **Closed form of the diagonal.** With `x = q²`,
`cdiag a m k · (x − 1)² · x^{a+k} = x (x^{a+k} − 1)(x^{m+k+1} − 1)`. -/
theorem cdiag_mul_eq (a m k : ℕ) :
    cdiag q a m k * ((q : K) * q - 1) ^ 2 * ((q : K) * q) ^ (a + k) =
      (q : K) * q * (((q : K) * q) ^ (a + k) - 1) * (((q : K) * q) ^ (m + k + 1) - 1) := by
  have h1 := pow_mul_jk_inv q (a + k)
  have h2 := jk_mul_sub_one ((q : K) * q) (a + k)
  have h3 := jk_mul_sub_one ((q : K) * q) (m + k + 1)
  rw [cdiag, ← h2, ← h3]
  linear_combination (jk ((q : K) * q) (m + k + 1) * ((q : K) * q - 1) ^ 2) * h1

/-- **Distinct diagonal.** For `q²` not a root of unity, `k ↦ cdiag a m k` is injective. -/
theorem cdiag_injective (hp : ∀ n : ℕ, ((q : K) * q) ^ (n + 1) ≠ 1) (a m : ℕ)
    {k n : ℕ} (hkn : k < n) : cdiag q a m n ≠ cdiag q a m k := by
  intro heq
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_lt hkn
  have en := cdiag_mul_eq q a m (k + d + 1)
  have ek := cdiag_mul_eq q a m k
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  set x : K := (q : K) * q
  have hx0 : x ≠ 0 := mul_ne_zero hq0 hq0
  set u := x ^ k
  set v := x ^ (d + 1)
  set A := x ^ a
  set M := x ^ (m + 1)
  have e1 : x ^ (a + (k + d + 1)) = A * u * v := by
    simp only [A, u, v, ← pow_add]; ring_nf
  have e2 : x ^ (m + (k + d + 1) + 1) = M * u * v := by
    simp only [M, u, v, ← pow_add]; ring_nf
  have e3 : x ^ (a + k) = A * u := by simp only [A, u, ← pow_add]
  have e4 : x ^ (m + k + 1) = M * u := by simp only [M, u, ← pow_add]; ring_nf
  rw [e1, e2, heq] at en
  rw [e3, e4] at ek
  have key : x * (v - 1) * (A * M * u * u * v - 1) = 0 := by
    clear_value u v A M x
    linear_combination v * ek - en
  have hv : v - 1 ≠ 0 := fun h0 => hp d (sub_eq_zero.mp h0)
  have hz : A * M * u * u * v - 1 ≠ 0 := by
    intro h0
    apply hp (a + m + 2 * k + d + 1)
    have e : x ^ (a + m + 2 * k + d + 1 + 1) = A * M * u * u * v := by
      simp only [A, M, u, v, ← pow_add]; ring_nf
    rw [e]; exact sub_eq_zero.mp h0
  exact mul_ne_zero (mul_ne_zero hx0 hv) hz key

/-- `p^{(a,m)}_n`: the degree-`n` eigenpolynomial of `L` on `α^a β^m K[ζ]`. -/
noncomputable def compPoly (a m n : ℕ) : K[X] := triPoly (Lc q a m) (cdiag q a m) n

/-- **Eigen-equation on the component.**
`L(α^a β^m p^{(a,m)}_n(ζ)) = [a+n]_{q⁻²} [m+n+1]_{q²} · α^a β^m p^{(a,m)}_n(ζ)`. -/
theorem lap_compPoly (a m n : ℕ) :
    lap q (α (R := K) q ^ a * β q ^ m * ev q (compPoly q a m n)) =
      cdiag q a m n • (α q ^ a * β q ^ m * ev q (compPoly q a m n)) := by
  rw [lap_mono_ev, compPoly, tri_triPoly _ _ (Lc_tri q a m), map_smul, mul_smul_comm]

theorem compPoly_mem (a m n : ℕ) : compPoly q a m n ∈ degreeLT K (n + 1) :=
  triPoly_mem _ _ (Lc_tri q a m) n

/-- **The component eigenpolynomials span `K[X]`.** -/
theorem compPoly_span (hp : ∀ n : ℕ, ((q : K) * q) ^ (n + 1) ≠ 1) (a m : ℕ) :
    Submodule.span K (Set.range (compPoly q a m)) = ⊤ :=
  triPoly_span _ _ (Lc_tri q a m) (cdiag_injective q hp a m)

theorem coeff_compPoly_ne_zero (hp : ∀ n : ℕ, ((q : K) * q) ^ (n + 1) ≠ 1) (a m n : ℕ) :
    (compPoly q a m n).coeff n ≠ 0 :=
  coeff_triPoly_ne_zero _ _ (Lc_tri q a m) (cdiag_injective q hp a m) n

end Component

end QOU.FluidDynamics.ComponentLap
