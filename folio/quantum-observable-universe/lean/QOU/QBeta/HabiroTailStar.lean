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

This file pins the algebra and **proves (★) at every order `n`,
sorry-free** (bean qou-rk84): the Gaussian binomial by the Pascal
recurrence with its vanishing and dual-Pascal lemmas, the
**bar-inversion lemma** `[n,k]_q = q^{k(n−k)}·[n,k]_{q⁻¹}` (the
mathematical heart of (★): it is what collapses the quadratic
exponents), the **squared-Pochhammer inversion**
`(q;q)_n² = q^{n(n+1)}·(q⁻¹;q⁻¹)_n²` (the prefactor's half of the same
collapse — squaring clears the `(−1)ⁿ` and the half-exponent), the
Masbaum coefficient, and the general-`n` theorem.

Proof shape: bar-inversion turns each summand's `a`-exponent
`3n²+5n+k²−2k−3nk−k(n−k)` into `3n²+5n−2k−2nk`; the overall
`a^{−(5n²+7n)}` then leaves `−2(n+1)(n+k)`, i.e. exactly
`(a²)^{−n(n+1)}·((a²)^{−1})^{k(n+1)}` — linear in `k`, with the
`(a²)^{−n(n+1)}` absorbed by the Pochhammer inversion. So the compute
that verified (★) machine-exactly for n ≤ 32 is now discharged as a
theorem for all n.

## Base ring (§7c)

No archimedean construct appears anywhere: the whole file is pre-wall.
It is split at the weakest typeclass each part actually needs, following
the convention already used by `QOU.QBeta.QCasoratianBarParity` and
`QOU.QBeta.LevelMapValuation` in this same directory:

* **`section BaseRing` — generic `CommRing R`, division-free.** The
  Gaussian binomial, its Pascal recurrences, the Pochhammer, and *both
  bar-inversion lemmas* live here. Bar-inversion needs only that `q` has
  an inverse, which is carried as the **paired witness** `hq : q * qi = 1`
  (the R[h] pattern) rather than as a field division — so the identities
  hold verbatim over `ℤ[q, q⁻¹]`, which is where these coefficients
  actually live. This is the mathematical heart of (★).
* **`section FieldCompat` — `Field R`, `a ≠ 0`.** Only `masbaumC` and
  `star` sit here, and only because the Masbaum coefficient carries
  **negative integer powers** `a ^ (z : ℤ)` of a ring element, which need
  a `GroupWithZero`/`Field` (or `a : Rˣ`) to be `zpow`. The two literal
  `q⁻¹` bar-inversion lemmas are re-derived here from the division-free
  ones for downstream convenience (`HabiroTailCorollaries`,
  `LevelMapValuation` consume these signatures unchanged).
-/
import Mathlib.Tactic

namespace QOU.QBeta.HabiroTailStar

open Finset

section BaseRing

variable {R : Type*} [CommRing R]

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

/-- **Bar-inversion** (the heart of (★)), division-free over a generic
`CommRing`: whenever `qi` is a two-sided inverse of `q` (`hq : q * qi = 1`),
`[n,k]_q = q^{k(n−k)}·[n,k]_{qi}`, unconditional (both sides vanish for
`k > n`). This is the lemma that collapses the quadratic exponents of the
Masbaum transform, and it needs no field — only the unit witness, so it
holds verbatim over `ℤ[q, q⁻¹]`. The literal `q⁻¹` form is
`gaussBinom_inv` below. -/
lemma gaussBinom_inv' (q qi : R) (hq : q * qi = 1) : ∀ n k : ℕ,
    gaussBinom q n k = q ^ (k * (n - k)) * gaussBinom qi n k := by
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
      have h5 := gaussBinom_succ_succ' qi n k
      have hik := ih k
      have hik1 := ih (k + 1)
      rw [e2]
      rcases Nat.lt_or_ge k n with hlt | hge
      · -- k < n: rewrite n−k = (n−(k+1))+1 so a single subtraction atom
        -- remains, then close with the q·qi = 1 power identity
        have e3 : n - k = (n - (k + 1)) + 1 := by omega
        rw [e3] at h5 hik ⊢
        have hu : q ^ ((n - (k + 1)) + 1) * qi ^ ((n - (k + 1)) + 1)
            = 1 := by
          rw [← mul_pow, hq, one_pow]
        linear_combination h4 - q ^ ((k + 1) * ((n - (k + 1)) + 1)) * h5
          + hik + q ^ (k + 1) * hik1
          - q ^ (k * ((n - (k + 1)) + 1)) * gaussBinom qi n k * hu
      · -- k ≥ n: the (k+1)-column terms vanish on both sides
        have hzq : gaussBinom q n (k + 1) = 0 :=
          gaussBinom_eq_zero_of_lt q (Nat.lt_succ_of_le hge)
        have hzi : gaussBinom qi n (k + 1) = 0 :=
          gaussBinom_eq_zero_of_lt qi (Nat.lt_succ_of_le hge)
        have hu0 : q ^ (n - k) * qi ^ (n - k) = 1 := by
          rw [← mul_pow, hq, one_pow]
        linear_combination h4 - q ^ ((k + 1) * (n - k)) * h5
          + hik - q ^ (k * (n - k)) * gaussBinom qi n k * hu0
          + q ^ (k + 1) * hzq - q ^ ((k + 1) * (n - k)) * hzi

