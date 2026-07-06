"""
Python → Rust hecke-engine bridge.

Calls the compiled Rust binary for ground-state search and Hecke algebra
computation, parsing JSON output. Falls back to Python hecke_engine.py
if the binary is not available.

The Rust engine is ~100x faster for large nuclei (A > 14) due to:
- rayon parallel ground-state search
- BigInt/CRT exact arithmetic without Fraction overhead
- i128 Laurent polynomial arithmetic
- Gebauer-Möller filtered Gröbner-Shirshov reduction

Usage:
    from hecke_rust_bridge import compute_nucleus, is_rust_available

    if is_rust_available():
        result = compute_nucleus(6, 8)  # ¹⁴C
    else:
        # falls back to Python
        result = compute_nucleus(6, 8)

@module computations/hecke_rust_bridge
"""


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional

# ── Locate the Rust binary ───────────────────────────────────────

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_HECKE_DIR = _REPO_ROOT / "tools" / "hecke-engine"
_HECKE_BIN = _HECKE_DIR / "target" / "release" / "hecke-engine"
_HECKE_QVALUES = _HECKE_DIR / "target" / "release" / "hecke-qvalues"

_HECKE_BIN_PATH = None
for candidate in [_HECKE_BIN, _HECKE_QVALUES]:
    if candidate.exists():
        _HECKE_BIN_PATH = candidate
        break


def is_rust_available() -> bool:
    """Check if the compiled Rust hecke-engine binary exists."""
    return _HECKE_BIN_PATH is not None


def _find_binary(name: str = "hecke-engine") -> Optional[Path]:
    """Find a specific Rust binary."""
    candidate = _HECKE_DIR / "target" / "release" / name
    if candidate.exists():
        return candidate
    return None


def _run_binary(
    binary_name: str,
    args: list[str],
    timeout: int = 120,
) -> Optional[str]:
    """Run a Rust binary and return stdout."""
    binary = _find_binary(binary_name)
    if binary is None:
        return None

    try:
        result = subprocess.run(
            [str(binary)] + args,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(_HECKE_DIR),
        )
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"hecke-engine error: {result.stderr[:200]}", file=sys.stderr)
            return None
    except subprocess.TimeoutExpired:
        print(f"hecke-engine timeout after {timeout}s", file=sys.stderr)
        return None
    except FileNotFoundError:
        return None


# ── High-level API ───────────────────────────────────────────────

def compute_nucleus(
    p: int,
    n: int,
    Q_exp: Optional[float] = None,
    timeout: int = 120,
) -> Optional[dict]:
    """Compute Hecke algebra data for nucleus N(p,n).

    Tries Rust binary first; falls back to Python HeckeEngine.

    Returns dict with keys:
        nucleus, p, n, A, ordering_par, ordering_dau, conv_pos,
        trace_par_float, trace_dau_float, eIeR_float, elapsed_s
    """
    # Try Rust first
    output = _run_binary("hecke-qvalues", [str(p), str(n)], timeout=timeout)
    if output:
        # Parse JSON from stdout (hecke-qvalues outputs one JSON per line)
        for line in output.strip().split("\n"):
            line = line.strip()
            if line.startswith("{"):
                try:
                    return json.loads(line)
                except json.JSONDecodeError:
                    continue

    # Fall back to Python
    try:
        from hecke_engine import HeckeEngine
        engine = HeckeEngine()
        ordering, method = engine.ground_state_ordering(p, n)
        tr = float(engine.qr.markov_trace(ordering))
        return {"p": p, "n": n, "ordering": ordering,
                "trace_par_float": tr, "ordering_method": method}
    except (ImportError, AttributeError):
        return None


def compute_table(
    nuclei: list[tuple[int, int]],
    timeout: int = 300,
) -> list[Optional[dict]]:
    """Compute Hecke data for a list of (p, n) pairs.

    Loops over nuclei and calls compute_nucleus for each.
    """
    results = []
    for p, n in nuclei:
        results.append(compute_nucleus(p, n, timeout=timeout))
    return results


def ground_state_ordering(
    p: int,
    n: int,
    timeout: int = 60,
) -> Optional[list[int]]:
    """Get the ground-state nucleon ordering for N(p,n).

    Returns list of 0/1 (0=neutron, 1=proton) or None on failure.
    """
    result = compute_nucleus(p, n, timeout=timeout)
    if result and "ordering_par" in result:
        return result["ordering_par"]
    return None


def build_rust_engine(verbose: bool = False) -> bool:
    """Attempt to build the Rust hecke-engine (requires cargo)."""
    global _HECKE_BIN_PATH

    if not (_HECKE_DIR / "Cargo.toml").exists():
        print("No Cargo.toml found in tools/hecke-engine/", file=sys.stderr)
        return False

    try:
        cmd = ["cargo", "build", "--release"]
        result = subprocess.run(
            cmd,
            cwd=str(_HECKE_DIR),
            capture_output=not verbose,
            timeout=600,
        )
        if result.returncode == 0:
            _HECKE_BIN_PATH = _HECKE_BIN if _HECKE_BIN.exists() else _HECKE_QVALUES
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return False


# ── CLI ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"Rust hecke-engine bridge")
    print(f"  Binary dir: {_HECKE_DIR}")
    print(f"  Available:  {is_rust_available()}")
    if _HECKE_BIN_PATH:
        print(f"  Binary:     {_HECKE_BIN_PATH}")

    if len(sys.argv) >= 3:
        p, n = int(sys.argv[1]), int(sys.argv[2])
        print(f"\nComputing N({p},{n})...")
        result = compute_nucleus(p, n)
        if result:
            print(json.dumps(result, indent=2, default=str))
        else:
            print("Failed (no Rust binary and Python fallback unavailable)")
    else:
        # Quick test with tritium
        print("\nQuick test: ³H (p=1, n=2)")
        result = compute_nucleus(1, 2)
        if result:
            for k, v in result.items():
                if not isinstance(v, list):
                    print(f"  {k}: {v}")
        else:
            print("  (no engine available)")
