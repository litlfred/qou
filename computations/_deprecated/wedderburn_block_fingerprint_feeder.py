#!/usr/bin/env python3
"""
F4.2.β: Wedderburn-block character fingerprint discovery.

Deeper structural discovery than F4.2.α (channel-signature):
fingerprint each atomic braid by the **full vector of per-Wedderburn-
block characters** `(λ, χ_λ(β))` for every partition λ ⊢ n.

Two braids share a sub-structure iff their fingerprints agree on
specific (λ, χ_λ) pairs.  This is the closest practical analogue to
SDP discovery without solving an actual SDP — the character vector
IS the dual structure that an SDP would extract.

## Method

For each isotope (Z, N):
  1. Build the atomic braid β.
  2. For every partition λ ⊢ 3A (where 3A = number of strands):
     compute χ_λ(β) using the Hoefsmit f64 kernel
     (`pyhecke_native.chi_lambda_braid`).
  3. The vector `(χ_λ(β))_λ` is the Wedderburn-block fingerprint.
  4. Group blocks by character magnitude bins; cache as
     `KnotOperation` entries.

## Cross-isotope sharing detection

Two braids share a "knot operation" if their fingerprints agree on
at least one (λ, χ_λ) pair to high precision.  We bin characters by
log-magnitude rounded to a configurable precision (default 4 digits)
and use the bin label as the operation's cache key.

## Status

- F4.2.β α: per-block character extraction + bin-based fingerprinting
  (this script).  Catalogs 148 ops across D / T / ³He / ⁴He at
  precision=4 (sign + log-magnitude rounded to 4 digits).
- F4.2.β β: cross-isotope sharing detection.  Currently 0 shared ops
  observed because exact characters differ between Z/N variants.
  Need coarser invariants:
    - |χ_λ(β)| only (drop sign) → groups T/³He by magnitude
    - log10|χ_λ(β)| rounded to ≤ 2 digits → broader bins
    - sign-only signature → very coarse, always matches across isotopes
  Defer to a higher-level analysis pass that picks the right
  invariant for each downstream use.
- F4.2.β γ: SDP feasibility check on the centralizer ideal at each
  Wedderburn block (deferred — requires cvxpy + the full y-lambda
  SDP machinery from PR #430).

Usage:
    python3 wedderburn_block_fingerprint_feeder.py --isotope D
    python3 wedderburn_block_fingerprint_feeder.py --all

@module computations/wedderburn_block_fingerprint_feeder
"""
from __future__ import annotations
import argparse
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pyhecke_native as p  # type: ignore[import]
from hecke_characters import partitions_of  # type: ignore[import]
from knot_operation_cache import KnotOperation, KnotOperationCache
from plancherel_term_7 import atomic_braid_word
from q_parameter import Q as Q0_FLOAT  # type: ignore[import]


def signature_bin(value: float, precision: int = 4) -> str:
    """Bin a real character value by log-magnitude rounded to `precision`.

    `value` may be 0; `None` is returned for that case.  Otherwise we
    take `sign(value) * round(log10(|value|), precision)` as the bin
    label.  This groups characters of similar magnitude together.
    """
    if value == 0:
        return "0"
    sign = "+" if value > 0 else "-"
    log_mag = round(math.log10(abs(value)), precision)
    return f"{sign}{log_mag}"


def fingerprint_isotope(
    Z: int, N: int, q: float = float(Q0_FLOAT), precision: int = 4
) -> dict:
    """Compute the Wedderburn-block character fingerprint of the
    atomic braid of (Z, N)."""
    A = Z + N
    n = 3 * A
    word = atomic_braid_word(Z, N)
    word_m = [(1 if s == "+" else -1, g) for s, g in word]

    parts = list(partitions_of(n))
    chis = p.chi_lambdas_braid(
        [list(lam) for lam in parts], word_m, q
    )
    fingerprint = []
    for lam, chi in zip(parts, chis):
        fingerprint.append({
            "lambda": tuple(lam),
            "chi": float(chi),
            "bin": signature_bin(float(chi), precision),
        })
    return {
        "Z": Z, "N": N, "A": A, "n": n, "n_partitions": len(parts),
        "q": q, "precision": precision,
        "fingerprint": fingerprint,
    }


