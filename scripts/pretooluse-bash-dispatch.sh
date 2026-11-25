#!/usr/bin/env bash
# pretooluse-bash-dispatch.sh — the ONE PreToolUse hook on the Bash tool.
#
# It runs the eight warn-only checks that used to be wired as eight separate
# hooks, but only the ones whose trigger the command actually matches, and it
# hands Claude Code a single answer.
#
# WHY THIS EXISTS (2026-11-25)
# ----------------------------
# The owner saw "A hook gave no usable answer, so it didn't check this action."
# eight times on Bash calls. Measured from the session transcript: every one of
# them was a `hook_non_blocking_error` with exit code 127, "a shell's code for a
# program it could not run". The eight hooks were wired as `./scripts/<x>.sh`,
# and a hook runs in the session's CURRENT directory. The main session keeps a
# `cd` between Bash calls, so after `cd beans/defs`, `cd folio/.../lean` or a
# `cd /tmp/...` worktree, `./scripts/...` does not exist and all eight fail at
# once. 72 of 73 PreToolUse hook results in that session were this failure, and
# each preceding Bash call had moved the cwd away from the repo root.
#
# Three further defects were found while fixing it:
#   - precommit-bean-id-warn.sh and prebranch-bean-loss-warn.sh read the
#     command from their ARGUMENTS ("$*"), but the hooks were wired with no
#     arguments, so both returned early on every call and never warned.
#   - precommit-ledger-shrink-warn.sh ran its git check on every Bash call.
#   - Warnings written to stderr on exit 0 reach neither the user nor Claude.
#
# WHAT IT DOES
# ------------
# - Reads the PreToolUse JSON from stdin once and extracts tool_input.command.
# - Exits 0 with NO output, in a few milliseconds, unless the command is a
#   `git commit`, `git add`, branch-store push, or a branch-creating checkout or
#   switch. Those are the only commands any of the eight checks acts on.
# - Runs the matching checks in parallel. Each keeps its own logic and its own
#   messages; the payload is piped to the stdin readers, and the command is
#   passed as the argument to the two checks that read their arguments.
# - Collects each check's stdout and stderr. When there is anything to say, it
#   prints ONE JSON object: `systemMessage` (shown to the user) and
#   `hookSpecificOutput.additionalContext` (shown to Claude). It never sets
#   permissionDecision.
# - ALWAYS exits 0. The checks stay warn-only, as AGENTS.md requires
#   (§"A warn-only commit hook ..."). Do not make this blocking.
#
# Each check script still runs standalone, as before.

set -u

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd)" || exit 0

payload="$(cat 2>/dev/null || true)"
cmd=""
if command -v jq >/dev/null 2>&1; then
  cmd="$(printf '%s' "$payload" | jq -r '.tool_input.command // empty' 2>/dev/null || true)"
elif command -v python3 >/dev/null 2>&1; then
  cmd="$(printf '%s' "$payload" | python3 -c \
    'import json,sys
try: print(json.load(sys.stdin).get("tool_input",{}).get("command",""))
except Exception: pass' 2>/dev/null || true)"
fi
[ -z "$cmd" ] && cmd="$payload"

# Fast path: no git, no branch-store -> nothing to check.
case "$cmd" in
  *git*|*branch-store*) ;;
  *) exit 0 ;;
esac

# Same separator discipline as the individual checks, so `echo git commit`
# and `# git commit later` do not count.
is_commit=0
printf '%s' "$cmd" | grep -qE '(^|[;&|(])[[:space:]]*git[[:space:]]+(-[^[:space:]]+[[:space:]]+)*commit([[:space:]]|$)' && is_commit=1

checks=()
if [ "$is_commit" = 1 ]; then
  checks+=(precommit-precision-warn.sh
           precommit-voice-ratchet-warn.sh
           precommit-ledger-shrink-warn.sh
           precommit-bootstrap-order-warn.sh
           precommit-tolerance-floor-warn.sh
           precommit-tolerance-tautology-warn.sh)
fi
case "$cmd" in
  *"git commit"*|*"git add"*|*"branch-store"*"push"*) checks+=(precommit-bean-id-warn.sh) ;;
esac
case "$cmd" in
  *"checkout -b"*|*"checkout -B"*|*"switch -c"*|*"switch -C"*) checks+=(prebranch-bean-loss-warn.sh) ;;
esac
[ "${#checks[@]}" -eq 0 ] && exit 0

tmp="$(mktemp -d 2>/dev/null)" || exit 0
trap 'rm -rf "$tmp"' EXIT INT TERM

for c in "${checks[@]}"; do
  [ -x "$here/$c" ] || continue
  case "$c" in
    precommit-bean-id-warn.sh|prebranch-bean-loss-warn.sh)
      # These two read the command from their arguments.
      ( "$here/$c" "$cmd" </dev/null >"$tmp/$c.out" 2>&1 ) & ;;
    precommit-ledger-shrink-warn.sh)
      # Hook mode is its default (no argument); it reads no stdin.
      ( "$here/$c" </dev/null >"$tmp/$c.out" 2>&1 ) & ;;
    *)
      ( printf '%s' "$payload" | "$here/$c" >"$tmp/$c.out" 2>&1 ) & ;;
  esac
done
wait

msg=""
for c in "${checks[@]}"; do
  f="$tmp/$c.out"
  [ -s "$f" ] || continue
  msg="${msg}${msg:+$'\n\n'}[${c%.sh}]"$'\n'"$(cat "$f")"
done
[ -z "$msg" ] && exit 0

if command -v jq >/dev/null 2>&1; then
  jq -cn --arg m "$msg" \
    '{systemMessage: $m,
      hookSpecificOutput: {hookEventName: "PreToolUse", additionalContext: $m}}' \
    2>/dev/null || true
elif command -v python3 >/dev/null 2>&1; then
  printf '%s' "$msg" | python3 -c \
    'import json,sys
m=sys.stdin.read()
print(json.dumps({"systemMessage":m,"hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":m}}))' \
    2>/dev/null || true
fi
exit 0
