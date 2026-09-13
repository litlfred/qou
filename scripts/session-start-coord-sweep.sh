#!/usr/bin/env bash
# session-start-coord-sweep.sh
#
# Runs at session start (per .claude/settings.json SessionStart hook).
# Emits a brief context block that the agent reads + uses to decide
# whether to dispatch a background subagent for full coord-sweep.
#
# Per AGENTS.md "User accessibility" §5-minute idle trigger AND
# .claude/skills/local/coordinate.md: at session start fetch origin/main,
# list relevant new commits, summarize sibling PR activity. Pass the
# heavy work off to a background Explore subagent — don't disrupt
# user-facing flow.
#
# Output: markdown that's printed back to the agent as a system reminder.

set -euo pipefail

# Acquire global lock to prevent parallel git fetches across agent workspaces
exec 200>"/tmp/qou-coord-sweep.lock"
flock 200

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# ── 0. Long-running producer: is it still alive? ────────────────────────────
#
# FIRST in this file, deliberately. The reader truncates this output at about
# 2 KB, so anything below the beans priming is not seen; and this is the only
# time-critical line here.
#
# WHY A HOOK AND NOT A SUPERVISOR. The qou-uiut table takes hours and the
# container is recycled every ~25-45 minutes, which kills the run. On
# 2026-09-13 I wrote .work/hkt-supervise.sh to poll-restart it, and that was
# the wrong shape: a recycle kills the SUPERVISOR TOO, so it cannot protect
# against the one failure it was built for. It still earns its place for a
# process that dies inside a living container. But this hook is the only thing
# that runs AFTER a recycle, so this is where a restart has to be prompted.
#
# REPORTS, DOES NOT START. Launching a multi-hour 100%-CPU producer in every
# session that opens this repo is a side effect nobody asked for, and a
# sibling agent doing unrelated work would pay for it. The restart is one
# command and it is printed here.
#
# 🛑 THIS ONLY FIRES FOR A qou-ROOTED SESSION. Corrected 2026-09-13, the same
# day it was written, after watching it not fire. The hook command is
# `bash "$CLAUDE_PROJECT_DIR/scripts/session-start-coord-sweep.sh"`, and
# CLAUDE_PROJECT_DIR is whichever repo the session is rooted in. A session
# rooted in folio-assistant runs THAT repo's script -- which exists, has the
# same filename, and emits its own "## Coord sweep" -- so this file is never
# executed and this block never prints. Identified by the branch name in the
# output: it reported `claude/agent-4677-padding-1idnru`, a folio-assistant
# branch, not the qou one.
#
# Do NOT "fix" that by adding a qou table check to folio-assistant's sweep.
# folio-assistant is the PLATFORM and this table is FOLIO content; that edit
# is the exact boundary violation its AGENTS.md opens by warning about. An
# agent working qou from a folio-assistant-rooted session has to check by
# hand, and knowing that is the point of this note.
_hkt_ckpt="$REPO_ROOT/.work/hkt-uiut-ckpt.json"
if [ -f "$_hkt_ckpt" ]; then
  _hkt_n="$(python3 -c 'import json,sys; print(len(json.load(open(sys.argv[1]))["atoms"]))'             "$_hkt_ckpt" 2>/dev/null || echo '?')"
  if [ "$_hkt_n" != "19" ]; then
    if ps -eo cmd --no-headers 2>/dev/null          | grep -q '^python3 computations/hadron_knot_table.py'; then
      echo "## qou-uiut table — RUNNING, ${_hkt_n}/19 atoms"
    else
      echo "## 🛑 qou-uiut table — STOPPED at ${_hkt_n}/19. Restart it:"
      echo
      echo '    scripts/hkt-resume.sh --commit'
      echo
      echo "Idempotent (refuses a second producer in one checkout) and gated on"
      echo "the mpfr LP kernel, whose absence makes the run silently wrong."
      echo "Completed atoms are committed; work inside the atom in flight is"
      echo "carried by \`.work/kernel-memo/\`, which survives a recycle -- so a"
      echo "restart resumes partway rather than from the atom's start."
    fi
    echo
  fi
fi

# 1. Fetch origin/main quietly
git fetch origin main >/dev/null 2>&1 || {
  echo "## Coord sweep — origin/main fetch failed (network?)"
  exit 0
}

# 1b. Fetch the refs step 3 reads. A clone whose configured refspec is
# `+refs/heads/main:refs/remotes/origin/main` -- the default in ephemeral
# containers here -- NEVER updates refs/remotes/origin/claude/*, so step 3 read a
# frozen snapshot (usually empty) and step 4 then omitted the sibling section
# altogether: absence of refs rendered as absence of siblings. Pass the refspec
# explicitly so this does not depend on how the clone happens to be configured.
if command -v timeout >/dev/null 2>&1; then
  _fetch_siblings() { timeout 45 git fetch --quiet --prune origin "$1" >/dev/null 2>&1; }
