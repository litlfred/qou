import CompactQuantumMetrics.OqSU2LittleQJacobiBasis
import QOU.FluidDynamics.q_ns_block_haar_ibp

/-!
# QOU.FluidDynamics.q_ns_triad_raising_coupling — the spin-raising triad coupling

Bean `qou-q3dc` (progress on `qou-pa7n`, Part A of `conj:regularity-breakdown`, which stays
open). Triad front, magnitude question: how large are the quadratic couplings that move energy
into high spin?

Take the triad whose velocity mode is `βδ` (weight `(−1, 1)`), whose advected mode is the little
q-Jacobi polynomial `p_r(ζ)` on the Cartan block, and whose receiving mode is `p_n(ζ)`. Its
coupling along the twisted field `X₊` is

  `C(n, r) = h(p_n(ζ) · βδ · X₊ p_r(ζ))`.

The weights balance (`q_ns_haar_triad_weight`), and `a + m = 0` for the receiving block, so this
is a triad where the transfer is exactly skew.

## Results (over a field `K`, `q : Kˣ`, `q²` not a root of unity)

* `ev_raise`: `βδ · X₊ (P(ζ)) = (Raise P)(ζ)` for an explicit linear map `Raise` on `K[X]`,
  `Raise X^{k+1} = q⁻¹ [k+1]_{q²} q^{−2k} (X^{k+1} + q⁻¹ X^{k+2})`. The product reduces to the
  Cartan block (`betaDelta_zeta_pow`, `betaDelta_alphaGamma`).
* `raise_mem`: `Raise` raises degree by at most one.
* `haarState_jacobiPoly_mul_eq_zero_of_mem`: `h(p_n · P) = 0` for `deg P < n`.
* `haarState_jacobiPoly_mul_top`: `h(p_n · P) = (P_n / c_n) · h(p_n²)` for `deg P ≤ n`, where
  `c_n` is the top coefficient of `p_n`.
* **Finite reach** (`coupling_eq_zero_of_lt`): `C(n, r) = 0` for `n ≥ r + 2`. A spin-one velocity
  raises spin by at most one step (the q-Clebsch–Gordan bound `j ≤ j₁ + j₂`).
* **The raising coupling in closed form** (`coupling_raise`):
  `C(s+2, s+1) = κ_s · (c_{s+1} / c_{s+2}) · h(p_{s+2}²)`, with
  `κ_s = q⁻² [s+1]_{q²} q^{−2s}`.

So the size of every spin-raising coupling is fixed by the norms `h(p_n²)` alone.

## The norms (closed in `q_ns_qlegendre_norm`)

* **The closed form of `h(p_n²)`** is proved in `QOU/FluidDynamics/q_ns_qlegendre_norm.lean`
  (`H_eq_prod`, `haarState_jacobiPoly_sq_eq`, sorry-free, bean `qou-9obv`). For monic `P_n` it is the little
  q-Legendre norm
  `‖P_n‖² = q^{−2n} p^{n²} (p;p)_n⁴ (1 − p) / ((p;p)_{2n} (p;p)_{2n+1})`, with `p = q⁻²`
  ([gasper-rahman-2004] §7.3), stated there as a product of its ratios. Substituting it, the
  normalised raising coupling is
  `C̃(r)² = q^{−6} p^{2r+1} ((1 − p^r)/(1 − p))² (1 − p^{r+1})⁴ /
  ((1 − p^{2r+1})(1 − p^{2r+2})²(1 − p^{2r+3}) ‖βδ‖²)`. At fixed `q > 1` the square decays like
  `q^{−4r}`, so the amplitude `C̃(r)` decays like `q^{−2r}`; as `q → 1` the amplitude grows like
  `r`. The decay is not uniform in `q`. The norm-only part of this substitution is the Lean
  statement `QLegendreNorm.coupling_raise_sq`: `C_s² = (q⁻¹κ_s)² · H_{s+2}/H_{s+1} · ‖p_{s+2}‖²‖p_{s+1}‖²`.

## Not established

* Positivity of the norms over an ordered field, other velocity modes, other fields, any rate,
  and Part A.

No empirical value enters any proof. Sorry-free.
-/

namespace QOU.FluidDynamics.TriadRaising

open Polynomial Finset
open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2
open QOU.FluidDynamics.HaarFieldInvariance QOU.FluidDynamics.BlockLadder

variable {K : Type*} [Field K] (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))

/-! ## Orthogonal projection onto the top mode -/

