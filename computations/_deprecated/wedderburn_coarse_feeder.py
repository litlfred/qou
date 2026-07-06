#!/usr/bin/env python3
"""
F4.2.β.β: Coarser-invariant Wedderburn fingerprint feeders.

The F4.2.β feeder fingerprints by sign × log-magnitude rounded to
4 digits — too granular to detect cross-isotope sharing.  This
script provides three coarser feeders that DO expose recurring
sub-structures across isotopes:

  1. **Sign-only feeder**: bin per-Wedderburn-block by sign of
     χ_λ(β) (positive / negative / zero).  Very coarse → high
     cross-isotope sharing.
  2. **Magnitude-only feeder**: bin by |χ_λ(β)| log-magnitude
     rounded to 1 digit.  Mid-coarseness.
  3. **Sign-magnitude feeder**: combined fingerprint at precision=2.
     Finer than (1) but coarser than F4.2.β's precision=4.

Each feeder produces a separate set of `KnotOperation` cache keys.
Operations recurring across different isotopes (e.g., T and ³He
sharing a sign-pattern at depth 3) get observed in `discovered_in`
multiple times → "multi-feeder ops".

@module computations/wedderburn_coarse_feeder
"""
from __future__ import annotations
import argparse
import hashlib
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pyhecke_native as p  # type: ignore[import]
from hecke_characters import partitions_of  # type: ignore[import]
from knot_operation_cache import KnotOperation, KnotOperationCache
from plancherel_term_7 import atomic_braid_word
from q_parameter import Q as Q0_FLOAT  # type: ignore[import]


# ── Bin functions ─────────────────────────────────────────────

def bin_sign_only(value: float) -> str:
    if value > 0:
        return "+"
    if value < 0:
        return "-"
    return "0"


def bin_magnitude_only(value: float, precision: int = 1) -> str:
    if value == 0:
        return "0"
    return f"|{round(math.log10(abs(value)), precision)}|"


def bin_sign_magnitude(value: float, precision: int = 2) -> str:
    if value == 0:
        return "0"
    sign = "+" if value > 0 else "-"
    return f"{sign}{round(math.log10(abs(value)), precision)}"


# ── Feeder factory ─────────────────────────────────────────────

def discover_with_binner(
    Z: int, N: int, cache: KnotOperationCache,
    bin_fn, feeder_name: str,
    q: float = float(Q0_FLOAT),
) -> dict:
    """Generic feeder — fingerprint χ_λ(β) for every λ via `bin_fn`,
    group by bin, emit one KnotOperation per non-trivial bin."""
    A = Z + N
    n = 3 * A
    word = atomic_braid_word(Z, N)
    word_m = [(1 if s == "+" else -1, g) for s, g in word]
    parts = list(partitions_of(n))
    chis = p.chi_lambdas_braid([list(lam) for lam in parts], word_m, q)

    by_bin: dict[str, list[tuple]] = {}
    for lam, chi in zip(parts, chis):
        label = bin_fn(float(chi))
        by_bin.setdefault(label, []).append((tuple(lam), float(chi)))

    new_ops = []
    for bin_label, items in sorted(by_bin.items()):
        if bin_label == "0":
            continue
        # Per Copilot review #r3144...: keep bin identity in the
        # `fingerprint` metadata rather than overloading
        # `braid_word_normal_form` (reserved for actual Hecke NFs).
        # Cache_key derives from (n, fingerprint) when NF is empty.
        sig = {
            "n_partitions_in_bin": float(len(items)),
            "max_height": float(max(len(l) for l, _ in items)),
        }
        fingerprint = {
            "feeder": feeder_name,
            "bin_label": bin_label,
        }
        op = KnotOperation(
            n=n,
            braid_word_normal_form=[],  # no real NF for coarse-bin entries
            plancherel_signature=sig,
            fingerprint=fingerprint,
        )
        cache_key = cache.add_operation(op, discovered_in=feeder_name)
        new_ops.append(cache_key)

    cache.add_factorization(
        parent_n=n,
        parent_braid_id=f"atom_Z{Z}_N{N}_{feeder_name}",
        factor_keys=new_ops,
        discovered_by=feeder_name,
    )
    return {
        "isotope": f"Z={Z},N={N}",
        "n": n,
        "n_bins": len(by_bin),
        "factor_keys": new_ops,
    }


# ── Public feeder entry points ─────────────────────────────────

def discover_for_isotope_sign_only(Z, N, cache, feeder_name="sign_only_feeder"):
    return discover_with_binner(Z, N, cache, bin_sign_only, feeder_name)


def discover_for_isotope_magnitude_only(Z, N, cache, feeder_name="magnitude_only_feeder"):
    return discover_with_binner(
        Z, N, cache, bin_magnitude_only, feeder_name)


def discover_for_isotope_sign_mag_p2(Z, N, cache, feeder_name="sign_magnitude_p2_feeder"):
    return discover_with_binner(
        Z, N, cache,
        lambda v: bin_sign_magnitude(v, precision=2),
        feeder_name,
    )


# ── CLI ────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cache-path", type=Path,
        default=Path(__file__).parent / "knot-operation-cache.json",
    )
    parser.add_argument(
        "--feeder",
        choices=["sign_only", "magnitude_only", "sign_magnitude_p2", "all"],
        default="all",
    )
    args = parser.parse_args()

    cache = KnotOperationCache(args.cache_path)
    print(f"Loaded cache: {len(cache.operations)} operations\n")

    isotopes = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
    feeders_to_run = []
    if args.feeder in ("sign_only", "all"):
        feeders_to_run.append(("sign_only_feeder", discover_for_isotope_sign_only))
    if args.feeder in ("magnitude_only", "all"):
        feeders_to_run.append(("magnitude_only_feeder", discover_for_isotope_magnitude_only))
    if args.feeder in ("sign_magnitude_p2", "all"):
        feeders_to_run.append(("sign_magnitude_p2_feeder", discover_for_isotope_sign_mag_p2))

    for fname, fn in feeders_to_run:
        print(f"=== {fname} ===")
        for iso_name, Z, N in isotopes:
            try:
                summary = fn(Z, N, cache, feeder_name=fname)
                print(f"  {iso_name}: n={summary['n']}, "
                      f"{summary['n_bins']} bins, "
                      f"{len(summary['factor_keys'])} ops")
            except Exception as e:
                print(f"  {iso_name}: ERROR {type(e).__name__}: {e}")
        print()

    cache.save()

    # Summarize cross-feeder + cross-isotope sharing.
    print(f"Final cache: {len(cache.operations)} operations")
    multi = [op for op in cache.operations.values()
             if len(op.discovered_in) > 1]
    print(f"Multi-feeder ops (recurring structure): {len(multi)}")
    if multi:
        print("  Sample shared keys:")
        for op in multi[:5]:
            print(f"    {op.cache_key()}: {op.discovered_in}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
