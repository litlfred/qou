/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Habiro / $(q;q)_n$ Cyclotomic-Basis Expansion of the $q$-Heat Kernel and Archimedean Trichotomy

Task: `qou-8ex3` (Gap 8 under epic `qou-10v9` / `qou-avtq`, owner ruling `Q-10V9-4 = 1`).
Probe companion: `computations/qbeta/q_heat_kernel_habiro_cyclotomic_expansion_probe.py`.
Witness companion: `computations/qbeta/q-heat-kernel-habiro-cyclotomic-expansion.witness.json`.

## Mathematical Summary

Expanding the heat-kernel weight $\exp(-\alpha(q - 1)) = \exp(\alpha(1 - q))$ (where $\alpha = \mu_\lambda s_*$
is the Wedderburn block Casimir scale) in the Habiro cyclotomic basis
$(q;q)_n = \prod_{k=1}^n (1 - q^k)$ produces a formal series
$$F(q; \alpha) \;\sim\; \sum_{n=0}^{\infty} a_n(\alpha)\,(q;q)_n.$$

This module formalizes the exact algebraic structure of this expansion and its archimedean vs.
root-of-unity evaluation trichotomy:

1. **Lower-Triangular $(1 - q)$-Adic Basis Expansion (`qPoch_one_in_eps`, `qPoch_two_in_eps`,
   `qPoch_three_in_eps`, `triangular_solve_order3_unique`):**
   In terms of $\varepsilon = 1 - q$, $(q;q)_n = n!\,\varepsilon^n + O(\varepsilon^{n+1})$ is
   strictly lower-triangular with invertible diagonal $n! \neq 0$:
   $$(q;q)_1 = \varepsilon, \qquad (q;q)_2 = 2\varepsilon^2 - \varepsilon^3, \qquad
     (q;q)_3 = 6\varepsilon^3 - 9\varepsilon^4 + 5\varepsilon^5 - \varepsilon^6.$$
   Hence the Habiro coefficients $a_n(\alpha)$ of any formal power series $\sum_{m \ge 0} c_m \varepsilon^m$
   are uniquely determined by forward triangular elimination.

2. **Exact Symbolic Heat-Kernel Habiro Coefficients and Jet Matching
   (`heatKernelHabiroCoeff`, `habiro_quadratic_jet_remainder`, `habiro_cubic_jet_remainder`):**
   For $c_m = \alpha^m / m!$, forward elimination yields parameter-free polynomials in $\mathbb{Q}[\alpha]$:
   $$a_0(\alpha) = 1, \quad a_1(\alpha) = \alpha, \quad a_2(\alpha) = \frac{\alpha^2}{4}, \quad
     a_3(\alpha) = \frac{\alpha^2(2\alpha + 3)}{72}, \quad a_4(\alpha) = \frac{\alpha^2(\alpha + 3)^2}{576},$$
   whose $N$-th partial sum matches the Taylor jet $\sum_{m=0}^N \frac{\alpha^m}{m!}(1 - q)^m$
   modulo $(1 - q)^{N+1}$.

3. **Root-of-Unity Truncation vs. Archimedean $q_0 > 1$ Divergence & $q$-Borel Reflection
   (`habiroPartialSum_eq_of_pow_eq_one`, `habiroTerm_reflection`, `habiroTerm_abs_ge_of_one_lt`,
   `habiro_heat_kernel_trichotomy`):**
   - At any $N$-th root of unity ($q^N = 1$, $N \ge 1$), $(q;q)_n = 0$ for all $n \ge N$, so the
     partial sums `habiroPartialSum q a M` stabilize identically at $M = N$.
   - At the real archimedean substrate pin $q_0 > 1$, the exact reflection identity
     $$a_n\,(q_0; q_0)_n \;=\; (-1)^n\,q_0^{n(n+1)/2}\,a_n\,(q_0^{-1}; q_0^{-1})_n$$
     exhibits the $q_0^{n(n+1)/2}$ blow-up factor (resolved by dividing by the RSZ $q$-Borel
     kernel $q_0^{n(n+1)/2}$ to pass to the convergent bar-partner $(q_0^{-1}; q_0^{-1})_n$),
     while for all $n \ge N_0$ (`2 ≤ q₀ ^ (n + 1)`), $|a_n \mathrm{qPoch}(q_0, n)| \ge |a_n| \cdot |\mathrm{qPoch}(q_0, N_0)|$
     with $|\mathrm{qPoch}(q_0, N_0)| > 0$.

