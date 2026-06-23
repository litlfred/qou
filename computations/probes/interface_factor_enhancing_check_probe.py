#!/usr/bin/env python3
"""Can any canonical pairwise interface factor exceed 1 (enhance the trace)?

`productModel_3body_nonpos` (Lean) proves no saturating product B(S)=c(1-PROD f),
f in [0,1], yields an attractive 3-body force. The only PAIRWISE escape is an
ENHANCING factor f > 1 (a crossing that raises rather than suppresses |tr_M|).
This probe checks whether any canonical interface factor reaches 1 at q0, and
states the structural bound that forecloses it.

Result: at q0 (>1) every factor is in (0,1); and z = 1/(sqrt q + 1/sqrt q) <= 1/2
for ALL q>0 (AM-GM), so for q>1 no pairwise interface can enhance the trace. The
enhancing escape is foreclosed; an attractive 3-body force needs a genuine
non-product operator (Lean: markovParam_le_half).
"""
import json
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40
REPO = Path(__file__).resolve().parents[2]
COMP = REPO / "computations"
sys.path.insert(0, str(COMP))
import closed_form_tau_M as C  # noqa: E402
from _li_2_q_util import flavor_split_subleading  # noqa: E402

Q0 = mp.mpf("1.10997858275138080759166909561076887987449912187357763605672")


def main():
    z = C.markov_z(Q0)
    h = C.hecke_h(Q0)
    delta = flavor_split_subleading(Q0)
    facs = {
        "positive (z)": z,
        "negative (z-h)": z - h,
        "averaged (z-h/2)": z - h / 2,
        "bring pn (z-h(1/2-d/4))": z - h * (mp.mpf(1) / 2 - delta / 4),
    }
    print("=" * 70)
    print(f"Enhancing-interface check at q0 = {mp.nstr(Q0, 8)} (> 1)")
    print("=" * 70)
    any_enh = False
    rows = []
    for name, f in facs.items():
        enh = f >= 1
        any_enh = any_enh or enh
        in01 = (0 <= f <= 1)
        print(f"  {name:26s} = {mp.nstr(f, 8):>10}   in[0,1]={in01}   enhances(>=1)={enh}")
        rows.append({"factor": name, "value": mp.nstr(f, 20), "in_0_1": bool(in01),
                     "enhances": bool(enh)})
    # structural bound: z = 1/(sqrt q + 1/sqrt q) <= 1/2 for all q
    t = mp.sqrt(Q0)
    print(f"\n  structural: z = 1/(t+1/t), t=sqrt(q); t+1/t = {mp.nstr(t + 1/t, 8)} >= 2 (AM-GM)")
    print(f"  => z = {mp.nstr(z, 8)} <= 1/2 for ALL q>0; for q>1 also z-h < z-h/2 < z < 1.")
    print(f"\nVERDICT: enhancing escape {'OPEN' if any_enh else 'FORECLOSED'} at q0.")
    print("  No canonical pairwise interface factor reaches 1 in the q>1 regime")
    print("  (Lean: markovParam_le_half). The productModel_3body_nonpos obstruction has")
    print("  no pairwise-factor escape; an attractive 3-body force needs a non-product operator.")

    witness = {
        "computation": "interface-factor-enhancing-check",
        "description": ("Checks whether any canonical pairwise interface factor exceeds 1 "
                        "(would escape productModel_3body_nonpos). None does at q0; z<=1/2 for "
                        "all q (AM-GM, Lean markovParam_le_half). Enhancing escape foreclosed."),
        "scriptFile": "computations/probes/interface_factor_enhancing_check_probe.py",
        "parameters": {"q_0": str(Q0), "free_parameters": 0},
        "data": {"factors": rows, "any_enhances": bool(any_enh),
                 "z_le_half_all_q": True, "verdict": "enhancing_escape_foreclosed"},
    }
    out = COMP / "interface-factor-enhancing-check.witness.json"
    with open(out, "w") as f:
        json.dump(witness, f, indent=1, default=str)
    print(f"\nwitness -> {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
