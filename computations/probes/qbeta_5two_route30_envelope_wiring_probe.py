#!/usr/bin/env python3
"""Route 30 -- the two joins that were never written, and the envelope wired.

Bean `qou-trns`. Pairs with three Lean modules, all sorry-free and lake green:
  QOU/QBeta/FiveTwoBranchPinned.lean    (4 theorems)  -- taking imaginary parts
  QOU/QBeta/FiveTwoEnvelopeWiring.lean  (5 theorems)  -- V's derivative along a path
  QOU/QBeta/FiveTwoBranchPinnedB.lean   (9 theorems)  -- the second branch integer

WHAT THIS CLOSES
----------------
Three things that were being called "assembly of proved parts":

  (1) exp(sum_j log(1 - x y_j) - log x) = 1  ==>  sum_j arg(1 - x y_j) = phi + 2 pi k.
      Both ends existed; the step between them did not.
  (2) the instantiation of the envelope theorem at the actual potential
      V(x,y) = Li2(y) + Li2(xy) + Li2(y/x) + log(-y)^2.
  (3) the SECOND pinned log-sum, sum_j log(1 - y_j/x) = -log x, which
      `sum_dVdx_of_pinned` also consumes. It became visible only once (1) was
      written -- which is the argument for writing joins out.

G6 is the payoff and the gate to read first: it checks Re(dS/dphi) = 2 phi directly.

G2 CORRECTS a claim this lane almost shipped: that the envelope hypothesis
dVdy = 0 is free on the curve. It is not -- at the positive real root
dVdy = 2 pi i / t, because -t sits on log's cut. The transport survives because
the leak is purely imaginary and S = sum_j Re V takes real parts, but the Lean
statement had to be weakened to match, and the docstring that claimed otherwise
was wrong.

G7 and G8 are non-vacuity gates with teeth: `logSumA_eq_log` has FIFTEEN
hypotheses and `logSumB_eq_neg_log` has sixteen. A theorem with that many
hypotheses is worth suspecting of being vacuous, so the probe checks every one
of them holds simultaneously at every arc point, and then that the conclusion
holds too.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (arg, cos, diff, exp, fabs, im, log, mp, mpf, nstr, pi, polylog,
                    polyroots, re, sin)
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


def dVdx_closed(x, y):
    return (-log(1 - x * y) + log(1 - y / x)) / x


def dVdy_closed(x, y):
    return (-log(1 - y) - log(1 - x * y) - log(1 - y / x) + 2 * log(-y)) / y


def track(ph, y_ref, dh):
    """The root of the curve at ph nearest to y_ref -- a local branch labelling."""
    rs = roots_at(exp(1j * ph))
    return min(rs, key=lambda r: fabs(r - y_ref))


def main() -> int:
    set_compute_dps()
    tol = mpf(10) ** -25
    N = 400
    gates = []

    # ---- G1 / G2: the two partials are what the Lean file says they are ------
    worst_x = worst_y = mpf(0)
    for i in range(1, 40):
        ph = pi * i / 40
        x = exp(1j * ph)
        for r in roots_at(x):
            dx = diff(lambda z: V(z, r), x)
            dy = diff(lambda w: V(x, w), r)
            worst_x = max(worst_x, fabs(dx - dVdx_closed(x, r)))
            worst_y = max(worst_y, fabs(dy - dVdy_closed(x, r)))
    gates.append({
        "gate": "G1",
        "claim": "dVdx = [-log(1 - x y) + log(1 - y/x)] / x and "
                 "dVdy = [-log(1-y) - log(1 - x y) - log(1 - y/x) + 2 log(-y)] / y really ARE "
                 "the partials of V = Li2(y) + Li2(xy) + Li2(y/x) + log(-y)^2, checked against "
                 "numerical differentiation of mpmath's independently-implemented polylog. These "
                 "are the closed forms Lean's `hasDerivAt_deformedV_path` produces",
        "worst_dVdx_residual": nstr(worst_x, 10), "worst_dVdy_residual": nstr(worst_y, 10),
        "pass": bool(worst_x < mpf(10) ** -20 and worst_y < mpf(10) ** -20),
    })

    # ---- G2: dVdy on the curve -- and where it is NOT zero -------------------
    worst_other = mpf(0)
    worst_real = mpf(0)
    worst_exp = mpf(0)
    for i in range(1, N):
        ph = pi * i / N
        x = exp(1j * ph)
        for r in roots_at(x):
            worst_exp = max(worst_exp, fabs((1 - r) * (1 - x * r) * (1 - r / x) - r ** 2))
            if fabs(im(r)) < mpf(10) ** -20 and re(r) > 0:
                worst_real = max(worst_real, fabs(dVdy_closed(x, r) - 2j * pi / r))
            else:
                worst_other = max(worst_other, fabs(dVdy_closed(x, r)))
    gates.append({
        "gate": "G2",
        "claim": "CORRECTS A CLAIM THIS LANE ALMOST SHIPPED. `deformed_saddle_iff_curve` gives "
                 "the EXPONENTIATED saddle on the curve, and an earlier draft concluded from it "
                 "that dVdy = 0 there, i.e. that the envelope hypothesis is free. It is not. "
                 "dVdy = 0 at the two roots other than the positive real one, but at the "
                 "positive real root t it is exactly 2 pi i / t -- because -t is a NEGATIVE REAL "
                 "and sits on log's cut, so log(-t) = log t + i pi and the 2 log(-y) term leaves "
                 "a bare 2 pi i. Exponentiating is necessary, not sufficient: the branch integers "
                 "have to line up too",
        "n_points": N - 1,
        "worst_exponentiated_saddle_residual": nstr(worst_exp, 10),
        "worst_dVdy_at_other_two_roots": nstr(worst_other, 10),
        "worst_dVdy_minus_2pi_i_over_t_at_real_root": nstr(worst_real, 10),
        "pass": bool(worst_exp < mpf(10) ** -20 and worst_other < mpf(10) ** -20
                     and worst_real < mpf(10) ** -20),
    })

    # ---- G3: the collection identity, with the logs held opaque --------------
    worst_c = mpf(0)
    for i in range(1, 20):
        x = exp(1j * pi * i / 20) * (1 + mpf(i) / 10)
        y = exp(1j * pi * i / 7) * (mpf(1) / 2 + mpf(i) / 20)
        xp = 1 + 1j * mpf(i) / 5
        yp = mpf(i) / 4 - 1j
        L1, L2, L3, M = mpf(2) / 3, -mpf(1) / 5, mpf(7) / 4, -mpf(3) / 8
        lhs = (-(L1 / y) * yp + -(L2 / (x * y)) * (xp * y + x * yp)
               + -(L3 / (y / x)) * ((yp * x - y * xp) / x ** 2) + 2 * M * (yp / y))
        rhs = ((-L2 + L3) / x) * xp + ((-L1 - L2 - L3 + 2 * M) / y) * yp
        worst_c = max(worst_c, fabs(lhs - rhs))
    gates.append({
        "gate": "G3",
        "claim": "`dV_collect`: the four chain-rule outputs sum to dVdx*x' + dVdy*y'. Checked "
                 "with the logarithms replaced by ARBITRARY constants, exactly as the Lean "
                 "statement has them -- which is the point: field_simp rewrites 1 - y/x to "
                 "(x-y)/x, and inside a logarithm that changes the branch. That bug happened "
                 "once in this lane already",
        "worst_residual": nstr(worst_c, 10),
        "pass": bool(worst_c < mpf(10) ** -25),
    })

    # ---- G4 / G5: the two pinned log-sums -----------------------------------
    worst_A = worst_B = mpf(0)
    for i in range(1, N):
        ph = pi * i / N
        x = exp(1j * ph)
        rs = roots_at(x)
        A = sum(log(1 - x * r) for r in rs)
        B = sum(log(1 - r / x) for r in rs)
        worst_A = max(worst_A, fabs(A - log(x)))
        worst_B = max(worst_B, fabs(B + log(x)))
    gates.append({
        "gate": "G4",
        "claim": "sum_j log(1 - x y_j) = log x on the open arc -- `logSumA_eq_log`, the first "
                 "pinned sum. Vieta gives exp(A - log x) = 1; the new step is taking imaginary "
                 "parts (`exists_int_im_eq`) and feeding the sector bound",
        "n_points": N - 1, "worst_residual": nstr(worst_A, 10),
        "pass": bool(worst_A < mpf(10) ** -25),
    })
    gates.append({
        "gate": "G5",
        "claim": "sum_j log(1 - y_j/x) = -log x -- `logSumB_eq_neg_log`, the second pinned sum, "
                 "which `sum_dVdx_of_pinned` also needs and which nobody had noticed was "
                 "missing. Proved by MIRRORING the sector argument, not by the conjugation "
                 "identity of Route 27 G5 (that would need the root multiset to be "
                 "conjugation-closed as a permutation)",
        "n_points": N - 1, "worst_residual": nstr(worst_B, 10),
        "pass": bool(worst_B < mpf(10) ** -25),
    })

    # ---- G6: THE PAYOFF -- Re(dS/dphi) = 2 phi, and the leak that Re kills ----
    worst_env_re = mpf(0)
    worst_env_raw = mpf(0)
    worst_dS = mpf(0)
    checked = 0
    for frac in ["0.10", "0.25", "0.40", "0.55", "0.70", "0.85", "0.95"]:
        ph = pi * mpf(frac)
        x = exp(1j * ph)
        rs = roots_at(x)
        for r in rs:
            dtot = diff(lambda p: V(exp(1j * p), track(p, r, None)), ph)
            pred = dVdx_closed(x, r) * (1j * x)
            worst_env_re = max(worst_env_re, fabs(re(dtot) - re(pred)))
            worst_env_raw = max(worst_env_raw, fabs(dtot - pred))
            checked += 1
        tot = sum(dVdx_closed(x, r) * (1j * x) for r in rs)
        worst_dS = max(worst_dS, fabs(re(tot) - 2 * ph))
    gates.append({
        "gate": "G6",
        "claim": "THE PAYOFF, stated as it actually holds: per root "
                 "Re(d/dphi V(x(phi), y(phi))) = Re(dVdx * i x). The UNREDUCED difference is NOT "
                 "zero -- it reaches 2.47, the 2 pi i t'/t leak from G2 -- but that leak is "
                 "purely imaginary because t and t' are real, so Re kills it, and S = sum_j Re V "
                 "takes real parts. Lean: `hasDerivAt_re_deformedV_envelope`, whose hypothesis is "
                 "Re(dVdy * y') = 0 rather than the false dVdy = 0. And summing over the three "
                 "roots, Re sum_j dVdx*(i x) = 2 phi EXACTLY -- which is dS/dphi",
        "n_root_paths_checked": checked,
        "worst_Re_envelope_collapse": nstr(worst_env_re, 10),
        "worst_UNREDUCED_difference": nstr(worst_env_raw, 10),
        "worst_dS_dphi_minus_2phi": nstr(worst_dS, 10),
        "pass": bool(worst_env_re < mpf(10) ** -15 and worst_dS < mpf(10) ** -25
                     and worst_env_raw > 1),
    })

    # ---- G7 / G8: NON-VACUITY -- every hypothesis, simultaneously ------------
    bad7 = {k: 0 for k in
            ["x_ne_0", "b1_ne_0", "b2_ne_0", "b3_ne_0", "vieta1", "vieta2", "vieta3",
             "x_im_pos", "x_norm", "t_in_01", "im_xy3_nonpos", "im_xy2_when_big",
             "phi_range", "x_arg_eq_phi", "conclusion"]}
    bad8 = {k: 0 for k in
            ["c1_ne_0", "c2_ne_0", "c3_ne_0", "im_y2_div_pos", "im_y3_div_when_big",
             "conclusion"]}
    for i in range(1, N):
        ph = pi * i / N
        x = exp(1j * ph)
        c = cos(ph)
        rs = roots_at(x)
        reals = [r for r in rs if fabs(im(r)) < mpf(10) ** -20]
        t = [re(r) for r in reals if re(r) > 0][0]
        others = [r for r in rs if fabs(r - t) > mpf(10) ** -20]
        # label so that y3 is the one with Im(x y) <= 0
        y2, y3 = others[0], others[1]
        if im(x * y2) <= 0 and im(x * y3) > 0:
            y2, y3 = y3, y2
        if fabs(x) < tol:
            bad7["x_ne_0"] += 1
        for nm, v in (("b1_ne_0", 1 - x * t), ("b2_ne_0", 1 - x * y2), ("b3_ne_0", 1 - x * y3)):
            if fabs(v) < mpf(10) ** -20:
                bad7[nm] += 1
        if fabs(x * (t + y2 + y3) - (x ** 2 + 1)) > tol:
            bad7["vieta1"] += 1
        if fabs(x * (t * y2 + t * y3 + y2 * y3) - (x ** 2 + x + 1)) > tol:
            bad7["vieta2"] += 1
        if fabs(t * y2 * y3 - 1) > tol:
            bad7["vieta3"] += 1
        if not im(x) > 0:
            bad7["x_im_pos"] += 1
        if fabs(re(x) ** 2 + im(x) ** 2 - 1) > tol:
            bad7["x_norm"] += 1
        if not (0 < t < 1):
            bad7["t_in_01"] += 1
        if not im(x * y3) <= 0:
            bad7["im_xy3_nonpos"] += 1
        if ph > pi / 2 and not im(x * y2) <= 0:
            bad7["im_xy2_when_big"] += 1
        if not (0 <= ph < pi):
            bad7["phi_range"] += 1
        if fabs(arg(x) - ph) > tol:
            bad7["x_arg_eq_phi"] += 1
        if fabs(log(1 - x * t) + log(1 - x * y2) + log(1 - x * y3) - log(x)) > mpf(10) ** -25:
            bad7["conclusion"] += 1
        # --- B side
        for nm, v in (("c1_ne_0", 1 - t / x), ("c2_ne_0", 1 - y2 / x), ("c3_ne_0", 1 - y3 / x)):
            if fabs(v) < mpf(10) ** -20:
                bad8[nm] += 1
        if not im(y2 / x) > 0:
            bad8["im_y2_div_pos"] += 1
        if ph > pi / 2 and not im(y3 / x) > 0:
            bad8["im_y3_div_when_big"] += 1
        if fabs(log(1 - t / x) + log(1 - y2 / x) + log(1 - y3 / x) + log(x)) > mpf(10) ** -25:
            bad8["conclusion"] += 1
    gates.append({
        "gate": "G7",
        "claim": "NON-VACUITY with teeth: `logSumA_eq_log` has FIFTEEN hypotheses, which is "
                 "enough to be worth suspecting of vacuity. Every one of them is checked to hold "
                 "SIMULTANEOUSLY at every arc point, and then the conclusion is checked too",
        "n_points": N - 1, "violations": {k: v for k, v in bad7.items()},
        "pass": bool(all(v == 0 for v in bad7.values())),
    })
    gates.append({
        "gate": "G8",
        "claim": "the same for `logSumB_eq_neg_log` (sixteen hypotheses). Note the labelling: y2 "
                 "is chosen so that Im(x y3) <= 0, and then Im(y2/x) > 0 comes out positive "
                 "without being asked for -- the mirror the Lean proof exploits",
        "n_points": N - 1, "violations": {k: v for k, v in bad8.items()},
        "pass": bool(all(v == 0 for v in bad8.values())),
    })

    out = {
        "probe": "qbeta_5two_route30_envelope_wiring",
        "bean": "qou-trns", "dps": mp.dps,
        "pairs_with_lean": ["QOU/QBeta/FiveTwoBranchPinned.lean",
                            "QOU/QBeta/FiveTwoEnvelopeWiring.lean",
                            "QOU/QBeta/FiveTwoBranchPinnedB.lean"],
        "gates": gates,
        "verdict": {
            "what_it_closes": "three joins that were being called assembly: taking imaginary "
                              "parts of the Vieta exp-identity; instantiating the envelope "
                              "theorem at the actual V; and the SECOND pinned log-sum, which "
                              "`sum_dVdx_of_pinned` needs and which only became visible once the "
                              "first was written.",
            "the_payoff": "G6: per root the envelope collapses, and summing over the three roots "
                          "gives Re sum_j dVdx*(i x) = 2 phi exactly -- dS/dphi.",
            "what_is_still_not_written": "S(phi) itself is not defined in Lean as "
                                         "sum_j Re V(x phi, y_j phi) with a differentiable root "
                                         "labelling, so `envelope_integrate` is not yet applied "
                                         "to it. That needs the IFT output "
                                         "(`exists_hasDerivAt_root`) threaded through, which is "
                                         "the next join -- and it is a join, so it will be "
                                         "written rather than called assembly.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route30-envelope-wiring.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:84]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + ("the three joins are written; Re(dS/dphi) = 2 phi per root and summed, "
                         "and dVdy is NOT zero at the real root."
                         if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
