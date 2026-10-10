#!/usr/bin/env bash
# folio-pin-coupling-check.sh — assert `.folio-assistant-pin` and the platform sha
# in `.github/workflows/build.yml` are the SAME commit.
#
# WHY THIS EXISTS (bean qou-pwp9)
# ------------------------------
# The platform version is chosen in TWO places and the pin file used to claim it
# was one:
#
#   .folio-assistant-pin          -> what an agent MEASURES in its local checkout
#   build.yml's `uses:` line      -> what actually PUBLISHES
#
# Until 2026-09-26 the second read `@main`, so the published artifact tracked
# platform main while the pin governed only local measurement. Two platforms, one
# repo, and no signal when they disagreed — the exact failure the pin file exists
# to prevent, one level down.
#
# Pinning them together fixed the instance. This script is what stops the CLASS
# coming back, because the coupling is otherwise only prose in two comments, and
# this repo's own record is that a rule living only in prose gets broken (AGENTS.md
# §"a gate nobody invokes is documentation").
#
# WHAT IT DOES NOT DO
# -------------------
# It does NOT check that the sha exists upstream or that the platform is current.
# Advancing the pin is a deliberate owner-reviewable decision (qou-8321); this only
# asserts the two local declarations agree. A DRIFTED pair is a defect; an OLD pair
# is a choice.
#
# Exit 0 = agree. Exit 1 = drift (or either declaration is unreadable/absent).
#
# Usage:  folio-pin-coupling-check.sh [--quiet]
#         folio-pin-coupling-check.sh --selftest
set -uo pipefail

PIN_FILE=".folio-assistant-pin"
WF_FILE=".github/workflows/build.yml"

# Pure functions of a root, so --selftest can run them against a fixture.
pin_sha() {  # $1 = root
  # Last non-comment, non-blank line. The file is mostly rationale comments.
  grep -vE '^\s*(#|$)' "$1/$PIN_FILE" 2>/dev/null | tail -1 | tr -d '[:space:]'
}
wf_sha() {   # $1 = root
  # Match ONLY at a real `uses:` key, not in a comment. A comment quoting the line
  # is not a declaration, and this file now carries several such comments — the
  # naive grep for `publish.yml@` matches them and would report the wrong sha.
  grep -E '^[[:space:]]*uses:[[:space:]]*litlfred/folio-assistant/\.github/workflows/publish\.yml@' \
    "$1/$WF_FILE" 2>/dev/null | head -1 | sed -E 's/.*publish\.yml@//' | tr -d '[:space:]'
}

check() {  # $1 = root ; prints diagnosis, returns 0/1
  local root="$1" p w
  p=$(pin_sha "$root"); w=$(wf_sha "$root")
  if [ -z "$p" ]; then echo "FAIL: no sha in $PIN_FILE"; return 1; fi
  if [ -z "$w" ]; then
    echo "FAIL: $WF_FILE has no pinned platform sha on a \`uses:\` line."
    echo "      If it reads \`@main\`, that is the qou-pwp9 defect: the published"
    echo "      build would track platform main and bypass the pin."
    return 1
  fi
  if [ "$p" != "$w" ]; then
    echo "FAIL: platform pin DRIFT — the two declarations disagree."
    echo "      $PIN_FILE : $p"
    echo "      $WF_FILE  : $w"
    echo "      Bumping the platform means editing BOTH, in one commit."
    return 1
  fi
  [ "${QUIET:-0}" = 1 ] || echo "ok: platform pin coupled — both declare ${p:0:11}"
  return 0
}

if [ "${1:-}" = "--selftest" ]; then
  echo "SELFTEST — does it catch drift, @main, and a comment-only mention?"
  t=$(mktemp -d); trap 'rm -rf "$t"' EXIT INT TERM
  ok=1
  mk() {  # $1=dir $2=pin sha $3=uses-value ; $4 optional extra comment line
    mkdir -p "$t/$1/.github/workflows"
    { echo "# rationale comment"; echo; echo "$2"; } > "$t/$1/.folio-assistant-pin"
    { echo "jobs:"; echo "  publish:";
      [ -n "${4:-}" ] && echo "    # $4";
      echo "    uses: litlfred/folio-assistant/.github/workflows/publish.yml@$3"; } \
      > "$t/$1/.github/workflows/build.yml"
  }
  SHA=df28d02dcd3e3f51aad4690c56b2348ab52efd4c
  OTHER=42ccfb38b63aaaaaaaaaaaaaaaaaaaaaaaaaaaaa

  mk agree   "$SHA" "$SHA"
  QUIET=1 check "$t/agree" >/dev/null 2>&1 \
    && echo "  matching pair passes        -> YES" \
    || { echo "  matching pair passes        -> NO"; ok=0; }

  mk drift   "$SHA" "$OTHER"
  QUIET=1 check "$t/drift" >/dev/null 2>&1 \
    && { echo "  drift detected              -> NO"; ok=0; } \
    || echo "  drift detected              -> YES"

  mk atmain  "$SHA" "main"
  QUIET=1 check "$t/atmain" >/dev/null 2>&1 \
    && { echo "  \`@main\` rejected            -> NO"; ok=0; } \
    || echo "  \`@main\` rejected            -> YES"

  # THE ONE THAT MATTERS: build.yml now CARRIES comments quoting the old `@main`
  # form. A grep for `publish.yml@` anywhere would read the comment and could pass
  # a drifted file or fail a clean one. Require the `uses:` key.
  mk comment "$SHA" "$SHA" "this read publish.yml@main until 2026-09-26"
  QUIET=1 check "$t/comment" >/dev/null 2>&1 \
    && echo "  comment mention ignored     -> YES" \
    || { echo "  comment mention ignored     -> NO"; ok=0; }

  mk cmtdrift "$SHA" "$OTHER" "this read publish.yml@$SHA until today"
  QUIET=1 check "$t/cmtdrift" >/dev/null 2>&1 \
    && { echo "  comment cannot mask drift   -> NO"; ok=0; } \
    || echo "  comment cannot mask drift   -> YES"

  echo
  [ "$ok" = 1 ] && { echo "  PASS"; exit 0; }
  echo "  FAIL — do not trust this guard."; exit 1
fi

[ "${1:-}" = "--quiet" ] && QUIET=1
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "not a git repo"; exit 1; }
check "$ROOT"
