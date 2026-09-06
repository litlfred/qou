---
# qou-7br7
title: The ingest producer pdf-structure.py is absent from BOTH repos here, and migrate's orphan fallback is exactly what fires when it has not run
status: todo
type: task
priority: normal
created_at: 2026-09-06T23:25:01Z
updated_at: 2026-09-06T23:25:53Z
---

Found 2026-09-06 by a **new selector**: beans naming repo paths that no longer
exist. That is the complement of `scripts/bean-staleness-triage.py`, which ranks
by *"the tree moved UNDER the bean"*; this asks *"did the tree move OUT FROM
UNDER it"*. The ranking structurally cannot see this class — a deleted path has
no commits touching it after the bean's `updated_at`, so it scores **zero** and
sorts to the bottom.

## The finding

`scripts/pdf-structure.py` and `extract-candidates.py` — the producers of every
`structure.json`, `sections/*.md` and `candidates.json` in `library/`, i.e. the
whole of corpus-grep path 5 — are **absent from both repos reachable here**,
verified at full depth:

    find . -name 'pdf-structure*'                 -> nothing   (qou)
    find folio-assistant -name 'pdf-structure*'   -> nothing   (pinned 428ca5c)

`AGENTS.md:5243` attributes them to *"folio-assistant's
`scripts/pdf-structure.py` + `extract-candidates.py`"*, and
`scripts/migrate-uploads-to-library.py:7` says the same. They are in neither.

## Why it is worse than a missing tool

`migrate-uploads-to-library.py` does **not** key the doc-id on the filename by
design. `build_mapping()` is documented *"basename.pdf -> doc-id, **from the
generated `structure.json` files**"* — it reads `pdf-structure.py`'s **output**
and only falls back to the basename when no `structure.json` claims the PDF. Its
own comment calls that fallback benign:

> Fallback for PDFs no structure.json claims. Two causes, **both benign**: a
> duplicate upload (`X (1).pdf` beside `X.pdf`) and an alternate filename for
> the same arXiv id — in both cases another PDF wrote the directory and won the
> `source.file` field.

**It does not anticipate the third cause: `pdf-structure.py` never ran.** Then
*no* `structure.json` exists, the mapping is **empty**, and **every** PDF takes
the fallback — which is precisely the orphan-minting path. The comment's
"benign" reasoning assumes a sibling directory that, in that case, does not
exist.

## Relation to `qou-cvx9` — sharpened, not contradicted

`qou-cvx9` diagnoses the two scripts as keying on different things
(filename vs page-1 arXiv stamp) and is right about the **effect**. The causal
story is one step short: `migrate` *consumes* the stamp-derived id and degrades
to the basename only in the producer's absence. So the precondition is not "two
conventions disagree", it is **"the producer has not run"** — which here is
guaranteed, because the producer is not present.

That also means the guard `qou-cvx9` proposes (reconcile the two keys) treats
the symptom. The stronger guard is: **`migrate` should refuse when
`build_mapping()` comes back empty**, rather than silently rewriting every path
to a basename.

## Scoped honestly: this is about THIS container

Siblings demonstrably ingested **17 PDFs** today (`2c567cca9c`, INDEX 589 → 606),
so the capability exists somewhere — a different container, a newer
`folio-assistant`, or a local copy. **This is not a claim that ingest is broken
corpus-wide.** It is a claim that an agent in a container provisioned like this
one cannot complete an ingest, and that if it runs `migrate` alone it will mint
orphans without warning.

## Five open beans cite the bare path as if it were qou-relative

`qou-cvx9`, `qou-k1hs`, `qou-qad3`, `qou-47nf`, `qou-b9c3` — each carries an
ingest recipe naming `scripts/pdf-structure.py`. **I propagated it too**, in
coordination comments on #6962 and #6964 today, without checking it resolved.
The bare form reads as qou-relative and is not.

## Next steps, none taken

1. **Guard `migrate`** — refuse (or warn loudly) on an empty mapping. Small,
   local, and it converts a silent orphan into an error. The best value here.
2. **Fix the path in the five beans and in `AGENTS.md:5243`** to say where the
   producer actually lives, once that is known.
3. **Establish where it lives.** It is not in `folio-assistant` at the pinned
   `428ca5c`; `.folio-assistant-pin` may simply predate it, since that pin is
   169 commits behind `main` per the AGENTS.md §4d note. Checking a newer
   folio-assistant is the cheapest next measurement and I have not done it.

## Detector note, for whoever generalises the selector

The raw run reports **80** open beans naming a vanished path, and that
over-reports. Three classes, and only the third is a finding:

* **placeholders** — `computations/X.witness.json`, `computations/substrate/x.py`
  are metasyntactic examples in prose;
* **moved, not deleted** — `computations/_deprecated/hecke_core_legacy.py` is now
  `computations/hecke_core_legacy.py`; several hits are elided paths (`.../`)
  that the regex mangled;
* **genuinely absent** — this one.

Do not quote the 80. The selector is worth keeping, but it wants the first two
classes filtered before it is a gate.
