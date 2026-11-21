# `home_page/` — a Jekyll site index, imported unwired

Two files: `_config.yml` (`baseurl: "/qou"`, `title: "litlfred's Papers"`,
`theme: minima`) and `index.md`, a table linking the paper, its viewer, its PDF
and its markdown, plus a formalization-resources table.

**Nothing here is wired to anything.** No workflow reads it, this repository
publishes `gh-pages` by another route, and importing it changes no build.

## Where it came from

`litlfred/folio-assistant` at `cat-harness/home_page/`, put there by the
2026-09-20 repo partition along with `blueprint/`. That repository's `AGENTS.md`
says the platform holds no folio content, so it is leaving
([folio-assistant#1223](https://github.com/litlfred/folio-assistant/issues/1223)).
No copy existed here on `main` or `gh-pages`, so it is imported rather than
deleted. Issue #7452.

## Read this before deciding where it lands

**Two of the three things `index.md` links do not exist on this repository's
`gh-pages`.** Measured 2026-09-24 against `gh-pages` (`45cf621dd`):

| link in `index.md` | on `gh-pages`? |
|---|---|
| `papers/…` | **yes** |
| `blueprint/` | **no** |
| `blueprint.pdf` | **no** |

Importing the page does not make them resolve. `blueprint/` arrives in the same
change as unwired source, so the first link could be made to resolve by building
it; `blueprint.pdf` would need the print target run and published.

So this is a site index for a site that was never published in this shape. It is
imported to avoid destroying the only copy, not because it is ready to serve.
Deleting it, rewriting its links, or wiring it to a build are all open — and all
of them are better decided here, where the site it describes actually lives,
than in the platform repository it was sitting in.
