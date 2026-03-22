#!/bin/bash
# Cross-reference open todos with content blocks modified in the current branch.
# Outputs JSON: { "matches": [...], "count": N }
#
# Each match: { "rootName": "...", "todo": {...}, "changedFiles": ["..."] }
#
# Usage: ./scripts/check-branch-todos.sh [base-branch]
#   base-branch defaults to "main"

set -euo pipefail

BASE="${1:-main}"
FEEDBACK_DIR="$(cd "$(dirname "$0")/.." && pwd)/.qou-feedback"

# If no feedback dir or not in a git repo, exit clean
if [ ! -d "$FEEDBACK_DIR" ]; then
  echo '{"matches":[],"count":0}'
  exit 0
fi

# Get current branch
CURRENT=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "")
if [ -z "$CURRENT" ] || [ "$CURRENT" = "$BASE" ]; then
  echo '{"matches":[],"count":0}'
  exit 0
fi

# Check if base branch exists
if ! git rev-parse --verify "$BASE" &>/dev/null; then
  echo '{"matches":[],"count":0}'
  exit 0
fi

# Get content files changed in this branch vs base
changed_files=$(git diff --name-only "$BASE"...HEAD -- 'content/**/*.ts' 'content/**/*.md' 'content/**/*.lean' 2>/dev/null || true)

if [ -z "$changed_files" ]; then
  echo '{"matches":[],"count":0}'
  exit 0
fi

# Extract unique root names from changed files
root_names=$(echo "$changed_files" | sed 's|.*/||; s/\.[^.]*$//' | sort -u)

# Find matching todos
matches=""
count=0

for rootName in $root_names; do
  # Search for feedback files matching this root name
  feedback_files=$(find "$FEEDBACK_DIR" -name "${rootName}.json" -type f 2>/dev/null || true)

  for ff in $feedback_files; do
    [ -z "$ff" ] && continue
    [ ! -f "$ff" ] && continue

    # Get open todos from this file
    if command -v jq &>/dev/null; then
      open_todos=$(jq -c '[.[] | select(.status == "open")]' "$ff" 2>/dev/null)
      todo_count=$(echo "$open_todos" | jq 'length' 2>/dev/null || echo "0")

      if [ "$todo_count" -gt 0 ]; then
        # Get the changed files for this root name
        block_files=$(echo "$changed_files" | grep "/${rootName}\." | jq -R -s 'split("\n") | map(select(length > 0))' 2>/dev/null)

        # Add each open todo as a match
        echo "$open_todos" | jq -c ".[] | {rootName: \"$rootName\", todo: ., changedFiles: $block_files}" 2>/dev/null | while read -r match; do
          if [ -n "$matches" ]; then
            matches="${matches},${match}"
          else
            matches="${match}"
          fi
          count=$((count + 1))
          echo "$match"
        done
      fi
    else
      # No jq: just check if file has "open" in it
      if grep -q '"open"' "$ff" 2>/dev/null; then
        echo "{\"rootName\":\"$rootName\",\"todo\":{\"status\":\"open\"},\"changedFiles\":[]}"
        count=$((count + 1))
      fi
    fi
  done
done | {
  # Collect all matches into a JSON array
  if command -v jq &>/dev/null; then
    jq -s '{matches: ., count: length}'
  else
    items=""
    n=0
    while read -r line; do
      [ -n "$items" ] && items="${items},"
      items="${items}${line}"
      n=$((n + 1))
    done
    echo "{\"matches\":[${items}],\"count\":${n}}"
  fi
}
