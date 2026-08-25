#!/usr/bin/env python3
"""qbeta_eigenphase_branch_and_barodd_projection_probe.py — the ladder phase in
the amplifier-free coordinate, and what the bar-odd projection actually buys.

Bean `qou-cds1`. Two results, one of which RETRACTS an earlier claim of mine.

## 1. RETRACTION: "neither asserted phase reproduces CODATA at N=2"

`qbeta_alpha_required_c_vs_d_probe` (mine, 2026-08-18) reported that both
conventions leave "~0.1 rad for the c_3 rung to absorb", and concluded that
the un-derived phase is open in C exactly as much as in D. **That is wrong,
and the error is elementary: `cos` is EVEN, and `mp.acos` returns only the
principal (positive) branch.**

    cos(alpha_eff_req) = Q_codata / (Q_A (1 - u^2))

is solved by BOTH `+alpha_eff_req` and `-alpha_eff_req`. The convention-C
phase sits on the NEGATIVE branch. Measured against the nearest branch its
residual is `2.26e-5` rad, not `0.113`. That tiny residual, amplified by
`1/u^3 = 1.6e6` (QOU.QBeta.c3Of_sub_mul_u_cubed), is exactly the observed
`c_3 = -2.069`. The old figure was the distance to the WRONG branch, and it
was ~5000x too large.

## 2. What the bar-odd projection buys, in the right coordinate

`qbeta-d-frame-eigenphase-bar-parity` (2026-08-16) established, symbolically:

  * under C the eigenphase is bar-odd, `bar(alpha) + alpha = 0`;
  * under D (full-bar `bar(z) = z - h`) it is not, with a **z-independent**
    defect `bar(alpha) + alpha = h^2/2`;
  * so the forced bar-odd projection is `alpha - h^2/4`, and it moves
    `c_3` from `-974.43` to `-86.08` -- recorded there as "improves
    substantially but does NOT restore the C-frame numbers".

Through `c_3` that reads like a failure: `-86` still looks nothing like `-2`.
In the amplifier-free coordinate it reads very differently, because `c_3`
exaggerates every phase difference by `1/u^3`.

**This probe proposes NO correction and searches NO space.** It evaluates the
single already-derived projection in the coordinate where the numbers are not
inflated. That distinction matters: the source witness explicitly fences
further correction-hunting as fitting, and this respects that fence -- it adds
a coordinate, not a candidate.

Anchors: proton (default) and muon.
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
    q = mp.mpf(q)
    h = q - 1 / q
    hbar = (q - 1) / q
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = mp.sqrt(d1 * d2 + 1)
    u = b * hbar ** 2
    Q_A = mp.mpf(M_E_MEV) * (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)
    return {"q": q, "h": h, "hbar": hbar, "b": b, "u": u, "Q_A": Q_A,
            "half": b * hbar ** 2 / 2}


def main() -> int:
    Qc = mp.mpf(str(Q_BETA_MEV))
    print("=" * 78)
    print(" The ladder phase in the amplifier-free coordinate")
    print("=" * 78)

    rows = []
    for label, q in (("proton", q_at()), ("muon", q_muon_at())):
        s = substrate(q)
        h, u, QA, half = s["h"], s["u"], s["Q_A"], s["half"]
        zC = mp.sqrt(s["q"]) / (1 + s["q"])
        zD = s["q"] ** 3 / (s["q"] ** 2 + 1)
        a_req = mp.acos(Qc / (QA * (1 - u ** 2)))          # principal branch

        print(f"\n  {label}:  alpha_eff_req = ±{mp.nstr(a_req, 14)}  "
              f"(cos is EVEN — BOTH branches solve it)")
        print(f"    {'phase':<12}{'alpha_eff':>17}{'gap(+)':>13}"
              f"{'gap(-)':>14}{'NEAREST':>14}{'c_3':>14}")
        print("    " + "-" * 84)

        entry = {"anchor": label, "alpha_eff_required_principal": fmt(a_req),
                 "h_sq_over_4": fmt(h ** 2 / 4), "phases": []}
        for nm, a in (("C", (zC - 1) * h / 2),
                      ("D", (zD - 1) * h / 2),
                      ("D - h^2/4", (zD - 1) * h / 2 - h ** 2 / 4)):
            aeff = a - half
            gp, gm = a_req - aeff, -a_req - aeff
            near = gm if abs(gm) < abs(gp) else gp
            branch = "-" if abs(gm) < abs(gp) else "+"
            c3 = (Qc / (QA * mp.cos(aeff) * (1 - u ** 2)) - 1) / u ** 3
            print(f"    {nm:<12}{mp.nstr(aeff, 12):>17}{mp.nstr(gp, 6):>13}"
                  f"{mp.nstr(gm, 6):>14}{mp.nstr(near, 6):>14}{mp.nstr(c3, 8):>14}")
            entry["phases"].append({
                "name": nm, "alpha_eff": fmt(aeff),
                "gap_to_plus_branch": fmt(gp), "gap_to_minus_branch": fmt(gm),
                "nearest_branch": branch, "nearest_gap": fmt(near),
                "c3": fmt(c3)})
        rows.append(entry)

    p = rows[0]["phases"]
    gC, gD, gP = (abs(mp.mpf(p[i]["nearest_gap"])) for i in (0, 1, 2))
    closed = (1 - gP / gD) * 100
    short_of_C = gP / gC
    # the old, wrong figure: distance to the principal branch
    old_gap = abs(mp.mpf(p[0]["gap_to_plus_branch"]))
    overstatement = old_gap / gC

    print(f"""
{'=' * 78}
 Reading
{'=' * 78}

  ** RETRACTION. ** My earlier probe reported that both conventions leave
  ~0.1 rad for c_3 to absorb, and that "neither asserted phase reproduces
  CODATA at N=2". Both statements are WRONG. `cos` is even, `mp.acos` returns
  only the principal branch, and the C phase sits on the NEGATIVE one:

      distance to the + branch (what I reported) : {mp.nstr(old_gap, 8)}
      distance to the - branch (the real one)    : {mp.nstr(gC, 8)}
      overstatement factor                       : {mp.nstr(overstatement, 6)}x

  The C phase reproduces CODATA at N=2 to {mp.nstr(gC, 6)} rad. Amplified by
  1/u^3 = 1.6e6 that IS the observed c_3 = -2.069 — which is the consistency
  check my earlier framing could not have passed, and I did not run it.

  ** What the bar-odd projection buys. ** Through c_3 the derived projection
  alpha - h^2/4 reads as a failure: -974 -> -86, still nothing like -2. In the
  amplifier-free coordinate:

      D phase gap            : {mp.nstr(gD, 8)}
      after alpha - h^2/4    : {mp.nstr(gP, 8)}
      closed                 : {mp.nstr(closed, 5)} % of the D gap
      still short of C by    : {mp.nstr(short_of_C, 5)}x

  So ONE structurally-forced correction — not fitted, forced by requiring the
  bar-oddness that holds identically under C — recovers {mp.nstr(closed, 4)} % of the phase
  discrepancy. "Improves substantially but does not restore" is right, and the
  amount is {mp.nstr(closed, 4)} %, not the ~91 % improvement in c_3 that the inflated
  coordinate suggests.

  This STRENGTHENS the D programme rather than the reverse: the D phase is not
  wild, it is one derived correction and a {mp.nstr(short_of_C, 3)}x residual away from the
  frame that works.

  NO correction is proposed and NO space is searched — the source witness
  fences further correction-hunting as fitting, and this adds a coordinate,
  not a candidate. alpha remains asserted in both frames and derived in
  neither.
