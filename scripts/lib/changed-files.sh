#!/usr/bin/env bash
# Shared changed-file collection — SOURCE this, do not execute.
#
#   Defines:  changed_files_base()   the merge-base to diff against, or ""
#             changed_files()        one path per line, deduplicated
#   Reads:    CHANGED_FILES_BASE_REF   override the upstream ref (default origin/main)
#   Warns on: an unresolvable base, every call — see "THE SILENT NARROWING"
#
# WHY THIS EXISTS (bean qou-pt9b)
# ------------------------------
# Four scripts in this repo compute "what did this change touch", and on
# 2026-08-22 ALL FOUR were measured collecting something narrower than the
# branch:
#
#   precision-gates.sh      working tree only   false all-clear after a commit
#   check-sidecars.sh       working tree only   same -- and it is the Phase-4
#                                               merge gate, where the changes
#                                               are ALWAYS committed
#   staleness-gates.sh      working tree only   same
#   lean-verify-changed.sh  HEAD~1              verified the last commit only
#
# They were written at different times by different agents, and each one
# independently reached for the same idiom. That is not four mistakes; it is a
# default that looks right as you type it and is wrong given AGENTS.md rule 3
# (one commit per logically distinct change) and rule 0 (commit early, commit
# often). The fifth gate script will reach for it too, which is the argument
# for one definition rather than four.
#
# Measured under-coverage for the Lean one across six live sibling branches,
# HEAD~1 vs merge-base: 0 vs 26, 3 vs 9, 2 vs 9, 2 vs 9, 0 vs 1, 0 vs 0. Five
# of six under-covered; the first prints "no .lean files to check" and exits 0
# over twenty-six changed Lean files.
#
# THE SILENT NARROWING THIS EXISTS TO STOP
# ----------------------------------------
# The four fixes each wrote, independently:
#
#     base=$(git merge-base HEAD origin/main 2>/dev/null || true)
#     [ -n "$base" ] && git diff --name-only "$base"...HEAD
#
# which is correct when `origin/main` resolves and SILENTLY REVERTS TO THE
# ORIGINAL BUG when it does not. Measured in a single-branch clone
# (`git clone --depth 1 --branch <feature> --single-branch`), where
# `refs/remotes/origin/main` is absent: `merge-base` fails, `base` is empty,
# the branch half contributes nothing, and precision-gates.sh --changed prints
#
#     precision-gates: no witness or computations/ script touched — skipped.
#
# with no indication that half its input was dropped. A fix that degrades to
# the bug it fixed, without saying so, is worse than the bug -- the bug at
# least did not carry a comment claiming it was fixed.
#
# So: this resolves a base through documented fallbacks, and when it cannot,
# it says so ON STDERR and names the one-line remedy. It never silently
# narrows. Callers that want the narrow set can still have it -- by passing an
# explicit ref -- but never by accident.

# Emit the base commit to diff against, or "" if none could be resolved.
# Warns once per shell on failure. Never fetches: a gate that reaches the
# network on its own is a gate that hangs in an offline container.
changed_files_base() {
  local upstream="${CHANGED_FILES_BASE_REF:-origin/main}" base
  if base=$(git merge-base HEAD "$upstream" 2>/dev/null); then
    printf '%s\n' "$base"
    return 0
  fi
  # Local `main` is the common case in a clone made without remote-tracking
  # refs; it is a weaker base (it can lag origin) but it is a real one.
  if base=$(git merge-base HEAD main 2>/dev/null); then
    printf '%s\n' "$base"
    return 0
  fi
  # WARNS ON EVERY CALL, DELIBERATELY. The first draft guarded this with a
  # `_CHANGED_FILES_WARNED` flag to warn "once per shell". Its own test caught
  # that the guard CANNOT FIRE under the way every caller actually invokes
  # this: `$(changed_files)` is a command substitution, so each call runs in a
  # fresh subshell and the flag never survives to the next one. A guard that
  # cannot fire in the calling convention is not a guard -- it is a comment
  # claiming a behaviour the code does not have, which is the same family of
  # defect this whole file exists to stop. Each gate calls this once, so
  # warning per call is both correct and quiet.
  printf '%s\n' \
    "WARNING: cannot resolve '$upstream' — committed changes on this branch" \
    "         are INVISIBLE to this check, which now sees only uncommitted" \
    "         work. This is the qou-pt9b false-all-clear, not a pass." \
    "         Fix:  git fetch origin main" >&2
  return 1
}

# A one-line description of WHAT was compared, for a caller's skip message.
#
# Requested on #5495 by the sibling working #5453, who audited their own
# session transcript for the incidence: across 73 `precision-gates.sh`
# invocations, 3 were `--changed` used as an actual verification step. Low but
# non-zero -- and invisible, because
#
#     precision-gates: no witness or computations/ script touched — skipped.
#
# is printed both when nothing genuinely changed AND when the merge-base half
# was dropped, which after a commit mean opposite things. A caller cannot tell
# a real skip from the defect by reading its own output. So callers print this
# beside the skip, and the two cases read differently.
#
# NOT returned through a variable, deliberately: every caller invokes
# `$(changed_files)`, a subshell, so a variable set inside cannot reach them.
# That is the same constraint that killed the once-per-shell warning guard
# (see below), and it is why this is a function the caller calls rather than
# state the caller reads.
#
# Exit status is the base's: 0 when a real base was compared, 1 when it was
# not, so `changed_files_scope || <treat as unverified>` is available.
changed_files_scope() {
  local upstream="${CHANGED_FILES_BASE_REF:-origin/main}" base n
  if ! base=$(changed_files_base 2>/dev/null); then
    printf '%s\n' "working tree ONLY — '$upstream' unresolved, so COMMITTED work was NOT examined"
    return 1
  fi
  n=$(git rev-list --count "$base"..HEAD 2>/dev/null || echo "?")
  printf '%s\n' "working tree + $n commit(s) since $upstream ($(git rev-parse --short "$base" 2>/dev/null))"
}


