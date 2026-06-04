#!/usr/bin/env python3
"""Validate ck-dk-registry.json against the flip-flop guard invariants.

The registry (docs/coordination/ck-dk-canonical-registry.md + its JSON
twin ck-dk-registry.json) is the single source of truth for the
canonical-vs-empirical status of the Q_β c_k ladder and the m_p d_k
tower. This validator enforces the §8 flip-flop guard so the registry
cannot silently drift:

  1. Any WIRED rung must be tier `canonical` (anchor-stable, derived).
     (No empirical/near-match/fit/refuted rung may be wired.)
  2. Every rung's tier must be one of the declared tiers.
  3. production.qbeta_wired_rungs must match the rungs marked wired=true.

Exit 0 if consistent; exit 1 with a report otherwise. No external deps.

Usage:
  python3 docs/coordination/ck_dk_registry_validate.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTRY = HERE / "ck-dk-registry.json"


def main() -> int:
    d = json.loads(REGISTRY.read_text(encoding="utf-8"))
    tiers = set(d["meta"]["tiers"].keys())
    errors: list[str] = []

    def check_rungs(family_key: str, rungs: list[dict]) -> list[int]:
        wired = []
        for r in rungs:
            rung = r.get("rung")
            tier = r.get("tier")
            if tier not in tiers:
                errors.append(f"{family_key} rung {rung}: unknown tier {tier!r}")
            if r.get("wired"):
                wired.append(rung)
                if tier != "canonical":
                    errors.append(
                        f"{family_key} rung {rung}: WIRED but tier={tier!r} "
                        f"(flip-flop guard: only `canonical` may be wired)"
                    )
        return wired

    ck_wired = check_rungs("qbeta_ck", d["qbeta_ck_ladder"]["rungs"])
    dk_wired = check_rungs("mp_dk", d["mp_dk_tower"]["rungs"])

    prod = d["production"]
    # rungs are uniformly strings; single rungs are bare digits, ranges
    # contain "-" (e.g. "6-7"). Only single rungs may be wired.
    def _is_single(rung) -> bool:
        return isinstance(rung, str) and "-" not in rung

    if sorted(x for x in ck_wired if _is_single(x)) != sorted(
        prod["qbeta_wired_rungs"]
    ):
        errors.append(
            f"production.qbeta_wired_rungs {prod['qbeta_wired_rungs']} "
            f"!= rungs marked wired {ck_wired}"
        )
    if sorted(x for x in dk_wired if _is_single(x)) != sorted(
        prod["mp_wired_rungs"]
    ):
        errors.append(
            f"production.mp_wired_rungs {prod['mp_wired_rungs']} "
            f"!= rungs marked wired {dk_wired}"
        )

    if errors:
        print("ck-dk-registry.json: FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("ck-dk-registry.json: OK")
    print(f"  Q_β c_k wired rungs: {ck_wired or 'none'} "
          f"(canonical only — flip-flop guard satisfied)")
    print(f"  m_p d_k wired rungs: {dk_wired or 'none'}")
    print(f"  dashboard: {prod['dashboard_beats_100x']}/{prod['dashboard_total']} "
          f"beats-100×")
    return 0


if __name__ == "__main__":
    sys.exit(main())
