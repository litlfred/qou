# Prune-restoration tranches — index and the one caveat that gates all of them

Generated 2026-08-15. Bean `prn1`. **Nothing is restored by any of these.**

`2026-08-15-prune-damage-redrive.md` established that the damage cuts far better
by **target** than by source: 692 still-lost edges across 320 blocks become a
few dozen questions when you ask "must a reader have read `T` first?" once per
`T`. These are the first four, largest first.

| # | target | sources | prose-linked | mention only | sheet |
|---|---|---|---|---|---|
| 1 | `thm:jones-markov-trace` | 21 | **2** | 4 | [sheet](2026-08-15-tranche-1-jones-markov-trace.md) |
| 2 | `def:hecke-normal-form` | 20 | **1** | 8 | [sheet](2026-08-15-tranche-hecke-normal-form.md) |
| 3 | `def:borromean-baryon` | 16 | **0** | 4 | [sheet](2026-08-15-tranche-borromean-baryon.md) |
| 4 | `def:crossing-energy` | 12 | **3** | 6 | [sheet](2026-08-15-tranche-crossing-energy.md) |

69 sources, **6 with a prose link to the target they omit from `uses[]`** — the
block's own two halves contradicting each other, which is a defect rather than a
matter of taste. Around 22 more mention the concept without linking; that is
where a reader's judgement actually decides something.

## The caveat that gates application: restoring an edge can CREATE a forward reference

This is the interaction with the `fwr` arc, and it is not hypothetical.

`uses[]` pointing at a block positioned *later* in the same chapter is a forward
reference — the thing `detangler-no-forward-ref` counts and the arc has spent
five PRs reducing from 274 to 194. Restoring a pruned edge adds a `uses[]`
entry, so **some restorations will push that number back up.**

Concretely, from tranche 4: `def:crossing-energy` was relocated into
`knots-particles-confinement` **§8** on 2026-08-09, precisely so the
electroweak results would stop forward-referencing their own definitions. One of
the blocks that lost the edge to it, `prop:hadron-exists`, sits in **§3** of the
same chapter. Restoring `prop:hadron-exists → def:crossing-energy` would create
exactly the kind of forward reference that relocation was performed to remove.

So each tranche needs a third question after the two editorial ones:

1. Must a reader have read `T` before this block? (the tranche question)
2. Is this particular source an exception? (the per-source reading)
3. **Does restoring it point forward, and if so, is that acceptable or does the
   block need `foreshadows[]` — or does something need to move?**

Question 3 is mechanical and should be automated before any tranche is applied.
It is not automated yet: the position map lives in `loadChapterGraph`, which is
private to `qa-checkers-extended.ts`, so a consumer that wants to ask "where is
this block?" has no accessor and would have to hand-roll a second manifest
parser. That is the exact duplication `fsl7` exists to prevent and `#116` just
finished undoing, so the right move is an accessor on the platform side, not a
second parser here.

**Until question 3 can be answered mechanically, no tranche should be applied
in bulk** — not because the editorial reading is unsound, but because a correct
restoration can silently undo a different piece of correct work.

## Tranche notes

- **Tranche 2 (`def:hecke-normal-form`)** — read the mention column carefully.
  "normal form" alone is generic and appears for unrelated reasons; the strong
  hits are the three blocks matching **"hecke normal form"** exactly
  (`prop:gb-spectral-sequence`, `def:confinement-level`,
  `prop:gb-residue-spectral-sum`). The bare "normal form" matches are weak
  evidence and should not be treated as corroboration.
- **Tranche 3 (`def:borromean-baryon`)** — the weakest of the four and worth
  saying so: **no source links to it**, and 10 of 16 have no `.lean` at all.
  It is a narrative cluster of remarks, an example and a simulator. This tranche
  is a genuine reading question with almost no mechanical signal, so it should
  not be done first merely because it is large.
- **Tranche 4 (`def:crossing-energy`)** — the strongest: 3 of 12 link, 6 of 12
  mention, and `rem:commutative-crossing-energy` both links in prose *and*
  references the declaration in Lean. It is also the tranche where the
  forward-reference caveat bites hardest, per above.

The `uses-editorial-review` two-reader standard governs what is applied.
