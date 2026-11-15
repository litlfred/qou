#!/usr/bin/env bash
# Put qou's branch-kept state on disk: fsh-guts/ (the kept trashcan) and,
# since the beans cutover (issue #7642), beans/ (the work-plan).
#
# Both live on branch stores, not on main:
#   cat/cat-harness/fsh-guts  -> fsh-guts/   (owner 2026-10-10; bean qou-6u3n, issue #7621)
#   cat/cat-harness/beans     -> beans/      (owner 2026-10-10, re-confirmed 2026-11-15; issue #7642)
#
# Order of preference:
#   1. The platform's `state:mount` (folio-assistant/). It keeps the per-worktree
#      marker that `state:push` needs, so only a mount made this way can be
#      written back. If the platform clone is absent, this script installs it
#      first with scripts/setup-folio-assistant.sh (measured 2026-11-15: about
#      1-2 min, 1.8 GB at pin 82b389982).
#   2. fsh-guts only: a READ-ONLY `git archive` copy when (1) fails.
#      beans/ gets NO read-only fallback (owner, 2026-11-15: install the
#      platform at start instead). If the beans mount fails, this script says
#      so loudly, because an empty work-plan and an unreachable one look
#      identical to an agent.
set -u
ROOT=$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel) || exit 0
cd "$ROOT" || exit 0

if command -v bun >/dev/null 2>&1; then
  if [ ! -d folio-assistant/cat-harness-tools/scripts ]; then
    echo "mount-fsh-guts: platform clone absent; running setup-folio-assistant.sh"
    timeout 900 ./scripts/setup-folio-assistant.sh >"${TMPDIR:-/tmp}/qou-setup-folio-assistant.log" 2>&1 \
      || echo "mount-fsh-guts: platform setup failed (log: ${TMPDIR:-/tmp}/qou-setup-folio-assistant.log)" >&2
  fi
  if [ -d folio-assistant/cat-harness-tools/scripts ]; then
    bun folio-assistant/cat-harness-tools/scripts/state-mount.ts
    # state:mount exits non-zero for graphs it does not mount (lake-cache is
    # handed to its own Tool), so judge by what is on disk, not by the status.
  fi
fi

readonly_copy() { # <branch> <path>
  local branch=$1 path=$2
  if [ -d "$path" ] && [ -n "$(ls -A "$path" 2>/dev/null)" ]; then
    echo "mount-fsh-guts: $path/ already populated; left as is"
    return 0
  fi
  if git fetch -q --depth=1 origin "$branch" 2>/dev/null; then
    git archive FETCH_HEAD "$path" | tar -x -C "$ROOT" \
      && echo "mount-fsh-guts: READ-ONLY copy of $branch at $path/ (no platform mount; edits here cannot be state:push'd)"
  else
    echo "mount-fsh-guts: could not fetch $branch — $path/ is NOT mounted" >&2
  fi
}

readonly_copy cat/cat-harness/fsh-guts fsh-guts
if [ -z "$(ls -A beans/defs 2>/dev/null)" ]; then
  echo "mount-fsh-guts: beans/ is NOT mounted (platform setup or state:mount failed)." >&2
  echo "mount-fsh-guts: the bean work-plan is UNAVAILABLE in this session; an empty \`beans list\` must not be believed." >&2
  echo "mount-fsh-guts: fix: ./scripts/setup-folio-assistant.sh && bun folio-assistant/cat-harness-tools/scripts/state-mount.ts" >&2
fi
exit 0
