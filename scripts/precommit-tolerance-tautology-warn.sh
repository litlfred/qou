#!/usr/bin/env bash
# precommit-tolerance-tautology-warn.sh — WARN (never block) when a commit adds
# an assertion that CANNOT FAIL.
#
# WHY
# ---
# `Assertion.passed` is `|computed - expected| <= tolerance`. Three shapes make
# that inequality hold for every possible input, so the assertion records
# `passed: true` having tested nothing:
#
#   identical-after-substitution  computed and expected are one expression once
#                                 single-assignment names are substituted, so
#                                 the residual is identically 0.
#   triangle-bound                tolerance is k*max(|c|,|e|) with k>=2, or
#                                 k*(|c|+|e|) with k>=1, or k*|c-e| with k>=1.
#                                 True by the triangle inequality, always.
#   residual-named                the tolerance's residual-named quantity
#                                 resolves, through assignments, to a
#                                 SUBTRACTION of both sides.
#
# The first two are proofs about arithmetic, not heuristics.
#
# THE MIRROR OF precommit-tolerance-floor-warn.sh. That one asks whether a
# tolerance is too SMALL for the arithmetic to reach. This asks whether it is
# so LARGE the check is vacuous. Six existing assertion audits catch neither:
# they compare `computed` to `expected`, and here those two differ, correctly.
#
# Measured 2026-09-05 (bean qou-t0wm): seven such assertions live on main,
# across six producers. One of them recorded a 121 % miss as `passed: true` —
# kappa 0.1875 against an expected -0.9160, opposite signs.
#
# WHY --files
# -----------
# Whole-tree is 22.1 s (every .py under computations/, scripts/, tools/ parsed);
# the files one commit touches is 0.07 s. A PreToolUse hook runs BEFORE the tool
# call, so that is 22 seconds added to every commit versus none. Same reasoning
# as precommit-tolerance-floor-warn.sh and precommit-bootstrap-order-warn.sh.
#
# WARN-ONLY, ALWAYS EXITS 0
# -------------------------
# Matches the four sibling precommit-*-warn.sh. A PreToolUse hook exiting
# non-zero blocks the tool call; the owner chose warn-on-commit on 2026-08-25
# and declined a push-side block. Do not upgrade without asking.
#
# This one cannot brick a bare container even in principle: the audit imports
# only `ast`, `argparse`, `json`, `re`, `sys` and `pathlib` — no mpmath, no
# numpy, no scipy.
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
  | grep -E '^(computations|scripts|tools)/.*\.py$' \
  | grep -v '^computations/_deprecated/' | sort -u )"
[ -z "$relevant" ] && exit 0

audit="computations/audits/tolerance_from_residual_audit.py"
[ -f "$audit" ] || exit 0

# Exit code alone is the signal: the audit exits 1 on a BLOCKING hit and 0
# otherwise. The `review` tier is deliberately NOT warned on — measured
# 0-for-4 precision on main (a 2-sigma CODATA error bar, two residual-vs-zero
# checks under fixed tolerances, and one deliberate error-vs-error comparison).
# shellcheck disable=SC2086
out="$(timeout 60 python3 "$audit" --files $relevant 2>&1)"; rc=$?

case "$rc" in
  0) : ;;  # clean -- say nothing
  124)
    echo "tolerance-tautology-warn: audit timed out; not evaluated. Run: python3 $audit"
    ;;
  1)
    echo "=============================================================="
    echo "tolerance-tautology-warn: an assertion in this commit CANNOT"
    echo "FAIL. It will record passed:true whatever the code computes."
    echo "=============================================================="
    printf '%s\n' "$out" | sed -n '/^== blocking/,/^== review/p' | sed '$d'
    echo "  The fix is at the ASSERTION, never at the detector. Give it an"
    echo "  INDEPENDENT expected value -- often the producer's own \`source\`"
    echo "  field already names the checkable claim. If the honest result is"
    echo "  a failing assertion, let it fail: AGENTS.md asks for the negative."
    echo "  Bean qou-t0wm; docs/audits/2026-09-05-tolerance-that-bounds-its-own-residual.md"
    ;;
  *)
    echo "tolerance-tautology-warn: audit exited $rc; not evaluated."
    ;;
esac

exit 0
