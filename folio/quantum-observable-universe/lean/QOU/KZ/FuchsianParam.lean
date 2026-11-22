import QOU.KZ.KZHalfMonodromy
import QOU.KZ.FuchsianConvergence
import Mathlib.Analysis.Complex.LocallyUniformLimit
import Mathlib.Analysis.Complex.Liouville

/-!
# Fuchsian gauge transformations depending holomorphically on a parameter

A brick of Step 1 of `docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md`. We consider the
Fuchsian equation in `ε`

  `ε ∂_ε F = M(s, ε) F`,   `M(s, ε) = E + ∑_{j ≥ 1} ε^j M_j(s)`,

whose residue `E` does **not** depend on the parameter `s`, while the higher coefficients
`M_j(s)` are holomorphic in `s` on an open set `U` and uniformly bounded by `C ρ^j`.

The normalised gauge transformation `H(s, ε) = ∑ ε^k H_k(s)`, `H_0 = 1`, of
`QOU.KZ.FuchsianFormal` (applied for each fixed `s`) then satisfies:

* every coefficient `H_k` is holomorphic in `s` (`differentiableOn_coeff`): the inverse of the
  indicial operator `k − ad_E` is a *continuous* linear map (open mapping theorem), and it does
  not depend on `s`;
* the weighted coefficients `‖H_k(s)‖ r^k` are bounded **uniformly in `s ∈ U`** for `r ρ < 1`
  (`exists_uniform_bound`), by the majorant argument of `QOU.KZ.FuchsianConvergence`;
* `H(s, ·) ε^E` solves the equation for `0 < ‖ε‖ < r` off the cut (`hasDerivAt_hpar_cpowA`),
  `H(s, ·)` is holomorphic on the disc of radius `r` (`differentiableOn_hpar`), and
  `H(s, 0) = 1` (`hpar_zero`);
* `H(·, ε)` is holomorphic in `s`, with `∂_s H = ∑ ε^k ∂_s H_k` (`hasDerivAt_hpar_param`), and that
  derivative is again a convergent power series in `ε` (`analyticAt_cseries_deriv`);
* `‖H(s, ε) − 1‖ ≤ D q/(1 − q)`, `q = ‖ε‖/r`, uniformly in `s`, so `H(s, ε)` is invertible for
  `‖ε‖` small, uniformly in `s` (`hpar_sub_one_le`, `exists_isUnit_hpar`);
* anything commuting with `E` and every `M_j(s)` commutes with every `H_k(s)`
  (`commute_formalSol`, `commute_coeff`).

Base: complete normed `ℂ`-algebra (archimedean by necessity: this is an analytic step).
Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1
-/

namespace QOU.KZ.FuchsianParam

open Finset QOU.KZ.FuchsianFormal QOU.KZ.FuchsianConvergence QOU.KZ.FuchsianAnalytic
  QOU.KZ.KZComplex

section Commutation

variable {R : Type*} [Ring R]

/-- The indicial operator intertwines `ad_c` whenever `c` commutes with the residue. -/
theorem indicial_ad_comm (c A X : R) (hcA : Commute c A) (k : ℕ) :
    indicial A k (c * X - X * c) = c * indicial A k X - indicial A k X * c := by
  have hk : (k : R) * c = c * k := (Nat.cast_commute k c)
  have e : indicial A k (c * X - X * c) - (c * indicial A k X - indicial A k X * c)
      = ((k : R) * c - c * k) * X + (c * A - A * c) * X + X * (A * c - c * A) := by
    simp only [indicial, ad]; noncomm_ring
  simp only [hk, hcA.eq, sub_self, zero_mul, mul_zero, add_zero] at e
  exact sub_eq_zero.1 e

/-- **Commutation**: an element commuting with every coefficient of `M` commutes with every
coefficient of the normalised formal solution. -/
theorem commute_formalSol (M : ℕ → R) (h : NonResonant (M 0)) (c : R)
    (hc : ∀ j, Commute c (M j)) (k : ℕ) : Commute c (formalSol M h k) := by
  induction k using Nat.strong_induction_on with
  | _ k ih =>
    rcases Nat.eq_zero_or_pos k with rfl | hk
    · rw [formalSol_zero]; exact Commute.one_right c
    · have hrec := indicial_formalSol M h k hk
      have hzero : indicial (M 0) k (c * formalSol M h k - formalSol M h k * c) = indicial (M 0) k 0 := by
        rw [indicial_ad_comm _ _ _ (hc 0), hrec, mul_sum, sum_mul, ← sum_sub_distrib]
        have : indicial (M 0) k (0 : R) = 0 := by simp [indicial, ad]
        rw [this]
        refine sum_eq_zero fun j hj => ?_
        rw [← mul_assoc, (hc (k - j)).eq, mul_assoc, (ih j (mem_range.1 hj)).eq, mul_assoc,
          sub_self]
      exact sub_eq_zero.1 ((h k hk).1 hzero)

