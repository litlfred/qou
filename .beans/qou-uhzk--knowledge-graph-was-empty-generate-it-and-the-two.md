---
# qou-uhzk
title: 'Knowledge graph was empty: generate it, and the two generator defects that found'
status: completed
type: task
priority: normal
created_at: 2026-09-03T04:07:44Z
updated_at: 2026-09-03T04:54:51Z
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


---

## Wired up (2026-09-03) — the graph is now reachable from the checklist

The graph was correct and unused: `graphSearch` lived in a pipeline module with
a CLI, and the discipline an agent actually follows is a list of greps. A
capability behind a script path and a flag spelling is not on that list.

**`corpus_search` (MCP)** — folio-assistant `6d79ff4`. Added to
`adapters/mcp-server/tools/graph.ts` beside `search_graph` / `get_neighbors`,
which are deliberately disjoint (one answers "which nodes contain these words",
the other "what is adjacent") so that using them together meant search → copy
an id → walk → repeat, and the graph contributed nothing to a search. I first
wrote it as a separate tool in the document adapter and undid that: the graph
tools share a lazily-built index measured at 29,780 nodes on this corpus, and a
separate tool would have rebuilt it per call.

**`AGENTS.md` step 0** — qou `85be360bea`. Placed BEFORE the six greps, not as
a seventh path, because it is not another sample of the same kind: all six are
greps and they share one blind spot — a grep finds prior work only if it used
YOUR words. It also says what to read in the answer (`why` / `~` for a
backwards edge, `seedsByProvenance`, `emptyRoots`), that it does not replace
the six, and that it is not a gate.

**`emptyRoots` got its own TRAP** in `corpus-grepper`'s memory, because it is
this same failure one level up: before today qou had 3595 blocks, 576 library
documents and zero `.jsonld`, so every graph query returned nothing in the
shape of "no results" rather than "nothing was indexed".

Memory hit 230 lines against the 200-line injection cap, so two sections
already duplicated in the sibling became pointers and the 29-line resolved-
topics lookup split into `resolved-topics.md` (198 now). The sibling carried
one heading twice; removed.

Verified on a live question: `corpus_search "Hoefsmit"` → 20 seeds, 47
graph-reached, `byProvenance {"authored": 67}` — **zero ingested**, which is
`hoefsmit1974` (83 citations, source not held) visible in one line.
