---
layout: default
title: Home
nav_order: 1
---

# Quantum Observable Universe — documentation

This site renders the repository's `docs/` tree. **The paper itself is not here** —
it lives as content objects under `content/quantum-observable-universe/`, and the
`.md` file of each block is its authoritative human-readable face.

What is here is the working record around that paper.

## Sections

| section | `.md` | what it holds |
|---|---:|---|
| **Audits** | 2,584 | Dated records of a single analysis each. **Not in the sidebar** — see below. |
| [Coordination](coordination/) | 190 | Ledgers for multi-session arcs: who is on what, what closed, what is still open. |
| [Workplans](workplans/) | 106 | Planned tranches, mostly historical. |
| [Scope](scope/) | 58 | Scope determinations. |
| [QA](qa/) | 16 | QA-pipeline notes. |
| [Handover](handover/) · [Ports](ports/) | 7 | Session handovers and port notes. |
| *(top level)* | 53 | Cheat sheets and standing references, including the canonical-derivation cheat sheet and the precision goals. |

Total **3,038** markdown files. `docs/_archive/` is excluded from the site.

## Why the audits are not in the sidebar

`docs/audits/` is **2,584 of the 3,038** markdown files here. A just-the-docs
sidebar with 2,832 leaves is not navigation, it is a wall — and the navigation is
the reason the theme was chosen. So audits carry `nav_exclude: true`.

They are **not** excluded from the site. Every one is rendered, linkable, and
**searchable** — just-the-docs indexes `nav_exclude`d pages, so the search box is
the way in. Use it rather than the sidebar.

## How this site is built

Front matter is **injected into a staging copy** by
[`scripts/docs-site-frontmatter.py`](https://github.com/litlfred/qou/blob/main/scripts/docs-site-frontmatter.py),
never into the repository. Jekyll renders a `.md` file only if it carries front
matter — without it the file is copied verbatim as a static asset — and **0 of
3,037** of these files had any. Rather than rewrite every dated audit record to
satisfy a renderer, the generator adds what Jekyll needs at build time and leaves
the records as records.

The theme is [just-the-docs](https://github.com/just-the-docs/just-the-docs),
pinned to the same ref the `folio-assistant` platform pins, whose `docs-site.yml`
this build mirrors. It mirrors rather than calls it because that workflow declares
no `workflow_call:` trigger.

## Elsewhere

- **The paper** — `content/quantum-observable-universe/`
- **The work plan** — `beans/defs/`, via the `beans` CLI
- **Agent instructions** — [`AGENTS.md`](https://github.com/litlfred/qou/blob/main/AGENTS.md)
