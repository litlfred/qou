#!/usr/bin/env bash
# Scope resolution for the Lean CI gates — SOURCE this, do not execute.
#
#   Defines:  lean_scope_files <scope> <base_input> <pr_base> <set>
#             where <scope> is all|changed and <set> is all|siblings
#   Emits:    a space-separated file list on stdout
#   Exits 1:  on a scope it cannot compute, or an EMPTY whole-tree list
#
# WHY THIS EXISTS (bean qou-lsib, 2026-09-07)
# -------------------------------------------
# `.github/workflows/lean-content-siblings.yml` computed its file list as
#
#     base="origin/${{ github.base_ref }}"
#     files=$(git diff --name-only --diff-filter=d "$base"...HEAD -- '*.lean' | tr '\n' ' ')
#
# in BOTH of its jobs. `github.base_ref` is empty for `workflow_dispatch`,
# which — auto-triggers being disabled repo-wide since 2026-06-30 for Actions
# billing — is the workflow's ONLY trigger. So `base` was the literal string
# `origin/`, git answered
#
#     fatal: bad revision 'origin/...HEAD'
#
# and `files` came back empty. `set -e` did not catch it: the assignment's
# status is the PIPELINE's, and the pipeline ends in `tr`, which succeeded.
# Every downstream step was guarded `if: files != ''`, so both jobs SKIPPED
# EVERYTHING AND REPORTED GREEN.
#
# The bean had this as "diff-scoped, so it reaches neither the 34 known
# failures nor anything on a push". That understates it. It reached nothing at
# all, on every run it was capable of, and said so in green.
#
# THE SHAPE OF THE BUG, NOT JUST THE INSTANCE
# -------------------------------------------
# The failure is not "wrong ref". It is that an unresolvable scope and a
# genuinely-empty scope produced the SAME OUTPUT — an empty list — and the
# caller could not tell them apart. That is the same defect
# `scripts/lib/changed-files.sh` was written to stop one layer down, and the
# reason this is a shared function rather than two inline `run:` blocks: the
# third gate to want a file list will reach for the same idiom.
#
# So: a scope that cannot be computed FAILS LOUDLY, and a whole-tree scope
# that comes back empty FAILS LOUDLY, because the tree is never empty and an
# empty answer there means the enumeration broke. Only `scope=changed` may
# legitimately return nothing, and it says so.

# lean_scope_files <scope> <base_input> <pr_base> <set>
#
#   scope       all      every tracked .lean in <set>
#               changed  only those differing from a base ref
#   base_input  explicit base for scope=changed ("" to fall back to pr_base)
#   pr_base     github.base_ref, i.e. a BRANCH NAME without the origin/ prefix
#               ("" under workflow_dispatch — the case that caused all this)
#   set         all       every tracked *.lean, library tree included
#               siblings  content/**/*.lean OUTSIDE any lean/ tree (lake owns
#                         those), which is the content-sibling population
lean_scope_files() {
  local scope="${1:-}" base_input="${2:-}" pr_base="${3:-}" set_name="${4:-siblings}"
  local base files

  case "$set_name" in
    all)      _lean_scope_all()      { git ls-files -- '*.lean'; } ;;
    siblings) _lean_scope_all()      { git ls-files -- content | grep '\.lean$' | grep -v '/lean/'; } ;;
    *) echo "::error::lean_scope_files: unknown set '$set_name' (want all|siblings)" >&2; return 1 ;;
  esac

  case "$scope" in
    all)
      files=$(_lean_scope_all || true)
      if [ -z "$files" ]; then
        # The tree always has .lean files. Empty here means the enumeration
        # broke (wrong cwd, shallow checkout, pathspec typo) — exactly the
        # class that used to pass green.
        echo "::error::scope=all produced ZERO files for set '$set_name'." \
             "The tree is never empty; the enumeration is broken. Refusing to" \
             "report green over nothing." >&2
        return 1
      fi
      ;;
    changed)
      base="$base_input"
      if [ -z "$base" ] && [ -n "$pr_base" ]; then base="origin/$pr_base"; fi
      if [ -z "$base" ]; then
        echo "::error::scope=changed needs a base ref. Pass the 'base' input" \
             "(e.g. origin/main), or use scope=all. Under workflow_dispatch" \
             "github.base_ref is EMPTY — that is the qou-lsib green-no-op." >&2
        return 1
      fi
      git fetch origin "${base#origin/}" --depth=1 >/dev/null 2>&1 || true
      if ! git rev-parse --verify --quiet "$base" >/dev/null; then
        echo "::error::base ref '$base' does not resolve. Refusing to diff" \
             "against nothing and report green." >&2
        return 1
      fi
      case "$set_name" in
        all)      files=$(git diff --name-only --diff-filter=d "$base"...HEAD -- '*.lean' || true) ;;
        siblings) files=$(git diff --name-only --diff-filter=d "$base"...HEAD -- content \
                          | grep '\.lean$' | grep -v '/lean/' || true) ;;
      esac
      # Empty IS legitimate here: a PR may touch no Lean at all.
      ;;
    *)
      echo "::error::unknown scope '$scope' (want all|changed)" >&2
      return 1
      ;;
  esac

  printf '%s' "$files" | tr '\n' ' '
}

