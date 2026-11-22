import QOU.Mass.QuantumSl2ClaspDeltaF
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Trace

/-!
# `V_{m+1} ⊗ V_{m+1} = ⊕_n V_{2n+1}` and the quantum trace

The `F`-strings `Δ(F)^i w_j` (`0 ≤ j ≤ m`, `0 ≤ i ≤ 2(m−j)`) of the highest-weight vectors
form a basis of `V_{m+1} ⊗ V_{m+1}`, for generic `q`. On that basis an operator that is scalar,
`c_j`, on each string has quantum trace `tr(K X) = Σ_j c_j [2(m−j)+1]`. This is the
decomposition step of van der Veen's Lemma 1: the closure of a tangle that acts as
`⊕_n Tangle(n) · id_{V_{2n+1}}` is `Σ_n [2n+1] Tangle(n)`.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, proof of Lemma 1
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. VI–VII
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

/-! ### Strings below a highest-weight vector, in any representation -/

/-- The scalar in `E F^{k+1} w = strSc N k · F^k w` for `w` of weight `q^N`. -/
def strSc (q : 𝕜) (N k : ℕ) : 𝕜 :=
  qint q (k + 1) * ((q - q⁻¹)⁻¹ * (q⁻¹ ^ k * q ^ N - q ^ k * q⁻¹ ^ N))

namespace Rep

variable {q : 𝕜} {ι : Type*} [Fintype ι] [DecidableEq ι]

theorem Km_mulVec_of_Kp (hq : q ≠ 0) (ρ : Rep q ι) (w : ι → 𝕜) (N : ℕ)
    (hK : ρ.Kp *ᵥ w = q ^ N • w) : ρ.Km *ᵥ w = q⁻¹ ^ N • w := by
  have h : ρ.Km *ᵥ (ρ.Kp *ᵥ w) = w := by rw [mulVec_mulVec, ρ.Km_Kp, one_mulVec]
  rw [hK, mulVec_smul] at h
  calc ρ.Km *ᵥ w = q⁻¹ ^ N • (q ^ N • (ρ.Km *ᵥ w)) := by
        rw [smul_smul, ← mul_pow, inv_mul_cancel₀ hq, one_pow, one_smul]
    _ = q⁻¹ ^ N • w := by rw [h]

theorem Dk_mulVec_of_Kp (hq : q ≠ 0) (ρ : Rep q ι) (w : ι → 𝕜) (N k : ℕ)
    (hK : ρ.Kp *ᵥ w = q ^ N • w) :
    ρ.Dk k *ᵥ w = ((q - q⁻¹)⁻¹ * (q⁻¹ ^ k * q ^ N - q ^ k * q⁻¹ ^ N)) • w := by
  unfold Dk
  rw [smul_mulVec, sub_mulVec, smul_mulVec, smul_mulVec, hK,
    Km_mulVec_of_Kp hq ρ w N hK, smul_smul, smul_smul, ← sub_smul, smul_smul]

variable (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) (ρ : Rep q ι) (w : ι → 𝕜) (N : ℕ)
  (hE : ρ.E *ᵥ w = 0) (hK : ρ.Kp *ᵥ w = q ^ N • w)
include hq hq2 hE hK

theorem E_F_succ_hw (k : ℕ) :
    ρ.E *ᵥ (ρ.F ^ (k + 1) *ᵥ w) = strSc q N k • (ρ.F ^ k *ᵥ w) := by
  have h := ρ.E_F_pow hq hq2 k
  rw [sub_eq_iff_eq_add] at h
  rw [mulVec_mulVec, h, add_mulVec, ← mulVec_mulVec, hE, mulVec_zero, add_zero,
    smul_mulVec, ← mulVec_mulVec, Dk_mulVec_of_Kp hq ρ w N k hK, mulVec_smul, smul_smul]
  rfl

theorem E_pow_F_pow_hw_eq (b : ℕ) :
    ρ.E ^ b *ᵥ (ρ.F ^ b *ᵥ w) = (∏ k ∈ Finset.range b, strSc q N k) • w := by
  induction b with
  | zero => simp
  | succ b ih =>
    rw [pow_succ ρ.E, ← mulVec_mulVec, E_F_succ_hw hq hq2 ρ w N hE hK, mulVec_smul, ih,
      smul_smul, Finset.prod_range_succ, mul_comm]

