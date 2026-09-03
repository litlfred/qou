#!/usr/bin/env bash
# Auto-commit the hadron-knot-table regeneration journal as it advances.
#
# WHY (bean `qou-uiut`): the journal is written after each atom completes, but
# it only becomes durable when committed and pushed. Until now that was gated
# on an agent turn reacting to a monitor event, leaving a window between an
# atom finishing and it surviving a container reclaim. That window cost n14
# (28 minutes) once. For fe56 (~169 minutes) the window is the same size and
# the loss is six times larger.
#
# The proper fix is for the producer to commit its own journal, but the
# journal's key hashes `hadron_knot_table.py`, so editing it mid-run discards
# every atom computed so far. This watcher is a NEW file: it closes the same
# window without touching anything the key covers.
#
# Explicit path only — never `git add -A`. Retries on index lock, because the
# agent may be committing something else at the same moment.
set -uo pipefail
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"
JOURNAL=".work/hadron-knot-table-regen.json"
BRANCH="${1:-claude/anchor-followups-2026-08-08}"
INTERVAL="${2:-60}"

last=""
while true; do
  if [ -f "$JOURNAL" ]; then
    cur="$(python3 -c "
import json,sys
try:
    print(','.join(json.load(open('$JOURNAL'))['atoms']))
except Exception:
    print('')
")"
    # Only act when the journal actually differs from HEAD. Without this the
    # first iteration tries to commit an already-committed file, `git commit`
    # exits non-zero on "nothing to commit", and the retry loop spins for no
    # reason on every pass.
    if [ -n "$cur" ] && [ "$cur" != "$last" ] && \
       ! git diff --quiet -- "$JOURNAL" 2>/dev/null; then
      n="$(printf '%s' "$cur" | awk -F, '{print NF}')"
      newest="$(printf '%s' "$cur" | awk -F, '{print $NF}')"
      for attempt in 1 2 3 4 5; do
        if git add "$JOURNAL" 2>/dev/null && \
           git commit -q -m "regen journal: ${newest} (${n}/19) [auto]

Committed by scripts/watch-regen-journal.sh, which closes the window between
an atom completing and the journal becoming durable. See bean qou-uiut.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01WhxgtMTFH5XjSJTmGzVDQM" 2>/dev/null; then
          for p in 1 2 3; do
            git push origin "$BRANCH" >/dev/null 2>&1 && break
            sleep $((p * 5))
          done
          echo "[watcher] committed ${newest} (${n}/19)"
          last="$cur"
          break
        fi
        sleep $((attempt * 3))   # index lock held by the agent; back off
      done
    elif [ -n "$cur" ]; then
      last="$cur"          # already durable; nothing to do
    fi
  fi
  sleep "$INTERVAL"
done