end Commutation

variable {R : Type*} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]

section Defs

/-- The coefficient sequence `E, M_1(s), M_2(s), …` at parameter `s`. -/
def Mx (E : R) (M : ℕ → ℂ → R) (s : ℂ) (j : ℕ) : R := if j = 0 then E else M j s

omit [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R] in
@[simp] theorem Mx_zero (E : R) (M : ℕ → ℂ → R) (s : ℂ) : Mx E M s 0 = E := if_pos rfl

omit [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R] in
theorem Mx_of_pos (E : R) (M : ℕ → ℂ → R) (s : ℂ) {j : ℕ} (hj : 0 < j) : Mx E M s j = M j s :=
  if_neg hj.ne'

/-- The `k`-th coefficient `H_k(s)` of the normalised gauge transformation. -/
noncomputable def coeff (E : R) (hE : NonResonant E) (M : ℕ → ℂ → R) (k : ℕ) (s : ℂ) : R :=
  formalSol (Mx E M s) (by simpa [Mx] using hE) k

/-- The gauge transformation `H(s, ε) = ∑ ε^k H_k(s)`. -/
noncomputable def hpar (E : R) (hE : NonResonant E) (M : ℕ → ℂ → R) (s ε : ℂ) : R :=
  cseries (fun k => coeff E hE M k s) ε

variable (E : R) (hE : NonResonant E) (M : ℕ → ℂ → R)

omit [NormedAlgebra ℂ R] [CompleteSpace R] in
theorem coeff_zero (s : ℂ) : coeff E hE M 0 s = 1 := formalSol_zero _ _

omit [NormedAlgebra ℂ R] [CompleteSpace R] in
theorem isFormalGauge_coeff (s : ℂ) :
    IsFormalGauge (Mx E M s) (fun k => coeff E hE M k s) :=
  formalSol_isFormalGauge _ _

omit [CompleteSpace R] in
theorem hpar_zero (s : ℂ) : hpar E hE M s 0 = 1 := by
  unfold hpar; rw [KZHalfMonodromy.cseries_zero, coeff_zero]

omit [NormedAlgebra ℂ R] [CompleteSpace R] in
/-- **Commutation with the parameter**: if `c` commutes with `E` and with every `M_j(s)`, it
commutes with every `H_k(s)`. -/
theorem commute_coeff (s : ℂ) (c : R) (hcE : Commute c E)
    (hcM : ∀ j, 0 < j → Commute c (M j s)) (k : ℕ) : Commute c (coeff E hE M k s) := by
  refine commute_formalSol _ _ c (fun j => ?_) k
  rcases Nat.eq_zero_or_pos j with rfl | hj
  · simpa using hcE
  · rw [Mx_of_pos E M s hj]; exact hcM j hj

end Defs

section Inverse

/-- The indicial operator `X ↦ k X − ad_E X` as a continuous `ℂ`-linear map. -/
noncomputable def indicialCLM (E : R) (k : ℕ) : R →L[ℂ] R :=
  (k : ℂ) • ContinuousLinearMap.id ℂ R -
    (ContinuousLinearMap.mul ℂ R E - (ContinuousLinearMap.mul ℂ R).flip E)

omit [CompleteSpace R] in
theorem indicialCLM_apply (E : R) (k : ℕ) (X : R) : indicialCLM E k X = indicial E k X := by
  simp [indicialCLM, indicial, ad, natCast_mul_eq_csmul]

/-- The continuous inverse of the indicial operator (open mapping theorem). -/
noncomputable def indInv (E : R) (hE : NonResonant E) (k : ℕ) (hk : 0 < k) : R →L[ℂ] R :=
  (ContinuousLinearEquiv.ofBijective (indicialCLM E k)
    (LinearMap.ker_eq_bot.2 (by
      intro x y hxy
      exact (hE k hk).1 (by simpa [indicialCLM_apply] using hxy)))
    (LinearMap.range_eq_top.2 (by
      intro y
      obtain ⟨x, hx⟩ := (hE k hk).2 y
      exact ⟨x, by simpa [indicialCLM_apply] using hx⟩))).symm.toContinuousLinearMap

