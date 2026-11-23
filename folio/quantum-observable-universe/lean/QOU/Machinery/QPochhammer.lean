/-
Copyright (c) 2026 litlfred. All rights reserved.

# q-Pochhammer symbols `(q;q)_n` — categorical machinery scaffold (2026-06-04)

This file scaffolds the q-Pochhammer infrastructure needed for the
Habiro-element promotion of the Q_β residue A and m_μ closure
(audit doc `docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`).

## Definitions provided

| Symbol | Definition | Notes |
|--------|-----------|-------|
| `qPochhammerFinite a q n` | `∏_{k=0}^{n-1} (1 - a·q^k)` | Finite q-Pochhammer `(a;q)_n` |
| `qPochhammerDiag q n` | `qPochhammerFinite q q n = ∏_{k=0}^{n-1} (1 - q^(k+1))` | Diagonal case `(q;q)_n` |
| `qBinomial n k q` | `(q;q)_n / ((q;q)_k · (q;q)_{n-k})` | Gaussian q-binomial |

## Theorems provided (all proved)

- `qPochhammerFinite_zero`: `(a;q)_0 = 1` (empty product)
- `qPochhammerFinite_one`: `(a;q)_1 = 1 - a`
- `qPochhammerFinite_succ_eq_mul`: recursion `(a;q)_{n+1} = (a;q)_n · (1 - a·q^n)`
- `qPochhammerDiag_zero`: `(q;q)_0 = 1`
- `qPochhammerDiag_one`: `(q;q)_1 = 1 - q`
- `qPochhammerDiag_at_q_one`: `(q;q)_n = 0` for all `n ≥ 1` at `q = 1` (collapses)

## Cross-refs

