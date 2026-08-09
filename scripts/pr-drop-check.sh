#!/bin/bash
# Per #4840: deliverable-level tracing cannot see a dropped edit to a
# file that was MODIFIED on both sides. Three-way test per modified file.
MAIN=origin/main
for pr in 3793 4551 4519 4538 4540 4525 4521 4176 4106; do
  head=refs/prheads/$pr
  mb=$(git merge-base $MAIN $head)
  echo "=== PR #$pr (base ${mb:0:8}) ==="
  # only files the branch MODIFIED (pure adds land or conflict loudly)
  git diff --name-status --diff-filter=M "$mb" "$head" | cut -f2 | while read -r f; do
    a=$(git rev-parse "$mb:$f" 2>/dev/null)
    b=$(git rev-parse "$head:$f" 2>/dev/null)
    m=$(git rev-parse "$MAIN:$f" 2>/dev/null)
    if [ -z "$m" ]; then echo "  GONE-FROM-MAIN  $f"; continue; fi
    if [ "$b" = "$m" ]; then continue; fi                       # landed identical
    if [ "$a" = "$m" ]; then echo "  DROP            $f"; continue; fi  # main untouched, branch content absent
    echo "  BOTH-MODIFIED   $f"                                  # needs line-level read
  done
done
