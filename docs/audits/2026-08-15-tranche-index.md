# Prune-restoration tranches — index

Regenerated 2026-08-15 on the **union** editorial graph. Bean `prn1`.

> **Earlier revisions of these sheets are superseded twice over.** Two platform
> changes landed while this audit was being worked, and both revealed declared
> dependencies the graph could not previously see:
>
> - **`extractUses` fix** (folio-assistant #117) — a comment between the
>   previous field's comma and a manifest's `uses:` key made the whole array
>   invisible. 27 blocks, 53 edges.
> - **`interprets` is an editorial edge** (bean `i8ad`, owner decision) — 342
>   authored dependencies were outside the graph entirely.
>
> Any `declares now` count or still-lost total predating these is wrong, and
> wrong in the same direction: it overstated the damage.

**18 edges restored** under this bean. Still-lost now: **581**, down from 785 at
the audit's writing and 658 before `interprets` counted.

| # | target | sources left | prose-linked | forward | sheet |
|---|---|---|---|---|---|
| 1 | `def:hecke-normal-form` | 18 | 0 | 0 | [sheet](2026-08-15-tranche-hecke-normal-form.md) |
| 2 | `def:borromean-baryon` | 15 | 0 | **4** | [sheet](2026-08-15-tranche-borromean-baryon.md) |
| 3 | `def:habiro-ring` | 11 | 0 | 1 | [sheet](2026-08-15-tranche-habiro-ring.md) |
| 4 | `thm:jones-markov-trace` | 10 | 0 | 0 | [sheet](2026-08-15-tranche-1-jones-markov-trace.md) |
| 5 | `def:crossing-energy` | 8 | 0 | 1 | [sheet](2026-08-15-tranche-crossing-energy.md) |
| 6 | `def:motivic-substrate` | 8 | 0 | 1 | [sheet](2026-08-15-tranche-motivic-substrate.md) |
| 7 | `rem:conway-normal-form` | 7 | 0 | 0 | [sheet](2026-08-15-tranche-conway-normal-form.md) |
| 8 | `def:archimedean-realization-functor` | 7 | 0 | 0 | [sheet](2026-08-15-tranche-archimedean-realization-functor.md) |
| 9 | `def:hadron` | 6 | 0 | 0 | [sheet](2026-08-15-tranche-hadron.md) |
| 10 | `def:categorical-neutron` | 6 | 0 | 1 | [sheet](2026-08-15-tranche-categorical-neutron.md) |
| 11 | `def:categorical-proton` | 6 | 0 | **2** | [sheet](2026-08-15-tranche-categorical-proton.md) |
| 12 | `def:q-from-epsilon` | 5 | 0 | 0 | [sheet](2026-08-15-tranche-q-from-epsilon.md) |

**107 sources remain**, down from 153. Ten would point forward if restored.

## The structural pass is closed

**`prose-linked` is zero in every tranche**, and
`scripts/prune-structural-candidates.ts` reports **0 candidates corpus-wide**.

That is the terminal state for the part of this work that could be decided
mechanically. Every block whose prose linked a target its declarations omitted
is resolved:

- **18 restored** — each carrying a prose link to a target it did not declare,
  cleared of forward-reference and cycle refusals, each linking sentence read
  and confirmed a prerequisite use.
- **4 withdrawn on evidence.** Three declared the target via `interprets`, and
  the `i8ad` change has since made that visible to the graph — they now resolve
  as declared rather than lost, which is the outcome withholding them
  anticipated. The fourth, `prop:strangelet-crossing-energy`, carried an author
  comment saying the edge was deliberately absent because it is reached through
  `def:coulomb-charge`; that comment was correct and my candidate list was an
  artifact of the `extractUses` bug.

## What remains needs reading, not tooling

The 107 remaining sources carry **no textual signal at all** — no prose link,
and for most no concept mention either. "The prune removed it" is a reason to
*ask* whether an edge belongs, not an answer.

Deciding them requires reading the blocks, and the `uses-editorial-review`
standard asks for two independent readers per verdict. That is a budget
decision, not a technical one.

Ordering, if it resumes: nine of the twelve are free of forward-reference risk
entirely. Only **10 blocks in 107** would point forward, four of them in
`def:borromean-baryon` — which is also the tranche with the least evidence, so
it is the worst candidate to start on despite being the largest.

## What none of this decides

Whether an edge belongs. The prune applied a mechanical rule across a corpus
without reading, and restoring mechanically repeats it in the opposite
direction. Two deliberate removals are now on record — `def:adelic-substrate`
losing `def:classical-limit-functor` by owner decision in `78a570365d`, and the
`prop:strangelet-crossing-energy` comment above — and both were found only by
looking.

Regenerate any sheet: `bun run scripts/prune-tranche-sheet.ts <target-label>`.
Re-check for structural candidates:
`bun run scripts/prune-structural-candidates.ts`.
Re-measure the damage: `bun run scripts/prune-damage-redrive.ts`.
