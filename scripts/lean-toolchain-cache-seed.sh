#!/usr/bin/env bash
# Seed the `lake-cache/toolchain-<slug>` orphan branch with the prebuilt
# Lean toolchain binary, so firewalled sandboxes can restore the compiler
# via `git` (the one protocol that stays reachable when the elan
# downloader and GitHub release-asset paths are blocked). Mirrors the
# olean-cache seeding scheme: tar the toolchain, split into git-blob-sized
# parts, push to an orphan branch.
#
# RUN THIS ON A NON-FIREWALLED MACHINE that already has the pinned
# toolchain installed (`elan toolchain install $(cat lean-toolchain)` or a
# prior `lake build`). It reads `~/.elan/toolchains/<name>` and pushes it;
# it does NOT need network access to lean-lang.org (only push to origin).
#
# Restore side: `scripts/lean-toolchain-cache-restore.sh`.
#
# Usage:  scripts/lean-toolchain-cache-seed.sh [--force]
# Exit:   0 on push; non-zero if the toolchain dir is missing.
set -uo pipefail
source "$(dirname "$0")/lib/lean-env.sh"

FORCE=0
[ "${1:-}" = "--force" ] && FORCE=1

slug="$(lean_toolchain_slug)"                      # v4-24-0
branch="lake-cache/toolchain-$slug"
toolchain_line="$(tr -d '\r' < "$REPO_ROOT/lean-toolchain")"   # leanprover/lean4:v4.24.0
dest_root="$HOME/.elan/toolchains"

# Find the installed toolchain dir carrying bin/lean. elan's dir-naming
# has varied ('--' vs '-'); match by "has bin/lean and dir name mentions
# the version" rather than guessing the exact string.
ver="$(printf '%s' "$toolchain_line" | cut -d: -f2)"    # v4.24.0
tdir="$(find "$dest_root" -maxdepth 1 -type d -name "*${ver//./?}*" 2>/dev/null | head -1)"
[ -z "$tdir" ] && tdir="$(find "$dest_root" -maxdepth 2 -type f -name lean -path '*/bin/lean' \
                            -printf '%h\n' 2>/dev/null | sed 's#/bin$##' | head -1)"
if [ -z "${tdir:-}" ] || [ ! -x "$tdir/bin/lean" ]; then
  echo "lean-toolchain-cache-seed: no installed toolchain for '$toolchain_line' under $dest_root." >&2
  echo "  Install it first (non-firewalled machine):  elan toolchain install $toolchain_line" >&2
  exit 1
fi
tname="$(basename "$tdir")"
echo "lean-toolchain-cache-seed: packing $tdir  ->  branch $branch"
"$tdir/bin/lean" --version || true

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
# Tar rooted at the toolchain dir NAME (so restore extracts into
# ~/.elan/toolchains/<name>/), then split into 90 MB parts (< GitHub's
# 100 MB blob hard-limit).
tar czf "$work/lean-toolchain.tgz" -C "$dest_root" "$tname"
split -b 90m -d -a 3 "$work/lean-toolchain.tgz" "$work/lean-toolchain.tgz.part"
size="$(du -h "$work/lean-toolchain.tgz" | cut -f1)"
nparts="$(ls "$work"/lean-toolchain.tgz.part* | wc -l | tr -d ' ')"
echo "lean-toolchain-cache-seed: $size in $nparts part(s)."

# Build the orphan branch payload in a temp worktree to avoid disturbing
# the working tree.
seedwt="$(mktemp -d)"
git -C "$REPO_ROOT" worktree add --detach "$seedwt" >/dev/null 2>&1 || {
  echo "lean-toolchain-cache-seed: could not create worktree." >&2; exit 1; }
trap 'git -C "$REPO_ROOT" worktree remove --force "$seedwt" 2>/dev/null; rm -rf "$work"' EXIT
(
  cd "$seedwt"
  git checkout --orphan "seed-$slug" >/dev/null 2>&1
  git rm -rf . >/dev/null 2>&1 || true
  cp "$work"/lean-toolchain.tgz.part* .
  {
    echo "# Lean toolchain cache: $toolchain_line"
    echo "toolchain: $toolchain_line"
    echo "dir_name: $tname"
    echo "parts: $nparts"
    echo "restore: scripts/lean-toolchain-cache-restore.sh"
  } > TOOLCHAIN-CACHE-README.md
  git add lean-toolchain.tgz.part* TOOLCHAIN-CACHE-README.md
  git -c user.name=lean-cache -c user.email=lean-cache@local \
    commit -q -m "seed toolchain cache $toolchain_line ($nparts parts)"
  push_args=(origin "HEAD:$branch")
  [ "$FORCE" = 1 ] && push_args=(--force-with-lease "${push_args[@]}")
  git push "${push_args[@]}"
)
echo "lean-toolchain-cache-seed: pushed $branch. Sandboxes can now run scripts/lean-toolchain-cache-restore.sh"
