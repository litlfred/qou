import QOU.FluidDynamics.q_ns_block_pairing_nondegenerate
import QOU.FluidDynamics.q_ns_block_weight_lap
import QOU.FluidDynamics.q_ns_block_ladder_negative
import QOU.FluidDynamics.q_ns_haar_field_invariance_full

/-!
# QOU.FluidDynamics.q_ns_block_self_adjoint — `L` is self-adjoint on every weight block

Thread "Audit the q-Bessel special-function dictionary" (2026-11-27); bean `qou-qd8k`
(q-NS Part A). `q_ns_block_pairing_nondegenerate` showed that the weight-block pairing
`⟨P, Q⟩_s = h(P(ζ)(βδ)^s · (αγ)^s Q(ζ))` is nondegenerate, and listed as not established
that `L = X₊X₋` is self-adjoint for it. This file proves that, for every `s = r + 1`.

## Results (over a field `K`, `q : Kˣ`, `q^n ≠ 1` for `n > 0` where Haar is used)

* `fieldPlus_zeta_pow_betaDelta_pow`, `fieldMinus_zeta_pow_betaDelta_pow`: `X±` on the dual
  block monomials `ζ^k (βδ)^r`.
* `Lb r`: `L` on `B_{r+1}` in the coordinate `ζ`, a `K`-linear map `K[X] → K[X]`, with
  `lap_alphaGamma_pow_ev`: `L((αγ)^{r+1} Q(ζ)) = (αγ)^{r+1} (Lb r Q)(ζ)`.
* `fieldMinus_fieldPlus_ev_betaDelta_pow`: on the dual block, `X₋X₊` acts by the same
  coordinate operator up to the scalar `q^{2(2r+1)}`:
  `X₋X₊(P(ζ)(βδ)^{r+1}) = q^{2(2r+1)} (Lb r P)(ζ) (βδ)^{r+1}`.
* `haarState_mul_lap_block`: `h(a · L b) = q^{-2(2r+1)} h(X₋X₊ a · b)` for `b ∈ B_{r+1}`,
  from `h ∘ X± = 0` and the twisted Leibniz rule.
* `lap_block_self_adjoint`: `⟨Lb P, Q⟩_{r+1} = ⟨P, Lb Q⟩_{r+1}`. The two scalars cancel.
* `lap_block_eigen_orthogonal`: eigenvectors of `Lb r` with distinct eigenvalues are
  orthogonal for the block pairing.

All identities were checked first in exact rational arithmetic (sympy, words in
`αγ, ζ, βδ`).

## Not established

* That `Lb r` has `n + 1` distinct diagonal entries on `K[X]_{≤n}`, so that it is
  diagonalisable with a polynomial eigenbasis (the little q-Jacobi family with `α = s`).
  `Lb r` is lower bidiagonal in the monomial basis, so this reduces to injectivity of its
  diagonal in `k`; that step is not stated here.
* The `s = 0` block is the Cartan block, done in `OqSU2LittleQJacobiBasis`.
* Whether this budget is the q-NS transport budget (bean `qou-pa7n`).

Everything is algebraic. No empirical value enters any proof. Sorry-free.
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


