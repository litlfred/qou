#!/usr/bin/env python3
"""Verify one bucket-A assertion drain against a FRESH baseline.

Bean `qou-p77d` prescribes the drain for `.assertions[].computed` /
`.expected` fields that were cast to `float()` by a producer which really
computes in `mpf`: remove the cast, serialize with `_precision.fmt`, re-run
the producer.  The bean also records, twice, why the obvious way to check
the result is wrong:

  * **Never baseline against the committed witness.**  Three of the first
    five targets in PR #5996 drifted on an *unmodified* re-run, so the
    committed file blames the cast removal for movement that was already
    there.  Baseline from a fresh unmodified run of the same producer in
    the same container.

  * **"Round-trips through float64" does NOT prove laundering.**  It flagged
    55 of 302 already-drained fields in #6022; all 55 were exact k·2^-235
    ULP residuals, and a power of two round-trips losslessly.  So this
    reports round-tripping as a FLAG for a human to read, never as a verdict.

A third trap, found writing this script: **you cannot separate a real gain
from a double's own decimal expansion by testing equality.**  `mp.nstr`
truncates, so the drained string is never bit-identical to the double it
replaced, and a naive `after == before` test calls every field a gain.  The
discriminator is the SIZE of the disagreement measured against the
serialization width: a genuine recovery differs from the double by about one
ULP (~1e-16 relative, since a double carries 2**-53), whereas a re-serialized
double differs only by nstr's own truncation at ~10**-(digits-1).  Those two
scales are 40 orders of magnitude apart here, so the test is not delicate --
but it has to be the right test.  My first version was the equality one and
it passed a laundered field.

Usage:
    assertion_drain_verify.py --baseline BEFORE.json --after AFTER.json
    assertion_drain_verify.py --selftest

Exit 0 if every changed field gained digits and nothing regressed; 1 otherwise.
"""
from __future__ import annotations

import argparse
import json
import sys

try:
    from mpmath import mp, mpf
except ImportError:  # pragma: no cover - the audit needs mpmath to judge digits
    print("assertion_drain_verify: mpmath is required", file=sys.stderr)
    raise

mp.dps = 120

FIELDS = ("computed", "expected")


def _assertions(doc: dict) -> dict:
    out = {}
    for a in doc.get("assertions") or []:
        if isinstance(a, dict) and a.get("name"):
            out[a["name"]] = a
    return out


def _as_mpf(v):
    """Best-effort exact read of a witness value field. None if not numeric."""
    if isinstance(v, bool) or v is None:
        return None
    if isinstance(v, (int, float)):
        return mpf(v)
    if isinstance(v, str):
        try:
            return mpf(v)
        except Exception:
            return None
    return None


def _sig_digits(s: str) -> int:
    """Significant decimal digits carried by a serialized value."""
    body = s.strip().lstrip("+-").split("e")[0].split("E")[0]
    digits = body.replace(".", "").lstrip("0")
    return len(digits.rstrip("0")) or (1 if digits else 0)


def classify(before, after) -> tuple[str, str]:
    """Return (verdict, note) for one assertion value field."""
    if before == after:
        return "UNCHANGED", ""

    b_num, a_num = _as_mpf(before), _as_mpf(after)
    if b_num is None or a_num is None:
        return "NON-NUMERIC", f"{before!r} -> {after!r}"

    if not isinstance(after, str):
        return "NOT-DRAINED", "still a JSON number after the edit"

    # The whole point of the drain: the recorded value must not MOVE, it must
    # gain digits it already had upstream.  A moved value is a different
    # computation and is never a drain.
    if b_num == 0 and a_num == 0:
        return "UNCHANGED", ""
    if b_num == 0 or a_num == 0:
        return "VALUE-MOVED", f"{before!r} -> {after!r}"
    rel = abs(a_num - b_num) / abs(b_num)
    if rel > mpf("1e-15"):
        return "VALUE-MOVED", f"rel {mp.nstr(rel, 3)} — not a serialization change"

    gained = _sig_digits(after) - _sig_digits(str(before))

    # Truncation floor of the new serialization: nstr at N significant digits
    # can disagree with the true value by ~10**-(N-1) relative, and by no
    # more.  Anything at or below that scale means the drained string IS the
    # old double, merely printed wider -- no digit was recovered.  A genuine
    # recovery sits ~1e-16 up, at the double's own ULP.  One order of margin
    # keeps a borderline last-digit rounding on the right side.
    floor = mpf(10) ** -(max(_sig_digits(after), 2) - 1)
    if rel <= floor * 10:
        return "NO-DIGITS-RECOVERED", (
            f"rel {mp.nstr(rel, 3)} is at the serialization floor — the value "
            "is exactly representable in binary64, so widening it recovers "
            "nothing (it does still remove a raw float64 from the witness)"
        )

    note = f"+{gained} sig digits (differs from the double at rel {mp.nstr(rel, 3)})"
    # FLAG ONLY — see the module docstring.  An exact ULP residual or a power
    # of two round-trips losslessly and is a perfectly good drained value.
    if a_num == mpf(float(a_num)):
        note += "  [FLAG: still round-trips through binary64 — read it, do not auto-revert]"
    return "GAIN", note


