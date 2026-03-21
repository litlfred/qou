#!/bin/bash
# Link all WASM objects into final snappea_kernel.wasm + .js
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
BUILD_DIR="${ROOT_DIR}/build"
DIST_DIR="${ROOT_DIR}/dist"
PREFIX="${BUILD_DIR}/local"

echo "=== Linking snappea_kernel WASM module ==="

mkdir -p "$DIST_DIR"

# Collect all SnapPea .o files
SNAPPEA_OBJECTS="${BUILD_DIR}/snappea/*.o"

# Check for PARI/GMP (optional for M1 milestone — stub if missing)
PARI_LIB=""
GMP_LIB=""
PARI_FLAGS=""

if [ -f "${PREFIX}/lib/libgmp.a" ]; then
    GMP_LIB="${PREFIX}/lib/libgmp.a"
    echo "GMP found: ${GMP_LIB}"
fi

PARI_A="$(find "${BUILD_DIR}/pari" -name 'libpari.a' 2>/dev/null | head -1 || true)"
if [ -n "$PARI_A" ]; then
    PARI_LIB="$PARI_A"
    PARI_FLAGS="-I${BUILD_DIR}/pari/pari-*/src/headers"
    echo "PARI found: ${PARI_LIB}"
fi

# Exported functions
EXPORTED_FUNCTIONS="[
  '_snappea_init',
  '_snappea_destroy',
  '_snappea_triangulation_from_string',
  '_snappea_triangulation_to_string',
  '_snappea_free_string',
  '_snappea_copy_triangulation',
  '_snappea_free_triangulation',
  '_snappea_get_name',
  '_snappea_get_num_tetrahedra',
  '_snappea_get_num_cusps',
  '_snappea_get_num_or_cusps',
  '_snappea_get_num_nonor_cusps',
  '_snappea_get_orientability',
  '_snappea_find_complete_hyperbolic_structure',
  '_snappea_volume',
  '_snappea_solution_type',
  '_snappea_set_cusp_info',
  '_snappea_do_dehn_filling',
  '_snappea_remove_dehn_fillings',
  '_snappea_get_cusp_m_l',
  '_snappea_get_cusp_topology',
  '_snappea_get_tet_shape',
  '_snappea_chern_simons',
  '_snappea_simplify',
  '_snappea_orient',
  '_snappea_canonize',
  '_snappea_homology',
  '_snappea_fundamental_group',
  '_snappea_version',
  '_malloc',
  '_free'
]"

# Remove newlines for emcc
EXPORTED_FUNCTIONS="$(echo "$EXPORTED_FUNCTIONS" | tr -d '\n' | tr -s ' ')"

EXPORTED_RUNTIME="['ccall','cwrap','UTF8ToString','stringToUTF8','getValue','setValue','allocateUTF8']"

echo "Linking..."
emcc \
    -O3 \
    ${SNAPPEA_OBJECTS} \
    ${PARI_LIB} \
    ${GMP_LIB} \
    -s WASM=1 \
    -s ALLOW_MEMORY_GROWTH=1 \
    -s INITIAL_MEMORY=67108864 \
    -s EXPORTED_FUNCTIONS="${EXPORTED_FUNCTIONS}" \
    -s EXPORTED_RUNTIME_METHODS="${EXPORTED_RUNTIME}" \
    -s MODULARIZE=1 \
    -s EXPORT_NAME="createSnapPeaModule" \
    -s EXPORT_ES6=0 \
    -s ENVIRONMENT='web,node,worker' \
    -s FILESYSTEM=1 \
    -s NO_EXIT_RUNTIME=1 \
    -s ERROR_ON_UNDEFINED_SYMBOLS=0 \
    -lm \
    -o "${DIST_DIR}/snappea_kernel.js"

echo "=== Link complete ==="
ls -lh "${DIST_DIR}/snappea_kernel.js" "${DIST_DIR}/snappea_kernel.wasm"
echo "Total WASM size: $(du -sh "${DIST_DIR}/snappea_kernel.wasm" | cut -f1)"
