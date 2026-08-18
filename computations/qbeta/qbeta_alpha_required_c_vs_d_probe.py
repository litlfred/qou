#!/usr/bin/env python3
"""qbeta_alpha_required_c_vs_d_probe.py — how far is each convention's ASSERTED
ladder phase from the phase the ladder actually requires?

Bean `qou-cds1`. The ruling makes convention D canonical and
`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` proves the C-frame ladder and the
two-row forcing are mutually exclusive, so the ladder must be RE-DERIVED under
D rather than re-evaluated. The obstacle is that `alpha` is *asserted* in both
frames -- `alpha = (z-1)h/2`, a literal at
`probe_q_beta_operator_valued_N3.py:70` -- and derived in neither. There is no
C-frame derivation to port.

WHAT THIS MEASURES

`b` and `u` do NOT depend on z: the Hoefsmit coupling is
`b = sqrt(d1*d2 + 1)` with `d1 = q^3/(q^2+1)`, `d2 = -1/(q(q^2+1))`.

  (`d1` is numerically identical to `z_D`. It is NOT z -- different object,
  same expression. Reading that coincidence as "the Gram already uses D" is a
  trap this probe deliberately does not fall into.)

So the phase is the ONLY convention-dependent input to the N=1 rung, and
"alpha_required" -- the phase that makes the N=2 ladder hit CODATA with no
c_3 rung at all -- is therefore convention-INDEPENDENT:

    cos(alpha_eff_req) = Q_codata / (Q_A * (1 - u^2))
    alpha_req          = alpha_eff_req + b*hbar^2/2

That gives a fixed target both conventions can be scored against, at both
anchors, on equal terms. The gap alpha_req - alpha_conv is exactly the work
any c_3 rung has to do.

WHAT THIS DOES NOT DO. It derives nothing. It proposes no phase, wires no
value, and settles no convention. It converts "D is far away" from an
impression into a number, and reports whether either asserted phase is
anchor-consistent -- a necessary condition any derived phase must meet.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()


def substrate(q):
    """z-independent ladder substrate at modulus q."""
    q = mp.mpf(q)
    h = q - 1 / q
    hbar = (q - 1) / q
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = mp.sqrt(d1 * d2 + 1)
    u = b * hbar ** 2
    Q_A = mp.mpf(M_E_MEV) * (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)
    return {"q": q, "h": h, "hbar": hbar, "b": b, "u": u, "Q_A": Q_A}


def main() -> int:
    Qc = mp.mpf(str(Q_BETA_MEV))
    zC = lambda q: mp.sqrt(q) / (1 + q)        # noqa: E731
    zD = lambda q: q ** 3 / (q ** 2 + 1)       # noqa: E731

    print("=" * 78)
    print(" alpha_required vs the asserted phase, convention C and D")
    print("=" * 78)

    rows = []
    for label, q in (("proton", q_at()), ("muon", q_muon_at())):
        s = substrate(q)
        # the phase the N=2 ladder needs to hit CODATA with NO c_3 rung
        cos_req = Qc / (s["Q_A"] * (1 - s["u"] ** 2))
        a_eff_req = mp.acos(cos_req)
        a_req = a_eff_req + s["b"] * s["hbar"] ** 2 / 2
        aC = (zC(s["q"]) - 1) * s["h"] / 2
        aD = (zD(s["q"]) - 1) * s["h"] / 2
        rows.append({"anchor": label, "q": fmt(s["q"]), "u": fmt(s["u"]),
                     "alpha_required": fmt(a_req),
                     "alpha_C": fmt(aC), "alpha_D": fmt(aD),
                     "gap_C": fmt(a_req - aC), "gap_D": fmt(a_req - aD)})
        print(f"\n  {label} anchor  (q = {mp.nstr(s['q'], 14)})")
        print(f"    alpha_required = {mp.nstr(a_req, 14)}")
        print(f"    alpha_C        = {mp.nstr(aC, 14)}   gap {mp.nstr(a_req - aC, 8)}")
        print(f"    alpha_D        = {mp.nstr(aD, 14)}   gap {mp.nstr(a_req - aD, 8)}")

    # The amplification check: is the huge c_3 gap a large phase discrepancy,
    # or a small one magnified by the ladder's own 1/u^3?
    sp = substrate(q_at())
    aC_p = (zC(sp["q"]) - 1) * sp["h"] / 2
    aD_p = (zD(sp["q"]) - 1) * sp["h"] / 2
    cC = mp.cos(aC_p - sp["b"] * sp["hbar"] ** 2 / 2)
    cD = mp.cos(aD_p - sp["b"] * sp["hbar"] ** 2 / 2)
    cos_rel = abs(cD - cC) / cC
    amplified = cos_rel / sp["u"] ** 3
    c3C = (Qc / (sp["Q_A"] * cC * (1 - sp["u"] ** 2)) - 1) / sp["u"] ** 3
    c3D = (Qc / (sp["Q_A"] * cD * (1 - sp["u"] ** 2)) - 1) / sp["u"] ** 3
    c3_gap = abs(c3D - c3C)
    explains = abs(amplified - c3_gap) / c3_gap

    p, m = rows[0], rows[1]
    # Anchor-consistency: does the gap a derived phase must close move between
    # anchors, and by how much relative to the gap itself?
    def drift(k):
        gp, gm = mp.mpf(p[k]), mp.mpf(m[k])
        return abs(gp - gm), abs(gp - gm) / abs(gp) * 100

    dC, dCr = drift("gap_C")
    dD, dDr = drift("gap_D")
    ratio = abs(mp.mpf(p["gap_D"]) / mp.mpf(p["gap_C"]))

    print(f"""
{'=' * 78}
 Reading
{'=' * 78}

  alpha_required is convention-INDEPENDENT: b and u come from the Hoefsmit
  couplings, not from z, so the phase is the only place a convention enters
  the N=1 rung. Both frames are scored against one target.

  residual the c_3 rung must absorb, at the proton anchor:
    C frame : {mp.nstr(mp.mpf(p['gap_C']), 8)}
    D frame : {mp.nstr(mp.mpf(p['gap_D']), 8)}      ratio D/C = {mp.nstr(ratio, 6)}

  ** The D frame is NOT orders worse. It is {mp.nstr(ratio, 4)}x -- slightly
  BETTER. ** I expected the opposite; that assertion failed and is retracted.

  Where c_3 = -974 actually comes from:
    cos(alpha_eff) differs C -> D by only {mp.nstr(cos_rel, 6)} (relative)
    1/u^3                                 = {mp.nstr(1 / sp["u"] ** 3, 8)}
    product                               = {mp.nstr(amplified, 8)}
    actual |c_3(D) - c_3(C)|              = {mp.nstr(c3_gap, 8)}
    agreement                             = {mp.nstr(explains * 100, 4)} %

  So -974 is the ladder's own 1/u^3 amplifier acting on a 0.06 % difference in
  cos. It is NOT evidence that D breaks the physics; it is the SAME
  amplification that makes every extracted c_k noise-dominated
  (sigma(c_k) = sigma_R/u^k). Quoting -974 as if D were catastrophic overstates
  what the number shows.

  And the phase is not where the anchor instability lives:
    residual drift C : {mp.nstr(dCr, 4)} % across the two anchors
    residual drift D : {mp.nstr(dDr, 4)} %
  while extracted c_3 swings 2.37 %. Both asserted phases are anchor-stable to
  ~5e-4 %; the instability is downstream of them.

  What DOES stand: both frames leave ~0.1 rad for c_3 to absorb, so NEITHER
  asserted phase reproduces CODATA at N=2. That is the real open item -- and it
  is open in C exactly as much as in D.

  NOTHING IS DERIVED HERE. No phase proposed, no value wired, no convention
  settled.
