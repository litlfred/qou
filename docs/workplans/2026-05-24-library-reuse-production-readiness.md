# Workplan: Python/Rust Library Production-Readiness & Reuse

**Date:** 2026-05-24  
**Branch:** `copilot/analyze-python-rust-library-reuse`  
**Status:** DRAFT — awaiting owner decisions on options  
**Downstream targets confirmed:** WebAssembly, Pyodide  
**Downstream targets under discussion:** npm, Java/JVM, native Node.js  

---

## 1. Current State — Package Inventory

| Package | Version | Published | WASM-ready | Consumer-ready |
|---------|---------|-----------|------------|----------------|
| `hecke-engine` (Rust core) | 0.8.0 | ❌ not on crates.io (Clarabel fork blocks) | ❌ (GMP/rug dep) | ❌ |
| `pyhecke-native` (PyO3/maturin) | 0.9.0 | 🔵 GH Releases wheels only | ❌ | Partial |
| `pyhecke` (pure Python) | 0.1.0 | ❌ not on PyPI | ✅ Pyodide-compatible | Partial |
| `@snappea/kernel` (Emscripten WASM) | 0.1.0 | ❌ not on npm | ✅ | Partial |
| `folio-assistant` (TypeScript) | 0.1.0 | 🔵 GH Packages (@litlfred/folio-assistant) | ✅ | Partial |

### Key files

```
tools/hecke-engine/Cargo.toml        — Rust 27.8K LOC, version 0.8.0
tools/pyhecke/pyproject.toml         — Pure Python, hatchling, version 0.1.0
tools/pyhecke-native/Cargo.toml      — PyO3 cdylib, version 0.9.0
tools/pyhecke-native/pyproject.toml  — maturin backend, version 0.9.0
folio-assistant/package.json         — TypeScript MCP server, version 0.1.0
folio-assistant/snappea-wasm/        — Emscripten C→WASM build
```

### Blockers for crates.io / public registry

- **Clarabel fork** (`https://github.com/litlfred/Clarabel.rs` rev `9673209`) — patched for bigrational backend. Cannot publish to crates.io with `[patch.crates-io]`. When upstream merges the changes, this unblocks.
- **GMP/rug system dep** — `rug = "1.26"` (MPFR via gmp-mpfr-sys). Blocks `wasm32-*` target. Pure-Rust alternative needed for WASM builds.

---

## 2. Downstream Target Analysis

### Tier 1 — Ready now with minimal work (1–2 days each)

| Target | What to do | Benefit |
|--------|-----------|---------|
| **PyPI** (pyhecke) | `hatch build && twine upload` + add publish step to CI | `pip install pyhecke` → Pyodide `micropip.install("pyhecke")` |
| **PyPI** (pyhecke-native wheels) | Add `twine upload` to `pyhecke-native-wheels.yml` | `pip install pyhecke-native` for x86_64 Linux + macOS arm64 |
| **npm** (@snappea/kernel) | `npm publish` in `snappea_wasm.yml` | Browser/Node consumers get Emscripten WASM kernel |
| **npm** (folio-assistant schemas) | Already partially configured | TypeScript consumers get Zod schemas + types |

### Tier 2 — Requires architectural work (1–2 weeks)

| Target | Blocker | Resolution options |
|--------|---------|-------------------|
| **WASM (hecke-engine)** | `rug`/GMP C dep | **Option A:** Feature-gate `rug` behind `#[cfg(not(target_arch = "wasm32"))]`; use `astro-float` or `dashu` for WASM. **Option B:** Emscripten-compile GMP (proven pattern in this repo via snappea-wasm). **Option C:** f64-only API surface for WASM (skip MPFR). |
| **Pyodide (native)** | pyhecke-native is a cdylib → needs Emscripten or cross-compile | Use pure-Python `pyhecke` for Pyodide; native only for CPython |

### Tier 3 — Possible but no current demand

