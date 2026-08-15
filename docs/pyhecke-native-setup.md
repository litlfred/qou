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

## IMPORTANT: installing the wheel does NOT (yet) accelerate `pyhecke.gram`

`pyhecke.gram` **deliberately refuses** the native wheel even when installed —
`_native_ok()` raises `RuntimeError` — because the Rust crate currently
**diverges** from the Python module (bean `qou-m7py`):

1. `trace_weights` in `tools/hecke-engine/src/gram.rs` ends `z³` where the
   Python `TR_M` ends `h·z² + z` (the 2026-05-19 trace fix was never ported);
   this makes the crate's Gram non-singular.
2. The crate hardcodes the **muon** pin `Q_0 = 1.1099785955541805`, while the
   Python reads the **proton** pin `1.1099785827513808` (2.19e-8 on z).

An environment-dependent silent divergence is worse than a loud refusal, so the
dispatch refuses; `QOU_ALLOW_NATIVE_DIVERGENCE=1` is the explicit override.
**So building the wheel is necessary infrastructure, but the native fast path
for gram-based compute is unlocked only when `qou-m7py` ports the trace fix +
proton pin into `tools/hecke-engine/src/gram.rs`.** Until then gram-based
computes run on the pure-Python path.

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
