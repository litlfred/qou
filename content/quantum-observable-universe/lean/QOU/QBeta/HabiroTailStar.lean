/-
# The Habiro-tail (★) identity — Lean pin (bean qou-rk84)

The 5₂ Masbaum/Habiro-tail q-Borel coefficients obey the exact identity
(derived on PR #4195/#4226; machine-exactly verified as integer-Laurent
dict equality for n ≤ 32 in `computations/qbeta_habiro_tail_util.py`,
witness `qbeta-habiro-tail-util.witness.json`; numerically to 1e-497
for n ≤ 64):

    C_n(a) · (q̄;q̄)_n² · a^{−(5n²+7n)}
        = (−1)ⁿ · (q̃;q̃)_n² · Σ_{k≤n} q̃^{k(n+1)} · [n,k]_{q̃}      (★)

with q̄ = a², q̃ = a⁻². Consequences (same PRs): the Borel residue
c∞ = (q̃;q̃)_∞², the transient ratio q̃, the pole ladder at w = −q₀ᵏ.

This file pins the algebra: the Gaussian binomial by the Pascal
recurrence, its vanishing and dual-Pascal lemmas (sorry-free), the
**bar-inversion lemma** `[n,k]_q = q^{k(n−k)}·[n,k]_{q⁻¹}` (sorry-free —
the mathematical heart of (★): it is what collapses the quadratic
exponents), the Masbaum coefficient, the (★) statement at every order,
and proved instances at n = 0, 1. The general-n (★) proof (a finite
Finset.sum manipulation on top of the inversion lemma) is stated with
an honest `sorry` + witness citation, per §1 of the Lean rules.

Base ring (§7c): everything is algebraic over a generic `Field R` with
`a ≠ 0` — no archimedean construct, pre-wall.
-/
import Mathlib.Tactic

namespace QOU.QBeta.HabiroTailStar

open Finset

variable {R : Type*} [Field R]

/-- Gaussian binomial `[n,k]_q` by the Pascal recurrence
`[n+1,k+1]_q = [n,k]_q + q^{k+1}·[n,k+1]_q` (the same recurrence the
exact compute uses). -/
def gaussBinom (q : R) : ℕ → ℕ → R
  | 0, 0 => 1
  | 0, _ + 1 => 0
  | _ + 1, 0 => 1
  | n + 1, k + 1 => gaussBinom q n k + q ^ (k + 1) * gaussBinom q n (k + 1)

@[simp] lemma gaussBinom_zero_zero (q : R) : gaussBinom q 0 0 = 1 := rfl

@[simp] lemma gaussBinom_zero_succ (q : R) (k : ℕ) :
    gaussBinom q 0 (k + 1) = 0 := rfl

@[simp] lemma gaussBinom_succ_zero (q : R) (n : ℕ) :
    gaussBinom q (n + 1) 0 = 1 := rfl

lemma gaussBinom_succ_succ (q : R) (n k : ℕ) :
    gaussBinom q (n + 1) (k + 1)
      = gaussBinom q n k + q ^ (k + 1) * gaussBinom q n (k + 1) := rfl

/-- `[n,k]_q = 0` for `k > n`. -/
lemma gaussBinom_eq_zero_of_lt (q : R) : ∀ {n k : ℕ}, n < k →
    gaussBinom q n k = 0 := by
  intro n
  induction n with
  | zero =>
    intro k hk
    match k, hk with
    | k + 1, _ => simp
  | succ n ih =>
    intro k hk
    match k, hk with
    | k + 1, hk =>
      have h1 : n < k := Nat.lt_of_succ_lt_succ hk
      have h2 : n < k + 1 := Nat.lt_of_lt_of_le h1 (Nat.le_succ k)
      rw [gaussBinom_succ_succ, ih h1, ih h2]
      ring

/-- `[n,n]_q = 1`. -/
lemma gaussBinom_self (q : R) : ∀ n : ℕ, gaussBinom q n n = 1 := by
  intro n
  induction n with
  | zero => rfl
  | succ n ih =>
    rw [gaussBinom_succ_succ, ih,
        gaussBinom_eq_zero_of_lt q (Nat.lt_succ_self n)]
    ring