theorem E_pow_F_pow_hw_lt (b a : ℕ) (hab : b < a) :
    ρ.E ^ a *ᵥ (ρ.F ^ b *ᵥ w) = 0 := by
  induction b generalizing a with
  | zero =>
    obtain ⟨a, rfl⟩ : ∃ a', a = a' + 1 := ⟨a - 1, by omega⟩
    rw [pow_succ, ← mulVec_mulVec, pow_zero, one_mulVec, hE, mulVec_zero]
  | succ b ih =>
    obtain ⟨a, rfl⟩ : ∃ a', a = a' + 1 := ⟨a - 1, by omega⟩
    rw [pow_succ ρ.E, ← mulVec_mulVec, E_F_succ_hw hq hq2 ρ w N hE hK, mulVec_smul,
      ih a (by omega), smul_zero]

theorem E_pow_F_pow_hw_le (a b : ℕ) (hab : a ≤ b) :
    ρ.E ^ a *ᵥ (ρ.F ^ b *ᵥ w)
      = (∏ k ∈ Finset.Ico (b - a) b, strSc q N k) • (ρ.F ^ (b - a) *ᵥ w) := by
  induction a generalizing b with
  | zero => simp
  | succ a ih =>
    obtain ⟨b, rfl⟩ : ∃ b', b = b' + 1 := ⟨b - 1, by omega⟩
    rw [pow_succ ρ.E, ← mulVec_mulVec, E_F_succ_hw hq hq2 ρ w N hE hK, mulVec_smul,
      ih b (by omega), smul_smul, show b + 1 - (a + 1) = b - a by omega,
      Finset.prod_Ico_succ_top (by omega), mul_comm]

omit hq hq2 hE in
theorem Kp_F_pow_hw (i : ℕ) :
    ρ.Kp *ᵥ (ρ.F ^ i *ᵥ w) = (q ^ N * (q⁻¹ ^ 2) ^ i) • (ρ.F ^ i *ᵥ w) := by
  rw [mulVec_mulVec, ρ.Kp_F_pow, smul_mulVec, ← mulVec_mulVec, hK, mulVec_smul, smul_smul,
    mul_comm]

end Rep

theorem strSc_eq (q : 𝕜) (hq : q ≠ 0) (N k : ℕ) (hk : k ≤ N) :
    strSc q N k = qint q (k + 1) * qint q (N - k) := by
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hk
  unfold strSc
  rw [Nat.add_sub_cancel_left]
  congr 1
  have h1 : q⁻¹ ^ k * q ^ (k + d) = q ^ d := by
    rw [pow_add, ← mul_assoc, ← mul_pow, inv_mul_cancel₀ hq, one_pow, one_mul]
  have h2 : q ^ k * q⁻¹ ^ (k + d) = q⁻¹ ^ d := by
    rw [pow_add, ← mul_assoc, ← mul_pow, mul_inv_cancel₀ hq, one_pow, one_mul]
  rw [h1, h2, qint, div_eq_mul_inv, mul_comm]

theorem prod_strSc_ne_zero (q : 𝕜) (hq : q ≠ 0) (N b : ℕ) (hb : b ≤ N)
    (hint : ∀ i, 0 < i → i ≤ N → qint q i ≠ 0) :
    ∏ k ∈ Finset.range b, strSc q N k ≠ 0 := by
  rw [Finset.prod_ne_zero_iff]
  intro k hk
  rw [Finset.mem_range] at hk
  rw [strSc_eq q hq N k (by omega)]
  exact mul_ne_zero (hint _ (by omega) (by omega)) (hint _ (by omega) (by omega))

/-! ### The tensor square `V_{m+1} ⊗ V_{m+1}` -/

section Tensor

variable (q : 𝕜) (hq : q ≠ 0) (m : ℕ)

/-- `V_{m+1} ⊗ V_{m+1}` as a representation. -/
abbrev tens : Rep q (Fin (m + 1) × Fin (m + 1)) := Rep.tensor hq (irrep hq m) (irrep hq m)

theorem tens_F : (tens q hq m).F = deltaF q m m := by
  show irrepF q m ⊗ₖ 1 + irrepKm q m ⊗ₖ irrepF q m = _
  unfold deltaF; exact add_comm _ _

theorem tens_E : (tens q hq m).E = irrepE q m ⊗ₖ irrepKp q m + 1 ⊗ₖ irrepE q m := rfl

theorem tens_Kp : (tens q hq m).Kp = deltaK q m m := rfl

