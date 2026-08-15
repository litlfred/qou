# Prune-restoration tranches — index

Regenerated 2026-08-15, **after** the `extractUses` fix (folio-assistant #117).
Bean `prn1`.

> **Earlier revisions of these sheets were wrong** in one column. `extractUses`
> failed on any manifest with a comment between the previous field's comma and
> its `uses:` key, so 27 blocks and 53 declared edges were invisible to the
> graph and those blocks read as declaring nothing. Every `declares now` count
> and every still-lost total predating the fix is superseded by this page.

**18 edges have been restored** under this bean. The twelve largest targets now
stand at **131 remaining sources**, of which **3 are prose-linked** and **10
would point forward if restored**.

| # | target | sources left | prose-linked | forward | sheet |
|---|---|---|---|---|---|
| 1 | `thm:jones-markov-trace` | 19 | 0 | 0 | [sheet](2026-08-15-tranche-1-jones-markov-trace.md) |
| 2 | `def:hecke-normal-form` | 18 | 0 | 0 | [sheet](2026-08-15-tranche-hecke-normal-form.md) |
| 3 | `def:borromean-baryon` | 16 | 0 | **4** | [sheet](2026-08-15-tranche-borromean-baryon.md) |
| 4 | `def:crossing-energy` | 9 | 1† | 1 | [sheet](2026-08-15-tranche-crossing-energy.md) |
| 5 | `rem:conway-normal-form` | 10 | 1† | 0 | [sheet](2026-08-15-tranche-conway-normal-form.md) |
| 6 | `def:habiro-ring` | 11 | 0 | 1 | [sheet](2026-08-15-tranche-habiro-ring.md) |
| 7 | `def:motivic-substrate` | 8 | 0 | 1 | [sheet](2026-08-15-tranche-motivic-substrate.md) |
| 8 | `def:archimedean-realization-functor` | 10 | 1† | 0 | [sheet](2026-08-15-tranche-archimedean-realization-functor.md) |
| 9 | `def:q-from-epsilon` | 5 | 0 | 0 | [sheet](2026-08-15-tranche-q-from-epsilon.md) |
| 10 | `def:hadron` | 10 | 0 | 0 | [sheet](2026-08-15-tranche-hadron.md) |
| 11 | `def:categorical-neutron` | 7 | 0 | 1 | [sheet](2026-08-15-tranche-categorical-neutron.md) |
| 12 | `def:categorical-proton` | 8 | 0 | **2** | [sheet](2026-08-15-tranche-categorical-proton.md) |

† The three remaining prose-linked blocks are **withheld deliberately** — see
"the `interprets` question" below. They are not pending work.

## The structural pass is finished

Every block whose prose linked a target its `uses[]` omitted has been resolved:
18 restored, 4 withdrawn on evidence. What remains in these twelve tranches
carries **no textual signal at all** — no prose link, and for most no concept
mention either.

That is the honest boundary. "The prune removed it" is a reason to *ask* whether
an edge belongs, not an answer. Deciding the remaining 131 requires reading the
blocks, and the `uses-editorial-review` standard asks for two independent
readers per verdict.

## The `interprets` question — open, and it changes the numbers

`buildContentGraph` builds editorial edges from `uses[]` **alone**.
`interprets:` is a second authored relation, and the detangler already treats it
as an ordering constraint — no block may precede one it interprets. So the graph
and the checker disagree about whether `interprets` is an editorial edge.

**37 of the still-lost edges are declared via `interprets:`.** Three of them sit
in these tranches (`rem:commutative-crossing-energy`,
`rem:body-asymptotics-catalog`, `rem:archimedean-image-table`), which is why
they are withheld rather than restored.

This makes the damage figure answer a narrower question than it appears to:

- **"unreachable through `uses[]`"** — **658** edges. Correct for the ordering
  metrics, which run on exactly that graph.
- **"the author never declared this dependency"** — **621**. The other 37 are
  stated, just in the other field.

(Measured after the 18 restorations. The figure moves faster than the count of
edges applied, because restoring one edge can make several others reachable
transitively — which is the same effect the original prune was trying to
exploit, and got wrong by dropping both legs of the triangle.)

Both are defensible; they are not interchangeable, and the audit has been
reporting the first while being read as the second.

## What none of this decides

Whether an edge belongs. The prune applied a mechanical rule across a corpus
without reading, and restoring mechanically repeats it in the opposite
direction — at least one removal is known deliberate (`def:adelic-substrate`
lost `def:classical-limit-functor` by owner decision in `78a570365d`, and
restoring it re-opens a cycle), and a second was found here: the author comment
on `prop:strangelet-crossing-energy` turned out to be correct against a
candidate list built on a broken parser.

Regenerate any sheet: `bun run scripts/prune-tranche-sheet.ts <target-label>`.
Find structural candidates corpus-wide:
`bun run scripts/prune-structural-candidates.ts`.
