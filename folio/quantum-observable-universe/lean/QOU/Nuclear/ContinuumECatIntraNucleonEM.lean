import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FinCases
import QOU.Nuclear.ProtonBorromeanAssembly

/-!
# Continuum `E_cat` Subdivision Convergence, `H_3` Schur Duality, and Intra-Nucleon Borromean EM

Workstream W10 / `Q-Gap-6` + Charge-Unit `L_cal` Route 1 (beans `qou-mjo7`, `qou-pzsi`,
`qou-37y0`, `qou-17mq`, `qou-zp6a`, `qou-awxv`).

Every declaration in this module is stated over a generic commutative ring `[CommRing R]`,
field `[Field K]`, or strict ordered field `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`
(§7c base-ring discipline: zero `ℝ`, zero empirical literals, zero `sorry`, zero custom axioms).

## Main Results

1. **Discrete-to-Continuum `E_cat` Subdivision Convergence (`qou-pzsi`):**
   - `regInvDistSq_lipschitz` & `regPairKernel_lipschitz`: For any short-distance regulator
     `0 < δ` in an ordered field `K`, the regulated chordal/pair kernel
     `K_δ(u, v) = ((u - v)² + δ²)⁻¹` satisfies the global `ℓ¹`-Lipschitz bound
     `|K_δ(u₁, v₁) - K_δ(u₂, v₂)| ≤ (1 / δ³) * (|u₁ - u₂| + |v₁ - v₂|)` on all of `K × K`.
   - `subdivision_riemann_error_bound`: For the discrete `N`-point pair-interaction sum
     `S_N = (1 / N²) ∑_{i,j < N} K(i / N, j / N)` and any continuum cell-average decomposition
     `I = (1 / N²) ∑_{i,j < N} cellAvg i j` with per-cell Lipschitz error `≤ C_δ / N`,
     `|S_N - I| ≤ C_δ / N`.
   - `subdivision_dyadic_step_bound` & `regPairKernel_dyadic_step_bound`: Unconditional dyadic
     refinement bound `|S_N(K) - S_{2N}(K)| ≤ L_δ / (2 * N)`, instantiated directly at
     `K_δ` as `|S_N(K_δ) - S_{2N}(K_δ)| ≤ 1 / (2 * δ³ * N)`.

2. **`S_3` / `H_3(q²)` Wedderburn Block Decomposition, Schur Self-Duality, and Proton
   `(k₁ = -3, k₂ = 2, k₃ = 12)` Characterization (`qou-mjo7`, `qou-pzsi`):**
   - `wedderburn_dim_H3` & `ecat_regular_block_decomposition`: On the three partitions
     `(3), (2,1), (1³)` of `3` with Specht dimensions `(1, 2, 1)`, `∑_λ d_λ² = 6` and the
     regular trace decomposes as `E_cat = E_{(3)} + 2 * E_{(2,1)} + E_{(1³)}`.
   - `conjPart3_fixed_iff` & `schurH3_conj_duality`: Conjugate-partition duality swaps
     `(3) ↔ (1³)` and fixes `(2,1)` uniquely; the three `H_3(Q)` Schur elements satisfy
     `schurH3 Q⁻¹ λ = schurH3 Q (conjPart3 λ)` for all `Q ≠ 0`.
   - `schurH3_molien_sum_eq_one` & `schurH3_std21_mult_unique`: The Molien/Plancherel identity
     `1 / c_{(3)}(Q) + m / c_{(2,1)}(Q) + 1 / c_{(1³)}(Q) = 1` holds iff `m = 2 = dim S^{(2,1)}`.
   - `schurH3_sign111_eq_qFact3_div_q_cubed` & `proton_k_minus3_sign_schur_iff`: In balanced
     Hecke variables (`Q = q²`), `c_{(1³)}(q²) = [3]_q! / q³`, and over any ordered field at
     `0 < q ≠ 1`, `q ^ k * [3]_q! = c_{(1³)}(q²) ↔ k = -3`, while at `q = 1`,
     `dim S^{(2,1)} * c_{(1³)}(1) = 2 * 6 = 12` (`proton_structural_integers_12`, bridging to
     `QOU.AppendixQValues.ProtonBorromeanAssembly`).

3. **Intra-Nucleon Borromean Electromagnetic Self-Energy & Scheme-Comparable `m_d - m_u`
   (`qou-37y0`, `qou-17mq`, `qou-zp6a`, `qou-awxv` Gate G-II):**
   - Exact quark-charge sum rules at `(q_u, q_d) = (2/3, -1/3)`:
     * `proton_pair_charge_sum_eq_zero`: `∑_{i<j} Q_i Q_j(p) = 0`.
     * `neutron_pair_charge_sum_eq_neg_third`: `∑_{i<j} Q_i Q_j(n) = -1/3`.
     * `pn_pair_charge_diff_eq_third`: `∑_{i<j} Q_i Q_j(p) - ∑_{i<j} Q_i Q_j(n) = 1/3`.
     * `pn_self_charge_diff_eq_third`: `∑_i Q_i²(p) = 1`, `∑_i Q_i²(n) = 2/3`, difference `1/3`.
   - `odd_milnor_functional_vanishes` & `even_milnor_sq_distinguishes_borromean_from_unlink`:
     Any functional odd in the Milnor triple linking number `μ̄_{123}` and symmetric under
     exchanging like-charged quarks vanishes identically, whereas `μ̄_{123}²` is exchange-even,
     vanishes on the 3-unlink (`0`), and equals `1` on both chiralities `B_3^±` (`μ̄_{123} = ±1`).
   - `strong_md_sub_mu_decomposition` & `route1_self_consistent_em_pos`: Removing the repulsive
     intra-nucleon Borromean EM self-energy yields
     `(m_d - m_u)_scheme = (m_n - m_p) + (1/6) K_self + (1/3) K₀ > m_n - m_p` whenever `K₀ > 0`
     and `K_self ≥ 0` (and under `L_cal` Route 1, `Δ_EM = α * m_model * f > 0` whenever
     `α, m_model, f > 0`).
   - `intranucleon_em_cancels_in_nuclear_binding` & `o2_neutralized_h3_green_positivity_window`:
     Single-nucleon intra-baryon EM self-energy cancels identically in nuclear binding energies
     `B(Z, N)`, and the O2 zero-mean `H³` Green's kernel `(u + 1)/(u - 1) - c₀` is strictly
     positive throughout `1 < u < (c₀ + 1)/(c₀ - 1)`.

-- Ref: [leitner2026] appendix-standard-model/sm-gating-objects.md §2 (Gate G-II)
-- Ref: [leitner2026] QOU/QBeta/ECatBlockDecomposition.lean
-- Ref: [leitner2026] QOU/AppendixQValues/ProtonBorromeanAssembly.lean
-- Ref: [geckpfeiffer2000] Characters of Finite Coxeter Groups and Iwahori-Hecke Algebras, §10.5
-- Ref: [milnor1954] J. Milnor, Ann. of Math. 59 (1954), 177-205
-/

namespace QOU.QBeta.ContinuumECatIntraNucleonEM

open BigOperators

/-! ## Part I. Discrete-to-Continuum `E_cat` Subdivision Convergence (`qou-pzsi`) -/

section ContinuumSubdivision

/-- Short-distance regulated inverse-square kernel `K_δ(r) = 1 / (r² + δ²)`. -/
def regInvDistSq {K : Type*} [Field K] (δ r : K) : K :=
  1 / (r ^ 2 + δ ^ 2)