-- Ref: [habiro-2002] Habiro, Invent. Math. 171 (2008), 1-81
-- Ref: [ramis-sauloy-zhang-2013] Ramis, Sauloy & Zhang, Astérisque 355 (2013) (q-Borel kernel)
-- Ref: [manuscript] computations/qbeta/q_heat_kernel_habiro_cyclotomic_expansion_probe.py
-/
import QOU.QBeta.HabiroEvaluationTrichotomy

namespace QOU.QBeta.QHeatKernelHabiroExpansion

open QOU.QBeta.HabiroEvaluationTrichotomy

/-! ## 1. Partial Sums in the Habiro Cyclotomic Basis $(q;q)_n$ -/

/-- The $N$-term partial sum $\sum_{n=0}^{N-1} a_n\,(q;q)_n$ of a Habiro series with coefficient
sequence $a : \mathbb{N} \to R$. -/
def habiroPartialSum {R : Type*} [CommRing R] (q : R) (a : ℕ → R) (N : ℕ) : R :=
  ∑ n ∈ Finset.range N, a n * qPoch q n

@[simp]
theorem habiroPartialSum_zero {R : Type*} [CommRing R] (q : R) (a : ℕ → R) :
    habiroPartialSum q a 0 = 0 := by
  simp [habiroPartialSum]

theorem habiroPartialSum_succ {R : Type*} [CommRing R] (q : R) (a : ℕ → R) (N : ℕ) :
    habiroPartialSum q a (N + 1) = habiroPartialSum q a N + a N * qPoch q N := by
  unfold habiroPartialSum
  rw [Finset.sum_range_succ]

theorem habiroPartialSum_one {R : Type*} [CommRing R] (q : R) (a : ℕ → R) :
    habiroPartialSum q a 1 = a 0 := by
  rw [habiroPartialSum_succ, habiroPartialSum_zero, qPoch_zero, mul_one, zero_add]

/-- **Exact Root-of-Unity Truncation (`habiroPartialSum_eq_of_pow_eq_one`):**
If $q^N = 1$ with $N \ge 1$, then $(q;q)_n = 0$ for all $n \ge N$, so the Habiro partial sums
stabilize identically at order $N$: for every $M \ge N$,
`habiroPartialSum q a M = habiroPartialSum q a N`. -/
theorem habiroPartialSum_eq_of_pow_eq_one {R : Type*} [CommRing R] {q : R} (a : ℕ → R)
    {N : ℕ} (hN : 1 ≤ N) (hq : q ^ N = 1) :
    ∀ {M : ℕ}, N ≤ M → habiroPartialSum q a M = habiroPartialSum q a N := by
  intro M hNM
  induction M, hNM using Nat.le_induction with
  | base => rfl
  | succ k hk ih =>
    rw [habiroPartialSum_succ, ih, qPoch_eq_zero_of_pow_eq_one q N hN hq k hk, mul_zero, add_zero]

/-! ## 2. Triangular $(1 - q)$-Adic Basis Expansion and Heat-Kernel Jet Matching -/

/-- At $n = 1$, $(q;q)_1 = 1 - q = \varepsilon$. -/
theorem qPoch_one_in_eps {R : Type*} [CommRing R] (q : R) :
    qPoch q 1 = 1 - q := by
  simp [qPoch]

