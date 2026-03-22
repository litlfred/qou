#!/bin/bash
# Check for open todos across all todo files.
# Called by SessionStart hook. Outputs JSON summary to stdout.
#
# Output JSON: { "count": N, "todos": [...], "summary": "..." }

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TODOS_DIR="$REPO_ROOT/todos"

if [ ! -d "$TODOS_DIR" ]; then
  echo '{"count":0,"todos":[],"summary":"No open todos."}'
  exit 0
fi

# Check for .ts files
ts_files=$(find "$TODOS_DIR" -name '*.ts' -type f 2>/dev/null)
if [ -z "$ts_files" ]; then
  echo '{"count":0,"todos":[],"summary":"No open todos."}'
  exit 0
fi

# Use npx tsx to evaluate TypeScript todo files properly
if command -v npx &>/dev/null; then
  todos_json=$(npx --yes tsx -e "
import { readdirSync } from 'fs';
import { join } from 'path';
import type { TodoItem } from '../content/schema/types';

const dir = '$TODOS_DIR';
const files = readdirSync(dir).filter(f => f.endsWith('.ts'));
const allTodos: (TodoItem & { file: string })[] = [];

for (const f of files) {
  try {
    const mod = require(join(dir, f));
    const items: TodoItem[] =
      mod.default ?? mod.contentTodos ?? mod.infraTodos ?? [];
    for (const item of items) {
      if (item.status === 'open' || item.status === 'in_progress') {
        allTodos.push({ ...item, file: f });
      }
    }
  } catch {}
}

console.log(JSON.stringify(allTodos));
" 2>/dev/null)
fi

if [ -z "$todos_json" ] || [ "$todos_json" = "[]" ]; then
  echo '{"count":0,"todos":[],"summary":"No open todos."}'
  exit 0
fi

if command -v jq &>/dev/null; then
  count=$(echo "$todos_json" | jq 'length')
  high=$(echo "$todos_json" | jq '[.[] | select(.priority == "high")] | length')
  medium=$(echo "$todos_json" | jq '[.[] | select(.priority == "medium")] | length')
  low=$(echo "$todos_json" | jq '[.[] | select(.priority == "low")] | length')

  summary="Open todos: $count"
  [ "$high" -gt 0 ] && summary="$summary | high: $high"
  [ "$medium" -gt 0 ] && summary="$summary | medium: $medium"
  [ "$low" -gt 0 ] && summary="$summary | low: $low"

  top=$(echo "$todos_json" | jq -r '
    sort_by(if .priority == "high" then 0 elif .priority == "medium" then 1 else 2 end) |
    .[0:5] |
    .[] |
    "  [\(.priority)] \(.targetLabel // .file): \(.summary // "(no summary)" | .[0:60])"
  ')

  if [ -n "$top" ]; then
    summary="$summary
$top"
  fi

  jq -n --argjson todos "$todos_json" --arg summary "$summary" \
    '{count: ($todos | length), todos: $todos, summary: $summary}'
else
  count=$(echo "$todos_json" | grep -o '"id"' | wc -l | tr -d ' ')
  echo "{\"count\":$count,\"todos\":$todos_json,\"summary\":\"$count open todo(s). Install jq for details.\"}"
fi