include hq in
/-- **Weight of `w_j`:** `Δ(K) w_j = q^{2(m−j)} w_j`. -/
theorem deltaK_hwVec (j : ℕ) (hj : j ≤ m) :
    deltaK q m m *ᵥ hwVec q m m j = q ^ (2 * (m - j)) • hwVec q m m j := by
  funext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩
  simp only [deltaK, irrepKp, diagonal_kronecker_diagonal, mulVec_diagonal, Pi.smul_apply,
    smul_eq_mul]
  unfold hwVec
  dsimp only
  split_ifs with h
  · have e : (m - p) + (m - r) = 2 * (m - j) + (p + r) := by omega
    calc q ^ (m - p) * q⁻¹ ^ p * (q ^ (m - r) * q⁻¹ ^ r) * hwCoef q m m j p
        = (q ^ ((m - p) + (m - r)) * q⁻¹ ^ (p + r)) * hwCoef q m m j p := by ring
      _ = _ := by
        rw [e, h, pow_add, mul_assoc (q ^ (2 * (m - j))), ← mul_pow, mul_inv_cancel₀ hq,
          one_pow, mul_one]
  · simp

/-- A vector is supported in grade `g` if it vanishes off `p + r = g`. -/
def InGrade (g : ℕ) (u : Fin (m + 1) × Fin (m + 1) → 𝕜) : Prop :=
  ∀ x : Fin (m + 1) × Fin (m + 1), (x.1 : ℕ) + x.2 ≠ g → u x = 0

theorem inGrade_deltaF (g : ℕ) (u : Fin (m + 1) × Fin (m + 1) → 𝕜) (hu : InGrade m g u) :
    InGrade m (g + 1) (deltaF q m m *ᵥ u) := by
  rintro ⟨⟨p, hp⟩, ⟨r, hr⟩⟩ hx
  dsimp only at hx
  rw [dF_apply]
  split_ifs with h1 h2 h2
  · rw [hu _ (by dsimp only; omega), hu _ (by dsimp only; omega)]; simp
  · rw [hu _ (by dsimp only; omega)]; simp
  · rw [hu _ (by dsimp only; omega)]; simp
  · simp

