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
# elan's on-disk directory name for `leanprover/lean4:v4.24.0`:
toolchain_name="$(cut -d: -f1 "$REPO_ROOT/lean-toolchain" | tr -d '\r')"   # leanprover/lean4
toolchain_ver="$(cut -d: -f2 "$REPO_ROOT/lean-toolchain" | tr -d '\r')"    # v4.24.0
elan_dir_name="$(printf '%s:%s' "$toolchain_name" "$toolchain_ver" | tr '/' '-' | tr ':' '-')"
# -> leanprover-lean4-v4.24.0  (elan uses this convention; both `--` and
#    single `-` variants exist historically, so we probe for either)
dest_root="$HOME/.elan/toolchains"
echo "lean-toolchain-cache-restore: slug=$slug branch=$branch toolchain=$toolchain_name:$toolchain_ver"

# Already present? (any toolchain dir carrying a runnable `bin/lean`.)
existing="$(find "$dest_root" -maxdepth 2 -type f -name lean -path '*/bin/lean' 2>/dev/null | head -1)"
if [ -n "${existing:-}" ]; then
  echo "lean-toolchain-cache-restore: lean binary already present at $existing — skipping."
  "$existing" --version 2>/dev/null || true
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

lean_bin="$(find "$dest_root" -maxdepth 2 -type f -name lean -path '*/bin/lean' 2>/dev/null | head -1)"
if [ -z "${lean_bin:-}" ]; then
  echo "lean-toolchain-cache-restore: extracted, but no bin/lean found under $dest_root." >&2
  exit 1
fi
chmod +x "$lean_bin" 2>/dev/null || true
# Point elan's default at this toolchain if elan is present (so the
# `lean`/`lake` wrappers resolve); harmless if elan is absent — use the
# binary directly / via scripts/lean-verify.sh which sets LEAN_PATH.
elan_toolchain_dir="$(dirname "$(dirname "$lean_bin")")"
echo "lean-toolchain-cache-restore: restored toolchain at $elan_toolchain_dir"
"$lean_bin" --version 2>/dev/null || {
  echo "lean-toolchain-cache-restore: WARNING '$lean_bin --version' failed (arch/glibc mismatch?)." >&2
  exit 1
}
echo "lean-toolchain-cache-restore: OK. Next: scripts/lean-cache-restore.sh (oleans), then scripts/lean-verify.sh <file.lean>"
