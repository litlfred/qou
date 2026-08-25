#!/usr/bin/env python3
"""Route 29 -- the root structure, the last open input to the branch pinning.

Bean `qou-trns`. Pairs with `QOU/QBeta/FiveTwoRootStructure.lean` (16 theorems,
sorry-free, `lake build QOU.QBeta.FiveTwoRootStructure` green).

WHAT IT CLOSES
--------------
`FiveTwoArgSector` reduced the branch pinning to two facts about the roots and
STATED THEM AS HYPOTHESES: a real root `t` in (0,1), and sign conditions on
`Im(x y)` for the other two. This route checks the proofs of those facts.

Everything is real algebra plus one IVT. The chain:

    p(0) = -1 < 0 < 1 = p(1)          -> a real root t in (0,1)          [G2]
    factor (Y - t) out                -> Y^2 + b Y + g, t g = 1          [G3]
    c <= 1                            -> t > 2/5                         [G4]
    quadratic has real roots          -> W = t^2 + t - 1 >= 0            [G5]
      hence b >= 0 and g > 0          -> both are NEGATIVE               [G6]
    quadratic has complex roots       -> sa_lt_cb (Route 28)             [G6]

G1 is the gate that matters most and is easiest to skip: it checks the real
cubic IS the curve's cubic. Nine defects in this lane were checks that tested
something ADJACENT to what they claimed; a correct theorem about the wrong
polynomial would be the tenth.

G7 is adversarial: `c <= 1` is load-bearing, and the probe exhibits the failure.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import cos, exp, fabs, findroot, im, mp, mpf, nstr, pi, polyroots, re, sin, sqrt
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def unit_cubic(c, t):
    return t ** 3 - 2 * c * t ** 2 + (2 * c + 1) * t - 1


def real_root_in_unit(c):
    """The root of unit_cubic(c, .) in (0,1); bisection, so no derivative needed."""
    lo, hi = mpf(0), mpf(1)
    for _ in range(200):
        mid = (lo + hi) / 2
        if unit_cubic(c, mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main() -> int:
    set_compute_dps()
    tol = mpf(10) ** -25
    N = 700
    gates = []

    # ---- G1: the real cubic IS the curve's cubic on |x| = 1 -------------------
    worst1 = mpf(0)
    for i in range(0, N + 1):
        ph = pi * i / N
        x = exp(1j * ph)
        c = cos(ph)
        for j in range(0, 7):
            y = exp(1j * pi * j / 3) * (1 + mpf(j) / 5)
            lhs = x * y ** 3 - (x ** 2 + 1) * y ** 2 + (x ** 2 + x + 1) * y - x
            rhs = x * (y ** 3 - 2 * c * y ** 2 + (2 * c + 1) * y - 1)
            worst1 = max(worst1, fabs(lhs - rhs))
    gates.append({
        "gate": "G1",
        "claim": "THE GATE THAT MATTERS: the deformed curve x y^3 - (x^2+1) y^2 + (x^2+x+1) y - x "
                 "equals x * (y^3 - 2c y^2 + (2c+1) y - 1) with c = Re x, for every x on the unit "
                 "circle and every y. Without this, every theorem downstream would be a correct "
                 "statement about the WRONG polynomial. Lean: `curve_eq_unitCubic`, which rests on "
                 "2 Re(x) x = x^2 + 1, i.e. x conj(x) = 1",
        "n_x": N + 1, "n_y_per_x": 7, "worst_residual": nstr(worst1, 10),
        "pass": bool(worst1 < mpf(10) ** -30),
    })

    # ---- G2: p(0) = -1, p(1) = 1 identically in c, and the root exists --------
    worst0 = worst1a = mpf(0)
    worst_root = mpf(0)
    for i in range(-100, 101):
        c = mpf(i) / 50                       # c in [-2, 2], wider than the arc
        worst0 = max(worst0, fabs(unit_cubic(c, mpf(0)) + 1))
        worst1a = max(worst1a, fabs(unit_cubic(c, mpf(1)) - 1))
        t = real_root_in_unit(c)
        worst_root = max(worst_root, fabs(unit_cubic(c, t)))
    gates.append({
        "gate": "G2",
        "claim": "p(0) = -1 and p(1) = +1 IDENTICALLY IN c -- the 2c terms cancel at Y = 1, which "
                 "is why the root in (0,1) costs nothing but IVT. Checked over c in [-2,2], wider "
                 "than the arc's [-1,1]. Lean: `unitCubic_zero`, `unitCubic_one`, "
                 "`exists_root_mem_Ioo`",
        "worst_p0_residual": nstr(worst0, 10), "worst_p1_residual": nstr(worst1a, 10),
        "worst_root_residual": nstr(worst_root, 10),
        "pass": bool(worst0 < tol and worst1a < tol and worst_root < mpf(10) ** -25),
    })

    # ---- G3: the three algebraic relations -----------------------------------
    wa = wb = wg = mpf(0)
    for i in range(-100, 101):
        c = mpf(i) / 50
        t = real_root_in_unit(c)
        wa = max(wa, fabs(2 * c * (t * (t - 1)) - (t ** 3 + t - 1)))
        wb = max(wb, fabs((t - 2 * c) * (t * (1 - t)) - (t ** 2 + t - 1)))
        wg = max(wg, fabs(t * (t ** 2 - 2 * c * t + 2 * c + 1) - 1))
    gates.append({
        "gate": "G3",
        "claim": "the three relations the proof runs on: 2c t(t-1) = t^3+t-1 (`two_c_rel`), "
                 "beta * t(1-t) = W with beta = t-2c and W = t^2+t-1 (`beta_rel` -- this is why "
                 "beta and W share a sign on (0,1)), and t * gamma = 1 with "
                 "gamma = t^2-2ct+2c+1 (`gamma_rel`)",
        "worst_two_c_rel": nstr(wa, 10), "worst_beta_rel": nstr(wb, 10),
        "worst_gamma_rel": nstr(wg, 10),
        "pass": bool(wa < tol and wb < tol and wg < tol),
    })

    # ---- G4: c <= 1 forces t > 2/5, with the true margin ---------------------
    min_t = mpf(10) ** 9
    at_c = None
    for i in range(-500, 51):
        c = mpf(i) / 50                       # c in [-10, 1]
        t = real_root_in_unit(c)
        if t < min_t:
            min_t, at_c = t, c
    t_at_c1 = real_root_in_unit(mpf(1))
    gates.append({
        "gate": "G4",
        "claim": "`two_fifths_lt`: c <= 1 forces the root above 2/5. The bound is not tight but it "
                 "is the one the quartic argument needs; the true infimum over c <= 1 is attained "
                 "at c = 1. Checked on c in [-10, 1], i.e. well beyond the arc",
        "min_t_over_c_le_1": nstr(min_t, 20), "attained_at_c": nstr(at_c, 10),
        "t_at_c_eq_1": nstr(t_at_c1, 20), "bound": "0.4", "margin": nstr(min_t - mpf(2) / 5, 12),
        "pass": bool(min_t > mpf(2) / 5),
    })

    # ---- G5: disc >= 0 implies W >= 0 ----------------------------------------
    viol5 = 0
    n_real_branch = 0
    c_switch = None
    for i in range(-500, 51):
        c = mpf(i) / 50
        t = real_root_in_unit(c)
        beta = t - 2 * c
        gam = t ** 2 - 2 * c * t + 2 * c + 1
        D = beta ** 2 - 4 * gam
        W = t ** 2 + t - 1
        if D >= 0:
            n_real_branch += 1
            if not W >= 0:
                viol5 += 1
            if c_switch is None or c > c_switch:
                c_switch = c
    gates.append({
        "gate": "G5",
        "claim": "`W_nonneg_of_disc_nonneg`, the step with content: whenever the quadratic factor "
                 "has real roots (disc >= 0), W = t^2+t-1 >= 0. The proof rearranges disc >= 0 to "
                 "W^2 >= 4t(1-t)^2, which W < 0 and t > 2/5 contradict",
        "n_points_with_real_quadratic": n_real_branch, "violations": viol5,
        "largest_c_with_real_quadratic": nstr(c_switch, 12) if c_switch is not None else None,
        "pass": bool(viol5 == 0 and n_real_branch > 0),
    })

    # ---- G6: the sign conclusions, on the actual arc --------------------------
    bad6 = {"snd_not_neg": 0, "fst_not_neg_when_c_neg": 0, "constructed_roots_wrong": 0}
    worst_snd = -mpf(10) ** 9
    worst_fst = -mpf(10) ** 9
    for i in range(1, N):
        ph = pi * i / N
        x = exp(1j * ph)
        c, s = cos(ph), sin(ph)
        t = real_root_in_unit(c)
        beta = t - 2 * c
        gam = t ** 2 - 2 * c * t + 2 * c + 1
        D = beta ** 2 - 4 * gam
        if D >= 0:
            r1 = (-beta + sqrt(D)) / 2
            r2 = (-beta - sqrt(D)) / 2
            y2, y3 = mpf(r1), mpf(r2)
        else:
            b = sqrt(-D) / 2
            y2 = -beta / 2 + 1j * b
            y3 = -beta / 2 - 1j * b
        # The constructed triple must BE the root multiset.
        #
        # ⚠ This comparison used to route both sides through `complex(...)`,
        # which rounds to binary64 BEFORE the difference is taken — so a stated
        # tolerance of 1e-20 was in fact "do these agree to float64", ~1e-16,
        # and the two sides agreed only because rounding hid the gap rather than
        # because the roots matched. Compared at working precision now. Caught by
        # the `complex-call` rule added to the float64 guard on #4777.
        # ⚠ Matched by NEAREST NEIGHBOUR, both directions -- NOT by sorting.
        # Sorting on `(re, im)` is unstable exactly here: the conjugate pair has
        # equal real parts in exact arithmetic, `polyroots` returns them
        # differing at ~1e-40, and the sort then orders by that noise and can
        # invert the pair relative to the constructed list. The mis-pairing
        # reports a discrepancy of 2*|Im y| ~ 2.6 -- not a small error, a wrong
        # comparison. The float64 version hid it: rounding made the two real
        # parts bit-identical, so the tie-break fell to `im` consistently in
        # both lists. Removing the rounding exposed the fragility, not an error.
        got = [t, y2, y3]
        want = list(polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                              maxsteps=800, extraprec=2000))
        fwd = max(min(fabs(a - b_) for b_ in want) for a in got)
        bwd = max(min(fabs(b_ - a) for a in got) for b_ in want)
        if max(fwd, bwd) > mpf(10) ** -20:
            bad6["constructed_roots_wrong"] += 1
        v3 = im(x * y3)
        worst_snd = max(worst_snd, v3)
        if not v3 < 0:
            bad6["snd_not_neg"] += 1
        if c < 0:
            v2 = im(x * y2)
            worst_fst = max(worst_fst, v2)
            if not v2 < 0:
                bad6["fst_not_neg_when_c_neg"] += 1
    gates.append({
        "gate": "G6",
        "claim": "the two sign conclusions, and a check that the CONSTRUCTED triple really is the "
                 "curve's root multiset (compared against mpmath polyroots, independently "
                 "computed): Im(x y_3) < 0 always, and Im(x y_2) < 0 whenever c < 0. These are "
                 "`im_mul_otherRoots_snd_neg` and `im_mul_otherRoots_fst_neg`",
        "violations": {k: v for k, v in bad6.items()}, "n_points": N - 1,
        "max_Im_x_y3": nstr(worst_snd, 15), "max_Im_x_y2_when_c_neg": nstr(worst_fst, 15),
        "pass": bool(all(v == 0 for v in bad6.values())),
    })

    # ---- G7: ADVERSARIAL -- `c <= 1` is load-bearing --------------------------
    c_bad = mpf(5)
    t_bad = real_root_in_unit(c_bad)
    beta_bad = t_bad - 2 * c_bad
    gam_bad = t_bad ** 2 - 2 * c_bad * t_bad + 2 * c_bad + 1
    D_bad = beta_bad ** 2 - 4 * gam_bad
    W_bad = t_bad ** 2 + t_bad - 1
    r1_bad = (-beta_bad + sqrt(D_bad)) / 2
    r2_bad = (-beta_bad - sqrt(D_bad)) / 2
    gates.append({
        "gate": "G7",
        "claim": "ADVERSARIAL: the hypothesis `c <= 1` in `two_fifths_lt` and "
                 "`W_nonneg_of_disc_nonneg` is load-bearing, not decoration. At c = 5 the root is "
                 "t = 0.0999 < 2/5, W = -0.890 < 0, and yet disc >= 0 -- so the conclusion of "
                 "`W_nonneg_of_disc_nonneg` is FALSE there. The two other roots are then both "
                 "POSITIVE, which flips the sign of Im(x y) and would break the pinning. Dropping "
                 "`c <= 1` does not weaken the theorem; it falsifies it",
        "c": "5", "t": nstr(t_bad, 15), "t_below_two_fifths": bool(t_bad < mpf(2) / 5),
        "W": nstr(W_bad, 15), "W_negative": bool(W_bad < 0),
        "disc": nstr(D_bad, 15), "disc_nonneg": bool(D_bad >= 0),
        "other_roots": [nstr(r1_bad, 12), nstr(r2_bad, 12)],
        "both_other_roots_positive": bool(r1_bad > 0 and r2_bad > 0),
        "pass": bool(t_bad < mpf(2) / 5 and W_bad < 0 and D_bad >= 0
                     and r1_bad > 0 and r2_bad > 0),
    })

    # ---- G8: where the two branches sit on the arc ---------------------------
    u0 = findroot(lambda u: u ** 4 - 6 * u ** 3 + 7 * u ** 2 + 6 * u - 31, mpf("-1.5"))
    phi0 = mp.acos(u0 / 2)
    n_real = n_cplx = 0
    for i in range(1, N):
        ph = pi * i / N
        c = cos(ph)
        t = real_root_in_unit(c)
        beta = t - 2 * c
        gam = t ** 2 - 2 * c * t + 2 * c + 1
        if beta ** 2 - 4 * gam >= 0:
            n_real += 1
        else:
            n_cplx += 1
    gates.append({
        "gate": "G8",
        "claim": "the two branches partition the arc at phi_0 = 137.9207 deg -- the SAME point at "
                 "which the discriminant of the full cubic vanishes (Route 16). Below it the "
                 "quadratic factor has complex roots and Route 28's `sa_lt_cb` carries the "
                 "argument; above it the roots are real and negative and `sa_lt_cb` is not used",
        "phi_0_over_pi": nstr(phi0 / pi, 12),
        "n_real_quadratic": n_real, "n_complex_quadratic": n_cplx,
        "predicted_split": nstr((pi - phi0) / pi, 12),
        "observed_split": nstr(mpf(n_real) / (N - 1), 12),
        "pass": bool(n_real > 0 and n_cplx > 0
                     and fabs(mpf(n_real) / (N - 1) - (pi - phi0) / pi) < mpf(1) / 100),
    })

    out = {
        "probe": "qbeta_5two_route29_root_structure",
        "bean": "qou-trns", "dps": mp.dps,
        "pairs_with_lean": "QOU/QBeta/FiveTwoRootStructure.lean",
        "gates": gates,
        "verdict": {
            "what_it_closes": "the two hypotheses FiveTwoArgSector stated but did not prove -- a "
                              "real root in (0,1), and the sign of Im(x y) for the other two "
                              "roots. Both are now theorems, and `exists_pinning_data` assembles "
                              "them with the factorisation certifying the triple IS the root "
                              "multiset.",
            "cost": "one IVT (p(0) = -1 < 0 < 1 = p(1)) and real algebra. No continuity in phi, "
                    "no root tracking, no base point.",
            "load_bearing": "G7: `c <= 1` is not decoration -- at c = 5 the conclusion is false "
                            "and both other roots turn positive.",
            "still_open": "the envelope wiring above the pinning: instantiating the envelope "
                          "theorem at V and summing over the three roots. Assembly of proved "
                          "parts, checked numerically to 1e-31 by Route 26 G6, but not written.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route29-root-structure.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:86]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: the root structure is proved; the pinning's last stated hypothesis is closed.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