/-- Two-point regulated pair-interaction kernel `K_δ(u, v) = 1 / ((u - v)² + δ²)`. -/
def regPairKernel {K : Type*} [Field K] (δ u v : K) : K :=
  regInvDistSq δ (u - v)

/-- Discrete `N`-point pair-interaction Riemann sum on `[0, 1)²`:
`S_N(K) = (1 / N²) ∑_{i,j < N} K(i / N, j / N)`. -/
def discretePairSum {K : Type*} [Field K] (K_ker : K → K → K) (N : ℕ) : K :=
  (1 / (N : K) ^ 2) *
    ∑ i : Fin N, ∑ j : Fin N, K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K))

/-- **Global Lipschitz regularity of the regulated inverse-square kernel:**
Over any strict ordered field `K`, for every `0 < δ` and all `r₁, r₂ : K`,
`|1 / (r₁² + δ²) - 1 / (r₂² + δ²)| ≤ (1 / δ³) * |r₁ - r₂|`. -/
theorem regInvDistSq_lipschitz {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {δ : K} (hδ : 0 < δ) (r₁ r₂ : K) :
    |regInvDistSq δ r₁ - regInvDistSq δ r₂| ≤ (1 / δ ^ 3) * |r₁ - r₂| := by
  have hδ2 : 0 < δ ^ 2 := pow_pos hδ 2
  have hδ3 : 0 < δ ^ 3 := pow_pos hδ 3
  have hD1 : 0 < r₁ ^ 2 + δ ^ 2 := add_pos_of_nonneg_of_pos (sq_nonneg r₁) hδ2
  have hD2 : 0 < r₂ ^ 2 + δ ^ 2 := add_pos_of_nonneg_of_pos (sq_nonneg r₂) hδ2
  have hD12 : 0 < (r₁ ^ 2 + δ ^ 2) * (r₂ ^ 2 + δ ^ 2) := mul_pos hD1 hD2
  have hD1_ne : r₁ ^ 2 + δ ^ 2 ≠ 0 := ne_of_gt hD1
  have hD2_ne : r₂ ^ 2 + δ ^ 2 ≠ 0 := ne_of_gt hD2
  have hsub : regInvDistSq δ r₁ - regInvDistSq δ r₂ =
      (r₂ - r₁) * (r₁ + r₂) / ((r₁ ^ 2 + δ ^ 2) * (r₂ ^ 2 + δ ^ 2)) := by
    unfold regInvDistSq
    field_simp
    ring
  rw [hsub, abs_div, abs_mul, abs_sub_comm r₂ r₁, abs_of_pos hD12, one_div_mul_eq_div]
  rw [div_le_div_iff₀ hD12 hδ3]
  have ham1 : 2 * δ * |r₁| ≤ r₁ ^ 2 + δ ^ 2 := by
    have hsq : 0 ≤ (|r₁| - δ) ^ 2 := sq_nonneg (|r₁| - δ)
    have habs2 : |r₁| ^ 2 = r₁ ^ 2 := sq_abs r₁
    linarith
  have ham2 : 2 * δ * |r₂| ≤ r₂ ^ 2 + δ ^ 2 := by
    have hsq : 0 ≤ (|r₂| - δ) ^ 2 := sq_nonneg (|r₂| - δ)
    have habs2 : |r₂| ^ 2 = r₂ ^ 2 := sq_abs r₂
    linarith
  have hprod1 : 2 * |r₁| * δ ^ 3 ≤ (r₁ ^ 2 + δ ^ 2) * (r₂ ^ 2 + δ ^ 2) := by
    have hle2 : δ ^ 2 ≤ r₂ ^ 2 + δ ^ 2 := le_add_of_nonneg_left (sq_nonneg r₂)
    have hmul : (2 * δ * |r₁|) * δ ^ 2 ≤ (r₁ ^ 2 + δ ^ 2) * (r₂ ^ 2 + δ ^ 2) :=
      mul_le_mul ham1 hle2 (le_of_lt hδ2) (le_of_lt hD1)
    linarith
  have hprod2 : 2 * |r₂| * δ ^ 3 ≤ (r₁ ^ 2 + δ ^ 2) * (r₂ ^ 2 + δ ^ 2) := by
    have hle1 : δ ^ 2 ≤ r₁ ^ 2 + δ ^ 2 := le_add_of_nonneg_left (sq_nonneg r₁)
    have hmul : δ ^ 2 * (2 * δ * |r₂|) ≤ (r₁ ^ 2 + δ ^ 2) * (r₂ ^ 2 + δ ^ 2) :=
      mul_le_mul hle1 ham2 (by positivity) (le_of_lt hD1)
    linarith
  have hsum_bound : |r₁ + r₂| * δ ^ 3 ≤ (r₁ ^ 2 + δ ^ 2) * (r₂ ^ 2 + δ ^ 2) := by
    have htri : |r₁ + r₂| ≤ |r₁| + |r₂| := abs_add_le r₁ r₂
    have htri_mul : |r₁ + r₂| * δ ^ 3 ≤ (|r₁| + |r₂|) * δ ^ 3 :=
      mul_le_mul_of_nonneg_right htri (le_of_lt hδ3)
    linarith
  have hfinal : (|r₁ - r₂| * |r₁ + r₂|) * δ ^ 3 = |r₁ - r₂| * (|r₁ + r₂| * δ ^ 3) := by ring
  rw [hfinal]
  exact mul_le_mul_of_nonneg_left hsum_bound (abs_nonneg (r₁ - r₂))

/-- **Two-variable `ℓ¹`-Lipschitz bound for `regPairKernel`:**
For any `0 < δ` and `u₁, v₁, u₂, v₂ : K`,
`|K_δ(u₁, v₁) - K_δ(u₂, v₂)| ≤ (1 / δ³) * (|u₁ - u₂| + |v₁ - v₂|)`. -/
theorem regPairKernel_lipschitz {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {δ : K} (hδ : 0 < δ) (u₁ v₁ u₂ v₂ : K) :
    |regPairKernel δ u₁ v₁ - regPairKernel δ u₂ v₂| ≤
      (1 / δ ^ 3) * (|u₁ - u₂| + |v₁ - v₂|) := by
  unfold regPairKernel
  have h1 := regInvDistSq_lipschitz hδ (u₁ - v₁) (u₂ - v₂)
  have hdiff : (u₁ - v₁) - (u₂ - v₂) = (u₁ - u₂) + (v₂ - v₁) := by ring
  have htri : |(u₁ - v₁) - (u₂ - v₂)| ≤ |u₁ - u₂| + |v₁ - v₂| := by
    rw [hdiff, abs_sub_comm v₁ v₂]
    exact abs_add_le (u₁ - u₂) (v₂ - v₁)
  have hpos : 0 ≤ 1 / δ ^ 3 := by
    have : 0 < δ ^ 3 := pow_pos hδ 3
    positivity
  exact le_trans h1 (mul_le_mul_of_nonneg_left htri hpos)

/-- **Riemann Cell-Average Subdivision Error Bound (`|S_N(δ) - I(δ)| ≤ C(δ) / N`):**
Over any strict ordered field `K`, if `I_cont` decomposes over the `N × N` grid cells via cell
averages `cellAvg : Fin N → Fin N → K` satisfying the per-cell Lipschitz oscillation bound
`|K_ker (i / N) (j / N) - cellAvg i j| ≤ C_δ / N`, then the global pair-sum discretization error
satisfies `|discretePairSum K_ker N - I_cont| ≤ C_δ / N`. -/
theorem subdivision_riemann_error_bound {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] (K_ker : K → K → K) {N : ℕ} (hN : 0 < N)
    (cellAvg : Fin N → Fin N → K) {I_cont C_δ : K}
    (hI : I_cont = (1 / (N : K) ^ 2) * ∑ i : Fin N, ∑ j : Fin N, cellAvg i j)
    (hcell : ∀ i j : Fin N,
      |K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K)) - cellAvg i j| ≤ C_δ / (N : K)) :
    |discretePairSum K_ker N - I_cont| ≤ C_δ / (N : K) := by
  have hN_pos : (0 : K) < (N : K) := Nat.cast_pos.mpr hN
  have hN_ne : (N : K) ≠ 0 := ne_of_gt hN_pos
  have hinv_pos : (0 : K) < 1 / (N : K) ^ 2 := one_div_pos.mpr (pow_pos hN_pos 2)
  have hdiff : discretePairSum K_ker N - I_cont =
      (1 / (N : K) ^ 2) * ∑ i : Fin N, ∑ j : Fin N,
        (K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K)) - cellAvg i j) := by
    rw [discretePairSum, hI, ← mul_sub, ← Finset.sum_sub_distrib]
    congr 1
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [← Finset.sum_sub_distrib]
  rw [hdiff, abs_mul, abs_of_pos hinv_pos]
  have hsum_le :
      |∑ i : Fin N, ∑ j : Fin N,
        (K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K)) - cellAvg i j)| ≤
      (N : K) ^ 2 * (C_δ / (N : K)) := by
    calc
      |∑ i : Fin N, ∑ j : Fin N,
          (K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K)) - cellAvg i j)|
        ≤ ∑ i : Fin N, |∑ j : Fin N,
            (K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K)) - cellAvg i j)| :=
          Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ i : Fin N, ∑ j : Fin N,
            |K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K)) - cellAvg i j| := by
          refine Finset.sum_le_sum fun i _ => Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ _i : Fin N, ∑ _j : Fin N, (C_δ / (N : K)) := by
          refine Finset.sum_le_sum fun i _ => Finset.sum_le_sum fun j _ => hcell i j
      _ = (N : K) ^ 2 * (C_δ / (N : K)) := by
          simp [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
          ring
  calc
    (1 / (N : K) ^ 2) *
        |∑ i : Fin N, ∑ j : Fin N,
          (K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K)) - cellAvg i j)|
      ≤ (1 / (N : K) ^ 2) * ((N : K) ^ 2 * (C_δ / (N : K))) :=
        mul_le_mul_of_nonneg_left hsum_le (le_of_lt hinv_pos)
    _ = C_δ / (N : K) := by
        field_simp

