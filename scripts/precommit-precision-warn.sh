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
# `git ls-files --others` is load-bearing, not belt-and-braces: a BRAND-NEW
# witness that has not been `git add`ed yet appears in NEITHER `git diff` nor
# `git diff --cached`, so without it this early exit fires and the hook never
# examines the one case it most wants to see. Measured 2026-09-03 while adding
# the q0-anchor ratchet below: the new-file test case produced no warning at
# all, and the cause was here rather than in the new code.
relevant="$( { git diff --cached --name-only; git diff --name-only; \
               git ls-files --others --exclude-standard; } 2>/dev/null \
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

out="$(timeout 120 python3 "$audit" --strict --no-write 2>&1)"; rc=$?

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

# ── q0 ANCHOR RATCHET (added 2026-09-03) ──────────────────────────────────────
#
# AGENTS.md: "Say which pin you used. Any new witness must record its q0 so a
# later reader can tell which layer it belongs to." Nothing enforced it, and the
# refill ratchet went NEW 0 -> 147 in the five days after it was last drained to
# zero (measured 2026-09-03 on d502ed06ce9; ~29/day, still arriving).
#
# WHY THIS IS A RATCHET, NOT AN AUDIT. 1,663 witnesses on main carry no
# q0Anchor. Warning whenever a commit touches one of those would fire on a
# pre-existing condition the committer did not cause -- which this file's own
# comments already identify as how a warning gets learned as noise. So it speaks
# ONLY on:
#
#   NEW       a witness not present in HEAD, committed without a q0Anchor
#   REGRESSED a witness that HAD one in HEAD and does not now
#
# Measured against the live refill: ALL 150 of the currently-flagged witnesses
# did not exist at a788e78ce2b, i.e. every one is a NEW-file case this catches.
# (A first pass at that measurement reported 0 of 150 -- `git log --format=A` is
# an invalid pretty format, it failed on every file, and stderr was discarded.
# A command that fails silently on every input returns a clean, plausible,
# completely wrong answer. The check below shells out to nothing.)
#
# COST: pure stdlib JSON over the handful of witnesses in the commit. No corpus
# walk, no producer run, no witness written -- so nothing to snapshot/restore.
# Warn-only and exit 0, exactly as above; do not upgrade to blocking.

q0_relevant="$( { git diff --cached --name-only; git diff --name-only; \
                  git ls-files --others --exclude-standard; } 2>/dev/null \
  | grep -E '\.witness\.json$' | sort -u )"

if [ -n "$q0_relevant" ] && command -v python3 >/dev/null 2>&1; then
  q0_out="$(printf '%s\n' "$q0_relevant" | python3 -c '
import json, subprocess, sys

def anchored(text):
    try:
        return bool(json.loads(text).get("q0Anchor"))
    except Exception:
        return None          # unparseable -> say nothing, not this hook is job

new, regressed = [], []
for path in (l.strip() for l in sys.stdin if l.strip()):
    try:
        cur = anchored(open(path, encoding="utf-8").read())
    except OSError:
        continue             # deleted in this commit
    if cur is not False:
        continue             # has one, or unparseable
    head = subprocess.run(["git", "show", f"HEAD:{path}"],
                          capture_output=True, text=True)
    if head.returncode != 0:
        new.append(path)                     # not in HEAD at all
    elif anchored(head.stdout) is True:
        regressed.append(path)               # had one, lost it

for label, group in (("NEW", new), ("REGRESSED", regressed)):
    for p in group[:10]:
        print(f"  {label:9s} {p}")
    if len(group) > 10:
        print(f"  {label:9s} ... and {len(group) - 10} more")
' 2>/dev/null)"

  if [ -n "$q0_out" ]; then
    echo "=============================================================="
    echo "precision-warn: WITNESS COMMITTED WITHOUT A q0Anchor."
    echo "=============================================================="
    printf '%s\n' "$q0_out"
    echo
    echo "  Declare the pin at the PRODUCER, in the save call:"
    echo "      w.save({\"q0Anchor\": \"proton\", \"q0Value\": mp.nstr(Q, 50)})"
    echo "  or, for a computation with no substrate pin at all:"
    echo "      w.save({\"q0Anchor\": \"independent\", \"q0AnchorReason\": \"...\"})"
    echo
    echo "  \"independent\" is producer-declared only and needs a REASON."
    echo "  Do NOT stamp \"proton\" to silence this -- that asserts a pin the"
    echo "  computation may not have, which is the failure q0Anchor exists to"
    echo "  prevent. Do NOT add the file to q0-anchor-missing-baseline.json."
    echo
    echo "  This is a WARNING; your commit is proceeding."
    echo "=============================================================="
  fi
fi

exit 0