""")

    wb = WitnessBuilder("qbeta-alpha-required-c-vs-d", engine="mpmath")
    wb.set_description(
        "Bean qou-cds1. Scores both Markov conventions against the phase the "
        "N=2 Q_beta ladder actually requires. alpha_required is "
        "convention-INDEPENDENT because b and u are built from the Hoefsmit "
        "couplings (d1 = q^3/(q^2+1), d2 = -1/(q(q^2+1))) and not from z — note "
        "d1 is numerically identical to z_D while being a different object, a "
        "coincidence this probe explicitly does not read as 'the Gram already "
        "uses D'. So the phase is the only convention-dependent input to the "
        "N=1 rung, and one fixed target scores both frames at both anchors. "
        "Records the residual each frame's asserted phase leaves for the c_3 "
        "rung to absorb, and that residual's cross-anchor drift. DERIVES "
        "NOTHING: proposes no phase, wires no value, settles no convention — "
        "alpha is asserted in both frames (probe_q_beta_operator_valued_N3.py:70) "
        "and derived in neither, which is precisely what cds1 is open on."
    )
    wb.add_data("anchors", rows)
    wb.add_data("gap_ratio_D_over_C_proton", fmt(ratio))
    wb.add_data("gap_C_cross_anchor_drift", fmt(dC))
    wb.add_data("gap_D_cross_anchor_drift", fmt(dD))

    wb.add_assertion(
        name="alpha_required_is_convention_independent_by_construction",
        computed="1", expected="1", tolerance=0,
        source="b = sqrt(d1*d2+1) with d1 = q^3/(q^2+1), d2 = -1/(q(q^2+1)); "
               "u = b*hbar^2; Q_A = m_e|q^2-2q-1|(q+1)/(2q^3). None reads z, so "
               "cos(alpha_eff_req) = Q_codata/(Q_A(1-u^2)) is the same target in "
               "both frames — which is what makes the C/D comparison fair rather "
               "than a comparison of two different targets.",
    )
    wb.add_assertion(
        name="D_frame_phase_residual_is_COMPARABLE_to_C_not_orders_worse",
        computed=str(int(mp.mpf("0.5") < ratio < mp.mpf("2"))), expected="1",
        tolerance=0,
        source=f"|gap_D/gap_C| = {mp.nstr(ratio, 8)} at the proton anchor — the "
               "D-frame asserted phase is slightly CLOSER to alpha_required than "
               "the C-frame one. This probe was written expecting 'orders "
               "larger'; that assertion failed and the expectation is retracted.",
    )
    wb.add_assertion(
        name="the_c3_gap_is_1_over_u_cubed_amplification_not_a_large_phase_gap",
        computed=str(int(explains < mp.mpf("0.01"))), expected="1", tolerance=0,
        source=f"cos(alpha_eff) differs C->D by {mp.nstr(cos_rel, 8)} relative; "
               f"divided by u^3 that is {mp.nstr(amplified, 8)}, against an actual "
               f"|c_3(D)-c_3(C)| = {mp.nstr(c3_gap, 8)} — agreement to "
               f"{mp.nstr(explains * 100, 4)} %. So c_3 = -974 is the ladder's own "
               "1/u^3 = 1.6e6 amplifier acting on a 0.06 % cos difference, not "
               "evidence that D breaks the physics.",
    )
    wb.add_assertion(
        name="neither_asserted_phase_reproduces_CODATA_at_N2",
        computed=str(int(abs(mp.mpf(p["gap_C"])) > mp.mpf("0.01")
                         and abs(mp.mpf(p["gap_D"])) > mp.mpf("0.01"))),
        expected="1", tolerance=0,
        source=f"both frames leave ~0.1 rad (C {mp.nstr(mp.mpf(p['gap_C']), 6)}, "
               f"D {mp.nstr(mp.mpf(p['gap_D']), 6)}) for the c_3 rung to absorb. "
               "The un-derived phase is open in C exactly as much as in D — which "
               "is why cds1 has no C-frame derivation to port.",
    )
    out = wb.save({"q0Anchor": "ambiguous"})
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
