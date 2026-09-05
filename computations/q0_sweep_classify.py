#!/usr/bin/env python3
"""q0_sweep_classify.py — classify q0_muon_reproduction_sweep.py log output.

Reads one or more sweep logs (the per-producer lines emitted by
q0_muon_reproduction_sweep.py) and buckets every producer:

  PASS            — reproduced its committed witness at the correct CAL anchor.
  Q0_ANCHOR       — SUBSTANTIVE, and the q₀ VALUE itself flips between the muon
                    and proton signatures (the muon override did not reach this
                    producer's q₀ path — a real anchor residual to follow up).
  PRECISION_PATH  — SUBSTANTIVE, but q₀ is consistent; derived values drift
                    (committed-side rounding / a different precision path), not
                    a q₀ regression.
  RUN_FAILED      — producer errored (non-zero exit).
  TIMEOUT         — exceeded the per-producer timeout.
  NO_WITNESS/NO_COMMITTED — nothing to compare (skipped, not a failure).

Detection of a true q₀-anchor residual is VALUE-based, not field-name based: a
diff whose committed/fresh pair is {muon-sig, proton-sig}. This deliberately does
NOT flag derived quantities merely named `tr_M_q0` / `..._at_q0` (values evaluated
*at* q₀, whose drift is precision-path, not an anchor flip).

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

# Canonical q₀ decimal signatures (CAL two-layer convention). A *true* q₀-anchor
# residual is when the q₀ VALUE itself flips between these two signatures — NOT
# a derived quantity that merely happens to be named `..._q0` / `..._at_q0`.
_MUON_SIG = "1.109978595557"     # ideal / canonical 3-CAL (CAL-2 = P_skew^β)
_PROTON_SIG = "1.10997858275"    # physical-observations (m_p/m_e)


def _is_anchor_flip(a: str, b: str) -> bool:
    return (_MUON_SIG in a and _PROTON_SIG in b) or (_PROTON_SIG in a and _MUON_SIG in b)


def classify(logs: list[str]) -> dict[str, list]:
    buckets: dict[str, list] = defaultdict(list)
    cur = None            # (name, status_text)
    cur_q0 = False
    cur_diffs: list = []

    def flush():
        nonlocal cur, cur_q0, cur_diffs
        if cur is None:
            return
        name, status = cur
        if status.startswith("PASS"):
            buckets["PASS"].append(name)
        elif status.startswith("SUBSTANTIVE"):
            if cur_q0:
                flips = [d for d in cur_diffs if _is_anchor_flip(d[1], d[2])]
                buckets["Q0_ANCHOR"].append((name, (flips or cur_diffs)[:2]))
            else:
                buckets["PRECISION_PATH"].append((name, cur_diffs[:2]))
        elif status.startswith("RUN_FAILED"):
            buckets["RUN_FAILED"].append((name, status[:120]))
        elif status.startswith("TIMEOUT"):
            buckets["TIMEOUT"].append(name)
        elif status.startswith("NO_WITNESS") or status.startswith("NO_COMMITTED"):
            buckets["SKIPPED"].append(name)
        else:
            buckets["OTHER"].append((name, status[:120]))
        cur, cur_q0, cur_diffs = None, False, []

    for path in logs:
        for line in open(path, encoding="utf-8", errors="replace"):
            line = line.rstrip("\n")
            m = _RES.match(line)
            if m:
                flush()
                cur = (m.group(1), m.group(2))
                continue
            d = _DIFF.match(line)
            if d and cur is not None:
                cur_diffs.append((d.group(1), d.group(2), d.group(3)))
                # True q₀-anchor residual: the q₀ VALUE flips muon↔proton (the
                # override did not reach this producer's q₀ path). Value-based, so
                # derived `tr_M_q0` / `..._at_q0` fields are NOT false-flagged.
                if _is_anchor_flip(d.group(2), d.group(3)):
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
