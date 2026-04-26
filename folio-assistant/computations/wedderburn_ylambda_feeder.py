#!/usr/bin/env python3
"""
F4.2.γ: y_λ-based Wedderburn-block feeder using the Jones-Markov
witness from `y-lambda-jones-markov-witness.json` (PR #430).

Unlike the previous channel-signature / character-magnitude bin
feeders, this one uses the **actual Jones-Markov block weights**
y_λ — solved from `tr_M(w_μ) = z^{n−ℓ(μ)}` for cycle-type
representatives — as the `plancherel_signature` of each
KnotOperation.  This is the *canonical* Wedderburn fingerprint:
two operations with the same y_λ vector are spectrally
indistinguishable on H_n(R, q).

## What it emits

For each `n` in the witness file (n=2..12), a single
`KnotOperation` per partition `λ ⊢ n` with:

  - `n` = strand count
  - `braid_word_normal_form` = []  (witness is per-partition, not
    per-word)
  - `plancherel_signature` = {`y_lambda`: <float>, `depth`: <float>}
  - `fingerprint` = {`feeder`: ..., `partition`: '(p1,p2,...)',
    `n`: str(n)}

Cross-isotope dedup is automatic because the cache key is derived
from `(n, fingerprint)` and the fingerprint contains only the
partition + n + feeder name (no isotope-specific metadata, per
PR #428 round-3 review).

## Status

- Inputs: `y-lambda-jones-markov-witness.json` (must exist; from PR #430).
- Outputs: appends to `knot-operation-cache.json`.
- Cross-isotope: shares with the channel-signature feeder
  (`wedderburn_discovery_feeder.py`) for the same `n` since both
  use the same KnotOperationCache.  The discovery layer can later
  match channel-signature operations to y_λ operations by `n` and
  cluster the per-partition y_λ values.

@module folio-assistant/computations/wedderburn_ylambda_feeder
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from knot_operation_cache import KnotOperation, KnotOperationCache


WITNESS_PATH = Path(__file__).parent / "y-lambda-jones-markov-witness.json"


def discover_for_n(
    n: int,
    cache: KnotOperationCache,
    witness: dict,
    feeder_name: str = "wedderburn_ylambda_feeder",
    refresh: bool = False,
) -> dict:
    """For partition table at strand-count `n`, emit one KnotOperation
    per `λ ⊢ n` with the witness y_λ as `plancherel_signature`.

    If `refresh=True` (Copilot review #r3143884872), existing cache
    entries with matching `cache_key` have their `plancherel_signature`
    overwritten with the freshly-loaded witness values — useful when
    the witness JSON has been regenerated and the cache should
    treat it as the source of truth.  By default re-runs only merge
    `discovered_in` and leave existing y_λ values untouched
    (idempotent under unchanged inputs)."""
    table = witness["tables_by_n"].get(str(n))
    if table is None:
        return {"n": n, "n_partitions": 0, "cache_keys": []}

    new_ops = []
    for entry in table["weights"]:
        partition = tuple(entry["partition"])
        y_lambda = float(entry["y_lambda"])
        depth = float(entry["depth"])

        partition_str = "(" + ",".join(str(p) for p in partition) + ")"
        fingerprint = {
            "feeder": feeder_name,
            "n": str(n),
            "partition": partition_str,
        }
        plancherel_sig = {
            "y_lambda": y_lambda,
            "depth": depth,
        }
        op = KnotOperation(
            n=n,
            braid_word_normal_form=[],
            plancherel_signature=plancherel_sig,
            fingerprint=fingerprint,
        )
        cache_key = cache.add_operation(op, discovered_in=feeder_name)
        # On --refresh, force-overwrite plancherel_signature on the
        # existing entry so a regenerated witness propagates.
        if refresh and cache_key in cache.operations:
            cache.operations[cache_key].plancherel_signature = plancherel_sig
        new_ops.append(cache_key)

    cache.add_factorization(
        parent_n=n,
        parent_braid_id=f"H{n}_full_y_lambda_table",
        factor_keys=new_ops,
        discovered_by=feeder_name,
    )

    return {
        "n": n,
        "q_0": table.get("q_0"),
        "z_markov": table.get("z_markov"),
        "n_partitions": len(table["weights"]),
        "cache_keys": new_ops,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--n", type=int, default=None,
        help="Single n to feed (defaults to all).",
    )
    parser.add_argument(
        "--cache-path", type=Path,
        default=Path(__file__).parent / "knot-operation-cache.json",
    )
    parser.add_argument(
        "--witness", type=Path, default=WITNESS_PATH,
        help="Jones-Markov witness JSON path.",
    )
    parser.add_argument(
        "--refresh", action="store_true",
        help="Force-overwrite plancherel_signature on existing cache "
             "entries from the freshly-loaded witness (Copilot review "
             "#r3143884872).  Default: leave existing entries unchanged.",
    )
    args = parser.parse_args()

    if not args.witness.exists():
        print(f"ERROR: witness not found at {args.witness}", file=sys.stderr)
        print("       Run y_lambda_jones_markov_witness.py first or merge PR #430.")
        return 1

    # Explicit utf-8 (Gemini #r3145...): JSON files in this repo are
    # ASCII-safe but the encoding default on Windows is cp1252; force
    # utf-8 for cross-platform consistency.
    with open(args.witness, encoding="utf-8") as f:
        witness = json.load(f)

    cache = KnotOperationCache(args.cache_path)
    print(f"Loaded cache: {len(cache.operations)} operations, "
          f"{len(cache.factorizations)} factorizations")

    available_ns = sorted(int(k) for k in witness["tables_by_n"].keys())
    targets = [args.n] if args.n is not None else available_ns

    for n in targets:
        if n not in available_ns:
            print(f"  skip n={n} (not in witness)")
            continue
        summary = discover_for_n(n, cache, witness, refresh=args.refresh)
        print(f"\nn={n}: {summary['n_partitions']} partitions, "
              f"q_0={summary['q_0']}, z_markov={summary['z_markov']}")
        if summary["cache_keys"]:
            head = ", ".join(summary["cache_keys"][:3])
            tail = "..." if len(summary["cache_keys"]) > 3 else ""
            print(f"   first keys: {head}{tail}")

    cache.save()
    print(f"\nFinal cache: {len(cache.operations)} operations, "
          f"{len(cache.factorizations)} factorizations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
