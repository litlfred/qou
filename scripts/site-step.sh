#!/usr/bin/env bash
# site-step.sh — qou's own steps in the platform's site build.
#
#   bash scripts/site-step.sh <step> <dir>
#
# qou is a platform layer (owner ruling 2026-11-24, "1 qou is platform
# later"), and its site is built as the dth-hrh folio's is: cat-harness-tools'
# build-instance-site.ts runs the recipe in index.config.json (`site.build`),
# each entry a package script from package.json. The `site:<step>` scripts
# call this file. A SOURCE step gets the Jekyll source directory; a SITE step
# gets the built site (see build-instance-site.ts). Every step says what it
# skipped and why; none is silently empty.
#
# Steps:
#   landing    (source) the rest of the root landing: the declared pages
#              (Accuracy, QA, Work plan, Lean), CONTRIBUTING, LICENSE, source,
#              appended under the Documents list site:document writes.
#   export     (site) each paper's exports at en/<slug>/export/, under the
#              platform's stable names (document-export.ts `latestNames`):
#              the LaTeX PDF (scripts/build-paper-pdf.sh; pandoc PDF is not
#              used for this paper, see that script's header) and the Word
#              .docx (document-export.ts docx), plus an index.html listing them.
#   accuracy   (site) the 80-dps accuracy scorecard QA gate + HTML, /accuracy/.
#   beans      (site) the work plan, /beans/ (cat-harness-tools beans-board.ts).
#   qa         (site) the integrated QA panel, /qa/ (qa-page-standalone.ts).
#   lean       (site) the Lean library render, /lean/. ONE declared slot with a
#              renderer chosen by QOU_LEAN_RENDERER: `store` (default) copies
#              the stored render mounted at lean/ (qou.json `lean-docs`);
#              `verso` runs folio-assistant-sci's Verso tool once it exists
#              (owner ruling 2026-11-24, "2 verso"). Never builds Lean.
#   papers     (site) /papers/<slug>/ -> the paper's page en/<slug>/, keeping
#              ?query#fragment. Files already on gh-pages under papers/ are
#              not this build's to touch.
#   relink     (site) the papers' own links the page cannot serve: a block's
#              .md -> its anchor, an image or simulator copied in, any other
#              repository file -> GitHub at this commit (site-extras.py --relink).
#   repo-files (site) CONTRIBUTING (/contributing/) and LICENSE (/LICENSE.txt).
set -euo pipefail
STEP=${1:?step}; DIR=${2:?site or source dir}
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"
. scripts/lib/platform-root.sh
PLAT=$(qou_platform_root "$ROOT") || { echo "site-step: no platform (mount the layers: bash .github/mount-from-lock.sh)" >&2; exit 2; }
TOOLS="$PLAT/cat-harness-tools/scripts"
DIR=$(cd "$DIR" && pwd)

