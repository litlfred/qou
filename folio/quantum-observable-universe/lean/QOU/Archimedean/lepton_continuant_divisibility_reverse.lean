import Mathlib.Tactic
import QOU.Archimedean.lepton_continuant_recurrence

/-!
# QOU.Archimedean.lepton_continuant_divisibility_reverse — reverse continuant divisibility

**Proposition** ([`prop:lepton-continuant-recurrence`](../../../quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md)).

*Let `b_n = morganVoyceB n` be the Morgan–Voyce continuant over
`Polynomial ℤ` (`b_0 = 0`, `b_1 = 1`, `b_{n+2} = X·b_{n+1} + b_n`),
i.e. the Fibonacci-polynomial sequence with indeterminate `X` playing
the Hecke parameter `h = q − q⁻¹`.  Then for every `a ≥ 1`,*

```
  b_a ∣ b_n  →  a ∣ n .
```

Together with the forward law `a ∣ n → b_a ∣ b_n`
(`morganVoyceB_dvd_of_dvd`, re-proved locally here), this establishes
the **strong-divisibility equivalence** `b_a ∣ b_n ⟺ a ∣ n`
(`morganVoyceB_dvd_iff`) — the polynomial Fibonacci divisibility law,
closing the mathematical half of the three-generation continuant
residual.

## Route

The `Polynomial ℤ` gcd-monoid infrastructure is thin, so we avoid the
`gcd(b_m, b_n) = b_{gcd(m,n)}` identity and argue by a direct
mod-reduction + degree bound:

1. **Addition law** `b_{m+n+1} = b_{m+1} b_{n+1} + b_m b_n`
   (`morganVoyceB_add`, re-proved locally: the sibling forward-law
   branch is not on `main`).
2. **Consecutive coprimality** `IsCoprime b_n b_{n+1}`
   (`morganVoyceB_coprime_succ`), from which
   `IsCoprime b_a b_{a·q+1}` (since `b_a ∣ b_{a·q}`).
3. **Mod reduction**: writing `n = a·q + r`, the addition law +
   coprime cancellation give `b_a ∣ b_n → b_a ∣ b_r`.
4. **Degree bound**: `b_k` is monic with `natDegree = k − 1` for
   `k ≥ 1` (`morganVoyceB_monic_natDegree`).  For `0 < r < a`,
   `b_r ≠ 0` and `natDegree b_r = r − 1 < a − 1 = natDegree b_a`, so
   `b_a ∣ b_r` (with `b_r ≠ 0`) forces `natDegree b_a ≤ natDegree b_r`
   (`natDegree_le_of_dvd`) — a contradiction.  Hence `r = 0`, i.e.
   `a ∣ n`.

Kept over generic `Polynomial ℤ` (§7c: no archimedean specialisation
required — this is pure `q`-deformation combinatorics).

-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
-/

namespace QOU.Archimedean

open Polynomial

/-! ### Addition law and forward strong divisibility (local re-proofs)

These two results also live on the sibling branch
`claude/electroweak-even-tower-2026-08-02` (file
`QOU/ParticleInteractions/even_tower_continuant_harmonics.lean`).
They are re-proved here so this file is self-contained when branched
off `main`, where that sibling is not yet merged. -/

/-- **Addition law** for the Morgan–Voyce continuant:
    `b_{m+n+1} = b_{m+1} b_{n+1} + b_m b_n`.

    The polynomial Fibonacci addition identity, specialised to
    `b_1 = 1`, `b_2 = X`.  Two-step induction on `m` from
    `morganVoyceB_recurrence`. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
theorem morganVoyceB_add (m n : ℕ) :
    morganVoyceB (m + n + 1)
      = morganVoyceB (m + 1) * morganVoyceB (n + 1)
        + morganVoyceB m * morganVoyceB n := by
  induction m using Nat.twoStepInduction with
  | zero =>
      simp only [Nat.zero_add, morganVoyceB, one_mul, zero_mul, add_zero]
  | one =>
      rw [show 1 + n + 1 = n + 2 from by omega, morganVoyceB_recurrence]
      simp only [morganVoyceB]
      ring
  | more m ih1 ih2 =>
      rw [show m + 2 + n + 1 = (m + n + 1) + 2 from by omega,
          morganVoyceB_recurrence,
          show (m + n + 1) + 1 = (m + 1) + n + 1 from by omega,
          ih2, ih1,
          show m + 2 + 1 = (m + 1) + 2 from by omega,
          morganVoyceB_recurrence (m + 1),
          show (m + 1) + 1 = m + 2 from by omega,
          morganVoyceB_recurrence m]
      ring

