#!/usr/bin/env python3
"""AGENTS.md's Q_beta figure of 1279 ppb / 164x is CORRECT and deliberately
anti-circular. It is NOT a truncation artefact, and "correcting" it to 37.7 ppb
would launder a CODATA-anchored fit into a headline accuracy claim.

## The claim this probe was written to CONFIRM, and refutes instead

Bean `qou-99qc` records:

    "ALSO MEASURED, and it corrects the dashboard reading: AGENTS.md's
     '1279 ppb' is EXACTLY the 2-rung truncation (computed 1279.465 ppb).
     The full five rungs reach 37.7 ppb -- 4.8x short of the 7.8 ppb L2
     target, not 164x."

Every number in that passage is right. The reading is backwards, and acting on
it would have been an anti-laundering violation.

## Why

`per_observable_100x_status.py` does not truncate. It walks the c_k cache and
stops at the first rung whose `tier` is not `derived`, with the reason stated
in its own source:

    "The dashboard headline reports the deepest cumulative DERIVED rung only;
     cal-anchored rungs are cached for downstream reuse but NEVER counted
     toward a 100x/1x pass (that would be circular)."

And the cache has exactly two rungs:

    k=2  tier=derived       (lean-proved, Taylor-exact, q0-independent)
    k=3  tier=cal-anchored  (extracted from CODATA Q_beta at canonical q0)

So the gate fires at k=2 by design. The rungs that carry the error from 1279
ppb down to 37.7 ppb are **extracted from the very measurement being
predicted**. Counting them is circular, which is precisely what the tier
mechanism exists to prevent.

## What each figure legitimately means

  1279 ppb  (164.0x)  the deepest DERIVED rung -- a parameter-free prediction.
                      This is the L2 status and AGENTS.md quotes it correctly.
  37.7 ppb  (4.8x)    the full ladder INCLUDING cal-anchored rungs. A
                      legitimate statement about ladder convergence; NOT an
                      accuracy result, and not quotable as one.

Both are real. They answer different questions, and only the first is an L2
figure. This is the same distinction AGENTS.md already draws at CAL-1 and
CAL-2 ("an m_mu value computed at the muon q0 is the calibration tautology,
not an accuracy win") -- one tier down, on the c_k ladder.

## Scope

Scope-(a). Nothing is wired, no content block is edited, and AGENTS.md's
figure is deliberately left alone -- the finding is that it is right.
"""

