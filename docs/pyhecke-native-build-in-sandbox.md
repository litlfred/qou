# Building `pyhecke-native` in the web sandbox (Hecke-compute unblock)

**Date:** 2026-06-25 · **Status:** working recipe, validated.
**TL;DR:** run [`scripts/build-pyhecke-native.sh`](../scripts/build-pyhecke-native.sh) — it
builds + installs the native wheel in ~2.5 min and every Hecke-dependent producer then runs at
full mpf/MPFR precision.

## Why this was thought blocked (and isn't)

`pyhecke-native` is the Rust `hecke-engine` PyO3 acceleration layer for the `pyhecke` Python
package. It is **not on PyPI**, so it must be built from `tools/pyhecke-native` with `maturin`.
Earlier session audits (e.g. `2026-06-25-session-bean-triage.md`,
`2026-06-25-witness-staleness-cite-cosmetic-footprint.md`) recorded it as **sandbox-blocked**,
which made the whole Hecke-compute bean class (ct80 m_e regen, mass-table sweeps, λ_A
migrations, the dashboards) look like full-env-only work, and made any Hecke-dependent witness
refresh an `mpf → f64` regression risk (the ct80 / [#2747](https://github.com/litlfred/qou/pull/2747)
class).

The actual blocker was narrow: `pyhecke-native`'s Cargo graph pins a git fork
`github.com/litlfred/Clarabel.rs` (the Clarabel SDP solver). The sandbox has a global git
`insteadOf` that rewrites **every** `https://github.com/…` fetch to a local mirror serving only
`litlfred/qou`, so the fork 403s and `cargo metadata` dies. Two facts dissolve the block:

1. **The agent proxy allows `github.com` directly** (owner-authorised — the owner explicitly
   directed agents to clone from github when needed). Only the *mirror rewrite* was 403-ing.
2. **`origin` uses an explicit `127.0.0.1` mirror URL**, not the rewrite — so the rewrite can be
   safely disabled for the build and restored afterwards without touching push/fetch of this repo.

## The recipe (what the script does)

1. `pip install --user maturin` (if absent).
2. `export CARGO_NET_GIT_FETCH_WITH_CLI=true` — cargo then uses the git **CLI** (which honours
   `HTTPS_PROXY` + the proxy CA bundle) for the fork fetch, instead of its bundled libgit2 (which
   403s against the proxy).
3. Temporarily `git config --global --unset` the github→mirror `insteadOf` (detected by value, so
   it is port-agnostic), guarded by a `trap … EXIT` that **always restores** it.
4. `maturin build --release` in `tools/pyhecke-native`, then `pip install --user` the wheel.

## Validation (2026-06-25)

```
$ scripts/build-pyhecke-native.sh        # ~2m29s, wheel built + installed, import OK
$ cd computations && python3 -c "import sys; \
    sys.path[:0]=['.','../tools/pyhecke/python','../tools/qou-substrate/python']; \
    import canonical_mass as c; print(c.proton_mass_mev(), c.neutron_mass_mev())"
938.2720881603788 939.565421496897      # CODATA 938.272 / 939.565 ✓
```

The native API surface (`pyhecke_native.dir()`): `gram_matrix[_n]`, `gram_inverse[_n]`,
`gram_determinant`, `chi_lambda_*[_mpfr]`, `chi_q_atomic[_all_partitions]`, `hecke_h`,
`build_atom_nf`, `kl_betti_sum_rust`, `gauge_aligned_a_combiner_*_mpfr`, … (mpfr variants give
the full-precision path).

## Caveat — the wheel is ephemeral

It installs into the session's user site-packages (`~/.local/lib/python3.11/site-packages/`) and
is gone when the container is reclaimed. **Re-run the script in each fresh session** before any
Hecke-precision compute. The script is idempotent (cargo is incremental, so re-runs are fast).
