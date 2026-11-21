#!/usr/bin/env bash
# Wire up the Folio Assistant platform for a local qou checkout.
#
# Context: qou is CONTENT ONLY. The platform it consumes (content
# pipeline, schemas, LaTeX rendering, viewer, computations) lives in a
# SEPARATE repo, litlfred/folio-assistant. qou's content `.ts` files and
# the `folio/schema/*.ts` shims import the platform through the in-repo
# path `folio-assistant/` (e.g. `folio/schema/builders.ts` re-exports the
# builders from `../../folio-assistant/cat-harness/schemas/builders`), and the
# package.json scripts run `../folio-assistant/cat-harness-tools/pipeline/*.ts`.
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

# A 40-hex SHA pin (the default, from .folio-assistant-pin) cannot be cloned with
# --branch, and the fallback full clone of the monorepo did not finish within ten
# minutes through a proxied sandbox (2026-10-04). Fetch exactly the pinned commit
# instead: one shallow fetch, then the unified checkout below finds it locally.
if [ ! -d "$CLONE_DIR/.git" ] && printf '%s' "$REF" | grep -Eq '^[0-9a-f]{40}$'; then
  info "pin is a SHA — fetching only $REF into $CLONE_DIR"
  mkdir -p "$CLONE_DIR" && git -C "$CLONE_DIR" init --quiet \
    && git -C "$CLONE_DIR" remote add origin "$REPO_URL" \
    && git_retry git -C "$CLONE_DIR" fetch --quiet --depth 1 origin "$REF" \
    && git -C "$CLONE_DIR" checkout --quiet FETCH_HEAD \
    || die "shallow fetch of $REF failed (check network / repo access)"
  SHALLOW_PIN_FETCHED=1
fi

if [ ! -d "$CLONE_DIR/.git" ]; then
  info "cloning $REPO_URL -> $CLONE_DIR (ref: $REF)"
  # --branch accepts a branch or tag but NOT a SHA; on a SHA ref this first
  # clone fails and we fall back to a default-branch clone — the unified
  # checkout below then moves to $REF.
  git_retry git clone --branch "$REF" "$REPO_URL" "$CLONE_DIR" \
    || git_retry git clone "$REPO_URL" "$CLONE_DIR" \
    || die "clone failed after retries (check network / repo access)"
elif [ "${SHALLOW_PIN_FETCHED:-0}" = 1 ]; then
  : # just fetched exactly the pinned commit above; a full `fetch --tags` would undo the point
elif printf '%s' "$REF" | grep -Eq '^[0-9a-f]{40}$' && ! git -C "$CLONE_DIR" rev-parse --verify --quiet "$REF^{commit}" >/dev/null 2>&1; then
  info "platform clone exists at $CLONE_DIR — fetching only the pinned commit $REF"
  git_retry git -C "$CLONE_DIR" fetch --quiet --depth 1 origin "$REF" \
    || info "fetch failed (offline?) — using existing clone as-is"
elif printf '%s' "$REF" | grep -Eq '^[0-9a-f]{40}$'; then
  # The pinned commit is already in the clone, and a SHA cannot move, so there
  # is nothing to fetch. This branch used to fall through to the `fetch --tags
  # origin` below, which in a cloud session is a disaster: the session's own
  # shallow checkout of litlfred/folio-assistant sits at ../folio-assistant
  # (the default CLONE_DIR) and usually already contains the pin, and a
  # refspec-wide fetch from a shallow clone pulls the FULL history of all
  # ~4,200 branches. Measured 2026-11-17: 10.7 million objects, the pack past
  # 4.9 GB and still growing after 6 minutes, so the agent's timeout killed
  # setup before the layer mount and the symlink were made, and no
  # folio-assistant/ link was left behind.
  info "platform clone exists at $CLONE_DIR and already has $REF — no fetch needed"
else
  # A branch or tag name. Fetch only that ref, shallow if the clone is shallow,
  # never every branch: see the SHA case above for what a full fetch costs.
  info "platform clone exists at $CLONE_DIR — fetching $REF"
  _depth=""
  [ "$(git -C "$CLONE_DIR" rev-parse --is-shallow-repository 2>/dev/null)" = true ] && _depth="--depth 1"
  # shellcheck disable=SC2086
  git_retry git -C "$CLONE_DIR" fetch --quiet $_depth origin \
      "+refs/heads/$REF:refs/remotes/origin/$REF" 2>/dev/null \
    || git_retry git -C "$CLONE_DIR" fetch --quiet $_depth origin "refs/tags/$REF:refs/tags/$REF" \
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

