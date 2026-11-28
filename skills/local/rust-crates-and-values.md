---
name: rust-crates-and-values
roles: [collaborator, owner]
description: >
  Workflow, architecture, and build/KG discipline for QOU's top-level Rust
  workspace (`Cargo.toml` + `crates/*`), `folio-assistant-sci` domain-neutral
  library boundary, `tool-defs/` Knowledge Graph crate registration
  (`scripts/gen-crate-tools.ts`), shared `CARGO_TARGET_DIR` resource caps, and
  80-dps proton-pinned witnessed-value evaluation via `qou-values`. Read BEFORE
  creating, moving, building, or wiring any crate under `crates/` or evaluating
  witnessed values from Rust.
allowed-tools: Read Bash Grep Glob Edit Write Skill
---

# Rust Crates Workspace & Witnessed Values (`crates/*` + `tool-defs/`)

Governing BPMN process: [`processes/tools/rust-crates-and-values.bpmn`](../../../processes/tools/rust-crates-and-values.bpmn).

## 1. Top-level Cargo workspace layout (Owner rulings A1/A2/A3, 2026-11-28)

All Rust crates live under top-level [`Cargo.toml`](../../../Cargo.toml) and `crates/*` (declared in [`qou.json`](../../../qou.json) as `"id": "crates"`, `"graphTypologies": ["code"]`, with two-phase `"moves"` entries per `two-phase-move`), while Python packages remain at `tools/pyhecke` and `tools/qou-substrate` and QOU's `tools` Knowledge Graph lives at `tool-defs/` (`qou.json` `"id": "tools"`):

| Crate path | Layer / Scope | Role |
|---|---|---|
| `crates/gs-basis` | **General math (`folio-assistant-sci`-reusable, 0 QOU domain specifics)** | Standalone non-commutative Buchberger–Shirshov engine, Coxeter / Iwahori–Hecke / Temperley–Lieb normal forms, Markov tower peeling, binomial/toric Gröbner reduction, and 3-tier Hecke / TL / jet GS reduction (Ruling A1: `1A+1B`). |
| `crates/qou-gg-core` | QOU algebra (`3A+3B`) | Pure algebraic $\gamma\gamma$ 4-photon interaction algebra, $Z = 0\ldots 118$ `T3` / Hopf atomic-chart word generator, and 4-strand / 6-strand channel structures built on top of `gs-basis`. |
| `crates/qou-gg-eval` | QOU evaluation (`3A+3B`) | Arbitrary-precision MPFR / exact Laurent evaluation of `qou-gg-core` observables and channel traces at the proton pin. |
| `crates/qou-clarabel` | QOU optimization (`3C`) | 80-dps MPFR LP/SDP shadow-price & dual certificates via the pinned `Clarabel.rs` fork (`rev = "37f06c3"`, native MPFR Cholesky / Jacobi-eigen / Jacobi-SVD PSD cones). |
| `crates/qou-values` | QOU witnessed values (`3C`) | General fast `.rs` witnessed-value evaluator emitting and querying 80-dps proton-pinned `*.witness.json` payloads for `ACCURACY.md` and paper `:val[...]` / `{{ qou.computations.<witness>.<path> }}` references. |
| `crates/hecke-engine` | QOU / Hecke core + CLI | Canonical Iwahori–Hecke $H_n(q)$ normal-form, Hoefsmit seminormal, Wenzl LR-bridge, Markov-trace, and Clarabel LP/SDP CLI binaries (`clarabel-operator-selection-lp`, `tl-cable-mpfr`, etc.). |
| `crates/pyhecke-native` | Python FFI (`cdylib`) | PyO3 native extension wheel (`pyhecke_native`) exposing `hecke-engine` MPFR/exact primitives to Python (`scripts/build-pyhecke-native.sh`). |
| `crates/borromean-recurrence-crt` | Modular CRT CLI | Modular $u64$ RREF nullspace sampler + rational-function CRT lift for Borromean colored-Jones recurrences. |
| `crates/hecke-engine-{c,wasm,node,jvm}` | Multi-language FFI | C ABI (`cbindgen`), WASM (`wasm-bindgen`, excluded from workspace `mpfr` unification), Node.js (`napi-rs`), and Kotlin/Swift (`uniffi`) FFI wrappers. |

## 2. `folio-assistant-sci` Library Boundary & Semver Discipline (`package-release`)

