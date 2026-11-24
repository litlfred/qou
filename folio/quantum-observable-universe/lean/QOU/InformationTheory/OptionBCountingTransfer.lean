import Mathlib.Tactic

/-!
# QOU.Information.OptionBCountingTransfer — the non-fiat transfer, analysed

Option B (the *native* reading): the observation trace computes the `#P` count
`J_L(q₀)`.  We get counting-hardness for free — but the question is whether any
route to `P ≠ NP` exists that is **not by fiat** (not just *assuming* the
degree-0 = decision identification).

The decisive fact, formalised here: **the generic transfer "counting-hard ⟹
decision-hard" is FALSE.**  The witness is the **permanent / perfect matching**:

* counting perfect matchings is `#P`-complete (Valiant 1979), yet
* deciding whether a perfect matching *exists* is in `P` (König /
  Hopcroft–Karp).

So a `#P`-hard count can sit on top of a poly-time decision.  Any transfer from
"the QOU trace is `#P`-hard" to "`P ≠ NP`" therefore **cannot** be a generic
principle — it must exploit QOU-specific structure that the matching problem
lacks.  That is exactly what "not by fiat" would require, and no such structure
is known.

## What a non-fiat transfer would actually need

To get `P ≠ NP` honestly from Option B you would need a **decision lower
bound** on a specific QOU-encoded `NP`-complete problem `L`:

1. **Encode** an `NP`-complete `L` as a family of links `β_{L,n}` so that
   deciding `L` reduces to reading `J_{β_{L,n}}(q₀)` — this exists (JVW-style
   reductions of `NP`-hard problems into Jones/Tutte evaluations).
2. **Prove `L` has no poly-time decider** — i.e. that deciding `L` genuinely
   requires the degree-0 obstruction, with *no shortcut* of the matching kind.
   This step is a circuit/TM lower bound; it is `P` vs `NP` itself, and the
   Razborov–Rudich natural-proofs barrier blocks any uniform/relativizing
   argument (which a "works at every non-torsion q₀" argument is).

Step 1 is real and reusable; **step 2 is the wall**, and it is not the trace's
counting-hardness — that is step 0, already free.

## The one physically-motivated non-fiat candidate (weaker than P vs NP)

The corpus's **Bekenstein / bandwidth** bound (`𝔅(q) = qη_q/(q-1)²` q-bits per
Planck step; the computational horizon is where the effective tree exceeds the
polynomial bandwidth budget) is an *information* lower bound.  It could give a
genuine, non-fiat lower bound — but only in a **bandwidth-limited (physical)**
model of computation, not for abstract Turing machines.  It would prove a
*physical Church–Turing*-style statement ("no bandwidth-limited device decides
`L` in poly time"), which is **strictly weaker** than abstract `P ≠ NP`.  That
is the honest ceiling of the non-fiat route.
-/

namespace QOU.Information

/-- Counting perfect matchings is `#P`-hard (Valiant). -/
opaque matchingCountHard : Prop

/-- Deciding whether a perfect matching exists is in `P` (König /
    Hopcroft–Karp) — i.e. matching-decision is *not* hard. -/
opaque matchingDecisionEasy : Prop

/-- **Cited facts about perfect matching** (no instance — established, and
    Mathlib has no `#P`).  Both hold simultaneously: a `#P`-hard count over a
    poly-time decision. -/
class MatchingFacts : Prop where
  /-- Valiant: the permanent / matching count is `#P`-hard. -/
  count_hard : matchingCountHard
  /-- König: matching *existence* is decidable in polynomial time. -/
  decision_easy : matchingDecisionEasy

/-- A **generic** counting→decision transfer would assert, for the matching
    problem, that its `#P`-hard count forces its decision to be hard (i.e. not
    easy). -/
def GenericTransfer : Prop := matchingCountHard → ¬ matchingDecisionEasy

/-- **The generic counting→decision transfer is FALSE (sorry-free).**  Perfect
    matching has a `#P`-hard count *and* a poly-time decision, so
    counting-hardness cannot imply decision-hardness in general.  Hence any QOU
    route from "trace is `#P`-hard" to "`P ≠ NP`" must use QOU-specific
    structure — it can never be the generic principle.  This is why Option A's
    degree-0 identification, read as a general law, is refuted, and why a
    *non-fiat* transfer needs a genuine decision lower bound. -/
theorem generic_transfer_false [M : MatchingFacts] : ¬ GenericTransfer :=
  fun transfer => transfer M.count_hard M.decision_easy

/-- The exact observation trace `J_L(q₀)` is `#P`-hard (JVW at non-torsion). -/
opaque traceCountHard : Prop

/-- **What the QOU trace gives, honestly (Option B, no instance).**  Its exact
    evaluation is `#P`-hard; that is counting-hardness, and it is *all* the
    trace supplies.  The step to `P ≠ NP` is a separate decision lower bound
    (`generic_transfer_false` shows it is not automatic), left open. -/
class QOUTraceCountHard : Prop where
  /-- The trace's exact value is `#P`-hard. -/
  holds : traceCountHard

end QOU.Information
