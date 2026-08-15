# Prune-restoration tranches — index, and why size is the wrong order

Generated 2026-08-15. Bean `prn1`. **Nothing is restored by any of these.**

`2026-08-15-prune-damage-redrive.md` established that the damage cuts far better
by **target** than by source: 692 still-lost edges across 320 blocks become a few
dozen questions when you ask "must a reader have read `T` first?" once per `T`.
These are the twelve largest, covering **153 of the 692 still-lost edges**.

| # | target | sources | prose-linked | would point forward | sheet |
|---|---|---|---|---|---|
| 1 | `thm:jones-markov-trace` | 21 | 2 | 0 | [sheet](2026-08-15-tranche-1-jones-markov-trace.md) |
| 2 | `def:hecke-normal-form` | 20 | 1 | 0 | [sheet](2026-08-15-tranche-hecke-normal-form.md) |
| 3 | `def:borromean-baryon` | 16 | 0 | **4** | [sheet](2026-08-15-tranche-borromean-baryon.md) |
| 4 | `def:crossing-energy` | 12 | 3 | 1 | [sheet](2026-08-15-tranche-crossing-energy.md) |
| 5 | `rem:conway-normal-form` | 11 | 2 | 0 | [sheet](2026-08-15-tranche-conway-normal-form.md) |
| 6 | `def:habiro-ring` | 11 | 0 | 1 | [sheet](2026-08-15-tranche-habiro-ring.md) |
| 7 | `def:motivic-substrate` | 11 | 2 | 1 | [sheet](2026-08-15-tranche-motivic-substrate.md) |
| 8 | `def:archimedean-realization-functor` | 11 | 2 | 0 | [sheet](2026-08-15-tranche-archimedean-realization-functor.md) |
| **9** | **`def:q-from-epsilon`** | 10 | **5** | **0** | [sheet](2026-08-15-tranche-q-from-epsilon.md) |
| 10 | `def:hadron` | 10 | 0 | 0 | [sheet](2026-08-15-tranche-hadron.md) |
| 11 | `def:categorical-neutron` | 10 | 3 | 1 | [sheet](2026-08-15-tranche-categorical-neutron.md) |
| 12 | `def:categorical-proton` | 10 | 2 | **2** | [sheet](2026-08-15-tranche-categorical-proton.md) |

153 sources. **22 carry a prose link to the target they omit from `uses[]`** — the
block's own two halves contradicting each other, which is a defect rather than a
matter of taste. **10 of 153 would point forward if restored.**

## Start with tranche 9 — and it indicts the earlier restoration

`def:q-from-epsilon` has **the highest prose-link rate of any tranche by far**
(5 of 10, against a next-best of 3 of 12) and **nothing points forward**, so it
is ordering-safe wholesale.

What makes it more than a good candidate is *which* five link. From the re-drive,
six blocks had edges re-declared since the prune: `rem:yang-mills-surreal-bound`
(6), `rem:p-vs-np-surreal-bound` (6), `rem:rh-surreal-bound` (4),
`rem:millennium-unification` (3), `rem:bsd-surreal-bound` (3), `conj:p-vs-np-qou`
(2).

**Five of those six are exactly the five whose prose links to
`def:q-from-epsilon`.** Someone went through these blocks, restored 3–6
dependencies to each, and omitted in every case the one their own narrative
sends the reader to. That is not five independent editorial judgements; it is one
systematic gap in the restoration pass, visible five times.

The blocks that *don't* link are the ones that pass never reached:
`rem:ns-surreal-bound` (declares nothing), `prop:surreal-rate-calculus`,
`rem:adelic-tate-squeeze`, `rem:ns-blowup-physical-evidence`, and the
least-restored family member `conj:p-vs-np-qou`.

## Restoring an edge can create a forward reference — measured, not assumed

`uses[]` pointing at a block later in the same chapter is what
`detangler-no-forward-ref` counts, and what the `fwr` arc spent five PRs cutting
from 274 to 194. Restoration adds `uses[]` entries, so **a correct restoration can
silently undo a different piece of correct work.**

The concrete case: `def:crossing-energy` was relocated into
`knots-particles-confinement` **§8** on 2026-08-09 *so that* the electroweak
results would stop forward-referencing their own definitions.
`prop:hadron-exists`, one of the blocks that lost the edge to it, sits at
within-chapter **21** against `crossing-energy`'s **87**. Restoring that edge
recreates exactly what the relocation removed.

Every sheet costs this per source via `pointsForward`, exported from
`qa-checkers-extended.ts` so nobody hand-rolls a third manifest parser (the
duplication `fsl7` exists to prevent). It answers `n/a` when either block is
unplaced: **unknown, not safe.**

## The order

**Nine of the twelve tranches are ordering-safe wholesale** — tranches 1, 2, 5,
8, 9, 10 have zero forward edges, and 4, 6, 7, 11 have exactly one apiece.
Only **10 blocks in all 153** need individual handling, each wanting
`foreshadows[]`, a relocation, or a deliberate decision to accept the edge.

Recommended order, by evidence rather than size:

1. **`def:q-from-epsilon`** (5/10 linked, 0 forward) — above.
2. **`def:crossing-energy`** (3/12, 1 forward) — `rem:commutative-crossing-energy`
   both links in prose *and* references the declaration in Lean.
3. **`def:categorical-neutron`** (3/10, 1 forward).
4. **`thm:jones-markov-trace`** (2/21, 0 forward) — the largest, and free of
   ordering risk.
5. Then tranches 5, 7, 8, 12, 2.
6. **Last: `def:borromean-baryon` (3), `def:habiro-ring` (6), `def:hadron` (10)**
   — no prose links at all between them, and `borromean-baryon` carries 4 of the
   10 forward edges. Being large is the worst reason to do one of these first.

## Two cautions on reading the sheets

- **Tranche 2's mention column.** Bare "normal form" is generic and appears for
  unrelated reasons. Only the three blocks matching **"hecke normal form"**
  exactly carry weight.
- **The `lean` column is never corroboration.** It reports the *formal* relation,
  which is not the editorial one and diverges from it legitimately. `uses[]` must
  never be populated from Lean.

## What none of this decides

Whether the edge belongs. The prune applied a mechanical rule across a corpus
without reading, and restoring mechanically repeats it in the opposite direction
— at least one removal is known deliberate (`def:adelic-substrate` lost
`def:classical-limit-functor` by owner decision in `78a570365d`, and restoring it
re-opens a cycle). The `uses-editorial-review` two-reader standard governs what is
applied. These sheets remove the busywork from that reading and guarantee it
cannot quietly cost the paper its ordering.

Regenerate any sheet: `bun run scripts/prune-tranche-sheet.ts <target-label>`.