theorem sub_top_mem {j : ℕ} (hc : (jacobiPoly q j).coeff j ≠ 0) {P : K[X]}
    (hP : P ∈ degreeLT K (j + 1)) :
    P - (P.coeff j / (jacobiPoly q j).coeff j) • jacobiPoly q j ∈ degreeLT K j := by
  rw [mem_degreeLT, degree_lt_iff_coeff_zero]
  intro m hm
  have hm' : j ≤ m := by exact_mod_cast hm
  have hPm := mem_degreeLT.mp hP
  have hJm := mem_degreeLT.mp (jacobiPoly_mem q j)
  rcases Nat.lt_or_ge j m with h | h
  · have hjm : ((j + 1 : ℕ) : WithBot ℕ) ≤ (m : WithBot ℕ) := by exact_mod_cast h
    have e1 : P.coeff m = 0 := coeff_eq_zero_of_degree_lt (hPm.trans_le hjm)
    have e2 : (jacobiPoly q j).coeff m = 0 := coeff_eq_zero_of_degree_lt (hJm.trans_le hjm)
    rw [coeff_sub, coeff_smul, e1, e2, smul_zero, sub_zero]
  · have : m = j := by omega
    subst this
    rw [coeff_sub, coeff_smul, smul_eq_mul, div_mul_cancel₀ _ hc, sub_self]

variable (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1)
include hp

/-- `h(p_n · P) = 0` for `deg P < n`. -/
theorem haarState_jacobiPoly_mul_eq_zero_of_mem {n j : ℕ} (hj : j ≤ n) {P : K[X]}
    (hP : P ∈ degreeLT K j) : haarState q (ev q (jacobiPoly q n) * ev q P) = 0 := by
  induction j generalizing P with
  | zero => rw [eq_zero_of_mem_degreeLT_zero hP, map_zero, mul_zero, map_zero]
  | succ j ih =>
    have hR := sub_top_mem q (coeff_jacobiPoly_ne_zero q hp j) hP
    set a := P.coeff j / (jacobiPoly q j).coeff j
    have hPeq : P = a • jacobiPoly q j + (P - a • jacobiPoly q j) := by abel
    rw [hPeq, map_add, map_smul, mul_add, mul_smul_comm, map_add, map_smul,
      haarState_jacobiPoly_orthogonal q hp (show n ≠ j by omega), smul_zero, zero_add]
    exact ih (by omega) hR

/-- `h(p_n · P) = (P_n / c_n) · h(p_n²)` for `deg P ≤ n`. -/
theorem haarState_jacobiPoly_mul_top {n : ℕ} {P : K[X]} (hP : P ∈ degreeLT K (n + 1)) :
    haarState q (ev q (jacobiPoly q n) * ev q P) =
      (P.coeff n / (jacobiPoly q n).coeff n) *
        haarState q (ev q (jacobiPoly q n) * ev q (jacobiPoly q n)) := by
  have hR := sub_top_mem q (coeff_jacobiPoly_ne_zero q hp n) hP
  set a := P.coeff n / (jacobiPoly q n).coeff n
  have hPeq : P = a • jacobiPoly q n + (P - a • jacobiPoly q n) := by abel
  conv_lhs => rw [hPeq]
  rw [map_add, map_smul, mul_add, mul_smul_comm, map_add, map_smul,
    haarState_jacobiPoly_mul_eq_zero_of_mem q hp le_rfl hR, add_zero, smul_eq_mul]

omit hp

/-! ## The raising map -/

/-- Coefficient of `βδ · X₊ ζ^{k+1}`. -/
noncomputable def kap (k : ℕ) : K := qi * jk ((q : K) * q) (k + 1) * (qi * qi) ^ k

/-- `βδ · X₊` on `X^n`. -/
noncomputable def raiseX : ℕ → K[X]
  | 0 => 0
  | k + 1 => C (kap q k) * (X ^ (k + 1) + C qi * X ^ (k + 2))

/-- `βδ · X₊` transported to `K[X]`. -/
noncomputable def Raise : K[X] →ₗ[K] K[X] :=
  lsum fun n => LinearMap.smulRight LinearMap.id (raiseX q n)

theorem Raise_monomial (n : ℕ) (c : K) : Raise q (monomial n c) = c • raiseX q n := by
  simp [Raise, lsum_apply, sum_monomial_index]

theorem Raise_X_pow (n : ℕ) : Raise q (X ^ n) = raiseX q n := by
  rw [← monomial_one_right_eq_X_pow, Raise_monomial, one_smul]

theorem ev_raiseX (n : ℕ) :
    ev q (raiseX q n) = (β q * δ q) * fieldPlus q (zetaB q ^ n) := by
  cases n with
  | zero => simp [raiseX, fieldPlus_one]
  | succ k =>
    rw [fieldPlus_zeta_pow, mul_smul_comm, ← mul_assoc, betaDelta_zeta_pow, smul_mul_assoc,
      mul_assoc, betaDelta_alphaGamma, smul_smul]
    rw [raiseX]
    simp only [map_mul, map_add, map_pow, ev, aeval_C, aeval_X]
    rw [Algebra.algebraMap_eq_smul_one, Algebra.algebraMap_eq_smul_one]
    simp only [smul_mul_assoc, one_mul, kap]
    congr 1
    simp only [pow_succ, mul_assoc, mul_add, mul_smul_comm]

/-- **`βδ · X₊ P(ζ) = (Raise P)(ζ)`.** -/
theorem ev_raise (P : K[X]) :
    ev q (Raise q P) = (β q * δ q) * fieldPlus q (ev q P) := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => simp only [map_add, h₁, h₂, mul_add]
  | monomial n c =>
    rw [Raise_monomial, map_smul, ev_raiseX, ev_monomial, map_smul, mul_smul_comm]

