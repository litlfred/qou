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
