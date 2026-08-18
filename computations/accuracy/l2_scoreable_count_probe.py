#!/usr/bin/env python3
"""L2 100x status: how many SCOREABLE predictions meet the target?

The committed dashboard reports `beats_100x_count = 2` and AGENTS.md carries
that as "2/7 met (m_e, m_K/m_pi)". This probe separates *calibration inputs*
from *predictions* and recounts.

The dashboard already excludes one anchor from scoring:

    m_p : is_anchor_roundtrip = True, beats_100x = None
          "NOT SCORED. q_0 is pinned from m_p/m_e, so this 'prediction' is
           m_e x (m_p/m_e) re-evaluated through the identity that pinned it --
           the framework content cancels."

but scores the other:

    m_e : role = "CAL-1 anchor", err_ppb = 0, beats_100x = True
          "calibration anchor -- err defined as 0"

m_e is the CAL-1 input that *defines* the MeV unit, so its ratio to itself is 1
by construction and its error is not measured but *defined* zero. That is the
same reasoning m_p is excluded for, only stronger: m_p at least carries a
nonzero round-trip residual. Counting m_e as a "beat" is the calibration-
tautology error class that AGENTS.md section "q_0 anchor convention" rule 1
already names for m_mu.

No new physics here -- this only recounts what the committed witness holds.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "computations" / "per-observable-100x-status.witness.json"


def main() -> int:
    rows = json.loads(SRC.read_text())["data"]["rows"]
    summary = json.loads(SRC.read_text())["data"]["summary"]

    anchors = [r for r in rows if "anchor" in (r.get("role") or "").lower()]
    preds = [r for r in rows if r not in anchors]
    met = [r for r in preds if r.get("beats_100x_experimental") is True]

    print(f"{'obs':<12} {'role':<28} {'err_ppb':>12} {'miss':>10}  100x")
    for r in rows:
        tag = "INPUT" if r in anchors else str(r.get("beats_100x_experimental"))
        print(f"{r['obs']:<12} {(r.get('role') or '')[:28]:<28} "
              f"{str(r.get('err_ppb')):>12} {str(r.get('miss_factor'))[:10]:>10}  {tag}")

    print()
    print(f"committed beats_100x_count : {summary['beats_100x_count']}  "
          f"(counts m_e, a definitional zero)")
    print(f"calibration INPUTS         : {[r['obs'] for r in anchors]}")
    print(f"scoreable PREDICTIONS      : {[r['obs'] for r in preds]}")
    print(f"of those, meet 100x        : {[r['obs'] for r in met]}")
    print()
    print(f"HONEST SCOREABLE RATIO     : {len(met)}/{len(preds)}")

    # The failures group into exactly two root classes.
    qbeta_chain = {"Q_beta", "m_n", "Delta_pn"}
    fails = {r["obs"] for r in preds if r.get("beats_100x_experimental") is False}
    print()
    print(f"failures                   : {sorted(fails)}")
    print(f"  Q_beta chain (one root)  : {sorted(fails & qbeta_chain)}")
    print(f"  independent (mu-p)       : {sorted(fails - qbeta_chain)}")

    ok = (len(met) == 1 and len(preds) == 5
          and summary["beats_100x_count"] == 2
          and fails >= qbeta_chain)
    print()
    print("ASSERTIONS PASS" if ok else "ASSERTIONS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
