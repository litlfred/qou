---
# qou-yqko
title: Move content/ to folio/ to match the platform convention
status: todo
type: feature
priority: normal
tags:
    - platform
    - migration
created_at: 2026-09-26T11:19:21Z
updated_at: 2026-09-26T11:25:43Z
parent: qou-n4r9
---

**Owner direction, 2026-09-26:** *"Can move content/ for to folio/ to match.
Align to f-asst unless specific reason not to"*.

This **reverses the premise of `harness.json`**, which exists (its own words)
because *"qou keeps `content/` — five folios, a bun workspace, CI paths and every
cross-reference in the corpus point at it — so rather than move the tree, it SAYS
where the tree is."* The owner has now said the tree may move.

## Measured blast radius

| population | files |
|---|---|
| tracked files under `content/` | **18,768** |
| files outside `content/` mentioning the string `content/` | 36,653 |
| …of which are in `library/` | **31,241** |
| …of which are in `.beans/` | 1,161 |
| **genuine path-shaped referrers** (excl. `library/`, `.beans/`) | **4,237** |

Largest referrer groups: `content/quantum-observable-universe` 2,655 files,
`content/pipeline` 1,988, `content/schema` 1,155. Seven `.github/workflows/*`
reference it.

## 🛑 THE TRAP, and it would look like success

The 31,241 `library/` hits are **not paths**. They are JSON-LD namespace URLs:

```json
"@context": "https://litlfred.github.io/folio-assistant/ns/content/v1.jsonld"
```

That is the platform's own `ns/content/v1` vocabulary, nothing to do with qou's
directory. A naive `sed -i 's|content/|folio/|g'` across the tree would rewrite
all 31,241 to `ns/folio/v1.jsonld`, **break every block's JSON-LD context**, and
report a clean rename. The knowledge graph would go quiet rather than error —
`corpus_search`'s `emptyRoots` case, which AGENTS.md already warns reads as
"nobody has done this".

**So the rename must be path-anchored, never string-anchored.** Match
`content/<known-folio-dir>` and `content/{schema,pipeline}` explicitly; never bare
`content/`.

## `content/pipeline` may be largely STALE already

1,988 files reference it, but the pipeline moved to the platform in the miga
migration — `folio-assistant/content/pipeline/`. So a large share of those
referrers may already be dead and should be audited as part of this, not blindly
rewritten. Measure before rewriting; a dead reference rewritten is still dead.

## Sequencing

Do this when nothing else is in flight. It touches ~23k files and will conflict
with every open branch. It should land **after** `qou-yf1y` (so the declaration
can point at `folio/` in the same change) and ideally after `qou-utbr` (so the
`.beans/` referrer count is not being rewritten twice).

`harness.json`/`qou.json`'s `directories[0].path` changes `content/` → `folio/`
in the same commit, or the declaration points at a directory that no longer
exists.

## Not started. No files moved.
