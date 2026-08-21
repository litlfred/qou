#!/usr/bin/env python3
"""What did the q₀ proton migration actually move? — by quantity, not by file.

## Why from git, and not from the sweep

`q0_repin_sweep.py` measures movement in-process by snapshotting each witness
before it runs. That is fine for a live progress line and useless as a record:
the snapshot resets on every restart, and this migration has survived several.
Worse, a producer re-run twice reports "no change" the second time, because by
then the file on disk is already the new value — so the in-process number
UNDER-reports exactly the quantities that moved.

Git does not have that problem. The merge-base with `origin/main` is the true
pre-migration state, it survives restarts, and it cannot be confused by a
re-run. So the authoritative movement report is a diff, computed here.

## By quantity, not by file

Reporting "37 witnesses changed" says nothing about whether the framework's
predictions moved. `qou-eea0` sets the standard: report the impact on physical
quantities. So fields are grouped by their leaf name (`tr_M_at_q0`,
`B_pred_canonical_MeV`, `m_mu_pred_MeV`, …) across every witness that carries
them, and each group reports its own spread.

A q₀ re-pin of 11.54 ppb should move most things by ~11.5 ppb. Two bands are
worth a reader's attention and are called out separately:

  * **≈ 11.5 ppb** — the expected re-pin signature. Unremarkable, and its
    absence would be the surprise.
  * **anything much larger** — either an amplified quantity (a ratio near a
    pole, a difference of near-equal numbers) or a producer that changed for a
    reason unrelated to the pin. Both need a human; neither is assumed benign.

Fields whose magnitude is below `_FLOOR` are excluded from the relative
statistic: a residual going 1e-60 → 1.5e-59 is a 900 %-looking move that says
nothing. They are still counted as "changed".

Usage:
    python3 q0_migration_movement_report.py                 # vs merge-base
    python3 q0_migration_movement_report.py --base <ref>
    python3 q0_migration_movement_report.py --top 40
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import subprocess
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
NUM = re.compile(r"^-?\d*\.?\d+(?:[eE][-+]?\d+)?$")
_FLOOR = 1e-20

# Changing with every run and carrying no mathematical content.
EPHEMERAL = ("computedAt", "durationMs", "commitSha", "scriptCommitSha",
             "scriptHash", "engineVersion", "timestamp", "compute_time_sec",
             "bridge_elapsed_sec", "elapsed")


def _git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                          text=True).stdout


def _numbers(o, out: dict, pre: str = "") -> dict:
    if isinstance(o, dict):
        for k, v in o.items():
            _numbers(v, out, f"{pre}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            _numbers(v, out, f"{pre}[{i}]")
    elif isinstance(o, bool):
        pass
    elif isinstance(o, (int, float)):
        out[pre] = float(o)
    elif isinstance(o, str) and NUM.match(o):
        try:
            out[pre] = float(o)
        except ValueError:
            pass
    return out


def _leaf(path: str) -> str:
    """`.data.rows[3].tr_M_at_q0` -> `tr_M_at_q0` — the QUANTITY, not its slot."""
    return re.sub(r"\[\d+\]", "", path).rsplit(".", 1)[-1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="", help="ref to diff against "
                    "(default: merge-base with origin/main)")
    ap.add_argument("--top", type=int, default=25)
    args = ap.parse_args()

    base = args.base or _git("merge-base", "HEAD", "origin/main").strip()
    if not base:
        raise SystemExit("cannot resolve a base ref; fetch origin first")

    changed = [l for l in _git("diff", "--name-only", base, "--",
                               "computations").splitlines()
               if l.endswith(".witness.json")]
    print("=" * 78)
    print(f" q₀ migration movement — {len(changed)} witness(es) vs {base[:12]}")
    print("=" * 78)
    if not changed:
        print("  nothing changed yet")
        return 0

    by_q: dict[str, list[float]] = defaultdict(list)
    unchanged_files = 0
    for f in changed:
        old_raw = _git("show", f"{base}:{f}")
        cur = ROOT / f
        if not old_raw or not cur.exists():
            continue
        try:
            A = _numbers(json.loads(old_raw), {})
            B = _numbers(json.loads(cur.read_text(encoding="utf-8")), {})
        except Exception:  # noqa: BLE001
            continue
        moved_here = False
        for k, a in A.items():
            if k not in B or any(s in k for s in EPHEMERAL):
                continue
            if abs(a) < _FLOOR or B[k] == a:
                continue
            by_q[_leaf(k)].append(abs(B[k] - a) / abs(a))
            moved_here = True
        if not moved_here:
            unchanged_files += 1

    if not by_q:
        print("  no numeric field moved above the floor "
              f"({unchanged_files} file(s) changed in metadata only)")
        return 0

    rows = sorted(by_q.items(), key=lambda t: -statistics.median(t[1]))
    print(f"\n  {'quantity':<34} {'n':>5}  {'median':>12}  {'max':>12}")
    print(f"  {'-'*34} {'-'*5}  {'-'*12}  {'-'*12}")
    for q, v in rows[:args.top]:
        print(f"  {q[:34]:<34} {len(v):>5}  "
              f"{statistics.median(v)*1e9:>10,.1f}p  {max(v)*1e9:>10,.1f}p")
    if len(rows) > args.top:
        print(f"  … {len(rows)-args.top} more quantities")

    allv = [x for v in by_q.values() for x in v]
    repin = [x for x in allv if 1.0e-8 < x < 1.3e-8]
    big = [x for x in allv if x > 1e-6]
    print(f"\n  fields moved            : {len(allv):,}")
    print(f"  at the re-pin signature : {len(repin):,} "
          f"(~11.5 ppb — expected; its ABSENCE would be the surprise)")
    print(f"  above 1000 ppb          : {len(big):,} "
          f"(amplified, or moved for a non-pin reason — needs a human)")
    print(f"  metadata-only files     : {unchanged_files}")
    print("\n  Units are ppb. 'p' suffix = ppb.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
