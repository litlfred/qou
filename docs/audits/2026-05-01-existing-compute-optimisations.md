# Survey of existing compute optimisations

**User request (2026-05-01)**: review existing compute optimisations before
investing in new ones for P2.2c-12C.

**Branch**: `claude/audit-math-framework-FXlp2`

## Headline

Substantial optimisation infrastructure already exists in the repo:

| Tier | Mechanism | Status |
|------|-----------|--------|
| **Native (Rust)** | `tools/hecke-engine/` + `tools/pyhecke-native/` | 🟡 source exists, **not built** |
| Python wrappers | `tools/pyhecke/` | 🟢 in use |
| Python caches | `syt_prefix_cache`, `hecke_startup_cache`, `ordering_cache`, `knot_operation_cache`, `q_mn_recursive_memoized` | 🟢 |
| Sparse seminormal | auto-sparse for `dim > 500` in `build_seminormal_matrices` | 🟢 |
| Symbolic-in-q | sympy + `witness_polynomial` helper | 🟡 partially wired (P2.5 Tier B) |
| CRT poly recon | `crt_markov.py` (low levels only) | 🟢 |
| mpmath direct | `schur_weyl_mpmath.py` (this session) | 🟢 |

The most important unused asset is the **Rust kernel** (`pyhecke_native`),
which would unlock A=12+ q-Hecke compute via:
- C-level seminormal matrix multiplication (vs Python/scipy.sparse)
- mpfr-backed arbitrary-precision character evaluation
- Geck-Pfeiffer character algorithm (vs Murnaghan-Nakayama recursion)

## 1. Native Rust kernel (`tools/hecke-engine/` + `tools/pyhecke-native/`)

### What's there

- **`hecke-engine/`** — Rust crate with the hot kernels:
  - `seminormal::seminormal_matrices(shape, q)` → seminormal matrices
  - `seminormal::chi_lambda_braid(shape, word, q)` → character on braid word (f64)
  - `seminormal_mpfr::chi_lambda_braid_mpfr(...)` → arbitrary-precision character
  - `geck_pfeiffer::chi_lambda_via_gp_hoefsmit(...)` → Geck-Pfeiffer + Hoefsmit
  - `geck_pfeiffer::chi_lambda_via_geck_pfeiffer(...)` → Geck-Pfeiffer alone
  - `seminormal_mn::mn_chi(lambda, mu)` → MN character in Rust
  - `gram::*` — Gram matrix, Markov weights, NF multiplication

- **`pyhecke-native/`** — PyO3 bindings exposing the Rust kernels as a
  Python `pyhecke_native` module. Built with `maturin build --release`.

- **`pyhecke/`** — pure-Python wrapper / bridge that uses the native module
  when available, falls back to Python.

### Why it matters

- `hecke_characters.chi_lambda_braid(precision="mpfr_50dps")` requires
  `pyhecke_native`; raises `precision=mpfr_50dps requires the Rust kernel
  (pyhecke_native). Install via 'maturin build' in tools/pyhecke-native/`
  when not built.

- For A ≥ 12, length-≤-2 partition dims explode (`dim_{(33, 3)} = 6510`,
  `dim_{(28, 8)} ≈ 380M`, `dim_{(18, 18)} ≈ 478M`). Python sparse-trace
  is O(dim² × k) per partition — minutes to hours per partition.

- Rust LTO + opt-level=3 typically delivers **50–200×** speedup over
  Python for matrix-heavy kernels, and the Geck-Pfeiffer algorithm
  bypasses the Hoefsmit dim-explosion entirely.

### Action

This session attempts to **build** `pyhecke-native` (`maturin build --release`
in `tools/pyhecke-native/`). If successful, P2.2c-12C unlocks via
`chi_lambda_braid(..., precision="mpfr_50dps")`.

## 2. Python-side caches

### `syt_prefix_cache.py`

Per the `compute_mass_at_level` docstring (in `hecke_characters.py`):

