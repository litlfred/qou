# corpus-grepper — memory

Entry types: **STABLE** · **TRAP** · **BASELINE** (re-measure, never quote).
Seeded 2026-08-29 from `AGENTS.md`. Confirm entries as you use them.

---

## STABLE — step 0: `corpus_search` (MCP), before any grep

All six paths below are greps, and they share one blind spot: a grep finds
prior work only if it used **your** words. Work written in different words is
the case that actually costs a session — the grep comes back empty and reads
as a clean bill.

`corpus_search` seeds lexically and then expands along the knowledge graph,
across the authored corpus and the ingested library at once. A block that
never says "Temperley-Lieb" but `uses` one that does is one hop from the query.

Read three fields. **`why`** — MATCHED vs REACHED, and by which edge; a `~`
prefix means the edge ran backwards, so that node depends on the seed rather
than the reverse. **`seedsByProvenance`** — many ingested hits with no authored
ones means *cite it*, not *derive it*. **`emptyRoots`** — a directory present
but holding no graph nodes; an ungenerated `.jsonld` corpus answers every query
with a silence indistinguishable from "nobody has done this".

It does not replace the six: it seeds on labels, titles, kinds and tags
(`searchText: true` for companion prose), so a topic named only inside a proof
body is still a grep's job.

## TRAP — an empty `corpus_search` is not evidence until you have read `emptyRoots`

Added 2026-09-03, from the run that generated the graph. Before that day the
qou graph was **empty**: 3595 authored blocks, 576 library documents, **zero**
`.jsonld`. Every graph-backed query returned nothing and returned it in the
shape of "no results" rather than "nothing was indexed". The distinction is the
entire value of the field, so check it before treating an empty answer as an
absence — this is the same failure the tool exists to prevent, one level up.

## STABLE — the six paths, in order

All six must return empty (modulo the originating file) before anything is
declared open. A source file's own `## Status` / `Open math` note is **not
authoritative** — the corpus is.

1. `grep -rln <topic> docs/audits/` — owner-authorised resolutions land here
   first; the originating file's status note can lag by months.
2. `grep -rln <topic> content/` — **whole tree**, not just the chapter you
   started in. Conjectures cross-cut chapters.
3. `grep -rln <topic> computations/` — implemented Python may already
   realise what a source file calls open.
4. `docs/coordination/<theme>.md` — the ledgers. A prior agent may have
   closed it.
5. **`library/`, three tiers, cheapest first** — see below.
6. **`.beans/`** — `grep -rl <topic> .beans/`. See the TRAP below; this is
   the path most often skipped and the one that most often holds the answer.

## STABLE — the library: read [`library-and-staleness-traps.md`](library-and-staleness-traps.md)

Three tiers (`INDEX.md` -> `summary.json` -> `sections/`) plus the fourth (`ocr/`), with the counts and the commands. Moved there 2026-09-03 to stay under the 200-line cap; the traps below stay here because they are what gets skipped.

## TRAP — for some docs `sections/` is BOILERPLATE; the text is in `ocr/`

25 of 542 library dirs keep their real text in `ocr/`, and the documented
`sections/` grep cannot see it. Worked cases and the measured share:
`library-and-staleness-traps.md`.

## TRAP — `uploads/` is invisible to path 5

`uploads/` and `library/` are **two stages of one pipeline, not a rename**.
A PDF sits in `uploads/` until it is processed into `library/<doc-id>/`, and
`uploads/` stays live for the next drop. Path 5 searches `library/` only, so
an un-ingested paper will not be found by any "has the corpus got this?"
check — which is exactly how a held source gets re-derived.
`scripts/migrate-uploads-to-library.py` moves one across.

(`AGENTS.md` said "renamed from uploads/ 2026-08-15" until corrected
2026-08-25; reading it that way makes a live queue look like a dead alias.)

## TRAP — the library holds 19 works more than once

Extra copies keep their text on disk, so a full-text grep lands in them.
Each carries `duplicate_of` in its section front-matter naming the copy to
prefer. **Two hits on one work are not two sources.** Neumann–Zagier is
present three times. Adjudicated in
`docs/audits/library-duplicate-ledger.json`.
`scripts/library-find-duplicates.py` *proposes*; its same-work and
different-work score ranges overlap, so a proposal is not a verdict — a
sequel sharing its setup sections outscores four true duplicates.

## TRAP — the beans path is not reachable from paths 1–5

`.beans/` is not under `docs/`, `content/`, `computations/` or `library/`,
and a coordination ledger is a different file. It is a corpus in its own
right (tens of thousands of files) and it is where a prior agent's
*conclusion* usually sits before it reaches an audit doc or a block.

Read `status` and the **whole body**, not the title:

- a **`completed`** bean is the one that bites — the answer may be a single
  sentence in the body with no artifact anywhere else;
- a **`scrapped`** bean usually names the bean that superseded it, which is
  how you find the live carrier.

Worked case (added 2026-08-26 after a PR re-derived two held results): the
trail ran `qou-8pl3` → `qou-8p1i` (scrapped) → `qou-dwsh` (completed,
2026-08-03), whose body states the conclusion the PR spent a tranche
proving. Paths 1–5 cannot reach that sentence.

