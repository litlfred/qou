#!/usr/bin/env bash
# Build all Lean projects in the content/ directory.
#
# Discovers paper directories containing a lean-toolchain file
# and runs `lake build` in each. Can be invoked from any directory.
#
# Usage:
#   ./scripts/lean-build-all.sh           # build all papers
#   ./scripts/lean-build-all.sh --paper quantum-observable-universe
#   ./scripts/lean-build-all.sh --cache   # fetch Mathlib cache first
#   ./scripts/lean-build-all.sh --update  # run lake update first
#
# Exit code: 0 if all builds succeed, 1 if any fail.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CONTENT_DIR="$REPO_ROOT/content"

export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH"

# ── Parse args ────────────────────────────────────────────────────
FILTER_PAPER=""
DO_CACHE=false
DO_UPDATE=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --paper)  FILTER_PAPER="$2"; shift 2 ;;
        --cache)  DO_CACHE=true; shift ;;
        --update) DO_UPDATE=true; shift ;;
        -h|--help)
            echo "Usage: $0 [--paper NAME] [--cache] [--update]"
            echo "  --paper NAME   Build only the named paper"
            echo "  --cache        Run 'lake exe cache get' before building"
            echo "  --update       Run 'lake update' before building"
            exit 0 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

# ── Pre-check ─────────────────────────────────────────────────────
if ! command -v lake &>/dev/null; then
    echo "Error: lake not found. Install Lean via: curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh"
    exit 1
fi

# ── Discover Lean projects ────────────────────────────────────────
# A Lean project is a directory under content/<paper>/lean/ that
# contains a lean-toolchain file.
LEAN_DIRS=()

for paper_dir in "$CONTENT_DIR"/*/; do
    paper_name=$(basename "$paper_dir")

    # Filter if --paper was given
    if [ -n "$FILTER_PAPER" ] && [ "$paper_name" != "$FILTER_PAPER" ]; then
        continue
    fi

    lean_dir="$paper_dir/lean"
    if [ -f "$lean_dir/lean-toolchain" ]; then
        LEAN_DIRS+=("$lean_dir")
    fi
done

if [ ${#LEAN_DIRS[@]} -eq 0 ]; then
    if [ -n "$FILTER_PAPER" ]; then
        echo "No Lean project found for paper: $FILTER_PAPER"
    else
        echo "No Lean projects found in $CONTENT_DIR"
    fi
    exit 1
fi

echo "Found ${#LEAN_DIRS[@]} Lean project(s):"
for d in "${LEAN_DIRS[@]}"; do
    paper=$(basename "$(dirname "$d")")
    toolchain=$(cat "$d/lean-toolchain" 2>/dev/null)
    echo "  $paper  ($toolchain)"
done
echo ""

# ── Build each project ────────────────────────────────────────────
TOTAL=0
PASSED=0
FAILED_PAPERS=()

for lean_dir in "${LEAN_DIRS[@]}"; do
    paper=$(basename "$(dirname "$lean_dir")")
    TOTAL=$((TOTAL + 1))

    echo "═══════════════════════════════════════════════════════"
    echo "  Building: $paper"
    echo "  Directory: $lean_dir"
    echo "═══════════════════════════════════════════════════════"

    cd "$lean_dir"

    # Optional: lake update
    if [ "$DO_UPDATE" = true ]; then
        echo "  → lake update"
        if ! lake update 2>&1 | tail -5; then
            echo "  ⚠ lake update had warnings (continuing)"
        fi
    fi

    # Optional: fetch Mathlib cache
    if [ "$DO_CACHE" = true ]; then
        echo "  → lake exe cache get"
        lake exe cache get 2>&1 | tail -5 || true
    fi

    # Build
    echo "  → lake build"
    BUILD_START=$(date +%s)

    if lake build 2>&1; then
        BUILD_END=$(date +%s)
        elapsed=$((BUILD_END - BUILD_START))
        echo ""
        echo "  ✓ $paper built successfully (${elapsed}s)"
        PASSED=$((PASSED + 1))
    else
        BUILD_END=$(date +%s)
        elapsed=$((BUILD_END - BUILD_START))
        echo ""
        echo "  ✗ $paper build FAILED (${elapsed}s)"
        FAILED_PAPERS+=("$paper")
    fi
    echo ""
done

# ── Summary ───────────────────────────────────────────────────────
echo "═══════════════════════════════════════════════════════"
echo "  Results: $PASSED/$TOTAL passed"
if [ ${#FAILED_PAPERS[@]} -gt 0 ]; then
    echo "  Failed:  ${FAILED_PAPERS[*]}"
fi
echo "═══════════════════════════════════════════════════════"

[ ${#FAILED_PAPERS[@]} -eq 0 ]
