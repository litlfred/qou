import QOU.FluidDynamics.q_ns_block_pairing_nondegenerate
import QOU.FluidDynamics.q_ns_block_weight_lap
import QOU.FluidDynamics.q_ns_block_ladder_negative
import QOU.FluidDynamics.q_ns_haar_field_invariance_full
import CompactQuantumMetrics.OqSU2LittleQJacobiBasis

/-!
# QOU.FluidDynamics.q_ns_block_self_adjoint — `L` on every weight block: self-adjoint, with an orthogonal eigenbasis

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
* `bdiag_mul_eq`: `Lb r` is upper triangular in the monomial basis, and with `x = q²` its
  diagonal is `bdiag r n = (x^{n+1} − 1)(x^{n+2r+2} − 1) / ((x − 1)² x^{n+2r+1})`, that is
  `q^{2-2n-4s}(q^{2(n+1)} − 1)(q^{2(n+2s)} − 1)/(q² − 1)²` with `s = r + 1`.
* `bdiag_injective`: for `q²` not a root of unity the diagonal entries are pairwise distinct.
* `blockPoly r n`, `Lb_blockPoly`, `blockPoly_span`: a degree-`n` eigenpolynomial for every
  `n`, and together they span `K[X]`. This is the per-block basis (the little q-Jacobi family
  with parameter `α = s`).
* `blockPoly_orthogonal`, `blockPoly_norm_ne_zero`: orthogonal for the block pairing, with
  nonzero norms.

So every weight block now has the same complete description as the Cartan block.

All identities were checked first in exact rational arithmetic (sympy, words in
`αγ, ζ, βδ`).

## Not established

* Identification of `blockPoly r n` with a classical little q-Jacobi family and its
  parameters. Here the polynomials are fixed only up to scale, by the eigen-equation.
* (The `s = 0` block is the Cartan block, done in `OqSU2LittleQJacobiBasis`.)
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

section Basis

open Finset

variable {K : Type*} [Field K] (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))

/-- Diagonal entry of `Lb r`: the coefficient of `X^n` in `Lb r (X^n)`. -/
noncomputable def bdiag (r : ℕ) : ℕ → K
  | 0 => qi * (((q : K) + qi) * jk ((qi * qi) * (qi * qi)) (r + 1))
  | k + 1 => (((q : K) + qi) * jk ((qi * qi) * (qi * qi)) (r + 1) +
          jk (qi * qi) (k + 1) * (((q : K) * q) ^ k * ((q : K) * q * q))) *
        (qi * jk (qi * qi) (k + 2))

/-- Off-diagonal entry of `Lb r`: the coefficient of `X^k` in `Lb r (X^{k+1})`. -/
noncomputable def bsub (r k : ℕ) : K :=
  (jk (qi * qi) (r + 1) + jk (qi * qi) (k + 1) * (((q : K) * q) ^ k * ((q : K) * q))) *
    (qi * jk (qi * qi) (k + 1))

theorem blapX_zero (r : ℕ) : blapX q r 0 = C (bdiag q r 0) := rfl

theorem blapX_succ (r k : ℕ) :
    blapX q r (k + 1) = C (bsub q r k) * X ^ k + C (bdiag q r (k + 1)) * X ^ (k + 1) := rfl

theorem jk_eq_div {y : K} (hy : y ≠ 1) (n : ℕ) : jk y n = (y ^ n - 1) / (y - 1) :=
  eq_div_of_mul_eq (sub_ne_zero.mpr hy) (jk_mul_sub_one y n)