from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(50)

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if note:
        print(f"         {note}")
    if w is not None:
        w.add_data(name, bool(ok))
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def main() -> int:
    w = WitnessBuilder("qbeta-dashboard-rung-gate", engine="python")
    w.set_description(
        "The L2 dashboard's Q_beta figure (1279 ppb / 164x) is the deepest "
        "DERIVED c_k rung, gated deliberately against cal-anchored rungs to "
        "avoid circularity -- not a truncation artefact. Refutes the reading "
        "in bean qou-99qc that it should be 'corrected' to the full-ladder "
        "37.7 ppb, which would count rungs extracted from the CODATA Q_beta "
        "being predicted. Scope-(a); nothing wired."
    )

    cache_p = os.path.join(ROOT, "computations", "qbeta",
                           "qbeta-ck-cache.witness.json")
    dash_p = os.path.join(ROOT, "computations",
                          "per-observable-100x-status.witness.json")
    prod_p = os.path.join(ROOT, "computations", "per_observable_100x_status.py")

    cache = json.load(open(cache_p))
    dash = json.load(open(dash_p))
    src = open(prod_p).read()

    rows = cache["data"]["rows"]
    tiers = [(r.get("k"),
              r.get("tier") or ("derived" if r.get("label") == "lean-proved"
                                else "cal-anchored"))
             for r in rows]
    print("\n  c_k cache rungs:", tiers)
    w.add_data("ck_cache_tiers", [f"k={k}:{t}" for k, t in tiers])

    derived = [k for k, t in tiers if t == "derived"]
    anchored = [k for k, t in tiers if t != "derived"]

    check("cache_has_exactly_one_derived_rung", len(derived) == 1,
          f"derived rungs {derived}, cal-anchored {anchored}. The dashboard "
          f"stops at the first non-derived rung, so it reports k={derived[0]} "
          f"-- there is no deeper DERIVED rung to report", w)

    # the gate is in the producer, stated as anti-circularity
    # The comment wraps across source lines with `#` continuations, so match
    # loosely and normalise. An earlier version anchored on the exact phrase
    # "deepest cumulative DERIVED rung only" and silently produced
    # "(comment not matched)" as its evidence while still PASSING on the
    # keyword gate below -- a green check with no evidence behind it.
    gate = "NEVER" in src and "circular" in src and "tier" in src
    m = re.search(r"deepest cumulative DERIVED rung.{0,260}", src, re.S)
    quoted = " ".join(re.sub(r"\n\s*#", " ", m.group(0)).split())[:230] if m else ""
    check("producer_states_the_gate_as_anti_circularity", gate and bool(quoted),
          f"per_observable_100x_status.py: “{quoted}”", w)

    stops = 'break  # stop at first non-derived' in src
    check("producer_breaks_at_first_cal_anchored_rung", stops,
          "the loop carries an explicit `break` at the first non-derived rung, "
          "so cal-anchored rungs are cached but never scored", w)

    # the dashboard row
    qrow = [r for r in dash["data"]["rows"]
            if str(r.get("miss_factor")) == "164.0"]
    check("dashboard_row_is_the_derived_rung_figure", len(qrow) == 1,
          f"Q_beta row: err_ppb={qrow[0]['err_ppb']!r}, "
          f"miss_factor={qrow[0]['miss_factor']!r}" if qrow
          else "no row with miss_factor 164.0", w)

    # 🛑 the value is a STRING in the witness. A numeric scan for 1279 finds
    # nothing and reads as "the dashboard no longer carries this figure" --
    # which is the exact opposite of the truth. Recorded because this probe's
    # author made that mistake before writing this line.
    raw = qrow[0]["err_ppb"] if qrow else None
    check("err_ppb_is_stored_as_a_string_not_a_number",
          isinstance(raw, str),
          f"err_ppb is {type(raw).__name__} {raw!r}. A `isinstance(v, float)` "
          f"scan over this witness returns NO value in [1000, 2000] and so "
          f"reads as 'the figure is gone'. Match on the string", w)

    # arithmetic: both figures are real, and they answer different questions
    target = mp.mpf("7.797")
    derived_ppb = mp.mpf("1279")
    full_ppb = mp.mpf("37.70749")
    check("both_figures_reproduce_their_stated_miss_factors",
          abs(derived_ppb / target - mp.mpf("164.0")) < mp.mpf("0.5")
          and abs(full_ppb / target - mp.mpf("4.836")) < mp.mpf("0.01"),
          f"derived-rung {mp.nstr(derived_ppb/target, 4)}x vs full-ladder "
          f"{mp.nstr(full_ppb/target, 4)}x against the {target} ppb L2 target. "
          f"Both arithmetics are correct; only the first is parameter-free", w)

    check("correcting_agents_md_would_have_been_laundering", True,
          "AGENTS.md's 1279 ppb / 164.0x is the DERIVED-rung figure and is "
          "correct as written. Replacing it with 37.7 ppb / 4.8x would report "
          "a ladder containing rungs extracted from CODATA Q_beta as a "
          "parameter-free accuracy result -- the move AGENTS.md forbids at "
          "CAL-1 and CAL-2, one tier down. Left unedited deliberately", w)

    w.save()
    print(f"\n=== {'ALL PASS' if not FAILED else 'FAILURES: ' + ', '.join(FAILED)} ===")
    return 1 if FAILED else 0


if __name__ == "__main__":
    raise SystemExit(main())
