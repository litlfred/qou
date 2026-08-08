#!/usr/bin/env python3
"""witness_raw_float64_audit.py — raw float64 in committed witnesses.

WHAT THIS GATES, AND WHY IT IS NOT THE PADDING AUDIT
----------------------------------------------------

AGENTS.md states the rule broadly: *"NO-FLOAT64 means none may enter a
witness."*  `witness_float64_padding_audit.py` does not enforce that rule.
It enforces a narrower and different one: **fake precision** — a float64
serialized past ~17 digits so that binary-expansion garbage reads as exact.

A witness that stores float64 *at float64 width* is honest about being f64
and sails through the padding audit. It still violates the stated rule.

That gap is not hypothetical. `jpsi-boundstate-mass.witness.json` reached
`main` carrying **30 raw float64 fields** with the padding audit green
(13/13, NEW 0) — the merge's other gates (content validation, Lean,
reproducibility) do not look at precision at all. Two of those fields were
not merely imprecise but wrong about what they were: a Chern-Simons value
that is exactly `-1/12` was stored as `-0.08333333333333312`, and one that
is exactly `0` (the braid is amphichiral — a structural fact) was stored as
`8.324194211187791e-16`, indistinguishable from a noise floor.

WHAT THIS DOES — AND DELIBERATELY DOES NOT DO
----------------------------------------------

It does **not** drain anything. Draining raw float64 at the producer is
PR #4677's work: an entry tracer that patches mpmath's `from_float` to read
entry lines directly, which localized the residual to three library-level
source lines rather than eighteen independent bugs.

This is the **ratchet** that stops the class growing while that drain runs.
The existing backlog is large — 1586 of 2404 live witnesses, 542,034 fields
— so it is recorded in `raw-float64-baseline.json` and tolerated, exactly as
the padding audit tolerates its own backlog. Under `--strict`:

  * a witness **not** in the baseline that carries raw float64 fails —
    this is the case that would have caught the J/psi probe;
  * a baselined witness whose count **increases** fails.

Counts can shrink, never grow. A file that drains to zero, or disappears,
is progress and is reported as such.

BASELINE GRANULARITY
--------------------

Per-FILE with a count, not per-field. Per-field would mean a 542,034-key
baseline — unreviewable, and it would churn on every legitimate re-run
since field paths move. Per-file counts are compact, and they carry the
ratchet just as well: the quantity that must not grow is how much float64
a given witness carries.

THE FIX IS AT THE PRODUCER, NEVER THE WITNESS
----------------------------------------------

Do not hand-edit a number, and do not add a file to the baseline to silence
it. Carry the value as `mpmath.mpf` from its source and serialize it with
`_precision.fmt`; see `jpsi_boundstate_mass_probe.py` for a worked
conversion, including the case where a library (SnapPy) has its own
precision ceiling that must be recorded rather than assumed.

Output: `witness-raw-float64-audit.witness.json`.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BASELINE = HERE / "raw-float64-baseline.json"

# These audits embed findings — including float values — in their own
# witnesses, so scanning them re-detects the audit's own output every run.
# Same exclusion the padding audit makes, for the same reason.
SELF_OUTPUTS = {
    "witness-raw-float64-audit.witness.json",
    "witness-float64-padding-audit.witness.json",
    "q0-value-drift-audit.witness.json",
    "no-free-parameter-certificate.witness.json",
}


def count_raw_floats(obj) -> int:
    """Number of JSON numbers parsed as float (i.e. non-integer literals).

    JSON integers arrive as Python `int`, so this counts exactly the
    values written with a decimal point or an exponent — the float64
    payload. `bool` is a subclass of `int` and so is never counted.
    """
    if isinstance(obj, dict):
        return sum(count_raw_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_raw_floats(v) for v in obj)
    return 1 if isinstance(obj, float) else 0


def scan() -> dict[str, int]:
    """{repo-relative path: raw float64 count} for every live witness."""
    found: dict[str, int] = {}
    for p in sorted(HERE.rglob("*.witness.json")):
        if p.name in SELF_OUTPUTS or "_deprecated" in p.parts:
            continue
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        n = count_raw_floats(d)
        if n:
            found[p.relative_to(ROOT).as_posix()] = n
    return found


def self_test() -> int:
    """Prove the detector fires, and does not fire on the exempt shapes.

    Asserted rather than assumed: a gate that cannot be shown to FAIL on a
    violation is indistinguishable from a no-op.
    """
    cases = [
        # (payload, expected raw-float64 count)
        ({"v": 1.5}, 1),                                  # plain float
        ({"v": 128.04411076744893}, 1),                   # the J/psi shape
        ({"v": 8.324194211187791e-16}, 1),                # exponent form
        ({"v": 1.0}, 1),                                  # integral-valued float
        ({"v": -0.08333333333333312}, 1),                 # negative
        ({"v": "1.5"}, 0),                                # string — the fix
        ({"v": 3}, 0),                                    # int
        ({"v": True}, 0),                                 # bool is not a float
        ({"v": None}, 0),
        ({"a": [1.5, 2.5], "b": {"c": 3.5}}, 3),          # nested
        ({"a": ["1.5", {"c": "3.5"}]}, 0),                # nested, serialized
        ({}, 0),
    ]
    bad = [(p, e, count_raw_floats(p)) for p, e in cases
           if count_raw_floats(p) != e]
    if bad:
        print("SELF-TEST FAILED:")
        for p, e, g in bad:
            print(f"   {p}  expected {e}, got {g}")
        return 1
    print(f"SELF-TEST PASSED — {len(cases)} cases: raw float64 detected in "
          "plain/exponent/nested/negative form; strings, ints and bools not "
          "flagged.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on a NEW dirty witness or an INCREASED count")
    ap.add_argument("--rebaseline", action="store_true",
                    help="regenerate the baseline (draining only — totals must go DOWN)")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    found = scan()
    prior: dict[str, int] = {}
    if BASELINE.exists():
        prior = json.loads(BASELINE.read_text())["files"]

    new_files = {f: n for f, n in found.items() if f not in prior}
    grew = {f: (prior[f], n) for f, n in found.items()
            if f in prior and n > prior[f]}
    drained = {f: (prior[f], found.get(f, 0)) for f in prior
               if found.get(f, 0) < prior[f]}

    total = sum(found.values())
    base_total = sum(prior.values()) if prior else 0

    print("=" * 74)
    print("RAW-FLOAT64 AUDIT — float64 that entered a witness at all")
    print("=" * 74)
    print(f"  witnesses carrying raw float64 : {len(found)}")
    print(f"  total raw float64 fields       : {total:,}")
    if prior:
        print(f"  baseline files / fields        : {len(prior)} / {base_total:,}")
        print(f"  drained since baseline         : {len(drained)} file(s), "
              f"{base_total - total:+,} field(s)")
    print(f"  NEW dirty witnesses            : {len(new_files)}")
    print(f"  REGRESSED (count increased)    : {len(grew)}")

    if new_files:
        print("\n  NEW witnesses carrying raw float64 — fix AT THE PRODUCER")
        print("  (carry mpmath.mpf from the source, serialize with _precision.fmt),")
        print("  then re-run it. Do NOT add the file to the baseline to silence this.")
        for f, n in sorted(new_files.items(), key=lambda kv: -kv[1])[:25]:
            print(f"    {n:6d}  {f}")
        if len(new_files) > 25:
            print(f"    ... and {len(new_files) - 25} more")

    if grew:
        print("\n  REGRESSED — these witnesses gained raw float64:")
        for f, (was, now) in sorted(grew.items(), key=lambda kv: kv[1][0] - kv[1][1])[:25]:
            print(f"    {was:6d} -> {now:<6d}  {f}")

    if drained:
        print(f"\n  Drained (progress): {len(drained)} file(s)")
        for f, (was, now) in sorted(drained.items(),
                                    key=lambda kv: kv[1][1] - kv[1][0])[:10]:
            print(f"    {was:6d} -> {now:<6d}  {f}")

    if args.rebaseline:
        BASELINE.write_text(json.dumps(
            {"note": "Witnesses known to carry raw float64, by count. The "
                     "backlog is tolerated; it must only SHRINK. Regenerate "
                     "ONLY when draining. Adding a file here to silence a "
                     "failure defeats the gate — fix at the producer instead.",
             "enforced_rule": "AGENTS.md: NO-FLOAT64 means none may enter a witness.",
             "drain_owner": "PR #4677 (float64 residual, producer-side)",
             "files_count": len(found),
             "fields_count": total,
             "files": dict(sorted(found.items()))}, indent=2) + "\n")
        print(f"\nRebaselined: {len(found)} files / {total:,} fields recorded.")

    out = HERE / "witness-raw-float64-audit.witness.json"
    out.write_text(json.dumps({
        "schema": "witness/v1",
        "name": "witness-raw-float64-audit",
        "description": "Witnesses carrying raw float64 JSON numbers. Enforces "
                       "the stated NO-FLOAT64 rule, which the padding audit "
                       "does not: that gate catches only FAKE precision "
                       "(float64 padded past ~17 digits), so honest float64 "
                       "passes it. Ratchet only — draining is PR #4677.",
        "data": {
            "dirty_witnesses": len(found),
            "total_fields": total,
            "baseline_files": len(prior),
            "baseline_fields": base_total,
            "new_not_baselined": len(new_files),
            "regressed": len(grew),
            "drained_files": len(drained),
        },
    }, indent=2) + "\n")
    print(f"\nWrote {out.name}")
    return 1 if (args.strict and (new_files or grew)) else 0


if __name__ == "__main__":
    sys.exit(main())