/-- **Closed form of the diagonal.** With `x = q²`,
`bdiag r n · (x − 1)² · x^{n+2r+1} = (x^{n+1} − 1)(x^{n+2r+2} − 1)`. -/
theorem bdiag_mul_eq (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1) (r n : ℕ) :
    bdiag q r n * ((q : K) * q - 1) ^ 2 * ((q : K) * q) ^ (n + 2 * r + 1) =
      (((q : K) * q) ^ (n + 1) - 1) * (((q : K) * q) ^ (n + 2 * r + 2) - 1) := by
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  have h1 : (q : K) * q ≠ 1 := by simpa using hp 0
  have h2 : (q : K) * q * ((q : K) * q) ≠ 1 := by simpa [pow_two] using hp 1
  have hi1 : (q : K)⁻¹ * (q : K)⁻¹ ≠ 1 := by
    intro h; apply h1
    rw [← inv_inv ((q : K) * q), mul_inv, h, inv_one]
  have hi2 : (q : K)⁻¹ * (q : K)⁻¹ * ((q : K)⁻¹ * (q : K)⁻¹) ≠ 1 := by
    intro h; apply h2
    simpa [mul_inv] using congrArg Inv.inv h
  have hs1 : ((q : K) * q - 1) ≠ 0 := sub_ne_zero.mpr h1
  have hs2 : ((q : K) ^ 2 - 1) ≠ 0 := by rwa [pow_two]
  have ht2 : (1 : K) - (q : K) ^ 2 ≠ 0 := by
    intro h; apply h1; rw [← pow_two]; linear_combination -h
  have ht4 : (1 : K) - (q : K) ^ 4 ≠ 0 := by
    intro h; apply h2; linear_combination -h
  cases n with
  | zero =>
    simp only [bdiag, qi_eq_inv]
    simp only [jk_eq_div hi2]
    simp only [← mul_inv, inv_pow]
    field_simp
    ring
  | succ k =>
    simp only [bdiag, qi_eq_inv]
    simp only [jk_eq_div hi1, jk_eq_div hi2]
    simp only [← mul_inv, inv_pow]
    field_simp
    ring

/-! ### Triangularity of `Lb r` -/

theorem Lb_X_pow (r n : ℕ) : Lb q r (X ^ n) = blapX q r n := by
  rw [← monomial_one_right_eq_X_pow, Lb_monomial, one_smul]

theorem blapX_mem (r k : ℕ) : blapX q r k ∈ degreeLT K (k + 1) := by
  cases k with
  | zero => rw [blapX_zero, ← mul_one (C _), ← pow_zero X]; exact CX_mem _ (by omega)
  | succ k => exact Submodule.add_mem _ (CX_mem _ (by omega)) (CX_mem _ (by omega))

/-- `(Lb r − bdiag r m)` maps degree `≤ m` into degree `< m`. -/
theorem Lb_sub_mem (r m : ℕ) {P : K[X]} (hP : P ∈ degreeLT K (m + 1)) :
    Lb q r P - bdiag q r m • P ∈ degreeLT K m := by
  classical
  let M : K[X] →ₗ[K] K[X] := Lb q r - bdiag q r m • LinearMap.id
  have hM : ∀ R, M R = Lb q r R - bdiag q r m • R := fun R => rfl
  suffices h : degreeLT K (m + 1) ≤ (degreeLT K m).comap M by
    have := h hP; rwa [Submodule.mem_comap, hM] at this
  rw [degreeLT_eq_span_X_pow, Submodule.span_le]
  intro x hx
  simp only [coe_image, coe_range, Set.mem_image, Set.mem_Iio] at hx
  obtain ⟨k, hk, rfl⟩ := hx
  rw [SetLike.mem_coe, Submodule.mem_comap, hM, Lb_X_pow]
  rcases Nat.lt_or_ge k m with hkm | hkm
  · exact Submodule.sub_mem _ ((degreeLT_mono hkm) (blapX_mem q r k))
      (Submodule.smul_mem _ _ (X_pow_mem hkm))
  · have hk' : k = m := by omega
    subst hk'
    cases k with
    | zero =>
      rw [blapX_zero, smul_eq_C_mul, pow_zero, mul_one, sub_self]; exact Submodule.zero_mem _
    | succ j =>
      have : blapX q r (j + 1) - bdiag q r (j + 1) • X ^ (j + 1) = C (bsub q r j) * X ^ j := by
        rw [blapX_succ, smul_eq_C_mul]; ring
      rw [this]; exact CX_mem _ (by omega)

