/-
  The trajectory target for `conj:diophantine-birthday`, and how much of it is already
  a theorem.

  Bean `qou-bday`.  Reads on from `DiophantineBirthdayScope.lean`, which fixed the target
  without stating it.

  ═══ WHERE THIS PICKS UP ═══

  `DiophantineBirthdayScope.lean` proved that the separation **cannot** be by the birthday
  of the number: `birthday_ofReal_le_omega` puts every real at birthday `≤ ω`, in Conway's
  surreals every non-dyadic real is born exactly on day `ω`, so `birthday(√2) = ω =
  birthday(π)` and `no_birthday_only_separation` shows no predicate on the birthday can
  then tell them apart.  It concluded that the conjecture's own gloss — "separated by
  birthday **trajectory**" — was right, and its formalisation was not.

  This module asks the next question: **does that obstruction also kill the trajectory
  version?**  It does not, and the reason is sharp enough to state as a theorem.

  ═══ §1 — WHY THE OBSTRUCTION DOES NOT TRANSFER ═══

  A trajectory criterion reads a real's **sign expansion**, and two reals whose sign
  expansions share a tail differ by a dyadic rational — that is what changing finitely
  many signs does.  So for a criterion to be a function of the *trajectory* at all, it
  must be **invariant under adding a rational**.  That looks like a second collapse
  waiting to happen: it is exactly the kind of blanket invariance that flattened the
  birthday version.

  It is not, and Mathlib already has the reason.  `LiouvilleWith p` — "`x` is approximable
  to order `p` by rationals" — is invariant under a rational shift (`add_rat_iff`) **and
  is not constant**.  Both facts are recorded below as `liouvilleWith_rat_shift_invariant`
  and `liouvilleWith_separates`.  The contrast with `no_birthday_only_separation` is the
  content:

  | criterion | invariant under the ambiguity | constant on the irrationals |
  |---|---|---|
  | `birthday ∘ ofReal` | — | **yes** — collapses, cannot separate |
  | `LiouvilleWith p`   | yes (rational shift) | **no** — separates |

  So the redirection to trajectories in `DiophantineBirthdayScope` was not just a change
  of wording; it moves to a criterion that survives the invariance its own encoding forces.

  ═══ §2 — ONE DIRECTION OF THE CONJECTURE IS A MATHLIB THEOREM ═══

  The conjecture is glossed as separating algebraic from transcendental by approximation
  rate.  **Liouville's theorem is that separation in one direction, and Mathlib proves
  it**: `Liouville.transcendental`.  Recorded here as
  `liouville_trajectory_direction_settled`, discharged, not assumed.

  This matters for how the conjecture should be labelled.  A file carrying
  `conj:diophantine-birthday` as wholly open overstates what is open: the
  fast-approximation ⟹ transcendental direction is closed, in the corpus's own toolchain,
  and has a concrete witness (`liouvilleNumber 2`).

  ═══ ⚠ §3 — WHAT IS STILL MISSING, STATED SO IT IS NOT MISREAD ═══

  **This module does not connect `gonshor` to `LiouvilleWith`, and that bridge is the
  actual open work.**  A faithful trajectory statement needs

      |α − gonshor (prefix of length n)|   compared against   the Liouville exponent

  and nothing *here* relates the two.

  **It was built afterwards: `QOU/AppendixSurreals/GonshorConvergence.lean`.**

      expansion_approximates (α : ℝ) (n : ℕ) (hb : Bracketed (expandState α n)) (k : ℕ) :
        |α − ((expandState α (n + k)).value : ℝ)| ≤ ((expandState α n).gap / 2 ^ k : ℚ)

  For **any** real `α`: `expandState α` is `α`'s own sign expansion (the greedy rule — emit
  `+` when the current value undershoots `α`, `-` otherwise), it provably **brackets** `α`
  at every step (`expandState_brackets`), and once bracketed each further sign **halves**
  the bracket.  So prefix length controls approximation quality with a denominator
  exponential in that length — which is exactly the quantity a Liouville exponent is
  measured against, now for a genuine given real rather than the expansion's own interval.

  Non-vacuity is proved rather than assumed there, since every statement is conditional on
  `Bracketed`: `expandState_half_bracketed` exhibits a concrete `α` whose expansion reaches
  the regime.

  ⚠ **One gap remains, and it is the birthday lift.**  `SignSequence.lean` records that
  Gonshor's `birthday ≤ s.length` is not derivable from the `SurrealField` axioms, because
  the halving step wants a per-step bound on `birthday (x / 2)` that is not among them.
  Note this never blocked the rate above, which stays in `ℚ` — the two have genuinely
  different status, and conflating them is what made the bridge look harder than it was.

  So: §1 says the target is **not obstructed**, §2 says part of it is **already proved**,
  the approximation bridge is **built**, and the lift from rational approximants to surreal
  *birthday* is **not**.  Nothing here should be read as formalising
  `conj:diophantine-birthday` — in particular nothing yet compares
  `expansion_approximates`' rate against `LiouvilleWith`, which is the next step and needs
  the exponent bookkeeping, not new infrastructure.

  A second gap, inherited and unclosed: the Conway fact that every non-dyadic real is born
  on day `ω` is **cited, not proved** — `SurrealField` does not pin the birthday of an
  irrational.  `DiophantineBirthdayScope` says so too.

  -- Ref: [conway1976] On Numbers and Games, Ch. 0–2
  -- Ref: [gonshor1986] An Introduction to the Theory of Surreal Numbers
