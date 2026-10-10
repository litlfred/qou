#!/usr/bin/env bash
# Put qou's kept trashcan on disk at fsh-guts/.
#
# Since 2026-10-10 (owner; bean qou-6u3n, issue #7621) fsh-guts/ and the
# former _deprecated/ trees live on the branch store `cat/cat-harness/fsh-guts`,
# not on main. Readers that need them (the _path_bridge last-resort fallback,
# simulator blocks whose `html:` sits under fsh-guts/deprecated/simulators/,
# a content block citing a deprecated producer) find nothing until it is
# mounted. run-validate measured: 9 issues mounted, 18 (INVALID) unmounted.
#
# Prefers the platform's `state:mount` (folio-assistant/), which keeps the
# per-worktree marker that `state:push` needs. Falls back to a read-only
# `git archive` copy when the platform clone is absent; that copy cannot be
# pushed back, and the script says so.
set -u
ROOT=$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel) || exit 0
cd "$ROOT" || exit 0
BRANCH=cat/cat-harness/fsh-guts

if [ -d folio-assistant/cat-harness/scripts ] && command -v bun >/dev/null 2>&1; then
  bun folio-assistant/cat-harness/scripts/state-mount.ts && exit 0
  echo "mount-fsh-guts: state:mount failed; trying the read-only fallback" >&2
fi

if [ -d fsh-guts ] && [ -n "$(ls -A fsh-guts 2>/dev/null)" ]; then
  echo "mount-fsh-guts: fsh-guts/ already populated; left as is"
  exit 0
fi
if git fetch -q --depth=1 origin "$BRANCH" 2>/dev/null; then
  git archive FETCH_HEAD fsh-guts | tar -x -C "$ROOT" \
    && echo "mount-fsh-guts: READ-ONLY copy of $BRANCH at fsh-guts/ (no platform clone; edits here cannot be state:push'd)"
else
  echo "mount-fsh-guts: could not fetch $BRANCH — fsh-guts/ is NOT mounted; deprecated witnesses and parked simulators will be missing" >&2
fi
exit 0
