# Prune damage re-drive — 785 → 692, and the parity family is no longer uniform

Generated 2026-08-15 by `scripts/prune-damage-redrive.ts`. Re-reads the edge
list in `2026-08-10-transitive-prune-overreach.md` and asks what is true of each
edge in the corpus **today**. Bean: `prn1`.

Editorial edges only. `ContentGraph`'s accessors default to the union of
editorial and formal edges; `prn1` is about what a *reader* can reach through
`uses[]`, so counting Lean edges would report paths nobody can follow and make
the damage look smaller than it is.

| | audit 2026-08-10 | today |
|---|---|---|
| edges claimed still-lost | 785 | 785 parsed |
| source block gone | — | 0 |
| target block gone | — | 27 |
| edge re-declared since | — | **39** |
| reachable again via a path | — | 27 |
| **still lost** | **785** | **692** |
| across blocks | 335 | **320** |
| of which declare nothing | 80 | **78** |

93 edges repaired in five days, none of it by this re-drive — nothing here
restores anything.

## The parity family has been half-repaired, and that changes `fwr10`

`prn1`'s methodological finding was that sibling parity cannot be evidence
where a bulk edit ran: two readers judged the surreal-bound family
"deliberately empty" from uniformity that the prune had manufactured. `fwr10`
recorded four blocks whose `correctly-empty` verdicts rested on that argument
and needed re-reading.

**21 of the 39 re-declared edges landed on exactly this family**, and every one
of them is an edge the prune removed:

| block | declares now | of which re-declared prune edges | still lost |
|---|---|---|---|
| `rem:yang-mills-surreal-bound` | 6 | 6 | 2 |
| `rem:p-vs-np-surreal-bound` | 6 | 6 | 2 |
| `rem:rh-surreal-bound` | 4 | 4 | 3 |
| `rem:bsd-surreal-bound` | 3 | 3 | 5 |
| `conj:p-vs-np-qou` | 2 | 2 | 4 |
| `rem:ns-surreal-bound` | **0** | 0 | **9** |
| `rem:archimedean-stpart-strategy` | **0** | 0 | **7** |

So the parity argument is dead twice over: the uniformity was manufactured, and
it is gone. Three of `fwr10`'s four blocks have since been re-populated, which
shrinks that re-reading task rather than confirming it.

**The asymmetry now points the other way, and harder.** `rem:ns-surreal-bound`
declares nothing while five siblings have been restored to 2–6 edges each. When
the whole family was empty, "deliberately empty" was a reasonable reading. With
five restored and one left at zero, the same uniformity argument now says the
opposite. It is the strongest single candidate in this file, and
`rem:archimedean-stpart-strategy` — `fwr10`'s fourth block, still at zero, 7
lost — is the second.

## Tranche by target, not by source

The audit lists damage per source block, which makes 320 separate questions. Cut
the same data by **target** and it collapses into a few:

| sources that lost it | target |
|---|---|
| 21 | `thm:jones-markov-trace` |
| 20 | `def:hecke-normal-form` |
| 16 | `def:borromean-baryon` |
| 12 | `def:crossing-energy` |
| 11 | `rem:conway-normal-form` |
| 11 | `def:habiro-ring` |
| 11 | `def:motivic-substrate` |
| 11 | `def:archimedean-realization-functor` |
| 10 | `def:q-from-epsilon` |
| 10 | `def:hadron` |
| 10 | `def:categorical-neutron` |
| 10 | `def:categorical-proton` |

These are foundational definitions, which is what a transitive prune eats: they
sit at the bottom of long chains, so *every* `A → B → foundational` triangle
offered them up, and the pass dropped `B → foundational` in the same sweep.

Restoring `thm:jones-markov-trace` to its 21 sources is **one** editorial
question — "must a reader have this before those blocks?" — asked once and
applied 21 times, rather than 21 unrelated judgements. That is the tranche
structure `prn1` asked for.

`def:q-from-epsilon` is a smaller but sharper case: lost by 10 sources, and by
**all seven** members of the surreal-bound family, including the five that have
since been restored on every other edge. Whoever restored those five did not
put it back, so either it is genuinely unwanted there or it was missed —
and that is a question with one answer for all seven.

## What this is still not

Not a licence to restore 692 edges. The original error was a mechanical rule
applied across a corpus without reading; restoring mechanically repeats it in
the opposite direction. At least one removal is known to be deliberate —
`def:adelic-substrate` lost `def:classical-limit-functor` by owner decision in
`78a570365d`, and restoring it re-opens a cycle.

This produces the candidate list and its priority order. The two-reader standard
in the `uses-editorial-review` skill still governs what is applied.

Reproduce: `bun run scripts/prune-damage-redrive.ts` (add `--all` for every
still-lost edge).