else
  _fetch_siblings() { git fetch --quiet --prune origin "$1" >/dev/null 2>&1; }
fi
SIBLING_REFS="unrefreshed"
if _fetch_siblings '+refs/heads/claude/*:refs/remotes/origin/claude/*'; then
  SIBLING_REFS="fresh"
fi

CURRENT_BRANCH="$(git symbolic-ref --short HEAD 2>/dev/null || echo "DETACHED")"

# 2. Did main change since this branch was created?
NEW_COMMITS_ON_MAIN="$(git log --oneline HEAD..origin/main 2>/dev/null | wc -l | tr -d ' ')"

# 3. Sibling claude/* branches updated in the last 24h. The window is applied
# HERE now; it used to be asserted only in the heading while the code sorted by
# date and took the top 8 regardless of age.
SIBLING_CUTOFF="$(( $(date -u +%s) - 86400 ))"
SIBLING_ALL="$(git for-each-ref --sort=-committerdate \
  --format='%(committerdate:unix)|%(refname:short)|%(committerdate:relative)|%(subject)' \
  refs/remotes/origin/claude 2>/dev/null \
  | grep -v "|origin/$CURRENT_BRANCH|" || true)"
SIBLING_TOTAL="$(printf '%s' "$SIBLING_ALL" | grep -c . || true)"
SIBLING_RECENT="$(printf '%s\n' "$SIBLING_ALL" \
  | awk -F'|' -v c="$SIBLING_CUTOFF" 'NF && $1 >= c' || true)"
SIBLING_RECENT_N="$(printf '%s' "$SIBLING_RECENT" | grep -c . || true)"
# Rebuild the subject from field 4 onward: commit subjects may contain `|`.
RECENT_SIBLINGS="$(printf '%s\n' "$SIBLING_RECENT" \
  | awk -F'|' 'NF { s=$4; for (i=5; i<=NF; i++) s=s"|"$i; print $2" "$3" "s }' \
  | head -8 || true)"

# 4. Emit the markdown block
cat <<EOF
## Coord sweep (session start) — $(date -u +%Y-%m-%dT%H:%M:%SZ)

**Branch:** \`$CURRENT_BRANCH\`
**Origin/main is ahead by:** $NEW_COMMITS_ON_MAIN commit(s) since this branch diverged.

EOF

if [ "$NEW_COMMITS_ON_MAIN" -gt 0 ]; then
  echo "**Recent main landings (last 10):**"
  # `git log | head` makes git log receive SIGPIPE once head closes; under
  # `set -euo pipefail` that 141 aborts the whole hook. Guard with `|| true`.
  { git log --oneline HEAD..origin/main | head -10 | sed 's/^/- /'; } || true
  echo
fi

# Always emit this section, including when it is empty. Omitting it on an empty
# list is what let "the refs were never fetched" look identical to "no siblings
# are active" -- the reader cannot tell a measured zero from an unmeasured one.
echo "**Sibling \`claude/*\` branches on origin:**"
if [ "$SIBLING_REFS" != "fresh" ]; then
  echo "- **NOT REFRESHED** (sibling fetch failed or timed out) - the list below is"
  echo "  whatever this clone already had. Do NOT read an empty list as \"no siblings\"."
fi
if [ -n "$RECENT_SIBLINGS" ]; then
  echo "_${SIBLING_RECENT_N} updated in the last 24h, of ${SIBLING_TOTAL} known; showing up to 8:_"
  echo "$RECENT_SIBLINGS" | sed 's/^/- /'
else
  echo "_0 of ${SIBLING_TOTAL} known sibling branch(es) updated in the last 24h._"
fi
echo

# 4b. Active beans — the bean work-plan (anti-stall). Read .beans/ directly
# so this works even when the `beans` CLI is absent (fresh containers) and
# regardless of the status underscore/hyphen skew. Non-completed only.
if [ -d .beans ]; then
  # Parsing frontmatter with grep|sed|tr trips errexit/pipefail whenever a
  # field (id/parent) is absent — the failing substitution would abort the
  # hook. Disable both for the loop, restore after.
  set +e +o pipefail
  ACTIVE_BEANS=""
  for f in .beans/*.md; do
    [ -e "$f" ] || continue
    status="$(grep -m1 '^status:' "$f" | sed 's/^status:[[:space:]]*//' | tr -d '\r')"
    case "$status" in completed|done) continue;; esac
    # id: `id:` field (old format) → else the filename prefix before `--`.
    id="$(grep -m1 '^id:' "$f" | sed 's/^id:[[:space:]]*//' | tr -d '\r')"
    if [ -z "$id" ]; then id="$(basename "$f" | sed 's/--.*//')"; fi
    parent="$(grep -m1 '^parent:' "$f" | sed 's/^parent:[[:space:]]*//' | tr -d '\r')"
    # title: quoted `title:` field (hmans/beans format) → else a body
    # `# Heading` (old format). Strip surrounding quotes.
    title="$(grep -m1 '^title:' "$f" | sed "s/^title:[[:space:]]*//; s/^['\"]//; s/['\"]$//" | tr -d '\r')"
    if [ -z "$title" ]; then title="$(grep -m1 '^# ' "$f" | sed 's/^#[[:space:]]*//' | tr -d '\r')"; fi
    if [ -n "$parent" ]; then parent=" (parent: $parent)"; fi
    ACTIVE_BEANS="${ACTIVE_BEANS}- \`${id:-?}\` [${status:-?}] ${title:-$f}${parent}
