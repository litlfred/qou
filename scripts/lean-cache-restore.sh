#!/usr/bin/env bash
# Restore prebuilt Lean/Mathlib oleans from a GitHub Release asset
# (tar.zst, ~1.4 GB) instead of building Mathlib from source (~30+ min).
#
# The release is tagged `lean-cache/v<version>` (e.g. `lean-cache/v4.24.0`)
# and contains a single asset `lake-oleans.tar.zst`.
#
# Fallback: if the release is not found (or `gh`/`zstd` are unavailable),
# falls back to the legacy orphan-branch restore (chunked tgz blobs on
# `lake-cache/qou-<slug>`).
#
# Idempotent: skips if oleans are already present. After extracting,
# resets the mathlib `origin` URL (lean_mathlib_url_fix) so a subsequent
# `lake` run does not detect a URL change and wipe the restore.
#
# Usage:  scripts/lean-cache-restore.sh
# Exit:   0 = oleans present (restored or already there); non-zero = no
#         matching cache / empty payload.
set -uo pipefail
source "$(dirname "$0")/lib/lean-env.sh"

slug="$(lean_toolchain_slug)"
version="$(cut -d: -f2 "$REPO_ROOT/lean-toolchain" | tr -d '\r')"
release_tag="lean-cache/$version"
echo "lean-cache-restore: toolchain=$version  slug=$slug  release=$release_tag"

# Already restored? (count mathlib oleans; ~2900+ when complete)
existing=$(find "$REPO_ROOT/.lake/packages/mathlib" -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
if [ "${existing:-0}" -ge 2000 ]; then
  echo "lean-cache-restore: $existing mathlib oleans already present — skipping."
  lean_mathlib_url_fix
  exit 0
fi

# ── PRIMARY: GitHub Release asset (tar.zst) ────────────────────────────
restore_from_release() {
  if ! has gh; then
    echo "lean-cache-restore: gh CLI not found — skipping release path." >&2
    return 1
  fi
  if ! has zstd; then
    echo "lean-cache-restore: zstd not found — skipping release path." >&2
    return 1
  fi

  local asset="/tmp/lake-oleans.tar.zst"
  trap 'rm -f "$asset"' RETURN

  echo "lean-cache-restore: downloading release asset from $release_tag ..."
  if ! gh release download "$release_tag" \
       --repo litlfred/qou \
       --pattern 'lake-oleans.tar.zst' \
       --output "$asset" \
       --clobber 2>/dev/null; then
    echo "lean-cache-restore: release '$release_tag' not found or download failed." >&2
    return 1
  fi

  echo "lean-cache-restore: extracting $(du -h "$asset" | cut -f1) ..."
  zstd -d "$asset" --stdout | tar xf - -C "$REPO_ROOT" || {
    echo "lean-cache-restore: tar.zst extraction failed." >&2
    return 1
  }
  return 0
}

# ── FALLBACK: legacy orphan-branch chunked tgz ────────────────────────
restore_from_orphan_branch() {
  local branch="lake-cache/qou-$slug"
  echo "lean-cache-restore: trying legacy orphan branch $branch ..."

  if ! git -C "$REPO_ROOT" fetch --depth=1 origin "$branch" 2>/dev/null; then
    echo "lean-cache-restore: branch '$branch' not found on origin." >&2
    return 1
  fi

  local tgz
  tgz="$(mktemp)"
  trap 'rm -f "$tgz"' RETURN

  git -C "$REPO_ROOT" ls-tree --name-only FETCH_HEAD \
    | grep '^lake-oleans\.tgz\.part' | sort \
    | while read -r p; do git -C "$REPO_ROOT" show "FETCH_HEAD:$p"; done > "$tgz"
  if [ ! -s "$tgz" ]; then
    echo "lean-cache-restore: no 'lake-oleans.tgz.part*' blobs on $branch." >&2
    return 1
  fi
  tar xzf "$tgz" -C "$REPO_ROOT" || {
    echo "lean-cache-restore: tar extraction failed." >&2
    return 1
  }
  return 0
}

# ── Try release first, then orphan branch ──────────────────────────────
if restore_from_release || restore_from_orphan_branch; then
  lean_mathlib_url_fix
  count=$(find "$REPO_ROOT/.lake/packages/mathlib" -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
  echo "lean-cache-restore: restored — $count mathlib oleans present."
  echo "lean-cache-restore: verify a file with  scripts/lean-verify.sh <file.lean>"
  exit 0
else
  echo "lean-cache-restore: no cache source available (release + orphan branch both failed)." >&2
  exit 1
fi
