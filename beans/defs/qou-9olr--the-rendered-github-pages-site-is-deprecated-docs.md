---
# qou-9olr
title: The rendered GitHub Pages site is deprecated, docs-site is the only workflow that has ever succeeded since 2026-06-30, and AGENTS.md documented three workflows absent from the tree
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-27T07:41:07Z
updated_at: 2026-10-04T15:25:00Z
parent: qou-n4r9
---


## 2026-09-27 — RETRACTION, and it is the third wrong answer to one question

This bean's own title says *"AGENTS.md documented three workflows absent from
the tree"*. **That claim is wrong, I pushed it to `main` in #7480, and I am the
second session in two days to make it.**

### The three readings, all wrong, in different ways

| | claim | verdict |
|---|---|---|
| 2026-09-26, bean `qou-w5av`, first pass | all three ABSENT | wrong for `publish.yml` |
| 2026-09-26, `qou-w5av`, self-correction | *"they MOVED — all three exist in the platform"* | wrong for `blueprint.yml` / `lean_ci.yml` |
| 2026-09-27, mine (#7480) | all three ABSENT | repeats reading 1, having not read `qou-w5av` |

### What is actually true, measured three ways

| workflow | qou `.github/workflows/` | platform `.github/workflows/` | reality |
|---|---|---|---|
| `publish.yml` | absent | **PRESENT** | **live on dispatch** — `build.yml:27`, `uses: litlfred/folio-assistant/.github/workflows/publish.yml@37a36ce9296…`, pinned to `.folio-assistant-pin` |
| `blueprint.yml` | absent | absent | a **TEMPLATE**: `cat-harness/templates/paper/github/workflows/blueprint.yml` |
| `lean_ci.yml` | absent | absent | same — template only |

So: **one of the three is live, two are paper-scaffolding templates runnable
nowhere.** Neither "all absent" nor "all moved to the platform" is right.

### What the error contaminated, and what it did not

Contaminated, now fixed on the branch: `AGENTS.md` §"Build output (gh-pages)"
(two blocks), `README.md` §Published Artefacts, `docs/ARCHITECTURE.md`,
`.claude/skills/local/docs-generation.md`, and the #7480 PR body + commit
message (the commit message stands as history; a correction comment is on the
PR).

**The load-bearing false inference was not the count — it was *"every workflow
that produced any of it is gone or dead, so the snapshot cannot be
refreshed"*.** The paper-build half of `gh-pages` (`papers/`, `index.html`, the
PDFs, `schema-docs/`, `drafts/`) has a **live** producer. The site is stale
because `build.yml` has not been **dispatched** since 2026-06-30 — dormant, not
unrefreshable, and the remedy is a dispatch rather than a rebuild. Only the
`lean/` subtree genuinely has no producer left.

**NOT contaminated — the deprecation actions are unaffected**, because they rest
on the owner's instruction rather than on my reasoning: `doc-gen4.yml` →
`fsh-guts/deprecated/workflows/` (461 runs, dead since 2026-06-30, only job was
`gh-pages/lean`), the `docs-site.yml` publish step removed (never fired in 5
runs — independently verified by `git ls-tree`), and the README's rendered
column dropped. Also unaffected: `docs-site` being the only workflow to succeed
since 2026-06-30, the six never-run gates, and there being no STAGING pipeline
on qou.

### Why it happened, which is the reusable part

Two causes, and the second is worse.

1. **I measured qou's tree and reported an absence as an existence claim.** The
   repo's own detector-blindness taxonomy is largely about this; `qou-w5av`
   names it in those words.
2. **`qou-w5av` was returned by my own corpus-grep and I misread my own
   output.** I ran `grep -ril "gh-pages.*deprecat" beans/defs`, it printed
   `qou-w5av--deprecate-qous-own-rendering-in-favour-of-folio-as.md`, and I
   read past it to an `echo "(empty = no existing bean)"` marker on the next
   line and created this bean anyway. Path 6 of the corpus-grep checklist
   worked exactly as designed; **the failure was downstream of the grep, in
   reading its result.** A checklist cannot protect against that, which is why
   it is worth writing down.

**Do NOT delete or "clean up" `build.yml` or `paper-builder-image.yml`.**
`build.yml` is qou's only render entry point and produces the paper PDFs
README's chapter table links; `paper-builder-image.yml` builds the TeX image
`build.yml` passes in as `builder_image:`, consumed at three job sites in the
platform's `publish.yml` and hardcoded nowhere. Whether PDF output goes away is
an owner decision, framed in `qou-w5av`.

**Superseded-by note:** the live carrier for the rendering question is
**`qou-w5av`** (*"Deprecate qou's own rendering in favour of folio-assistant
justthepages"*, `todo`, parent `qou-n4r9`). This bean should have been an append
to it. Keeping it as the record of the retraction, cross-referenced both ways.
