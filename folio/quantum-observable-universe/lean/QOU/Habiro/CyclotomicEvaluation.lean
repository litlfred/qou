import Mathlib.Tactic
import Mathlib.RingTheory.RootsOfUnity.Basic
import QOU.Common.CyclotomicValueTruncates

/-!
# Habiro cyclotomic evaluation — truncation, well-definedness, non-vanishing

Infrastructure for the Habiro ring `ℤ[q]^ = lim_← ℤ[q]/((q;q)_n)` at the level
actually needed by `def:qou-motivic-galois-instance` (bean `qou-lwyo`): the
evaluation of a cyclotomic series `Σ_m a_m (q;q)_m` at a root of unity.

`QOU.Common.qPochDiag` and `cyclotomic_value_truncates` already existed and are
reused; this file supplies the three things they did not have.

## 1. The bridge from roots of unity

`cyclotomic_value_truncates` assumes `(ζ;ζ)_N = 0` as a *hypothesis*.
`qPochDiag_eq_zero_of_pow_eq_one` **derives** it from `ζ^N = 1`: the `k = N`
factor is `1 - ζ^N = 0`. That is the actual Habiro mechanism, and without it the
truncation lemma cannot be applied to a root of unity without assuming its own
conclusion.

## 2. Well-definedness of the evaluation

`habiroEval_stable` — past the order of `ζ`, truncating further changes nothing.
This is what makes `ev_ζ` well defined on the inverse limit: a coherent sequence
has one value regardless of the level it is read at. `habiroEval_add` gives
additivity.

**Multiplicativity is NOT proved here.** The Habiro product in cyclotomic
coordinates is not termwise, so `ev_ζ` being a *ring* hom is a larger build. What
this file establishes is a well-defined additive evaluation, which is what the
`frobenius_at` construction consumes. Do not cite it as a ring hom.

## 3. Non-vanishing, and why the obvious criterion is useless here

`habiroEval_ne_zero_of_head_not_dvd`: if the `j`-term head is not divisible by
`(ζ;ζ)_j`, the whole evaluation is non-zero — **for every `N ≥ j`**, so this is a
genuine "for all p" criterion rather than a per-prime check.

The natural instance is `j = 1`, giving *"`(1-ζ) ∤ a₀ ⇒ ev ≠ 0"*
(`habiroEval_ne_zero_of_head_not_dvd_one`). **At the primes this framework needs,
that is vacuous.** The norm of `1 - ζ_n` is `Φ_n(1)`, which is `1` unless `n` is a
prime power. For `n = 2p` with `p` odd, `2p` is not a prime power, so `1 - ζ_{2p}`
is a **unit** and divides everything. Computed:

    p        2     3     5     7    11    13
    n = 2p   4     6    10    14    22    26
    Φ_n(1)   2     1     1     1     1     1
             ok  unit  unit  unit  unit  unit

So `j = 1` covers `p = 2` and nothing else. `head_criterion_vacuous_of_isUnit`
states that failure mode as a theorem rather than a comment.

The escape is `j = 2`: `(ζ;ζ)_2 = (1-ζ)(1-ζ²)`, and for a primitive `2p`-th root
`ζ²` is a primitive `p`-th root, so `1 - ζ²` has norm `Φ_p(1) = p` — a non-unit.
The `j`-general form above is stated precisely so this instance is available.

**What remains open for `qou-lwyo`.** This file reduces "non-vanishing at every
prime" to a concrete arithmetic condition on the *head* of the atomic Markov
trace's Habiro expansion. Whether that head satisfies it is not settled here, and
no instance is provided. That is a sharper open question than the one it
replaces, not a closed one.

**Base ring (§7c).** Generic `[CommRing R]` throughout — no ordering, no `ℝ`.
The cyclotomic specialisation only needs `IsPrimitiveRoot`.

Ref: [habiro2002]
Ref: [leitner2026] def:qou-motivic-galois-instance
Ref: [leitner2026] def:motivic-galois-character
-/

open Finset
namespace QOU.Habiro
open QOU.Common
variable {R : Type*} [CommRing R]

theorem qPochDiag_eq_zero_of_pow_eq_one (u : R) {N : ℕ} (hN : 0 < N) (hu : u ^ N = 1) :
    qPochDiag u N = 0 := by
  unfold qPochDiag
  apply Finset.prod_eq_zero (i := N - 1)
  · rw [Finset.mem_range]; omega
  · have h : N - 1 + 1 = N := by omega
    rw [h, hu, sub_self]

