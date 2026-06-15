#!/usr/bin/env bash
# Wire up the Folio Assistant platform for a local qou checkout.
#
# Context: qou is CONTENT ONLY. The platform it consumes (content
# pipeline, schemas, LaTeX rendering, viewer, computations) lives in a
# SEPARATE repo, litlfred/folio-assistant. qou's content `.ts` files and
# the `content/schema/*.ts` shims import the platform through the in-repo
# path `folio-assistant/` (e.g. `content/schema/types.ts` does
# `export * from "../../folio-assistant/schemas/types"`), and the
# package.json scripts run `../folio-assistant/content/pipeline/*.ts`.
# Both resolve to `<repo-root>/folio-assistant/`.
#
# This script makes `<repo-root>/folio-assistant/` resolve by:
#   1. cloning (or updating) litlfred/folio-assistant as a SIBLING dir
#      (default `../folio-assistant`, kept OUT of qou's git history), and
#   2. creating an in-repo symlink `<repo-root>/folio-assistant` -> that
#      clone, so every import path resolves to the real platform tree.
#
# After running this, `cd content && bun run validate` (and build:docs,
# build:content, export-json, test, lint) work against the local platform.
#
# Idempotent — safe to re-run. Re-running fetches the latest platform ref
# and repairs a stale/missing symlink without clobbering local edits in
# the clone.
#
# Configuration (env vars):
#   FOLIO_ASSISTANT_REPO  git URL of the platform repo
#                         (default https://github.com/litlfred/folio-assistant.git)
#   FOLIO_ASSISTANT_REF   branch/tag/sha to check out (default main)
#   FOLIO_ASSISTANT_DIR   where to clone it (default ../folio-assistant,
#                         relative to the qou repo root; absolute also OK)
#   FOLIO_SKIP_INSTALL    set to 1 to skip `bun install` in the clone
#
# NOTE on internal layout: the import paths this script makes resolvable
# assume the platform repo exposes `schemas/` (top-level) and
# `content/pipeline/` — the same assumptions already encoded in qou's
# content shims and package.json. If the folio-assistant repo lays those
# out differently, fix the subpaths in those consumers; this script only
# wires the `folio-assistant/` -> platform-root link.
#
# Exit codes: 0 on success; non-zero on a hard failure (clone failed,
# would clobber tracked files, cannot create the symlink).

set -uo pipefail

REPO_URL="${FOLIO_ASSISTANT_REPO:-https://github.com/litlfred/folio-assistant.git}"
REF="${FOLIO_ASSISTANT_REF:-main}"

die() { echo "setup-folio-assistant: ERROR: $*" >&2; exit 1; }
info() { echo "setup-folio-assistant: $*" >&2; }

# --- locate the qou repo root --------------------------------------------
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" \
  || die "not inside a git checkout (run this from the qou repo)"
cd "$ROOT" || die "cannot cd to repo root $ROOT"