# Platform main (2026-10) carries bootstrap/ and bootstrap-tools/ as git
# SUBMODULES; without them every pipeline import fails with "Cannot find module
# ../../bootstrap-tools/schemas/graph". Initialise them at the recorded commits.
if [ -f "$CLONE_DIR/.gitmodules" ]; then
  git_retry git -C "$CLONE_DIR" submodule update --init --depth 1 --quiet \
    || warn "submodule init failed — imports into bootstrap/ and bootstrap-tools/ will not resolve"
fi

# Platform main (from 2026-10-09) carries NO layer in-tree: cat-harness,
# cat-harness-tools, folio-assistant-core, folio-assistant-sci, bootstrap, ...
# are remote mounts recorded in `index.lock.json`, each pinned to a commit and
# verified against a tree digest. A clone at such a pin has none of them until
# they are laid down, and every `folio-assistant/cat-harness/...` import fails.
# The platform's own entry point does it with nothing but bun + git; it is
# idempotent (an intact mount is reported `current`).
if [ -f "$CLONE_DIR/index.lock.json" ] && [ -f "$CLONE_DIR/.github/mount-from-lock.sh" ]; then
  info "mounting platform layers from index.lock.json"
  (cd "$CLONE_DIR" && bash .github/mount-from-lock.sh --root .) >&2 \
    || warn "mount-from-lock failed — platform layers (cat-harness, folio-assistant-sci, …) may be absent"
fi

# absolute, normalized path to the clone
CLONE_ABS="$(cd "$CLONE_DIR" && pwd)" || die "cannot resolve $CLONE_DIR"

# --- which layout is this clone? -----------------------------------------
# folio-assistant split its own tree on 2026-09-20: the platform (schemas/,
# content/pipeline/, src/, scripts/, adapters/) moved from the clone ROOT down
# into `cat-harness/`. The clone root keeps package.json and node_modules, so
# `bun install` and the dep check below still belong there — only the code
# moved.
#
# This is DETECTED rather than assumed, and it has to be, because the two
# layouts coexist right now: `.folio-assistant-pin` still names a pre-split
# SHA, so a fresh run of this script checks out a clone with no `cat-harness/`
# at all. Hardcoding either answer breaks the other, and it breaks it the
# quiet way — every `folio-assistant/...` import resolves to nothing and the
# first error names bun's global cache rather than this link (the 2026-09-13
# `qou-wdh9` shape).
#
# Probe for a FILE the platform must have, not for the directory: a stray
# empty `cat-harness/` would otherwise answer "split" and point the link at
# nothing.
#
# The LINK points at the clone ROOT in both layouts (bean qou-msp2). Every qou
# importer writes the split path in full — `folio-assistant/cat-harness/<x>` —
# since the 2026-09-26 pin bump re-pointed them. Until 2026-09-29 this script
# linked one level deeper, to `<clone>/cat-harness`, so each of those imports
# resolved to `cat-harness/cat-harness/<x>` and failed: `run-validate.ts` could
# not start after a stock setup. The layout is still DETECTED, because the
# bibliography bridge below applies to a pre-split clone only, but it is kept
# in PLATFORM_SPLIT rather than inferred from where the link points.
# The schemas code moved to cat-harness-tools/schemas/ on 2026-10-30 (bean 8lcl);
# either location means the split layout.
if [ -f "$CLONE_ABS/cat-harness-tools/schemas/types.ts" ] || [ -f "$CLONE_ABS/cat-harness/schemas/types.ts" ]; then
  PLATFORM_ABS="$CLONE_ABS"
  PLATFORM_SPLIT=1
  PLATFORM_LAYOUT="split (code under cat-harness/)"
elif [ -f "$CLONE_ABS/schemas/types.ts" ]; then
  PLATFORM_ABS="$CLONE_ABS"
  PLATFORM_SPLIT=0
  PLATFORM_LAYOUT="pre-split (code at clone root)"
  warn "pre-split platform clone: qou imports folio-assistant/cat-harness/<x>, which a pre-split clone does not have"