theorem qPochDiag_dvd_of_le (u : R) {j m : ℕ} (h : j ≤ m) :
    qPochDiag u j ∣ qPochDiag u m := by
  unfold qPochDiag
  have hsub : Finset.range j ⊆ Finset.range m := by
    intro x hx; rw [Finset.mem_range] at hx ⊢; omega
  exact Finset.prod_dvd_prod_of_subset _ _ _ hsub

noncomputable def habiroEval (a : ℕ → R) (ζ : R) (N : ℕ) : R :=
  ∑ m ∈ Finset.range N, a m * qPochDiag ζ m

theorem habiroEval_add (a b : ℕ → R) (ζ : R) (N : ℕ) :
    habiroEval (a + b) ζ N = habiroEval a ζ N + habiroEval b ζ N := by
  unfold habiroEval
  rw [← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl (fun k _ => by simp [add_mul])

/-- **Well-definedness.** Past the order of `ζ`, truncating further changes nothing. -/
theorem habiroEval_stable (a : ℕ → R) {ζ : R} {N : ℕ} (hN : 0 < N) (hζ : ζ ^ N = 1)
    {M : ℕ} (hM : N ≤ M) : habiroEval a ζ M = habiroEval a ζ N := by
  unfold habiroEval
  have hsub : Finset.range N ⊆ Finset.range M := by
    intro x hx; rw [Finset.mem_range] at hx ⊢; omega
  rw [← Finset.sum_sdiff hsub]
  have hz : (∑ k ∈ Finset.range M \ Finset.range N, a k * qPochDiag ζ k) = 0 := by
    apply Finset.sum_eq_zero
    intro k hk
    rw [Finset.mem_sdiff, Finset.mem_range, Finset.mem_range, not_lt] at hk
    rw [qPochDiag_eq_zero_of_ge ζ (qPochDiag_eq_zero_of_pow_eq_one ζ hN hζ) hk.2, mul_zero]
  rw [hz, zero_add]

theorem habiroEval_sub_head (a : ℕ → R) (ζ : R) {j N : ℕ} (h : j ≤ N) :
    qPochDiag ζ j ∣ (habiroEval a ζ N - habiroEval a ζ j) := by
  unfold habiroEval
  have hsub : Finset.range j ⊆ Finset.range N := by
    intro x hx; rw [Finset.mem_range] at hx ⊢; omega
  rw [← Finset.sum_sdiff hsub, add_sub_cancel_right]
  apply Finset.dvd_sum
  intro k hk
  rw [Finset.mem_sdiff, Finset.mem_range, Finset.mem_range, not_lt] at hk
  exact Dvd.dvd.mul_left (qPochDiag_dvd_of_le ζ hk.2) _

/-- **Non-vanishing criterion (j-term head).** -/
theorem habiroEval_ne_zero_of_head_not_dvd (a : ℕ → R) (ζ : R) {j N : ℕ} (h : j ≤ N)
    (hhead : ¬ (qPochDiag ζ j ∣ habiroEval a ζ j)) : habiroEval a ζ N ≠ 0 := by
  intro hzero
  apply hhead
  have hd := habiroEval_sub_head a ζ h
  rw [hzero, zero_sub] at hd
  exact (dvd_neg.mp hd)

theorem habiroEval_one (a : ℕ → R) (ζ : R) : habiroEval a ζ 1 = a 0 := by
  unfold habiroEval qPochDiag; simp

/-- j = 1 specialisation. **Vacuous whenever `1 - ζ` is a unit** — in particular
    at every primitive `2p`-th root for odd prime `p`, where `Φ_{2p}(1) = 1`. -/
theorem habiroEval_ne_zero_of_head_not_dvd_one (a : ℕ → R) (ζ : R) {N : ℕ} (h : 1 ≤ N)
    (hhead : ¬ ((1 - ζ) ∣ a 0)) : habiroEval a ζ N ≠ 0 := by
  apply habiroEval_ne_zero_of_head_not_dvd a ζ h
  rw [habiroEval_one]
  have : qPochDiag ζ 1 = 1 - ζ := by unfold qPochDiag; simp
  rw [this]; exact hhead

theorem habiroEval_two (a : ℕ → R) (ζ : R) :
    habiroEval a ζ 2 = a 0 + a 1 * (1 - ζ) := by
  unfold habiroEval qPochDiag
  simp [Finset.sum_range_succ]

theorem qPochDiag_two (ζ : R) : qPochDiag ζ 2 = (1 - ζ) * (1 - ζ ^ 2) := by
  unfold qPochDiag
  simp [Finset.prod_range_succ]

/-- **j = 2 specialisation — the index that is actually usable at `ζ_{2p}`.**

    `habiroEval_ne_zero_of_head_not_dvd_one` is vacuous at every odd prime,
    because `Norm(1 - ζ_n) = Φ_n(1) = 1` unless `n` is a prime power, so
    `1 - ζ_{2p}` is a **unit** there and `head_criterion_vacuous_of_isUnit`
    applies. At `j = 2` the divisor picks up the second factor `1 - ζ² = 1 - ζ_p`,
    whose norm is `Φ_p(1) = p`; that is a non-unit at every prime, so this form of
    the criterion has content everywhere.

    Concretely, in `ℤ[ζ_{2p}] = ℤ[ζ_p]` with `𝔭 = (1 - ζ_p)` the unique prime above
    `p` and residue field `𝔽_p` (in which `ζ_{2p} ≡ -1`), the hypothesis reduces to
    the single integer condition `a₀(-1) + 2·a₁(-1) ≢ 0 (mod p)` — one integer per
    series, deciding non-vanishing at **every** odd prime outside its finite set of
    divisors, with no dependence on how far the coefficients are known. -/
theorem habiroEval_ne_zero_of_head_not_dvd_two (a : ℕ → R) (ζ : R) {N : ℕ} (h : 2 ≤ N)
    (hhead : ¬ ((1 - ζ) * (1 - ζ ^ 2) ∣ a 0 + a 1 * (1 - ζ))) :
    habiroEval a ζ N ≠ 0 := by
  apply habiroEval_ne_zero_of_head_not_dvd a ζ h
  rw [habiroEval_two, qPochDiag_two]
  exact hhead

theorem habiroEval_three (a : ℕ → R) (ζ : R) :
    habiroEval a ζ 3 = a 0 + a 1 * (1 - ζ) + a 2 * ((1 - ζ) * (1 - ζ ^ 2)) := by
  unfold habiroEval qPochDiag
  simp [Finset.sum_range_succ, Finset.prod_range_succ]

theorem qPochDiag_three (ζ : R) :
    qPochDiag ζ 3 = (1 - ζ) * (1 - ζ ^ 2) * (1 - ζ ^ 3) := by
  unfold qPochDiag
  simp [Finset.prod_range_succ]

/-- **j = 3 specialisation — what is needed when `j = 2` is silent.**

    The `j = 2` criterion is silent exactly when `p` divides the integer
    `A = a₀(-1) + 2·a₁(-1)` (see `habiroEval_ne_zero_of_head_not_dvd_two`).
    Measured on this corpus, the only odd prime that ever divides `A` is `3`,
    and it does so exactly for the mixed atoms; at `j = 3` the divisor picks up
    the further factor `1 - ζ³`, and the criterion fires there for every one of
    them. Silence at one index says nothing about the value — it says the test
    at that index cannot see it. -/
theorem habiroEval_ne_zero_of_head_not_dvd_three (a : ℕ → R) (ζ : R) {N : ℕ}
    (h : 3 ≤ N)
    (hhead : ¬ ((1 - ζ) * (1 - ζ ^ 2) * (1 - ζ ^ 3) ∣
        a 0 + a 1 * (1 - ζ) + a 2 * ((1 - ζ) * (1 - ζ ^ 2)))) :
    habiroEval a ζ N ≠ 0 := by
  apply habiroEval_ne_zero_of_head_not_dvd a ζ h
  rw [habiroEval_three, qPochDiag_three]
  exact hhead

/-! ### The prime 2: four explicit terms, so no criterion is needed

At a primitive fourth root the Pochhammer collapses to constants and the whole
evaluation is four terms. Non-vanishing at `p = 2` is therefore decided by
*evaluating*, not by a divisibility criterion — which matters because the
criterion provably cannot decide it: `qPochDiag ζ 4 = 0` caps the divisor, so
`habiroEval_ne_zero_of_head_not_dvd` has only `j = 1, 2, 3` to work with. -/

theorem qPochDiag_two_of_sq_eq_neg_one (ζ : R) (hζ : ζ ^ 2 = -1) :
    qPochDiag ζ 2 = 2 * (1 - ζ) := by
  rw [qPochDiag_two, hζ]; ring

theorem qPochDiag_three_of_sq_eq_neg_one (ζ : R) (hζ : ζ ^ 2 = -1) :
    qPochDiag ζ 3 = 4 := by
  rw [qPochDiag_three, hζ]
  have h3 : ζ ^ 3 = -ζ := by
    have : ζ ^ 3 = ζ ^ 2 * ζ := by ring
    rw [this, hζ]; ring
  rw [h3]
  have : (1 - ζ) * (1 - -1) * (1 - -ζ) = 2 * ((1 - ζ) * (1 + ζ)) := by ring
  rw [this]
  have : (1 - ζ) * (1 + ζ) = 1 - ζ ^ 2 := by ring
  rw [this, hζ]; ring

theorem qPochDiag_four_of_sq_eq_neg_one (ζ : R) (hζ : ζ ^ 2 = -1) :
    qPochDiag ζ 4 = 0 := by
  have h4 : ζ ^ 4 = 1 := by
    have : ζ ^ 4 = (ζ ^ 2) ^ 2 := by ring
    rw [this, hζ]; ring
  unfold qPochDiag
  rw [Finset.prod_range_succ]
  simp [h4]

/-- **Evaluation at a primitive fourth root is four explicit terms.**

    `2` and `4` here are the collapsed Pochhammers `(ζ;ζ)_2 = 2(1-ζ)` and
    `(ζ;ζ)_3 = 4`; `(ζ;ζ)_4 = 0` truncates everything beyond. So at this root
    the value depends on `a 0 … a 3` alone, however long the series is. -/
theorem habiroEval_at_sq_eq_neg_one (a : ℕ → R) (ζ : R) (hζ : ζ ^ 2 = -1)
    {N : ℕ} (hN : 4 ≤ N) :
    habiroEval a ζ N
      = a 0 + a 1 * (1 - ζ) + a 2 * (2 * (1 - ζ)) + a 3 * 4 := by
  have h4 : ζ ^ 4 = 1 := by
    have : ζ ^ 4 = (ζ ^ 2) ^ 2 := by ring
    rw [this, hζ]; ring
  rw [habiroEval_stable a (by norm_num : 0 < 4) h4 hN]
  unfold habiroEval
  rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_succ,
    Finset.sum_range_succ, Finset.sum_range_zero]
  rw [qPochDiag_two_of_sq_eq_neg_one ζ hζ, qPochDiag_three_of_sq_eq_neg_one ζ hζ]
  have h0 : qPochDiag ζ 0 = 1 := by unfold qPochDiag; simp
  have h1 : qPochDiag ζ 1 = 1 - ζ := by unfold qPochDiag; simp
  rw [h0, h1]; ring

