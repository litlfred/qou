---
# qou-70g5
title: 'Lean cache restore leaves the clone SHALLOW: --depth=1 silently corrupts every ahead/behind measurement'
status: completed
type: task
priority: normal
created_at: 2026-08-09T02:29:25Z
updated_at: 2026-08-09T10:15:44Z
---


Found 2026-08-09 by hitting it (bean `qou-x6as`, the stalled-PR takeover).
Reported on PR #4409, which rewrites one of the two affected scripts.

## The defect

```bash
git -C "$REPO_ROOT" fetch --depth=1 origin "$branch"   # lean-cache-restore.sh:33
```

`--depth=1` marks the **whole working clone** shallow, permanently, as a side
effect of fetching a cache blob. After the documented restore,
`git rev-parse --is-shallow-repository` returns `true` and `origin/main` holds
**67 commits**.

**Why it matters: it fails quietly and produces confident wrong numbers.**
Every ahead/behind measurement across 41 open PRs came back "67 behind,
clean". Caught only because the uniformity was implausible. Recovery is
`git fetch --unshallow origin`.

## Affected sites

| file | line |
|---|---|
| `scripts/lean-cache-restore.sh` | 33 |
| `scripts/lean-toolchain-cache-restore.sh` | 66 |
| `AGENTS.md` (documented recipe) | 2634 |
| `.claude/skills/local/lean-environment-setup.md` | 8 occurrences |
| PR #4409 | keeps it in the orphan-branch fallback |

## The obvious fix is WRONG — checked

Dropping `--depth=1` on the theory that `lake-cache/*` are single-commit
orphans does not work: `lake-cache/qou-v4-24-0` has **18 commits** and its
head has a parent. Each re-seed adds a generation carrying ~1.4 GB of blobs,
so a full fetch is expensive. `--depth=1` is doing real work.

## The fix that works — shallow-fetch in a throwaway gitdir

```bash
tmp=$(mktemp -d)
git -C "$tmp" init -q
git -C "$tmp" remote add origin "$(git -C "$REPO_ROOT" remote get-url origin)"
git -C "$tmp" fetch --depth=1 origin "$branch"
# reassemble + extract into $REPO_ROOT from $tmp, then rm -rf "$tmp"
```

The real clone is never marked. `lean-environment-setup.md:787` already
sketches this shape. Belt-and-braces: capture
`git rev-parse --is-shallow-repository` before the fetch and warn loudly if
the script turned a full clone shallow.

## Related, found in the same pass

The release asset's `browser_download_url` **404s** —
`https://github.com/litlfred/qou/releases/download/lean-cache/v4.24.0/lake-oleans.tar.zst`
— because the tag name contains a `/`. `gh release download` handles it, so
#4409 is unaffected, but a `curl`-based restore cannot use the documented URL.

## FIXED 2026-08-09 (PR #4834)

Both restore scripts now shallow-fetch into a **throwaway gitdir**, so the
working clone is never marked:

- `scripts/lean-cache-restore.sh`
- `scripts/lean-toolchain-cache-restore.sh`

Plus a **belt-and-braces warning** in `lean-cache-restore.sh`: if the clone is
shallow on exit (from an earlier run of the old recipe, or a shallow
`git clone`), it says so loudly and names the recovery.

Docs updated so the copy-paste recipes stop spreading it:
- `AGENTS.md` Step-0 recipe — now uses a scratch gitdir, with the warning above it.
- `.claude/skills/local/lean-environment-setup.md` §"PRESERVE THE BUILD" —
  warning banner stating that every hand-rolled recipe below it predates the
  fix and must have the scratch-gitdir shape applied.

**Verified, not assumed:**

```
main clone shallow BEFORE : false      origin/main commits: 24438
scratch clone shallow     : true       <- shallow, as intended
main clone shallow AFTER  : false      origin/main commits: 24438  <- unchanged
```

`bash -n` clean on both scripts; `lean-cache-restore.sh` re-run end-to-end on
a populated tree (takes the idempotent skip path, 6990 oleans).

**Not done:** #4409 rewrites `lean-cache-restore.sh` wholesale for the
GitHub-Release migration and keeps the old `--depth=1` in its fallback. That
PR will need this fix re-applied when it rebases — flagged in its thread.
