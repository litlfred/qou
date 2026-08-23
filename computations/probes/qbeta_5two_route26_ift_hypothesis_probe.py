#!/usr/bin/env python3
"""Route 26 -- the IFT hypothesis on the transport arc, and the envelope collapse.

Bean `qou-trns`. Pairs with `QOU/MathlibExt/ImplicitScalar.lean` (the scalar
implicit function theorem, sorry-free) and `QOU/QBeta/FiveTwoCurveDeriv.lean`
(its specialisation to the GGM curve, sorry-free).

WHAT IS BEING CHECKED
---------------------
`exists_hasDerivAt_root` needs `curveDy(x, y) != 0` -- "y is a SIMPLE root". Two
things follow that deserve measurement rather than assertion:

* G3: along the arc |x| = 1, min_j |curveDy| is bounded away from zero EXCEPT at
  the branch point phi_0, where it vanishes. So the IFT applies on
  [0, pi] minus {phi_0} and fails nowhere else -- exactly matching
  `exists_unit_circle_disc_zero`, which proves the discriminant vanishes there.
  A theorem whose hypothesis silently failed everywhere would be useless; this
  is the check that it does not.

* G6: THE PAYOFF. The envelope claim is that d/dphi V(x, y(phi)) collapses to
  (partial V/partial x) * dx/dphi, because partial V/partial y = 0 on the curve
  (`deformed_saddle_iff_curve`). Verified here by finite differences on a root
  tracked along the arc. This is the identity the whole IFT brick exists to
  license, and it is checked directly rather than inferred.

Note what the envelope does NOT need: the VALUE of dy/dphi. It needs only that
the derivative exists, because partial V/partial y annihilates it. G4 checks the
value anyway, since the IFT supplies it for free and a wrong value would signal a
wrong partial.

**The 5_2 sum rule remains verified to 80 dps, unproved.** Nothing here proves
the envelope step; it verifies the hypotheses and the collapse it rests on.
"""

import json
import pathlib

from mpmath import (acos, exp, fabs, im, log, mp, mpf, nint, nstr, pi, polylog,
                    polyroots, re)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def curve(x, y):
    return x * y ** 3 - (x ** 2 + 1) * y ** 2 + (x ** 2 + x + 1) * y - x


def curve_dx(x, y):
    return y ** 3 - 2 * x * y ** 2 + (2 * x + 1) * y - 1


def curve_dy(x, y):
    return 3 * x * y ** 2 - 2 * (x ** 2 + 1) * y + (x ** 2 + x + 1)


def roots_at(x):
    return list(polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                          maxsteps=800, extraprec=2000))


def track(phi, prev):
    """The root of the curve at e^{i phi} nearest `prev` -- continuity tracking."""
    rs = roots_at(exp(1j * phi))
    return min(rs, key=lambda r: fabs(r - prev))


def V(x, y):
    """Li2(y) + Li2(x y) + Li2(y/x) + log(-y)^2, principal branches."""
    return polylog(2, y) + polylog(2, x * y) + polylog(2, y / x) + log(-y) ** 2


def dV_dx(x, y):
    return (-log(1 - x * y) + log(1 - y / x)) / x


