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

# --- resolve the platform ref (PINNED by default) ------------------------
# The checkers live in the platform repo, so every count this repo quotes
# ("validate: N issues", "wall-side M/1190") is a function of TWO inputs — the
# corpus and the platform — and only one of them used to be visible in `git log`.
# Defaulting to `main` meant two agents on the same corpus commit could measure
# different numbers and each be right; that happened (bean `vbase`), and cost a
# round of argument about whose baseline was wrong.
#
# So the default is now the SHA in `.folio-assistant-pin`. Moving the platform is
# a deliberate, reviewable one-line commit to that file, not a silent consequence
# of when you happened to clone. `FOLIO_ASSISTANT_REF` still overrides for
# testing against an unreleased platform.
PIN_FILE="$(dirname "$0")/../.folio-assistant-pin"
if [ -n "${FOLIO_ASSISTANT_REF:-}" ]; then
  REF="$FOLIO_ASSISTANT_REF"
elif [ -f "$PIN_FILE" ]; then
  # strip comments and blank lines; take the first remaining token
  REF="$(sed 's/#.*//' "$PIN_FILE" | tr -d '[:space:]' | head -c 64)"
  [ -n "$REF" ] || REF="main"
else
  REF="main"
fi

die() { echo "setup-folio-assistant: ERROR: $*" >&2; exit 1; }
info() { echo "setup-folio-assistant: $*" >&2; }
warn() { echo "setup-folio-assistant: WARNING: $*" >&2; }

# Report when the clone's checkout is NOT at $REF. $REF may be a branch name or
# a pinned SHA (.folio-assistant-pin), so resolve origin/$REF first and fall
# back to $REF itself — comparing against "origin/<sha>" silently yields nothing.
report_off_ref() {
  _tgt="$REF"
  if git -C "$CLONE_DIR" rev-parse --verify --quiet "refs/remotes/origin/$REF" >/dev/null 2>&1; then
    _tgt="origin/$REF"
  fi
  _want="$(git -C "$CLONE_DIR" rev-parse --verify --quiet "$_tgt^{commit}" 2>/dev/null)" || return 0
  _have="$(git -C "$CLONE_DIR" rev-parse HEAD 2>/dev/null)" || return 0
  [ "$_want" = "$_have" ] && return 0
  _behind="$(git -C "$CLONE_DIR" rev-list --count "HEAD..$_want" 2>/dev/null || echo '?')"
  warn "platform clone is NOT at $_tgt ($_behind commit(s) behind); it is at $(git -C "$CLONE_DIR" rev-parse --short HEAD)"
  warn "  every pipeline run below uses that code, not the pinned code."
  warn "  usually the clone is dirty because qa-sweep rewrites its script-sidecars; to fix:"
  warn "    git -C \"$CLONE_DIR\" checkout -- content/pipeline/script-sidecars/ && $0"
}

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
# A non-git path already sitting at the clone location is a mistake.
if [ -e "$CLONE_DIR" ] && [ ! -d "$CLONE_DIR/.git" ]; then
  die "$CLONE_DIR exists but is not a git clone — move it aside or set FOLIO_ASSISTANT_DIR"
fi

if [ ! -d "$CLONE_DIR/.git" ]; then
  info "cloning $REPO_URL -> $CLONE_DIR (ref: $REF)"
  # --branch accepts a branch or tag but NOT a SHA; on a SHA ref this first
  # clone fails and we fall back to a default-branch clone — the unified
  # checkout below then moves to $REF.
  git_retry git clone --branch "$REF" "$REPO_URL" "$CLONE_DIR" \
    || git_retry git clone "$REPO_URL" "$CLONE_DIR" \
    || die "clone failed after retries (check network / repo access)"
else
  info "platform clone exists at $CLONE_DIR — fetching $REF"
  git_retry git -C "$CLONE_DIR" fetch --tags origin \
    || info "fetch failed (offline?) — using existing clone as-is"
fi
[ -d "$CLONE_DIR/.git" ] || die "clone directory $CLONE_DIR not present after setup"