| Target | Effort | Tech |
|--------|--------|------|
| **Native Node.js addon** | 3 days | `napi-rs` crate (same pattern as PyO3) |
| **Java/JVM** | 1 week | `jni` crate bindings from hecke-engine |
| **Swift/Kotlin mobile** | 1 week | Mozilla UniFFI |
| **R** | 3 days | `extendr` crate |
| **C FFI** | 1 day | Already possible via PyO3's underlying ABI; formalize with `cbindgen` |

### What you already have via TypeScript

- ✅ **npm publish** of `folio-assistant` schemas — consumers get `@litlfred/folio-assistant`
- ✅ **Zod schemas** are runtime-usable from any JS/TS project
- ✅ **Content pipeline** can be consumed as a library (Bun/Node)
- ❌ Not a compute library — no Hecke algebra operations in TS

---

## 3. Missing SEMVER & Release Infrastructure

### Current gaps

1. **No workspace-level version** — hecke-engine (0.8.0) ≠ pyhecke-native (0.9.0) ≠ pyhecke (0.1.0)
2. **No CHANGELOG** for any package
3. **No release-please or semantic-release** automation
4. **No version-sync CI check** (Cargo.toml ↔ pyproject.toml can drift)
5. **No crates.io publish** (blocked by fork)
6. **No PyPI publish** pipeline

### Options (pick one)

