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

echo "[pyhecke-native] done — Hecke-dependent producers now run at full precision."
echo "[pyhecke-native] smoke test: cd computations && python3 -c \"import sys; sys.path[:0]=['.','../tools/pyhecke/python','../tools/qou-substrate/python']; import canonical_mass as c; print(c.proton_mass_mev())\""
