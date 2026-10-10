---
# qou-w5av
title: Deprecate qou's own rendering in favour of folio-assistant justthepages
status: todo
type: feature
priority: normal
tags:
    - rendering
    - platform
    - reorg-2026-10-04
created_at: 2026-09-26T11:21:37Z
updated_at: 2026-10-04T15:15:53Z
parent: qou-n4r9
---

## 🟩 UNBLOCKED 2026-09-26 — the owner answered: "just the docs rendering pipeline"

**`justthepages` is not a repo. It is literal: the `just-the-docs` Jekyll theme**, i.e. the
platform's docs rendering pipeline. Confirmed at platform main `42ccfb38b63`:

    cat-harness/docs/_config.yml:
      remote_theme: just-the-docs/just-the-docs@v0.12.0     # PINNED
      title: folio-assistant
      baseurl: "/folio-assistant"
      url:     "https://litlfred.github.io"

- **1,210 files** under `cat-harness/docs/` — a full Jekyll site: `_config.yml`, `_data/`
  (`harness.json`, `stickies.json`, `translations.json`, translation-QA data), `_includes/`
  with a `generated/` subtree (`navbar-footer.html`, `todo-listing.html`), and multi-language
  page trees (`ar/` present).
- Built by **`.github/workflows/docs-site.yml`** via `actions/jekyll-build-pages` (which
  whitelists `jekyll-remote-theme`). The `Gemfile` is for local preview only — its own header
  says CI does not use it.

So my three earlier candidates are resolved to the third: a **pages-only publish path**, and
specifically a Jekyll/just-the-docs one. The searches that found nothing were looking for the
wrong kind of thing (a repo name), which is why every surface came back empty.

## 🛑 THE SCOPE IS MUCH SMALLER THAN THIS BEAN'S TITLE SUGGESTS — measured

"Deprecate qou rendering" implies there is a qou rendering pipeline to retire. **There is
almost nothing left.** Measured 2026-09-26:

### 🛑 CORRECTING MY OWN CLAIM FROM AN HOUR AGO — they are NOT absent, they MOVED

I reported in chat that all three workflows AGENTS.md §"Build output (gh-pages)" documents
are **ABSENT**, and that "the whole gh-pages section describes workflows that don't exist."
**That is wrong, and the error is the one this repo's own detector-blindness taxonomy is
about: I measured the wrong tree.** All three exist — in the *platform*:

| workflow AGENTS.md documents | in `qou/.github/workflows/` | in `folio-assistant/.github/workflows/` |
|---|---|---|
| `blueprint.yml` | absent | **PRESENT** |
| `lean_ci.yml` | absent | **PRESENT** |
| `publish.yml` | absent | **PRESENT** |

They are reached from qou by exactly one line, `.github/workflows/build.yml`:

    uses: litlfred/folio-assistant/.github/workflows/publish.yml@main

So **the rendering pipeline is live, not gone.** What is stale in AGENTS.md is the *location
attribution*, not the existence: its "Workflow → artifact mapping" table reads as a list of
files in this repo, so an agent that greps `.github/workflows/` for `blueprint.yml` finds
nothing and concludes the pipeline was deleted. I did exactly that. That is a real doc defect
worth fixing — but it is a one-paragraph relocation note, not the excision it looked like.

**And the obvious next wrong inference, pre-empted by measurement:
`paper-builder-image.yml` is NOT orphaned.** It builds
`ghcr.io/litlfred/qou-paper-builder:latest`, its comments say "what publish.yml pins", and
publish.yml is not in this repo — so it reads as a live workflow feeding a dead one. It is
not: `build.yml` passes the image in as `builder_image:`, and the platform's `publish.yml`
consumes that input at **three** job sites (lines 402, 518, 582) while hardcoding
`qou-paper-builder` **nowhere**. The design is deliberate and build.yml's own comment states
it — the TeX image is a folio asset so the platform pipeline stays folio-agnostic. Do not
"clean up" that workflow.

qou's **only** rendering entry point is `.github/workflows/build.yml` — 13 workflows in the
tree, and this is the one — which is `workflow_dispatch:`-only and whose entire job is:

    uses: litlfred/folio-assistant/.github/workflows/publish.yml@main

So the heavy render (`content-pipeline`, `paper-pdf`, `appendix-pdfs`, `blueprint-html`,
`diff-pdf`, `per-chapter-split`, `assemble`, `deploy`; ~15-20 min critical path) is **already
the platform's**, reached by one `uses:` line. What is genuinely qou's own:

- `main.tex`, **964 lines** of preamble + document structure
- `chapters/*.tex` — **36 files, 0 tracked**; `.gitignore` marks them "Generated LaTeX
  chapters (from content pipeline)", so the `.tex` layer is already a build artifact
