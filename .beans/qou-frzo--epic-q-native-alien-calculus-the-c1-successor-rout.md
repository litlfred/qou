---
# qou-frzo
title: 'EPIC: q-native alien calculus — the C1 successor route the RSZ closure names'
status: in-progress
type: milestone
priority: normal
created_at: 2026-09-07T06:24:35Z
updated_at: 2026-09-07T06:27:44Z
---

Owner directive 2026-09-07: *"Take up idle as relevant. Do q-native alien calculus.
What is workplan. Bean up and roast."*

Parent of `qou-wgnx` and `qou-odh5` (both taken up today; both were ~30 d idle with
`status: in-progress`). Successor to the RSZ slope-½ chain closed 2026-08-08.

---

# 🔥 THE ROAST — written BEFORE the plan, so the plan has to survive it

Owner asked for a roast. Standing critical-distance licence, applied to my own
proposal. **Seven objections, ordered by how likely they are to kill it.**

## R1. The corpus has a LOT of alien machinery, and that is a reason for suspicion, not comfort

`AlienDerivation.lean`, `AlienBridgeEquation.lean` (13 thms), `QAlienBridgeEquation.lean`
(~25 thms), `BorelLaplace`, `BorelWatson*` (×8), `BorelSingularity`, `QBorelResummation`
(14 thms). That is a large, mostly sorry-free surface built over months.

**And the arc it serves has produced no wired result.** If that much machinery has not
moved a single L2 number, the bottleneck is not more machinery. A plan whose first
instinct is "build more Lean" is answering the question the corpus has already
answered five times over.

**The `qbs4` scrap text says this in the corpus's own words:** *"not a session brick."*

## R2. The classical bricks may be worse than useless — they are ATTRACTIVE and WRONG

The closure audit is explicit that C1 **cannot** be confluenced to the classical
setting and handed to Écalle. So every classical-only brick in the list above is a
**trap**: it compiles, it is sorry-free, it looks applicable, and it silently assumes
a limit that does not exist here.

This is the exact failure this session already committed twice at smaller scale —
`RamifiedShiftCalculus` cited as absent while present, and the RSZ chain cited as live
while retired. **A sorry-free Lean file is not evidence that it applies to your
object.** Until each brick is triaged q-native vs classical-only, the machinery count
is a liability.

## R3. The one concrete alien number rests on an unsupported identification

`A_ω = 4√2·e^{−3/8}` at `ω₀ = 1/√2`, `A₂ = 1/4` — probe-verified and explicitly **NOT
wired**. Bean `qou-q3np` records that the `A_ω → S` identification is
**literature-unsupported**, and AGENTS.md §13a cites that bean as the type case of a
conjecture that must not be closed.

So the headline datum is a number in search of a theorem. Wiring it would be exactly
the laundering the anti-fit rules forbid.

## R4. ANTI-FIT is the hardest constraint here, and alien calculus is the most fit-prone place in the corpus

`qou-qbs4`'s own scrap text: *"ANTI-FIT (hard). `U` must be DERIVED. Two constants
tuned so a downstream number lands is a fit, must be labelled one, and may NOT be
wired as canonical. The Q_β `Φ₂` precedent — the forbidden seventh ansatz — applies
directly."*

Alien calculus **produces Stokes constants**. Its whole output shape is "a small number
of constants that fix the resummation." That is the shape the corpus has ruled against
six times on Δ_λ. **The route's natural deliverable is the corpus's forbidden object.**
Any plan must say up front how a derived constant is distinguished from a fitted one —
and if it cannot, the plan is a fit generator.

## R5. The motivation cites a scoreboard that is 0/5

`qou-odh5`: *"the c₃ closure is the shared root of three of the five L2 misses."*
But AGENTS.md records the honest L2 count as **0/5 unconditional parameter-free** —
the single "scoreable win" is truncation-fitted and α_em-`sorry`-conditional.

So "closing c₃ fixes 3 of 5" is a claim about a denominator that does not survive its
own audit. The motivation is inherited from a framing the corpus has since corrected.
**Not fatal — c₃ may still be worth closing — but the stated payoff is overstated and
must not be repeated in a PR body.**

## R6. My own track record on the adjacent problem, this session

