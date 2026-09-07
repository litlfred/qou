#!/usr/bin/env bash
# Build + install the `pyhecke-native` PyO3 wheel — the Rust `hecke-engine`
# acceleration layer for the `pyhecke` Python package. Once installed, every
# Hecke-dependent producer runs at full mpf / MPFR precision: NO silent
# mpf -> f64 fallback (the ct80 / #2747 regression class).
#
# WHY THIS SCRIPT EXISTS
# ----------------------
# `pyhecke-native` is NOT on PyPI; it must be built from `tools/pyhecke-native`
# with maturin. Its Cargo graph pins a git fork `github.com/litlfred/Clarabel.rs`
# (the Clarabel SDP solver). In the Claude-Code-on-the-web sandbox a global git
# `insteadOf` rewrites every `https://github.com/...` fetch to a local mirror
# that only serves `litlfred/qou`, so the fork 403s and the build dies at
# `cargo metadata` ("revision ... not found / 403"). The agent proxy DOES allow
# github.com directly (owner-authorised: the owner explicitly directed agents to
# clone from github when needed), so this script temporarily disables that one
# rewrite for the duration of the build and restores it on exit via a trap.
# `origin` uses an explicit `127.0.0.1` mirror URL and is therefore unaffected.
#
# VALIDATED 2026-06-25: build ~2.5 min on the web sandbox;
# `canonical_mass.proton_mass_mev()` -> 938.2720882 (CODATA 938.272),
# `neutron_mass_mev()` -> 939.5654215 (CODATA 939.565) after install.
#
# NOTE: the wheel installs into the session's user site-packages and is
# EPHEMERAL — it dies when the container is reclaimed. Re-run this script in a
# fresh session before any Hecke-precision compute.
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"

command -v maturin >/dev/null 2>&1 || pip install --user maturin
export PATH="$HOME/.local/bin:$PATH"
# Use the git CLI (honours HTTPS_PROXY + the proxy CA bundle) for the fork fetch,
# instead of cargo's bundled libgit2 (which 403s against the proxy).
export CARGO_NET_GIT_FETCH_WITH_CLI=true

# Detect the github->mirror `insteadOf` rewrite by VALUE (the key name embeds a
# per-session mirror port, so match on the rewritten target rather than the key).
KEY="$(git config --global --get-regexp 'url\..*\.insteadof' 2>/dev/null \
        | awk '$2=="https://github.com/"{print $1; exit}' || true)"
OLD=""
restore() { [ -n "${KEY:-}" ] && [ -n "${OLD:-}" ] && git config --global "$KEY" "$OLD" || true; }
trap restore EXIT
if [ -n "${KEY:-}" ]; then
  OLD="https://github.com/"
  git config --global --unset "$KEY" 2>/dev/null || true
  echo "[pyhecke-native] temporarily disabled github->mirror rewrite: $KEY"
fi

echo "[pyhecke-native] maturin build --release (fetches Clarabel.rs fork direct from github)"
( cd "$ROOT/tools/pyhecke-native" && maturin build --release )

WHL="$(find "$ROOT/tools/pyhecke-native/target/wheels" -name 'pyhecke_native*.whl' 2>/dev/null | head -1)"
[ -n "$WHL" ] || { echo "[pyhecke-native] ERROR: no wheel produced" >&2; exit 1; }
pip install --user --force-reinstall "$WHL"
python3 -c "import pyhecke_native; print('[pyhecke-native] import OK:', pyhecke_native.__file__)"

# ── LP-kernel presence gate ──────────────────────────────────────────────────
# A DIFFERENT failure from the convention gate below, and it must be checked
# separately: that one asks whether the binary computes the right convention,
# this one asks whether the Hecke path uses the binary at all.
#
# `hecke_core_legacy.py:1367` decides with
#     _HAS_LP_KERNEL = hasattr(_PHN, "lp_accumulator_step_traces_mpfr")
# and on False falls back to `_build_ysn_matrices`, which VIOLATES the braid
# relation (audits/ysn_braid_relation_audit.py) -- not a representation of
# H_n(q), so the products are not Markov traces of braids.
#
# Hit on 2026-09-07 in a rebuilt container. It is dangerous because the
# fallback is silent IN THE NUMBERS: proton, neutron and protium came out
# byte-identical to a known-good run (0.629328 / 0.475134 / 1.146338) and it
# only diverges on compounds -- 17.3% at deuterium. A wheel missing this symbol
# imports fine and passes the convention gate, because markov_z is a separate
# export. Only asking for the symbol catches it.
echo "[pyhecke-native] LP-kernel gate: lp_accumulator_step_traces_mpfr must be exported"
python3 - <<'PYLP' || { echo "[pyhecke-native] ERROR: LP kernel MISSING — Hecke producers would silently use the braid-violating ysn fallback. Do NOT run them with this build." >&2; exit 1; }
import sys
import pyhecke_native as pn
if not hasattr(pn, "lp_accumulator_step_traces_mpfr"):
    print("  lp_accumulator_step_traces_mpfr: MISSING")
    sys.exit(1)
print("  lp_accumulator_step_traces_mpfr: present")
PYLP

# ── Trace-convention gate ────────────────────────────────────────────────────
# An import check cannot tell a fresh wheel from a stale one. On 2026-08-09 the
# INSTALLED .so returned convention C (markov_z(q0) = 0.4993203341836945) while
# its own source, tools/hecke-engine/src/gram.rs, read convention D — the wheel
# predated b5f4cb5b9 ("the Rust engine stack C -> D, all nine bindings") by a
# day. Source review could not see it, the content-layer axis passed, and the
# registry was correct; only calling the binary exposes it.
#
# That matters most at exactly this moment. The standing rule in this repo is
# "never hand-edit witness numbers, regenerate from the producer" — so a stale
# artifact here turns the remediation into the reintroduction vector, stamping
# fresh convention-C numbers into witnesses with a producer's authority.
#
# markov_z is re-exported through all nine language bindings and drives
# trace_weights and the v_std quark-volume channel, so this one value gates the
# whole native path. Compared against the registry rather than a literal, so a
# convention change re-arms the gate automatically.
echo "[pyhecke-native] trace-convention gate: markov_z(q0) must match the registry"
python3 - "$ROOT" <<'PYGATE' || { echo "[pyhecke-native] ERROR: convention gate FAILED — do NOT run producers with this build" >&2; exit 1; }
import json, sys, pathlib
root = pathlib.Path(sys.argv[1])
reg = json.loads((root / "docs/coordination/trace-convention-registry.json").read_text())
q0 = float(reg["meta"]["q0"]["value"])
want = float(next(c for c in reg["conventions"] if c["id"] == "D")["z_at_q0"])
import pyhecke_native as pn
got = pn.markov_z(q0)
d = abs(got - want)
print(f"  markov_z(q0) = {got!r}")
print(f"  registry D   = {want!r}")
print(f"  |difference| = {d:.3e}   (tolerance 1e-15, f64 path)")
if d > 1e-15:
    zc = 1.0 / (q0 ** 0.5 + q0 ** -0.5)
    if abs(got - zc) <= 1e-15:
        print("  -> this build is CONVENTION C. It is stale: rebuild from the current tree.")
    else:
        print("  -> matches neither convention D nor convention C.")
    sys.exit(1)
print("  -> convention D confirmed.")
PYGATE

echo "[pyhecke-native] done — Hecke-dependent producers now run at full precision."
echo "[pyhecke-native] smoke test: cd computations && python3 -c \"import sys; sys.path[:0]=['.','../tools/pyhecke/python','../tools/qou-substrate/python']; import canonical_mass as c; print(c.proton_mass_mev())\""
