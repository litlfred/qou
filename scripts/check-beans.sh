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
# Two more added 2026-09-07. Both PARSE — which is why the four above missed
# them, and why the field loop below was not enough on its own: it tested that
# `title:` and `status:` were PRESENT, never that their values were usable.
#   5. `title:` present and EMPTY        (blocking; 5 of 5053, all repaired)
#   6. `status:` outside beans' own vocabulary   (ADVISORY; 46 of 5053)
#
# Shape 6 is advisory on purpose. The obvious repair -- rewrite `done` to
# `completed` -- is wrong: `done` does not reliably mean finished, and at least
# one such bean is a live gap. Read the block at shape 6 before touching them.
#
# Usage:  scripts/check-beans.sh [--quiet]
# Exit:   0 clean (advisories do not fail), 1 problems found.

set -uo pipefail
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "not a git repo"; exit 0; }
cd "$ROOT"
[ -d .beans ] || { echo "check-beans: no .beans/ directory"; exit 0; }

quiet=0; [ "${1:-}" = "--quiet" ] && quiet=1

bad=0 total=0 advisory=0
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

  # Shape 5: front-matter READABLE, `title:` present, and EMPTY.
  #
  # The four shapes above are all parser failures. This one parses perfectly and
  # still lands the file in the state this script's header describes — invisible
  # in `beans list`, unfindable by the corpus-grep checklist's `.beans/` path,
  # and a false match for the exact-title existence check AGENTS.md requires
  # before every `beans create` (an empty title matches every other empty one).
  #
  # Measured 2026-09-07: 5 of 5053 files, dated 2026-06-14 to 2026-08-10, so it
  # recurs rather than being a single event. In 4 of the 5 the title had been
  # moved into the body as an H1 and blanked here, so it was recoverable
  # exactly; a body H1 is NOT the healthy convention (48 of 5053), which is how
  # they were told apart.
  title_val=$(grep -m1 '^title:' <<<"$fm" | sed 's/^title:[[:space:]]*//')
  case "$title_val" in
    ""|"''"|'""')
      echo "⚠ $f"
      echo "    front-matter parses but 'title:' is EMPTY — invisible in \`beans list\`."
      echo "    → shape 5: check the body for an '# <H1>' holding the real title and"
      echo "      lift it into 'title:'. If there is none, de-slugify the filename and"
      echo "      say in the commit that the title is slug-derived, not recovered."
      bad=$((bad+1)) ;;
  esac
  # Shape 6, ADVISORY: `status:` outside the vocabulary beans itself accepts
  # (`beans update --help`: in-progress, todo, draft, completed, scrapped).
  #
  # Measured 2026-09-07: 46 of 5053 — `done` (43) and `open` (3). beans does
  # NOT normalise them: a `done` bean is absent from `beans list --status
  # completed` and present only under `--status done`, and the three `open`
  # ones are absent from `--status todo`. So every status-filtered query misses
  # them. `session-start-coord-sweep.sh` hand-patches `done` alone
  # (`case "$status" in completed|done) continue`), which is why they have not
  # been showing up as active work.
  #
  # ADVISORY, NOT BLOCKING, and deliberately so: the obvious repair — rewrite
  # `done` to `completed` — is WRONG. `done` is not reliably "finished".
  # `qou-argp` carries `status: done` over a body reading "Everything the
  # converse zero locus needs is proved EXCEPT ONE NAMED LEMMA" — a live gap.
  # Bulk-normalising would close it, which AGENTS.md rule 13a forbids outright
  # ("Don't close beans with open conjectures!!!", owner directive).
  #
  # So these need per-bean adjudication by someone who can read the body and
  # decide, not a sweep. This surfaces them; it does not fail the gate, because
  # a gate nobody can turn green gets disabled instead of drained.
  status_val=$(grep -m1 '^status:' <<<"$fm" | sed "s/^status:[[:space:]]*//" | tr -d "'\"")
  case "$status_val" in
    in-progress|todo|draft|completed|scrapped|"") ;;
    *)
      if [ "$quiet" -eq 0 ]; then
        echo "· $f"
        echo "    ADVISORY: status '$status_val' is outside beans' vocabulary"
        echo "      (in-progress, todo, draft, completed, scrapped), so this bean is"
        echo "      missed by every \`beans list --status\` query. Read the body before"
        echo "      changing it — 'done' does NOT reliably mean finished."
      fi
      advisory=$((advisory+1)) ;;
  esac

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
  if [ "$quiet" -eq 0 ]; then
    echo "check-beans: $total bean file(s), all structurally sound."
    [ "$advisory" -gt 0 ] && echo "check-beans: $advisory advisory (non-blocking) — see '·' lines above."
  fi
  exit 0
fi
echo
echo "check-beans: $bad problem(s) across $total bean file(s)."
exit 1
