#!/usr/bin/env bash
# precommit-bean-id-warn.sh — WARN (never block) when two bean files claim the
# same id.
#
# WHY THIS EXISTS
# ---------------
# scripts/check-beans.sh ALREADY detects this. It has detected it since it was
# written: failure shape 4, "two files claiming the same `# <id>`", and it exits
# 1 on a duplicate. Nothing ever ran it. A gate nobody invokes is documentation
# — the same finding scripts/precommit-precision-warn.sh records for
# precision-gates.sh, one directory over.
#
# The cost of that, measured 2026-08-30: `qou-rrgk` was carried by TWO unrelated
# beans on main — the alpha_em germ-viability probe (completed) and a q0-anchor
# drain (todo). `beans show qou-rrgk` resolved silently to the DRAIN one, so the
# germ bean was unreachable by its own id, and commit 13cb825068 saying "Decides
# bean qou-rrgk" read as closing a q0 drain it never touched. Four tracked files
# cite that id meaning the germ bean.
#
# It is also a REGRESSION, not a leftover: qou-xqno drained the previous two
# duplicate ids and is completed. The create-guard added under qou-2ryn is an
# exact-TITLE existence check (AGENTS.md §Agent work-plan policy item 1), and
# these two beans have completely different titles — nothing checked the id.
#
# WHY A NARROW CHECK AND NOT check-beans.sh ITSELF
# ------------------------------------------------
# Measured 2026-08-30 on this corpus (4332 bean files):
#
#     scripts/check-beans.sh            40.4 s
#     duplicate-id pass only             0.024 s
#
# A PreToolUse hook runs BEFORE the tool call. Wiring the full validator here
# would add forty seconds to every bean-touching commit, and bean-touching
# commits are the most frequent kind in this repo — that buys avoidance, not
# safety. So this runs the ONE check that the 2026-08-30 incident turned up and
# names check-beans.sh for the other three failure shapes (missing front-matter,
# front-matter not at top, missing opening `---`).
#
# WHY WARN AND NEVER BLOCK
# ------------------------
# A PreToolUse hook exiting non-zero stops the tool call. Following the posture
# the owner chose for the precision hook on 2026-08-25 (warn-on-commit; a
# push-side block was offered and declined), this ALWAYS exits 0. Do not upgrade
# it to blocking without asking.
#
# Bean: qou-ut5r.
set -uo pipefail

# Only speak when the tool call WRITES beans: a commit (while beans/ is still
# tracked) or, since the cutover to the `cat/cat-harness/beans` branch (issue
# #7642), the push of the mounted copy (`branch-store.ts push --id beans`).
case "${1:-}${*:-}" in
  *"git commit"*|*"git add"*|*"branch-store"*"push"*) ;;
  *) exit 0 ;;
esac

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
cd "$ROOT" || exit 0
[ -d beans/defs ] || exit 0

# Cheap relevance gate: nothing changed under beans/defs/ ⇒ silent. While
# beans/ is tracked that is `git status`; once it is a gitignored branch mount,
# git status cannot see it at all (which would make this hook silently inert),
# so a push of the mount is always checked.
if git ls-files --error-unmatch beans/defs >/dev/null 2>&1; then
  if ! git status --porcelain -- beans/defs 2>/dev/null | grep -q .; then
    exit 0
  fi
fi

dups=$(grep -m1 -H '^# ' beans/defs/*.md 2>/dev/null \
  | sed 's|^\beans/defs/||; s|\.md:# |\t|' \
  | awk -F'\t' '{ c[$2] = c[$2] " " $1 ; n[$2]++ }
                END { for (i in c) if (n[i] > 1) print i "\t" c[i] }')

if [ -n "$dups" ]; then
  echo "⚠ bean-id collision — two files claim the same id:" >&2
  printf '%s\n' "$dups" | while IFS=$'\t' read -r id files; do
    echo "    $id  ←$files" >&2
  done
  echo '  `beans show <id>` serves only ONE of them, silently; the other is' >&2
  echo "  unreachable by its own id. Re-issue whichever is cited LEAST outside" >&2
  echo "  beans/defs/ under a fresh id (check with: git grep -l '<id>' -- . ':!beans/defs/')." >&2
  echo "  Full validator: scripts/check-beans.sh   (bean qou-ut5r)" >&2
fi

exit 0
