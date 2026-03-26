# snappea-wasm Requirements

SnapPea kernel + PARI/GMP compiled to WebAssembly via Emscripten. Computation-only npm package — no UI, no rendering. Embeddable in Pyodide, Node.js, or any browser JS runtime.

- **npm package:** `@snappea/kernel`
- **License:** GPL-2.0-or-later
- **Repository:** `https://github.com/<org>/snappea-wasm`

---

## Goals

- Ship the SnapPea C kernel as a single statically-linked WASM module via npm
- Include PARI/GP + GMP for exact arithmetic (Smith normal form, homology)
- Zero UI dependencies — computation only, consumers supply their own frontend
- Usable from plain JS/TS, Node.js, Pyodide, Deno, or any WASM host
- All existing SnapPy kernel-level tests pass against the WASM build
- GitHub Actions CI: build, test, publish to npm

## Non-goals

- No GUI, Tkinter, OpenGL, or rendering of any kind
- No Python runtime bundled (consumers bring their own, e.g. Pyodide)
- No Cython — replaced by JS/TS bindings via Emscripten ccall/cwrap
- No census databases bundled (load on demand via fetch or user-supplied data)
- No SnapPyHP quad-double precision in v1 (future enhancement)

---

## Architecture

**Build toolchain:** Emscripten (emcc/em++)
**Linking:** Static — single `.wasm` binary containing SnapPea kernel + PARI + GMP
**Rationale:** Static linking avoids dynamic linking overhead (5-10% perf hit) and simplifies distribution as a single npm package.

### Source components

#### SnapPea kernel

- **Origin:** https://github.com/3-manifolds/SnapPy
- **Path:** `src/snappy/extensions/SnapPy/kernel/`
- **Size:** ~148 C/H files, ~90,000 lines

| Subdirectory | Lines | Purpose |
|-------------|-------|---------|
| `kernel_code/` | 76K | Core algorithms |
| `addl_code/` | 4.5K | Extensions (ptolemy, gluing equations) |
| `headers/` | 7.3K | Public + internal API |
| `unix_kit/` | 2K | Platform shims (to be stubbed) |

#### PARI/GP

- **Origin:** https://pari.math.u-bordeaux.fr/
- **WASM reference:** https://github.com/sagemathinc/wasm-pari-gmp
- **Purpose:** Smith normal form (matsnf), exact integer matrix ops, number-theoretic functions
- **API entry:** `gp_embedded_init(long, long)` + `gp_embedded(const char*) -> const char*`
- **Status:** `@sagemath/pari` is **deprecated** — use `@sagemath/pari-gmp` (v1.0.0, ~7.5 MB)
- **PARI version:** 2.13.2
- **Build scripts:** `build-gmp.sh` (GMP 6.2.1), `build-pari.sh` (PARI 2.13.2)
- **Exported C functions:** `_gp_embedded`, `_gp_embedded_init`, `_pari_emscripten_plot_init`
- **Build patch:** `#undef UNIX` appended to `paricfg.h` (prevents `getpwuid`/`popen` calls)

#### GMP

- **Origin:** https://gmplib.org/
- **Purpose:** Arbitrary-precision integer arithmetic used by PARI
- **Note:** Included via wasm-pari-gmp build or compiled separately with Emscripten

### Output artifacts

| File | Purpose |
|------|---------|
| `snappea_kernel.wasm` | Combined WASM binary (~2-4 MB estimated) |
| `snappea_kernel.js` | Emscripten JS glue/loader |
| `index.js` | Main entry — async init, typed API wrapper |
| `index.d.ts` | TypeScript declarations |
| `index.mjs` | ESM entry point |

**Module formats:** CommonJS, ESM
**Target environments:** browser, node, deno, pyodide, worker

---

## Exported API

JS/TS API surface exposed via Emscripten `EXPORTED_FUNCTIONS` + `cwrap`/`ccall` wrappers. Grouped by domain.

### Core lifecycle

```typescript
init():  async () => Module  // load WASM, initialize PARI stack
destroy(): void              // free all allocations
```

### Triangulation

