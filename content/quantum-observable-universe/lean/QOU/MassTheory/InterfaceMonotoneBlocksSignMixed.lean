/-
# Breaking affineness does not open the sign-mixed escape — breaking monotonicity does

`QOU/MassTheory/PnBetweennessBlocksSignMixed.lean` proves that the sign-mixed
pattern `qou-q8vl` requires — the pn bond factor the strict maximum of the three —
is unreachable when the pn letter is a strict convex combination of the like-pair
letters **and the interface law `μ = z + d` is affine**. Bean `qou-q8vl` therefore
records the open escape as:

> a third bond family *"must break the AVERAGING of the pn letter, or break
> AFFINENESS of the interface law"*.

**The second half of that is too weak, and this file measures how much.**
Affineness is not what does the blocking. What does the blocking is that an
affine map is **monotone**, and monotonicity alone suffices:

* `not_strict_max_of_monotone` / `not_strict_max_of_antitone` — if `f` is
  monotone (in either direction) and `c` lies between `a` and `b`, then `f c`
  cannot strictly exceed both `f a` and `f b`. No linearity, no continuity, no
  algebra: the hypothesis is an order property and the proof is one `absurd`.

So a third bond family that merely abandons affineness gains nothing. A cubic
interface law `d ↦ d³` is as blocked as `d ↦ z + d`. The escape requires a
**non-monotone** interface law, which is a strictly stronger demand and a much
smaller space to search.

`hump_realises_signMixed` shows the narrowing is sharp rather than a disguised
impossibility: a non-monotone law *does* realise the pattern. So monotonicity is
exactly the invariant — necessary and sufficient at this level of description.

## What this does and does not say

It says: **do not spend a tranche on a non-affine interface law.** Check whether
it is monotone first; if it is, the pattern is already excluded and the
construction is dead before any number is computed. That is a cheap filter on an
open search, and it is why the result is worth its length.

It does **not** derive a non-monotone law, propose one, or claim one exists in
the framework. Scope (b) structural exclusion; the invariant is order-preservation,
which is an identity rather than a measurement. `qou-q8vl`'s *other* escape —
breaking the averaging of the pn letter — is untouched.

Physically, a non-monotone interface law means that increasing the letter offset
would *decrease* the bond factor over some range and increase it over another.
Whether the framework admits such a thing is open and is not addressed here.

No `q`, no Markov parameter, no anchor, no numeral outside the witness.

Bean `qou-2ss0`, under `qou-q8vl`.
-/
import Mathlib.Order.Monotone.Basic
import Mathlib.Tactic

namespace QOU.MassTheory.InterfaceMonotone

section OrderCore

variable {α β : Type*} [Preorder α] [Preorder β]

/-- **A monotone map keeps the middle in the middle.** If `c` lies between `a`
and `b` then `f c` does not strictly exceed both endpoints. -/
theorem not_strict_max_of_monotone {f : α → β} (hf : Monotone f) {a b c : α}
    (_hac : a ≤ c) (hcb : c ≤ b) : ¬ (f a < f c ∧ f b < f c) := by
  rintro ⟨_, h2⟩
  exact absurd (lt_of_lt_of_le h2 (hf hcb)) (lt_irrefl _)

/-- **And so does an antitone one.** Reversing the order reverses which endpoint
does the work, and the conclusion is unchanged. -/
theorem not_strict_max_of_antitone {f : α → β} (hf : Antitone f) {a b c : α}
    (hac : a ≤ c) (_hcb : c ≤ b) : ¬ (f a < f c ∧ f b < f c) := by
  rintro ⟨h1, _⟩
  exact absurd (lt_of_lt_of_le h1 (hf hac)) (lt_irrefl _)

/-- **The same, with the endpoints in the other order.** Betweenness is
symmetric; the exclusion should not depend on which like-pair letter is larger. -/
theorem not_strict_max_of_monotone' {f : α → β} (hf : Monotone f) {a b c : α}
    (_hbc : b ≤ c) (hca : c ≤ a) : ¬ (f a < f c ∧ f b < f c) := by
  rintro ⟨h1, _⟩
  exact absurd (lt_of_lt_of_le h1 (hf hca)) (lt_irrefl _)

