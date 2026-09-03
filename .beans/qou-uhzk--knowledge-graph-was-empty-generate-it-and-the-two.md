---
# qou-uhzk
title: 'Knowledge graph was empty: generate it, and the two generator defects that found'
status: completed
type: task
priority: normal
created_at: 2026-09-03T04:07:44Z
updated_at: 2026-09-03T04:08:03Z
---

Done on `claude/rag-document-ingestion-options-orasrw` (qou 40538dbcfc, fa d07c325).

**The graph was empty.** 3595 authored blocks, 576 library documents, **zero
`.jsonld`**. Every graph-backed query returned nothing and returned it as "no
results" rather than "nothing was indexed" — the failure mode the whole
`emptyRoots` reporting in `graph-search` exists to prevent, sitting live in
the folio the tooling was written for.

Generated: **3573** authored siblings, **19181** library nodes across 576
documents (38938 files). Committed, per the design: a sandboxed session with
no toolchain can read them, and `--check` is the gate against the `.ts` and
the `.jsonld` becoming two truths.

**Running it against real data found two defects that fixtures could not.**

1. **`graph-search` lost the edge term on every backwards hop** (fa fdae09b).
   `neighbors` orients an edge by the GRAPH (`from` -> `to`), not by travel, so
   under the default `direction: "both"` an incoming edge arrives with the
   newly-reached node as `from`. The path reconstruction keyed on `to` alone.
   Measured: 20 of 50 graph-reached nodes on a 1-hop "Temperley-Lieb" search
   rendered `via ?`. Incoming was the LARGER half (`~uses` 16 vs `uses` 6).
   Fixed, and each path step now carries `dir`: the edge vocabulary is
   asymmetric, so rendering "A uses B" and "B uses A" identically collapsed the
   one distinction an impact question needs.

2. **A prefix-less reference was refused, deleting 35 real edges** (fa
   d07c325). All 35 pointed at blocks that exist — seven `prose`/`example`
   blocks in the transfer-matrix appendix and braids-and-knots, prefix-less
   because `prose` requires no prefix. `parseReference` now returns a
   `bare-label` form; it resolves through the same helper `mintNodeId` uses, so
   a reference and its target agree by construction. The two genuinely
   ambiguous cases (unknown prefix, empty slug) stay strict.

   The old contract's stated reason was that forgiveness "would mask every
   typo". It does the opposite, and there is a test for it now: a typo mints an
   IRI no node claims, so the edge is emitted and shows as **dangling** when the
   graph is walked — whereas refusing it deleted the edge, and a missing edge is
   what nobody notices.

Corpus after: **0 dangling**, 35 prefix-less reported in their own list (kept
apart from dangling because one is data loss and the other is a naming nit).

**One finding worth its own item.** `graph-search "Wenzl"` returns 20 authored
seeds and **0 ingested**. Wenzl 1988 is not in `library/` — so every Wenzl-weight
result in this corpus is unbacked by the source it cites, and the provenance
split is now what makes that visible at a glance rather than something you have
to already suspect. Same for Jones 1987.