| # | Approach | Effort | Pros | Cons |
|---|----------|--------|------|------|
| **A** | `release-please` (Google's tool) | 2 days | Auto-bumps from conventional commits, generates CHANGELOGs, creates GH Releases | Requires conventional-commit discipline |
| **B** | Cargo workspace version inheritance + Python version derived from Cargo.toml + single `release.yml` | 3 days | Atomic multi-package release | Complex cross-language version sync |
| **C** | Independent versions + version-check CI job + manual `release-all.yml` dispatch | 1 day | Simplest, lowest risk | No automation, manual process |

---

## 4. CI Parallelization Opportunities

### `publish.yml` — current bottleneck

**Current state:** 1 monolithic job (lines 80–1012) does everything sequentially.  
**Estimated wall time:** 20–40 min.

**Proposed parallel DAG:**

```
                    ┌─ validate-content ─┐
                    │                    │
dispatch ──────────├─ build-lean ───────┤──► deploy
                    │                    │
                    ├─ compile-papers ───┤
                    │   (matrix per      │
                    │    paper)          │
                    │                    │
                    └─ gen-witnesses ────┘
```

| Step | Current (sequential) | Proposed (parallel) | Depends on |
|------|---------------------|--------------------:|------------|
| Content validation + schema docs | In monolith | `validate` job | nothing |
| Witness regeneration | In monolith | `witnesses` job | nothing |
| Per-paper LaTeX compile | In monolith | `compile` job (matrix: [qou, ugb, fred2005]) | `validate` |
| PDF split + QA | In monolith | `post-process` job | `compile` |
| latexdiff | In monolith | `diff` job (optional) | `compile` |
| Deploy to gh-pages | In monolith | `deploy` job | all above |

**Expected speedup:** ~2–3× (30 min → 10–15 min).

### `lean_ci.yml` — already reasonable

4 sequential phases with cache forwarding. Main improvement is caching strategy (see §5).

---

## 5. Lean Integration — Prebuilt Oleans Strategy

### Problem

- Lean/Lake build from scratch: ~15–25 min
- `.lake/` grows to ~2–4 GB with Mathlib oleans
- Pollutes `main` if committed; wastes CI time if rebuilt each run
- Users who don't need Lean still clone 2+ GB

### Options

| # | Strategy | Effort | Pros | Cons |
|---|----------|--------|------|------|
| **A** | `lean-cache` orphan branch | 2 days | Clean main, fast CI (~3-5 min), opt-in for users | Branch maintenance, stale if Mathlib bumps |
| **B** | GitHub Releases artifact (`.lake.tar.zst`) | 1 day | Versioned, no branch pollution | 2-4 GB upload limits, manual release step |
| **C** | Improved `actions/cache` + weekly warm job | 1 day | Simplest, no ceremony | 7-day GH eviction policy, slow on first miss |

**Recommended: Option A** — orphan branch `lean-cache`:
- Separate `update-lean-cache.yml` runs weekly or on `lakefile.toml` changes
- CI: `git fetch origin lean-cache && git checkout lean-cache -- .lake/build/lib/`
- Users: `git fetch origin lean-cache && git checkout lean-cache -- .lake/`
- Same pattern for `witness-cache` branch (93 MB of JSON out of main history)

---

## 6. Missing Auto-Generated Documentation

| What | Status | Proposed fix |
|------|--------|--------------|
| **Rustdoc** (hecke-engine API) | ❌ Not generated | Add `cargo doc --no-deps` to CI; deploy to gh-pages `/rust-api/` |
| **Python API docs** (pyhecke + pyhecke-native) | ❌ Not generated | Add `pdoc` build; deploy to gh-pages `/python-api/` |
| **TypeDoc** (folio-assistant schemas) | ✅ Configured in `typedoc.json` | Already works; needs explicit publish step in `publish.yml` |
| **CONTRIBUTING.md** | ❌ Missing | Build/test/lint instructions for each sub-project |
| **Architecture overview** | ❌ Missing | `docs/ARCHITECTURE.md` with component diagram |
| **Package consumer guide** | ❌ Missing | "How to install and use pyhecke / pyhecke-native / snappea-wasm" |
| **WASM integration guide** | ❌ Missing | Browser + Node.js usage of `@snappea/kernel` |
| **Witness format spec** | Partial (in-code) | Publish JSON schema as formal spec |
| **Lean doc-gen4** | ✅ Configured | Runs in `blueprint.yml`, deploys to `/docs/` |

---

## 7. Reuse Maximization — What exists vs. what's needed

### Already reusable (just needs publishing)

- ✅ **WitnessBuilder** pattern (Python) — schema-validated JSON computation records
- ✅ **Content pipeline** (TypeScript) — Zod schemas, markdown→LaTeX, block validation
- ✅ **PyO3 binding pattern** — pyhecke-native as template for more crate bindings
- ✅ **Emscripten WASM pattern** — snappea-wasm as proven template
- ✅ **cibuildwheel config** — multi-platform wheel builds working

### Blocking reuse

- ❌ **No public registry presence** — can't `pip install` or `npm install`
- ❌ **No API documentation** — consumers can't discover functions
- ❌ **No stability guarantees** — no semver policy, no deprecation warnings
- ❌ **No integration examples** — no "getting started" for downstream

### Target architecture

```
┌─────────────────────────────────────────────────────┐
│              hecke-engine (Rust core)                │
│  Cargo.toml: version = "1.0.0"                      │
│  Features: [mpfr, wasm, sdp, clarabel]              │
└──────────┬──────────────┬──────────────┬────────────┘
           │              │              │
  ┌────────▼──────┐ ┌────▼────────┐ ┌──▼──────────┐
  │ pyhecke-native│ │ @qou/hecke  │ │ hecke-jni   │
  │ (PyO3→PyPI)  │ │ (wasm-pack  │ │ (JNI→Maven) │
  │              │ │  →npm)      │ │ (Tier 3)    │
  └───────┬──────┘ └──────┬──────┘ └─────────────┘
          │                │
  ┌───────▼──────┐  ┌─────▼───────┐
  │ pyhecke      │  │ Browser /   │
  │ (PyPI)       │  │ Pyodide     │
  └──────────────┘  └─────────────┘
```

---

## 8. Prioritized Action Items

### Phase 1 — Quick wins (1–2 days each, no dependencies between them)

- [ ] **1a.** Publish `pyhecke` to PyPI (add `hatch build && twine upload` to CI)
- [ ] **1b.** Publish `@snappea/kernel` to npm (add `npm publish` step)
- [ ] **1c.** Add `cargo doc --no-deps` to CI → deploy rustdoc to gh-pages
- [ ] **1d.** Add `pdoc` generation for pyhecke + pyhecke-native → gh-pages
- [ ] **1e.** Create `CONTRIBUTING.md` (build/test/lint commands from existing CI)
- [ ] **1f.** Create `docs/ARCHITECTURE.md` (component diagram + data flow)
- [ ] **1g.** Ensure TypeDoc runs in publish.yml and deploys to gh-pages `/schema-docs/`

### Phase 2 — Release infrastructure (3–5 days)

- [ ] **2a.** Add `release-please` GitHub Action (conventional-commit bumps + changelogs)
- [ ] **2b.** Version-sync CI check (Cargo.toml ↔ pyproject.toml)
- [ ] **2c.** Publish pyhecke-native wheels to PyPI (add twine to wheels workflow)
- [ ] **2d.** Create unified `release.yml` manual-dispatch workflow

### Phase 3 — CI parallelization (3–5 days)

- [ ] **3a.** Split `publish.yml` monolith into parallel job DAG
- [ ] **3b.** Add `lean-cache` orphan branch with weekly warm workflow
- [ ] **3c.** Optional: `witness-cache` orphan branch (decouple 93 MB from main)

### Phase 4 — WASM for hecke-engine (1–2 weeks)

- [ ] **4a.** Feature-gate `rug`/GMP behind `#[cfg(feature = "mpfr")]`
- [ ] **4b.** Add `dashu` or `astro-float` as pure-Rust multiprecision fallback
- [ ] **4c.** Add `wasm-pack` build → publish `@qou/hecke-engine` to npm
- [ ] **4d.** Pyodide integration: pyhecke consuming WASM module via micropip

### Phase 5 — Extended targets (optional, 1–2 weeks each)

- [ ] **5a.** `napi-rs` bindings (native Node.js addon, faster than WASM for server)
- [ ] **5b.** JNI bindings (Java/Kotlin)
- [ ] **5c.** UniFFI (Swift/Kotlin mobile)

---

## 9. Decision Points for Owner

These require your input before proceeding:

1. **SEMVER strategy** — Option A (release-please), B (workspace inheritance), or C (manual + CI check)?
2. **Lean cache strategy** — Option A (orphan branch), B (release artifact), or C (improved actions/cache)?
3. **WASM approach for hecke-engine** — Option A (feature-gate + pure-Rust fallback), B (Emscripten GMP), or C (f64-only surface)?
4. **Phase 1 ordering** — which quick-wins to tackle first?
5. **Registry targets** — PyPI + npm confirmed? crates.io deferred until Clarabel upstream?
6. **Witness separation** — move 93 MB to orphan branch, or keep in main?

---

## Appendix: Existing CI Workflows (17 total, 3,636 LOC)

| Workflow | LOC | Trigger | Type |
|----------|-----|---------|------|
| `lean_ci.yml` | 533 | push main / PR / manual | Sequential (4 phases) |
| `publish.yml` | 1,061 | manual dispatch | Monolithic single job |
| `blueprint.yml` | 256 | manual dispatch | Sequential (5 phases) |
| `pyhecke.yml` | 54 | manual dispatch | Parallel (test matrix) |
| `pyhecke-native-wheels.yml` | 128 | push main / manual | Parallel (build + test) |
| `witness-pipeline.yml` | 466 | push main / PR / manual | Sequential (4 phases) |
| `lean-build.yml` | 131 | manual dispatch | Sequential |
| `snappea_wasm.yml` | 103 | manual dispatch | Sequential build, parallel tests |
| `deploy-folio.yml` | 155 | push main / manual | Sequential |
| `release-folio-assistant.yml` | 111 | manual dispatch | Sequential |
| `build-lean-mcp.yml` | 107 | manual dispatch | Sequential |
| `qa-sweep.yml` | 154 | manual dispatch | Parallel |
| `agent-review.yml` | 92 | manual dispatch | Single job |
| `build-latex-image.yml` | 67 | manual dispatch | Single job |
| `docker-ci-image.yml` | 65 | manual dispatch | Single job |
| `sync-skills.yml` | 95 | schedule (nightly) + manual | Single job |
| `copilot-setup-steps.yml` | 58 | reusable workflow | Includes |
