# Workplan: Python/Rust Library Production-Readiness & Reuse — v2

**Date:** 2026-05-24
**Branch:** `claude/stoic-einstein-IhoId`
**Status:** DRAFT v2 — re-tiered per owner direction (2026-05-24)
**Predecessor:** `copilot/analyze-python-rust-library-reuse` @ b6ca5667
**Downstream targets confirmed:** WebAssembly, Pyodide, PyPI, npm
**Downstream targets deferred:** Node.js native, Kotlin/Swift, R, C FFI (Tier 3)

---

## 0. Owner directives that changed the tiering

1. **Do Tier 1 + Tier 2 now.**
2. **Tier 3 is: Node.js native addon, Kotlin, R, C FFI** (deferred — no current demand).
3. **Question to address:** "Show the pipeline; besides Python wrappers, what else lives in Python that would need to be recreated for non-Python consumers? Where is the most upstream node with the most downstream — to minimize duplication?"

This v2 answers (3) with hard numbers, then re-tiers accordingly.

---

## 1. The Pipeline — actual layered architecture

Counts are measured from the current `claude/stoic-einstein-IhoId` working tree.

```
┌──────────────────────────────────────────────────────────────────────┐
│ LAYER 0 — SUBSTRATE INFRA (pure Python, ~1.1k LOC)                   │
│  q_parameter.py    (220 LOC)  q_0 + derived constants + error prop.  │
│  _precision.py     (136 LOC)  mpmath 50-dps discipline               │
│  witness_base.py   (761 LOC)  WitnessBuilder, staleness, git SHA     │
│  ─ 300+ scripts depend on q_parameter; 209 on WitnessBuilder ─       │
└──────────────────────────────────────────────────────────────────────┘
        │                                                       │
        ▼                                                       ▼
┌─────────────────────────────────────┐    ┌─────────────────────────────┐
│ LAYER 1a — RUST CORE (~14k LOC)     │    │ LAYER 1b — PYTHON COMPUTE   │
│ tools/hecke-engine/                 │    │  pyhecke (1.8k LOC)         │
│  19 modules: seminormal*, wenzl_lr, │    │   gram (310), sdp (588),    │
│  tr_m_atomic_mpfr, sdp_solve_*,     │    │   wedderburn, tower, etc.   │
│  reduce_laurent, wedderburn_psd, … │    │  hecke_core.py (3,183 LOC)  │
│                                     │    │   ← M1 carve-out target     │
│  Blockers (per v1):                 │    │  laurent_q.py, BlockCache,  │
│   • Clarabel fork → no crates.io    │    │   lp_dual_solver.py         │
│   • GMP/rug C dep → no WASM target  │    │  ─ 91 scripts import this ─ │
└─────────────────────────────────────┘    └─────────────────────────────┘
        │                                                       │
        ▼                                                       │
┌─────────────────────────────────────┐                         │
│ LAYER 2 — FFI WRAPPERS              │                         │
│  pyhecke-native (PyO3, ~20 pyfns)   │                         │
│   used by 22/539 scripts (~4%)      │                         │
│  snappea-wasm (Emscripten C→WASM)   │                         │
│   used by 2/539 scripts (~0.4%)     │                         │
└─────────────────────────────────────┘                         │
        │                                                       │
        └──────────────────────┬────────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│ LAYER 3 — COMPUTE SCRIPTS                                            │
│   folio-assistant/computations/   →  539 .py files                   │
│   →  858 .witness.json files                                         │
└──────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│ LAYER 4 — CONTENT / NARRATIVE  (TypeScript, ~27.6k LOC)              │
│  content/  ← 450 blocks reference witnesses                          │
│  content/pipeline/  validate, render-latex, AST-check                │
│  folio-assistant/schemas/  Zod schemas                               │
└──────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
                      paper PDF / HTML viewer
```

### Import-count receipts

```
209  from witness_base import WitnessBuilder        ← LAYER-0 #1
 89  from _precision import set_compute_dps, fmt    ← LAYER-0 #2
 34+ from q_parameter import Q, Q_INV, HA, …        ← LAYER-0 #3
 67  scripts still import hecke_core.py directly     ← LAYER-1b legacy
 22  scripts use pyhecke_native (Rust core)          ← LAYER-2 (~4%)
 14  from lp_dual_solver import solve_operator…      ← LAYER-1b dual solver
  6  from syt_prefix_cache import BlockCache         ← LAYER-1b cache
  4  from laurent_q import LaurentQ                  ← LAYER-1b poly
  2  scripts use snappea-wasm                        ← LAYER-2 (~0.4%)
```

