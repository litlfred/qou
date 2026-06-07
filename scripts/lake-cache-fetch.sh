#!/usr/bin/env bash
# scripts/lake-cache-fetch.sh — agent-side Tier-2 cache fetch
#
# Fetches the pre-built `.lake/` artifacts from the populated orphan
# branch `lake-cache/qou-v<toolchain-slug>` and extracts them into the
# repo root. The CI-side equivalent lives at
# `.github/actions/lake-cache-restore/action.yml` (Tier 2 step); this
# script is the local-agent equivalent for sessions in ephemeral
# containers where `lake build` from source would take 1-3 hours and
# `lake exe cache get` 403s on the Mathlib oleans CDN.
#
# Storage format on the orphan branch (as of 2026-06-04 reseed):
# the `.lake/` tree is bundled as a gzipped tarball split into
# `lake-oleans.tgz.part00`..`partNN` chunks of ≤ 100 MB each (under
# GitHub's per-blob limit). This script fetches the branch shallowly,
# concatenates the parts, untars into the repo root, then prunes.
#
# Usage:
#   ./scripts/lake-cache-fetch.sh           # default: qou package, toolchain auto-detected
#   ./scripts/lake-cache-fetch.sh --force   # re-extract even if .lake/build/lib/ exists
#   ./scripts/lake-cache-fetch.sh --branch lake-cache/qou-v4-24-0   # explicit branch
#
# Exit codes:
#   0 = cache restored OR already warm
#   1 = orphan branch not found, fetch failed, or extraction failed
#   2 = bad invocation

set -uo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Parse flags.
FORCE=0
BRANCH=""
while [ $# -gt 0 ]; do
  case "$1" in
    --force) FORCE=1 ; shift ;;
    --branch) BRANCH="$2" ; shift 2 ;;
    -h|--help)
      sed -n '2,30p' "$0" | sed 's|^# ||;s|^#||'
      exit 0
      ;;
    *) echo "Unknown flag: $1" >&2 ; exit 2 ;;
  esac
done

# Auto-derive branch name from lean-toolchain if not provided.
if [ -z "$BRANCH" ]; then
  if [ ! -f lean-toolchain ]; then
    echo "lake-cache-fetch: no lean-toolchain file at repo root" >&2
    exit 1
  fi
  toolchain=$(grep -oE 'v[0-9]+\.[0-9]+\.[0-9]+' lean-toolchain | head -1)
  if [ -z "$toolchain" ]; then
    echo "lake-cache-fetch: could not parse toolchain version from lean-toolchain" >&2
    exit 1
  fi
  slug=$(echo "$toolchain" | tr '.' '-')
  BRANCH="lake-cache/qou-${slug}"
fi

# Warm-cache short-circuit unless --force.
if [ "$FORCE" -eq 0 ] && [ -d "$REPO_ROOT/.lake/build/lib" ]; then
  count=$(find "$REPO_ROOT/.lake/build/lib" -maxdepth 1 -mindepth 1 2>/dev/null | wc -l)
  if [ "$count" -gt 0 ]; then
    echo "lake-cache-fetch: .lake/build/lib/ already populated ($count entries); use --force to re-extract"
    exit 0
  fi
fi

echo "lake-cache-fetch: fetching orphan branch '$BRANCH' from origin"
# Shallow-fetch the orphan branch (no history). Tolerate fetch failure.
if ! git fetch --depth=1 origin "$BRANCH" 2>&1 | tail -5; then
  echo "lake-cache-fetch: ERROR — orphan branch '$BRANCH' does not exist on origin" >&2
  echo "  Hint: refresh the cache via the lake-cache-refresh.yml workflow_dispatch," >&2
  echo "  or set --branch <name> if your toolchain differs from the populated branch." >&2
  exit 1
fi

# Discover parts. The branch tip has one tree; list all blobs whose
# path matches lake-oleans.tgz.part*. Stream each blob into a temp
# scratch dir.
TMP=$(mktemp -d -t lake-cache-fetch.XXXXXX)
trap "rm -rf '$TMP'" EXIT INT TERM

parts=$(git ls-tree --name-only FETCH_HEAD 2>/dev/null \
        | grep -E '^lake-oleans\.tgz\.part[0-9]+$' \
        | sort)

if [ -z "$parts" ]; then
  echo "lake-cache-fetch: ERROR — branch $BRANCH has no lake-oleans.tgz.part* blobs" >&2
  echo "  Branch tree:" >&2
  git ls-tree --name-only FETCH_HEAD 2>&1 | head -10 | sed 's/^/    /' >&2
  exit 1
fi

n_parts=$(echo "$parts" | wc -l)
echo "lake-cache-fetch: found $n_parts chunks; extracting blobs to $TMP"

# Extract each part blob to the temp dir. `git show <ref>:<path>`
# streams the blob content to stdout.
for p in $parts; do
  if ! git show "FETCH_HEAD:$p" > "$TMP/$p" 2>/dev/null; then
    echo "lake-cache-fetch: ERROR — failed to extract blob $p" >&2
    exit 1
  fi
done

# Concatenate parts into one tarball and verify.
echo "lake-cache-fetch: assembling tarball + extracting into $REPO_ROOT"
cat "$TMP"/lake-oleans.tgz.part* > "$TMP/lake-oleans.tgz"
tar_size=$(stat -c '%s' "$TMP/lake-oleans.tgz" 2>/dev/null || stat -f '%z' "$TMP/lake-oleans.tgz")
echo "  assembled tarball: $((tar_size / 1024 / 1024)) MB"

# Extract into the repo root. tar -C handles the atomic write; we
# don't need a temp-dir-then-rename because tar refuses to overwrite
# unrelated files (writes into .lake/ only).
if ! tar -xzf "$TMP/lake-oleans.tgz" -C "$REPO_ROOT" 2>&1 | tail -5; then
  echo "lake-cache-fetch: ERROR — tar extraction failed" >&2
  exit 1
fi

# Verify the extraction populated .lake/build/lib/.
if [ ! -d "$REPO_ROOT/.lake/build/lib" ]; then
  echo "lake-cache-fetch: ERROR — extraction did not produce .lake/build/lib/" >&2
  echo "  Tarball top-level:" >&2
  tar -tzf "$TMP/lake-oleans.tgz" | head -10 | sed 's/^/    /' >&2
  exit 1
fi

lib_count=$(find "$REPO_ROOT/.lake/build/lib" -maxdepth 1 -mindepth 1 -type d 2>/dev/null | wc -l)
lake_size=$(du -sh "$REPO_ROOT/.lake" 2>/dev/null | awk '{print $1}')
echo "lake-cache-fetch: ✓ restored .lake/ from $BRANCH"
echo "  .lake/ size:         $lake_size"
echo "  .lake/build/lib/ has $lib_count top-level directories"
echo ""
echo "Next: 'lake build QOU' should now complete in seconds rather than hours."
