/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Group.Abs
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Algebra.Polynomial.AlgebraMap
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Data.Rat.Lemmas
import Mathlib.RingTheory.PowerSeries.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Figure-Eight ($4_1$) Steinberg Torsion, 2–3 Pachner Polynomial Jet Obstructions, Formal Dilogarithm Transcendence, and the Liouville Root-Separation Bound

This module formalizes over commutative rings and formal power series (`0 sorry`, standard axioms
only, zero `[Field]` / `field_simp` binders, zero `QOU/Transcendental/` or analytic imports) the
four algebraic mechanisms governing how transcendentals arise — and where algebraic error-bound /
surreal-jet methods succeed versus hit the Kontsevich–Zagier period wall — for the figure-eight
knot $4_1$:

1. **Part A — Purely Algebraic $4_1$ Gluing Locus & 6-Torsion Steinberg Wedge (`[CommRing R]`):**
   - At any root $\omega \in R$ of $\omega^2 - \omega + 1 = 0$, constructs the exact unit pair
     `omegaUnit hω` and `oneSubOmegaUnit hω` (`1 - ω = ω⁻¹`, `ω^3 = -1`, `ω^6 = 1`,
     `ω^2 * (1 - ω)^2 = 1`), and proves that for every bimultiplicative skew-symmetric wedge
     `w : Rˣ → Rˣ → M` into an additive abelian group `M`, `2 • w (omegaUnit hω) (oneSubOmegaUnit hω) = 0`
     and `6 • w (omegaUnit hω) (oneSubOmegaUnit hω) = 0`. Thus the $4_1$ gluing shapes are
     algebraic of degree $2$ and lie in the torsion kernel of the Steinberg map $z \wedge (1 - z)$
     (complementing `QOU.Archimedean.NahmBlochBridge` without `[Field]` binders).

2. **Part B — 2–3 Pachner Pentagon No-Polynomial-Jet Theorem & Truncation Error Bounds:**
   - Defines `clearedPachnerPentagon P N x y` over any `[CommRing R]` by clearing `x^N (1 - y)^N`
     across the 5-term Bloch–Wigner / 2–3 Pachner relation for a degree-`N` polynomial jet `P`,
     proving the universal boundary residue identity
     `clearedPachnerPentagon P N x 1 = P.coeff N * (x ^ N - 1) * (1 - x) ^ N` (`N ≥ 1`), and
     deducing `pachner_pentagon_no_polynomial_jet`: **no non-constant polynomial jet over `ℚ`
     satisfies the 2–3 Pachner 5-term relation with zero error**.
   - Proves the exact parity-cancellation tail formula `dilogTrunc_duplication_tail` and explicit
     all-`M` two-sided rational error bounds `dilogTrunc_duplication_two_sided_bounds` on the
     truncated dilogarithm jet $L_N(z) = \sum_{k=1}^N z^k / k^2$, together with exact non-vanishing
     of the Abel 5-term truncation defect at $(x, y) = (1/2, 1/3)$.

3. **Part C — All-Degree Formal / Surreal-Jet Transcendence of $-\log(1-z)$ and $\mathrm{Li}_2(z)$
   over $\mathbb{Q}[z]$ (`PowerSeries ℚ`, `0 sorry`):**
   - While `QOU.Archimedean.SurrealPrune` proves raw `ord_ω` grade-squeezing on `ℝ` cannot decide
     rationality of standard reals, lifting to the formal deformation / surreal-jet ring
     `PowerSeries ℚ` (`ℚ[[z]]`, paralleling `TowerHeightAttack` and `LawvereCut` prior to
     Archimedean `Coev`) restores derivation structure via the Euler operator $\theta = z\partial_z$
     satisfying $(1 - X) \theta^2 L_2 = X$.
   - Using two coupled division-free Wronskian descents — at $X = 1$ for weight $1$ (`logSeries`)
     and at $X = 0$ on `(ℚ[T])[X]` for weight $2$ (`dilogSeries`) — proves:
     * `logSeries_transcendental`: no non-zero polynomial over `ℚ[X]` annihilates `logSeries`;
     * `logSeries_dilogSeries_alg_independent`: the trivariate evaluation `(T, X, Y) ↦ (logSeries, X, dilogSeries)`
       is **injective** (transcendence degree $2$ over `ℚ(X)`);
     * `dilogSeries_transcendental` (and corollaries `dilogSeries_not_rational`,
       `dilogSeries_not_quadratic`): **for every degree $m \ge 1$, no non-zero polynomial
       $\Phi(Y) \in (\mathbb{Q}[X])[Y]$ vanishes at $Y = \sum_{k=1}^\infty X^k / k^2$**.

4. **Part D — Division-Free Liouville Root-Separation & Rational-Approximation Bound (`ℤ` / `ℚ`):**
   - Proves for every `P : Polynomial ℤ` (`P.natDegree ≤ d`), `p : ℤ`, and `q > 0` with
     `P_ℚ(p / q) ≠ 0` that `|homogEvalInt P d p q| ≥ 1` in `ℤ` and `1 / (q : ℚ)^d ≤ |P_ℚ(p / q)|`,
     establishing the exact denominator-exponent threshold (`q_n^d |P(p_n/q_n)| < 1 ⇒ P(p_n/q_n) = 0`)
     against which the companion 80-dps probe measures the weight-2 `lcm(1..3n)^2` period wall.

-- Ref: [dupont-sah1982] Dupont & Sah, J. Pure Appl. Algebra 25 (1982) 159-195
-- Ref: [zagier-dilogarithm] Zagier, The Dilogarithm Function, Springer (2007) 3-65
-- Ref: [kontsevich-zagier2001] Kontsevich & Zagier, Periods, Mathematics Unlimited (2001) 771-808
-- Ref: [beukers1979] Beukers, Bull. London Math. Soc. 11 (1979) 268-272
-- Ref: [nahm2007] Nahm, Conformal Field Theory and Torsion Elements of the Bloch Group, Springer (2007) 67-132
-- Ref: [nesterenko1996] Nesterenko, Sb. Math. 187 (1996) 1319-1348
-/

set_option autoImplicit false

namespace QOU.BraidsAndKnots
namespace FigureEightPachnerAndJetTranscendence

open scoped BigOperators

/-! ## Part A: Algebraic $4_1$ Gluing Locus & 6-Torsion Steinberg Wedge (`[CommRing R]`) -/

section FigureEightSteinbergTorsion

/-- Exact cyclotomic-6 identities for the $4_1$ regular-ideal-tetrahedron shape root
`ω² - ω + 1 = 0` over any commutative ring `R`. -/
theorem fourOne_sixth_root_identities {R : Type*} [CommRing R] {ω : R}
    (hω : ω ^ 2 - ω + 1 = 0) :
    ω * (1 - ω) = 1 ∧ (1 - ω) * ω = 1 ∧ ω ^ 3 = -1 ∧ ω ^ 6 = 1 ∧
      ω ^ 2 * (1 - ω) ^ 2 = 1 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · linear_combination -hω
  · linear_combination -hω
  · linear_combination (ω + 1) * hω
  · linear_combination (ω ^ 4 + ω ^ 3 - ω - 1) * hω
  · linear_combination (ω ^ 2 - ω - 1) * hω

/-- The $4_1$ tetrahedron shape `ω` packaged as a unit in `Rˣ` with explicit inverse `1 - ω`. -/
def omegaUnit {R : Type*} [CommRing R] {ω : R} (hω : ω ^ 2 - ω + 1 = 0) : Rˣ where
  val := ω
  inv := 1 - ω
  val_inv := (fourOne_sixth_root_identities hω).1
  inv_val := (fourOne_sixth_root_identities hω).2.1

/-- The complementary shape `1 - ω` packaged as a unit in `Rˣ` with explicit inverse `ω`. -/
def oneSubOmegaUnit {R : Type*} [CommRing R] {ω : R} (hω : ω ^ 2 - ω + 1 = 0) : Rˣ where
  val := 1 - ω
  inv := ω
  val_inv := (fourOne_sixth_root_identities hω).2.1
  inv_val := (fourOne_sixth_root_identities hω).1

theorem oneSubOmegaUnit_eq_inv {R : Type*} [CommRing R] {ω : R} (hω : ω ^ 2 - ω + 1 = 0) :
    oneSubOmegaUnit hω = (omegaUnit hω)⁻¹ := by
  ext
  rfl

theorem omegaUnit_pow_six {R : Type*} [CommRing R] {ω : R} (hω : ω ^ 2 - ω + 1 = 0) :
    (omegaUnit hω) ^ 6 = 1 := by
  ext
  exact (fourOne_sixth_root_identities hω).2.2.2.1

/-- **Purely algebraic 2-torsion and 6-torsion Steinberg wedge theorem for $4_1$:**
For any commutative ring `R`, any root `ω` of `ω² - ω + 1 = 0`, and any bimultiplicative
skew-symmetric pairing `w : Rˣ → Rˣ → M` into an additive abelian group `M`, the Steinberg
element `w (omegaUnit hω) (oneSubOmegaUnit hω)` representing `ω ∧ (1 - ω)` satisfies
`2 • w (omegaUnit hω) (oneSubOmegaUnit hω) = 0` and `6 • w (omegaUnit hω) (oneSubOmegaUnit hω) = 0`. -/
theorem fourOne_steinberg_torsion {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M]
    {ω : R} (hω : ω ^ 2 - ω + 1 = 0)
    (w : Rˣ → Rˣ → M)
    (hw_mul : ∀ u₁ u₂ v, w (u₁ * u₂) v = w u₁ v + w u₂ v)
    (hw_skew : ∀ u v, w u v = -w v u) :
    2 • w (omegaUnit hω) (oneSubOmegaUnit hω) = 0 ∧
      6 • w (omegaUnit hω) (oneSubOmegaUnit hω) = 0 := by
  set u := omegaUnit hω
  have hw_one_left : ∀ v, w 1 v = 0 := fun v => by
    have h1 := hw_mul 1 1 v
    rw [one_mul] at h1
    exact left_eq_add.mp h1
  have hw_mul_right : ∀ a v₁ v₂, w a (v₁ * v₂) = w a v₁ + w a v₂ := fun a v₁ v₂ => by
    rw [hw_skew a (v₁ * v₂), hw_mul v₁ v₂ a, neg_add_rev, ← hw_skew a v₂, ← hw_skew a v₁, add_comm]
  have hw_inv : w u u⁻¹ = -w u u := by
    have h := hw_mul_right u u u⁻¹
    rw [mul_inv_cancel, hw_skew u 1, hw_one_left u, neg_zero] at h
    exact eq_neg_of_add_eq_zero_right h.symm
  have h2u : 2 • w u u = 0 := by
    rw [two_nsmul]
    exact add_eq_zero_iff_eq_neg.mpr (hw_skew u u)
  have h2 : 2 • w u (oneSubOmegaUnit hω) = 0 := by
    rw [oneSubOmegaUnit_eq_inv hω, hw_inv, smul_neg, h2u, neg_zero]
  refine ⟨h2, ?_⟩
  have h6 : (6 : ℕ) • w u (oneSubOmegaUnit hω) = 3 • (2 • w u (oneSubOmegaUnit hω)) := by
    rw [← mul_nsmul]
  rw [h6, h2, smul_zero]

end FigureEightSteinbergTorsion

/-! ## Part B: 2–3 Pachner Pentagon No-Polynomial-Jet Obstruction & Truncation Error Bounds -/

section PachnerErrorBounds

/-- Denominator-cleared 2–3 Pachner / Bloch–Wigner 5-term polynomial defect over `[CommRing R]`,
obtained by multiplying `P(x) - P(y) + P(y/x) - P((1 - x⁻¹)/(1 - y⁻¹)) + P((1 - x)/(1 - y))`
by `x^N (1 - y)^N` for a polynomial jet `P` of degree at most `N`. -/
def clearedPachnerPentagon {R : Type*} [CommRing R] (P : Polynomial R) (N : ℕ) (x y : R) : R :=
  ∑ k ∈ Finset.range (N + 1), P.coeff k *
    (x ^ N * (1 - y) ^ N * x ^ k
      - x ^ N * (1 - y) ^ N * y ^ k
      + x ^ (N - k) * (1 - y) ^ N * y ^ k
      - x ^ (N - k) * (1 - y) ^ (N - k) * y ^ k * (1 - x) ^ k
      + x ^ N * (1 - y) ^ (N - k) * (1 - x) ^ k)

