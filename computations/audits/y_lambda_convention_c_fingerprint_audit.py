#!/usr/bin/env python3
# polynomial_q_not_applicable: convention-frame audit over committed witnesses.
"""Find witnesses whose payload is convention-C-frame, by the ANSWER not the source.

Convention D (`z = q³/(q²+1)`, canonical since the 2026-08-15 owner ruling;
cascade landed 2026-08-09) collapses the Wenzl bridge to `X = q⁴ = Q²` exactly
— the integral Wenzl level `r = 2`, whose row cap is `ℓ(λ) ≤ 2`. So under D:

    y_λ  is EXACTLY 0  for every partition with three or more rows.

Under C, `X` was not a power of `Q` (1.7202517512 at q₀ against Q² =
1.5179532498) and `y_(1³) ≠ 0`. That asymmetry is a complete convention test
that needs no source, no `z` grep, and no anchor:

    a NONZERO y_λ on a ≥3-row partition is impossible under D.

This is the counter-move AGENTS.md prescribes for exactly this problem — every
source-level detector keys on how the convention was *written*, and the
detector-blindness taxonomy already catalogues thirteen spellings that evade
that. The algebraic form of the *result* keys on what it is. A value cannot be
stale, mislabelled, re-spelled, or inherited from a stale record and still
carry a nonzero y_λ on a 4-row partition under D.

WHAT A HIT IS AND IS NOT
    A hit says the witness's PAYLOAD is C-frame. It does NOT say the producer
    is: the producer may have been migrated while the witness was never
    recomputed (that is the common case — see su4_1111_markov_trace_probe,
    whose producer crashes, so no one COULD have recomputed it). Re-run the
    producer to tell the two apart. A producer that still emits the fingerprint
    is a live source defect and a much stronger finding than a stale witness.

    A NON-hit is not a clean bill: a witness with only ≤2-row partitions is
    silent under this test, because C and D agree there.

THE LIMIT OF THIS TOOL — it keys on a FIELD NAME, which is the very trap the
docstring above congratulates itself for avoiding one level up. The row-cap
argument is sound for the WENZL y_λ; this scan finds any field *named*
`y_lambda` / `y` sitting beside a partition. AGENTS.md is explicit that the
three partition-weight families `y_λ` / `w_λ` / `w̃_λ` are DISTINCT at q ≠ 1
and must never be conflated, so a hit on a field that is not the Wenzl y_λ is
a false positive this cannot rule out by itself.

    Confirmed by hand so far: su4-1111-markov-trace (traced to
    y_lambda_wenzl_bridge_numeric, the change reproduced by re-running).
    The other files are CANDIDATES — resolve each by checking which weight
    its producer computes before calling it a convention defect.

So treat the count as an upper bound on C-frame witnesses and a lower bound on
nothing. It is a triage list, not a verdict.

Usage:  python3 computations/audits/y_lambda_convention_c_fingerprint_audit.py [--json OUT]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

Y_KEYS = {"y_lambda", "ylambda", "y_lam", "y"}
LAMBDA_KEYS = {"lambda", "lam", "partition", "shape"}
MIN_ROWS = 3          # C and D agree at <= 2 rows, so those are silent
PARTITION_TEXT = re.compile(r"[\[\(\s\d,\]\)]+")


def rows_of(value) -> int | None:
    """Row count of a partition written as a list or as its repr, else None."""
    if isinstance(value, list) and value and all(isinstance(x, int) for x in value):
        return len(value)
    if isinstance(value, str) and PARTITION_TEXT.fullmatch(value):
        return len(re.findall(r"\d+", value))
    return None


def is_nonzero(value) -> bool:
    try:
        return float(str(value)) != 0.0
    except (TypeError, ValueError):
        return False


def scan_payload(obj) -> list[tuple]:
    """Every (partition, y) pair in this payload that D forbids."""
    hits: list[tuple] = []

    def walk(node):
        if isinstance(node, dict):
            y_key = next((k for k in node if k.lower() in Y_KEYS), None)
            lam_key = next((k for k in node if k.lower() in LAMBDA_KEYS), None)
            if y_key and lam_key:
                rows = rows_of(node[lam_key])
                if rows is not None and rows >= MIN_ROWS and is_nonzero(node[y_key]):
                    hits.append((node[lam_key], node[y_key]))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(obj)
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="repo root to scan")
    ap.add_argument("--json", help="write the full report here")
    ap.add_argument("--include-deprecated", action="store_true")
    args = ap.parse_args()

    root = pathlib.Path(args.root)
    report, scanned, deprecated = {}, 0, 0
    for path in sorted(root.rglob("computations/**/*.witness.json")):
        try:
            payload = json.loads(path.read_text())
        except Exception:
            continue
        scanned += 1
        hits = scan_payload(payload)
        if not hits:
            continue
        rel = str(path.relative_to(root))
        if "_deprecated" in rel and not args.include_deprecated:
            deprecated += 1
            continue
        report[rel] = {
            "computedAt": payload.get("computedAt") or payload.get("timestamp"),
            "n_fields": len(hits),
            "sample": [[lam, str(y)[:40]] for lam, y in hits[:3]],
        }

    total = sum(v["n_fields"] for v in report.values())
    print("=" * 74)
    print("CONVENTION-C FINGERPRINT — nonzero y_lambda on a >=3-row partition")
    print("=" * 74)
    print(f"  witnesses scanned          : {scanned}")
    print(f"  live files with fingerprint: {len(report)}")
    print(f"  fields                     : {total}")
    if deprecated:
        print(f"  (+ {deprecated} under _deprecated, excluded; --include-deprecated to show)")
    print()
    for rel, info in sorted(report.items()):
        print(f"  {info['n_fields']:4d}  {rel}")
        print(f"        computedAt: {info['computedAt']}")
        for lam, y in info["sample"][:2]:
            print(f"        lambda={lam}  y={y}")
    if report:
        print("\n  A hit is about the WITNESS, not the producer. Re-run the producer to")
        print("  tell a stale payload from a live source defect; the latter is worse.")
    if args.json:
        pathlib.Path(args.json).write_text(json.dumps(report, indent=2) + "\n")
        print(f"\n  wrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
