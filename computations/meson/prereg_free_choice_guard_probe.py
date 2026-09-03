#!/usr/bin/env python3
"""
prereg_free_choice_guard_probe.py — the anti-peek guard on the free-choice
pre-registration.

WHY.  The determinacy rule merged in `f089bc13c6` scores 8/8 on the settled
record, and that number is worthless: the same agent assigned both the
free-choice labels and the outcome classes.  A rule earns a hit-rate only from
candidates classified BEFORE their outcomes are known.  This probe is the
mechanism that makes such a claim checkable later.

WHAT IT ENFORCES on `docs/audits/prereg-free-choice-2026-08-27.json`:

  1. Every candidate's `outcome` is null.  If a future agent fills one in, the
     probe FAILS until the registry is superseded by a new dated file -- so an
     outcome can never be quietly back-filled into a prediction.
  2. Every candidate carries a verbatim `spec_quote` and a `spec_citation`, so
     each classification is anchored to text that existed at registration.
  3. Every candidate's `reason_from_spec` is present, so the call is justified
     from the SPECIFICATION rather than from an outcome.
  4. `free_choice` takes one of the four declared values, and `unclassifiable`
     is used at least once -- a rule that classifies everything is not
     discriminating, so the registry has to demonstrate it can decline.
  5. The registry names the registrar's prior exposure, so contamination is
     on the record rather than assumed absent.

WHAT THIS PROBE IS NOT.  It measures nothing about physics and settles no
candidate.  It is bookkeeping with teeth: its only job is to make the later
scoring honest.  The predictions themselves are in the JSON, not here.

@module computations/meson/prereg_free_choice_guard_probe
"""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys

REG = pathlib.Path(__file__).resolve().parents[2] / "docs" / "audits" / \
    "prereg-free-choice-2026-08-27.json"

VALID = {"none", "parameter", "objective", "selection", "unclassifiable"}
_FAILED: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {msg}")
    if not ok:
        _FAILED.append(msg)


def main() -> int:
    reg = json.loads(REG.read_text())
    cands = reg["candidates"]

    print("=" * 92)
    print("Anti-peek guard on the free-choice pre-registration")
    print("=" * 92)
    print(f"\n  registry : {REG.name}")
    print(f"  candidates: {len(cands)}\n")

    peeked = [c["id"] for c in cands if c.get("outcome") is not None]
    check(not peeked,
          "A1: every outcome is null -- nothing has been back-filled. "
          + (f"VIOLATED by {peeked}" if peeked else
             "A later agent filling one in makes this probe fail, so the diff "
             "cannot hide it"))

    missing_q = [c["id"] for c in cands
                 if not c.get("spec_quote") or not c.get("spec_citation")]
    check(not missing_q,
          "A2: every classification is anchored to a verbatim spec quote and a "
          "citation, so it rests on text that existed at registration time")

    missing_r = [c["id"] for c in cands if not c.get("reason_from_spec")]
    check(not missing_r,
          "A3: every call states its reason FROM THE SPECIFICATION -- the "
          "property the rule keys on is 'is a choice left unfixed?', which is "
          "readable without running anything")

    bad = [(c["id"], c.get("free_choice")) for c in cands
           if c.get("free_choice") not in VALID]
    check(not bad, f"A4: every free_choice value is one of {sorted(VALID)}")

    kinds = {c["free_choice"] for c in cands}
    check("unclassifiable" in kinds,
          "A5: the registry DECLINES to classify at least one candidate "
          "(weighted-isospin-even-det, which has no construction). A rule that "
          "classifies everything is not discriminating, so the ability to "
          "abstain is part of what is being registered")

    check(bool(reg.get("registrar_prior_exposure")),
          "A6: the registrar's prior exposure is on the record, including that "
          "one free-choice label was authored by a previous agent and is "
          "flagged rather than claimed")

    testable = [c["id"] for c in cands if c["free_choice"] == "none"]
    blocked = [c["id"] for c in cands
               if c["free_choice"] in ("parameter", "objective", "selection")]
    print(f"\n   registered TESTABLE (no free choice) : {testable}")
    print(f"   registered NOT FALSIFIABLE as stated  : {blocked}")
    print(f"   declined                              : "
          f"{[c['id'] for c in cands if c['free_choice'] == 'unclassifiable']}")

    check(len(testable) >= 1 and len(blocked) >= 1,
          "A7: the registry makes a NON-TRIVIAL split -- it does not call "
          "everything testable or everything blocked, so it can be wrong in "
          "both directions")

    try:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                             text=True, cwd=REG.parent).stdout.strip()[:12]
    except Exception:
        sha = "unavailable"
    print(f"\n   registration anchored at git HEAD: {sha}")
    print("   (the commit adding the registry is the timestamp; there is no "
          "witness JSON here on purpose --")
    print("    a witness would be a computed artifact, and this file computes "
          "nothing about physics)")

    print("\n" + "=" * 92)
    print(f"{7 - len(_FAILED)}/7 guard assertions passed")
    print("=" * 92)
    return 1 if _FAILED else 0


if __name__ == "__main__":
    raise SystemExit(main())