theorem inGrade_strVec (j i : ℕ) : InGrade m (j + i) (deltaF q m m ^ i *ᵥ hwVec q m m j) := by
  induction i with
  | zero =>
    rintro x hx
    simp only [pow_zero, one_mulVec, hwVec]
    rw [if_neg (by omega)]
  | succ i ih =>
    rw [pow_succ', ← mulVec_mulVec]
    exact inGrade_deltaF q m _ _ ih

/-- Index of the string basis: `j ≤ m` and `i ≤ 2(m−j)`. -/
abbrev StrIdx (m : ℕ) := Σ j : Fin (m + 1), Fin (2 * (m - j) + 1)

/-- The string vectors `Δ(F)^i w_j`. -/
def strVec (x : StrIdx m) : Fin (m + 1) × Fin (m + 1) → 𝕜 :=
  deltaF q m m ^ (x.2 : ℕ) *ᵥ hwVec q m m x.1

theorem hwVec_top (j : Fin (m + 1)) :
    hwVec q m m j (⟨0, by omega⟩, j) = 1 := by
  simp [hwVec, hwCoef]

variable (hq2 : q - q⁻¹ ≠ 0)

include hq hq2 in
/-- **The string vectors are linearly independent** (generic `q`). -/
theorem strVec_linearIndependent (hint : ∀ i, 0 < i → i ≤ 2 * m → qint q i ≠ 0) :
    LinearIndependent 𝕜 (strVec q m) := by
  classical
  rw [Fintype.linearIndependent_iff]
  intro c hc
  by_contra hne
  push_neg at hne
  obtain ⟨x1, hx1⟩ := hne
  set S := Finset.univ.filter
    (fun x : StrIdx m => c x ≠ 0 ∧ (x.1 : ℕ) + x.2 = (x1.1 : ℕ) + x1.2) with hS
  have hSne : S.Nonempty := ⟨x1, by simp [hS, hx1]⟩
  obtain ⟨x0, hx0S, hmin⟩ := Finset.exists_min_image S (fun x => (x.1 : ℕ)) hSne
  have hx0 : c x0 ≠ 0 ∧ (x0.1 : ℕ) + x0.2 = (x1.1 : ℕ) + x1.2 := by
    simpa [hS] using hx0S
  set i0 : ℕ := (x0.2 : ℕ)
  set j0 : Fin (m + 1) := x0.1
  have hi0 : i0 ≤ 2 * (m - j0) := by have := x0.2.isLt; omega
  -- the representation facts for each `w_j`
  have hEw : ∀ j : Fin (m + 1), (tens q hq m).E *ᵥ hwVec q m m j = 0 := fun j =>
    hwVec_E q hq m m j (by omega) (by omega) (fun p hp => hint _ (by omega) (by omega))
  have hKw : ∀ j : Fin (m + 1), (tens q hq m).Kp *ᵥ hwVec q m m j
      = q ^ (2 * (m - j)) • hwVec q m m j := fun j => deltaK_hwVec q hq m j (by omega)
  have hF : (tens q hq m).F = deltaF q m m := tens_F q hq m
  -- apply `E^{i0}` and read off the `(0, j0)` coordinate
  have key := congrArg (fun v => ((tens q hq m).E ^ i0 *ᵥ v) (⟨0, by omega⟩, j0)) hc
  simp only [Matrix.mulVec_sum, Matrix.mulVec_smul, Finset.sum_apply, Pi.smul_apply,
    smul_eq_mul, mulVec_zero, Pi.zero_apply] at key
  rw [Finset.sum_eq_single x0] at key
  · have h0 := Rep.E_pow_F_pow_hw_eq hq hq2 (tens q hq m) (hwVec q m m j0) (2 * (m - j0))
      (hEw j0) (hKw j0) i0
    rw [hF] at h0
    rw [strVec, h0, Pi.smul_apply, smul_eq_mul, hwVec_top] at key
    have hP := prod_strSc_ne_zero q hq (2 * (m - j0)) i0 hi0
      (fun i h1 h2 => hint i h1 (by omega))
    exact (mul_ne_zero hx0.1 (by simpa using hP)) key
  · intro x _ hxne
    by_cases hcx : c x = 0
    · simp [hcx]
    by_cases hlt : (x.2 : ℕ) < i0
    · have := Rep.E_pow_F_pow_hw_lt hq hq2 (tens q hq m) (hwVec q m m x.1) (2 * (m - x.1))
        (hEw x.1) (hKw x.1) x.2 i0 hlt
      rw [hF] at this
      simp [strVec, this]
    · push_neg at hlt
      have h1 := Rep.E_pow_F_pow_hw_le hq hq2 (tens q hq m) (hwVec q m m x.1) (2 * (m - x.1))
        (hEw x.1) (hKw x.1) i0 x.2 hlt
      rw [hF] at h1
      rw [strVec, h1, Pi.smul_apply, smul_eq_mul]
      by_cases hg : (x.1 : ℕ) + (x.2 - i0) = j0
      · exfalso
        have hxS : x ∈ S := by
          simp only [hS, Finset.mem_filter, Finset.mem_univ, true_and]
          exact ⟨hcx, by omega⟩
        have := hmin x hxS
        have e1 : (x.1 : ℕ) = x0.1 := by omega
        have e2 : (x.2 : ℕ) = x0.2 := by omega
        exact hxne (Sigma.ext (Fin.ext e1) ((Fin.heq_ext_iff (by rw [e1])).mpr e2))
      · rw [inGrade_strVec q m x.1 (x.2 - i0) _ (by dsimp only; omega)]
        simp
  · intro h; exact absurd (Finset.mem_univ x0) h

theorem card_strIdx : Fintype.card (StrIdx m) = (m + 1) * (m + 1) := by
  rw [Fintype.card_sigma]
  simp only [Fintype.card_fin]
  rw [Fin.sum_univ_eq_sum_range (fun j => 2 * (m - j) + 1) (m + 1)]
  have hr := Finset.sum_range_reflect (fun j => 2 * j + 1) (m + 1)
  have he : ∑ j ∈ Finset.range (m + 1), (2 * (m - j) + 1)
      = ∑ j ∈ Finset.range (m + 1), (2 * (m + 1 - 1 - j) + 1) := by
    refine Finset.sum_congr rfl fun j _ => ?_; congr 2
  rw [he, hr]
  clear hr he
  induction m with
  | zero => simp
  | succ m ih => rw [Finset.sum_range_succ, ih]; ring

theorem card_strIdx_eq_finrank :
    Fintype.card (StrIdx m) = Module.finrank 𝕜 (Fin (m + 1) × Fin (m + 1) → 𝕜) := by
  rw [card_strIdx, Module.finrank_fintype_fun_eq_card, Fintype.card_prod, Fintype.card_fin]

instance : Nonempty (StrIdx m) := ⟨⟨0, 0⟩⟩

/-- **The string basis of `V_{m+1} ⊗ V_{m+1}`**: `V_{m+1} ⊗ V_{m+1} = ⊕_{j ≤ m} V_{2(m−j)+1}`. -/
noncomputable def strBasis (hint : ∀ i, 0 < i → i ≤ 2 * m → qint q i ≠ 0) :
    Module.Basis (StrIdx m) 𝕜 (Fin (m + 1) × Fin (m + 1) → 𝕜) :=
  basisOfLinearIndependentOfCardEqFinrank (strVec_linearIndependent q hq m hq2 hint)
    (card_strIdx_eq_finrank m)

theorem strBasis_apply (hint : ∀ i, 0 < i → i ≤ 2 * m → qint q i ≠ 0) (x : StrIdx m) :
    strBasis q hq m hq2 hint x = strVec q m x := by
  simp [strBasis]

include hq hq2 in
/-- The weights of `V_{N+1}` sum to the quantum dimension: `Σ_{i ≤ N} q^{N−2i} = [N+1]`. -/
theorem sum_string_weights (N : ℕ) :
    ∑ i : Fin (N + 1), q ^ N * (q⁻¹ ^ 2) ^ (i : ℕ) = qint q (N + 1) := by
  have hterm : ∀ i : Fin (N + 1), q ^ N * (q⁻¹ ^ 2) ^ (i : ℕ) = q ^ wt N i := by
    intro i
    unfold wt
    rw [zpow_sub₀ hq, ← pow_mul, inv_pow, zpow_natCast, div_eq_mul_inv]
    congr 2
    norm_cast
  simp only [hterm]
  have hg := geom_wt q hq N
  unfold qint
  rw [eq_div_iff hq2, mul_comm, hg, zpow_neg, ← zpow_natCast, ← zpow_natCast q⁻¹, inv_zpow']
  push_cast
  rw [zpow_neg]

include hq hq2 in
/-- **The quantum trace on `V_{m+1} ⊗ V_{m+1}`.** If `X` is the scalar `c_j` on each string
`Δ(F)^i w_j`, i.e. on each summand `V_{2(m−j)+1}`, then `tr(Δ(K) X) = Σ_j c_j [2(m−j)+1]`. -/
theorem trace_deltaK_mul (hint : ∀ i, 0 < i → i ≤ 2 * m → qint q i ≠ 0)
    (X : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (c : Fin (m + 1) → 𝕜) (hX : ∀ x : StrIdx m, X *ᵥ strVec q m x = c x.1 • strVec q m x) :
    trace (deltaK q m m * X) = ∑ j : Fin (m + 1), c j * qint q (2 * (m - j) + 1) := by
  set b := strBasis q hq m hq2 hint
  have heig : ∀ x : StrIdx m, (deltaK q m m * X) *ᵥ b x
      = (c x.1 * (q ^ (2 * (m - x.1)) * (q⁻¹ ^ 2) ^ (x.2 : ℕ))) • b x := by
    intro x
    have hKw : (tens q hq m).Kp *ᵥ hwVec q m m x.1
        = q ^ (2 * (m - x.1)) • hwVec q m m x.1 := deltaK_hwVec q hq m x.1 (by omega)
    have hK := Rep.Kp_F_pow_hw (tens q hq m) (hwVec q m m x.1) (2 * (m - x.1)) hKw x.2
    rw [tens_F, tens_Kp] at hK
    rw [strBasis_apply, ← mulVec_mulVec, hX, mulVec_smul, strVec, hK, smul_smul]
  rw [← Matrix.trace_toLin'_eq, LinearMap.trace_eq_matrix_trace 𝕜 b]
  simp only [Matrix.trace, Matrix.diag, LinearMap.toMatrix_apply, Matrix.toLin'_apply, heig,
    map_smul, Module.Basis.repr_self, Finsupp.smul_apply, Finsupp.single_eq_same, smul_eq_mul,
    mul_one]
  rw [Fintype.sum_sigma]
  refine Finset.sum_congr rfl fun j _ => ?_
  dsimp only
  rw [← Finset.mul_sum, sum_string_weights q hq hq2]

end Tensor

end QOU.Mass.QuantumSl2
