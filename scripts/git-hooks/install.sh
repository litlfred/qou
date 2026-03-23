#!/bin/sh
# Install git hooks from scripts/git-hooks/ into .git/hooks/
# Run from repo root:  ./scripts/git-hooks/install.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
HOOK_DIR="$(git rev-parse --show-toplevel)/.git/hooks"

for hook in "$SCRIPT_DIR"/post-checkout "$SCRIPT_DIR"/pre-commit; do
    name="$(basename "$hook")"
    [ -f "$hook" ] || continue
    cp "$hook" "$HOOK_DIR/$name"
    chmod +x "$HOOK_DIR/$name"
    echo "Installed $name"
done
