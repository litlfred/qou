#!/usr/bin/env bash
# Build qou's folio site (just-the-docs/harness chrome) and, with --deploy,
# publish it to gh-pages STAGING/<slug>/.
#
# Steps = the platform's stage-folio-local.ts (folio-assistant-core), with one
# qou step added after the build: qou-site-extras.py (per-block QA report,
# resolved Lean link + compile status, Lean nav group).
#
# Needs a checkout of litlfred/folio-assistant main with its layers mounted:
#   git -C ../folio-assistant worktree add ../fa-main origin/main
#   (cd ../fa-main && bash .github/mount-from-lock.sh --root . && bun install)
#
# Env:
#   FA_MAIN        platform checkout (default ../fa-main)
#   SITE           output dir (default _site)
#   SLUG           STAGING slug (default folio-kg-site)
#   LEAN_STATUS    qou-lean-status/v1 JSON from a lean-direct sweep (optional;
#                  without it every Lean link says "build unchecked")
#   PLAYWRIGHT_CHROMIUM_EXECUTABLE  e.g. /opt/pw-browsers/chromium in a sandbox
#   FA_ASSETS / KATEX_DIR  local copies when github.io / jsdelivr are firewalled
#                  (chrome check only)
set -euo pipefail
ROOT=$(git rev-parse --show-toplevel)
FA_MAIN=${FA_MAIN:-$ROOT/../fa-main}
SITE=$(realpath -m "${SITE:-$ROOT/_site}")
SLUG=${SLUG:-folio-kg-site}
EXTRA=()
[ -n "${LEAN_STATUS:-}" ] && EXTRA+=(--lean-status "$LEAN_STATUS")
BUILD="bun run $FA_MAIN/folio-assistant-core/scripts/build-folio-site.ts --out $SITE && python3 -I scripts/folio-site/qou-site-extras.py --site $SITE ${EXTRA[*]:-}"
ARGS=(--repo "$ROOT" --slug "$SLUG" --site-dir "$SITE" --publish-repo litlfred/qou
      --pr-url "${PR_URL:-https://github.com/litlfred/qou}" --run-url "${RUN_URL:-https://github.com/litlfred/qou}"
      --build "$BUILD" --check-page cat-harness/folio/quantum-observable-universe/quantum-universes/)
[ -n "${FA_ASSETS:-}" ] && ARGS+=(--assets "$FA_ASSETS")
[ -n "${KATEX_DIR:-}" ] && ARGS+=(--katex "$KATEX_DIR")
cd "$FA_MAIN"
exec bun run folio-assistant-core/scripts/stage-folio-local.ts "${ARGS[@]}" "$@"
