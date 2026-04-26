#!/usr/bin/env python3
"""
F4.3: Coordinator script — run all knot-operation discovery feeders.

The HYBRID architecture (per F4 design) has multiple feeders that
each extract structural information from existing infrastructure:

  Feeder                                | Source of factorization
  ------                                | -----------------------
  wedderburn_discovery_feeder           | atom_per_generator_volumes
                                          channel signatures
  wedderburn_block_fingerprint_feeder   | per-Wedderburn-block χ_λ(β)
                                          fingerprints
  hyperbolic_knot_subword_feeder        | sub-word matches against
                                          hyperbolic knot DB (TODO)
  ...                                    ...

This script runs them all in sequence, populating
`knot-operation-cache.json` with their combined output.

Usage:
    python3 run_all_feeders.py
    python3 run_all_feeders.py --rebuild  # delete cache first

@module folio-assistant/computations/run_all_feeders
"""
from __future__ import annotations
import argparse
import importlib
import sys
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).parent))

from knot_operation_cache import KnotOperationCache  # type: ignore[import]


# Registry of available feeders.  Each entry is:
#   (feeder_name, module, function, isotopes_list)
# where `function(Z, N, cache, feeder_name=...)` populates the cache.
FEEDERS: list[tuple[str, str, str]] = [
    ("wedderburn_discovery_feeder",
     "wedderburn_discovery_feeder",
     "discover_for_isotope"),
    ("wedderburn_block_fingerprint_feeder",
     "wedderburn_block_fingerprint_feeder",
     "discover_for_isotope"),
    # Future feeders here:
    # ("hyperbolic_knot_subword_feeder", ...),
    # ("light_isotope_sweep_feeder", ...),
]

DEFAULT_ISOTOPES = [
    ("D", 1, 1),
    ("T", 1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
]


def _load_feeder(module_name: str, func_name: str) -> Callable:
    """Import a feeder function by name."""
    module = importlib.import_module(module_name)
    return getattr(module, func_name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--rebuild", action="store_true",
        help="Delete the cache before running feeders.",
    )
    parser.add_argument(
        "--cache-path", type=Path,
        default=Path(__file__).parent / "knot-operation-cache.json",
    )
    args = parser.parse_args()

    if args.rebuild and args.cache_path.exists():
        args.cache_path.unlink()
        print(f"Deleted: {args.cache_path}")

    cache = KnotOperationCache(args.cache_path)
    print(f"Loaded cache: {len(cache.operations)} operations, "
          f"{len(cache.factorizations)} factorizations\n")

    for feeder_name, module_name, func_name in FEEDERS:
        print(f"=== Feeder: {feeder_name} ===")
        try:
            fn = _load_feeder(module_name, func_name)
        except ImportError as e:
            print(f"  SKIP: import failed — {e}")
            continue

        for iso_name, Z, N in DEFAULT_ISOTOPES:
            try:
                summary = fn(Z, N, cache, feeder_name=feeder_name)
                cache_keys = summary.get("cache_keys", summary.get("factor_keys", []))
                key_count = len(cache_keys) if hasattr(cache_keys, "__len__") else 0
                print(f"  {iso_name} (Z={Z}, N={N}): {key_count} keys")
            except Exception as e:
                print(f"  {iso_name} (Z={Z}, N={N}): ERROR {type(e).__name__}: {e}")
        print()

    cache.save()
    print(f"Final cache: {len(cache.operations)} operations, "
          f"{len(cache.factorizations)} factorizations")
    print(f"Saved to: {args.cache_path}")

    # Summary by n.
    by_n: dict[int, int] = {}
    for op in cache.operations.values():
        by_n[op.n] = by_n.get(op.n, 0) + 1
    print(f"Ops by n: {dict(sorted(by_n.items()))}")

    # Multi-feeder ops (observed by 2+ feeders → strongest signal of
    # recurring structure).
    multi = [op for op in cache.operations.values()
             if len(op.discovered_in) > 1]
    print(f"Multi-feeder ops: {len(multi)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
