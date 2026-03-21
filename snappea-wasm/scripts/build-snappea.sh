#!/bin/bash
# Compile SnapPea kernel C source to WASM object files
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
SRC_DIR="${ROOT_DIR}/src"
BUILD_DIR="${ROOT_DIR}/build/snappea"

SNAPPEA_DIR="${SRC_DIR}/snappea"
HEADERS_DIR="${SNAPPEA_DIR}/headers"
BINDINGS_DIR="${SRC_DIR}/bindings"
STUBS_DIR="${SRC_DIR}/stubs"

CFLAGS="-O3 -Wall -Wno-unused-variable -Wno-unused-but-set-variable"
INCLUDES="-I${HEADERS_DIR} -I${BINDINGS_DIR}"

echo "=== Compiling SnapPea kernel for WASM ==="

mkdir -p "$BUILD_DIR"

compile_file() {
    local src="$1"
    local obj="${BUILD_DIR}/$(basename "${src%.c}.o")"
    echo "  CC $src"
    emcc ${CFLAGS} ${INCLUDES} -c "$src" -o "$obj"
}

# Compile kernel_code
echo "--- kernel_code ---"
for f in "${SNAPPEA_DIR}/kernel_code/"*.c; do
    compile_file "$f"
done

# Compile addl_code
echo "--- addl_code ---"
for f in "${SNAPPEA_DIR}/addl_code/"*.c; do
    compile_file "$f"
done

# Compile stubs
echo "--- stubs ---"
for f in "${STUBS_DIR}/"*.c; do
    compile_file "$f"
done

# Compile bindings
echo "--- bindings ---"
for f in "${BINDINGS_DIR}/"*.c; do
    compile_file "$f"
done

echo "=== SnapPea compilation complete ==="
echo "Object files: ${BUILD_DIR}/"
ls -la "${BUILD_DIR}/"*.o | wc -l
echo " .o files produced"
