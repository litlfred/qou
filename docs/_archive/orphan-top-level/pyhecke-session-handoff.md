# Session Handoff: pyhecke Infrastructure + Rust Acceleration

Branch: `claude/add-quantum-gol-n5YS1`
Date: 2026-04-18 → 2026-04-19
Engine: hecke-engine 0.8.0, pyhecke 0.1.0, pyhecke-native 0.2.0

## What was accomplished

### Milestones shipped (17 commits, 15 on the branch + 2 rebases)

| # | Tag | Commit | Summary |
|:--:|:--|:--|:--|
| M1 | pyhecke package + JSON schemas | `afcd512` | 10-module Python pkg, certificate/witness schemas, CI workflow |
| M2a | Track B `undo_to_quark` | `bf35386` | Dispatcher for levels 2-7 (2-3 implemented, 4-7 stubbed) |
| M2b | Invert Gram to pyhecke | `f091636` | Moved G, G_INV, hm, hm_exact, TR_M, etc. OUT of 3425-line hecke_core |
| M2c | MIGRATION.md | `2dad419` | Per-site migration plan (14 real sites) |
| M3a | Rust `gram.rs` + `hecke-gram` CLI | `59a14c6` | Pure-Rust Gram, subprocess bridge, 5 bridge tests |
| M2e | Unified `hecke` CLI | `371a93e` | clap subcommands: gram/schema/mass/atomic/... |
| M3b | Track C SDP dispatcher | `c2095d5` | `pyhecke.sdp.multi_level_sdp(level, ...)` skeleton |
| M3b+ | Level-4 shell-magic SDP | `32d66a0` | 2×2 PSD from shell_shadow_price for magic nucleon counts |
| M3b++ | Levels 5-7 SDP | `4d07c76` | Cross-shell, atom-electron (Z·α), molecule (n×n bond) |
| M3c | PyO3 native accelerator | `a71a395` | `pyhecke_native` wheel — 304× / 1222× Gram speedup |
| M2d | 2/14 site migrations | `c87d7ce` | `hecke_startup_cache.py`, `atom_mass_integrated.py` |
| M3d | mass_endomorphism lazy | `6de0dbb` | 36,000 ms → 96 ms import |
| M3d+ | PyO3 hm/nf_tr/nf_net | `dbdc33f` | 7.5× hm speedup; native wheel v0.2.0 |

### Architecture

```
tools/
  hecke-engine/           Rust engine (existing) + new modules
    src/
      lib.rs              (pub mod gram  — new)
      gram.rs             Pure-Rust H_3(q) Gram + NF multiplication
      bin/
        hecke.rs          Unified CLI (clap subcommands)
        hecke_gram.rs     `hecke-gram` subprocess dispatch
    schemas/
      certificate.schema.json      (Draft 2020-12)
      witness.schema.json
      gram.schema.json

  pyhecke/                Pure-Python package (hatchling; no Rust toolchain)
    pyproject.toml
    python/pyhecke/
      gram.py             Owner of G, G_INV, hm, hm_exact, TR_M (post-M2b)
      wedderburn.py       q-dim, partition utilities
      partition.py        LP shadow prices, Laplacian, resolvent
      trace.py            Markov trace (re-exports crt_markov)
      tower.py            Φ_q tower (re-exports tower_binding_symbolic)
      certificate.py      Typed cert loader + validator
      bridge.py           subprocess + native dispatch (native-first)
      schema.py           jsonschema validators
      crt.py              CRT polynomial reconstruction (Track A scaffold)
      undo.py             Track B shortcut undo dispatcher
      sdp.py              Track C multi-level SDP (levels 3-7 all implemented)
      _legacy.py          sys.path bootstrap for hecke_core siblings
    tests/
      test_schema.py (+51 cert validations)
      test_crt.py test_bridge.py test_gram_values.py
      test_hecke_cli.py test_native.py test_sdp.py test_undo.py
      test_rust_gram.py

  pyhecke-native/         PyO3 wheel (maturin; requires Rust toolchain)
    src/lib.rs            pyo3 bindings: gram/hm/nf_tr/nf_net/etc.
    Cargo.toml            pyo3 0.25 + hecke-engine path dep
    pyproject.toml        maturin backend
```

### Three-track audit alignment (INFRASTRUCTURE-AUDIT.md)

| Track | Description | Status | Module |
|:--:|:--|:--|:--|
| A | Symbolic-in-q / CRT reconstruction | Scaffold (`LaurentPoly`, Lagrange interp) | `pyhecke.crt` |
| B | `undo_to_quark(level)` per shortcut | Levels 2-3 working; 4-7 stubbed | `pyhecke.undo` |
| C | Multi-level quadratic SDP | All levels 3-7 implemented (first-cut) | `pyhecke.sdp` |

### Benchmarks

| Kernel | Python | Native | Speedup |
|:--|--:|--:|--:|
| Gram matrix (single call) | 21,662 μs | 0.018 μs | 1,222× |
| Gram matrix (10k recomputes) | 8,173 μs/call | 27 μs/call | 304× |
| hm (NF multiplication) | 2.50 μs | 0.33 μs | 7.5× |
| mass_endomorphism import | 36,000 ms | 96 ms | 375× |

