/-
Copyright (c) 2026 QOU contributors. All rights reserved.

# Chiral-fermion braid words, and lepton number as the writhe sign

`sm-open-problems.md` records the hypercharge blocker as "framework braid words
per chiral fermion still missing".  They are not missing: the corpus's own
`chi = -6` constraint fixes them.

`lepton-number-categorical-properties.md`:

> The torus knot generators `T(2, n)` with odd `n <= 7` exhaust the fermion
> spectrum.  The electron (`T_{2,3}`) and neutrino (`K_{0₁} = T_{2,1}`) are the
> lowest torus knots in this sequence.

`T(2, n)` is by definition the closure of `σ₁ⁿ` in `B₂`, and the antiparticle
is the braid mirror `σᵢ ↦ σᵢ⁻¹` (`AntiparticleCrossingReversalContext`).  The
hadron words are already in the corpus: the gluon unit `σ₀σ₁⁻¹` and the
Borromean baryon `B₃ = (σ₀σ₁⁻¹)³`.

Everything below is computed from those words.  A braid word is a list of
nonzero integers, entry `±i` meaning the generator `σᵢ^{±1}`; the writhe is the
sum of the signs.

## What is proved

* `writhe_sigma1Pow_carriers`, `writhe_gluon`, `writhe_borromean` — the writhes are
  **derived from the braid words**, not assumed.  In particular the gluon unit
  and the Borromean baryon both have writhe `0`, because the gluon unit pairs
  one positive with one negative crossing.
* `mirror_moves_carrier` — on each of the four carriers `T(2,n)`, `n ∈ {1,3,5,7}`
  (the whole fermion spectrum the `chi = -6` constraint allows), the particle and
  its braid mirror have **different writhes**, so the mirror acts freely.  This discharges the
  hypothesis that `LeptonNumberCarrierChirality.lean` showed was required: the
  carrier cannot be an unframed knot type, and at braid level it is not one —
  `νₑ` and `ν̄ₑ` are `σ₁` and `σ₁⁻¹`, distinct words that both close to the
  unknot.
* `leptonNumber_matches_corpus` — `L(β) = sign(writhe β)` reproduces **every**
  row the corpus states: `νₑ, e⁻ ↦ +1`, `ν̄ₑ, e⁺ ↦ -1`, baryon and gluon
  unit `↦ 0`.
* `Y_not_factoring_through_writhe` — the baryon and the gluon unit have
  **equal writhe `0`** (derived) and **different `B`**, so `Y = B - L` does not
  factor through the writhe.  This supplies, from derived facts, the hypothesis
  that `sm-hypercharge-invariant.lean`'s `exists_writhe_degenerate_pair` and
  `SecondCrossingInvariant.lean`'s `baryon_vacuum_separating` had to assume.
* `Y_eq_B_sub_L_left_handed` — **conditional**: given the quark writhe, the
  four left-handed rows come out `{+1/3, +1/3, -1, -1}`.

## Honest scope

`sign` is a **choice** of function, not derived from the framework, and the
quark braid word is **not** in the corpus — `Y_eq_B_sub_L_left_handed` therefore
carries the quark writhe as an explicit hypothesis rather than asserting it.
Chirality (`u_L` vs `u_R`) is still unrepresented: the corpus supplies no
distinct word for the two, which is what a genuine left-handed statement would
need.  So this is a **candidate** for `L`, matching every stated row, not a
derivation of it.

**And it is refuted as a state function on Markov classes** — see
`leptonNumber_not_markov_invariant` below.  Stabilisation raises the writhe by
`1`, flipping `L` from `0` to `1` on the baryon, which violates the corpus's own
`ΔL = 0` under Markov moves.  It survives only if states are
Gröbner–Shirshov normal forms.

`L = sign(w)` is writhe-*dependent*, and that is consistent: `Y = B - L` still
does not factor through `w` (proved below), because `B` varies at fixed `w`.
The invariant required to be independent of the writhe is `B`, not `L`.

