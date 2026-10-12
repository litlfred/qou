# Folio site render size: where the bytes go (2026-10-10)

Owner ask, 2026-10-10: *"examine/analyze the render pipeline so html does not get
too big … where possible, load content from a KG and have thin .html pages for each
chapter/section/sub-section/…/content-block … look at existing cat-harness infra and
reuse … add in [edit] and [feedback] links like the other renderers."*

## What was measured

- **Pipeline:** folio-assistant-core `scripts/build-folio-site.ts` (platform main
  `05fcf008ea`, folio-assistant-core mount `a5a5837b`). Then qou's
  `scripts/folio-site/qou-site-extras.py`, then cat-harness
  `rail-standalone-pages.ts --foreign-site` and `staging-banner.ts`, all run by
  `scripts/folio-site/stage.sh`.
- **Corpus:** qou `591753053` (this branch).
- **Method:** Chromium via Playwright against a local server. Every response body is
  summed by type. Sizes are **uncompressed**; GitHub Pages gzips JSON, JS and CSS, so
  transfer is smaller (for example `outline.json` is 736 KB raw and 114 KB gzipped).

## The pipeline is already "thin shells + KG payloads"

`build-folio-site.ts` writes one small HTML shell per paper, chapter and section
(400 shells for qou). It also writes one JSON payload per block: the block's KG node
(`<block>.jsonld`) plus rendered `html`, 3,616 files with an average of 4.2 KB. A
shell fetches only the blocks in its scope, and loads them a unit at a time as the
reader scrolls. **Edit** and **feedback** already come from the platform's shared
`edit-links.js`, the same recipe the other renderers use.

So the architecture the owner asked for exists. What is too big is what every page
loads *besides* the content.

## Per-page bytes: a section page with 2 blocks

`quantum-universes/qou-intro/`, 2,940 KB total:

| what | KB | share | whose |
|---|---:|---:|---|
| `outline.json` (whole paper: chapters, labels, numbers) | 735.8 | 25 % | platform `build-folio-site.ts` |
| `docs-ui.js` | 613.7 | 21 % | platform harness chrome |
| KaTeX (JS, CSS, fonts) | 409.5 | 14 % | CDN |
| `docs-ui.css` | 374.6 | 13 % | platform harness chrome |
| three `landing-*-card.webp` images | 684.6 | 23 % | platform navbar (loaded eagerly on a paper page) |
| `navbar-row.js` | 22.7 | 1 % | platform |
| qou QA summary for the chapter | 20.2 | 0.7 % | qou |
| **block payloads (the content)** | **5.9** | **0.2 %** | |
| HTML shell | 7.9 | 0.3 % | platform, after rail and banner injection |

The content is 0.2 % of what the page loads. The chrome, KaTeX and images are cached
after the first page. `outline.json` is fetched by **every** page, a single-section
page included.

## Findings, in order of payoff

1. **`outline.json` is the whole paper's index, fetched by every page.** It is 736 KB:
   `labels` 334 KB, `chapters` 305 KB, `numbers` 119 KB. A section page needs its own
   chapter's outline and nothing else. `labels` and `numbers` are needed only to
   resolve a cross-reference.
   *Proposal (platform):* write a small top-level outline (chapter titles only), one
   outline per chapter, and a label index sharded by chapter that is fetched only when
   a `#label` is not on the page. Expected per-page cost: roughly 10–40 KB instead of
   736 KB.
2. **The navbar loads three landing-card images (685 KB) on a folio page.** They
   belong to the platform's landing or glass tiles.
   *Proposal (platform):* `loading="lazy"`, or load them only on the surface that
   shows them.
3. **The harness chrome (`docs-ui.js` + `.css`, 988 KB) is one bundle for every
   surface.** It is cached across pages, so this is a first-visit cost.
   *Proposal (platform):* split the bundle so a standalone folio page loads only the
   navbar and rail.
4. **Rail injection grows each shell from about 600 B to 7.9 KB.** The JSON islands
   `fa-navbar-row` and `fa-rail` are inlined into every page. `kg-render.js`'s own
   header records the same class of cost on the docs site (a 9.3 KB island repeated
   1,571 times, 14.26 MB).
   *Proposal (platform):* move the islands to one fetched file. This matters before
   adding per-block pages: about 3,600 per-block shells × 7.9 KB ≈ 28 MB, against
   about 2 MB if the shells stay at about 600 B.
5. **Two block payloads are huge.** `recursive-atom-knot-atlas-registry` is 1,066 KB
   and `definition-index` is 388 KB.
   *Proposal (platform or qou):* render large tables lazily or paginate them.
6. **Reuse:** `folio-site.js` implements its own fetch and error handling and writes
   block HTML with `innerHTML`. The platform already has `kg-render.js`, the shared
   three-state fetch (loading / failed / loaded, a load that fails says so) with
   print-waits-for-render, built for exactly this.
   *Proposal (platform):* port `folio-site.js` onto `kg-render.js`.
7. **Fixed this session (qou side):** the per-block QA payloads were 34 requests and
   630 KB on a chapter page, more than the blocks themselves. They are now one
   per-chapter summary (20 KB), with the full report fetched only when the [QA] badge
   is clicked.

## Per-content-block pages (not built yet)

Today a block is reachable as `<section page>#<label>`; there is no page of its own.
Adding `<paper>/b/<label>/index.html` is a small change to `build-folio-site.ts` and
`folio-site.js`: the shell names one block, and the loader shows that one payload
with its breadcrumbs. Do **finding 4 first**, or the site grows by about 28 MB of
repeated chrome.

## Why most of this is a platform change

The renderer is in `litlfred/folio-assistant-core`, and the chrome is in
`litlfred/cat-harness`. This session could not push to either repository. Only
finding 7 is fixable in qou alone.
