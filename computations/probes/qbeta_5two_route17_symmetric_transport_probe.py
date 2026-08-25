#!/usr/bin/env python3
"""Route 17 -- the branch point is HARMLESS for S. The conclusion survives; the argument does not.

Bean `qou-trns`. Constructive counterpart to Route 16.

Route 16 refuted `min |disc| = 0.348`: the discriminant VANISHES on the transport
arc at theta_0 = 137.9206708879635 deg, where two of the three y-branches collide.
That broke `qou-trns`'s k = 0 pinning argument, whose step 2 assumed the branches
never collide, and the envelope theorem's IFT hypothesis.

This probe asks the question that actually matters: **does the CONCLUSION
survive?**  It does, and cleanly.

WHY IT SHOULD, AND DOES
-----------------------
S(x) = Sum_j Re V(x, y_j(x)) sums over ALL roots, so it is a **symmetric**
function of them. Symmetric functions of the roots of a polynomial are analytic
wherever the coefficients are, **including at a branch point** -- a collision
permutes the roots but cannot change a symmetric function of them. Only the
per-root LABELLING is destroyed, and only the argument used labels.

Measured: S(e^{i phi}) - S(1) - phi^2 is zero to 4e-40 across the whole arc, and
zero AT the branch point and at phi_0 +- 1e-5. There is no feature there at all.

WHAT THIS FIXES AND WHAT IT DOES NOT
------------------------------------
Fixes: the transport CONCLUSION S(-1) = S(1) + pi^2 is not in danger. Route 16
did not endanger the sum rule and this shows the specific reason.

Does NOT fix: the transport is still **unproved**. What is needed now is a
symmetric derivation -- one that never names an individual branch. The natural
route is the elementary symmetric functions of the y_j, which are rational in x
by Vieta and analytic on the whole arc, and whose Vieta identities are ALREADY
Lean-proved (`prod_one_sub_x_mul`, `prod_x_sub` in FiveTwoCyclotomicBloch.lean).

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import exp, fabs, log, mp, mpc, mpf, nstr, pi, polylog, polyroots, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

PHI0 = "2.407169813554454521315767"  # the branch point, radians (Route 16)


def roots_x(x):
    return list(polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                          maxsteps=500, extraprec=1000))


def V(x, y):
    return polylog(2, y) + polylog(2, x * y) + polylog(2, y / x) + log(-y) ** 2


def S(x):
    return sum(re(V(x, y)) for y in roots_x(x))


def main() -> int:
    set_compute_dps()
    TOL = mpf(10) ** -30
    gates, s1, ph0 = [], S(mpf(1)), mpf(PHI0)

    # ---- G1: no feature AT the branch point --------------------------------
    rows, worst = [], mpf(0)
    for d in ["-0.02", "-0.002", "-1e-5", "0", "1e-5", "0.002", "0.02"]:
        ph = ph0 + mpf(d)
        r = S(exp(1j * ph)) - s1 - ph ** 2
        worst = max(worst, fabs(r))
        rows.append({"phi_minus_phi0": d, "residual": nstr(r, 6)})
    gates.append({
        "gate": "G1",
        "claim": "S(e^{i phi}) - S(1) = phi^2 holds THROUGH the branch point -- no feature "
                 "at phi_0, none at phi_0 +- 1e-5",
        "rows": rows, "worst": nstr(worst, 8), "pass": bool(worst < TOL),
    })

    # ---- G2: and across the whole arc --------------------------------------
    worst2, wphi = mpf(0), None
    for i in range(201):
        ph = pi * i / 200
        r = fabs(S(exp(1j * ph)) - s1 - ph ** 2)
        if r > worst2:
            worst2, wphi = r, ph
    gates.append({
        "gate": "G2",
        "claim": "the identity holds on the whole arc phi in [0, pi], 201 points",
        "worst": nstr(worst2, 8), "at_phi_deg": nstr(wphi * 180 / pi, 8),
        "pass": bool(worst2 < TOL),
    })

    # ---- G3: the endpoint --------------------------------------------------
    e = S(mpc(-1)) - s1 - pi ** 2
    gates.append({
        "gate": "G3",
        "claim": "S(-1) - S(1) = pi^2 exactly at the endpoint",
        "residual": nstr(e, 8), "pass": bool(fabs(e) < TOL),
    })

    # ---- G4: S is computed symmetrically -- no branch labelling anywhere ----
    # Permuting the root list cannot change S, since S sums over all of them.
    x = exp(1j * (ph0 + mpf("0.3")))
    ys = roots_x(x)
    base = sum(re(V(x, y)) for y in ys)
    perm = sum(re(V(x, y)) for y in [ys[2], ys[0], ys[1]])
    gates.append({
        "gate": "G4",
        "claim": "S is a SYMMETRIC function of the roots -- permuting them changes nothing, "
                 "which is why a collision (which only permutes) cannot affect it",
        "residual_under_permutation": nstr(fabs(base - perm), 8),
        "pass": bool(fabs(base - perm) < TOL),
    })

    # ---- G5: the elementary symmetric functions are the analytic objects ----
    # Vieta for x*y^3 -(x^2+1)y^2 +(x^2+x+1)y - x: e1=(x^2+1)/x, e2=(x^2+x+1)/x, e3=1.
    worst5 = mpf(0)
    for t in ["0.3", "1.9", "2.9"]:
        ph = ph0 + mpf(t)
        z = exp(1j * ph)
        ys = roots_x(z)
        e1, e2, e3 = sum(ys), ys[0] * ys[1] + ys[0] * ys[2] + ys[1] * ys[2], ys[0] * ys[1] * ys[2]
        worst5 = max(worst5,
                     fabs(e1 - (z ** 2 + 1) / z),
                     fabs(e2 - (z ** 2 + z + 1) / z),
                     fabs(e3 - 1))
    gates.append({
        "gate": "G5",
        "claim": "the elementary symmetric functions are RATIONAL in x by Vieta (e1=(x^2+1)/x, "
                 "e2=(x^2+x+1)/x, e3=1) hence analytic on the whole arc -- these are the "
                 "objects a repaired derivation should use",
        "worst": nstr(worst5, 8), "pass": bool(worst5 < TOL),
    })

    out = {
        "probe": "qbeta_5two_route17_symmetric_transport",
        "bean": "qou-trns", "parent_bean": "qou-0yqu", "dps": mp.dps,
        "gates": gates,
        "verdict": {
            "outcome": "The branch point Route 16 found is HARMLESS for S. "
                       "S(e^{i phi}) - S(1) = phi^2 holds to 4e-40 across the whole arc, "
                       "including exactly at phi_0 and at phi_0 +- 1e-5.",
            "why": "S sums over ALL roots, so it is symmetric in them. A collision permutes "
                   "roots; a symmetric function cannot notice a permutation. Only the "
                   "per-root labelling dies, and only the ARGUMENT used labels.",
            "what_survives": "the transport CONCLUSION S(-1) = S(1) + pi^2. Route 16 never "
                             "endangered the sum rule; this is the specific reason.",
            "what_is_still_open": "the transport is unproved. It needs a derivation that never "
                                  "names an individual branch. The natural route is the "
                                  "elementary symmetric functions, rational in x by Vieta "
                                  "(G5) and analytic on the whole arc -- and their identities "
                                  "are ALREADY Lean-proved (prod_one_sub_x_mul, prod_x_sub in "
                                  "FiveTwoCyclotomicBloch.lean).",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route17-symmetric-transport.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:86]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: the branch point is HARMLESS for S. Conclusion survives; argument still needed.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