theorem aeval_Lb_X_sub_C_apply (r : ℕ) (a : K) (P : K[X]) :
    aeval (Lb q r) (X - C a) P = Lb q r P - a • P := by
  simp [Algebra.algebraMap_eq_smul_one]

/-- `(Lb r − a)` keeps degree `≤ m` and scales the `X^m` coefficient by `bdiag r m − a`. -/
theorem Lb_sub_coeff (r m : ℕ) (a : K) {P : K[X]} (hP : P ∈ degreeLT K (m + 1)) :
    Lb q r P - a • P ∈ degreeLT K (m + 1) ∧
      (Lb q r P - a • P).coeff m = (bdiag q r m - a) * P.coeff m := by
  have h1 := Lb_sub_mem q r m hP
  have hsplit : Lb q r P - a • P = (Lb q r P - bdiag q r m • P) + (bdiag q r m - a) • P := by
    rw [sub_smul]; abel
  refine ⟨?_, ?_⟩
  · rw [hsplit]
    exact Submodule.add_mem _ (degreeLT_mono (Nat.le_succ m) h1) (Submodule.smul_mem _ _ hP)
  · rw [hsplit, coeff_add, coeff_smul, smul_eq_mul]
    have : (Lb q r P - bdiag q r m • P).coeff m = 0 :=
      coeff_eq_zero_of_degree_lt ((mem_degreeLT.mp h1).trans_le le_rfl)
    rw [this, zero_add]

/-- **Triangular Cayley–Hamilton on `B_{r+1}`.** -/
theorem Lb_charPoly_annihilates (r m : ℕ) {P : K[X]} (hP : P ∈ degreeLT K (m + 1)) :
    aeval (Lb q r) (∏ k ∈ range (m + 1), (X - C (bdiag q r k))) P = 0 := by
  induction m generalizing P with
  | zero =>
    have := Lb_sub_mem q r 0 hP
    rw [prod_range_one, aeval_Lb_X_sub_C_apply]
    exact eq_zero_of_mem_degreeLT_zero this
  | succ m ih =>
    rw [prod_range_succ, map_mul, Module.End.mul_apply, aeval_Lb_X_sub_C_apply]
    exact ih (Lb_sub_mem q r (m + 1) hP)

/-! ### The block eigenpolynomials -/

/-- `p^{(r)}_n = Π_{k<n} (Lb r − bdiag r k) X^n`: the degree-`n` eigenpolynomial of `L` on
`B_{r+1}`. -/
noncomputable def blockPoly (r n : ℕ) : K[X] :=
  aeval (Lb q r) (∏ k ∈ range n, (X - C (bdiag q r k))) (X ^ n)

theorem blockPoly_aux (r n j : ℕ) :
    aeval (Lb q r) (∏ k ∈ range j, (X - C (bdiag q r k))) (X ^ n) ∈ degreeLT K (n + 1) ∧
      (aeval (Lb q r) (∏ k ∈ range j, (X - C (bdiag q r k))) (X ^ n)).coeff n =
        ∏ k ∈ range j, (bdiag q r n - bdiag q r k) := by
  induction j with
  | zero => simp [X_pow_mem (Nat.lt_succ_self n)]
  | succ j ih =>
    rw [prod_range_succ, mul_comm, map_mul, Module.End.mul_apply, aeval_Lb_X_sub_C_apply,
      prod_range_succ]
    obtain ⟨h1, h2⟩ := Lb_sub_coeff q r n (bdiag q r j) ih.1
    exact ⟨h1, by rw [h2, ih.2, mul_comm]⟩

theorem blockPoly_mem (r n : ℕ) : blockPoly q r n ∈ degreeLT K (n + 1) :=
  (blockPoly_aux q r n n).1

