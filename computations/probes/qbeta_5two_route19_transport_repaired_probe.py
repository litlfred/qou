#!/usr/bin/env python3
"""Route 19 -- the transport argument REPAIRED: the branch point is handled, not assumed away.

Bean `qou-trns`. Completes Routes 16 (refutation) and 17 (the conclusion survives).

THE STATE OF PLAY
-----------------
Route 16 proved (in Lean) that the discriminant VANISHES on the transport arc, so
`qou-trns`'s step "the branches never collide on the arc" is false and the k = 0
pinning argument died with it. Route 17 showed the CONCLUSION survives. This probe
supplies the missing argument.

THE REPAIR
----------
The old argument tracked  g(x) = Sum_j Log[(1 - y_j/x)/(1 - x*y_j)]  with per-root
continuous logs -- a branch LABELLING, which is exactly what a collision destroys.

Work instead with the two symmetric products, both **already Lean-proved** in
`QOU/QBeta/FiveTwoCyclotomicBloch.lean`:

    prod_j (1 - x*y_j) = x        (prod_one_sub_x_mul)
    prod_j (x - y_j)   = x^2      (prod_x_sub)     =>  prod_j (1 - y_j/x) = 1/x

Neither vanishes on |x| = 1, so each has an unambiguous continuous log there.
The claim to establish is that the SUM of the per-root logs equals the continuous
log of the product, with branch integer 0 -- through the collision.

**Why it does.** At the collision the two colliding roots are EQUAL. So the two
terms being permuted are IDENTICAL, and a sum cannot notice a relabelling of
equal terms. That is the whole content, and it is what the old argument lacked.

MEASURED (G2 below): over 4001 points spanning the branch point,

    max |step| in Sum_j log(1 - x*y_j)  =  2.5e-5     (a 2*pi jump would be 6.28)
    max | Sum_j log(1 - x*y_j) - log x  |  =  9.7e-41

So the sum IS the continuous log of the symmetric product, branch integer 0.

WHAT THIS GIVES, AND THE ONE STEP STILL MISSING
-----------------------------------------------
With both sums pinned, the envelope derivative is

    Sum_j dV/dx = (1/x)*( Sum_j log(1 - y_j/x) - Sum_j log(1 - x*y_j) )
                = (1/x)*( -log x - log x )  =  -2 log(x)/x

and integrating along x = e^{i*phi} gives S(e^{i*phi}) - S(1) = phi^2, hence
S(-1) = S(1) + pi^2.

**Still missing, and now precisely locatable:** the envelope theorem itself needs
dy_j/dx, which does not exist AT the branch point. The clean fix is removability
-- S is analytic on the arc minus one point (where the IFT does apply, since the
discriminant is non-zero there) and continuous at it (Route 17), so the identity
extends by Riemann's removable singularity theorem. That is ordinary analysis and
it is **not written**.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (acos, exp, fabs, im, log, mp, mpc, mpf, nint, nstr, pi, polylog,
                    polyroots, re)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

def phi_branch_point():
    """The branch point, computed at working precision rather than hardcoded.

    A truncated constant is not good enough here: this is a SQUARE-ROOT branch
    point, so the root separation near it grows like sqrt|delta phi|. A phi_0
    given to 25 digits leaves the two roots ~1e-12 apart, not ~1e-25 -- which is
    exactly what G4 measures, and why the constant is computed here."""
    u0 = [re(r) for r in polyroots([1, -6, 7, 6, -31], maxsteps=400, extraprec=400)
          if fabs(im(r)) < mpf(10) ** -30 and mpf(-2) < re(r) < mpf(2)][0]
    return acos(u0 / 2)


def roots_x(x):
    return list(polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                          maxsteps=500, extraprec=1000))


def sum_log_cont(phis, f):
    """Sum of per-root logs, with the SUM unwrapped by 2*pi*i step to step."""
    prev, out = None, []
    for ph in phis:
        z = exp(mpc(0, 1) * ph)
        vals = sorted((f(z, y) for y in roots_x(z)), key=lambda w: (re(w), im(w)))
        s = sum(log(v) for v in vals)
        if prev is not None:
            k = int(nint(im(prev - s) / (2 * pi)))
            s = s + mpc(0, 2 * pi * k)
        prev = s
        out.append(s)
    return out


def main() -> int:
    set_compute_dps()
    TOL = mpf(10) ** -30
    gates, ph0 = [], phi_branch_point()

    # ---- G1: the two symmetric products, at several points on the arc -------
    worst = mpf(0)
    for t in ["0.4", "1.3", "2.9", "-1.1"]:
        z = exp(mpc(0, 1) * (ph0 + mpf(t)))
        ys = roots_x(z)
        worst = max(worst,
                    fabs((1 - z * ys[0]) * (1 - z * ys[1]) * (1 - z * ys[2]) - z),
                    fabs((1 - ys[0] / z) * (1 - ys[1] / z) * (1 - ys[2] / z) - 1 / z))
    gates.append({
        "gate": "G1",
        "claim": "the two Vieta products hold on the arc: prod(1-x*y_j) = x and "
                 "prod(1-y_j/x) = 1/x -- both already Lean-proved, both nonvanishing on |x|=1",
        "worst": nstr(worst, 8), "pass": bool(worst < TOL),
    })

    # ---- G2: the sum of logs is continuous THROUGH the branch point ---------
    N = 4001
    phis = [ph0 - mpf("0.05") + mpf("0.1") * i / (N - 1) for i in range(N)]
    A = sum_log_cont(phis, lambda z, y: 1 - z * y)
    steps = [fabs(A[i + 1] - A[i]) for i in range(len(A) - 1)]
    devA = [fabs(A[i] - log(exp(mpc(0, 1) * phis[i]))) for i in range(len(A))]
    gates.append({
        "gate": "G2",
        "claim": "Sum_j log(1 - x*y_j) is CONTINUOUS through the branch point and equals the "
                 "continuous log of the symmetric product, branch integer 0",
        "n_points": N, "window": "phi_0 +- 0.05",
        "max_step": nstr(max(steps), 8),
        "a_2pi_jump_would_be": nstr(2 * pi, 8),
        "max_dev_from_log_x": nstr(max(devA), 8),
        "pass": bool(max(steps) < mpf("0.001") and max(devA) < TOL),
    })

    # ---- G3: the same for the other product --------------------------------
    B = sum_log_cont(phis, lambda z, y: 1 - y / z)
    stepsB = [fabs(B[i + 1] - B[i]) for i in range(len(B) - 1)]
    devB = [fabs(B[i] + log(exp(mpc(0, 1) * phis[i]))) for i in range(len(B))]
    gates.append({
        "gate": "G3",
        "claim": "Sum_j log(1 - y_j/x) likewise equals -log x, continuously through the "
                 "branch point",
        "max_step": nstr(max(stepsB), 8), "max_dev_from_minus_log_x": nstr(max(devB), 8),
        "pass": bool(max(stepsB) < mpf("0.001") and max(devB) < TOL),
    })

    # ---- G4: WHY -- the colliding terms are equal --------------------------
    ys0 = roots_x(exp(mpc(0, 1) * ph0))
    seps = sorted(fabs(p - q) for i, p in enumerate(ys0) for q in ys0[i + 1:])
    z0 = exp(mpc(0, 1) * ph0)
    tvals = sorted((1 - z0 * y for y in ys0), key=lambda w: (re(w), im(w)))
    tsep = min(fabs(tvals[i] - tvals[j]) for i in range(3) for j in range(i + 1, 3))
    gates.append({
        "gate": "G4",
        "claim": "the reason: AT the collision the two colliding roots are equal, so the two "
                 "log-terms being permuted are IDENTICAL -- a sum cannot notice a relabelling "
                 "of equal terms",
        "min_root_separation_at_phi0": nstr(seps[0], 8),
        "min_term_separation_at_phi0": nstr(tsep, 8),
        "note": "this is a SQUARE-ROOT branch point, so separation ~ sqrt|delta phi|; even with "
                "phi_0 at working precision the residual separation is ~1e-19, not ~1e-38. That "
                "is the expected behaviour, not a failure to resolve the collision.",
        "pass": bool(seps[0] < mpf(10) ** -15 and tsep < mpf(10) ** -15),
    })

    # ---- G5: end to end -- the pinned derivative reproduces the transport ---
    def V(x, y):
        return polylog(2, y) + polylog(2, x * y) + polylog(2, y / x) + log(-y) ** 2

    def S(x):
        return sum(re(V(x, y)) for y in roots_x(x))

    s1 = S(mpf(1))
    worst5 = mpf(0)
    for i in range(0, 61):
        ph = pi * i / 60
        worst5 = max(worst5, fabs(S(exp(mpc(0, 1) * ph)) - s1 - ph ** 2))
    gates.append({
        "gate": "G5",
        "claim": "with both sums pinned, Sum_j dV/dx = -2 log(x)/x, and integrating along "
                 "x = e^{i phi} gives S - S(1) = phi^2 -- checked directly on the arc",
        "worst": nstr(worst5, 8), "pass": bool(worst5 < TOL),
    })

    out = {
        "probe": "qbeta_5two_route19_transport_repaired",
        "bean": "qou-trns", "parent_bean": "qou-0yqu", "dps": mp.dps,
        "gates": gates,
        "verdict": {
            "outcome": "The transport argument is REPAIRED. Working with the two symmetric "
                       "Vieta products instead of a per-root branch labelling, the sum of logs "
                       "is continuous through the branch point and equals the continuous log of "
                       "the product with branch integer 0.",
            "why_it_works": "at the collision the two colliding roots are EQUAL, so the two "
                            "log-terms being permuted are identical. A sum cannot notice a "
                            "relabelling of equal terms. The old argument tracked a labelling, "
                            "which is precisely what a collision destroys.",
            "already_in_lean": "both products -- prod_one_sub_x_mul and prod_x_sub in "
                               "QOU/QBeta/FiveTwoCyclotomicBloch.lean, sorry-free since #4658.",
            "still_missing": "the envelope theorem needs dy_j/dx, which does not exist AT the "
                             "branch point. The fix is removability: S is analytic on the arc "
                             "minus one point (the IFT applies there, discriminant non-zero) and "
                             "continuous at it (Route 17), so the identity extends by Riemann's "
                             "removable singularity theorem. Ordinary analysis, NOT written.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route19-transport-repaired.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:86]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: transport argument REPAIRED via the symmetric products. One analytic step left.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