I closed **five** routes to `REV` (extensivity, cumulant expansion, polynomial `Var`,
palindromicity, spectrum limit-shape) and cracked none. `REV` is a **vastly** smaller
problem than q-native alien calculus: one scalar sequence, exact combinatorics
available, no new formalism required.

**A plan that treats q-native alien calculus as tractable in the same sessions that
could not settle `REV` is not calibrated.**

## R7. "q-native" has no agreed definition here, and that is where the plan will rot

Nobody has said what would COUNT as a q-native alien derivation. Without a falsifiable
acceptance criterion, the work drifts into "build q-analogues of classical lemmas
until something looks like Écalle" — months of sorry-free Lean that nothing consumes,
which is R1 again one level down.

**The first deliverable must be the acceptance criterion, not a lemma.**

---

## What survives the roast

Not nothing, and the honest residue is narrow:

- **The negative is solid.** RSZ is closed for a stated, checkable reason (§3.3 is
  integral-slope-only). That is real and already banked.
- **The direction is the corpus's own**, not mine: the closure audit argues alien
  derivations need no slope filtration, which is precisely why they survive where RSZ
  died.
- **`REV` is genuinely Borel-plane structure**, so the deuteron work and this arc do
  meet — that convergence was measured today, not asserted.

**Therefore the plan below is deliberately NOT "build q-native alien calculus."** It is
the smallest sequence that would tell us whether that is even the right target, with
each step falsifiable and cheap, and with the anti-fit gate stated before any constant
is computed. Plan follows in the next update, after the corpus-grep returns.


---

# The acceptance criterion for "q-native" (R7's demand, answered first)

R7 says the plan rots without a falsifiable definition of the target. So here it is,
**before any lemma**. A construction counts as a **q-native alien derivation** iff all
four hold:

**(A) Domain.** It is defined for a q-Gevrey series of the corpus's actual class —
`deg_q(c_n) = n²` (proved for C1, `C1InfDegreeLaw`) — and **not merely** for classical
Gevrey-1. A construction that needs `n!`-type growth is classical machinery wearing a
`q`.

**(B) Twisted Leibniz.** Its product rule is stated and proved for the **σ-twisted**
product — `Δ(fg) = Δ(f)·g + σ(f)·Δ(g)` with `σ` the q-shift `f(z) ↦ f(qz)` — not the
untwisted classical rule. The classical rule must be recovered only in a limit the
construction never takes.

**(C) Commutation with the q-difference operator, not `d/dz`.** Classically the
alien derivative is normalised so `Δ̇_ω = e^{−ωz}Δ_ω` commutes with `d/dz`. The
q-native statement must commute (up to the analogous twist) with `σ_q`. **This is the
criterion that RSZ failed** — its machinery is filtration-based, and the closure audit's
whole point is that alien derivations need no filtration.

**(D) No archimedean or confluence dependence in the import cone.** MECHANICALLY
CHECKABLE, and this is the one that makes the criterion real rather than rhetorical:
nothing in the cone may assume continuity in `z`, a `q → 1` limit, or a classical
Borel-plane geometry. The closure audit states C1 **cannot** be confluenced, so any
such dependence is a silent falsehood.

## Why (D) is the load-bearing one

(A)–(C) are mathematical judgements a reviewer must make. **(D) is a static analysis a
script can run**, and it converts R2 — "the classical bricks are attractive and wrong" —
from a worry into a measurement.

That gives the epic its first brick, and it is deliberately **not** a formalization:

> **Brick 0 — triage the existing alien/Borel surface q-native vs classical-only, by
> import cone and by whether each statement quantifies over a q-difference operator at
> all.**

Cheap, falsifiable, no new mathematics, and it either de-risks the largest objection or
kills the route early. If Brick 0 finds the surface is classical-only, then the corpus's
"large alien machinery" is a liability rather than an asset, R1 and R2 both bite hard,
and the honest report is that this frontier is much further away than the file count
suggests.

**Note what Brick 0 is NOT:** it is not "check the files are sorry-free." They already
are. Sorry-freeness says the proofs are complete; it says nothing about whether the
statements apply to a q-difference object. That distinction is the whole of R2.
