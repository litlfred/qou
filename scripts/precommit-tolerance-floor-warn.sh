#!/usr/bin/env bash
# precommit-tolerance-floor-warn.sh — WARN (never block) when a commit adds an
# assertion whose tolerance is finer than the arithmetic that produced it.
#
# WHY
# ---
# `computed=float(x), tolerance=1e-40` cannot mean what it says: IEEE double
# resolves ~2.2e-16, so the assertion is either trivially true (the cast is
# exactly 0.0, measuring nothing) or must fail. It can never mean "verified to
# 1e-40" — and in a witness that is exactly how it reads.
#
# Measured 2026-08-30: 61 such assertions across 38 files. The class grew
# unnoticed because no audit compared the TOLERANCE against the RESOLUTION of
# the type the value is carried in.
#
# WHY --files
# -----------
# Whole-tree is ~9.7 s (3490 files AST-parsed); the files one commit touches is
# ~38 ms. A PreToolUse hook runs BEFORE the tool call, so that difference is
# seconds on every commit versus none. Same reasoning as
# precommit-bootstrap-order-warn.sh.
#
# WARN-ONLY, ALWAYS EXITS 0
# -------------------------
# Matches the three sibling precommit-*-warn.sh. A PreToolUse hook exiting
# non-zero blocks the tool call; the owner chose warn-on-commit on 2026-08-25
# and declined a push-side block. Do not upgrade without asking.
set -u

payload="$(cat 2>/dev/null || true)"

cmd=""
if command -v jq >/dev/null 2>&1; then
  cmd="$(printf '%s' "$payload" | jq -r '.tool_input.command // empty' 2>/dev/null || true)"
fi
[ -z "$cmd" ] && cmd="$payload"

# Same separator discipline as the sibling hooks, so `echo git commit` and
# `# run git commit later` do not fire a banner.
printf '%s' "$cmd" | grep -qE '(^|[;&|])[[:space:]]*git[[:space:]]+(-[^[:space:]]+[[:space:]]+)*commit([[:space:]]|$)' || exit 0

cd "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || exit 0

# `git commit -a` stages at commit time, so unstaged tracked changes count too.
relevant="$( { git diff --cached --name-only; git diff --name-only; } 2>/dev/null \
  | grep -E '^computations/.*\.py$' | grep -v '^computations/_deprecated/' | sort -u )"
[ -z "$relevant" ] && exit 0

audit="computations/audits/tolerance_below_arithmetic_floor_audit.py"
[ -f "$audit" ] || exit 0

# shellcheck disable=SC2086
out="$(timeout 60 python3 "$audit" --files $relevant 2>&1)"; rc=$?

case "$rc" in
  0) : ;;  # clean -- say nothing
  124)
    echo "tolerance-floor-warn: audit timed out; not evaluated. Run: python3 $audit"
    ;;
  *)
    if printf '%s' "$out" | grep -q "flagged assertions        : 0"; then
      : ;  # non-zero for another reason and nothing flagged; stay quiet
    else
      echo "=============================================================="
      echo "tolerance-floor-warn: an assertion in this commit claims a"
      echo "tolerance its own arithmetic cannot support."
      echo "=============================================================="
      printf '%s\n' "$out"
      echo
      echo "  float64 resolves ~2.2e-16. A tighter tolerance on a float()-cast"
      echo "  value is either trivially true or must fail -- it can never mean"
      echo "  what it says, and a witness records it as if it did."
      echo
      echo "  Usual fix is one token: drop the float(). The value is already"
      echo "  mpf at most of these sites, so \`computed=x\` makes the assertion"
      echo "  mean what it claims. Bean qou-58zw."
    fi
    ;;
esac

exit 0
