import QCalculus.HabiroColoredJones
import BraidKnotOctonion.AJTrefoilAnnihilation

/-!
# QCalculus.HabiroTrefoil — the trefoil's cyclotomic expansion at every colour

The corpus defines the coloured Jones tower of the (left-handed) trefoil as the
Rosso–Jones twist-eigenvalue sum `QOU.BraidKnot.AJTrefoil.coloredJonesTrefoil`
(closure of `σ₁³ ∈ B₂`, at `w = q^{1/4}`), and proves that it is annihilated by
an order-1 inhomogeneous `q`-difference operator
(`QOU.BraidKnot.AJTrefoil.trefoilOperator_annihilates`, sorry-free).

This file proves that the same tower is Habiro's cyclotomic polynomial
`∑_{n<N} q^{-n(n+2)} (q^{1+N};q)_n (q^{1-N};q)_n`, for every colour `N ≥ 1`,
whenever `q = w⁴` is not a root of unity. The coefficients
`C_n = q^{-n(n+2)}` are therefore the trefoil's cyclotomic coefficients.

## Method (a creative-telescoping certificate)

Write `x = q^N` and `t_N(n)` for the `n`-th summand. With
`G(n) = q(q x⁻² − x⁻⁴) · q^{-n²} · ∏_{k<n}(1 − x q^{k+1}) · ∏_{k<n}(1 − q^k/x)`,
each summand satisfies the first-order identity
`a₀ t_N(n) + a₁ t_{N+1}(n) = G(n+1) − G(n)`,
where `a₀, a₁` are the operator's coefficients. Summing over `n ≤ N` telescopes
to `−G(0)`, which is the operator's right-hand side, because `G(N+1)` contains
the factor `1 − q^N/x = 0`. So the Habiro tower satisfies the same recurrence;
both towers equal `1` at `N = 1`, and the leading coefficient `a₁` does not
vanish when `q` is not a root of unity, so the towers agree at every colour.

## Base ring (§7c)

Generic `{K : Type*} [Field K]`. No `ℝ`, no ordering, no analytic input.
-/

namespace QCalculus.HabiroTrefoil

open Finset QOU.BraidKnot.AJTrefoil QOU.BraidKnot.AJFigureEight

variable {K : Type*} [Field K]

/-- `∏_{k<n} (1 − x q^{k+1})`, the factor `(q^{1+N};q)_n` at `x = q^N`. -/
def prodA (q x : K) (n : ℕ) : K := ∏ k ∈ range n, (1 - x * q ^ (k + 1))

/-- `∏_{k<n} (1 − x q^{k+2})`, the factor `(q^{2+N};q)_n` at `x = q^N`. -/
def prodA' (q x : K) (n : ℕ) : K := ∏ k ∈ range n, (1 - x * q ^ (k + 2))

/-- `∏_{k<n} (1 − q^{k+1}/x)`, the factor `(q^{1-N};q)_n` at `x = q^N`. -/
def prodC (q x : K) (n : ℕ) : K := ∏ k ∈ range n, (1 - q ^ (k + 1) / x)

/-- `∏_{k<n} (1 − q^k/x)`, the factor `(q^{-N};q)_n` at `x = q^N`. -/
def prodD (q x : K) (n : ℕ) : K := ∏ k ∈ range n, (1 - q ^ k / x)

/-- The trefoil's cyclotomic coefficient `C_n = q^{-n(n+2)}`. -/
def trefoilCoeff (q : K) (n : ℕ) : K := q⁻¹ ^ (n * (n + 2))

/-- Summand at colour `N` (`x = q^N`). -/
def term0 (q x : K) (n : ℕ) : K := trefoilCoeff q n * prodA q x n * prodC q x n

/-- Summand at colour `N + 1`, still written with `x = q^N`. -/
def term1 (q x : K) (n : ℕ) : K := trefoilCoeff q n * prodA' q x n * prodD q x n

/-- The telescoping certificate. -/
def cert (q x : K) (n : ℕ) : K :=
  q * (q / x ^ 2 - 1 / x ^ 4) * q⁻¹ ^ (n * n) * prodA q x n * prodD q x n

theorem prodA_succ (q x : K) (n : ℕ) :
    prodA q x (n + 1) = prodA q x n * (1 - x * q ^ (n + 1)) := prod_range_succ _ _

