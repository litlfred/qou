#!/bin/bash
# Setup SageMath for nuclear braid computations.
#
# Usage:
#   ./scripts/setup-sage.sh
#
# Installs SageMath via conda (fastest method).
# If conda is not available, falls back to system package manager.
#
# After install, run:
#   sage folio-assistant/computations/sage-nuclear-braid.sage

set -e

echo "=== SageMath setup for QOU nuclear braid computations ==="
echo

# Check if sage is already installed
if command -v sage &>/dev/null; then
    echo "SageMath already installed:"
    sage --version
    echo
    echo "Run the computation with:"
    echo "  sage folio-assistant/computations/sage-nuclear-braid.sage"
    exit 0
fi

# Try conda first (fastest, cleanest)
if command -v conda &>/dev/null; then
    echo "Installing SageMath via conda..."
    conda install -y -c conda-forge sage
    echo
    echo "Done. Run:"
    echo "  sage folio-assistant/computations/sage-nuclear-braid.sage"
    exit 0
fi

# Try mamba (faster conda)
if command -v mamba &>/dev/null; then
    echo "Installing SageMath via mamba..."
    mamba install -y -c conda-forge sage
    echo
    echo "Done. Run:"
    echo "  sage folio-assistant/computations/sage-nuclear-braid.sage"
    exit 0
fi

# macOS: try brew
if [[ "$(uname)" == "Darwin" ]]; then
    if command -v brew &>/dev/null; then
        echo "Installing SageMath via Homebrew (this takes a while)..."
        brew install --cask sage
        echo
        echo "Done. Run:"
        echo "  sage folio-assistant/computations/sage-nuclear-braid.sage"
        exit 0
    fi
fi

# Linux: try apt
if command -v apt &>/dev/null; then
    echo "Installing SageMath via apt..."
    sudo apt update
    sudo apt install -y sagemath
    echo
    echo "Done. Run:"
    echo "  sage folio-assistant/computations/sage-nuclear-braid.sage"
    exit 0
fi

# Nothing worked — suggest conda install
echo "No package manager found that can install SageMath."
echo
echo "Recommended: install miniforge (lightweight conda) first:"
echo "  curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-\$(uname)-\$(uname -m).sh"
echo "  bash Miniforge3-*.sh"
echo "  conda install -c conda-forge sage"
echo
echo "Or use Docker:"
echo "  docker run -v \$(pwd):/qou -w /qou sagemath/sagemath:latest sage folio-assistant/computations/sage-nuclear-braid.sage"
exit 1
