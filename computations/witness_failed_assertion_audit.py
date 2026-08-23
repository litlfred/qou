#!/usr/bin/env python3
"""Witness failed-assertion audit — the mirror of `witness_hollowness_audit`.

`witness_hollowness_audit` catches a witness that claims GREEN with nothing
behind it (`allPassed: true`, `assertions: []`). This one catches the opposite
and, measured, commoner case: a witness that recorded RED and was committed
anyway.

    allPassed: false, and nobody read it.

WHY THIS IS WORTH A GATE
------------------------

A recorded-but-unread failure is strictly WORSE than no check at all, because
the existence of the check is what stops anyone looking. The detector fired,
wrote a correct verdict to disk, and the file was committed with the verdict
inside it.

The motivating case (bean `qou-4e5k`). `tr-m-algebraic-q.witness.json` carried

    allPassed: false
    symbolic_delta_matches_li2q  computed=1.3381598e-06  tol=1e-12  passed=false

from 2026-08-09. That assertion names, precisely and numerically, a real defect:
two definitions of the colour split δ disagreeing by exactly ℏ³. It was
rediscovered twelve days later by hand-measuring a deuteron trace, by an agent
who did not know the repo had already written it down. Nothing between those two
dates consumed the field.

Its sibling assertion is the other half of the lesson and is NOT caught here:
`algebraic_q0_matches_transfer` was *passing* at `6.88e-08` against a
`tolerance=1e-07` whose `source` string explained the residual away as a
"~1e-8 float64-eval floor". It was the same δ defect. Post-fix the value is
`3.50e-15`, so the claimed floor sat ~17 orders above the real one. **A
tolerance chosen to fit an unexplained gap converts a detector into a
rationalisation, and it passes forever.** No mechanical check can see that;
it is named here because this file is where someone will look for it.

WHAT IS A FAILURE, AND WHAT IS NOT
-----------------------------------

Only `allPassed is False`, or an assertion with `passed is False`. A witness
with no `assertions` key uses a different schema and is not flagged; neither is
one whose `allPassed` is absent. Being conservative here matters, because the
third category below is the reason the field became ignorable in the first
place.

Three things a red witness can be, and they need different fixes:

  1. **A real defect.** Fix the producer. (`tr-m-algebraic-q` was this.)
  2. **A tolerance that was always wrong.** Fix the tolerance, and say why in
     the `source` string — never widen it to fit an unexplained residual.
  3. **A probe recording an expected negative.** `allPassed` is the wrong
     mechanism for this: a refuted hypothesis is a successful probe. Such a
     witness should carry its verdict in `data`, not as a failed assertion.

Category 3 is the one to identify FIRST when draining, because every instance
of it teaches readers that a red witness is normal.

RATCHET, NOT A BOOLEAN
----------------------

108 of 2681 live witnesses are red as of 2026-08-21, spread across four months
(NOTE 2026-08-23: `2681` is the whole corpus, which overstates the denominator —
519 of those witnesses carry neither an `assertions` entry nor an `allPassed`
key, so they can never be counted red. The red rate is over the EVALUABLE
subset, not the corpus. The run now prints both numbers; qou-i5jy finding #3.)
(2026-05: 1, 06: 38, 07: 25, 08: 44). A gate that is red on arrival gets
skipped — `precision-gates.sh` says so in its own comments, and that is how a
checker goes quiet. So the backlog is recorded in
`witness-failed-assertion-baseline.json` and tolerated, exactly as the
raw-float64 and padding ratchets tolerate theirs. Under `--strict`:

  * a witness **not** in the baseline that is red fails;
  * a baselined witness whose failed-assertion count **increases** fails.

Counts shrink, never grow. A file that goes green, or disappears, is progress
and is reported as such.

BASELINE GRANULARITY
--------------------

Per-file with a count of failed assertions. Per-assertion-name would churn
whenever a producer renames an assertion, and the quantity that must not grow
is how much recorded failure a given witness carries.

THE FIX IS AT THE PRODUCER, NEVER THE BASELINE
-----------------------------------------------

Do not add a file here to silence it, and do not flip `allPassed` by hand. Fix
the producer, the tolerance, or the schema misuse, and re-run.

Usage:
  python3 computations/witness_failed_assertion_audit.py            # report
  python3 computations/witness_failed_assertion_audit.py --strict   # gate
  python3 computations/witness_failed_assertion_audit.py --list     # full list
  python3 computations/witness_failed_assertion_audit.py --write-baseline
  python3 computations/witness_failed_assertion_audit.py --self-test
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCAN_ROOT = os.path.join(ROOT, "computations")
BASELINE = os.path.join(ROOT, "computations",
                        "witness-failed-assertion-baseline.json")


def _iter_witnesses(scan_root: str):
    for dirpath, dirnames, filenames in os.walk(scan_root):
        dirnames[:] = [d for d in dirnames if d != "_deprecated"]
        for fn in filenames:
            if fn.endswith(".witness.json"):
                yield os.path.join(dirpath, fn)


def failed_assertions(w: dict) -> list[str]:
    """Names of assertions this witness records as failed.

    A witness can be red via `allPassed` with no per-assertion flag (older
    schema), so an empty name list with `allPassed is False` still counts as
    one offence — reported as `<allPassed>`.
    """
    if not isinstance(w, dict):
        return []
    names = [
        str(a.get("name", "<unnamed>"))
        for a in (w.get("assertions") or [])
        if isinstance(a, dict) and a.get("passed") is False
    ]
    if not names and w.get("allPassed") is False:
        return ["<allPassed>"]
    if names and w.get("allPassed") is not False:
        # A per-assertion red with allPassed not set false: still a recorded
        # failure, and the inconsistency is itself worth surfacing.
        return names
    return names


def scan(scan_root: str = SCAN_ROOT,
         coverage_out: dict | None = None) -> dict[str, dict]:
    """Red witnesses. Pass `coverage_out` to also receive the denominator.

    `failed_assertions` is deliberately conservative: a witness carrying neither
    an `assertions` entry nor an `allPassed` key uses a different schema and is
    never flagged (see WHAT IS A FAILURE above). That conservatism is correct —
    but it means the red count has a denominator SMALLER than the corpus, and
    this report printed only the numerator, so a reader had no way to see how
    much of the corpus could be counted red at all.

    Filled in the same walk rather than a second pass: this script is a gate in
    `scripts/precision-gates.sh` and should not double its I/O to report its own
    coverage.
    """
    cov = {"scanned": 0, "unparseable": 0, "no_signal": 0, "evaluable": 0}
    out: dict[str, dict] = {}
    for path in sorted(_iter_witnesses(scan_root)):
        cov["scanned"] += 1
        try:
            with open(path, encoding="utf-8") as fh:
                w = json.load(fh)
        except Exception:
            cov["unparseable"] += 1
            continue
        a = w.get("assertions") if isinstance(w, dict) else None
        if (isinstance(w, dict)
                and not (isinstance(a, list) and a)
                and "allPassed" not in w):
            cov["no_signal"] += 1
        else:
            cov["evaluable"] += 1
        names = failed_assertions(w)
        if names:
            rel = os.path.relpath(path, ROOT)
            out[rel] = {
                "count": len(names),
                "failed": names,
                "computedAt": str(w.get("computedAt", ""))[:10],
            }
    if coverage_out is not None:
        coverage_out.update(cov)
    return out


def _load_baseline() -> dict[str, int]:
    if not os.path.exists(BASELINE):
        return {}
    with open(BASELINE, encoding="utf-8") as fh:
        b = json.load(fh)
    return {k: int(v) for k, v in (b.get("witnesses") or {}).items()}


def _self_test() -> int:
    cases = [
        ({"allPassed": False, "assertions": []}, ["<allPassed>"]),
        ({"allPassed": True, "assertions": []}, []),
        ({"assertions": [{"name": "a", "passed": False}]}, ["a"]),
        ({"allPassed": False,
          "assertions": [{"name": "a", "passed": False},
                         {"name": "b", "passed": True}]}, ["a"]),
        ({"allPassed": True, "assertions": [{"name": "a", "passed": True}]}, []),
        # No assertions key and no allPassed: a different schema, not an offence.
        ({"data": {"x": 1}}, []),
        # allPassed absent but a per-assertion red: still recorded failure.
        ({"assertions": [{"name": "z", "passed": False}]}, ["z"]),
        (["not", "a", "dict"], []),
    ]
    bad = 0
    for i, (w, want) in enumerate(cases):
        got = failed_assertions(w)
        if got != want:
            print(f"  self-test {i}: got {got!r}, want {want!r}")
            bad += 1
    print(f"self-test: {len(cases) - bad}/{len(cases)} passed")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        return _self_test()

    cov: dict = {}
    found = scan(coverage_out=cov)
    total_files = len(found)
    total_asserts = sum(v["count"] for v in found.values())

    if "--write-baseline" in argv:
        payload = {
            "note": (
                "Witnesses committed with a recorded assertion failure. This "
                "baseline DRAINS, never grows: fix the producer, the tolerance, "
                "or the schema misuse (see the module docstring's three "
                "categories) and re-run. Adding a file here to silence it "
                "defeats the mechanism."
            ),
            "count": total_files,
            "witnesses": {k: v["count"] for k, v in sorted(found.items())},
        }
        with open(BASELINE, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, sort_keys=True)
            fh.write("\n")
        print(f"wrote baseline: {total_files} witnesses, "
              f"{total_asserts} failed assertion(s)")
        return 0

    baseline = _load_baseline()
    new, grown, drained = [], [], []
    for rel, info in sorted(found.items()):
        if rel not in baseline:
            new.append((rel, info))
        elif info["count"] > baseline[rel]:
            grown.append((rel, info, baseline[rel]))
    for rel, was in sorted(baseline.items()):
        now = found.get(rel, {}).get("count", 0)
        if now < was:
            drained.append((rel, was, now))

    print(f"witnesses with a recorded assertion failure: {total_files} "
          f"({total_asserts} failed assertion(s))")
    print(f"  denominator: {cov['evaluable']} EVALUABLE of {cov['scanned']} "
          f"scanned")
    if cov["no_signal"]:
        print(f"  NOT EVALUABLE: {cov['no_signal']} witness(es) carry neither an "
              "assertions[] entry\n                 nor an allPassed key, so they "
              "can never be counted red.\n                 A different schema, not "
              "a clean result — see WHAT IS A FAILURE.")
    if cov["unparseable"]:
        print(f"  UNPARSEABLE: {cov['unparseable']} witness(es) skipped")
    print(f"baseline: {len(baseline)} witness(es)")

    if "--list" in argv:
        for rel, info in sorted(found.items(), key=lambda kv: kv[1]["computedAt"]):
            print(f"  {info['computedAt']}  {rel}")
            for n in info["failed"][:4]:
                print(f"              FAILED: {n}")

    if drained:
        print(f"\nDRAINED ({len(drained)}):")
        for rel, was, now in drained:
            print(f"  {rel}: {was} -> {now}")

    if new:
        print(f"\nNEW — not in the baseline ({len(new)}):")
        for rel, info in new:
            print(f"  {rel}  ({info['count']} failed: "
                  f"{', '.join(info['failed'][:3])})")
    if grown:
        print(f"\nGROWN ({len(grown)}):")
        for rel, info, was in grown:
            print(f"  {rel}: {was} -> {info['count']}")

    if "--strict" in argv and (new or grown):
        print("\nRED: a witness may not be committed with a recorded assertion "
              "failure. Fix the producer, the tolerance, or the schema misuse — "
              "do NOT add it to the baseline.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