# ── Self-test ───────────────────────────────────────────────────────
#
#   bash scripts/lib/ci-lean-scope.sh --self-test
#
# Case 1 REPRODUCES the original defect against the old idiom, so the fix is
# measured against the bug rather than asserted past it. The rest pin the
# behaviours that make an empty answer unambiguous.
_ci_lean_scope_self_test() {
  local fail=0 out rc
  _cls_chk() { if [ "$2" = "$3" ]; then printf '  [ok  ] %s\n' "$1"
               else printf '  [FAIL] %s\n       want: %s\n       got : %s\n' "$1" "$2" "$3"; fail=1; fi; }

  local d=/tmp/cls-selftest
  rm -rf "$d"; mkdir -p "$d/content/paper/chap" "$d/content/paper/lean/QOU"
  cd "$d" || return 1
  git init -q -b main .; git config user.email t@t; git config user.name t
  echo "-- sibling" > content/paper/chap/block.lean
  echo "-- library" > content/paper/lean/QOU/Lib.lean
  git add -A; git commit -qm base

  # 1. THE ORIGINAL DEFECT, reproduced: empty base_ref -> empty list, exit 0.
  out=$(base="origin/"; git diff --name-only --diff-filter=d "$base"...HEAD -- '*.lean' 2>/dev/null | tr '\n' ' '); rc=$?
  _cls_chk "old idiom, empty base_ref -> empty list" "" "$out"
  _cls_chk "old idiom, empty base_ref -> exit 0 (the green no-op)" "0" "$rc"

  # 2. The fix refuses that same input instead of passing empty.
  out=$(lean_scope_files changed "" "" siblings 2>/dev/null); rc=$?
  _cls_chk "scope=changed, no base -> exit 1" "1" "$rc"

  # 3. Whole-tree finds the sibling and EXCLUDES the library tree.
  out=$(lean_scope_files all "" "" siblings 2>/dev/null)
  _cls_chk "scope=all siblings -> sibling only" "content/paper/chap/block.lean" "$out"
  out=$(lean_scope_files all "" "" all 2>/dev/null)
  _cls_chk "scope=all all -> both" \
    "content/paper/chap/block.lean content/paper/lean/QOU/Lib.lean" "$out"

  # 4. A whole-tree scope that comes back empty must FAIL, not pass green.
  local e=/tmp/cls-selftest-empty
  rm -rf "$e"; mkdir -p "$e"; cd "$e" || return 1
  git init -q -b main .; git config user.email t@t; git config user.name t
  echo x > a.txt; git add -A; git commit -qm base
  lean_scope_files all "" "" siblings >/dev/null 2>&1 && \
    { printf '  [FAIL] scope=all, empty tree -> exit 0, want 1\n'; fail=1; } || \
    printf '  [ok  ] scope=all, empty tree -> exit 1\n'

  # 5. An unresolvable explicit base fails rather than diffing against nothing.
  lean_scope_files changed "origin/does-not-exist" "" siblings >/dev/null 2>&1 && \
    { printf '  [FAIL] scope=changed, bad base -> exit 0, want 1\n'; fail=1; } || \
    printf '  [ok  ] scope=changed, bad base -> exit 1\n'

  # 6. A real base with no Lean changes IS legitimately empty, and exits 0 —
  #    the one case where empty means what it says.
  cd "$d" || return 1
  git switch -qc feat; echo y > note.txt; git add -A; git commit -qm nolean
  out=$(lean_scope_files changed "main" "" siblings 2>/dev/null); rc=$?
  _cls_chk "scope=changed, real base, no .lean touched -> empty" "" "$out"
  _cls_chk "scope=changed, real base, no .lean touched -> exit 0" "0" "$rc"

  # 7. …and a base that DID touch a sibling reports it.
  echo "-- edit" >> content/paper/chap/block.lean; git add -A; git commit -qm edit
  out=$(lean_scope_files changed "main" "" siblings 2>/dev/null)
  _cls_chk "scope=changed picks up the edited sibling" "content/paper/chap/block.lean" "$out"

  # 8. pr_base is a BRANCH NAME and gets the origin/ prefix; base_input does not.
  git update-ref refs/remotes/origin/main main
  out=$(lean_scope_files changed "" "main" siblings 2>/dev/null)
  _cls_chk "pr_base branch name -> origin/ prefixed and resolved" \
    "content/paper/chap/block.lean" "$out"

  cd /; rm -rf "$d" "$e"
  echo
  if [ "$fail" -eq 0 ]; then echo "ci-lean-scope self-test passed"; else echo "ci-lean-scope self-test FAILED"; fi
  return "$fail"
}

if [ "${BASH_SOURCE[0]}" = "$0" ]; then
  case "${1:-}" in
    --self-test) _ci_lean_scope_self_test; exit $? ;;
    *) echo "scripts/lib/ci-lean-scope.sh — source this file; --self-test to test it" >&2; exit 2 ;;
  esac
fi