-/
import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith
import Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleNumber
import QOU.AppendixSurreals.DiophantineBirthdayScope
import QOU.AppendixSurreals.GonshorConvergence

namespace QOU.AppendixSurreals

open Filter

/-! ### §1 — the criterion is invariant under the trajectory's ambiguity, and still separates

Two reals whose sign expansions share a tail differ by a rational.  A trajectory criterion
must therefore be rational-shift invariant to be well defined; the question is whether that
invariance forces the collapse `no_birthday_only_separation` exhibits for birthdays. -/

/-- **The Liouville exponent is a function of the trajectory tail.**

Changing finitely many signs of a sign expansion shifts the real by a rational, and
`LiouvilleWith p` does not see that shift.  So this criterion is well defined on tails —
the precondition any trajectory criterion has to meet. -/
theorem liouvilleWith_rat_shift_invariant (p x : ℝ) (r : ℚ) :
    LiouvilleWith p (x + r) ↔ LiouvilleWith p x :=
  LiouvilleWith.add_rat_iff

/-- **And it does not collapse.**  Unlike `birthday ∘ ofReal`, which is constant on the
irrationals and therefore separates nothing, `LiouvilleWith 2` takes both truth values:
`liouvilleNumber 2` satisfies it and `0` does not.

This is the exact point where the trajectory version departs from the birthday version.
`no_birthday_only_separation` says every predicate on the birthday agrees on `√2` and `π`;
no such collapse is available here, because the criterion is already non-constant. -/
theorem liouvilleWith_separates :
    ∃ x y : ℝ, LiouvilleWith 2 x ∧ ¬ LiouvilleWith 2 y := by
  refine ⟨liouvilleNumber 2, 0, (liouville_liouvilleNumber (le_refl 2)).liouvilleWith 2, ?_⟩
  intro h
  -- `LiouvilleWith p x` with `1 < p` forces `x` irrational; `0` is not.
  exact (h.irrational (by norm_num)).ne_rat 0 (by norm_num)

/-! ### §2 — the fast-approximation direction is settled, in Mathlib

`Liouville x` is "approximable to *every* order `p`" (`forall_liouvilleWith_iff`), and
Liouville's theorem turns that into transcendence. -/

/-- **Liouville's theorem, as the trajectory conjecture's settled direction.**

If a real is approximable to every order — the strongest possible trajectory condition —
it is transcendental.  Discharged from Mathlib, not assumed.

This is why labelling `conj:diophantine-birthday` as wholly open overstates it: one
direction of the separation is a theorem in the corpus's own toolchain. -/
theorem liouville_trajectory_direction_settled (x : ℝ)
    (h : ∀ p : ℝ, LiouvilleWith p x) : Transcendental ℤ x :=
  (forall_liouvilleWith_iff.mp h).transcendental

/-- A **concrete witness** that the settled direction is not vacuous: `liouvilleNumber 2`
is approximable to every order, hence transcendental. -/
theorem liouvilleNumber_two_transcendental : Transcendental ℤ (liouvilleNumber 2) :=
  transcendental_liouvilleNumber (le_refl 2)

/-! ### §3 — the shape of what remains

Stated as a definition so the open content has a name, **not** as a class with a
stipulated field.  `DiophantineBirthday`'s defect was that its class fields chose their
own witness, asserting exactly what the conjecture is supposed to claim, so withholding
an instance encoded nothing.  (Fixed upstream by bean `qou-ffwk`, #5238 — that class now
takes the trajectory as a parameter and its inhabitation depends on it.  The reason for
using a `def` here stands regardless: a `def` of a `Prop` cannot be inhabited by
stipulation at all.) -/