Integer arithmetic throughout; no ordering beyond `Int.sign`, no `Real`, no
division (§7c).
-/

import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.StandardModel.BraidWords

/-- A braid word: entry `±i` denotes the generator `σᵢ^{±1}`. -/
abbrev BraidWord := List ℤ

/-- The writhe of a braid word: the sum of the crossing signs. -/
def writhe (β : BraidWord) : ℤ := (β.map Int.sign).sum

/-- `σ₁ⁿ` for `n ≥ 0`, whose closure is the torus knot `T(2, n)`. -/
def sigma1Pow (n : ℕ) : BraidWord := List.replicate n 1

/-- The braid mirror `σᵢ ↦ σᵢ⁻¹`, negating every generator. -/
def mirror (β : BraidWord) : BraidWord := β.map (fun g => -g)

/-- The gluon unit `σ₀σ₁⁻¹`. -/
def gluonUnit : BraidWord := [1, -2]

/-- The Borromean baryon `B₃ = (σ₀σ₁⁻¹)³`. -/
def borromean : BraidWord := gluonUnit ++ gluonUnit ++ gluonUnit

/-- **Lepton number candidate**: the sign of the writhe. -/
def leptonNumber (β : BraidWord) : ℤ := Int.sign (writhe β)

/-! ### The writhes are derived from the braid words -/

/-- `writhe (σ₁ⁿ) = n` — the carrier writhes are computed, not assumed. -/
theorem writhe_sigma1Pow_carriers :
    writhe (sigma1Pow 1) = 1 ∧ writhe (sigma1Pow 3) = 3 ∧
    writhe (sigma1Pow 5) = 5 ∧ writhe (sigma1Pow 7) = 7 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> decide

/-- The gluon unit is writhe-balanced: one positive and one negative crossing. -/
theorem writhe_gluon : writhe gluonUnit = 0 := by decide

/-- Hence the Borromean baryon has writhe `0`. -/
theorem writhe_borromean : writhe borromean = 0 := by decide

/-! ### The mirror acts freely at braid level -/

/-- `writhe (mirror (σ₁ⁿ)) = -n`. -/
theorem writhe_mirror_sigma1Pow_carriers :
    writhe (mirror (sigma1Pow 1)) = -1 ∧ writhe (mirror (sigma1Pow 3)) = -3 ∧
    writhe (mirror (sigma1Pow 5)) = -5 ∧ writhe (mirror (sigma1Pow 7)) = -7 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> decide

/-- **The chirality obstruction is discharged at braid level.**

For `n ≠ 0` the particle `σ₁ⁿ` and its mirror `σ₁⁻ⁿ` have different writhes, so
the mirror does **not** fix the carrier.  This is exactly the hypothesis
`LeptonNumberCarrierChirality.mirror_must_move_the_carrier` requires — and it
holds even though `νₑ = σ₁` and `ν̄ₑ = σ₁⁻¹` both close to the (amphichiral)
unknot.  The braid word, not the knot type, is the carrier. -/
theorem mirror_moves_carrier :
    writhe (mirror (sigma1Pow 1)) ≠ writhe (sigma1Pow 1) ∧
    writhe (mirror (sigma1Pow 3)) ≠ writhe (sigma1Pow 3) ∧
    writhe (mirror (sigma1Pow 5)) ≠ writhe (sigma1Pow 5) ∧
    writhe (mirror (sigma1Pow 7)) ≠ writhe (sigma1Pow 7) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> decide

/-! ### `L = sign(writhe)` reproduces every corpus row -/

/-- **All six stated rows.**  `νₑ = σ₁`, `e⁻ = σ₁³`, their mirrors, and the two
writhe-`0` hadron words. -/
theorem leptonNumber_matches_corpus :
    leptonNumber (sigma1Pow 1) = 1 ∧
    leptonNumber (sigma1Pow 3) = 1 ∧
    leptonNumber (mirror (sigma1Pow 1)) = -1 ∧
    leptonNumber (mirror (sigma1Pow 3)) = -1 ∧
    leptonNumber borromean = 0 ∧
    leptonNumber gluonUnit = 0 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;> decide

