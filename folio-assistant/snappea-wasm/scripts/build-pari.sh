#!/bin/bash
# Build PARI/GP 2.13.2 for WebAssembly using Emscripten
set -euo pipefail

PARI_VERSION="2.13.2"
PARI_URL="https://pari.math.u-bordeaux.fr/pub/pari/unix/pari-${PARI_VERSION}.tar.gz"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
BUILD_DIR="${ROOT_DIR}/build/pari"
PREFIX="${ROOT_DIR}/build/local"

echo "=== Building PARI ${PARI_VERSION} for WASM ==="

# Verify GMP was built
if [ ! -f "${PREFIX}/lib/libgmp.a" ]; then
    echo "ERROR: GMP not found at ${PREFIX}/lib/libgmp.a"
    echo "Run build-gmp.sh first."
    exit 1
fi

mkdir -p "$BUILD_DIR"

# Download if not cached
if [ ! -f "${BUILD_DIR}/pari-${PARI_VERSION}.tar.gz" ]; then
    echo "Downloading PARI ${PARI_VERSION}..."
    curl -L -o "${BUILD_DIR}/pari-${PARI_VERSION}.tar.gz" "$PARI_URL"
fi

# Extract
if [ ! -d "${BUILD_DIR}/pari-${PARI_VERSION}" ]; then
    echo "Extracting..."
    cd "$BUILD_DIR"
    tar xf "pari-${PARI_VERSION}.tar.gz"
fi

cd "${BUILD_DIR}/pari-${PARI_VERSION}"

# Configure for Emscripten with GMP
echo "Configuring PARI for Emscripten..."
emconfigure ./Configure \
    --host=wasm-emscripten \
    --graphic=none \
    --with-gmp-include="${PREFIX}/include" \
    --with-gmp-lib="${PREFIX}/lib"

# Patch: #undef UNIX to prevent getpwuid/popen calls
PARICFG="Olinux-wasm/paricfg.h"
if [ -f "$PARICFG" ] && ! grep -q "undef UNIX" "$PARICFG"; then
    echo "" >> "$PARICFG"
    echo "/* WASM patch: disable UNIX-specific functions */" >> "$PARICFG"
    echo "#undef UNIX" >> "$PARICFG"
    echo "Patched ${PARICFG}: #undef UNIX"
fi

# Build with Emscripten flags
echo "Building PARI..."
emmake make -j"$(nproc)" \
    CC_FLAVOR="-s ERROR_ON_UNDEFINED_SYMBOLS=0" \
    2>&1

echo "=== PARI build complete ==="
echo "Library: $(find . -name 'libpari.a' -o -name 'libpari*.a' | head -1)"