theorem indInv_indicial (E : R) (hE : NonResonant E) (k : ℕ) (hk : 0 < k) (X : R) :
    indInv E hE k hk (indicial E k X) = X := by
  rw [← indicialCLM_apply]
  exact (ContinuousLinearEquiv.ofBijective (indicialCLM E k) _ _).symm_apply_apply X

variable (E : R) (hE : NonResonant E) (M : ℕ → ℂ → R)

/-- The recursion for the coefficients through the continuous inverse. -/
theorem coeff_rec (k : ℕ) (hk : 0 < k) (s : ℂ) :
    coeff E hE M k s = indInv E hE k hk (∑ j ∈ range k, M (k - j) s * coeff E hE M j s) := by
  have h := indicial_formalSol (Mx E M s) (by simpa [Mx] using hE) k hk
  simp only [Mx_zero] at h
  have hs : ∑ j ∈ range k, Mx E M s (k - j) * formalSol (Mx E M s) (by simpa [Mx] using hE) j
      = ∑ j ∈ range k, M (k - j) s * coeff E hE M j s := by
    refine sum_congr rfl fun j hj => ?_
    rw [Mx_of_pos E M s (by have := mem_range.1 hj; omega)]; rfl
  rw [hs] at h
  rw [← h]
  exact (indInv_indicial E hE k hk _).symm

/-- **Holomorphy of the coefficients in the parameter.** -/
theorem differentiableOn_coeff {U : Set ℂ} (hM : ∀ j, 0 < j → DifferentiableOn ℂ (M j) U) (k : ℕ) :
    DifferentiableOn ℂ (coeff E hE M k) U := by
  induction k using Nat.strong_induction_on with
  | _ k ih =>
    rcases Nat.eq_zero_or_pos k with rfl | hk
    · have : coeff E hE M 0 = fun _ => 1 := funext (coeff_zero E hE M)
      rw [this]; exact differentiableOn_const _
    · have : coeff E hE M k =
          (indInv E hE k hk) ∘ (fun s => ∑ j ∈ range k, M (k - j) s * coeff E hE M j s) :=
        funext (coeff_rec E hE M k hk)
      rw [this]
      refine (indInv E hE k hk).differentiable.comp_differentiableOn ?_
      refine DifferentiableOn.fun_sum fun j hj => ?_
      have hj := mem_range.1 hj
      exact (hM (k - j) (by omega)).mul (ih j hj)

end Inverse


section Bounds