papers() {  # every document the site builds: folio/<slug>/<slug>.ts
  for d in folio/*/; do s=$(basename "$d"); [ -f "folio/$s/$s.ts" ] && echo "$s"; done
}

case "$STEP" in
landing)
  python3 -I scripts/site-extras.py --landing-source "$DIR"
  ;;
export)
  PDFDIR=${QOU_PDF_DIR:-$ROOT/build/site-pdf}
  for s in $(papers); do
    out="$DIR/en/$s/export"; mkdir -p "$out"
    pdf="$s-public-comment-latest.pdf"; docx="$s-public-comment-latest.docx"
    if [ ! -f "$PDFDIR/$s.pdf" ]; then
      echo "== site-step export: LaTeX PDF for $s"
      bash scripts/build-paper-pdf.sh --paper "$s" --out-dir "$PDFDIR/$s" >"$PDFDIR.$s.log" 2>&1 \
        || { echo "site-step export: build-paper-pdf.sh --paper $s failed; see $PDFDIR.$s.log" >&2; exit 1; }
      cp "$PDFDIR/$s/main.pdf" "$PDFDIR/$s.pdf"
    fi
    cp "$PDFDIR/$s.pdf" "$out/$pdf"
    echo "== site-step export: Word for $s"
    bun run "$PLAT/folio-assistant-core/scripts/document-export.ts" docx --document "$s" --repo "$ROOT" \
      --out "$PDFDIR/docx-$s" --allow-dirty >"$PDFDIR.$s.docx.log" 2>&1 \
      || { echo "site-step export: document-export docx --document $s failed; see $PDFDIR.$s.docx.log" >&2; exit 1; }
    # The Word file is document-export's editing copy (`docx`; Track Changes on, one
    # bookmark per block). Its `release` review copy needs LibreOffice for its PDF,
    # which this paper does not use (the PDF is LaTeX).
    cp "$PDFDIR/docx-$s/$s-offline-latest.docx" "$out/$docx"
    python3 -I scripts/site-extras.py --export-index "$out" --paper "$s"
  done
  ;;
accuracy)
  python3 -c "import mpmath" >/dev/null 2>&1 || python3 -m pip install --quiet mpmath
  python3 scripts/generate-accuracy-scorecard.py --check --qa-report --html-out "$DIR/accuracy/index.html"
  ;;
beans)
  BOARD="$TOOLS/beans-board.ts"
  if [ ! -f "$BOARD" ]; then
    echo "== site-step beans SKIPPED: the mounted cat-harness-tools has no scripts/beans-board.ts (cat-harness-tools#2511; re-pin), so the site has no beans/."
    exit 0
  fi
  [ -d beans/defs ] || bun "$TOOLS/state-mount.ts" >/dev/null || true
  set +e; bun run "$BOARD" --repo . --out "$DIR/beans" --title "Work plan"; rc=$?; set -e
  [ "$rc" = 3 ] && { echo "== site-step beans SKIPPED: no bean store is mounted."; exit 0; }
  exit "$rc"
  ;;
qa)
  QAPAGE="$TOOLS/qa-page-standalone.ts"
  if [ ! -f "$QAPAGE" ]; then
    echo "== site-step qa SKIPPED: the mounted cat-harness-tools has no scripts/qa-page-standalone.ts (cat-harness-tools#2512; re-pin), so the site has no qa/."
    exit 0
  fi
  bun run "$QAPAGE" --repo . --out "$DIR/qa"
  ;;
lean)
  case "${QOU_LEAN_RENDERER:-store}" in
  store)
    [ -f lean/data/index.json ] || bun "$TOOLS/state-mount.ts" >/dev/null || true
    if [ -f lean/index.html ] && [ -f lean/data/index.json ]; then
      rm -rf "$DIR/lean" && mkdir -p "$DIR/lean" && cp -a lean/. "$DIR/lean/"
      echo "== site-step lean: the stored render (lean/, cat/folio-assistant-sci/lean-docs) -> /lean/"
    else
      echo "== site-step lean SKIPPED: the Lean store is not mounted at lean/ (state-mount), so the site has no lean/."
    fi
    ;;
  verso)
    VERSO="$PLAT/folio-assistant-sci/tools/verso-render/verso-render.ts"
    [ -f "$VERSO" ] || { echo "site-step lean: QOU_LEAN_RENDERER=verso but $VERSO is not on the mounted folio-assistant-sci (re-pin)" >&2; exit 2; }
    bun run "$VERSO" --repo . --site "$DIR" --route lean
    ;;
  *) echo "site-step lean: unknown QOU_LEAN_RENDERER=$QOU_LEAN_RENDERER (store|verso)" >&2; exit 2 ;;
  esac
  ;;
papers)
  python3 -I scripts/site-extras.py --redirects "$DIR"
  ;;
relink)
  python3 -I scripts/site-extras.py --relink "$DIR"
  ;;
repo-files)
  mkdir -p "$DIR/contributing"
  cp LICENSE "$DIR/LICENSE.txt"
  python3 -I scripts/site-extras.py --contributing CONTRIBUTING.md --out "$DIR/contributing/index.html"
  ;;
*) echo "site-step: unknown step $STEP" >&2; exit 2 ;;
esac
