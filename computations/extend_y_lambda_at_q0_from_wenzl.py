#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical merge script; q is fixed
# at q_0 throughout via the upstream Wenzl-bridge closed-form output.
"""Merge n ≥ 13 entries from `y-lambda-wenzl-witness.json` (numerical
closed-form output at q_0, 100 dps) into `y-lambda-at-q0.witness.json`
(the production cache, 50-dps strings).

**Why this script exists.** The original cache builder
`y_lambda_at_q0_cache.py` reads from `y-lambda-wenzl-bridge-symbolic-
witness.json`, which only ships symbolic y_λ(q) for n ∈ {2..12}. The
sympy `sp.cancel + factor` path that produces those symbolic strings
scales **exponentially** in n — extending it to n ≥ 13 takes hours
per shape (per the `2026-05-17-1ppb-workplan-v1-refined.md` audit
on PR #689).

`y_lambda_wenzl_bridge.py` already implements a **closed-form
numerical evaluator** based on the fractional Wenzl principal Schur
specialisation `s_{λ,X}(Q)` (Macdonald I.3 ex.1 + analytic
continuation in `X`). It runs all 412 partitions of n=13..15 at
100 dps in **seconds**. The output `y-lambda-wenzl-witness.json`
carries y_λ(q_0) at 100 dps numerically — sufficient for every
downstream consumer that reads via `wedderburn_jones_markov.y_lambda_at(n, q_0)`.

This script bridges the two: it reads the new wenzl-witness file
and writes additive entries into the production cache at the
canonical 50 dps. Existing entries (n=2..12 from the symbolic
source) are **not touched** — they remain the source of truth for
those n.

**Coverage extension chain:** running this script + the upstream
generator unlocks Rust canonical-χ evaluation for:
  - ⁵Li (n=15)  ← this PR
  - ⁶Li (n=18)  ← next: run `y_lambda_wenzl_bridge.py 16 17 18`
  - ⁷Li/⁷Be (n=21)  ← then `... 19 20 21`
  - ⁸Be (n=24)  ← then `... 22 23 24`

Each step takes O(seconds) of Wenzl-bridge compute. Per-script
ceiling: ~n=30 before the per-partition closed-form evaluation
itself becomes slow at 100 dps (closed form is O(n) per partition;
total partition count grows ~exp(π·√(2n/3)) but each is fast).

Usage:
    python3 extend_y_lambda_at_q0_from_wenzl.py

Idempotent — re-running with no new entries in the upstream file
is a no-op.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60  # enough precision to truncate 100-dps → 50-dps cleanly

HERE = Path(__file__).resolve().parent
SRC = HERE / "y-lambda-wenzl-witness.json"
DST = _pb.witness_path("y-lambda-at-q0.witness.json", HERE)


def main() -> int:
    if not SRC.exists():
        raise FileNotFoundError(
            f"missing upstream {SRC.name}; run "
            f"`python3 y_lambda_wenzl_bridge.py 13 14 15` first."
        )
    src = json.loads(SRC.read_text())
    dst = json.loads(DST.read_text())
    src_tables = src.get("tables_by_n", {})
    dst_by_n = dst["data"]["by_n"]

    added: list[int] = []
    for n_str, entry in sorted(src_tables.items(), key=lambda kv: int(kv[0])):
        n = int(n_str)
        if str(n) in dst_by_n:
            # Already covered (n=2..12 from symbolic source); don't
            # clobber. The closed-form numerical values agree with
            # the symbolic-eval values at q_0 to all displayed digits
            # at the existing precision — verified manually on n=12.
            continue
        rows = []
        for w in entry["weights"]:
            y_full = mp.mpf(w["y_lambda_numeric"])
            rows.append({
                "partition": w["partition"],
                "y_at_q0_50dps": mp.nstr(y_full, 50, strip_zeros=False),
            })
        dst_by_n[str(n)] = rows
        added.append(n)
        print(f"  added n={n}: {len(rows)} partitions")

    # Keep the witness metadata self-consistent with the by_n data
    # (per Gemini review on PR #691): n_values, n_total_partitions,
    # and description all need to reflect the current ceiling, not
    # the original n=12 boundary baked into the legacy witness.
    # Runs unconditionally (even when `added` is empty) so a stale
    # witness from a prior partial run gets fixed up on the next
    # invocation.
    params = dst.setdefault("parameters", {})
    new_n_values = sorted(int(k) for k in dst_by_n.keys())
    new_total = sum(len(rows) for rows in dst_by_n.values())
    metadata_stale = (
        params.get("n_values") != new_n_values
        or params.get("n_total_partitions") != new_total
    )
    if not added and not metadata_stale:
        print("  no new entries; metadata already consistent — no-op.")
        return 0
    params["n_values"] = new_n_values
    params["n_total_partitions"] = new_total
    n_min, n_max = new_n_values[0], new_n_values[-1]
    dst["description"] = (
        f"Numeric cache of y_λ(q_0) at 50 dps for n ∈ "
        f"{{{n_min}, ..., {n_max}}}. Source for n=2..12 is "
        f"`y-lambda-wenzl-bridge-symbolic-witness.json` evaluated "
        f"via sympy.subs; source for n ≥ 13 is the numerical "
        f"closed-form Wenzl-bridge evaluator "
        f"(`y-lambda-wenzl-witness.json`, merged by "
        f"`extend_y_lambda_at_q0_from_wenzl.py`). Output strings "
        f"trimmed to exactly 50 dps via mp.nstr."
    )

    sources = params.setdefault("sources", [])
    new_src = (
        f"y-lambda-wenzl-witness.json (n={'/'.join(str(n) for n in added)}, "
        "numerical closed-form via Wenzl bridge)"
    )
    if new_src not in sources:
        sources.append(new_src)

    # Save via WitnessBuilder.wrap_legacy so scriptHash, scriptCommitSha,
    # computedAt and durationMs are refreshed automatically. This
    # keeps the drift detector aware that THIS script touched the
    # file (per Gemini review on PR #691).
    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "y-lambda-at-q0",
        dst,
        script_path=__file__,
        engine="mpmath",
    )
    out = builder.save()
    covered = sorted(dst_by_n.keys(), key=int)
    print(f"\n  extended {Path(out).name}: n now = {covered}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
