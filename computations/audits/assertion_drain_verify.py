#!/usr/bin/env python3
"""Verify one bucket-A assertion drain against a FRESH baseline.

Bean `qou-p77d` prescribes the drain for `.assertions[].computed` /
`.expected` fields that a producer cast to `float()` while really computing
in `mpf`: remove the cast, serialize with `_precision.fmt`, re-run the
producer.  The bean records the methodology twice and no tool implemented
it, so the checks below are that methodology plus the traps met writing it.

Traps the bean already carried:

  * **Never baseline against the committed witness.**  Three of the first
    five targets in PR #5996 drifted on an *unmodified* re-run, so the
    committed file blames the cast removal for movement that was already
    there.  Baseline from a fresh unmodified run in the same container.

  * **"Round-trips through float64" does NOT prove laundering.**  It flagged
    55 of 302 already-drained fields in #6022; all 55 were exact k·2^-235
    ULP residuals, and a power of two round-trips losslessly.

Three more, each found by this script reporting something false first:

  1. **Equality cannot separate a real gain from a double's own decimal
     expansion.**  `mp.nstr` truncates, so a drained string is never
     bit-identical to the double it replaced, and `after == before` calls
     every field a gain.  The first version did that and passed a laundered
     field in its own selftest.

  2. **A JSON float must be read as its `repr`, not as the exact binary
     double.**  Reading it as the double puts every 17-digit field ~1e-17
     from its own drained string — an artifact of the comparison.  That bug
     reported five phantom gains on `he4_sdp_compositional_probe.py`, whose
     values are byte-identical before and after.

  3. **`fmt()` short-circuits a Python `float` to `str()`** (its own
     docstring says so).  So a drain can change the JSON type and nothing
     else.  That is `DRAIN-NO-OP`, and it means the field is float64 *in
     fact* however much dps the producer raises — the raise does not reach
     it.  Such a producer is misfiled as bucket A.

The question that actually decides a gain is therefore not "did the string
change" but **does the drained string carry information binary64 cannot
hold?**  Only then were digits recovered.  This is weaker than, and does not
contradict, the bean's ruling above: an exact ULP residual round-trips
because it IS exact — perfectly honest, and precisely why widening it
recovers nothing.  Laundering is about intent; this is about information.

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
except ImportError:  # pragma: no cover
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
    """Exact read of a witness value field. None if not numeric."""
    if isinstance(v, bool) or v is None:
        return None
    if isinstance(v, int):
        return mpf(v)
    if isinstance(v, float):
        # `repr` is the SHORTEST round-tripping string, i.e. exactly what the
        # witness claims.  Reading it as the exact binary double instead makes
        # every 17-digit field look ~1e-17 from its own drained string.
        return mpf(repr(v))
    if isinstance(v, str):
        try:
            return mpf(v)
        except Exception:
            return None
    return None


def _sig_digits(s: str) -> int:
    body = s.strip().lstrip("+-").split("e")[0].split("E")[0]
    digits = body.replace(".", "").lstrip("0")
    return len(digits.rstrip("0")) or (1 if digits else 0)


def _floor(after: str):
    """nstr's own truncation scale for a string of this width."""
    return mpf(10) ** -(max(_sig_digits(after), 2) - 1)


def _roundtrips(a_num, after: str) -> bool:
    """True if `after` holds no information a binary64 double cannot.

    Compared with a tolerance, not for equality — see trap 1.
    """
    d = mpf(float(a_num))
    if d == 0:
        return a_num == 0
    return abs(a_num - d) / abs(d) <= _floor(after) * 10


def classify(before, after) -> tuple[str, str]:
    """Return (verdict, note) for one assertion value field."""
    if before == after:
        return "UNCHANGED", ""

    b_num, a_num = _as_mpf(before), _as_mpf(after)
    if b_num is None or a_num is None:
        return "NON-NUMERIC", f"{before!r} -> {after!r}"
    if not isinstance(after, str):
        return "NOT-DRAINED", "still a JSON number after the edit"

    if b_num == a_num and _sig_digits(after) <= _sig_digits(str(before)):
        # Two very different things land here and the witness alone cannot
        # separate them, so do not assert the stronger one.
        #
        #   (a) a COMPUTED value that is float64 in fact -- `fmt()` short-
        #       circuited a Python float to `str()` (its docstring says it
        #       does), so the producer's dps raise never reached it and the
        #       producer is misfiled as bucket A;
        #   (b) an AUTHOR-TYPED constant, e.g. `expected=2.358`. Nothing
        #       computed it, nothing is misfiled, and stringifying it is a
        #       small fidelity WIN: the witness then records what the author
        #       wrote instead of the binary64 nearest it (2.35799999...).
        #
        # A short decimal is characteristic of (b) -- a double that came out
        # of real arithmetic almost never prints in 6 digits. Characteristic,
        # not decisive: check the source before acting.
        if _sig_digits(after) <= 6:
            return "LITERAL-ONLY", (
                f"{after!r} — no digits to recover. Reads as an AUTHOR-TYPED "
                "constant, where stringifying is a fidelity fix (the witness "
                "records what was written, not the binary64 nearest it). If "
                "it is in fact computed, the producer is float64 there. The "
                "witness cannot tell — read the source."
            )
        return "DRAIN-NO-OP", (
            "value byte-identical, only the JSON type changed — `fmt()` "
            "short-circuited a Python float to `str()` (see its docstring). "
            "This field is float64 IN FACT whatever dps the producer raises: "
            "the raise does not reach it, so the producer is misfiled as A."
        )

    # A drain recovers digits the value already had; it must never MOVE it.
    if b_num == 0 and a_num == 0:
        return "UNCHANGED", ""
    if b_num == 0 or a_num == 0:
        return "VALUE-MOVED", f"{before!r} -> {after!r}"
    rel = abs(a_num - b_num) / abs(b_num)
    if rel > mpf("1e-15"):
        return "VALUE-MOVED", f"rel {mp.nstr(rel, 3)} — not a serialization change"

    if _roundtrips(a_num, after):
        if rel <= _floor(after) * 100:
            why = ("exactly representable in binary64 — the extra digits are "
                   "true but carry nothing new")
        else:
            why = ("the extra digits are the BINARY64 EXPANSION of the "
                   "recorded value, not measured digits — do not present them "
                   "as precision (AGENTS.md: never report a float64 agreement "
                   "to N digits)")
        return "NO-DIGITS-RECOVERED", why

    gained = _sig_digits(after) - _sig_digits(str(before))
    off = abs(a_num - mpf(float(a_num))) / abs(a_num)
    return "GAIN", (f"+{gained} sig digits; differs from its own binary64 "
                    f"rounding at rel {mp.nstr(off, 3)}")


