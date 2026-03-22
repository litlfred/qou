#!/bin/bash
# Cross-reference open todos with content blocks modified in the current branch.
# Outputs JSON: { "matches": [...], "count": N }
#
# Usage: ./scripts/check-branch-todos.sh [base-branch]
#   base-branch defaults to "main"

set -euo pipefail

BASE="${1:-main}"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TODOS_DIR="$REPO_ROOT/todos"

# If no todos dir or not in a git repo, exit clean
if [ ! -d "$TODOS_DIR" ]; then
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

# Use the check-todos.sh output to find matching todos by targetLabel
if ! command -v node &>/dev/null; then
  echo '{"matches":[],"count":0}'
  exit 0
fi

# Get all open todos and match against changed root names
node -e "
const { readdirSync, readFileSync } = require('fs');
const { join } = require('path');

const todosDir = '$TODOS_DIR';
const rootNames = new Set($(echo "$root_names" | jq -R -s 'split("\n") | map(select(length > 0))'));
const changedFiles = $(echo "$changed_files" | jq -R -s 'split("\n") | map(select(length > 0))');

// Read all todo files
const allTodos = [];
try {
  for (const f of readdirSync(todosDir).filter(f => f.endsWith('.ts'))) {
    const src = readFileSync(join(todosDir, f), 'utf8');
    const match = src.match(/\[[\s\S]*\]/);
    if (!match) continue;
    try {
      const cleaned = match[0].replace(/\/\/[^\n]*/g, '').replace(/,(\s*[\]}])/g, '\$1');
      for (const item of JSON.parse(cleaned)) {
        if (item.status === 'open' || item.status === 'in_progress') {
          allTodos.push({ ...item, file: f });
        }
      }
    } catch {}
  }
} catch {}

// Match todos whose targetLabel contains a root name
const matches = [];
for (const todo of allTodos) {
  const label = todo.targetLabel || '';
  // Extract the root-name part from the label (e.g. 'def:localized-knot' -> 'localized-knot')
  const labelRoot = label.includes(':') ? label.split(':').slice(1).join(':') : label;
  if (rootNames.has(labelRoot)) {
    const relevant = changedFiles.filter(f => f.includes(labelRoot));
    matches.push({ rootName: labelRoot, todo, changedFiles: relevant });
  }
}

console.log(JSON.stringify({ matches, count: matches.length }));
" 2>/dev/null || echo '{"matches":[],"count":0}'
