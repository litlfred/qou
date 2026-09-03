---
# qou-an21
title: 'Cited-but-not-held sources: 411 keys, and the ledger is wrong in both directions'
status: completed
type: task
priority: normal
created_at: 2026-09-03T04:16:26Z
updated_at: 2026-09-03T04:26:13Z
---

Measured and partly repaired on `claude/rag-document-ingestion-options-orasrw`
(qou f7e948d825). Detector: `scripts/cited-source-availability-audit.py`.

**Started from "is Wenzl/Jones ingested?" and the answer was a whole join
nobody had computed.** 464 bibliography keys are cited across the corpus (346
via block `cites[]`, 303 via Lean `-- Ref:`, union 464). Before this change
**54** of them had a source file on disk.

**The ledger was wrong in BOTH directions.**

*Recorded absent, actually held — 30 keys, now re-pointed (`reachable` 54 ->
84).* This is the class that costs a session: corpus-grep path 5 asks "do we
hold this", gets no, and the agent re-derives instead of citing.
`thurston1978` 105 citations (`library/thurston`); `jones1985` 87 — and it is
one of the 25 OCR-tier docs the documented `sections/` grep cannot see, i.e.
AGENTS.md's own fourth-tier warning biting on the exact source in question;
`codata2022` 25 — the constants table every empirical comparison here is made
against, recorded as a vanished `uploads/*.txt` while
`library/revmodphys97025002pdf` holds the paper; `milnor1982` 37.

*Held and triaged but UNCITABLE — 212 entries with `id: null`*, of which
**51 are relevance `core`** and 91 `supporting`. In the repo, read, judged, and
no block can cite them, so the corpus cannot tell them from a source we lack.
Invisible until now because every reader keyed the ledger on `e["id"]` and
collapsed all 212 onto one key. **Not fixed** — each needs a `references.ts`
entry, which is authoring, not bookkeeping.

*15 duplicate bib ids*, where an id-keyed lookup keeps one row and drops the
rest. **Not fixed.**

**The original question, answered:** `jones1987` (390 citations),
`wenzl1988` (213) and `hoefsmit1974` (83) are genuinely not held. Nor is
`wenzl1987`/`wenzl1990`/`kazhdanwenzl1993` — those three are not in the ledger
at all, never triaged. "Not held" is about this repo, not about the literature;
the fix is to obtain them or mark them external deliberately.

**Prior art, not a discovery.** 28 of the 44 upload-with-missing-file rows
already carried an earlier agent's diagnosis that the PDF "only ever existed on
the machine that ran that pass". I confirmed all 44 were never committed
(`git log --all` empty for each) and found 16 undiagnosed; I did not find the
class. Related bean `qou-f4el` proposed the discriminated `source` union this
measures against.

**Instrument note.** My first Lean-citation count was **0 of 6221** because
`grep -- '-- Ref:' content --include=*.lean` makes `--include` a PATH, not a
flag. Reporting that 0 as "Lean cites nothing" would have been a false negative
about the larger half of the citation surface. The option order is now written
into the script with the reason.
