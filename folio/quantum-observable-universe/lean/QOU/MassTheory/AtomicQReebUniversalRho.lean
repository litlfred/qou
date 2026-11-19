/-
Copyright (c) 2026 Quantum Observable Universe Collaboration. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Collaboration
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# Universal-$\rho$ Normalisation on the Atomic $q$-Reeb Object (Lever 3)

Unconditional formalization of `prop:atomic-q-reeb-universal-rho`
(`mass-theory/atomic-q-reeb-universal-rho.md`):

1. **Per-Block Compact $q$-Reeb Eigenphase (`qReebBlockPhase`):**
   On any rotation block $\lambda$ with $d_\lambda > 0$ and $|\chi_\lambda| \le d_\lambda$,
   $\theta_\lambda = \arccos(\chi_\lambda / d_\lambda) \in [0, \pi]$ recovers
   $d_\lambda \cos \theta_\lambda = \chi_\lambda$.

2. **Markov-Weighted Atomic $q$-Reeb Phase Sum (`atomicReebPhaseSum`):**
   $S(K) = \sum_\lambda y_\lambda\, d_\lambda\, |\theta_\lambda(\mathrm{atom}) - \theta_\lambda(\mathrm{free})|$
   is non-negative whenever $y_\lambda, d_\lambda \ge 0$, symmetric under exchanging free and bound
   configurations, strictly positive whenever at least one positively weighted block shifts phase,
   and bounded above by $\pi \sum_\lambda y_\lambda d_\lambda$ on compact blocks.

3. **Exact $\rho$-Cancellation in the $A = 3$ Mirror Ratio (`lever3_mirror_ratio_rho_independent`):**
   Under the Lever-3 linear law $B(\rho, K) = \rho \cdot S(K)$, for **every** nonzero scale
   $\rho \neq 0$ and any $S(K_2) \neq 0$,
   $$\frac{B(\rho, K_1)}{B(\rho, K_2)} = \frac{\rho \cdot S(K_1)}{\rho \cdot S(K_2)} = \frac{S(K_1)}{S(K_2)},$$
   eliminating $\rho$ identically. Moreover, the relative mirror-ratio residual equals the relative
   spread of the empirical required scales $\rho_{\mathrm{need}}(K) = B_{\mathrm{exp}}(K) / S(K)$,
   and on the witnessed $A = 3$ ($^3\mathrm{H} / {}^3\mathrm{He}$) $q_0$-substrate phase sums
   satisfies $1.1172 < S({}^3\mathrm{H}) / S({}^3\mathrm{He}) < 1.1174$ with $< 1.7\% < 2\%$
   agreement against AME2020.

4. **Structural Underdetermination of Per-Block $\rho_\lambda$ (`per_block_rho_underdetermined`):**
   On any two active rotation blocks ($w_1 > 0, w_2 > 0$), a non-trivial 1-parameter null-space
   family $(\rho_1 + t w_2,\, \rho_2 - t w_1)$ preserves the total binding
   $B = \rho_1 w_1 + \rho_2 w_2$ identically for all $t \in \mathbb{R}$, proving that a single
   total binding observable cannot determine per-block $\rho_\lambda$.
-/

namespace QOU.MassTheory.AtomicQReebUniversalRho

open scoped BigOperators

/-- Per-block $q$-Reeb eigenphase $\theta_\lambda = \arccos(\chi_\lambda / d_\lambda)$ on a
compact rotation block ($|\chi_\lambda / d_\lambda| \le 1$). -/
noncomputable def qReebBlockPhase (χ d : ℝ) : ℝ :=
  Real.arccos (χ / d)

/-- Markov-weighted aggregate free-to-bound $q$-Reeb phase shift
$S(K) = \sum_\lambda y_\lambda\, d_\lambda\, |\theta_\lambda^{\mathrm{atom}} - \theta_\lambda^{\mathrm{free}}|$. -/
def atomicReebPhaseSum {ι : Type*} [Fintype ι] (y d θAtom θFree : ι → ℝ) : ℝ :=
  ∑ i : ι, y i * d i * |θAtom i - θFree i|