omit [CompleteSpace R] in
/-- **Majorant step with a prescribed bound** (variant of `bounded_weighted`): beyond the
threshold `k₁`, the weighted coefficients never exceed a bound `D` valid below `k₁`. -/
theorem weighted_le_of_initial (M H : ℕ → R) (h0 : H 0 = 1) (hH : IsFormalGauge M H)
    (C ρ r : ℝ) (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hr : 0 < r) (hθ : r * ρ < 1)
    (hM : ∀ m, 0 < m → ‖M m‖ ≤ C * ρ ^ m) (k1 : ℕ)
    (hk1 : 4 * ‖M 0‖ + 2 * C * (r * ρ) / (1 - r * ρ) + 1 < k1) (D : ℝ) (hD0 : 0 ≤ D)
    (hDk : ∀ j < k1, ‖H j‖ * r ^ j ≤ D) (k : ℕ) : ‖H k‖ * r ^ k ≤ D := by
  set θ := r * ρ with hθdef
  have hθ0 : 0 ≤ θ := mul_nonneg hr.le hρ
  have h1θ : 0 < 1 - θ := by linarith
  induction k using Nat.strong_induction_on with
  | _ k ih =>
    by_cases hk : k < k1
    · exact hDk k hk
    push_neg at hk
    have hkpos : (0 : ℝ) < k := by
      have : (1 : ℝ) < k1 := by
        have : 0 ≤ 2 * C * θ / (1 - θ) := by positivity
        linarith [norm_nonneg (M 0)]
      exact lt_of_lt_of_le (by linarith) (Nat.cast_le.2 hk)
    have hk0 : 0 < k := by exact_mod_cast hkpos
    have hkbig : 4 * ‖M 0‖ + 2 * C * θ / (1 - θ) ≤ k := by
      have : (k1 : ℝ) ≤ k := Nat.cast_le.2 hk
      linarith
    have hk4 : 4 * ‖M 0‖ ≤ k := by
      have : 0 ≤ 2 * C * θ / (1 - θ) := by positivity
      linarith
    have hkθ : 2 * C * θ / (1 - θ) ≤ k := by linarith [norm_nonneg (M 0)]
    have hest := norm_coeff_le M H h0 hH k hk0 hk4
    have hterm : ∀ j ∈ range k,
        ‖M (k - j)‖ * ‖H j‖ * r ^ k ≤ C * (θ ^ (k - j) * D) := by
      intro j hj
      have hjk := mem_range.1 hj
      have hMj := hM (k - j) (by omega)
      have hrk : r ^ k = r ^ (k - j) * r ^ j := by rw [← pow_add]; congr 1; omega
      calc ‖M (k - j)‖ * ‖H j‖ * r ^ k
          ≤ C * ρ ^ (k - j) * ‖H j‖ * r ^ k := by gcongr
        _ = C * (θ ^ (k - j) * (‖H j‖ * r ^ j)) := by rw [hrk, hθdef, mul_pow]; ring
        _ ≤ C * (θ ^ (k - j) * D) := by gcongr; exact ih j hjk
    have hsum : (k : ℝ) * (‖H k‖ * r ^ k) ≤ 2 * C * D * (θ / (1 - θ)) := by
      calc (k : ℝ) * (‖H k‖ * r ^ k) = ((k : ℝ) * ‖H k‖) * r ^ k := by ring
        _ ≤ (2 * ∑ j ∈ range k, ‖M (k - j)‖ * ‖H j‖) * r ^ k := by gcongr
        _ = 2 * ∑ j ∈ range k, ‖M (k - j)‖ * ‖H j‖ * r ^ k := by rw [mul_assoc, sum_mul]
        _ ≤ 2 * ∑ j ∈ range k, C * (θ ^ (k - j) * D) :=
          mul_le_mul_of_nonneg_left (sum_le_sum hterm) (by norm_num)
        _ = 2 * C * D * ∑ j ∈ range k, θ ^ (k - j) := by
          rw [← mul_sum, ← sum_mul]; ring
        _ ≤ 2 * C * D * (θ / (1 - θ)) := by
          gcongr; exact sum_pow_sub_le θ hθ0 (by linarith) k
    have : 2 * C * D * (θ / (1 - θ)) ≤ (k : ℝ) * D := by
      have : 2 * C * θ / (1 - θ) * D ≤ (k : ℝ) * D := by gcongr
      calc 2 * C * D * (θ / (1 - θ)) = 2 * C * θ / (1 - θ) * D := by ring
        _ ≤ _ := this
    exact le_of_mul_le_mul_left (hsum.trans this) hkpos

variable (E : R) (hE : NonResonant E) (M : ℕ → ℂ → R) {U : Set ℂ} {C ρ r : ℝ}

/-- Finitely many coefficients are bounded uniformly in the parameter. -/
theorem exists_bound_le (hC : 0 ≤ C) (hρ : 0 ≤ ρ)
    (hMb : ∀ j, 0 < j → ∀ s ∈ U, ‖M j s‖ ≤ C * ρ ^ j) (n : ℕ) :
    ∃ B, 0 ≤ B ∧ ∀ k ≤ n, ∀ s ∈ U, ‖coeff E hE M k s‖ ≤ B := by
  induction n with
  | zero =>
    exact ⟨‖(1 : R)‖, norm_nonneg _, fun k hk s _ => by rw [Nat.le_zero.1 hk, coeff_zero]⟩
  | succ n ih =>
    obtain ⟨B, hB0, hB⟩ := ih
    refine ⟨max B (‖indInv E hE (n + 1) n.succ_pos‖ *
      ∑ j ∈ range (n + 1), C * ρ ^ (n + 1 - j) * B), le_max_of_le_left hB0,
      fun k hk s hs => ?_⟩
    rcases Nat.lt_or_eq_of_le hk with hk | rfl
    · exact (hB k (by omega) s hs).trans (le_max_left _ _)
    · refine le_trans ?_ (le_max_right _ _)
      rw [coeff_rec E hE M (n + 1) n.succ_pos s]
      refine ((indInv E hE (n + 1) n.succ_pos).le_opNorm _).trans
        (mul_le_mul_of_nonneg_left ?_ (norm_nonneg _))
      refine (norm_sum_le _ _).trans (sum_le_sum fun j hj => ?_)
      have hj := mem_range.1 hj
      exact (norm_mul_le _ _).trans (mul_le_mul (hMb _ (by omega) s hs)
        (hB j (by omega) s hs) (norm_nonneg _) (by positivity))