def verify(baseline: dict, after: dict) -> int:
    b, a = _assertions(baseline), _assertions(after)
    counts: dict[str, int] = {}
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
        print(f"  {verdict:<20} {loc:<50} {note}")
    if not rows:
        print("  (no value field changed)")

    print("\n  " + "  ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print(f"  allPassed: {bp} -> {ap}" + ("   PASS/FAIL FLIPPED" if pass_flip else ""))

    if pass_flip or any(counts.get(k) for k in
                        ("VALUE-MOVED", "NOT-DRAINED", "NON-NUMERIC", "DROPPED")):
        print("\n  VERDICT: REVERT — this is not a serialization change.")
        return 1
    if counts.get("LITERAL-ONLY") and not counts.get("GAIN") \
            and not counts.get("DRAIN-NO-OP"):
        print("\n  VERDICT: REVIEW — nothing was recovered, and the changed "
              "fields read as author-typed constants. Keeping is defensible as "
              "a fidelity fix; say that is the reason. Check the source.")
        return 2
    if counts.get("DRAIN-NO-OP") and not counts.get("GAIN"):
        print("\n  VERDICT: REVERT — the edit changed the JSON type and nothing "
              "else. These fields are float64 in fact; the producer is MISFILED "
              "as bucket A. Fix upstream or reclassify — do not stringify.")
        return 1
    if not counts.get("GAIN"):
        print("\n  VERDICT: NO GAIN — nothing was recovered. Keep only if you "
              "want the raw float64 out of the witness, and say that is why.")
        return 1
    print("\n  VERDICT: KEEP — every changed field gained digits, value and "
          "pass/fail preserved.")
    return 0


def selftest() -> int:
    """Pin every verdict, including the three traps in the module docstring."""
    def doc(vals, passed=True):
        return {"allPassed": passed,
                "assertions": [{"name": n, "computed": c, "expected": e}
                               for n, (c, e) in vals.items()]}

    ulp = mpf(2) ** -235
    cases = [
        # the ordinary good drain: same value, real digits beyond binary64
        ("gain", classify(
            0.714099204348418,
            "0.714099204348417993722694330759362545228900913403775475279459"),
         "GAIN"),
        # a value that MOVED is never a drain
        ("moved", classify(0.5, "0.6000000000000000000000000000"), "VALUE-MOVED"),
        # trap 1: a double's own expansion, printed wider, is not a gain.
        # The mix below is the FIXTURE, not a leak: without constructing a
        # binary64 value and re-serializing it, the selftest cannot prove the
        # classifier separates a real gain from a widened double.
        # float64-intentional: builds the defect this case exists to catch
        ("reserialized-double", classify(0.1, mp.nstr(mpf(float(0.1)), 40)),
         "NO-DIGITS-RECOVERED"),
        # a field the edit failed to stringify
        ("not-drained", classify(0.5, 0.5000000000000001), "NOT-DRAINED"),
        ("unchanged", classify(1.0, 1.0), "UNCHANGED"),
        # trap 3: fmt() short-circuited a Python float (he4_sdp_compositional)
        ("fmt-short-circuit", classify(13.19687380754797, "13.19687380754797"),
         "DRAIN-NO-OP"),
        # the bean's 55/302 class: exact, honest, and recovers nothing
        ("ulp-residual", classify(float(ulp), mp.nstr(ulp, 60)),
         "NO-DIGITS-RECOVERED"),
        # an author-typed reference constant must NOT be reported as evidence
        # that the producer is misfiled -- the witness cannot know that
        ("author-typed-literal", classify(2.358, "2.358"), "LITERAL-ONLY"),
    ]

    ok = True
    for name, (verdict, note), want in cases:
        good = verdict == want
        ok &= good
        print(f"  {'ok  ' if good else 'FAIL'}  {name:<20} got {verdict:<20} want {want}")

    # a pass/fail flip is a revert however good the digits look
    good = verify(doc({"a": (0.5, 0.5)}, True),
                  doc({"a": ("0.500000000000000000001", "0.5")}, False)) == 1
    ok &= good
    print(f"  {'ok  ' if good else 'FAIL'}  pass-flip forces REVERT")

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
