#!/usr/bin/env python3
"""
F4.2: Wedderburn-block discovery from atom_per_generator_volumes.

The simplest concrete discovery primitive: for a given isotope, run
`hecke_core.atom_per_generator_volumes(Z, N)` to get the per-generator
Wedderburn channel volumes `(sym, std, alt, full)`, then identify
recurring channel-signatures across generators.  Each unique signature
becomes a `KnotOperation` cached for reuse.

This populates `knot-operation-cache.json` from the existing
infrastructure without requiring new SDP solvers.

Usage:
    python3 wedderburn_discovery_feeder.py --isotope D
    python3 wedderburn_discovery_feeder.py --all  # D, T, 3He, 4He

Per user directive (HYBRID): existing 33 scripts continue to work
unchanged; this script is a thin feeder that extracts factorizations
from `atom_per_generator_volumes` and emits cache entries.

@module computations/wedderburn_discovery_feeder
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from hecke_core import atom_per_generator_volumes  # type: ignore[import]
from knot_operation_cache import KnotOperation, KnotOperationCache


# Tolerance for considering two channel volumes "the same" — discovery
# uses hash-of-rounded-volumes as a fingerprint.
DEFAULT_VOL_PRECISION = 6


def channel_signature(vols: dict, precision: int = DEFAULT_VOL_PRECISION) -> str:
    """Stable string fingerprint of a per-generator channel-volume dict.

    Two generators with the same (sym, std, alt, full) up to `precision`
    decimal digits are considered the same operation.
    """
    keys = sorted(vols.keys())
    parts = [f"{k}={round(float(vols[k]), precision)}" for k in keys]
    return "|".join(parts)


def discover_for_isotope(
    Z: int,
    N: int,
    cache: KnotOperationCache,
    feeder_name: str = "wedderburn_discovery_feeder",
) -> dict:
    """Discover recurring per-generator operations in the atomic braid
    of (Z, N).  Returns a summary dict.
    """
    vols = atom_per_generator_volumes(Z, N, include_inter=True)
    n_gens = len(vols)
    A = Z + N
    n_strands = 3 * A

    # Group generators by channel-signature.
    groups: dict[str, list[int]] = {}
    for i, v in enumerate(vols):
        sig = channel_signature(v)
        groups.setdefault(sig, []).append(i)

    # Each group becomes a candidate KnotOperation.
    # Per Copilot review #r3144... (round 3): the cache-key fingerprint
    # must NOT include isotope-specific data (gen_indices), otherwise
    # the same channel-signature observed in two different isotopes
    # produces different keys and dedup fails.  Keep only feeder name +
    # channel signature in the cache-key fingerprint; expose
    # gen_indices and group size as non-key metadata in
    # plancherel_signature.
    new_ops = []
    for sig, gen_indices in sorted(groups.items()):
        fingerprint = {
            "feeder": feeder_name,
            "channel_signature": sig,
        }
        plancherel_sig = {
            "channel_signature": _signature_hash_to_float(sig),
            "n_generators_grouped": float(len(gen_indices)),
            # Track per-isotope occurrence as float metadata (uses the
            # bit-pattern of a stable hash so isotopes with different
            # gen-index sets are still distinguishable in metadata
            # while NOT contributing to the cache key).
            "gen_indices_hash": _signature_hash_to_float(
                ",".join(str(i) for i in sorted(gen_indices))
            ),
        }
        op = KnotOperation(
            n=n_strands,
            braid_word_normal_form=[],
            plancherel_signature=plancherel_sig,
            fingerprint=fingerprint,
        )
        cache_key = cache.add_operation(op, discovered_in=feeder_name)
        new_ops.append(cache_key)

    # Record the factorization: this isotope's atomic braid factors
    # into the discovered operations.
    parent_braid_id = f"atom_Z{Z}_N{N}_3A{n_strands}"
    cache.add_factorization(
        parent_n=n_strands,
        parent_braid_id=parent_braid_id,
        factor_keys=new_ops,
        discovered_by=feeder_name,
    )

    return {
        "isotope": f"Z={Z},N={N}",
        "n_strands": n_strands,
        "n_generators": n_gens,
        "n_unique_signatures": len(groups),
        "factor_keys": new_ops,
    }


def _signature_hash_to_float(sig: str) -> float:
    """Hash the signature to a single float for plancherel_signature
    storage (KnotOperation.plancherel_signature requires float values).

    Renamed from `_signature_to_dict` per Copilot review #r3143...
    (the function returns a float, not a dict).
    """
    import hashlib
    h = int(hashlib.sha256(sig.encode()).hexdigest()[:8], 16)
    return float(h % 1_000_000) / 1_000_000.0


# ─────────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--isotope",
        choices=["D", "T", "3He", "4He"],
        help="Single isotope to discover.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Discover for D, T, 3He, 4He.",
    )
    parser.add_argument(
        "--cache-path",
        type=Path,
        default=Path(__file__).parent / "knot-operation-cache.json",
        help="Cache JSON path.",
    )
    args = parser.parse_args()

    isotopes = {
        "D": (1, 1),
        "T": (1, 2),
        "3He": (2, 1),
        "4He": (2, 2),
    }

    if args.all:
        targets = list(isotopes.items())
    elif args.isotope:
        targets = [(args.isotope, isotopes[args.isotope])]
    else:
        parser.error("specify --isotope X or --all")

    cache = KnotOperationCache(args.cache_path)
    print(f"Loaded cache: {len(cache.operations)} operations, "
          f"{len(cache.factorizations)} factorizations")

    for name, (Z, N) in targets:
        print(f"\nDiscovering: {name} (Z={Z}, N={N})")
        try:
            summary = discover_for_isotope(Z, N, cache, feeder_name="wedderburn_discovery_feeder")
            print(f"  n_strands     = {summary['n_strands']}")
            print(f"  n_generators  = {summary['n_generators']}")
            print(f"  unique groups = {summary['n_unique_signatures']}")
            print(f"  factor keys   = {summary['factor_keys']}")
        except Exception as e:
            print(f"  ERROR: {type(e).__name__}: {e}")

    cache.save()
    print(f"\nFinal cache state:")
    print(cache.report())
    return 0


if __name__ == "__main__":
    sys.exit(main())