else
  # Neither answers. Do NOT guess: linking to a root that holds no schemas/
  # produces a link that exists and resolves nothing, which is the state this
  # script is for detecting. Say so and stop.
  die "clone at $CLONE_ABS holds schemas/types.ts at neither the root nor cat-harness/ — not a folio-assistant checkout, or a failed clone"
fi
info "platform layout: $PLATFORM_LAYOUT -> $PLATFORM_ABS"

# --- create the in-repo symlink: <root>/folio-assistant -> clone ----------
LINK="$ROOT/folio-assistant"

# Safety: never clobber tracked files. Nothing under folio-assistant/ is
# tracked post-migration; bail loudly if that ever changes.
if [ -n "$(git -C "$ROOT" ls-files folio-assistant/ 2>/dev/null)" ]; then
  die "folio-assistant/ has git-tracked files — refusing to replace with a symlink"
fi

# Prefer a relative symlink target (portable across machines); fall back
# to the absolute path if realpath lacks --relative-to.
if TARGET="$(realpath --relative-to="$ROOT" "$PLATFORM_ABS" 2>/dev/null)"; then :; else
  TARGET="$PLATFORM_ABS"
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
    win_link="$(cygpath -w "$LINK")"; win_target="$(cygpath -w "$PLATFORM_ABS")"
    cmd //c mklink //j "$win_link" "$win_target" >/dev/null \
      || die "could not create directory junction (use WSL, or run 'mklink /j' manually)"
    info "created Windows directory junction: folio-assistant -> $PLATFORM_ABS"
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
# ONLY for a pre-split clone. Both consumers were fixed upstream and the
# bridges are not merely unnecessary against a split clone — they are WRONG
# there, because `mkdir -p "$CLONE_ABS/folio/schema"` would mint directories
# at a clone root that no longer holds any of the platform's code, and the
# consumer looking for them has stopped looking.
#
# What changed, checked in the platform tree on 2026-09-20 rather than assumed:
#
#   qa-checkers-extended.ts  reads `join(FOLIO_DIR, "schema", "references.ts")`,
#                            and FOLIO_DIR is `folioDir(findContentRepoRoot())`.
#                            For qou that resolves through `qou.json` to
#                            `<qou>/content` — the source of truth itself. The
#                            bridge existed because the path used to be
#                            import-relative and landed in the platform clone.
#
#   export-bibtex.ts         no longer imports `../../schemas/references` at
#                            all. It imports `./references-registry-di`, a DI
#                            point the folio fills by calling
#                            `configureReferenceRegistry` — which qou's
#                            `scripts/run-validate.ts` does, under `--strict`
#                            only and for reasons recorded there (bean
#                            `qou-cite`). So the bridge is inert rather than
#                            merely unnecessary: the file it creates is at a
#                            path nothing imports. Note that qou has no caller
#                            of export-bibtex today, so `references.bib` is not
#                            regenerated from here by any route; that is a
#                            pre-existing gap this script never closed, and
#                            leaving the bridge in place would not close it.
#
# So this whole block is dead the moment `.folio-assistant-pin` moves past the
# split. It is kept, guarded, because the pin has NOT moved yet: until it does,
# a fresh clone is pre-split and needs these links exactly as before.
if [ "$PLATFORM_SPLIT" = 0 ]; then
  # qa-checkers-extended.ts (pre-split) resolved references.ts relative to the
  # PLATFORM clone (CONTENT_DIR = <clone>/content), but the bibliography source
  # of truth lives in THIS repo at folio/schema/references.ts. Without this
  # bridge every \cite{} fails bib-cite-resolves with "does not resolve in
  # references.ts" (the 2026-06-21 233-block false-fail batch).
  if [ ! -e "$CLONE_ABS/folio/schema/references.ts" ]; then
    mkdir -p "$CLONE_ABS/folio/schema"
    ln -s "$ROOT/folio/schema/references.ts" \
      "$CLONE_ABS/folio/schema/references.ts" \
      && info "bridged folio/schema/references.ts into pre-split platform clone" \
      || info "could not bridge references.ts — bib-cite-resolves will false-fail"
  fi

  # The pre-split platform imported the bibliography by TWO different paths,
  # and bridging only the one above left the other broken:
  #
  #   qa-checkers-extended.ts  -> <clone>/folio/schema/references  (above)
  #   export-bibtex.ts         -> <clone>/schemas/references         (here)
  #
  # Without this second link, regenerating references.bib dies with
  # "Cannot find module '../../schemas/references'", the .bib silently
  # stays stale, and every \cite{} added since the last successful export
  # renders as an undefined citation in the PDF. Measured 2026-08-16: 16
  # keys present in references.ts were missing from references.bib, for
  # 23 "Citation ... undefined" warnings in the full build.
  if [ ! -e "$CLONE_ABS/schemas/references.ts" ]; then
    mkdir -p "$CLONE_ABS/schemas"
    ln -s "$ROOT/folio/schema/references.ts" \
      "$CLONE_ABS/schemas/references.ts" \
      && info "bridged schemas/references.ts into pre-split platform clone" \
      || info "could not bridge schemas/references.ts — export-bibtex will fail"
  fi
