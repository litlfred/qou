#!/usr/bin/env bash
# check-beans.sh — structural validator for the `.beans/` flat-file tracker.
#
# The beans work-plan is the agent's source of truth for "what next"
# (AGENTS.md §Agent work-plan policy). A bean file that a front-matter parser
# cannot read carries no id, no status and no title, so it is invisible to
# `beans list` and therefore to the §4 idle-backlog policy that walks it —
# while still looking, to `git`, like a tracked and healthy bean.
#
# Measured 2026-08-23 over 3833 files: 12 were unreadable this way, between
# them holding ~700 lines of real work including a `status: todo` research item
# and a CLOSED proof-route record. Every one arrived the same way: `cat >>` to a
# GUESSED filename. `beans create` slugs a title by dropping punctuation
# (`placeholders/TODOs` -> `placeholderstodos`, `n=2` -> `n2`, `s5-so3` ->
# `s5so3`), so an agent reconstructing the path by hyphenating misses by one
# character and silently creates a new, front-matter-less file beside the real
# bean. Nothing errors; the append just goes somewhere nobody reads.
#
# Four failure shapes, all seen in that set:
#   1. no front-matter at all          (orphaned `cat >>` to a guessed slug)
#   2. front-matter present but not at the top   (body PREPENDED above it)
#   3. opening `---` missing, fields and closing `---` present
#   4. two files claiming the same `# <id>`
#
# Usage:  scripts/check-beans.sh [--quiet]
# Exit:   0 clean, 1 problems found (so it can gate a commit).

set -uo pipefail
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "not a git repo"; exit 0; }
cd "$ROOT"
[ -d .beans ] || { echo "check-beans: no .beans/ directory"; exit 0; }

quiet=0; [ "${1:-}" = "--quiet" ] && quiet=1

bad=0 total=0
declare -A idfile

for f in .beans/*.md; do
  [ -f "$f" ] || continue
  total=$((total+1))

  # Herestring for the same pipefail/SIGPIPE reason as the field checks below.
  if ! grep -q '^---$' <<<"$(head -1 "$f")"; then
    # Distinguish shape 2/3 from shape 1 — the fix differs.
    if grep -qE '^# [A-Za-z0-9-]+$' "$f" && grep -q '^title:' "$f"; then
      if grep -qn '^---$' "$f"; then
        echo "⚠ $f"
        echo "    front-matter fields present but the file does not START with '---'."
        echo "    → shape 2/3: either the body was prepended above the front-matter,"
        echo "      or the opening delimiter is missing. Move the block to the top."
      fi
    else
      echo "⚠ $f"
      echo "    NO front-matter — no id, no status, no title. Invisible to the tracker."
      echo "    → shape 1: almost certainly a 'cat >>' to a guessed slug. Find the real"
      echo "      bean (ls .beans/ | grep '^<id>'), append this body to it, remove this file."
    fi
    bad=$((bad+1)); continue
  fi

  # Front-matter starts at the top; check it is complete.
  fm=$(sed -n '2,/^---$/p' "$f")
  id=$(grep -m1 -oE '^# [A-Za-z0-9-]+$' <<<"$fm" | sed 's/^# //')
  # HERESTRING, not `printf | grep -q`. Under `set -o pipefail` that pipeline
  # reports FAILURE on a successful match: `grep -q` exits at the first hit and
  # closes the pipe, `printf` takes SIGPIPE (141), and pipefail propagates the
  # rightmost non-zero status. It is intermittent by construction — it fires only
  # when grep exits before printf has finished writing — which is why it hit
  # exactly 2 of 3825 bean files and reported `title:`/`status:` missing on two
  # beans that plainly have both.
  for field in title status; do
    grep -q "^$field:" <<<"$fm" || {
      echo "⚠ $f"; echo "    front-matter missing '$field:'"; bad=$((bad+1)); }
  done
  if [ -z "$id" ]; then
    echo "⚠ $f"; echo "    front-matter has no '# <id>' line"; bad=$((bad+1))
  elif [ -n "${idfile[$id]:-}" ]; then
    echo "⚠ $f"
    echo "    duplicate id '$id' — also claimed by ${idfile[$id]}"
    echo "    → the two files are NOT necessarily the same bean re-slugged. Read both"
    echo "      before deleting either; re-issue one under a fresh id if they differ."
    bad=$((bad+1))
  else
    idfile[$id]="$f"
  fi
done

if [ "$bad" -eq 0 ]; then
  [ "$quiet" -eq 1 ] || echo "check-beans: $total bean file(s), all structurally sound."
  exit 0
fi
echo
echo "check-beans: $bad problem(s) across $total bean file(s)."
exit 1
