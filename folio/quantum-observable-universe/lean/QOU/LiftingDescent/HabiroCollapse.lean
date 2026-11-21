import Mathlib.Tactic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.ZMod.Basic

/-!
# The Habiro collapse at a `2p`-th root of unity — and what it does not give

`MotivicPerpetualObstructionFromTrace.lean` proves the QOU Frobenius is a
non-unit *conditional on* a hypothesis `h_collapse : reduce p (frob p) = C`.
Bean `qou-lrnd` recorded that discharging `h_collapse` "needs cyclotomic ring
theory over `ℤ[ζ_2p]`". This file does two things to that.

**One: the collapse is not cyclotomic at all.** It factors into a general
ring-theoretic statement plus a single arithmetic input. If `φ : R →+* S` sends
`q ↦ -1`, then `φ ((q;q)_m) = 0` for every `m ≥ 2` — because the `i = 2` factor
is `1 - q²` and `1 - (-1)² = 0`. So any Habiro expansion `Σ_{m<N} a m (q;q)_m`
has image `φ (a 0) + 2 φ (a 1)`, with no roots of unity, no ramification, and
no ring of integers anywhere in the proof (`map_habiro_expansion`). The
cyclotomic content of `h_collapse` is exactly one fact, `φ ζ_{2p} = -1`, and
everything else was already ordinary algebra.

**Two: the collapse does not imply what it is used for.** Downstream,
`h_collapse` feeds `not_isUnit_of_image`: `¬IsUnit (φ x) → ¬IsUnit x`. That
needs the *residue* to be a non-unit. The residue here is `C = 4` in
`O/𝔭 ≅ 𝔽_p`, and `4` is a unit there for every `p ≠ 2` (`isUnit_four_zmod`).
So the transfer is inapplicable at every odd prime — the direction of
`not_isUnit_of_image` is what breaks, not its statement.

This is a **structural exclusion**, not a failed search: there is an explicit
unit with the required residue. The cyclotomic unit
`u₄ = 1 + ζ + ζ² + ζ³ = (1 - ζ⁴)/(1 - ζ)` is a unit of `ℤ[ζ_p]` — its inverse
`1 + ζ⁴ + ζ⁸ + ⋯ + ζ^{4(b-1)}`, where `4b ≡ 1 (mod p)`, is integral by
inspection — and `ζ ≡ 1 (mod 𝔭)` gives `u₄ ≡ 4 (mod 𝔭)`. Verified exactly
(integer arithmetic, no floats) for `p ∈ {3,…,31, 101, 1009}` in
`computations/probes/cyclotomic_residue_four_unit_probe.py`.

So `Frob_p ≡ 4 (mod 𝔭)` is *compatible with `Frob_p` being a unit*, and cannot
on its own establish the perpetual obstruction.

Ref: [leitner2026] bean `qou-lrnd`
-/

namespace QOU.LiftingDescent

open Finset

variable {R S : Type*} [CommRing R] [CommRing S]

/-- The Habiro `q`-Pochhammer symbol `(q;q)_m = ∏_{i=1}^{m} (1 - qⁱ)`.

    Distinct from `QOU.MathlibExt.QuantumDilogarithm.qPochProd`, which is the
    Faddeev symbol `(-qx; q²)_N`. -/
def qPoch (q : R) : ℕ → R
  | 0 => 1
  | m + 1 => qPoch q m * (1 - q ^ (m + 1))

@[simp] theorem qPoch_zero (q : R) : qPoch q 0 = 1 := rfl

theorem qPoch_succ (q : R) (m : ℕ) :
    qPoch q (m + 1) = qPoch q m * (1 - q ^ (m + 1)) := rfl

@[simp] theorem qPoch_one (q : R) : qPoch q 1 = 1 - q := by
  simp [qPoch_succ]

theorem qPoch_two (q : R) : qPoch q 2 = (1 - q) * (1 - q ^ 2) := by
  rw [qPoch_succ, qPoch_one]

