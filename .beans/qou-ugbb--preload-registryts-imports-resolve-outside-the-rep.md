---
# qou-ugbb
title: preload-registry.ts imports resolve outside the repo (worktree-fragile)
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T20:26:35Z
updated_at: 2026-08-22T20:26:57Z
---

## Finding

`scripts/preload-registry.ts` imported the platform via `../../folio-assistant/…`
on lines 14 and 16. Its own docstring (lines 10-11) says the symlink "is reached
via `../folio-assistant/`", and its sibling `scripts/run-validate.ts:14,16` uses
that single-`../` form. So the file disagreed with both its own documentation and
the only other script doing the same job.

## What it does NOT do — a correction to my own earlier claim

I relayed a sibling agent's report that this breaks `check-sidecars.sh` and that
my sidecar audit "hasn't been running". **Measured, that is false.** From the
repo root at `/home/user/qou`, `../../folio-assistant/` resolves to
`/home/user/folio-assistant` — the real sibling clone the symlink points at —
so the import succeeds by *bypassing* the symlink rather than following it.
`bun run scripts/preload-registry.ts` exits 0 on unpatched `main`.

## What it does do

The resolution is relative to the *file*, so it is correct only for a checkout
sited exactly at `<parent>/qou` with the platform clone at `<parent>/folio-assistant`.
In an isolated `git worktree` — the setup I have been mandating for background
agents — the same import walks two levels up from the worktree's `scripts/` and
lands outside any tree that carries the symlink. Measured on this container:

    /home/user/folio-assistant   exists   (repo-root case, works by accident)
    /home/folio-assistant        absent
    /folio-assistant             absent

## Fix

Lines 14 and 16 → `../folio-assistant/…`, matching `run-validate.ts` exactly
(including dropping the `.ts` extension on line 14). Verified: exit 0.
