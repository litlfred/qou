# `pyhecke-native` — build, verify, and the precision-fallback policy

Quick reference for agents. `pyhecke-native` is the Rust `hecke-engine`
acceleration layer for the `pyhecke` Python package (Gram / Markov-trace / χ
primitives, ~100× on the larger atoms). It is **not on PyPI** and the wheel is
**ephemeral** — it lives in the session's user site-packages and dies when the
container is reclaimed, so a fresh container starts without it.

## It is now built by default

As of this change, `SessionStart` runs
[`scripts/build-pyhecke-native.sh`](../scripts/build-pyhecke-native.sh) in the
background (`.claude/settings.json`, alongside `lean-build-bg.sh`). Log:
`${TMPDIR:-/tmp}/qou-pyhecke-native-build.log`. Budget ~2.5 min. If a session
needs it immediately (before the background build finishes), run the script by
hand and wait.

## Build / verify by hand

```bash
./scripts/build-pyhecke-native.sh        # maturin build --release + install + convention gate
python3 -c "import pyhecke_native; print(pyhecke_native.__version__)"   # 0.9.0
```

The script handles the two things that trip a naive `maturin build`:
- **The Clarabel.rs git fork.** The Cargo graph pins
  `github.com/litlfred/Clarabel.rs`; the sandbox's global git `insteadOf`
  rewrite (which points every `github.com` fetch at the local `litlfred/qou`
  mirror) makes that fork 403. The script disables that one rewrite for the
  build and restores it on exit, and sets `CARGO_NET_GIT_FETCH_WITH_CLI=true`
  so the fetch honours the proxy.
- **The convention gate.** After install it calls `pyhecke_native.markov_z(q0)`
  and checks it against convention **D** in
  `docs/coordination/trace-convention-registry.json`. An import check cannot
  tell a fresh wheel from a stale convention-C one; only calling the binary can.

Rust toolchain (`cargo`, `rustc`) is present in these environments; `maturin`
is pip-installed by the script if absent. `rug`/MPFR builds from source (no
system GMP/MPFR packages needed).

## Native `pyhecke.gram` acceleration — ENABLED (qou-m7py RESOLVED 2026-08-15)

The native fast path is now on by default when the wheel is installed. The
qou-m7py port brought the crate and every language binding onto **convention
D**: `gram_matrix`/`nf_tr` and every binding's `trace_weights` export use
`gram::trace_weights_markov` (`TR_M[5] = h·z² + z`), `Q_0` is the proton pin
`1.1099785827513808`, and the (singular-under-D) Gram is handled by
`gram_quotient_inverse` + `gram_radical` rather than a removed `gram_inverse`.

`_native_ok()` no longer refuses on principle. It runs a **runtime
convergence self-check**: it compares the installed wheel's
`trace_weights`/`gram_matrix` against this module's convention-D reference
(`TR_M`, `G`) at `q0`, and

- **matches** → the native path is used (~100× on ⁴⁰Ca);
- **diverges** (an OLD wheel built before the port — still `z³` / muon pin) →
  refused **loudly** with a `RuntimeWarning` + rebuild hint. No silent
  divergence either way.

`QOU_DISABLE_NATIVE=1` is the explicit opt-out (forces the pure-Python path).
The old `QOU_ALLOW_NATIVE_DIVERGENCE=1` opt-in is obsolete. If the self-check
fails, `bash scripts/build-pyhecke-native.sh` rebuilds a convergent wheel.

Verified native == Python-D exactly at q0: `trace_weights` Δ=0, `gram_matrix`
Δ=0, `gram_quotient_inverse` vs `G_PINV` Δ=4.4e-16, `gram_radical` Δ=0,
`gram_determinant`=0 (singular, as expected under D).

## Producer-level fast paths are separate

Some producers (e.g. `rho_k_co_casimir_extended.py`) do **not** go through
`pyhecke.gram` at all — they select χ locally: `chi_numpy` (numpy f64) with a
silent `except ImportError` fallback to `chi_numeric` (mpmath). That silent
degradation to the slow path is the "ct80 / #2747 regression class" the build
script warns about, and is tracked separately from the wheel. When you touch
such a producer, prefer a **loud** failure (raise unless an explicit
`QOU_ALLOW_*` opt-in is set) over a silent fallback, matching `gram.py`'s
`_native_ok()` philosophy.

## Related tooling

- `scripts/build-pyhecke-native.sh` — build + install + convention gate (above).
- `scripts/convention-c-producer-audit.py` — AST scan for convention-C Markov
  definitions in live producers (reports 0 actionable; producers are all D).
- `scripts/regenerate-convention-c-witnesses.py` — `--plan` / `--run` /
  `--report`: re-run every producer whose committed witness still carries a
  convention-C fingerprint (serial, resumable). This is the canonical way to
  refresh a stale witness such as `rho-k-co-casimir-extended` — not a hand-edit.
