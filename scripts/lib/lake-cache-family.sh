# shellcheck shell=bash
# The Lean build-cache branch FAMILY, read from qou.json — sourced, not run.
#
# One place says where qou's cache branches live, and it is the declaration:
# the `lake-cache` directory entry in qou.json, `storage.branchPrefix`
# (platform beans rva2 / lehh / j9cs, owner 2026-10-03: "each harness
# declares it … why centralize?"). Before this file every script below
# hardcoded `lake-cache/`, so the name was written down twelve times.
#
# THE MIGRATION (owner, 2026-10-05: "migratez qou"). The family moved from
# `lake-cache/<member>` to `cat/folio-assistant-sci/lake-cache/<member>`,
# the platform's name for it. Old branches are NOT renamed or deleted — they
# are load-bearing, and AGENTS.md rule 9 forbids deleting branches. Instead:
#
#   - WRITES go to the declared (new) name only;
#   - READS take the declared name if the member exists there, else the
#     legacy `lake-cache/<member>`.
#
# So a member's new-name branch is created by its first seed after this
# lands, and from then on it is the newer of the two by construction: only
# the legacy name is frozen. Branches were deliberately NOT copied ahead of
# time — a copy made before merge would go stale on the next old-name seed,
# and readers prefer the new name.
#
# Usage:
#   . "$REPO_ROOT/scripts/lib/lake-cache-family.sh"
#   lake_cache_write_branch qou-v4-24-0     # -> cat/folio-assistant-sci/lake-cache/qou-v4-24-0
#   lake_cache_read_branch  qou-v4-24-0     # -> whichever of new / legacy exists on origin
#   lake_cache_ls_remote                    # ls-remote over every name, new first

_lcf_root="${REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"

# The declared prefix, with a trailing slash. Falls back to the platform's
# name only if qou.json cannot be read — a missing declaration is reported,
# never silently replaced by the legacy name.
LAKE_CACHE_PREFIX="$(python3 - "$_lcf_root/qou.json" <<'PY' 2>/dev/null
import json, sys
d = json.load(open(sys.argv[1]))
for e in d.get("directories", []):
    st = e.get("storage") or {}
    if "lake-cache" in (e.get("graphTypologies") or e.get("graphKinds") or []) and st.get("keyedBy") == "family":
        print(st["branchPrefix"]); break
PY
)"
if [ -z "$LAKE_CACHE_PREFIX" ]; then
  echo "lake-cache-family: qou.json declares no lake-cache family; using the platform default" >&2
  LAKE_CACHE_PREFIX="cat/folio-assistant-sci/lake-cache/"
fi
# Read-only fallbacks, newest first. Never written to.
LAKE_CACHE_LEGACY_PREFIXES="lake-cache/"
export LAKE_CACHE_PREFIX LAKE_CACHE_LEGACY_PREFIXES

lake_cache_write_branch() { printf '%s%s\n' "$LAKE_CACHE_PREFIX" "$1"; }

# The branch to read MEMBER from: the declared name if origin has it, else
# the first legacy name that does. Prints the declared name when none exists,
# so a caller's own "not found" message names where it looked first.
lake_cache_read_branch() {
  local member="$1" p
  for p in "$LAKE_CACHE_PREFIX" $LAKE_CACHE_LEGACY_PREFIXES; do
    if git -C "$_lcf_root" ls-remote --exit-code --heads origin "$p$member" >/dev/null 2>&1; then
      printf '%s%s\n' "$p" "$member"; return 0
    fi
  done
  printf '%s%s\n' "$LAKE_CACHE_PREFIX" "$member"
  return 1
}

# `git ls-remote --heads origin` over every name the family has, newest name
# first. Runs the command itself so the globs are never word-split or
# expanded against local files.
lake_cache_ls_remote() {
  local -a pats=() ; local p
  for p in "$LAKE_CACHE_PREFIX" $LAKE_CACHE_LEGACY_PREFIXES; do pats+=("$p*"); done
  git -C "$_lcf_root" ls-remote --heads origin "${pats[@]}"
}