/-- `b_n ∣ b_{n·k}`: the continuant of every multiple winding is
    divisible by that of the base winding.  Induction on `k` from the
    addition law. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
theorem morganVoyceB_dvd_mul (n k : ℕ) : morganVoyceB n ∣ morganVoyceB (n * k) := by
  induction k with
  | zero => simp [morganVoyceB]
  | succ k ih =>
      rcases Nat.eq_zero_or_pos n with hn | hn
      · subst hn; simp [morganVoyceB]
      · obtain ⟨n', rfl⟩ : ∃ n', n = n' + 1 := ⟨n - 1, by omega⟩
        have hidx : (n' + 1) * (k + 1) = ((n' + 1) * k) + n' + 1 := by ring
        rw [hidx, morganVoyceB_add]
        exact dvd_add (dvd_mul_left _ _) (ih.mul_right _)

/-- **Forward strong divisibility**: `a ∣ n → b_a ∣ b_n`. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
theorem morganVoyceB_dvd_of_dvd {a n : ℕ} (h : a ∣ n) :
    morganVoyceB a ∣ morganVoyceB n := by
  obtain ⟨k, rfl⟩ := h
  exact morganVoyceB_dvd_mul a k

/-! ### Consecutive coprimality -/

/-- **Consecutive continuants are coprime**: `IsCoprime b_n b_{n+1}`.

    Induction on `n`.  Base `IsCoprime b_0 b_1 = IsCoprime 0 1`; step
    `b_{n+2} = X·b_{n+1} + b_n`, so coprimality with `b_{n+1}` is
    inherited from `IsCoprime b_{n+1} b_n` by adding a multiple of
    `b_{n+1}` (`IsCoprime.add_mul_right_right`). -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
theorem morganVoyceB_coprime_succ (n : ℕ) :
    IsCoprime (morganVoyceB n) (morganVoyceB (n + 1)) := by
  induction n with
  | zero =>
      have h : IsCoprime (morganVoyceB 0) (morganVoyceB 1) := by
        simpa [morganVoyceB] using
          (isCoprime_one_right : IsCoprime (0 : Polynomial ℤ) 1)
      exact h
  | succ k ih =>
      have hrec : morganVoyceB (k + 1 + 1)
          = Polynomial.X * morganVoyceB (k + 1) + morganVoyceB k :=
        morganVoyceB_recurrence k
      have hc : IsCoprime (morganVoyceB (k + 1)) (morganVoyceB k) := ih.symm
      -- goal (after hrec): IsCoprime b_{k+1} (X·b_{k+1} + b_k); commute the
      -- polynomial sum (target the specific summands, not the ℕ index k+1).
      rw [hrec, add_comm (Polynomial.X * morganVoyceB (k + 1)) (morganVoyceB k)]
      exact hc.add_mul_right_right Polynomial.X

/-! ### Monicity and degree -/

/-- `b_{n+1}` is **monic** with `natDegree = n`.  Joint two-step
    induction; the sum `X·b_{n+1} + b_n` has its leading term supplied
    by the strictly-higher-degree first summand. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
theorem morganVoyceB_monic_natDegree (n : ℕ) :
    (morganVoyceB (n + 1)).Monic ∧ (morganVoyceB (n + 1)).natDegree = n := by
  induction n using Nat.twoStepInduction with
  | zero =>
      exact ⟨monic_one, natDegree_one⟩
  | one =>
      have h2 : morganVoyceB (1 + 1) = X := by simp [morganVoyceB]
      rw [h2]
      exact ⟨monic_X, natDegree_X⟩
  | more m ih1 ih2 =>
      obtain ⟨_, hm1_deg⟩ := ih1
      obtain ⟨hm2_monic, hm2_deg⟩ := ih2
      have hrec : morganVoyceB (m + 2 + 1)
          = X * morganVoyceB (m + 1 + 1) + morganVoyceB (m + 1) :=
        morganVoyceB_recurrence (m + 1)
      have hp_monic : (X * morganVoyceB (m + 1 + 1)).Monic := monic_X.mul hm2_monic
      have hp_deg : (X * morganVoyceB (m + 1 + 1)).natDegree = m + 2 := by
        rw [Monic.natDegree_mul monic_X hm2_monic, natDegree_X, hm2_deg]
        omega
      have hlt : (morganVoyceB (m + 1)).natDegree
          < (X * morganVoyceB (m + 1 + 1)).natDegree := by
        rw [hp_deg, hm1_deg]; omega
      refine ⟨?_, ?_⟩
      · rw [hrec]; exact hp_monic.add_of_left (degree_lt_degree hlt)
      · rw [hrec, natDegree_add_eq_left_of_natDegree_lt hlt, hp_deg]