else
  info "split platform: no bibliography bridge needed (FOLIO_DIR and the DI registry resolve it)"
fi

# --- install the platform's own deps, and VERIFY it ----------------------
#
# Still best-effort (a failure here does not abort setup), but no longer SILENT.
#
# Measured 2026-09-13 (bean qou-wdh9): this block ran, `bun` was on PATH,
# FOLIO_SKIP_INSTALL was unset, and the clone still had no node_modules three
# hours later. Why was unrecoverable -- the `|| info` swallowed the reason and
# nothing was logged. What the agent saw instead, from `run-validate`, was
#
#     error: Cannot find module 'unist-util-visit-parents/do-not-use-color'
#       from '/root/.bun/install/cache/unist-util-visit-parents@6.0.2@@@1/lib/index.js'
#
# which names bun's GLOBAL CACHE and neither this script nor the clone. The
# remark/unified family lives in the PLATFORM's package.json and nowhere in qou,
# so with no node_modules bun resolves out of that cache, where it does not
# honour the `./do-not-use-color` conditional subpath export. The agent
# reasonably read it as a broken gate and ran `bun install` in qou/ -- which
# cannot work, and measured no change.
#
# So two things are added: the install output is KEPT, and the outcome is
# CHECKED against the artifact that actually matters (node_modules), not against
# bun's exit code. Checking the exit code alone would not have caught this if
# the clone was materialised by some path that never reached this block.
if [ "${FOLIO_SKIP_INSTALL:-0}" != "1" ] && [ -f "$CLONE_ABS/package.json" ]; then
  if command -v bun >/dev/null 2>&1; then
    _install_log="${TMPDIR:-/tmp}/folio-assistant-bun-install.log"
    info "installing platform deps (bun install in $CLONE_ABS; log: $_install_log)"
    (cd "$CLONE_ABS" && bun install) >"$_install_log" 2>&1 \
      || warn "bun install exited non-zero — see $_install_log"
  else
    warn "bun not found — platform deps NOT installed. Install bun, then run:"
    warn "    cd $CLONE_ABS && bun install"
  fi
fi

# Verify the artifact, not the exit code. This runs even when the install was
# skipped, so a clone materialised by any other route is still checked.
if [ -f "$CLONE_ABS/package.json" ] && [ ! -d "$CLONE_ABS/node_modules" ]; then
  warn "=============================================================="
  warn "PLATFORM DEPS ARE MISSING: $CLONE_ABS/node_modules does not exist."
  warn ""
  warn "Every checker runs from the platform clone, so the content gate"
  warn "will fail before validating anything, with an error naming bun's"
  warn "global cache rather than this clone. It looks like a broken gate."
  warn "It is not. Running 'bun install' in the qou repo will NOT fix it —"
  warn "the missing packages are declared in the PLATFORM's package.json."
  warn ""
  warn "Fix:  cd $CLONE_ABS && bun install"
  warn "=============================================================="
fi

cat >&2 <<EOF
setup-folio-assistant: done.
  platform clone : $CLONE_ABS
  in-repo link   : $LINK -> $TARGET

Next, from the REPO ROOT:
  bun run scripts/run-validate.ts folio/quantum-observable-universe

(\`bun run validate\` no longer exists — the package.json alias was dropped in
the folio-assistant migration; run-validate.ts is its standalone replacement.)
EOF