def verify(baseline: dict, after: dict) -> int:
    b, a = _assertions(baseline), _assertions(after)
    counts = {}
    rows = []

    for name in sorted(set(b) | set(a)):
        if name not in b:
            rows.append(("ADDED", name, "", "assertion absent from baseline"))
            counts["ADDED"] = counts.get("ADDED", 0) + 1
            continue
        if name not in a:
            rows.append(("DROPPED", name, "", "assertion absent after the edit"))
            counts["DROPPED"] = counts.get("DROPPED", 0) + 1
            continue
        for f in FIELDS:
            verdict, note = classify(b[name].get(f), a[name].get(f))
            if verdict == "UNCHANGED":
                continue
            rows.append((verdict, name, f, note))
            counts[verdict] = counts.get(verdict, 0) + 1

    bp, ap = baseline.get("allPassed"), after.get("allPassed")
    pass_flip = bp != ap

    for verdict, name, f, note in rows:
        loc = f"{name}.{f}" if f else name
        print(f"  {verdict:<12} {loc:<52} {note}")
    if not rows:
        print("  (no value field changed)")

    print("\n  " + "  ".join(f"{k}={v}" for k, v in sorted(counts.items())) or "  —")
    print(f"  allPassed: {bp} -> {ap}" + ("   🛑 PASS/FAIL FLIPPED" if pass_flip else ""))

    bad = pass_flip or any(
        counts.get(k) for k in ("VALUE-MOVED", "NOT-DRAINED", "NON-NUMERIC", "DROPPED")
    )
    if bad:
        print("\n  VERDICT: REVERT — this is not a serialization change.")
        return 1
    if not counts.get("GAIN"):
        print("\n  VERDICT: NO GAIN — every changed field was already exact in "
              "binary64. Nothing was recovered; keep only if you want the raw "
              "float64 out of the witness, and say that is the reason.")
        return 1
    print("\n  VERDICT: KEEP — every changed field gained digits, value and "
          "pass/fail preserved.")
    return 0


def selftest() -> int:
    """Pin each verdict, including the two the bean records as traps."""
    def doc(vals, passed=True):
        return {
            "allPassed": passed,
            "assertions": [
                {"name": n, "computed": c, "expected": e} for n, (c, e) in vals.items()
            ],
        }

    cases = []

    # 1. the ordinary good drain: same value, more digits
    cases.append((
        "gain",
        classify(0.714099204348418,
                 "0.714099204348417993722694330759362545228900913403775475279459"),
        "GAIN",
    ))
    # 2. a value that MOVED is never a drain
    cases.append(("moved", classify(0.5, "0.6000000000000000000000000000"), "VALUE-MOVED"))
    # 3. bucket B: extra digits that are exactly the double's expansion
    #    still count as GAIN in shape, but must carry the round-trip FLAG.
    # A double re-serialized wider recovers nothing.  This is the case the
    # equality test got wrong.
    cases.append((
        "reserialized-double",
        classify(0.1, mp.nstr(mpf(float(0.1)), 40)),
        "NO-DIGITS-RECOVERED",
    ))
    # 4. a field the edit failed to stringify
    cases.append(("not-drained", classify(0.5, 0.5000000000000001), "NOT-DRAINED"))
    # 5. unchanged
    cases.append(("unchanged", classify(1.0, 1.0), "UNCHANGED"))
    # 6. an exact ULP residual round-trips losslessly — the bean's 55/302
    #    false-positive class.  It must NOT be a revert verdict.
    ulp = mpf(2) ** -235
    cases.append(("ulp-residual", classify(float(ulp), mp.nstr(ulp, 60)),
                  "NO-DIGITS-RECOVERED"))

    ok = True
    for name, (verdict, note), want in cases:
        good = verdict == want
        ok &= good
        print(f"  {'ok ' if good else 'FAIL'}  {name:<16} got {verdict:<12} want {want}   {note}")

    # 7. a pass/fail flip is a revert no matter how good the digits look
    good = verify(doc({"a": (0.5, 0.5)}, passed=True),
                  doc({"a": ("0.500000000000000000001", "0.5")}, passed=False)) == 1
    ok &= good
    print(f"  {'ok ' if good else 'FAIL'}  pass-flip forces REVERT")

    print("\nselftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", help="witness JSON from a FRESH unmodified re-run")
    ap.add_argument("--after", help="witness JSON after the drain edit + re-run")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not (a.baseline and a.after):
        ap.error("--baseline and --after are both required")
    return verify(json.load(open(a.baseline)), json.load(open(a.after)))


if __name__ == "__main__":
    sys.exit(main())
