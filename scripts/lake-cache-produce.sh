#!/usr/bin/env bash
# scripts/lake-cache-produce.sh — refresh the Tier-2 lake-cache/<pkg>-<toolchain>
# orphan branch from the current .lake/ directory.
#
# Format: per-file blobs at .lake/* in the orphan branch tree, matching
# the format produced by .github/workflows/lake-cache-refresh.yml and
# the format the lake-cache-restore Action expects (`git archive
# --format=tar FETCH_HEAD -- '.lake'`). Granular: changing one .olean
# updates one git blob, not the whole tarball.
#
# Two files are excluded because they are NOT needed by `lake build`
# from a warm cache (confirmed by the 2026-06-07 strip experiment —
# `lake build QOU` ran cleanly with both removed):
#   - .lake/packages/*/.git/                 (Mathlib's cloned-repo history; large)
#   - .lake/packages/mathlib/.lake/build/bin/cache  (`lake exe cache get` binary)
# This shrinks the cache from ~2.0 GB → ~1.4 GB.
#
# Pre-requisites:
#   - Current branch should be 'main' or a fresh dev checkout
#   - .lake/ must be fully populated (run `lake build QOU` first, or
#     fetch the existing cache via `lake-cache-fetch.sh`)
#   - Push access to origin (orphan branch is force-pushed)
#
# Usage:
#   ./scripts/lake-cache-produce.sh                       # refresh canonical branch
#   ./scripts/lake-cache-produce.sh --branch lake-cache/qou-test  # push to test branch
#   ./scripts/lake-cache-produce.sh --dry-run             # don't push; show diff stats
#
# Exit codes:
#   0 = orphan branch refreshed and pushed
#   1 = pre-flight failure (missing .lake/, wrong format, etc.)
#   2 = bad invocation

set -uo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

DRY_RUN=0
BRANCH=""
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ; shift ;;
    --branch)
      if [ $# -lt 2 ] || [ -z "${2:-}" ]; then
        echo "lake-cache-produce: --branch requires a non-empty value" >&2
        exit 2
      fi
      BRANCH="$2" ; shift 2 ;;
    -h|--help)
      sed -n '2,32p' "$0" | sed 's|^# ||;s|^#||'
      exit 0
      ;;
    *) echo "Unknown flag: $1" >&2 ; exit 2 ;;
  esac
done

# Derive default branch name from lean-toolchain
if [ -z "$BRANCH" ]; then
  toolchain=$(grep -oE 'v[0-9]+\.[0-9]+\.[0-9]+' lean-toolchain | head -1)
  if [ -z "$toolchain" ]; then
    echo "lake-cache-produce: could not parse toolchain version from lean-toolchain" >&2
    exit 1
  fi
  slug=$(echo "$toolchain" | tr '.' '-')
  BRANCH="lake-cache/qou-${slug}"
fi

# Pre-flight: .lake/ must have mathlib oleans
WARMSIG="$REPO_ROOT/.lake/packages/mathlib/.lake/build/lib"
if [ ! -d "$WARMSIG" ]; then
  echo "lake-cache-produce: ERROR — $WARMSIG is missing" >&2
  echo "  Run './scripts/lake-cache-fetch.sh' first to populate .lake/," >&2
  echo "  OR build from source with 'lake build QOU'." >&2
  exit 1
fi

echo "lake-cache-produce: producing $BRANCH from current .lake/"
echo "  Source size: $(du -sh .lake/ | awk '{print $1}')"

# Use a worktree at a detached HEAD so the current checkout (and any
# in-progress edits) is untouched. We then `git checkout --orphan`
# inside the worktree to construct the parentless cache branch.
WORKDIR=$(mktemp -d -t lake-cache-produce.XXXXXX)
trap "git worktree remove --force '$WORKDIR' 2>/dev/null ; rm -rf '$WORKDIR'" EXIT INT TERM

git worktree add --detach "$WORKDIR" HEAD 2>&1 | tail -3
cd "$WORKDIR"

# Make this worktree the orphan branch. `git checkout --orphan` clears
# the index but leaves working-tree files alone — we then explicitly
# `git rm -rf --cached` and remove working-tree files so the orphan
# starts empty.
git checkout --orphan "$BRANCH" 2>&1 | tail -2
git rm -rf --cached --quiet . 2>/dev/null || true
# Remove every working-tree entry except the .git symlink-file that
# `git worktree` placed here.
find . -mindepth 1 -maxdepth 1 ! -name '.git' -exec rm -rf {} + 2>/dev/null

# Stage the .lake/ tree, minus the two stripped components.
echo "lake-cache-produce: copying .lake/ into worktree (excluding .git/ + bin/cache)"
cp -r "$REPO_ROOT/.lake" .
find .lake/packages -name '.git' -type d -prune -exec rm -rf {} + 2>/dev/null
rm -f .lake/packages/mathlib/.lake/build/bin/cache
final_size=$(du -sh .lake | awk '{print $1}')
echo "  Stripped size: $final_size"

# Stage + commit. -f is required because .lake/ may be in .gitignore.
echo "lake-cache-produce: git add -f .lake (will take ~30-60s for ~10k files)"
git add -f .lake
n_files=$(git diff --cached --name-only | wc -l)
echo "  Staged files: $n_files"

if [ "$n_files" -eq 0 ]; then
  echo "lake-cache-produce: nothing to commit (empty .lake/ after strip?)" >&2
  exit 1
fi

# Use `git -c user.name=... commit` rather than `git config user.name`
# so the author setting applies ONLY to this commit and doesn't write
# into the shared `.git/config` (which would affect the parent repo
# and all worktrees). Per the Copilot review on PR #1953.
toolchain_short=$(grep -oE 'v[0-9]+\.[0-9]+\.[0-9]+' "$REPO_ROOT/lean-toolchain" | head -1)
src_sha=$(git -C "$REPO_ROOT" rev-parse HEAD 2>/dev/null || echo unknown)
msg="reseed lean cache: per-file blobs at ${toolchain_short}

Source main commit: ${src_sha}
Stripped: .lake/packages/*/.git/, .lake/packages/mathlib/.lake/build/bin/cache
Generated by scripts/lake-cache-produce.sh on $(date -u +%Y-%m-%dT%H:%M:%SZ).
Restore: ./scripts/lake-cache-fetch.sh (handles both per-file + chunked-tgz formats)."
git -c user.name="qou-lake-cache-bot" \
    -c user.email="qou-lake-cache-bot@users.noreply.github.com" \
    commit -m "$msg" --quiet

if [ "$DRY_RUN" -eq 1 ]; then
  echo "lake-cache-produce: dry-run — not pushing $BRANCH"
  echo "  Commit: $(git rev-parse HEAD)"
  echo "  Tree files: $n_files"
  echo "  Run without --dry-run to push."
  exit 0
fi

echo "lake-cache-produce: pushing $BRANCH (force) — may take 5-15 min for ~1.4 GB upload"
git push --force origin "$BRANCH" 2>&1 | tail -5

echo "lake-cache-produce: ✓ refreshed $BRANCH"