/-- `(q;q)_n = ∏_{j=1..n} (1 − q^j)`. -/
def qPoch (q : R) (n : ℕ) : R := ∏ j ∈ range n, (1 - q ^ (j + 1))

/-- **Bar-inversion of the squared Pochhammer**, division-free:
`(q;q)_n² = q^{n(n+1)}·(qi;qi)_n²` whenever `q * qi = 1`. (The unsquared
form carries a `(−1)ⁿ` and the half-exponent `n(n+1)/2`; squaring clears
both, and the square is what (★) needs.) The literal `q⁻¹` form is
`qPoch_sq_inv` below. -/
lemma qPoch_sq_inv' (q qi : R) (hq : q * qi = 1) : ∀ n : ℕ,
    qPoch q n ^ 2 = q ^ (n * (n + 1)) * qPoch qi n ^ 2 := by
  intro n
  induction n with
  | zero => simp [qPoch]
  | succ n ih =>
    have hu : q ^ (n + 1) * qi ^ (n + 1) = 1 := by
      rw [← mul_pow, hq, one_pow]
    have hp : qPoch q (n + 1) = qPoch q n * (1 - q ^ (n + 1)) := by
      simp only [qPoch, Finset.prod_range_succ]
    have hpi : qPoch qi (n + 1) = qPoch qi n * (1 - qi ^ (n + 1)) := by
      simp only [qPoch, Finset.prod_range_succ]
    have hsq : (1 - q ^ (n + 1)) ^ 2
        = (q ^ (n + 1)) ^ 2 * (1 - qi ^ (n + 1)) ^ 2 := by
      linear_combination
        (2 * q ^ (n + 1) - q ^ (n + 1) * qi ^ (n + 1) - 1) * hu
    have he : (n + 1) * (n + 1 + 1) = n * (n + 1) + 2 * (n + 1) := by ring
    rw [hp, hpi, mul_pow, mul_pow, ih, he, hsq]
    ring

end BaseRing

section FieldCompat

variable {R : Type*} [Field R]

/-- Literal-`q⁻¹` form of `gaussBinom_inv'`, for `q ≠ 0` in a field. The
mathematical content is the division-free lemma; this is the shape the
Masbaum transform and the downstream corollaries consume. -/
lemma gaussBinom_inv (q : R) (hq : q ≠ 0) : ∀ n k : ℕ,
    gaussBinom q n k = q ^ (k * (n - k)) * gaussBinom q⁻¹ n k :=
  gaussBinom_inv' q q⁻¹ (mul_inv_cancel₀ hq)

