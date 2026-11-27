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
#      written back. If the platform is absent, this script installs the
#      light subset with scripts/mount-platform-lite.sh (measured 2026-11-15:
#      about 20 s, 165 MB at pin 82b389982). The full
#      scripts/setup-folio-assistant.sh (1.7 GB) is only for validate,
#      qa-sweep and rendering; run it by hand when you need those.
#   2. fsh-guts only: a READ-ONLY `git archive` copy when (1) fails.
#      beans/ gets NO read-only fallback (owner, 2026-11-15: install the
#      platform at start instead). If the beans mount fails, this script says
#      so loudly, because an empty work-plan and an unreachable one look
#      identical to an agent.
set -u
ROOT=$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel) || exit 0
cd "$ROOT" || exit 0

if command -v bun >/dev/null 2>&1; then
  # qou is a platform layer (owner ruling 2026-11-24): index.lock.json mounts the
  # platform at the repository root, and that is the route used when it is on
  # disk. The folio-assistant/ link is the compatibility path, kept for a
  # checkout that has it and no root mounts (scripts/lib/platform-root.sh).
  STATE=""
  # Replay index.lock.json at the root when its layers are not on disk, or the
  # lock moved past the replay stamp (owner, 2026-11-25). Before this, a fresh
  # session got only the light platform under folio-assistant/, on which
  # gen-block-jsonld emits the shared default @context and would rewrite every
  # qou node -- so agents generated none, and the 2026-11-25 photon PRs left 11
  # block nodes stale (fixed after the fact by #9433). Measured 2026-11-25 on a
  # cold cache: mount-from-lock 29 s + bun install 12 s, about 500 MB
  # (layers 170 MB, node_modules 330 MB). Idempotent: a current mount is a no-op.
  if [ -f index.lock.json ] && [ "${QOU_SKIP_LOCK_MOUNT:-0}" != "1" ]; then
    stamp=$(git rev-parse --git-path cat-mounted-lock 2>/dev/null)
    want=$(sha256sum index.lock.json | cut -d' ' -f1)
    if [ ! -f cat-harness-tools/package.json ] || [ ! -d node_modules ] \
       || [ "$(cat "$stamp" 2>/dev/null)" != "$want" ]; then
      echo "mount-fsh-guts: replaying index.lock.json at the root (layer mounts)"
      if timeout 600 bash .github/mount-from-lock.sh >"${TMPDIR:-/tmp}/qou-mount-from-lock.log" 2>&1 \
         && timeout 600 bun install >"${TMPDIR:-/tmp}/qou-bun-install.log" 2>&1; then
        . scripts/lib/platform-root.sh && qou_platform_shim "$ROOT"
      else
        echo "mount-fsh-guts: lock replay failed (logs: ${TMPDIR:-/tmp}/qou-mount-from-lock.log, qou-bun-install.log); falling back to the light platform. scripts/gen-block-jsonld.sh will refuse to run until the root mounts exist." >&2
      fi
    fi
  fi
  if [ -f cat-harness-tools/scripts/state-mount.ts ] && [ -d node_modules ]; then
    STATE=cat-harness-tools/scripts/state-mount.ts
    . scripts/lib/platform-root.sh && qou_platform_shim "$ROOT"
  elif [ ! -d folio-assistant/cat-harness-tools/scripts ]; then
    # Light install (about 20 s, 165 MB), not the full setup (1.7 GB, which
    # timed out or filled the disk in two sessions on 2026-11-15).
    echo "mount-fsh-guts: platform absent; running mount-platform-lite.sh"
    timeout 600 ./scripts/mount-platform-lite.sh >"${TMPDIR:-/tmp}/qou-mount-platform-lite.log" 2>&1 \
      || echo "mount-fsh-guts: light platform install failed (log: ${TMPDIR:-/tmp}/qou-mount-platform-lite.log)" >&2
  fi
  [ -z "$STATE" ] && [ -d folio-assistant/cat-harness-tools/scripts ] && STATE=folio-assistant/cat-harness-tools/scripts/state-mount.ts
  if [ -n "$STATE" ]; then
    bun "$STATE"
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
  echo "mount-fsh-guts: fix: bash .github/mount-from-lock.sh && bun install && bun cat-harness-tools/scripts/state-mount.ts (or, on the compatibility path: ./scripts/mount-platform-lite.sh && bun folio-assistant/cat-harness-tools/scripts/state-mount.ts)" >&2
fi
exit 0
