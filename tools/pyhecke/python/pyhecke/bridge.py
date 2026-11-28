"""Subprocess dispatch to the Rust crates/hecke-engine/ binaries.

Keeps backward-compatible with the existing hecke_rust_bridge.py helper
in computations/.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional


def engine_dir(override: Optional[str | Path] = None) -> Path:
    """Return the crates/hecke-engine/ directory (falling back to legacy tools/hecke-engine/)."""
    if override:
        return Path(override)
    env = os.environ.get("HECKE_ENGINE_DIR")
    if env:
        return Path(env)

    d = Path(__file__).resolve()
    for anc in d.parents:
        for rel in (("crates", "hecke-engine"), ("tools", "hecke-engine")):
            cand = anc.joinpath(*rel)
            if cand.is_dir():
                return cand
    raise FileNotFoundError(
        "Could not locate crates/hecke-engine/. Set $HECKE_ENGINE_DIR."
    )


def binary_path(name: str) -> Optional[Path]:
    """Locate a compiled hecke-engine binary by name.

    Search order:
      1. $HECKE_ENGINE_DIR/target/release/<name> (when $HECKE_ENGINE_DIR is set)
      2. $CARGO_TARGET_DIR/release/<name>
      3. <repo-root>/target/release/<name> (Cargo workspace target)
      4. crates/hecke-engine/target/release/<name>
      5. $PATH lookup (shutil.which)
    """
    eng = engine_dir()
    candidates: list[Path] = []
    if os.environ.get("HECKE_ENGINE_DIR"):
        candidates.append(eng / "target" / "release" / name)
    cargo_target = os.environ.get("CARGO_TARGET_DIR")
    if cargo_target:
        candidates.append(Path(cargo_target) / "release" / name)
    repo_root = eng.parent.parent
    candidates.append(repo_root / "target" / "release" / name)
    candidates.append(eng / "target" / "release" / name)

    for release in candidates:
        if release.is_file() and os.access(release, os.X_OK):
            return release
    which = shutil.which(name)
    if which:
        return Path(which)
    return None


def run(
    name: str, args: list[str],
    timeout: Optional[float] = None,
    capture_stderr: bool = False,
) -> subprocess.CompletedProcess:
    """Invoke a hecke-engine binary. Raises FileNotFoundError if missing."""
    bin_path = binary_path(name)
    if bin_path is None:
        raise FileNotFoundError(
            f"hecke-engine binary {name!r} not found. "
            f"Build with `cargo build --release -p hecke-engine --bin {name}`."
        )
    cmd = [str(bin_path), *args]
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )


def run_json(name: str, args: list[str], **kwargs) -> dict:
    """Invoke a binary whose stdout is JSON; return parsed dict.

    Raises RuntimeError if the process exits non-zero or stdout is not JSON.
    """
    proc = run(name, args, **kwargs)
    if proc.returncode != 0:
        raise RuntimeError(
            f"{name} exited {proc.returncode}: {proc.stderr[:500]}"
        )
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(
            f"{name} stdout was not valid JSON: {e}\n"
            f"first 500 chars: {proc.stdout[:500]}"
        ) from e


# ─── Gram matrix via Rust engine ────────────────────────────────────

def _import_native():
    """Try to import the PyO3 acceleration module. Returns None if not
    built."""
    try:
        import pyhecke_native  # type: ignore[import-not-found]
        return pyhecke_native
    except ImportError:
        return None


_NATIVE = _import_native()


def has_native() -> bool:
    """True if the PyO3 acceleration layer is importable."""
    return _NATIVE is not None


def gram_from_rust(q: Optional[float] = None) -> dict:
    """Return the Gram matrix, computed by the Rust `hecke-gram` binary.

    Falls back to raising FileNotFoundError if the binary isn't built;
    callers should catch this and use the pure-Python `pyhecke.gram.G`.

    Parameters
    ----------
    q : float, optional
        Substrate parameter. Defaults to the Rust-side Q_0.

    Returns
    -------
    dict
        Parsed output of `hecke-gram --pretty` matching gram.schema.json.
    """
    args = ["--pretty"]
    if q is not None:
        args.extend(["--q", f"{q:.17g}"])
    return run_json("hecke-gram", args)


def _native_convergent() -> bool:
    """True iff `pyhecke_native` is importable AND passes `pyhecke.gram._native_ok()`.

    Prevents `bridge` from calling a pre-2026-08-15 convention-C `.so` wheel
    after `pyhecke.gram` has already quarantined it (`_NATIVE_VERIFIED = False`).
    """
    if _NATIVE is None:
        return False
    from . import gram as _pg
    return _pg._native_ok()


def _default_q0() -> float:
    """Canonical proton-pinned substrate `q_0` from `pyhecke.gram`."""
    from . import gram as _pg
    return float(_pg.q0)


def gram_matrix_from_rust(q: Optional[float] = None):
    """Return just the 6×6 Gram matrix as a numpy array (Rust-computed).

    Dispatches in this order:
      1. `pyhecke_native` (PyO3 in-process, gated on `gram._native_ok()`) — ~20ns/call.
      2. `hecke-gram` subprocess — ~20ms/call (fork+exec).
      3. FileNotFoundError if neither is available.
    """
    try:
        import numpy as np
    except ImportError as e:  # pragma: no cover
        raise ImportError("pyhecke.bridge.gram_matrix_from_rust requires numpy") from e

    if _native_convergent():
        q_val = q if q is not None else _default_q0()
        return np.array(_NATIVE.gram_matrix(q_val))

    cert = gram_from_rust(q=q)
    return np.array(cert["matrix"])


def gram_det_from_rust(q: Optional[float] = None) -> float:
    """Return det(G) at `q`. Fast path via verified PyO3, fallback via subprocess."""
    if _native_convergent():
        q_val = q if q is not None else _default_q0()
        return float(_NATIVE.gram_determinant(q_val))
    return float(gram_from_rust(q=q)["determinant"])
