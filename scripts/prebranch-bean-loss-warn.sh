#!/usr/bin/env bash
# prebranch-bean-loss-warn.sh — WARN (never block) when creating a branch from a
# new base would silently remove beans that exist only on the current branch.
#
# WHY THIS EXISTS (bean qou-keu7)
# -------------------------------
# AGENTS.md's merged-PR rule says to restart the designated branch from the
# latest default branch:
#
#     git checkout -B <branch> origin/<default>
#
# That is correct for CODE and destructive for `.beans/`. A bean committed on the
# old branch but not merged is a TRACKED file absent from the new base, so the
# checkout DELETES it from the worktree — with no warning, and `git status`
# afterwards is CLEAN, which is exactly what makes it invisible.
#
# Measured cost, 2026-08-30: two beans erased. `qou-jr5r` stayed on main as an
# open high-priority bug report for a defect that does not exist, with its
# retraction stranded on the unmerged branch; `qou-s3zd` vanished entirely while
# a merged PR's body and commit message went on citing it.
#
# `git add -A` IS NOT A SAFETY NET. It stages what is in the worktree and says
# nothing about what the worktree lost — the next commit after that incident
# landed two files and no `.beans/` at all, because there was nothing left to
# stage.
#
# WHY WARN AND NEVER BLOCK
# ------------------------
# A PreToolUse hook exiting non-zero stops the tool call. Following the posture
# the owner chose for the precision hook on 2026-08-25 (warn-on-commit; a
# push-side block was offered and declined), this ALWAYS exits 0. Do not upgrade
# it to blocking without asking. Creating a branch from a fresh base is usually
# right — the point is to say what it is about to cost, not to prevent it.
#
# WHY IT LOOKS AT `-b` AS WELL AS `-B`
# ------------------------------------
# The bean names `checkout -B`, but `-B` is not what does the damage: moving the
# worktree to a commit that lacks files the current HEAD has, is. Plain
# `git checkout -b <new> origin/main` from a branch carrying unmerged beans loses
# them the same way. Both forms are matched; a branch created with no explicit
# base cannot lose anything and is ignored.
#
# Usage:  prebranch-bean-loss-warn.sh "<the tool call's command string>"
#         prebranch-bean-loss-warn.sh --selftest
set -uo pipefail

# --- the check, as a pure function of (base ref) -----------------------------
# Prints the beans that would be lost or reverted. Empty output = nothing to say.
bean_delta() {  # $1 = base ref
  local base="$1"
  git rev-parse --verify --quiet "$base" >/dev/null 2>&1 || return 0
  local added modified
  added=$(git diff --name-only --diff-filter=A "$base...HEAD" -- .beans/ 2>/dev/null)
  modified=$(git diff --name-only --diff-filter=M "$base...HEAD" -- .beans/ 2>/dev/null)
  [ -n "$added$modified" ] || return 0
  echo "── prebranch-bean-loss-warn ───────────────────────────────────────────"
  echo "Creating a branch from '$base' will change .beans/ in the worktree."
  if [ -n "$added" ]; then
    echo
    echo "  WOULD VANISH (exist only on this branch — $(echo "$added" | grep -c .)):"
    echo "$added" | sed 's/^/    /'
  fi
  if [ -n "$modified" ]; then
    echo
    echo "  WOULD REVERT to the base's version ($(echo "$modified" | grep -c .)):"
    echo "$modified" | sed 's/^/    /'
  fi
  echo
  echo "  If those are pushed, they are safe on the remote but ABSENT from the"
  echo "  new worktree — and \`git add -A\` cannot re-add what the checkout removed."
  echo "  Recover onto the new branch with:"
  echo "      git checkout $(git rev-parse --short HEAD) -- .beans/"
  echo "───────────────────────────────────────────────────────────────────────"
}

# --- selftest ----------------------------------------------------------------
if [ "${1:-}" = "--selftest" ]; then
  echo "SELFTEST — does it fire on a real bean loss, and stay quiet otherwise?"
  tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT INT TERM
  (
    cd "$tmp" || exit 1
    git init -q .; git config user.email t@t; git config user.name t
    mkdir -p .beans; echo base > .beans/keep.md
    git add -A; git commit -qm base
    git branch base-ref
    # a branch that ADDS one bean and MODIFIES another
    git checkout -q -b work
    echo new > .beans/new-bean.md; echo changed > .beans/keep.md
    git add -A; git commit -qm "bean work"
  ) >/dev/null 2>&1
  ok=1
  out=$(cd "$tmp" && bean_delta base-ref)
  echo "$out" | grep -q "new-bean.md" && echo "  added bean detected      -> YES" || { echo "  added bean detected      -> NO"; ok=0; }
  echo "$out" | grep -q "WOULD REVERT" && echo "  modified bean detected   -> YES" || { echo "  modified bean detected   -> NO"; ok=0; }
  # and it must be SILENT when the branch carries no bean work
  (cd "$tmp" && git checkout -q base-ref) >/dev/null 2>&1
  quiet=$(cd "$tmp" && bean_delta base-ref)
  [ -z "$quiet" ] && echo "  silent with nothing new  -> YES" || { echo "  silent with nothing new  -> NO"; ok=0; }
  # a nonexistent base must not error
  noisy=$(cd "$tmp" && bean_delta refs/heads/does-not-exist)
  [ -z "$noisy" ] && echo "  unknown base is silent   -> YES" || { echo "  unknown base is silent   -> NO"; ok=0; }
  echo
  [ "$ok" = 1 ] && { echo "  PASS"; exit 0; }
  echo "  FAIL — do not trust this guard."; exit 1
fi

# --- hook path ---------------------------------------------------------------
CMD="${*:-}"

# Only speak for a branch CREATION that names an explicit base.
case "$CMD" in
  *"checkout -b "*|*"checkout -B "*|*"switch -c "*|*"switch -C "*) ;;
  *) exit 0 ;;
esac

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
cd "$ROOT" || exit 0
[ -d .beans ] || exit 0

# Extract the base ref: the token AFTER the new branch name. No base ⇒ branches
# from HEAD ⇒ nothing can be lost.
BASE=$(printf '%s\n' "$CMD" \
  | grep -oE '(checkout -[bB]|switch -[cC])[[:space:]]+[^[:space:]]+[[:space:]]+[^[:space:]]+' \
  | head -1 | awk '{print $NF}')
[ -n "$BASE" ] || exit 0

bean_delta "$BASE"
exit 0