/-- **Universal pole-residue evaluation at `y = 1` over `[CommRing R]`:**
For every `N ≥ 1`, evaluating `clearedPachnerPentagon P N x y` at `y = 1` isolates the top
coefficient `P.coeff N * (x ^ N - 1) * (1 - x) ^ N`. -/
theorem clearedPachnerPentagon_eval_one {R : Type*} [CommRing R] (P : Polynomial R)
    {N : ℕ} (hN : 1 ≤ N) (x : R) :
    clearedPachnerPentagon P N x 1 = P.coeff N * (x ^ N - 1) * (1 - x) ^ N := by
  unfold clearedPachnerPentagon
  rw [Finset.sum_range_succ]
  have hlow : ∑ k ∈ Finset.range N, P.coeff k *
      (x ^ N * (1 - (1 : R)) ^ N * x ^ k
        - x ^ N * (1 - (1 : R)) ^ N * (1 : R) ^ k
        + x ^ (N - k) * (1 - (1 : R)) ^ N * (1 : R) ^ k
        - x ^ (N - k) * (1 - (1 : R)) ^ (N - k) * (1 : R) ^ k * (1 - x) ^ k
        + x ^ N * (1 - (1 : R)) ^ (N - k) * (1 - x) ^ k) = 0 := by
    refine Finset.sum_eq_zero fun k hk => ?_
    have hkN : N - k ≠ 0 := Nat.sub_ne_zero_of_lt (Finset.mem_range.mp hk)
    have hN0 : N ≠ 0 := Nat.one_le_iff_ne_zero.mp hN
    simp [sub_self, zero_pow hN0, zero_pow hkN]
  have hN0 : N ≠ 0 := Nat.one_le_iff_ne_zero.mp hN
  rw [hlow, zero_add]
  simp only [sub_self, zero_pow hN0, Nat.sub_self, pow_zero, one_pow]
  ring

/-- **2–3 Pachner Pentagon No-Polynomial-Jet Theorem (`pachner_pentagon_no_polynomial_jet`):**
No non-constant polynomial `P : Polynomial ℚ` (`1 ≤ P.natDegree`) satisfies the cleared
2–3 Pachner 5-term relation identically; explicitly, the defect is non-zero at `(x, y) = (2, 1)`. -/
theorem pachner_pentagon_no_polynomial_jet (P : Polynomial ℚ) (hdeg : 1 ≤ P.natDegree) :
    clearedPachnerPentagon P P.natDegree 2 1 ≠ 0 := by
  rw [clearedPachnerPentagon_eval_one P hdeg 2]
  have hP0 : P ≠ 0 := by
    intro h0
    rw [h0, Polynomial.natDegree_zero] at hdeg
    omega
  have hlead : P.coeff P.natDegree ≠ 0 := Polynomial.leadingCoeff_ne_zero.mpr hP0
  have hpow2 : (2 : ℚ) ^ P.natDegree - 1 ≠ 0 := by
    have hgt : (1 : ℚ) < (2 : ℚ) ^ P.natDegree := one_lt_pow₀ (by norm_num) (by omega)
    linarith
  have hm1 : (1 - (2 : ℚ)) ^ P.natDegree ≠ 0 := pow_ne_zero _ (by norm_num)
  exact mul_ne_zero (mul_ne_zero hlead hpow2) hm1

/-- Finite-birthday / degree-`N` rational dilogarithm truncation `∑_{k=1}^N z^k / k^2`. -/
def dilogTrunc (N : ℕ) (z : ℚ) : ℚ :=
  ∑ k ∈ Finset.Icc 1 N, z ^ k / (k : ℚ) ^ 2

/-- Finite-birthday / degree-`N` rational logarithm truncation `∑_{k=1}^N z^k / k`. -/
def logTrunc (N : ℕ) (z : ℚ) : ℚ :=
  ∑ k ∈ Finset.Icc 1 N, z ^ k / (k : ℚ)

/-- Duplication / distribution defect `L_N(z^2) - 2 L_N(z) - 2 L_N(-z)` on `dilogTrunc`. -/
def dilogDupDefect (N : ℕ) (z : ℚ) : ℚ :=
  dilogTrunc N (z ^ 2) - 2 * dilogTrunc N z - 2 * dilogTrunc N (-z)

/-- Exact parity-cancellation tail identity: at even truncation `2 * M`,
`L_{2M}(z^2) - 2 L_{2M}(z) - 2 L_{2M}(-z) = ∑_{k = M+1}^{2M} (z^2)^k / k^2`. -/
theorem dilogTrunc_duplication_tail (M : ℕ) (z : ℚ) :
    dilogDupDefect (2 * M) z = ∑ k ∈ Finset.Icc (M + 1) (2 * M), (z ^ 2) ^ k / (k : ℚ) ^ 2 := by
  induction M with
  | zero =>
    simp [dilogDupDefect, dilogTrunc]
  | succ m ih =>
    have hIcc2 : ∀ f : ℕ → ℚ,
        ∑ k ∈ Finset.Icc 1 (2 * (m + 1)), f k =
          (∑ k ∈ Finset.Icc 1 (2 * m), f k) + f (2 * m + 1) + f (2 * m + 2) := fun f => by
      have h1 : 2 * (m + 1) = (2 * m + 1) + 1 := by omega
      rw [h1, Finset.sum_Icc_succ_top (by omega), Finset.sum_Icc_succ_top (by omega)]
    have hTail : ∀ f : ℕ → ℚ,
        ∑ k ∈ Finset.Icc (m + 2) (2 * (m + 1)), f k =
          (∑ k ∈ Finset.Icc (m + 1) (2 * m), f k) - f (m + 1) + f (2 * m + 1) + f (2 * m + 2) := fun f => by
      have hbot : ∑ k ∈ Finset.Icc (m + 1) (2 * m + 1), f k =
          f (m + 1) + ∑ k ∈ Finset.Icc (m + 2) (2 * m + 1), f k := by
        have hlt : m + 1 < 2 * m + 2 := by omega
        have hb := Finset.sum_eq_sum_Ico_succ_bot hlt f
        simpa [Finset.Ico_succ_right_eq_Icc] using hb
      have htop1 : ∑ k ∈ Finset.Icc (m + 1) (2 * m + 1), f k =
          (∑ k ∈ Finset.Icc (m + 1) (2 * m), f k) + f (2 * m + 1) :=
        Finset.sum_Icc_succ_top (by omega) f
      have htop2 : ∑ k ∈ Finset.Icc (m + 2) (2 * (m + 1)), f k =
          (∑ k ∈ Finset.Icc (m + 2) (2 * m + 1), f k) + f (2 * m + 2) := by
        have h1 : 2 * (m + 1) = (2 * m + 1) + 1 := by omega
        rw [h1, Finset.sum_Icc_succ_top (by omega)]
      linarith
    unfold dilogDupDefect dilogTrunc at ih ⊢
    rw [hIcc2, hIcc2, hIcc2, hTail]
    have hodd : (-z) ^ (2 * m + 1) = -(z ^ (2 * m + 1)) := by
      have ho : Odd (2 * m + 1) := ⟨m, rfl⟩
      exact ho.neg_pow z
    have heven : (-z) ^ (2 * m + 2) = z ^ (2 * m + 2) := by
      have he : Even (2 * m + 2) := ⟨m + 1, by omega⟩
      exact he.neg_pow z
    have hpow2 : z ^ (2 * m + 2) = (z ^ 2) ^ (m + 1) := by ring
    have hcast : ((2 * m + 2 : ℕ) : ℚ) ^ 2 = 4 * ((m + 1 : ℕ) : ℚ) ^ 2 := by
      push_cast
      ring
    rw [hodd, heven, hpow2, hcast]
    linear_combination ih

/-- **Explicit all-`M` two-sided rational truncation error bounds (`0 < z^2 ≤ 1`):**
For every `M ≥ 1` and `z ≠ 0` with `z^2 ≤ 1`, the truncation defect `dilogDupDefect (2 * M) z`
is strictly positive and bracketed between `(z^2)^(M+1) / (M+1)^2` and `M * (z^2)^(M+1) / (M+1)^2`. -/
theorem dilogTrunc_duplication_two_sided_bounds {M : ℕ} (hM : 1 ≤ M) {z : ℚ}
    (hz0 : z ≠ 0) (hz1 : z ^ 2 ≤ 1) :
    (z ^ 2) ^ (M + 1) / ((M + 1 : ℕ) : ℚ) ^ 2 ≤ dilogDupDefect (2 * M) z ∧
      dilogDupDefect (2 * M) z ≤ (M : ℚ) * ((z ^ 2) ^ (M + 1) / ((M + 1 : ℕ) : ℚ) ^ 2) := by
  rw [dilogTrunc_duplication_tail]
  have hz2_pos : 0 < z ^ 2 := sq_pos_of_ne_zero hz0
  have hz2_nonneg : 0 ≤ z ^ 2 := le_of_lt hz2_pos
  have hmem : M + 1 ∈ Finset.Icc (M + 1) (2 * M) := Finset.mem_Icc.mpr ⟨le_rfl, by omega⟩
  refine ⟨?_, ?_⟩
  · refine Finset.single_le_sum (f := fun k : ℕ => (z ^ 2) ^ k / (k : ℚ) ^ 2) (fun k _ => ?_) hmem
    exact div_nonneg (pow_nonneg hz2_nonneg k) (sq_nonneg _)
  · have hterm_le : ∀ k ∈ Finset.Icc (M + 1) (2 * M),
        (z ^ 2) ^ k / (k : ℚ) ^ 2 ≤ (z ^ 2) ^ (M + 1) / ((M + 1 : ℕ) : ℚ) ^ 2 := by
      intro k hk
      rcases Finset.mem_Icc.mp hk with ⟨hk_lo, _⟩
      have hpow_le : (z ^ 2) ^ k ≤ (z ^ 2) ^ (M + 1) :=
        pow_le_pow_of_le_one hz2_nonneg hz1 hk_lo
      have hden_pos : (0 : ℚ) < ((M + 1 : ℕ) : ℚ) ^ 2 := by positivity
      have hden_le : ((M + 1 : ℕ) : ℚ) ^ 2 ≤ (k : ℚ) ^ 2 := by
        have hnat : ((M + 1 : ℕ) : ℚ) ≤ (k : ℚ) := by exact_mod_cast hk_lo
        nlinarith
      have h1 : (z ^ 2) ^ k / (k : ℚ) ^ 2 ≤ (z ^ 2) ^ (M + 1) / (k : ℚ) ^ 2 :=
        div_le_div_of_nonneg_right hpow_le (sq_nonneg _)
      have h2 : (z ^ 2) ^ (M + 1) / (k : ℚ) ^ 2 ≤ (z ^ 2) ^ (M + 1) / ((M + 1 : ℕ) : ℚ) ^ 2 :=
        div_le_div_of_nonneg_left (pow_nonneg hz2_nonneg _) hden_pos hden_le
      exact le_trans h1 h2
    have hsum := Finset.sum_le_card_nsmul (Finset.Icc (M + 1) (2 * M))
      (fun k => (z ^ 2) ^ k / (k : ℚ) ^ 2)
      ((z ^ 2) ^ (M + 1) / ((M + 1 : ℕ) : ℚ) ^ 2) hterm_le
    have hcard : (Finset.Icc (M + 1) (2 * M)).card = M := by
      rw [Nat.card_Icc]
      omega
    rw [hcard, nsmul_eq_mul] at hsum
    exact hsum

/-- Truncated Abel 5-term 2–3 Pachner defect at rational interior test point `(x, y) = (1/2, 1/3)`
(`xy = 1/6`, `u = 2/5`, `v = 1/5`). -/
def abelFiveTermDefectHalfThird (N : ℕ) : ℚ :=
  dilogTrunc N (1 / 2) + dilogTrunc N (1 / 3) - dilogTrunc N (1 / 6)
    - dilogTrunc N (2 / 5) - dilogTrunc N (1 / 5)
    - logTrunc N (2 / 5) * logTrunc N (1 / 5)

theorem abelFiveTermDefectHalfThird_one_and_two :
    abelFiveTermDefectHalfThird 1 = -1 / 75 ∧ abelFiveTermDefectHalfThird 2 = -7 / 1250 := by
  have h12 : Finset.Icc 1 2 = ({1, 2} : Finset ℕ) := by decide
  refine ⟨?_, ?_⟩
  · simp [abelFiveTermDefectHalfThird, dilogTrunc, logTrunc]
    norm_num
  · simp [abelFiveTermDefectHalfThird, dilogTrunc, logTrunc, h12]
    norm_num

end PachnerErrorBounds

/-! ## Part C: All-Degree Formal / Surreal-Jet Transcendence of $-\log(1-z)$ and $\mathrm{Li}_2(z)$ -/

noncomputable section FormalJetTranscendence