/-- Lever-3 proportional binding functional $B(\rho, S) = \rho \cdot S$. -/
def lever3Binding (ρ S : ℝ) : ℝ :=
  ρ * S

/-- Empirical single-isotope required scale $\rho_{\mathrm{need}}(B_{\mathrm{exp}}, S) = B_{\mathrm{exp}} / S$. -/
noncomputable def rhoNeed (B_exp S : ℝ) : ℝ :=
  B_exp / S

/-- Compactness bounds $[0, \pi]$ and exact character recovery $d \cos\theta_\lambda = \chi_\lambda$
on every rotation block with $0 < d$ and $|\chi| \le d$. -/
theorem qReebBlockPhase_bounds_and_cos {χ d : ℝ} (hd : 0 < d) (hχ : |χ| ≤ d) :
    0 ≤ qReebBlockPhase χ d ∧
      qReebBlockPhase χ d ≤ Real.pi ∧
      d * Real.cos (qReebBlockPhase χ d) = χ := by
  have hd_ne : d ≠ 0 := ne_of_gt hd
  have hbounds := abs_le.mp hχ
  have hlo : -1 ≤ χ / d := by
    rw [le_div_iff₀ hd]
    linarith
  have hhi : χ / d ≤ 1 := by
    rw [div_le_iff₀ hd]
    linarith
  refine ⟨Real.arccos_nonneg _, Real.arccos_le_pi _, ?_⟩
  unfold qReebBlockPhase
  rw [Real.cos_arccos hlo hhi]
  exact mul_div_cancel₀ χ hd_ne

/-- Structural properties of `atomicReebPhaseSum`:
1. Non-negativity (`0 ≤ S`),
2. Free-bound exchange symmetry (`S(atom, free) = S(free, atom)`),
3. Strict positivity whenever at least one positively weighted block has $\theta^{\mathrm{atom}}_i \neq \theta^{\mathrm{free}}_i$,
4. Compactness upper bound `S ≤ π * ∑_i y_i d_i` whenever all block angles lie in `[0, π]`. -/
theorem atomicReebPhaseSum_properties {ι : Type*} [Fintype ι] [DecidableEq ι]
    {y d θAtom θFree : ι → ℝ}
    (hy : ∀ i, 0 ≤ y i) (hd : ∀ i, 0 ≤ d i) :
    0 ≤ atomicReebPhaseSum y d θAtom θFree ∧
      atomicReebPhaseSum y d θAtom θFree = atomicReebPhaseSum y d θFree θAtom ∧
      ((∃ i₀ : ι, 0 < y i₀ ∧ 0 < d i₀ ∧ θAtom i₀ ≠ θFree i₀) →
        0 < atomicReebPhaseSum y d θAtom θFree) ∧
      ((∀ i, 0 ≤ θAtom i ∧ θAtom i ≤ Real.pi) →
        (∀ i, 0 ≤ θFree i ∧ θFree i ≤ Real.pi) →
        atomicReebPhaseSum y d θAtom θFree ≤ Real.pi * ∑ i : ι, y i * d i) := by
  have hterm_nonneg : ∀ i : ι, 0 ≤ y i * d i * |θAtom i - θFree i| := fun i =>
    mul_nonneg (mul_nonneg (hy i) (hd i)) (abs_nonneg _)
  refine ⟨Finset.sum_nonneg (fun i _ => hterm_nonneg i), ?_, ?_, ?_⟩
  · unfold atomicReebPhaseSum
    apply Finset.sum_congr rfl
    intro i _
    rw [abs_sub_comm]
  · rintro ⟨i₀, hy₀, hd₀, hne⟩
    unfold atomicReebPhaseSum
    have hpos₀ : 0 < y i₀ * d i₀ * |θAtom i₀ - θFree i₀| :=
      mul_pos (mul_pos hy₀ hd₀) (abs_pos.mpr (sub_ne_zero.mpr hne))
    exact lt_of_lt_of_le hpos₀
      (Finset.single_le_sum (fun i _ => hterm_nonneg i) (Finset.mem_univ i₀))
  · intro hA hF
    unfold atomicReebPhaseSum
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro i _
    have habs_le : |θAtom i - θFree i| ≤ Real.pi := by
      rw [abs_le]
      exact ⟨by linarith [(hA i).1, (hF i).2], by linarith [(hA i).2, (hF i).1]⟩
    calc
      y i * d i * |θAtom i - θFree i| ≤ y i * d i * Real.pi :=
        mul_le_mul_of_nonneg_left habs_le (mul_nonneg (hy i) (hd i))
      _ = Real.pi * (y i * d i) := by ring