/-- **Eigen-equation.** `Lb r p^{(r)}_n = bdiag r n · p^{(r)}_n`. -/
theorem Lb_blockPoly (r n : ℕ) : Lb q r (blockPoly q r n) = bdiag q r n • blockPoly q r n := by
  have h := Lb_charPoly_annihilates q r n (X_pow_mem (K := K) (Nat.lt_succ_self n))
  rw [prod_range_succ, mul_comm, map_mul, Module.End.mul_apply,
    aeval_Lb_X_sub_C_apply] at h
  exact sub_eq_zero.mp h

/-- **Distinct diagonal.** For `q²` not a root of unity, `bdiag r` is injective. -/
theorem bdiag_injective (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1) (r : ℕ)
    {k n : ℕ} (hkn : k < n) : bdiag q r n ≠ bdiag q r k := by
  intro heq
  set p : K := (q : K) * q
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  have hp0 : p ≠ 0 := mul_ne_zero hq0 hq0
  have hp1 : p - 1 ≠ 0 := fun h0 => hp 0 (by rw [zero_add, pow_one]; exact sub_eq_zero.mp h0)
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_lt hkn
  have en := bdiag_mul_eq q hp r (k + d + 1)
  have ek := bdiag_mul_eq q hp r k
  set u := p ^ k
  set v := p ^ (d + 1)
  set w := p ^ (2 * r)
  have e1 : p ^ (k + d + 1 + 2 * r + 1) = p * u * v * w := by
    simp only [u, v, w, ← pow_add, ← pow_succ']; ring_nf
  have e2 : p ^ (k + d + 1 + 1) = p * u * v := by
    simp only [u, v, ← pow_add, ← pow_succ']; ring_nf
  have e3 : p ^ (k + d + 1 + 2 * r + 2) = p * p * u * v * w := by
    simp only [u, v, w]; ring_nf
  have e4 : p ^ (k + 2 * r + 1) = p * u * w := by
    simp only [u, w, ← pow_add, ← pow_succ']; ring_nf
  have e5 : p ^ (k + 1) = p * u := by simp only [u, ← pow_succ']
  have e6 : p ^ (k + 2 * r + 2) = p * p * u * w := by
    simp only [u, w]; ring_nf
  rw [e1, e2, e3] at en
  rw [e4, e5, e6] at ek
  rw [heq] at en
  have key : (v - 1) * (p * p * p * u * u * v * w - 1) = 0 := by
    clear_value u v w p
    linear_combination v * ek - en
  have hu0 : u ≠ 0 := pow_ne_zero _ hp0
  have hw0 : w ≠ 0 := pow_ne_zero _ hp0
  have hv : v - 1 ≠ 0 := fun h0 => hp d (sub_eq_zero.mp h0)
  have hz : p * p * p * u * u * v * w - 1 ≠ 0 := by
    intro h0
    apply hp (2 * k + d + 2 * r + 3)
    have e : p ^ (2 * k + d + 2 * r + 3 + 1) = p * p * p * u * u * v * w := by
      simp only [u, v, w]; ring_nf
    rw [e]; exact sub_eq_zero.mp h0
  exact mul_ne_zero hv hz key

theorem coeff_blockPoly_ne_zero (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1) (r n : ℕ) :
    (blockPoly q r n).coeff n ≠ 0 := by
  rw [show (blockPoly q r n).coeff n = _ from (blockPoly_aux q r n n).2, prod_ne_zero_iff]
  intro k hk
  exact sub_ne_zero.mpr (bdiag_injective q hp r (mem_range.mp hk))

/-- **The block eigenpolynomials span `K[X]`.** -/
theorem blockPoly_span (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1) (r : ℕ) :
    Submodule.span K (Set.range (blockPoly q r)) = ⊤ := by
  classical
  set S := Submodule.span K (Set.range (blockPoly q r))
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
        set c := (blockPoly q r k).coeff k
        have hc : c ≠ 0 := coeff_blockPoly_ne_zero q hp r k
        have hrest : blockPoly q r k - c • X ^ k ∈ degreeLT K k := by
          rw [mem_degreeLT, degree_lt_iff_coeff_zero]
          intro m hm
          have hmem := mem_degreeLT.mp (blockPoly_mem q r k)
          rcases Nat.lt_or_ge k m with h | h
          · rw [coeff_sub, coeff_smul, coeff_X_pow, if_neg (by omega), smul_zero, sub_zero]
            exact coeff_eq_zero_of_degree_lt (hmem.trans_le (by exact_mod_cast h))
          · have : m = k := by omega
            subst this
            rw [coeff_sub, coeff_smul, coeff_X_pow, if_pos rfl, smul_eq_mul, mul_one, sub_self]
        have hx : (X ^ k : K[X]) = c⁻¹ • (blockPoly q r k - (blockPoly q r k - c • X ^ k)) := by
          rw [sub_sub_cancel, smul_smul, inv_mul_cancel₀ hc, one_smul]
        rw [SetLike.mem_coe, hx]
        exact S.smul_mem _ (S.sub_mem (Submodule.subset_span ⟨k, rfl⟩) (ih hrest))
  rw [eq_top_iff]
  intro P _
  exact hlt (P.natDegree + 1)
    (mem_degreeLT.mpr (degree_le_natDegree.trans_lt (by exact_mod_cast Nat.lt_succ_self _)))

/-! ### Orthogonality with nonzero norms -/

variable (hq : ∀ n : ℕ, 0 < n → (q : K) ^ n ≠ 1)

include hq in
theorem hp_of_hq : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1 := by
  intro m
  rw [← pow_two, ← pow_mul]
  exact hq _ (by omega)

include hq in
/-- **Orthogonality on every weight block.** -/
theorem blockPoly_orthogonal (r : ℕ) {m n : ℕ} (hmn : m ≠ n) :
    haarState q (ev q (blockPoly q r m) * (β q * δ q) ^ (r + 1) *
      ((α q * γ q) ^ (r + 1) * ev q (blockPoly q r n))) = 0 := by
  refine lap_block_eigen_orthogonal q hq r _ _ _ _ (Lb_blockPoly q r m) (Lb_blockPoly q r n) ?_
  rcases Nat.lt_or_gt_of_ne hmn with h | h
  · exact (bdiag_injective q (hp_of_hq q hq) r h).symm
  · exact bdiag_injective q (hp_of_hq q hq) r h

include hq in
/-- **Nonzero norms on every weight block.** -/
theorem blockPoly_norm_ne_zero (r n : ℕ) :
    haarState q (ev q (blockPoly q r n) * (β q * δ q) ^ (r + 1) *
      ((α q * γ q) ^ (r + 1) * ev q (blockPoly q r n))) ≠ 0 := by
  have hp := hp_of_hq q hq
  intro h0
  have hall : ∀ Q : K[X], haarState q (ev q (blockPoly q r n) * (β q * δ q) ^ (r + 1) *
      ((α q * γ q) ^ (r + 1) * ev q Q)) = 0 := by
    intro Q
    have hQ : Q ∈ Submodule.span K (Set.range (blockPoly q r)) := by
      rw [blockPoly_span q hp r]; trivial
    induction hQ using Submodule.span_induction with
    | mem x hx =>
      obtain ⟨m, rfl⟩ := hx
      by_cases hmn : n = m
      · subst hmn; exact h0
      · exact blockPoly_orthogonal q hq r hmn
    | zero => simp
    | add x y _ _ hx hy => rw [map_add, mul_add, mul_add, map_add, hx, hy, add_zero]
    | smul a x _ hx => rw [map_smul, mul_smul_comm, mul_smul_comm, map_smul, hx, smul_zero]
  have h0' := block_pairing_nondegenerate_left q hp (r + 1) (blockPoly q r n) hall
  exact coeff_blockPoly_ne_zero q hp r n (by rw [h0', coeff_zero])

end Basis

end QOU.FluidDynamics.BlockLadder