/-- **Uniform weighted bound** `‖H_k(s)‖ r^k ≤ D` for all `s ∈ U`, all `k`, with `D ≥ 0`. -/
theorem exists_uniform_bound (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hr : 0 < r) (hθ : r * ρ < 1)
    (hMb : ∀ j, 0 < j → ∀ s ∈ U, ‖M j s‖ ≤ C * ρ ^ j) :
    ∃ D, 0 ≤ D ∧ ∀ s ∈ U, ∀ k, ‖coeff E hE M k s‖ * r ^ k ≤ D := by
  obtain ⟨k1, hk1⟩ := exists_nat_gt (4 * ‖E‖ + 2 * C * (r * ρ) / (1 - r * ρ) + 1)
  obtain ⟨B, hB0, hB⟩ := exists_bound_le E hE M hC hρ hMb k1
  refine ⟨∑ j ∈ range k1, B * r ^ j, sum_nonneg fun j _ => by positivity, fun s hs k => ?_⟩
  refine weighted_le_of_initial (Mx E M s) (fun k => coeff E hE M k s) (coeff_zero E hE M s)
    (isFormalGauge_coeff E hE M s) C ρ r hC hρ hr hθ (fun m hm => ?_) k1 (by rwa [Mx_zero]) _
    (sum_nonneg fun j _ => by positivity) (fun j hj => ?_) k
  · rw [Mx_of_pos E M s hm]; exact hMb m hm s hs
  · refine le_trans ?_ (single_le_sum (f := fun j => B * r ^ j) (fun j _ => by positivity)
      (mem_range.2 hj))
    exact mul_le_mul_of_nonneg_right (hB j hj.le s hs) (by positivity)

/-- The uniform weighted bound, in the form `∃ D, …`. -/
theorem exists_weighted_bound (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hr : 0 < r) (hθ : r * ρ < 1)
    (hMb : ∀ j, 0 < j → ∀ s ∈ U, ‖M j s‖ ≤ C * ρ ^ j) :
    ∃ D, ∀ s ∈ U, ∀ k, ‖coeff E hE M k s‖ * r ^ k ≤ D :=
  let ⟨D, _, hD⟩ := exists_uniform_bound E hE M hC hρ hr hθ hMb
  ⟨D, hD⟩

omit [NormedAlgebra ℂ R] [CompleteSpace R] in
theorem boundedOn_coeff {D : ℝ} (hD : ∀ s ∈ U, ∀ k, ‖coeff E hE M k s‖ * r ^ k ≤ D) {s : ℂ}
    (hs : s ∈ U) : BoundedOn (fun k => coeff E hE M k s) r := by
  intro t ht0 htr
  refine ⟨D, fun k => le_trans ?_ (hD s hs k)⟩
  exact mul_le_mul_of_nonneg_left (pow_le_pow_left₀ ht0.le htr.le k) (norm_nonneg _)

omit [NormedAlgebra ℂ R] [CompleteSpace R] in
theorem boundedOn_Mx (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hθ : r * ρ < 1)
    (hMb : ∀ j, 0 < j → ∀ s ∈ U, ‖M j s‖ ≤ C * ρ ^ j) {s : ℂ} (hs : s ∈ U) :
    BoundedOn (Mx E M s) r := by
  intro t ht0 htr
  refine ⟨max ‖E‖ C, fun k => ?_⟩
  rcases Nat.eq_zero_or_pos k with rfl | hk
  · simp
  · rw [Mx_of_pos E M s hk]
    have h1 : (t * ρ) ^ k ≤ 1 :=
      pow_le_one₀ (by positivity) (by nlinarith [mul_le_mul_of_nonneg_right htr.le hρ])
    calc ‖M k s‖ * t ^ k ≤ C * ρ ^ k * t ^ k := by gcongr; exact hMb k hk s hs
      _ = C * (t * ρ) ^ k := by rw [mul_pow]; ring
      _ ≤ C * 1 := by gcongr
      _ ≤ max ‖E‖ C := by rw [mul_one]; exact le_max_right _ _

