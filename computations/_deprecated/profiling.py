#!/usr/bin/env python3
"""
Compute-infra profiling registry.

Tracks per-routine wallclock + per-precision breakdown across ALL
character/mass/binding computations.  Used to identify where to focus
optimization (per user direction: "hybrid keep track of profiling
benchmarks to figure out where to focus").

Usage:

    from profiling import profile, dump_profiles

    with profile("plancherel_term_7", precision="mpfr_50dps", n=12):
        result = compute_term_7(Z, N)

    dump_profiles("/path/to/profile.json")  # writes accumulated stats

The registry accumulates calls into a global dict, keyed by
(routine, precision, n).  Each entry tracks:
  - call_count
  - total_wallclock_seconds
  - mean_wallclock_seconds
  - last_run_iso

The profile JSON survives across runs (read on init, written on exit)
so optimization decisions can be made from accumulated data, not
single runs.

@module folio-assistant/computations/profiling
"""
from __future__ import annotations
import contextlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

PROFILE_PATH = Path(__file__).parent / "compute-profiling.json"

# Global accumulator: keyed by (routine, precision_tag, optional n / extras).
_PROFILES: dict[str, dict] = {}


def _key(routine: str, precision: str, **extras) -> str:
    """Canonical key for a profile entry."""
    parts = [routine, precision]
    for k in sorted(extras):
        parts.append(f"{k}={extras[k]}")
    return "|".join(parts)


def load_existing(path: Path = PROFILE_PATH) -> None:
    """Load any existing profile JSON into the global accumulator."""
    if path.exists():
        try:
            data = json.loads(path.read_text())
            for k, v in data.items():
                _PROFILES[k] = v
        except (json.JSONDecodeError, OSError):
            pass


@contextlib.contextmanager
def profile(routine: str, precision: str = "f64_numeric_fallback", **extras):
    """Context manager that times its block and accumulates the result.

    Args:
        routine: human-readable routine name (e.g., 'plancherel_term_7').
        precision: precision tag (e.g., 'f64_numeric_fallback',
                   'mpfr_50dps', 'symbolic_q').
        **extras: any extra dimensions to bucket by (e.g., n=12, A=4,
                  isotope='4He').
    """
    t0 = time.time()
    yield
    elapsed = time.time() - t0
    k = _key(routine, precision, **extras)
    entry = _PROFILES.get(k, {
        "routine": routine,
        "precision": precision,
        **extras,
        "call_count": 0,
        "total_wallclock_seconds": 0.0,
        "mean_wallclock_seconds": 0.0,
    })
    entry["call_count"] = entry.get("call_count", 0) + 1
    entry["total_wallclock_seconds"] = (
        entry.get("total_wallclock_seconds", 0.0) + elapsed
    )
    entry["mean_wallclock_seconds"] = (
        entry["total_wallclock_seconds"] / entry["call_count"]
    )
    entry["last_run_iso"] = datetime.now(timezone.utc).isoformat()
    _PROFILES[k] = entry


def dump_profiles(path: Optional[Path] = None) -> Path:
    """Write the accumulated profile data to JSON.  Returns the path."""
    target = Path(path) if path else PROFILE_PATH
    # Sort by total wallclock descending (slowest first → focus targets).
    sorted_data = dict(sorted(
        _PROFILES.items(),
        key=lambda kv: -kv[1].get("total_wallclock_seconds", 0.0),
    ))
    target.write_text(json.dumps(sorted_data, indent=2, default=str))
    return target


def report(top_n: int = 10) -> str:
    """Human-readable summary of the top-N hot routines."""
    sorted_entries = sorted(
        _PROFILES.values(),
        key=lambda e: -e.get("total_wallclock_seconds", 0.0),
    )[:top_n]
    if not sorted_entries:
        return "(no profile data)"
    lines = [
        f"{'routine':<40} {'precision':<22} {'count':>5} "
        f"{'total (s)':>12} {'mean (s)':>10}"
    ]
    lines.append("─" * 92)
    for e in sorted_entries:
        lines.append(
            f"{e['routine']:<40} {e['precision']:<22} "
            f"{e.get('call_count', 0):>5} "
            f"{e.get('total_wallclock_seconds', 0.0):>12.3f} "
            f"{e.get('mean_wallclock_seconds', 0.0):>10.4f}"
        )
    return "\n".join(lines)


# Auto-load on import; auto-dump on Python exit so accumulated stats
# survive across runs.
load_existing()

import atexit
atexit.register(dump_profiles)


if __name__ == "__main__":
    # Allow `python3 profiling.py` to print the current report.
    print(report(top_n=20))