/-- The naive converse of `liouville_trajectory_direction_settled`: that slow rational
approximation is enough for algebraicity.

⚠ **This is FALSE at every `p`, and is named here only so the conjecture's wording is not
mistaken for it.**  Almost every real is transcendental with approximation exponent exactly
`2`, so for any `p > 2` there are transcendentals satisfying `¬ LiouvilleWith p x` — the
hypothesis holds and the conclusion fails.  It is deliberately **not** asserted, instanced,
or used as a hypothesis anywhere.

**Roth's theorem does not repair this direction**, and it is worth being explicit because
the conjecture's gloss cites Roth.  Roth sharpens the *settled* direction — algebraic
irrationals have exponent exactly `2`, hence `LiouvilleWith p x` with `p > 2` already
forces `x` transcendental, improving on Liouville's degree-dependent bound.  It says
nothing about reals that approximate slowly.  So citing Roth buys a better exponent on the
direction that is already closed, not progress on the one that is open.  (Roth is in any
case not in Mathlib; Liouville is.)

The genuinely open content of `conj:diophantine-birthday` is therefore neither this nor
§2, but the **surreal** claim: that the sign-expansion trajectory computes the
approximation exponent.  That is the bridge §3 of the header says is unbuilt. -/
def SlowApproximationImpliesAlgebraic (p : ℝ) : Prop :=
  ∀ x : ℝ, ¬ LiouvilleWith p x → ¬ Transcendental ℤ x

/-- ⚠ **At `p = 1` the statement above is not merely false but VACUOUSLY TRUE**, which is
the trap worth having in the corpus.

`liouvilleWith_one` makes *every* real approximable to order `1`, so the hypothesis
`¬ LiouvilleWith 1 x` is never satisfied and the implication holds with no content.  A
reader who instantiated the target at a convenient exponent would obtain a **proved Lean
theorem** whose statement reads like the conjecture and which says nothing — worse than
the false version, because it carries a proof.

This is the same failure mode as `birthday_avg_le` in `Basic.lean` (satisfied vacuously
under any bounded birthday) and as `DiophantineBirthday`'s **former** stipulated field
(since replaced upstream, bean `qou-ffwk`): a statement whose form suggests content it
does not carry. -/
theorem slowApproximation_vacuous_at_one : SlowApproximationImpliesAlgebraic 1 := by
  intro x hx
  exact absurd (liouvilleWith_one x) hx

/-! ### §3b — the bridge, closed: runs give `LiouvilleWith`

`GonshorConvergence` proves that a run of `k ≥ n·t` signs in `α`'s own expansion yields an
explicit dyadic `m/2ⁿ` with error at most `1/(2ⁿ)ᵗ`. That is the Diophantine shape in this
development's vocabulary; the theorem below states it in **Mathlib's**, which is what makes
the lane's claim checkable against the literature rather than only internally consistent.

⚠ The hypothesis quantifies over **infinitely many** `n` — that is `LiouvilleWith`'s own
`∃ᶠ` and it cannot be removed. Whether a given `α` satisfies it is a fact about that `α`:
bounded runs for an algebraic irrational (Thue–Siegel–Roth, §4), unbounded for a Liouville
number. So this is a **bridge**, not a decision procedure. -/

open scoped Classical in
/-- **Infinitely many runs of length `n·t` ⟹ `LiouvilleWith t`.**

The implication the trajectory picture always asserted, now proved: run structure in the
sign expansion controls the Diophantine exponent.

