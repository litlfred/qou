#!/usr/bin/env bash
# precommit-ledger-shrink-warn.sh — WARN (never block) when a commit would
# DELETE adjudicated verdicts from the shared vacuity ledger.
#
# WHY THIS EXISTS
# ---------------
# docs/audits/lean-vacuity-review-ledger.json is written by several agents at
# once and conflicts on essentially every concurrent branch. Resolving that
# conflict by taking a side silently destroys the other side's verdicts, and an
# agent verdict HAS NO PRODUCER: no script regenerates it, so a lost entry stays
# lost until someone re-reads the declaration.
#
# Measured cost, twice in one week:
#
#   2026-08-30  a rebase resolved by taking one side dropped 83 entries from
#               main — 78 proof-borrowed-name, 3 carrier-inhabited-by-probe,
#               1 no-provable-axiom, 1 no-self-assuming-projection; by verdict
#               50 legit, 21 advisory, 12 genuine. It sat on main ~2 hours and
#               surfaced only because an unrelated rebase happened to print a
#               union count that looked wrong.
#   earlier     a --review-ledger run deleted 116 of 268 entries. THAT one is
#               guarded, by content/pipeline/lean-vacuity-ledger-foreign-entries.test.ts.
#
# WHY THE EXISTING GUARD COULD NOT CATCH THE 83
# ---------------------------------------------
# That test protects foreign categories from --review-ledger's DELETE LOOP. The
# 83 went in a REBASE RESOLUTION. Same outcome, different mechanism — and 78 of
# them were in exactly the foreign category the test exists to protect. A guard
# aimed one hazard over is not a guard against this one.
#
# WHY WARN AND NOT BLOCK
# ----------------------
# Matches scripts/precommit-precision-warn.sh, whose header records the owner's
# 2026-08-25 choice: a PreToolUse hook exiting non-zero stops the tool call, and
# a deliberate deletion is legitimate (an entry whose declaration genuinely went
# away). Blocking makes the honest case impossible and the dishonest case merely
# annoying. This always exits 0 as a hook.
#
# For a hard gate — CI, or an agent that wants to fail — run it directly:
#     scripts/precommit-ledger-shrink-warn.sh --check    # 1 = shrink, 2 = did not run
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT" || exit 0
LEDGER="${LEDGER_OVERRIDE:-docs/audits/lean-vacuity-review-ledger.json}"
MODE="${1:-hook}"

if [ "$MODE" = "hook" ]; then
  git diff --cached --name-only 2>/dev/null | grep -qx "$LEDGER" || exit 0
  STAGED=$(git show :"$LEDGER" 2>/dev/null) || exit 0
else
  STAGED=$(cat "$LEDGER" 2>/dev/null) || exit 0
fi
BASE="${BASE_OVERRIDE_FILE:+$(cat "$BASE_OVERRIDE_FILE")}"
[ -n "$BASE" ] || BASE=$(git show HEAD:"$LEDGER" 2>/dev/null) || exit 0

# The ledger is ~1 MB. Passing it through the ENVIRONMENT hits E2BIG —
# `python3: Argument list too long` on stderr while the script still exits 0
# with an EMPTY result, i.e. the guard reports OK on a real shrink. Caught by
# this script's own selftest on its first run. Hence temp files.
TMPB=$(mktemp) && TMPS=$(mktemp) || exit 0
trap 'rm -f "$TMPB" "$TMPS"' EXIT INT TERM
printf '%s' "$BASE"   > "$TMPB"
printf '%s' "$STAGED" > "$TMPS"

RESULT=$(python3 "$ROOT/scripts/lib/ledger_shrink_check.py" "$TMPB" "$TMPS" 2>/dev/null)

# An EMPTY result means the comparison did not run (E2BIG, missing python3, a
# crash). Silence must never read as "no shrink" — that is the exact failure
# this script exists to prevent, and the one it hit first.
if [ -z "$RESULT" ]; then
  echo "  ⚠  ledger-shrink guard DID NOT RUN (empty result) — treat as UNCHECKED" >&2
  [ "$MODE" = "--check" ] && exit 2
  exit 0
fi

case "$RESULT" in
  SHRINK*)
    {
      echo ""
      echo "  ⚠  VACUITY LEDGER WOULD LOSE VERDICTS"
      echo "$RESULT" | sed "s/^/     /"
      echo ""
      echo "     An agent verdict has NO PRODUCER — nothing regenerates it. If this"
      echo "     is a conflict resolution, resolve by UNION instead:"
      echo "         python3 scripts/resolve-vacuity-ledger-conflict.py"
      echo "     If the deletion is deliberate (the declaration is genuinely gone),"
      echo "     say so in the commit message and carry on — this never blocks."
      echo ""
    } >&2
    [ "$MODE" = "--check" ] && exit 1
    ;;
  *)
    [ "$MODE" = "--check" ] && echo "ledger-shrink: $RESULT"
    ;;
esac
exit 0