# One path per line: uncommitted (unstaged + staged + untracked) UNION
# everything this branch has committed since the base.
changed_files() {
  local base
  base=$(changed_files_base) || base=""
  {
    git diff --name-only HEAD 2>/dev/null
    git diff --cached --name-only 2>/dev/null
    git ls-files --others --exclude-standard 2>/dev/null
    [ -n "$base" ] && git diff --name-only "$base"...HEAD 2>/dev/null
  } | sort -u | grep -v '^$' || true
}

# ── Self-test ───────────────────────────────────────────────────────
#
# Sourcing this file defines the two functions and nothing else. Running it
# directly with --self-test exercises them against real throwaway repos:
#
#   bash scripts/lib/changed-files.sh --self-test
#
# Every case below is a shape that was actually wrong somewhere. Case 2 is the
# defect the four gates shared (a COMMITTED change reported as nothing). Case
# 5 is the silent narrowing described in the header, reproduced rather than
# asserted. Case 6 exists because the first draft of this file claimed to warn
# "once per shell" and this test proved the guard could never fire, since every
# caller invokes `$(changed_files)` in a subshell.
_changed_files_self_test() {
  local fail=0 out warn n
  _cf_mk() { rm -rf "$1"; mkdir -p "$1"; cd "$1" || return 1
             git init -q -b main .; git config user.email t@t; git config user.name t
             echo base > a.txt; git add -A; git commit -qm base; }
  _cf_chk() { if [ "$2" = "$3" ]; then printf '  [ok  ] %s\n' "$1"
              else printf '  [FAIL] %s\n       want: %s\n       got : %s\n' "$1" "$2" "$3"; fail=1; fi; }

  _cf_mk /tmp/cf-selftest-1 >/dev/null 2>&1
  git remote add origin . >/dev/null 2>&1; git update-ref refs/remotes/origin/main HEAD
  _cf_chk "on main, clean -> empty" "" "$(changed_files)"

  git switch -qc feat; echo x > committed.txt; git add -A; git commit -qm work
  _cf_chk "branch, change COMMITTED -> seen" "committed.txt" "$(changed_files)"

  echo y > dirty.txt
  _cf_chk "committed + untracked -> both" "committed.txt
dirty.txt" "$(changed_files)"

  git add dirty.txt
  _cf_chk "staged still counted" "committed.txt
dirty.txt" "$(changed_files)"

  _cf_mk /tmp/cf-selftest-2 >/dev/null 2>&1
  git switch -qc feat2; echo z > only-committed.txt; git add -A; git commit -qm w2
  git branch -qD main 2>/dev/null
  out=$(changed_files 2>/dev/null)
  warn=$(changed_files 2>&1 >/dev/null | head -1)
  _cf_chk "no base -> narrows (documented)" "" "$out"
  case "$warn" in
    WARNING:*) printf '  [ok  ] no base -> WARNS on stderr\n' ;;
    *) printf '  [FAIL] no base -> expected WARNING, got: %s\n' "$warn"; fail=1 ;;
  esac

  n=$(changed_files 2>&1 >/dev/null | grep -c '^WARNING:')
  _cf_chk "warning still fires on a later call" "1" "$n"

  # changed_files_scope: the two cases must READ differently and must carry
  # different exit statuses, because that difference is the whole point --
  # "0 files considered" and "the base was dropped" were one message before.
  case "$(changed_files_scope)" in
    *"working tree ONLY"*) printf '  [ok  ] scope, no base -> says COMMITTED work was not examined\n' ;;
    *) printf '  [FAIL] scope, no base -> %s\n' "$(changed_files_scope)"; fail=1 ;;
  esac
  changed_files_scope >/dev/null 2>&1 && { printf '  [FAIL] scope, no base -> exit 0, want 1\n'; fail=1; } \
    || printf '  [ok  ] scope, no base -> exit 1\n'

  _cf_mk /tmp/cf-selftest-3 >/dev/null 2>&1
  git branch -q rel; git switch -qc feat3; echo q > f.txt; git add -A; git commit -qm w3
  _cf_chk "explicit base ref honoured" "f.txt" "$(CHANGED_FILES_BASE_REF=rel changed_files)"
  case "$(CHANGED_FILES_BASE_REF=rel changed_files_scope)" in
    *"1 commit(s) since rel"*) printf '  [ok  ] scope, base resolved -> names ref and commit count\n' ;;
    *) printf '  [FAIL] scope, base resolved -> %s\n' "$(CHANGED_FILES_BASE_REF=rel changed_files_scope)"; fail=1 ;;
  esac

  cd /; rm -rf /tmp/cf-selftest-1 /tmp/cf-selftest-2 /tmp/cf-selftest-3
  echo
  if [ "$fail" -eq 0 ]; then echo "changed-files self-test passed"; else echo "changed-files self-test FAILED"; fi
  return "$fail"
}

if [ "${BASH_SOURCE[0]}" = "$0" ]; then
  case "${1:-}" in
    --self-test) _changed_files_self_test; exit $? ;;
    *) echo "scripts/lib/changed-files.sh — source this file; --self-test to test it" >&2; exit 2 ;;
  esac
fi