`Irrational α` is required by `LiouvilleWith`'s own `x ≠ m / n` clause — a rational `α`
eventually *is* one of its dyadic approximants, and the predicate excludes that case by
definition rather than by accident. -/
theorem liouvilleWith_of_frequent_runs (α : ℝ) (t : ℕ) (hirr : Irrational α)
    (hfreq : ∀ N : ℕ, ∃ n, N ≤ n ∧ Bracketed (expandState α n)
      ∧ (expandState α n).gap ≤ 1
      ∧ ∀ j, j < n * t → ((expandState α (n + j)).value : ℝ) < α) :
    LiouvilleWith (t : ℝ) α := by
  refine ⟨2, Filter.frequently_atTop.mpr fun a => ?_⟩
  obtain ⟨n, hn, hb, hg, hrun⟩ := hfreq a
  obtain ⟨m, hm⟩ := approx_exponent_of_run α n (n * t) t hb hg hrun (le_refl _)
  refine ⟨2 ^ n, le_trans hn (Nat.le_of_lt Nat.lt_two_pow_self), m, ?_, ?_⟩
  · -- `α ≠ m / 2ⁿ`: the right-hand side is rational and `α` is not.
    intro h
    exact hirr ⟨(m : ℚ) / 2 ^ n, by rw [h]; push_cast; ring⟩
  · -- `|α − m/2ⁿ| ≤ 1/(2ⁿ)ᵗ < 2/(2ⁿ)ᵗ`.
    have hcast : ((2 ^ n : ℕ) : ℝ) = (2 : ℝ) ^ n := by push_cast; ring
    rw [hcast, Real.rpow_natCast]
    have hpos : (0 : ℝ) < ((2 : ℝ) ^ n) ^ t := by positivity
    calc |α - (m : ℝ) / (2 : ℝ) ^ n|
        ≤ 1 / ((2 : ℝ) ^ n) ^ t := hm
      _ < 2 / ((2 : ℝ) ^ n) ^ t := by
          rw [div_lt_div_iff_of_pos_right hpos]; norm_num

/-! ### §4 — the remaining input is a THEOREM, not a conjecture

What stands between the pieces above and an actual separation is **Thue–Siegel–Roth**: an
algebraic irrational has approximation exponent exactly `2`, so it is not approximable to
any order `p > 2`.  Roth proved it in 1955 and it earned the Fields Medal.

⚠ **So it must not be recorded as a conjecture.**  Doing so would label a settled theorem
as open — the same class of error this arc already found three times in
`conj:diophantine-birthday` (an "honest open state" that encoded nothing, a separation
that was impossible as stated, and a direction already proved in Mathlib).  It is stated
here as an explicit **hypothesis**, and results that need it take it as an argument.

⚠ **A name collision that will mislead a search.**  Mathlib *does* contain
`Mathlib/Combinatorics/Additive/Corner/Roth.lean`, proving **"Roth's theorem"** — but that
is the additive-combinatorics one about 3-term arithmetic progressions, an unrelated
result that happens to share the name.  Thue–Siegel–Roth appears in Mathlib only as a
docstring aside in `LiouvilleWith.lean`.  Checking "is Roth in Mathlib?" by name returns
yes and the answer is no.

Stated as a `def` of a `Prop` rather than a class, for the reason given in §3: a `Prop`
taken as a hypothesis cannot be discharged by stipulating a field. -/

/-- **Thue–Siegel–Roth** (Roth 1955): an algebraic irrational is not approximable to any
order beyond `2`.

A known theorem, **not** formalised in Mathlib and not proved here. Anything below that
needs it takes it as an explicit hypothesis. -/
def RothExponent : Prop :=
  ∀ α : ℝ, IsAlgebraic ℚ α → Irrational α → ∀ p : ℝ, 2 < p → ¬ LiouvilleWith p α

/-- **Conditional on Roth, `LiouvilleWith 3` genuinely separates.**

Both halves are here, and only the first needs the hypothesis:

* no algebraic irrational satisfies it — this is Roth;
* some transcendental does — `liouvilleNumber 2`, unconditionally, from Mathlib.

That is what "separated by trajectory" has to mean to be worth anything: a criterion
taking different values on the two classes. Compare `no_birthday_only_separation`, where
the criterion provably cannot. -/
theorem roth_separates (hR : RothExponent) :
    (∀ α : ℝ, IsAlgebraic ℚ α → Irrational α → ¬ LiouvilleWith 3 α)
      ∧ LiouvilleWith 3 (liouvilleNumber 2) :=
  ⟨fun α ha hi => hR α ha hi 3 (by norm_num),
   (liouville_liouvilleNumber (le_refl 2)).liouvilleWith 3⟩

/-- ⚠ The hypothesis is **not** vacuously available: `RothExponent` is a strictly stronger
statement than anything proved here, since it constrains *every* algebraic irrational at
*every* exponent above `2`, while the unconditional results only ever conclude
transcendence from approximability.

Recorded because the temptation, on finding a hypothesis one cannot discharge, is to weaken
it until it becomes provable — at which point it stops carrying the separation. -/
theorem rothExponent_implies_liouville_direction (hR : RothExponent) (α : ℝ)
    (ha : IsAlgebraic ℚ α) (hi : Irrational α) : ¬ ∀ p : ℝ, LiouvilleWith p α :=
  fun h => hR α ha hi 3 (by norm_num) (h 3)

end QOU.AppendixSurreals
