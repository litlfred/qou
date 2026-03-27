#!/usr/bin/env bash
# Run all Sage witness computations for the QOU open problems.
#
# Usage (from repo root — copy-paste this single line):
#
#   ./scripts/setup-sage.sh && ./scripts/run-sage-witnesses.sh
#
# Or if Sage is already installed:
#
#   ./scripts/run-sage-witnesses.sh
#
# Output:
#   folio-assistant/computations/sage-borromean-gA.witness.json
#   folio-assistant/computations/sage-cgeom.witness.json
#   folio-assistant/computations/sage-nuclear-braid.witness.json

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
COMP_DIR="$REPO_ROOT/folio-assistant/computations"

echo "═══════════════════════════════════════════════════════════"
echo "QOU Sage witness computations"
echo "═══════════════════════════════════════════════════════════"
echo

# Check Sage is available
if ! command -v sage &>/dev/null; then
    echo "✗ SageMath not found."
    echo
    echo "If you installed via conda, activate the environment first:"
    echo
    echo "  conda activate qou-sage && ./scripts/run-sage-witnesses.sh"
    echo
    echo "If not installed yet:"
    echo
    echo "  ./scripts/setup-sage.sh"
    echo
    exit 1
fi

echo "▸ Sage version: $(sage --version 2>&1 | head -1)"
echo

# ── 1. g_A from Borromean Hecke algebra ──────────────────────────
echo "═══ [1/3] g_A from Borromean Hecke algebra ═══"
echo "    Target: g_A = 1.2754 (PDG 2024)"
echo
sage "$COMP_DIR/sage-borromean-gA.sage" && \
  echo && echo "✓ g_A computation complete" && echo

# ── 2. C_geom from electron-proton Skein weight ─────────────────
echo "═══ [2/3] C_geom from electron-proton Skein weight ═══"
echo "    Target: C_geom ≈ 14.25"
echo
sage "$COMP_DIR/sage-cgeom.sage" && \
  echo && echo "✓ C_geom computation complete" && echo

# ── 3. Nuclear braid traces (existing) ──────────────────────────
echo "═══ [3/3] Nuclear braid Markov traces ═══"
echo
sage "$COMP_DIR/sage-nuclear-braid.sage" && \
  echo && echo "✓ Nuclear braid computation complete"
echo

# ── Summary ──────────────────────────────────────────────────────
echo "═══════════════════════════════════════════════════════════"
echo "All witness files:"
echo
ls -la "$COMP_DIR"/sage-*.witness.json 2>/dev/null || echo "(none found)"
echo
echo "To review results:"
echo "  cat folio-assistant/computations/sage-borromean-gA.witness.json | python3 -m json.tool"
echo "  cat folio-assistant/computations/sage-cgeom.witness.json | python3 -m json.tool"
echo "═══════════════════════════════════════════════════════════"
