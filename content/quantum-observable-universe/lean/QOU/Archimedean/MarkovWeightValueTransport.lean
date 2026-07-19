/-
# T4 — weight-value transport: (¾, ¼) derived, the anchor forced, the monodromy point singular

F-construction T4 (bean `qou-bfdq`, milestone `qou-a46k`; T1 cover #4039,
T2 Burau-at-i #4040, T3 deck reality merged; T5 assembly open): the canonical
H₂ Jones–Markov weight VALUES are derived from the T1 Chevalley–Weil dims,
sorry-free.

The canonical Jones–Markov H₂ weights in the Wenzl variable `s = √q`
(corpus `wedderburn_jones_markov.y_lambda_at`, symbolically matched in
`computations/alpha_em/alpha_em_f_t4_weight_value_transport_probe.py`):

    y₂(s)  = (s³+s²+1) / ((s²+1)(s⁴+1)),
    y₁₁(s) = s³(s³+s−1) / ((s²+1)(s⁴+1)).

Three facts, each proved below:

1. **Value identity** — `y₂ 1 = 3/4`, `y₁₁ 1 = 1/4`, and `y₂ + y₁₁ = 1`
   identically: at the classical point the canonical weight equals the
   normalized T1 isotypic projector trace, (moving, invariant)/g = (3,1)/4.
2. **The anchor is forced** — `anchor_forced`: for `s > 0`,
   `y₂ s = 3/4 ↔ s = 1`, via the exact factorization
   `4·num − 3·den = −(s−1)(3s⁵+3s⁴+6s³+2s²+s+1)` and strict positivity of
   the quintic cofactor. The transport point is derived, not chosen — no
   dictionary freedom.
3. **The monodromy point is singular** — the weight denominator in the
   q-variable factors as `q³+q²+q+1 = (q+1)(q²+1)` (over any commutative
   ring, §7c-generic) and vanishes at the T2 Hecke evaluation `q = i`.
   Value transport is anchored at `q = 1`; module structure lives at
   `q = i`; the two legs are complementary, never interchangeable.

Scope guard (STRICT, §Axiomatization is NOT a Proof): T4 only. Nothing here
inhabits `ArchimedeanTauRealization` with functorial provenance — T5
(assembly + F = framework-τ residual) remains THE open wall. Nothing wired;
`1/(8π)` stays phase-4.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

namespace QOU.Archimedean.MarkovWeightValueTransport

/-- Canonical H₂ Jones–Markov weight of the symmetric channel `λ = [2]`,
in the Wenzl variable `s = √q`. -/
noncomputable def y2 (s : ℝ) : ℝ := (s ^ 3 + s ^ 2 + 1) / ((s ^ 2 + 1) * (s ^ 4 + 1))

/-- Canonical H₂ Jones–Markov weight of the antisymmetric channel `λ = [1,1]`. -/
noncomputable def y11 (s : ℝ) : ℝ :=
  s ^ 3 * (s ^ 3 + s - 1) / ((s ^ 2 + 1) * (s ^ 4 + 1))

lemma den_pos (s : ℝ) : 0 < (s ^ 2 + 1) * (s ^ 4 + 1) := by positivity

/-- The weights are normalized: `y₂ + y₁₁ = 1` identically. -/
theorem weights_normalized (s : ℝ) : y2 s + y11 s = 1 := by
  unfold y2 y11
  field_simp
  ring

/-- Value identity, symmetric channel: `y₂(1) = 3/4` — the T1 Chevalley–Weil
moving dimension 3 over the genus g = 4. -/
theorem y2_at_one : y2 1 = 3 / 4 := by norm_num [y2]

/-- Value identity, antisymmetric channel: `y₁₁(1) = 1/4` — the T1 invariant
dimension 1 over the genus g = 4. -/
theorem y11_at_one : y11 1 = 1 / 4 := by norm_num [y11]

/-- The exact factorization behind the forced anchor:
`4·num − 3·den = −(s−1)·(quintic)`. -/
theorem matching_factorization (s : ℝ) :
    4 * (s ^ 3 + s ^ 2 + 1) - 3 * ((s ^ 2 + 1) * (s ^ 4 + 1)) =
      -(s - 1) * (3 * s ^ 5 + 3 * s ^ 4 + 6 * s ^ 3 + 2 * s ^ 2 + s + 1) := by
  ring

lemma quintic_pos {s : ℝ} (hs : 0 < s) :
    0 < 3 * s ^ 5 + 3 * s ^ 4 + 6 * s ^ 3 + 2 * s ^ 2 + s + 1 := by positivity

/-- **The anchor is forced**: on `s > 0`, the canonical weight matches the
Chevalley–Weil dimension fraction `3/4` exactly at `s = 1` and nowhere else.
The transport point is derived, not chosen. -/
theorem anchor_forced {s : ℝ} (hs : 0 < s) : y2 s = 3 / 4 ↔ s = 1 := by
  constructor
  · intro h
    have hden : ((s ^ 2 + 1) * (s ^ 4 + 1)) ≠ 0 := (den_pos s).ne'
    rw [y2, div_eq_iff hden] at h
    have hzero : (s - 1) * (3 * s ^ 5 + 3 * s ^ 4 + 6 * s ^ 3 + 2 * s ^ 2 + s + 1) = 0 := by
      have hf := matching_factorization s
      nlinarith [hf, h]
    rcases mul_eq_zero.mp hzero with h1 | h2
    · linarith
    · exact absurd h2 (quintic_pos hs).ne'
  · rintro rfl
    exact y2_at_one

/-- The weight denominator in the q-variable factors — over ANY commutative
ring (§7c-generic): `q³+q²+q+1 = (q+1)(q²+1)`. -/
theorem denominator_factors {R : Type*} [CommRing R] (q : R) :
    q ^ 3 + q ^ 2 + q + 1 = (q + 1) * (q ^ 2 + 1) := by ring

/-- The Wenzl-variable denominator is the q-variable denominator at `q = s²`:
the two presentations agree. -/
theorem den_in_q (s : ℝ) :
    (s ^ 2 + 1) * (s ^ 4 + 1) = (s ^ 2) ^ 3 + (s ^ 2) ^ 2 + s ^ 2 + 1 := by ring

/-- **The monodromy point is singular**: the weight denominator vanishes at
the T2 Hecke evaluation `q = i`. The Markov weights have a genuine pole at
the monodromy point — value transport is anchored at `q = 1`, module
structure at `q = i`; complementary, never interchangeable. -/
theorem weight_denominator_vanishes_at_monodromy :
    Complex.I ^ 3 + Complex.I ^ 2 + Complex.I + 1 = 0 := by
  have h2 : Complex.I ^ 2 = -1 := Complex.I_sq
  have h3 : Complex.I ^ 3 = -Complex.I := by
    rw [pow_succ, h2]; ring
  rw [h2, h3]; ring

end QOU.Archimedean.MarkovWeightValueTransport
