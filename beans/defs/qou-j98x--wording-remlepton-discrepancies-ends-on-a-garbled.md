---
# qou-j98x
title: 'WORDING: rem:lepton-discrepancies ends on a garbled sentence with no referent or predicate (''This is likely where the discrepancy tracks specifically with the tau channel'')'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - split-from-6766
    - 8f-decide
created_at: 2026-10-10T08:14:29Z
updated_at: 2026-10-10T08:14:45Z
parent: qou-8lxd
---

Split out of `qou-6766` on 2026-10-10 (seven findings in one title). Residual
item (4) of four. **One sentence; it is the block's last.**

## The sentence

`folio/quantum-observable-universe/observations/lepton-discrepancies.md`
(kind `remark`, `label: rem:lepton-discrepancies`,
`interprets: def:categorical-reeb`), final sentence of a five-sentence block:

> "This is likely where the discrepancy tracks specifically with the tau
> channel."

It has no referent for "This", no predicate that asserts anything, and it
restates the preceding sentence's content ("the tau satisfies only the first")
without adding a claim. Read charitably it is a truncation of something like
*"the structural asymmetry predicts the discrepancy tracks the tau channel
specifically"* — but that is a guess at intent, which is why this waits for the
author rather than being repaired.

## What is NOT wrong with it

Worth stating, because the obvious objection does not apply. The preceding
sentence —

> "Anomalous magnetic-moment tensions and lepton flavour universality violations
> observed at $B$-factories may reflect this structural asymmetry rather than new
> heavy-particle loops."

— is an **empirical interpretation inside a `remark`**, which AGENTS.md §3a
permits explicitly: a remark makes no logical claim, and interpretation is what
remark blocks are for. It is correctly hedged ("may reflect"). So this bean is
**not** a no-empirical-predictions finding; the only defect is the garbled
closer.

## Options

1. **Delete the sentence.** The block ends on the `B`-factory interpretation,
   which already carries the point. Cost: one line. Risk: none — nothing cites a
   sentence.
2. **Replace it** with what it appears to mean, e.g. *"If so, the tension should
   track the tau channel specifically and not the electron or muon channels,
   which satisfy both criteria."* Cost: one line. This version states a
   falsifiable consequence of the structural reading, which is more useful than
   either the current text or (1) — but it is the author's claim to make, not
   the agent's.
3. **Nothing.**

**Recommendation (agent judgement):** (2), because it converts a dead sentence
into the one thing a reader would want from this remark — what would distinguish
the structural reading from the heavy-loop reading. (1) if the author would
rather not commit to the consequence.

**Default if unanswered: (3).** The block keeps a sentence that says nothing;
no number, label, or downstream reader is affected.

**Blast radius:** `rem:lepton-discrepancies` only. Its two outbound links
(`rem:archimedean-leptons`, `rem:symmetry-preserving-leptons`) are untouched by
any of the three options.