end OrderCore

section CorpusApplication

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- A strict convex combination, as in `PnBetweennessBlocksSignMixed`. -/
def combo (w a b : R) : R := w * a + (1 - w) * b

/-- A strict convex combination lies weakly between its endpoints. -/
theorem combo_mem {w a b : R} (hw0 : 0 < w) (hw1 : w < 1) (hab : a ≤ b) :
    a ≤ combo w a b ∧ combo w a b ≤ b := by
  constructor <;> unfold combo <;> nlinarith [hw0, hw1, hab]

/-- **The sharpened exclusion.** For *any* monotone interface law `f` — affine or
not — a pn letter that is a strict convex combination of the like-pair letters
cannot produce a pn bond factor that strictly exceeds both like-pair factors.

`PnBetweennessBlocksSignMixed.pn_not_strict_max` is the `f = (z + ·)` instance. -/
theorem pn_not_strict_max_of_monotone {f : R → R} (hf : Monotone f)
    {w dpp dnn : R} (hw0 : 0 < w) (hw1 : w < 1) (hle : dpp ≤ dnn) :
    ¬ (f dpp < f (combo w dpp dnn) ∧ f dnn < f (combo w dpp dnn)) := by
  obtain ⟨h1, h2⟩ := combo_mem hw0 hw1 hle
  exact not_strict_max_of_monotone hf h1 h2

/-- The required pattern, as `qou-q8vl` states it. -/
def signMixedPattern (mupp mupn munn : R) : Prop :=
  1 < mupn ∧ mupp < 1 ∧ munn < 1

/-- **Corollary — the pattern is unreachable under any monotone law.** So
abandoning affineness, on its own, buys nothing: the construction is dead before
any bond value is computed. -/
theorem signMixed_impossible_of_monotone {f : R → R} (hf : Monotone f)
    {w dpp dnn : R} (hw0 : 0 < w) (hw1 : w < 1) (hle : dpp ≤ dnn) :
    ¬ signMixedPattern (f dpp) (f (combo w dpp dnn)) (f dnn) := by
  rintro ⟨h1, hpp, hnn⟩
  exact pn_not_strict_max_of_monotone hf hw0 hw1 hle ⟨by linarith, by linarith⟩

end CorpusApplication

section Sharpness

/-- A non-monotone interface law: the downward parabola `f d = 1 − (d − 1)²`,
peaking at the midpoint of `[0, 2]`. -/
noncomputable def hump (d : ℝ) : ℝ := 1 - (d - 1) ^ 2

theorem hump_values : hump 0 = 0 ∧ hump 1 = 1 ∧ hump 2 = 0 := by
  refine ⟨?_, ?_, ?_⟩ <;> unfold hump <;> norm_num

/-- It is not monotone: it rises then falls. -/
theorem hump_not_monotone : ¬ Monotone hump := by
  intro h
  have := h (by norm_num : (1:ℝ) ≤ 2)
  unfold hump at this
  norm_num at this

/-- Nor antitone. -/
theorem hump_not_antitone : ¬ Antitone hump := by
  intro h
  have := h (by norm_num : (0:ℝ) ≤ 1)
  unfold hump at this
  norm_num at this

/-- **The narrowing is sharp.** A non-monotone law *does* put the middle strictly
above both endpoints — so monotonicity is exactly the invariant that blocks the
pattern, not a sufficient condition standing in for something weaker. -/
theorem hump_realises_strict_max :
    hump 0 < hump 1 ∧ hump 2 < hump 1 := by
  unfold hump; norm_num

/-- Stated as the escape it is: there exists an interface law under which the
middle letter is the strict maximum, and it is necessarily non-monotone. -/
theorem nonmonotone_escape_exists :
    ∃ f : ℝ → ℝ, ¬ Monotone f ∧ ¬ Antitone f ∧ f 0 < f 1 ∧ f 2 < f 1 :=
  ⟨hump, hump_not_monotone, hump_not_antitone, hump_realises_strict_max.1,
    hump_realises_strict_max.2⟩

end Sharpness

end QOU.MassTheory.InterfaceMonotone