"
  done
  set -e -o pipefail
  if [ -n "$ACTIVE_BEANS" ]; then
    echo "**Active beans (bean work-plan — \`.beans/\`, non-completed):**"
    printf '%s\n' "$ACTIVE_BEANS"
    echo "_Agent work-plans are **bean-based** (anti-stall, cross-session). Identify/claim the bean your PR works and narrate open/close. CLI: \`bash scripts/install-beans.sh\` then \`beans list\`; or read \`.beans/\` directly. See \`.claude/skills/local/bean-coordination.md\`._"
    echo
  fi
fi

# 4b. Lean artifact freshness — a stale olean silently inverts `#print axioms`
#
# Measured 2026-09-05 (bean qou-pdgc): QOU/HeckeAlgebra/MarkovTrace.olean was
# ~3 months behind its source, and in it THREE declarations that are `def`s in
# source were AXIOMS, five theorems were absent, and wenzlBridge carried a form
# the source had already retracted. `lean`-direct verifies against the oleans on
# disk, so a footprint read there can name constants that do not exist in source.
# That is invisible unless someone looks, which is what this line is for.
if [ -x scripts/lean-olean-staleness-audit.py ] || [ -f scripts/lean-olean-staleness-audit.py ]; then
  echo "**Lean artifact freshness:**"
  echo
  python3 scripts/lean-olean-staleness-audit.py --top 5 2>/dev/null | sed 's/^/    /' \
    || echo "    (could not run — NOT a pass; nothing was compared)"
  echo
  echo "_Repair, do not interpret: \`bash scripts/lean-direct-cone.sh <Module>\`._"
  echo "_A \`#print axioms\` taken against a stale olean is a statement about a cache._"
  echo
fi

# 4c. Can the axiom gate report at all?
#
# scripts/lean-axiom-guard.py exits 2 -- producing NO verdict -- when any olean in
# its cone is missing or stale. Correctly: a verdict from a stale set is the axiom
# status of an old snapshot. But nothing surfaced that it WAS exiting 2, so it sat
# unable to report for ~a month while ~104 of its modules went stale (two were
# never built). It was not red; it was BLIND, and blind looks like silence. When
# restored it immediately reported a month-old promotion nobody had seen (bean
# qou-1knw). A gate that can go quietly non-functional needs a check on its own
# liveness, and that is this line.
if [ -f scripts/lean-axiom-guard.py ]; then
  echo "**Axiom gate liveness:**"
  echo
  # `set -euo pipefail` is in force (line 16) and --can-run exits 3 when the gate
  # is blind, which is its NORMAL informative outcome. A bare assignment would
  # abort the whole hook on exactly the case this line exists to report, so the
  # rc is captured through `||`. Same hazard the note at the top of section 3
  # records for exit 141.
  GUARD_RC=0
  GUARD_OUT="$(timeout 120 python3 scripts/lean-axiom-guard.py --can-run 2>&1)" || GUARD_RC=$?
  case "$GUARD_RC" in
    0|3) printf '%s\n' "$GUARD_OUT" | sed 's/^/    /' ;;
    *) echo "    could not determine whether the axiom gate can run (exit $GUARD_RC)."
       echo "    That is NOT a pass -- it is the watchdog itself going dark." ;;
  esac
  echo
fi

# 5. Recommended action
echo "**Recommended action:**"
echo
echo "If the current request touches a goal listed in \`STATUS.md\`:"
echo "1. Read the goal's master ledger (\`docs/coordination/<goal>.md\`)"
echo "2. Read the queue (\`todos/<goal>-queue.json\`)"
echo "3. Run \`/session-intent\` to declare intent + claim a probe"
echo "4. **Dispatch a background \`Agent(subagent_type=Explore)\`** to"
echo "   triage the new main commits + sibling activity above — do NOT"
echo "   do it in the foreground. Escalate to user only if the subagent"
echo "   surfaces something actionable against the current workplan."
echo
echo "*See \`.claude/skills/local/coordinate.md\` §11 (multi-agent same-goal)*"
