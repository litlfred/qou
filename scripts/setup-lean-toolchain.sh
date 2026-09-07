#!/usr/bin/env bash
# Install the Lean toolchain pinned in lean-toolchain, working around
# `release.lean-lang.org` being unreachable from this container.
#
# In the Claude Code remote-execution container, `release.lean-lang.org`
# responds 403 "Host not in allowlist" (network policy). That breaks
# `elan toolchain install`, which depends on parsing release.lean-lang.org
# JSON. We bypass elan's downloader by:
#   1. Fetching the Lean toolchain zip directly from
#      github.com/leanprover/lean4/releases (which IS reachable).
#   2. Extracting it to /tmp/lean-<version>.
#   3. Registering it with `elan toolchain link <name> <path>`.
#   4. Setting the per-repo override.
#
# Idempotent — safe to re-run. Detects partial state (e.g. /tmp survives
# but ~/.elan settings reset) and re-links + re-overrides without
# re-downloading.
#
# Exit codes:
#   0 — toolchain is installed AND the per-repo override resolves it,
#       verified by a final `lake --version` matching the pinned VERSION
#   non-zero — verification failed; stderr identifies the failing step

set -uo pipefail

# Acquire global lock to prevent parallel downloads/extracts across agent workspaces (if flock is available)
if command -v flock >/dev/null 2>&1; then
  exec 200>"/tmp/qou-toolchain.lock"
  flock 200
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLCHAIN_FILE="$REPO_ROOT/lean-toolchain"
ELAN_HOME="${ELAN_HOME:-$HOME/.elan}"
export PATH="$ELAN_HOME/bin:$PATH"

# 0. Ensure elan is present. Fresh remote-exec containers often ship
#    WITHOUT elan, in which case the old code skipped EVERYTHING below —
#    toolchain install AND the orphan-branch cache fetch (step 6) — so
#    every such session fell into the 30-60 min from-source Mathlib
#    rebuild. Since elan.lean-lang.org / release.lean-lang.org are
#    firewalled here, bootstrap elan from its GitHub release asset (the
#    same host policy that already lets us fetch the toolchain zip below).
#    `--default-toolchain none` installs elan WITHOUT touching the
#    firewalled release host; the pinned toolchain is linked in step 2.
if ! command -v elan >/dev/null 2>&1; then
  echo "setup-lean-toolchain: elan not found — bootstrapping from GitHub releases" >&2
  # Pinned for reproducibility/debuggability; override with ELAN_VERSION=vX.Y.Z.
  ELAN_VERSION="${ELAN_VERSION:-v4.2.3}"
  ELAN_URL="https://github.com/leanprover/elan/releases/download/$ELAN_VERSION/elan-x86_64-unknown-linux-gnu.tar.gz"
  # mktemp dir → unique per run (no collision with concurrent sessions or a
  # stale partial tarball from a prior failed download); removed unconditionally.
  _elan_tmp="$(mktemp -d)"
  ELAN_TGZ="$_elan_tmp/elan-init.tar.gz"
  if command -v curl >/dev/null 2>&1 \
     && curl --fail --show-error -sL --max-time 180 -o "$ELAN_TGZ" "$ELAN_URL" \
     && tar xzf "$ELAN_TGZ" -C "$_elan_tmp" 2>/dev/null \
     && [ -x "$_elan_tmp/elan-init" ]; then
    # Install elan only; the pinned toolchain is fetched from GitHub below.
    ELAN_HOME="$ELAN_HOME" "$_elan_tmp/elan-init" -y --default-toolchain none --no-modify-path >&2 2>&1 || true
    export PATH="$ELAN_HOME/bin:$PATH"
    hash -r 2>/dev/null || true
  fi
  rm -rf "$_elan_tmp"
  if ! command -v elan >/dev/null 2>&1; then
    echo "setup-lean-toolchain: elan bootstrap failed (network?) — skipping; Lean unavailable this session" >&2
    exit 0
  fi
  echo "setup-lean-toolchain: elan bootstrapped ($(elan --version 2>/dev/null || echo elan))" >&2
