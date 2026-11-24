#!/usr/bin/env bash
# build-site — build qou's published site into $SITE_DIR (default _site).
#
# This is the folio's `build_command` for the platform's reusable
# `folio-staging.yml` (called from .github/workflows/build.yml), and the
# build step of scripts/publish-main-local.sh, which agents run after a merge
# to main when GitHub Actions is not enabled (owner, 2026-11-23).
#
# Five parts:
#   1. The folio site: folio-assistant-core's build-folio-site.ts.
#   2. The 80-dps observational accuracy scorecard QA gate + standalone HTML
#      render (`scripts/generate-accuracy-scorecard.py --check --qa-report
#      --html-out $SITE/accuracy/index.html`), railed at `/accuracy/`.
#   3. The work plan (beans), the `beans` directory's visualiser declared in
#      qou.json: cat-harness-tools' beans-board.ts, the platform's own "Plans
#      and work" board (lib/bean-index.ts + work-plan.js), at <site>/beans/.
#      It needs the bean store mounted (state-mount.ts, which this runs when
#      beans/defs is absent) and a platform that carries beans-board.ts
#      (cat-harness-tools#2511); without either it is SKIPPED and says so.
#   4. The Lean library render, the folio's `lean` visualiser declared in
#      qou.json: folio-assistant-sci's lean-docs-build.sh (doc-gen4, restores
#      the warm lake cache first) and lean-render.ts (stages it at <site>/lean/
#      with the harness navbar). Skill: folio-assistant-sci `lean-html-docs`.
#   5. The root landing page, <site>/index.html: scripts/build-site-landing.py,
#      a short list of links (paper, PDF, and every coverage.visualiser that
#      qou.json declares under _site/), derived, never hand-written. Last, so
#      it can say which declared pages this build produced.
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

echo "== build-site: accuracy scorecard QA gate & HTML -> $SITE/accuracy"
python3 -c "import mpmath" >/dev/null 2>&1 || python3 -m pip install --quiet mpmath
python3 scripts/generate-accuracy-scorecard.py --check --qa-report --html-out "$SITE/accuracy/index.html"

BOARD="$PLAT/cat-harness-tools/scripts/beans-board.ts"
if [ ! -f "$BOARD" ]; then
  echo "== build-site: work plan SKIPPED: the platform at $PLAT has no cat-harness-tools/scripts/beans-board.ts (cat-harness-tools#2511; re-pin), so $SITE has no beans/."
else
  [ -d beans/defs ] || bun "$PLAT/cat-harness-tools/scripts/state-mount.ts" >/dev/null || true
  echo "== build-site: work plan (beans) -> $SITE/beans"
  set +e; bun run "$BOARD" --repo . --out "$SITE/beans" --title "Work plan"; rc=$?; set -e
  if [ "$rc" = 3 ]; then
    echo "== build-site: work plan SKIPPED: no bean store is mounted, so $SITE has no beans/."
  elif [ "$rc" != 0 ]; then
    echo "build-site: beans-board.ts failed (exit $rc)" >&2; exit "$rc"
  fi
fi

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
echo "== build-site: landing page -> $SITE/index.html"
python3 scripts/build-site-landing.py --site "$SITE"
echo "== build-site: done ($SITE)"
