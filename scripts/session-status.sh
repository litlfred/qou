#!/usr/bin/env bash
# session-status.sh — SessionStart surface for the bean work-plan system.
#
# Wired in .claude/settings.json (SessionStart hooks). Surfaces the current
# session beans at the top of every session so every agent immediately
# discovers and adopts the bean-based work-plan.
#
# Owner directive (anti-stall): session work revolves around beans. Agents
# must identify the bean(s) they are working and open/close them
# (`beans update <id> --status in-progress` / `--status completed`)
# actively in the session discussion. See
# .claude/skills/local/bean-coordination.md + todo-manager.md.
set -u

echo "## Bean work-plan — session start"
echo
echo "Owner directive (anti-stall): **session work revolves around beans**."
echo "Identify the bean(s) you are working; open them (\`beans update <id>"
echo "--status in-progress\`) and close them (\`--status completed\`) actively"
echo "in the session discussion. beans != sidecars (QA / witness queues stay"
echo "as bulk JSON, never \`beans create\`-d)."
echo

BEANS_BIN=""
if command -v beans >/dev/null 2>&1; then
  BEANS_BIN="beans"
elif [ -x "$HOME/.local/bin/beans" ]; then
  BEANS_BIN="$HOME/.local/bin/beans"
fi

if [ -n "$BEANS_BIN" ]; then
  echo "Current beans (open + recent):"
  "$BEANS_BIN" list 2>/dev/null | head -40
  echo
  echo "New work -> beans create \"<title>\" --type task [--parent <milestone>]"
else
  echo "beans CLI not installed — run:  bash scripts/install-beans.sh"
  echo "  (or: go install github.com/hmans/beans@latest ; needs Go on PATH)"
fi