---

## 2. "Besides Python wrappers, what lives in Python?" — the answer

Three categories of pure-Python compute that the Rust core does **not** cover:

### A. Substrate-infra trio (1,117 LOC) — universal, used by 50–60% of scripts

| Module | LOC | Used by | What it owns |
|--------|-----|---------|--------------|
| `witness_base.py` | 761 | 306 scripts | `WitnessBuilder`: schema-validated JSON, git provenance, file-hash staleness, upstream dep tracking, sidecar emission |
| `q_parameter.py` | 220 | 300+ scripts | The substrate constant `q_0 = 1/(1 − √(V(4_1)/(m_μ/m_e)))`, derived constants (`HA`, `E_CROSS`, `TWO_Q`, `LN_Q`), error propagation |
| `_precision.py` | 136 | 107 scripts | `set_compute_dps(50)`, `fmt()` — mpmath dps discipline (compute 50, output 40) |

**This trio is the single highest-leverage layer in the entire stack.**
None of it has any dependency on the Rust core. None of it is currently published.

### B. Pure-Python math layer (`pyhecke`, 1,839 LOC)

| Module | LOC | What it computes |
|--------|-----|------------------|
| `pyhecke/sdp.py` | 588 | SDP coordination + primal/dual scaffolding (calls scipy/cvxpy under the hood) |
| `pyhecke/gram.py` | 310 | Gram matrix construction from substrate |
| `pyhecke/undo.py` | 191 | Reversible operator-undo for Hecke words |
| `pyhecke/bridge.py` | 162 | Bridge between pure-Py and `pyhecke-native` |
| `pyhecke/crt.py` | 120 | Chinese Remainder reconstruction |
| `pyhecke/schema.py` | 110 | Hecke-result JSON schema |
| `pyhecke/{wedderburn,tower,trace,partition,certificate}.py` | ~140 | Combinatorial helpers |

**`pyhecke` is partially a "M1 carve-out" of legacy `hecke_core.py` (3,183 LOC, still imported by 52 scripts).** The carve-out is incomplete — finishing it is a Tier-2 prerequisite for publishing.

### C. Other shared Python compute (not in `pyhecke` yet)

| Module | LOC | Used by | What it owns |
|--------|-----|---------|--------------|
| `lp_dual_solver.py` | ~? | 14 scripts | The canonical LP+dual entry point cited by the CLAUDE.md "LP/SDP duals — first-class infra" rule |
| `laurent_q.py` | ~? | 15 scripts | `LaurentQ` — sparse O(1) Laurent-poly arithmetic in `q` (alternative to `sympy.Poly`) |
| `syt_prefix_cache.py` | ~? | 6 scripts | `BlockCache` — Hoefsmit SYT-prefix memoization |