/-- At `q ↦ -1` the second factor already vanishes: `1 - (-1)² = 0`. -/
theorem map_qPoch_two (φ : R →+* S) {q : R} (hq : φ q = -1) :
    φ (qPoch q 2) = 0 := by
  rw [qPoch_two, map_mul]
  have h2 : φ (1 - q ^ 2) = 0 := by
    rw [map_sub, map_one, map_pow, hq]; ring
  rw [h2, mul_zero]

/-- **The collapse, factor by factor.** A ring map sending `q ↦ -1` kills
    `(q;q)_m` for every `m ≥ 2`. No cyclotomic input is used. -/
theorem map_qPoch_eq_zero (φ : R →+* S) {q : R} (hq : φ q = -1)
    {m : ℕ} (hm : 2 ≤ m) : φ (qPoch q m) = 0 := by
  induction m with
  | zero => omega
  | succ n ih =>
    rcases Nat.lt_or_ge n 2 with hn | hn
    · have hn1 : n = 1 := by omega
      subst hn1
      exact map_qPoch_two φ hq
    · rw [qPoch_succ, map_mul, ih hn, zero_mul]

/-- **Habiro collapse.** Under any ring map sending `q ↦ -1`, a Habiro
    expansion collapses to its two lowest coefficients:
    `φ (Σ_{m<N} a m · (q;q)_m) = φ (a 0) + 2 · φ (a 1)`.

    This is the whole content of `h_collapse` in
    `MotivicPerpetualObstructionFromTrace.lean`, minus the single arithmetic
    input `φ q = -1`. The `2` is `φ ((q;q)_1) = 1 - (-1)`. -/
theorem map_habiro_expansion (φ : R →+* S) {q : R} (hq : φ q = -1)
    (a : ℕ → R) {N : ℕ} (hN : 2 ≤ N) :
    φ (∑ m ∈ range N, a m * qPoch q m) = φ (a 0) + 2 * φ (a 1) := by
  have hsub : range 2 ⊆ range N := by
    intro m hm
    simp only [Finset.mem_range] at hm ⊢
    omega
  rw [map_sum, ← Finset.sum_subset hsub]
  · simp only [Finset.sum_range_succ, qPoch_zero,
      qPoch_one, map_mul, map_one, map_sub, hq, mul_one]
    ring
  · intro m _ hm2
    simp only [Finset.mem_range, not_lt] at hm2
    rw [map_mul, map_qPoch_eq_zero φ hq hm2, mul_zero]

/-- `4` is a unit of `𝔽_p` for every odd prime — so a residue of `4` is
    **not** an obstruction, and `not_isUnit_of_image` cannot be applied to it.

    `O/𝔭 ≅ 𝔽_p` is where the collapse of the QOU Frobenius lands, which is why
    this blocks the intended argument at every prime except `2`. -/
theorem isUnit_four_zmod {p : ℕ} (hp : p.Prime) (hp2 : p ≠ 2) :
    IsUnit (4 : ZMod p) := by
  haveI : Fact p.Prime := ⟨hp⟩
  refine Ne.isUnit ?_
  intro h
  have h4 : ((4 : ℕ) : ZMod p) = 0 := by push_cast; exact h
  have hdvd : p ∣ 4 := (CharP.cast_eq_zero_iff (ZMod p) p 4).mp h4
  have h22 : p ∣ 2 ^ 2 := by norm_num; exact hdvd
  exact hp2 ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp
    (hp.dvd_of_dvd_pow h22))

/-- The shape of the gap, stated so it cannot be mistaken for a search that
    failed: whenever the residue is a unit downstream, the image says nothing
    about `x`, because `not_isUnit_of_image` runs the other way. -/
theorem residue_unit_gives_no_obstruction (φ : R →+* S) (x : R) {C : S}
    (hx : φ x = C) (hC : IsUnit C) : IsUnit (φ x) := hx ▸ hC

end QOU.LiftingDescent
