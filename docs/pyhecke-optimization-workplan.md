# pyhecke / hecke_core optimization workplan

Consolidated plan to address 12 identified optimization opportunities
across pyhecke, pyhecke_native, hecke_core, the Rust engine, and the
CI pipeline. Each item carries expected impact, implementation notes,
verification command, and ordered phase assignment so a future session
can pick up anywhere without losing coherence.

All work lands on `claude/add-quantum-gol-n5YS1` (or successor). Tests
must stay green: 138 pyhecke pytest + 9 Rust unit tests + 51 cert
schema validations.

---

## Phase A — cheap wins (≤ 1 h each)

### A1. Lazy `pyhecke.__init__` submodule loading

**Goal:** `import pyhecke.schema` must not force `pyhecke.trace`,
`pyhecke.tower`, etc. to load.

**Why it matters:** Today `pyhecke/__init__.py` imports every
submodule eagerly. A CLI that needs only `pyhecke.schema` pays the
full import chain including `crt_markov` and `tower_binding_symbolic`.

**Implementation:**
- Replace eager `from . import gram / wedderburn / trace / …` block
  with `__getattr__(name)` that imports on demand.
- Keep a `__all__` tuple so `dir(pyhecke)` still lists everything.
- Preserve the top-level re-exports (`G`, `G_INV`, `hm`, …) — they
  must trigger the lazy gram import, then expose the symbols.

**Files:** `tools/pyhecke/python/pyhecke/__init__.py`

**Verification:**
```bash
python3 -c "
import time, sys
t0 = time.monotonic()
import pyhecke.schema
dt = (time.monotonic()-t0)*1000
# Must not have loaded trace / tower / gram yet
assert 'pyhecke.trace' not in sys.modules
assert 'pyhecke.tower' not in sys.modules
print(f'{dt:.1f} ms, schema-only: OK')
"
```

### A2. Cache `jsonschema.Draft202012Validator` in `pyhecke.schema`

**Goal:** Avoid re-compiling the schema for every `validate()` call.

**Why it matters:** CI validates 51 certificates × 3 Python versions
= 153 compile-then-validate cycles. `functools.lru_cache` eliminates
150 of them.

**Implementation:**
- Wrap `validator(kind)` with `@functools.lru_cache(maxsize=4)`.

**Files:** `tools/pyhecke/python/pyhecke/schema.py`

**Verification:**
```bash
cd tools/pyhecke && pytest tests/test_schema.py -v
# Measure: before ~60s, after ~40s
```

### A3. Witness-staleness pre-check

**Goal:** Skip regeneration of a `*.witness.json` when the generating
script's content hash and all Python deps haven't changed.

**Why it matters:** Many pipelines run all scripts; most produce the
same witness they did last time.

**Implementation:**
- Extend `witness_base.WitnessBuilder` with a `skip_if_fresh(self)`
  method that compares `script_hash` against the existing witness's
  `scriptHash` field.
- Scripts that want the optimization wrap their main with
  `if not w.skip_if_fresh(): compute()`.

**Files:** `computations/substrate/witness_base.py`

**Verification:** rerun any migrated script twice; second run should
log "fresh; skipping" and take < 100 ms.

---

## Phase B — medium (2–4 h each)

### B1. Bisect `hecke_core` 42 s cold import  ⭐ HIGHEST ROI

**Goal:** Identify and eliminate whatever block of module-level code
takes 42 s to execute at import.

**Why it matters:** Every one of 260 scripts in `folio-assistant/
computations/` pays this tax on the first Python invocation.

**Implementation (bisect protocol):**
1. Copy `hecke_core.py` → `/tmp/hecke_core_test.py`.
2. Bisect: comment out the bottom half → time; then bottom quarter; etc.
3. Once the heavy block is < 100 lines, line-profile with `cProfile`
   wrapping the *suspected* sub-expression.
4. Fix: if it's a precomputation, gate behind `functools.cache` or
   move to a lazy `@property` on a `_HeckeConstants` class; if it's
   debug code, remove.

**Candidates flagged but not confirmed:**
- `build_nucleon_nf(...)` at lines 3040-3041 (`PROTON_NF`, `NEUTRON_NF`)
- `_chebyshev_magic()` at line 631
- `_load_categorical_shell()` at line 1371
- `_compute_k_coefficients()` at line 741
- `atom_per_generator_volumes` cache initialization
- Any `scipy.sparse` re-import overhead

**Files:** `computations/substrate/hecke_core.py`

**Verification:**
```bash
python3 -c "
import time
t0 = time.monotonic()
import hecke_core
dt = (time.monotonic()-t0)*1000
assert dt < 2000, f'hecke_core import still slow: {dt} ms'
print(f'{dt:.0f} ms — acceptable')
"
```

Target: < 2000 ms (21× speedup).

### B2. Port `build_atom_nf` / `additive_wedderburn_volumes` to Rust

**Goal:** PyO3 `pyhecke_native.build_atom_nf(Z, N)` and
`pyhecke_native.additive_wedderburn_volumes(n_strands, cross)`.

**Why it matters:** Heavy-atom tower witnesses (e.g. ⁴⁰Ca) spend
~80 % of wall time in these two functions.

