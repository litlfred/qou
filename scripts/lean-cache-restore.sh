#!/usr/bin/env bash
# Restore prebuilt Lean/Mathlib oleans from the `lake-cache/qou-<slug>`
# orphan branch (≈2 min) instead of building Mathlib from source
# (≈30+ min). The slug is DERIVED from `lean-toolchain` so this stays
# correct across toolchain bumps.
#
# Idempotent: skips if the oleans are already present. After extracting,
# resets the mathlib `origin` URL (lean_mathlib_url_fix) so a subsequent
# `lake` run does not detect a URL change and wipe the restore.
#
# Canonical recipe + gotchas:
#   docs/coordination/2026-06-08-lean-cache-architecture.md
#   .claude/skills/local/lean-environment-setup.md  ("PRESERVE THE BUILD")
#
# Usage:  scripts/lean-cache-restore.sh
# Exit:   0 = oleans present (restored or already there); non-zero = no
#         matching cache branch / empty payload.
set -uo pipefail
source "$(dirname "$0")/lib/lean-env.sh"

slug="$(lean_toolchain_slug)"
branch="lake-cache/qou-$slug"
echo "lean-cache-restore: toolchain slug=$slug  branch=$branch"

# Already restored? (count mathlib oleans; ~2900 when complete)
existing=$(find "$REPO_ROOT/.lake/packages/mathlib" -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
if [ "${existing:-0}" -ge 2000 ]; then
  echo "lean-cache-restore: $existing mathlib oleans already present — skipping."
  lean_mathlib_url_fix
  exit 0
fi

# Fetch into a PRIVATE ref, not FETCH_HEAD. `FETCH_HEAD` is global and mutable:
# a concurrent `git fetch` (a background `fetch origin main`, a parallel agent)
# repoints it mid-read, so the blobs silently resolve against the wrong commit and
# the assembled tarball is truncated — presenting as a corrupt cache
# ("gzip: not in gzip format"). Cost a session on 2026-06-22.
restore_ref="refs/lean-cache-restore"
trap 'git -C "$REPO_ROOT" update-ref -d "$restore_ref" 2>/dev/null || true' EXIT

if ! git -C "$REPO_ROOT" fetch --depth=1 origin "+$branch:$restore_ref" 2>/dev/null; then
  echo "lean-cache-restore: branch '$branch' not found on origin." >&2
  echo "  available lake-cache branches:" >&2
  git -C "$REPO_ROOT" ls-remote origin 'lake-cache/*' 2>/dev/null \
    | awk '{print "    " $2}' >&2
  exit 1
fi

# The payload is chunked into lake-oleans.tgz.part* blobs. Stream them straight
# into `tar` rather than reassembling a temp tarball first: the payload is ~1 GB,
# so a temp file both doubles peak disk (tarball + extracted tree) and leaks that
# GB if the process dies before its cleanup trap runs. Ten such orphaned
# /tmp/tmp.* tarballs (~9 GB) were found on a session container on 2026-08-07.
mapfile -t parts < <(git -C "$REPO_ROOT" ls-tree --name-only "$restore_ref" \
  | grep '^lake-oleans\.tgz\.part' | sort)
if [ "${#parts[@]}" -eq 0 ]; then
  echo "lean-cache-restore: no 'lake-oleans.tgz.part*' blobs on $branch." >&2
  exit 1
fi
echo "lean-cache-restore: streaming ${#parts[@]} part(s) into tar (no temp file)"
# PIPESTATUS is checked so a mid-stream git failure is not masked by tar's exit 0.
set -o pipefail
for p in "${parts[@]}"; do
  git -C "$REPO_ROOT" cat-file blob "$restore_ref:$p"
done | tar xz -C "$REPO_ROOT" || {
  echo "lean-cache-restore: extraction failed (exit $?) — truncated or corrupt payload." >&2
  exit 1
}
lean_mathlib_url_fix

count=$(find "$REPO_ROOT/.lake/packages/mathlib" -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
echo "lean-cache-restore: restored — $count mathlib oleans present."
echo "lean-cache-restore: verify a file with  scripts/lean-verify.sh <file.lean>"