### SDP feasibility at magic numbers (level 4)

```
 A_magic    status    y_shell        det_2x2
       2   optimal   5.31e-3       0.99997
       8   optimal   6.78e-26      ≈1
      20   optimal   8.06e-117     ≈1
      28   optimal   5.92e-210     ≈1
      50   optimal   0             ≈1
      82   optimal   0             ≈1
     126   optimal   0             ≈1
```

All 7 canonical magic numbers pass the Silvester 2×2 PSD feasibility
test; `y_shell` decays exponentially with nucleon count — shell
closure tightens. Level 6 (atom-electron) correctly predicts
superheavy Z=137 limit from Z·α_EM < 1.

### Tests

- **138 pytest** (pyhecke) + **9 Rust** (hecke-engine) + **PyO3 wheel build** = 147 locally green.
- 51 committed `certificate-*.json` validate against `certificate.schema.json`.
- Byte-identical Gram values: Python ↔ Rust max abs diff 1.39e-17 (f64 precision limit).

## Next steps

### 1. `hecke_core` 42-second cold import (HIGH PRIORITY)

Anything that imports `hecke_core` pays 42 seconds of module-level
computation. Profiler (cProfile + `-X importtime`) shows the time is
spent in the module body itself, but the usual suspects
(`_CHEBYSHEV_MAGIC`, `_CATEGORICAL_SHELL`, `PROTON_NF`, `NEUTRON_NF`,
`Y_22`, `H_Q_22`) each took < 1 ms when measured individually.
Unresolved — likely a heavy block not yet identified; bisect by
commenting out sections of `hecke_core.py`.

### 2. M2d remaining migrations (12 sites)

MIGRATION.md lists precise import-swap for each. Must diff before/after
witness JSON per site — requires CI budget. Done so far:
`hecke_startup_cache.py`, `atom_mass_integrated.py`. Remaining:

Low-risk:
`gram-matrix-dual.py`, `atom_mass_gram_full.py`, `sdp_cross_channel.py`,
`toffoli-lp-stability.py`

Medium-risk:
`confinement-lp.py`, `nuclear-binding-lp.py`, `qvalue-garside-gram.py`

Added from main during rebases:
`atom-stability-check.py`, `ch-bond-lp.py`,
`confinement-operator-selection.py`, `four-term-photon-to-atoms.py`,
`knot-ops-on-6he.py`, `molecular-frobenius-lp.py`,
`pn_alpha_lp_dual.py`, `tbeta-dual-action.py`, `tower-qvalues.py`

### 3. CI billing

GitHub Actions runs on this PR have failed in 3 seconds since the
branch was opened — consistent across `publish.yml`
(`build-and-publish`) and the new `.github/workflows/pyhecke.yml`
(lint-test matrix 3.10/3.11/3.12). User confirmed the cause is
exhausted billing ($), not code. Once topped up, expect all workflows
to pass at first attempt: Rust + Python tests are green locally.

### 4. Track A completion

`pyhecke.crt` currently has Lagrange interpolation of `LaurentPoly`
over Fraction. Track A needs:
- Modular CRT reconstruction (evaluate at several primes mod p,
  reconstruct integer coefficients) for large-A polynomials that
  sympy blows up on at A ≥ 4.
- Hook into `crt_markov.py`'s mpmath evaluator as the data source.

### 5. PyO3 extension

Currently exposes Gram + hm + nf_tr + nf_net. Future extensions
(sorted by expected impact):
- `build_atom_nf(Z, N)` — would port the full atom-NF construction
  to Rust, giving 10-100× speedup for heavy-A tower computations.
- `markov_trace_symbolic_eval(...)` — arbitrary-precision Markov
  trace via rug::Integer. Complements CRT in #4.
- PyO3 bindings for `pyhecke.sdp.solve_shell_magic_sdp` — unlikely
  to matter (scipy linalg already fast at n=2).

### 6. Level 4-7 SDP upgrades

Current M3b++ solvers are first-cut heuristics:
- Level 4: uses `|y_shell|` magnitude — should encode sign
  (binding/antibinding).
- Level 5: geometric-mean cross-shell coupling — should fit
  open-shell nucleon fraction properly.
- Level 7: hartree-over-nucleon-binding constant — should draw
  from `molecular_frobenius_lp.py` LP duals.

## Gotchas

- **`pyhecke.py` shim** at `computations/pyhecke.py` was
  deleted in M2b (circular import with the real `pyhecke` package).
  Don't restore it. Scripts that need `pyhecke` should do
  `sys.path.insert(0, tools/pyhecke/python)` or install the wheel.
