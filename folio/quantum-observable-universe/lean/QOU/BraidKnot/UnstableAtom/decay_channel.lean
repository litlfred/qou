import Mathlib.Tactic

/-!
# `QOU.BraidKnot.UnstableAtom.decay_channel` — intentionally empty; the formalisation lives in the content-block sibling

This module used to hold `DecayChannelContext` together with a projection
that discharged all three manuscript sub-claims from that class's own fields.
Both are removed (2026-08-31).  It is the fifteenth and last of the drained
library shells for bean `qou-z9ws`, and it was **held back** from the first
fourteen because its sibling's docstring said the opposite of the pattern:

> *"The **substantive** Lean encoding (the `DecayChannelContext` class plus
> the `decay_channel` conditional result) lives at the **canonical library
> path** `QOU/BraidKnot/UnstableAtom/decay_channel.lean`."*

That claim was wrong twice.

**Unreachable.**  Per AGENTS.md §0a a block's `lean.ref` resolves to the
**sibling first**, and the sibling
[`mass-theory/unstable-atom-decay-channel.lean`](../../../mass-theory/unstable-atom-decay-channel.lean)
exists — so `qou:QOU.BraidKnot.UnstableAtom.decay_channel` resolved there,
never here.  Worse, the sibling declared `decay_channel_unique` and no
`decay_channel`, so the ref named a declaration that existed only at a path
resolution could not reach.

**Not substantive.**  `DecayChannelContext` carried `Z`, `N`, `q`,
`PartitionIdx`, `lam_star`, `E_lambda`, `on_boundary`, `lam_alt`, `q_1`,
`q_2` **and** all three sub-claims as its own fields, and `decay_channel`
returned the three claim fields as a triple.  Since the data were fields the
instance chose them: `on_boundary := fun _ => True` makes sub-claim (ii)
vacuous (`¬ True` is false), `q_1 := 1, q_2 := 0` makes (iii) vacuous, and
`E_lambda := 1` discharges (i).  So a `[DecayChannelContext]` binder assumed
nothing — AGENTS.md §3b-cond item 5.

**The sibling now carries the encoding, under the name the ref names**, and
sub-claim (iii) is **derived** there rather than assumed: *"stable at `q₁`,
unstable at `q₂` implies `∃ q* ∈ [q₁, q₂]` with `E(λ*, q*) = 0"* is the
intermediate value theorem for a continuous energy, which is what the
manuscript's own Connection-to-phase-boundary paragraph argues.  Sub-claim
(ii) is derived from the LP-duality selection input, and what is not encoded
— sub-claim (i)'s LP construction, the boundary variety, continuity of `E` —
is stated there rather than implied.

**Nothing imports this module**, and nothing else in `content/` names the
class (measured 2026-08-31 across every `.lean` in the tree).

The file is kept rather than deleted so that the `lean.ref`'s second
resolution candidate —
`<lakeRoot>/QOU/BraidKnot/UnstableAtom/decay_channel.lean` — still exists as
a real path.

Bean `qou-z9ws`; `docs/audits/2026-08-30-the-remainder-is-vacuous-not-open.md`.
-/
