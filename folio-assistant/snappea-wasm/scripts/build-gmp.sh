#!/bin/bash
# Build GMP 6.2.1 for WebAssembly using Emscripten
set -euo pipefail

GMP_VERSION="6.2.1"
GMP_URL="https://gmplib.org/download/gmp/gmp-${GMP_VERSION}.tar.xz"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
BUILD_DIR="${ROOT_DIR}/build/gmp"
PREFIX="${ROOT_DIR}/build/local"

echo "=== Building GMP ${GMP_VERSION} for WASM ==="

mkdir -p "$BUILD_DIR" "$PREFIX"

# Download if not cached
if [ ! -f "${BUILD_DIR}/gmp-${GMP_VERSION}.tar.xz" ]; then
    echo "Downloading GMP ${GMP_VERSION}..."
    curl -L -o "${BUILD_DIR}/gmp-${GMP_VERSION}.tar.xz" "$GMP_URL"
fi

# Extract
if [ ! -d "${BUILD_DIR}/gmp-${GMP_VERSION}" ]; then
    echo "Extracting..."
    cd "$BUILD_DIR"
    tar xf "gmp-${GMP_VERSION}.tar.xz"
fi

cd "${BUILD_DIR}/gmp-${GMP_VERSION}"

# Configure for Emscripten
# --disable-assembly: GMP's hand-tuned asm won't work in WASM
# --build/--host: cross-compile settings
# ABI=standard: avoid ABI detection issues
echo "Configuring GMP for Emscripten..."
emconfigure ./configure \
    --build i686-pc-linux-gnu \
    --host=none \
    --disable-assembly \
    --prefix="$PREFIX" \
    CFLAGS="-O3 -Wall" \
    CC_FOR_BUILD=gcc \
    ABI=standard

# Build
echo "Building GMP..."
emmake make -j"$(nproc)" 2>&1

# Install
echo "Installing GMP to ${PREFIX}..."
emmake make install

echo "=== GMP build complete ==="
echo "Headers: ${PREFIX}/include/"
echo "Library: ${PREFIX}/lib/libgmp.a"
