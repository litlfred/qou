#!/usr/bin/env python3
"""A witness that asserts NOTHING and reports `allPassed: true`.

Bean `qou-srvu`. Surfaced while draining `qou-3e5m`, and the drain is one of
the things that produces it: honestly removing a self-comparison that could
never fail can leave a witness with no assertions at all, and nothing noticed.

## What this catches, and what it deliberately does not

The defect is **claiming green while asserting nothing**, not "having no
assertions". Those are different, and conflating them inflates the number by
~2.8x:

    assertions: []          + allPassed: true    -> VACUOUS-GREEN   (defect)
    no `assertions` key     + allPassed: true    -> VACUOUS-GREEN   (defect)
    no `assertions` key     + no `allPassed`     -> SILENT          (fine)
    assertions: [...]                            -> ASSERTS         (fine)

A SILENT witness is a pure data emitter. It makes no claim, so there is
nothing to be wrong about, and 756 of them on `main` are exactly that. A
VACUOUS-GREEN one is indistinguishable from a passing witness to every
consumer that reads `allPassed` — "all zero of them passed" is vacuously true
and operationally misleading.

## This is NOT the first detector on this defect — read `qou-vfy1` first

`scripts/check-computation-status.py` already classifies exactly this shape and
calls it **vacuous**: `allPassed: true` over an empty assertions array, where
`all([]) is True` means the witness reports everything passed having tested
nothing. Bean `qou-vfy1`, measured 2026-08-22: of 221 content blocks marked
`status: "verified"`, **43 were vacuous**. It has a `--strict-unbacked` flag.

**The obvious fix is already settled and WITHDRAWN, so do not re-propose it.**
Making `WitnessBuilder` emit `allPassed: null` for an empty assertion list was
investigated under `qou-vfy1` and rejected on measurement: about a dozen
producers hand-roll `return 0 if wit["allPassed"] else 1`, and `None` is falsy,
so the change turns a silent false positive into a loud false negative. That
checker therefore reads `len(assertions)` directly and needs no schema change.

## What THIS audit adds, and it is a different population

`check-computation-status.py` walks content blocks and only sees a witness that
some block CITES while claiming `verified` — the consequential subset, and the
right one to gate on. It cannot see a vacuous witness that no block cites, or
one cited by a block with any other status.

    qou-vfy1  : 43 vacuous, of 221 `verified` BLOCKS       (consequential)
    qou-srvu  : 420 vacuous, of 3280 WITNESSES on main     (superset)

This audit is the wider hygiene net over the superset, and it ratchets — the
count may fall, never rise — which the block-level checker does not do. Use
`check-computation-status.py --strict-unbacked` to gate what a paper CLAIMS;
use this to stop the population growing.

## Why the assertion-level detector cannot see this

`self_fulfilling_assertion_audit.py` scans `add_assertion` CALL SITES. A
producer that never calls it has no site to scan, so the limiting case of an
assertion that cannot fail — no assertion at all — is invisible to the tool
built for exactly that defect. Same shape as taxonomy row 22: a detector that
keys on a construct's presence is blind to its absence.

## Ratchet, not a sweep

420 live instances is not a thing to fix in one pass, and some are legitimate
(a probe whose honest state is "I measured X and have nothing falsifiable to
say about it" — see `casimir_q_factorial_probe`, whose only assertion was
removed *because* asserting it would have encoded an open conjecture). So this
is a ratchet against a committed baseline: the count may fall, never rise.
Draining an entry means either giving the witness a real assertion or, where
it genuinely has nothing to assert, dropping its `allPassed` claim.

Usage:
    python3 computations/audits/vacuous_green_witness_audit.py
    python3 computations/audits/vacuous_green_witness_audit.py --selftest
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # computations/
BASELINE = Path(__file__).resolve().parent / "vacuous-green-baseline.json"

ASSERTS, VACUOUS_GREEN, SILENT = "ASSERTS", "VACUOUS-GREEN", "SILENT"


def classify(doc) -> str:
    """Classify one parsed witness document.

    Split out so the selftest can exercise it directly on dicts, without
    inventing a file layout that the real corpus does not have.
    """
    if not isinstance(doc, dict):
        return SILENT
    has_key = "assertions" in doc
    n = len(doc.get("assertions") or []) if has_key else 0
    if has_key and n > 0:
        return ASSERTS
    # asserts nothing. The claim is what decides it.
    return VACUOUS_GREEN if doc.get("allPassed") is True else SILENT


def scan(root: Path = ROOT):
    counts = {ASSERTS: 0, VACUOUS_GREEN: 0, SILENT: 0}
    live, deprecated = [], []
    for p in sorted(root.rglob("*.witness.json")):
        try:
            doc = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        verdict = classify(doc)
        counts[verdict] += 1
        if verdict == VACUOUS_GREEN:
            rel = p.relative_to(root.parent).as_posix()
            (deprecated if "_deprecated/" in rel else live).append(rel)
    return counts, live, deprecated


def _selftest() -> int:
    """Fixtures pin the NARROWING, not only the matching.

    Row 22 of the detector-blindness taxonomy is this exact failure: a
    selftest built from the same assumption as the code tests the
    assumption's consequences, never the assumption. The assumption most
    likely to be wrong here is that "no assertions" is one state. It is two,
    and the no-key/empty-list pair below is what pins that. Cases 3 and 4
    are the ones a same-author fixture would omit.
    """
    cases = [
        ("has assertions",            {"assertions": [{"name": "x"}], "allPassed": True},  ASSERTS),
        ("empty list, claims green",  {"assertions": [], "allPassed": True},               VACUOUS_GREEN),
        ("NO KEY, claims green",      {"allPassed": True},                                 VACUOUS_GREEN),
        ("NO KEY, claims nothing",    {"data": {"x": 1}},                                  SILENT),
        ("empty list, claims nothing",{"assertions": []},                                  SILENT),
        ("empty list, claims red",    {"assertions": [], "allPassed": False},              SILENT),
        # allPassed must be the literal True, not merely truthy: a witness
        # carrying a string or 1 is not making the same claim, and treating
        # it as one would over-report.
        ("allPassed is a string",     {"assertions": [], "allPassed": "true"},             SILENT),
        ("not a dict",                ["assertions"],                                      SILENT),
    ]
    bad = 0
    for label, doc, want in cases:
        got = classify(doc)
        ok = got == want
        bad += (not ok)
        print(f"  {'ok  ' if ok else 'FAIL'}  {label:28s} -> {got}")
    print("selftest:", "PASS" if not bad else f"FAIL ({bad})")
    return 1 if bad else 0


def main() -> int:
    if "--selftest" in sys.argv:
        return _selftest()

    counts, live, deprecated = scan()
    base = json.loads(BASELINE.read_text(encoding="utf-8")) if BASELINE.exists() else {"live": []}
    baseline = set(base.get("live", []))
    new = [f for f in live if f not in baseline]
    drained = [f for f in baseline if f not in set(live)]

    total = sum(counts.values())
    print("=" * 72)
    print(" VACUOUS-GREEN WITNESS AUDIT (bean qou-srvu)")
    print("=" * 72)
    print(f"  witnesses scanned            : {total}")
    print(f"    ASSERTS (has assertions)   : {counts[ASSERTS]}")
    print(f"    SILENT  (claims nothing)   : {counts[SILENT]}   [not a defect]")
    print(f"    VACUOUS-GREEN              : {counts[VACUOUS_GREEN]}")
    print(f"      under _deprecated/       : {len(deprecated)}")
    print(f"      LIVE                     : {len(live)}")
    print()
    print(f"  baseline                     : {len(baseline)}")
    print(f"  NEW (not in baseline)        : {len(new)}")
    print(f"  drained since baseline       : {len(drained)}")
    for f in new[:20]:
        print(f"      NEW  {f}")
    if len(new) > 20:
        print(f"      ... and {len(new) - 20} more")
    print()
    print("  A VACUOUS-GREEN witness reports `allPassed: true` while making no")
    print("  falsifiable claim. Drain one by giving it a real assertion, or --")
    print("  where it genuinely has nothing to assert -- by dropping the")
    print("  `allPassed` claim rather than inventing an assertion to justify it.")
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main())
