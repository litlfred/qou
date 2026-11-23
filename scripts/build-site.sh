#!/usr/bin/env bash
# build-site — build qou's published site into $SITE_DIR (default _site).
#
# This is the folio's `build_command` for the platform's reusable
# `folio-staging.yml` (called from .github/workflows/build.yml), and the
# build step of scripts/publish-main-local.sh, which agents run after a merge
# to main when GitHub Actions is not enabled (owner, 2026-11-23).
#
# Two parts:
#   1. The folio site: folio-assistant-core's build-folio-site.ts.
#   2. The Lean library render, the folio's `lean` visualiser declared in
#      qou.json: folio-assistant-sci's lean-docs-build.sh (doc-gen4, restores
#      the warm lake cache first) and lean-render.ts (stages it at <site>/lean/
#      with the harness navbar). Skill: folio-assistant-sci `lean-html-docs`.
#
# The Lean part needs `lake` on PATH and a warm cache. When `lake` is absent it
# is SKIPPED and says so: the site still builds, without lean/. Set
# QOU_LEAN_DOCS=0 to skip it on purpose, =1 to make a missing lake an error.
set -euo pipefail
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"
SITE=${SITE_DIR:-_site}
PLAT=${PLATFORM_DIR:-folio-assistant}
LEAN=${QOU_LEAN_DOCS:-auto}

[ -d "$PLAT/folio-assistant-core" ] || { echo "build-site: platform not found at $PLAT (run scripts/setup-folio-assistant.sh)" >&2; exit 2; }

echo "== build-site: folio site -> $SITE"
bun run "$PLAT/folio-assistant-core/scripts/build-folio-site.ts" --out "$SITE"

if [ "$LEAN" = 0 ]; then
  echo "== build-site: Lean render skipped (QOU_LEAN_DOCS=0)"
elif ! command -v lake >/dev/null 2>&1; then
  if [ "$LEAN" = 1 ]; then echo "build-site: QOU_LEAN_DOCS=1 but lake is not on PATH" >&2; exit 3; fi
  echo "== build-site: Lean render SKIPPED: lake is not on PATH, so $SITE has no lean/. Set up Lean (scripts/setup-lean-toolchain.sh) and re-run to include it."
else
  echo "== build-site: Lean render -> $SITE/lean"
  bash "$PLAT/folio-assistant-sci/adapters/paper/lean/lean-docs-build.sh" \
    --lake-root folio/quantum-observable-universe/lean --lib QOU --platform "$PLAT" --restore
  bun run "$PLAT/folio-assistant-sci/adapters/paper/lean/lean-render.ts" \
    --docs folio/quantum-observable-universe/lean/.lake/build/doc \
    --site "$SITE" --route lean --modules QOU,UGB,Fred2005 --home-label qou \
    --platform "$PLAT"
fi
echo "== build-site: done ($SITE)"
