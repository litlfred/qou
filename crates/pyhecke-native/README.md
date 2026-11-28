# pyhecke-native

> *Part of the [QOU library stack](../https://github.com/litlfred/qou/blob/main/docs/ARCHITECTURE.md#two-axes-of-organisation-domain-vs-workflow). See the two-axis explanation for how this package fits relative to the in-repo `computations/` clusters.*

PyO3 native acceleration layer for `pyhecke`.

Exposes zero-copy Rust implementations of the hottest H_n(q) kernels
as a Python extension module `pyhecke_native`, built via maturin.

## Functions

```python
pyhecke_native.gram_matrix(q: float) -> list[list[float]]
pyhecke_native.gram_determinant(q: float) -> float
pyhecke_native.markov_z(q: float) -> float
pyhecke_native.hecke_h(q: float) -> float
pyhecke_native.trace_weights(q: float) -> list[float]
```

## Build

Requires [maturin](https://www.maturin.rs), a working Rust toolchain, and
system **GMP + MPFR** (for `rug`). As of 2026-06-28 the default wheel also
builds the Clarabel MPFR LP backend, which needs the **litlfred Clarabel.rs
fork** reachable — see [§"Clarabel (litlfred fork)"](#clarabel-litlfred-fork)
below for why, and for the restricted-network fallbacks.

```bash
pip install maturin
cd tools/pyhecke-native
maturin develop --release      # default features = ["clarabel-lp"]
```

or for a distributable wheel:

```bash
maturin build --release
# produces target/wheels/pyhecke_native-*.whl
```

`maturin develop` requires an active virtualenv/conda env; otherwise use
`maturin build --release` and `pip install target/wheels/pyhecke_native-*.whl`.

## Clarabel (litlfred fork)

The wheel's default `clarabel-lp` feature pulls **Clarabel.rs from the litlfred
fork**, pinned in `[patch.crates-io]` of both this crate's and
`tools/hecke-engine/Cargo.toml`:

```toml
[patch.crates-io]
clarabel = { git = "https://github.com/litlfred/Clarabel.rs", rev = "9673209" }
```

**Why the fork (not crates.io `clarabel`):** the QOU compute needs Clarabel's
`MpfrFloat` arbitrary-precision scalar backend (the `mpfr` cargo feature) plus
the `bigrational` backend and the `rug`-interop that lets `seminormal_mpfr`'s
`rug::Float` outputs flow into the solver without an f64 round-trip. Those land
on the fork (upstream PR <https://github.com/litlfred/Clarabel.rs/pull/1>);
crates.io `clarabel` 0.11 does **not** carry the `mpfr` feature, so a plain
`cargo`/crates.io resolution fails. The pin is validated at rev `9673209`
(71/71 hecke-engine tests pass under `--features clarabel-sdp`); see
[`tools/hecke-engine/CLARABEL_PRECISION_PLAN.md`](../hecke-engine/CLARABEL_PRECISION_PLAN.md).
The pin will be lifted once the fork merges to its own `main` and cuts a
crates.io release.

**No BLAS needed.** `clarabel-lp` → `hecke-engine/clarabel-mpfr` uses the
`MpfrFloat` scalar, **not** the netlib SDP cone backend, so it needs only system
GMP + MPFR (already required by `rug`) — **not** OpenBLAS/LAPACK/gfortran. The
f64 SDP solver (`hecke-engine`'s `clarabel-sdp`, which *does* need BLAS) stays
opt-in. Since fork rev 37f06c3 it combines with `clarabel-mpfr` as
`hecke-engine`'s `clarabel-mpfr-sdp` (MPFR SDPs at 50+ digits; needs gfortran).

### Restricted-network / egress-blocked builds

Some environments (e.g. a web sandbox whose egress policy returns **403** for
`github.com/litlfred/Clarabel.rs`) cannot fetch the fork. The seminormal / Gram
/ Markov-trace primitives — including `seminormal_matrices_mpfr` and
`chi_lambda_braid_mpfr` — do **not** need clarabel, so either:

1. **Drop clarabel:** `maturin build --release --no-default-features`
   (builds the `rug`/MPFR kernels only — everything except `operator_selection_lp`).
2. **Stub clarabel:** create a local empty crate `clarabel` v0.11.x declaring the
   referenced features as empty —
   `[features] mpfr=[] sdp-netlib=[] serde=[] bigrational=[]` — with an empty
   `src/lib.rs`, then repoint `[patch.crates-io] clarabel = { path = "<stub>" }`.
   Because clarabel is an *optional* dep that the default-but-feature-gated build
   only *resolves* (never compiles unless a clarabel feature actually pulls its
   code), the stub lets the rug/MPFR surface build with the default features.
   Restore `Cargo.toml`/`Cargo.lock` afterwards — the stub is a build-only hack,
   never committed.

## Use from pyhecke

`pyhecke.bridge` automatically discovers and uses `pyhecke_native` when
it is importable, and falls back to subprocess dispatch (and then
pure-Python) otherwise. No caller-side changes are needed.

## Why a separate crate?

The pure-Python `pyhecke` package uses hatchling so `pip install -e .`
works with no Rust toolchain. The native acceleration lives in this
sibling crate, which requires maturin and Rust. Users who want speed
opt in; users who only want correctness get the pure-Python path by
default.
