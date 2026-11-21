#!/usr/bin/env bash
# precommit-voice-ratchet-warn.sh — WARN (never block) when a commit would add
# a voice leak (Lean talk, backticked identifiers, first person, premature q,
# forward links) to a content block that the draining ratchet has locked.
#
# WHY THIS EXISTS (owner "Ok", 2026-11-21, epic qou-d4kh)
# ------------------------------------------------------
# folio/pipeline/voice-leak-ratchet.ts was wired only into /prepare-merge §4c.
# Merges that skip /prepare-merge never ran it, and in ~9 h after the baseline
# was locked, sibling merges re-added 27 counts across 19 blocks (22 of them
# drained by #8712). A gate nobody runs is documentation — the same lesson as
# precommit-precision-warn.sh.
#
# SCOPE: only the .md files this commit touches. The ratchet compares the whole
# paper; reporting another session's regression on every commit would train
# readers to ignore the banner. Runs in ~1.3 s.
#
# WARN-ONLY, always exit 0, like every other precommit-*-warn hook here.
set -u

payload="$(cat 2>/dev/null || true)"
cmd=""
if command -v jq >/dev/null 2>&1; then
  cmd="$(printf '%s' "$payload" | jq -r '.tool_input.command // empty' 2>/dev/null || true)"
fi
[ -z "$cmd" ] && cmd="$payload"

printf '%s' "$cmd" | grep -qE '(^|[;&|])[[:space:]]*git[[:space:]]+(-[^[:space:]]+[[:space:]]+)*commit([[:space:]]|$)' || exit 0

cd "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || exit 0

touched="$( { git diff --cached --name-only; git diff --name-only; \
              git ls-files --others --exclude-standard; } 2>/dev/null \
  | grep -E '^folio/quantum-observable-universe/.*\.md$' | sort -u )"
[ -z "$touched" ] && exit 0

ratchet="folio/pipeline/voice-leak-ratchet.ts"
[ -f "$ratchet" ] || exit 0
command -v bun >/dev/null 2>&1 || exit 0

grown="$(bun run "$ratchet" 2>/dev/null | sed -n 's/^NEW  //p')"
[ -z "$grown" ] && exit 0

hits=""
while IFS= read -r line; do
  f="${line%%  *}"
  printf '%s\n' "$touched" | grep -qxF "$f" && hits="${hits}  ${line}"$'\n'
done <<< "$grown"
[ -z "$hits" ] && exit 0

{
  echo "⚠ voice-leak ratchet: this commit adds leak counts above the locked baseline:"
  printf '%s' "$hits"
  echo "  Restate the sentence in mathematical terms; move Lean names, probe and"
  echo "  witness paths to the block's .ts authorNotes. Never raise the baseline."
  echo "  Check: bun run folio/pipeline/voice-leak-ratchet.ts  (warn-only hook)"
}
exit 0