""")

    wb = WitnessBuilder("qbeta-eigenphase-branch-and-barodd-projection",
                        engine="mpmath")
    wb.set_description(
        "Bean qou-cds1. (1) RETRACTS my own qbeta_alpha_required_c_vs_d claim "
        "that both conventions leave ~0.1 rad for c_3 and that neither phase "
        "reproduces CODATA at N=2: cos is EVEN and mp.acos returns only the "
        "principal branch, so that figure was the distance to the WRONG branch, "
        "overstated ~5000x. The C phase sits on the negative branch with a "
        "residual of 2.26e-5 rad, which under the proved 1/u^3 amplification "
        "(QOU.QBeta.c3Of_sub_mul_u_cubed) is exactly the observed c_3 = -2.069. "
        "(2) Re-expresses the already-derived bar-odd projection alpha - h^2/4 "
        "(from qbeta-d-frame-eigenphase-bar-parity, where the D-frame defect "
        "bar(alpha)+alpha = h^2/2 is symbolic-exact and z-independent) in that "
        "amplifier-free coordinate: it closes ~92% of the D phase gap, leaving "
        "a residual ~42x the C-frame one. Through c_3 alone that correction "
        "reads as a failure (-974 -> -86); in phase space it is most of the way "
        "there. PROPOSES NO CORRECTION and SEARCHES NO SPACE — the source "
        "witness fences further correction-hunting as fitting; this adds a "
        "coordinate, not a candidate. alpha remains asserted in both frames and "
        "derived in neither."
    )
    wb.add_data("ladder_frame", "u")
    wb.add_data("anchors", rows)
    wb.add_data("barodd_projection_closes_pct_of_D_gap", fmt(closed))
    wb.add_data("residual_multiple_of_C_gap", fmt(short_of_C))
    wb.add_data("previous_claim_overstatement_factor", fmt(overstatement))

    wb.add_assertion(
        name="RETRACTED_the_C_phase_does_reproduce_CODATA_via_the_negative_branch",
        computed=str(int(gC < mp.mpf("1e-4"))), expected="1", tolerance=0,
        source=f"the C phase's residual against the NEAREST arccos branch is "
               f"{mp.nstr(gC, 8)} rad, not the {mp.nstr(old_gap, 6)} I reported "
               f"({mp.nstr(overstatement, 5)}x overstatement) — I compared only to "
               "the principal branch although cos is even. Amplified by 1/u^3 "
               "this reproduces c_3 = -2.069, the consistency check the earlier "
               "framing would have failed.",
    )
    wb.add_assertion(
        name="barodd_projection_closes_most_of_the_D_phase_gap",
        computed=str(int(closed > 90)), expected="1", tolerance=0,
        source=f"the derived projection alpha - h^2/4 takes the D phase gap from "
               f"{mp.nstr(gD, 8)} to {mp.nstr(gP, 8)} rad, closing "
               f"{mp.nstr(closed, 5)}%. Invisible through c_3, which only shows "
               "-974 -> -86 because 1/u^3 inflates every phase difference.",
    )
    wb.add_assertion(
        name="a_real_residual_remains_after_the_projection",
        computed=str(int(short_of_C > 10)), expected="1", tolerance=0,
        source=f"the post-projection gap is {mp.nstr(short_of_C, 5)}x the C-frame "
               "residual, so bar-oddness is necessary and not sufficient — the "
               "source witness's verdict, now quantified in the coordinate where "
               "it is not inflated by the amplifier.",
    )
    out = wb.save({"q0Anchor": "ambiguous"})
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
