"""Cross-check witness — SnapPy-tier Borromean volume ≡ 8·G at every precision tier.

Companion to `snappy_borromean_volume.py` (the producer witness).
This script provides the **independence layer** of the SnapPy
migration pattern: it verifies that the values emitted by the
producer agree with `8·mpmath.catalan` at the declared precision
of each tier, via an independent recomputation.

The cross-check is intentionally redundant with the producer's
internal computation — when SnapPy is locally available, the
producer asserts `snappy_value == 8·G` directly; this script
asserts the same identity from a fresh mpmath computation,
guaranteeing the producer witness wasn't drift-modified.

## Architecture

Per the migration pattern (see `snappy_borromean_volume.py`
docstring):

```
                     ┌─► snappy-borromean-volume.witness.json (producer)
SnapPy / Adams 1985 ─┤
                     └─► snappy-borromean-volume-cross-check.witness.json (this)
                            cross-validates each precision tier
                            via independent 8·G recomputation
```

Both witnesses point at the canonical mathematical truth
(`Vol(L6a4) = 8·G`) but via independent code paths. If one drifts
(typo, stale literal, bad precision tier), the staleness check
in the witness pipeline surfaces the disagreement.

## Why a separate script (not inlined in producer)

- **Independence**: producer could be modified to emit wrong
  values; cross-check would catch it.
- **Reproducibility audit**: this script can be re-run on demand
  against a stored producer witness without re-running the
  producer.
- **Layering hygiene**: producer = SnapPy authority + Adams 1985
  fallback; cross-check = mpmath authority via Catalan identity.

References:
- Adams, C. C. (1985), Proc. Amer. Math. Soc. 100, 601-606
  (the `Vol(L6a4) = 8·G` identity).
- Lewin (1981), Polylogarithms §4.2 eq. 4.2.21 (`Λ(π/4) = G/2`,
  underpins the 8·G derivation).
- `snappy_borromean_volume.py` — producer witness.
- `borromean_volume_100dps.py` — existing 100-dps Lobachevsky-
  integration cross-check (this script complements it across the
  full tier ladder).
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path
import mpmath as mp
from mpmath import mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


# Producer witness this script verifies against.
PRODUCER_WITNESS_NAME = "snappy-borromean-volume.witness.json"


def load_witness(name: str) -> dict:
    p = HERE / name
    if not p.exists():
        return {}
    return json.loads(p.read_text())


def canonical_via_catalan(dps: int) -> mpf:
    """The canonical Vol(L6a4) = 8·G at the requested precision.

    Identical to `snappy_borromean_volume.canonical_via_catalan`;
    duplicated here intentionally for code-path independence
    (cross-check must not import the producer).
    """
    with mp.workdps(dps + 10):  # safety margin
        return 8 * mp.catalan


def main():
    _t0 = time.perf_counter()
    set_compute_dps()

    print("=" * 76)
    print("  SnapPy Borromean volume — Catalan cross-check across precision tiers")
    print("=" * 76)
    print()

    # Load the producer witness.
    producer = load_witness(PRODUCER_WITNESS_NAME)
    producer_data = producer.get("data", {})
    alt_precision = producer_data.get("alt_precision", {})
    if not alt_precision:
        print(f"  ERROR: producer witness {PRODUCER_WITNESS_NAME} has no")
        print("         alt_precision data — was the producer re-run after")
        print("         the migration to the tiered-precision format?")
        return 1

    print(f"  Producer witness: {PRODUCER_WITNESS_NAME}")
    print(f"  Producer manifold: {producer_data.get('manifold', '?')}")
    print(f"  Producer canonical identity: "
          f"{producer_data.get('canonical_identity', '?')}")
    print()

    print(f"  {'tier (dps)':>11}  {'producer_value':>40}  "
          f"{'|producer − 8·G|':>22}")
    print(f"  {'-'*11}  {'-'*40}  {'-'*22}")

    cross_check_results = []
    all_tiers_pass = True
    for tier_str, producer_value_str in sorted(
            alt_precision.items(), key=lambda kv: int(kv[0])):
        tier = int(tier_str)
        with mp.workdps(tier + 20):
            producer_value = mpf(producer_value_str)
            canonical = canonical_via_catalan(tier)
            delta = abs(producer_value - canonical)
            # tolerance: 5 ULP at this precision tier
            tolerance = mpf(10) ** (-(tier - 2))
            passes = delta < tolerance
        if not passes:
            all_tiers_pass = False
        print(f"  {tier:>11d}  {producer_value_str[:40]:>40}  "
              f"{float(delta):>22.3e}")
        cross_check_results.append({
            "tier_dps": tier,
            "producer_value": producer_value_str,
            "canonical_8G": mp.nstr(canonical, tier, strip_zeros=False),
            "delta": mp.nstr(delta, 5),
            "tolerance": mp.nstr(tolerance, 5),
            "passes": bool(passes),
        })

    print()
    print(f"  All tiers pass cross-check: {all_tiers_pass}")
    print()

    w = WitnessBuilder("snappy-borromean-volume-cross-check",
                       engine="mpmath", start_time=_t0)
    w.set_description(
        "Cross-check witness for Vol(L6a4) = 8·G: verifies that "
        f"`{PRODUCER_WITNESS_NAME}` agrees with an independent 8·G "
        "recomputation at every emitted precision tier (15 / 30 / "
        "50 / 100 / 200 dps). Independence layer of the SnapPy "
        "migration pattern — if the producer is drift-modified "
        "the disagreement surfaces here."
    )
    w.add_data("producer_witness", PRODUCER_WITNESS_NAME)
    w.add_data("cross_check_results", cross_check_results)
    w.add_data("all_tiers_pass", all_tiers_pass)
    w.add_data("identity_under_test", "Vol(L6a4) = 8·mpmath.catalan (Adams 1985)")
    w.add_assertion(
        "all_precision_tiers_match_canonical",
        computed=1 if all_tiers_pass else 0, expected=1, tolerance=0,
        source=(f"Producer witness {PRODUCER_WITNESS_NAME} agrees "
                f"with 8·G at every emitted precision tier within "
                "5 ULP of declared precision.")
    )
    print(f"  Witness: {w.save()}")
    # Per Copilot review: return non-zero on tier mismatch so CI
    # runners keyed on exit code detect drift between producer and
    # canonical 8·G. The "independence layer" guarantee depends on
    # this — without it, drift would only surface via the witness
    # JSON `passed` field, which CI may not inspect.
    return 0 if all_tiers_pass else 1


if __name__ == "__main__":
    sys.exit(main())