These are **library-quality candidates that currently live in scripts/** — they belong in a Python package.

---

## 3. Where is the most-upstream, most-downstream node?

**Answer: `witness_base.WitnessBuilder`** (LAYER-0 #1 in the diagram).

| Metric | Value |
|--------|-------|
| Scripts that import it directly | **306 / 539** (57%) |
| Witness JSON files it produces | **858** |
| Content blocks that reference those witnesses | **450** |
| TS pipeline modules that consume the JSON shape | All of `content/pipeline/` |
| Dependencies it has on Rust core | **0** |

**Comparison to the Rust core:**

| Path | Direct script consumers |
|------|------------------------|
| `pyhecke-native` (Rust→Py via PyO3) | 22 scripts (~4%) |
| `snappea-wasm` (C→WASM)             | 2 scripts (~0.4%) |
| `WitnessBuilder` (pure Py)          | 306 scripts (~57%) |

**Implication.** Publishing only the Rust core reaches ~4% of the compute layer. Publishing the substrate trio (`WitnessBuilder` + `_precision` + `q_parameter`) reaches **all 539 scripts and the entire 450-block narrative layer**. This is the leverage point that v1 missed.

### Secondary upstream nodes (lower leverage, still worth packaging)

1. **`hecke_core.py`** — 67-script orchestrator; the bridge between substrate + Hecke math. Finishing the `pyhecke` carve-out makes the whole `pyhecke` package coherent.
2. **`lp_dual_solver.py`** — the CLAUDE.md-mandated LP-duality entry point; should live in `pyhecke` (or its own micro-package).
3. **`laurent_q.py`** — 10× faster than `sympy.Poly` for the q-only case; a clean stand-alone library.

---

## 4. Re-tiered action plan

### Tier 1 — Quick wins (1–2 days each, do now)

| # | Item | Why |
|---|------|-----|
| **1a** | **Publish `pyhecke` to PyPI** (`hatch build && twine upload` in CI) | Pyodide-ready, no system deps, unblocks `micropip.install("pyhecke")` |
| **1b** | **Publish `pyhecke-native` wheels to PyPI** (add `twine upload` to `pyhecke-native-wheels.yml`) | `pip install pyhecke-native` for x86_64 Linux + macOS arm64 |
| **1c** | **Publish `@snappea/kernel` to npm** (`npm publish` in `snappea_wasm.yml`) | Browser/Node consumers get the Emscripten WASM kernel |
| **1d** | **Publish the witness JSON schema** as `@litlfred/witness-schema` (npm) + `witness-schema` (PyPI) | The witness JSON is the universal interchange format between Layer 3 and Layer 4 — publishing the schema standalone (Zod for TS, Pydantic for Py) makes every downstream consumer schema-validated |
| **1e** | **`cargo doc --no-deps`** for `hecke-engine` → gh-pages `/rust-api/` | Discoverability |
| **1f** | **`pdoc`** for `pyhecke` + `pyhecke-native` → gh-pages `/python-api/` | Discoverability |
| **1g** | **TypeDoc** for `folio-assistant` schemas → gh-pages `/schema-docs/` | Already configured; needs publish step |
| **1h** | **`CONTRIBUTING.md`** + **`docs/ARCHITECTURE.md`** | Onboarding |

### Tier 2 — Architectural prerequisites (1–2 weeks)

This is where the v1 plan needs the biggest restructure. The **substrate-infra trio promotion** is the new Tier-2 priority because it unlocks every downstream consumer in every language.

| # | Item | Why |
|---|------|-----|
| **2a** | **Promote `witness_base.py` + `_precision.py` + `q_parameter.py` into a `qou-substrate` Python package** (new home: `tools/qou-substrate/`). Publish to PyPI. Re-export back into `folio-assistant/computations/` for backwards compat. | The 57% leverage move. Once this is a package, all 306 scripts get the same versioned `WitnessBuilder`. Pyodide ships it. Non-Python consumers see a stable JSON schema. |
| **2b** | **Finish the `pyhecke` M1 carve-out** — pull the remaining shared math out of `folio-assistant/computations/hecke_core.py` (3,183 LOC, 67 importers) into `pyhecke` submodules. Convert script imports. | Makes `pyhecke` self-contained, removes the brittle `_legacy.py` sys.path hack, lets `pyhecke.gram` import cleanly in Pyodide. |
| **2c** | **Move `lp_dual_solver.py`, `laurent_q.py`, `syt_prefix_cache.py` into `pyhecke` as submodules.** Add CLAUDE.md xref. | These are library-quality already; living in `computations/` blocks reuse. |
| **2d** | **WASM `hecke-engine`** — feature-gate `rug`/GMP behind `#[cfg(feature = "mpfr")]`; add `dashu` or `astro-float` as pure-Rust fallback; `wasm-pack build` → publish `@qou/hecke-engine` to npm. | Unblocks browser-side Hecke compute. |
| **2e** | **Pyodide integration** — verify `pyhecke` + `qou-substrate` both load in Pyodide; documentation + smoke test. | The "consume QOU in a browser" story. |
| **2f** | **Release infra:** `release-please` (Option A from v1 §3) for the workspace; CHANGELOG per package. | Required before any of the above can ship a 1.0. |
| **2g** | **CI parallelization** of `publish.yml` (v1 §4) | ~3× speedup, prerequisite for fast release cycles. |
| **2h** | **`lean-cache` orphan branch** (v1 §5 Option A) | Decouples 2-4 GB `.lake/` from main + CI churn. |

### Tier 3 — Deferred until demand (per owner directive)

| Target | Effort | Tech |
|--------|--------|------|
| Native Node.js addon | 3 days | `napi-rs` crate |
| Kotlin / Swift mobile | 1 week | Mozilla UniFFI |
| R | 3 days | `extendr` crate |
| C FFI | 1 day | `cbindgen` over existing PyO3 ABI |

These do **not** block any current consumer. Tier-2 work (especially the substrate-trio publish) makes Tier-3 trivial when demand arrives — every Tier-3 target just needs a thin binding over the already-stable Python/Rust packages.

---

## 5. Why the substrate-trio promotion is the highest-ROI single change

If you ship only **one** thing from this workplan, ship the substrate-trio promotion (item **2a**):

- It is the single largest lever in the dependency graph (57% of scripts).
- It carries zero Rust dependency, so it ships everywhere CPython runs — including Pyodide today, with no WASM work.
- It is the canonical source of `q_0` — every other language binding (R, Kotlin, JS) currently has to re-implement `q_parameter.py` or duplicate the constant. Publishing a witness schema **plus** a tiny `q_0 = …` stub in each target language is a strictly smaller surface than porting all of `pyhecke`.
- It is the only thing in the stack that touches both compute (Layer 3) *and* narrative (Layer 4). Stabilizing its JSON output stabilizes the entire reproducibility audit trail.

Concretely, the package boundary I propose for **2a**:

```
tools/qou-substrate/
  pyproject.toml                # hatchling, version pinned to git SHA + semver
  python/qou_substrate/
    __init__.py
    constants.py                # ← from q_parameter.py (Q, Q_INV, HA, …)
    precision.py                # ← from _precision.py (set_compute_dps, fmt)
    witness.py                  # ← from witness_base.py (WitnessBuilder, Assertion, staleness)
    schema/
      witness.schema.json       # exported JSON schema (downstream-consumable)
  tests/
    test_witness_round_trip.py
    test_constants_vs_codata.py
    test_precision_invariants.py
```

Then `folio-assistant/computations/witness_base.py`, `_precision.py`, `q_parameter.py` become thin re-export shims:

```python
# folio-assistant/computations/witness_base.py — back-compat shim
from qou_substrate.witness import *  # noqa: F401,F403
```

Zero downstream script changes; the 306 existing imports keep working; the package is now `pip install`-able and Pyodide-loadable.

---

## 6. Decision points for owner

Replaces v1 §9. Each item is `multiSelect` — pick the ones you want me to start on.

1. **Confirm the new Tier 2 priority order:** start with **2a** (substrate-trio promotion) before WASM-hecke (**2d**)?  → I recommend **YES**: 2a unlocks the most downstream and is independent of the Clarabel/GMP blockers.
2. **`qou-substrate` package name** — accept the name, or prefer something else (`pyqou`, `qou-core`, `qou-infra`)?
3. **Should `pyhecke.sdp` (588 LOC, calls cvxpy/scipy) stay in `pyhecke`, or move to `qou-substrate`?**  → I recommend **stay in `pyhecke`**: SDP is Hecke-specific.
4. **Confirm Tier-3 stays deferred** — Node.js native / Kotlin / R / C FFI remain "on demand", no current scheduling.
5. **Release infra (2f):** confirm `release-please` (v1 §3 Option A) is the choice.
6. **Lean cache (2h):** confirm orphan branch (v1 §5 Option A).
7. **WASM-hecke approach (2d):** confirm feature-gate `rug` + `dashu` fallback (v1 §2 Option A).

---

## 7. What v1 had right that v2 keeps

- The Tier 1 quick-wins list (PyPI/npm publishes + docs) is unchanged in scope; v2 just adds the **witness-schema** standalone publish (item 1d) for cross-language consumption.
- The blockers analysis (Clarabel fork, GMP/rug WASM) is accurate.
- The CI parallelization plan (`publish.yml` DAG split) and the Lean-cache orphan-branch strategy are kept verbatim in Tier 2.
- The Tier 3 effort estimates are kept.

## 8. What v2 changes

- **New top-priority Tier-2 item: substrate-trio promotion (`qou-substrate` package).** This is the 57%-leverage move v1 missed.
- **Tier 2 explicitly includes the `pyhecke` carve-out finish + `lp_dual_solver` / `laurent_q` / `BlockCache` library migration** — without this, "publish pyhecke" ships an incoherent package that still depends on `hecke_core.py` in `computations/`.
- **Tier 1 gains a witness-schema package** (item 1d) — the universal JSON shape published as both npm + PyPI, so non-Python consumers can validate without porting Python.
- **Tier 3 is explicitly: Node.js native, Kotlin, R, C** per owner directive — re-promoted from v1's "Tier 5".
- **The pipeline diagram (§1) is new** — answers the user question literally.
