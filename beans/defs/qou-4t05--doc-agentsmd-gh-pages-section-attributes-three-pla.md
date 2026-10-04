---
# qou-4t05
title: 'DOC: AGENTS.md gh-pages section attributes three platform workflows to this repo'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-26T13:05:38Z
updated_at: 2026-10-04T15:18:53Z
parent: qou-n4r9
---

## The defect

AGENTS.md §"Build output (gh-pages)" opens:

> Three workflows deploy to the `gh-pages` branch.

and then gives a **"Workflow → artifact mapping"** table plus an "Expected gh-pages contents"
table, both keyed on `blueprint.yml`, `lean_ci.yml` and `publish.yml`. Read in this repo, that
says three local workflow files. **None of the three is in `qou/.github/workflows/`** (13
workflows there; measured 2026-09-26).

**They are not gone — they are the PLATFORM's**, all three present in
`folio-assistant/.github/workflows/`, reached from qou by one line in
`.github/workflows/build.yml`:

    uses: litlfred/folio-assistant/.github/workflows/publish.yml@main

So the pipeline is live and the *mapping* is substantially still correct; what is wrong is the
**location attribution** and the sentence "Three workflows deploy" stated of this repo.

## Why this is worth a bean rather than a shrug

It produced the exact false conclusion it invites, in the session that filed it. Working
`qou-w5av` (deprecate qou rendering) I grepped `.github/workflows/`, found nothing, and
reported to the owner that "all three workflows AGENTS.md documents are ABSENT" and "the whole
gh-pages section describes workflows that don't exist" — i.e. I read a relocation as an
excision, and told the owner the render pipeline was gone when it is one `uses:` line away.
Retracted in `qou-w5av` in the same PR.

This is the repo's own detector-blindness class one level up: **the surface I measured was the
wrong tree, and an empty result read as an absence.** AGENTS.md is the file every agent loads
first, so the mis-attribution is maximally reachable.

## What is actually dead (one row, dead on both sides)

`home_page/` — AGENTS.md's project-structure table calls it *"Jekyll landing page for GitHub
Pages"*. Measured:

- **does not exist** in qou — `ls home_page/` fails; not merely empty. `git ls-files` 0.
- `home_page` appears **nowhere** in the platform's `publish.yml` either.
- no `_config.yml` anywhere in qou.

So that row describes nothing, on either side of the split.

## The negative — do NOT "clean up" `paper-builder-image.yml`

It is the obvious next wrong inference and it is wrong. That workflow builds
`ghcr.io/litlfred/qou-paper-builder:latest`; six of its comments name `publish.yml`
("what publish.yml pins", "Phase B of the publish.yml parallelization plan"), and publish.yml
is not in this repo — so it presents as a live workflow feeding a deleted one. Measured
otherwise: `build.yml` passes the image in as `builder_image:`, and the platform's
`publish.yml` consumes that input at **three** job sites (lines 402 / 518 / 582) and hardcodes
`qou-paper-builder` at **none**. `build.yml`'s own comment states the intent — the TeX image is
a folio asset, passed in so the platform pipeline stays folio-agnostic. It is correctly wired.

## Blast radius of the same mis-attribution elsewhere

`publish.yml` is named in **25 files** outside `beans/`+`library/`, of which only **2** qualify
it as the platform's. The other 23 read as references to a local file. Discriminated by
whether the reference is prose or code:

- **Nothing executes a dead reference.** All hits in `computations/run_pipeline.py` (2),
  `scripts/make-all-tables.py` (1), `paper-builder-image.yml` (6) and `build-lean-mcp.yml` (2)
  are in comments/docstrings. So there is **no functional breakage** — this is a
  documentation-currency defect only, and saying otherwise would overstate it.
- **Live instruction surfaces** (worth fixing): `AGENTS.md` (10 hits), `docs/ARCHITECTURE.md`
  (7), `.claude/skills/local/docs-generation.md` (8 — a *routed* skill, so an agent is sent
  there), `CONTRIBUTING.md` (2), `README.md` (1), two more `local/` skills (1 each).
- **Dated audit / workplan docs** — deliberately NOT in scope. Same decision as the `4.66e6`
  drain (`qou-3nva`): they are records of their own analyses at their own dates.

## Proposed fix (small, and it is a doc change — ASK-THE-OWNER applies)

1. AGENTS.md §"Build output (gh-pages)": replace "Three workflows deploy to the `gh-pages`
   branch" with a sentence naming the platform as their home and `build.yml`'s `uses:` line as
   the entry point. Keep both tables — they still describe the artifacts correctly.
2. Delete the `home_page/` row from the project-structure table.
3. Same relocation note in `docs/ARCHITECTURE.md` and `local/docs-generation.md`.

Not exempt under either ASK-THE-OWNER carve-out (it raises no precision), so it waits — except
the `home_page/` row, which is exemption 2 (the corpus decides it: the directory is absent and
the platform never names it).

**Interaction with `qou-w5av`:** if that bean's just-the-docs adoption lands, this section gets
rewritten anyway. Fixing it first is still worth it, because it is what mis-led the analysis
*of* `qou-w5av`.



## Reasons for Scrapping

Duplicate of `qou-9olr` (work-plan reorganisation 2026-10-04). Evidence: [B] both about AGENTS.md gh-pages section mis-attributing workflows; 9olr carries the corrected 3-way measurement
Content is untouched; only this work item is closed.
