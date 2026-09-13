#!/usr/bin/env python3
"""A witness that STAMPS the anchor and COMPUTES at something else.

Bean `qou-q0rf`. Every existing q0 gate checks the *declaration*:
`q0_anchor_consistency_audit` verifies the label maps to a real pin and that
`q0Value` carries that pin's digits; `q0_anchor_ratchet` verifies the stamp is
present at all; `q0_value_drift_audit` verifies the stamped value has not gone
stale. All three read the STAMP.

None of them reads what the producer actually used.

MEASURED, not hypothetical. `computations/hecke/hecke-division.witness.json`
declared `q0Anchor: proton` and the full 50-digit
`q0Value = 1.1099785827513808075916690956107688798744991218736`, and every one
of its numbers was computed at `q_val = 1.110` -- a bare float literal, five
sites, four of them default arguments. 19.3 ppm from the anchor it claimed, and
green on all three gates above, because the stamp was right. The computation
was not.

METHOD. For each witness carrying a `q0Value`, read `parameters.<k>` for the
first `k` the producer exposes and compare relatively. That is the whole check:
the producer has already told us both numbers, and nobody was comparing them.

TOLERANCE, and why it is 1e-10 rather than exact. Measured over the corpus:
4 witnesses disagree at all, and they separate by four orders of magnitude.

    1.93e-5    hecke-division            q = 1.11          <- the defect
    1.24e-12   low-isotope-binding-model-comparison        \\
    1.24e-12   binding-sym-vs-lin-two-models                > q0 = 1.10997858275
    1.24e-12   binding-recurrence-spectral-bridge          /

The three at 1.24e-12 are one thing: the anchor written to ELEVEN digits, a
display rounding rather than a different q. A gate that fires on those trains
its reader to skim, which `scripts/precision-gates.sh`'s own header warns is
how a gate stops being read. 1e-10 sits two orders above the truncation band
and five below the real defect, so it is not a number chosen to make today
green -- there is nothing in between to choose it against.

BLOCKS AT ZERO, no baseline. After the hecke-division fix the corpus is clean at
this tolerance, so there is no backlog to tolerate and no state in which a
finding should be recorded rather than repaired -- the same standing as the
python compile gate rather than the ratchets around it.

COVERAGE, stated so it is not mistaken for completeness: 1560 witnesses carry a
`q0Value`, and 522 of them (33 %) also expose a q parameter this can read. The
other 1038 tell us what they stamped and not what they used, and are outside
what any static check can see. This gate is a floor, not a proof.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

# The names producers actually use, by frequency over the corpus:
# q_0 (275), q0 (187), q (37), Q_0 (21), q0_value (2). Ordered so the most
# specific spelling wins when a producer exposes more than one.
Q_KEYS = ("q_0", "q0", "q", "Q_0", "Q0", "q_val", "q_value", "qval", "q0_value")

# See the module docstring: two orders above the 11-digit display band, five
# below the one real defect, and nothing in between.
TOL = mp.mpf("1e-10")


def _q_of(params: dict):
    """-> (key, mpf) for the first q-like parameter, or None."""
    if not isinstance(params, dict):
        return None
    for k in Q_KEYS:
        if k not in params:
            continue
        v = params[k]
        if isinstance(v, bool) or not isinstance(v, (int, float, str)):
            continue
        try:
            q = mp.mpf(str(v))
        except (ValueError, TypeError):
            continue
        if q == 0:
            continue
        return k, q
    return None


def scan_witness(doc: dict):
    """-> (key, stamped, used, relative) when they disagree, else None."""
    if not isinstance(doc, dict):
        return None
    stamped_raw = doc.get("q0Value")
    if stamped_raw is None:
        return None
    try:
        stamped = mp.mpf(str(stamped_raw))
    except (ValueError, TypeError):
        return None
    if stamped == 0:
        return None
    got = _q_of(doc.get("parameters"))
    if got is None:
        return None
    key, used = got
    rel = abs(used - stamped) / abs(stamped)
    return (key, stamped, used, rel) if rel > TOL else None


def _tracked() -> list[str]:
    out = subprocess.run(["git", "ls-files", "*.witness.json"], cwd=ROOT,
                         capture_output=True, text=True).stdout.split()
    return [f for f in out if "_deprecated" not in f.split("/")]


def _selftest() -> int:
    Q = "1.1099785827513808075916690956107688798744991218736"
    cases = [
        ({"q0Value": Q, "parameters": {"q": 1.11}}, True,
         "the type case: stamps the anchor, computed at a round 1.110 "
         "(19.3 ppm) -- hecke-division, measured"),
        ({"q0Value": Q, "parameters": {"q0": "1.10997858275"}}, False,
         "11-digit display rounding at 1.24e-12 is NOT a different q; three "
         "witnesses do this and firing on them would train the reader to skim"),
        ({"q0Value": Q, "parameters": {"q_0": Q}}, False,
         "stamp and parameter agree exactly"),
        ({"q0Value": Q}, False,
         "no parameters block -- unknowable, not a finding"),
        ({"parameters": {"q": 1.11}}, False,
         "no stamp to compare against"),
        ({"q0Value": Q, "parameters": {"q": "not-a-number"}}, False,
         "unparseable parameter is skipped, not guessed at"),
        ({"q0Value": Q, "parameters": {"q": 0}}, False,
         "a zero q is a sentinel, not a 100% disagreement"),
        ({"q0Value": Q, "parameters": {"dps": 50, "q_0": 1.11}}, True,
         "...and it finds the q key past an unrelated one"),
    ]
    bad = 0
    for doc, want, why in cases:
        got = scan_witness(doc) is not None
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} want={str(want):5} got={str(got):5}  {why}")
    print(f"\nselftest: {len(cases) - bad}/{len(cases)} passed")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", "--selftest", action="store_true",
                    dest="selftest")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on any disagreement (blocks at ZERO)")
    a = ap.parse_args(argv)
    if a.selftest:
        return _selftest()

    mp.mp.dps = 60
    findings, scanned, stamped, comparable = [], 0, 0, 0
    for f in _tracked():
        try:
            doc = json.loads((ROOT / f).read_text(encoding="utf-8"))
        except Exception:                                  # noqa: BLE001
            continue
        if not isinstance(doc, dict):
            continue
        scanned += 1
        if doc.get("q0Value") is None:
            continue
        stamped += 1
        if _q_of(doc.get("parameters")) is not None:
            comparable += 1
        hit = scan_witness(doc)
        if hit:
            findings.append((f, *hit))

    print("=" * 78)
    print("witness STAMPING the anchor and COMPUTING at something else")
    print("=" * 78)
    print(f"  witnesses scanned           : {scanned}")
    print(f"  ...carrying a q0Value stamp : {stamped}")
    print(f"  ...also exposing a q param  : {comparable}  <- what this can check")
    print(f"  DISAGREEMENTS (> {mp.nstr(TOL, 2)})      : {len(findings)}")

    for f, key, st, used, rel in sorted(findings, key=lambda r: -r[4]):
        print(f"\n  {f}")
        print(f"      stamped q0Value      : {mp.nstr(st, 25)}")
        print(f"      parameters.{key:<10s}: {mp.nstr(used, 25)}")
        print(f"      relative disagreement: {mp.nstr(rel, 4)}")

    if findings:
        print("\n  The STAMP is not the defect -- it is very likely correct, which is")
        print("  why the other q0 gates pass. Fix the PRODUCER to compute at the")
        print("  anchor it declares, then re-run it. Do NOT edit the witness, and")
        print("  do NOT relax the stamp to match a value the producer should not")
        print("  have used.")
    else:
        print("\n  Every comparable witness computed at the anchor it stamped.")

    return 1 if (findings and a.strict) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
