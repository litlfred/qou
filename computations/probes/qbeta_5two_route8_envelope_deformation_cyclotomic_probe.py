#!/usr/bin/env python3
"""Route 8 of the 5₂ saddle sum rule: transport it along GGM's deformation to the
totally real cyclotomic point.

Context
-------
Bean ``qou-8v3k`` (child of ``qou-0yqu``).  The sum rule

    Σⱼ Re Vⱼ = −3π²/2,    V(x,y) = Li₂(y) + Li₂(xy) + Li₂(y/x) + (log(−y))²

is verified to 80 dps and unproved.  Routes 1–7 all attacked it *at* ``x = 1``.
This route moves in ``x`` instead.

The mechanism, in four elementary steps
---------------------------------------
**(1) The saddles are critical points of V.**  Solving ``∂V/∂y = 0`` gives
``(1−y)(1−xy)(1−y/x) = y²``, which clears to

    x·y³ − (x²+1)·y² + (x²+x+1)·y − x = 0

— *exactly* GGM's deformed 5₂ curve (§6.1), already Lean-proved in the corpus as
``FiveTwoSaddleCurve.lean``.  So ``yⱼ(x)`` are critical points, by construction.

**(2) Two Vieta identities.**  Dividing by ``x``, the cubic has
``e₁ = (x²+1)/x``, ``e₂ = (x²+x+1)/x``, ``e₃ = ∏yⱼ = 1``.  Then
``∏ⱼ(1 − a·yⱼ) = 1 − a·e₁ + a²·e₂ − a³`` gives, with no cancellation of content:

    ∏ⱼ (1 − x·yⱼ) = x           ∏ⱼ (1 − yⱼ/x) = 1/x

**(3) Envelope theorem.**  Since ``∂V/∂y = 0`` at ``yⱼ``,
``d/dx V(x,yⱼ(x)) = ∂V/∂x = (1/x)·log[(1 − yⱼ/x)/(1 − x·yⱼ)]``.

**(4) Sum and integrate.**  Summing over the three branches and using (2),

    S'(x) = (1/x)·log[(1/x)/x] = −2·log(x)/x        ⟹   S(x) = S(1) − log²x

with ``S(x) := Σⱼ Re V(x, yⱼ(x))``.  The branch ambiguity enters as
``+2πik·log x``, which is purely imaginary for real ``x > 0`` (so it cannot
affect ``Re``) and real on ``|x| = 1``, where it is measured to be ``k = 0``.

The payoff
----------
On ``|x| = 1``, ``log²x = −φ²``, so ``S(e^{iφ}) = S(1) + φ²``.  At ``φ = π``:

    S(−1) = S(1) + π² = −3π²/2 + π² = −π²/2

and **at ``x = −1`` the curve degenerates to ``y³ + 2y² − y − 1 = 0``, of
discriminant 49 — the totally real cyclotomic field ℚ(ζ₇)⁺**, with roots
*exactly* ``yₖ = −1 − 2cos(2πk/7)``.

So the sum rule is **equivalent** to a dilogarithm identity at 7th roots of unity:

    Σₖ Re[ Li₂(yₖ) + 2·Li₂(−yₖ) + (log(−yₖ))² ] = −π²/2,  yₖ = −1 − 2cos(2πk/7)

Why that is a gain: at ``x = 1`` the field is the **complex** cubic of disc −23,
where Bloch–Wigner ``D ≠ 0`` and the classical ladder literature computes the
*volume* (imaginary) side — the caveat that has blocked every literature route.
At ``x = −1`` the field is **totally real and abelian**, so ``D ≡ 0`` identically
and Rogers-type sums are expected in ``π²ℚ`` — the Frenkel–Szenes / Y-system
regime, which is the one regime where ``−π²/2`` is the natural kind of answer.

⚠ **This is a REDUCTION, not a proof.**  ``S(1)`` is the constant of integration,
so steps (1)–(4) transport the unknown without evaluating it.  The cyclotomic
identity in G7 is **not proved here**.  Sum rule remains verified, unproved.

Gates
-----
G1  ∂V/∂y = 0 reproduces GGM's deformed curve.
G2  The two Vieta product identities, at several x.
G3  The envelope derivative: S'(x) = −2 log(x)/x, by finite differences.
G4  S(x) = S(1) − log²x on real x ∈ [0.2, 5].
G5  Palindromy S(x) = S(1/x) (GGM eq 306 / corpus curve_palindromic).
G6  Continuation on |x| = 1 runs with branch integer k = 0 up to φ = π.
G7  x = −1: discriminant 49, roots exactly −1 − 2cos(2πk/7), and the reduced
    cyclotomic identity evaluates to −π²/2.
"""
from __future__ import annotations

import json
import pathlib

from mpmath import (cos, exp, fabs, im, log, mp, mpc, mpf, nstr, pi, polylog,
                    polyroots, re)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def roots_x(x):
    return list(polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                          maxsteps=500, extraprec=1000))


def V(x, y):
    return polylog(2, y) + polylog(2, x * y) + polylog(2, y / x) + log(-y) ** 2