private lemma natDegree_finset_sum_le {S : Type*} [Semiring S] {ι : Type*}
    (s : Finset ι) (f : ι → Polynomial S) (d : ℕ)
    (hf : ∀ i ∈ s, (f i).natDegree ≤ d) :
    (∑ i ∈ s, f i).natDegree ≤ d := by
  refine Polynomial.natDegree_le_iff_coeff_eq_zero.mpr fun m hm => ?_
  rw [Polynomial.finset_sum_coeff]
  refine Finset.sum_eq_zero fun i hi => ?_
  exact Polynomial.coeff_eq_zero_of_natDegree_lt (lt_of_le_of_lt (hf i hi) hm)

/-- Formal Euler derivation `θ = X d/dX` on `PowerSeries ℚ`, multiplying the `n`-th coefficient by `n`. -/
def eulerDeriv : PowerSeries ℚ →ₗ[ℚ] PowerSeries ℚ where
  toFun f := PowerSeries.mk fun n => (n : ℚ) * PowerSeries.coeff n f
  map_add' f g := by
    ext n
    simp [PowerSeries.coeff_mk, mul_add]
  map_smul' c f := by
    ext n
    simp [PowerSeries.coeff_mk]
    ring

@[simp] theorem coeff_eulerDeriv (f : PowerSeries ℚ) (n : ℕ) :
    PowerSeries.coeff n (eulerDeriv f) = (n : ℚ) * PowerSeries.coeff n f := by
  change PowerSeries.coeff n (PowerSeries.mk fun k => (k : ℚ) * PowerSeries.coeff k f) = _
  exact PowerSeries.coeff_mk n _

