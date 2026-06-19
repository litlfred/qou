#!/usr/bin/env bash
# install-beans.sh — install the `beans` flat-file issue tracker CLI.
#
# `beans` (https://github.com/hmans/beans) is the Go binary that backs the
# bean-based session work-plan system used by this repo's agent skills
# (see .claude/skills/local/todo-manager.md, session-intent.md, pending-show.md).
# Issues are stored as markdown files under .beans/.
#
# Cloud sandboxes / fresh containers do NOT ship the binary, so this script
# (re)installs it on demand. It is idempotent — safe to re-run.
#
#   NOTE: the npm package named "beans" is an UNRELATED abandoned tool.
#         Do NOT `npm install beans`.
set -euo pipefail

BIN_DIR="${BEANS_BIN_DIR:-$HOME/.local/bin}"
BEANS_PKG="github.com/hmans/beans@latest"

if command -v beans >/dev/null 2>&1; then
  echo "beans already installed: $(command -v beans)"
  beans --version 2>/dev/null || true
  exit 0
fi

if ! command -v go >/dev/null 2>&1; then
  echo "ERROR: Go toolchain not found on PATH; cannot install beans." >&2
  echo "       Install Go (it ships in most sandboxes), or place an existing" >&2
  echo "       'beans' binary on PATH, then re-run." >&2
  exit 1
fi

mkdir -p "$BIN_DIR"
# `go install` requires GOBIN to be an ABSOLUTE path; resolve it so a relative
# BEANS_BIN_DIR (e.g. "bin") does not make the install fail.
BIN_DIR="$(cd "$BIN_DIR" && pwd)"
echo "Installing $BEANS_PKG into $BIN_DIR ..."
GOBIN="$BIN_DIR" go install "$BEANS_PKG"

# PATH hint (don't fail if not yet exported).
case ":${PATH:-}:" in
  *":$BIN_DIR:"*) ;;
  *) echo "NOTE: add $BIN_DIR to PATH:  export PATH=\"$BIN_DIR:\$PATH\"" ;;
esac

if command -v beans >/dev/null 2>&1; then
  echo "beans installed: $(command -v beans)"
  beans --version 2>/dev/null || true
else
  echo "beans installed to $BIN_DIR/beans (not yet on PATH)"
fi

# Quick smoke test when run from the repo root with a .beans/ dir present.
# Fall back to the freshly-installed binary if BIN_DIR is not on PATH yet.
if [ -d .beans ]; then
  echo "--- beans check ---"
  if command -v beans >/dev/null 2>&1; then
    beans check || true
  elif [ -x "$BIN_DIR/beans" ]; then
    "$BIN_DIR/beans" check || true
  fi
fi