- **Strict domain neutrality in general math crates:** General mathematical crates — above all `crates/gs-basis` (non-commutative Buchberger–Shirshov, Coxeter/Hecke/TL normal forms, Markov tower peeling, binomial/toric Gröbner reduction) — MUST stay **100% free of QOU domain specifics** (no particle names, no CODATA constants, no $q_0$ pins, no QOU witness paths) so they can be consumed directly by `folio-assistant-sci` and external scientific crates.
- **Layered application crates:** QOU-specific physics/model constructions (`3A` $\gamma\gamma$ 4-photon & $Z = 0\ldots 118$ `T3`/Hopf chart, `3B` 4-strand/6-strand channel probes, `3C` `Clarabel.rs` shadow-price wrappers and `qou-values`) sit cleanly in higher-level `qou-*` crates depending *on* `gs-basis`.
- **Manifest metadata & strict semver (`package-release.md`):** Every `crates/*/Cargo.toml` MUST carry exact `[package]` metadata (`name`, exact `version` triple with no ranges, `edition`, `description`, `license = "MIT"`, `repository = "https://github.com/litlfred/qou"`). Workspace-wide `[profile.release]` and `[patch.crates-io]` live **only** in root `Cargo.toml` for workspace members (excluded target-specific FFI crates keep their own standalone profiles). Breaking exported API removals require a major bump (or minor pre-1.0 per `release-please` config); tagged versions are never reused.

## 3. Mandatory Disk & CPU Discipline (`CARGO_TARGET_DIR`)

Rust `target/` directories with `rug`/`gmp-mpfr-sys` and `Clarabel.rs` grow to several GB per worktree if left unshared. **Every** `cargo` or `maturin` invocation MUST share one target directory and cap build parallelism:

```bash
PATH="$HOME/.cargo/bin:$PATH" \
CARGO_TARGET_DIR=/tmp/qou-shared-cargo-target CARGO_BUILD_JOBS=2 nice -n 15 \
  cargo check -p hecke-engine
```

- Prepend `$HOME/.cargo/bin` to `PATH` on macOS workstations where `/opt/local/bin/rustc` (MacPorts 1.77) may precede rustup's modern `rustc` (`>= 1.85` required by `rug` / `clap`).
- Check `df -h /` before and after large builds so `/` stays `>= 13–14 GB` free (`[profile.dev] debug = 0` in root `Cargo.toml` suppresses DWARF bloat).
- Python bridges (`tools/pyhecke/python/pyhecke/bridge.py`, `lp_dual_solver.py`, `computations/hecke/hecke_rust_bridge.py`) resolve binaries in order: explicit env override -> `$CARGO_TARGET_DIR/release/<bin>` -> `<repo-root>/target/release/<bin>` -> `crates/<crate>/target/release/<bin>` -> legacy `tools/<crate>/target/release/<bin>`.
- For native wheel builds, always pass `--out` (handled automatically by `CARGO_TARGET_DIR=/tmp/qou-shared-cargo-target CARGO_BUILD_JOBS=2 nice -n 15 bash scripts/build-pyhecke-native.sh`).

## 4. Registering Crates in the `tools` Knowledge Graph (`tool-defs/`)

Per `tool-authoring.md` Step 4 ("One folder per Tool, always"), every top-level crate under `crates/*/Cargo.toml` is registered as its own `tool-definition/v1` folder `tool-defs/crate-<slug>/crate-<slug>.json` alongside the summary manifest `tool-defs/crates.json`:

1. Add the crate under `crates/<name>/Cargo.toml` with complete `[package]` metadata (`name`, `version`, `edition`, `description`, `license`, `repository`), `[[bin]]` targets, and `[features]`, and list `"crates/<name>"` in root `Cargo.toml` `[workspace].members` (or `exclude` if target-specific like WASM/N-API/UniFFI).
2. Generate `tool-defs/crates.json` + `tool-defs/crate-*/crate-*.json` and verify the `tools` Knowledge Graph:
   ```bash
   bun run scripts/gen-crate-tools.ts
   bun run scripts/gen-crate-tools.ts --check
   bun run cat check:tools
   ```
3. Never hand-edit `tool-defs/crates.json` or `tool-defs/crate-*/crate-*.json`; `tool-defs/index.ts` loads them via `toolsFromFolders()` so every crate is a validated `ToolDefinition` node (`satisfies: ["rust-crates-and-values", "compute-author"]`).

## 5. Proton-Pin Witnessed Values via `qou-values`

Per the **2026-11-28 Owner Rulings** (proton pin only; muon pin on hold until rederivation; 80-dps MPFR certificates):

- **Active anchor:** All active Rust and Python evaluations use the **proton pin** ($q_0$ solved from CODATA $m_p / m_e$); the muon pin stays one switch away (`QOU_Q0_ANCHOR=muon`) on hold until the muon mass ratio is rederived.
- **Precision floor:** Compute at $\ge 80$ decimal digits (`prec_bits >= 280` in MPFR / `rug::Float`) and serialize exact decimal strings into `*.witness.json` with `"q0Anchor": "proton"` and `"q0Value"`. Never round through `f64`.
- **Evaluating & consuming values (`crates/qou-values`):**
  - Run `CARGO_TARGET_DIR=/tmp/qou-shared-cargo-target CARGO_BUILD_JOBS=2 nice -n 15 cargo run --release -p qou-values -- ...` to evaluate or query witnessed values directly from Rust without Python/sympy startup overhead.
  - Refresh/check `ACCURACY.md` via `python3 scripts/generate-accuracy-scorecard.py --check` (`--self-test`), and verify Folio JSON-LD freshness via `bash scripts/gen-block-jsonld.sh --check`.
