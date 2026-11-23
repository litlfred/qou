#!/usr/bin/env bash
# publish-main-local — rebuild qou's site from main and publish it at the root
# of gh-pages, from an agent's checkout, when GitHub Actions is not enabled.
#
# Owner, 2026-11-23: "agents should rebuild when merge to main if github
# actions not enabled". This runs the same steps, in the same order, as the
# `publish-main` job of the platform's folio-staging.yml (which build.yml
# calls), so the result is the same whichever route ran:
#
#   1. build            scripts/build-site.sh (folio site + Lean render)
#   2. rail             cat-harness-tools rail-standalone-pages.ts --foreign-site
#   3. publish          cat-harness-tools publish-main-site.ts: deletes only the
#                       files its previous publish listed in _main-site.json, so
#                       branches/, the old lean/, drafts/ and the PDFs that
#                       README links are never touched
#   4. log + commit     render-log.ts, then one commit on gh-pages
#   5. push             only with --deploy; without it, stops after the commit
#                       in a local worktree and prints where
#
# Usage (from a clean checkout of main at the merged commit):
#   bash scripts/publish-main-local.sh            # build + stage, no push
#   bash scripts/publish-main-local.sh --deploy   # ... and push gh-pages
#
# Skill: .claude/skills/local/post-merge-rebuild.md
set -euo pipefail
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"
PLAT=${PLATFORM_DIR:-folio-assistant}
SITE=${SITE_DIR:-_site}
PAGES=${PAGES_DIR:-$ROOT/.gh-pages-worktree}
DEPLOY=0; [ "${1:-}" = "--deploy" ] && DEPLOY=1

BRANCH=$(git rev-parse --abbrev-ref HEAD)
SHA=$(git rev-parse HEAD)
if [ "$BRANCH" != main ]; then
  echo "publish-main-local: on '$BRANCH', not main. Check out the merged main first." >&2; exit 2
fi
git fetch -q origin main
if [ "$SHA" != "$(git rev-parse origin/main)" ]; then
  echo "publish-main-local: HEAD $SHA is not origin/main; pull first." >&2; exit 2
fi

rm -rf "$SITE"
SITE_DIR="$SITE" PLATFORM_DIR="$PLAT" bash scripts/build-site.sh

bun run "$PLAT/cat-harness-tools/scripts/rail-standalone-pages.ts" \
  --site "$SITE" --built cat-harness --foreign-site --home-label qou

git worktree remove --force "$PAGES" 2>/dev/null || true
git fetch -q --depth 1 origin gh-pages
git worktree add -q -B gh-pages "$PAGES" origin/gh-pages

bun run "$PLAT/cat-harness-tools/scripts/publish-main-site.ts" \
  --site "$SITE" --pages "$PAGES" --commit "$SHA"
printf '%s\n' "{\"summary\":\"main's site published at the root (agent, Actions not enabled)\"}" \
  | bun run "$PLAT/cat-harness-tools/scripts/render-log.ts" --dir "$PAGES" \
      --event rendered --kind main-site --path / --slug main \
      --branch main --commit "$SHA" --run "local:$(hostname)"
git -C "$PAGES" add -A .
if ! git -C "$PAGES" commit -q -m "main-site: from $SHA" -m "render-log: rendered the root from main" -m "published locally by an agent: GitHub Actions not enabled"; then
  echo "publish-main-local: nothing changed on gh-pages"; exit 0
fi
if [ "$DEPLOY" = 1 ]; then
  for attempt in 1 2 3 4; do
    if git -C "$PAGES" push -q origin HEAD:gh-pages; then echo "pushed gh-pages (attempt $attempt)"; exit 0; fi
    bash "$PLAT/cat-harness-tools/scripts/render-log-union-attr.sh" "$PAGES" || true
    git -C "$PAGES" pull -q --rebase origin gh-pages
    sleep $((2 ** attempt))
  done
  echo "publish-main-local: push failed after 4 attempts" >&2; exit 1
fi
echo "publish-main-local: committed in $PAGES, NOT pushed (pass --deploy)."
