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
# That is correct for CODE and destructive for `beans/defs/`. A bean committed on the
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
# landed two files and no `beans/defs/` at all, because there was nothing left to
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
  added=$(git diff --name-only --diff-filter=A "$base...HEAD" -- beans/defs/ 2>/dev/null)
  modified=$(git diff --name-only --diff-filter=M "$base...HEAD" -- beans/defs/ 2>/dev/null)
  [ -n "$added$modified" ] || return 0
  echo "── prebranch-bean-loss-warn ───────────────────────────────────────────"
  echo "Creating a branch from '$base' will change beans/defs/ in the worktree."
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
  echo "      git checkout $(git rev-parse --short HEAD) -- beans/defs/"
  echo "───────────────────────────────────────────────────────────────────────"
}

# --- the matcher, as a pure function of the command string -------------------
# Prints the base ref of a REAL branch-creation invocation, or nothing.
#
# MATCH AT A COMMAND POSITION, not anywhere in the string. A substring test fires
# on a command that merely QUOTES the invocation — measured: `git commit -m
# 'docs: explains git checkout -b claude/foo origin/main'` warned, and the commit
# documenting THIS GUARD is exactly such a message. A guard that cries on the
# commit describing it is noise, and noise is what gets guards ignored.
#
# So: split on command separators, then require the fragment to BEGIN with
# `git checkout|switch`. A quoted mention sits mid-fragment and is skipped.
base_ref() {
  printf '%s\n' "$1" \
    | sed -E 's/(\|\||&&|[;|]|`|\$\()/\n/g' \
    | sed -E 's/^[[:space:]]+//' \
    | grep -E '^git[[:space:]]+(checkout[[:space:]]+-[bB]|switch[[:space:]]+-[cC])[[:space:]]' \
    | grep -oE '(checkout[[:space:]]+-[bB]|switch[[:space:]]+-[cC])[[:space:]]+[^[:space:]]+[[:space:]]+[^[:space:]]+' \
    | head -1 | awk '{print $NF}'
}

# --- selftest ----------------------------------------------------------------
if [ "${1:-}" = "--selftest" ]; then
  echo "SELFTEST — does it fire on a real bean loss, and stay quiet otherwise?"
  tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT INT TERM
  (
    cd "$tmp" || exit 1
    git init -q .; git config user.email t@t; git config user.name t
    mkdir -p beans/defs; echo base > beans/defs/keep.md
    git add -A; git commit -qm base
    git branch base-ref
    # a branch that ADDS one bean and MODIFIES another
    git checkout -q -b work
    echo new > beans/defs/new-bean.md; echo changed > beans/defs/keep.md
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
  # --- the MATCHER, which bean_delta tests do not touch ---------------------
  # Each row: expected base ("-" = must not fire) then the command string.
  echo
  echo "  matcher (expected | got):"
  while IFS='|' read -r want cmd; do
    [ -n "$want" ] || continue
    got=$(base_ref "$cmd"); got=${got:--}
    if [ "$got" = "$want" ]; then mark="  ok"; else mark="FAIL"; ok=0; fi
    printf "    %s  %-12s %-12s %s\n" "$mark" "$want" "$got" "$(echo "$cmd" | cut -c1-58)"
  done <<'ROWS'
origin/main|git checkout -B claude/foo origin/main
origin/main|git checkout -b claude/foo origin/main
origin/main|git switch -C claude/foo origin/main
origin/main|git fetch -q origin main && git checkout -b claude/foo origin/main
-|git checkout -b claude/foo
-|git commit -m 'docs: explains git checkout -b claude/foo origin/main and why'
-|grep -rn "git checkout -b claude/x origin/main" docs/
-|echo "run git switch -c claude/y origin/main first"
-|git commit -m x
ROWS

  echo
  [ "$ok" = 1 ] && { echo "  PASS"; exit 0; }
  echo "  FAIL — do not trust this guard."; exit 1
fi

# --- hook path ----------------------------------------------------------------
CMD="${*:-}"

# Cheap pre-filter before any git work.
case "$CMD" in
  *"checkout -b"*|*"checkout -B"*|*"switch -c"*|*"switch -C"*) ;;
  *) exit 0 ;;
esac

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
cd "$ROOT" || exit 0
[ -d beans/defs ] || exit 0

BASE=$(base_ref "$CMD")
[ -n "$BASE" ] || exit 0

# A ref that does not resolve is not a base we can reason about (a placeholder
# like `origin/<default>` in prose, or a trailing quote from a mention).
git rev-parse --verify --quiet "$BASE" >/dev/null 2>&1 || exit 0

bean_delta "$BASE"
exit 0
