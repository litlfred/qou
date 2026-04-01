/*
 *  snappea_wasm.h
 *
 *  C API for the SnapPea WASM module.
 *  These functions are exported via Emscripten EXPORTED_FUNCTIONS
 *  and called from JavaScript via ccall/cwrap.
 */

#ifndef SNAPPEA_WASM_H
#define SNAPPEA_WASM_H

#ifdef __EMSCRIPTEN__
#include <emscripten/emscripten.h>
#define WASM_EXPORT EMSCRIPTEN_KEEPALIVE
#else
#define WASM_EXPORT
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* --- Lifecycle --- */

/* Initialize the SnapPea WASM module. Call once before any other function.
 * Returns 0 on success, nonzero on failure. */
WASM_EXPORT int snappea_init(void);

/* Clean up all resources. */
WASM_EXPORT void snappea_destroy(void);

/* --- Triangulation I/O --- */

/* Create a triangulation from a SnapPea-format string.
 * Returns an opaque handle (pointer), or 0 on failure. */
WASM_EXPORT void *snappea_triangulation_from_string(const char *data);

/* Serialize a triangulation to a SnapPea-format string.
 * Caller must free the returned string with snappea_free_string(). */
WASM_EXPORT const char *snappea_triangulation_to_string(void *tri);

/* Free a string returned by snappea_triangulation_to_string. */
WASM_EXPORT void snappea_free_string(char *s);

/* Copy a triangulation. Returns new handle. */
WASM_EXPORT void *snappea_copy_triangulation(void *tri);

/* Free a triangulation. */
WASM_EXPORT void snappea_free_triangulation(void *tri);

/* --- Basic properties --- */

WASM_EXPORT const char *snappea_get_name(void *tri);
WASM_EXPORT int snappea_get_num_tetrahedra(void *tri);
WASM_EXPORT int snappea_get_num_cusps(void *tri);
WASM_EXPORT int snappea_get_num_or_cusps(void *tri);
WASM_EXPORT int snappea_get_num_nonor_cusps(void *tri);

/* Returns 1 for orientable, 0 for non-orientable */
WASM_EXPORT int snappea_get_orientability(void *tri);

/* --- Hyperbolic structure --- */

/* Compute the complete hyperbolic structure.
 * Returns the SolutionType as an integer (see SnapPea.h enum). */
WASM_EXPORT int snappea_find_complete_hyperbolic_structure(void *tri);

/* Get the volume. Returns 0.0 if no structure computed. */
WASM_EXPORT double snappea_volume(void *tri);

/* Get the solution type as integer. */
WASM_EXPORT int snappea_solution_type(void *tri);

/* --- Dehn filling --- */

/* Set filling coefficients on a cusp. */
WASM_EXPORT void snappea_set_cusp_info(void *tri, int cusp_index,
                                        double m, double l);

/* Compute filled structure. Returns SolutionType. */
WASM_EXPORT int snappea_do_dehn_filling(void *tri);

/* Remove all fillings. */
WASM_EXPORT void snappea_remove_dehn_fillings(void *tri);

/* --- Cusp info --- */

/* Get filling coefficients. Writes to *m and *l. */
WASM_EXPORT void snappea_get_cusp_m_l(void *tri, int cusp_index,
                                       double *m, double *l);

/* Get cusp topology: 0=torus, 1=Klein bottle */
WASM_EXPORT int snappea_get_cusp_topology(void *tri, int cusp_index);

/* --- Tetrahedron shapes --- */

/* Get shape of tet at index. Writes real and imag parts. */
WASM_EXPORT void snappea_get_tet_shape(void *tri, int tet_index,
                                        double *real, double *imag);

/* --- Invariants --- */

/* Chern-Simons value. Returns 0 and sets *known=0 if unknown. */
WASM_EXPORT double snappea_chern_simons(void *tri, int *known);

/* --- Triangulation operations --- */

WASM_EXPORT void snappea_simplify(void *tri);
WASM_EXPORT void snappea_orient(void *tri);
WASM_EXPORT int snappea_canonize(void *tri);

/* --- Homology (as JSON string) --- */

/* Returns JSON like "[0, 0, 2]" for elementary divisors.
 * Caller must free with snappea_free_string(). */
WASM_EXPORT const char *snappea_homology(void *tri);

/* --- Fundamental group (as JSON string) --- */

/* Returns JSON with generators and relations.
 * Caller must free with snappea_free_string(). */
WASM_EXPORT const char *snappea_fundamental_group(void *tri, int simplify_presentation);

/* --- Version --- */

WASM_EXPORT const char *snappea_version(void);

#ifdef __cplusplus
}
#endif

#endif /* SNAPPEA_WASM_H */