**Implementation:**
- Rust port in `tools/hecke-engine/src/gram.rs` (or new `src/nf.rs`):
  `pub fn build_atom_nf(z: u32, n: u32) -> [f64; 6]`
  `pub fn additive_wedderburn_volumes(n_strands: u32, cross: &[Vec<(f64, f64)>]) -> Vec<[f64; 3]>`
- PyO3 wrapping in `tools/pyhecke-native/src/lib.rs`.
- `pyhecke.bridge.build_atom_nf_native(Z, N)` dispatcher.

**Files:**
- `tools/hecke-engine/src/gram.rs` or new `nf.rs`
- `tools/pyhecke-native/src/lib.rs`
- `tools/pyhecke/python/pyhecke/bridge.py`
- `tools/pyhecke/tests/test_native.py`

**Verification:** add `test_native_build_atom_nf_matches_python` that
runs Python and Rust versions on (Z, N) ∈ {(1,0), (6,6), (20,20)} and
asserts max abs diff < 1e-12.

**Expected impact:** 50–100× speedup for ⁴⁰Ca witnesses; end-to-end
heavy-atom pipeline goes from minutes to seconds.

### B3. Audit all module-level side effects — DONE (documented)

**Status:** audit complete. 26 scripts have top-level
`WitnessBuilder(...)` + `.save()` NOT guarded by `__main__`:

```
atom_mass_atomic_braid.py
atom_mass_combined.py
ch-bond-writhe-lp.py
co-molecular-binding.py
co2-molecular-binding.py
confined_knot_binding.py
correlated_channel_mass.py
electron-shell-ilp.py
frobenius-bond-all.py
h2-integer-lp.py
h2-molecular-binding.py
hadron_knot_table.py
hh-trefoil-corrected.py
hh-vertex-volume.py
intermediate_knot_detection.py
jet_knot_invariants.py
molecular-frobenius-lp.py
molecular-ilp.py
molecular-integer-lp.py
molecular-trefoil-scan.py
molecular-valence-channel.py
molecular-vertex-volume.py
nf_transition_lifting.py
nuclear_ilp.py
unified-mass-molecular.py
universal-ilp.py
```

**Gotcha:** None of these are imported by any other script. So the
tax only fires when they are run directly as `python <name>.py` —
which is exactly what you want. Adding `if __name__ == "__main__":`
guards is hygiene, not performance.

**Action:** skipped in this session. A follow-up cosmetic pass can
wrap each in `__main__` for consistency with `mass_endomorphism.py`
(M3d), but no end-to-end speedup is available here.

### B3-historical. Previously audited

**Goal:** Grep every `computations/*.py` for
top-level `WitnessBuilder`, `print`, heavy function calls; guard each
under `if __name__ == "__main__":`.

**Why it matters:** `mass_endomorphism` was 36 s; others may have
similar hidden costs.

**Implementation:**
```bash
cd computations
for f in *.py; do
  # Find top-level WitnessBuilder / heavy compute after the last
  # def/class
  python3 -c "
  import ast
  src = open('$f').read()
  tree = ast.parse(src)
  for node in tree.body:
      if isinstance(node, ast.Expr):
          print(f'$f:{node.lineno}: top-level Expr')
      if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
          # Assignment that calls something
          fn = getattr(node.value.func, 'id', '<attr>')
          if fn in ('WitnessBuilder',):
              print(f'$f:{node.lineno}: top-level {fn}(...)')
  "
done
```

Then per-site: wrap the heavy block under `__main__`.

**Files:** Many. Estimate 3–8 additional scripts.

**Verification:**
```bash
python3 -c "
import time, importlib
TEST = ['confinement_level_walk', 'tower_binding_full', ...]
for m in TEST:
    t0 = time.monotonic()
    importlib.import_module(m)
    dt = (time.monotonic()-t0)*1000
    assert dt < 500, f'{m}: {dt} ms still slow'
"
```

### B4. Parallelise `run_pipeline.py`

**Goal:** Run independent witness computations in parallel processes.

**Why it matters:** `run_pipeline.py --content-only` is sequential.
On a 4-core runner, a trivial `multiprocessing.Pool(4)` gives ~3×.

**Implementation:**
- Identify dependency-free scripts (no shared state beyond files).
- Replace loop with `Pool.imap_unordered`.
- Cap concurrency to `min(4, cpu_count())` to avoid CI OOM.

**Files:** `computations/run_pipeline.py`

**Verification:** wall time on full pipeline drops from minutes to
~⅓; all witnesses still produced.

### B5. Audit `hecke_startup_cache` adoption

**Goal:** Every script that imports `hecke_core` should first try
`hecke_startup_cache.load_cache()` (which is < 10 ms when fresh) and
only fall back to `from hecke_core import …` for symbols not in the
cache.

**Why it matters:** `hecke_startup_cache` precomputes `G`, `alpha_em`,
Wedderburn weights, etc. Once B1 lands, the 50 ms cache load
eliminates the hecke_core cold-path entirely for common constants.