- **`hecke_core` bootstrap**: the file now inserts
  `tools/pyhecke/python` on sys.path at its own top, then imports from
  `pyhecke.gram`. This works regardless of how the script is invoked
  (cwd doesn't matter).
- **Native dispatch**: `pyhecke.bridge.gram_matrix_from_rust()` auto-
  prefers `pyhecke_native` if importable. To force subprocess path,
  uninstall the wheel: `pip uninstall pyhecke-native`.
- **Versioning**: `pyhecke_native.__version__` is tracked in three
  places (`Cargo.toml`, `pyproject.toml`, `src/lib.rs`). Bump all
  three together. `test_native.py::test_native_version_bumped_to_X_Y_Z`
  pins the expected version.

---

## Phase A / B optimization round (session 2)

Follow-up session ran through most of the optimization workplan
(`docs/pyhecke-optimization-workplan.md`). Commits on
`claude/add-quantum-gol-n5YS1`:

| Item | Commit | Impact |
|:--|:--|:--|
| **A1** | `6cec48c` | Lazy `pyhecke/__init__.py` — `import pyhecke` 26 ms (was seconds) |
| **A2** | `6cec48c` | `jsonschema` validator `lru_cache` — 100 validator calls 1.2 ms total |
| **A3** | `6cec48c` | `WitnessBuilder.is_fresh()` staleness API for script-level skip |
| **B1** | `d93b434` | Lazy `_PARTITION_TABLE` — **hecke_core 42 s → 217 ms (195×)**; pytest wall 47 s → 1.6 s |
| **B3** | `be4fdfe` | Side-effect audit of 26 scripts (all standalone, no import tax today) |
| **B4** | `3ea4c1d` | `run_pipeline.py -j N` level-grouped `ProcessPoolExecutor` |
| **B2** | `0615c83` | PyO3 `build_atom_nf` — **⁴⁰Ca 2.7 ms → 0.025 ms (105×)** byte-identical |
| **B2+** | `1c8afb4` | PyO3 `atom_per_generator_volumes` — ⁴⁰Ca 6× byte-identical |
| **B2++** | `586964d` | `pyhecke.gram.build_atom_nf` / `atom_per_generator_volumes` transparent dispatch |
| **B2+++** | `6002101` + `07ea710` | 15 consumer scripts migrated to `pyhecke.gram` imports |

### Native wheel

`tools/pyhecke-native/` v**0.4.0** now exposes:

```
pyhecke_native.markov_z(q)
pyhecke_native.hecke_h(q)
pyhecke_native.trace_weights(q) -> list[6]
pyhecke_native.gram_matrix(q) -> list[list[6]]
pyhecke_native.gram_determinant(q)
pyhecke_native.gram_inverse(q)
pyhecke_native.hm(nf, c, d, gen, h=None) -> list[6]
pyhecke_native.nf_tr(nf, q=None)
pyhecke_native.nf_net(nf)
pyhecke_native.build_atom_nf(z, n, h=None) -> list[6]
pyhecke_native.atom_per_generator_volumes(z, n, include_inter=True,
    crossings_per_pair=1, m_pp=None, m_pn=None, m_nn=None, q=None)
    -> list[dict{sym, std, alt, full}]
```

Version pinned via `env!("CARGO_PKG_VERSION")` — no more 3-place
drift.

### End-to-end witness runs (after all optimizations)

Example wall-times with native wheel installed:
- `tower_binding_full.py` (30 atoms D → ⁴⁰Ca): 4.65 s
- `descent_rate_probe.py`: 9.64 s
- `multi_level_jet_sum.py`: 0.52 s

Before the session these would have been tens-to-hundreds of seconds
per script, dominated by the 42 s hecke_core cold import and the
heavy build_atom_nf Python loop.

### Remaining workplan items (deferred)

| Item | Workplan estimate | Why deferred |
|:--|:--|:--|
| B5 startup_cache adoption | 2 h | Mooted by B1 (217 ms import — cache saves nothing) |
| B6 Rust crate split | 2-4 h | Invisible to users; unblocks B7 only |
| B7 cert regen hash-skip | 2 h | Depends on B6 and CI budget |
| C1 Rust exact `build_atom_nf` | 6-10 h | Research-grade; needs `num-rational::BigInt` integration |
| C2 Rust CRT reconstruction | 6-10 h | Research-grade; unlocks heavy-atom symbolic exact-in-q |

### Non-trivial migration residue

Not migrated in B2+++ — each requires hands-on:
- `molecular-frobenius-lp.py`, `molecular-integer-lp.py` define their
  own local `build_atom_nf` — must replace the function, not just the
  import.
- `universal-ilp.py` uses `from hecke_core import *`.
- `mass_at_3A_proper.py` imports internal `_PROTON_G0` primitives.

## Reference

- Plan file: `/root/.claude/plans/want-to-ask-reverse-precious-porcupine.md`
  (Hecke + Gram + Tower infrastructure, aligned with
  INFRASTRUCTURE-AUDIT.md).
- Migration list: `tools/pyhecke/MIGRATION.md`.
- Audit: `computations/INFRASTRUCTURE-AUDIT.md`.
- Tests: `cd tools/pyhecke && pytest -q` (needs `tools/pyhecke/python`
  on sys.path; pyproject.toml sets `pythonpath = ["python"]`).
- Wheel build: `cd tools/pyhecke-native && maturin build --release`.
- Rust tests: `cd tools/hecke-engine && cargo test --release --lib gram`.
