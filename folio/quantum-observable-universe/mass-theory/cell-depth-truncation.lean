import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic

/-!
# Block-depth truncation of a trace, and the failure of the `Φ_q` stabilisation

Standalone companion to `conj:phi-q-categorical-truncation`
(output of the `phi-q-truncation` demotion review).

Abstract setting. `ι` is the (finite) set of blocks of a split semisimple
algebra (for `H_n(K, q)` at generic `q`: the partitions `λ ⊢ n`); `c λ ∈ R` is the
block coefficient of an element `x` under a trace, `c λ = τ(e_λ x) = y_λ χ_λ(x)`;
`d : ι → ℕ` is a depth function on blocks (in the paper: Lusztig's `a`-function of the
two-sided Kazhdan–Lusztig cell). Nothing here depends on which `d` is chosen; that is
the point of the first half: the vanishing / stabilisation statement is a property of
*any* block-indexed depth, and its only input is the definition of the support.

Second half: the claim's other equality, `Σ_{k ≤ K} α_k m^(k)|_i = Φ_q^{[≤K]}(z_i)` for
every `K`, is incompatible with stabilisation whenever `z_i ≠ 0`, because the
truncated products `Φ_q^{[≤K]}` strictly change with `K`.
-/

namespace QOU.MassCore.CellDepthTruncation

open Finset

section Vanishing

variable {ι R : Type*} [Fintype ι] [CommRing R] [DecidableEq R]

/-- Support of the block-coefficient vector: the blocks where `τ(e_λ x) ≠ 0`. -/
def supp (c : ι → R) : Finset ι := univ.filter (fun l => c l ≠ 0)

/-- `k⋆(x)`: the maximal depth over the support (`0` if the support is empty). -/
def kstar (d : ι → ℕ) (c : ι → R) : ℕ := (supp c).sup d

/-- The depth-`k` stratum `m^(k)(x) = τ(E_k x) = Σ_{d λ = k} τ(e_λ x)`. -/
def stratum (d : ι → ℕ) (c : ι → R) (k : ℕ) : R :=
  ∑ l ∈ univ.filter (fun l => d l = k), c l

lemma le_kstar (d : ι → ℕ) (c : ι → R) {l : ι} (hl : c l ≠ 0) : d l ≤ kstar d c :=
  le_sup (f := d) (by simp [supp, hl])

/-- **Vanishing lemma.** Every stratum strictly above `k⋆` is zero. -/
theorem stratum_eq_zero_of_gt (d : ι → ℕ) (c : ι → R) {k : ℕ} (hk : kstar d c < k) :
    stratum d c k = 0 := by
  apply sum_eq_zero
  intro l hl
  simp only [mem_filter, mem_univ, true_and] at hl
  by_contra h
  have := le_kstar d c h
  omega

/-- **Stabilisation.** For arbitrary weights `α_k`, the weighted tower truncated at any
`K ≥ k⋆` equals the tower truncated at `k⋆`. -/
theorem tower_stable (α : ℕ → R) (d : ι → ℕ) (c : ι → R) {K : ℕ} (hK : kstar d c ≤ K) :
    ∑ k ∈ range (K + 1), α k * stratum d c k
      = ∑ k ∈ range (kstar d c + 1), α k * stratum d c k := by
  have hsub : range (kstar d c + 1) ⊆ range (K + 1) := by
    intro j hj; simp only [mem_range] at *; omega
  rw [← sum_sdiff hsub]
  have htail : ∀ j ∈ range (K + 1) \ range (kstar d c + 1), α j * stratum d c j = 0 := by
    intro j hj
    simp only [mem_sdiff, mem_range] at hj
    rw [stratum_eq_zero_of_gt d c (by omega), mul_zero]
  rw [sum_eq_zero htail, zero_add]

/-- **Reconstruction.** With unit weights the truncated tower is the whole trace
`τ(x) = Σ_λ τ(e_λ x)` (since `Σ_λ e_λ = 1`). -/
theorem tower_total (d : ι → ℕ) (c : ι → R) :
    ∑ k ∈ range (kstar d c + 1), stratum d c k = ∑ l, c l := by
  classical
  have h1 : ∑ l, c l = ∑ l ∈ univ.filter (fun l => d l ≤ kstar d c), c l := by
    rw [sum_filter]
    apply sum_congr rfl
    intro l _
    split_ifs with h
    · rfl
    · by_contra hc
      exact h (le_kstar d c hc)
  rw [h1, ← sum_fiberwise_of_maps_to (g := d) (t := range (kstar d c + 1))]
  · apply sum_congr rfl
    intro k hk
    simp only [mem_range] at hk
    unfold stratum
    rw [filter_filter]
    apply sum_congr _ (fun _ _ => rfl)
    ext l
    simp only [mem_filter, mem_univ, true_and]
    constructor
    · intro h; exact ⟨by omega, h⟩
    · intro h; exact h.2
  · intro l hl
    simp only [mem_filter, mem_univ, true_and] at hl
    simp only [mem_range]; omega