- `MmuR9V9Closure.lean` (downstream consumer for residue A promotion)
- `QBetaCategoricalPrecisionLadder.lean` (uses ℏ_q^k which is dual to (q;q)_n)
- Audit: [`docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](../../../../../docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md)
-/

import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.Ring.GeomSum
import Mathlib.Tactic.Ring

open BigOperators

namespace QOU.Machinery

/-! ## Finite q-Pochhammer `(a;q)_n`

Base ring is a generic `[CommRing R]` per AGENTS.md §7c: the q-Pochhammer
symbol and its recursion are purely algebraic (`q ^ k` is `Monoid.npow`,
`k : ℕ`), with no archimedean construct. The archimedean specialisation
`R := ℝ` at the substrate `q₀` happens at the consumer sites. Only the
Gaussian q-binomial (which divides) needs `[Field R]`. -/

variable {R : Type*}

/-- Finite q-Pochhammer `(a;q)_n = ∏_{k=0}^{n-1} (1 - a·q^k)`. -/
noncomputable def qPochhammerFinite [CommRing R] (a q : R) (n : ℕ) : R :=
  ∏ k ∈ Finset.range n, (1 - a * q ^ k)

/-- Diagonal q-Pochhammer `(q;q)_n`, defined as `qPochhammerFinite q q n
= ∏_{k=0}^{n-1} (1 - q·q^k)`. Note this equals the textbook form
`∏_{k=0}^{n-1} (1 - q^(k+1))` (provably, via `q·q^k = q^(k+1)`), but the
two are not definitionally equal — we keep the `q·q^k` form so that
`qPochhammerDiag` reuses `qPochhammerFinite` directly. -/
noncomputable def qPochhammerDiag [CommRing R] (q : R) (n : ℕ) : R :=
  qPochhammerFinite q q n

/-! ## Basic identities (proved) -/

/-- **(a;q)_0 = 1** (empty product). -/
theorem qPochhammerFinite_zero [CommRing R] (a q : R) :
    qPochhammerFinite a q 0 = 1 := by
  unfold qPochhammerFinite
  simp

/-- **(a;q)_1 = 1 - a**. -/
theorem qPochhammerFinite_one [CommRing R] (a q : R) :
    qPochhammerFinite a q 1 = 1 - a := by
  unfold qPochhammerFinite
  simp

/-- **(q;q)_0 = 1** (empty product). -/
theorem qPochhammerDiag_zero [CommRing R] (q : R) : qPochhammerDiag q 0 = 1 := by
  unfold qPochhammerDiag
  exact qPochhammerFinite_zero q q

/-- **(q;q)_1 = 1 - q**. -/
theorem qPochhammerDiag_one [CommRing R] (q : R) : qPochhammerDiag q 1 = 1 - q := by
  unfold qPochhammerDiag
  exact qPochhammerFinite_one q q

/-- **Recursion**: `(a;q)_{n+1} = (a;q)_n · (1 - a·q^n)`. Direct
application of `Finset.prod_range_succ` (the term closes the goal up
to beta-reduction of `f n`). -/
theorem qPochhammerFinite_succ [CommRing R] (a q : R) (n : ℕ) :
    qPochhammerFinite a q (n + 1) = qPochhammerFinite a q n * (1 - a * q ^ n) := by
  unfold qPochhammerFinite
  exact Finset.prod_range_succ _ n

/-- **At q = 1**, `(q;q)_n = 0` for all `n ≥ 1` because the `k = 0`
factor is `1 - q^1 = 0`. -/
theorem qPochhammerDiag_at_q_one [CommRing R] (n : ℕ) (hn : 0 < n) :
    qPochhammerDiag (1 : R) n = 0 := by
  unfold qPochhammerDiag qPochhammerFinite
  apply Finset.prod_eq_zero (i := 0)
  · exact Finset.mem_range.mpr hn
  · simp

/-! ## Gaussian q-binomial `[n choose k]_q`

The standard form `[n k]_q = (q;q)_n / ((q;q)_k · (q;q)_{n-k})`.
Currently a placeholder; promotion to `derived` requires the q-binomial
theorem and Pascal-type recursion (q-deformed).

**Normalization note (bean `5ldf` consolidation, 2026-06-26).** This is the
**standard** `(q;q)` q-binomial — a *distinct* object from the QOU-canonical
**balanced** `QOU.MathlibExt.QPartitionCombinatorics.qBinom`
(`(qⁿ−q⁻ⁿ)/(q−q⁻¹)` brackets): e.g. `[2 choose 1]` is `1+q` here vs `q+q⁻¹`
there. The two are NOT interchangeable; pick by which bracket convention the
caller needs. (The balanced one has the proved q-Pascal `qBinom_pascal`.) -/

/-- **Gaussian q-binomial** `[n k]_q` as a quotient of q-Pochhammers (standard
`(q;q)` normalization — see the normalization note above; distinct from the
balanced canonical `QPartitionCombinatorics.qBinom`).
Well-defined when `(q;q)_k ≠ 0` and `(q;q)_{n-k} ≠ 0`. -/
noncomputable def qBinomial [Field R] (n k : ℕ) (q : R) : R :=
  qPochhammerDiag q n / (qPochhammerDiag q k * qPochhammerDiag q (n - k))

/-- `[n 0]_q = 1`, provided the diagonal q-Pochhammer `(q;q)_n` is
nonzero (needed so the quotient `(q;q)_n / (q;q)_n` cancels to `1`;
`qBinomial` is defined as a real quotient and is not totalized at the
`(q;q)_n = 0` locus, e.g. roots of unity). -/
theorem qBinomial_zero [Field R] (n : ℕ) (q : R) (hq : qPochhammerDiag q n ≠ 0) :
    qBinomial n 0 q = 1 := by
  unfold qBinomial
  rw [qPochhammerDiag_zero, Nat.sub_zero, one_mul]
  exact div_self hq

/-! ## The q-Pochhammer / Habiro projective system and root-of-unity truncation (bean `qou-n2un`)

The Habiro ring `ℤ[q]^∧ = lim_← ℤ[q]/((q;q)_n)` rests on two structural properties of the
diagonal q-Pochhammer tower `(q;q)_n = qPochhammerDiag q n` over any commutative ring `R`:

1. **Divisibility tower (`qPochhammerDiag_dvd_of_le`):** for `m ≤ n`, `(q;q)_m ∣ (q;q)_n`, so
   the principal ideals `((q;q)_n)` form a descending chain and the quotient maps
   `R / ((q;q)_n) → R / ((q;q)_m)` are well-defined.
2. **Root-of-unity vanishing and Habiro series truncation (`qPochhammerDiag_eq_zero_of_pow_eq_one`,
   `habiro_series_truncates_at_root_of_unity`):** if `q ^ k = 1` for some `1 ≤ k ≤ n`, then
   `(q;q)_n = 0`, so every Habiro series `∑_{j < N} c_j · (q;q)_j` with `N ≥ k` truncates
   identically to its finite prefix `∑_{j < k} c_j · (q;q)_j`.
-/

/-- **Tower divisibility for `qPochhammerFinite`:** for `m ≤ n`, `(a;q)_m ∣ (a;q)_n`. -/
theorem qPochhammerFinite_dvd_of_le [CommRing R] (a q : R) {m n : ℕ} (hmn : m ≤ n) :
    qPochhammerFinite a q m ∣ qPochhammerFinite a q n := by
  induction hmn with
  | refl => exact dvd_rfl
  | @step k _ ih =>
    rw [qPochhammerFinite_succ]
    exact dvd_mul_of_dvd_left ih (1 - a * q ^ k)

/-- **Habiro projective-system divisibility:** for `m ≤ n`, `(q;q)_m ∣ (q;q)_n`. -/
theorem qPochhammerDiag_dvd_of_le [CommRing R] (q : R) {m n : ℕ} (hmn : m ≤ n) :
    qPochhammerDiag q m ∣ qPochhammerDiag q n :=
  qPochhammerFinite_dvd_of_le q q hmn

/-- **Root-of-unity vanishing:** if `q ^ k = 1` for some `1 ≤ k ≤ n`, then the
    `(k - 1)`-th factor `1 - q * q ^ (k - 1) = 1 - q ^ k` vanishes, so `(q;q)_n = 0`. -/
theorem qPochhammerDiag_eq_zero_of_pow_eq_one [CommRing R] (q : R) {k n : ℕ}
    (hk1 : 1 ≤ k) (hkn : k ≤ n) (hroot : q ^ k = 1) :
    qPochhammerDiag q n = 0 := by
  unfold qPochhammerDiag qPochhammerFinite
  apply Finset.prod_eq_zero (i := k - 1)
  · exact Finset.mem_range.mpr (by omega)
  · have hpow : q * q ^ (k - 1) = q ^ k := by
      rw [← pow_succ', Nat.sub_add_cancel hk1]
    rw [hpow, hroot, sub_self]

/-- **Habiro series root-of-unity truncation (evaluation homomorphism):** if `q ^ k = 1`
    for `1 ≤ k ≤ N`, then every Habiro expansion `∑_{j < N} c j * (q;q)_j` truncates
    exactly to its degree-`< k` prefix `∑_{j < k} c j * (q;q)_j`. -/
theorem habiro_series_truncates_at_root_of_unity [CommRing R] (q : R) (c : ℕ → R)
    {k N : ℕ} (hk1 : 1 ≤ k) (hkN : k ≤ N) (hroot : q ^ k = 1) :
    (∑ j ∈ Finset.range N, c j * qPochhammerDiag q j) =
      ∑ j ∈ Finset.range k, c j * qPochhammerDiag q j := by
  symm
  apply Finset.sum_subset (Finset.range_mono hkN)
  intro j hjN hjk
  rw [Finset.mem_range] at hjN hjk
  push_neg at hjk
  rw [qPochhammerDiag_eq_zero_of_pow_eq_one q hk1 hjk hroot, mul_zero]

end QOU.Machinery