theorem raiseX_mem (k : ℕ) : raiseX q k ∈ degreeLT K (k + 2) := by
  cases k with
  | zero => simp [raiseX]
  | succ k =>
    rw [raiseX, mul_add, ← mul_assoc, ← C_mul]
    exact Submodule.add_mem _ (CX_mem _ (by omega)) (CX_mem _ (by omega))

/-- `Raise` raises degree by at most one. -/
theorem raise_mem (m : ℕ) {P : K[X]} (hP : P ∈ degreeLT K (m + 1)) :
    Raise q P ∈ degreeLT K (m + 2) := by
  classical
  have hsub : degreeLT K (m + 1) ≤ (degreeLT K (m + 2)).comap (Raise q) := by
    rw [degreeLT_eq_span_X_pow, Submodule.span_le]
    intro x hx
    simp only [coe_image, coe_range, Set.mem_image, Set.mem_Iio] at hx
    obtain ⟨k, hk, rfl⟩ := hx
    rw [SetLike.mem_coe, Submodule.mem_comap, Raise_X_pow]
    exact degreeLT_mono (by omega) (raiseX_mem q k)
  exact hsub hP

/-- `Raise` raises degree by at most one, and its new top coefficient is `κ · P_{m}`. -/
theorem raise_mem_and_coeff (m : ℕ) {P : K[X]} (hP : P ∈ degreeLT K (m + 2)) :
    Raise q P ∈ degreeLT K (m + 3) ∧
      (Raise q P).coeff (m + 2) = kap q m * qi * P.coeff (m + 1) := by
  classical
  let M : K[X] →ₗ[K] K := (lcoeff K (m + 2)).comp (Raise q) - (kap q m * qi) • lcoeff K (m + 1)
  have hM : ∀ R, M R = (Raise q R).coeff (m + 2) - kap q m * qi * R.coeff (m + 1) := by
    intro R; simp [M, smul_eq_mul]
  have hsub : degreeLT K (m + 2) ≤ (degreeLT K (m + 3)).comap (Raise q) ⊓ LinearMap.ker M := by
    rw [degreeLT_eq_span_X_pow, Submodule.span_le]
    intro x hx
    simp only [coe_image, coe_range, Set.mem_image, Set.mem_Iio] at hx
    obtain ⟨k, hk, rfl⟩ := hx
    refine ⟨?_, ?_⟩
    · rw [SetLike.mem_coe, Submodule.mem_comap, Raise_X_pow]
      exact degreeLT_mono (by omega) (raiseX_mem q k)
    · rw [SetLike.mem_coe, LinearMap.mem_ker, hM, Raise_X_pow, coeff_X_pow]
      rcases Nat.lt_or_ge k (m + 1) with h | h
      · rw [if_neg (by omega), mul_zero, sub_zero]
        exact coeff_eq_zero_of_degree_lt
          ((mem_degreeLT.mp (raiseX_mem q k)).trans_le (by exact_mod_cast (by omega : k + 2 ≤ m + 2)))
      · have : k = m + 1 := by omega
        subst this
        rw [if_pos rfl, mul_one, raiseX]
        simp [mul_add, coeff_C_mul, coeff_X_pow]
  have h := hsub hP
  refine ⟨h.1, ?_⟩
  have h2 := h.2
  rw [SetLike.mem_coe, LinearMap.mem_ker, hM] at h2
  exact sub_eq_zero.mp h2

/-! ## The couplings -/

include hp

/-- **Finite reach.** A spin-one velocity raises spin by at most one step. -/
theorem coupling_eq_zero_of_lt {n r : ℕ} (hn : r + 2 ≤ n) :
    haarState q (ev q (jacobiPoly q n) * ((β q * δ q) * fieldPlus q (ev q (jacobiPoly q r)))) =
      0 := by
  rw [← ev_raise]
  refine haarState_jacobiPoly_mul_eq_zero_of_mem q hp hn ?_
  exact raise_mem q r (jacobiPoly_mem q r)

/-- **The raising coupling.**
`h(p_{s+2} · βδ · X₊ p_{s+1}) = κ_s (c_{s+1} / c_{s+2}) h(p_{s+2}²)`, where
`κ_s = kap s · q⁻¹ = q⁻² [s+1]_{q²} q^{−2s}`. -/
theorem coupling_raise (s : ℕ) :
    haarState q (ev q (jacobiPoly q (s + 2)) *
        ((β q * δ q) * fieldPlus q (ev q (jacobiPoly q (s + 1))))) =
      (kap q s * qi * (jacobiPoly q (s + 1)).coeff (s + 1) /
          (jacobiPoly q (s + 2)).coeff (s + 2)) *
        haarState q (ev q (jacobiPoly q (s + 2)) * ev q (jacobiPoly q (s + 2))) := by
  obtain ⟨hmem, hcoeff⟩ := raise_mem_and_coeff q s (jacobiPoly_mem q (s + 1))
  rw [← ev_raise, haarState_jacobiPoly_mul_top q hp hmem, hcoeff]

end QOU.FluidDynamics.TriadRaising
