#!/usr/bin/env bash
# Build the QOU paper PDF locally (no Docker required).
#
# Prerequisites:
#   - latexmk, pdflatex (texlive-full)
#   - Node.js + npx (for content pipeline via tsx)
#   - Bun (for installing content deps, if node_modules missing)
#
# Usage:
#   ./scripts/build-pdf.sh                          # build current branch
#   ./scripts/build-pdf.sh --branch main            # checkout branch, build, return
#   ./scripts/build-pdf.sh --branch feature/foo     # same for any branch
#   ./scripts/build-pdf.sh --tex-only               # skip content pipeline
#   ./scripts/build-pdf.sh --clean                  # clean aux files first
#   ./scripts/build-pdf.sh --diff main              # generate latexdiff vs branch
#
# Output: build/<branch-slug>.pdf  (or build/main.pdf, etc.)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PAPER="${PAPER:-quantum-observable-universe}"
TEX_ONLY=false
CLEAN=false
STRICT=false
BRANCH=""
DIFF_BASE=""
BUILD_DIR="$REPO_ROOT/build"

usage() {
  cat <<'USAGE'
Usage: build-pdf.sh [OPTIONS]

Options:
  --branch REF   Checkout REF before building (returns to original branch after)
  --diff BASE    After building, generate a latexdiff PDF against BASE branch
  --tex-only     Skip content pipeline, compile existing .tex files
  --clean        Remove LaTeX aux files before compilation
  --strict       Fail on LaTeX errors (no -f flag)
  --paper DIR    Paper directory name (default: quantum-observable-universe)
  --help         Show this help

Examples:
  ./scripts/build-pdf.sh                        # build current branch
  ./scripts/build-pdf.sh --branch main          # build main, return to current
  ./scripts/build-pdf.sh --branch feature/x --diff main   # build + diff vs main
USAGE
  exit 0
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --branch)   BRANCH="$2"; shift 2 ;;
    --diff)     DIFF_BASE="$2"; shift 2 ;;
    --tex-only) TEX_ONLY=true; shift ;;
    --clean)    CLEAN=true; shift ;;
    --strict)   STRICT=true; shift ;;
    --paper)    PAPER="$2"; shift 2 ;;
    --help)     usage ;;
    *)          echo "Unknown option: $1"; usage ;;
  esac
done

cd "$REPO_ROOT"

# ── Verify tools ────────────────────────────────────────────────
for cmd in latexmk pdflatex node npx; do
  if ! command -v "$cmd" &>/dev/null; then
    echo "ERROR: $cmd not found. Install texlive-full and Node.js." >&2
    exit 1
  fi
done

# ── Branch switching ────────────────────────────────────────────
ORIGINAL_BRANCH=""
if [ -n "$BRANCH" ]; then
  ORIGINAL_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || git rev-parse --short HEAD)
  if [ "$ORIGINAL_BRANCH" = "$BRANCH" ]; then
    ORIGINAL_BRANCH=""
  else
    # Ensure clean working tree before switching
    if ! git diff --quiet || ! git diff --cached --quiet; then
      echo "ERROR: Working tree has uncommitted changes. Commit or stash first." >&2
      exit 1
    fi
    echo "==> Switching to branch: $BRANCH"
    git switch "$BRANCH" && git pull origin "$BRANCH"
  fi
fi

# Return to original branch on exit (success or failure)
cleanup() {
  if [ -n "$ORIGINAL_BRANCH" ]; then
    echo "==> Returning to branch: $ORIGINAL_BRANCH"
    git checkout "$ORIGINAL_BRANCH" --
  fi
}
trap cleanup EXIT

# ── Determine output name ───────────────────────────────────────
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "detached")
BRANCH_SLUG=$(echo "$CURRENT_BRANCH" | sed 's|[/:]|-|g; s|[^a-zA-Z0-9._-]||g')
mkdir -p "$BUILD_DIR"

# ── Clean aux files if requested ────────────────────────────────
if [ "$CLEAN" = true ]; then
  echo "==> Cleaning LaTeX aux files..."
  rm -f main.aux main.log main.fls main.fdb_latexmk main.out main.toc \
       main.lof main.lot main.bbl main.blg main.bcf main.run.xml \
       main.synctex.gz main.pdf
fi

# ── Content pipeline ────────────────────────────────────────────
if [ "$TEX_ONLY" = false ]; then
  echo "==> Running content pipeline..."
  cd content
  if [ ! -d node_modules ]; then
    echo "    Installing dependencies..."
    if command -v bun &>/dev/null; then
      bun install --frozen-lockfile
    else
      echo "ERROR: Bun required for content deps (bun.lock). Use --tex-only to skip." >&2
      exit 1
    fi
  fi

  echo "    Building LaTeX from content objects..."
  npx tsx ../scripts/docker-latex-build/run-build.ts \
    "$PAPER/$PAPER.ts" \
    --out-dir ../chapters/ \
    --generate-main --main-out ../main.tex \
    --preamble ../latex/preamble.tex

  echo "    Exporting BibTeX..."
  npx tsx pipeline/export-bibtex.ts

  cd "$REPO_ROOT"
  echo "==> Content pipeline complete."