# --- resolve the clone location (sibling by default) ---------------------
CLONE_DIR="${FOLIO_ASSISTANT_DIR:-$ROOT/../folio-assistant}"
case "$CLONE_DIR" in
  /*) : ;;                       # absolute — use as-is
  *)  CLONE_DIR="$ROOT/$CLONE_DIR" ;;  # relative — anchor to repo root
esac

# retry a network git op up to 4 times with exponential backoff (2/4/8/16s)
git_retry() {
  local delay=2 attempt
  for attempt in 1 2 3 4 5; do
    if "$@"; then return 0; fi
    [ "$attempt" -eq 5 ] && return 1
    info "git op failed (attempt $attempt); retrying in ${delay}s..."
    sleep "$delay"; delay=$((delay * 2))
  done
}

# --- clone or update the platform repo -----------------------------------
if [ -d "$CLONE_DIR/.git" ]; then
  info "platform clone exists at $CLONE_DIR — fetching $REF"
  git_retry git -C "$CLONE_DIR" fetch --tags origin \
    || info "fetch failed (offline?) — using existing clone as-is"
  # Only move to $REF if it resolves; never clobber uncommitted local work.
  if git -C "$CLONE_DIR" rev-parse --verify --quiet "$REF^{commit}" >/dev/null; then
    if git -C "$CLONE_DIR" diff --quiet && git -C "$CLONE_DIR" diff --cached --quiet; then
      git -C "$CLONE_DIR" checkout --quiet "$REF" 2>/dev/null || true
      git -C "$CLONE_DIR" merge --ff-only --quiet "origin/$REF" 2>/dev/null || true
    else
      info "clone has local changes — leaving its checkout untouched"
    fi
  fi
elif [ -e "$CLONE_DIR" ]; then
  die "$CLONE_DIR exists but is not a git clone — move it aside or set FOLIO_ASSISTANT_DIR"
else
  info "cloning $REPO_URL -> $CLONE_DIR (ref: $REF)"
  git_retry git clone --branch "$REF" "$REPO_URL" "$CLONE_DIR" \
    || git_retry git clone "$REPO_URL" "$CLONE_DIR" \
    || die "clone failed after retries (check network / repo access)"
fi
[ -d "$CLONE_DIR" ] || die "clone directory $CLONE_DIR not present after setup"

# absolute, normalized path to the clone
CLONE_ABS="$(cd "$CLONE_DIR" && pwd)" || die "cannot resolve $CLONE_DIR"

# --- create the in-repo symlink: <root>/folio-assistant -> clone ----------
LINK="$ROOT/folio-assistant"

# Safety: never clobber tracked files. Nothing under folio-assistant/ is
# tracked post-migration; bail loudly if that ever changes.
if [ -n "$(git -C "$ROOT" ls-files folio-assistant/ 2>/dev/null)" ]; then
  die "folio-assistant/ has git-tracked files — refusing to replace with a symlink"
fi

# Prefer a relative symlink target (portable across machines); fall back
# to the absolute path if realpath lacks --relative-to.
if TARGET="$(realpath --relative-to="$ROOT" "$CLONE_ABS" 2>/dev/null)"; then :; else
  TARGET="$CLONE_ABS"
fi

if [ -L "$LINK" ]; then
  cur="$(readlink "$LINK" 2>/dev/null || true)"
  if [ "$cur" = "$TARGET" ]; then
    info "symlink already correct: folio-assistant -> $TARGET"
  else
    rm -f "$LINK" && ln -s "$TARGET" "$LINK" || die "could not refresh symlink $LINK"
    info "repaired symlink: folio-assistant -> $TARGET"
  fi
elif [ -e "$LINK" ]; then
  # Untracked husk dir/file (e.g. leftover bun.lock + node_modules). Move
  # aside rather than rm (repo convention: prefer mv over rm).
  bak="$LINK.husk.$(date +%s)"
  mv "$LINK" "$bak" || die "could not move aside existing $LINK"
  info "moved leftover husk $LINK -> $bak"
  ln -s "$TARGET" "$LINK" || die "could not create symlink $LINK"
  info "created symlink: folio-assistant -> $TARGET"
else
  ln -s "$TARGET" "$LINK" || die "could not create symlink $LINK"
  info "created symlink: folio-assistant -> $TARGET"
fi

# --- best-effort: install the platform's own deps ------------------------
if [ "${FOLIO_SKIP_INSTALL:-0}" != "1" ] && [ -f "$CLONE_ABS/package.json" ]; then
  if command -v bun >/dev/null 2>&1; then
    info "installing platform deps (bun install in $CLONE_ABS)"
    (cd "$CLONE_ABS" && bun install) || info "bun install failed — run it manually in $CLONE_ABS"
  else
    info "bun not found — skip platform deps (install bun, then 'cd $CLONE_ABS && bun install')"
  fi
fi

cat >&2 <<EOF
setup-folio-assistant: done.
  platform clone : $CLONE_ABS
  in-repo link   : $LINK -> $TARGET
Next: cd content && bun install && bun run validate
EOF
