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

# Fetch the payload into a THROWAWAY gitdir, never into $REPO_ROOT.
#
# Why: `git fetch --depth=1` marks the *whole clone* shallow, permanently, as
# a side effect. A shallow clone reports nonsense for every ancestry query —
# `origin/main` collapses to a handful of commits, so `git rev-list --count`,
# ahead/behind, and merge-base all return confident wrong answers with no
# warning. That is not hypothetical: it silently corrupted a 41-PR triage
# sweep (bean qou-70g5), which reported every branch as "67 commits behind"
# because that was the entire history left in the clone.
#
# `--depth=1` cannot simply be dropped — `lake-cache/*` are NOT single-commit
# orphans (qou-v4-24-0 carries 18 commits, each re-seed adding a ~1.4 GB
# generation), so a full fetch would pull all of it. Fetching shallowly into a
# temp gitdir keeps the saving and leaves the real clone untouched.
scratch="$(mktemp -d)"
trap 'rm -rf "$scratch" "${tgz:-}"' EXIT

origin_url="$(git -C "$REPO_ROOT" remote get-url origin 2>/dev/null)"
if [ -z "$origin_url" ]; then
  echo "lean-cache-restore: cannot resolve 'origin' remote URL." >&2
  exit 1
fi

git -C "$scratch" init -q 2>/dev/null
git -C "$scratch" remote add origin "$origin_url" 2>/dev/null
if ! git -C "$scratch" fetch --depth=1 origin "$branch" 2>/dev/null; then
  echo "lean-cache-restore: branch '$branch' not found on origin." >&2
  echo "  available lake-cache branches:" >&2
  git -C "$REPO_ROOT" ls-remote origin 'lake-cache/*' 2>/dev/null \
    | awk '{print "    " $2}' >&2
  exit 1
fi

tgz="$(mktemp)"
# The payload is chunked into lake-oleans.tgz.part* blobs; concatenate
# them in order back into one tarball.
git -C "$scratch" ls-tree --name-only FETCH_HEAD \
  | grep '^lake-oleans\.tgz\.part' | sort \
  | while read -r p; do git -C "$scratch" show "FETCH_HEAD:$p"; done > "$tgz"
if [ ! -s "$tgz" ]; then
  echo "lean-cache-restore: no 'lake-oleans.tgz.part*' blobs on $branch." >&2
  exit 1
fi
tar xzf "$tgz" -C "$REPO_ROOT" || {
  echo "lean-cache-restore: tar extraction failed (exit $?)." >&2
  exit 1
}
lean_mathlib_url_fix

# Belt-and-braces: if the clone is shallow, say so loudly. This script no
# longer causes it, but an earlier run of the old recipe (or a shallow
# `git clone`) leaves the same landmine, and it fails silently.
if [ "$(git -C "$REPO_ROOT" rev-parse --is-shallow-repository 2>/dev/null)" = "true" ]; then
  echo "lean-cache-restore: WARNING — this clone is SHALLOW." >&2
  echo "  Ancestry queries (rev-list --count, ahead/behind, merge-base) will" >&2
  echo "  return wrong answers with no error. Fix: git fetch --unshallow origin" >&2
fi

count=$(find "$REPO_ROOT/.lake/packages/mathlib" -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
echo "lean-cache-restore: restored — $count mathlib oleans present."
echo "lean-cache-restore: verify a file with  scripts/lean-verify.sh <file.lean>"