/-- Pairwise grouping of a `Fin (2 * N)` sum into `N` consecutive dyadic pairs `(2i, 2i + 1)`. -/
theorem sum_fin_two_mul {M : Type*} [AddCommMonoid M] (N : ℕ) (g : ℕ → M) :
    (∑ k : Fin (2 * N), g k.val) = ∑ i : Fin N, (g (2 * i.val) + g (2 * i.val + 1)) := by
  induction N with
  | zero => simp
  | succ n ih =>
    have h2n : 2 * (n + 1) = (2 * n + 1) + 1 := by omega
    rw [Fin.sum_univ_castSucc (n := n)]
    -- Rewrite LHS via Fin.castIso on h2n
    have hlhs : (∑ k : Fin (2 * (n + 1)), g k.val) =
        (∑ k : Fin (2 * n), g k.val) + (g (2 * n) + g (2 * n + 1)) := by
      have hcast : (∑ k : Fin (2 * (n + 1)), g k.val) =
          ∑ k : Fin ((2 * n + 1) + 1), g k.val := by
        refine Fintype.sum_equiv (Fin.castOrderIso h2n).toEquiv _ _ fun k => rfl
      rw [hcast, Fin.sum_univ_castSucc, Fin.sum_univ_castSucc]
      simp [add_assoc]
    rw [hlhs, ih]
    simp

