#!/usr/bin/env python3
"""witness_prose_drift_audit.py — a witness whose PROSE quotes a number its own
DATA does not contain.

Bean `qou-n62l`. Every staleness mechanism here compares a witness against its
PRODUCER — `scriptHash`, `q0Anchor`, the raw-float64 ratchet, the dps floor.
None of them reads a `description`. So a description that hardcodes a finding
keeps asserting it after the data moves underneath, and the witness ends up
contradicting itself in a single file, green the whole time.

MEASURED, not hypothetical. `rho-binding-constancy.witness.json` said

    "the ratio varies ~182% (D 5.73, T 81.5, ³He 37.4)"

while carrying D 3.87 / T 36.99 / ³He 19.12 — and after regeneration under the
corrected atom word (bean qou-hu1f) 14.64 / 291.0 / 131.7. The prose matched
NEITHER the committed data nor the fresh data: it had been stale across at
least two regenerations. Same file also claimed "the D ratio 5.728 reproduces
the published α_M 5.729 (cross-validates the pipeline)", a CLAIM that had
silently stopped holding.

Checking the other witnesses regenerated in that pass found two more, and one
that looked stale and was not:

    delta-lambda-qdim-route-probe          0.41, 5.62, 82.9   worst 33 %
    delta-lambda-cancellation-ascaling     0.28, 1.27, 1.31   worst  8 %
    delta-lambda-l1-ceiling-sign-prune     0.59 vs 0.5661     4 %  ROUNDING

That last one is why this reports distance rather than a boolean: a naive
"is the string present" test flags an honest 3-significant-figure rounding as
loudly as a 49 % contradiction.

METHOD. For each witness with a `description`, pull every decimal number out of
the prose and every number out of the rest of the document, then bucket each
prose number by its distance to the NEAREST data value:

    EXACT      the digits appear verbatim in the data
    ROUNDING   rel < 5e-3   — a quoted 3-4 sig-fig form of a value present
    NEAR       rel < 5e-2   — plausible rounding, or a small genuine drift
    DRIFT      5e-2 .. 0.6  — REPORTED: close enough that it looks like it
                              should match, far enough that it does not
    UNRELATED  rel > 0.6    — a different quantity: an external constant, a
                              tolerance, a count. Not reported.

The upper edge is set FROM the measured cases, not guessed: the three known
drifts sit at 0.058, 0.069, 0.079, 0.33 and 0.55. Everything the first run put
above 0.6 saturated at the cap and ranked identically, which is the signature
of an unrelated quantity rather than a drifted copy.

The band is bounded on BOTH sides deliberately. Ranking by raw relative
distance flags a prose tolerance of `9.0e-18` beside data of order 1e-2 at
5e15 and buries every real finding underneath it. The three measured cases all
land inside: 5.73-vs-3.87 is 0.33, 81.5-vs-36.99 is 0.55, 82.9-vs-55.4 is 0.33.

A decimal point is REQUIRED, which drops years, PR numbers (#1105), bean ids
and issue numbers without needing a list of them. Percent forms are matched
against both `x` and `x/100`, because prose says "~189.6 %" where the data
carries `1.89576`.

⚠ FAR IS A CANDIDATE, NOT A VERDICT. A description may legitimately quote a
number that is not in its own data: a published constant, an AME value, a
figure from a cited bean. `rho-binding`'s own "α_M 5.729" is exactly that — an
external reference — sitting right beside "5.728", a stale claim about a
computed quantity. No static rule separates those two; a reader must. This
audit narrows 4-figure haystacks to a handful of lines to read.

VALIDATED against the four cases whose status was already known:

    delta-lambda-qdim-route-probe          FLAGGED 0.41, 5.62   (known stale)
    delta-lambda-cancellation-ascaling     FLAGGED 0.28, 1.27, 1.31  (known stale)
    delta-lambda-l1-ceiling-sign-prune     clean               (known ROUNDING)
    rho-binding-constancy                  FLAGGED 5.728, 5.729

The last is the limitation demonstrating itself, and is worth reading. That
description was FIXED to interpolate its numbers, and none of its live figures
(189.6, 14.64, 291.0, 131.7) is flagged. What is flagged is the sentence
withdrawing the old claim — "used to claim 'the D ratio 5.728 reproduces the
published α_M 5.729', which no longer holds". Those digits are quoted history
and an external constant, correctly absent from the data. The audit cannot tell
a withdrawn number from a live one, and should not pretend to.

SCOPE. A DETECTOR. The durable fix is not to correct the numbers, which only
resets the clock — it is to make the prose DERIVE them.
`rho_binding_constancy_probe.py` now interpolates its description from the
computed ratios, so it cannot go stale again; that is the pattern.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

import mpmath as mp                                        # noqa: E402
from _precision import fmt, set_compute_dps                # noqa: E402

set_compute_dps()

SKIP_DIRS = ("_deprecated", "__pycache__", "node_modules", ".git")
NUM = re.compile(r"-?\d+\.\d+(?:[eE][-+]?\d+)?")
ROUNDING_REL = 5e-3
NEAR_REL = 5e-2
# Above this the prose number is almost certainly a DIFFERENT quantity -- an
# external constant, a tolerance, a count -- not a drifted copy of a data
# value. Ranking by raw relative distance without this cap is useless: a prose
# tolerance of 9.0e-18 beside data of order 1e-2 scores 5e15 and buries every
# real finding. The interesting band is bounded on BOTH sides.
UNRELATED_REL = 0.6


def _numbers_in(obj, out=None):
    """Every number anywhere in a JSON document, including numeric strings."""
    out = [] if out is None else out
    if isinstance(obj, bool):
        return out
    if isinstance(obj, (int, float)):
        out.append(float(obj))
    elif isinstance(obj, str):
        for m in NUM.findall(obj):
            try:
                out.append(float(m))
            except ValueError:
                pass
    elif isinstance(obj, dict):
        for v in obj.values():
            _numbers_in(v, out)
    elif isinstance(obj, list):
        for v in obj:
            _numbers_in(v, out)
    return out


def _nearest_rel_mp(raw: str, vals: list[float]):
    """Nearest relative distance, in mpf, from the prose number's own digits.

    The bucketing above runs in float because the band edges (5e-3, 5e-2, 0.6)
    sit nowhere near float64 resolution, so triage is unaffected. The value
    RECORDED is another matter: the raw-float64 gate is right that a float64
    quotient discards digits the source decimal strings actually carried, and a
    witness is not the place to do that (NO-FLOAT64). `mp.mpf(raw)` reads the
    prose digits exactly; `repr` is the shortest round-tripping form of a float
    that arrived as a JSON number, the same conversion `codata_constants`
    uses.
    """
    x = mp.mpf(raw)
    if x == 0:
        return None
    best = None
    for v in vals:
        if v == 0.0:
            continue
        mv = mp.mpf(repr(v))
        for cand in (x, x / 100):
            d = abs(mv - cand) / abs(cand)
            if best is None or d < best:
                best = d
    return None if best is None else fmt(best)


def classify(prose_num: float, raw: str, data_vals: list[float], body: str) -> str:
    if raw in body:
        return "EXACT"
    # A ZERO is never a drifted copy of a nonzero result, but witnesses are full
    # of zero counts and flags -- and |0 - x| / |x| is EXACTLY 1.0 for every x,
    # so leaving zeros in makes every prose number in every such witness score
    # 1.0 and saturates the ranking. 225 "candidates" collapsed to a handful
    # once they were dropped.
    data_vals = [v for v in data_vals if v != 0.0]
    if not data_vals:
        return "NO-DATA"
    best = None
    # try the plain value and the percent form: prose says "189.6 %" where the
    # data carries 1.89576
    for cand in (prose_num, prose_num / 100.0):
        for v in data_vals:
            d = abs(v - cand) / max(abs(cand), 1e-300)
            if best is None or d < best:
                best = d
    if best < ROUNDING_REL:
        return "ROUNDING"
    if best < NEAR_REL:
        return "NEAR"
    if best <= UNRELATED_REL:
        return "DRIFT"
    return "UNRELATED"


def scan_witness(doc: dict):
    """-> (findings, reason_skipped). findings = [(raw, bucket, nearest_rel)]"""
    desc = doc.get("description") or doc.get("data", {}).get("description")
    if not isinstance(desc, str) or not desc.strip():
        return [], "no-description"
    rest = {k: v for k, v in doc.items() if k != "description"}
    body = json.dumps(rest)
    vals = _numbers_in(rest)
    out = []
    for raw in dict.fromkeys(NUM.findall(desc)):     # de-dup, keep order
        try:
            x = float(raw)
        except ValueError:
            continue
        b = classify(x, raw, vals, body)
        if b == "DRIFT":
            out.append((raw, b, _nearest_rel_mp(raw, vals)))
    return out, None


BASELINE = HERE / "witness-prose-drift-baseline.json"


def _load_baseline() -> dict:
    if BASELINE.exists():
        try:
            return json.loads(BASELINE.read_text())["files"]
        except Exception:                              # noqa: BLE001
            return {}
    return {}


def _ratchet(current: dict, strict: bool, rebaseline: bool) -> int:
    """Tolerate the committed backlog, block anything NEW.

    The pattern the gates array already uses (`q0_anchor_ratchet`,
    `never_raises_dps_audit`): blocking is only safe because the gate is GREEN
    at its own baseline, so it can fire on a regression and never on the
    backlog it inherited.

    DO NOT add a file to the baseline to silence a failure. A finding here is a
    name that is not defined; the fix is to define it, or to find out where the
    definition went.
    """
    prior = _load_baseline()
    new_files = sorted(set(current) - set(prior))
    grew = sorted(f for f in current if f in prior and current[f] > prior[f])
    drained = sorted(set(prior) - set(current))
    print(f"\n  baseline files              : {len(prior)}")
    print(f"  drained since baseline      : {len(drained)}")
    print(f"  NEW (not baselined)         : {len(new_files)}")
    print(f"  GREW above baseline         : {len(grew)}")
    for f in new_files:
        print(f"      NEW   {f}  ({current[f]})")
    for f in grew:
        print(f"      GREW  {f}  {prior[f]} -> {current[f]}")
    if rebaseline:
        # Bootstrap: with no baseline on disk every file reads as NEW, so the
        # draining-only guard would refuse to create the very first one.
        if BASELINE.exists() and (new_files or grew):
            print("\n  REFUSED to rebaseline: counts went UP. Rebaselining is for "
                  "DRAINING only -- fix the finding instead of recording it.")
            return 1
        BASELINE.write_text(json.dumps(
            {"files": current, "total": sum(current.values())},
            indent=1, sort_keys=True) + "\n")
        print(f"\n  Rebaselined: {len(current)} file(s), "
              f"{sum(current.values())} finding(s).")
        return 0
    if strict and (new_files or grew):
        return 1
    return 0


def _selftest() -> int:
    cases = [
        ({"description": "the ratio is 5.73", "r": "3.8677"}, ["5.73"],
         "the type case: prose number far from the data it sits beside"),
        ({"description": "the ratio is 3.8677", "r": "3.8677"}, [],
         "EXACT — digits present verbatim"),
        ({"description": "the ratio is 0.59", "r": "0.5661373968"}, [],
         "ROUNDING at 4% is NOT drift — the calibrated false positive"),
        ({"description": "spread ~189.6%", "relative_spread": "1.89576"}, [],
         "PERCENT FORM: prose says 189.6%, data carries 1.89576"),
        ({"description": "see PR #1105 from 2026-08-19", "x": "1.0"}, [],
         "a decimal point is required, so PR ids and dates never enter"),
        ({"description": "tolerance 1e-9 held", "x": "1.0"}, [],
         "no decimal point in 1e-9 either — not a candidate"),
        ({"description": "value 2.2245662", "x": 2.2245662}, [],
         "matches a numeric (non-string) data value"),
        ({"description": "nothing numeric here", "x": "1.0"}, [],
         "no numbers in prose"),
        ({"description": "value 7.5", "note": "no numbers at all"}, [],
         "witness carries no data numbers -> NO-DATA, not a finding"),
        ({"description": "value 7.5", "count": 0, "flag": 0.0}, [],
         "ZEROS DROPPED: |0-x|/|x| is exactly 1.0 for every x, which would "
         "otherwise flag every prose number in every witness holding a zero"),
    ]
    bad = 0
    for doc, want, why in cases:
        got = [r for r, _, _ in scan_witness(doc)[0]]
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} want={want!s:10} got={got!s:10}  {why}")
    print(f"\nselftest: {len(cases) - bad}/{len(cases)} passed")
    return 1 if bad else 0


def _tracked_witnesses() -> list[str]:
    out = subprocess.run(["git", "ls-files", "*.witness.json"], cwd=ROOT,
                         capture_output=True, text=True).stdout.split()
    return [f for f in out if not any(d in f.split("/") for d in SKIP_DIRS)]


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    # BOTH spellings. `scripts/precision-gates.sh` invokes
    # `python3 <script> --self-test` (hyphenated) and treats a non-zero exit as
    # "a detector that cannot be shown to fire is a no-op" -- so a script
    # offering only `--selftest` fails its gate on arrival, silently, for a
    # reason that has nothing to do with what it detects. Found by running the
    # harness rather than by reading the array.
    ap.add_argument("--self-test", "--selftest", action="store_true",
                    dest="selftest")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-witness", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on a NEW candidate, or a baselined witness "
                         "whose count grew (the gates-array ratchet contract)")
    ap.add_argument("--rebaseline", action="store_true",
                    help="regenerate the baseline (DRAINING only)")
    ap.add_argument("--top", type=int, default=25)
    a = ap.parse_args(argv)
    if a.selftest:
        return _selftest()

    files = _tracked_witnesses()
    findings, no_desc, unparsed = [], 0, 0
    for f in files:
        try:
            doc = json.loads((ROOT / f).read_text(encoding="utf-8"))
        except Exception:                          # noqa: BLE001
            unparsed += 1
            continue
        if not isinstance(doc, dict):
            unparsed += 1
            continue
        hits, why = scan_witness(doc)
        if why == "no-description":
            no_desc += 1
            continue
        for raw, bucket, rel in hits:
            findings.append({"witness": f, "prose_number": raw,
                             "nearest_relative_distance": rel})

    by_file: dict[str, list] = {}
    for x in findings:
        by_file.setdefault(x["witness"], []).append(x)
    # Rank by HOW MANY prose numbers in one description drift, then by
    # distance. A single stray number is usually an external citation; three or
    # four in one sentence is a finding that was written once and never updated,
    # which is the shape this audit exists to catch.
    def _worst(xs):
        vals = [mp.mpf(y["nearest_relative_distance"]) for y in xs
                if y["nearest_relative_distance"] is not None]
        return max(vals) if vals else mp.mpf(0)

    ranked = sorted(by_file.items(), key=lambda kv: (-len(kv[1]), -_worst(kv[1])))

    if a.json:
        print(json.dumps({"findings": findings, "scanned": len(files),
                          "no_description": no_desc, "unparsed": unparsed},
                         indent=2, default=str))
        return 1 if findings else 0

    print("=" * 78)
    print("witness PROSE quoting a number its own DATA does not contain")
    print("=" * 78)
    print(f"  witnesses scanned           : {len(files)}")
    print(f"  without a description       : {no_desc}")
    print(f"  unparsed                    : {unparsed}")
    print(f"  witnesses with candidates   : {len(by_file)}")
    print(f"  candidate numbers           : {len(findings)}")
    print(f"\n  worst {min(a.top, len(ranked))} by distance"
          f"  (DRIFT is a CANDIDATE, not a verdict — prose may cite an")
    print("   external constant that is legitimately absent from the data):")
    for f, xs in ranked[:a.top]:
        nums = ", ".join(sorted({x["prose_number"] for x in xs}))
        worst = _worst(xs)
        w = f"{mp.nstr(worst, 3)} rel"
        print(f"\n  {f}\n      {nums}\n      worst {w}")
    current = {f: len(v) for f, v in by_file.items()}
    rc = _ratchet(current, a.strict, a.rebaseline)
    if a.rebaseline:
        return rc

    if not a.no_witness:
        from witness_base import WitnessBuilder      # noqa: E402
        w = WitnessBuilder("witness-prose-drift-audit", engine="python")
        w.set_description(
            "Witness descriptions quoting a number the witness's own data does "
            "not contain. No staleness mechanism here reads a description -- "
            "they all compare a witness to its PRODUCER -- so a description "
            "that hardcodes a finding keeps asserting it after the data moves, "
            "and the file contradicts itself while staying green. Measured: "
            "rho-binding-constancy said '~182% (D 5.73, T 81.5, He3 37.4)' "
            "while carrying 3.87/36.99/19.12, matching neither the committed "
            "nor the regenerated data. Buckets by DISTANCE, not presence, so a "
            "4% three-sig-fig rounding is not flagged like a 49% "
            "contradiction. FAR is a candidate, not a verdict: prose may cite "
            "an external constant. Bean qou-n62l.")
        w.add_data("witnesses_scanned", len(files))
        w.add_data("without_description", no_desc)
        w.add_data("witnesses_with_candidates", len(by_file))
        w.add_data("findings", findings)
        w.add_assertion("no witness prose quotes a number absent from its data",
                        computed=len(findings), expected=0)
        w.set_audit_only("computations/audits/witness_prose_drift_audit.py")
        out = w.save()
        print(f"\n[witness] {out}")
    return rc if a.strict else (1 if findings else 0)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