end Bounds

section Epsilon

variable (E : R) (hE : NonResonant E) (M : ℕ → ℂ → R) {U : Set ℂ} {C ρ r : ℝ}

/-- **The `ε`-equation**: `H(s, ε) ε^E` solves `ε ∂_ε F = M(s, ε) F` off the cut, `‖ε‖ < r`. -/
theorem hasDerivAt_hpar_cpowA (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hr : 0 < r) (hθ : r * ρ < 1)
    (hMb : ∀ j, 0 < j → ∀ s ∈ U, ‖M j s‖ ≤ C * ρ ^ j) {s : ℂ} (hs : s ∈ U) {ε : ℂ}
    (hε0 : ε ∈ Complex.slitPlane) (hε : ‖ε‖ < r) :
    HasDerivAt (fun e => hpar E hE M s e * cpowA E e)
      (ε⁻¹ • (cseries (Mx E M s) ε * (hpar E hE M s ε * cpowA E ε))) ε := by
  obtain ⟨D, -, hD⟩ := exists_uniform_bound E hE M hC hρ hr hθ hMb
  have h := hasDerivAt_csolution (boundedOn_Mx E M hC hρ hθ hMb hs)
    (boundedOn_coeff E hE M hD hs) (isFormalGauge_coeff E hE M s) hε0 hε
  rw [Mx_zero] at h
  exact h

/-- **Holomorphy in `ε`** on the disc of radius `r`. -/
theorem differentiableOn_hpar (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hr : 0 < r) (hθ : r * ρ < 1)
    (hMb : ∀ j, 0 < j → ∀ s ∈ U, ‖M j s‖ ≤ C * ρ ^ j) {s : ℂ} (hs : s ∈ U) :
    DifferentiableOn ℂ (hpar E hE M s) (Metric.ball 0 r) := by
  obtain ⟨D, -, hD⟩ := exists_uniform_bound E hE M hC hρ hr hθ hMb
  intro ε hε
  rw [Metric.mem_ball, dist_zero_right] at hε
  exact (hasDerivAt_cseries (boundedOn_coeff E hE M hD hs) hε).differentiableAt.differentiableWithinAt

theorem analyticAt_hpar (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hr : 0 < r) (hθ : r * ρ < 1)
    (hMb : ∀ j, 0 < j → ∀ s ∈ U, ‖M j s‖ ≤ C * ρ ^ j) {s : ℂ} (hs : s ∈ U) :
    AnalyticAt ℂ (hpar E hE M s) 0 :=
  (differentiableOn_hpar E hE M hC hρ hr hθ hMb hs).analyticAt (Metric.ball_mem_nhds 0 hr)

end Epsilon

section Param

variable (E : R) (hE : NonResonant E) (M : ℕ → ℂ → R) {U : Set ℂ} {C ρ r : ℝ}

