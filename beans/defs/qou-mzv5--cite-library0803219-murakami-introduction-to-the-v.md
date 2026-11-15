---
# qou-mzv5
title: 'CITE: library/0803219 (Murakami, Introduction to the Volume Conjecture) is held but unregistered — M — qou-ic22 has no key to cite'
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:04:09Z
updated_at: 2026-11-15T13:27:18Z
parent: qou-1qhv
---

**Class M — held, greppable, and unciteable because it has no key.**

`library/0803219/` is **Murakami, Hitoshi, *An introduction to the volume
conjecture and its generalizations*, Acta Mathematica Vietnamica** (the `INDEX.md`
row reads "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME
CONJECTURE AND ITS GENERALIZATIONS"). It is ingested with sections
(`1 Preliminaries`, `1.1 colored Jones polynomial`, `1.2 SL(2,C) character
variety`, `1.3 Volume and the Chern–Simons invariant`, …) and is greppable:
`Murakami` 16 section files, `colored Jones` 10, `simplicial volume` 2,
`Gromov norm` 1.

**`grep -n "0803219" content/schema/references.ts` returns nothing.** The document
is held and has no `ref()` entry, so nothing in the corpus can cite it — the same
class as the `milnor1982` case, whose own note records *"the library held this
paper unlinked, so it read as an unregistered document"*.

**Where it bites.** Bean `qou-ic22` (*"KVC DISCHARGE: cite Murakami 3.3 per-knot
for 4_1 Borromean 5_2 6_2 torus/Hopf — the anchors are all PROVED, this is
bookkeeping"*, `todo`, parent `qou-9ot5`, empty body) is a locator task against
**§3.3 of this survey**, and there is no key to write. It is also the natural
survey-level companion at every `[murakami-murakami2001]` site, which matters
because that primary is **not held** (sibling bean).

**Fix:** add a `ref()` entry with `library: { docId: "0803219", dir:
"library/0803219", … }`. Check the `INDEX.md` row's mangled title against the PDF
first — the extractor has taken page furniture as title elsewhere in this library
(`thurston1978`'s note records exactly that failure).

**Do not assume this is the only one.** This was found incidentally; a systematic
`library/<docId>` ↔ `references.ts library.docId` reconciliation was NOT run.
`references.ts` has 828 entries of which **394 carry a `docId`**, against **576
library directories** — the residual is unmeasured and includes duplicates, so the
gap is not simply 182.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.

Done 2026-11-15 on branch claude/library-reingest-kg-2026-11-15: key `murakami2008-acta-vietnam` (Acta Math. Vietnam. 33(3), 219-253, 2008) registered against library/0803219/, metadata from the PDF's page 1. qou-ic22 can now cite it.
