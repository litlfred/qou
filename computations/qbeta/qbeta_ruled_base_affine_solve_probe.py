#!/usr/bin/env python3
"""qbeta_ruled_base_affine_solve_probe.py — the Q_beta base is AFFINE in z, so
the whole one-parameter family is solvable: exactly one z reaches CODATA, and
it is not an admissible convention-D root.

Bean `qou-cds1` (re-derive the c_k ladder under convention D). Scope **(a)** —
every number here is numerics on the committed assembly.

## What was already known, and what this adds

`qbeta_ladder_form_cannot_reach_ruled_base_probe` proves the ladder's factor
`F(alpha) = cos(alpha - u/2)(1 - u^2) prod(1 + c_k u^k)` satisfies `F <= 1 - u^2
< 1` for EVERY real alpha, and the merged audit
`docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md` §5.1 adds
that pushing the shortfall into the rungs is excluded too — every recorded `c_k`
is negative, so each further rung shrinks `F` monotonically. Together: the FORM
is bounded by 1, so `Q_pred = Q_base * F <= Q_base`, and any base below CODATA
is permanently out of reach.

That settles the two admissible cells. It leaves the question the audit states
as live — *what object supplies a factor above 1 at all, about the base or the
assembly* — and it leaves one thing uncomputed: **whether any z reaches CODATA
at all.** Both prior results test the two roots. This tests the family.

## The assembly, reproduced from q_0 alone

From `per_observable_100x_status._qbeta_ruled_base`:

    tr_M(Delta_S)(z) = q^2/2 - q z - 1 + z/q + 1/(2 q^2)
    E_0              = m_e / (q (q - 1))
    Q_beta(z)        = |tr_M(Delta_S)(z)| * E_0

`tr` is AFFINE in z — `tr(z) = A + B z` with `A = q^2/2 - 1 + 1/(2q^2)` and
`B = 1/q - q < 0` — so `Q_beta` is monotone in z on the branch where `tr < 0`,
and inverting it is one line rather than a search. **No fit is involved and
none is possible:** a monotone affine map has exactly one preimage, so this
reports THE z, not a best one.

## Result

    z required for CODATA   0.99850030441113
    admissible D roots      {q = 1.10997858275, z_D = 0.61268803715}

Neither. The required z sits **0.15 % below the excluded `z = 1`** coordinate
sum — which is why that retired cell so nearly worked (`F_required` 0.9983) —
and 0.111 / 0.386 away from the two roots `ConventionDAdmissibleRoots` admits.

So the search over z is closed, negatively. The shortfall on the ruled base is
not a missing factor that some object might supply, and not a phase, and not a
rung: within this assembly it would have to be a different z, and the only z
that works is inadmissible. Any route to CODATA under D must change the
ELEMENT or the FUNCTIONAL, not the parameter.

**What this does NOT say.** It does not propose `z = 0.9985` as anything — it is
reported as the inadmissible preimage, and adopting it would be the forbidden
return to the coordinate sum (`ConventionDAdmissibleRoots.one_not_root`, and
`qbeta_d_frame_admissible_base_correction_search_probe` on the same trap). It
does not touch the C-frame ladder results, which stand on their own terms.

-- Ref: computations/qbeta/qbeta_ladder_form_cannot_reach_ruled_base_probe.py
-- Ref: docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md
-- Ref: computations/per_observable_100x_status.py::_qbeta_ruled_base
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
for _p in (ROOT, ROOT / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp                                            # noqa: E402
from _precision import set_compute_dps, fmt                    # noqa: E402
set_compute_dps()
import qou_substrate.constants as CONST                        # noqa: E402
from witness_base import WitnessBuilder                        # noqa: E402

#: The three cells the merged audit publishes, used as a CALIBRATION: if this
#: file's independent assembly does not reproduce them, the inversion below is
#: not trustworthy and the probe fails rather than reporting a number.
PUBLISHED = {
    "z_D (RULED)":        "0.444700408522",
    "z=q (augmentation)": "0.87989056126",
    "z=1 (retired)":      "0.783645827375",
}
#: `F_required` for the retired `z = 1` cell, from the same audit table. Used
#: ONLY to recover Q_codata from a published ratio, so no CODATA constant is
#: read here and the base stays derived from q_0 alone.
F_REQ_Z1 = "0.998325241673"


def main() -> int:
    q = mp.mpf(str(CONST.Q_50_DIGIT_STR))
    m_e = mp.mpf(str(CONST.M_E_MEV))
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)
    A = q**2 / 2 - 1 + 1 / (2 * q**2)
    B = 1 / q - q
    z_D = q**3 / (q**2 + 1)

    def tr(z):
        return A + B * z

    def Q(z):
        return abs(tr(z)) * E0

    cells = {"z_D (RULED)": z_D, "z=q (augmentation)": q, "z=1 (retired)": mp.mpf(1)}

    print("=" * 74)
    print(" Q_beta base is affine in z — solving the family, not the two roots")
    print("=" * 74)
    print(f"  E_0 = m_e/(q(q-1)) = {mp.nstr(E0, 12)} MeV")
    print(f"  tr(z) = A + B z    A = {mp.nstr(A, 12)}   B = {mp.nstr(B, 12)}")
    print()

    worst = mp.mpf(0)
    rows = []
    for nm, z in cells.items():
        got = Q(z)
        ref = mp.mpf(PUBLISHED[nm])
        rel = abs(got - ref) / ref
        worst = max(worst, rel)
        rows.append({"cell": nm, "z": fmt(z), "abs_tr": fmt(abs(tr(z))),
                     "Q_MeV": fmt(got), "published": PUBLISHED[nm],
                     "rel": fmt(rel)})
        print(f"  {nm:20s} z={mp.nstr(z, 12):>15s}  Q={mp.nstr(got, 12):>15s} MeV"
              f"   vs published {PUBLISHED[nm]}  (rel {mp.nstr(rel, 3)})")

    q_codata = Q(mp.mpf(1)) * mp.mpf(F_REQ_Z1)
    # tr < 0 on this branch, so |tr| = -(A + Bz)  =>  z = -(Q/E0 + A)/B
    z_req = (-q_codata / E0 - A) / B
    d_zD, d_q = abs(z_req - z_D), abs(z_req - q)
    admissible = bool(d_zD < mp.mpf("1e-9") or d_q < mp.mpf("1e-9"))

    print()
    print(f"  Q_codata (from the published z=1 F_required) = "
          f"{mp.nstr(q_codata, 12)} MeV")
    print(f"  z REQUIRED for CODATA                        = "
          f"{mp.nstr(z_req, 14)}")
    print(f"     distance to z_D {mp.nstr(d_zD, 6)}   to q {mp.nstr(d_q, 6)}"
          f"   to the excluded z=1 {mp.nstr(abs(z_req - 1), 6)}")
    print(f"     an admissible convention-D root? {admissible}")
    print()
    print("  -> The search over z is CLOSED, negatively. The ruled base's")
    print("     shortfall is not a factor, a phase or a rung; within this")
    print("     assembly it would have to be a different z, and the only z that")
    print("     works is inadmissible. A route to CODATA under D must change")
    print("     the ELEMENT or the FUNCTIONAL, not the parameter.")

    wb = WitnessBuilder("qbeta-ruled-base-affine-solve", engine="mpmath")
    wb.set_description(
        "The Q_beta base tr_M(Delta_S)(z)*E_0 is AFFINE in z, so the whole "
        "one-parameter family inverts in closed form. Exactly one z reaches "
        "CODATA and it is not an admissible convention-D root — it sits 0.15% "
        "below the excluded z=1 coordinate sum. Closes the search over z "
        "negatively; complements the F<=1 form bound, which closes the phase "
        "and the rungs."
    )
    wb.add_parameter("q0", fmt(q))
    wb.add_parameter("E0_MeV", fmt(E0))
    wb.add_data("affine_A", fmt(A))
    wb.add_data("affine_B", fmt(B))
    wb.add_data("cells", rows)
    wb.add_data("z_required_for_codata", fmt(z_req))
    wb.add_data("distance_to_z_D", fmt(d_zD))
    wb.add_data("distance_to_q", fmt(d_q))
    wb.add_assertion(
        name="assembly_reproduces_the_three_published_cells",
        computed=fmt(worst), expected="0", tolerance="1e-9",
        source="independent rebuild of tr_M(Delta_S)(z)*E_0 from q_0 against "
               "the three Q_base values in the merged 2026-09-13 audit §5.1")
    wb.add_assertion(
        name="required_z_is_NOT_an_admissible_convention_D_root",
        computed="0" if admissible else "1", expected="1", tolerance="0",
        source="z solving Q_beta(z) = Q_codata against the roots {q, z_D} of "
               "ConventionDAdmissibleRoots.admissible_markov_param_iff")
    out = wb.save()
    print(f"\n  witness: {out}")
    return 0 if (worst < mp.mpf("1e-9") and not admissible) else 1


if __name__ == "__main__":
    raise SystemExit(main())