**Implementation:**
- Grep for `from hecke_core import` across the 260 scripts.
- For each, check whether the imported symbols are cached.
- If yes: change to `from hecke_startup_cache import load_cache;
  C = load_cache(); G = C["gram_matrix"]; …`.
- Alternatively: add a pyhecke-level `load_constants()` helper that
  prefers the cache, falls back to hecke_core.

**Files:** ~30 scripts under `computations/`.

**Verification:** each migrated script imports in < 50 ms.

### B6. Rust-binary linking / crate-split

**Goal:** Reduce `cargo build --release` wall time from 10–20 s per
binary to ≤ 5 s.

**Why it matters:** `rug`/`gmp-mpfr-sys` are the slow linker
dependencies. Currently rebuilt for each of 15 binaries.

**Implementation:**
- Move the MPFR-dependent code to its own crate
  `tools/hecke-engine-rug/` exposed as a library.
- The 15 binaries depend on the thin library, not on `rug` directly.
- Standard Cargo incremental build caches the library's .o files.

**Files:** `tools/hecke-engine/Cargo.toml` + new crate scaffolding.

**Verification:** `cargo build --release --bin hecke-mass` after a
clean lib build completes in < 5 s.

### B7. Certificate regen hash-skip

**Goal:** Only regenerate `certificate-*.json` when `engine/v19_…`
source (or its deps) has changed.

**Why it matters:** Once CI is back, cert-diff gating should be fast.

**Implementation:**
- Embed `git hash-object` of the producing binary + `certificate.rs`
  into every cert's `engine.commit` field at generation time.
- In the regen CI job: `for cert in certs; check commit; skip if matches`.

**Files:** `tools/hecke-engine/src/certificate.rs`, future `.github/
workflows/cert-regen.yml`.

**Verification:** clean CI run on PR that doesn't touch hecke-engine:
the cert-regen job logs "all 51 certs up-to-date, skipped".

---

## Phase C — research-grade (6–10 h each)

### C1. Port `build_atom_nf` full correctness (B2 extended)

Once B2 scaffolding works for simple `(Z, N)`, extend to:
- Full atom NF with electron insertion (Z electrons).
- `build_atom_nf_exact` variant (Fraction arithmetic in Rust via
  `num-rational::Ratio<BigInt>`).
- Molecule construction via `atom × bond × atom`.

**Effort:** 6–10 h on top of B2. Significant Lean-side parallel: any
theorem in `QOU/Descartes/NuclearNormalForms.lean` that references
`build_atom_nf` needs its Lean counterpart updated, though proofs
stay `sorry`.

### C2. CRT polynomial reconstruction in Rust

Replace `sympy` in `tower_binding_symbolic.py` with a Rust
`pyhecke_native.crt_reconstruct(points)` backed by
`num-rational::Ratio<BigInt>` Lagrange interpolation.

**Implementation:**
- `tools/pyhecke-native/src/crt.rs` exposing
  `crt_reconstruct(points: Vec<(Fraction, Fraction)>, e_min: i32, e_max: i32) -> LaurentPoly`.
- `LaurentPoly` serde-serializable, compatible with pyhecke `crt.py`.

**Expected impact:** enables `tower_binding_symbolic` at A ≥ 4
(currently explodes in sympy). Unlocks exact symbolic-in-q evaluation
for heavy-atom binding without mpmath rounding.

---

## Dependency graph

```
A1 (lazy __init__) ──────┐
                         │
A2 (jsonschema cache) ───┴──► Phase B ready
A3 (witness skip)    ───┘

B1 (hecke_core bisect) ◄── HIGHEST ROI, do first in Phase B
   │
   ├──► B5 (startup_cache adoption) — uses B1's speedup
   └──► B3 (module-side-effect audit) — parallel

B2 (Rust build_atom_nf) ──► C1 (extended correctness)

B4 (parallelise pipeline) — independent
B6 (crate split)         — independent, helps B7
B7 (cert regen skip)     — requires B6 for speed
```

## Test strategy

Every change must keep:

1. `cd tools/pyhecke && pytest -q` — 138 passing
2. `cd tools/hecke-engine && cargo test --release --lib` — 9 passing
3. `cd tools/pyhecke-native && maturin build --release` — clean build
4. `python -c "import json, jsonschema; ..."` — all 51 certs validate

Add one new test per item, placed in the appropriate `tests/test_*.py`
or `#[cfg(test)] mod tests` block.

## Commit cadence

One commit per lettered item (A1, A2, …, C1, C2). Commit messages
follow the session convention `Mx: <title>` where x reflects the
item. CI-diff verification of witness JSON is still blocked on
billing; document manual local verification in each commit body.

## Estimated total effort

| Phase | Hours | Outcome |
|:--|--:|:--|
| A (1 + 2 + 3) | ~3 | Cheap wins in place |
| B (1 through 7) | ~18 | Major speedups; import ≤ 2 s; heavy-atom witnesses seconds not minutes |
| C (1 + 2) | ~15 | Exact symbolic pipeline; ⁴⁰Ca end-to-end in Rust |

~36 hours of focused work to land the full slate. Phase A can ship in
one session; Phase B splits cleanly into 7 independent sessions.