## TRAP — a sibling's bean is not a primary source either

The "not authoritative, the corpus is" rule applies to beans verbatim,
including beans by other agents that look authoritative because they are
specific and recent. Worked case: bean `qou-q7lf` reports a scipy-sparse
boundary in `hecke_core_legacy.unified_iterative_correction`; commits
`da645cf0f32` and `46dcfc62a57` fixed exactly that site the next day. The
bean was stale and was believed over the code.

## TRAP — grep the claim SHAPE, not only the topic

Four conflations reached durable artifacts in one session (2026-08-15), each
having survived a topic-grep. Read the declaration's **type**, and check:

1. **One proposition, or a family?** (`kappa_vanishes : ℕ → Prop` is indexed.)
2. **Pointwise, or the universal closure?** (`v ↔ ∀P, Pred P` is trivial.)
3. **Shared type, or shared instance?** (two legs at different values.)
4. **Set-level premise, truth-value conclusion?** (independent claims.)

Also check the **binder generality** — it decides scope. Worked 2026-08-30:
`b3_eq_zero_ofBondFunctional (f : R → R) (μ : Fin 4 → Fin 4 → R)` quantifies
over *every* bond functional and allows *bond-dependent* weights, so it excludes
a whole assembly class, not one ansatz — but `Fin 4` fixes `A = 4`, so "for all
`A`" is not what was proved.

Criterion `da-arity-conflation` in
`.claude/skills/local/devils-advocate-watcher.md` carries the worked
examples and why a machine checker cannot do this.

## TRAP — `beans create` is not idempotent

Run the exact-title existence check before every create; an unguarded
re-run once produced 14,688 duplicates. Detail:
`library-and-staleness-traps.md`.

## TRAP — an inherited "X is unavailable" is HALF a measurement

2026-09-03: the corpus said *"the ptolemy DB is firewalled; only `4_1`/`5_2`/
`3_1` ship Magma fixtures"*. I carried both halves into a PR body, a bean and a
report. **Firewall: real** (403 on CONNECT, re-verified two ways). **Fixture
list: wrong** — the wheel ships **seven** manifolds; nobody had run `ls`.

**The shape: a claim bundling an ENVIRONMENT fact (a host is blocked) with a
CORPUS fact (what we hold locally).** The environment half ages slowly and is
usually right; the local half is cheap to check and is the one that is wrong.
Enumerate the local surface yourself before repeating either half.

## STABLE — refutation scoping

- **(a) scope-limited negative** — "this construction, *alone*, does not
  reproduce the numbers as-is." This is what a failed numerical probe
  actually shows. **Default to this phrasing.**
- **(b) structural exclusion** — "this ingredient cannot appear in any
  closure." Permitted only with a **proved invariant**: parity/sign, a
  dimension/orbit-count/degree bound, a Lean-proved impossibility, an
  entropy or precision bound. **Cite it.**

Two permanence principles that make most (b) claims wrong: a Lean-proved or
structurally-exact piece stays a correct contribution even while the total
is inaccurate; and a compositional/trace object is already many-body, so
"pairwise can't do it" against `1 − ∏ᵢ fᵢ` is a category error — the probe
measures the size of the missing higher term, it does not exclude the
factor.

Found an over-claimed (b)? Re-scope to (a). Do not delete the finding — the
numerical result stands, only the scope was wrong.

## Resolved topics — where the answer actually lives

A lookup table, not a thing to carry: consulted when a specific topic
comes up. Moved to `resolved-topics.md` — read it before declaring any of
these open, and add a row whenever a sweep settles one.

## BASELINE — re-measure, do not quote

| what | command | last seen | when |
|---|---|---|---|
| library size | `git ls-tree -r --name-only origin/main -- library/ \| cut -d/ -f2 \| sort -u \| wc -l` | **536 dirs** (was recorded 332 — that figure was low, not merely old) | 2026-08-30 |
| docs with `ocr/` | same, filtered to `/ocr/` | 25 dirs; 11 single-section; 10 of those <15 % sections/ocr bytes | 2026-08-30 |
| INDEX.md briefs | `wc -l library/INDEX.md` | 320 briefs, ~14k tokens | 2026-08 |
| duplicate works | `docs/audits/library-duplicate-ledger.json` | 19 works held more than once | 2026-08 |

---

## Session log — one line per sweep. Prune this, never the TRAPs.
- 2026-08-30 · `qou-brng` linking-vs-self-energy · **partially covered / target moved** · found on paths 1, 3, 4, 6; the citable source on path 5 was reachable only via `ocr/`.
- 2026-09-03 · `qou-q9ih` D1-b NZ->(Q,W) dictionary · **open on all six paths**; NZ *input* side already implemented (`one_loop_torsion.py`, Route-74/75 probes) — reuse, do not rebuild. The 2026-09-02 Markov/Ocneanu span-rank entry moved to [`resolved-topics.md`](resolved-topics.md) (it was past line 200).