```typescript
triangulationFromString(snappeaFileContents: string): TriangulationPtr
triangulationToString(tri: TriangulationPtr): string
copyTriangulation(tri: TriangulationPtr): TriangulationPtr
freeTriangulation(tri: TriangulationPtr): void
getNumTetrahedra(tri: TriangulationPtr): number
getNumCusps(tri: TriangulationPtr): number
getOrientability(tri: TriangulationPtr): 'orientable' | 'nonorientable'
getTriangulationName(tri: TriangulationPtr): string
simplifyTriangulation(tri: TriangulationPtr): void
orient(tri: TriangulationPtr): void
```

### Hyperbolic structure

```typescript
findCompleteHyperbolicStructure(tri: TriangulationPtr): SolutionType
doDehnFilling(tri: TriangulationPtr): SolutionType
removeDehnFillings(tri: TriangulationPtr): void
getTetShape(tri: TriangulationPtr, tetIndex: number): Complex
volume(tri: TriangulationPtr): number
solutionType(tri: TriangulationPtr): SolutionType
```

### Cusps

```typescript
getCuspInfo(tri: TriangulationPtr, cuspIndex: number): CuspInfo
setCuspInfo(tri: TriangulationPtr, cuspIndex: number, m: number, l: number): void
getHolonomy(tri: TriangulationPtr, cuspIndex: number): { meridian: Complex, longitude: Complex }
```

### Algebra

```typescript
homology(tri: TriangulationPtr): AbelianGroup
fundamentalGroup(tri: TriangulationPtr, simplify: boolean): GroupPresentation
symmetryGroup(tri: TriangulationPtr): SymmetryGroup
```

### Invariants

```typescript
complexVolume(tri: TriangulationPtr): Complex
chernSimons(tri: TriangulationPtr): number | null
```

### Geometry

```typescript
canonize(tri: TriangulationPtr): void
protoCanonize(tri: TriangulationPtr): void
computeIsometries(tri1: TriangulationPtr, tri2: TriangulationPtr): IsometryList | null
lengthSpectrum(tri: TriangulationPtr, cutoffLength: number): GeodesicInfo[]
```

### Link complements

```typescript
triangulateLinkComplement(pdCode: number[][]): TriangulationPtr
```

### PARI direct

```typescript
pariEval(expression: string): string       // thin wrapper over gp_embedded
smithNormalForm(matrix: number[][]): number[]
```

### Types

```typescript
type Complex = { re: number, im: number }

type SolutionType =
  | 'not_attempted' | 'geometric' | 'nongeometric'
  | 'flat' | 'degenerate' | 'other'
  | 'no_solution' | 'externally_computed'

type CuspInfo = {
  topology: 'torus' | 'Klein_bottle'
  m: number, l: number
  modulus: Complex, shape: Complex
}

type AbelianGroup = { elementary_divisors: number[] }

type GroupPresentation = {
  num_generators: number
  relations: string[]
  num_orig_gens: number
}

type GeodesicInfo = { length: Complex, parity: number, topology: number }

type TriangulationPtr = number  // opaque WASM heap pointer
```

---

## Platform adaptations

| Area | Problem | Solution | Effort |
|------|---------|----------|--------|
| File I/O | `interface.c` uses `stdio FILE*` for SnapPea format | Emscripten MEMFS + string-based wrappers | Low |
| Memory | `my_malloc.c` wraps malloc with tracking | Works as-is under Emscripten | None |
| RNG | `rand()` in `simplify_triangulation.c` | Emscripten provides `rand()`. Seed via JS if needed. | None |
| Long computation | `uLongComputationContinues()` callback | No-op stub, or JS callback for cancellation | Low |
| unix_kit | Platform-specific code (2K lines) | Stub/remove — console I/O and signals not needed | Low |

---

## Build system

**Convention:** Shell scripts (following wasm-pari-gmp pattern), NOT Makefile.

### Directory layout