/-- **Vacuity.** If some block of maximal depth lies in the support, `k⋆` is the global
maximum, so the truncation removes nothing. For `H_n(q)` and `x = T_w` (or any braid
image) this applies: the index and sign characters `q^{ℓ(w)}`, `(-q⁻¹)^{ℓ(w)}` never
vanish, and both the `a`-function and `gbDepth` attain their maximum on one of them. -/
theorem kstar_eq_of_max_in_supp (d : ι → ℕ) (c : ι → R) {l₀ : ι} (h₀ : c l₀ ≠ 0)
    (hmax : ∀ l, d l ≤ d l₀) : kstar d c = d l₀ :=
  le_antisymm (Finset.sup_le fun l _ => hmax l) (le_kstar d c h₀)

end Vanishing

section PhiQ

variable {F : Type*} [Field F]

/-- `Φ_q^{[≤K]}(z) = ∏_{j=1}^{K} (1 - q^{-j} z)^{-1}`. -/
def phiTrunc (q z : F) (K : ℕ) : F := ∏ j ∈ range K, (1 - (q ^ (j + 1))⁻¹ * z)⁻¹

lemma phiTrunc_succ (q z : F) (K : ℕ) :
    phiTrunc q z (K + 1) = phiTrunc q z K * (1 - (q ^ (K + 1))⁻¹ * z)⁻¹ := by
  unfold phiTrunc; rw [prod_range_succ]

lemma phiTrunc_ne_zero (q z : F) (h : ∀ j : ℕ, 1 - (q ^ (j + 1))⁻¹ * z ≠ 0) (K : ℕ) :
    phiTrunc q z K ≠ 0 := by
  unfold phiTrunc
  exact prod_ne_zero_iff.mpr fun j _ => inv_ne_zero (h j)

/-- **The `Φ_q` side does not stabilise.** For `q ≠ 0`, `z ≠ 0` and no pole hit,
`Φ_q^{[≤K+1]}(z) ≠ Φ_q^{[≤K]}(z)` for every `K`. -/
theorem phiTrunc_succ_ne (q z : F) (hq : q ≠ 0) (hz : z ≠ 0)
    (h : ∀ j : ℕ, 1 - (q ^ (j + 1))⁻¹ * z ≠ 0) (K : ℕ) :
    phiTrunc q z (K + 1) ≠ phiTrunc q z K := by
  intro hEq
  rw [phiTrunc_succ] at hEq
  have hP := phiTrunc_ne_zero q z h K
  have hu : (1 - (q ^ (K + 1))⁻¹ * z)⁻¹ = 1 := by
    have := mul_left_cancel₀ hP (hEq.trans (mul_one _).symm)
    exact this
  have hu' : 1 - (q ^ (K + 1))⁻¹ * z = 1 := by
    have := congrArg (·⁻¹) hu
    simpa using this
  have : (q ^ (K + 1))⁻¹ * z = 0 := by linear_combination -hu'
  rcases mul_eq_zero.mp this with h1 | h1
  · exact inv_ne_zero (pow_ne_zero _ hq) h1
  · exact hz h1

/-- **The conjunction in the original claim is inconsistent.** No sequence can both
(i) equal `Φ_q^{[≤K]}(z)` at every truncation level `K` and (ii) be constant from some
level `k⋆` on, when `q ≠ 0`, `z ≠ 0` and no pole is hit. -/
theorem no_stable_phi_tower (q z : F) (hq : q ≠ 0) (hz : z ≠ 0)
    (h : ∀ j : ℕ, 1 - (q ^ (j + 1))⁻¹ * z ≠ 0)
    (S : ℕ → F) (k₀ : ℕ) (hS : ∀ K, S K = phiTrunc q z K)
    (hstab : ∀ K, k₀ ≤ K → S K = S k₀) : False := by
  apply phiTrunc_succ_ne q z hq hz h k₀
  rw [← hS, ← hS, hstab (k₀ + 1) (by omega)]

/-- The hypotheses are satisfiable: `q = 2`, `z = 1` over `ℚ`. -/
theorem witness_hyp : ∀ j : ℕ, (1 : ℚ) - ((2 : ℚ) ^ (j + 1))⁻¹ * 1 ≠ 0 := by
  intro j hj
  have h2 : (1 : ℚ) < 2 ^ (j + 1) := one_lt_pow₀ (by norm_num) (by omega)
  have : ((2 : ℚ) ^ (j + 1))⁻¹ = 1 := by linear_combination -hj
  rw [inv_eq_one] at this
  linarith

end PhiQ

end QOU.MassCore.CellDepthTruncation