fi
if [ ! -f "$TOOLCHAIN_FILE" ]; then
  echo "setup-lean-toolchain: no lean-toolchain file at $TOOLCHAIN_FILE" >&2
  exit 0
fi

# Parse e.g. "leanprover/lean4:v4.24.0" → VERSION=v4.24.0
TOOLCHAIN_SPEC=$(tr -d '[:space:]' < "$TOOLCHAIN_FILE")
VERSION="${TOOLCHAIN_SPEC#leanprover/lean4:}"
if [ "$VERSION" = "$TOOLCHAIN_SPEC" ] || [ -z "$VERSION" ]; then
  echo "setup-lean-toolchain: unsupported toolchain spec '$TOOLCHAIN_SPEC'" >&2
  exit 0
fi

OS_NAME="$(uname -s)"
if [ "$OS_NAME" = "Darwin" ]; then
  LINK_NAME="$TOOLCHAIN_SPEC"
else
  LINK_NAME="lean-$VERSION"
fi
EXTRACT_DIR="/tmp/lean-$VERSION"
# elan's canonical name for the pinned spec `leanprover/lean4:vX.Y.Z`
# (`/`→`--`, `:`→`---`) — what the Lean LSP server resolves, distinct from
# the `lean-<version>` LINK_NAME this script overrides to. See step 3a.
CANONICAL_NAME="leanprover--lean4---$VERSION"
ZIP_URL="https://github.com/leanprover/lean4/releases/download/$VERSION/lean-${VERSION#v}-linux.zip"
ZIP_PATH="/tmp/lean-$VERSION-linux.zip"

