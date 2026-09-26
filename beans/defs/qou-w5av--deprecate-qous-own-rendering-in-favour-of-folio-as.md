---
# qou-w5av
title: Deprecate qou's own rendering in favour of folio-assistant justthepages
status: todo
type: feature
priority: normal
tags:
    - rendering
    - platform
created_at: 2026-09-26T11:21:37Z
updated_at: 2026-09-26T11:27:38Z
parent: qou-n4r9
---

**Owner direction, 2026-09-26:** *"Want to deprecate qou rendering and move to
folio-assistant justthepages"*.

## 🛑 BLOCKED ON A DEFINITION — and this is an ABSENCE, not a conclusion

**I could not find `justthepages`.** Stating the surfaces searched, because
"I found nothing" and "it does not exist" are different claims and only the first
was measured:

| searched | result |
|---|---|
| `git grep -il 'justthepages\|just-the-pages\|just_the_pages'` over platform `origin/main` (`42ccfb38b63`) | **0 hits** |
| GitHub repository search, query `justthepages` | `total_count: 0` |
| the 60 repositories this session can reach (`list_repos`) | absent |
| platform file tree, `*page*` and `*render|publish|latex*` | nothing by that name |

Nearest things that do exist: `litlfred/folio-test`, `litlfred/cat-harness-test`
(neither in this session's repo scope), and the platform skills
`.claude/skills/local/content-publish.json` and `document-publishing.json`.

**What would separate the possibilities**, so the next agent does not re-search:
it is either (a) a repo not yet created or not yet shared with this session, (b) a
folio-assistant feature/mode under a different internal name — `content-publish`
and `document-publishing` are the candidates — or (c) shorthand for a *pages-only*
publish path, i.e. HTML to `gh-pages` without the LaTeX/PDF jobs. **Owner input
resolves this in one line; nothing else will.**

## What "qou rendering" actually is — measured, so the scope is known either way

qou-side:

- `main.tex`, **964 lines** of preamble + document structure
- `chapters/*.tex` — **36 files, 0 tracked**; `.gitignore` lines 15-17 mark them
  *"Generated LaTeX chapters (from content pipeline)"*, so the `.tex` layer is
  already a build artifact rather than source
- `*.pdf` gitignored, with one carve-out: `!content/**/rendered/*.pdf`

platform-side, via `.github/workflows/build.yml:10` calling
`litlfred/folio-assistant/.github/workflows/publish.yml@main`: jobs
`content-pipeline`, `paper-pdf`, `appendix-pdfs`, `blueprint-html`, `diff-pdf`,
`per-chapter-split`, `assemble`, `deploy`, stated critical path ~15-20 min.

**So most of "qou rendering" is already the platform's.** What is genuinely qou's
own is `main.tex` and the 13 local workflows. That materially shrinks this story
from what it sounds like — and it means the real lever is the `uses:` line, which
is `qou-pwp9`.

## What deprecating it would have to preserve

The README's `folio:toc` section renders PDF links per chapter, and **38 of 40
chapters already render `—`** because no per-chapter PDF exists on `gh-pages`
(measured 2026-09-26). So the current rendering pipeline is *already* not
producing most of what the README advertises. Any replacement should be judged
against that, not against an imagined working baseline — and if `justthepages`
drops PDFs entirely, the honest move is to drop the PDF column too rather than
leave 40 em-dashes.

## Not started, and deliberately

No workflow disabled, no `main.tex` touched. Deprecating a render path before
knowing what replaces it would leave the folio with neither.