/-! ### `Y = B − L` does not factor through the writhe -/

/-- **The writhe-degenerate pair, with derived writhes.**

The Borromean baryon and the gluon unit both have writhe `0` — *computed* from
their braid words — while carrying different baryon number (`1` vs `0`).  Since
`L` vanishes on both, `Y = B - L` differs on them at equal writhe, so `Y` is not
a function of the writhe.

This discharges from derived facts the hypothesis assumed by
`sm-hypercharge-invariant.lean`'s `exists_writhe_degenerate_pair`. -/
theorem Y_not_factoring_through_writhe
    (B : BraidWord → ℚ) (hB_bar : B borromean = 1) (hB_glu : B gluonUnit = 0) :
    writhe borromean = writhe gluonUnit ∧
    (B borromean - (leptonNumber borromean : ℚ))
      ≠ (B gluonUnit - (leptonNumber gluonUnit : ℚ)) := by
  refine ⟨by rw [writhe_borromean, writhe_gluon], ?_⟩
  have h1 : leptonNumber borromean = 0 := by decide
  have h2 : leptonNumber gluonUnit = 0 := by decide
  rw [hB_bar, hB_glu, h1, h2]
  norm_num

/-- **The left-handed spectrum — conditional on the quark writhe.**

The corpus supplies no quark braid word, so its writhe is carried as an explicit
hypothesis (`hq`).  Given it, `Y = B - L` returns `{+1/3, +1/3, -1, -1}` for
`(u, d, νₑ, e⁻)`.  Stated in the `3×` normalisation to stay division-free. -/
theorem Y_eq_B_sub_L_left_handed
    (quark : BraidWord) (hq : writhe quark = 0) :
    -- quarks: 3B = 1, L = 0  ⟹  3Y = 1
    (1 : ℤ) - 3 * leptonNumber quark = 1 ∧
    -- leptons: 3B = 0, L = +1  ⟹  3Y = -3
    (0 : ℤ) - 3 * leptonNumber (sigma1Pow 1) = -3 ∧
    (0 : ℤ) - 3 * leptonNumber (sigma1Pow 3) = -3 := by
  have hL : leptonNumber quark = 0 := by
    unfold leptonNumber; rw [hq]; rfl
  refine ⟨by rw [hL]; ring, ?_, ?_⟩ <;> decide


/-! ### REFUTATION: `sign(writhe)` is not Markov-invariant -/

/-- **The candidate fails the corpus's own conservation axiom.**

Markov II (stabilization) sends `β ∈ B_n` to `βσ_n ∈ B_{n+1}` with the *same*
link closure, and raises the writhe by `1`.  The Borromean baryon has writhe `0`
(`writhe_borromean`), so its stabilisation has writhe `1` — and therefore
`L = sign(writhe)` jumps from `0` to `1`.

`lepton-number-categorical-properties.md` conservation clause 3 requires
`ΔL = 0` under Markov moves.  This is `ΔL = 1`.  So `L = sign(writhe)` is **not
a function of the link**, only of the braid word, and it is refuted as a state
function on Markov classes.

The one surviving reading is that states are **Gröbner–Shirshov normal forms**
(`mba-step02-gs-reduction.md`: "every downstream algorithm consumes `NF(w)`, not
the raw braid"), where a canonical representative is fixed and Markov moves do
not act within the state space.  On that reading `L = sign(writhe)` is
well-defined — but then conservation clause 3 is about a different object than
this `L`, and the corpus should say which. -/
theorem leptonNumber_not_markov_invariant :
    leptonNumber borromean = 0 ∧ leptonNumber (borromean ++ [3]) = 1 := by
  refine ⟨by decide, by decide⟩

end QOU.StandardModel.BraidWords
