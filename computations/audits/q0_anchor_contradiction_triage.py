#!/usr/bin/env python3
# polynomial_q_not_applicable: validator, not a q-series compute.
"""Triage the witnesses that DECLARE `q0Anchor: proton` and carry a
non-proton q0-shaped value -- the `qou-bdkx` contradictory class -- and split
the false positives out of it before anyone acts on the count.

WHY THIS EXISTS. `witness_constant_staleness.py` answers "does this witness
embed a q0-shaped value that is not the current pin?". That is the right
question for a staleness gate and the WRONG question for a triage queue: a
witness can embed such a value for at least four reasons, only one of which
is a defect. Measured over the tree (2026-08-23), acting on the raw count
would have meant chasing 28 non-problems out of 49.

    21  REAL         a pin-like field carries a genuinely different value
    15  named        `q0_muon_pin`, `stale_muon_pin_q0`, `per_anchor.muon.q`,
                     `q0_anchor_note` -- deliberate and self-describing
     9  derived      matches the basin regex but is not a pin at all. The
                     clearest is an LP DUAL COORDINATE,
                     `.data.sigma_f_chain[17].dual.y_star[121] =
                     1.109940825176`, which differs from the proton pin in
                     the FIFTH decimal -- a coincidental hit on
                     `1\\.1099\\d{6,}`, not an anchor.
      3  short       a correct proton pin serialized with fewer digits
      1  rounded     a correct proton pin rounded up at its last place

SCOPE NOTE. The `short` and `rounded` classes are the fixed-width comparator
bug that PR #5578 fixes at source. This module deliberately does NOT
re-implement the comparison -- it imports `Q0_SHAPE`, `AUDIT_SUFFIXES` and
`derived_output_exempt` from the detector, so when that fix lands those two
classes disappear here with no edit. A triage tool that re-implements the
predicate it triages measures itself.

The (a)/(b) rubric is `qou-bdkx`'s and the split needs the PRODUCER, not the
witness:

    (a) declaration right, payload stale  -> re-run the producer at the
                                             declared pin
    (b) payload right, declaration wrong  -> fix the declaration, at the
                                             producer, and re-run

so each REAL row is annotated with `q0_producer_pin_classifier.classify`'s
verdict on its producer. A producer that resolves `muon` while its witness
declares `proton` is (b): the computation is muon, the label is a lie, and
correcting the label moves no number. That is NOT the `qou-1c4y` migration --
it is the prerequisite for the migration to be measurable at all.

Usage:
    python3 q0_anchor_contradiction_triage.py            # summary + REAL list
    python3 q0_anchor_contradiction_triage.py --all      # every class
    python3 q0_anchor_contradiction_triage.py --json     # machine-readable
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE = HERE.parent
REPO = COMPUTE.parent
for p in (str(HERE), str(COMPUTE), str(COMPUTE / "substrate")):
    if p not in sys.path:
        sys.path.insert(0, p)

import witness_constant_staleness as G  # noqa: E402
from q0_producer_pin_classifier import classify, find_producer  # noqa: E402

SKIP_PARTS = (".git", ".claude", "_deprecated", "node_modules")

# A field whose NAME says it holds a muon or comparison value is not a
# contradiction -- it is the producer documenting itself.
NAMED = re.compile(
    r"muon|stale|cross_anchor|per_anchor|anchor_note|\.pins?\.|comparison", re.I)

# A field that plausibly records THE pin. Anything else carrying a
# basin-shaped number is a derived output that happens to look like one.
PINLIKE = re.compile(
    r"(^|\.)(q0|q_0|q0Value|q_0_50dps|q0_50dps|q_0_at_50dps|q_\d+dps)(\[|$|\.)"
    r"|(^|\.)(parameters|constants|inputs|substrate)\.[^.]*q[_0]", re.I)


def basin_paths(node, path: str = ""):
    """(json_path, basin_prefix) for every q0-shaped number or string."""
    if isinstance(node, dict):
        for k, v in node.items():
            yield from basin_paths(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from basin_paths(v, f"{path}[{i}]")
    else:
        s = repr(node) if isinstance(node, (int, float)) else (
            node if isinstance(node, str) else None)
        if s:
            m = G.Q0_SHAPE.search(s)
            if m:
                yield path, m.group(0)[:14]


def same_pin_written_short(value: str, canonical: str) -> str | None:
    """Is `value` the canonical pin, merely written with fewer digits?"""
    if canonical.startswith(value):
        return "short-serialization"
    frac = value.split(".")
    if len(frac) != 2:
        return None
    n = len(frac[1])
    rounded = Decimal(canonical).quantize(
        Decimal(1).scaleb(-n), rounding=ROUND_HALF_UP)
    return "rounded-proton" if str(rounded) == value else None


def triage() -> list[dict]:
    canonical = G.Q_50_DIGIT_STR
    cur = canonical[:14]
    rows: list[dict] = []
    for wf in sorted(REPO.rglob("*.witness.json")):
        if any(p in SKIP_PARTS for p in wf.parts):
            continue
        if wf.name.endswith(G.AUDIT_SUFFIXES):
            continue
        try:
            raw = wf.read_text(encoding="utf-8")
            doc = json.loads(raw)
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(doc, dict) or doc.get("q0Anchor") != "proton":
            continue
        vals = {m.group(0)[:14] for m in G.Q0_SHAPE.finditer(raw)}
        if not any(v != cur for v in vals):
            continue
        if G.derived_output_exempt(raw, 12, cur):
            continue

        flagged = [(p, v) for p, v in basin_paths(doc) if v != cur]
        kinds = []
        for path, value in flagged:
            short = same_pin_written_short(value, canonical)
            if short:
                kinds.append(short)
            elif NAMED.search(path):
                kinds.append("named-muon-or-comparison")
            elif not PINLIKE.search(path):
                kinds.append("derived-output")
            else:
                kinds.append("REAL")
        # A witness is a false positive only if EVERY flagged field is one.
        cls = "REAL" if "REAL" in kinds else (
            sorted(set(kinds))[0] if kinds else "no-scalar-field")

        script = doc.get("scriptFile") or doc.get("script") or doc.get("producer")
        producer, verdict = None, "(no producer field)"
        if script:
            producer = find_producer(Path(str(script)).name)
            if producer is None:
                verdict = "(producer not on disk)"
            else:
                try:
                    verdict, _ev = classify(producer)
                except Exception as exc:  # noqa: BLE001
                    verdict = f"(classify failed: {exc})"
        rows.append({
            "witness": str(wf.relative_to(REPO)),
            "class": cls,
            "fields": flagged[:6],
            "producer": str(producer.relative_to(REPO)) if producer else script,
            "producer_pin": verdict,
        })
    return rows


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--all", action="store_true", help="list every class")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    rows = triage()
    if args.json:
        json.dump({"total": len(rows), "rows": rows}, sys.stdout, indent=1)
        return 0

    by_class = collections.Counter(r["class"] for r in rows)
    print("=" * 72)
    print("q0Anchor=proton witnesses carrying a non-proton q0-shaped value")
    print("=" * 72)
    print(f"  flagged by the staleness predicate : {len(rows)}")
    for k, n in by_class.most_common():
        print(f"  {n:5d}  {k}")
    real = [r for r in rows if r["class"] == "REAL"]
    print(f"\n  FALSE POSITIVES: {len(rows) - len(real)} of {len(rows)}"
          f"  ({(len(rows) - len(real)) * 100 // max(len(rows), 1)}%)")

    by_pin = collections.Counter(r["producer_pin"] for r in real)
    print("\n  REAL, by what the PRODUCER actually pins:")
    for k, n in by_pin.most_common():
        note = ""
        if k == "muon":
            note = "  -> (b) declaration wrong; fix the label, moves no number"
        elif k == "proton":
            note = "  -> (a) payload stale; re-run at the declared pin"
        elif k == "BOTH":
            note = "  -> read it: a comparison producer may be correct"
        print(f"    {n:3d}  {k}{note}")

    show = rows if args.all else real
    print()
    for r in sorted(show, key=lambda r: (r["class"], r["witness"])):
        tag = "" if args.all is False else f"[{r['class']}] "
        print(f"  {tag}{r['witness']}")
        print(f"      producer {r['producer']} -> {r['producer_pin']}")
        for path, value in r["fields"][:3]:
            print(f"      {path} = {value}")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