/-! ### Reverse divisibility and the equivalence -/

/-- **Reverse strong divisibility of the Morgan–Voyce continuant.**
    For `a ≥ 1`, `b_a ∣ b_n → a ∣ n`.

    Mod-reduction: with `r = n % a`, if `r ≥ 1` then the addition law +
    coprime cancellation give `b_a ∣ b_r`, contradicting the strict
    degree bound `natDegree b_r = r − 1 < a − 1 = natDegree b_a`.  Hence
    `r = 0`, i.e. `a ∣ n`. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
theorem morganVoyceB_dvd_reverse {a n : ℕ} (ha : 1 ≤ a)
    (hdvd : morganVoyceB a ∣ morganVoyceB n) : a ∣ n := by
  rcases Nat.eq_zero_or_pos (n % a) with hr0 | hrpos
  · exact Nat.dvd_of_mod_eq_zero hr0
  · exfalso
    have hr_lt : n % a < a := Nat.mod_lt n ha
    obtain ⟨s, hrs⟩ : ∃ s, n % a = s + 1 := ⟨n % a - 1, by omega⟩
    obtain ⟨a', ha'⟩ : ∃ a', a = a' + 1 := ⟨a - 1, by omega⟩
    -- name the quotient so the index rewrite below does not recurse into `n / a`
    obtain ⟨Q, hQ⟩ : ∃ Q, n / a = Q := ⟨n / a, rfl⟩
    have hdm : a * Q + n % a = n := by have := Nat.div_add_mod n a; rwa [hQ] at this
    have hn_idx : n = a * Q + s + 1 := by omega
    -- addition law at n = (a·Q) + s + 1
    have hsum : morganVoyceB n
        = morganVoyceB (a * Q + 1) * morganVoyceB (s + 1)
          + morganVoyceB (a * Q) * morganVoyceB s := by
      rw [hn_idx]; exact morganVoyceB_add (a * Q) s
    have hdQ : morganVoyceB a ∣ morganVoyceB (a * Q) := morganVoyceB_dvd_mul a Q
    have hT2 : morganVoyceB a ∣ morganVoyceB (a * Q) * morganVoyceB s := hdQ.mul_right _
    have hsumdvd : morganVoyceB a ∣
        morganVoyceB (a * Q + 1) * morganVoyceB (s + 1)
          + morganVoyceB (a * Q) * morganVoyceB s := by
      rw [← hsum]; exact hdvd
    have hT1 : morganVoyceB a ∣ morganVoyceB (a * Q + 1) * morganVoyceB (s + 1) :=
      (dvd_add_left hT2).mp hsumdvd
    have hcop : IsCoprime (morganVoyceB a) (morganVoyceB (a * Q + 1)) :=
      (morganVoyceB_coprime_succ (a * Q)).of_isCoprime_of_dvd_left hdQ
    have hdr : morganVoyceB a ∣ morganVoyceB (s + 1) := hcop.dvd_of_dvd_mul_left hT1
    obtain ⟨hmono_r, hdeg_r⟩ := morganVoyceB_monic_natDegree s
    obtain ⟨_, hdeg_a⟩ := morganVoyceB_monic_natDegree a'
    have hle : (morganVoyceB a).natDegree ≤ (morganVoyceB (s + 1)).natDegree :=
      natDegree_le_of_dvd hdr hmono_r.ne_zero
    rw [ha', hdeg_a, hdeg_r] at hle
    omega

/-- **Strong-divisibility equivalence (polynomial Fibonacci
    divisibility).** For `a ≥ 1`, `b_a ∣ b_n ⟺ a ∣ n`.

    Forward: `morganVoyceB_dvd_of_dvd`; reverse:
    `morganVoyceB_dvd_reverse`. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
theorem morganVoyceB_dvd_iff {a n : ℕ} (ha : 1 ≤ a) :
    morganVoyceB a ∣ morganVoyceB n ↔ a ∣ n :=
  ⟨morganVoyceB_dvd_reverse ha, morganVoyceB_dvd_of_dvd⟩

end QOU.Archimedean