def discover_for_isotope(
    Z: int, N: int, cache: KnotOperationCache,
    feeder_name: str = "wedderburn_block_fingerprint_feeder",
    precision: int = 4,
) -> dict:
    """Discover Wedderburn-block operations for an isotope and emit
    them as `KnotOperation` cache entries."""
    fp = fingerprint_isotope(Z, N, precision=precision)

    # Group partitions by character bin.
    by_bin: dict[str, list[dict]] = {}
    for entry in fp["fingerprint"]:
        by_bin.setdefault(entry["bin"], []).append(entry)

    # Each non-empty bin is a candidate KnotOperation.  The cache_key
    # is a SHA-256 hash of (n, NF), so we need the NF marker itself
    # to carry the bin's identity — otherwise different bins collide.
    # Strategy: encode (sign, gen) pairs where `sign` carries bin-hash
    # info (positive 32-bit ID) and `gen` is the partition's row count
    # (a stable per-partition statistic that disambiguates within a bin).
    new_ops = []
    for bin_label, entries in sorted(by_bin.items()):
        if bin_label == "0":
            continue  # vanishing-character bin is uninformative
        # Per Copilot review #r3144...: bin identity lives in the
        # `fingerprint` metadata.  `braid_word_normal_form` stays
        # empty since no real Hecke NF is computed for these bins.
        sig = {
            "n_partitions_in_bin": float(len(entries)),
            "max_partition_depth": float(max(len(e["lambda"]) - 1 for e in entries)),
            "min_partition_depth": float(min(len(e["lambda"]) - 1 for e in entries)),
        }
        fingerprint = {
            "feeder": feeder_name,
            "bin_label": bin_label,
        }
        op = KnotOperation(
            n=fp["n"],
            braid_word_normal_form=[],
            plancherel_signature=sig,
            fingerprint=fingerprint,
        )
        cache_key = cache.add_operation(op, discovered_in=feeder_name)
        new_ops.append(cache_key)

    cache.add_factorization(
        parent_n=fp["n"],
        parent_braid_id=f"atom_Z{Z}_N{N}_3A{fp['n']}_wblock_fp",
        factor_keys=new_ops,
        discovered_by=feeder_name,
    )

    return {
        "isotope": f"Z={Z},N={N}",
        "n": fp["n"],
        "n_partitions": fp["n_partitions"],
        "n_unique_bins": len(by_bin),
        "cache_keys": new_ops,
    }


def _bin_to_float(bin_label: str) -> float:
    """Reduce a bin label string to a stable float for storage."""
    import hashlib
    h = int(hashlib.sha256(bin_label.encode()).hexdigest()[:8], 16)
    return float(h % 1_000_000) / 1_000_000.0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--isotope", choices=["D", "T", "3He", "4He"])
    parser.add_argument("--all", action="store_true")
    parser.add_argument(
        "--cache-path", type=Path,
        default=Path(__file__).parent / "knot-operation-cache.json",
    )
    parser.add_argument("--precision", type=int, default=4)
    args = parser.parse_args()

    isotopes = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
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
        print(f"\nFingerprinting: {name} (Z={Z}, N={N})")
        try:
            summary = discover_for_isotope(
                Z, N, cache,
                feeder_name="wedderburn_block_fingerprint_feeder",
                precision=args.precision,
            )
            print(f"  n              = {summary['n']}")
            print(f"  n_partitions   = {summary['n_partitions']}")
            print(f"  unique bins    = {summary['n_unique_bins']}")
            print(f"  cache keys     = {summary['cache_keys'][:5]}"
                  f"{'...' if len(summary['cache_keys']) > 5 else ''}")
        except Exception as e:
            print(f"  ERROR {type(e).__name__}: {e}")

    cache.save()
    print(f"\nFinal cache: {len(cache.operations)} operations, "
          f"{len(cache.factorizations)} factorizations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
