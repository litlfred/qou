#!/usr/bin/env bash
# Give every restored Lake package a git checkout at its manifest revision, so a
# later `lake` run does not delete the restored olean cache (bean qou-r13s).
#
# WHY.  `lean-cache-restore.sh` unpacks `.lake/packages/<pkg>/.lake/build/...`
# from a tarball.  The tarball carries oleans and traces but no `.git` and no
# `.lean` sources.  Lake decides whether a git dependency is usable by asking the
# package directory's git remote.  With no `.git` it prints
#
#     info: mathlib: URL has changed; deleting '.../.lake/packages/mathlib' and cloning again
#
# and deletes the directory, restored oleans included, before it builds anything.
# Measured 2026-11-21 on a copy of a fresh restore: `lake build --no-build
# Mathlib.Algebra.Group.Defs` took the tree from 3915 oleans to 2, for all 8
# restored packages, and `--no-build` did not prevent it.  So the eviction in
# qou-r13s is caused by the missing `.git`, not by missing traces.
# `lean_mathlib_url_fix` (scripts/lib/lean-env.sh) cannot help: it returns
# early when `.git` is absent, which after a tarball restore is always.
#
# WHAT IT DOES.  For each `type: git` package in the root lake-manifest.json
# whose directory exists without `.git`: `git init`, add the manifest URL as
# `origin`, shallow-fetch the manifest `rev`, and check it out.  The checkout
# adds the sources and leaves the restored `.lake/` in place (`.lake` is
# untracked).  Packages that already have `.git` are left alone.
#
# Measured on the same copy after this repair: `lake build --no-build
# Mathlib.Analysis.Complex.Basic Mathlib.Tactic Mathlib.RepresentationTheory.Basic`
# exit 0, "All targets up-to-date (3086 jobs)", olean count unchanged.  This
# covers DEPENDENCY oleans only.  QOU's own oleans rebuilt with lean-direct have
# no matching traces, so `lake build QOU` still recompiles those (it does not
# evict Mathlib).
#
# Cost: one shallow fetch per package; mathlib is the large one (a few hundred
# MB of source).  Network: github.com only.
#
# Usage:  scripts/lake-restore-package-git.sh [--dry-run]
# Exit:   0 = every restored git package now has .git at its manifest rev;
#         1 = a fetch or checkout failed (named on stderr).
set -uo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANIFEST="$REPO_ROOT/lake-manifest.json"
PKGS="$REPO_ROOT/.lake/packages"
DRY=0; [ "${1:-}" = "--dry-run" ] && DRY=1
command -v jq >/dev/null || { echo "lake-restore-package-git: jq not found" >&2; exit 1; }
[ -f "$MANIFEST" ] || { echo "lake-restore-package-git: no $MANIFEST" >&2; exit 1; }

fail=0
while IFS=$'\t' read -r name url rev; do
  dir="$PKGS/$name"
  [ -d "$dir" ] || continue                       # not restored: Lake may clone it
  if [ -d "$dir/.git" ]; then
    have="$(git -C "$dir" rev-parse HEAD 2>/dev/null || echo none)"
    [ "$have" = "$rev" ] || echo "lake-restore-package-git: $name has .git at $have, manifest wants $rev (left alone)" >&2
    continue
  fi
  echo "lake-restore-package-git: $name: no .git -> checkout $rev from $url"
  [ "$DRY" = 1 ] && continue
  if git -C "$dir" init -q \
     && git -C "$dir" remote add origin "$url" \
     && git -C "$dir" fetch -q --depth 1 origin "$rev" \
     && git -C "$dir" -c advice.detachedHead=false checkout -q -f FETCH_HEAD; then
    [ "$(git -C "$dir" rev-parse HEAD)" = "$rev" ] || { echo "lake-restore-package-git: $name: HEAD != $rev" >&2; fail=1; }
  else
    echo "lake-restore-package-git: $name: fetch/checkout FAILED" >&2
    rm -rf "$dir/.git"                            # leave the tree as it was
    fail=1
  fi
done < <(jq -r '.packages[] | select(.type=="git") | [.name, .url, .rev] | @tsv' "$MANIFEST")
exit $fail