/-- Literal-`q⁻¹` form of `qPoch_sq_inv'`, for `q ≠ 0` in a field. -/
lemma qPoch_sq_inv (q : R) (hq : q ≠ 0) : ∀ n : ℕ,
    qPoch q n ^ 2 = q ^ (n * (n + 1)) * qPoch q⁻¹ n ^ 2 :=
  qPoch_sq_inv' q q⁻¹ (mul_inv_cancel₀ hq)

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
  have ha2 : (a ^ 2 : R) ≠ 0 := pow_ne_zero _ ha
  -- `(a²)^m` and `((a²)⁻¹)^m` as `zpow`s of `a`
  have hpos : ∀ m : ℕ, ((a ^ 2 : R)) ^ m = a ^ (2 * (m : ℤ)) := by
    intro m
    rw [show (2 * (m : ℤ)) = ((2 * m : ℕ) : ℤ) by push_cast; ring,
        zpow_natCast, pow_mul]
  have hinv : ∀ m : ℕ, ((a ^ 2 : R)⁻¹) ^ m = a ^ (-(2 * (m : ℤ))) := by
    intro m
    rw [inv_pow, hpos m, ← zpow_neg]
  -- exponent-collecting shapes (the base is nonzero, so `zpow` adds)
  have e1 : ∀ (x y z : ℤ) (g : R),
      a ^ x * (a ^ y * g) * a ^ z = a ^ (x + y + z) * g := by
    intro x y z g
    rw [zpow_add₀ ha, zpow_add₀ ha]
    ring
  have e2 : ∀ (x y : ℤ) (g : R), a ^ x * (a ^ y * g) = a ^ (x + y) * g := by
    intro x y g
    rw [zpow_add₀ ha]
    ring
  -- the Pochhammer prefactor, inverted
  have hP := qPoch_sq_inv (a ^ 2) ha2 n
  -- the prefactor cancellation `(a²)^{n(n+1)} · a^{−2n(n+1)} = 1`
  have hcancel : (a ^ 2 : R) ^ (n * (n + 1))
      * a ^ (-(2 * ((n : ℤ) * ((n : ℤ) + 1)))) = 1 := by
    rw [hpos (n * (n + 1)), ← zpow_add₀ ha]
    have hz : (2 * ((n * (n + 1) : ℕ) : ℤ))
        + (-(2 * ((n : ℤ) * ((n : ℤ) + 1)))) = 0 := by
      push_cast
      ring
    rw [hz, zpow_zero]
  -- the sum-level identity: bar-inversion collapses every term, and the
  -- surviving `a`-exponent is `−2(n+1)(n+k)` — linear in `k` after the
  -- quadratic parts cancel.
  have hsum : masbaumC a n * a ^ (-(5 * (n : ℤ) ^ 2 + 7 * n))
      = (-1) ^ n * (a ^ (-(2 * ((n : ℤ) * ((n : ℤ) + 1))))
          * ∑ k ∈ range (n + 1),
              ((a ^ 2)⁻¹) ^ (k * (n + 1)) * gaussBinom (a ^ 2)⁻¹ n k) := by
    rw [masbaumC, mul_assoc]
    congr 1
    rw [Finset.sum_mul, Finset.mul_sum]
    refine Finset.sum_congr rfl ?_
    intro k hk
    have hkn : k ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
    have hcast : ((n - k : ℕ) : ℤ) = (n : ℤ) - (k : ℤ) := Nat.cast_sub hkn
    rw [gaussBinom_inv (a ^ 2) ha2 n k, hpos (k * (n - k)),
        hinv (k * (n + 1)), e1, e2]
    congr 1
    push_cast [hcast]
    ring
  -- Ref: [leitner2026] computations/qbeta-habiro-tail-util.witness.json
  -- (machine-exact n ≤ 32) + qbeta-5two-gbar-pole-ladder.witness.json
  -- (1e-497, n ≤ 64) — the compute this proof now discharges.
  linear_combination (masbaumC a n * a ^ (-(5 * (n : ℤ) ^ 2 + 7 * n))) * hP
    + ((a ^ 2 : R) ^ (n * (n + 1)) * qPoch (a ^ 2)⁻¹ n ^ 2) * hsum
    + ((-1 : R) ^ n * qPoch (a ^ 2)⁻¹ n ^ 2
        * ∑ k ∈ range (n + 1),
            ((a ^ 2)⁻¹) ^ (k * (n + 1)) * gaussBinom (a ^ 2)⁻¹ n k) * hcancel

/-- (★) at `n = 0`: both sides are `1`. -/
example (a : R) :
    masbaumC a 0 * qPoch (a ^ 2) 0 ^ 2 * a ^ (-(5 * (0 : ℤ) ^ 2 + 7 * 0))
      = (-1) ^ 0 * qPoch (a ^ 2)⁻¹ 0 ^ 2
          * ∑ k ∈ range 1,
              ((a ^ 2)⁻¹) ^ (k * 1) * gaussBinom (a ^ 2)⁻¹ 0 k := by
  simp [masbaumC, qPoch, gaussBinom]

end FieldCompat

end QOU.QBeta.HabiroTailStar
