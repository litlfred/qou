---
# qou-za45
title: chapters/ holds two generated .tex that .gitignore excludes and git tracks — the 2026-03-21 decision to untrack them was silently undone
status: completed
type: bug
priority: normal
created_at: 2026-08-24T17:38:47Z
updated_at: 2026-08-24T17:39:22Z
---


## What is going on with `chapters/`

It holds exactly two files, `brings-surface.tex` and `introduction.tex`, and
both are **generated LaTeX** — `\clearpage`, `\chapter*{…}`, `\chapterannot`,
the output of `content/pipeline/build.ts --out-dir chapters/`.

`.gitignore:16-17` excludes them:

```
# Generated LaTeX chapters (from content pipeline)
chapters/*.tex
chapters/*.md
```

They were tracked anyway, and `.gitignore` has no effect on an
already-tracked path.

## The decision to untrack them already exists

`4960cda5` (2026-03-21) — **"Remove generated .tex chapters from repo; build
as part of pipeline"**:

> - Add `chapters/*.tex` and `chapters/*.md` to .gitignore (generated artifacts)
> - **Remove 25 tracked chapter files from git** (content pipeline generates them)
> - Make content build step in publish.yml required (no fallback to "existing
>   LaTeX chapters" since they no longer exist in the repo)
>
> The content pipeline (.ts + .md → .tex) is now the **sole source** of chapter
> LaTeX, both in CI and local MCP builds.

25 files removed, the rule written down. Two came back.

## How they came back

`f0ebd9b830` (2026-07-08, Carl Leitner) — *"docs: move Descartes quote to
Bring's Surface chapter"*. Both files appear in that diff as `new file mode`,
2438 insertions, 0 deletions. The commit's PURPOSE was a content edit; the
artifacts rode along with it.

**The content edit survived and is fine.** The quote lives in
`content/quantum-observable-universe/introduction/intro.md` line 1 today, and
renders into `chapters/introduction.tex`. Nothing is lost by untracking.

Two later commits treated them as a fixture rather than a mistake:
`790a45515` (2026-08-16) noted *"`chapters/brings-surface.tex` and
`chapters/introduction.tex` are the only two chapter artifacts git tracks;
refreshed in the same pass"*, and `4466753ec` (2026-08-17) refreshed one again.
Refreshing a file the repo has already decided not to track keeps the
inconsistency alive at the cost of a rebuild each time.

## Why it matters — the repo has already been bitten, twice

Both are recorded in `790a45515`'s own message:

1. **`main.tex` is tracked, generated, and drifted** — the committed copy had
   lost five chapters, so *"Building from it renders a PDF that is silently
   missing content"*: `knots-particles-confinement`, `eightfold-way`,
   `nuclear-interactions`, `appendix-standard-model`, `appendix-nf-witnesses`.
2. **A hand-edit to a generated file was silently reverted on every
   regeneration** — a `\newunicodechar` fix applied to the artifact instead of
   the preamble it comes from.

And the two files are stale right now: last content change **2026-08-19**,
while `brings-surface/` and `introduction/` sources both changed **2026-08-24**.
A reader opening them gets a chapter that no longer matches its source.

## Fix

`git rm --cached chapters/brings-surface.tex chapters/introduction.tex`. The
files stay on disk, `.gitignore:16` now actually applies, and the pipeline
remains the sole source exactly as `4960cda5` intended.

## The wider class — reported, not fixed here

`git ls-files -i -c --exclude-standard` lists **29 tracked-but-ignored files**.
Same shape, different risk:

- **generated LaTeX**: `main.tex`, `qou-all-tables.tex`,
  `standalone-index-of-definitions.tex`
- **build output**: `papers/quantum-observable-universe/quantum-observable-universe.pdf`
- **reference PDFs**: ~18 under `uploads/` and the repo root
- other: `content/bun.lock`, `.beans/integration-audit-ledger.md`,
  `.agents/rules/lean-infra-rule.md`,
  `computations/delta-lambda-empirical-tabulation.witness.json`,
  `todos/qa-q-CAL-1-2-3-audit.json`

`main.tex` is the one with a live defect history, but untracking it is not the
obvious call: `790a45515` deliberately REGENERATED it rather than removing it,
so something may want it present. Left for the owner.