theorem prodA_succ' (q x : K) (n : ℕ) :
    prodA q x (n + 1) = prodA' q x n * (1 - x * q) := by
  rw [prodA, prod_range_succ', prodA']
  simp only [zero_add, pow_one]

theorem prodD_succ (q x : K) (n : ℕ) :
    prodD q x (n + 1) = prodD q x n * (1 - q ^ n / x) := prod_range_succ _ _

theorem prodD_succ' (q x : K) (n : ℕ) :
    prodD q x (n + 1) = prodC q x n * (1 - 1 / x) := by
  rw [prodD, prod_range_succ', prodC]
  simp

/-- **The per-summand certificate identity.** -/
theorem term_cert {q x : K} (hq : q ≠ 0) (hx : x ≠ 0) (hx1 : x ≠ 1) (hxq : x * q ≠ 1)
    (n : ℕ) :
    trCoeff 0 q x * term0 q x n + trCoeff 1 q x * term1 q x n
      = cert q x (n + 1) - cert q x n := by
  have hA' : prodA' q x n = prodA q x n * (1 - x * q ^ (n + 1)) / (1 - x * q) := by
    have h := (prodA_succ' q x n).symm.trans (prodA_succ q x n)
    have hne : (1 - x * q) ≠ 0 := sub_ne_zero.mpr (Ne.symm hxq)
    field_simp
    linear_combination h
  have hC : prodC q x n = prodD q x n * (x - q ^ n) / (x - 1) := by
    have h := (prodD_succ' q x n).symm.trans (prodD_succ q x n)
    have hne : x - 1 ≠ 0 := sub_ne_zero.mpr hx1
    rw [eq_div_iff hne]
    field_simp at h
    linear_combination h
  have hE1 : q⁻¹ ^ ((n + 1) * (n + 1)) = q⁻¹ ^ (n * n) * (q ^ n)⁻¹ * (q ^ n)⁻¹ * q⁻¹ := by
    rw [← inv_pow, show (n + 1) * (n + 1) = n * n + n + n + 1 by ring, pow_add, pow_add,
      pow_add, pow_one]
  have hE2 : q⁻¹ ^ (n * (n + 2)) = q⁻¹ ^ (n * n) * (q ^ n)⁻¹ * (q ^ n)⁻¹ := by
    rw [← inv_pow, show n * (n + 2) = n * n + n + n by ring, pow_add, pow_add]
  have hz : q ^ n ≠ 0 := pow_ne_zero _ hq
  have h1x : x - 1 ≠ 0 := sub_ne_zero.mpr hx1
  have h1xq : (1 - x * q) ≠ 0 := sub_ne_zero.mpr (Ne.symm hxq)
  rw [term0, term1, cert, cert, trefoilCoeff, prodA_succ, prodD_succ, hA', hC, hE1, hE2,
    pow_succ q n]
  simp only [trCoeff]
  generalize q ^ n = z at hz ⊢
  generalize q⁻¹ ^ (n * n) = E
  generalize prodA q x n = P
  generalize prodD q x n = D
  field_simp
  ring

theorem cert_zero (q x : K) : cert q x 0 = q * (q / x ^ 2 - 1 / x ^ 4) := by
  simp [cert, prodA, prodD]

theorem cert_top {q : K} (hq : q ≠ 0) (N : ℕ) : cert q (q ^ N) (N + 1) = 0 := by
  rw [cert, prodD, prod_range_succ, div_self (pow_ne_zero _ hq), sub_self]
  ring

/-- **The Habiro sums satisfy the trefoil recurrence** (`x = q^N`). -/
theorem sum_recurrence {q : K} (hq : q ≠ 0) {N : ℕ} (hx1 : q ^ N ≠ 1)
    (hxq : q ^ N * q ≠ 1) :
    trCoeff 0 q (q ^ N) * ∑ n ∈ range (N + 1), term0 q (q ^ N) n
      + trCoeff 1 q (q ^ N) * ∑ n ∈ range (N + 1), term1 q (q ^ N) n
      = trRhs q (q ^ N) := by
  have hx : q ^ N ≠ 0 := pow_ne_zero _ hq
  rw [mul_sum, mul_sum, ← sum_add_distrib]
  rw [sum_congr rfl fun n _ => term_cert hq hx hx1 hxq n, sum_range_sub, cert_top hq,
    cert_zero, trRhs]
  field_simp
  ring

open QCalculus.HabiroSeries in
/-- The Habiro tower at colour `N ≥ 1` is the sum of the `term0` summands. -/
theorem coloredJonesAt_eq_sum0 {q : K} (hq : q ≠ 0) {N : ℕ} (hN : 1 ≤ N) :
    coloredJonesAt q q⁻¹ (trefoilCoeff q) N = ∑ n ∈ range (N + 1), term0 q (q ^ N) n := by
  have hx : q ^ N ≠ 0 := pow_ne_zero _ hq
  rw [sum_range_succ]
  have htop : term0 q (q ^ N) N = 0 := by
    rw [term0, prodC]
    obtain ⟨M, rfl⟩ : ∃ M, N = M + 1 := ⟨N - 1, by omega⟩
    rw [prod_range_succ, div_self hx, sub_self, mul_zero, mul_zero]
  rw [htop, add_zero, coloredJonesAt]
  refine sum_congr rfl fun n hn => ?_
  have hnN := mem_range.mp hn
  rw [term0, prodA, prodC, mul_assoc, mul_assoc]
  congr 2
  · refine prod_congr rfl fun k _ => ?_
    rw [show N + 1 + k = N + (k + 1) by ring, pow_add]
  · refine prod_congr rfl fun k hk => ?_
    have hkn := mem_range.mp hk
    congr 1
    have hsplit : q ^ N = q ^ (N - 1 - k) * q ^ (k + 1) := by
      rw [← pow_add]; congr 1; omega
    rw [inv_pow, eq_div_iff hx, hsplit, inv_mul_cancel_left₀ (pow_ne_zero _ hq)]

open QCalculus.HabiroSeries in
/-- The Habiro tower at colour `N + 1` is the sum of the `term1` summands. -/
theorem coloredJonesAt_succ_eq_sum1 {q : K} (hq : q ≠ 0) (N : ℕ) :
    coloredJonesAt q q⁻¹ (trefoilCoeff q) (N + 1)
      = ∑ n ∈ range (N + 1), term1 q (q ^ N) n := by
  have hx : q ^ N ≠ 0 := pow_ne_zero _ hq
  rw [coloredJonesAt]
  refine sum_congr rfl fun n hn => ?_
  have hnN := mem_range.mp hn
  rw [term1, prodA', prodD, mul_assoc, mul_assoc]
  congr 2
  · refine prod_congr rfl fun k _ => ?_
    rw [show N + 1 + 1 + k = N + (k + 2) by ring, pow_add]
  · refine prod_congr rfl fun k hk => ?_
    have hkn := mem_range.mp hk
    congr 1
    have hsplit : q ^ N = q ^ (N + 1 - 1 - k) * q ^ k := by
      rw [← pow_add]; congr 1; omega
    rw [inv_pow, eq_div_iff hx, hsplit, inv_mul_cancel_left₀ (pow_ne_zero _ hq)]

open QCalculus.HabiroSeries in
/-- **The Habiro trefoil tower satisfies the trefoil recurrence** at every colour
    `N ≥ 1` where `q^N ≠ 1` and `q^{N+1} ≠ 1`. -/
theorem habiro_recurrence {q : K} (hq : q ≠ 0) {N : ℕ} (hN : 1 ≤ N) (hx1 : q ^ N ≠ 1)
    (hxq : q ^ (N + 1) ≠ 1) :
    trCoeff 0 q (q ^ N) * coloredJonesAt q q⁻¹ (trefoilCoeff q) N
      + trCoeff 1 q (q ^ N) * coloredJonesAt q q⁻¹ (trefoilCoeff q) (N + 1)
      = trRhs q (q ^ N) := by
  rw [coloredJonesAt_eq_sum0 hq hN, coloredJonesAt_succ_eq_sum1 hq]
  exact sum_recurrence hq hx1 (by rwa [← pow_succ])

/-- `J_1 = 1` for the Rosso–Jones tower, once `w⁴ ≠ 1`. -/
theorem coloredJonesTrefoil_one {w : K} (hw : w ≠ 0) (h4 : w ^ 4 ≠ 1) :
    coloredJonesTrefoil w 1 = 1 := by
  have hv : w ^ 2 - (w ^ 2)⁻¹ ≠ 0 := by
    intro h
    apply h4
    have hw2 : w ^ 2 ≠ 0 := pow_ne_zero _ hw
    have : w ^ 2 * w ^ 2 = 1 := by
      have := congrArg (· * w ^ 2) (sub_eq_zero.mp h)
      simp only [inv_mul_cancel₀ hw2] at this
      exact this
    rw [← this]; ring
  have hq1 : qInt (w ^ 2) 1 = 1 := by
    rw [qInt, pow_one]; exact div_self hv
  simp [coloredJonesTrefoil, twistEigenvalue, hq1]

open QCalculus.HabiroSeries in
/-- **The trefoil's cyclotomic expansion at every colour.** When `q = w⁴` is not a
    root of unity, the Rosso–Jones tower of the trefoil equals Habiro's cyclotomic
    polynomial `∑_{n<N} q^{-n(n+2)} (q^{1+N};q)_n (q^{1-N};q)_n` for every `N ≥ 1`. -/
theorem coloredJonesTrefoil_eq_coloredJonesAt {w : K} (hw : w ≠ 0)
    (hroot : ∀ k : ℕ, 0 < k → (w ^ 4) ^ k ≠ 1) {N : ℕ} (hN : 1 ≤ N) :
    coloredJonesTrefoil w N = coloredJonesAt (w ^ 4) (w ^ 4)⁻¹ (trefoilCoeff (w ^ 4)) N := by
  have hq : w ^ 4 ≠ 0 := pow_ne_zero _ hw
  induction N, hN using Nat.le_induction with
  | base =>
    rw [coloredJonesTrefoil_one hw (by simpa using hroot 1 one_pos)]
    simp [coloredJonesAt, trefoilCoeff]
  | succ N hN ih =>
    have hJ := trefoilOperator_annihilates hw N
    simp only [trefoilOperator, sum_range_succ, sum_range_zero, zero_add] at hJ
    change trCoeff 0 (w ^ 4) ((w ^ 4) ^ N) * coloredJonesTrefoil w N
      + trCoeff 1 (w ^ 4) ((w ^ 4) ^ N) * coloredJonesTrefoil w (N + 1)
      = trRhs (w ^ 4) ((w ^ 4) ^ N) at hJ
    have hH := habiro_recurrence hq hN (hroot N (by omega)) (hroot (N + 1) (by omega))
    rw [ih] at hJ
    have ha1 : trCoeff 1 (w ^ 4) ((w ^ 4) ^ N) ≠ 0 := by
      have hx : (w ^ 4) ^ N ≠ 0 := pow_ne_zero _ hq
      have hxq : (w ^ 4) ^ N * w ^ 4 - 1 ≠ 0 := by
        rw [sub_ne_zero, ← pow_succ]; exact hroot (N + 1) (by omega)
      simp only [trCoeff]
      exact div_ne_zero (neg_ne_zero.mpr (mul_ne_zero hq hxq)) (pow_ne_zero _ hx)
    exact mul_left_cancel₀ ha1 (by linear_combination hJ - hH)

section HabiroElement

open QCalculus.HabiroSeries Polynomial

variable {R : Type*} [CommRing R]

/-- The trefoil's cyclotomic coefficients in the Habiro ring, `C_n = q^{-n(n+2)}`. -/
noncomputable def trefoilCoeffHabiro (n : ℕ) : Habiro R := qInv ^ (n * (n + 2))

/-- The trefoil's Kashaev element `∑_n q^{-n(n+2)} (q;q)_n²` in the Habiro ring. -/
noncomputable def trefoilKashaev : Habiro R := kashaevElement trefoilCoeffHabiro

set_option synthInstance.maxHeartbeats 200000 in
/-- At a root of unity of order `N`, the colour-`N` Habiro trefoil polynomial takes the
    value of the single element `trefoilKashaev`. -/
theorem evalRoot_trefoil_coloredJones {S : Type*} [CommRing S] [Algebra R S] {N : ℕ}
    (hN : N ≠ 0) {ζ : S} (hζ : aeval ζ (cyclotomic N R) = 0) :
    evalRoot hN ζ hζ (coloredJones trefoilCoeffHabiro N)
      = evalRoot hN ζ hζ (trefoilKashaev (R := R)) :=
  evalRoot_coloredJones hN hζ _

end HabiroElement

end QCalculus.HabiroTrefoil
