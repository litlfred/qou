#!/usr/bin/env bash
# Restore the prebuilt Lean **toolchain binary** from the
# `lake-cache/toolchain-<slug>` orphan branch, for sandboxes where the
# elan downloader is firewalled (`release.lean-lang.org` 403 and the
# GitHub `releases/download/` path blocked, so `elan`/`lake exe cache
# get` cannot fetch the compiler). The `git` protocol to the qou remote
# stays reachable, so a toolchain vendored onto a qou branch — split into
# git-blob-sized parts, exactly like the olean cache
# (`scripts/lean-cache-restore.sh`) — is fetchable when nothing else is.
#
# The slug is DERIVED from `lean-toolchain` so this stays correct across
# toolchain bumps. Pairs with `scripts/lean-toolchain-cache-seed.sh`
# (run once on a NON-firewalled machine that already has the toolchain,
# to populate the branch).
#
# After restoring the compiler, restore the oleans too
# (`scripts/lean-cache-restore.sh`) and verify a file with
# `scripts/lean-verify.sh <file.lean>` (lean-direct — no `lake build`).
#
# Usage:  scripts/lean-toolchain-cache-restore.sh
# Exit:   0 = toolchain present (restored or already there);
#         non-zero = no matching cache branch / empty payload.
set -uo pipefail
source "$(dirname "$0")/lib/lean-env.sh"

slug="$(lean_toolchain_slug)"                      # e.g. v4-24-0
branch="lake-cache/toolchain-$slug"
# Pinned toolchain name/version (used for logging + the version-match check).
# The extracted directory name (elan uses `leanprover--lean4---v4.24.0`) is NOT
# recomputed here — detection is by `find … -path '*/bin/lean'`, which is
# name-agnostic, so it stays correct regardless of elan's dash convention.
toolchain_name="$(cut -d: -f1 "$REPO_ROOT/lean-toolchain" | tr -d '\r')"   # leanprover/lean4
toolchain_ver="$(cut -d: -f2 "$REPO_ROOT/lean-toolchain" | tr -d '\r')"    # v4.24.0
dest_root="$HOME/.elan/toolchains"
echo "lean-toolchain-cache-restore: slug=$slug branch=$branch toolchain=$toolchain_name:$toolchain_ver"

# Already present AND matching the pinned version? Only then skip — a
# different preinstalled toolchain must NOT satisfy this (it would leave the
# wrong compiler and defeat the pin). `lean --version` prints e.g.
# "Lean (version 4.24.0, ...)"; match the numeric part of the pinned version.
vernum="${toolchain_ver#v}"                        # v4.24.0 -> 4.24.0

# First `bin/lean` under $dest_root whose `--version` matches the pinned
# $vernum. Filtering by version (rather than `find … | head -1`) is robust to
# multiple installed toolchains — it never selects the wrong compiler, so a
# valid preinstalled match is not missed and a non-matching one is not mistaken
# for success. `lean --version` prints e.g. "Lean (version 4.24.0, ...)".
first_matching_lean() {
  local bin
  find "$dest_root" -maxdepth 3 -type f -name lean -path '*/bin/lean' 2>/dev/null \
    | while read -r bin; do
        if "$bin" --version 2>/dev/null | grep -qF "version $vernum"; then
          echo "$bin"; break
        fi
      done
}

# Already present AND matching the pinned version? Only then skip — a different
# preinstalled toolchain must NOT satisfy this (it would defeat the pin).
existing="$(first_matching_lean)"
if [ -n "$existing" ]; then
  echo "lean-toolchain-cache-restore: matching lean $vernum already present at $existing — skipping."
  exit 0
fi

if ! git -C "$REPO_ROOT" fetch --depth=1 origin "$branch" 2>/dev/null; then
  echo "lean-toolchain-cache-restore: branch '$branch' not found on origin." >&2
  echo "  Seed it first (on a machine WITH the toolchain installed):" >&2
  echo "    scripts/lean-toolchain-cache-seed.sh" >&2
  echo "  available lake-cache branches:" >&2
  git -C "$REPO_ROOT" ls-remote origin 'lake-cache/*' 2>/dev/null \
    | awk '{print "    " $2}' >&2
  exit 1
fi

tgz="$(mktemp)"
trap 'rm -f "$tgz"' EXIT
# Payload is chunked into lean-toolchain.tgz.part* blobs; concatenate in
# order back into one tarball (same scheme as the olean cache).
git -C "$REPO_ROOT" ls-tree --name-only FETCH_HEAD \
  | grep '^lean-toolchain\.tgz\.part' | sort \
  | while read -r p; do git -C "$REPO_ROOT" show "FETCH_HEAD:$p"; done > "$tgz"
if [ ! -s "$tgz" ]; then
  echo "lean-toolchain-cache-restore: no 'lean-toolchain.tgz.part*' blobs on $branch." >&2
  exit 1
fi

mkdir -p "$dest_root"
# The tarball is rooted at the toolchain directory name, so it extracts
# straight into ~/.elan/toolchains/<name>/.
tar xzf "$tgz" -C "$dest_root" || {
  echo "lean-toolchain-cache-restore: tar extraction failed (exit $?)." >&2
  exit 1
}

lean_bin="$(first_matching_lean)"
if [ -z "$lean_bin" ]; then
  echo "lean-toolchain-cache-restore: extracted, but no bin/lean matching $vernum found under $dest_root." >&2
  exit 1
fi
chmod +x "$lean_bin" 2>/dev/null || true
elan_toolchain_dir="$(dirname "$(dirname "$lean_bin")")"
# The binary is now runnable directly (and via scripts/lean-verify.sh, which
# sets LEAN_PATH for lean-direct). This does NOT modify elan's default
# toolchain; if you want the `lean`/`lake` elan wrappers to resolve to it,
# register it yourself with:  elan toolchain link qou-cached "$elan_toolchain_dir"
echo "lean-toolchain-cache-restore: restored toolchain at $elan_toolchain_dir"
"$lean_bin" --version 2>/dev/null || {
  echo "lean-toolchain-cache-restore: WARNING '$lean_bin --version' failed (arch/glibc mismatch?)." >&2
  exit 1
}
echo "lean-toolchain-cache-restore: OK. Next: scripts/lean-cache-restore.sh (oleans), then scripts/lean-verify.sh <file.lean>"