def S(x):
    return sum(re(V(x, y)) for y in roots_x(x))


def main():
    gates = []
    TOL = mpf(10) ** -30
    S1 = S(mpf(1))
    target = -3 * pi ** 2 / 2

    # G1 -- the critical-point equation IS the GGM curve
    # (1-y)(1-xy)(1-y/x) - y^2, cleared by x, equals x y^3 -(x^2+1)y^2 +(x^2+x+1)y - x
    worst = mpf(0)
    for xv in ("0.6", "1.3", "2.5"):
        x = mpf(xv)
        for yv in ("0.3", "1.7", "-0.9"):
            y = mpf(yv)
            lhs = x * ((1 - y) * (1 - x * y) * (1 - y / x) - y ** 2)
            rhs = -(x * y ** 3 - (x ** 2 + 1) * y ** 2 + (x ** 2 + x + 1) * y - x)
            worst = max(worst, fabs(lhs - rhs))
    gates.append({"gate": "G1",
                  "claim": "dV/dy = 0  <=>  GGM deformed curve x y^3 -(x^2+1)y^2 +(x^2+x+1)y - x = 0",
                  "worst_abs_error": nstr(worst, 8), "pass": bool(worst < TOL)})

    # G2 -- Vieta products
    v2 = []
    w = mpf(0)
    for xv in ("0.5", "0.7", "1.3", "2.0", "3.7"):
        x = mpf(xv)
        Y = roots_x(x)
        p1 = mpf(1)
        p2 = mpf(1)
        for y in Y:
            p1 *= (1 - x * y)
            p2 *= (1 - y / x)
        e1, e2 = fabs(re(p1) - x), fabs(re(p2) - 1 / x)
        w = max(w, e1, e2)
        v2.append({"x": xv, "err_prod_1_minus_xy": nstr(e1, 6),
                   "err_prod_1_minus_y_over_x": nstr(e2, 6)})
    gates.append({"gate": "G2", "claim": "prod(1 - x y_j) = x  and  prod(1 - y_j/x) = 1/x",
                  "per_x": v2, "worst": nstr(w, 8), "pass": bool(w < TOL)})

    # G3 -- envelope derivative by central differences
    h = mpf(10) ** -12
    d3 = []
    w3 = mpf(0)
    for xv in ("0.6", "0.9", "1.4", "2.2"):
        x = mpf(xv)
        num = (S(x + h) - S(x - h)) / (2 * h)
        ana = -2 * log(x) / x
        err = fabs(num - ana)
        w3 = max(w3, err)
        d3.append({"x": xv, "numeric": nstr(num, 14), "analytic": nstr(ana, 14),
                   "abs_err": nstr(err, 6)})
    gates.append({"gate": "G3", "claim": "S'(x) = -2 log(x)/x  (envelope theorem + Vieta)",
                  "per_x": d3, "worst": nstr(w3, 8),
                  "note": "central differences at h=1e-12, so ~1e-20 agreement is the ceiling",
                  "pass": bool(w3 < mpf(10) ** -18)})

    # G4 -- the integrated closed form
    d4 = []
    w4 = mpf(0)
    for xv in ("0.2", "0.5", "0.7", "0.9", "1.1", "1.4", "2.0", "3.0", "5.0"):
        x = mpf(xv)
        err = fabs((S(x) - S1) - (-log(x) ** 2))
        w4 = max(w4, err)
        d4.append({"x": xv, "S_minus_S1": nstr(S(x) - S1, 20), "abs_err": nstr(err, 6)})
    gates.append({"gate": "G4", "claim": "S(x) = S(1) - log^2 x  on real x > 0",
                  "per_x": d4, "worst": nstr(w4, 8), "pass": bool(w4 < TOL)})

    # G5 -- palindromy
    w5 = mpf(0)
    for xv in ("0.5", "0.7", "1.4", "2.0"):
        x = mpf(xv)
        w5 = max(w5, fabs(S(x) - S(1 / x)))
    gates.append({"gate": "G5", "claim": "S(x) = S(1/x)  (GGM eq 306 / curve_palindromic)",
                  "worst": nstr(w5, 8), "pass": bool(w5 < TOL)})

    # G6 -- continuation on the unit circle, branch integer k
    d6 = []
    w6 = mpf(0)
    for t in ("0.125", "0.25", "0.375", "0.5", "0.625", "0.75", "0.875", "1.0"):
        ph = mpf(t) * pi
        s = S(exp(1j * ph))
        pred = S1 + ph ** 2
        k = (pred - s) / (2 * pi * ph)
        w6 = max(w6, fabs(k))
        d6.append({"phi_over_pi": t, "S": nstr(s, 18), "S1_plus_phi2": nstr(pred, 18),
                   "implied_k": nstr(k, 8)})
    gates.append({"gate": "G6",
                  "claim": "on |x|=1, S(e^{i phi}) = S(1) + phi^2, i.e. branch integer k = 0 throughout",
                  "per_phi": d6, "worst_implied_k": nstr(w6, 8), "pass": bool(w6 < mpf(10) ** -30)})

    # G6b -- k=0 is not just sampled: k is integer-valued and locally constant
    # wherever the branches do not collide, and the discriminant is bounded away
    # from 0 on the arc, so k is CONSTANT there; k -> 0 as phi -> 0.
    def disc_poly(x):
        a, b, c, d = x, -(x ** 2 + 1), x ** 2 + x + 1, -x
        return (18 * a * b * c * d - 4 * b ** 3 * d + b ** 2 * c ** 2
                - 4 * a * c ** 3 - 27 * a ** 2 * d ** 2)

    N = 200
    worst_k = mpf(0)
    min_disc = None
    for i in range(1, N + 1):
        ph = mpf(i) * pi / N
        kk = ((S1 + ph ** 2) - S(exp(1j * ph))) / (2 * pi * ph)
        worst_k = max(worst_k, fabs(kk))
        dv = fabs(disc_poly(exp(1j * ph)))
        min_disc = dv if min_disc is None else min(min_disc, dv)
    gates.append({"gate": "G6b",
                  "claim": "k = 0 on the whole arc: no root collision (disc bounded away from 0), so the "
                           "integer k is locally constant hence constant, and k -> 0 as phi -> 0",
                  "n_samples": N,
                  "max_implied_k": nstr(worst_k, 8),
                  "min_abs_discriminant_on_arc": nstr(min_disc, 8),
                  "note": "this upgrades step (4) from 'measured at 8 points' to 'constant by "
                          "local-constancy on a collision-free arc' -- an argument, not a sample",
                  "pass": bool(worst_k < mpf(10) ** -20 and min_disc > mpf(10) ** -6)})

    # G7 -- the cyclotomic point
    p, q, r = mpf(2), mpf(-1), mpf(-1)
    disc = 18 * p * q * r - 4 * p ** 3 * r + p ** 2 * q ** 2 - 4 * q ** 3 - 27 * r ** 2
    Yc = sorted([-1 - 2 * cos(2 * pi * k / 7) for k in (1, 2, 3)])
    Rc = sorted([re(t) for t in polyroots([mpf(1), mpf(2), mpf(-1), mpf(-1)],
                                          maxsteps=400, extraprec=800)])
    root_err = max(fabs(a - b) for a, b in zip(Yc, Rc))
    tot = sum(re(polylog(2, y) + 2 * polylog(2, -y) + log(-y) ** 2) for y in Yc)
    id_err = fabs(tot + pi ** 2 / 2)
    gates.append({"gate": "G7",
                  "claim": "x=-1: disc 49 (Q(zeta_7)+), roots = -1-2cos(2 pi k/7), and the reduced "
                           "identity sum_k Re[Li2(y)+2Li2(-y)+(log(-y))^2] = -pi^2/2",
                  "discriminant": nstr(disc, 8),
                  "root_identification_err": nstr(root_err, 6),
                  "reduced_sum": nstr(tot, 26),
                  "target_minus_half_pi_sq": nstr(-pi ** 2 / 2, 26),
                  "abs_err": nstr(id_err, 6),
                  "pass": bool(fabs(disc - 49) < TOL and root_err < mpf(10) ** -30
                               and id_err < mpf(10) ** -30)})

    out = {
        "probe": "qbeta_5two_route8_envelope_deformation_cyclotomic",
        "bean": "qou-8v3k",
        "parent_bean": "qou-0yqu",
        "dps": mp.dps,
        "gates": gates,
        "verdict": {
            "route8": "REDUCTION ACHIEVED, NOT CLOSED",
            "what_is_established": "The sum rule sum_j Re V_j = -3pi^2/2 at x=1 is EQUIVALENT, by an "
                                   "elementary and formalizable mechanism (critical-point identification "
                                   "+ two Vieta products + envelope theorem + integration + continuation "
                                   "with measured branch integer k=0), to the cyclotomic identity "
                                   "sum_k Re[Li2(y_k)+2Li2(-y_k)+(log(-y_k))^2] = -pi^2/2 at "
                                   "y_k = -1-2cos(2 pi k/7), the totally real field Q(zeta_7)+ of disc 49.",
            "what_is_NOT_established": "The cyclotomic identity itself. S(1) is the constant of "
                                       "integration, so this transports the unknown rather than "
                                       "evaluating it.",
            "why_the_transport_is_worth_it": "At x=1 the field is the COMPLEX cubic of disc -23, where "
                                             "Bloch-Wigner D != 0 and the classical ladder literature "
                                             "computes the volume/imaginary side -- the caveat that "
                                             "blocked every literature route. At x=-1 the field is "
                                             "TOTALLY REAL and abelian, so D == 0 identically and "
                                             "Rogers-type sums are expected in pi^2 Q. That is the one "
                                             "regime where -pi^2/2 is the natural kind of answer.",
            "sum_rule_status": "verified to 80 dps, unproved -- UNCHANGED",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route8-envelope-deformation-cyclotomic.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:88]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: reduction to the Q(zeta_7)+ cyclotomic identity. NOT a proof of the sum rule.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