/-- **Lever-3 $\rho$-Free Mirror Ratio Theorem:**
1. For **every** nonzero normalisation scale $\rho \neq 0$ and any $S_2 \neq 0$,
   $B(\rho, S_1) / B(\rho, S_2) = S_1 / S_2$ (exact cancellation of $\rho$);
2. Consequently any two nonzero scales $\rho_1, \rho_2 \neq 0$ predict the identical mirror ratio;
3. For positive empirical bindings $B_1, B_2 > 0$ and positive phase sums $S_1, S_2 > 0$,
   the $\rho$-free ratio residual $(S_1 / S_2) / (B_1 / B_2) - 1$ equals the required-scale spread
   $\rho_{\mathrm{need}}(B_2, S_2) / \rho_{\mathrm{need}}(B_1, S_1) - 1$, vanishing iff
   $\rho_{\mathrm{need}}(B_1, S_1) = \rho_{\mathrm{need}}(B_2, S_2)$. -/
theorem lever3_mirror_ratio_rho_independent
    {ρ ρ₁ ρ₂ S₁ S₂ B₁ B₂ : ℝ}
    (hρ : ρ ≠ 0) (hρ₁ : ρ₁ ≠ 0) (hρ₂ : ρ₂ ≠ 0)
    (hS₁ : 0 < S₁) (hS₂ : 0 < S₂) (hB₁ : 0 < B₁) (hB₂ : 0 < B₂) :
    lever3Binding ρ S₁ / lever3Binding ρ S₂ = S₁ / S₂ ∧
      lever3Binding ρ₁ S₁ / lever3Binding ρ₁ S₂ =
        lever3Binding ρ₂ S₁ / lever3Binding ρ₂ S₂ ∧
      (S₁ / S₂) / (B₁ / B₂) - 1 = rhoNeed B₂ S₂ / rhoNeed B₁ S₁ - 1 ∧
      (rhoNeed B₁ S₁ = rhoNeed B₂ S₂ ↔ S₁ / S₂ = B₁ / B₂) := by
  have hS₁_ne : S₁ ≠ 0 := ne_of_gt hS₁
  have hS₂_ne : S₂ ≠ 0 := ne_of_gt hS₂
  have hB₁_ne : B₁ ≠ 0 := ne_of_gt hB₁
  have hB₂_ne : B₂ ≠ 0 := ne_of_gt hB₂
  have hc0 : lever3Binding ρ S₁ / lever3Binding ρ S₂ = S₁ / S₂ := by
    unfold lever3Binding
    exact mul_div_mul_left S₁ S₂ hρ
  have hc1 : lever3Binding ρ₁ S₁ / lever3Binding ρ₁ S₂ = S₁ / S₂ := by
    unfold lever3Binding
    exact mul_div_mul_left S₁ S₂ hρ₁
  have hc2 : lever3Binding ρ₂ S₁ / lever3Binding ρ₂ S₂ = S₁ / S₂ := by
    unfold lever3Binding
    exact mul_div_mul_left S₁ S₂ hρ₂
  refine ⟨hc0, hc1.trans hc2.symm, ?_, ?_⟩
  · unfold rhoNeed
    field_simp [hS₁_ne, hS₂_ne, hB₁_ne, hB₂_ne]
  · unfold rhoNeed
    rw [div_eq_div_iff hS₁_ne hS₂_ne, div_eq_div_iff hS₂_ne hB₂_ne]
    constructor <;> intro h <;> linarith