/-- At $n = 2$, $(q;q)_2 = (1 - q)(1 - q^2) = 2(1 - q)^2 - (1 - q)^3$ with leading diagonal
coefficient $2! = 2$. -/
theorem qPoch_two_in_eps {R : Type*} [CommRing R] (q : R) :
    qPoch q 2 = 2 * (1 - q) ^ 2 - (1 - q) ^ 3 := by
  simp only [qPoch]
  ring

/-- At $n = 3$, $(q;q)_3 = (1 - q)(1 - q^2)(1 - q^3) = 6(1 - q)^3 - 9(1 - q)^4 + 5(1 - q)^5 - (1 - q)^6$
with leading diagonal coefficient $3! = 6$. -/
theorem qPoch_three_in_eps {R : Type*} [CommRing R] (q : R) :
    qPoch q 3 = 6 * (1 - q) ^ 3 - 9 * (1 - q) ^ 4 + 5 * (1 - q) ^ 5 - (1 - q) ^ 6 := by
  simp only [qPoch]
  ring

/-- Exact symbolic Habiro coefficients $a_n(\alpha)$ ($0 \le n \le 4$) for the heat-kernel
expansion $\exp(-\alpha(q - 1)) = \exp(\alpha(1 - q)) = \sum_{n \ge 0} a_n(\alpha)\,(q;q)_n$:
- $a_0(\alpha) = 1$
- $a_1(\alpha) = \alpha$
- $a_2(\alpha) = \alpha^2 / 4$
- $a_3(\alpha) = \alpha^2 (2\alpha + 3) / 72$
- $a_4(\alpha) = \alpha^2 (\alpha + 3)^2 / 576$. -/
def heatKernelHabiroCoeff (α : ℚ) : ℕ → ℚ
  | 0 => 1
  | 1 => α
  | 2 => α ^ 2 / 4
  | 3 => α ^ 2 * (2 * α + 3) / 72
  | 4 => α ^ 2 * (α + 3) ^ 2 / 576
  | _ => 0

/-- At $\alpha = 1$, the first five exact rational Habiro coefficients are
$(1, 1, 1/4, 5/72, 1/36)$, matching `q_heat_kernel_habiro_cyclotomic_expansion_probe.py`. -/
theorem heatKernelHabiroCoeff_at_one :
    heatKernelHabiroCoeff 1 0 = 1 ∧
    heatKernelHabiroCoeff 1 1 = 1 ∧
    heatKernelHabiroCoeff 1 2 = 1 / 4 ∧
    heatKernelHabiroCoeff 1 3 = 5 / 72 ∧
    heatKernelHabiroCoeff 1 4 = 1 / 36 := by
  unfold heatKernelHabiroCoeff
  norm_num

/-- **Unique Forward Triangular Elimination through Order $3$ (`triangular_solve_order3_unique`):**
Matching the lower-triangular $(q;q)_n$ basis coefficients against the cubic exponential Taylor
jet $c_0 = 1, c_1 = \alpha, c_2 = \alpha^2 / 2, c_3 = \alpha^3 / 6$:
$$a_0 = 1, \qquad a_1 = \alpha, \qquad 2\,a_2 = \frac{\alpha^2}{2}, \qquad -a_2 + 6\,a_3 = \frac{\alpha^3}{6}$$
uniquely forces $a_n = \mathrm{heatKernelHabiroCoeff}\,\alpha\,n$ for $n \in \{0, 1, 2, 3\}$. -/
theorem triangular_solve_order3_unique {α a0 a1 a2 a3 : ℚ}
    (h0 : a0 = 1)
    (h1 : a1 = α)
    (h2 : 2 * a2 = α ^ 2 / 2)
    (h3 : -a2 + 6 * a3 = α ^ 3 / 6) :
    a0 = heatKernelHabiroCoeff α 0 ∧
    a1 = heatKernelHabiroCoeff α 1 ∧
    a2 = heatKernelHabiroCoeff α 2 ∧
    a3 = heatKernelHabiroCoeff α 3 := by
  dsimp only [heatKernelHabiroCoeff]
  refine ⟨h0, h1, ?_, ?_⟩
  · linarith
  · linarith