else
  echo "==> Skipping content pipeline (--tex-only)"
  if [ ! -f main.tex ]; then
    echo "ERROR: main.tex not found. Run without --tex-only first." >&2
    exit 1
  fi
fi

# ── LaTeX compilation ───────────────────────────────────────────
LATEXMK_FLAGS="-pdf -interaction=nonstopmode"
if [ "$STRICT" = false ]; then
  LATEXMK_FLAGS="$LATEXMK_FLAGS -f"
else
  LATEXMK_FLAGS="$LATEXMK_FLAGS -halt-on-error"
fi

echo "==> Compiling PDF with latexmk..."
latexmk $LATEXMK_FLAGS main.tex

if [ -f main.pdf ]; then
  cp main.pdf "$BUILD_DIR/$BRANCH_SLUG.pdf"
  SIZE=$(du -h main.pdf | cut -f1)
  PAGES=$(pdfinfo main.pdf 2>/dev/null | grep Pages | awk '{print $2}' || echo "?")
  echo "==> SUCCESS: build/$BRANCH_SLUG.pdf ($SIZE, $PAGES pages)"
else
  echo "==> FAILED: main.pdf not produced" >&2
  exit 1
fi

# ── Standalone appendices ───────────────────────────────────────
for tex in standalone-*.tex; do
  [ -f "$tex" ] || continue
  echo "==> Compiling standalone: $tex"
  latexmk $LATEXMK_FLAGS "$tex"
  base=$(basename "$tex" .tex)
  cp "$base.pdf" "$BUILD_DIR/" 2>/dev/null || true
done

# ── Diff PDF (optional) ────────────────────────────────────────
if [ -n "$DIFF_BASE" ]; then
  if ! command -v latexdiff &>/dev/null; then
    echo "WARNING: latexdiff not found, skipping diff PDF." >&2
  elif ! command -v latexpand &>/dev/null; then
    echo "WARNING: latexpand not found, skipping diff PDF." >&2
  else
    echo "==> Generating diff against $DIFF_BASE..."

    # Flatten current branch
    latexpand main.tex > "$BUILD_DIR/branch-flat.tex" 2>/dev/null

    # Build base branch in a temp worktree
    WORKTREE_DIR=$(mktemp -d)
    git worktree add "$WORKTREE_DIR" "$DIFF_BASE" --quiet 2>/dev/null

    (
      cd "$WORKTREE_DIR"
      if [ -d content/node_modules ] || [ -L content/node_modules ]; then
        true  # deps available
      elif [ -d "$REPO_ROOT/content/node_modules" ]; then
        ln -s "$REPO_ROOT/content/node_modules" content/node_modules
      fi
      cd content
      npx tsx ../scripts/docker-latex-build/run-build.ts \
        "$PAPER/$PAPER.ts" \
        --out-dir ../chapters/ \
        --generate-main --main-out ../main.tex \
        --preamble ../latex/preamble.tex 2>/dev/null || true
      npx tsx pipeline/export-bibtex.ts 2>/dev/null || true
      cd ..
      latexpand main.tex > "$BUILD_DIR/base-flat.tex" 2>/dev/null
    )

    git worktree remove "$WORKTREE_DIR" --force 2>/dev/null || rm -rf "$WORKTREE_DIR"

    if [ -f "$BUILD_DIR/base-flat.tex" ] && [ -f "$BUILD_DIR/branch-flat.tex" ]; then
      latexdiff "$BUILD_DIR/base-flat.tex" "$BUILD_DIR/branch-flat.tex" \
        --type=CFONT > "$BUILD_DIR/diff.tex" 2>/dev/null
      (cd "$BUILD_DIR" && latexmk -pdf -interaction=nonstopmode -f diff.tex 2>/dev/null)
      if [ -f "$BUILD_DIR/diff.pdf" ]; then
        mv "$BUILD_DIR/diff.pdf" "$BUILD_DIR/$BRANCH_SLUG-diff-vs-${DIFF_BASE//\//-}.pdf"
        echo "==> Diff PDF: build/$BRANCH_SLUG-diff-vs-${DIFF_BASE//\//-}.pdf"
      else
        echo "WARNING: Diff PDF compilation failed." >&2
      fi
    else
      echo "WARNING: Could not flatten base branch TeX." >&2
    fi

    # Cleanup temp files
    rm -f "$BUILD_DIR/base-flat.tex" "$BUILD_DIR/branch-flat.tex" \
          "$BUILD_DIR/diff.tex" "$BUILD_DIR/diff.aux" "$BUILD_DIR/diff.log" \
          "$BUILD_DIR/diff.fls" "$BUILD_DIR/diff.fdb_latexmk" "$BUILD_DIR/diff.out"
  fi
fi

echo "==> Build complete. Output in build/"
