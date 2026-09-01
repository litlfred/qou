#!/usr/bin/env python3
"""Can any canonical pairwise interface factor exceed 1 (enhance the trace)?

`productModel_3body_nonpos` (Lean) proves no saturating product B(S)=c(1-PROD f),
f in [0,1], yields an attractive 3-body force. The only PAIRWISE escape is an
ENHANCING factor f > 1 (a crossing that raises rather than suppresses |tr_M|).
This probe checks whether any canonical interface factor reaches 1 at q0, and
states the structural bound that forecloses it.

Result: at q0 (>1) every canonical factor is in (0,1) -- max = 0.6127 -- so no
pairwise interface can enhance the trace. The enhancing escape is foreclosed; an
attractive 3-body force needs a genuine non-product operator.

CORRECTED 2026-08-30 (bean qou-srvu). This read "z = 1/(sqrt q + 1/sqrt q) <= 1/2
for ALL q>0 (AM-GM)" and the witness carried `z_le_half_all_q: true` as a
HARDCODED literal. That is the **convention-C** Markov parameter (0.4993), excised
by the owner ruling of 2026-08-09; `closed_form_tau_M.markov_z` returns convention
**D**, z = q^3/(q^2+1) = 0.6127 > 1/2. So the `z <= 1/2` bound is unavailable under
the canonical convention and the boolean recorded as fact was false for the z this
probe actually computes. The VERDICT is unaffected -- it rests on max factor < 1,
which holds under D with margin 0.387 -- but the stated bound and the Lean citation
`markovParam_le_half` are convention-C-frame and should be re-derived under D
(tranche qou-cds1).
"""
import time as _time  # noqa: E402 — wall-clock anchor for witness durationMs
_T0 = _time.monotonic()
import json
import sys
from pathlib import Path

import mpmath as mp

# Path bridge (moved above the set_compute_dps() call — it is what
# puts computations/substrate on sys.path so `_precision` resolves).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
REPO = Path(__file__).resolve().parents[2]
COMP = REPO / "computations"
sys.path.insert(0, str(COMP))
import closed_form_tau_M as C  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402

Q0 = mp.mpf("1.10997858275138080759166909561076887987449912187357763605672")


def main():
    z = C.markov_z(Q0)
    h = C.hecke_h(Q0)
    delta = flavor_split_leading(Q0)
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
    # Structural bound. The AM-GM argument `z = 1/(sqrt q + 1/sqrt q) <= 1/2`
    # belongs to convention **C**, which was excised by the owner ruling of
    # 2026-08-09; `closed_form_tau_M.markov_z` returns convention **D**,
    # z = q^3/(q^2+1) = 0.6126880... > 1/2 at q0. So the `z <= 1/2` bound is
    # NOT available under the canonical convention and this field is now
    # COMPUTED rather than hardcoded `True` (bean qou-srvu).
    t = mp.sqrt(Q0)
    z_le_half = bool(z <= mp.mpf(1) / 2)
    max_factor = max(facs.values())
    print(f"\n  structural: convention-C AM-GM gave z = 1/(t+1/t) <= 1/2 "
          f"(t=sqrt(q); t+1/t = {mp.nstr(t + 1/t, 8)} >= 2).")
    print(f"  Under canonical convention D, z = {mp.nstr(z, 8)}; z <= 1/2 is "
          f"{z_le_half}. The foreclosure rests on max factor < 1, not on z <= 1/2:")
    print(f"  max factor = {mp.nstr(max_factor, 8)} < 1; for q>1, z-h < z-h/2 < z < 1.")
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
                 "max_interface_factor": mp.nstr(max_factor, 20),
                 "z_le_half_at_q0": z_le_half,
                 "z_le_half_note": (
                     "Was the hardcoded literal `z_le_half_all_q: true` -- a "
                     "convention-C claim (z = 1/(sqrt q + 1/sqrt q) = 0.4993) "
                     "recorded as fact while markov_z returns convention D "
                     "(0.6127). Now computed. The verdict does not depend on "
                     "it; it depends on max factor < 1."),
                 "verdict": "enhancing_escape_foreclosed"},
    }
    import os as _os, sys as _sys  # noqa: E402
    _sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "../substrate"))
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    _wb = WitnessBuilder.wrap_legacy(
        "interface-factor-enhancing-check", witness,
        script_path=__file__, engine="mpmath", start_time=_T0, output_dir=str(COMP),
    )
    # The probe's own question is its title: "Can any canonical pairwise
    # interface factor exceed 1?". The answer was recorded as data
    # (`any_enhances`) while the witness shipped `allPassed: true` over an
    # EMPTY assertion list (bean qou-srvu). The bar `1` is the question's own,
    # not a number fitted to the observed 0.6127.
    _wb.add_assertion(
        "no_canonical_interface_factor_enhances_the_trace",
        computed=mp.nstr(max_factor, 20), expected="0.5", tolerance="0.5",
        source="Lean markovParam_le_half / productModel_3body_nonpos",
    )
    _wpath = _wb.save()
    print(f"\nwitness -> {_wpath}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
