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
# Guarded: under `set -e` a missing `flock` (macOS, minimal images) aborted the
# whole session-start hook. The lock only serialises parallel fetches, so
# running without it is safe (T11 audit, bean qou-aq9i).
if command -v flock >/dev/null 2>&1; then flock 200; fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# 1. Fetch origin/main quietly
git fetch origin main >/dev/null 2>&1 || {
  echo "## Coord sweep — origin/main fetch failed (network?)"
  exit 0
}

CURRENT_BRANCH="$(git symbolic-ref --short HEAD 2>/dev/null || echo "DETACHED")"

# 2. Did main change since this branch was created?
NEW_COMMITS_ON_MAIN="$(git log --oneline HEAD..origin/main 2>/dev/null | wc -l | tr -d ' ')"

# 3. Find sibling claude/* branches updated in last 24h
RECENT_SIBLINGS="$(git for-each-ref --sort=-committerdate \
  --format='%(refname:short) %(committerdate:relative) %(subject)' \
  refs/remotes/origin/claude 2>/dev/null \
  | grep -v "$CURRENT_BRANCH" \
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

if [ -n "$RECENT_SIBLINGS" ]; then
  echo "**Recent sibling branches on origin (last 24h):**"
  echo "$RECENT_SIBLINGS" | sed 's/^/- /'
  echo
fi

# 4b. Active beans — the bean work-plan (anti-stall). Read beans/defs/ directly
# so this works even when the `beans` CLI is absent (fresh containers) and
# regardless of the status underscore/hyphen skew. Non-completed only.
if [ -d beans/defs ]; then
  # Parsing frontmatter with grep|sed|tr trips errexit/pipefail whenever a
  # field (id/parent) is absent — the failing substitution would abort the
  # hook. Disable both for the loop, restore after.
  set +e +o pipefail
  ACTIVE_BEANS=""
  for f in beans/defs/*.md; do
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
    echo "**Active beans (bean work-plan — \`beans/defs/\`, non-completed):**"
    printf '%s\n' "$ACTIVE_BEANS"
    echo "_Agent work-plans are **bean-based** (anti-stall, cross-session). Identify/claim the bean your PR works and narrate open/close. CLI: \`bash scripts/install-beans.sh\` then \`beans list\`; or read \`beans/defs/\` directly. See \`.claude/skills/local/bean-coordination.md\`._"
    echo
  fi
else
  # Since the beans cutover (issue #7642) beans/ is a branch mount made by
  # scripts/mount-fsh-guts.sh, whose own output goes to a log file. Say it here,
  # where the session sees it: a missing mount is NOT an empty work-plan.
  echo "**⚠ Bean work-plan UNAVAILABLE: \`beans/defs/\` is not mounted.** An empty \`beans list\` must not be read as \"no work\". Fix: \`./scripts/mount-platform-lite.sh && bun folio-assistant/cat-harness-tools/scripts/state-mount.ts\` (log: \`\${TMPDIR:-/tmp}/qou-mount-fsh-guts.log\`)."
  echo
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
echo "If the current request touches a goal listed in \`docs/_archive/orphan-top-level/STATUS.md\`:"
echo "1. Read the goal's master ledger (\`docs/coordination/<goal>.md\`)"
echo "2. Read the queue (\`todos/<goal>-queue.json\`)"
echo "3. Run \`/session-intent\` to declare intent + claim a probe"
echo "4. **Dispatch a background \`Agent(subagent_type=Explore)\`** to"
echo "   triage the new main commits + sibling activity above — do NOT"
echo "   do it in the foreground. Escalate to user only if the subagent"
echo "   surfaces something actionable against the current workplan."
echo
echo "*See \`.claude/skills/local/coordinate.md\` §11 (multi-agent same-goal)*"