```
src/
  snappea/        Vendored SnapPea kernel (kernel_code/, addl_code/, headers/)
  pari/           PARI source or pre-built WASM artifact from wasm-pari-gmp
  gmp/            GMP source or pre-built WASM artifact
  bindings/       C wrapper functions for Emscripten EXPORTED_FUNCTIONS
  stubs/          Platform stubs (unix_kit replacements, uLongComputation no-op)
test/
  unit/           C-level unit tests compiled to WASM, run via Node.js
  integration/    JS/TS tests exercising the public API
  fixtures/       SnapPea triangulation files (.tri) for test input
  reference/      Expected outputs from native SnapPy for comparison
dist/             Build output (wasm, js, d.ts, package.json)
scripts/
  build-gmp.sh          Download GMP 6.2.1, emconfigure/emmake
  build-pari.sh         Download PARI 2.13.2, patch, emconfigure/emmake
  build-snappea.sh      Compile SnapPea kernel to .o files
  build-bindings.sh     Compile C binding wrappers
  link.sh               Final link → dist/snappea_kernel.{wasm,js}
  gen-types.sh          Generate index.d.ts
  package.sh            Bundle dist/ with package.json, README, LICENSE
  extract-fixtures.py   Pull test triangulations from SnapPy census
  generate-reference.py Run native SnapPy to produce expected test outputs
```

### Emscripten flags

```bash
# Final link flags
-O3
-s WASM=1
-s EXPORTED_FUNCTIONS=[_gp_embedded,_gp_embedded_init,..._snappea_* wrappers]
-s EXPORTED_RUNTIME_METHODS=['ccall','cwrap','UTF8ToString','stringToUTF8','getValue','setValue']
-s MODULARIZE=1
-s EXPORT_ES6=1
-s ENVIRONMENT='web,node,worker'
-s FILESYSTEM=1
-s NO_EXIT_RUNTIME=1
-s SINGLE_FILE=0
-s ERROR_ON_UNDEFINED_SYMBOLS=0
-lm
```

### Memory strategy

wasm-pari-gmp uses fixed `INITIAL_MEMORY=2146435072` (~2GB) with **no** memory growth for PARI performance. For snappea-wasm we have two options:

| Option | Flags | Pros | Cons |
|--------|-------|------|------|
| **A: Fixed 2GB** | `-s INITIAL_MEMORY=2146435072` | Best PARI perf, proven pattern | Wastes memory, may fail on 32-bit browsers |
| **B: Growable from 64MB** | `-s INITIAL_MEMORY=67108864 -s ALLOW_MEMORY_GROWTH=1` | Low baseline, works everywhere | Slight PARI perf impact (acceptable — asm.js issue doesn't apply to WASM) |

**Recommendation:** Option B for v1. Most consumers do small computations. Add configurable initial memory in `init()` options.

### Dependency build flags

```bash
# GMP
emconfigure ./configure --build i686-pc-linux-gnu --host=none \
  --disable-assembly CFLAGS='-O3 -Wall' ABI=standard

# PARI
emconfigure ./Configure --host=wasm-emscripten --graphic=none \
  --with-gmp-include=$PREFIX/include --with-gmp-lib=$PREFIX/lib
```

### Build steps

1. `scripts/build-gmp.sh` — Download GMP 6.2.1, emconfigure/emmake, install to `build/local/`
2. `scripts/build-pari.sh` — Download PARI 2.13.2, patch paricfg.h (`#undef UNIX`), emconfigure/emmake with GMP paths
3. `scripts/build-snappea.sh` — Compile SnapPea kernel_code + addl_code + stubs with `emcc -c`
4. `scripts/build-bindings.sh` — Compile C binding wrappers with `emcc -c`
5. `scripts/link.sh` — Final emcc link: all `.o` + `libpari.a` + `libgmp.a` → `dist/snappea_kernel.{wasm,js}`
6. `scripts/gen-types.sh` — Generate `index.d.ts` from binding signatures
7. `scripts/package.sh` — Bundle into `dist/` with package.json, README, LICENSE

### Prior art

- [wasm-pari-gmp](https://github.com/sagemathinc/wasm-pari-gmp) — GMP+PARI build pattern
- [wasm-flint](https://github.com/sagemathinc/wasm-flint) — Multi-library chained static linking (MPFR->MPIR->FLINT)
- [JSage](https://github.com/sagemathinc/JSage) — Package architecture for WASM math libraries

---

## Testing

**Framework:** vitest (JS/TS) + custom C harness compiled to WASM

### Test tiers

| Tier | Description | Count | Runtime |
|------|-------------|-------|---------|
| **T0 — Smoke** | WASM loads, PARI initializes, basic triangulation round-trips | ~10 | <5s |
| **T1 — Core API** | Each exported function with known inputs vs reference values | ~100 | <30s |
| **T2 — Algebraic** | Homology, fundamental group, symmetry group for census manifolds | ~200 | <2min |
| **T3 — Geometric** | Canonize, isometry detection, length spectrum, link complements | ~50 | <1min |
| **T4 — PARI direct** | pari_eval and smith_normal_form with various matrices | ~20 | <10s |
| **T5 — Regression** | SnapPy doctest-derived fixtures, outputs compared to native SnapPy | ~500 | <5min |

**T1 coverage:**
- Triangulation creation/destruction/serialization
- Hyperbolic structure computation (trefoil, figure-eight, etc.)
- Volume computation (compare to known values +/-1e-10)
- Cusp info get/set
- Dehn filling
- Homology (requires PARI Smith normal form)
- Fundamental group
- Chern-Simons invariant

### Reference generation

Run native SnapPy (CPython) on test inputs, serialize outputs as JSON fixtures.

**Test manifolds:**
- `m004` (figure-eight knot complement)
- `m003` (trefoil complement — non-hyperbolic, tests error handling)
- `m015`, `m016`, `m017` (various cusped manifolds)
- `4_1`, `5_2`, `6_3` (knot complements by Alexander-Briggs)
- `L2a1` (Hopf link — 2-cusped)
- OrientableCuspedCensus sample (first 50 manifolds)

**Output format:** `{ manifold, volume, solution_type, num_tet, cusps, homology, chern_simons, fundamental_group }`

### Test environments

- Node.js >= 18 (primary)
- Chrome/Firefox headless via Playwright (browser validation)
- Pyodide smoke test (import from Python-in-browser)

---

## CI/CD

**Platform:** GitHub Actions

### build_and_test.yml

**Triggers:** push, pull_request

| Job | Runs on | Steps |
|-----|---------|-------|
| **build** | `ubuntu-latest` + `emscripten/emsdk:latest` container | Checkout, cache Emscripten sysroot + GMP/PARI objects, build all, upload `dist/` artifact |
| **test_node** | `ubuntu-latest` (needs: build) | Download artifact, `npm ci`, `npx vitest run --reporter=verbose` |
| **test_browser** | `ubuntu-latest` (needs: build) | Download artifact, install Playwright Chromium, `npx vitest run --browser.name=chromium` |
| **test_pyodide** | `ubuntu-latest` (needs: build) | Download artifact, `npm ci`, `node test/pyodide-smoke.mjs` |

### publish.yml

**Triggers:** release (published)

- Checkout, build (or download release artifact), `npm publish --access public`
- **Secrets:** `NPM_TOKEN`

### lint.yml

**Triggers:** push, pull_request

- `eslint`, `tsc --noEmit`, `prettier --check`

### Caching

| Cache | Contents |
|-------|----------|
| `~/.emscripten_cache` | Sysroot and system library WASM objects |
| `src/pari/dist/wasm`, `src/gmp/dist/wasm` | Pre-built `.a` archives |
| `~/.npm` | npm package cache |

---

## npm package

```json
{
  "name": "@snappea/kernel",
  "main": "dist/index.js",
  "module": "dist/index.mjs",
  "types": "dist/index.d.ts",
  "files": ["dist/"],
  "exports": {
    ".": {
      "import": "./dist/index.mjs",
      "require": "./dist/index.js",
      "types": "./dist/index.d.ts"
    }
  },
  "engines": { "node": ">=18" },
  "sideEffects": false
}
```

### Usage — JavaScript

```javascript
const { init } = require('@snappea/kernel');
const snappea = await init();
const tri = snappea.triangulationFromString(snappeaFileData);
console.log(snappea.volume(tri));
console.log(snappea.homology(tri));
snappea.freeTriangulation(tri);
snappea.destroy();
```

### Usage — Pyodide

```python
import pyodide_js
from js import require
kernel = require('@snappea/kernel')
snappea = await kernel.init()
tri = snappea.triangulationFromString(data)
print(snappea.volume(tri))
snappea.freeTriangulation(tri)
```

---

## WASM limitations

- **No signal handling** — Ctrl+C during computation kills Node.js (WASM has no signals). Provide cancellation via `uLongComputationContinues` callback.
- **No threads** — single-threaded only (no `-pthread`). Long computations block the caller.
- **32-bit WASM** — limited to ~4 GB address space maximum.
- **No filesystem by default** — PARI commands requiring data files (e.g. `polgalois`) need `--embed-file` at build time. SnapPea file I/O uses MEMFS.
- **No popen/getpwuid** — `#undef UNIX` patch required for PARI build.

---

## Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| PARI/GMP Emscripten build complexity | Medium | High — blocks project | Use pre-built WASM artifacts from sagemathinc/wasm-pari-gmp |
| SnapPea kernel IEEE 754 double edge cases | Low | Medium — subtle numerical bugs | WASM mandates IEEE 754. Run T5 regression suite. |
| Memory growth performance in tight loops | Low | Low | Set generous INITIAL_MEMORY (64MB). Profile with census batch. |
| WASM binary too large for casual browser use | Medium | Medium — slow first load | Target <4MB. Use `-O3` + `wasm-opt`. Gzipped ~1MB. |
| License compatibility (GPL-2 + GPL-2 + LGPL) | Low | Low — all copyleft-compatible | Ship as GPL-2.0-or-later. NOTICE file. |
| No C-level unit tests upstream | Certain | Medium — harness from scratch | Generate reference fixtures from native SnapPy. |

---

## Milestones

| Milestone | Description | Deliverable | Effort |
|-----------|-------------|-------------|--------|
| **M0 — Skeleton** | Repo setup, CI pipeline, emscripten container builds empty module | Green CI, placeholder npm publish | 2-3 days |
| **M1 — Kernel compiles** | SnapPea kernel_code + addl_code compiles to .wasm with PARI stubs | Triangulation round-trip in Node.js | 3-5 days |
| **M2 — PARI/GMP linked** | Static link PARI+GMP. Smith normal form works. | `homology()` correct for figure-eight knot | 3-5 days |
| **M3 — Full API + TS** | All exported functions wrapped with typed JS/TS bindings | Complete `index.d.ts`, all cwrap bindings | 3-5 days |
| **M4 — Test suite** | T0-T5 tiers implemented, reference fixtures generated, all pass | vitest green: Node + browser + Pyodide | 5-7 days |
| **M5 — v1.0 release** | npm publish, README, CI publish workflow | `npm install @snappea/kernel` works | 2-3 days |

**Total estimated effort:** 3-5 weeks for one developer familiar with Emscripten.

---

## References

- [SnapPy source](https://github.com/3-manifolds/SnapPy)
- [SnapPy docs](https://snappy.computop.org/)
- [wasm-pari (deprecated)](https://github.com/sagemathinc/wasm-pari)
- [wasm-pari-gmp](https://github.com/sagemathinc/wasm-pari-gmp)
- [PARI/GP](https://pari.math.u-bordeaux.fr/)
- [PARI/GP WASM (official)](https://pari.math.u-bordeaux.fr/gpwasm.html)
- [PARI developer guide](https://pari.math.u-bordeaux.fr/pub/pari/manuals/2.16.1/develop.pdf)
- [Emscripten docs](https://emscripten.org/docs/)
- [Emscripten dynamic linking](https://emscripten.org/docs/compiling/Dynamic-Linking.html)
- [wasm-flint (multi-library linking)](https://github.com/sagemathinc/wasm-flint)
- [JSage (WASM math package architecture)](https://github.com/sagemathinc/JSage)