/-- **Quadratic Heat-Kernel Jet Matching (`habiro_quadratic_jet_remainder`):**
The quadratic Habiro partial sum $\sum_{n=0}^2 a_n(\alpha)\,(q;q)_n$ matches the quadratic Taylor
jet $1 + \alpha(1 - q) + \frac{\alpha^2}{2}(1 - q)^2$ of $\exp(\alpha(1 - q))$ with exact cubic
remainder $-\frac{\alpha^2}{4}(1 - q)^3$. -/
theorem habiro_quadratic_jet_remainder (q α : ℚ) :
    habiroPartialSum q (heatKernelHabiroCoeff α) 3 -
      (1 + α * (1 - q) + (α ^ 2 / 2) * (1 - q) ^ 2) =
      -(α ^ 2 / 4) * (1 - q) ^ 3 := by
  simp only [habiroPartialSum_succ, habiroPartialSum_zero, heatKernelHabiroCoeff, qPoch]
  ring

/-- **Cubic Heat-Kernel Jet Matching (`habiro_cubic_jet_remainder`):**
The cubic Habiro partial sum $\sum_{n=0}^3 a_n(\alpha)\,(q;q)_n$ matches the cubic Taylor jet
$1 + \alpha(1 - q) + \frac{\alpha^2}{2}(1 - q)^2 + \frac{\alpha^3}{6}(1 - q)^3$ modulo $(1 - q)^4$:
the difference factors exactly as $(1 - q)^4 \cdot \mathrm{rem}_4(q, \alpha)$. -/
theorem habiro_cubic_jet_remainder (q α : ℚ) :
    habiroPartialSum q (heatKernelHabiroCoeff α) 4 -
      (1 + α * (1 - q) + (α ^ 2 / 2) * (1 - q) ^ 2 + (α ^ 3 / 6) * (1 - q) ^ 3) =
      (1 - q) ^ 4 *
        ((α ^ 2 * (2 * α + 3) / 72) * (-9 + 5 * (1 - q) - (1 - q) ^ 2)) := by
  simp only [habiroPartialSum_succ, habiroPartialSum_zero, heatKernelHabiroCoeff, qPoch]
  ring

/-! ## 3. $q$-Borel Reflection Identity and Archimedean Divergence at $q_0 > 1$ -/

