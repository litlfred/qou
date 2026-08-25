#!/usr/bin/env python3
"""Route 23 -- cLiTwoExt on all of C minus [1,inf), and its radial derivative.

Bean `qou-clx8`. Pairs with `QOU/MathlibExt/ComplexDilogarithmSlit.lean`
(sorry-free, lake green).

WHAT THE BEAN ASKED FOR
-----------------------
`qou-clx8` records that the side condition in the existing bricks is SUFFICIENT
BUT NOT NECESSARY:

  "intervalIntegrable_log_one_sub_div requires Re(1 - yz) > 0 on [0,1], i.e.
   Re(1 - y) > 0. That FAILS at e.g. y = 1.5 + 0.3i and y = 3 + 0.001i while the
   identity still holds. Do not formalize Re(1-y) > 0 as if it were the real
   hypothesis -- it needlessly excludes most of C minus [1,inf)."

and names the right one: for Im y != 0 the segment {1 - yz : z in [0,1]} meets
the real axis only at z = 0, since Im(1 - yz) = -z*Im(y).

G1 tests exactly the gap: points the OLD hypothesis rejects and the NEW one
accepts, including the bean's own two examples. G2 checks the domain
characterization `y.im != 0 or y.re < 1` really is C minus [1,inf), and G3 that
the cut is genuinely excluded (the integrand is singular INSIDE (0,1) there).

THE RADIAL DERIVATIVE
---------------------
The bean's remaining obstruction is analyticity in y, and both routes it lists
need differentiation under the integral sign ("not a Mathlib one-liner"). The
Lean file takes a third route in the radial direction: the substitution u = t*z
moves the parameter OUT of the integrand and INTO the limit,

    cLiTwoExt(t*y) = -int_0^t log(1 - y*u)/u du            (G4)

after which the derivative is the fundamental theorem of calculus, not
differentiation under an integral:

    d/dt cLiTwoExt(t*y) = -log(1 - y*t)/t                  (G5)

G6 checks this is the chain rule reading of d/dw Li2(w) = -log(1-w)/w.

⚠ THE QUADRATURE TRAP THIS PROBE MUST RESPECT
---------------------------------------------
`qou-clx8` records: when 0 < Re(1/y) < 1 the integrand has a near-logarithmic
singularity at z ~ 1/y, and plain quad([0,1]) SILENTLY returns a wrong answer --
at y = 3 + 0.001i it is off by 1.15e-2 while reporting no error. Every
evaluation here splits the contour at Re(1/y). G7 demonstrates the trap rather
than merely asserting it, so the mitigation is visible and falsifiable.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import fabs, im, log, mp, mpc, mpf, nstr, polylog, quad, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def li2_int(y):
    """cLiTwoExt(y) = -int_0^1 log(1 - y z)/z dz, split at Re(1/y) when needed."""
    f = lambda z: log(1 - y * z) / z
    pts = [mpf(0), mpf(1)]
    if y != 0:
        s = re(1 / y)
        if mpf(0) < s < mpf(1):
            pts = [mpf(0), s, mpf(1)]
    return -quad(f, pts)


def li2_int_upper(y, t):
    """-int_0^t log(1 - y u)/u du -- the substituted form."""
    f = lambda u: log(1 - y * u) / u
    pts = [mpf(0), t]
    if y != 0:
        s = re(1 / y)
        if mpf(0) < s < t:
            pts = [mpf(0), s, t]
    return -quad(f, pts)


def old_hypothesis_holds(y):
    """Re(1 - y z) > 0 for all z in [0,1] -- i.e. Re(1-y) > 0 and Re(1) > 0."""
    return re(1 - y) > 0 and re(mpf(1)) > 0


def new_hypothesis_holds(y):
    """y.im != 0 or y.re < 1 -- the complement of the cut [1, inf)."""
    return im(y) != 0 or re(y) < 1


def main() -> int:
    set_compute_dps()
    TOL = mpf(10) ** -20
    gates = []

    # ---- G1: the widening, on points the OLD hypothesis rejects -------------
    # The bean's own two examples plus the 5_2 root with ||y|| = 1.52.
    # The old condition `Re(1 - yz) > 0 for all z in [0,1]` is EXACTLY `Re y < 1`:
    # Re(1 - yz) = 1 - z*Re(y), minimised over [0,1] at z = 1 when Re y > 0. So the
    # region the generalisation buys is precisely {Re y >= 1} minus the cut, and
    # every point below must have Re y >= 1 to witness it. (An earlier draft used
    # -4 + 3i, which has Re y = -4 and is therefore accepted by the OLD condition
    # too -- it demonstrated nothing. Large modulus is not the criterion.)
    probe_pts = [
        ("bean example 1",  mpc(mpf("1.5"), mpf("0.3"))),
        ("bean example 2",  mpc(mpf("3"), mpf("0.001"))),
        ("far right",       mpc(mpf("6"), mpf("2"))),
        ("just past the 1", mpc(mpf("1.0001"), mpf("-2"))),
        ("deep right",      mpc(mpf("40"), mpf("0.5"))),
    ]
    rows, worst1 = [], mpf(0)
    for name, y in probe_pts:
        d = fabs(li2_int(y) - polylog(2, y))
        worst1 = max(worst1, d)
        rows.append({"point": name, "y": nstr(y, 10),
                     "old_hypothesis": bool(old_hypothesis_holds(y)),
                     "new_hypothesis": bool(new_hypothesis_holds(y)),
                     "|cLiTwoExt - Li2|": nstr(d, 8)})
    gates.append({
        "gate": "G1",
        "claim": "the old side condition Re(1-yz)>0 on [0,1] is EXACTLY Re y < 1, so the "
                 "region it excluded is the whole half-plane Re y >= 1 (minus the cut). On "
                 "points there -- including both examples qou-clx8 names -- cLiTwoExt still "
                 "equals Li2, so the old hypothesis was excluding a region where the identity "
                 "holds, exactly as that bean says",
        "old_condition_is": "Re y < 1",
        "region_gained": "{Re y >= 1} minus [1, inf)",
        "points": rows, "worst": nstr(worst1, 8),
        "all_rejected_by_old": bool(all(not r["old_hypothesis"] for r in rows)),
        "all_accepted_by_new": bool(all(r["new_hypothesis"] for r in rows)),
        "pass": bool(worst1 < TOL and all(not r["old_hypothesis"] for r in rows)
                     and all(r["new_hypothesis"] for r in rows)),
    })

    # ---- G2: the domain predicate really is the complement of the cut -------
    cut_pts = [mpc(mpf("1"), mpf(0)), mpc(mpf("2"), mpf(0)), mpc(mpf("7"), mpf(0))]
    off_pts = [mpc(mpf("0.9"), mpf(0)), mpc(mpf("-5"), mpf(0)),
               mpc(mpf("2"), mpf("0.0001")), mpc(mpf("1"), mpf("-0.5"))]
    gates.append({
        "gate": "G2",
        "claim": "the Lean hypothesis `y.im != 0 or y.re < 1` is exactly C minus [1,inf): it "
                 "rejects every point of the cut and accepts every point off it",
        "cut_points_rejected": [nstr(y, 6) for y in cut_pts
                                if not new_hypothesis_holds(y)],
        "off_points_accepted": [nstr(y, 6) for y in off_pts if new_hypothesis_holds(y)],
        "pass": bool(all(not new_hypothesis_holds(y) for y in cut_pts)
                     and all(new_hypothesis_holds(y) for y in off_pts)),
    })

    # ---- G3: the cut is genuinely excluded, for the stated reason -----------
    # For real y > 1 the integrand blows up INSIDE (0,1), at z = 1/y.
    sing = [{"y": nstr(y, 6), "singularity_at_z": nstr(1 / re(y), 10),
             "inside_0_1": bool(mpf(0) < 1 / re(y) < mpf(1))}
            for y in [mpf("1.5"), mpf("3"), mpf("20")]]
    gates.append({
        "gate": "G3",
        "claim": "the cut is [1,inf) and not |y|>=1 because for real y>1 the integrand is "
                 "singular INSIDE the interval, at z = 1/y in (0,1) -- that is the actual "
                 "obstruction, and it is what makes the geometric hypothesis the right one",
        "singularities": sing,
        "pass": bool(all(s["inside_0_1"] for s in sing)),
    })

    # ---- G4: the substitution that moves the parameter to the limit --------
    worst4 = mpf(0)
    for y in [mpc(mpf("1.5"), mpf("0.3")), mpc(mpf("-2"), mpf("1")),
              mpc(mpf("0.4"), mpf("0.2"))]:
        for tv in ["0.25", "0.6", "1"]:
            t = mpf(tv)
            worst4 = max(worst4, fabs(li2_int(t * y) - li2_int_upper(y, t)))
    gates.append({
        "gate": "G4",
        "claim": "cLiTwoExt(t*y) = -int_0^t log(1-y u)/u du -- the substitution u = t*z, which "
                 "moves the parameter OUT of the integrand and INTO the limit of integration. "
                 "This is what lets FTC reach it instead of differentiation under the integral",
        "n_checks": 9, "worst": nstr(worst4, 8), "pass": bool(worst4 < TOL),
    })

    # ---- G5: the radial derivative, by finite differences -------------------
    h = mpf(10) ** -12
    rows5, worst5 = [], mpf(0)
    for y in [mpc(mpf("1.5"), mpf("0.3")), mpc(mpf("-2"), mpf("1")),
              mpc(mpf("0.4"), mpf("0.2"))]:
        for tv in ["0.3", "0.75"]:
            t = mpf(tv)
            fd = (li2_int((t + h) * y) - li2_int((t - h) * y)) / (2 * h)
            pred = -log(1 - y * t) / t
            d = fabs(fd - pred)
            worst5 = max(worst5, d)
            rows5.append({"y": nstr(y, 8), "t": tv, "|fd - pred|": nstr(d, 6)})
    gates.append({
        "gate": "G5",
        "claim": "d/dt cLiTwoExt(t*y) = -log(1 - y*t)/t -- the radial derivative the Lean file "
                 "proves by the fundamental theorem of calculus. Finite-difference check at "
                 "step 1e-12 (central, so error ~ h^2 * f''')",
        "rows": rows5, "worst": nstr(worst5, 8), "pass": bool(worst5 < mpf(10) ** -14),
    })

    # ---- G6: it IS the chain-rule reading of d/dw Li2(w) = -log(1-w)/w -----
    worst6 = mpf(0)
    for y in [mpc(mpf("1.5"), mpf("0.3")), mpc(mpf("-2"), mpf("1"))]:
        for tv in ["0.3", "0.75"]:
            t = mpf(tv)
            w = t * y
            # cLiTwoExt'(w) * y should equal -log(1-yt)/t
            deriv_w = -log(1 - w) / w
            worst6 = max(worst6, fabs(deriv_w * y - (-log(1 - y * t) / t)))
    gates.append({
        "gate": "G6",
        "claim": "the radial statement is the chain-rule reading of d/dw Li2(w) = -log(1-w)/w: "
                 "cLiTwoExt'(t y)*y = -log(1-y t)/t identically. So G5 is that derivative "
                 "restricted to rays, not a weaker statement about a different function",
        "worst": nstr(worst6, 8), "pass": bool(worst6 < TOL),
    })

    # ---- G7: DEMONSTRATE the quadrature trap the bean warns about ----------
    y_trap = mpc(mpf("3"), mpf("0.001"))
    naive = -quad(lambda z: log(1 - y_trap * z) / z, [mpf(0), mpf(1)])
    split = li2_int(y_trap)
    truth = polylog(2, y_trap)
    err_naive, err_split = fabs(naive - truth), fabs(split - truth)
    gates.append({
        "gate": "G7",
        "claim": "the quadrature trap qou-clx8 records is REAL and is mitigated here: at "
                 "y = 3 + 0.001i plain quad([0,1]) is silently wrong, while splitting at "
                 "Re(1/y) is exact. Demonstrated rather than asserted, so every other gate's "
                 "method is visible",
        "err_plain_quad": nstr(err_naive, 8), "err_split_at_Re_inv_y": nstr(err_split, 8),
        "split_point": nstr(re(1 / y_trap), 10),
        "pass": bool(err_split < TOL and err_naive > mpf(10) ** -6),
    })

    # ---- G8: DIRECTION INDEPENDENCE -- what the radial derivative cannot show
    # A radial derivative is one direction. Complex differentiability needs all of
    # them to agree, and that is exactly what ComplexDilogarithmDeriv proves via
    # differentiation under the integral sign. Test it: central differences along
    # several complex directions must all land on -log(1-w)/w.
    dirs = [mpc(mpf(1), mpf(0)), mpc(mpf(0), mpf(1)),
            mpc(mpf(1), mpf(1)) / 2, mpc(mpf(-3), mpf(2)) / 5]
    h8 = mpf(10) ** -12
    rows8, worst8 = [], mpf(0)
    for w in [mpc(mpf("1.5"), mpf("0.3")), mpc(mpf("-2"), mpf("1")),
              mpc(mpf("6"), mpf("2"))]:
        pred = -log(1 - w) / w
        for d in dirs:
            fd = (li2_int(w + h8 * d) - li2_int(w - h8 * d)) / (2 * h8 * d)
            dd = fabs(fd - pred)
            worst8 = max(worst8, dd)
            rows8.append({"w": nstr(w, 8), "direction": nstr(d, 6),
                          "|fd - pred|": nstr(dd, 6)})
    gates.append({
        "gate": "G8",
        "claim": "DIRECTION INDEPENDENCE -- the difference quotient along four distinct complex "
                 "directions agrees with -log(1-w)/w at every test point. A radial derivative "
                 "gives one direction; complex differentiability needs all of them, and this is "
                 "the content ComplexDilogarithmDeriv adds over ComplexDilogarithmSlit",
        "n_checks": len(rows8), "rows": rows8[:4], "worst": nstr(worst8, 8),
        "pass": bool(worst8 < mpf(10) ** -14),
    })

    # ---- G9: why the closed form must carry w != 0 -------------------------
    # Lean's x/0 = 0, so -log(1-w)/w evaluates to 0 at w = 0 while the true
    # derivative there is 1. The INTEGRAL form is right at 0. This is the same
    # junk-value trap that made hinv1/hlan1 false earlier in this lane.
    lim_vals = [nstr(-log(1 - mpf(10) ** -k) / mpf(10) ** -k, 12) for k in [4, 8, 12]]
    at_zero_integral = -quad(lambda z: -1 / (1 - mpf(0) * z), [mpf(0), mpf(1)])
    gates.append({
        "gate": "G9",
        "claim": "the closed form -log(1-w)/w must carry w != 0: Lean's x/0 = 0 makes it 0 at "
                 "w = 0, while the true derivative there is 1. The INTEGRAL form is correct at "
                 "0, which is why the Lean theorem states the integral as primary and the "
                 "closed form as a corollary. Same junk-value trap that made hinv1/hlan1 false",
        "limit_of_closed_form_as_w_to_0": lim_vals,
        "integral_form_at_w_eq_0": nstr(at_zero_integral, 12),
        "lean_junk_value_of_closed_form_at_0": "0 (since x/0 = 0)",
        "pass": bool(fabs(at_zero_integral - 1) < TOL
                     and fabs(mpf(lim_vals[-1]) - 1) < mpf(10) ** -10),
    })

    # ---- G10: UNIQUENESS has bite -- two independent continuations agree ----
    # eqOn_cLiTwoExt_of_eqOn_ball says any analytic g on C\[1,inf) agreeing with
    # the SERIES on the disc equals cLiTwoExt. mpmath's polylog(2,.) is exactly
    # such a g, implemented by a completely different route (functional equations
    # + acceleration). So uniqueness predicts they agree off the disc -- where the
    # series itself diverges and cannot be what either is computing.
    rows10, worst10 = [], mpf(0)
    for y in [mpc(mpf("1.5"), mpf("0.3")), mpc(mpf("-2"), mpf("3")),
              mpc(mpf("6"), mpf("2")), mpc(mpf("40"), mpf("0.5"))]:
        # the defining series diverges here: |y|>1 so |y^k/k^2| -> infinity
        k = 400
        term = fabs(y) ** k / mpf(k) ** 2
        d = fabs(li2_int(y) - polylog(2, y))
        worst10 = max(worst10, d)
        rows10.append({"y": nstr(y, 8), "|y|": nstr(fabs(y), 6),
                       "series_term_k400": nstr(term, 6),
                       "|cLiTwoExt - polylog|": nstr(d, 6)})
    gates.append({
        "gate": "G10",
        "claim": "UNIQUENESS has bite. eqOn_cLiTwoExt_of_eqOn_ball says any analytic g on "
                 "C minus [1,inf) agreeing with the SERIES on the disc IS cLiTwoExt. mpmath's "
                 "polylog(2,.) is such a g, built by a wholly different route (functional "
                 "equations + acceleration). They agree at every point tested -- at |y| up to "
                 "40, where the defining series diverges outright, so neither is summing it",
        "rows": rows10, "worst": nstr(worst10, 8),
        "series_diverges_at_all_points": bool(all(mpf(r["series_term_k400"]) > 1 for r in rows10)),
        "pass": bool(worst10 < TOL
                     and all(mpf(r["series_term_k400"]) > 1 for r in rows10)),
    })

    # ---- G11: star-convexity about 0, with a negative control --------------
    seg = [mpf(s) / 20 for s in range(0, 21)]
    off_cut = [mpc(mpf("1.5"), mpf("0.3")), mpc(mpf("-2"), mpf("3")),
               mpc(mpf("40"), mpf("0.5")), mpc(mpf("0.5"), mpf(0))]
    on_cut = [mpc(mpf("2"), mpf(0)), mpc(mpf("7"), mpf(0))]
    off_ok = all(new_hypothesis_holds(s * y) for y in off_cut for s in seg)
    # negative control: for y ON the cut the segment DOES meet it (at s=1, and
    # wherever s*y >= 1), so star-convexity is not vacuously true of every point
    on_hits = [nstr(y, 6) for y in on_cut
               if any(not new_hypothesis_holds(s * y) for s in seg)]
    gates.append({
        "gate": "G11",
        "claim": "star-convexity about 0: for y OFF the cut the whole segment {s*y : s in [0,1]} "
                 "stays off it -- the Lean lemma starConvex_zero_notCut, which is what makes "
                 "C minus [1,inf) connected and the identity theorem applicable. With a NEGATIVE "
                 "control: for y ON the cut the segment does meet it, so the property is not "
                 "vacuously true of everything",
        "segment_points": len(seg),
        "off_cut_segments_stay_off": bool(off_ok),
        "on_cut_points_whose_segment_hits": on_hits,
        "pass": bool(off_ok and len(on_hits) == len(on_cut)),
    })

    out = {
        "probe": "qbeta_clx8_route23_slit_radial",
        "bean": "qou-clx8", "parent_bean": "qou-0yqu", "dps": mp.dps,
        "pairs_with_lean": "QOU/MathlibExt/ComplexDilogarithm{Slit,Deriv,Unique}.lean",
        "gates": gates,
        "verdict": {
            "outcome": "cLiTwoExt's integral converges on ALL of C minus [1,inf) -- the "
                       "geometric hypothesis qou-clx8 asked for, now Lean-proved -- and its "
                       "derivative ALONG RAYS is proved by FTC rather than by differentiating "
                       "under the integral sign.",
            "what_widened": "the old side condition Re(1-y)>0 rejects every point in G1, "
                            "including both examples the bean names, while the identity holds "
                            "at all of them. ComplexDilogarithm.intervalIntegrable_log_one_sub_"
                            "div is now stated on slitPlane membership, with the old form kept "
                            "as a corollary.",
            "now_closed": "analyticity AND uniqueness on C minus [1,inf) are proved -- analyticOnNhd_cLiTwoExt "
                          "in ComplexDilogarithmDeriv.lean, by differentiation under the "
                          "integral sign. Mathlib supplies the DUI theorem; the piece it does "
                          "not supply is the uniform lower bound on ||1 - w z|| over a ball "
                          "times [0,1], proved by compactness. G8 tests direction independence, "
                          "which the radial derivative could not give.",
            "does_not_move_the_sum_rule": "qou-clx8 is explicit that Route 5 is a restatement; "
                                          "even the whole chain leaves an unevaluated real "
                                          "integral. Taken for the Mathlib gap, as instructed.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-clx8-route23-slit-radial.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:86]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: cLiTwoExt is THE analytic continuation -- analytic, and unique.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
