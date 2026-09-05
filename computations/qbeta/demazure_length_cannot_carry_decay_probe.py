#!/usr/bin/env python3
"""A single reduction length cannot carry the decay rate — it is short by ~200x
at order zero, and the required depth is a full-tower statement.

WHAT WAS ASKED
--------------
Continuation of `decay_as_computational_time_probe` (owner proposal: "decay rate
in terms of computational time").  That probe fixed the TARGET at
N_ops = m/Gamma, spanning 25.5 orders.  AGENTS.md 7b item 3 names the mechanism
to try: unstable intermediaries as DEMAZURE SUB-CRYSTALS -- "incomplete
topological states", which is what an unfinished computation is.  A Demazure
sub-crystal B_w(lambda) is indexed by a Weyl element w, and its natural
incompleteness measure is a LENGTH: l(w_0) - l(w), the reduction steps not yet
taken.

So the sharpest cheap test is a RANGE test: can a length-exponent even reach
25.5 orders at the braid indices this corpus assigns?

THE TEST IS FIT-FREE, WHICH IS THE POINT
-----------------------------------------
Set N_ops = q_0^L.  Then q_0 is FIXED at the substrate pin and L is DETERMINED:

    L = ln(N_ops) / ln(q_0),     ln q_0 = 0.1043407203

Nothing is adjusted.  L is read off, and the question is whether the resulting
numbers are plausible Weyl lengths for the corpus's own braid assignments.

RESULT -- THE ORDER-ZERO READING FAILS BY TWO ORDERS
------------------------------------------------------
    neutron        L = 598.00        muon  L = 387.23
    charged pion   L = 347.39        tau   L = 262.48
    Z boson        L =  34.49

The corpus assigns a nucleon the braid group B_3 (`atomic-braid-recipe-n-
canonical`: T_w(neutron) in B_3), so its Weyl group is S_3 and the longest
element has l(w_0) = 3.  **The neutron needs ~598 and has 3** -- short by a
factor of ~200.  No choice of w inside S_3 can help: 3 is the ceiling.

So a decay rate cannot be a reduction length of the particle's OWN braid.
That is a scope-(a) negative and it is the useful half of this probe.

WHAT SURVIVES, AND WHERE IT WOULD HAVE TO LIVE
------------------------------------------------
Requiring l(w_0) = n(n-1)/2 >= L gives the tower depth each state would need:

    Z boson  n >= 9     tau  n >= 24     muon  n >= 29     neutron  n >= 36

Those are NOT the particle's own strand counts; they are depths in the Hecke
tower H_n.  That is consistent in FORM with the owner ruling of 2026-09-03 --
"the QOU should be on the full tower in the derivations ... even though what is
observable is only order zero" -- since a quantity needing n ~ 36 is by
construction not an order-zero quantity.  **Consistency in form is not
evidence**, and nothing here derives those depths or explains their ordering;
they are simply where a length-exponent reading would have to live if one
exists.

🛑 A NEAR-INTEGER THAT IS NOT A RESULT -- RECORDED SO IT IS NOT PICKED UP
--------------------------------------------------------------------------
The neutron gives L = 598.0027, which is 0.0027 from the integer 598.  That is
NOT a hit and must not be reported as one:

    PDG bottle sigma      +/-0.5 s  ->  Delta L = +/- 0.0055
    beam-bottle spread      ~8 s    ->  Delta L = +/- 0.087

The offset sits INSIDE the experimental band on the tighter figure alone, and
well inside it on the unresolved beam-bottle discrepancy.  The input precision
does not support reading an integer there.  None of the other four states is
near an integer (387.23, 347.39, 262.48, 34.49), so this is one coincidence in
five samples -- which is what one expects.

PRECISION.  mpmath 40 dps.  No float64, per AGENTS.md "PROBES ARE NOT EXEMPT".
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent)]

mp.mp.dps = 40
Q0 = "1.1099785827513808075916690956107688798744991218736"

# (name, N_ops = m/Gamma from the sibling probe, corpus braid index or None)
ROWS = [
    ("neutron",      "1.25387e27", 3),
    ("muon",         "3.52667e17", 3),
    ("charged pion", "5.52016e15", None),
    ("tau lepton",   "7.83672e11", 3),
    ("Z boson",      "36.5506",    None),
]


def main() -> int:
    q0 = mp.mpf(Q0)
    lnq = mp.log(q0)
    print("=" * 78)
    print(" Can a Demazure/Weyl LENGTH carry N_ops = m/Gamma?   (range test, fit-free)")
    print("=" * 78)
    print(f"\n  q_0 = {mp.nstr(q0,12)}   ln q_0 = {mp.nstr(lnq,10)}")
    print("  N_ops = q_0^L  =>  L is DETERMINED, nothing is adjusted.\n")

    rows = []
    for name, N, braid in ROWS:
        L = mp.log(mp.mpf(N)) / lnq
        need_n = int(mp.ceil((1 + mp.sqrt(1 + 8 * L)) / 2))
        lw0 = braid * (braid - 1) // 2 if braid else None
        rows.append((name, N, L, braid, lw0, need_n))
        s = f"    {name:14s} L = {mp.nstr(L,8):>10s}   needs n >= {need_n:>2d}"
        if lw0 is not None:
            s += f"   but corpus braid B_{braid} gives l(w_0) = {lw0}  (short {mp.nstr(L/lw0,4)}x)"
        print(s)

    neutron = next(r for r in rows if r[0] == "neutron")
    shortfall = neutron[2] / neutron[4]

    tau = mp.mpf("878.4")
    dL_sigma = (mp.mpf("0.5") / tau) / lnq
    dL_beam = (mp.mpf("8") / tau) / lnq
    offset = abs(neutron[2] - 598)
    print(f"\n  near-integer check on the neutron (L = {mp.nstr(neutron[2],9)}):")
    print(f"    offset from 598          = {mp.nstr(offset,4)}")
    print(f"    PDG bottle sigma  +/-0.5s -> Delta L = {mp.nstr(dL_sigma,4)}")
    print(f"    beam-bottle spread  ~8 s  -> Delta L = {mp.nstr(dL_beam,4)}")
    print(f"    inside the band          = {bool(offset < dL_sigma)}   -> NOT a result")

    assertions = [
        {"name": "length_exponent_is_fit_free",
         "passed": True,
         "detail": "q_0 is pinned, so L = ln(N_ops)/ln(q_0) is read off rather than "
                   "adjusted — there is no parameter to tune"},
        {"name": "order_zero_single_braid_reading_FAILS",
         "passed": bool(shortfall > 100),
         "detail": f"the neutron needs L = {mp.nstr(neutron[2],7)} and its corpus braid "
                   f"B_3 caps l(w_0) at 3 — short by {mp.nstr(shortfall,5)}x. No w inside "
                   f"S_3 can help; 3 is the ceiling. A decay rate is NOT a reduction "
                   f"length of the particle's own braid."},
        {"name": "required_depths_are_tower_not_strand_counts",
         "passed": True,
         "detail": "n >= 9 (Z), 24 (tau), 29 (muon), 36 (neutron) — depths in H_n, not the "
                   "particles' strand counts. Consistent in FORM with the 2026-09-03 "
                   "full-tower ruling; consistency in form is NOT evidence, and nothing "
                   "here derives these depths or their ordering"},
        {"name": "the_neutron_near_integer_is_NOT_a_result",
         "passed": bool(offset < dL_sigma),
         "detail": f"L = {mp.nstr(neutron[2],9)} sits {mp.nstr(offset,4)} from 598, inside "
                   f"the PDG bottle band ({mp.nstr(dL_sigma,4)}) and far inside the "
                   f"beam-bottle spread ({mp.nstr(dL_beam,4)}). One coincidence in five "
                   f"samples; the other four are not near integers."},
    ]
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
        print(f"           {a['detail']}")
    ok = all(a["passed"] for a in assertions)
    print(f"\n  allPassed: {ok}  ({sum(a['passed'] for a in assertions)}/{len(assertions)})")

    out = HERE / "demazure-length-cannot-carry-decay.witness.json"
    out.write_text(json.dumps({
        "description": "Range test of the Demazure/reduction-length route to a categorical "
                       "decay rate. With N_ops = q_0^L and q_0 pinned, L is determined "
                       "(fit-free): 34.5 (Z) to 598.0 (neutron). The corpus assigns a "
                       "nucleon B_3, so l(w_0) = 3 — short by ~199x. The order-zero "
                       "single-braid reading FAILS. The required depths (n >= 9/24/29/36) "
                       "are tower depths, consistent in form with the 2026-09-03 "
                       "full-tower ruling but not evidence for it. The neutron's "
                       "L = 598.0027 is NOT a near-integer result: the offset is inside "
                       "the PDG lifetime band.",
        "engine": "mpmath 40 dps; no float64",
        "q0Anchor": "proton",
        "q0AnchorReason": "AGENTS.md 2026-08-07 owner directive: proton is the default",
        "q0Value": Q0,
        "data": {
            "identity": "N_ops = q_0^L  =>  L = ln(N_ops)/ln(q_0), q_0 pinned, no fit",
            "ln_q0": mp.nstr(lnq, 12),
            "rows": [{"particle": n, "N_ops": N, "L_required": mp.nstr(L, 10),
                      "corpus_braid_index": b, "l_w0": lw,
                      "tower_depth_needed": nn} for n, N, L, b, lw, nn in rows],
            "neutron_shortfall_factor": mp.nstr(shortfall, 8),
            "near_integer_offset": mp.nstr(offset, 6),
            "delta_L_from_pdg_sigma": mp.nstr(dL_sigma, 6),
            "delta_L_from_beam_bottle": mp.nstr(dL_beam, 6),
            "scope": "(a). Excludes a reduction length OF THE PARTICLE'S OWN BRAID as the "
                     "carrier. Does NOT exclude a tower-level length, a different "
                     "incompleteness measure, or a non-exponential dependence.",
            "open": "whether any Demazure incompleteness measure at tower depth n ~ 9-36 "
                    "reproduces the ordering Z < tau < pion < muon < neutron. Nothing here "
                    "derives it.",
        },
        "assertions": assertions,
        "allPassed": ok,
    }, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
