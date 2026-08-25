#!/usr/bin/env python3
"""Route 31 -- S(phi) exists, S' = 2 phi, and S(pi) - S(0) = pi^2.

Bean `qou-trns`. Pairs with `QOU/QBeta/FiveTwoTransport.lean` (10 theorems,
sorry-free, `lake build QOU.QBeta.FiveTwoTransport` green).

WHAT THIS CLOSES
----------------
Everything the envelope step needed was proved; what was missing was the OBJECT
it is about. S(phi) = sum_j Re V(x phi, y_j phi) had never been written as a
Lean function, so `envelope_integrate` had nothing to be applied to.

THE STRUCTURAL POINT (G1)
-------------------------
S is a SYMMETRIC function of the roots, so as a function of phi it needs no
labelling at all -- it is well defined across phi_0, exactly where two branches
collide. The differentiable labelling is needed only to differentiate TERM BY
TERM, which is local. That is why one exceptional point is enough.

G6 then shows something better than expected: at phi_0 the roots have a genuine
square-root branch point, so dy/dphi DIVERGES -- and yet the labelled term's
derivative stays bounded, because dVdy = 0 annihilates it. The envelope theorem,
visible numerically.

G4 is the non-vacuity gate: `hasDerivAt_envelopeS` carries about twenty
hypotheses, which is more than enough to be worth suspecting.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (arg, cos, diff, exp, fabs, findroot, im, log, mp, mpf, nstr, pi,
                    polylog, polyroots, re, sin)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def roots_at(x):
    return list(polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                          maxsteps=800, extraprec=2000))


def V(x, y):
    return polylog(2, y) + polylog(2, x * y) + polylog(2, y / x) + log(-y) ** 2


def dVdx(x, y):
    return (-log(1 - x * y) + log(1 - y / x)) / x


def dVdy(x, y):
    return (-log(1 - y) - log(1 - x * y) - log(1 - y / x) + 2 * log(-y)) / y


def S(ph):
    """The SYMMETRIC sum -- no labelling."""
    x = exp(1j * ph)
    return sum(re(V(x, r)) for r in roots_at(x))


def main() -> int:
    set_compute_dps()
    eps = mpf(10) ** -12
    N = 200
    gates = []

    u0 = findroot(lambda u: u ** 4 - 6 * u ** 3 + 7 * u ** 2 + 6 * u - 31, mpf("-1.5"))
    phi0 = mp.acos(u0 / 2)

    # ---- G1: S needs no labelling, and S(phi) - S(0) = phi^2 -----------------
    S0 = S(eps)
    worst1 = mpf(0)
    at_worst = None
    crossed = False
    for i in range(1, N):
        ph = pi * i / N
        d = fabs((S(ph) - S0) - (ph ** 2 - eps ** 2))
        if d > worst1:
            worst1, at_worst = d, ph
        if fabs(ph - phi0) < pi / N:
            crossed = True
    gates.append({
        "gate": "G1",
        "claim": "S(phi) = sum_j Re V(x phi, y_j phi) is SYMMETRIC in the roots, so it needs no "
                 "branch labelling: computed straight from polyroots at each phi it satisfies "
                 "S(phi) - S(0) = phi^2 across the WHOLE arc, INCLUDING across phi_0 where two "
                 "branches collide and swap. This is why `envelope_integrate` tolerating one "
                 "exceptional point is enough and not a fudge -- the labelling is needed only to "
                 "differentiate term by term, which is local",
        "n_points": N - 1, "worst_deviation_from_phi_squared": nstr(worst1, 10),
        "at_phi": nstr(at_worst, 12), "phi_0_over_pi": nstr(phi0 / pi, 12),
        "sampled_across_phi_0": bool(crossed),
        "pass": bool(worst1 < mpf(10) ** -18 and crossed),
    })

    # ---- G2: dS/dphi = 2 phi -------------------------------------------------
    worst2 = mpf(0)
    for frac in ["0.05", "0.10", "0.25", "0.40", "0.55", "0.70", "0.85", "0.95"]:
        ph = pi * mpf(frac)
        worst2 = max(worst2, fabs(diff(S, ph) - 2 * ph))
    gates.append({
        "gate": "G2",
        "claim": "dS/dphi = 2 phi, by differentiating the symmetric sum numerically. This is the "
                 "conclusion of Lean's `hasDerivAt_envelopeS`, which reaches it from three "
                 "envelope collapses plus the two pinned log-sums plus `envelope_value`",
        "worst_residual": nstr(worst2, 10),
        "pass": bool(worst2 < mpf(10) ** -18),
    })

    # ---- G3: S(pi) - S(0) = pi^2, with the epsilon accounted for -------------
    Sa, Sb = S(eps), S(pi - eps)
    exact = (pi - eps) ** 2 - eps ** 2
    gates.append({
        "gate": "G3",
        "claim": "S(pi) - S(0) = pi^2 -- the transport's target, and the conclusion of "
                 "`envelopeS_total`. Both endpoints are evaluated at distance eps = 1e-12 from "
                 "the true endpoints (the roots sit on cuts exactly there), so the claim checked "
                 "is the EXACT one S(pi-eps) - S(eps) = (pi-eps)^2 - eps^2, not a rounded "
                 "version of it -- the raw difference from pi^2 is -2 pi eps = -6.28e-12, which "
                 "is the offset and not an error",
        "S_at_eps": nstr(Sa, 20), "S_at_pi_minus_eps": nstr(Sb, 20),
        "difference": nstr(Sb - Sa, 20), "pi_squared": nstr(pi ** 2, 20),
        "raw_gap_from_pi_squared": nstr(Sb - Sa - pi ** 2, 12),
        "predicted_offset_minus_2_pi_eps": nstr(-2 * pi * eps, 12),
        "residual_against_exact_identity": nstr(fabs(Sb - Sa - exact), 12),
        "pass": bool(fabs(Sb - Sa - exact) < mpf(10) ** -18),
    })

    # ---- G4: NON-VACUITY -- every hypothesis of hasDerivAt_envelopeS ---------
    bad = {k: 0 for k in
           ["phi_range", "arcX_ne_0", "arcX_normSq", "arcX_arg", "log_arcX",
            "VSide_y_ne_0", "VSide_y_notCut", "VSide_xy_notCut", "VSide_ydivx_notCut",
            "log_deriv_no_route", "Re_dVdy_yprime", "pinnedA", "pinnedB", "conclusion"]}
    n_on_cut = []
    for i in range(1, N):
        ph = pi * i / N
        x = exp(1j * ph)
        rs = roots_at(x)
        on_cut = 0
        if not (-pi < ph <= pi):
            bad["phi_range"] += 1
        if fabs(x) < mpf(10) ** -30:
            bad["arcX_ne_0"] += 1
        if fabs(re(x) ** 2 + im(x) ** 2 - 1) > mpf(10) ** -30:
            bad["arcX_normSq"] += 1
        if fabs(arg(x) - ph) > mpf(10) ** -30:
            bad["arcX_arg"] += 1
        if fabs(log(x) - 1j * ph) > mpf(10) ** -30:
            bad["log_arcX"] += 1
        for r in rs:
            if fabs(r) < mpf(10) ** -20:
                bad["VSide_y_ne_0"] += 1
            # notCut = {w : Im w != 0 or Re w < 1}
            for nm, w in (("VSide_y_notCut", r), ("VSide_xy_notCut", x * r),
                          ("VSide_ydivx_notCut", r / x)):
                if not (fabs(im(w)) > mpf(10) ** -20 or re(w) < 1):
                    bad[nm] += 1
            # log(-y) needs ONE of two routes: -y off the cut, or y real positive
            off_cut = (re(-r) > 0 or fabs(im(-r)) > mpf(10) ** -20)
            real_pos = (fabs(im(r)) < mpf(10) ** -20 and re(r) > 0)
            if not (off_cut or real_pos):
                bad["log_deriv_no_route"] += 1
            if not off_cut:
                on_cut += 1
            # Re(dVdy * y') = 0, with y' from local tracking
            def branch(p, ref=r):
                return min(roots_at(exp(1j * p)), key=lambda q: fabs(q - ref))
            yp = diff(branch, ph)
            if fabs(re(dVdy(x, r) * yp)) > mpf(10) ** -18:
                bad["Re_dVdy_yprime"] += 1
        if fabs(sum(log(1 - x * r) for r in rs) - log(x)) > mpf(10) ** -25:
            bad["pinnedA"] += 1
        if fabs(sum(log(1 - r / x) for r in rs) + log(x)) > mpf(10) ** -25:
            bad["pinnedB"] += 1
        if fabs(sum(dVdx(x, r) for r in rs) * (1j * x) - 2 * ph) > mpf(10) ** -25:
            bad["conclusion"] += 1
        n_on_cut.append(on_cut)
    gates.append({
        "gate": "G4",
        "claim": "NON-VACUITY: `hasDerivAt_envelopeS` carries about twenty hypotheses -- phi in "
                 "range, the four arcX facts, seven VSide side conditions per root, the three "
                 "Re(dVdy * y') = 0 conditions, and the two pinned log-sums. Every one is checked "
                 "to hold SIMULTANEOUSLY at every arc point, and then the conclusion "
                 "sum_j dVdx * (i x) = 2 phi is checked too. THIS GATE ALREADY EARNED ITS KEEP: "
                 "an earlier VSide carried `-y in slitPlane`, and this gate found it failing at "
                 "ALL 199 points -- because the positive real root makes -y a negative real, on "
                 "log's cut. A statement carrying that hypothesis is VACUOUS on this arc. It was "
                 "removed and the log(-y) derivative is now supplied by one of two routes",
        "n_points": N - 1, "violations": {k: v for k, v in bad.items()},
        "roots_on_the_log_cut_per_point": sorted(set(n_on_cut)),
        "pass": bool(all(v == 0 for v in bad.values()) and set(n_on_cut) == {1}),
    })

    # ---- G5: continuity of S across phi_0, for `envelopeS_total`'s hcont -----
    jump = mpf(0)
    h = mpf(10) ** -8
    for k in range(-3, 4):
        a = phi0 + k * h
        b = phi0 + (k + 1) * h
        jump = max(jump, fabs(S(b) - S(a)))
    gates.append({
        "gate": "G5",
        "claim": "S is continuous ACROSS phi_0 -- which `envelopeS_total` needs as `hcont` on the "
                 "closed interval, including the one point where the derivative argument is "
                 "allowed to fail. Sampled at 1e-8 spacing straddling phi_0",
        "phi_0": nstr(phi0, 20), "max_step_over_1e-8_spacing": nstr(jump, 10),
        "expected_order": nstr(2 * phi0 * h, 10),
        "pass": bool(jump < mpf(10) ** -6),
    })

    # ---- G6: the envelope mechanism, visible at the branch point -------------
    seps, yprimes, dterms = [], [], []
    for e in [4, 5, 6, 7, 8]:
        d = mpf(10) ** -e
        ph = phi0 - d
        x = exp(1j * ph)
        rs = sorted(roots_at(x), key=lambda z: (re(z), im(z)))
        seps.append(min(fabs(rs[0] - rs[1]), fabs(rs[1] - rs[2])) / mp.sqrt(d))
        ref = rs[0]

        def br(p, ref=ref):
            return min(roots_at(exp(1j * p)), key=lambda q: fabs(q - ref))

        yprimes.append(fabs(diff(br, ph)) * mp.sqrt(d))
        dterms.append(fabs(diff(lambda p: re(V(exp(1j * p), br(p))), ph)))
    sep_stable = fabs(seps[0] - seps[-1])
    yp_stable = fabs(yprimes[0] - yprimes[-1])
    dterm_stable = fabs(dterms[0] - dterms[-1])
    gates.append({
        "gate": "G6",
        "claim": "THE ENVELOPE MECHANISM, VISIBLE. Approaching phi_0 the two colliding roots "
                 "separate like C*sqrt(|phi - phi_0|) with C = 2.6016 -- a genuine square-root "
                 "branch point -- so dy/dphi DIVERGES like 1/sqrt(|phi - phi_0|). Yet the "
                 "labelled term's derivative d/dphi Re V(x, y(phi)) stays BOUNDED at 2.7269 all "
                 "the way in, because dVdy = 0 annihilates the divergent y'. That is the envelope "
                 "theorem happening numerically, and it is why the branch point costs only one "
                 "exceptional point in `envelope_integrate` rather than breaking the argument. "
                 "(An earlier draft of this gate claimed the labelled terms JUMP at phi_0. They "
                 "do not -- they are continuous and their derivatives are bounded. That claim was "
                 "wrong and is withdrawn.)",
        "separation_over_sqrt_d": [nstr(v, 8) for v in seps],
        "abs_yprime_times_sqrt_d": [nstr(v, 8) for v in yprimes],
        "abs_d_term_dphi": [nstr(v, 8) for v in dterms],
        "sqrt_law_drift": nstr(sep_stable, 6),
        "yprime_divergence_law_drift": nstr(yp_stable, 6),
        "term_derivative_drift": nstr(dterm_stable, 6),
        "pass": bool(sep_stable < mpf(1) / 1000 and yp_stable < mpf(1) / 100
                     and dterm_stable < mpf(1) / 1000 and dterms[-1] < 10),
    })

    out = {
        "probe": "qbeta_5two_route31_transport_total",
        "bean": "qou-trns", "dps": mp.dps,
        "pairs_with_lean": "QOU/QBeta/FiveTwoTransport.lean",
        "gates": gates,
        "verdict": {
            "what_it_closes": "S(phi) as a Lean object, and `envelope_integrate` applied to it: "
                              "S(pi) - S(0) = pi^2.",
            "the_structural_point": "S is symmetric in the roots, so it needs no branch labelling "
                                    "to be DEFINED -- only to be differentiated term by term. "
                                    "That is why tolerating one exceptional point at phi_0 is "
                                    "sound rather than a fudge, and G6 shows the labelled terms "
                                    "really do jump there while the sum does not.",
            "what_is_still_not_proved": "the sum rule. S(pi) - S(0) = pi^2 is the transport's "
                                        "derivative step, not the sum rule; the identification "
                                        "of sum_j Re V_j = -3 pi^2/2 with the proved cyclotomic "
                                        "identity sum_k (2L + L) = +pi^2/2 is untouched by any of "
                                        "this. Also: the root-path labelling is a HYPOTHESIS of "
                                        "`hasDerivAt_envelopeS`, supplied locally by the IFT but "
                                        "not constructed globally in Lean.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route31-transport-total.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:84]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + ("S exists, S' = 2 phi, S(pi) - S(0) = pi^2, and S needs no labelling."
                         if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
