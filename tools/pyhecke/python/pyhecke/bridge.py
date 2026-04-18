"""Subprocess dispatch to the Rust tools/hecke-engine/ binaries.

Keeps backward-compatible with the existing hecke_rust_bridge.py helper
in folio-assistant/computations/.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional


def engine_dir(override: Optional[str | Path] = None) -> Path:
    """Return the tools/hecke-engine/ directory."""
    if override:
        return Path(override)
    env = os.environ.get("HECKE_ENGINE_DIR")
    if env:
        return Path(env)

    d = Path(__file__).resolve()
    # walk up until a folder containing "tools/hecke-engine" is found
    for anc in d.parents:
        cand = anc / "tools" / "hecke-engine"
        if cand.is_dir():
            return cand
    raise FileNotFoundError(
        "Could not locate tools/hecke-engine/. Set $HECKE_ENGINE_DIR."
    )


def binary_path(name: str) -> Optional[Path]:
    """Locate a compiled hecke-engine binary by name.

    Search order:
      1. $HECKE_ENGINE_DIR/target/release/<name>
      2. tools/hecke-engine/target/release/<name>
      3. $PATH lookup (shutil.which)
    """
    release = engine_dir() / "target" / "release" / name
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
            f"Build with `cd tools/hecke-engine && cargo build --release`."
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


def gram_matrix_from_rust(q: Optional[float] = None):
    """Return just the 6×6 Gram matrix as a numpy array (Rust-computed).

    Raises FileNotFoundError if `hecke-gram` is not available; callers
    should fall back to `pyhecke.gram.G` or `gram_matrix()`.
    """
    try:
        import numpy as np
    except ImportError as e:  # pragma: no cover
        raise ImportError("pyhecke.bridge.gram_matrix_from_rust requires numpy") from e
    cert = gram_from_rust(q=q)
    return np.array(cert["matrix"])
