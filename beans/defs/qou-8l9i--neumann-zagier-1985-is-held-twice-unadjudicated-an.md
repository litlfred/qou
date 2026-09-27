---
# qou-8l9i
title: Neumann-Zagier 1985 is held TWICE, unadjudicated and doubly indexed (found while re-measuring the library counts)
status: todo
type: task
priority: normal
created_at: 2026-09-27T10:37:33Z
updated_at: 2026-09-27T10:38:19Z
---

## The finding, measured 2026-09-27

**Neumann–Zagier 1985, *Volumes of hyperbolic three-manifolds* (Topology 24(3),
307–332) is in the library TWICE, and nothing marks it as a duplicate.**

| | `…-three-manifolds` | `…-three-manifolds-co` |
|---|---|---|
| title in `structure.json` | Topology 24(3), 307–332, 1985 | identical |
| `sections/*.md` | 3 | 3 |
| section bytes | 57,294 | 57,324 |
| `duplicate_of` | **absent** | **absent** |
| own `INDEX.md` row | **yes** (line 666) | **yes** (line 667) |
| in `docs/audits/library-duplicate-ledger.json` (5 entries) | **no** | **no** |

0.05 % apart in bytes — an OCR-pass difference on the same scan, not two
editions.

**Why it matters, in corpus terms rather than call-graph terms.** AGENTS.md's
corpus-grep **path 5** is the check an agent runs before declaring anything
open, and its own rule is *"Do not read two hits on one work as two sources."*
The three mechanisms that enforce that rule — `duplicate_of` in the
front-matter, the adjudication ledger, and the one-row-per-work property of
`INDEX.md` — **all three miss this pair.** So a tier-1 scan returns two
adjacent rows and a full-text grep returns two directories, and both read as
two independent sources. This is not an obscure document: NZ 1985 is the
corpus's most-cited hyperbolic-volume source, upstream of `Vol(4₁)` and
therefore of the CAL-2 q₀ pin.

## The misattribution that hid it

AGENTS.md said *"and Neumann–Zagier three times"*, which reads as *this is
known and handled*. It is not NZ. The work held three times is
**`arxiv-2304.12545v1`** — *"Hyperbolic 3-manifolds, the Bloch group, and the
work of Walter Neumann"*, a 2023 survey **about** Neumann — and its two extra
copies (`hyperbolicandneumann`,
`celebratio-mathematica-neumann-hyperbolic-3-manifolds`) **do** carry
`duplicate_of` correctly. It is the only work in the library with more than one
extra copy.

So the sentence pointed at a *correctly handled* case using a name that made a
*mishandled* case look covered. Corrected in `105f45b017`.

## Decision for the library arc — NOT taken here

**What is being decided:** whether the `-co` copy is marked as a duplicate of
the other (or vice versa), and `INDEX.md` regenerated so one row remains.

- **What it means.** Set `duplicate_of` in one `structure.json`, add a row to
  `docs/audits/library-duplicate-ledger.json`, run
  `python3 scripts/summarize-library.py --apply`. The extra copy keeps its text
  on disk (that is by design), it simply stops presenting as a second source.
- **What it costs.** Three small edits plus one offline, model-free producer
  run. The producer is extractive and preserves agent-written summaries.
- **What it risks.** `INDEX.md` is a generated file with 693 rows; regenerating
  it touches a contended artifact, and the run rewrites rows for every
  document, so it collides with any sibling mid-ingest. Choosing the *wrong*
  survivor is the other risk — the two differ only by OCR pass, so whichever is
  dropped should be the one with fewer bytes unless someone has read both.
- **What it commits to.** Nothing beyond itself; it is reversible by clearing
  the field and re-running.

**Default if nobody acts:** the pair stays double-indexed and path 5 keeps
returning two hits for one work. Nothing breaks loudly; the cost is a reader
or an agent over-counting the evidence for a volume claim.

**My recommendation, and it is judgement rather than a finding:** mark `-co`
(the 57,324-byte copy, the later-suffixed stem) as `duplicate_of` the bare
stem, and let the next scheduled `summarize-library.py --apply` pick it up
rather than running a regeneration for one row. I did **not** do it because
AGENTS.md's own rule on this paragraph is that *a proposal is not a verdict*,
and `scripts/library-find-duplicates.py`'s same-work and different-work score
ranges overlap — so adjudication belongs to whoever owns that ledger, not to an
agent passing through on a count refresh.

## Also measured in the same pass (all landed in `105f45b017`)

Every figure in the path-5 block had drifted; the block's own instruction is
*"re-count, do not quote"*:

    ingested chars    24.7 M   ->  69.0 M sections/ + 1.1 M ocr/   (2.8x)
    INDEX.md          ~513 briefs / 527 lines  ->  693 rows / 710 lines
    directories       576      ->  715
    section files     11,528   ->  14,026
    index rows        552      ->  693
    duplicate copies  "23"     ->  21 copies over 20 distinct works
    ocr/ tier         25 of 576 -> 26 of 715

The character count is the load-bearing one: it is the whole argument for the
cheapest-first tier order, so understating it 2.8× understates the advice it
justifies.

**`INDEX.md` is CURRENT** — the block's invariant balances exactly,
`715 − 693 = 22 = 21 duplicates + 1 container`. So a clean tier-1 scan today is
evidence about the index, not about the library. Note this is *not* in tension
with the NZ finding: the pair is unmarked, so both copies are *correctly*
indexed under the invariant. **The invariant cannot detect an unadjudicated
duplicate** — it only checks that declared exclusions balance. That is the
reusable half of this bean.

A prefix trap met while checking: `grep -c '<stem>' library/INDEX.md` returns
**2** for the shorter NZ stem, because it is a prefix of the `-co` one. One
work's row reads as two. Same shape as the detector-blindness taxonomy's
spelling rows.

**11 PDFs are still sitting in `uploads/`** and are invisible to path 5 by
construction (it searches `library/` only). AGENTS.md's `uploads/` row already
states that hazard qualitatively and correctly, so nothing was edited; noted
because the count makes it concrete and an un-ingested paper is exactly how a
held source gets re-derived.

Left **`todo`**: the counts are corrected but the adjudication above is open,
and a bean whose first item is unresolved is not completed.