> `block_cache`, if given, must be a `syt_prefix_cache.BlockCache` pinned
> to the same q used for the seminormal-matrix build. When supplied, the
> per-partition loop routes through `syt_prefix_cache.build_seminormal_matrices_cached`
> instead of the uncached `build_seminormal_matrices`, reusing Hoefsmit
> content-distance arithmetic and the per-shape SYT→index map across
> shapes. **Expected 5–20× speedup on heavy atoms** (A ≥ 10, k = 3A
> with p(3A) ≥ 5604 partitions and dim_λ up to ~1000).

This is a real win for `compute_mass_at_level` callers, but is
**not used by my new `chi_lambda_atomic`** in `schur_weyl_q_hecke_v2.py`.
Wiring `BlockCache` would give a 5-20× speedup on top of any other
optimisation.

### `hecke_startup_cache.py`

Precomputes Gram matrix, Wedderburn weights, etc. for `hecke_core` —
loaded at startup.

### `ordering_cache.py` / `knot_operation_cache.py`

Caches for nucleon orderings and knot operations.

### `q_mn_recursive_memoized.py`

Recursive memoised Murnaghan-Nakayama. Cross-validated against S_3,
S_4, S_5 character tables. Faster than the naive `mn_character` for
batch character evaluation.

## 3. Sparse seminormal matrices

`build_seminormal_matrices(shape, sparse=None, q=None)` automatically
uses `scipy.sparse.csr_matrix` when `dim > 500`. Each Hoefsmit matrix
has at most 2 nonzeros per row (1×1 and 2×2 blocks), so sparse format
gives ~dim/2× memory savings.

**Limitation**: matrix-product accumulation densifies after ~log_2(dim)
multiplications. For A=12 with dim=6510, after ~13 of the ~75 atomic-braid
crossings, the running product becomes dense. The
`sparse_trace_of_product.py` (this session) bypasses by computing the
trace via per-basis-vector iterative products — still O(dim²·k) per
partition.

## 4. Symbolic-in-q (P2.5 Tier B)

The `witness_polynomial.py` helper (this session) factors the boilerplate
for exposing both symbolic-q and numerical-q-evaluation forms in a witness
JSON. Three exemplars migrated; ~78 scripts remain. Mechanical migration.

## 5. CRT polynomial reconstruction

`crt_markov.py` already has the CRT-style polynomial reconstruction
infrastructure (Lagrange interpolation across multiple rational q values,
recovering ℤ[q^{±1}] coefficients). Currently used at H_3 levels only.
Could scale to H_{3A} but mostly superseded by the mpmath direct path
(`schur_weyl_mpmath.py`) which is faster for most use cases.

## 6. mpmath direct (this session)

`schur_weyl_mpmath.py` bypasses sympy entirely for the q=1 MN Schur-Weyl
sum. Scales to A=40 in 0.25 s. The mass-tower production path now uses
this via `crt_markov.markov_trace_schur_weyl_eval`.

## What's NOT yet optimised

For q-Hecke at A=12+ (the live bottleneck):

1. **Geck-Pfeiffer character algorithm** — the Rust kernel has
   `chi_lambda_via_geck_pfeiffer` and `chi_lambda_via_gp_hoefsmit`. GP
   bypasses Specht-module dimension explosion by computing the character
   via Hecke-algebra basis identities, not matrix traces. Asymptotic
   complexity is much better than O(dim²·k).

2. **`syt_prefix_cache.BlockCache`** — not wired into
   `schur_weyl_q_hecke_v2.chi_lambda_atomic`. Would give 5-20× on top
   of whatever else.

3. **Native Rust** — `pyhecke_native` not built; building it (in flight
   as `maturin build --release`) unlocks the mpfr-precision and C-level
   speedups.

## Recommendation

**Order of operations** (most to least leverage for A=12+):
1. Build `pyhecke_native` — unlocks Rust kernels (this session attempt).
2. Wire `chi_lambda_via_geck_pfeiffer` (via Rust kernel) into
   `schur_weyl_q_hecke_v2.chi_lambda_atomic`.
3. Add `BlockCache` for cross-partition caching.

If steps 1 + 2 land, A=12+ q-Hecke becomes seconds-per-atom, not
minutes-per-partition.

If the build fails (e.g. PyO3 version mismatch with system Python),
the practical fallback is to keep the **HYBRID** at A ≤ 4 (which is
sufficient for the validation deliverable) and document A=12+ as
"unblocked by Rust kernel build".
