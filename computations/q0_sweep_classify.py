#!/usr/bin/env python3
"""q0_sweep_classify.py — classify q0_muon_reproduction_sweep.py log output.

Reads one or more sweep logs (the per-producer lines emitted by
q0_muon_reproduction_sweep.py) and buckets every producer:

  PASS            — reproduced its committed witness at the correct CAL anchor.
  Q0_ANCHOR       — SUBSTANTIVE, and a `q0`/`q_0` field itself differs between
                    committed and fresh (the muon override did not reach this
                    producer's q0 — a real anchor residual to follow up).
  PRECISION_PATH  — SUBSTANTIVE, but no q0-field mismatch; derived values drift
                    (committed-side rounding / a different precision path), not
                    a q0 regression.
  RUN_FAILED      — producer errored (non-zero exit).
  TIMEOUT         — exceeded the per-producer timeout.
  NO_WITNESS/NO_COMMITTED — nothing to compare (skipped, not a failure).

Usage:  python3 q0_sweep_classify.py <sweep.log> [more.log ...]
Prints a summary table + the member lists; exit 0 always (reporting tool).
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict

# a diff detail line looks like:  "      <path>: committed=<..> fresh=<..>"
_DIFF = re.compile(r"^\s+(\S+): committed=(.*?) fresh=(.*)$")
# a result line looks like: "✓ name.py: PASS [muon]"  /  "✗ name.py: SUBSTANTIVE [muon best] (5)"
_RES = re.compile(r"^[✓✗–]\s+(\S+\.py): (.*)$")


def classify(logs: list[str]) -> dict[str, list]:
    buckets: dict[str, list] = defaultdict(list)
    cur = None            # (name, status_text)
    cur_is_sub = False
    cur_q0 = False
    cur_diffs: list = []

    def flush():
        nonlocal cur, cur_is_sub, cur_q0, cur_diffs
        if cur is None:
            return
        name, status = cur
        if status.startswith("PASS"):
            buckets["PASS"].append(name)
        elif status.startswith("SUBSTANTIVE"):
            buckets["Q0_ANCHOR" if cur_q0 else "PRECISION_PATH"].append((name, cur_diffs[:3]))
        elif status.startswith("RUN_FAILED"):
            buckets["RUN_FAILED"].append((name, status[:120]))
        elif status.startswith("TIMEOUT"):
            buckets["TIMEOUT"].append(name)
        elif status.startswith("NO_WITNESS") or status.startswith("NO_COMMITTED"):
            buckets["SKIPPED"].append(name)
        else:
            buckets["OTHER"].append((name, status[:120]))
        cur, cur_is_sub, cur_q0, cur_diffs = None, False, False, []

    for path in logs:
        for line in open(path, encoding="utf-8", errors="replace"):
            line = line.rstrip("\n")
            m = _RES.match(line)
            if m:
                flush()
                cur = (m.group(1), m.group(2))
                cur_is_sub = m.group(2).startswith("SUBSTANTIVE")
                continue
            d = _DIFF.match(line)
            if d and cur is not None:
                field = d.group(1).rsplit(".", 1)[-1].lower()
                cur_diffs.append((d.group(1), d.group(2), d.group(3)))
                if field in ("q0", "q_0", "q") or field.endswith("q0"):
                    cur_q0 = True
    flush()
    return buckets


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 0
    b = classify(sys.argv[1:])
    order = ["PASS", "PRECISION_PATH", "Q0_ANCHOR", "RUN_FAILED", "TIMEOUT", "SKIPPED", "OTHER"]
    total = sum(len(b[k]) for k in order)
    print(f"=== q0 sweep classification ({total} producers) ===")
    for k in order:
        print(f"  {k:16s} {len(b[k])}")
    for k in ("Q0_ANCHOR", "PRECISION_PATH", "RUN_FAILED", "TIMEOUT", "OTHER"):
        if not b[k]:
            continue
        print(f"\n--- {k} ---")
        for item in b[k]:
            if isinstance(item, tuple):
                name, extra = item
                print(f"  {name}")
                if k in ("Q0_ANCHOR", "PRECISION_PATH"):
                    for pth, a, c in extra:
                        print(f"      {pth}: committed={a[:28]} fresh={c[:28]}")
                else:
                    print(f"      {extra}")
            else:
                print(f"  {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