/-- **Certified $A = 3$ ($^3\mathrm{H} / {}^3\mathrm{He}$) $\rho$-Free Mirror Ratio Enclosure:**
On the witnessed $H_9(q_0)$ rotation-phase sums $S({}^3\mathrm{H}) = 0.4623374074$ and
$S({}^3\mathrm{He}) = 0.4137994922$ against the AME2020 binding ratio
$R_{\mathrm{AME}} = 1.098957086$ (`binding-reeb-ratio-rho-free.witness.json`):
1. $1.1172 < B(\rho, {}^3\mathrm{H}) / B(\rho, {}^3\mathrm{He}) < 1.1174$ for **every** $\rho \neq 0$,
2. The relative $\rho$-free prediction residual satisfies $< 1.7\% < 2\%$. -/
theorem a3_mirror_reeb_ratio_within_two_percent {ρ : ℝ} (hρ : ρ ≠ 0) :
    let S_T : ℝ := 4623374074 / 10000000000
    let S_He3 : ℝ := 4137994922 / 10000000000
    let R_AME : ℝ := 1098957086 / 1000000000
    (11172 : ℝ) / 10000 < lever3Binding ρ S_T / lever3Binding ρ S_He3 ∧
      lever3Binding ρ S_T / lever3Binding ρ S_He3 < (11174 : ℝ) / 10000 ∧
      |(lever3Binding ρ S_T / lever3Binding ρ S_He3) / R_AME - 1| < (17 : ℝ) / 1000 ∧
      (17 : ℝ) / 1000 < (2 : ℝ) / 100 := by
  dsimp only
  have hcancel :
      lever3Binding ρ (4623374074 / 10000000000) /
          lever3Binding ρ (4137994922 / 10000000000) =
        (4623374074 / 10000000000 : ℝ) / (4137994922 / 10000000000 : ℝ) := by
    unfold lever3Binding
    exact mul_div_mul_left _ _ hρ
  rw [hcancel]
  refine ⟨by norm_num, by norm_num, by norm_num, by norm_num⟩

/-- **Structural Underdetermination of Per-Block $\rho_\lambda$ from a Single Total Binding:**
Whenever two rotation blocks carry positive phase weights $w_1 > 0$ and $w_2 > 0$, every candidate
pair $(\rho_1, \rho_2)$ admits a non-trivial 1-parameter affine line
$(\rho_1 + t w_2,\, \rho_2 - t w_1)$ ($t \neq 0$) with distinct block coefficients yet identical
total binding $\rho_1' w_1 + \rho_2' w_2 = \rho_1 w_1 + \rho_2 w_2$. -/
theorem per_block_rho_underdetermined
    {w₁ w₂ ρ₁ ρ₂ t : ℝ} (hw₁ : 0 < w₁) (hw₂ : 0 < w₂) (ht : t ≠ 0) :
    (ρ₁ + t * w₂) * w₁ + (ρ₂ - t * w₁) * w₂ = ρ₁ * w₁ + ρ₂ * w₂ ∧
      ρ₁ + t * w₂ ≠ ρ₁ ∧
      ρ₂ - t * w₁ ≠ ρ₂ := by
  refine ⟨by ring, ?_, ?_⟩
  · intro h
    have hmul : t * w₂ = 0 := by linarith
    exact (mul_eq_zero.mp hmul).elim ht (ne_of_gt hw₂)
  · intro h
    have hmul : t * w₁ = 0 := by linarith
    exact (mul_eq_zero.mp hmul).elim ht (ne_of_gt hw₁)

end QOU.MassTheory.AtomicQReebUniversalRho
