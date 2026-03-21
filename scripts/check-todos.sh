#!/bin/bash
# Check for open feedback/todos across all content blocks.
# Called by SessionStart hook. Outputs JSON summary to stdout
# and a human-readable summary to stderr.
#
# Output JSON: { "count": N, "todos": [...], "summary": "..." }

FEEDBACK_DIR="$(cd "$(dirname "$0")/.." && pwd)/.qou-feedback"

if [ ! -d "$FEEDBACK_DIR" ]; then
  echo '{"count":0,"todos":[],"summary":"No open todos."}'
  exit 0
fi

# Collect all open todos from all JSON files
todos_json=$(find "$FEEDBACK_DIR" -name '*.json' -type f 2>/dev/null | while read -r f; do
  paperId=$(basename "$(dirname "$f")")
  rootName=$(basename "$f" .json)
  # Extract open todos, annotate with paperId and rootName
  if command -v jq &>/dev/null; then
    jq -c --arg p "$paperId" --arg r "$rootName" \
      '[.[] | select(.status == "open") | . + {paperId: $p, rootName: $r}] | .[]' "$f" 2>/dev/null
  else
    # Fallback: just report file exists
    cat "$f" 2>/dev/null | grep -o '"status":"open"' | while read -r _; do
      echo "{\"paperId\":\"$paperId\",\"rootName\":\"$rootName\",\"status\":\"open\"}"
    done
  fi
done)

if [ -z "$todos_json" ]; then
  echo '{"count":0,"todos":[],"summary":"No open todos."}'
  exit 0
fi

# Build output
count=$(echo "$todos_json" | wc -l | tr -d ' ')

if command -v jq &>/dev/null; then
  # Build proper JSON array
  arr=$(echo "$todos_json" | jq -s '.')

  # Count by priority
  high=$(echo "$arr" | jq '[.[] | select(.priority == "high")] | length')
  medium=$(echo "$arr" | jq '[.[] | select(.priority == "medium")] | length')
  low=$(echo "$arr" | jq '[.[] | select(.priority == "low")] | length')

  # Build summary lines
  summary="Open todos: $count"
  [ "$high" -gt 0 ] && summary="$summary | high: $high"
  [ "$medium" -gt 0 ] && summary="$summary | medium: $medium"
  [ "$low" -gt 0 ] && summary="$summary | low: $low"

  # Top items for display
  top=$(echo "$arr" | jq -r '
    sort_by(if .priority == "high" then 0 elif .priority == "medium" then 1 else 2 end) |
    .[0:5] |
    .[] |
    "  [\(.priority)] \(.rootName): \(.summary // .comment // "no description" | .[0:60])"
  ')

  if [ -n "$top" ]; then
    summary="$summary
$top"
  fi

  jq -n --argjson todos "$arr" --arg summary "$summary" \
    '{count: ($todos | length), todos: $todos, summary: $summary}'
else
  # No jq fallback
  echo "{\"count\":$count,\"todos\":[],\"summary\":\"$count open todo(s). Install jq for details.\"}"
fi