/-- **Holomorphy in the parameter**, with the termwise `s`-derivative. -/
theorem hasDerivAt_hpar_param (hU : IsOpen U) (hMd : ∀ j, 0 < j → DifferentiableOn ℂ (M j) U)
    (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hr : 0 < r) (hθ : r * ρ < 1)
    (hMb : ∀ j, 0 < j → ∀ s ∈ U, ‖M j s‖ ≤ C * ρ ^ j) {ε : ℂ} (hε : ‖ε‖ < r) :
    DifferentiableOn ℂ (fun s => hpar E hE M s ε) U ∧
      ∀ s ∈ U, HasDerivAt (fun w => hpar E hE M w ε)
        (cseries (fun k => deriv (coeff E hE M k) s) ε) s := by
  obtain ⟨D, hD0, hD⟩ := exists_uniform_bound E hE M hC hρ hr hθ hMb
  set q := ‖ε‖ / r with hq
  have hq0 : 0 ≤ q := by positivity
  have hq1 : q < 1 := (div_lt_one hr).2 hε
  have hu : Summable fun k : ℕ => D * q ^ k := (summable_geometric_of_lt_one hq0 hq1).mul_left D
  have hF : ∀ k, DifferentiableOn ℂ (fun w => ε ^ k • coeff E hE M k w) U :=
    fun k => (differentiableOn_coeff E hE M hMd k).const_smul (ε ^ k)
  have hle : ∀ k, ∀ w ∈ U, ‖ε ^ k • coeff E hE M k w‖ ≤ D * q ^ k := by
    intro k w hw
    have hrk : 0 < r ^ k := pow_pos hr k
    calc ‖ε ^ k • coeff E hE M k w‖ = (‖coeff E hE M k w‖ * r ^ k) * q ^ k := by
          rw [norm_smul, norm_pow, hq, div_pow]; field_simp
      _ ≤ D * q ^ k := by gcongr; exact hD w hw k
  have hdiff : DifferentiableOn ℂ (fun s => hpar E hE M s ε) U :=
    Complex.differentiableOn_tsum_of_summable_norm hu hF hU hle
  refine ⟨hdiff, fun s hs => ?_⟩
  have hsum := Complex.hasSum_deriv_of_summable_norm hu hF hU hle hs
  have e : ∀ k, deriv (fun w => ε ^ k • coeff E hE M k w) s = ε ^ k • deriv (coeff E hE M k) s :=
    fun k => (((differentiableOn_coeff E hE M hMd k).differentiableAt
      (hU.mem_nhds hs)).hasDerivAt.const_smul (ε ^ k)).deriv
  simp only [e] at hsum
  have h2 : cseries (fun k => deriv (coeff E hE M k) s) ε = deriv (fun w => hpar E hE M w ε) s :=
    hsum.tsum_eq
  rw [h2]
  exact (hdiff.differentiableAt (hU.mem_nhds hs)).hasDerivAt

