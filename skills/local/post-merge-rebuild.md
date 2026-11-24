---
name: post-merge-rebuild
description: Rebuild and publish qou's site after a merge to main, from an agent's checkout, because GitHub Actions is not enabled on push. Run after every merge to main.
roles: [collaborator]
---

# post-merge-rebuild

Owner, 2026-11-23: *"agents should rebuild when merge to main if github actions
not enabled"*. Actions on qou is `workflow_dispatch`-only (owner directive
2026-06-30, billing), so a merge to `main` does not rebuild the site. The agent
that merged does.

## When

After **every** merge to `main` you perform or are told about, unless the
GitHub Actions run of `build` was dispatched for that commit and succeeded.

## How

```bash
cd ~/space_cats/qou        # or the container's checkout
bash scripts/setup-folio-assistant.sh   # once per container; installs the pinned platform
git fetch origin main && git switch main && git pull --ff-only
bash scripts/publish-main-local.sh --deploy
```

`publish-main-local.sh` runs the same steps, in the same order, as the
`publish-main` job of the platform's `folio-staging.yml`, which `build.yml`
calls when someone dispatches it:

0. `python3 scripts/generate-accuracy-scorecard.py --check --qa-report` (skill
   `accuracy-scorecard`), failing fast before the site build if `ACCURACY.md`
   drifted from its 12 upstream witnesses, failed public-reader hygiene, or lost
   its `README.md` link;
1. `scripts/build-site.sh`, the folio site plus `_site/accuracy/index.html`
   (`/accuracy/`) plus the Lean library render (folio-assistant-sci skill
   `lean-html-docs`), staged at `_site/lean/`;
2. the harness rail (`rail-standalone-pages.ts --foreign-site`), which rails
   both standalone harness pages and `/accuracy/`;
3. `publish-main-site.ts`, which deletes only the files its previous publish
   listed in `_main-site.json`, so `branches/`, the July `lean/`, `drafts/` and
   the PDFs README links are left alone;
4. a render-log entry and one commit on `gh-pages`;
5. the push (only with `--deploy`).

Without `--deploy` it stops after the commit in `.gh-pages-worktree/`, which is
the way to check a run before publishing.

## The Lean render needs Lean

`build-site.sh` builds `lean/` only when `lake` is on `PATH`. It restores the
warm cache first (`lean-docs-build.sh --restore`, about 2 minutes). Without
`lake` it prints **SKIPPED** and the site is published without a fresh
`lean/`. Say so in the merge report. `QOU_LEAN_DOCS=1` makes a missing `lake`
an error, for a run that must include it.

## Report

State in the merge report: the merged sha, whether the push happened, and
whether `lean/` was rebuilt or skipped. A skipped rebuild is reported, never
silent.

## What this does not do

- It does not build the TeX PDFs. `publish.yml` did, and the platform deleted
  it on 2026-11-10; nothing replaces it yet.
- It does not touch `branches/` previews. A branch preview is
  `folio-staging.yml` dispatched on that branch, or the platform's
  `stage-folio-local.ts`.
