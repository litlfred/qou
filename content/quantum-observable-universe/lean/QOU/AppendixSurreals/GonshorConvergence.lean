/-
  How fast Gonshor's sign expansion converges — the arithmetic half of the bridge
  `DiophantineBirthdayTrajectory` says is missing.

  Bean `qou-bday`.

  ═══ WHAT THIS IS FOR ═══

  `DiophantineBirthdayTrajectory.lean` established that a trajectory criterion for
  `conj:diophantine-birthday` is **not obstructed** (unlike birthday-of-the-number) and
  that one direction is already a Mathlib theorem, then recorded the remaining gap:

  > nothing here proves that `gonshor`'s length-`n` prefix value *is* the dyadic
  > approximant of `α` at denominator `2ⁿ`.

  This module supplies the quantitative core of that: **once the expansion has bracketed
  its target, every further sign halves the bracket.**

  ═══ ⚠ WHY THIS IS AVAILABLE WHEN THE SHARPER BIRTHDAY BOUND IS NOT ═══

  `SignSequence.lean` records that Gonshor's `birthday ≤ s.length` is **not** derivable
  from the `SurrealField` axioms, because the induction step needs a per-step bound on
  `birthday (x / 2)` — the halving move — which is not among the axioms and is not implied
  by them.

  That blocker is about **lifting to `birthday`**. It says nothing about the rational
  values themselves, and `gonshor : List Sign → ℚ` never leaves `ℚ`. So the convergence
  *rate* is ordinary rational arithmetic and needs no axiom at all. The two halves of the
  bridge have genuinely different status, and conflating them is what made this look
  harder than it is:

  | half | status |
  |---|---|
  | rate of the rational approximants | **proved here**, axiom-free |
  | lifting the rate to surreal birthday | blocked, needs a `birthday (x/2)` axiom |

  ═══ THE INVARIANT ═══

  `GonshorState.step` has two regimes. Before a bound exists it steps by `±1` (integer
  search); once the opposite bound appears it bisects. `Bracketed` names the bisection
  regime, and its load-bearing clause is `value = (lo + hi) / 2` — **the value is the
  midpoint of its own bracket**. That is what makes the halving work: without it,
  `step`'s new bracket `[value, hi]` would have no fixed relation to the old `[lo, hi]`.

  ═══ ⚠ SCOPE ═══

  This is about `gonshor`'s *own* bracket, not about any target real. Nothing here says a
  given sign sequence converges to a given `α` — that needs the sequence to be *the* sign
  expansion of `α`, which `SignSequence.lean` does not define. What is proved is the rate
  at which the bracket closes, which is the part the Liouville comparison needs and the
  part that was missing.

  -- Ref: [gonshor1986] An Introduction to the Theory of Surreal Numbers, Ch. 2
-/
import QOU.AppendixSurreals.SignSequence

namespace QOU.AppendixSurreals

/-- The **bisection regime**: both bounds exist, the value lies strictly inside them, and
— the clause that does the work — the value is the *midpoint* of its own bracket.

`GonshorState.step` re-establishes this at every step, which is why the bracket halves. -/
structure Bracketed (st : GonshorState) : Prop where
  hasLo : st.hasLo = true
  hasHi : st.hasHi = true
  mid : st.value = (st.lo + st.hi) / 2
  lt : st.lo < st.hi

/-- The bracket width. -/
def GonshorState.gap (st : GonshorState) : ℚ := st.hi - st.lo

/-- **One sign halves the bracket**, and leaves the state in the bisection regime.