/-- **Cauchy estimate** for the `s`-derivatives of the coefficients. -/
theorem norm_deriv_coeff_le (hMd : ∀ j, 0 < j → DifferentiableOn ℂ (M j) U) {D : ℝ}
    (hD : ∀ s ∈ U, ∀ k, ‖coeff E hE M k s‖ * r ^ k ≤ D) (hr : 0 < r) {s : ℂ} {ρ' : ℝ}
    (hρ' : 0 < ρ') (hball : Metric.closedBall s ρ' ⊆ U) (k : ℕ) :
    ‖deriv (coeff E hE M k) s‖ ≤ D / r ^ k / ρ' := by
  refine Complex.norm_deriv_le_of_forall_mem_sphere_norm_le hρ' ?_ fun z hz => ?_
  · apply DifferentiableOn.diffContOnCl
    rw [closure_ball s hρ'.ne']
    exact (differentiableOn_coeff E hE M hMd k).mono hball
  · rw [le_div_iff₀ (pow_pos hr k)]
    exact hD z (hball (Metric.sphere_subset_closedBall hz)) k

/-- **The `s`-derivative is again a convergent power series in `ε`**, with radius `≥ r`. -/
theorem boundedOn_deriv_coeff (hMd : ∀ j, 0 < j → DifferentiableOn ℂ (M j) U)
    (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hr : 0 < r) (hθ : r * ρ < 1)
    (hMb : ∀ j, 0 < j → ∀ s ∈ U, ‖M j s‖ ≤ C * ρ ^ j) {s : ℂ} {ρ' : ℝ} (hρ' : 0 < ρ')
    (hball : Metric.closedBall s ρ' ⊆ U) :
    BoundedOn (fun k => deriv (coeff E hE M k) s) r ∧
      AnalyticAt ℂ (fun e => cseries (fun k => deriv (coeff E hE M k) s) e) 0 := by
  obtain ⟨D, hD0, hD⟩ := exists_uniform_bound E hE M hC hρ hr hθ hMb
  have hb : BoundedOn (fun k => deriv (coeff E hE M k) s) r := by
    intro t ht0 htr
    refine ⟨D / ρ', fun k => ?_⟩
    have hrk : 0 < r ^ k := pow_pos hr k
    calc ‖deriv (coeff E hE M k) s‖ * t ^ k ≤ D / r ^ k / ρ' * r ^ k :=
          mul_le_mul (norm_deriv_coeff_le E hE M hMd hD hr hρ' hball k)
            (pow_le_pow_left₀ ht0.le htr.le k) (by positivity) (by positivity)
      _ = D / ρ' := by field_simp
  refine ⟨hb, DifferentiableOn.analyticAt (s := Metric.ball 0 r) (fun e he => ?_)
    (Metric.ball_mem_nhds 0 hr)⟩
  rw [Metric.mem_ball, dist_zero_right] at he
  exact (hasDerivAt_cseries hb he).differentiableAt.differentiableWithinAt

end Param

section Unit

variable (E : R) (hE : NonResonant E) (M : ℕ → ℂ → R) {U : Set ℂ} {C ρ r : ℝ}

/-- **Closeness to `1`**: `‖H(s, ε) − 1‖ ≤ D q/(1 − q)`, `q = ‖ε‖/r`, uniformly in `s ∈ U`. -/
theorem hpar_sub_one_le (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hr : 0 < r) (hθ : r * ρ < 1)
    (hMb : ∀ j, 0 < j → ∀ s ∈ U, ‖M j s‖ ≤ C * ρ ^ j) :
    ∃ D, 0 ≤ D ∧ (∀ s ∈ U, ∀ k, ‖coeff E hE M k s‖ * r ^ k ≤ D) ∧
      ∀ s ∈ U, ∀ ε : ℂ, ‖ε‖ < r →
        ‖hpar E hE M s ε - 1‖ ≤ D * (‖ε‖ / r) / (1 - ‖ε‖ / r) := by
  obtain ⟨D, hD0, hD⟩ := exists_uniform_bound E hE M hC hρ hr hθ hMb
  refine ⟨D, hD0, hD, fun s hs ε hε => ?_⟩
  set q := ‖ε‖ / r with hq
  have hq0 : 0 ≤ q := by positivity
  have hq1 : q < 1 := (div_lt_one hr).2 hε
  have hsum := summable_norm_cseries (boundedOn_coeff E hE M hD hs) hε
  have e : hpar E hE M s ε - 1 = ∑' k : ℕ, ε ^ (k + 1) • coeff E hE M (k + 1) s := by
    unfold hpar cseries
    rw [hsum.of_norm.tsum_eq_zero_add, pow_zero, one_smul, coeff_zero, add_sub_cancel_left]
  rw [e]
  have hg : HasSum (fun k : ℕ => D * q ^ (k + 1)) (D * q / (1 - q)) := by
    have := (hasSum_geometric_of_lt_one hq0 hq1).mul_left (D * q)
    convert this using 1
    funext k; ring
  refine tsum_of_norm_bounded hg fun k => ?_
  have hrk : 0 < r ^ (k + 1) := pow_pos hr _
  calc ‖ε ^ (k + 1) • coeff E hE M (k + 1) s‖
      = (‖coeff E hE M (k + 1) s‖ * r ^ (k + 1)) * q ^ (k + 1) := by
        rw [norm_smul, norm_pow, hq, div_pow]; field_simp
    _ ≤ D * q ^ (k + 1) := by gcongr; exact hD s hs (k + 1)

/-- **Uniform invertibility near `ε = 0`.** -/
theorem exists_isUnit_hpar (hC : 0 ≤ C) (hρ : 0 ≤ ρ) (hr : 0 < r) (hθ : r * ρ < 1)
    (hMb : ∀ j, 0 < j → ∀ s ∈ U, ‖M j s‖ ≤ C * ρ ^ j) :
    ∃ δ > 0, ∀ s ∈ U, ∀ ε : ℂ, ‖ε‖ < δ → IsUnit (hpar E hE M s ε) := by
  obtain ⟨D, hD0, -, hD⟩ := hpar_sub_one_le E hE M hC hρ hr hθ hMb
  have h2 : 0 < 2 * D + 2 := by linarith
  refine ⟨r / (2 * D + 2), by positivity, fun s hs ε hε => ?_⟩
  have hεr : ‖ε‖ < r := hε.trans_le (div_le_self hr.le (by linarith))
  set q := ‖ε‖ / r with hq
  have hq0 : 0 ≤ q := by positivity
  have hqs : q * (2 * D + 2) < 1 := by
    have := (lt_div_iff₀ h2).1 hε
    rw [hq, div_mul_eq_mul_div, div_lt_one hr]; exact this
  have h1q : 0 < 1 - q := by nlinarith
  have hlt : ‖hpar E hE M s ε - 1‖ < 1 := by
    refine (hD s hs ε hεr).trans_lt ?_
    rw [div_lt_one h1q]; nlinarith [mul_nonneg hq0 hD0]
  have h1 : ‖1 - hpar E hE M s ε‖ < 1 := by rwa [norm_sub_rev]
  refine ⟨Units.oneSub _ h1, ?_⟩
  simp [Units.oneSub]

end Unit

end QOU.KZ.FuchsianParam
