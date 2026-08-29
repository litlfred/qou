# corpus-grepper — memory

Entry types: **STABLE** · **TRAP** · **BASELINE** (re-measure, never quote).
Seeded 2026-08-29 from `AGENTS.md`. Confirm entries as you use them.

---

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

## STABLE — the library, three tiers

```sh
grep -in <topic> library/INDEX.md              # 320 one-line briefs, ~14k tokens total
cat library/<doc-id>/summary.json              # ~300 tokens: worth opening?
grep -rln <topic> library/<doc-id>/sections/   # the text itself
```

Full-text fallback: `grep -rln <topic> library/*/sections/` — 332 documents
/ 7,313 sections / 24.7 M characters. Do not grep straight into that when a
line of `INDEX.md` will do.

A section file's YAML front-matter names document, section and page range,
so a hit is immediately citable. `library/<doc-id>/candidates.json` holds
that document's extracted theorems and definitions.

Briefs and summaries are **extractive** — assembled from each document's own
abstract and section titles, nothing model-written — so a brief is only as
good as the abstract behind it.

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

Four conflations, all of which reached durable artifacts in a single
session (2026-08-15), each having survived a topic-grep:

1. **One proposition, or a family?** Read the declaration's type.
   `kappa_vanishes : ℕ → Prop` is a level-indexed family; there is no
   single truth value to be faithful to.
2. **Pointwise, or the universal closure?** `∀ P, v ↔ Pred P` and
   `v ↔ ∀ P, Pred P` are different, and the second is trivially inhabited.
   Refuting the first says nothing about it.
3. **Shared type, or shared instance?** A theorem fixing one `sys` and one
   `P` says nothing about two legs instantiated at different values — and
   the other instance may not satisfy the hypothesis.
4. **Set-level premise, truth-value conclusion?** "Undecidable", "not cut
   out by an ideal", "cofinite locus" are facts about sets, logically
   independent of whether a scalar is equivalent to a single proposition.

Criterion `da-arity-conflation` in
`.claude/skills/local/devils-advocate-watcher.md` carries the worked
examples and why a machine checker cannot do this.

## TRAP — `beans create` is not idempotent

It mints a fresh ID every call and dedupes on nothing. Run the exact-title
existence check in `.claude/skills/local/todo-manager.md` §"Check before you
create" first; on a match, claim the existing bean with
`beans update <id> --status in-progress`.

An unguarded re-run on 2026-08-04 produced **14,688** duplicate beans — 92%
of every open bean — which starved the idle-backlog policy of signal and
corrupted a later agent's corpus-grep badly enough to nearly land a false
correction in a PR body (bean `qou-2ryn`). Your searches read `.beans/`;
that is why this matters to you.

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

Append here whenever a sweep lands. Format: *question → where → verdict →
date*. This is the entry type that saves the most work.

- Groupoid with inequivalent fibre objects carrying a 3-dim `W` whose
  fundamental is not self-dual → bean `qou-dwsh` body (completed
  2026-08-03) → answered; reachable by path 6 only.

## BASELINE — re-measure, do not quote

| what | command | last seen | when |
|---|---|---|---|
| library size | `ls -d library/*/ \| wc -l` | 332 docs / 7,313 sections / 24.7 M chars | 2026-08 |
| INDEX.md briefs | `wc -l library/INDEX.md` | 320 briefs, ~14k tokens | 2026-08 |
| duplicate works | `docs/audits/library-duplicate-ledger.json` | 19 works held more than once | 2026-08 |

---

## Session log

One line per sweep: topic, verdict, which path found it. Keep under ~200
lines — prune the log, never the TRAPs or the resolved-topics table.