Both signs are covered: `+` keeps the upper bound and moves the lower one up to the old
value; `-` keeps the lower bound and moves the upper one down. In each case the new
bracket is exactly one half of the old, because the old value was its midpoint. -/
theorem Bracketed.step (st : GonshorState) (h : Bracketed st) (s : Sign) :
    Bracketed (st.step s) ∧ (st.step s).gap = st.gap / 2 := by
  obtain ⟨hlo, hhi, hmid, hlt⟩ := h
  cases s with
  | plus =>
    -- `hasHi` is true, so `step` bisects upward: new bracket is `[value, hi]`.
    refine ⟨⟨?_, ?_, ?_, ?_⟩, ?_⟩ <;>
      simp only [GonshorState.step, GonshorState.gap, hhi, if_true] <;>
      rw [hmid] <;> ring_nf <;> linarith
  | minus =>
    -- `hasLo` is true, so `step` bisects downward: new bracket is `[lo, value]`.
    refine ⟨⟨?_, ?_, ?_, ?_⟩, ?_⟩ <;>
      simp only [GonshorState.step, GonshorState.gap, hlo, if_true] <;>
      rw [hmid] <;> ring_nf <;> linarith

/-- **`n` signs shrink the bracket by `2ⁿ`.**

This is the rate the trajectory statement needs: prefix length `n` buys a bracket of width
`gap₀ / 2ⁿ`, so the approximant is within `gap₀ / 2ⁿ⁺¹` of anything the bracket still
contains — a dyadic approximation whose denominator is exponential in the prefix length,
which is exactly the quantity a Liouville exponent is measured against. -/
theorem Bracketed.foldl_gap (l : List Sign) :
    ∀ st : GonshorState, Bracketed st →
      Bracketed (l.foldl GonshorState.step st)
      ∧ (l.foldl GonshorState.step st).gap = st.gap / 2 ^ l.length := by
  induction l with
  | nil => intro st h; simpa using h
  | cons s t ih =>
    intro st h
    obtain ⟨hstep, hgap⟩ := Bracketed.step st h s
    obtain ⟨hb, hg⟩ := ih (st.step s) hstep
    refine ⟨hb, ?_⟩
    rw [List.foldl_cons] at *
    rw [hg, hgap, List.length_cons, pow_succ]
    ring

/-- The bracket stays positive, so the rate above is a genuine contraction rather than a
statement about an empty interval. -/
theorem Bracketed.gap_pos {st : GonshorState} (h : Bracketed st) : 0 < st.gap := by
  have := h.lt
  simp only [GonshorState.gap]
  linarith

/-! ### ⚠ Non-vacuity — without this the whole module proves nothing

Everything above is conditional on `Bracketed`. If no state reachable from
`GonshorState.init` ever satisfied it, all of it would be vacuously true and the module
would be an instance of exactly the degeneracy
`docs/audits/2026-08-09-inhabitation-is-a-weak-discriminator.md` catalogues — a statement
whose *form* suggests content it does not carry.

So the regime is exhibited, not assumed. `[+, -]` is the shortest sign sequence that
brackets: `+` steps to `1` with no upper bound, then `-` finds `hasLo` set and bisects,
producing `1/2` inside `(0, 1)`. -/

/-- **The bisection regime is reached**, by the shortest sequence that reaches it. -/
theorem bracketed_plus_minus :
    Bracketed ([Sign.plus, Sign.minus].foldl GonshorState.step GonshorState.init) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    norm_num [GonshorState.step, GonshorState.init]

/-- **The rate, on a concrete sequence.**  Extending `[+, -]` by `k` further signs leaves a
bracket of width `2⁻ᵏ`, since `[+, -]` brackets `(0, 1)` at width `1`.

This is the statement a Liouville comparison consumes: prefix length controls approximation
quality exponentially, with the dyadic denominator that `2ⁿ` names. -/
theorem gap_after_plus_minus (l : List Sign) :
    ((Sign.plus :: Sign.minus :: l).foldl GonshorState.step GonshorState.init).gap
      = 1 / 2 ^ l.length := by
  have h := (Bracketed.foldl_gap l _ bracketed_plus_minus).2
  have hg : ([Sign.plus, Sign.minus].foldl GonshorState.step GonshorState.init).gap = 1 := by
    norm_num [GonshorState.step, GonshorState.init, GonshorState.gap]
  -- Rewrite `h` BEFORE simping: `simpa [hg]` normalises the `foldl` on both sides first,
  -- after which `hg`'s literal `[Sign.plus, Sign.minus].foldl` no longer matches anything.
  rw [hg] at h
  simpa using h

end QOU.AppendixSurreals
