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
source "$(dirname "$0")/lib/lake-cache-family.sh"

slug="$(lean_toolchain_slug)"
branch="$(lake_cache_read_branch "qou-$slug")"
echo "lean-cache-restore: toolchain slug=$slug  branch=$branch"

# Paper oleans: QOU's own library tree under the DECLARED lake root.  Counting
# mathlib alone (the only check here until 2026-10-10) cannot see the paper half
# of a restore, and the paper half is exactly what the content/ -> folio/ rename
# broke: a restore made before the --transform below lands mathlib correctly at
# the workspace root and every paper olean under content/<paper>/lean/.lake,
# where nothing reads it.  The script then reported "N mathlib oleans present",
# exited 0, and on every later run SKIPPED, because mathlib was present -- so the
# stranded tree was never repaired and an agent saw an "unbuilt" QOU library.
# Measured 2026-10-10 in a container restored that way: 3480 mathlib oleans at
# the root, 0 QOU oleans under folio/, 2734 paper oleans under content/.
qou_oleans() {
  find "$REPO_ROOT/folio/quantum-observable-universe/lean/.lake/build/lib/lean/QOU" \
    -name '*.olean' 2>/dev/null | wc -l | tr -d ' '
}

# relocate_legacy_paper_trees: move a pre-rename restore into place.  Moves a
# whole content/<paper>/lean/.lake only when folio/<paper>/lean has NO .lake/build
# of its own, so a real build is never overwritten; prints what it moved.
relocate_legacy_paper_trees() {
  local src paper dst
  for src in "$REPO_ROOT"/content/*/lean/.lake; do
    [ -d "$src/build" ] || continue
    paper="$(basename "$(dirname "$(dirname "$src")")")"
    dst="$REPO_ROOT/folio/$paper/lean"
    if [ ! -d "$dst" ]; then
      echo "lean-cache-restore: $src has no folio/$paper/lean to move into — left." >&2
      continue
    fi
    if [ -e "$dst/.lake/build" ]; then
      echo "lean-cache-restore: folio/$paper/lean/.lake/build exists — legacy $src left in place." >&2
      continue
    fi
    mkdir -p "$dst/.lake"
    mv "$src/build" "$dst/.lake/build" \
      && echo "lean-cache-restore: moved legacy content/$paper/lean/.lake/build -> folio/$paper/lean/.lake/build"
  done
  return 0
}

# apply_addons: lay the two plain-tar addon branches over the base seed (owner,
# 2026-11-24: "migrate local lean to cache repos.. use existing infra").  The
# base branch is a Lake build of some past main; the addons are what keeps a
# fresh session current without a 2 h lean-direct rebuild:
#   1. lean-restore-gap-oleans.sh      Mathlib modules the base seed lacks
#                                      (fills only; never replaces a base olean)
#   2. lean-restore-refresh-oleans.sh  every QOU/UGB/Fred2005 olean rebuilt
#                                      lean-direct from a later main, each with a
#                                      .srcsha stamp, so lean-direct-cone.sh
#                                      rebuilds only what changed since
# Both are idempotent (a marker under .lake/ records the commit applied), so
# calling this on every run costs two ls-remote calls.  Best-effort: a failed
# addon leaves the base seed, which still works, only older.  Opt out with
# LEAN_CACHE_NO_ADDONS=1.  Like the addons themselves this is NOT a Lake
# restore: verify lean-direct, never `lake build` afterwards.
apply_addons() {
  [ "${LEAN_CACHE_NO_ADDONS:-0}" = 1 ] && return 0
  "$(dirname "$0")/lean-restore-gap-oleans.sh" \
    || echo "lean-cache-restore: gap addon not applied (best-effort)." >&2
  "$(dirname "$0")/lean-restore-refresh-oleans.sh" \
    || echo "lean-cache-restore: refresh addon not applied (best-effort); the base seed is older than main." >&2
  return 0
}

# Already restored?  BOTH halves: mathlib (~3480 when complete) AND the paper
# library.  A mathlib-only restore is repaired from a legacy tree if one exists,
# otherwise re-extracted.
existing=$(find "$REPO_ROOT/.lake/packages/mathlib" -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
if [ "${existing:-0}" -ge 2000 ]; then
  [ "$(qou_oleans)" -eq 0 ] && relocate_legacy_paper_trees
  q=$(qou_oleans)
  if [ "$q" -gt 0 ]; then
    echo "lean-cache-restore: $existing mathlib + $q QOU oleans already present — skipping."
    lean_mathlib_url_fix
    "$(dirname "$0")/lake-restore-package-git.sh" || echo "lean-cache-restore: package git checkout incomplete; do not run lake on this tree (qou-r13s)." >&2
    apply_addons
    exit 0
  fi
  echo "lean-cache-restore: $existing mathlib oleans present but 0 QOU oleans under folio/ — re-extracting."
fi

if ! git -C "$REPO_ROOT" fetch --depth=1 origin "$branch" 2>/dev/null; then
  echo "lean-cache-restore: branch '$branch' not found on origin." >&2
  echo "  available lake-cache branches:" >&2
  lake_cache_ls_remote 2>/dev/null \
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
# The seeded tarball stores PAPER paths as `content/<paper>/lean/...` (measured
# 2026-10-10: 13670 `content/` members, 0 `folio/`), because it was seeded before
# the `content/` -> `folio/` tree rename (#7485).  A plain extract therefore puts
# every paper olean in a directory nothing reads -- LEAN_PATH is built from
# `folio/*/lean/...`.  Transform on the way out; a no-op once the branch is
# re-seeded from a `folio/` tree.
if tar --version 2>/dev/null | grep -q 'GNU tar'; then
  tar xzf "$tgz" -C "$REPO_ROOT" --transform 's,^content/,folio/,' || {
    echo "lean-cache-restore: tar extraction failed (exit $?)." >&2
    exit 1
  }
else
  tar xzf "$tgz" -s ',^content/,folio/,' -C "$REPO_ROOT" || {
    echo "lean-cache-restore: tar extraction failed (exit $?)." >&2
    exit 1
  }
fi
# The base seed just overwrote whatever an addon had laid down, so forget that
# the addons were applied; apply_addons below re-lays them.
rm -f "$REPO_ROOT/.lake/lean-gap-addon.sha" "$REPO_ROOT/.lake/lean-refresh-addon.sha"
lean_mathlib_url_fix
# The tarball has no .git in .lake/packages/*, and Lake deletes a git package
# directory whose remote it cannot read, restored oleans and all (bean
# qou-r13s, measured 3915 -> 2).  Give each package a checkout at its manifest
# rev.  Non-fatal: lean-direct needs only the oleans, and works without it.
"$(dirname "$0")/lake-restore-package-git.sh" \
  || echo "lean-cache-restore: package git checkout incomplete; do not run lake on this tree (qou-r13s)." >&2

count=$(find "$REPO_ROOT/.lake/packages/mathlib" -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
q=$(qou_oleans)
echo "lean-cache-restore: restored — $count mathlib + $q QOU oleans present."
# Fail loudly on an empty paper half: exit 0 with no QOU oleans is the silent
# failure this check replaces.
if [ "$q" -eq 0 ]; then
  echo "lean-cache-restore: 0 QOU oleans under folio/quantum-observable-universe/lean/.lake/build — the paper half of $branch did not land where Lean reads it." >&2
  exit 1
fi
apply_addons
echo "lean-cache-restore: verify a file with  scripts/lean-verify.sh <file.lean>"
