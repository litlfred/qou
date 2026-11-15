#!/usr/bin/env python3
# polynomial_q_not_applicable: static triage over committed witnesses, not a q-series compute.
"""Which muon-anchored witnesses have assertion margin too thin to survive the proton move?

`qou-1c4y` step 2 item 2 says, in its own words: *"Re-verify tolerances first.
Measured anchor impact is ~1e-7 relative, so any witness whose assertions are
tighter than that may legitimately fail after the move. Those are findings, not
breakage — triage before regenerating en masse."*

Nothing measured it. The classify and regenerate halves both exist
(`q0_sweep_classify.py`, `q0_repin_regen_batch.py`), so the sweep could be run
today — and would then discover its tight-tolerance failures one producer at a
time, interleaved with real regressions and indistinguishable from them. This
script front-runs that: it reads the committed witnesses statically, with no
producer re-run, and says up front which assertions cannot absorb the move.

## What is actually being measured

Not the tolerance. The **unused margin**:

    slack = (tolerance - |computed - expected|) / |expected|

An assertion with a generous tolerance that is already sitting at 99 % of it is
just as fragile as one with a tight tolerance and room to spare, and only the
second reads as dangerous if you sort by tolerance alone. What matters is how
much room is left, relative to the ~1e-7 the anchor move will consume.

Both fields are needed, so an assertion carrying no numeric `tolerance` (a
boolean check, a count, a string match) is reported as UNMEASURABLE rather than
silently treated as safe -- a boolean assertion CAN flip, this script just
cannot predict it from the committed file.

## Scope, stated honestly

This is scope (a): it says which assertions have too little margin to be
*guaranteed* to survive. It does NOT predict failure -- the direction and size
of each value's response to the anchor is not known without re-running, and an
assertion with thin margin may move the safe way or not move at all. Nor does
clearing this triage prove a witness survives: a producer whose output depends
on the anchor non-smoothly, or that hits a cached muon-built artifact, can fail
with any amount of nominal margin.

Read it as a work-ordering tool: PINNED-TO-ANCHOR first, then AT-RISK, one at
a time and with attention. The other buckets are deliberately kept out of that
list -- DISCRETE and THRESHOLD-SEMANTICS both LOOK like zero margin and are
neither, and both were false positives in earlier versions of this script.
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from q0_provenance_audit import (  # noqa: E402
    Q_MUON,
    Q_PROTON,
    is_anchor_key,
)

#: Relative impact of the muon -> proton anchor move, measured on the mu3
#: Delta^2 g by `deltalambda/mu3_anchor_consistency_probe.py`. Recorded in
#: `qou-1c4y`. It is one measurement on one quantity, not a bound -- a producer
#: that amplifies the anchor can move further, which is exactly why the AT-RISK
#: band below is an order of magnitude wide rather than a sharp cut.
ANCHOR_IMPACT = 1e-7

#: Bucket edges in units of ANCHOR_IMPACT.
AT_RISK = 1.0      # slack below 1x the impact: cannot be guaranteed to survive
THIN = 10.0        # slack below 10x: survives this measurement, little room


def anchor_of(doc) -> str | None:
    """Which pin this witness records, by VALUE, or None if it records none.

    Value-based rather than field-name based, and deliberately reusing
    `q0_provenance_audit.is_anchor_key` rather than re-deriving it: three
    generations of that key pattern disagreed with each other, and a fourth
    private copy here would be a fourth generation.
    """
    best = None
    stack = [doc]
    while stack:
        o = stack.pop()
        if isinstance(o, dict):
            for k, v in o.items():
                if is_anchor_key(k):
                    try:
                        f = float(v)
                    except (TypeError, ValueError):
                        pass
                    else:
                        dp = abs(f - Q_PROTON) / Q_PROTON * 1e9
                        dm = abs(f - Q_MUON) / Q_MUON * 1e9
                        if dm < 30.0 and dm < dp:
                            best = "muon"
                        elif dp < 1.0 and best != "muon":
                            best = best or "proton"
                stack.append(v)
        elif isinstance(o, list):
            stack.extend(o)
    return best


def slack_of(a: dict) -> float | None:
    """Unused relative margin, or None if it cannot be computed from the file."""
    tol, comp, exp = a.get("tolerance"), a.get("computed"), a.get("expected")
    try:
        tol, comp, exp = float(tol), float(comp), float(exp)
    except (TypeError, ValueError):
        return None
    if exp == 0.0 or tol != tol or comp != comp:
        return None
    used = abs(comp - exp)
    return (tol - used) / abs(exp)


def is_discrete(a: dict) -> bool:
    """Is this assertion a COUNT or structural fact rather than a measurement?

    This distinction is why the first version of this script was wrong. It
    reported 291 assertions AT RISK; 229 of them looked like

        {"name": "all_77_y_lambda_computed", "tolerance": 0,
         "computed": 77, "expected": 77}

    Zero tolerance and zero margin, so the slack test flagged every one -- and
    every one is a false positive. "77 things were computed" and "3 rows were
    feasible" are not continuous functions of the anchor; an 11.5 ppb shift in
    q0 cannot make them 76 or 4. They either hold structurally or they do not,
    and if one breaks under the move it is because the producer took a
    different code path, which no static margin analysis was ever going to
    predict.

    Zero margin is the correct reading of the arithmetic and the wrong reading
    of the assertion. Sorting by slack alone puts the least informative rows at
    the top of the list, which is worse than not sorting at all.
    """
    tol, comp, exp = a.get("tolerance"), a.get("computed"), a.get("expected")
    try:
        tol, comp, exp = float(tol), float(comp), float(exp)
    except (TypeError, ValueError):
        return False
    if tol != 0.0:
        return False
    return comp == int(comp) and exp == int(exp)


def carries_the_anchor(a: dict) -> bool:
    """Does this assertion's value carry the muon anchor's own digits?

    The sharpest signal available statically. An assertion whose expected value
    IS the muon q0 (or agrees with it to well past where the two pins split)
    does not merely have thin margin -- it is pinned to the value being moved,
    so it moves by the full 11.5 ppb by construction. Example, live in the
    corpus:

        {"name": "lambda_plus_eq_q", "tolerance": 1e-18,
         "computed": 1.1099785955573347199, ...}

    1e-18 tolerance against a quantity that is about to shift 1.15e-8. That is
    ten orders of magnitude of overrun, and it is not a judgement call.
    """
    for key in ("computed", "expected"):
        try:
            v = abs(float(a.get(key)))
        except (TypeError, ValueError):
            continue
        if v == 0.0:
            continue
        # Scale-free: catch the anchor itself and simple multiples of it.
        for scale in (1.0, 2.0, 0.5):
            if abs(v / scale - Q_MUON) / Q_MUON < 1e-9:
                return True
    return False


def triage(path: pathlib.Path):
    try:
        doc = json.loads(path.read_text())
    except Exception:
        return None
    if not isinstance(doc, dict):
        return None
    if anchor_of(doc) != "muon":
        return None
    rows = []
    for a in doc.get("assertions") or []:
        if not isinstance(a, dict):
            continue
        name = a.get("name") or a.get("label") or "<unnamed>"
        s = slack_of(a)
        if s is None:
            rows.append((name, None, "UNMEASURABLE"))
        elif is_discrete(a):
            # A count or structural fact. Zero margin, but not anchor-continuous
            # -- see is_discrete(). Bucketed away from the triage list rather
            # than dropped, because one CAN break; just not for this reason.
            rows.append((name, s, "DISCRETE"))
        elif a.get("passed") is False:
            # Already failing as committed -- the move is not its problem.
            # Keyed on the witness's own `passed`, not on the sign of `slack`:
            # see THRESHOLD-SEMANTICS below.
            rows.append((name, s, "ALREADY-FAILING"))
        elif s < 0:
            # `passed: true` while |computed - expected| EXCEEDS `tolerance`.
            # That is not a contradiction, it is a different assertion
            # semantics: the fields encode an INEQUALITY, and `passed` records
            # whether the inequality held. Live example --
            #
            #   stage1_entropy_verdict_is_blocked: computed 2.21, expected 9.2,
            #   tolerance 0, passed TRUE, source "pre-registered kill
            #   criterion ... pass means the kill fired"
            #
            # 2.21 < 9.2 is the POINT. Reporting it as "already failing", which
            # an earlier version of this script did, inverts the meaning of a
            # deliberately pre-registered negative result. The margin model
            # simply does not apply, so say so rather than guess.
            rows.append((name, s, "THRESHOLD-SEMANTICS"))
        elif carries_the_anchor(a):
            rows.append((name, s, "PINNED-TO-ANCHOR"))
        elif s < AT_RISK * ANCHOR_IMPACT:
            rows.append((name, s, "AT-RISK"))
        elif s < THIN * ANCHOR_IMPACT:
            rows.append((name, s, "THIN"))
        else:
            rows.append((name, s, "ROOMY"))
    return doc.get("scriptFile") or doc.get("script") or "<unknown>", rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default="computations")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    by_producer = collections.defaultdict(list)
    verdicts = collections.Counter()
    files = 0
    no_assertions = 0

    for p in sorted(pathlib.Path(args.root).rglob("*.witness.json")):
        if ("_deprecated" in p.parts or "fsh-guts" in p.parts):
            continue
        r = triage(p)
        if r is None:
            continue
        producer, rows = r
        files += 1
        if not rows:
            no_assertions += 1
        for name, s, v in rows:
            verdicts[v] += 1
            if v in ("PINNED-TO-ANCHOR", "AT-RISK", "THIN"):
                by_producer[producer].append((p.name, name, s, v))

    if args.json:
        # Provenance stamp (bean qou-f1rs): the witness dict was built
        # INLINE at the write below, so there was nothing to stamp. It
        # is bound to a name here so this producer records which script
        # wrote it -- a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        _prov_payload = {
            "muon_witnesses": files,
            "without_assertions": no_assertions,
            "anchor_impact": ANCHOR_IMPACT,
            "verdicts": dict(verdicts),
            "flagged_by_producer": {
                k: [{"witness": w, "assertion": n, "slack": s, "verdict": v}
                    for w, n, s, v in sorted(vs)]
                for k, vs in sorted(by_producer.items())
            },
        }
        _prov_payload.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            _prov_payload, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(_prov_payload, sys.stdout, indent=2)
        print()
        return 0

    print(f"  muon-anchored witnesses     : {files}")
    print(f"    ...carrying no assertions : {no_assertions}  "
          f"(nothing to check; not the same as safe)")
    print(f"  anchor impact assumed       : {ANCHOR_IMPACT:.0e} relative "
          f"(one measurement, not a bound)\n")
    for v in ("PINNED-TO-ANCHOR", "AT-RISK", "THIN", "ALREADY-FAILING",
              "THRESHOLD-SEMANTICS", "DISCRETE", "UNMEASURABLE", "ROOMY"):
        print(f"    {v:16s} {verdicts[v]:5d}")
    print()

    LIVE = ("PINNED-TO-ANCHOR", "AT-RISK")
    flagged = {k: v for k, v in by_producer.items()
               if any(x[3] in LIVE for x in v)}
    print(f"  Producers with an anchor-sensitive thin assertion: {len(flagged)}"
          f"\n  -- regenerate these one at a time, not in a batch. "
          f"PINNED-TO-ANCHOR first:\n")
    for producer, rows in sorted(flagged.items()):
        risky = sorted((x for x in rows if x[3] in LIVE),
                       key=lambda x: (x[3] != "PINNED-TO-ANCHOR", x[0]))
        print(f"  {producer}  ({len(risky)} at risk)")
        for w, n, s, _v in risky[:4]:
            print(f"      [{_v}] {w}  {n}  slack={s:.2e}")
        if len(risky) > 4:
            print(f"      ... and {len(risky) - 4} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
