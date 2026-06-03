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

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLCHAIN_FILE="$REPO_ROOT/lean-toolchain"
ELAN_HOME="${ELAN_HOME:-$HOME/.elan}"
export PATH="$ELAN_HOME/bin:$PATH"

# 0. Skip if no elan, or no lean-toolchain file.
if ! command -v elan >/dev/null 2>&1; then
  echo "setup-lean-toolchain: elan not found, skipping" >&2
  exit 0
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
LINK_NAME="lean-$VERSION"
EXTRACT_DIR="/tmp/lean-$VERSION"
ZIP_URL="https://github.com/leanprover/lean4/releases/download/$VERSION/lean-${VERSION#v}-linux.zip"
ZIP_PATH="/tmp/lean-$VERSION-linux.zip"

# Helper: is the per-repo override already set to LINK_NAME?
override_ok() {
  (cd "$REPO_ROOT" && elan override list 2>/dev/null \
    | grep -qE "^$REPO_ROOT[[:space:]]+$LINK_NAME$")
}

# 1. Fully-ready short-circuit: linked + override + lake works.
if elan toolchain list 2>/dev/null | grep -qE "^$LINK_NAME( |$)" \
   && override_ok \
   && (cd "$REPO_ROOT" && lake --version 2>/dev/null | grep -q "Lean version ${VERSION#v}")
then
  exit 0
fi

# 2. Ensure the extracted toolchain exists on disk. Download if missing.
if [ ! -d "$EXTRACT_DIR/bin" ]; then
  if [ ! -f "$ZIP_PATH" ]; then
    echo "setup-lean-toolchain: downloading $ZIP_URL (~730 MB) ..." >&2
    if ! curl -sL -o "$ZIP_PATH" "$ZIP_URL"; then
      echo "setup-lean-toolchain: download failed" >&2
      rm -f "$ZIP_PATH"
      exit 1
    fi
  fi
  if ! command -v unzip >/dev/null 2>&1; then
    echo "setup-lean-toolchain: unzip not installed" >&2
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
fi

# 3. Register with elan (idempotent; harmless if already linked).
elan toolchain link "$LINK_NAME" "$EXTRACT_DIR" 2>/dev/null || true

# 4. Set repo-level override (always — survives container restarts where
#    the elan settings file resets but /tmp survives).
(cd "$REPO_ROOT" && elan override set "$LINK_NAME" 2>/dev/null) || true

echo "setup-lean-toolchain: ready ($LINK_NAME, override set on $REPO_ROOT)" >&2
exit 0