# Move to $REF in ALL cases (fresh clone or existing). Checking both the
# local ref and origin/$REF handles a SHA ref (which --branch can't clone)
# and a new remote branch not yet checked out locally. Never clobber
# uncommitted local work in the clone.
if git -C "$CLONE_DIR" rev-parse --verify --quiet "$REF^{commit}" >/dev/null 2>&1 \
   || git -C "$CLONE_DIR" rev-parse --verify --quiet "origin/$REF^{commit}" >/dev/null 2>&1; then
  if git -C "$CLONE_DIR" diff --quiet && git -C "$CLONE_DIR" diff --cached --quiet; then
    git -C "$CLONE_DIR" checkout --quiet "$REF" 2>/dev/null || true
    # Fast-forward to the remote tip only when $REF names a branch (not a SHA/tag).
    if git -C "$CLONE_DIR" show-ref --verify --quiet "refs/remotes/origin/$REF"; then
      git -C "$CLONE_DIR" merge --ff-only --quiet "origin/$REF" 2>/dev/null || true
    fi
    report_off_ref
  else
    # A dirty clone is NOT the rare case. `qa-sweep` rewrites
    # content/pipeline/script-sidecars/*.script.json (last_run_at, deps_hash) on
    # every run, so ANY pipeline use leaves the clone dirty and this branch is
    # taken from then on. Left as a bare info line, the clone silently freezes on
    # whatever commit it happened to be on while every later run keeps serving
    # that stale pipeline — the more the pipeline is used, the more permanently
    # stale it becomes.
    #
    # Measured 2026-08-23: the clone sat 236 commits behind origin/main, which
    # silently invalidated a session's QA measurements (an enumeration gap that
    # had already been fixed upstream in b48cff7 still reproduced locally, and a
    # "sweep degrades detangler verdicts" finding turned out to be an artifact of
    # the stale code). Report the distance instead of hiding it.
    info "clone has local changes — leaving its checkout untouched"
    report_off_ref
  fi
else
  info "ref '$REF' not found locally or on origin — leaving clone on its current branch"
fi

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

# Move an untracked husk (leftover bun.lock + node_modules, or a stale
# non-symlink) aside before (re)creating the link. mv, not rm (convention).
if [ -e "$LINK" ] && [ ! -L "$LINK" ]; then
  bak="$LINK.husk.$(date +%s)"
  mv "$LINK" "$bak" || die "could not move aside existing $LINK"
  info "moved leftover husk $LINK -> $bak"
fi

case "${OSTYPE:-}" in
  msys*|cygwin*|win32)
    # Native Windows Bun/Node cannot follow MSYS emulation symlinks, so use a
    # directory junction (mklink /j — no admin needed). NOTE: Linux-first repo
    # (Crostini); this branch is unverified here — Windows devs should report
    # issues or use WSL.
    [ -e "$LINK" ] && rm -rf "$LINK"
    win_link="$(cygpath -w "$LINK")"; win_target="$(cygpath -w "$CLONE_ABS")"
    cmd //c mklink //j "$win_link" "$win_target" >/dev/null \
      || die "could not create directory junction (use WSL, or run 'mklink /j' manually)"
    info "created Windows directory junction: folio-assistant -> $CLONE_ABS"
    ;;
  *)
    if [ -L "$LINK" ]; then
      cur="$(readlink "$LINK" 2>/dev/null || true)"
      if [ "$cur" = "$TARGET" ]; then
        info "symlink already correct: folio-assistant -> $TARGET"
      else
        rm -f "$LINK" && ln -s "$TARGET" "$LINK" || die "could not refresh symlink $LINK"
        info "repaired symlink: folio-assistant -> $TARGET"
      fi
    else
      ln -s "$TARGET" "$LINK" || die "could not create symlink $LINK"
      info "created symlink: folio-assistant -> $TARGET"
    fi
    ;;
esac

# --- bridge: expose the repo's bibliography to platform checkers ----------
# qa-checkers-extended.ts resolves references.ts relative to the PLATFORM
# clone (CONTENT_DIR = <clone>/content), but the bibliography source of
# truth lives in THIS repo at content/schema/references.ts. Without this
# bridge every \cite{} fails bib-cite-resolves with "does not resolve in
# references.ts" (the 2026-06-21 233-block false-fail batch).
if [ ! -e "$CLONE_ABS/content/schema/references.ts" ]; then
  mkdir -p "$CLONE_ABS/content/schema"
  ln -s "$ROOT/content/schema/references.ts" \
    "$CLONE_ABS/content/schema/references.ts" \
    && info "bridged content/schema/references.ts into platform clone" \
    || info "could not bridge references.ts — bib-cite-resolves will false-fail"
fi

# The platform imports the bibliography by TWO different paths, and
# bridging only the one above leaves the other broken:
#
#   qa-checkers-extended.ts  → <clone>/content/schema/references  (above)
#   export-bibtex.ts         → <clone>/schemas/references         (here)
#
# Without this second link, regenerating references.bib dies with
# "Cannot find module '../../schemas/references'", the .bib silently
# stays stale, and every \cite{} added since the last successful export
# renders as an undefined citation in the PDF. Measured 2026-08-16: 16
# keys present in references.ts were missing from references.bib, for
# 23 "Citation ... undefined" warnings in the full build.
if [ ! -e "$CLONE_ABS/schemas/references.ts" ]; then
  mkdir -p "$CLONE_ABS/schemas"
  ln -s "$ROOT/content/schema/references.ts" \
    "$CLONE_ABS/schemas/references.ts" \
    && info "bridged schemas/references.ts into platform clone" \
    || info "could not bridge schemas/references.ts — export-bibtex will fail"
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