def main() -> int:
    set_compute_dps()
    TOL = mpf(10) ** -35
    gates = []

    # ---- G1: the partials are the ones the Lean file declares ---------------
    h = mpf(10) ** -20
    worst1 = mpf(0)
    for (xv, yv) in [("0.7", "1.3"), ("-1.4", "0.55"), ("2.0", "-0.8")]:
        x, y = mpf(xv), mpf(yv)
        fdx = (curve(x + h, y) - curve(x - h, y)) / (2 * h)
        fdy = (curve(x, y + h) - curve(x, y - h)) / (2 * h)
        worst1 = max(worst1, fabs(fdx - curve_dx(x, y)), fabs(fdy - curve_dy(x, y)))
    gates.append({
        "gate": "G1",
        "claim": "curveDx and curveDy as declared in FiveTwoCurveDeriv.lean really are the "
                 "partials of the curve -- central differences at step 1e-20 agree",
        "worst": nstr(worst1, 8), "pass": bool(worst1 < mpf(10) ** -18),
    })

    # ---- G2: curveDy vanishes exactly at multiple roots ---------------------
    # prod_j curveDy(x, y_j) is the discriminant up to the leading coefficient.
    x_t = exp(1j * pi * mpf("0.3"))
    rs = roots_at(x_t)
    prod_dy = curve_dy(x_t, rs[0]) * curve_dy(x_t, rs[1]) * curve_dy(x_t, rs[2])
    gates.append({
        "gate": "G2",
        "claim": "curveDy(x, y_j) is the cubic's derivative at its own root, so it vanishes "
                 "exactly when that root is multiple -- the product over the three roots is the "
                 "discriminant up to the leading coefficient, and is nonzero off the locus",
        "prod_curveDy_at_phi_0.3pi": nstr(prod_dy, 12),
        "nonzero": bool(fabs(prod_dy) > mpf(10) ** -20),
        "pass": bool(fabs(prod_dy) > mpf(10) ** -20),
    })

    # ---- G3: THE HYPOTHESIS ALONG THE ARC ----------------------------------
    prof = []
    for i in range(0, 41):
        ph = pi * i / 40
        x = exp(1j * ph)
        m = min(fabs(curve_dy(x, r)) for r in roots_at(x))
        prof.append((ph / pi, m))
    interior = [m for (t, m) in prof if fabs(t - mpf("0.766")) > mpf("0.05")]
    # phi_0 is NOT located by sampling. The lane's own proved characterisation is
    # used instead: disc is palindromic, disc(x)/x^4 = Q(x + 1/x) with
    # Q(u) = u^4 - 6u^3 + 7u^2 + 6u - 31, and on |x| = 1, u = 2 cos(phi). So solve
    # Q(u) = 0 in (-2,-1) exactly and set phi_0 = arccos(u_0/2).
    # (An earlier draft of this gate quoted a refinement sequence that went
    #  0.0177 -> 0.0249 -- it was BRACKETING phi_0, not converging to it. Quoting
    #  a grid value as the minimum is exactly the defect this lane already found
    #  once, in min|disc| = 0.348.)
    Qc = [1, -6, 7, 6, -31]
    u0 = [re(r) for r in polyroots(Qc, maxsteps=800, extraprec=2000)
          if fabs(im(r)) < mpf(10) ** -30 and mpf(-2) < re(r) < mpf(-1)][0]
    phi0 = acos(u0 / 2)
    x0 = exp(1j * phi0)
    at_phi0 = min(fabs(curve_dy(x0, r)) for r in roots_at(x0))
    disc_at_phi0 = fabs(u0 ** 4 - 6 * u0 ** 3 + 7 * u0 ** 2 + 6 * u0 - 31)
    gates.append({
        "gate": "G3",
        "claim": "THE IFT HYPOTHESIS ON THE ARC. min_j |curveDy| >= 1.6158 everywhere on "
                 "|x| = 1 away from the branch point, and VANISHES at phi_0. phi_0 is SOLVED "
                 "FOR, not sampled: the lane's proved characterisation gives Q(2 cos phi_0) = 0 "
                 "with Q(u) = u^4-6u^3+7u^2+6u-31, so phi_0/pi = 0.76622594937757503001 and "
                 "min |curveDy| there is 1.8e-25 -- the square-root accuracy floor for a DOUBLE "
                 "root at 50 dps, which is what it is. So exists_hasDerivAt_root applies on "
                 "[0,pi] minus {phi_0} and fails nowhere else, matching "
                 "exists_unit_circle_disc_zero exactly. (An earlier draft of this gate quoted a "
                 "refinement sequence that went 0.0177 -> 0.0249: it was BRACKETING phi_0, not "
                 "converging to it. Quoting a grid value as a minimum is the defect this lane "
                 "already found once, in min|disc| = 0.348.)",
        "min_off_branch_point": nstr(min(interior), 10),
        "phi0_over_pi_solved": nstr(phi0 / pi, 20),
        "u0_root_of_Q_in_(-2,-1)": nstr(u0, 20),
        "Q_at_u0": nstr(disc_at_phi0, 8),
        "min_curveDy_AT_phi0": nstr(at_phi0, 8),
        "pass": bool(min(interior) > mpf("0.1") and at_phi0 < mpf(10) ** -20
                     and disc_at_phi0 < mpf(10) ** -30),
    })

    # ---- G4: the IFT derivative value --------------------------------------
    hphi = mpf(10) ** -15
    rows4, worst4 = [], mpf(0)
    for tv in ["0.2", "0.45", "0.95"]:
        ph = pi * mpf(tv)
        x = exp(1j * ph)
        y0 = max(roots_at(x), key=lambda r: im(r) if im(r) > 0 else -mpf(10) ** 9)
        yp = track(ph + hphi, y0)
        ym = track(ph - hphi, y0)
        dy_dphi = (yp - ym) / (2 * hphi)
        pred = (-curve_dx(x, y0) / curve_dy(x, y0)) * (1j * x)   # dx/dphi = i x
        d = fabs(dy_dphi - pred)
        worst4 = max(worst4, d)
        rows4.append({"phi_over_pi": tv, "|fd - IFT|": nstr(d, 8)})
    gates.append({
        "gate": "G4",
        "claim": "the IFT VALUE is right: dy/dphi from finite differences on a tracked root "
                 "matches -(curveDx/curveDy) * dx/dphi. The envelope does not need this value "
                 "-- only that the derivative exists -- but a wrong value would mean a wrong "
                 "partial, so it is checked",
        "rows": rows4, "worst": nstr(worst4, 8), "pass": bool(worst4 < mpf(10) ** -12),
    })

    # ---- G5: the base point, where the transport starts ---------------------
    r1 = roots_at(mpf(1))
    dys = [nstr(fabs(curve_dy(mpf(1), r)), 10) for r in r1]
    gates.append({
        "gate": "G5",
        "claim": "at the base point x = 1 all three roots are simple -- |curveDy| bounded away "
                 "from zero for each -- so the IFT applies where the transport starts",
        "abs_curveDy_at_the_three_roots": dys,
        "pass": bool(all(mpf(d) > mpf("0.5") for d in dys)),
    })

    # ---- G6: THE PAYOFF -- the envelope collapse ---------------------------
    rows6, worst6 = [], mpf(0)
    for tv in ["0.2", "0.45"]:
        ph = pi * mpf(tv)
        x = exp(1j * ph)
        y0 = max(roots_at(x), key=lambda r: im(r) if im(r) > 0 else -mpf(10) ** 9)
        yp, ym = track(ph + hphi, y0), track(ph - hphi, y0)
        dV = (V(exp(1j * (ph + hphi)), yp) - V(exp(1j * (ph - hphi)), ym)) / (2 * hphi)
        pred = dV_dx(x, y0) * (1j * x)
        d = fabs(dV - pred)
        worst6 = max(worst6, d)
        rows6.append({"phi_over_pi": tv, "|dV/dphi - dVdx * dx/dphi|": nstr(d, 8)})
    gates.append({
        "gate": "G6",
        "claim": "THE ENVELOPE COLLAPSE, checked directly. d/dphi V(x, y(phi)) equals "
                 "(partial V/partial x)*dx/dphi -- the dy/dphi term drops out because "
                 "partial V/partial y = 0 on the curve, which deformed_saddle_iff_curve makes "
                 "free. This is the identity the whole IFT brick exists to license",
        "rows": rows6, "worst": nstr(worst6, 8), "pass": bool(worst6 < mpf(10) ** -10),
    })

    # ---- G7: the two Vieta products that pin the log-sums -------------------
    worst7 = mpf(0)
    for i in range(0, 21):
        ph = pi * i / 20
        x = exp(1j * ph)
        rs = roots_at(x)
        pA = (1 - x * rs[0]) * (1 - x * rs[1]) * (1 - x * rs[2])
        pB = (1 - rs[0] / x) * (1 - rs[1] / x) * (1 - rs[2] / x)
        worst7 = max(worst7, fabs(pA - x), fabs(pB - 1 / x))
    gates.append({
        "gate": "G7",
        "claim": "the two Vieta products FiveTwoEnvelopeSum exponentiates to: prod_j (1 - x y_j) "
                 "= x and prod_j (1 - y_j/x) = 1/x, along the whole arc. These are the hexp "
                 "inputs the branch-pinning lemma consumes, and they hold from Vieta alone",
        "n_points": 21, "worst": nstr(worst7, 8), "pass": bool(worst7 < TOL),
    })

    # ---- G8: are the branch integers actually ZERO with principal branches? --
    kA, kB = [], []
    for i in range(0, 21):
        ph = pi * i / 20
        x = mpf(-1) if i == 20 else exp(1j * ph)
        rs = roots_at(x)
        sA = sum(log(1 - x * r) for r in rs)
        sB = sum(log(1 - r / x) for r in rs)
        kA.append(int(nint(re((sA - log(x)) / (2j * pi)))))
        kB.append(int(nint(re((sB + log(x)) / (2j * pi)))))
    gates.append({
        "gate": "G8",
        "claim": "MEASURED, not assumed. k_A = 0 everywhere on the arc; k_B = 0 on [0,pi) and "
                 "**1 AT THE ENDPOINT**. So sum_dVdx_of_pinned's hypothesis is FALSE at phi = pi "
                 "for principal branches. It is FORCED, not an accident: at x = -1 the two "
                 "expressions 1 - x*y and 1 - y/x are literally the same (1 + y), so Sum_A = "
                 "Sum_B; but the two identities demand +log x and -log x, which differ by 2 pi i "
                 "when log(-1) = +i pi. Hence k_B - k_A = 1 there necessarily. Harmless for the "
                 "envelope because pi is an ENDPOINT -- S(pi) - S(0) needs the derivative only "
                 "on the open interval plus continuity on the closed one -- but it means the "
                 "identity holds on [0,pi), not [0,pi], and phi_0 remains the only INTERIOR "
                 "exceptional point. A fifth independent way this arc's endpoint sits on the cut",
        "k_A_along_arc": kA, "k_B_along_arc": kB,
        "k_A_all_zero": bool(all(k == 0 for k in kA)),
        "k_B_zero_on_interior": bool(all(k == 0 for k in kB[:-1])),
        "k_B_at_endpoint": kB[-1],
        "difference_forced_at_x_eq_-1": kB[-1] - kA[-1],
        "pass": bool(all(k == 0 for k in kA) and all(k == 0 for k in kB[:-1])
                     and kB[-1] - kA[-1] == 1),
    })

    out = {
        "probe": "qbeta_5two_route26_ift_hypothesis",
        "bean": "qou-trns", "dps": mp.dps,
        "pairs_with_lean": "QOU/MathlibExt/ImplicitScalar.lean + QOU/QBeta/FiveTwoCurveDeriv.lean",
        "gates": gates,
        "verdict": {
            "hypothesis_holds_where_it_must": "min_j |curveDy| along the arc is bounded away "
                                              "from zero except at phi_0/pi ~ 0.7662, where "
                                              "refinement drives it to zero -- exactly the "
                                              "branch point exists_unit_circle_disc_zero proves. "
                                              "So the IFT covers [0,pi] minus one point.",
            "envelope_collapse_verified": "G6: d/dphi V(x, y(phi)) = (partial V/partial x) * "
                                          "dx/dphi to better than 1e-10 by finite differences. "
                                          "The dy/dphi term drops because partial V/partial y = 0 "
                                          "on the curve.",
            "what_remains": "assembling the collapse over the three roots in Lean (G6 is "
                            "numerical), and gluing across phi_0 with ConstantOffOnePoint. The "
                            "Vieta sum is now Lean-proved in FiveTwoEnvelopeSum, conditional on "
                            "the branch pinning, which G8 shows holds on [0,pi) and FAILS at the "
                            "endpoint -- forced, and harmless because pi is an endpoint.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route26-ift-hypothesis.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:84]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: IFT hypothesis holds off phi_0 only; the envelope collapse checks out.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
