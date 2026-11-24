#!/usr/bin/env bash
# build-site — build qou's published site into $SITE_DIR (default _site).
#
# qou is a platform LAYER (owner ruling 2026-11-24, "1 qou is platform later"),
# set up as the dth-hrh folio is, so its site is built by the platform's own
# route: cat-harness-tools' build-instance-site.ts, the same command
# stage-local.ts and the reusable folio-site-publish.yml run. It reads the
# recipe in index.config.json (`site.build`), whose steps are package scripts:
#
#   site:document  (source) the "Documents" landing and one interactive page per
#                  paper at en/<slug>/ (folio-assistant-core build-document-site.ts)
#   site:landing   (source) CONTRIBUTING, LICENSE and the source on the landing
#   Jekyll + the platform chrome, the left navbar (rail) on every page
#   site:export    the LaTeX PDF and the Word file per paper, en/<slug>/export/
#   site:accuracy  /accuracy/   site:beans /beans/   site:qa /qa/
#   site:lean      /lean/ (the declared Lean slot; stored render until Verso)
#   site:papers    /papers/<slug>/ -> en/<slug>/
#   site:repo-files  /contributing/, /LICENSE.txt
#   then the platform's link check, which refuses a site with a dead link.
#
# The steps themselves are scripts/site-step.sh. The layers are mounted at the
# repository root from index.lock.json; when they are absent this mounts them
# (.github/mount-from-lock.sh). It builds and checks; it never publishes —
# scripts/publish-main-local.sh does that.
#
# Environment: SITE_DIR (default _site), SITE_WORK (default build/site-work:
# Jekyll source, gems, logs), QOU_PDF_DIR (prebuilt <slug>.pdf files; default
# build/site-pdf, built on demand), QOU_LEAN_RENDERER (store|verso).
set -euo pipefail
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"
SITE=${SITE_DIR:-_site}
WORK=${SITE_WORK:-$ROOT/build/site-work}

if [ ! -f cat-harness-tools/scripts/build-instance-site.ts ]; then
  echo "== build-site: mounting the platform layers from index.lock.json"
  bash .github/mount-from-lock.sh --root "$ROOT"
fi
[ -d node_modules ] || bun install

rm -rf "$WORK/_site"
bun run cat-harness-tools/scripts/build-instance-site.ts --root . --instance qou \
  --out "$WORK" --no-mount "$@"

rm -rf "$SITE"
mkdir -p "$(dirname "$SITE")"
cp -a "$WORK/_site" "$SITE"
echo "== build-site: done ($SITE)"
