# qou-knot-wasm

Browser-side WASM kernel for the **Recursive Knot-Atlas Viewer**
(`folio-assistant/simulators/knot_atlas_viewer.html`).

## Build (locally)

```bash
# One-time
cargo install wasm-pack

# Build
cd tools/qou-knot-wasm
wasm-pack build --target web --release --out-name qou_knot_kernel
```

The CI workflow at `.github/workflows/wasm-build.yml` builds the
artefact and publishes it to gh-pages under `/wasm/` so the deployed
viewer can pick it up without a manual build.

## Surface

See `src/lib.rs`.  All `#[wasm_bindgen]` exports take/return JSON-
serialisable values via `serde-wasm-bindgen`.  Inputs are braid words
(arrays of nonzero `i32` — `+i` for σᵢ, `-i` for σᵢ⁻¹) and small
integers; outputs are plain JS objects/numbers.

## No-hardcoded-QOU-values contract

This kernel must NOT bake `q₀` or any other QOU substrate constant
into its code.  Any constant it emits is either a topological
invariant computed from the input braid word, or a small Wedderburn
witness-table entry whose justification lives in the matching witness
JSON.  See the module-level docstring in `src/lib.rs`.

## Slice C (Pyodide wheel) — future

The full Hecke-engine surface lives in `tools/hecke-engine` and is
exposed to Python via `tools/pyhecke-native` (PyO3 + maturin).  Once
the `wasm32-unknown-emscripten` cross-build of `pyhecke-native` is
wired up, the simulator will opt-in to the heavier Pyodide-loaded
wheel via `?backend=pyodide`.  The wasm-bindgen kernel here remains
the lightweight default.