/-- **Unconditional Dyadic Subdivision Step Bound (`|S_N(K) - S_{2N}(K)| ≤ L / (2 * N)`):**
For any two-variable `ℓ¹`-Lipschitz kernel `K_ker` with constant `L` and any `0 < N`,
refining the grid from `N` to `2 * N` changes `discretePairSum` by at most `L / (2 * N)`. -/
theorem subdivision_dyadic_step_bound {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] (K_ker : K → K → K) {L : K}
    (hlip : ∀ u₁ v₁ u₂ v₂ : K, |K_ker u₁ v₁ - K_ker u₂ v₂| ≤ L * (|u₁ - u₂| + |v₁ - v₂|))
    {N : ℕ} (hN : 0 < N) :
    |discretePairSum K_ker N - discretePairSum K_ker (2 * N)| ≤ L / (2 * (N : K)) := by
  have hN_pos : (0 : K) < (N : K) := Nat.cast_pos.mpr hN
  have hN_ne : (N : K) ≠ 0 := ne_of_gt hN_pos
  have h2N_pos : (0 : K) < 2 * (N : K) := by positivity
  have h4N2_pos : (0 : K) < 4 * (N : K) ^ 2 := by positivity
  -- Split S_{2N} over Fin N × Fin N blocks of 4 sub-nodes
  have hS2N : discretePairSum K_ker (2 * N) =
      (1 / (4 * (N : K) ^ 2)) * ∑ i : Fin N, ∑ j : Fin N,
        (K_ker (((2 * i.val : ℕ) : K) / (2 * (N : K))) (((2 * j.val : ℕ) : K) / (2 * (N : K))) +
         K_ker (((2 * i.val + 1 : ℕ) : K) / (2 * (N : K))) (((2 * j.val : ℕ) : K) / (2 * (N : K))) +
         K_ker (((2 * i.val : ℕ) : K) / (2 * (N : K))) (((2 * j.val + 1 : ℕ) : K) / (2 * (N : K))) +
         K_ker (((2 * i.val + 1 : ℕ) : K) / (2 * (N : K))) (((2 * j.val + 1 : ℕ) : K) / (2 * (N : K)))) := by
    unfold discretePairSum
    have hcast2N : ((2 * N : ℕ) : K) = 2 * (N : K) := by push_cast; ring
    rw [hcast2N]
    have hinv : (1 : K) / (2 * (N : K)) ^ 2 = 1 / (4 * (N : K) ^ 2) := by ring
    rw [hinv]
    congr 1
    rw [sum_fin_two_mul N (fun a => ∑ j : Fin (2 * N), K_ker ((a : K) / (2 * (N : K))) ((j.val : K) / (2 * (N : K))))]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [sum_fin_two_mul N (fun b => K_ker (((2 * i.val : ℕ) : K) / (2 * (N : K))) ((b : K) / (2 * (N : K))))]
    rw [sum_fin_two_mul N (fun b => K_ker (((2 * i.val + 1 : ℕ) : K) / (2 * (N : K))) ((b : K) / (2 * (N : K))))]
    rw [← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun j _ => ?_
    ring
  have hSN : discretePairSum K_ker N =
      (1 / (4 * (N : K) ^ 2)) * ∑ i : Fin N, ∑ j : Fin N,
        (4 * K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K))) := by
    unfold discretePairSum
    have hmul4 : ∑ i : Fin N, ∑ j : Fin N,
        (4 * K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K))) =
      4 * ∑ i : Fin N, ∑ j : Fin N, K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K)) := by
      rw [Finset.mul_sum]
      refine Finset.sum_congr rfl fun i _ => ?_
      rw [Finset.mul_sum]
    rw [hmul4]
    field_simp
  -- Bound each 4-subcell discrepancy by 2 * L / N
  have hblock : ∀ i j : Fin N,
      |4 * K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K)) -
        (K_ker (((2 * i.val : ℕ) : K) / (2 * (N : K))) (((2 * j.val : ℕ) : K) / (2 * (N : K))) +
         K_ker (((2 * i.val + 1 : ℕ) : K) / (2 * (N : K))) (((2 * j.val : ℕ) : K) / (2 * (N : K))) +
         K_ker (((2 * i.val : ℕ) : K) / (2 * (N : K))) (((2 * j.val + 1 : ℕ) : K) / (2 * (N : K))) +
         K_ker (((2 * i.val + 1 : ℕ) : K) / (2 * (N : K))) (((2 * j.val + 1 : ℕ) : K) / (2 * (N : K))))| ≤
        2 * L / (N : K) := by
    intro i j
    set xi : K := (i.val : K) / (N : K)
    set xj : K := (j.val : K) / (N : K)
    set hstep : K := 1 / (2 * (N : K))
    have hhstep_pos : 0 < hstep := one_div_pos.mpr h2N_pos
    have hx0 : ((2 * i.val : ℕ) : K) / (2 * (N : K)) = xi := by
      simp only [xi]; push_cast; field_simp
    have hy0 : ((2 * j.val : ℕ) : K) / (2 * (N : K)) = xj := by
      simp only [xj]; push_cast; field_simp
    have hx1 : ((2 * i.val + 1 : ℕ) : K) / (2 * (N : K)) = xi + hstep := by
      simp only [xi, hstep]; push_cast; field_simp
    have hy1 : ((2 * j.val + 1 : ℕ) : K) / (2 * (N : K)) = xj + hstep := by
      simp only [xj, hstep]; push_cast; field_simp
    rw [hx0, hy0, hx1, hy1]
    have hsplit : 4 * K_ker xi xj -
        (K_ker xi xj + K_ker (xi + hstep) xj + K_ker xi (xj + hstep) + K_ker (xi + hstep) (xj + hstep)) =
      (K_ker xi xj - K_ker (xi + hstep) xj) +
        ((K_ker xi xj - K_ker xi (xj + hstep)) + (K_ker xi xj - K_ker (xi + hstep) (xj + hstep))) := by
      ring
    rw [hsplit]
    have hb1 : |K_ker xi xj - K_ker (xi + hstep) xj| ≤ L * hstep := by
      have h := hlip xi xj (xi + hstep) xj
      have hd : |xi - (xi + hstep)| + |xj - xj| = hstep := by
        have : xi - (xi + hstep) = -hstep := by ring
        rw [this, sub_self, abs_zero, add_zero, abs_neg, abs_of_pos hhstep_pos]
      rw [hd] at h; exact h
    have hb2 : |K_ker xi xj - K_ker xi (xj + hstep)| ≤ L * hstep := by
      have h := hlip xi xj xi (xj + hstep)
      have hd : |xi - xi| + |xj - (xj + hstep)| = hstep := by
        have : xj - (xj + hstep) = -hstep := by ring
        rw [this, sub_self, abs_zero, zero_add, abs_neg, abs_of_pos hhstep_pos]
      rw [hd] at h; exact h
    have hb3 : |K_ker xi xj - K_ker (xi + hstep) (xj + hstep)| ≤ L * (2 * hstep) := by
      have h := hlip xi xj (xi + hstep) (xj + hstep)
      have hd : |xi - (xi + hstep)| + |xj - (xj + hstep)| = 2 * hstep := by
        have hxi : xi - (xi + hstep) = -hstep := by ring
        have hxj : xj - (xj + hstep) = -hstep := by ring
        rw [hxi, hxj, abs_neg, abs_of_pos hhstep_pos]; ring
      rw [hd] at h; exact h
    have htri1 := abs_add_le (K_ker xi xj - K_ker (xi + hstep) xj)
      ((K_ker xi xj - K_ker xi (xj + hstep)) + (K_ker xi xj - K_ker (xi + hstep) (xj + hstep)))
    have htri2 := abs_add_le (K_ker xi xj - K_ker xi (xj + hstep))
      (K_ker xi xj - K_ker (xi + hstep) (xj + hstep))
    have h4h : L * hstep + L * hstep + L * (2 * hstep) = 2 * L / (N : K) := by
      simp only [hstep]; field_simp; ring
    linarith
  set cellErr : Fin N → Fin N → K := fun i j =>
    4 * K_ker ((i.val : K) / (N : K)) ((j.val : K) / (N : K)) -
      (K_ker (((2 * i.val : ℕ) : K) / (2 * (N : K))) (((2 * j.val : ℕ) : K) / (2 * (N : K))) +
       K_ker (((2 * i.val + 1 : ℕ) : K) / (2 * (N : K))) (((2 * j.val : ℕ) : K) / (2 * (N : K))) +
       K_ker (((2 * i.val : ℕ) : K) / (2 * (N : K))) (((2 * j.val + 1 : ℕ) : K) / (2 * (N : K))) +
       K_ker (((2 * i.val + 1 : ℕ) : K) / (2 * (N : K))) (((2 * j.val + 1 : ℕ) : K) / (2 * (N : K))))
  have hdiff : discretePairSum K_ker N - discretePairSum K_ker (2 * N) =
      (1 / (4 * (N : K) ^ 2)) * ∑ i : Fin N, ∑ j : Fin N, cellErr i j := by
    rw [hSN, hS2N, ← mul_sub, ← Finset.sum_sub_distrib]
    congr 1
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [← Finset.sum_sub_distrib]
  have hinv_pos : (0 : K) < 1 / (4 * (N : K) ^ 2) := one_div_pos.mpr h4N2_pos
  rw [hdiff, abs_mul, abs_of_pos hinv_pos]
  have hsum_le :
      |∑ i : Fin N, ∑ j : Fin N, cellErr i j| ≤ (N : K) ^ 2 * (2 * L / (N : K)) := by
    calc
      |∑ i : Fin N, ∑ j : Fin N, cellErr i j|
        ≤ ∑ i : Fin N, |∑ j : Fin N, cellErr i j| := Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ i : Fin N, ∑ j : Fin N, |cellErr i j| :=
          Finset.sum_le_sum fun i _ => Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ _i : Fin N, ∑ _j : Fin N, (2 * L / (N : K)) :=
          Finset.sum_le_sum fun i _ => Finset.sum_le_sum fun j _ => hblock i j
      _ = (N : K) ^ 2 * (2 * L / (N : K)) := by
          simp [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
          ring
  calc
    (1 / (4 * (N : K) ^ 2)) * |∑ i : Fin N, ∑ j : Fin N, cellErr i j|
      ≤ (1 / (4 * (N : K) ^ 2)) * ((N : K) ^ 2 * (2 * L / (N : K))) :=
        mul_le_mul_of_nonneg_left hsum_le (le_of_lt hinv_pos)
    _ = L / (2 * (N : K)) := by field_simp; ring

/-- **Concrete Unconditional Dyadic Cauchy Bound for `regPairKernel`:**
For every `0 < δ` and `0 < N`,
`|S_N(K_δ) - S_{2N}(K_δ)| ≤ 1 / (2 * δ³ * N)` with zero unverified hypotheses. -/
theorem regPairKernel_dyadic_step_bound {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] {δ : K} (hδ : 0 < δ) {N : ℕ} (hN : 0 < N) :
    |discretePairSum (regPairKernel δ) N - discretePairSum (regPairKernel δ) (2 * N)| ≤
      1 / (2 * δ ^ 3 * (N : K)) := by
  have hδ3 : 0 < δ ^ 3 := pow_pos hδ 3
  have h := subdivision_dyadic_step_bound (regPairKernel δ) (regPairKernel_lipschitz hδ) hN
  have heq : (1 / δ ^ 3) / (2 * (N : K)) = 1 / (2 * δ ^ 3 * (N : K)) := by
    have hN_ne : (N : K) ≠ 0 := ne_of_gt (Nat.cast_pos.mpr hN)
    have hδ3_ne : δ ^ 3 ≠ 0 := ne_of_gt hδ3
    field_simp
  rwa [heq] at h

end ContinuumSubdivision

/-! ## Part II. `S_3` / `H_3(q²)` Wedderburn Decomposition, Schur Duality & Proton `(k = -3, 2, 12)` -/

section S3WedderburnAndSchur

/-- The three partitions `(3)`, `(2,1)`, `(1³)` of `3` indexing the Wedderburn blocks of `H_3(q)`. -/
inductive Partition3 : Type
  | sym3
  | std21
  | sign111
  deriving DecidableEq, Repr

instance : Fintype Partition3 where
  elems := {.sym3, .std21, .sign111}
  complete x := by cases x <;> simp

/-- Classical Specht module dimension `d_λ` on `S_3`: `(1, 2, 1)`. -/
def spechtDim3 : Partition3 → ℕ
  | .sym3    => 1
  | .std21   => 2
  | .sign111 => 1

/-- Partition transpose / conjugation `λ ↦ λ*`: swaps `(3) ↔ (1³)` and fixes `(2,1)`. -/
def conjPart3 : Partition3 → Partition3
  | .sym3    => .sign111
  | .std21   => .std21
  | .sign111 => .sym3

theorem conjPart3_involutive (p : Partition3) : conjPart3 (conjPart3 p) = p := by
  cases p <;> rfl

/-- `(2,1)` is the **unique** self-conjugate partition of `3`, with Specht dimension `2`. -/
theorem conjPart3_fixed_iff (p : Partition3) :
    conjPart3 p = p ↔ p = .std21 := by
  cases p <;> decide

/-- Wedderburn dimension identity on `H_3`: `d_{(3)}² + d_{(2,1)}² + d_{(1³)}² = 6 = |S_3|`. -/
theorem wedderburn_dim_H3 :
    (∑ p : Partition3, (spechtDim3 p) ^ 2) = 6 := by
  decide

/-- **Regular-representation Wedderburn block decomposition of `E_cat`:**
Over any commutative ring `R`, weighting per-irrep functionals `E : Partition3 → R` by Specht
multiplicities `d_p` yields `E_{(3)} + 2 * E_{(2,1)} + E_{(1³)}`. -/
theorem ecat_regular_block_decomposition {R : Type*} [CommRing R] (E : Partition3 → R) :
    (∑ p : Partition3, (spechtDim3 p : R) * E p) =
      E .sym3 + 2 * E .std21 + E .sign111 := by
  have h : (Finset.univ : Finset Partition3) = {.sym3, .std21, .sign111} := rfl
  rw [h]
  simp [spechtDim3]
  ring

/-- Schur elements `c_p(Q)` of `H_3(Q)` (`(T_i - Q)(T_i + 1) = 0`, Geck–Pfeiffer §10.5) over any
field `K`:
`c_{(3)}(Q) = (1 + Q)(1 + Q + Q²)`, `c_{(2,1)}(Q) = (1 + Q + Q²) / Q`,
`c_{(1³)}(Q) = (1 + Q)(1 + Q + Q²) / Q³`. -/
def schurH3 {K : Type*} [Field K] (Q : K) : Partition3 → K
  | .sym3    => (1 + Q) * (1 + Q + Q ^ 2)
  | .std21   => (1 + Q + Q ^ 2) / Q
  | .sign111 => (1 + Q) * (1 + Q + Q ^ 2) / Q ^ 3

/-- **Schur conjugate-transpose duality on `H_3(Q)`:**
Inverting `Q ↦ Q⁻¹` exchanges `(3)` with `(1³)` and leaves `(2,1)` strictly invariant:
`schurH3 Q⁻¹ p = schurH3 Q (conjPart3 p)`. -/
theorem schurH3_conj_duality {K : Type*} [Field K] {Q : K} (hQ : Q ≠ 0) (p : Partition3) :
    schurH3 Q⁻¹ p = schurH3 Q (conjPart3 p) := by
  cases p <;> simp only [schurH3, conjPart3] <;> field_simp <;> ring

/-- **Molien / symmetrizing-trace unit identity on `H_3(Q)`:**
`1 / c_{(3)}(Q) + 2 / c_{(2,1)}(Q) + 1 / c_{(1³)}(Q) = 1` whenever `1 + Q ≠ 0` and
`1 + Q + Q² ≠ 0`. -/
theorem schurH3_molien_sum_eq_one {K : Type*} [Field K] {Q : K}
    (hQ1 : 1 + Q ≠ 0) (hQ2 : 1 + Q + Q ^ 2 ≠ 0) :
    (∑ p : Partition3, (spechtDim3 p : K) / schurH3 Q p) = 1 := by
  have h : (Finset.univ : Finset Partition3) = {.sym3, .std21, .sign111} := rfl
  rw [h]
  simp only [Finset.sum_insert (by decide : Partition3.sym3 ∉ ({.std21, .sign111} : Finset Partition3)),
    Finset.sum_insert (by decide : Partition3.std21 ∉ ({.sign111} : Finset Partition3)),
    Finset.sum_singleton, spechtDim3, schurH3, Nat.cast_one, Nat.cast_ofNat]
  field_simp
  ring

/-- **Uniqueness of the `(2,1)` multiplicity `k₂ = 2` in the Molien sum:**
For `Q ≠ 0` and `1 + Q ≠ 0`, `1 / c_{(3)}(Q) + m / c_{(2,1)}(Q) + 1 / c_{(1³)}(Q) = 1`
holds if and only if `m = 2`. -/
theorem schurH3_std21_mult_unique {K : Type*} [Field K] {Q : K}
    (hQ0 : Q ≠ 0) (hQ1 : 1 + Q ≠ 0) (hQ2 : 1 + Q + Q ^ 2 ≠ 0) (m : K) :
    1 / schurH3 Q .sym3 + m / schurH3 Q .std21 + 1 / schurH3 Q .sign111 = 1 ↔ m = 2 := by
  simp only [schurH3]
  constructor
  · intro hm
    have hclear : 1 + m * Q * (1 + Q) + Q ^ 3 = (1 + Q) * (1 + Q + Q ^ 2) := by
      have hsub := sub_eq_zero.mpr hm
      field_simp at hsub
      linear_combination hsub
    have hfac : (m - 2) * (Q * (1 + Q)) = 0 := by
      linear_combination hclear
    have hQprod : Q * (1 + Q) ≠ 0 := mul_ne_zero hQ0 hQ1
    exact sub_eq_zero.mp ((mul_eq_zero.mp hfac).resolve_right hQprod)
  · rintro rfl
    field_simp
    ring

/-- Balanced quantum factorial `[3]_q! = (q² + 1 + q⁻²) * (q + q⁻¹)`. -/
def qFact3Balanced {K : Type*} [Field K] (q : K) : K :=
  (q ^ 2 + 1 + q⁻¹ ^ 2) * (q + q⁻¹)

/-- **Balanced-variable forms of all three `H_3(q²)` Schur elements:**
`c_{(3)}(q²) = q³ [3]_q!`, `c_{(2,1)}(q²) = q² + 1 + q⁻² = [3]_q`, and
`c_{(1³)}(q²) = [3]_q! / q³` (identifying `k₁ = -3` in `F_Bor` with the sign Schur element). -/
theorem schurH3_balanced_forms {K : Type*} [Field K] {q : K} (hq : q ≠ 0) :
    schurH3 (q ^ 2) .sym3 = q ^ 3 * qFact3Balanced q ∧
    schurH3 (q ^ 2) .std21 = q ^ 2 + 1 + q⁻¹ ^ 2 ∧
    schurH3 (q ^ 2) .sign111 = qFact3Balanced q / q ^ 3 := by
  refine ⟨?_, ?_, ?_⟩ <;> simp only [schurH3, qFact3Balanced] <;> field_simp <;> ring

/-- **Uniqueness of `k₁ = -3` as the sign-block Schur exponent:**
Over any strict ordered field `K`, for `0 < q` with `q ≠ 1` and any integer `k : ℤ`,
`q ^ k * [3]_q! = c_{(1³)}(q²) ↔ k = -3`. -/
theorem proton_k_minus3_sign_schur_iff {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] {q : K} (hq_pos : 0 < q) (hq1 : q ≠ 1) (k : ℤ) :
    q ^ k * qFact3Balanced q = schurH3 (q ^ 2) .sign111 ↔ k = -3 := by
  have hq_ne : q ≠ 0 := ne_of_gt hq_pos
  have hqf_pos : 0 < qFact3Balanced q := by
    unfold qFact3Balanced
    have hqi : 0 < q⁻¹ := inv_pos.mpr hq_pos
    positivity
  have hqf_ne : qFact3Balanced q ≠ 0 := ne_of_gt hqf_pos
  rw [(schurH3_balanced_forms hq_ne).2.2]
  have hrhs : qFact3Balanced q / q ^ 3 = q ^ (-3 : ℤ) * qFact3Balanced q := by
    rw [show (-3 : ℤ) = -((3 : ℕ) : ℤ) by rfl, zpow_neg, zpow_natCast]
    ring
  rw [hrhs, mul_left_inj' hqf_ne]
  exact (zpow_right_injective₀ hq_pos hq1).eq_iff

/-- **Classical `Q = 1` Schur values and `2 · 6 = 12` connection to `ProtonBorromeanAssembly`:**
At `Q = 1`, `c_{(3)}(1) = c_{(1³)}(1) = 6 = |S_3|`, `c_{(2,1)}(1) = 3`, and
`dim S^{(2,1)} · c_{(1³)}(1) = 2 · 6 = 12`, matching the conditional assembly parameters of
`QOU.AppendixQValues.ProtonBorromeanAssembly`. -/
theorem proton_structural_integers_12 {K : Type*} [Field K]
    [A : QOU.AppendixQValues.ProtonBorromeanAssembly K] :
    schurH3 (1 : K) .sym3 = 6 ∧
    schurH3 (1 : K) .std21 = 3 ∧
    schurH3 (1 : K) .sign111 = 6 ∧
    (spechtDim3 .std21 : K) * schurH3 (1 : K) .sign111 = 12 ∧
    A.protonMass =
      (spechtDim3 .std21 : K) * A.mMu * A.fBor -
        ((spechtDim3 .std21 : K) * schurH3 (1 : K) .sign111) * A.mE := by
  have hc3 : schurH3 (1 : K) .sym3 = 6 := by simp [schurH3]; ring
  have hc21 : schurH3 (1 : K) .std21 = 3 := by simp [schurH3]; norm_num
  have hc111 : schurH3 (1 : K) .sign111 = 6 := by simp [schurH3]; norm_num
  have h12 : (spechtDim3 .std21 : K) * schurH3 (1 : K) .sign111 = 12 := by
    rw [hc111]; simp [spechtDim3]; norm_num
  refine ⟨hc3, hc21, hc111, h12, ?_⟩
  rw [QOU.AppendixQValues.proton_mass_substrate_identity K, h12]
  simp [spechtDim3]

end S3WedderburnAndSchur

/-! ## Part III. Intra-Nucleon Borromean EM Self-Energy & Scheme-Comparable `m_d - m_u`
(`qou-37y0`, `qou-17mq`, `qou-zp6a`, `qou-awxv` Gate G-II) -/

section IntraNucleonBorromeanEM

/-- Constituent quark charges of the proton `p = (u, u, d) = (2/3, 2/3, -1/3)`. -/
def protonCharges (K : Type*) [Field K] : Fin 3 → K
  | 0 => 2 / 3
  | 1 => 2 / 3
  | 2 => -1 / 3

/-- Constituent quark charges of the neutron `n = (d, d, u) = (-1/3, -1/3, 2/3)`. -/
def neutronCharges (K : Type*) [Field K] : Fin 3 → K
  | 0 => -1 / 3
  | 1 => -1 / 3
  | 2 => 2 / 3

/-- Unordered pairwise charge-product sum `Q₀ Q₁ + Q₀ Q₂ + Q₁ Q₂`. -/
def pairChargeSum {R : Type*} [CommRing R] (Q : Fin 3 → R) : R :=
  Q 0 * Q 1 + Q 0 * Q 2 + Q 1 * Q 2

/-- Sum of squared constituent charges `Q₀² + Q₁² + Q₂²`. -/
def selfChargeSum {R : Type*} [CommRing R] (Q : Fin 3 → R) : R :=
  ∑ i : Fin 3, (Q i) ^ 2

/-- **Three-body charge-square decomposition:**
`(Q₀ + Q₁ + Q₂)² = (Q₀² + Q₁² + Q₂²) + 2 * (Q₀ Q₁ + Q₀ Q₂ + Q₁ Q₂)`. -/
theorem charge_sq_sum_rule {R : Type*} [CommRing R] (Q : Fin 3 → R) :
    (∑ i : Fin 3, Q i) ^ 2 = selfChargeSum Q + 2 * pairChargeSum Q := by
  unfold selfChargeSum pairChargeSum
  simp [Fin.sum_univ_three]
  ring

/-- **Proton pairwise quark-charge sum vanishes identically (`4/9 - 2/9 - 2/9 = 0`):** -/
theorem proton_pair_charge_sum_eq_zero (K : Type*) [Field K] [CharZero K] :
    pairChargeSum (protonCharges K) = 0 := by
  unfold pairChargeSum protonCharges
  norm_num

/-- **Neutron pairwise quark-charge sum equals `-1/3` (`1/9 - 2/9 - 2/9 = -1/3`):** -/
theorem neutron_pair_charge_sum_eq_neg_third (K : Type*) [Field K] [CharZero K] :
    pairChargeSum (neutronCharges K) = -1 / 3 := by
  unfold pairChargeSum neutronCharges
  norm_num

/-- **Proton-minus-neutron pairwise charge-product difference equals `+1/3`:** -/
theorem pn_pair_charge_diff_eq_third (K : Type*) [Field K] [CharZero K] :
    pairChargeSum (protonCharges K) - pairChargeSum (neutronCharges K) = 1 / 3 := by
  rw [proton_pair_charge_sum_eq_zero, neutron_pair_charge_sum_eq_neg_third]
  norm_num

/-- **Proton-minus-neutron constituent self-charge-square difference equals `+1/3`:**
`∑_i Q_i²(p) = 1`, `∑_i Q_i²(n) = 2/3`, and `∑_i Q_i²(p) - ∑_i Q_i²(n) = 1/3`. -/
theorem pn_self_charge_diff_eq_third (K : Type*) [Field K] [CharZero K] :
    selfChargeSum (protonCharges K) = 1 ∧
    selfChargeSum (neutronCharges K) = 2 / 3 ∧
    selfChargeSum (protonCharges K) - selfChargeSum (neutronCharges K) = 1 / 3 := by
  unfold selfChargeSum protonCharges neutronCharges
  simp only [Fin.sum_univ_three]
  refine ⟨by norm_num, by norm_num, by norm_num⟩

/-- **Gate G-II Linear-Milnor Odd-Parity Obstruction (`sm-gating-objects.md` §2):**
If a functional `F : K → K` of the Milnor triple linking number `μ` is odd (`F (-μ) = -F μ`)
and invariant under exchanging the two identical quarks (`F (-μ) = F μ`), then `F μ = 0`. -/
theorem odd_milnor_functional_vanishes {K : Type*} [Field K] [CharZero K]
    (F : K → K) (hodd : ∀ μ : K, F (-μ) = -F μ) {μ : K} (hexch : F (-μ) = F μ) :
    F μ = 0 := by
  have h2 : (2 : K) * F μ = 0 := by
    have h := hodd μ
    linear_combination h - hexch
  have h2ne : (2 : K) ≠ 0 := by norm_num
  exact (mul_eq_zero.mp h2).resolve_left h2ne

/-- Pairwise linking numbers `(lk12, lk13, lk23)` and Milnor triple linking invariant `mu123`
of an oriented 3-component link. -/
structure Link3TripleData (R : Type*) where
  lk12 : R
  lk13 : R
  lk23 : R
  mu123 : R

/-- Exchanging strands `1 ↔ 2` swaps `lk13 ↔ lk23` and reverses the sign of `mu123`. -/
def swapStrands12 {R : Type*} [Neg R] (L : Link3TripleData R) : Link3TripleData R :=
  { lk12 := L.lk12, lk13 := L.lk23, lk23 := L.lk13, mu123 := -L.mu123 }

/-- The 3-component unlink (`lk_ij = 0`, `μ̄_{123} = 0`). -/
def unlink3 (R : Type*) [Zero R] : Link3TripleData R :=
  ⟨0, 0, 0, 0⟩

/-- Positive-chirality Borromean link `B_3^+` (`lk_ij = 0`, `μ̄_{123} = +1`). -/
def borromeanPos (R : Type*) [Zero R] [One R] : Link3TripleData R :=
  ⟨0, 0, 0, 1⟩

/-- Negative-chirality Borromean link `B_3^-` (`lk_ij = 0`, `μ̄_{123} = -1`). -/
def borromeanNeg (R : Type*) [Zero R] [One R] [Neg R] : Link3TripleData R :=
  ⟨0, 0, 0, -1⟩

/-- Even quadratic Milnor invariant `μ̄_{123}²`. -/
def evenMilnorSq {R : Type*} [CommRing R] (L : Link3TripleData R) : R :=
  L.mu123 ^ 2

/-- **Even Milnor `μ̄_{123}²` resolves Gate G-II's parity & unlink obstructions:**
1. Every functional `G` of pairwise linking alone agrees on `B_3^+`, `B_3^-`, and `unlink3`;
2. `evenMilnorSq` is strictly invariant under `1 ↔ 2` strand exchange (`(-μ)² = μ²`);
3. `evenMilnorSq` equals `0` on `unlink3` and `+1` on both `B_3^+` and `B_3^-` (`1 ≠ 0`). -/
theorem even_milnor_sq_distinguishes_borromean_from_unlink {R : Type*} [CommRing R] [Nontrivial R] :
    (∀ G : R → R → R → R,
      G (borromeanPos R).lk12 (borromeanPos R).lk13 (borromeanPos R).lk23 =
        G (unlink3 R).lk12 (unlink3 R).lk13 (unlink3 R).lk23 ∧
      G (borromeanNeg R).lk12 (borromeanNeg R).lk13 (borromeanNeg R).lk23 =
        G (unlink3 R).lk12 (unlink3 R).lk13 (unlink3 R).lk23) ∧
    (∀ L : Link3TripleData R, evenMilnorSq (swapStrands12 L) = evenMilnorSq L) ∧
    evenMilnorSq (unlink3 R) = 0 ∧
    evenMilnorSq (borromeanPos R) = 1 ∧
    evenMilnorSq (borromeanNeg R) = 1 ∧
    evenMilnorSq (borromeanPos R) ≠ evenMilnorSq (unlink3 R) := by
  refine ⟨fun G => ⟨rfl, rfl⟩, fun L => ?_, ?_, ?_, ?_, ?_⟩
  · unfold evenMilnorSq swapStrands12; ring
  · unfold evenMilnorSq unlink3; ring
  · unfold evenMilnorSq borromeanPos; ring
  · unfold evenMilnorSq borromeanNeg; ring
  · unfold evenMilnorSq borromeanPos unlink3
    simp only [one_pow, zero_pow (by decide : 2 ≠ 0), ne_eq]
    exact one_ne_zero

/-- Intra-nucleon Borromean electromagnetic self-energy with symmetric `μ̄_{123}²`-weighted
pairwise spatial kernel `μ² * K₀` and 1-body constituent self-energy scale `K_self`:
`E_EM(Q; μ, K₀, K_self) = (1/2) (∑_i Q_i²) K_self + μ² K₀ (∑_{i<j} Q_i Q_j)`. -/
def intraNucleonEM {K : Type*} [Field K] (Q : Fin 3 → K) (μ K₀ K_self : K) : K :=
  (1 / 2) * selfChargeSum Q * K_self + μ ^ 2 * K₀ * pairChargeSum Q

/-- **Exact `p - n` intra-nucleon EM splitting formula:**
`E_EM(p) - E_EM(n) = (1/6) K_self + (1/3) μ² K₀`. -/
theorem intraNucleonEM_pn_diff {K : Type*} [Field K] [CharZero K] (μ K₀ K_self : K) :
    intraNucleonEM (protonCharges K) μ K₀ K_self -
      intraNucleonEM (neutronCharges K) μ K₀ K_self =
      (1 / 6) * K_self + (1 / 3) * μ ^ 2 * K₀ := by
  unfold intraNucleonEM
  have hpair := pn_pair_charge_diff_eq_third K
  have hself := (pn_self_charge_diff_eq_third K).2.2
  linear_combination (1 / 2) * K_self * hself + μ ^ 2 * K₀ * hpair

/-- **Pure-pairwise Borromean EM self-energies (`K_self = 0`, `μ² = 1`):**
On `B_3^±`, `E_EM(p) = 0`, `E_EM(n) = -(1/3) K₀`, and `ΔE_EM(p - n) = +(1/3) K₀`. -/
theorem intraNucleonEM_borromean_pure_pair {K : Type*} [Field K] [CharZero K]
    {μ : K} (hμ : μ ^ 2 = 1) (K₀ : K) :
    intraNucleonEM (protonCharges K) μ K₀ 0 = 0 ∧
    intraNucleonEM (neutronCharges K) μ K₀ 0 = -(1 / 3) * K₀ ∧
    intraNucleonEM (protonCharges K) μ K₀ 0 -
      intraNucleonEM (neutronCharges K) μ K₀ 0 = (1 / 3) * K₀ := by
  refine ⟨?_, ?_, ?_⟩
  · unfold intraNucleonEM
    rw [proton_pair_charge_sum_eq_zero, hμ]
    ring
  · unfold intraNucleonEM
    rw [neutron_pair_charge_sum_eq_neg_third, hμ]
    ring
  · rw [intraNucleonEM_pn_diff, hμ]
    ring

/-- **Scheme-Comparable `m_d - m_u` Decomposition (`qou-37y0`, Gate G-II):**
Over any strict ordered field `K`, on `B_3^±` (`μ² = 1`) with repulsive pairwise scale `0 < K₀`
and `0 ≤ K_self`, subtracting the intra-nucleon EM shift (`Δm_np = (m_d - m_u)_scheme - ΔE_EM(p-n)`)
yields
`(m_d - m_u)_scheme = Δm_np + (1/6) K_self + (1/3) K₀ > Δm_np`,
explaining structurally why current-quark `m_d - m_u` exceeds `m_n - m_p`. -/
theorem strong_md_sub_mu_decomposition {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] (deltaM_np_tot : K) {μ K₀ K_self : K}
    (hμ : μ ^ 2 = 1) (hK₀ : 0 < K₀) (hK_self : 0 ≤ K_self) :
    let deltaE_EM_pn :=
      intraNucleonEM (protonCharges K) μ K₀ K_self -
        intraNucleonEM (neutronCharges K) μ K₀ K_self
    let md_sub_mu_scheme := deltaM_np_tot + deltaE_EM_pn
    md_sub_mu_scheme = deltaM_np_tot + (1 / 6) * K_self + (1 / 3) * K₀ ∧
    deltaM_np_tot < md_sub_mu_scheme := by
  dsimp only
  rw [intraNucleonEM_pn_diff, hμ]
  refine ⟨by ring, ?_⟩
  linarith

/-- **Charge-Unit `L_cal` Route-1 Self-Consistent Positivity (`qou-awxv` item 1):**
Under `Δ_EM(p - n) = α * m_model * f` (equivalently pure-pairwise `K₀ = 3 * α * m_model * f`,
`K_self = 0` on `μ² = 1`), any positive coupling `0 < α`, positive self-consistent nucleon mass
`0 < m_model`, and positive dimensionless Borromean shape factor `0 < f` give
`Δ_EM(p - n) > 0` and `(m_d - m_u)_scheme = Δm_np + α * m_model * f > Δm_np`. -/
theorem route1_self_consistent_em_pos {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] (deltaM_np_tot : K) {μ α m_model f : K}
    (hμ : μ ^ 2 = 1) (hα : 0 < α) (hm : 0 < m_model) (hf : 0 < f) :
    let deltaE := intraNucleonEM (protonCharges K) μ (3 * α * m_model * f) 0 -
      intraNucleonEM (neutronCharges K) μ (3 * α * m_model * f) 0
    deltaE = α * m_model * f ∧ 0 < deltaE ∧ deltaM_np_tot < deltaM_np_tot + deltaE := by
  dsimp only
  have hpos : 0 < α * m_model * f := mul_pos (mul_pos hα hm) hf
  rw [(intraNucleonEM_borromean_pure_pair hμ (3 * α * m_model * f)).2.2]
  have hsimp : (1 / 3 : K) * (3 * α * m_model * f) = α * m_model * f := by ring
  rw [hsimp]
  exact ⟨rfl, hpos, by linarith⟩

/-- **Single-Nucleon Intra-Baryon EM Cancels Identically in Nuclear Binding (`sm-gating-objects.md` §2):**
Over any commutative ring `R`, if free nucleon masses split as `m_p = m_p0 + e_p` and
`m_n = m_n0 + e_n` and a nucleus `(Z, N)` has mass
`M(Z, N) = Z * (m_p0 + e_p) + N * (m_n0 + e_n) - B_inter`, then the nuclear binding energy
`Z * m_p + N * m_n - M(Z, N)` equals `B_inter` independently of `e_p` and `e_n`. -/
theorem intranucleon_em_cancels_in_nuclear_binding {R : Type*} [CommRing R]
    (Z N m_p0 m_n0 e_p e_n B_inter : R) :
    Z * (m_p0 + e_p) + N * (m_n0 + e_n) -
      (Z * (m_p0 + e_p) + N * (m_n0 + e_n) - B_inter) = B_inter := by
  ring

/-- O2 zero-mean neutralized `H³` Green's kernel `(u + 1)/(u - 1) - c₀` (`u = e^{2α} > 1`). -/
def h3GreenO2 {K : Type*} [Field K] (u c₀ : K) : K :=
  (u + 1) / (u - 1) - c₀

/-- **O2 Neutralized `H³` Green's Kernel Positivity Window (`qou-17mq`, `qou-zp6a`):**
Over any strict ordered field `K`, for `1 < u`:
1. At the infinite-volume boundary `c₀ = 1` (decaying Green's function),
   `h3GreenO2 u 1 = 2 / (u - 1) > 0` for all `1 < u`;
2. For any finite-volume zero-mean Robin constant `1 < c₀` (such as `c₀(B_3) > 1`),
   `0 < h3GreenO2 u c₀ ↔ u < (c₀ + 1) / (c₀ - 1)` (repulsive at short intra-baryon separation
   and sign-changing across `u* = (c₀ + 1) / (c₀ - 1)` as zero-mean neutrality requires). -/
theorem o2_neutralized_h3_green_positivity_window {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] {u c₀ : K} (hu : 1 < u) (hc₀ : 1 < c₀) :
    (h3GreenO2 u 1 = 2 / (u - 1) ∧ 0 < h3GreenO2 u 1) ∧
    (0 < h3GreenO2 u c₀ ↔ u < (c₀ + 1) / (c₀ - 1)) := by
  have hu_pos : 0 < u - 1 := sub_pos.mpr hu
  have hu_ne : u - 1 ≠ 0 := ne_of_gt hu_pos
  have hc_pos : 0 < c₀ - 1 := sub_pos.mpr hc₀
  have hc_ne : c₀ - 1 ≠ 0 := ne_of_gt hc_pos
  have hdec : h3GreenO2 u 1 = 2 / (u - 1) := by
    unfold h3GreenO2; field_simp; ring
  refine ⟨⟨hdec, by rw [hdec]; exact div_pos two_pos hu_pos⟩, ?_⟩
  have hrew : h3GreenO2 u c₀ = ((c₀ + 1) - (c₀ - 1) * u) / (u - 1) := by
    unfold h3GreenO2; field_simp; ring
  rw [hrew, div_pos_iff_of_pos_right hu_pos]
  constructor
  · intro hnum
    rw [lt_div_iff₀' hc_pos]
    linarith
  · intro hlt
    rw [lt_div_iff₀' hc_pos] at hlt
    linarith

end IntraNucleonBorromeanEM

end QOU.QBeta.ContinuumECatIntraNucleonEM