/-- A unit head-divisor makes the criterion unusable — stated so the failure mode
    is a theorem, not a footnote. -/
theorem head_criterion_vacuous_of_isUnit (a : ℕ → R) (ζ : R) {j : ℕ}
    (hu : IsUnit (qPochDiag ζ j)) : qPochDiag ζ j ∣ habiroEval a ζ j :=
  hu.dvd

/-! ### Cyclotomic specialisation: evaluation at a primitive `2p`-th root -/

section Cyclotomic
variable {A : Type*} [CommRing A]

/-- Evaluation at a primitive `2p`-th root truncates at `2p`: the concrete
    `ev_ζ : ℤ[q]^ → ℤ[ζ_{2p}]` well-definedness statement. -/
theorem habiroEval_at_primitiveRoot (a : ℕ → A) {ζ : A} {n : ℕ} (hn : 0 < n)
    (hζ : IsPrimitiveRoot ζ n) {M : ℕ} (hM : n ≤ M) :
    habiroEval a ζ M = habiroEval a ζ n :=
  habiroEval_stable a hn hζ.pow_eq_one hM

/-- The `2p` form used by `def:qou-motivic-galois-instance`. -/
theorem habiroEval_at_two_mul (a : ℕ → A) {ζ : A} {p : ℕ} (hp : 0 < p)
    (hζ : IsPrimitiveRoot ζ (2 * p)) {M : ℕ} (hM : 2 * p ≤ M) :
    habiroEval a ζ M = habiroEval a ζ (2 * p) :=
  habiroEval_at_primitiveRoot a (by omega) hζ hM

/-- Non-vanishing at **every** prime, from one head condition. -/
theorem habiroEval_ne_zero_at_two_mul (a : ℕ → A) {ζ : A} {p j : ℕ}
    (hj : j ≤ 2 * p) (hhead : ¬ (qPochDiag ζ j ∣ habiroEval a ζ j)) :
    habiroEval a ζ (2 * p) ≠ 0 :=
  habiroEval_ne_zero_of_head_not_dvd a ζ hj hhead

end Cyclotomic

end QOU.Habiro
