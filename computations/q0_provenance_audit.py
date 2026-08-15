#!/usr/bin/env python3
"""Which substrate anchor did each witness actually use?

AGENTS.md (owner directive, 2026-08-07) requires every new witness to record
its q₀, so a later reader can tell which layer it belongs to without inferring
it from a call site. This measures whether that is happening, and classifies
what was recorded.

It exists because the `tnjb` migration ("move the ~840 muon-q₀ witnesses to
proton") has been discussed as a bulk sweep without anyone measuring its actual
shape. A sweep you cannot count is a sweep you cannot scope.

CLASSIFICATION IS BY PHYSICAL DISTANCE, NOT STRING EQUALITY
-----------------------------------------------------------
An earlier pass of mine classified by exact float match against the f64 pin
literals and put ~350 files in an "other" bucket. That was wrong: most of them
record the muon pin at *higher* precision (a 50-dps string), which is the same
anchor, not a different one. Distance-based bucketing avoids that whole class
of error, and it is also the only framing in which the answer is meaningful —
what matters is which anchor a number sits on, not how many digits were typed.

Buckets, by |q − q_proton| / q_proton:

    proton     < 1 ppb        the production default
    muon      ~11.5 ppb       the ideal-layer CAL-2 proxy
    truncated ~1277 ppb       the 5-significant-digit `1.10998` literal
    other      anything else  neither pin — needs a human look

Usage:
    python3 computations/q0_provenance_audit.py
    python3 computations/q0_provenance_audit.py --list-other
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import sys

Q_PROTON = 1.1099785827513808
Q_MUON = 1.1099785955541805

# Keys that name a substrate anchor. Deliberately narrow: `q` alone is also
# used for unrelated quantities, so a value only counts when it also lands in
# the q₀ neighbourhood (see `classify`).
Q_KEYS = {"q0", "q_0", "q0_value", "q", "substrate_q0", "q0_anchor", "q_parameter"}

# Distance thresholds in ppb from the proton pin.
PROTON_PPB = 1.0
MUON_PPB_LO, MUON_PPB_HI = 5.0, 30.0
TRUNC_PPB_LO, TRUNC_PPB_HI = 1000.0, 1600.0


def classify(value) -> tuple[str, float] | None:
    """Bucket a recorded value, or None if it is not a substrate anchor."""
    try:
        f = float(value)
    except (TypeError, ValueError):
        return None
    # Only values in the q₀ neighbourhood count — this is what keeps a bare
    # `q` key holding an unrelated number out of the census.
    if not (1.05 < f < 1.20):
        return None
    ppb = abs(f - Q_PROTON) / Q_PROTON * 1e9
    if ppb < PROTON_PPB:
        return "proton", ppb
    if MUON_PPB_LO <= ppb <= MUON_PPB_HI:
        return "muon", ppb
    if TRUNC_PPB_LO <= ppb <= TRUNC_PPB_HI:
        return "truncated-5-digit", ppb
    return "other", ppb


def anchors_in(doc) -> list[tuple[str, object, str, float]]:
    """Every substrate anchor recorded anywhere in a witness."""
    found: list[tuple[str, object, str, float]] = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k.lower() in Q_KEYS:
                    hit = classify(v)
                    if hit:
                        found.append((k, v, hit[0], hit[1]))
                walk(v)
        elif isinstance(o, list):
            for i in o:
                walk(i)

    walk(doc)
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--list-other", action="store_true",
                    help="print every file in the 'other' bucket")
    ap.add_argument("--list-truncated", action="store_true",
                    help="print every file on the 5-digit truncated anchor")
    args = ap.parse_args()

    buckets = collections.Counter()
    mixed = []
    per_bucket_files = collections.defaultdict(list)
    total = 0
    unreadable = 0

    for p in sorted(pathlib.Path(args.root).rglob("*.witness.json")):
        if ".git" in str(p):
            continue
        total += 1
        try:
            doc = json.loads(p.read_text())
        except Exception:
            unreadable += 1
            continue
        hits = anchors_in(doc)
        if not hits:
            buckets["NOT RECORDED"] += 1
            continue
        kinds = {h[2] for h in hits}
        for k in kinds:
            buckets[k] += 1
            per_bucket_files[k].append(str(p))
        # A single witness carrying TWO different anchors MAY be the
        # layer-straddle AGENTS.md calls a defect regardless of size. It may
        # equally be correct by construction: a q-sweep or a pin-sensitivity
        # map has to carry both (`mu-p-pin-sensitivity-map` is exactly that).
        # So this is a high-recall CANDIDATE list for agent triage, not a
        # defect list — the tool flags, a human or agent adjudicates.
        if len(kinds) > 1:
            mixed.append((str(p), sorted(kinds)))

    print(f"  witnesses scanned  : {total}")
    if unreadable:
        print(f"  unreadable         : {unreadable}")
    rec = total - buckets["NOT RECORDED"] - unreadable
    print(f"  record an anchor   : {rec}  ({rec / total * 100:.1f}%)")
    print(f"  record NONE        : {buckets['NOT RECORDED']}  "
          f"({buckets['NOT RECORDED'] / total * 100:.1f}%)  "
          f"<- AGENTS.md requires new witnesses to record q0")
    print()
    for name in ("proton", "muon", "truncated-5-digit", "other"):
        if buckets[name]:
            print(f"  {buckets[name]:5d}  {name}")

    if mixed:
        print(f"\n  ** {len(mixed)} witness(es) record MORE THAN ONE anchor "
              f"-- CANDIDATES for a layer straddle, needing triage:")
        print("     (a q-sweep or pin-sensitivity map carries both by design "
              "and is NOT a defect)")
        for path, kinds in mixed[:10]:
            print(f"       {'+'.join(kinds):22s} {path}")

    if args.list_other:
        print("\n  'other' bucket (neither pin):")
        for f in per_bucket_files["other"]:
            print(f"    {f}")
    if args.list_truncated:
        print("\n  5-digit truncated anchor:")
        for f in per_bucket_files["truncated-5-digit"]:
            print(f"    {f}")

    print("\n  Scope note: this measures what each witness RECORDS, which is")
    print("  not the same as what its producer used. A witness in 'NOT")
    print("  RECORDED' may well be on the proton pin -- it simply does not say,")
    print("  which is the reportable defect.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
