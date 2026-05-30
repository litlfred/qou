# Wiring audit — Clarabel LP/SDP port (is it actually in the infra?)

**Date:** 2026-05-29
**Trigger:** Owner — "first make sure wired up completely in infra … do an audit."
**Scope:** the LP/SDP → Clarabel work on PR #1440 (branch
`claude/charming-keller-6flo8`).
**Method:** static grep of callers, `.github/workflows/`, `deploy/`,
`scripts/`, the pyhecke-native wheel build, and `pyhecke-native/src/lib.rs`.

## Verdict

**NOT wired into the infrastructure.** The port is *correct and
self-tested at the Rust level* (5 KKT/duality lib tests pass under
`--features clarabel-mpfr`; the CLI runs on the dummy LP), but it is a
**dormant, dev-only opt-in**: nothing in production calls it, no CI
builds or tests it, and a deployed Python calling `backend="clarabel"`
would `FileNotFoundError` (the binary it shells out to is built by no
workflow). This mirrors the *pre-existing* clarabel surface, which is
also dev-only — so this is a repo-wide gap the port inherited, not a
regression it introduced.

## Evidence — every wiring layer

| Layer | Status | Evidence |
|-------|:------:|----------|
| Production caller passes `backend="clarabel"` | ❌ none | grep empty; all 9 LP callers default to scipy/cvxpy |
| CLI `clarabel-operator-selection-lp` built by CI/deploy/scripts | ❌ no | grep empty across `.github/`, `deploy/`, `scripts/` |
| Rust LP correctness tests run in CI | ❌ no | the only hecke `cargo test --lib` (`hecke-engine-wasm.yml:99`, in the **wasm** crate) uses **default features**; my tests are gated on `clarabel-mpfr` → never compiled/run in CI |
| Any `clarabel-*` feature built/checked in CI | ❌ no | CI builds only `--features mpfr` (rug) + default; the single `clarabel` mention is a *gate-out comment* |
| Shipped `pyhecke_native` wheel carries an LP binding | ❌ no | 0 `clarabel`/LP symbols in `pyhecke-native/src/lib.rs`; wheel builds default features |
| Cross-check `clarabel_lp_crosscheck.py` runs in CI | ❌ no | grep empty |
| Runtime binary discoverability (deployed env) | ⚠️ broken | Python autodetects `tools/hecke-engine/target/release/clarabel-operator-selection-lp` — present only if *manually* built; no deploy/CI step produces it |
| Witness / LP-dual gate exercises the new path | ❌ no | the clarabel path emits no `*.witness.json` |

**Baseline:** pre-existing clarabel bins (`clarabel-certify`, …) are
**also** referenced by 0 workflows. The whole `clarabel-*` feature set
is manual/dev-only across the repo.

## Why (partly by design)

The port was deliberately shipped **opt-in / non-regressing** because
this container has no scipy/numpy/mpmath to run the mandatory q₀
cross-check. Keeping the default on scipy/cvxpy was the safe choice.
But "available behind a flag" ≠ "wired into infra," which is what the
audit was asked to verify — and it is not.

## What "completely wired" requires (dependency order)

1. **CI feature-test gate (cheapest, highest value).** Add a job step:
   ```bash
   cargo test  --release --manifest-path tools/hecke-engine/Cargo.toml \
       --features clarabel-mpfr --lib operator_selection_lp
   cargo build --release --manifest-path tools/hecke-engine/Cargo.toml \
       --features clarabel-mpfr --bin clarabel-operator-selection-lp
   ```
   Without this, the 5 proofs-as-tests are invisible to CI. **This is
   the single most important gap** and is mechanical/low-risk.

2. **Runtime availability — pick the home (architectural decision):**
   - **(a) PyO3 binding in `pyhecke_native`** — exposes
     `solve_operator_selection_lp` as a wheel function, riding the
     existing `pyhecke-native-wheels.yml` build/ship pipeline. Cleanest
     "wired into shipped infra," but pulls clarabel + rug/MPFR into the
     wheel (heavier build; the wheel job must enable the feature).
   - **(b) Build the CLI as a CI/deploy artifact** — lighter, keeps the
     subprocess design, but ships a separate binary the Python must find.

3. **Cross-check in CI** — run `clarabel_lp_crosscheck.py` in a
   scipy+numpy job; gate the default flip on it being green.

4. **Flip the default (or add a production caller)** — only after (3)
   passes. Until then the path stays opt-in.

## Recommendation

Land **(1)** now (mechanical, verifiable, makes the existing tests
count in CI). Decide **(2a) vs (2b)** with the owner — it's a real
wheel-weight-vs-extra-binary tradeoff. **(3)+(4)** need a scipy env and
the owner's go-ahead to change production behavior.