/-- Leibniz rule for the formal Euler derivation `eulerDeriv` on `PowerSeries ℚ`. -/
theorem eulerDeriv_mul (f g : PowerSeries ℚ) :
    eulerDeriv (f * g) = eulerDeriv f * g + f * eulerDeriv g := by
  ext n
  simp only [coeff_eulerDeriv, map_add, PowerSeries.coeff_mul, Finset.mul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun p hp => ?_
  have hsum : (n : ℚ) = (p.1 : ℚ) + (p.2 : ℚ) := by
    exact_mod_cast (Finset.mem_antidiagonal.mp hp).symm
  rw [hsum]
  ring

theorem eulerDeriv_pow (f : PowerSeries ℚ) (m : ℕ) :
    eulerDeriv (f ^ m) = (m : ℚ) • (f ^ (m - 1) * eulerDeriv f) := by
  induction m with
  | zero =>
    ext n
    simp [coeff_eulerDeriv]
  | succ k ih =>
    rw [pow_succ, eulerDeriv_mul, ih]
    cases k with
    | zero =>
      simp [one_smul]
    | succ j =>
      simp only [Nat.add_sub_cancel, Algebra.smul_def, map_natCast]
      push_cast
      ring

/-- Formal geometric series `∑_{n ≥ 1} X^n = X / (1 - X)` in `PowerSeries ℚ`. -/
def geomSeries : PowerSeries ℚ :=
  PowerSeries.mk fun n => if n = 0 then 0 else 1

/-- Formal weight-1 logarithm jet `-ln(1 - X) = ∑_{n ≥ 1} X^n / n` in `PowerSeries ℚ`. -/
def logSeries : PowerSeries ℚ :=
  PowerSeries.mk fun n => if n = 0 then 0 else 1 / (n : ℚ)

/-- Formal weight-2 dilogarithm jet `Li_2(X) = ∑_{n ≥ 1} X^n / n^2` in `PowerSeries ℚ`. -/
def dilogSeries : PowerSeries ℚ :=
  PowerSeries.mk fun n => if n = 0 then 0 else 1 / (n : ℚ) ^ 2

theorem eulerDeriv_dilogSeries : eulerDeriv dilogSeries = logSeries := by
  ext n
  simp only [coeff_eulerDeriv, dilogSeries, logSeries, PowerSeries.coeff_mk]
  split_ifs with hn
  · simp [hn]
  · have hn0 : (n : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hn
    have hsq : (n : ℚ) * ((n : ℚ)⁻¹ * (n : ℚ)⁻¹) = (n : ℚ)⁻¹ := by
      rw [← mul_assoc, mul_inv_cancel₀ hn0, one_mul]
    simpa [sq, one_div] using hsq

theorem eulerDeriv_logSeries : eulerDeriv logSeries = geomSeries := by
  ext n
  simp only [coeff_eulerDeriv, logSeries, geomSeries, PowerSeries.coeff_mk]
  split_ifs with hn
  · simp [hn]
  · have hn0 : (n : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hn
    exact mul_one_div_cancel hn0

theorem one_sub_X_mul_geomSeries :
    (1 - PowerSeries.X : PowerSeries ℚ) * geomSeries = PowerSeries.X := by
  ext n
  rw [sub_mul, one_mul, map_sub]
  cases n with
  | zero =>
    rw [PowerSeries.coeff_zero_X_mul]
    simp [geomSeries, PowerSeries.coeff_mk, PowerSeries.coeff_X]
  | succ k =>
    rw [PowerSeries.coeff_succ_X_mul]
    cases k with
    | zero =>
      simp [geomSeries, PowerSeries.coeff_mk, PowerSeries.coeff_X]
    | succ m =>
      simp [geomSeries, PowerSeries.coeff_mk, PowerSeries.coeff_X]

/-- **Exact second-order Fuchsian operator equation of the formal dilogarithm jet:**
`(1 - X) * θ(θ(dilogSeries)) = X` in `PowerSeries ℚ`. -/
theorem dilogSeries_fuchsian_ode :
    (1 - PowerSeries.X : PowerSeries ℚ) * eulerDeriv (eulerDeriv dilogSeries) = PowerSeries.X := by
  rw [eulerDeriv_dilogSeries, eulerDeriv_logSeries, one_sub_X_mul_geomSeries]

/-- Compatibility of `eulerDeriv` with polynomial coercion `Polynomial ℚ →+* PowerSeries ℚ`. -/
theorem eulerDeriv_coe_polynomial (P : Polynomial ℚ) :
    eulerDeriv (P : PowerSeries ℚ) = ((Polynomial.X * P.derivative : Polynomial ℚ) : PowerSeries ℚ) := by
  ext n
  rw [coeff_eulerDeriv, Polynomial.coeff_coe, Polynomial.coeff_coe]
  cases n with
  | zero =>
    simp
  | succ k =>
    rw [Polynomial.coeff_X_mul, Polynomial.coeff_derivative]
    push_cast
    ring

theorem coe_polynomial_injective {P Q : Polynomial ℚ}
    (h : (P : PowerSeries ℚ) = (Q : PowerSeries ℚ)) : P = Q := by
  ext n
  have hn := congr_arg (PowerSeries.coeff n) h
  simpa [Polynomial.coeff_coe] using hn

private lemma exists_pow_X_sub_C_mul {R : Type*} [CommRing R] [IsDomain R] (a : R) :
    ∀ Q : Polynomial R, Q ≠ 0 →
      ∃ (k : ℕ) (U : Polynomial R), Q = (Polynomial.X - Polynomial.C a) ^ k * U ∧ U.eval a ≠ 0 := by
  suffices ∀ (n : ℕ) (Q : Polynomial R), Q.natDegree = n → Q ≠ 0 →
      ∃ (k : ℕ) (U : Polynomial R), Q = (Polynomial.X - Polynomial.C a) ^ k * U ∧ U.eval a ≠ 0 by
    intro Q hQ
    exact this Q.natDegree Q rfl hQ
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro Q hdeg hQ
    by_cases ha : Q.eval a = 0
    · have hdvd : Polynomial.X - Polynomial.C a ∣ Q :=
        Polynomial.dvd_iff_isRoot.mpr ha
      rcases hdvd with ⟨Q₁, hQ₁_eq⟩
      have hX0 : (Polynomial.X - Polynomial.C a : Polynomial R) ≠ 0 :=
        Polynomial.X_sub_C_ne_zero a
      have hQ₁0 : Q₁ ≠ 0 := fun h0 => hQ (by simp [hQ₁_eq, h0])
      have hdeg_lt : Q₁.natDegree < n := by
        rw [← hdeg, hQ₁_eq, Polynomial.natDegree_mul hX0 hQ₁0, Polynomial.natDegree_X_sub_C]
        omega
      rcases ih Q₁.natDegree hdeg_lt Q₁ rfl hQ₁0 with ⟨k, U, hU_eq, hU_eval⟩
      refine ⟨k + 1, U, ?_, hU_eval⟩
      rw [hQ₁_eq, hU_eq, pow_succ']
      ring
    · exact ⟨0, Q, by simp, ha⟩

/-- Division-free `(X - 1)`-multiplicity descent on `Polynomial ℚ`:
for `c ≠ 0`, no non-zero polynomial `Q : Polynomial ℚ` satisfies
`(1 - X) * (Q * P' - Q' * P) + C c * Q^2 = 0`. -/
theorem no_polynomial_wronskian_one_sub_X {c : ℚ} (hc : c ≠ 0) :
    ∀ Q P : Polynomial ℚ,
      (1 - Polynomial.X) * (Q * P.derivative - Q.derivative * P) + Polynomial.C c * Q ^ 2 = 0 →
        Q = 0 := by
  suffices ∀ (n : ℕ) (Q P : Polynomial ℚ), Q.natDegree = n →
      (1 - Polynomial.X) * (Q * P.derivative - Q.derivative * P) + Polynomial.C c * Q ^ 2 = 0 →
        Q = 0 by
    intro Q P heq
    exact this Q.natDegree Q P rfl heq
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro Q P hdeg heq
    by_contra hQ
    rcases exists_pow_X_sub_C_mul (1 : ℚ) Q hQ with ⟨k, U, hQ_fac, hU1⟩
    have hQ1 : Q.eval 1 = 0 := by
      have hev := congr_arg (Polynomial.eval 1) heq
      simp only [Polynomial.eval_add, Polynomial.eval_mul, Polynomial.eval_sub,
        Polynomial.eval_one, Polynomial.eval_X, Polynomial.eval_C, Polynomial.eval_pow,
        Polynomial.eval_zero, sub_self, zero_mul, zero_add] at hev
      exact pow_eq_zero (mul_eq_zero.mp hev |>.resolve_left hc)
    have hk_pos : 1 ≤ k := by
      cases k with
      | zero =>
        simp only [pow_zero, one_mul] at hQ_fac
        exact False.elim (hU1 (hQ_fac ▸ hQ1))
      | succ k' => omega
    have hX1_ne : (Polynomial.X - 1 : Polynomial ℚ) ≠ 0 := by
      simpa using Polynomial.X_sub_C_ne_zero (1 : ℚ)
    have hQ_fac' : Q = (Polynomial.X - 1) ^ k * U := by simpa using hQ_fac
    have hQ_deriv : Q.derivative =
        Polynomial.C (k : ℚ) * (Polynomial.X - 1) ^ (k - 1) * U +
          (Polynomial.X - 1) ^ k * U.derivative := by
      rw [hQ_fac', Polynomial.derivative_mul]
      have hd_pow : ((Polynomial.X - 1 : Polynomial ℚ) ^ k).derivative =
          Polynomial.C (k : ℚ) * (Polynomial.X - 1) ^ (k - 1) := by
        rw [Polynomial.derivative_pow, Polynomial.derivative_sub,
          Polynomial.derivative_X, Polynomial.derivative_one, sub_zero, mul_one]
      rw [hd_pow]
    have h1sub : (1 - Polynomial.X : Polynomial ℚ) * (Polynomial.X - 1) ^ (k - 1) =
        -(Polynomial.X - 1) ^ k := by
      have hk_split : (Polynomial.X - 1 : Polynomial ℚ) ^ k =
          (Polynomial.X - 1) * (Polynomial.X - 1) ^ (k - 1) := by
        conv_lhs => rw [← Nat.sub_add_cancel hk_pos, pow_succ']
      rw [hk_split]
      ring
    have hfactor : (Polynomial.X - 1) ^ k *
        (-(Polynomial.X - 1) * (U * P.derivative - U.derivative * P)
          + Polynomial.C (k : ℚ) * U * P
          + Polynomial.C c * (Polynomial.X - 1) ^ k * U ^ 2) = 0 := by
      have hlhs : (1 - Polynomial.X) * (Q * P.derivative - Q.derivative * P) +
          Polynomial.C c * Q ^ 2 =
          (Polynomial.X - 1) ^ k *
            (-(Polynomial.X - 1) * (U * P.derivative - U.derivative * P)
              + Polynomial.C (k : ℚ) * U * P
              + Polynomial.C c * (Polynomial.X - 1) ^ k * U ^ 2) := by
        rw [hQ_deriv, hQ_fac']
        calc (1 - Polynomial.X) *
              ((Polynomial.X - 1) ^ k * U * P.derivative -
                (Polynomial.C (k : ℚ) * (Polynomial.X - 1) ^ (k - 1) * U +
                  (Polynomial.X - 1) ^ k * U.derivative) * P) +
              Polynomial.C c * ((Polynomial.X - 1) ^ k * U) ^ 2
            = (1 - Polynomial.X) * (Polynomial.X - 1) ^ k * (U * P.derivative - U.derivative * P) -
                Polynomial.C (k : ℚ) * ((1 - Polynomial.X) * (Polynomial.X - 1) ^ (k - 1)) * U * P +
                Polynomial.C c * (Polynomial.X - 1) ^ k * (Polynomial.X - 1) ^ k * U ^ 2 := by ring
          _ = (Polynomial.X - 1) ^ k *
                (-(Polynomial.X - 1) * (U * P.derivative - U.derivative * P)
                  + Polynomial.C (k : ℚ) * U * P
                  + Polynomial.C c * (Polynomial.X - 1) ^ k * U ^ 2) := by
                rw [h1sub]
                ring
      exact hlhs.symm.trans heq
    have hcof := (mul_eq_zero.mp hfactor).resolve_left (pow_ne_zero k hX1_ne)
    have hP1 : P.eval 1 = 0 := by
      have hev := congr_arg (Polynomial.eval 1) hcof
      have hk0 : k ≠ 0 := by omega
      simp only [Polynomial.eval_add, Polynomial.eval_mul, Polynomial.eval_neg,
        Polynomial.eval_sub, Polynomial.eval_X, Polynomial.eval_one, Polynomial.eval_C,
        Polynomial.eval_pow, Polynomial.eval_zero, sub_self, neg_zero, zero_mul, zero_pow hk0,
        mul_zero, add_zero, zero_add] at hev
      have hk_q : (k : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hk0
      exact (mul_eq_zero.mp hev).resolve_left (mul_ne_zero hk_q hU1)
    rcases Polynomial.dvd_iff_isRoot.mpr hQ1 with ⟨Q₁, hQ₁_raw⟩
    rcases Polynomial.dvd_iff_isRoot.mpr hP1 with ⟨P₁, hP₁_raw⟩
    have hQ₁ : Q = (Polynomial.X - 1) * Q₁ := by simpa using hQ₁_raw
    have hP₁ : P = (Polynomial.X - 1) * P₁ := by simpa using hP₁_raw
    have hQ₁_ne : Q₁ ≠ 0 := fun h0 => hQ (by simp [hQ₁, h0])
    have hwron : Q * P.derivative - Q.derivative * P =
        (Polynomial.X - 1) ^ 2 * (Q₁ * P₁.derivative - Q₁.derivative * P₁) := by
      rw [hQ₁, hP₁, Polynomial.derivative_mul, Polynomial.derivative_mul,
        Polynomial.derivative_sub, Polynomial.derivative_X, Polynomial.derivative_one,
        sub_zero, one_mul]
      ring
    have heq₁_mul : (Polynomial.X - 1) ^ 2 *
        ((1 - Polynomial.X) * (Q₁ * P₁.derivative - Q₁.derivative * P₁) +
          Polynomial.C c * Q₁ ^ 2) = 0 := by
      calc (Polynomial.X - 1) ^ 2 *
            ((1 - Polynomial.X) * (Q₁ * P₁.derivative - Q₁.derivative * P₁) +
              Polynomial.C c * Q₁ ^ 2)
          = (1 - Polynomial.X) * ((Polynomial.X - 1) ^ 2 *
              (Q₁ * P₁.derivative - Q₁.derivative * P₁)) +
              Polynomial.C c * ((Polynomial.X - 1) * Q₁) ^ 2 := by ring
        _ = (1 - Polynomial.X) * (Q * P.derivative - Q.derivative * P) + Polynomial.C c * Q ^ 2 := by
            rw [← hwron, ← hQ₁]
        _ = 0 := heq
    have heq₁ := (mul_eq_zero.mp heq₁_mul).resolve_left (pow_ne_zero 2 hX1_ne)
    have hdeg_lt : Q₁.natDegree < n := by
      rw [← hdeg, hQ₁, Polynomial.natDegree_mul hX1_ne hQ₁_ne]
      have hd1 : (Polynomial.X - 1 : Polynomial ℚ).natDegree = 1 := by
        simpa using Polynomial.natDegree_X_sub_C (1 : ℚ)
      omega
    exact hQ₁_ne (ih Q₁.natDegree hdeg_lt Q₁ P₁ rfl heq₁)

/-- Ring homomorphism `(ℚ[X])[T] →+* PowerSeries ℚ` evaluating `T ↦ logSeries`. -/
def evalAtLog : Polynomial (Polynomial ℚ) →+* PowerSeries ℚ :=
  Polynomial.eval₂RingHom (Polynomial.coeToPowerSeries.ringHom (R := ℚ)) logSeries

/-- **All-Degree Transcendence of `logSeries = -ln(1 - X)` over `Polynomial ℚ`:**
No non-zero polynomial `Φ ∈ (ℚ[X])[T]` vanishes at `T = logSeries` in `PowerSeries ℚ`. -/
theorem logSeries_transcendental :
    ∀ Φ : Polynomial (Polynomial ℚ), evalAtLog Φ = 0 → Φ = 0 := by
  suffices ∀ (m : ℕ) (Φ : Polynomial (Polynomial ℚ)), Φ.natDegree = m → evalAtLog Φ = 0 → Φ = 0 by
    intro Φ hΦ
    exact this Φ.natDegree Φ rfl hΦ
  intro m
  induction m using Nat.strong_induction_on with
  | h m ih =>
    intro Φ hm hΦ
    by_contra hne
    cases m with
    | zero =>
      have hconst : Φ = Polynomial.C (Φ.coeff 0) := Polynomial.eq_C_of_natDegree_eq_zero hm
      rw [hconst] at hΦ hne
      have hc_ev : ((Φ.coeff 0 : Polynomial ℚ) : PowerSeries ℚ) = 0 := by
        simpa [evalAtLog] using hΦ
      have hc0 : Φ.coeff 0 = 0 := coe_polynomial_injective hc_ev
      exact hne (by simp [hc0])
    | succ k =>
      set Pm := Φ.coeff (k + 1)
      have hPm : Pm ≠ 0 := by
        have hlead : Φ.leadingCoeff ≠ 0 := Polynomial.leadingCoeff_ne_zero.mpr hne
        rwa [Polynomial.leadingCoeff, hm] at hlead
      have hlt_deg : Φ.natDegree < k + 2 := by omega
      have hsum : evalAtLog Φ =
          ∑ i ∈ Finset.range (k + 2), ((Φ.coeff i : Polynomial ℚ) : PowerSeries ℚ) * logSeries ^ i := by
        unfold evalAtLog
        rw [Polynomial.coe_eval₂RingHom, Polynomial.eval₂_eq_sum_range' _ hlt_deg]
        rfl
      have hderiv0 : (1 - PowerSeries.X : PowerSeries ℚ) * eulerDeriv (evalAtLog Φ) = 0 := by
        rw [hΦ, map_zero, mul_zero]
      let coeffPsi : ℕ → Polynomial ℚ := fun i =>
        Polynomial.X * (1 - Polynomial.X) * (Pm * (Φ.coeff i).derivative - Pm.derivative * Φ.coeff i) +
          Polynomial.C ((i + 1 : ℕ) : ℚ) * Polynomial.X * Pm * Φ.coeff (i + 1)
      let Ψ : Polynomial (Polynomial ℚ) :=
        ∑ i ∈ Finset.range (k + 1), Polynomial.C (coeffPsi i) * Polynomial.X ^ i
      have hΨ_eval : evalAtLog Ψ =
          (Pm : PowerSeries ℚ) * ((1 - PowerSeries.X) * eulerDeriv (evalAtLog Φ)) -
            ((Polynomial.X * (1 - Polynomial.X) * Pm.derivative : Polynomial ℚ) : PowerSeries ℚ) * evalAtLog Φ := by
        have htheta : (1 - PowerSeries.X : PowerSeries ℚ) * eulerDeriv (evalAtLog Φ) =
            ∑ i ∈ Finset.range (k + 2),
              (((Polynomial.X * (1 - Polynomial.X) * (Φ.coeff i).derivative : Polynomial ℚ) : PowerSeries ℚ) *
                logSeries ^ i +
                ((i : ℚ) • (((Φ.coeff i : Polynomial ℚ) : PowerSeries ℚ) * PowerSeries.X * logSeries ^ (i - 1)))) := by
          rw [hsum, map_sum, Finset.mul_sum]
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [eulerDeriv_mul, eulerDeriv_coe_polynomial, eulerDeriv_pow, eulerDeriv_logSeries,
            mul_add, ← mul_assoc ((1 - PowerSeries.X : PowerSeries ℚ))]
          have h1x : (1 - PowerSeries.X : PowerSeries ℚ) *
              ((Polynomial.X * (Φ.coeff i).derivative : Polynomial ℚ) : PowerSeries ℚ) =
              ((Polynomial.X * (1 - Polynomial.X) * (Φ.coeff i).derivative : Polynomial ℚ) : PowerSeries ℚ) := by
            simp only [Polynomial.coe_mul, Polynomial.coe_sub, Polynomial.coe_one, Polynomial.coe_X]
            ring
          rw [h1x]
          congr 1
          rw [Algebra.smul_def, Algebra.smul_def]
          calc (1 - PowerSeries.X : PowerSeries ℚ) *
                (((Φ.coeff i : Polynomial ℚ) : PowerSeries ℚ) *
                  ((algebraMap ℚ (PowerSeries ℚ)) (i : ℚ) * (logSeries ^ (i - 1) * geomSeries)))
              = (algebraMap ℚ (PowerSeries ℚ)) (i : ℚ) *
                  ((Φ.coeff i : Polynomial ℚ) : PowerSeries ℚ) *
                  ((1 - PowerSeries.X) * geomSeries) * logSeries ^ (i - 1) := by ring
            _ = (algebraMap ℚ (PowerSeries ℚ)) (i : ℚ) *
                  (((Φ.coeff i : Polynomial ℚ) : PowerSeries ℚ) * PowerSeries.X * logSeries ^ (i - 1)) := by
                rw [one_sub_X_mul_geomSeries]
                ring
        have hΨ_sum : evalAtLog Ψ =
            ∑ i ∈ Finset.range (k + 1), ((coeffPsi i : Polynomial ℚ) : PowerSeries ℚ) * logSeries ^ i := by
          simp only [Ψ, map_sum, map_mul, map_pow]
          refine Finset.sum_congr rfl fun i _ => ?_
          have hc : evalAtLog (Polynomial.C (coeffPsi i)) = ((coeffPsi i : Polynomial ℚ) : PowerSeries ℚ) := by
            simp [evalAtLog]
          have hx : evalAtLog Polynomial.X = logSeries := by simp [evalAtLog]
          rw [hc, hx]
        rw [hΨ_sum, htheta, hsum, Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib]
        have hsplit1 : (∑ i ∈ Finset.range (k + 2),
              ((Pm : PowerSeries ℚ) *
                (((Polynomial.X * (1 - Polynomial.X) * (Φ.coeff i).derivative : Polynomial ℚ) : PowerSeries ℚ) *
                  logSeries ^ i) -
                (((Polynomial.X * (1 - Polynomial.X) * Pm.derivative : Polynomial ℚ) : PowerSeries ℚ) *
                  (((Φ.coeff i : Polynomial ℚ) : PowerSeries ℚ) * logSeries ^ i)))) =
            ∑ i ∈ Finset.range (k + 1),
              (((Polynomial.X * (1 - Polynomial.X) * (Pm * (Φ.coeff i).derivative - Pm.derivative * Φ.coeff i) :
                  Polynomial ℚ) : PowerSeries ℚ) * logSeries ^ i) := by
          rw [Finset.sum_range_succ]
          have htop : (Pm : PowerSeries ℚ) *
              (((Polynomial.X * (1 - Polynomial.X) * Pm.derivative : Polynomial ℚ) : PowerSeries ℚ) *
                logSeries ^ (k + 1)) -
              (((Polynomial.X * (1 - Polynomial.X) * Pm.derivative : Polynomial ℚ) : PowerSeries ℚ) *
                ((Pm : PowerSeries ℚ) * logSeries ^ (k + 1))) = 0 := by ring
          rw [htop, add_zero]
          refine Finset.sum_congr rfl fun i _ => ?_
          simp only [Polynomial.coe_mul, Polynomial.coe_sub]
          ring
        have hsplit2 : (∑ i ∈ Finset.range (k + 2),
              (Pm : PowerSeries ℚ) *
                ((i : ℚ) • (((Φ.coeff i : Polynomial ℚ) : PowerSeries ℚ) *
                  PowerSeries.X * logSeries ^ (i - 1)))) =
            ∑ i ∈ Finset.range (k + 1),
              (((Polynomial.C ((i + 1 : ℕ) : ℚ) * Polynomial.X * Pm * Φ.coeff (i + 1) :
                  Polynomial ℚ) : PowerSeries ℚ) * logSeries ^ i) := by
          rw [Finset.sum_range_succ']
          simp only [CharP.cast_eq_zero, zero_smul, mul_zero, add_zero, Nat.add_sub_cancel]
          refine Finset.sum_congr rfl fun i _ => ?_
          have hcoe_nat : ∀ r : ℕ, ((r : Polynomial ℚ) : PowerSeries ℚ) = (r : PowerSeries ℚ) :=
            fun r => map_natCast (Polynomial.coeToPowerSeries.ringHom (R := ℚ)) r
          simp only [Algebra.smul_def, Polynomial.coe_mul, Polynomial.coe_X,
            map_natCast, hcoe_nat]
          ring
        have hrhs_split : (∑ i ∈ Finset.range (k + 2),
              ((Pm : PowerSeries ℚ) *
                ((((Polynomial.X * (1 - Polynomial.X) * (Φ.coeff i).derivative : Polynomial ℚ) : PowerSeries ℚ) *
                  logSeries ^ i) +
                  ((i : ℚ) • (((Φ.coeff i : Polynomial ℚ) : PowerSeries ℚ) *
                    PowerSeries.X * logSeries ^ (i - 1)))) -
                (((Polynomial.X * (1 - Polynomial.X) * Pm.derivative : Polynomial ℚ) : PowerSeries ℚ) *
                  (((Φ.coeff i : Polynomial ℚ) : PowerSeries ℚ) * logSeries ^ i)))) =
            (∑ i ∈ Finset.range (k + 2),
              ((Pm : PowerSeries ℚ) *
                (((Polynomial.X * (1 - Polynomial.X) * (Φ.coeff i).derivative : Polynomial ℚ) : PowerSeries ℚ) *
                  logSeries ^ i) -
                (((Polynomial.X * (1 - Polynomial.X) * Pm.derivative : Polynomial ℚ) : PowerSeries ℚ) *
                  (((Φ.coeff i : Polynomial ℚ) : PowerSeries ℚ) * logSeries ^ i)))) +
            (∑ i ∈ Finset.range (k + 2),
              (Pm : PowerSeries ℚ) *
                ((i : ℚ) • (((Φ.coeff i : Polynomial ℚ) : PowerSeries ℚ) *
                  PowerSeries.X * logSeries ^ (i - 1)))) := by
          rw [← Finset.sum_add_distrib]
          refine Finset.sum_congr rfl fun i _ => ?_
          ring
        rw [hrhs_split, hsplit1, hsplit2, ← Finset.sum_add_distrib]
        refine Finset.sum_congr rfl fun i _ => ?_
        simp only [coeffPsi, Polynomial.coe_add]
        ring
      have hΨ0 : evalAtLog Ψ = 0 := by
        rw [hΨ_eval, hderiv0, hΦ, mul_zero, mul_zero, sub_self]
      have hΨ_deg : Ψ.natDegree ≤ k := by
        refine natDegree_finset_sum_le _ _ k fun i hi => ?_
        have hik : i ≤ k := Nat.lt_succ_iff.mp (Finset.mem_range.mp hi)
        exact le_trans (Polynomial.natDegree_C_mul_X_pow_le (coeffPsi i) i) hik
      have hΨ_zero : Ψ = 0 := ih Ψ.natDegree (by omega) Ψ rfl hΨ0
      have hcoeff_k : Ψ.coeff k = 0 := by simp [hΨ_zero]
      have hcoeff_k_eq : Ψ.coeff k = coeffPsi k := by
        unfold Ψ
        simp only [Polynomial.finset_sum_coeff, Polynomial.coeff_C_mul_X_pow]
        rw [Finset.sum_eq_single k]
        · simp
        · intro i _ hik
          exact if_neg hik.symm
        · intro hk_abs
          exact False.elim (hk_abs (Finset.mem_range.mpr (Nat.lt_succ_self k)))
      rw [hcoeff_k_eq] at hcoeff_k
      have hX_fac : Polynomial.X *
          ((1 - Polynomial.X) * (Pm * (Φ.coeff k).derivative - Pm.derivative * Φ.coeff k) +
            Polynomial.C ((k + 1 : ℕ) : ℚ) * Pm ^ 2) = 0 := by
        calc Polynomial.X *
              ((1 - Polynomial.X) * (Pm * (Φ.coeff k).derivative - Pm.derivative * Φ.coeff k) +
                Polynomial.C ((k + 1 : ℕ) : ℚ) * Pm ^ 2)
            = coeffPsi k := by
              dsimp [coeffPsi, Pm]
              ring
          _ = 0 := hcoeff_k
      have hwron0 := (mul_eq_zero.mp hX_fac).resolve_left Polynomial.X_ne_zero
      have hk1_ne : ((k + 1 : ℕ) : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.succ_ne_zero k)
      exact hPm (no_polynomial_wronskian_one_sub_X hk1_ne Pm (Φ.coeff k) hwron0)

/-- Ring homomorphism `(ℚ[T])[X] →+* PowerSeries ℚ` sending inner `T ↦ logSeries` and outer
`X ↦ PowerSeries.X`, used for the $X = 0$ Wronskian descent of `dilogSeries`. -/
def evalTX : Polynomial (Polynomial ℚ) →+* PowerSeries ℚ :=
  Polynomial.eval₂RingHom
    (Polynomial.eval₂RingHom (algebraMap ℚ (PowerSeries ℚ)) logSeries)
    PowerSeries.X

/-- Because `logSeries` is transcendental over `ℚ[X]`, `evalTX : (ℚ[T])[X] →+* PowerSeries ℚ`
is injective! -/
theorem evalTX_injective {A : Polynomial (Polynomial ℚ)} (hA : evalTX A = 0) : A = 0 := by
  let swapHom : Polynomial (Polynomial ℚ) →+* Polynomial (Polynomial ℚ) :=
    Polynomial.eval₂RingHom
      (Polynomial.eval₂RingHom (Polynomial.C.comp Polynomial.C) Polynomial.X)
      (Polynomial.C Polynomial.X)
  have hs_all : ∀ s : Polynomial ℚ,
      evalAtLog (Polynomial.eval₂ (Polynomial.C.comp Polynomial.C) Polynomial.X s) =
        Polynomial.eval₂ (algebraMap ℚ (PowerSeries ℚ)) logSeries s := fun s => by
    induction s using Polynomial.induction_on' with
    | add u v ihu ihv =>
      rw [Polynomial.eval₂_add, map_add, Polynomial.eval₂_add, ihu, ihv]
    | monomial j c =>
      simp only [Polynomial.eval₂_monomial, map_mul, map_pow, RingHom.coe_comp,
        Function.comp_apply]
      have hc : evalAtLog (Polynomial.C (Polynomial.C c)) = (algebraMap ℚ (PowerSeries ℚ)) c := by
        ext k
        simp [evalAtLog, Polynomial.coe_C, PowerSeries.coeff_C]
      have hx : evalAtLog Polynomial.X = logSeries := by simp [evalAtLog]
      rw [hc, hx]
  have heval_swap_all : ∀ B : Polynomial (Polynomial ℚ), evalAtLog (swapHom B) = evalTX B := fun B => by
    induction B using Polynomial.induction_on' with
    | add p q ihp ihq =>
      rw [map_add, map_add, map_add, ihp, ihq]
    | monomial n s =>
      have hmon : swapHom (Polynomial.monomial n s) =
          Polynomial.eval₂ (Polynomial.C.comp Polynomial.C) Polynomial.X s *
            Polynomial.C Polynomial.X ^ n := by
        simp [swapHom, Polynomial.eval₂_monomial]
      rw [hmon, map_mul, map_pow, hs_all s]
      have hx2 : evalAtLog (Polynomial.C Polynomial.X) = PowerSeries.X := by
        simp [evalAtLog, Polynomial.coe_X]
      rw [hx2]
      simp [evalTX, Polynomial.eval₂_monomial]
  have hswap0 : swapHom A = 0 := logSeries_transcendental (swapHom A) ((heval_swap_all A).trans hA)
  have hswap_invol : ∀ B : Polynomial (Polynomial ℚ), swapHom (swapHom B) = B := by
    intro B
    induction B using Polynomial.induction_on' with
    | add p q ihp ihq => simp [map_add, ihp, ihq]
    | monomial n s =>
      have hs : swapHom (Polynomial.eval₂ (Polynomial.C.comp Polynomial.C) Polynomial.X s) =
          Polynomial.C s := by
        induction s using Polynomial.induction_on' with
        | add u v ihu ihv =>
          rw [Polynomial.eval₂_add, map_add, Polynomial.C_add, ihu, ihv]
        | monomial j c =>
          rw [Polynomial.eval₂_monomial, map_mul, map_pow, RingHom.coe_comp, Function.comp_apply]
          have hcc : swapHom (Polynomial.C (Polynomial.C c)) = Polynomial.C (Polynomial.C c) := by
            simp [swapHom]
          have hxx : swapHom Polynomial.X = Polynomial.C Polynomial.X := by
            simp [swapHom]
          rw [hcc, hxx, ← map_pow, ← map_mul, Polynomial.C_mul_X_pow_eq_monomial]
      have hmon : swapHom (Polynomial.monomial n s) =
          Polynomial.eval₂ (Polynomial.C.comp Polynomial.C) Polynomial.X s *
            Polynomial.C Polynomial.X ^ n := by
        simp [swapHom, Polynomial.eval₂_monomial]
      have hx : swapHom (Polynomial.C Polynomial.X) = Polynomial.X := by
        simp [swapHom]
      rw [hmon, map_mul, map_pow, hs, hx, Polynomial.C_mul_X_pow_eq_monomial]
  rw [← hswap_invol A, hswap0, map_zero]

/-- Coefficientwise inner `T`-derivative on `Polynomial (Polynomial ℚ)` (`(ℚ[T])[X]`). -/
def innerDerivT (A : Polynomial (Polynomial ℚ)) : Polynomial (Polynomial ℚ) :=
  ∑ i ∈ A.support, Polynomial.monomial i (A.coeff i).derivative

theorem coeff_innerDerivT (A : Polynomial (Polynomial ℚ)) (n : ℕ) :
    (innerDerivT A).coeff n = (A.coeff n).derivative := by
  unfold innerDerivT
  rw [Polynomial.finset_sum_coeff]
  by_cases hn : n ∈ A.support
  · rw [Finset.sum_eq_single n]
    · simp
    · intro i _ hin
      rw [Polynomial.coeff_monomial]
      exact if_neg hin
    · intro h_abs
      exact False.elim (h_abs hn)
  · have hc0 : A.coeff n = 0 := Polynomial.notMem_support_iff.mp hn
    rw [hc0, map_zero]
    refine Finset.sum_eq_zero fun i hi => ?_
    have hin : i ≠ n := fun heq => hn (heq ▸ hi)
    simp [Polynomial.coeff_monomial, hin]

theorem innerDerivT_add (A B : Polynomial (Polynomial ℚ)) :
    innerDerivT (A + B) = innerDerivT A + innerDerivT B := by
  ext n m
  simp [coeff_innerDerivT]

theorem innerDerivT_monomial (n : ℕ) (s : Polynomial ℚ) :
    innerDerivT (Polynomial.monomial n s) = Polynomial.monomial n s.derivative := by
  ext k m
  rw [coeff_innerDerivT]
  by_cases hkn : n = k
  · subst hkn
    simp
  · simp [Polynomial.coeff_monomial, hkn]

theorem innerDerivT_mul (A B : Polynomial (Polynomial ℚ)) :
    innerDerivT (A * B) = innerDerivT A * B + A * innerDerivT B := by
  ext n m
  simp only [Polynomial.coeff_add, Polynomial.coeff_mul, coeff_innerDerivT,
    map_sum, Polynomial.derivative_mul, Finset.sum_add_distrib]

/-- Algebraic lift `deltaTX` on `(ℚ[T])[X]` of `(1 - X) * eulerDeriv` on `PowerSeries ℚ`:
`deltaTX A = X * (innerDerivT A + (1 - X) * A.derivative)`. -/
def deltaTX (A : Polynomial (Polynomial ℚ)) : Polynomial (Polynomial ℚ) :=
  Polynomial.X * (innerDerivT A + (1 - Polynomial.X) * A.derivative)

theorem deltaTX_add (A B : Polynomial (Polynomial ℚ)) :
    deltaTX (A + B) = deltaTX A + deltaTX B := by
  unfold deltaTX
  rw [innerDerivT_add, Polynomial.derivative_add]
  ring

theorem deltaTX_mul (A B : Polynomial (Polynomial ℚ)) :
    deltaTX (A * B) = deltaTX A * B + A * deltaTX B := by
  unfold deltaTX
  rw [innerDerivT_mul, Polynomial.derivative_mul]
  ring

theorem deltaTX_eval_zero (A : Polynomial (Polynomial ℚ)) :
    (deltaTX A).eval 0 = 0 := by
  simp [deltaTX]

theorem evalTX_deltaTX (A : Polynomial (Polynomial ℚ)) :
    evalTX (deltaTX A) = (1 - PowerSeries.X : PowerSeries ℚ) * eulerDeriv (evalTX A) := by
  induction A using Polynomial.induction_on' with
  | add p q ihp ihq =>
    rw [deltaTX_add, map_add, map_add, map_add, mul_add, ihp, ihq]
  | monomial n s =>
    have hs_deriv : ∀ t : Polynomial ℚ,
        (1 - PowerSeries.X : PowerSeries ℚ) *
          eulerDeriv (Polynomial.eval₂ (algebraMap ℚ (PowerSeries ℚ)) logSeries t) =
        PowerSeries.X * Polynomial.eval₂ (algebraMap ℚ (PowerSeries ℚ)) logSeries t.derivative := by
      intro t
      induction t using Polynomial.induction_on' with
      | add u v ihu ihv =>
        rw [Polynomial.eval₂_add, map_add, mul_add, ihu, ihv, Polynomial.derivative_add,
          Polynomial.eval₂_add, mul_add]
      | monomial j c =>
        rw [Polynomial.eval₂_monomial, Polynomial.derivative_monomial, Polynomial.eval₂_monomial]
        rw [← Algebra.smul_def c (logSeries ^ j), map_smul, eulerDeriv_pow, eulerDeriv_logSeries,
          map_mul, map_natCast, Algebra.smul_def, Algebra.smul_def, map_natCast]
        calc (1 - PowerSeries.X : PowerSeries ℚ) *
              ((algebraMap ℚ (PowerSeries ℚ)) c * ((j : PowerSeries ℚ) * (logSeries ^ (j - 1) * geomSeries)))
            = (algebraMap ℚ (PowerSeries ℚ)) c * (j : PowerSeries ℚ) *
                ((1 - PowerSeries.X) * geomSeries) * logSeries ^ (j - 1) := by ring
          _ = PowerSeries.X * (((algebraMap ℚ (PowerSeries ℚ)) c * (j : PowerSeries ℚ)) * logSeries ^ (j - 1)) := by
              rw [one_sub_X_mul_geomSeries]
              ring
    have hmon_delta : deltaTX (Polynomial.monomial n s) =
        Polynomial.X * Polynomial.monomial n s.derivative +
          Polynomial.X * (1 - Polynomial.X) *
            Polynomial.monomial (n - 1) (s * Polynomial.C (n : ℚ)) := by
      unfold deltaTX
      rw [innerDerivT_monomial, Polynomial.derivative_monomial]
      have hcast : s * (n : Polynomial ℚ) = s * Polynomial.C (n : ℚ) := by simp
      rw [hcast]
      ring
    rw [hmon_delta, map_add, map_mul, map_mul, map_mul, map_sub, map_one]
    have hx_ev : evalTX Polynomial.X = PowerSeries.X := by simp [evalTX]
    have hmon_ev : ∀ (k : ℕ) (t : Polynomial ℚ),
        evalTX (Polynomial.monomial k t) =
          Polynomial.eval₂ (algebraMap ℚ (PowerSeries ℚ)) logSeries t * PowerSeries.X ^ k := by
      intro k t
      simp [evalTX, Polynomial.eval₂_monomial]
    have hex : eulerDeriv (PowerSeries.X : PowerSeries ℚ) = PowerSeries.X := by
      ext k
      cases k with
      | zero => simp [coeff_eulerDeriv, PowerSeries.coeff_X]
      | succ m =>
        cases m <;> simp [coeff_eulerDeriv, PowerSeries.coeff_X]
    rw [hx_ev, hmon_ev, hmon_ev, hmon_ev, eulerDeriv_mul, mul_add]
    have hfirst : (1 - PowerSeries.X : PowerSeries ℚ) *
        (eulerDeriv (Polynomial.eval₂ (algebraMap ℚ (PowerSeries ℚ)) logSeries s) * PowerSeries.X ^ n) =
        PowerSeries.X * (Polynomial.eval₂ (algebraMap ℚ (PowerSeries ℚ)) logSeries s.derivative *
          PowerSeries.X ^ n) := by
      calc (1 - PowerSeries.X : PowerSeries ℚ) *
            (eulerDeriv (Polynomial.eval₂ (algebraMap ℚ (PowerSeries ℚ)) logSeries s) * PowerSeries.X ^ n)
          = ((1 - PowerSeries.X) *
              eulerDeriv (Polynomial.eval₂ (algebraMap ℚ (PowerSeries ℚ)) logSeries s)) *
              PowerSeries.X ^ n := by ring
        _ = PowerSeries.X * (Polynomial.eval₂ (algebraMap ℚ (PowerSeries ℚ)) logSeries s.derivative *
              PowerSeries.X ^ n) := by
            rw [hs_deriv s]
            ring
    rw [hfirst, eulerDeriv_pow, hex, Algebra.smul_def]
    simp only [Polynomial.eval₂_mul, Polynomial.eval₂_natCast, map_natCast]
    cases n with
    | zero =>
      simp
    | succ k =>
      simp only [Nat.add_sub_cancel]
      ring

/-- **Division-free `X = 0` descent on `(ℚ[T])[X]` for `dilogSeries`:**
For any `m ≥ 1`, no non-zero `Q : Polynomial (Polynomial ℚ)` satisfies
`Q * deltaTX P - deltaTX Q * P + C (C m * X) * (1 - X) * Q^2 = 0`. -/
theorem no_bivariate_wronskian_dilog {m : ℕ} (hm : 1 ≤ m) :
    ∀ Q P : Polynomial (Polynomial ℚ),
      Q * deltaTX P - deltaTX Q * P +
          Polynomial.C (Polynomial.C (m : ℚ) * Polynomial.X) * (1 - Polynomial.X) * Q ^ 2 = 0 →
        Q = 0 := by
  suffices ∀ (n : ℕ) (Q P : Polynomial (Polynomial ℚ)), Q.natDegree = n →
      Q * deltaTX P - deltaTX Q * P +
          Polynomial.C (Polynomial.C (m : ℚ) * Polynomial.X) * (1 - Polynomial.X) * Q ^ 2 = 0 →
        Q = 0 by
    intro Q P heq
    exact this Q.natDegree Q P rfl heq
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro Q P hdeg heq
    by_contra hQ
    rcases exists_pow_X_sub_C_mul (0 : Polynomial ℚ) Q hQ with ⟨k, U, hQ_fac_raw, hU0⟩
    have hQ_fac : Q = Polynomial.X ^ k * U := by simpa using hQ_fac_raw
    have hm_poly_ne : (Polynomial.C (m : ℚ) * Polynomial.X : Polynomial ℚ) ≠ 0 :=
      mul_ne_zero (Polynomial.C_ne_zero.mpr (Nat.cast_ne_zero.mpr (by omega))) Polynomial.X_ne_zero
    have hQ0 : Q.eval 0 = 0 := by
      have hev := congr_arg (Polynomial.eval 0) heq
      simp only [Polynomial.eval_add, Polynomial.eval_sub, Polynomial.eval_mul,
        Polynomial.eval_C, Polynomial.eval_one, Polynomial.eval_X, Polynomial.eval_pow,
        Polynomial.eval_zero, deltaTX_eval_zero, mul_zero, zero_mul, sub_self, zero_add,
        sub_zero, mul_one] at hev
      exact pow_eq_zero (mul_eq_zero.mp hev |>.resolve_left hm_poly_ne)
    have hk_pos : 1 ≤ k := by
      cases k with
      | zero =>
        simp only [pow_zero, one_mul] at hQ_fac
        exact False.elim (hU0 (hQ_fac ▸ hQ0))
      | succ k' => omega
    have hdX : deltaTX Polynomial.X = Polynomial.X * (1 - Polynomial.X) := by
      have hidX : innerDerivT Polynomial.X = 0 := by
        ext r s
        rw [coeff_innerDerivT, Polynomial.coeff_X]
        split_ifs <;> simp
      simp [deltaTX, hidX]
    have hdelta_Xpow : ∀ j : ℕ, deltaTX (Polynomial.X ^ j) =
        Polynomial.C (Polynomial.C (j : ℚ)) * Polynomial.X ^ j * (1 - Polynomial.X) := by
      intro j
      induction j with
      | zero =>
        have hid1 : innerDerivT 1 = 0 := by
          ext r s
          rw [coeff_innerDerivT, Polynomial.coeff_one]
          split_ifs <;> simp
        simp [deltaTX, hid1]
      | succ r ihr =>
        rw [pow_succ, deltaTX_mul, ihr, hdX]
        push_cast
        simp only [Polynomial.C_add, map_one]
        ring
    have hQ_delta : deltaTX Q =
        Polynomial.X ^ k *
          (Polynomial.C (Polynomial.C (k : ℚ)) * (1 - Polynomial.X) * U + deltaTX U) := by
      rw [hQ_fac, deltaTX_mul, hdelta_Xpow k]
      ring
    have hX_ne : (Polynomial.X : Polynomial (Polynomial ℚ)) ≠ 0 := Polynomial.X_ne_zero
    have hfactor : Polynomial.X ^ k *
        (U * deltaTX P -
          (Polynomial.C (Polynomial.C (k : ℚ)) * (1 - Polynomial.X) * U + deltaTX U) * P +
          Polynomial.C (Polynomial.C (m : ℚ) * Polynomial.X) * (1 - Polynomial.X) *
            Polynomial.X ^ k * U ^ 2) = 0 := by
      have hlhs : Q * deltaTX P - deltaTX Q * P +
          Polynomial.C (Polynomial.C (m : ℚ) * Polynomial.X) * (1 - Polynomial.X) * Q ^ 2 =
          Polynomial.X ^ k *
            (U * deltaTX P -
              (Polynomial.C (Polynomial.C (k : ℚ)) * (1 - Polynomial.X) * U + deltaTX U) * P +
              Polynomial.C (Polynomial.C (m : ℚ) * Polynomial.X) * (1 - Polynomial.X) *
                Polynomial.X ^ k * U ^ 2) := by
        rw [hQ_delta, hQ_fac]
        ring
      exact hlhs.symm.trans heq
    have hcof := (mul_eq_zero.mp hfactor).resolve_left (pow_ne_zero k hX_ne)
    have hP0 : P.eval 0 = 0 := by
      have hev := congr_arg (Polynomial.eval 0) hcof
      have hk0 : k ≠ 0 := by omega
      simp only [Polynomial.eval_add, Polynomial.eval_sub, Polynomial.eval_mul,
        Polynomial.eval_C, Polynomial.eval_one, Polynomial.eval_X, Polynomial.eval_pow,
        Polynomial.eval_zero, deltaTX_eval_zero, mul_zero, sub_zero, mul_one, add_zero,
        zero_pow hk0, zero_sub] at hev
      rw [zero_mul, add_zero] at hev
      have hk_c_ne : (Polynomial.C (k : ℚ) : Polynomial ℚ) ≠ 0 :=
        Polynomial.C_ne_zero.mpr (Nat.cast_ne_zero.mpr hk0)
      have hneg := neg_eq_zero.mp hev
      exact (mul_eq_zero.mp hneg).resolve_left (mul_ne_zero hk_c_ne hU0)
    rcases Polynomial.dvd_iff_isRoot.mpr hQ0 with ⟨Q₁, hQ₁_raw⟩
    rcases Polynomial.dvd_iff_isRoot.mpr hP0 with ⟨P₁, hP₁_raw⟩
    have hQ₁ : Q = Polynomial.X * Q₁ := by simpa using hQ₁_raw
    have hP₁ : P = Polynomial.X * P₁ := by simpa using hP₁_raw
    have hQ₁_ne : Q₁ ≠ 0 := fun h0 => hQ (by simp [hQ₁, h0])
    have hwron : Q * deltaTX P - deltaTX Q * P =
        Polynomial.X ^ 2 * (Q₁ * deltaTX P₁ - deltaTX Q₁ * P₁) := by
      rw [hQ₁, hP₁, deltaTX_mul, deltaTX_mul, hdX]
      ring
    have heq₁_mul : Polynomial.X ^ 2 *
        (Q₁ * deltaTX P₁ - deltaTX Q₁ * P₁ +
          Polynomial.C (Polynomial.C (m : ℚ) * Polynomial.X) * (1 - Polynomial.X) * Q₁ ^ 2) = 0 := by
      calc Polynomial.X ^ 2 *
            (Q₁ * deltaTX P₁ - deltaTX Q₁ * P₁ +
              Polynomial.C (Polynomial.C (m : ℚ) * Polynomial.X) * (1 - Polynomial.X) * Q₁ ^ 2)
          = Polynomial.X ^ 2 * (Q₁ * deltaTX P₁ - deltaTX Q₁ * P₁) +
              Polynomial.C (Polynomial.C (m : ℚ) * Polynomial.X) * (1 - Polynomial.X) *
                (Polynomial.X * Q₁) ^ 2 := by ring
        _ = Q * deltaTX P - deltaTX Q * P +
              Polynomial.C (Polynomial.C (m : ℚ) * Polynomial.X) * (1 - Polynomial.X) * Q ^ 2 := by
            rw [← hwron, ← hQ₁]
        _ = 0 := heq
    have heq₁ := (mul_eq_zero.mp heq₁_mul).resolve_left (pow_ne_zero 2 hX_ne)
    have hdeg_lt : Q₁.natDegree < n := by
      rw [← hdeg, hQ₁, Polynomial.natDegree_mul hX_ne hQ₁_ne, Polynomial.natDegree_X]
      omega
    exact hQ₁_ne (ih Q₁.natDegree hdeg_lt Q₁ P₁ rfl heq₁)

/-- Trivariate evaluation `((ℚ[T])[X])[Y] →+* PowerSeries ℚ` sending
`(T, X, Y) ↦ (logSeries, PowerSeries.X, dilogSeries)`. -/
def evalTXDilog : Polynomial (Polynomial (Polynomial ℚ)) →+* PowerSeries ℚ :=
  Polynomial.eval₂RingHom evalTX dilogSeries

/-- **Algebraic Independence of `(logSeries, dilogSeries)` over `ℚ[X]` (Transcendence Degree 2):**
Every polynomial `Θ ∈ ((ℚ[T])[X])[Y]` vanishing at `(logSeries, X, dilogSeries)` in
`PowerSeries ℚ` is identically zero. -/
theorem logSeries_dilogSeries_alg_independent :
    ∀ Θ : Polynomial (Polynomial (Polynomial ℚ)), evalTXDilog Θ = 0 → Θ = 0 := by
  suffices ∀ (m : ℕ) (Θ : Polynomial (Polynomial (Polynomial ℚ))),
      Θ.natDegree = m → evalTXDilog Θ = 0 → Θ = 0 by
    intro Θ hΘ
    exact this Θ.natDegree Θ rfl hΘ
  intro m
  induction m using Nat.strong_induction_on with
  | h m ih =>
    intro Θ hm hΘ
    by_contra hne
    cases m with
    | zero =>
      have hconst : Θ = Polynomial.C (Θ.coeff 0) := Polynomial.eq_C_of_natDegree_eq_zero hm
      rw [hconst] at hΘ hne
      have hc_ev : evalTX (Θ.coeff 0) = 0 := by simpa [evalTXDilog] using hΘ
      exact hne (by simp [evalTX_injective hc_ev])
    | succ k =>
      set Am := Θ.coeff (k + 1)
      have hAm : Am ≠ 0 := by
        have hlead : Θ.leadingCoeff ≠ 0 := Polynomial.leadingCoeff_ne_zero.mpr hne
        rwa [Polynomial.leadingCoeff, hm] at hlead
      have hlt_deg : Θ.natDegree < k + 2 := by omega
      have hsum : evalTXDilog Θ =
          ∑ i ∈ Finset.range (k + 2), evalTX (Θ.coeff i) * dilogSeries ^ i := by
        unfold evalTXDilog
        rw [Polynomial.coe_eval₂RingHom, Polynomial.eval₂_eq_sum_range' _ hlt_deg]
      have hderiv0 : (1 - PowerSeries.X : PowerSeries ℚ) * eulerDeriv (evalTXDilog Θ) = 0 := by
        rw [hΘ, map_zero, mul_zero]
      let coeffXi : ℕ → Polynomial (Polynomial ℚ) := fun i =>
        Am * deltaTX (Θ.coeff i) - deltaTX Am * Θ.coeff i +
          Polynomial.C (Polynomial.C ((i + 1 : ℕ) : ℚ) * Polynomial.X) *
            (1 - Polynomial.X) * Am * Θ.coeff (i + 1)
      let Ξ : Polynomial (Polynomial (Polynomial ℚ)) :=
        ∑ i ∈ Finset.range (k + 1), Polynomial.C (coeffXi i) * Polynomial.X ^ i
      have hΞ_eval : evalTXDilog Ξ =
          evalTX Am * ((1 - PowerSeries.X) * eulerDeriv (evalTXDilog Θ)) -
            evalTX (deltaTX Am) * evalTXDilog Θ := by
        have htheta : (1 - PowerSeries.X : PowerSeries ℚ) * eulerDeriv (evalTXDilog Θ) =
            ∑ i ∈ Finset.range (k + 2),
              (evalTX (deltaTX (Θ.coeff i)) * dilogSeries ^ i +
                evalTX (Polynomial.C (Polynomial.C (i : ℚ) * Polynomial.X) *
                  (1 - Polynomial.X) * Θ.coeff i) * dilogSeries ^ (i - 1)) := by
          rw [hsum, map_sum, Finset.mul_sum]
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [eulerDeriv_mul, mul_add, ← mul_assoc, ← evalTX_deltaTX, eulerDeriv_pow,
            eulerDeriv_dilogSeries, Algebra.smul_def]
          congr 1
          have hcoef : evalTX (Polynomial.C (Polynomial.C (i : ℚ) * Polynomial.X) *
              (1 - Polynomial.X) * Θ.coeff i) =
              (1 - PowerSeries.X) * (evalTX (Θ.coeff i) *
                ((algebraMap ℚ (PowerSeries ℚ)) (i : ℚ) * logSeries)) := by
            have hc_log : evalTX (Polynomial.C (Polynomial.C (i : ℚ) * Polynomial.X)) =
                (algebraMap ℚ (PowerSeries ℚ)) (i : ℚ) * logSeries := by
              simp [evalTX]
            have hx1 : evalTX (1 - Polynomial.X) = 1 - PowerSeries.X := by
              simp [evalTX]
            rw [map_mul, map_mul, hc_log, hx1]
            ring
          rw [hcoef]
          ring
        have hΞ_sum : evalTXDilog Ξ =
            ∑ i ∈ Finset.range (k + 1), evalTX (coeffXi i) * dilogSeries ^ i := by
          simp only [Ξ, map_sum, map_mul, map_pow]
          refine Finset.sum_congr rfl fun i _ => ?_
          have hc : evalTXDilog (Polynomial.C (coeffXi i)) = evalTX (coeffXi i) := by
            simp [evalTXDilog]
          have hy : evalTXDilog Polynomial.X = dilogSeries := by
            simp [evalTXDilog]
          rw [hc, hy]
        rw [hΞ_sum, htheta, hsum, Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib]
        have hsplit1 : (∑ i ∈ Finset.range (k + 2),
              (evalTX Am * (evalTX (deltaTX (Θ.coeff i)) * dilogSeries ^ i) -
                evalTX (deltaTX Am) * (evalTX (Θ.coeff i) * dilogSeries ^ i))) =
            ∑ i ∈ Finset.range (k + 1),
              evalTX (Am * deltaTX (Θ.coeff i) - deltaTX Am * Θ.coeff i) * dilogSeries ^ i := by
          rw [Finset.sum_range_succ]
          have htop : evalTX Am * (evalTX (deltaTX Am) * dilogSeries ^ (k + 1)) -
              evalTX (deltaTX Am) * (evalTX Am * dilogSeries ^ (k + 1)) = 0 := by ring
          rw [htop, add_zero]
          refine Finset.sum_congr rfl fun i _ => ?_
          simp only [map_sub, map_mul]
          ring
        have hsplit2 : (∑ i ∈ Finset.range (k + 2),
              evalTX Am *
                (evalTX (Polynomial.C (Polynomial.C (i : ℚ) * Polynomial.X) *
                  (1 - Polynomial.X) * Θ.coeff i) * dilogSeries ^ (i - 1))) =
            ∑ i ∈ Finset.range (k + 1),
              evalTX (Polynomial.C (Polynomial.C ((i + 1 : ℕ) : ℚ) * Polynomial.X) *
                (1 - Polynomial.X) * Am * Θ.coeff (i + 1)) * dilogSeries ^ i := by
          rw [Finset.sum_range_succ']
          simp only [CharP.cast_eq_zero, map_zero, zero_mul, mul_zero, add_zero, Nat.add_sub_cancel]
          refine Finset.sum_congr rfl fun i _ => ?_
          simp only [map_mul]
          ring
        have hrhs_split : (∑ i ∈ Finset.range (k + 2),
              (evalTX Am *
                (evalTX (deltaTX (Θ.coeff i)) * dilogSeries ^ i +
                  evalTX (Polynomial.C (Polynomial.C (i : ℚ) * Polynomial.X) *
                    (1 - Polynomial.X) * Θ.coeff i) * dilogSeries ^ (i - 1)) -
                evalTX (deltaTX Am) * (evalTX (Θ.coeff i) * dilogSeries ^ i))) =
            (∑ i ∈ Finset.range (k + 2),
              (evalTX Am * (evalTX (deltaTX (Θ.coeff i)) * dilogSeries ^ i) -
                evalTX (deltaTX Am) * (evalTX (Θ.coeff i) * dilogSeries ^ i))) +
            (∑ i ∈ Finset.range (k + 2),
              evalTX Am *
                (evalTX (Polynomial.C (Polynomial.C (i : ℚ) * Polynomial.X) *
                  (1 - Polynomial.X) * Θ.coeff i) * dilogSeries ^ (i - 1))) := by
          rw [← Finset.sum_add_distrib]
          refine Finset.sum_congr rfl fun i _ => ?_
          ring
        rw [hrhs_split, hsplit1, hsplit2, ← Finset.sum_add_distrib]
        refine Finset.sum_congr rfl fun i _ => ?_
        simp only [coeffXi, map_add]
        ring
      have hΞ0 : evalTXDilog Ξ = 0 := by
        rw [hΞ_eval, hderiv0, hΘ, mul_zero, mul_zero, sub_self]
      have hΞ_deg : Ξ.natDegree ≤ k := by
        refine natDegree_finset_sum_le _ _ k fun i hi => ?_
        have hik : i ≤ k := Nat.lt_succ_iff.mp (Finset.mem_range.mp hi)
        exact le_trans (Polynomial.natDegree_C_mul_X_pow_le (coeffXi i) i) hik
      have hΞ_zero : Ξ = 0 := ih Ξ.natDegree (by omega) Ξ rfl hΞ0
      have hcoeff_k : Ξ.coeff k = 0 := by simp [hΞ_zero]
      have hcoeff_k_eq : Ξ.coeff k = coeffXi k := by
        unfold Ξ
        simp only [Polynomial.finset_sum_coeff, Polynomial.coeff_C_mul_X_pow]
        rw [Finset.sum_eq_single k]
        · simp
        · intro i _ hik
          exact if_neg hik.symm
        · intro hk_abs
          exact False.elim (hk_abs (Finset.mem_range.mpr (Nat.lt_succ_self k)))
      rw [hcoeff_k_eq] at hcoeff_k
      have hwron0 : Am * deltaTX (Θ.coeff k) - deltaTX Am * Θ.coeff k +
          Polynomial.C (Polynomial.C ((k + 1 : ℕ) : ℚ) * Polynomial.X) *
            (1 - Polynomial.X) * Am ^ 2 = 0 := by
        calc Am * deltaTX (Θ.coeff k) - deltaTX Am * Θ.coeff k +
              Polynomial.C (Polynomial.C ((k + 1 : ℕ) : ℚ) * Polynomial.X) *
                (1 - Polynomial.X) * Am ^ 2
            = coeffXi k := by
              dsimp [coeffXi, Am]
              ring
          _ = 0 := hcoeff_k
      exact hAm (no_bivariate_wronskian_dilog (by omega) Am (Θ.coeff k) hwron0)

/-- Ring homomorphism `(ℚ[X])[Y] →+* PowerSeries ℚ` evaluating `Y ↦ dilogSeries`. -/
def evalAtDilog : Polynomial (Polynomial ℚ) →+* PowerSeries ℚ :=
  Polynomial.eval₂RingHom (Polynomial.coeToPowerSeries.ringHom (R := ℚ)) dilogSeries

/-- **MAIN TRANSCENDENCE THEOREM (`dilogSeries_transcendental`):**
The formal dilogarithm jet `dilogSeries = ∑_{k=1}^∞ X^k / k^2 ∈ ℚ[[X]]` is **transcendental of
all degrees** over `ℚ[X]`: every polynomial `Φ ∈ (ℚ[X])[Y]` satisfying `evalAtDilog Φ = 0` is
identically zero. -/
theorem dilogSeries_transcendental (Φ : Polynomial (Polynomial ℚ))
    (hΦ : evalAtDilog Φ = 0) : Φ = 0 := by
  let liftX : Polynomial ℚ →+* Polynomial (Polynomial ℚ) :=
    Polynomial.mapRingHom Polynomial.C
  have hliftX_inj : Function.Injective liftX :=
    Polynomial.map_injective Polynomial.C Polynomial.C_injective
  have heval_lift : ∀ P : Polynomial ℚ, evalTX (liftX P) = (P : PowerSeries ℚ) := by
    intro P
    induction P using Polynomial.induction_on' with
    | add u v ihu ihv => simp [map_add, ihu, ihv]
    | monomial n c =>
      simp only [liftX, evalTX, Polynomial.coe_mapRingHom, Polynomial.map_monomial,
        Polynomial.coe_eval₂RingHom, Polynomial.eval₂_monomial, Polynomial.eval₂_C,
        Polynomial.coe_monomial]
      ext k
      simp [PowerSeries.coeff_C_mul, PowerSeries.coeff_X_pow, PowerSeries.coeff_monomial]
  let Θ : Polynomial (Polynomial (Polynomial ℚ)) := Φ.map liftX
  have hΘ_eval : evalTXDilog Θ = evalAtDilog Φ := by
    unfold evalTXDilog evalAtDilog Θ
    rw [Polynomial.coe_eval₂RingHom, Polynomial.coe_eval₂RingHom, Polynomial.eval₂_map]
    exact Polynomial.eval₂_congr (RingHom.ext heval_lift) rfl rfl
  have hΘ0 : Θ = 0 := logSeries_dilogSeries_alg_independent Θ (hΘ_eval.trans hΦ)
  exact Polynomial.map_injective liftX hliftX_inj (by simpa [Θ] using hΘ0)

/-- **Non-Rationality Corollary (`dilogSeries_not_rational`):**
No non-zero polynomial `Q ∈ ℚ[X]` satisfies `Q(X) * Li_2(X) = P(X)` in `PowerSeries ℚ`. -/
theorem dilogSeries_not_rational (Q P : Polynomial ℚ)
    (h : (Q : PowerSeries ℚ) * dilogSeries = (P : PowerSeries ℚ)) :
    Q = 0 ∧ P = 0 := by
  let Φ : Polynomial (Polynomial ℚ) := Polynomial.C Q * Polynomial.X - Polynomial.C P
  have hΦ : evalAtDilog Φ = 0 := by
    simp only [Φ, map_sub, map_mul]
    have hq : evalAtDilog (Polynomial.C Q) = (Q : PowerSeries ℚ) := by simp [evalAtDilog]
    have hp : evalAtDilog (Polynomial.C P) = (P : PowerSeries ℚ) := by simp [evalAtDilog]
    have hx : evalAtDilog Polynomial.X = dilogSeries := by simp [evalAtDilog]
    rw [hq, hx, hp, h, sub_self]
  have hΦ0 := dilogSeries_transcendental Φ hΦ
  have hQ : Q = 0 := by
    have hc1 := congr_arg (fun T => T.coeff 1) hΦ0
    simpa [Φ] using hc1
  have hP : P = 0 := by
    have hc0 := congr_arg (fun T => T.coeff 0) hΦ0
    simpa [Φ, hQ] using hc0
  exact ⟨hQ, hP⟩

/-- **Non-Quadratic Corollary (`dilogSeries_not_quadratic`):**
No non-trivial quadratic relation `P₂(X) Li_2(X)^2 + P₁(X) Li_2(X) + P₀(X) = 0` holds in `ℚ[[X]]`. -/
theorem dilogSeries_not_quadratic (P₂ P₁ P₀ : Polynomial ℚ)
    (h : (P₂ : PowerSeries ℚ) * dilogSeries ^ 2 +
          (P₁ : PowerSeries ℚ) * dilogSeries + (P₀ : PowerSeries ℚ) = 0) :
    P₂ = 0 ∧ P₁ = 0 ∧ P₀ = 0 := by
  let Φ : Polynomial (Polynomial ℚ) :=
    Polynomial.C P₂ * Polynomial.X ^ 2 + Polynomial.C P₁ * Polynomial.X + Polynomial.C P₀
  have hΦ : evalAtDilog Φ = 0 := by
    simp only [Φ, map_add, map_mul, map_pow]
    have h2' : evalAtDilog (Polynomial.C P₂) = (P₂ : PowerSeries ℚ) := by simp [evalAtDilog]
    have h1' : evalAtDilog (Polynomial.C P₁) = (P₁ : PowerSeries ℚ) := by simp [evalAtDilog]
    have h0' : evalAtDilog (Polynomial.C P₀) = (P₀ : PowerSeries ℚ) := by simp [evalAtDilog]
    have hx : evalAtDilog Polynomial.X = dilogSeries := by simp [evalAtDilog]
    rw [h2', h1', h0', hx, h]
  have hΦ0 := dilogSeries_transcendental Φ hΦ
  have h2 : P₂ = 0 := by
    have hc := congr_arg (fun T => T.coeff 2) hΦ0
    simpa [Φ] using hc
  have h1 : P₁ = 0 := by
    have hc := congr_arg (fun T => T.coeff 1) hΦ0
    simpa [Φ, h2] using hc
  have h0 : P₀ = 0 := by
    have hc := congr_arg (fun T => T.coeff 0) hΦ0
    simpa [Φ, h2, h1] using hc
  exact ⟨h2, h1, h0⟩

end FormalJetTranscendence

/-! ## Part D: Division-Free Liouville Root-Separation & Rational-Approximation Bound (`ℤ` / `ℚ`) -/

section LiouvilleErrorBound

/-- Homogenized integer polynomial numerator `∑_{i=0}^d P_i * p^i * q^(d - i) ∈ ℤ`. -/
def homogEvalInt (P : Polynomial ℤ) (d : ℕ) (p q : ℤ) : ℤ :=
  ∑ i ∈ Finset.range (d + 1), P.coeff i * p ^ i * q ^ (d - i)

/-- Clearing `q^d` in `ℚ` turns `P_ℚ(p / q)` into the exact integer `homogEvalInt P d p q`. -/
theorem q_pow_mul_eval_rat (P : Polynomial ℤ) {d : ℕ} (hd : P.natDegree ≤ d)
    (p : ℤ) {q : ℤ} (hq : q ≠ 0) :
    (q : ℚ) ^ d * Polynomial.eval ((p : ℚ) / (q : ℚ)) (P.map (Int.castRingHom ℚ)) =
      (homogEvalInt P d p q : ℚ) := by
  have hdeg_map : (P.map (Int.castRingHom ℚ)).natDegree ≤ d :=
    le_trans Polynomial.natDegree_map_le hd
  rw [Polynomial.eval_eq_sum_range' (Nat.lt_succ_of_le hdeg_map), Finset.mul_sum]
  unfold homogEvalInt
  push_cast
  refine Finset.sum_congr rfl fun i hi => ?_
  rw [Polynomial.coeff_map]
  simp only [eq_intCast]
  have hid : i ≤ d := Nat.lt_succ_iff.mp (Finset.mem_range.mp hi)
  have hq0 : (q : ℚ) ≠ 0 := Int.cast_ne_zero.mpr hq
  have hpow_split : (q : ℚ) ^ d = (q : ℚ) ^ i * (q : ℚ) ^ (d - i) := by
    rw [← pow_add, Nat.add_sub_of_le hid]
  rw [div_pow, hpow_split]
  have hcancel : (q : ℚ) ^ i * ((p : ℚ) ^ i / (q : ℚ) ^ i) = (p : ℚ) ^ i :=
    mul_div_cancel₀ _ (pow_ne_zero i hq0)
  calc (q : ℚ) ^ i * (q : ℚ) ^ (d - i) * ((P.coeff i : ℚ) * ((p : ℚ) ^ i / (q : ℚ) ^ i))
      = (P.coeff i : ℚ) * ((q : ℚ) ^ i * ((p : ℚ) ^ i / (q : ℚ) ^ i)) * (q : ℚ) ^ (d - i) := by ring
    _ = (P.coeff i : ℚ) * (p : ℚ) ^ i * (q : ℚ) ^ (d - i) := by rw [hcancel]

/-- **Division-free integer Liouville bound:** any non-zero integer homogenized evaluation has
absolute value at least `1`. -/
theorem homogEvalInt_abs_ge_one {P : Polynomial ℤ} {d : ℕ} {p q : ℤ}
    (hne : homogEvalInt P d p q ≠ 0) :
    (1 : ℤ) ≤ |homogEvalInt P d p q| :=
  Int.one_le_abs hne

/-- **Rational Liouville Root-Separation Error Lower Bound (`liouville_eval_rat_lower_bound`):**
For every `P : Polynomial ℤ` of degree `≤ d`, every `p : ℤ`, and every `q > 0`, if `p / q` is
not a root of `P`, then `1 / q^d ≤ |P_ℚ(p / q)|`. -/
theorem liouville_eval_rat_lower_bound (P : Polynomial ℤ) {d : ℕ} (hd : P.natDegree ≤ d)
    (p : ℤ) {q : ℤ} (hq : 0 < q)
    (hne : Polynomial.eval ((p : ℚ) / (q : ℚ)) (P.map (Int.castRingHom ℚ)) ≠ 0) :
    1 / (q : ℚ) ^ d ≤ |Polynomial.eval ((p : ℚ) / (q : ℚ)) (P.map (Int.castRingHom ℚ))| := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq_pos : (0 : ℚ) < (q : ℚ) := Int.cast_pos.mpr hq
  have hqd_pos : (0 : ℚ) < (q : ℚ) ^ d := pow_pos hq_pos d
  have hhom_ne : homogEvalInt P d p q ≠ 0 := by
    intro h0
    have heq := q_pow_mul_eval_rat P hd p hq0
    rw [h0, Int.cast_zero] at heq
    exact hne ((mul_eq_zero.mp heq).resolve_left (ne_of_gt hqd_pos))
  have habs_int : (1 : ℚ) ≤ |(homogEvalInt P d p q : ℚ)| := by
    rw [← Int.cast_abs]
    exact_mod_cast homogEvalInt_abs_ge_one hhom_ne
  have habs_eq : (q : ℚ) ^ d *
      |Polynomial.eval ((p : ℚ) / (q : ℚ)) (P.map (Int.castRingHom ℚ))| =
      |(homogEvalInt P d p q : ℚ)| := by
    rw [← abs_of_pos hqd_pos, ← abs_mul, q_pow_mul_eval_rat P hd p hq0]
  rw [div_le_iff₀ hqd_pos, mul_comm]
  linarith

/-- **Contrapositive Transcendence / Irrationality Obstruction Criterion:**
No rational `p / q` (`q > 0`) can achieve `0 < |P_ℚ(p / q)| < 1 / q^d` for an integer polynomial
`P` of degree `≤ d`. -/
theorem liouville_no_subthreshold_nonzero_eval (P : Polynomial ℤ) {d : ℕ} (hd : P.natDegree ≤ d)
    (p : ℤ) {q : ℤ} (hq : 0 < q)
    (hpos : 0 < |Polynomial.eval ((p : ℚ) / (q : ℚ)) (P.map (Int.castRingHom ℚ))|)
    (hlt : |Polynomial.eval ((p : ℚ) / (q : ℚ)) (P.map (Int.castRingHom ℚ))| < 1 / (q : ℚ) ^ d) :
    False := by
  have hne : Polynomial.eval ((p : ℚ) / (q : ℚ)) (P.map (Int.castRingHom ℚ)) ≠ 0 :=
    abs_pos.mp hpos
  have hge := liouville_eval_rat_lower_bound P hd p hq hne
  linarith

end LiouvilleErrorBound

end FigureEightPachnerAndJetTranscendence
end QOU.BraidsAndKnots
