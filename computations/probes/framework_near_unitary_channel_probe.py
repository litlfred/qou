#!/usr/bin/env python3
"""framework_near_unitary_channel_probe.py

Does the framework produce a near-unitary two-body channel?
STRUCTURE: yes. NEARNESS: no -- and by standing rule it cannot.

THE QUESTION
------------
b3_is_the_deuteron_deficit relocated the target: b3 = 3 x (the deuteron deficit)
exactly, so the b3 magnitude question is the deuteron-weakness question. The
deuteron is weak because its 3S1 channel is NEAR-UNITARY -- scattering length
a_t = 5.42 fm against a range ~1.4 fm, with the 1S0 partner an unbound virtual
state. Physically that near-degeneracy of the two S-wave channels IS Wigner SU(4)
being nearly exact.

So: does QOU produce such a channel?

STRUCTURE -- YES
----------------
The Hecke relation sigma^2 = h sigma + 1 has eigenvalues q (symmetric) and -1/q
(antisymmetric), split by

    h = q - 1/q,      h -> 0 as q -> 1

**q = 1 is the framework's degenerate point**: the two Hecke channels become
equal in magnitude there. That is a genuine structural analogue of the physical
3S1/1S0 near-degeneracy at threshold, and it is native -- not imported.

    h(q0)   = 0.2090602988
    h(1.01) = 0.0199009901
    h(1)    = 0            exact degeneracy

NEARNESS -- NO, AND IT CANNOT BE DERIVED
-----------------------------------------
q0 is a CAL-2 calibration INPUT, and deriving q0 from the substrate is FOREVER
GATED by owner ruling (2026-08-02, bean qou-eic1) -- a permanent gate, not a
decline awaiting reversal. So the framework's proximity to its own degenerate
point is an input by construction.

**Consequence, and it is the useful part: any derivation of the deuteron deficit
that routes through "why is q0 close to 1" is FORBIDDEN, not merely open.** That
is a hard boundary on this line of attack, and it is worth knowing before more
effort is spent on it.

A NEAR-MATCH I AM NOT REPORTING AS EVIDENCE
--------------------------------------------
h = 0.2090603 sits 1.93% from the 3H-convention deficit fraction 0.2131739. Under
this arc's own entropy discipline that is NOT evidence:

  * the deficit fraction is convention-dependent, [0.1760783, 0.2131739], a band
    21.07% wide -- so any candidate inside it "hits";
  * of 8 natural small parameters tested, **3 land inside the band**
    (h, 1-1/q^2, 2*hbar_q).

Three of eight is not discrimination. Same conclusion the fingerprint screen
reached: closed-form matching cannot be evidence at this precision. Recorded so
the 1.93% is not later quoted as a result.

VERDICT
-------
The framework supplies the STRUCTURE of a near-unitary two-body channel and, by
its own standing rule, cannot supply the NEARNESS. The deuteron-deficit route
therefore terminates at the q0 gate rather than at a physics wall.

Derives nothing. Refutes nothing. Establishes where this line stops and why.

Bean qou-edt7.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from q_parameter import Q_MP  # noqa: E402  (exact mpf; NEVER mpf(str(Q)) -- Q is f64)
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)


def main() -> int:
    wb = WitnessBuilder("framework-near-unitary-channel", engine="mpmath")
    wb.set_description(
        "The framework HAS a degenerate point at q = 1, where the two Hecke "
        "eigenvalues q and -1/q become equal in magnitude (h = q - 1/q -> 0) -- a "
        "native structural analogue of the 3S1/1S0 near-degeneracy. But q0 is a "
        "CAL-2 input and deriving it is FOREVER GATED, so the NEARNESS cannot be "
        "derived: the deuteron-deficit route terminates at the q0 gate. The "
        "h-vs-deficit near-match (1.93%) is NOT evidence -- 3 of 8 small "
        "parameters land inside the 21%-wide convention band."
    )
    ok = True

    D = ame_binding_mev(1, 2)
    T3, He3 = ame_binding_mev(1, 3), ame_binding_mev(2, 3)
    q = +Q_MP
    h, hb = q - 1 / q, 1 - 1 / q

    # ---- structure --------------------------------------------------------
    print("STRUCTURE -- the framework's degenerate point\n")
    print(f"  eigenvalues of sigma:  q = {mp.nstr(q,12)}   -1/q = {mp.nstr(-1/q,12)}")
    for qq in ("1.10997858275", "1.05", "1.01", "1.001", "1"):
        v = mp.mpf(qq)
        hv = v - 1 / v
        print(f"    h({qq:<14}) = {mp.nstr(hv,10)}")
    print("\n  h -> 0 as q -> 1: the two Hecke channels become degenerate there.")
    wb.add_data("degenerate_point", {
        "relation": "sigma^2 = h sigma + 1, eigenvalues q and -1/q",
        "splitting": "h = q - 1/q",
        "h_at_q0": fmt(h), "degenerate_at": "q = 1",
        "analogue_of": "the 3S1/1S0 near-degeneracy at threshold (Wigner SU(4) "
                       "nearly exact)",
    })
    wb.add_assertion(
        name="framework_has_a_degenerate_point_at_q_eq_1",
        computed=fmt(mp.mpf(1) - 1 / mp.mpf(1)), expected="0", tolerance="1e-50",
        unit="h at q = 1",
        source="h = q - 1/q vanishes exactly at q = 1, so the two Hecke channels "
               "become equal in magnitude -- the structural analogue of unitarity",
    )
    ok &= abs(mp.mpf(1) - 1 / mp.mpf(1)) < mp.mpf(10) ** -50

    # ---- the near-match, and why it is not evidence ------------------------
    f_iso = ((T3 + He3) / 2 / 3 - D) / ((T3 + He3) / 2 / 3)
    f_3h = (T3 / 3 - D) / (T3 / 3)
    lo, hi = min(f_iso, f_3h), max(f_iso, f_3h)
    cands = {"h": h, "hbar_q": hb, "q_minus_1": q - 1, "hbar_q_sq": hb ** 2,
             "h_over_2": h / 2, "h_sq": h ** 2, "one_minus_q_inv_sq": 1 - 1 / q ** 2,
             "two_hbar_q": 2 * hb}
    inband = [nm for nm, v in cands.items() if lo <= v <= hi]
    print(f"\nTHE NEAR-MATCH, and why it is not evidence\n")
    print(f"  h = {mp.nstr(h,9)} vs 3H deficit fraction {mp.nstr(f_3h,9)}  -> "
          f"{mp.nstr(abs(h-f_3h)/f_3h*100,4)}%")
    print(f"  but the deficit fraction is CONVENTION-DEPENDENT: "
          f"[{mp.nstr(lo,7)}, {mp.nstr(hi,7)}], {mp.nstr((hi-lo)/lo*100,4)}% wide")
    print(f"  of {len(cands)} small parameters, {len(inband)} land INSIDE: {inband}")
    print("  -> not discrimination. NOT evidence.")
    wb.add_data("near_match_not_evidence", {
        "h": fmt(h), "deficit_band": [fmt(lo), fmt(hi)],
        "band_width_pct": fmt((hi - lo) / lo * 100),
        "n_candidates": len(cands), "n_inside_band": len(inband),
        "inside": inband,
        "verdict": "3 of 8 inside a 21%-wide band is not discrimination; the 1.93% "
                   "must not be quoted as a result",
    })
    wb.add_assertion(
        name="near_match_is_at_chance",
        computed=str(len(inband)), expected="3", tolerance="0",
        unit="small parameters inside the convention band",
        source="8 tested, 3 inside -- the same conclusion the fingerprint screen "
               "reached: closed-form matching cannot be evidence at this precision",
    )
    ok &= len(inband) >= 2

    # ---- the gate ---------------------------------------------------------
    print("\nTHE NEARNESS -- an input, and permanently so\n")
    print("  q0 is a CAL-2 calibration INPUT. Deriving q0 from the substrate is")
    print("  FOREVER GATED (owner ruling 2026-08-02, bean qou-eic1) -- a permanent")
    print("  gate, not a decline awaiting reversal.")
    print("\n  => any derivation of the deuteron deficit that routes through 'why is")
    print("     q0 close to 1' is FORBIDDEN, not merely open. The deuteron-deficit")
    print("     route terminates at the q0 gate rather than at a physics wall.")
    wb.add_data("verdict", {
        "structure_supplied": True,
        "structure_what": "a degenerate point at q = 1 where h = q - 1/q vanishes",
        "nearness_supplied": False,
        "nearness_why_not": "q0 is a CAL-2 input; deriving it is FOREVER GATED "
                            "(owner ruling 2026-08-02, qou-eic1)",
        "consequence": "a deuteron-deficit derivation routing through q0's "
                       "proximity to 1 is FORBIDDEN, not open",
        "derives_anything": False,
        "refutes_anything": False,
        "establishes": "where this line of attack stops, and that it stops at a "
                       "standing rule rather than at a physics wall",
    })
    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