/-- **Left side: `X₋X₊` on the dual block is `q^{4r+2} L` in the same coordinates.**
`X₋X₊(ζ^n (βδ)^{r+1}) = q^{2(2r+1)} (blapX r n)(ζ) (βδ)^{r+1}`. -/
theorem fieldMinus_fieldPlus_zeta_pow_betaDelta_pow (r n : ℕ) :
    fieldMinus q (fieldPlus q (zetaB (R := K) q ^ n * (β q * δ q) ^ (r + 1))) =
      (((q : K) * q) ^ (2 * r + 1)) • (ev q (blapX q r n) * (β q * δ q) ^ (r + 1)) := by
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  cases n with
  | zero =>
    rw [fieldPlus_zeta_pow_betaDelta_pow, map_add, map_smul, map_smul,
      fieldMinus_zeta_zero_betaDelta_pow, fieldMinus_zeta_pow_betaDelta_pow q 0 r, blapX, ev_C,
      smul_zero, zero_add, smul_smul, smul_mul_assoc, one_mul, pow_zero, one_mul, smul_smul]
    congr 1
    simp only [qi_eq_inv, jk_zero, jk_one, mul_zero, zero_mul, zero_add]
    field_simp
    ring
  | succ k =>
    rw [fieldPlus_zeta_pow_betaDelta_pow, map_add, map_smul, map_smul,
      fieldMinus_zeta_pow_betaDelta_pow q k r, fieldMinus_zeta_pow_betaDelta_pow q (k + 1) r, blapX,
      map_add, ev_C_mul, ev_C_mul, ev_X_pow, ev_X_pow, show k + 1 + 1 = k + 2 from rfl]
    simp only [add_mul, smul_mul_assoc, smul_add, smul_smul]
    have hr := jk_inv_mul_pow q r
    have hk := jk_inv_mul_pow q k
    match_scalars <;> simp only [← hr, ← hk] <;> field_simp <;> ring

theorem fieldMinus_fieldPlus_ev_betaDelta_pow (r : ℕ) (P : K[X]) :
    fieldMinus q (fieldPlus q (ev q P * (β q * δ q) ^ (r + 1))) =
      (((q : K) * q) ^ (2 * r + 1)) • (ev q (Lb q r P) * (β q * δ q) ^ (r + 1)) := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => simp only [map_add, add_mul, h₁, h₂, smul_add]
  | monomial n c =>
    rw [ev_monomial, smul_mul_assoc, map_smul, map_smul, fieldMinus_fieldPlus_zeta_pow_betaDelta_pow,
      Lb_monomial, map_smul, smul_mul_assoc, smul_comm]

end Coord

/-! ## Integration by parts and self-adjointness -/

section Haar

open QOU.FluidDynamics.HaarFieldInvarianceFull

variable {K : Type*} [Field K] (q : Kˣ) (hq : ∀ n : ℕ, 0 < n → (q : K) ^ n ≠ 1)

local notation "qi" => (((q⁻¹ : Kˣ) : K))

include hq

/-- `h(f · X₊ g) = −h(X₊ f · tw g)`. -/
theorem haarState_mul_fieldPlus (f g : OqSU2 K q) :
    haarState q (f * fieldPlus q g) =
      -haarState q (fieldPlus q f * torusScaleAlgHom q q⁻¹ q⁻¹⁻¹ g) := by
  have h0 := haarState_fieldPlus_eq_zero q hq (f * g)
  rw [field_leibniz, map_add] at h0
  linear_combination h0

/-- `h(f · X₋ g) = −h(X₋ f · tw g)`. -/
theorem haarState_mul_fieldMinus (f g : OqSU2 K q) :
    haarState q (f * fieldMinus q g) =
      -haarState q (fieldMinus q f * torusScaleAlgHom q q⁻¹ q⁻¹⁻¹ g) := by
  have h0 := haarState_fieldMinus_eq_zero q hq (f * g)
  rw [field_leibniz, map_add] at h0
  linear_combination h0

omit hq in
/-- The twist scales the block `B_{r+1}` by `q^{-2(r+1)}`. -/
theorem tw_block (r : ℕ) (Q : K[X]) :
    torusScaleAlgHom q q⁻¹ q⁻¹⁻¹ ((α q * γ q) ^ (r + 1) * ev q Q) =
      (qi * qi) ^ (r + 1) • ((α q * γ q) ^ (r + 1) * ev q Q) := by
  rw [map_mul, map_pow, tw_alphaGamma, tw_ev, smul_pow, smul_mul_assoc]