# Helper: is the per-repo override already set to LINK_NAME?
# Uses awk for exact-match on path (avoids regex metachar issues with
# paths containing '.', '+', '[', etc).
override_ok() {
  (cd "$REPO_ROOT" && elan override list 2>/dev/null \
    | awk -v r="$REPO_ROOT" -v n="$LINK_NAME" '
        BEGIN { found=0 }
        { sub(/[[:space:]]+/, " "); split($0, a, " ");
          if (a[1] == r && a[2] == n) found=1 }
        END { exit (found ? 0 : 1) }')
}

# Helper: does lake resolve to the pinned version inside REPO_ROOT?
lake_ok() {
  local v
  v=$(cd "$REPO_ROOT" && lake --version 2>/dev/null | grep -oE 'Lean version [0-9.]+' | head -1)
  [ "$v" = "Lean version ${VERSION#v}" ]
}

# Helper: the canonical-name entry the LSP resolves is present AND, if a
# symlink, points at THIS toolchain (`$EXTRACT_DIR`). A stale canonical
# link to a different directory would make the LSP resolve a different
# toolchain than the repo override (mismatched oleans — hard to debug), so
# it must NOT satisfy the short-circuit; step 3a repairs it. macOS uses the
# native toolchain, so no symlink is needed.
canonical_ok() {
  [ "$OS_NAME" = "Darwin" ] && return 0
  local link="$ELAN_HOME/toolchains/$CANONICAL_NAME"
  [ -e "$link" ] || return 1
  # Symlink: target must match EXTRACT_DIR. A real directory (not created by
  # this script) is left untouched and accepted as-is.
  if [ -L "$link" ]; then
    [ "$(readlink "$link")" = "$EXTRACT_DIR" ]
  else
    return 0
  fi
}

# 1. Fully-ready short-circuit: linked + override + lake works, AND (on
#    Linux) the canonical-name symlink the LSP needs is present and points
#    at this toolchain (`canonical_ok`). A warm session missing OR
#    mis-targeting that link does NOT short-circuit — it falls through to
#    step 3a, which (re)creates it. macOS uses the native toolchain.
if elan toolchain list 2>/dev/null | grep -qF "$LINK_NAME" \
   && override_ok && lake_ok && canonical_ok
then
  exit 0
fi

# On macOS, if not short-circuited, set override and check.
if [ "$OS_NAME" = "Darwin" ]; then
  echo "setup-lean-toolchain: macOS detected. Setting override to $TOOLCHAIN_SPEC..." >&2
  (cd "$REPO_ROOT" && elan override set "$TOOLCHAIN_SPEC" 2>/dev/null) || true
  if lake_ok; then
    echo "setup-lean-toolchain: native macOS toolchain $TOOLCHAIN_SPEC is ready" >&2
    exit 0
  else
    echo "setup-lean-toolchain: ERROR — native toolchain not working or not installed. Please run: elan toolchain install $TOOLCHAIN_SPEC" >&2
    exit 1
  fi
fi

# 2. Ensure the extracted toolchain exists on disk. Download if missing.
if [ ! -d "$EXTRACT_DIR/bin" ]; then
  # Disk preflight.  Staging needs ~5.0 GB (697 MB zip + 4.3 GB extract).
  # Without this the download proceeds until the filesystem is full, and a full
  # filesystem is not a degraded session -- it is a dead one: the agent harness
  # cannot write a child process's stdout, so EVERY command fails, including the
  # rm that would fix it.  Measured on this repo 2026-09-06, three times in one
  # session, twice reaching <100 KB free.  Skipping leaves Lean unavailable,
  # which is recoverable; filling the disk is not.
  _free_kb=$(df -k /tmp 2>/dev/null | awk 'NR==2 {print $4}')
  if [ -n "${_free_kb:-}" ] && [ "$_free_kb" -lt $((6*1024*1024)) ]; then
    echo "setup-lean-toolchain: only $((_free_kb/1024)) MB free; staging needs ~6 GB." >&2
    echo "setup-lean-toolchain: SKIPPING toolchain staging to keep the container usable." >&2
    echo "setup-lean-toolchain: free space, then re-run this script to get Lean." >&2
    exit 0
  fi
  if [ ! -f "$ZIP_PATH" ]; then
    echo "setup-lean-toolchain: downloading $ZIP_URL (~730 MB) ..." >&2
    # --fail: error out on non-2xx instead of downloading an HTML error
    # page. --show-error: surface curl errors. -L: follow redirects.
    if ! curl --fail --show-error -sL -o "$ZIP_PATH" "$ZIP_URL"; then
      echo "setup-lean-toolchain: download failed" >&2
      rm -f "$ZIP_PATH"
      exit 1
    fi
  fi
  if ! command -v unzip >/dev/null 2>&1; then
    echo "setup-lean-toolchain: unzip not installed" >&2
    exit 1
  fi
  # Sanity-check the zip before extracting (catches partial downloads
  # and HTML-disguised-as-zip).
  if ! unzip -t -q "$ZIP_PATH" >/dev/null 2>&1; then
    echo "setup-lean-toolchain: $ZIP_PATH is not a valid zip (corrupted? wrong URL?)" >&2
    rm -f "$ZIP_PATH"
    exit 1
  fi
  echo "setup-lean-toolchain: extracting to $EXTRACT_DIR ..." >&2
  rm -rf "$EXTRACT_DIR.tmp"
  mkdir -p "$EXTRACT_DIR.tmp"
  (cd "$EXTRACT_DIR.tmp" && unzip -q "$ZIP_PATH")
  # zip contains a top-level dir like lean-4.24.0-linux/
  inner=$(find "$EXTRACT_DIR.tmp" -mindepth 1 -maxdepth 1 -type d | head -1)
  if [ -z "$inner" ]; then
    echo "setup-lean-toolchain: unexpected zip layout" >&2
    rm -rf "$EXTRACT_DIR.tmp"
    exit 1
  fi
  mv "$inner" "$EXTRACT_DIR"
  rm -rf "$EXTRACT_DIR.tmp"
  # The zip is 697 MB and is pure redundancy once the tree is extracted: it is
  # kept only to skip a re-download if the extract is later removed, and /tmp
  # does not survive a new container anyway, so that saving is worth far less
  # than the space.  Measured 2026-09-06: zip 697 MB + extract 4.3 GB = 5.0 GB
  # staged per session start, in a ~38 GB quota holding a 33 GB repo.
  rm -f "$ZIP_PATH"
fi

# 3. Register with elan (idempotent; harmless if already linked).
elan toolchain link "$LINK_NAME" "$EXTRACT_DIR" 2>/dev/null || true

# 3a. Also register under elan's CANONICAL toolchain name for the pinned
#     spec (`leanprover/lean4:vX.Y.Z` → `leanprover--lean4---vX.Y.Z`), so
#     tools that resolve the *spec* directly rather than the per-repo
#     override's `LINK_NAME` find the toolchain locally. The Lean LSP
#     server (lean-lsp-mcp) does exactly this: it reads `lean-toolchain`
#     and looks up the canonical name, NOT the `lean-<version>` link this
#     script overrides to. Without this symlink the LSP fails to
#     initialize — it tries to fetch the toolchain from the firewalled
#     `release.lean-lang.org` and times out — even though `lake`/`lean`
#     work fine via the override. `elan toolchain link` cannot be used
#     (its names may not contain `/` or `:`), so we create the canonical
#     symlink directly, mirroring how `elan toolchain link` registers.
#     `ln -sfn` replaces a stale/mismatched symlink in place, so a
#     canonical link left pointing at a *different* toolchain by a prior
#     run is corrected rather than left to mis-resolve (Copilot review).
#     `canonical_ok` (above) both gates this and guards a real directory at
#     that path (accepted as-is, never clobbered).
if [ "$OS_NAME" != "Darwin" ] \
   && [ "$CANONICAL_NAME" != "$LINK_NAME" ] \
   && [ -d "$ELAN_HOME/toolchains" ] \
   && ! canonical_ok; then
  if ln -sfn "$EXTRACT_DIR" "$ELAN_HOME/toolchains/$CANONICAL_NAME" 2>/dev/null; then
    echo "setup-lean-toolchain: linked canonical name $CANONICAL_NAME -> $EXTRACT_DIR (LSP toolchain resolution)" >&2
  else
    echo "setup-lean-toolchain: could not link canonical name $CANONICAL_NAME (best-effort; LSP may not start)" >&2
  fi
fi

# 4. Set repo-level override (always — survives container restarts where
#    the elan settings file resets but /tmp survives).
(cd "$REPO_ROOT" && elan override set "$LINK_NAME" 2>/dev/null) || true

# 5. Verify the chain actually resolved. If not, emit a warning + exit
#    non-zero so CI/automation can detect the broken state.
if ! lake_ok; then
  echo "setup-lean-toolchain: WARNING — lake does not resolve to ${VERSION#v} after install" >&2
  echo "  toolchain list: $(elan toolchain list 2>/dev/null | tr '\n' ' ')" >&2
  echo "  override list:  $(elan override list 2>/dev/null | tr '\n' ' ')" >&2
  exit 1
fi

echo "setup-lean-toolchain: ready ($LINK_NAME, override set on $REPO_ROOT)" >&2

# 6. Auto-fetch pre-built oleans from the GitHub Release cache (or
#    legacy orphan-branch fallback) if .lake/build/lib/ isn't already
#    populated. This is what makes `lake build` complete in seconds
#    rather than the 1-3 hour from-source rebuild that would otherwise
#    be needed when the Mathlib oleans cache host 403s in restricted
#    containers. Best-effort: if neither the release nor the branch
#    is available, fall through to whatever lake build can do on its own.
FETCH_SCRIPT="$REPO_ROOT/scripts/lean-cache-restore.sh"
if [ -x "$FETCH_SCRIPT" ] && [ ! -d "$REPO_ROOT/.lake/packages/mathlib/.lake/build/lib" ]; then
  echo "setup-lean-toolchain: .lake/ not warm — fetching olean cache (release → orphan-branch fallback)" >&2
  "$FETCH_SCRIPT" >&2 || echo "setup-lean-toolchain: cache fetch failed (best-effort) — lake build will go from source" >&2
fi

exit 0
