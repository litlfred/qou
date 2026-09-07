# The inhabitation checker scanned `content/` only — 11 classes read as uninhabited that are not

**2026-09-07.** Beans `qou-z9ws`, `qou-9yt9`.

## The claim

[`scripts/lean-carrier-inhabited-check.py`](../../scripts/lean-carrier-inhabited-check.py)
answers the discriminator the vacuity ledger uses for a self-assuming
projection: *a projection is the legitimate Mathlib accessor idiom only when
something BUILDS the bundle.* Its `builders()` defaulted to `root="content"`,
so a witness anywhere else was invisible and the carrier came back
**UNINHABITED** — the finding-shaped answer.

That is the second blind spot in this one script, and both point the same way.
The first was a line-anchored grep that missed instances whose result type sits
four lines below the keyword; it reported a false zero for
`SkeinMultisetInvariant`, which is inhabited. This is the same defect one level
out: not *how* the declaration is written, but *where the file lives*.

## The measurement

Over the 58 distinct classes appearing as instance binders behind the corpus's
flagged `proof-no-self-assuming-projection` rows:

| | classes |
|---|---|
| built inside `content/` | **18** |
| built **only** outside it | **11** |
| no builder anywhere | **29** |

Every one of the 11 sits in a probe fragment that, by its own header, has no
imports and is imported by nothing:

| probe | classes |
|---|---|
| `docs/audits/2026-08-30-context-classes-hand-adjudicated.lean` | 7 |
| `docs/audits/2026-08-30-gate-classes-admit-zero.lean` | 3 |
| `docs/audits/2026-08-31-h2s-and-the-inert-radius-gate.lean` | 1 |

The 11: `DirectionSanityGateClass`, `FourTermPairNucleonContext`,
`H2SAngleS3HolonomyConjecture`, `HasBindingMultiplicity`, `HasFiniteLPDuality`,
`HasFrobeniusStability`, `HasMarkovTrace`, `LpDualStabilityContext`,
`MassAnchorStableGateClass`, `MassDirectionSanityGateClass`,
`ParityRegimeSelectionContext`.

`BarEvenKernel` was a twelfth. Its witness — at its *intended point*, and
non-degenerate — was moved into the content-block sibling in PR #7125, which is
why it is not in the list.

## 🛑 The fix is to report WHERE, not to widen the search

Scanning everything and printing one count would be **worse than the bug**, and
`2026-08-30-gate-classes-admit-zero.lean` is why. Its instances are
`DirectionSanityGateClass 0`, `MassAnchorStableGateClass 0`,
`HasFiniteLPDuality emptyLP`, `HasMarkovTrace probeParticle 0`. They were built
to show the gates **admit zero** — a demonstration that they are too weak. That
is a *negative result*.

Counting them as "the bundle is built" converts a negative result into a
certificate of health, which is the laundering `AGENTS.md`
§"Axiomatization is NOT a Proof" forbids. **Do not relocate those witnesses into
`content/`.** `BarEvenKernel` was relocatable precisely because its witness was
at the substrate values the gates were written for, not at values chosen to
make the class inhabited.

A probe witness answers *"is this satisfiable at all"*. A witness at the class
answers *"may a reader treat these projections as accessors"*. They are
different questions, so the script now prints three verdicts and never merges
the counts:

```
 1  BarEvenKernel                            <- built in content/
 0  DirectionSanityGateClass                 <- PROBE-ONLY
 0  ConfinementFrobeniusReciprocityContext   <- UNINHABITED
```

`--probes` opts into the wider scan; without it the behaviour is unchanged.

## What this does NOT establish

The 29 with no builder anywhere are **not** thereby defects. A conjecture
carrier with no instance is the honest §3b-tax shape for an unproved primary.
What the split gives is the question to ask per case — *is this class meant to
be inhabited?* — not a verdict.

And the 11 are not thereby cleared either. Each needs reading against its own
probe: `BarEvenKernel`'s witness was worth relocating, and at least four of the
others demonstrably are not.
