import CompactQuantumMetrics.OqSU2BudgetAllDirections
import CompactQuantumMetrics.OqSU2HaarState
import Mathlib.Algebra.Polynomial.AlgebraMap

/-!
# The off-diagonal budget on the torus-invariant block is the little q-Jacobi form

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`); thread "Use q-Bessel
functions to close derivation gaps" (2026-11-27), route 1.

`OqSU2BudgetAllDirections` and #9648 reduce the off-diagonal budget integrand
`h(X₊ a · X₋ a)` to a sign. This file computes its **size** on the subalgebra of
torus-biinvariant elements, the polynomials in `ζ := β γ`. That block is the
Cartan (zero-weight) block: by `zeroWeightFunctional`, the Haar state sees only it.

## Results

Write `x = q²`, `[n] = 1 + x + ⋯ + x^{n-1}` (`jk x n`), and `L = X₊ ∘ X₋`, with the
fields `fieldPlus`, `fieldMinus` of `OqSU2OffDiagonal` (twist `(q⁻¹α, qβ, q⁻¹γ, qδ)`).

Over a commutative ring `R` with `q : Rˣ`:

* `fieldMinus_zeta_pow`: `X₋ ζ^{k+1} = [k+1]_{q⁻²} · ζ^k β δ`.
* `fieldPlus_zeta_pow`: `X₊ ζ^{k+1} = q⁻¹ [k+1]_{q²} · ζ^k α γ`.
* `lap_zeta_pow`: `L ζ^{k+1} = [k+1]_{q⁻²} q [k+1] · ζ^k + [k+1]_{q⁻²} [k+2] · ζ^{k+1}`.
  So `L` preserves `R[ζ]` and is lower bidiagonal there, with diagonal
  `λ_n = [n]_{q⁻²} [n+1]_{q²} = q [n]_q [n+1]_q` (symmetric integers): the Casimir
  spectrum. This is the q-difference operator of the little q-Jacobi polynomials
  `p_n(ζ; 1, 1; q²)`.

Over a field `K`, with the Haar state `h` of `OqSU2HaarState`:

* `haarState_zetaB_pow`: `h(ζ^m) = (−q)^m / [m+1]`. These are the moments of the
  Jackson q-integral on `[0, 1]` in base `q²`, up to the sign convention of `β`.
* `haarState_zeta_pow_mul_lap`: for `j, n ≥ 0`,
  `h(ζ^j · L ζ^{n+1}) = −q³ (−q)^{j+n} [j][n+1] / ([j+n+1][j+n+2])`.
* `haarState_lap_const`: `h(L ζ^k) = 0`.
* `haarState_lap_symm`: `h(ζ^j L ζ^n) = h(ζ^n L ζ^j)`. So `L` is symmetric for `h` on
  the block. With `haarState_poly_lap_symm`, this holds for all polynomials in `ζ`.
* `haarState_eigen_orthogonal`: eigenpolynomials of `L` with different eigenvalues are
  `h`-orthogonal.
* `haarState_budget_zeta_pow` and `haarState_budget_poly`: the integration-by-parts
  identity `h(X₊ a · X₋ b) = −q⁻² h(a · L b)` for `a, b ∈ K[ζ]`.
* `torus_zeta`, `cartanField_ev`: every torus scaling fixes `ζ`, so the Cartan field
  `c⁻¹(f − R_u f)` vanishes on `K[ζ]`. The Cartan budget is zero on this block.

## Consequence for the q-NS budget

Take `a = Σ c_n p_n` with `L p_n = λ_n p_n`. Then
`h(X₊ a · X₋ a) = −q⁻² Σ_n λ_n c_n² h(p_n²)`. The budget is minus the Dirichlet form of
the q-Casimir, diagonal in the little q-Jacobi basis. Each mode carries the factor
`q⁻² λ_n = q⁻¹ [n]_q [n+1]_q`. At `q = 1` this is `n(n+1)`, the eigenvalue of the
Laplacian on `S²` on Legendre polynomials. For `q > 0`, `[k]_q ≥ k`, so each mode
dissipates at least as much as its classical value.

## The q-Bessel link (stated, not formalised)

The little q-Jacobi polynomials are the torus-biinvariant matrix coefficients of
`SU_q(2)`. Under the contraction `SU_q(2) → E_q(2)` they tend to Hahn–Exton
q-Bessel functions (Koelink 1994). That limit is analytic, and per the transcendental
boundary it is not stated here.

## Not established

* The other weight blocks `(j, s) ≠ (0, 0)`. Numerically, `L` preserves each of them.
* Existence of the eigenpolynomials `p_n`. They follow from triangularity once the
  `λ_n` are distinct, but that is not proved here.
* Haar positivity of `h(p_n²)`. That is #9646 (`haarState_star_mul_self_nonneg`).
* Which pairing of the three directions is the q-NS transport budget, and Part A
  (bean `qou-pa7n`).

No empirical value enters. Sorry-free.

## References

- [woronowicz1987-twisted-su2] Woronowicz, *Twisted SU(2) group*, Publ. RIMS 23 (1987).
- Koelink, *The quantum group of plane motions and the Hahn–Exton q-Bessel function*,
  Duke Math. J. 76 (1994). Cited for the contraction remark only.
-/

namespace QOU.AlgebraicSubstrate.OqSU2

open Finset

/-! ## Geometric sums -/

/-- `[n]_x = 1 + x + ⋯ + x^{n-1}`. -/
def jk {S : Type*} [CommRing S] (x : S) (n : ℕ) : S := ∑ i ∈ range n, x ^ i

section Jk

variable {S : Type*} [CommRing S] (x : S)

@[simp] theorem jk_zero : jk x 0 = 0 := by simp [jk]

theorem jk_succ (n : ℕ) : jk x (n + 1) = jk x n + x ^ n := by
  simp [jk, sum_range_succ]

theorem jk_succ' (n : ℕ) : jk x (n + 1) = 1 + x * jk x n := by
  rw [jk, sum_range_succ', jk, mul_sum]
  simp [pow_succ', add_comm]

@[simp] theorem jk_one : jk x 1 = 1 := by simp [jk]

/-- `[n + j] = [n] + x^n [j]`. -/
theorem jk_add (n j : ℕ) : jk x (n + j) = jk x n + x ^ n * jk x j := by
  induction j with
  | zero => simp
  | succ j ih => rw [← add_assoc, jk_succ, ih, jk_succ, pow_add]; ring

/-- The cross identity `[k][k+j+1] − [k+1][k+j] = −x^k [j]`. -/
theorem jk_cross (k j : ℕ) :
    jk x k * jk x (k + j + 1) - jk x (k + 1) * jk x (k + j) = -(x ^ k * jk x j) := by
  rw [jk_succ' x (k + j), jk_succ' x k, jk_add x k j]
  ring

/-- Reversing a geometric sum: `y^n · [n+1]_{y⁻¹} = [n+1]_y` when `y z = 1`. -/
theorem jk_reverse {y z : S} (hyz : y * z = 1) (n : ℕ) : y ^ n * jk z (n + 1) = jk y (n + 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [jk_succ' z (n + 1), jk_succ y (n + 1), ← ih, pow_succ]
    have : y * (z * jk z (n + 1)) = jk z (n + 1) := by
      rw [← mul_assoc, hyz, one_mul]
    linear_combination y ^ n * this

end Jk


variable {R : Type*} [CommRing R] (q : Rˣ)

/-! ## The block generator `ζ = β γ` and commutation -/

/-- The torus-invariant generator `ζ = βγ`. Named `zetaB` because `OqSU2HaarPositivity` already declares
`zeta` (an `abbrev` with the same body) in this namespace, and the two files are imported
together downstream. -/
noncomputable def zetaB : OqSU2 R q := β q * γ q

local notation "qi" => (((q⁻¹ : Rˣ) : R))

theorem qi_mul_q : qi * (q : R) = 1 := by simp

theorem q_mul_qi : (q : R) * qi = 1 := by simp

theorem gamma_beta_zetaB : γ q * β q = zetaB (R := R) q := (rel_bg q).symm

theorem delta_beta : δ q * β q = qi • (β (R := R) q * δ q) := by
  rw [rel_bd, smul_smul, qi_mul_q, one_smul]

theorem delta_gamma : δ q * γ q = qi • (γ (R := R) q * δ q) := by
  rw [rel_gd, smul_smul, qi_mul_q, one_smul]

/-- `β δ ζ = q⁻² ζ β δ`. -/
theorem betaDelta_zeta :
    (β (R := R) q * δ q) * zetaB q = (qi * qi) • (zetaB q * (β q * δ q)) := by
  unfold zetaB
  calc β q * δ q * (β q * γ q) = β q * ((δ q * β q) * γ q) := by simp only [mul_assoc]
    _ = qi • (β q * (β q * (δ q * γ q))) := by
        rw [delta_beta, smul_mul_assoc, mul_smul_comm]; simp only [mul_assoc]
    _ = (qi * qi) • (β q * (β q * (γ q * δ q))) := by
        rw [delta_gamma, mul_smul_comm, mul_smul_comm, smul_smul]
    _ = (qi * qi) • (β q * γ q * (β q * δ q)) := by
        congr 1
        calc β q * (β q * (γ q * δ q)) = β q * ((β q * γ q) * δ q) := by simp only [mul_assoc]
          _ = β q * ((γ q * β q) * δ q) := by rw [rel_bg]
          _ = β q * γ q * (β q * δ q) := by simp only [mul_assoc]

/-- `α ζ = q² ζ α`. -/
theorem alpha_zeta : α (R := R) q * zetaB q = ((q : R) * q) • (zetaB q * α q) := by
  unfold zetaB
  calc α q * (β q * γ q) = (α q * β q) * γ q := by simp only [mul_assoc]
    _ = (q : R) • (β q * (α q * γ q)) := by
        rw [rel_ab, smul_mul_assoc]; simp only [mul_assoc]
    _ = ((q : R) * q) • (β q * γ q * α q) := by
        rw [rel_ag, mul_smul_comm, smul_smul]; simp only [mul_assoc]

/-- `α γ ζ = q² ζ α γ`. -/
theorem alphaGamma_zeta :
    (α (R := R) q * γ q) * zetaB q = ((q : R) * q) • (zetaB q * (α q * γ q)) := by
  have hγ : γ (R := R) q * zetaB q = zetaB q * γ q := by
    unfold zetaB
    calc γ q * (β q * γ q) = (γ q * β q) * γ q := by simp only [mul_assoc]
      _ = (β q * γ q) * γ q := by rw [← rel_bg]
  calc α q * γ q * zetaB q = α q * (γ q * zetaB q) := by simp only [mul_assoc]
    _ = (α q * zetaB q) * γ q := by rw [hγ]; simp only [mul_assoc]
    _ = ((q : R) * q) • (zetaB q * (α q * γ q)) := by
        rw [alpha_zeta, smul_mul_assoc]; simp only [mul_assoc]

theorem alpha_delta : α (R := R) q * δ q = 1 + (q : R) • zetaB q := by
  have := rel_det_left (R := R) q
  unfold zetaB; rw [← this]; abel

/-- `α γ β δ = q² ζ + q³ ζ²`. -/
theorem alphaGamma_betaDelta :
    (α (R := R) q * γ q) * (β q * δ q) =
      ((q : R) * q) • zetaB q + ((q : R) * q * q) • (zetaB q * zetaB q) := by
  calc α q * γ q * (β q * δ q) = (α q * (γ q * β q)) * δ q := by simp only [mul_assoc]
    _ = (α q * zetaB q) * δ q := by rw [gamma_beta_zetaB]
    _ = ((q : R) * q) • (zetaB q * (α q * δ q)) := by
        rw [alpha_zeta, smul_mul_assoc]; simp only [mul_assoc]
    _ = ((q : R) * q) • zetaB q + ((q : R) * q * q) • (zetaB q * zetaB q) := by
        rw [alpha_delta, mul_add, mul_one, mul_smul_comm, smul_add, smul_smul]

/-- `αγ ζ^k = q^{2k} ζ^k αγ`. -/
theorem alphaGamma_zeta_pow (k : ℕ) :
    (α (R := R) q * γ q) * zetaB q ^ k = ((q : R) * q) ^ k • (zetaB q ^ k * (α q * γ q)) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, mul_assoc, alphaGamma_zeta, mul_smul_comm,
      smul_smul, ← mul_assoc, ← pow_succ]
    congr 1
    · ring
    · rw [← mul_assoc, ← pow_succ]

/-! ## The twist and the fields on `R[ζ]` -/

theorem tw_zeta : torusScaleAlgHom (R := R) q q⁻¹ q⁻¹⁻¹ (zetaB q) = zetaB q := by
  unfold zetaB
  obtain ⟨-, hb, hg, -⟩ := field_twist_generators (R := R) q
  rw [map_mul, hb, hg, smul_mul_smul_comm, q_mul_qi, one_smul]

theorem tw_betaDelta :
    torusScaleAlgHom (R := R) q q⁻¹ q⁻¹⁻¹ (β q * δ q) = ((q : R) * q) • (β q * δ q) := by
  obtain ⟨-, hb, -, hd⟩ := field_twist_generators (R := R) q
  rw [map_mul, hb, hd, smul_mul_smul_comm]

theorem fieldMinus_zeta : fieldMinus (R := R) q (zetaB q) = β q * δ q := by
  unfold zetaB
  obtain ⟨-, hb, hg, -⟩ := fieldMinus_generators (R := R) q
  rw [field_leibniz, hb, hg, zero_mul, zero_add]

theorem fieldPlus_zeta : fieldPlus (R := R) q (zetaB q) = qi • (α q * γ q) := by
  unfold zetaB
  obtain ⟨-, hb, hg, -⟩ := fieldPlus_generators (R := R) q
  obtain ⟨-, -, tg, -⟩ := field_twist_generators (R := R) q
  rw [field_leibniz, hb, hg, tg, mul_zero, add_zero, mul_smul_comm]

theorem fieldPlus_betaDelta :
    fieldPlus (R := R) q (β q * δ q) = (q : R) • (1 : OqSU2 R q) + ((q : R) * q + 1) • zetaB q := by
  obtain ⟨-, hb, -, hd⟩ := fieldPlus_generators (R := R) q
  obtain ⟨-, -, -, td⟩ := field_twist_generators (R := R) q
  rw [field_leibniz, hb, hd, td, mul_smul_comm, alpha_delta,
    show β (R := R) q * γ q = zetaB q from rfl]
  module

theorem fieldPlus_one : fieldPlus (R := R) q 1 = 0 := field_one q 0 1 0

theorem fieldMinus_one : fieldMinus (R := R) q 1 = 0 := field_one q 0 0 1

/-- `X₋ ζ^{k+1} = [k+1]_{q⁻²} · ζ^k β δ`. -/
theorem fieldMinus_zeta_pow (k : ℕ) :
    fieldMinus (R := R) q (zetaB q ^ (k + 1)) =
      jk (qi * qi) (k + 1) • (zetaB q ^ k * (β q * δ q)) := by
  induction k with
  | zero => simp [fieldMinus_zeta]
  | succ k ih =>
    rw [pow_succ, field_leibniz, ih, tw_zeta, fieldMinus_zeta, smul_mul_assoc, mul_assoc,
      betaDelta_zeta, mul_smul_comm, smul_smul, ← mul_assoc (zetaB q ^ k), ← pow_succ,
      jk_succ' (qi * qi) (k + 1)]
    module

/-- `X₊ ζ^{k+1} = q⁻¹ [k+1]_{q²} · ζ^k α γ`. -/
theorem fieldPlus_zeta_pow (k : ℕ) :
    fieldPlus (R := R) q (zetaB q ^ (k + 1)) =
      (qi * jk ((q : R) * q) (k + 1)) • (zetaB q ^ k * (α q * γ q)) := by
  induction k with
  | zero => simp [fieldPlus_zeta]
  | succ k ih =>
    rw [pow_succ, field_leibniz, ih, tw_zeta, fieldPlus_zeta, smul_mul_assoc, mul_assoc,
      alphaGamma_zeta, mul_smul_comm, smul_smul, ← mul_assoc (zetaB q ^ k), ← pow_succ,
      mul_smul_comm, jk_succ' ((q : R) * q) (k + 1)]
    module

/-- The block operator `L = X₊ ∘ X₋`. -/
noncomputable def lap : OqSU2 R q →ₗ[R] OqSU2 R q := (fieldPlus q).comp (fieldMinus q)

theorem lap_apply (x : OqSU2 R q) : lap q x = fieldPlus q (fieldMinus q x) := rfl

theorem lap_one : lap (R := R) q 1 = 0 := by rw [lap_apply, fieldMinus_one, map_zero]

/-- **`L` on `ζ^{k+1}`.** Lower bidiagonal on `R[ζ]`, with diagonal entry
`[k+1]_{q⁻²} [k+2]_{q²}` and subdiagonal entry `[k+1]_{q⁻²} q [k+1]_{q²}`. -/
theorem lap_zeta_pow (k : ℕ) :
    lap (R := R) q (zetaB q ^ (k + 1)) =
      (jk (qi * qi) (k + 1) * ((q : R) * jk ((q : R) * q) (k + 1))) • zetaB q ^ k +
      (jk (qi * qi) (k + 1) * jk ((q : R) * q) (k + 2)) • zetaB q ^ (k + 1) := by
  rw [lap_apply, fieldMinus_zeta_pow, map_smul, field_leibniz, tw_betaDelta, fieldPlus_betaDelta]
  rcases k with _ | m
  · rw [pow_zero, fieldPlus_one, zero_mul, zero_add, one_mul, pow_one,
      show (0 : ℕ) + 2 = 1 + 1 from rfl, jk_succ' ((q : R) * q) 1]
    simp only [jk_one]
    module
  · rw [fieldPlus_zeta_pow, smul_mul_assoc, mul_smul_comm, smul_smul,
      mul_assoc (zetaB q ^ m), alphaGamma_betaDelta]
    simp only [mul_add, mul_smul_comm, mul_one, ← mul_assoc (zetaB q ^ m), ← pow_succ]
    rw [show m + 1 + 2 = m + 1 + 1 + 1 from rfl, jk_succ' ((q : R) * q) (m + 1 + 1),
      jk_succ' ((q : R) * q) (m + 1)]
    have hs : qi * jk ((q : R) * q) (m + 1) * ((q : R) * q) = (q : R) * jk ((q : R) * q) (m + 1) := by
      linear_combination (jk ((q : R) * q) (m + 1) * (q : R)) * qi_mul_q q
    rw [hs]
    module

/-! ## The Haar state on the block -/

section Haar

variable {K : Type*} [Field K] (q : Kˣ)

theorem monoRep_zetaB_pow (m : ℕ) : monoRep q (zetaB q ^ m) (eb K 0 0 0) = eb K 0 m m := by
  induction m with
  | zero => simp
  | succ m ih =>
    rw [pow_succ', map_mul, Module.End.mul_apply, ih]
    simp [zetaB, monoRep]

/-- `h(ζ^m) = (−q)^m / [m+1]_{q²}`: the Jackson moments. -/
theorem haarState_zetaB_pow (m : ℕ) : haarState q (zetaB q ^ m) = haarMoment q m := by
  rw [haarState, zeroWeightFunctional_apply, monoRep_zetaB_pow, zeroRead_e]
  simp

theorem qSqNum_eq_jk (m : ℕ) : qSqNum q m = jk ((q : K) * q) (m + 1) := by
  simp [qSqNum, jk, pow_mul, sq]

theorem qi_eq_inv : (((q⁻¹ : Kˣ) : K)) = (q : K)⁻¹ := Units.val_inv_eq_inv_val q

/-- `[k+1]_{q⁻²} = q^{-2k} [k+1]_{q²}`. -/
theorem jk_inv_eq (k : ℕ) :
    jk ((((q⁻¹ : Kˣ) : K)) * ((q⁻¹ : Kˣ) : K)) (k + 1) =
      ((q : K)⁻¹ * (q : K)⁻¹) ^ k * jk ((q : K) * q) (k + 1) := by
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  have h := jk_reverse (S := K) (y := (q : K) * q) (z := (q : K)⁻¹ * (q : K)⁻¹)
    (by field_simp) k
  rw [qi_eq_inv, ← h, ← mul_assoc, ← mul_pow,
    show ((q : K)⁻¹ * (q : K)⁻¹) * ((q : K) * q) = 1 by field_simp, one_pow, one_mul]

/-- **The block form against the Haar state.** For `j, k ≥ 0`,
`h(ζ^j · L ζ^{k+1}) = −q³ (−q)^{j+k} [j][k+1] / ([j+k+1][j+k+2])`, `[n] = [n]_{q²}`. -/
theorem haarState_zeta_pow_mul_lap (hq : ∀ n, qSqNum q n ≠ 0) (j k : ℕ) :
    haarState q (zetaB q ^ j * lap q (zetaB q ^ (k + 1))) =
      -((q : K) ^ 3 * (-(q : K)) ^ (j + k) * jk ((q : K) * q) j * jk ((q : K) * q) (k + 1)) /
        (jk ((q : K) * q) (j + k + 1) * jk ((q : K) * q) (j + k + 2)) := by
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  have h1 : jk ((q : K) * q) (j + k + 1) ≠ 0 := by rw [← qSqNum_eq_jk]; exact hq _
  have h2 : jk ((q : K) * q) (j + k + 2) ≠ 0 := by
    rw [show j + k + 2 = (j + k + 1) + 1 from rfl, ← qSqNum_eq_jk]; exact hq _
  rw [lap_zeta_pow, mul_add, mul_smul_comm, mul_smul_comm, ← pow_add, ← pow_add, map_add,
    map_smul, map_smul, haarState_zetaB_pow, haarState_zetaB_pow, haarMoment, haarMoment,
    qSqNum_eq_jk, qSqNum_eq_jk, smul_eq_mul, smul_eq_mul, jk_inv_eq,
    show j + (k + 1) + 1 = j + k + 2 by omega, show j + (k + 1) = j + k + 1 by omega]
  have e2 : jk ((q : K) * q) (j + k + 2) = 1 + (q : K) * q * jk ((q : K) * q) (j + k + 1) :=
    jk_succ' _ _
  have ek : jk ((q : K) * q) (k + 2) = 1 + (q : K) * q * jk ((q : K) * q) (k + 1) := jk_succ' _ _
  have e1 : jk ((q : K) * q) (j + k + 1) =
      jk ((q : K) * q) (k + 1) + ((q : K) * q) ^ (k + 1) * jk ((q : K) * q) j := by
    rw [show j + k + 1 = (k + 1) + j by omega, jk_add]
  rw [e2] at h2 ⊢
  rw [ek]
  rw [e1] at h1 h2 ⊢
  generalize jk ((q : K) * q) j = A at h1 h2 ⊢
  generalize jk ((q : K) * q) (k + 1) = B at h1 h2 ⊢
  have hY : ((q : K)⁻¹ * (q : K)⁻¹) ^ k * ((q : K) * q) ^ k = 1 := by
    rw [← mul_pow]; field_simp; simp
  rw [pow_succ ((q : K) * q) k] at h1 h2 ⊢
  rw [pow_succ (-(q : K)) (j + k)]
  generalize ((q : K)⁻¹ * (q : K)⁻¹) ^ k = Y at hY ⊢
  generalize ((q : K) * q) ^ k = X at hY h1 h2 ⊢
  generalize (-(q : K)) ^ (j + k) = P
  rw [mul_div_assoc', mul_div_assoc', div_add_div _ _ h1 h2,
    div_eq_div_iff (mul_ne_zero h1 h2) (mul_ne_zero h1 h2)]
  linear_combination (-((q : K) ^ 3 * P * A * B * ((B + X * ((q : K) * q) * A) *
    (1 + (q : K) * q * (B + X * ((q : K) * q) * A))))) * hY

theorem haarState_lap_const (hq : ∀ n, qSqNum q n ≠ 0) (k : ℕ) :
    haarState q (lap q (zetaB q ^ k)) = 0 := by
  rcases k with _ | k
  · rw [pow_zero, lap_one, map_zero]
  · have := haarState_zeta_pow_mul_lap q hq 0 k
    rw [pow_zero, one_mul] at this
    rw [this, jk_zero]; simp

/-- **`L` is symmetric for the Haar state on the block.** -/
theorem haarState_lap_symm (hq : ∀ n, qSqNum q n ≠ 0) (j n : ℕ) :
    haarState q (zetaB q ^ j * lap q (zetaB q ^ n)) =
      haarState q (zetaB q ^ n * lap q (zetaB q ^ j)) := by
  rcases n with _ | n
  · rw [pow_zero, lap_one, mul_zero, map_zero, one_mul, haarState_lap_const q hq]
  rcases j with _ | j
  · rw [pow_zero, lap_one, mul_zero, map_zero, one_mul, haarState_lap_const q hq]
  rw [haarState_zeta_pow_mul_lap q hq, haarState_zeta_pow_mul_lap q hq,
    show j + 1 + n = n + 1 + j by omega]
  ring

/-- Evaluation `K[X] → O_q(SU(2))`, `X ↦ ζ`: the torus-invariant block. -/
noncomputable def ev : Polynomial K →ₐ[K] OqSU2 K q := Polynomial.aeval (zetaB q)

theorem ev_monomial (n : ℕ) (c : K) : ev q (Polynomial.monomial n c) = c • zetaB q ^ n := by
  rw [ev, Polynomial.aeval_monomial, Algebra.smul_def]

theorem ev_comm (P Q : Polynomial K) : ev q P * ev q Q = ev q Q * ev q P := by
  rw [← map_mul, ← map_mul, mul_comm]

/-- Symmetry of `L` for `h` on all of `K[ζ]`. -/
theorem haarState_poly_lap_symm (hq : ∀ n, qSqNum q n ≠ 0) (P Q : Polynomial K) :
    haarState q (ev q P * lap q (ev q Q)) = haarState q (ev q Q * lap q (ev q P)) := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => simp only [map_add, add_mul, mul_add, h₁, h₂]
  | monomial n a =>
    induction Q using Polynomial.induction_on' with
    | add Q₁ Q₂ g₁ g₂ => simp only [map_add, add_mul, mul_add, g₁, g₂]
    | monomial m b =>
      simp only [ev_monomial, map_smul, smul_mul_assoc, mul_smul_comm, smul_eq_mul]
      rw [haarState_lap_symm q hq n m]
      ring

/-- **Orthogonality.** Eigenpolynomials of `L` with different eigenvalues are orthogonal for
the Haar state. -/
theorem haarState_eigen_orthogonal (hq : ∀ n, qSqNum q n ≠ 0) {P Q : Polynomial K} {l m : K}
    (hP : lap q (ev q P) = l • ev q P) (hQ : lap q (ev q Q) = m • ev q Q) (hne : l ≠ m) :
    haarState q (ev q P * ev q Q) = 0 := by
  have s := haarState_poly_lap_symm q hq P Q
  rw [hP, hQ, mul_smul_comm, mul_smul_comm, map_smul, map_smul, smul_eq_mul, smul_eq_mul,
    ev_comm q Q P] at s
  have h0 : (m - l) * haarState q (ev q P * ev q Q) = 0 := by linear_combination s
  rcases mul_eq_zero.mp h0 with h | h
  · exact absurd (sub_eq_zero.mp h).symm hne
  · exact h

/-- **Integration by parts on the block.** `h(X₊ ζ^j · X₋ ζ^k) = −q⁻² h(ζ^j · L ζ^k)`. -/
theorem haarState_budget_zeta_pow (hq : ∀ n, qSqNum q n ≠ 0) (j k : ℕ) :
    haarState q (fieldPlus q (zetaB q ^ j) * fieldMinus q (zetaB q ^ k)) =
      -((q : K)⁻¹ * (q : K)⁻¹) * haarState q (zetaB q ^ j * lap q (zetaB q ^ k)) := by
  rcases k with _ | k
  · rw [pow_zero, fieldMinus_one, lap_one, mul_zero, mul_zero, map_zero, mul_zero]
  rcases j with _ | j
  · rw [pow_zero, fieldPlus_one, zero_mul, map_zero, one_mul, haarState_lap_const q hq, mul_zero]
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  rw [haarState_zeta_pow_mul_lap q hq, fieldPlus_zeta_pow, fieldMinus_zeta_pow, smul_mul_assoc,
    mul_smul_comm, smul_smul, mul_assoc (zetaB q ^ j), ← mul_assoc (α q * γ q),
    alphaGamma_zeta_pow, smul_mul_assoc, mul_smul_comm, smul_smul, mul_assoc (zetaB q ^ k),
    alphaGamma_betaDelta, ← mul_assoc (zetaB q ^ j), ← pow_add, mul_add, mul_smul_comm,
    mul_smul_comm, ← mul_assoc, ← pow_succ, ← pow_succ, map_smul, map_add, map_smul, map_smul,
    haarState_zetaB_pow, haarState_zetaB_pow, haarMoment, haarMoment, qSqNum_eq_jk, qSqNum_eq_jk,
    jk_inv_eq, qi_eq_inv, smul_eq_mul, smul_eq_mul, smul_eq_mul]
  rw [show j + 1 + k = j + k + 1 by omega]
  have h2 : jk ((q : K) * q) (j + k + 1 + 1) ≠ 0 := by rw [← qSqNum_eq_jk]; exact hq _
  have h3 : jk ((q : K) * q) (j + k + 1 + 1 + 1) ≠ 0 := by rw [← qSqNum_eq_jk]; exact hq _
  have hJ3 : jk ((q : K) * q) (j + k + 1 + 1 + 1) =
      1 + (q : K) * q * jk ((q : K) * q) (j + k + 1 + 1) := jk_succ' _ _
  rw [show j + k + 1 + 2 = j + k + 1 + 1 + 1 from rfl, pow_succ (-(q : K)) (j + k + 1)]
  generalize jk ((q : K) * q) (j + k + 1 + 1 + 1) = J3 at h3 hJ3 ⊢
  generalize jk ((q : K) * q) (j + k + 1 + 1) = J2 at h2 hJ3 ⊢
  field_simp
  have hZ : (q : K) ^ (k * 2) * (q : K)⁻¹ ^ (k * 2) = 1 := by
    rw [← mul_pow, mul_inv_cancel₀ hq0, one_pow]
  linear_combination (jk ((q : K) ^ 2) (j + 1) * jk ((q : K) ^ 2) (k + 1) *
      ((q : K) ^ (k * 2) * (q : K)⁻¹ ^ (k * 2))) * hJ3 +
    (jk ((q : K) ^ 2) (j + 1) * jk ((q : K) ^ 2) (k + 1)) * hZ

/-- **The budget on `K[ζ]` is minus the Dirichlet form of `L`.**
`h(X₊ a · X₋ b) = −q⁻² h(a · L b)` for `a = ev P`, `b = ev Q`. -/
theorem haarState_budget_poly (hq : ∀ n, qSqNum q n ≠ 0) (P Q : Polynomial K) :
    haarState q (fieldPlus q (ev q P) * fieldMinus q (ev q Q)) =
      -((q : K)⁻¹ * (q : K)⁻¹) * haarState q (ev q P * lap q (ev q Q)) := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => simp only [map_add, add_mul, mul_add, h₁, h₂]
  | monomial n a =>
    induction Q using Polynomial.induction_on' with
    | add Q₁ Q₂ g₁ g₂ => simp only [map_add, mul_add, g₁, g₂]
    | monomial m b =>
      simp only [ev_monomial, map_smul, smul_mul_assoc, mul_smul_comm, smul_eq_mul]
      rw [haarState_budget_zeta_pow q hq n m]
      ring

/-- Every torus scaling fixes `ζ`. -/
theorem torus_zeta {S : Type*} [CommRing S] (p u b : Sˣ) :
    torusScaleAlgHom p u b (zetaB p) = zetaB p := by
  simp only [zetaB, map_mul, torusScaleAlgHom, liftQuadruple_beta, liftQuadruple_gamma,
    smul_mul_smul_comm, Units.mul_inv, one_smul]

/-- **The Cartan field kills the block.** For any twist `u` and normalisation `c⁻¹`, the
Cartan field `c⁻¹(f − R_u f)` vanishes on `K[ζ]`. So the Cartan budget `h(Xa · Xa)` is zero
on the torus-invariant block, and the off-diagonal pair carries the whole budget there. -/
theorem cartanField_ev (u : Kˣ) (cinv : K) (P : Polynomial K) :
    leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap)) (ev q P) =
      0 := by
  rw [(cartanField q u cinv 1 1).1, ev, ← Polynomial.aeval_algHom_apply, torus_zeta, sub_self,
    smul_zero]

end Haar

end QOU.AlgebraicSubstrate.OqSU2
