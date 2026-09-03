#!/usr/bin/env bash
# precommit-precision-warn.sh — WARN (never block) when a commit would add raw
# float64 to a witness.
#
# WHY THIS EXISTS
# ---------------
# scripts/precision-gates.sh is documented as THE gate: CI is workflow_dispatch-
# only under the 2026-06-30 Actions-billing directive, reaffirmed by the owner on
# 2026-08-09 with the failure cost on the table. But nothing ever RAN it —
# core.hooksPath was unset, there was no .githooks/, and the only references in
# the tree were prose. A gate nobody invokes is documentation.
#
# The cost of that: beans qou-mnrd and qou-82ur both landed on the same finding
# from opposite directions. Dirty witnesses reach main, get drained, and are
# replaced by different dirty witnesses — a revolving door — because each one
# lands the same way the last did, unexamined.
#
# WHY ONLY THE RATCHET, NOT THE WHOLE FAMILY
# ------------------------------------------
# Measured 2026-08-25 on this corpus (2759 witnesses):
#
#     witness_raw_float64_audit.py --strict   1.8 s
#     scripts/precision-gates.sh (all gates)  3 m 12 s
#
# A PreToolUse hook runs BEFORE the tool call, so wiring the full family here
# would add three minutes to every witness-touching commit. That does not buy
# safety, it buys avoidance: an agent that finds committing slow commits less
# often and in bigger lumps. So this hook runs the ONE BLOCKING gate and names
# the full script for everything else. The advisory gates (f64-into-mpmath,
# provenance, no-free-parameter) are deliberately NOT run here.
#
# WARN-ONLY IS DELIBERATE (owner decision, 2026-08-25)
# ----------------------------------------------------
# This script ALWAYS exits 0. A PreToolUse hook that exits non-zero blocks the
# tool call, and a bare container is the DEFAULT here — mpmath/numpy/scipy are
# routinely absent on a fresh clone, which is exactly when a blocking hook would
# brick every commit in the session. The owner chose warn-on-commit and declined
# the push-side block; do not "upgrade" this to blocking without asking again.
set -u

payload="$(cat 2>/dev/null || true)"

cmd=""
if command -v jq >/dev/null 2>&1; then
  cmd="$(printf '%s' "$payload" | jq -r '.tool_input.command // empty' 2>/dev/null || true)"
fi
[ -z "$cmd" ] && cmd="$payload"

# Only speak on a real commit. `git commit` inside a longer compound command
# still counts -- that is how most agent commits are actually written.
# `git commit` must start the command or follow a real separator (; & | && ||
# or a newline -- grep is line-oriented, so ^ covers newline). Plain whitespace
# is NOT a separator: `echo git commit` and `# run git commit later` mention the
# words without committing anything, and firing a RED banner on those would
# train readers to ignore the banner.
printf '%s' "$cmd" | grep -qE '(^|[;&|])[[:space:]]*git[[:space:]]+(-[^[:space:]]+[[:space:]]+)*commit([[:space:]]|$)' || exit 0

cd "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || exit 0

# Relevance: staged, plus already-committed-but-unpushed is NOT this hook's
# business -- the commit at hand is. `git commit -a` stages at commit time, so
# consider unstaged tracked changes too.
relevant="$( { git diff --cached --name-only; git diff --name-only; } 2>/dev/null \
  | grep -E '(\.witness\.json$|^computations/.*\.py$)' | sort -u )"
[ -z "$relevant" ] && exit 0

audit="computations/witness_raw_float64_audit.py"
[ -f "$audit" ] || exit 0

export PYTHONPATH="$PWD/computations:$PWD/tools/qou-substrate/python:${PYTHONPATH:-}"

# THE AUDIT WRITES ITS OWN WITNESS, and this hook must not.
#
# witness_raw_float64_audit.py has no --no-write, so running it rewrites the
# tracked computations/witness-raw-float64-audit.witness.json -- on EVERY commit
# that touches a witness or a computations/*.py, which is precisely when this
# hook fires. The rewrite is almost always stamp-only (commitSha, computedAt);
# the counts move only when the corpus does.
#
# That is a warn-only hook silently dirtying the working tree, and the cost is
# on the record twice on one branch: the file was swept into a `git add -A`,
# reverted when caught, and swept in again one commit later. It then conflicts
# with main every time, because main regenerates the same file from a different
# tree -- two snapshots of different corpora, neither more current than the
# other.
#
# So: snapshot before, restore after. ONLY when the file is clean going in --
# an agent deliberately refreshing this witness has a modified copy staged or
# unstaged, and that copy is theirs to keep.
_w="computations/witness-raw-float64-audit.witness.json"
_snap=""
if [ -f "$_w" ] && git diff --quiet -- "$_w" 2>/dev/null \
   && git diff --cached --quiet -- "$_w" 2>/dev/null; then
  _snap="$(mktemp)"
  cp "$_w" "$_snap"
fi

out="$(timeout 120 python3 "$audit" --strict 2>&1)"; rc=$?

if [ -n "$_snap" ]; then
  cp "$_snap" "$_w"
  rm -f "$_snap"
fi

case "$rc" in
  0) : ;;  # green -- say nothing, the commit is the signal
  124)
    echo "precision-warn: raw-float64 ratchet timed out (>120s); not evaluated."
    echo "                Run scripts/precision-gates.sh by hand before pushing."
    ;;
  *)
    if printf '%s' "$out" | grep -q "ModuleNotFoundError\|No module named"; then
      echo "precision-warn: could not evaluate -- missing Python module(s)."
      echo "                This is NOT a gate failure: nothing was examined, so"
      echo "                nothing is known about this commit. pip install mpmath,"
      echo "                then run scripts/precision-gates.sh."
    else
      echo "=============================================================="
      echo "precision-warn: RAW-FLOAT64 RATCHET IS RED for this commit."
      echo "=============================================================="
      # Only the NEW-dirty section. A bare `^ +N +computations/` grep also
      # matches the DECLARED CARVE-OUT listings (float64-integrator,
      # deprecated-f64, LP-dual), which are not defects -- printing those
      # above the real offender is how a warning gets learned as noise.
      printf '%s\n' "$out" | grep -E "NEW dirty witnesses|REGRESSED \\(count"
      printf '%s\n' "$out" | awk '
        /NEW witnesses carrying raw float64/ { show=1; next }
        show && /^[[:space:]]*$/             { if (seen) exit; next }
        show && /^[[:space:]]+[0-9]+[[:space:]]+computations\//  { print; seen=1 }
      ' | head -15
      echo
      echo "  Fix AT THE PRODUCER: carry mpmath.mpf from the source and"
      echo "  serialize with _precision.fmt. Do NOT add the file to"
      echo "  raw-float64-baseline.json, do NOT --rebaseline, and do NOT"
      echo "  hand-edit a number. Baselines drain, never grow."
      echo
      echo "  This is a WARNING; your commit is proceeding. The full gate"
      echo "  family (~3 min) is scripts/precision-gates.sh."
      echo "=============================================================="
    fi
    ;;
esac

exit 0