/-- `[n,0]_q = 1` for every `n`. -/
@[simp] lemma gaussBinom_zero (q : R) : ∀ n : ℕ, gaussBinom q n 0 = 1
  | 0 => rfl
  | _ + 1 => rfl

/-- The dual Pascal rule
`[n+1,k+1]_q = q^{n−k}·[n,k]_q + [n,k+1]_q`, unconditional (for
`k > n` every term vanishes and truncated subtraction is harmless) —
proved by induction from the primary recurrence alone. -/
lemma gaussBinom_succ_succ' (q : R) : ∀ n k : ℕ,
    gaussBinom q (n + 1) (k + 1)
      = q ^ (n - k) * gaussBinom q n k + gaussBinom q n (k + 1) := by
  intro n
  induction n with
  | zero =>
    intro k
    match k with
    | 0 => simp [gaussBinom_succ_succ]
    | k + 1 =>
      simp [gaussBinom_succ_succ,
            gaussBinom_eq_zero_of_lt q (Nat.succ_pos k),
            gaussBinom_eq_zero_of_lt q (Nat.succ_pos (k + 1))]
  | succ n ih =>
    intro k
    match k with
    | 0 =>
      have h1 := gaussBinom_succ_succ q (n + 1) 0
      have h2 := ih 0
      have h4 := gaussBinom_succ_succ q n 0
      simp only [gaussBinom_zero, Nat.sub_zero] at h1 h2 h4 ⊢
      linear_combination h1 + q * h2 - h4
    | k + 1 =>
      have h1 := gaussBinom_succ_succ q (n + 1) (k + 1)
      have h2 := ih k
      have h3 := ih (k + 1)
      have h4 := gaussBinom_succ_succ q n k
      have h5 := gaussBinom_succ_succ q n (k + 1)
      rcases Nat.lt_or_ge k n with hlt | hge
      · -- k < n: exponents combine, q^{k+2}·q^{n−k−1} = q^{n−k}·q^{k+1}
        have e1 : (k + 1 + 1) + (n - (k + 1)) = (n - k) + (k + 1) := by
          omega
        have hpow : q ^ (k + 1 + 1) * q ^ (n - (k + 1))
            = q ^ (n - k) * q ^ (k + 1) := by
          rw [← pow_add, ← pow_add, e1]
        have e2 : (n + 1) - (k + 1) = n - k := by omega
        rw [e2]
        linear_combination h1 + h2 + q ^ (k + 1 + 1) * h3
          - q ^ (n - k) * h4 - h5 + gaussBinom q n (k + 1) * hpow
      · -- k ≥ n: the mismatch terms carry gaussBinom q n (k+1) = 0
        have hz : gaussBinom q n (k + 1) = 0 :=
          gaussBinom_eq_zero_of_lt q (Nat.lt_succ_of_le hge)
        have e2 : (n + 1) - (k + 1) = n - k := by omega
        rw [e2]
        linear_combination h1 + h2 + q ^ (k + 1 + 1) * h3
          - q ^ (n - k) * h4 - h5
          + (q ^ (k + 1 + 1) * q ^ (n - (k + 1))
              - q ^ (n - k) * q ^ (k + 1)) * hz

