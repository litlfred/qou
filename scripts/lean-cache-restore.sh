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

if ! git -C "$REPO_ROOT" fetch --depth=1 origin "$branch" 2>/dev/null; then
  echo "lean-cache-restore: branch '$branch' not found on origin." >&2
  echo "  available lake-cache branches:" >&2
  git -C "$REPO_ROOT" ls-remote origin 'lake-cache/*' 2>/dev/null \
    | awk '{print "    " $2}' >&2
  exit 1
fi

tgz="$(mktemp)"
trap 'rm -f "$tgz"' EXIT
# The payload is chunked into lake-oleans.tgz.part* blobs; concatenate
# them in order back into one tarball.
git -C "$REPO_ROOT" ls-tree --name-only FETCH_HEAD \
  | grep '^lake-oleans\.tgz\.part' | sort \
  | while read -r p; do git -C "$REPO_ROOT" show "FETCH_HEAD:$p"; done > "$tgz"
if [ ! -s "$tgz" ]; then
  echo "lean-cache-restore: no 'lake-oleans.tgz.part*' blobs on $branch." >&2
  exit 1
fi
tar xzf "$tgz" -C "$REPO_ROOT"
lean_mathlib_url_fix

count=$(find "$REPO_ROOT/.lake/packages/mathlib" -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
echo "lean-cache-restore: restored — $count mathlib oleans present."
echo "lean-cache-restore: verify a file with  scripts/lean-verify.sh <file.lean>"
