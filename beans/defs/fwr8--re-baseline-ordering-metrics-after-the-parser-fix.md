---
# fwr8
title: 're-baseline every ordering metric after the manifest parser fix'
status: completed
type: task
priority: normal
created_at: 2026-08-10T01:50:00Z
updated_at: 2026-08-10T01:50:00Z
parent: fwr6
---
folio-assistant #99 fixed a manifest parser that hid **45 of 3498 blocks** from
`loadChapterGraph`: a `]` inside a comment truncated the `blocks: [...]` array,
and every block below it lost its position. A block with no position reads as
"not listed" and returns `pass`, and edges pointing at it are skipped — so the
detangler reported clean on material it had never looked at. The reverse also
bit: a slug quoted inside a comment counted as a real entry, shifting every later
position in its chapter by one.

**Everything measured before that fix is wrong by an unknown few.** On the same
tree the paper reads **192 with the old parser, 195 with the new one** — three
real forward references were hidden behind the truncation, and the arc's starting
figure of 274 was understated the same way.

What needs redoing, in order:

1. **Re-run `detangler-no-forward-ref` corpus-wide** and record the true count.
   Cheap; one sweep.
2. **Re-check the 45 previously-invisible blocks specifically.** They have never
   been through the forward-ref criterion at all, so any finding there is new,
   not a regression. `braids-and-knots` (16) and `climax-volume-mass` (13) hold
   most of them.
3. **Re-check the chapters where a slug-in-a-comment shifted positions** —
   `knots-particles-confinement` and `nuclear-interactions` each counted one
   phantom entry, so every distance measured in them was off by one.
4. **Correct the arc's headline figures** in `fwr1`-`fwr6` rather than leaving
   the old numbers standing as if they had been measured.

The adjudications, reviews and moves from that arc are unaffected — they turned
on reading, not on the count. Only the numbers move.

---

**Outcome: the arc's headline is 274 -> 195. The start was right; the end was
understated by 3.**

Measured both endpoints with the fixed parser, in a worktree at the arc's base
commit `7e45748e82`:

| point | old parser | fixed parser |
|---|---|---|
| arc base | 274 | **274** |
| arc tip | 192 | **195** |

So my earlier claim that "the starting figure of 274 was understated the same
way" is **wrong**, and worth correcting rather than quietly restating. At the
base, 26 blocks were already invisible to the checker (braids-and-knots 16,
stochastic-mechanics 6, quantum-observable-universes 4) — but not one of them was
the source or the target of a forward reference, so the count was unaffected.

The divergence appeared **during** the arc. `main` landed a comment reading
"...and it has `uses: []` today" inside a `mass-theory` section array, and
another in `climax-volume-mass`, hiding 25 further blocks — and those *are*
forward-reference targets. Every figure quoted after that commit landed (200,
193, 192) is short by 3; every figure before it is exact.

**The three newly-visible findings**, all in `mass-theory`, all edges *pointing
at* a hidden block (an unpositioned target is skipped, so they were never
checked):

| d | edge |
|---|---|
| 524 | `rem:motivic-mass-rationale` -> `prop:mass-endomorphism-tower` |
| 212 | `prop:rigid-monoidal-structural-gap-invariance` -> `prop:spin-involution-lp-dual-invariance` |
| 151 | `prop:markov-pair-z2` -> `rem:mass-endomorphism-jet-tower` |

**Two of the three are already on the `fwr7` list.** They were found by an agent
reading the manifest with its own parser while the detangler was blind to them —
which is a point in favour of the reading passes, not just against the tool.

Zero forward references are *sourced* from a previously-invisible block: the 51
hidden blocks are themselves well-ordered. The damage was entirely on the target
side.

**The phantom entries deserve their own note.** The old parser did not just
invent labels — it invented fragments of section titles and prose caught between
quotes inside comments, e.g. `"Skein Generation and // Particle Correspondence :
generation"`. Six of them across the corpus, each occupying a position and
shifting every block after it in that chapter by one. One, in
`climax-volume-mass`, was a real label (`def:crossing-energy`) mentioned in a
comment, which is the case most likely to have produced a plausible-looking
wrong answer rather than an obviously broken one.
