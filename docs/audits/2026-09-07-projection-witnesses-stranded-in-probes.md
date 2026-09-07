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

`BarEvenKernel` was a twelfth *by this scan's arithmetic*, and the correction
below shows that is the wrong way to read it: its witness was at the class's
*intended point* and non-degenerate, which none of the eleven are. It was moved
into the content-block sibling in PR #7125, which is why it is not in the list.

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

## 🛑 CORRECTION, same day: it is not "at least four". It is ALL ELEVEN.

The paragraph below originally closed *"`BarEvenKernel`'s witness was worth
relocating, and at least four of the others demonstrably are not."* That number
was written having read **one** of the three probes. Reading all three, and
inspecting each instance rather than trusting the headers:

**Every one of the 11 is a satisfiability demonstration at degenerate data.
None is a witness at an intended point. Not one is relocatable.**

| class | the witness | probe |
|---|---|---|
| `DirectionSanityGateClass` | `… 0` | gate-classes-admit-zero |
| `MassAnchorStableGateClass` | `… 0` | gate-classes-admit-zero |
| `MassDirectionSanityGateClass` | `… 0` | gate-classes-admit-zero |
| `HasMarkovTrace` | `probeParticle 0`, `value := 0` | context-classes |
| `HasFrobeniusStability` | `frobStabZero`, `sigma := fun _ => 0` | context-classes |
| `LpDualStabilityContext` | `q := 0`, `κ_G := 0`, `y_star := 0` | context-classes |
| `HasFiniteLPDuality` | `emptyLP` | context-classes |
| `ParityRegimeSelectionContext` | `Z := 0`, `N := 1`, `a := b := 0` | context-classes |
| `HasBindingMultiplicity` | `probeShell`; its own docstring: *"the pair is jointly vacuous"* | context-classes |
| `FourTermPairNucleonContext` | *"a lookup table keyed on one bit satisfies both claims"* | context-classes |
| `H2SAngleS3HolonomyConjecture` | `⟨0, 0⟩` — its own text: *"the degenerate datum"* | h2s-and-the-inert-radius-gate |

Each probe says so in its own header. `context-classes-hand-adjudicated.lean`:
*"A class inhabited with no hypotheses constrains nothing … every class below
backs a declaration that projects."* These files were written to establish
**vacuity**. Their instances are the evidence for a negative result.

**So the correct framing is the opposite of the one this document opened with.**
`BarEvenKernel` was not "a twelfth" in a population of relocatable witnesses —
it is the **sole exception in the corpus**, the only probe-built witness that
sat at its class's intended point. The other eleven look identical to a
scanner and are the reverse in meaning.

That is also why the `--probes` flag prints a warning rather than a count:
measured, the probe-only bucket is **11 vacuity demonstrations and 0 usable
witnesses**, so treating "has a probe witness" as good news would be wrong
eleven times out of eleven.

## What this does NOT establish

The 29 with no builder anywhere are **not** thereby defects. A conjecture
carrier with no instance is the honest §3b-tax shape for an unproved primary.
What the split gives is the question to ask per case — *is this class meant to
be inhabited?* — not a verdict.

And the 11 are not thereby cleared either: they are confirmed vacuous by the
probes above, which is a finding about them, not an absolution.
