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
#   document   (source) the Documents landing and one interactive page per
#              paper at en/<slug>/ (folio-assistant-core build-document-site.ts).
#              Stages the Lean sub-KGs first (below) and passes them as
#              --lean-docs-index, so each block's ∀ panel links into its own
#              paper's sub-KG.
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
#   lean       (site) the Lean library render, one sub-KG per Lake package
#              (owner, 2026-11-24, "separate qou, UGB and Fred2005 into own
#              lean sub-KGs"): /lean/qou/, /lean/ugb/, /lean/fred2005/, and
#              /lean/ a page listing them. Each is folio-assistant-sci
#              lean-kg-publish --from-kg over the Lean store mounted at lean/
#              (qou.json `lean-docs`), so the site never builds Lean. With
#              QOU_LEAN_RENDERER=verso, the Verso tool once it exists (owner
#              ruling 2026-11-24, "2 verso"; route verso/<package>/).
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
mkdir -p "$DIR"
DIR=$(cd "$DIR" && pwd)
LEAN_PACKAGES="qou:quantum-observable-universe ugb:unital-groebner-bases fred2005:fred2005-formal-groups"

# Stage the Lean sub-KGs under $1/lean/<package>/ from the mounted Lean store.
# Returns 1 (and says so) when the store is not mounted.
lean_subkgs() {
  local dest=$1 kg="$PLAT/folio-assistant-sci/adapters/paper/lean/lean-kg-publish.ts"
  [ -f lean/data/index.json ] || bun "$TOOLS/state-mount.ts" >/dev/null 2>&1 || true
  if [ ! -f lean/data/index.json ]; then
    echo "== site-step: Lean sub-KGs SKIPPED: the Lean store is not mounted at lean/ (state-mount)"
    return 1
  fi
  grep -q -- '--from-kg' "$kg" || { echo "site-step: $kg has no --from-kg (re-pin folio-assistant-sci)" >&2; exit 2; }
  local repo ref pkg paper o roots sib
  repo=$(python3 -I -c 'import json;print(json.load(open("qou.json"))["repository"])')
  ref=${SITE_COMMIT:-$(git rev-parse HEAD)}
  for pair in $LEAN_PACKAGES; do
    pkg=${pair%%:*}; paper=${pair#*:}
    roots=$(python3 -I scripts/site-extras.py --lean-roots "folio/$paper/lean/lakefile.toml")
    sib=()
    for other in $LEAN_PACKAGES; do
      o=${other%%:*}; [ "$o" = "$pkg" ] && continue
      sib+=(--sibling "$(python3 -I scripts/site-extras.py --lean-roots "folio/${other#*:}/lean/lakefile.toml" | tr , '\n' | sed "s#^#$o/#" | paste -sd,)")
    done
    bun run "$kg" --from-kg lean --site "$dest" --route "lean/$pkg" --modules "$roots" "${sib[@]}" \
      --repo "$repo" --ref "$ref" --content-prefix folio/ --no-rail | grep -v 'NOT railed' || true
    [ -f "$dest/lean/$pkg/data/index.json" ] || { echo "site-step: the $pkg sub-KG was not written" >&2; exit 1; }
  done
}

pages_pdf() {  # pages_pdf <slug> <dest>: the paper PDF paper-pdf.yml published on GitHub Pages
  local repo owner name
  repo=$(git config --get remote.origin.url | sed -E 's#^.*github\.com[:/]##; s#\.git$##')
  owner=${repo%%/*}; name=${repo#*/}
  [ -n "$owner" ] && [ -n "$name" ] || return 1
  curl -fsSL --max-time 300 -o "$2" "https://$owner.github.io/$name/papers/$1/$1.pdf" 2>/dev/null \
    && head -c 5 "$2" | grep -q '%PDF-' || { rm -f "$2"; return 1; }
}
papers() {  # every document the site builds: folio/<slug>/<slug>.ts
  for d in folio/*/; do s=$(basename "$d"); [ -f "folio/$s/$s.ts" ] && echo "$s"; done
}

case "$STEP" in
document)
  # The sub-KGs are staged beside the Jekyll source (never in it: Jekyll would
  # copy 225 MB of JSON), read here for the ∀ links, and moved into the site by
  # the lean step.
  STAGE="$(dirname "$DIR")/lean-subkg"
  rm -rf "$STAGE"
  LEAN_INDEX=()
  if lean_subkgs "$STAGE"; then LEAN_INDEX=(--lean-docs-index "$STAGE"); fi
  bun run "$PLAT/folio-assistant-core/scripts/build-document-site.ts" --landing-layout default --document-layout default --downloads --lazy-chapters "${LEAN_INDEX[@]}" --out "$DIR"
  ;;
landing)
  python3 -I scripts/site-extras.py --landing-source "$DIR"
  ;;
export)
  PDFDIR=${QOU_PDF_DIR:-$ROOT/build/site-pdf}
  for s in $(papers); do
    out="$DIR/en/$s/export"; mkdir -p "$out"
    pdf="$s-public-comment-latest.pdf"; docx="$s-public-comment-latest.docx"
    # A missing export is a QA finding, never a refused publish (owner ruling
    # 2026-11-27: the only pre-publish red gate is the KG JSON-LD check). The
    # site runner has no LaTeX, so the PDF comes from, in order: an earlier
    # build in $PDFDIR, a local LaTeX build when latexmk exists, or the copy
    # paper-pdf.yml published on GitHub Pages (papers/<slug>/<slug>.pdf).
    mkdir -p "$PDFDIR"
    if [ ! -f "$PDFDIR/$s.pdf" ] && command -v latexmk >/dev/null 2>&1; then
      echo "== site-step export: LaTeX PDF for $s"
      if bash scripts/build-paper-pdf.sh --paper "$s" --out-dir "$PDFDIR/$s" >"$PDFDIR.$s.log" 2>&1; then
        cp "$PDFDIR/$s/main.pdf" "$PDFDIR/$s.pdf"
      else
        echo "::warning::site-step export: build-paper-pdf.sh --paper $s failed; see $PDFDIR.$s.log"
      fi
    fi
    if [ ! -f "$PDFDIR/$s.pdf" ] && pages_pdf "$s" "$PDFDIR/$s.pdf"; then
      echo "== site-step export: PDF for $s from GitHub Pages (papers/$s/$s.pdf)"
    fi
    if [ -f "$PDFDIR/$s.pdf" ]; then
      cp "$PDFDIR/$s.pdf" "$out/$pdf"
    else
      echo "::warning::site-step export: no PDF for $s (no LaTeX here and none on GitHub Pages); the export page lists the Word file only"
    fi
    echo "== site-step export: Word for $s"
    # The Word file is document-export's editing copy (`docx`; Track Changes on, one
    # bookmark per block). Its `release` review copy needs LibreOffice for its PDF,
    # which this paper does not use (the PDF is LaTeX).
    if bun run "$PLAT/folio-assistant-core/scripts/document-export.ts" docx --document "$s" --repo "$ROOT" \
      --out "$PDFDIR/docx-$s" --allow-dirty >"$PDFDIR.$s.docx.log" 2>&1; then
      cp "$PDFDIR/docx-$s/$s-offline-latest.docx" "$out/$docx"
    else
      echo "::warning::site-step export: document-export docx --document $s failed:"
      tail -n 5 "$PDFDIR.$s.docx.log" | sed 's/^/  /'
    fi
    python3 -I scripts/site-extras.py --export-index "$out" --paper "$s"
  done
  ;;
accuracy)
  python3 -c "import mpmath" >/dev/null 2>&1 || python3 -m pip install --quiet mpmath
  # Owner ruling 2026-11-27: no red gates except JSON-LD KG publication. The page is
  # rendered from the current witnesses; the strict --check (ACCURACY.md drift,
  # stale witnesses) is reported to QA and never stops the publish.
  python3 scripts/generate-accuracy-scorecard.py --html-out "$DIR/accuracy/index.html"
  python3 scripts/generate-accuracy-scorecard.py --check --qa-report \
    || echo "::warning::site-step accuracy: --check failed (reported, not gated; see test/results/compute-qa/accuracy-scorecard.json)"
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
    # The sub-KGs site:document staged; staged here when it did not run.
    STAGE="$(dirname "$DIR")/lean-subkg"
    if [ ! -f "$STAGE/lean/qou/data/index.json" ]; then
      rm -rf "$STAGE"
      lean_subkgs "$STAGE" || { echo "== site-step lean SKIPPED: no sub-KGs"; exit 0; }
    fi
    mkdir -p "$DIR/lean"
    LIST=""
    for pair in $LEAN_PACKAGES; do
      pkg=${pair%%:*}; paper=${pair#*:}
      rm -rf "$DIR/lean/$pkg"; mv "$STAGE/lean/$pkg" "$DIR/lean/$pkg"
      n=$(python3 -I -c 'import json,sys;t=json.load(open(sys.argv[1]))["totals"];print("{:,} modules, {:,} declarations".format(t["modules"],t["decls"]))' "$DIR/lean/$pkg/data/index.json")
      title=$(python3 -I -c 'import json,sys;d=json.load(open("qou.json"));print(next((x["coverage"]["visualiser"][0]["title"] for x in d["directories"] if x["path"]==f"folio/{sys.argv[1]}/lean/"),sys.argv[1]))' "$paper")
      LIST="$LIST<li><a href=\"$pkg/\">$title</a> — Lake package <code>$pkg</code>, <a href=\"../en/$paper/\">its paper</a>; $n</li>"
      echo "== site-step lean: sub-KG $pkg -> /lean/$pkg/ ($n)"
    done
    rm -rf "$STAGE"
    cat > "$DIR/lean/index.html" <<HTML
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Lean | Quantum Observable Universe</title></head>
<body><main><h1>Lean</h1>
<p>One Lean knowledge graph per Lake package. A declaration one package uses from another links to that package's graph.</p>
<ul>$LIST</ul></main></body></html>
HTML
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
