#!/usr/bin/env python3
"""I-ceil (magnitude leg) — the trace-magnitude ceiling admits the ⁴He connected excess.

Scoping: docs/scope/2026-07-05-gap-a4-ursell-operator-magnitude-scoping.md §3
(invariant I-ceil). Third and last GATE before the b₄^even value computation.
After I-par (target = b₄^even) and I-conn (irreducibly connected, A=4-local), this
unit asks the necessary-condition question: can the connected b₄^even magnitude
even REACH the needed excess, or is it excluded by the trace-magnitude ceiling?

NEEDED connected excess at ⁴He:
    B_AME(⁴He) − best_pairwise = 28.296 − 6.079·B_D = 28.296 − 13.523 = 14.773 MeV
(best_pairwise = the pairwise-ceiling witness's sup over {mult,add}×{chain,complete}).

TRACE-MAGNITUDE CEILING (parameter-free, no fit):
    B_vol(A) = a_V · A,   a_V = E₀ · ln(1/W_free) ≈ 7.584 MeV/nucleon
with W_free the free nucleon (1,1,1) Plancherel weight and E₀ = m_e/(q₀(q₀−1)).
This is the dashboard's all-knots entanglement volume term — the parameter-free
saturation scale of the trace framework (valid for all A). At ⁴He:
    B_vol(⁴He) = 30.334 MeV,   max connected room = B_vol − pairwise = 16.811 MeV.

RESULT (scope-(a), no fit):
    16.811 MeV (room)  ≥  14.773 MeV (needed)   ⇒  I-ceil PASSES (~14% headroom).
The trace framework has enough magnitude to accommodate the connected b₄^even
excess; the [1^4] term is NOT excluded by the ceiling. The value computation is
therefore LICENSED (had the room been < needed, it would be a scope-(b) exclusion
— stop before computing).

CAVEAT. This is a NECESSARY-condition ceiling, not the value: passing means "the
[1^4] term could supply it," not "it does." The ~14% headroom is modest — the
value computation must show the *connected* slice actually reaches ~14.8 MeV, not
merely that the total trace magnitude (30.3 MeV) does. That value computation (the
connected-cluster Markov trace on the ⁴He χ) is the remaining multi-session core.

`-- Ref:` scoping §3 I-ceil; standard-part-functor.md (B_vol / a_V);
interface-operator-pairwise-ceiling.witness.json (best_pairwise).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import mpmath as mp

# Path bridge (moved above the set_compute_dps() call — it is what
# puts computations/substrate on sys.path so `_precision` resolves).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from substrate.witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_HE4_MEV_VALIDATION

COMP = str(_COMP)


def main() -> int:
    # q0 read BY NAME from `q_parameter` (bean qou-9ugp, 2026-09-03). It was the
    # literal 1.1099785955573... -- the RETIRED self-certified muon pin A,
    # superseded 2026-08-22 by the CODATA-2022 lepton-ratio derivation. There is
    # no comparison leg here, so the 2026-08-30 owner ruling puts this producer
    # on the PROTON default; the pin moves 11.54 ppb. `q_parameter`, not
    # `qou_substrate.constants`, so the witness resolves its anchor stamp.
    q = Q_MP
    m_e = mp.mpf("0.51099895069")
    E0 = m_e / (q * (q - 1))
    B_D = mp.mpf("2.22452")
    B_AME_he4 = AME_B_HE4_MEV_VALIDATION
    best_pw_ratio = mp.mpf("6.079")           # sup over pairwise models, ceiling witness
    W_free = mp.mpf("0.163383")               # free nucleon (1,1,1) Plancherel weight

    pairwise = best_pw_ratio * B_D
    needed_excess = B_AME_he4 - pairwise
    a_V = E0 * mp.log(1 / W_free)
    B_vol = a_V * 4
    room = B_vol - pairwise
    passes = room >= needed_excess
    headroom_frac = (room - needed_excess) / needed_excess

    result = {
        "E0_MeV": mp.nstr(E0, 8),
        "B_AME_he4_MeV": mp.nstr(B_AME_he4, 8),
        "best_pairwise_MeV": mp.nstr(pairwise, 8),
        "needed_connected_excess_MeV": mp.nstr(needed_excess, 8),
        "a_V_MeV_per_nucleon": mp.nstr(a_V, 8),
        "trace_ceiling_B_vol_he4_MeV": mp.nstr(B_vol, 8),
        "max_connected_room_MeV": mp.nstr(room, 8),
        "headroom_fraction": mp.nstr(headroom_frac, 6),
        "verdict": (
            "I-ceil PASSES: max connected room (16.811 MeV = B_vol − pairwise) ≥ needed "
            "excess (14.773 MeV), ~14% headroom. The trace framework admits the connected "
            "b₄^even excess; the [1^4] term is NOT excluded by the norm ceiling — the value "
            "computation is licensed. NECESSARY condition only: passing ≠ the term supplies "
            "it; the connected-slice value (not the total 30.3 MeV) must reach ~14.8 MeV. "
            "Modest headroom. Scope-(a), no fit."),
        "gates_status": "I-par (done), I-conn (done), I-ceil (done) — all three magnitude gates cleared.",
    }

    payload = {
        "computation": "b4-iceil-norm-ceiling",
        "description": ("I-ceil: the parameter-free trace-magnitude ceiling B_vol(⁴He)=30.3 MeV "
                        "leaves 16.8 MeV connected room ≥ the 14.8 MeV needed excess ⇒ the [1^4] "
                        "connected term is not excluded (~14% headroom); value computation licensed. "
                        "audit-only, no fit."),
        "tier": "structural (parameter-free B_vol ceiling + committed pairwise best)",
        "result": result,
        "context": {
            "axis": "GAP-A-4 class-D — [1^4] Ursell operator magnitude, invariant I-ceil",
            "scoping": "docs/scope/2026-07-05-gap-a4-ursell-operator-magnitude-scoping.md §3",
            "ceiling_form": "B_vol = a_V·A, a_V = E₀·ln(1/W_free) (standard-part-functor.md)",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "b4-iceil-norm-ceiling", payload,
        script_path=__file__, engine="python+mpmath", output_dir=os.path.join(COMP, "probes"),
    )
    wb.add_assertion("trace_ceiling_admits_connected_excess", computed=str(bool(passes)), expected="True")
    wb.add_assertion("headroom_is_positive_but_modest",
                     computed=mp.nstr(headroom_frac, 4), expected="0.14", tolerance=0.03)
    out = wb.save(extra={"auditOnly": True})

    print("=== I-ceil: trace-magnitude ceiling vs needed connected excess (⁴He) ===")
    print(f"  B_AME(⁴He)                 = {float(B_AME_he4):.3f} MeV")
    print(f"  best pairwise              = {float(pairwise):.3f} MeV")
    print(f"  NEEDED connected excess    = {float(needed_excess):.3f} MeV")
    print(f"  trace ceiling B_vol(⁴He)   = {float(B_vol):.3f} MeV")
    print(f"  max connected room         = {float(room):.3f} MeV   (headroom {float(headroom_frac)*100:.1f}%)")
    print(f"  I-ceil PASS (room ≥ needed): {passes}")
    print("  ⇒ [1^4] term not excluded; value computation licensed. All three gates cleared.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