- `home_page/` — the one AGENTS.md row that IS dead, and dead on both sides. AGENTS.md calls
  it "Jekyll landing page for GitHub Pages"; the directory **does not exist** in qou (not
  merely empty — `ls` fails, 0 tracked), and `home_page` appears **nowhere** in the
  platform's `publish.yml` either. There is no `_config.yml` anywhere in qou.

**So the real lever is still the `uses:` line, which is `qou-pwp9`** — not a deprecation
sweep. (That conclusion is unchanged by the correction above: whether the heavy render lives
in an absent workflow or a present platform one, it is reached through that single line.) And adopting just-the-docs means **creating** a Jekyll site in qou, not migrating one:
there is no existing surface to convert. qou does have **3,070 markdown files under `docs/`**,
which is exactly the corpus a just-the-docs site would render.

## 🟡 THE DECISION THIS EXPOSES, and it is the owner's

**Does the PDF go away?** just-the-docs renders HTML pages. The platform's `publish.yml` is
what produces `quantum-observable-universe.pdf`, the per-chapter PDFs and `blueprint.pdf`.
Moving to a pages-only pipeline means either keeping `publish.yml` for the PDF *and* adding
Jekyll, or dropping PDF output.

Two measured facts that bear on it, in opposite directions:

- **The PDF is already mostly not being produced.** The README's `folio:toc` section renders
  a PDF link per chapter and **38 of 40 chapters already render `—`** because no per-chapter
  PDF exists on `gh-pages` (measured 2026-09-26, and the `gh-pages` branch does exist). So the
  current pipeline is already not delivering most of what the README advertises.
- **This is a mathematics paper aimed at a physics venue as well as a mathematics one**
  (AGENTS.md §"The paper is a MATHEMATICAL MODEL by default"). A submission artifact is a PDF.
  Dropping PDF output entirely is a publication decision, not an infrastructure one.

**Default if nothing is decided:** nothing changes. `build.yml` stays dispatch-only, the
platform keeps rendering on demand, the README keeps showing 38 em-dashes. That is survivable
and is the current state.

**Recommendation, marked as my judgement rather than a finding:** adopt just-the-docs for the
`docs/` corpus and the landing page — that is additive, it fills the empty `home_page/`, and it
needs no decision about PDFs — and keep `publish.yml` for the paper PDF until there is a
reason to drop it. Pin the `uses:` line first (`qou-pwp9`), because an unpinned platform
render is the thing that actually bites.

## Not started. No workflow touched, no `main.tex` change.


---

## The PDF measurement, sharpened — 79 days, with a date (from `qou-pwp9`, 2026-09-26)

The decision above cites "38 of 40 chapters already render `—`" as evidence little is
lost by dropping PDF output. A second, independent and sharper measurement of the same
thing, found while pinning `build.yml`:

**`origin/gh-pages` last deployed 2026-07-08 — 79 days ago.** Its tip is
`45cf621dd0 deploy: update PDF with \pm error formatting`, and there is nothing after it.

So the render pipeline is not merely producing incomplete output; it has produced
**none** for 79 days. That is a stronger form of the same point and it carries a date,
which the chapter count does not.

**It cuts both ways and should not be read as settling the decision.** It strengthens
"little is being lost in practice" — but it equally supports "the pipeline is broken
and should be fixed" rather than "replaced". A dormant pipeline is evidence about
*operation*, not about whether a PDF is *wanted*, and AGENTS.md's standing ruling that
this work must stand up in a physics venue is a statement about the latter. Still the
author's call.

## 2026-09-27 — your self-correction was over-broad too, and I repeated the original error

Recorded from the other side, in `qou-9olr`, after pushing the same wrong claim
to `main` in #7480.

**Your first pass said all three workflows are ABSENT. You corrected that to
*"they MOVED — all three exist in the platform"*. Measured a third time, both
are wrong:**

| workflow | qou | platform `.github/workflows/` | reality |
|---|---|---|---|
| `publish.yml` | absent | **PRESENT** | live on dispatch, `build.yml:27`, pinned |
| `blueprint.yml` | absent | **absent** | `cat-harness/templates/paper/github/workflows/` — a TEMPLATE |
| `lean_ci.yml` | absent | **absent** | same |

One is live; two are paper-scaffolding templates, runnable nowhere. Your
correction's table marks all three PRESENT in folio-assistant, which is right
for one of them.

**I then made your original mistake a day later** — reported all three absent,
in chat and in a durable AGENTS.md rewrite — **because I did not read this
bean, although my corpus-grep returned it.** Retraction, contamination list and
the reading-failure post-mortem are in `qou-9olr`.

**Your PDF/`uses:`-line analysis is unaffected and remains the live framing**;
`build.yml:27` is confirmed pinned to `37a36ce9296`, so `qou-pwp9` landed.