/-- **Integration by parts on `B_{r+1}`, for any left factor.**
`h(a · L b) = q^{-2(2r+1)} h(X₋X₊ a · b)` for `b ∈ B_{r+1}`. -/
theorem haarState_mul_lap_block (a : OqSU2 K q) (r : ℕ) (Q : K[X]) :
    haarState q (a * lap q ((α q * γ q) ^ (r + 1) * ev q Q)) =
      (qi * qi) ^ (2 * r + 1) *
        haarState q (fieldMinus q (fieldPlus q a) * ((α q * γ q) ^ (r + 1) * ev q Q)) := by
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  rw [lap_apply, haarState_mul_fieldPlus q hq, torus_fieldMinus, tw_block]
  simp only [map_smul, mul_smul_comm, smul_eq_mul]
  rw [haarState_mul_fieldMinus q hq, tw_block]
  simp only [map_smul, mul_smul_comm, smul_eq_mul, Units.val_inv_eq_inv_val, inv_inv]
  have key : (q : K) * q * (((q : K)⁻¹ * (q : K)⁻¹) ^ (r + 1) * ((q : K)⁻¹ * (q : K)⁻¹) ^ (r + 1))
      = ((q : K)⁻¹ * (q : K)⁻¹) ^ (2 * r + 1) := by
    rw [← pow_add, show r + 1 + (r + 1) = 2 * r + 1 + 1 by ring, pow_succ]
    field_simp
  linear_combination
    (haarState q (fieldMinus q (fieldPlus q a) * ((α q * γ q) ^ (r + 1) * ev q Q))) * key

/-- **`L` is self-adjoint on every weight block.** For `s = r + 1` and the block pairing
`(P, Q) ↦ h(P(ζ)(βδ)^s · (αγ)^s Q(ζ))`, the operator `Lb r` (that is, `L` on `B_s` in the
coordinate `ζ`) satisfies `⟨Lb P, Q⟩ = ⟨P, Lb Q⟩`. -/
theorem lap_block_self_adjoint (r : ℕ) (P Q : K[X]) :
    haarState q (ev q (Lb q r P) * (β q * δ q) ^ (r + 1) * ((α q * γ q) ^ (r + 1) * ev q Q)) =
      haarState q (ev q P * (β q * δ q) ^ (r + 1) * ((α q * γ q) ^ (r + 1) * ev q (Lb q r Q))) := by
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  rw [← lap_alphaGamma_pow_ev, haarState_mul_lap_block q hq,
    fieldMinus_fieldPlus_ev_betaDelta_pow, smul_mul_assoc, map_smul, smul_eq_mul, ← mul_assoc]
  have key : (qi * qi) ^ (2 * r + 1) * (((q : K) * q) ^ (2 * r + 1)) = 1 := by
    rw [← mul_pow, Units.val_inv_eq_inv_val,
      show (q : K)⁻¹ * (q : K)⁻¹ * ((q : K) * q) = 1 by field_simp, one_pow]
  linear_combination
    (-haarState q (ev q (Lb q r P) * (β q * δ q) ^ (r + 1) * (α q * γ q) ^ (r + 1) * ev q Q)) * key

/-- **Eigenvectors of `L` on a weight block are orthogonal.** If `Lb P = λ P`,
`Lb Q = μ Q` and `λ ≠ μ`, the block pairing of `P` and `Q` vanishes. -/
theorem lap_block_eigen_orthogonal (r : ℕ) (P Q : K[X]) (lam mu : K)
    (hP : Lb q r P = lam • P) (hQ : Lb q r Q = mu • Q) (hne : lam ≠ mu) :
    haarState q (ev q P * (β q * δ q) ^ (r + 1) * ((α q * γ q) ^ (r + 1) * ev q Q)) = 0 := by
  have h := lap_block_self_adjoint q hq r P Q
  rw [hP, hQ] at h
  simp only [map_smul, smul_mul_assoc, mul_smul_comm, smul_eq_mul] at h
  have h2 : (lam - mu) *
      haarState q (ev q P * (β q * δ q) ^ (r + 1) * ((α q * γ q) ^ (r + 1) * ev q Q)) = 0 := by
    linear_combination h
  exact (mul_eq_zero.mp h2).resolve_left (sub_ne_zero.mpr hne)

end Haar

end QOU.FluidDynamics.BlockLadder