/-- **Exact $q$-Borel Reflection Identity for Habiro Terms (`habiroTerm_reflection`):**
For any non-zero $q$ in a field $K$ and coefficient sequence $a : \mathbb{N} \to K$, the $n$-th
Habiro term relates to the reflected bar-partner term $a_n (q^{-1}; q^{-1})_n$ via the RSZ
$q$-Borel theta kernel $q^{\sum_{k < n}(k + 1)} = q^{n(n+1)/2}$:
$$q^{\sum_{k < n}(k + 1)} \cdot \bigl(a_n\,(q^{-1}; q^{-1})_n\bigr) \;=\; (-1)^n \cdot \bigl(a_n\,(q;q)_n\bigr).$$ -/
theorem habiroTerm_reflection {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (a : ℕ → K) (n : ℕ) :
    q ^ (∑ k ∈ Finset.range n, (k + 1)) * (a n * qPoch q⁻¹ n) =
      (-1 : K) ^ n * (a n * qPoch q n) := by
  have h := qPoch_reflection q hq n
  calc
    q ^ (∑ k ∈ Finset.range n, (k + 1)) * (a n * qPoch q⁻¹ n)
        = a n * (q ^ (∑ k ∈ Finset.range n, (k + 1)) * qPoch q⁻¹ n) := by ring
    _ = a n * ((-1 : K) ^ n * qPoch q n) := by rw [h]
    _ = (-1 : K) ^ n * (a n * qPoch q n) := by ring

/-- **Archimedean Term Lower Bound for $q > 1$ (`habiroTerm_abs_ge_of_one_lt`):**
On the real archimedean locus $q > 1$ with turnaround threshold $N_0$ (`∀ n ≥ N₀, 2 ≤ q ^ (n + 1)`),
every Habiro term of index $n \ge N_0$ satisfies
$$|a_n| \cdot |\mathrm{qPoch}(q, N_0)| \;\le\; |a_n \cdot \mathrm{qPoch}(q, n)|,
  \qquad 0 < |\mathrm{qPoch}(q, N_0)|.$$ -/
theorem habiroTerm_abs_ge_of_one_lt {q : ℝ} (hq : 1 < q) (a : ℕ → ℝ) (N₀ : ℕ)
    (hN₀ : ∀ n, N₀ ≤ n → 2 ≤ q ^ (n + 1)) {n : ℕ} (hn : N₀ ≤ n) :
    0 < |qPoch q N₀| ∧ |a n| * |qPoch q N₀| ≤ |a n * qPoch q n| := by
  have hpos : 0 < |qPoch q N₀| := abs_pos.mpr (qPoch_ne_zero_of_one_lt hq N₀)
  have hmono : |qPoch q N₀| ≤ |qPoch q n| := by
    induction n, hn using Nat.le_induction with
    | base => exact le_rfl
    | succ k hk ih =>
      exact le_trans ih (qPoch_abs_le_succ_of_one_lt (hN₀ k hk))
  refine ⟨hpos, ?_⟩
  rw [abs_mul]
  exact mul_le_mul_of_nonneg_left hmono (abs_nonneg (a n))

/-- **Habiro Heat-Kernel Evaluation Trichotomy Capstone (`habiro_heat_kernel_trichotomy`):**
Packages the three regimes of the Habiro expansion $\sum_{n \ge 0} a_n(\alpha)\,(q;q)_n$:
1. **(Root-of-unity finite termination):** At any $N$-th root of unity $\zeta^N = 1$ ($N \ge 1$),
   `habiroPartialSum ζ a M = habiroPartialSum ζ a N` for all $M \ge N$;
2. **($(1 - q)$-adic jet exactness at $q \to 1$):** The quadratic Habiro sum with
   `heatKernelHabiroCoeff α` matches $1 + \alpha(1-q) + \frac{\alpha^2}{2}(1-q)^2$ up to
   $-\frac{\alpha^2}{4}(1-q)^3$;
3. **(Archimedean non-convergence at $q_0 > 1$):** On the real archimedean substrate locus
   $q_0 > 1$ (`∀ n ≥ N₀, 2 ≤ q₀ ^ (n + 1)`), the cyclotomic basis does not tend to $0$
   (`¬ Filter.Tendsto (fun n => qPoch q₀ n) Filter.atTop (nhds 0)`). -/
theorem habiro_heat_kernel_trichotomy {R : Type*} [CommRing R]
    {ζ : R} (a : ℕ → R) {N M : ℕ} (hN : 1 ≤ N) (hζ : ζ ^ N = 1) (hNM : N ≤ M)
    (q_rat α : ℚ) {q₀ : ℝ} (hq₀ : 1 < q₀) (N₀ : ℕ)
    (hN₀ : ∀ n, N₀ ≤ n → 2 ≤ q₀ ^ (n + 1)) :
    habiroPartialSum ζ a M = habiroPartialSum ζ a N ∧
    habiroPartialSum q_rat (heatKernelHabiroCoeff α) 3 -
      (1 + α * (1 - q_rat) + (α ^ 2 / 2) * (1 - q_rat) ^ 2) =
      -(α ^ 2 / 4) * (1 - q_rat) ^ 3 ∧
    ¬ Filter.Tendsto (fun n => qPoch q₀ n) Filter.atTop (nhds 0) := by
  exact ⟨habiroPartialSum_eq_of_pow_eq_one a hN hζ hNM,
    habiro_quadratic_jet_remainder q_rat α,
    qPoch_not_tendsto_zero_of_one_lt hq₀ N₀ hN₀⟩

end QOU.QBeta.QHeatKernelHabiroExpansion
