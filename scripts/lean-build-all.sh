#!/usr/bin/env bash
# Build all Lean projects from the root Lake workspace.
#
# Discovers paper directories containing a lean-toolchain file and runs
# `lake build <target>` for each from the repo root (not a per-paper
# `cd`), so cross-package deps (e.g. qou → ugb) resolve via the root
# manifest instead of a possibly-stale per-paper manifest.
# Can be invoked from any directory.
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

# ── Root-workspace prep (update / cache once) ─────────────────────
cd "$REPO_ROOT"

if [ "$DO_UPDATE" = true ]; then
    echo "  → lake update (root workspace)"
    lake update 2>&1 | tail -5 || echo "  ⚠ lake update had warnings (continuing)"
fi

if [ "$DO_CACHE" = true ]; then
    echo "  → lake exe cache get (root workspace)"
    lake exe cache get 2>&1 | tail -5 || true
fi
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

    # Build from the root workspace so cross-package deps resolve via
    # the root manifest (a per-paper `cd` + `lake build` trips on a
    # stale per-paper manifest, e.g. qou's path dep on ugb).
    cd "$REPO_ROOT"

    # Derive the Lake library target (defaultTargets) from the paper's
    # lakefile, e.g. quantum-observable-universe → QOU.
    target=$(grep -E '^[[:space:]]*defaultTargets' "$lean_dir/lakefile.toml" 2>/dev/null \
                 | grep -oE '"[^"]+"' | tr -d '"' | head -1)
    if [ -z "$target" ]; then
        echo "  ⚠ no defaultTargets in $lean_dir/lakefile.toml — skipping"
        continue
    fi

    # Build
    echo "  → lake build $target"
    BUILD_START=$(date +%s)

    if lake build "$target" 2>&1; then
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