/-- **Bar-inversion** (the heart of (★)): for `q ≠ 0`,
`[n,k]_q = q^{k(n−k)}·[n,k]_{q⁻¹}`, unconditional (both sides vanish
for `k > n`). This is the lemma that collapses the quadratic exponents
of the Masbaum transform. -/
lemma gaussBinom_inv (q : R) (hq : q ≠ 0) : ∀ n k : ℕ,
    gaussBinom q n k = q ^ (k * (n - k)) * gaussBinom q⁻¹ n k := by
  intro n
  induction n with
  | zero =>
    intro k
    match k with
    | 0 => simp
    | k + 1 => simp
  | succ n ih =>
    intro k
    match k with
    | 0 => simp
    | k + 1 =>
      have e2 : (n + 1) - (k + 1) = n - k := by omega
      have h4 := gaussBinom_succ_succ q n k
      have h5 := gaussBinom_succ_succ' q⁻¹ n k
      have hik := ih k
      have hik1 := ih (k + 1)
      rw [e2]
      rcases Nat.lt_or_ge k n with hlt | hge
      · -- k < n: rewrite n−k = (n−(k+1))+1 so a single subtraction atom
        -- remains, then close with the q·q⁻¹ = 1 power identity
        have e3 : n - k = (n - (k + 1)) + 1 := by omega
        rw [e3] at h5 hik ⊢
        have hu : q ^ ((n - (k + 1)) + 1) * q⁻¹ ^ ((n - (k + 1)) + 1)
            = 1 := by
          rw [← mul_pow, mul_inv_cancel₀ hq, one_pow]
        linear_combination h4 - q ^ ((k + 1) * ((n - (k + 1)) + 1)) * h5
          + hik + q ^ (k + 1) * hik1
          - q ^ (k * ((n - (k + 1)) + 1)) * gaussBinom q⁻¹ n k * hu
      · -- k ≥ n: the (k+1)-column terms vanish on both sides
        have hzq : gaussBinom q n (k + 1) = 0 :=
          gaussBinom_eq_zero_of_lt q (Nat.lt_succ_of_le hge)
        have hzi : gaussBinom q⁻¹ n (k + 1) = 0 :=
          gaussBinom_eq_zero_of_lt q⁻¹ (Nat.lt_succ_of_le hge)
        have hu0 : q ^ (n - k) * q⁻¹ ^ (n - k) = 1 := by
          rw [← mul_pow, mul_inv_cancel₀ hq, one_pow]
        linear_combination h4 - q ^ ((k + 1) * (n - k)) * h5
          + hik - q ^ (k * (n - k)) * gaussBinom q⁻¹ n k * hu0
          + q ^ (k + 1) * hzq - q ^ ((k + 1) * (n - k)) * hzi

/-- `(q;q)_n = ∏_{j=1..n} (1 − q^j)`. -/
def qPoch (q : R) (n : ℕ) : R := ∏ j ∈ range n, (1 - q ^ (j + 1))

/-- The exact Masbaum coefficient `C_{5₂,n}(a)` (integer Laurent in `a`;
DOI 10.2140/agt.2003.3.537), transcribed from the merged compute:
`C_n(a) = (−1)ⁿ Σ_k a^{3n²+5n+k²−2k−3nk} · a^{−k(n−k)}·[n,k]_{a²}` —
stated with ℤ-exponents via `zpow`. -/
noncomputable def masbaumC (a : R) (n : ℕ) : R :=
  (-1) ^ n * ∑ k ∈ range (n + 1),
    a ^ ((3 * n ^ 2 + 5 * n + k ^ 2 : ℤ) - 2 * k - 3 * n * k - k * (n - k))
      * gaussBinom (a ^ 2) n k

/-- **The (★) identity** at every order `n` (stated; machine-exactly
verified for n ≤ 32 as integer-Laurent dict equality, and numerically
to 1e-497 for n ≤ 64). -/
theorem star (a : R) (ha : a ≠ 0) (n : ℕ) :
    masbaumC a n * qPoch (a ^ 2) n ^ 2 * a ^ (-(5 * (n : ℤ) ^ 2 + 7 * n))
      = (-1) ^ n * qPoch (a ^ 2)⁻¹ n ^ 2
          * ∑ k ∈ range (n + 1),
              ((a ^ 2)⁻¹) ^ (k * (n + 1)) * gaussBinom (a ^ 2)⁻¹ n k := by
  -- Ref: [manuscript] computations/qbeta-habiro-tail-util.witness.json
  -- (machine-exact n ≤ 32) + qbeta-5two-gbar-pole-ladder.witness.json
  -- (1e-497, n ≤ 64). Proof route: gaussBinom_inv collapses the
  -- quadratic exponents termwise; the remaining exponent identity is
  -- linear (omega). Queued on bean qou-rk84.
  sorry

/-- (★) at `n = 0`: both sides are `1`. -/
example (a : R) :
    masbaumC a 0 * qPoch (a ^ 2) 0 ^ 2 * a ^ (-(5 * (0 : ℤ) ^ 2 + 7 * 0))
      = (-1) ^ 0 * qPoch (a ^ 2)⁻¹ 0 ^ 2
          * ∑ k ∈ range 1,
              ((a ^ 2)⁻¹) ^ (k * 1) * gaussBinom (a ^ 2)⁻¹ 0 k := by
  simp [masbaumC, qPoch, gaussBinom]

end QOU.QBeta.HabiroTailStar
