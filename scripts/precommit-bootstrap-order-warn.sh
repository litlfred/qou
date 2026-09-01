#!/usr/bin/env bash
# precommit-bootstrap-order-warn.sh — WARN (never block) when a commit adds a
# `computations/` script that cannot be run standalone.
#
# WHY THIS EXISTS
# ---------------
# `computations/audits/path_bridge_bootstrap_audit.py` is a correct guard for a
# real defect class: a bare-name import (`_path_bridge`, `q_parameter`,
# `_precision`, `hoefsmit_symbolic`, ...) placed BEFORE the sys.path bootstrap
# that resolves it. A script in a cluster subdirectory has sys.path[0] set to
# its own directory, so such an import raises ModuleNotFoundError and the file
# cannot be executed at all.
#
# Nothing invoked that guard. Measured 2026-08-30: bean qou-0e1t drained six
# instances, and SIX MORE landed on main within days -- a disjoint set, every
# one committed the same day, all from one thematic cluster. The guard reported
# all six the moment it was run by hand. A guard nobody invokes is
# documentation; that is the same finding AGENTS.md records for
# precision-gates.sh before it got a commit hook, and this script is the same
# remedy for the same shape.
#
# WHY IT IS INVISIBLE WITHOUT A HOOK
# ----------------------------------
# The failure is SILENT in normal agent use. A shell that already exports
# PYTHONPATH, or a caller that imports the module rather than executing it,
# masks it completely -- so a probe can be written, run, and report n/n passing
# while being unrunnable on a fresh clone. Two of the instances even DOCUMENTED
# a `PYTHONPATH=... python3 ...` invocation in their docstring, which is the
# masking written down as an interface.
#
# WHY --files, NOT A FULL SWEEP
# -----------------------------
# Measured on this corpus: a whole-tree sweep is ~30 s (it EXECUTES each
# candidate, which is what makes its verdicts trustworthy), while scoping to
# the files a commit touches is ~0.8 s. A PreToolUse hook runs before the tool
# call, so 30 s on every commit would buy avoidance rather than safety --
# the same reasoning that keeps precommit-precision-warn.sh to one gate.
#
# WARN-ONLY IS DELIBERATE
# -----------------------
# This script ALWAYS exits 0, matching precommit-precision-warn.sh. A
# PreToolUse hook that exits non-zero blocks the tool call, and the audit
# EXECUTES candidate scripts -- which can fail for reasons that are not this
# defect (a missing optional dependency, a bare container). Blocking on that
# would brick commits for an environment fact. The owner declined a push-side
# block for the precision family on 2026-08-25; do not "upgrade" this one
# without asking either.
set -u

payload="$(cat 2>/dev/null || true)"

cmd=""
if command -v jq >/dev/null 2>&1; then
  cmd="$(printf '%s' "$payload" | jq -r '.tool_input.command // empty' 2>/dev/null || true)"
fi
[ -z "$cmd" ] && cmd="$payload"

# Only speak on a real commit; same separator discipline as the precision hook,
# so `echo git commit` and `# run git commit later` do not fire a banner.
printf '%s' "$cmd" | grep -qE '(^|[;&|])[[:space:]]*git[[:space:]]+(-[^[:space:]]+[[:space:]]+)*commit([[:space:]]|$)' || exit 0

cd "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || exit 0

# `git commit -a` stages at commit time, so unstaged tracked changes count too.
# Only files in a cluster SUBDIRECTORY can carry this defect: a script directly
# in computations/ has its imports as siblings on sys.path[0].
relevant="$( { git diff --cached --name-only; git diff --name-only; } 2>/dev/null \
  | grep -E '^computations/[^/]+/.*\.py$' \
  | grep -v '^computations/_deprecated/' | sort -u )"
[ -z "$relevant" ] && exit 0

audit="computations/audits/path_bridge_bootstrap_audit.py"
[ -f "$audit" ] || exit 0

# The audit writes no witness and mutates nothing, so unlike the precision hook
# there is no snapshot/restore dance here. It does EXECUTE the candidates,
# which can write THEIR witnesses -- but only for a file this commit is already
# touching, and only one that cannot currently run.
# shellcheck disable=SC2086
out="$(timeout 110 python3 "$audit" --files $relevant 2>&1)"; rc=$?

case "$rc" in
  0) : ;;  # clean -- say nothing, the commit is the signal
  124)
    echo "bootstrap-order-warn: audit timed out (>110s); not evaluated."
    echo "                      Run: python3 $audit"
    ;;
  *)
    if printf '%s' "$out" | grep -q "CONFIRMED broken (by run) : 0"; then
      : ;  # non-zero for some other reason and nothing was confirmed; stay quiet
    else
      echo "=============================================================="
      echo "bootstrap-order-warn: a file in this commit CANNOT RUN STANDALONE."
      echo "=============================================================="
      printf '%s\n' "$out"
      echo
      echo "  Confirmed by EXECUTION with PYTHONPATH stripped, not by pattern."
      echo "  Fix (per computations/_path_bridge.py's documented USAGE):"
      echo
      echo "    import sys as _sys, pathlib as _pl  # noqa: E402"
      echo "    _sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))"
      echo "    import _path_bridge  # noqa: F401, E402"
      echo
      echo "  placed BEFORE the first bare-name import. Beans qou-0e1t, qou-cds2."
    fi
    ;;
esac

exit 0
