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

A SECOND WAY A PASSING ASSERTION LIES: IT WENT STALE
-----------------------------------------------------

Also not caught here, also placed here because this is where someone will
look. The mechanism above is a *fitted tolerance*. This one needs no bad
tolerance at all — the assertion was correct when written and rotted in place.

**A stored assertion is evaluated when the producer RUNS and then frozen into
the file. It certifies the run that wrote it, never the file you are reading.**
If its reference moves afterwards, the recorded `computed` does not, and the
witness keeps reporting `passed: true` with a number that is now wrong.

Measured instance (2026-08-24, bean `qou-nmza`).
`averaged-block-swap-binding.witness.json` carried

    id_trace_matches_binding_canonical  computed≈0  tolerance=1e-9  passed=true

from 2026-06-11. Its `data.atom_traces.id` was `0.055358425349822354`. The
`binding-canonical.witness.json` it names as its reference was recomputed
2026-08-22 under convention D and reads `0.16097414544240738…`. So the
assertion had been advertising agreement at 1e-9 while the two disagreed by
**rel 0.6561 — 65.6 %** — for two and a half months. After re-running the
producer the same assertion holds at rel 2.96e-31.

Why the existing gates do not see it: this witness is not red (`allPassed`
is `true`), so *this* audit skips it; its producer's `scriptHash` had not
drifted, so the self-staleness check skips it; and `scriptCommitSha` drift is
deliberately ignored corpus-wide (rebase-merge makes it stale-on-arrival). The
staleness is in a DIFFERENT witness that this one merely reads.

Practical rules:

  * **Never read a passing assertion in a committed witness as evidence that
    the value is current.** It is evidence about a past run. Only re-running
    the producer, or an upstream-hash check, can tell you about the file.
  * An assertion that names another witness as its reference is a
    cross-witness dependency. `add_upstream` / `upstream_witness_hashes`
    records it — prefer that to an assertion whose `source` string mentions
    the upstream in prose, because only the recorded hash can be checked
    without a re-run.
  * When an upstream is recomputed under a new convention, its consumers do
    not merely go stale — they can go stale *while still claiming to agree
    with it*, which is worse than a plain stale number.

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


def scan(scan_root: str = SCAN_ROOT) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for path in sorted(_iter_witnesses(scan_root)):
        try:
            with open(path, encoding="utf-8") as fh:
                w = json.load(fh)
        except Exception:
            continue
        names = failed_assertions(w)
        if names:
            rel = os.path.relpath(path, ROOT)
            out[rel] = {
                "count": len(names),
                "failed": names,
                "computedAt": str(w.get("computedAt", ""))[:10],
            }
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

    found = scan()
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
