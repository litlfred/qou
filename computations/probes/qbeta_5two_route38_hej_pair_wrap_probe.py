#!/usr/bin/env python3
"""Route 38 -- `he_j` at the pair: WHERE the 2*pi wraps are, and which grouping
survives. Bean `qou-glbl`, obligation (1), the last one open.

Route 36 G13 reduced `he_j` at the pair to `k = 0` in `dVdy*y = -2*pi*i*k`,
equivalently to

    S := arg(1-y) + arg(1-xy) + arg(1-y/x) - 2*arg(-y)  ==  0,

measured identically 0 (within 9.2e-41), and it closed the term-by-term route
(the four terms bounded separately give 11.857 > 2*pi). What it left open was
"grouping 2", `arg(1-xy) + arg(1-y/x) - 2*arg(-y)`, measured under pi/2 and
needing only 3*pi/2.

WHAT CAME OUT
-------------
A FOUR-REGIME interval argument pins `k = 0` on the open arc without ever needing
the three splits to be individually legitimate. With `A = arg(1-y)`,
`a1 = arg(1-xy)`, `a2 = arg(1-y/x)`, `C = 2 arg(-y)`, the quantity `A + a1 + a2 - C`
is `2*pi*k`, and in each regime the four components lie in intervals whose sum is
STRICTLY inside `(-2pi, 2pi)`:

    regime                              supplies the missing pi/2 via        n
    complex pair, Re y > 0              Re y > 0 forces cos phi > 0,       160
                                        hence sign(Im xy) = sign(Im y)
    complex pair, Re y <= 0, cos <= 0   both terms of Im(xy) flip          107
    complex pair, Re y <= 0, cos > 0    Re(xy) + Re(y/x) = 2 cos(phi) Re y  40
                                        <= 0, so one factor has Re <= 0
    real pair (past the discriminant)   both roots negative: A = C = 0     186

Only `Im y > 0` is analysed. `Ypair.2 = conj Ypair.1` and conjugation swaps `x*y`
with `y/x` on `|x| = 1`, so `S(conj y) = -S(y)` and the second branch is free.

⚠ AND IT IS FALSE AT `phi = pi`, on `Ypair.2`, where `S = 2*pi` (G15). Benign --
`envelopeS_total` needs the derivative only on `Ico 0 pi` -- and it is the same
endpoint, with the same cause, as VSide's failure: `x*y = 2.2469796` lands ON
Li2's cut. That is the SECOND time an endpoint has hidden behind open-interval
sampling in this lane.

THE POINT OF THIS PROBE
-----------------------
`S = 0` is exactly the statement that three `Complex.log_mul` splits are all
legitimate at once:

    (i)   log(1-xy) + log(1-y/x) = log((1-xy)(1-y/x))   needs arg+arg in (-pi,pi]
    (ii)  log(1-y)  + log(that)  = log(y^2)             needs arg+arg in (-pi,pi]
    (iii) 2*log(-y)              = log(y^2)             needs 2*arg(-y) in (-pi,pi]

and (iii) is FALSE where `Re y > 0` -- Route 36 G13 measured `max Re y = 0.7848`
at the pair, attained near phi = 0 where the pair is genuinely complex. So the
naive three-split proof does not exist, and `S = 0` holds only because the wraps
CANCEL. This probe measures each wrap integer separately, so the Lean proof is
written against where they actually are rather than against a hope that they
vanish.

⚠ AND A HYPOTHESIS THAT IS NOT GLOBAL
-------------------------------------
The tree's sign facts are not uniform over the arc. `im_mul_Ypair_fst_neg` and
`im_div_Ypair_snd_pos` both carry `hcneg : cos phi < 0` -- they hold only on
`phi > pi/2`. Only `im_mul_Ypair_snd_neg` / `im_div_Ypair_fst_pos` are
unconditional. Any grouping argument that assumes all four signs everywhere is
assuming something the tree does not have and that is measurably false; G3 checks
exactly which of the four hold where.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (arg, cos, exp, fabs, findroot, im, log, mp, mpc, mpf, nint,
                    nstr, pi, polyroots, re, sin, sqrt)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def real_root(c):
    """The unique root of `unitCubic c t = t^3 - 2ct^2 + (2c+1)t - 1` in (0,1)."""
    rs = polyroots([1, -2 * c, 2 * c + 1, -1], maxsteps=200, extraprec=200)
    cands = [re(r) for r in rs if fabs(im(r)) < mpf(10) ** -25 and 0 < re(r) < 1]
    assert len(cands) == 1, f"c={c}: {len(cands)} roots in (0,1)"
    return cands[0]


def pair_at(ph):
    """`(Ypair.1, Ypair.2, pairDisc)` -- Lean's `otherRoots pairBeta pairGamma`.

    Lean's `otherRoots beta gamma` is piecewise on `beta^2 - 4*gamma`: the real
    branch `(-beta +- sqrt d)/2` when `d >= 0`, and `-beta/2 -+ i*sqrt(-d)/2`
    when `d < 0`. Reproduced here rather than read off `polyroots`, so the
    LABELLING matches the one the Lean proof will carry.
    """
    c = cos(ph)
    t = real_root(c)
    beta = t - 2 * c
    gamma = t ** 2 - 2 * c * t + 2 * c + 1
    d = beta ** 2 - 4 * gamma
    if d < 0:
        s = sqrt(-d) / 2
        return mpc(-beta / 2, s), mpc(-beta / 2, -s), d
    s = sqrt(d) / 2
    return mpc(-beta / 2 + s, 0), mpc(-beta / 2 - s, 0), d


def wrap(theta):
    """The integer `n` with `theta - 2*pi*n` in (-pi, pi]. Exact at 40 dps."""
    return int(nint(theta / (2 * pi)))


def main() -> int:
    set_compute_dps()
    N = 400
    gates = []

    samples = []
    for i in range(N):
        ph = pi * mpf(i + 1) / (N + 1)
        x = exp(mpc(0, 1) * ph)
        y1, y2, d = pair_at(ph)
        for label, y in (("fst", y1), ("snd", y2)):
            samples.append({
                "phi": ph, "x": x, "y": y, "disc": d, "branch": label,
                "c": cos(ph),
            })

    # ---- G1: `S` really is identically zero at the pair ---------------------
    worst_S = mpf(0)
    worst_curve = mpf(0)
    for s in samples:
        x, y = s["x"], s["y"]
        worst_curve = max(worst_curve,
                          fabs(x * y ** 3 - (x ** 2 + 1) * y ** 2
                               + (x ** 2 + x + 1) * y - x))
        S = arg(1 - y) + arg(1 - x * y) + arg(1 - y / x) - 2 * arg(-y)
        worst_S = max(worst_S, fabs(S))
    gates.append({
        "gate": "G1",
        "claim": "the quantity to be proved zero, re-measured on the LEAN labelling "
                 "(`otherRoots` reproduced branch-for-branch, not read off polyroots): "
                 "S = arg(1-y) + arg(1-xy) + arg(1-y/x) - 2 arg(-y) vanishes identically at both "
                 "pair branches, at all 800 checks. Also re-checks that each sampled y IS a root "
                 "of the curve, so the labelling has not drifted from the polynomial",
        "checks": len(samples),
        "worst_abs_S": nstr(worst_S, 12),
        "worst_curve_residual": nstr(worst_curve, 12),
        "pass": bool(worst_S < mpf(10) ** -30 and worst_curve < mpf(10) ** -30),
    })

    # ---- G2: the three wrap integers, separately ---------------------------
    # (i)   n1 = wrap(arg(1-xy) + arg(1-y/x))
    # (ii)  n2 = wrap(arg(1-y) + arg((1-xy)(1-y/x)))
    # (iii) n3 = wrap(2*arg(-y))
    wraps = {"n1": set(), "n2": set(), "n3": set()}
    n3_nonzero_needs_re_pos = True
    identity_holds = 0
    for s in samples:
        x, y = s["x"], s["y"]
        a_xy, a_yx = arg(1 - x * y), arg(1 - y / x)
        n1 = wrap(a_xy + a_yx)
        n2 = wrap(arg(1 - y) + arg((1 - x * y) * (1 - y / x)))
        n3 = wrap(2 * arg(-y))
        wraps["n1"].add(n1)
        wraps["n2"].add(n2)
        wraps["n3"].add(n3)
        if n3 != 0 and not (re(y) > 0):
            n3_nonzero_needs_re_pos = False
        # S = 0 must be exactly n1 + n2 - n3 = 0 after the splits
        if n1 + n2 - n3 == 0:
            identity_holds += 1
    gates.append({
        "gate": "G2",
        "claim": "WHERE THE WRAPS ARE. `S = 0` is three `log_mul` splits holding at once, and "
                 "they do NOT: the split (iii) `2 log(-y) = log(y^2)` needs 2 arg(-y) in "
                 "(-pi,pi], i.e. Re y <= 0, and Re y reaches +0.7848 at the pair. So a proof that "
                 "performs the three splits unconditionally is proving something false. The wraps "
                 "CANCEL -- n1 + n2 - n3 = 0 at every check -- which is a different theorem and "
                 "needs the cancellation argued, not assumed. Every n3 != 0 occurs at Re y > 0, "
                 "which is the shape a case split can key on",
        "n1_values": sorted(wraps["n1"]),
        "n2_values": sorted(wraps["n2"]),
        "n3_values": sorted(wraps["n3"]),
        "cancellation_holds_at": identity_holds,
        "checks": len(samples),
        "n3_nonzero_only_where_Re_y_positive": bool(n3_nonzero_needs_re_pos),
        "pass": bool(identity_holds == len(samples)),
    })

    # ---- G3: WHICH of the tree's four sign facts hold WHERE -----------------
    # `im_mul_Ypair_fst_neg` and `im_div_Ypair_snd_pos` carry `cos phi < 0`.
    # A grouping argument that assumes all four everywhere assumes something false.
    counts = {"fst_mul_neg": [0, 0], "snd_mul_neg": [0, 0],
              "fst_div_pos": [0, 0], "snd_div_pos": [0, 0]}
    fst_mul_fails_only_c_pos = True
    for s in samples:
        x, y, lab = s["x"], s["y"], s["branch"]
        key_mul = f"{lab}_mul_neg"
        key_div = f"{lab}_div_pos"
        ok_mul = im(x * y) < 0
        ok_div = im(y / x) > 0
        counts[key_mul][0 if ok_mul else 1] += 1
        counts[key_div][0 if ok_div else 1] += 1
        if lab == "fst" and not ok_mul and s["c"] < 0:
            fst_mul_fails_only_c_pos = False
    gates.append({
        "gate": "G3",
        "claim": "THE TREE'S SIGN FACTS ARE NOT UNIFORM, and a grouping argument must not assume "
                 "they are. `im_mul_Ypair_fst_neg` and `im_div_Ypair_snd_pos` carry `cos phi < 0` "
                 "as a hypothesis; only the `snd`/`fst` pair is unconditional. Measured: the "
                 "`fst` multiplicative sign genuinely FAILS on part of the arc, and every failure "
                 "is at cos phi > 0 -- so the hypothesis is exactly right rather than an artefact "
                 "of how the lemma was proved",
        "holds_vs_fails": {k: v for k, v in counts.items()},
        "fst_mul_failures_all_at_cos_positive": bool(fst_mul_fails_only_c_pos),
        "pass": bool(counts["snd_mul_neg"][1] == 0 and counts["fst_div_pos"][1] == 0
                     and counts["fst_mul_neg"][1] > 0 and fst_mul_fails_only_c_pos),
    })

    # ---- G4: is split (i) always legitimate? -------------------------------
    # If `arg(1-xy) + arg(1-y/x)` is always in (-pi, pi], (i) is unconditional and
    # the whole difficulty is (ii)+(iii).
    worst_i = mpf(0)
    i_ok = 0
    for s in samples:
        x, y = s["x"], s["y"]
        t = arg(1 - x * y) + arg(1 - y / x)
        worst_i = max(worst_i, fabs(t))
        if -pi < t <= pi:
            i_ok += 1
    gates.append({
        "gate": "G4",
        "claim": "split (i) -- log(1-xy) + log(1-y/x) = log of the product -- is legitimate at "
                 "EVERY check, with the sum staying inside (-pi, pi]. That is the one of the "
                 "three splits that costs nothing, and it is what turns the open obligation from "
                 "four correlated arguments into two",
        "checks_legitimate": i_ok, "checks": len(samples),
        "worst_abs_sum": nstr(worst_i, 12),
        "margin_to_pi": nstr(pi - worst_i, 12),
        "pass": bool(i_ok == len(samples)),
    })

    # ---- G5: the surviving obligation, as a bound --------------------------
    # grouping2 = arg(1-xy) + arg(1-y/x) - 2 arg(-y), needs |.| < 3*pi/2.
    worst_g2 = mpf(0)
    worst_g1 = mpf(0)
    at = None
    for s in samples:
        x, y = s["x"], s["y"]
        g2 = arg(1 - x * y) + arg(1 - y / x) - 2 * arg(-y)
        g1 = arg(1 - y)
        if fabs(g2) > worst_g2:
            worst_g2, at = fabs(g2), s["phi"]
        worst_g1 = max(worst_g1, fabs(g1))
    gates.append({
        "gate": "G5",
        "claim": "the surviving obligation as an inequality: |arg(1-xy) + arg(1-y/x) - 2 arg(-y)| "
                 "< 3*pi/2 would pin k = 0 given the already-proved |arg(1-y)| < pi/2. Measured "
                 "max is under pi/2, so there is a factor of three in hand -- but S = 0 means "
                 "grouping 2 is EXACTLY -arg(1-y), so the two maxima must agree, and a proof that "
                 "produced a different bound for them would be proving the wrong thing",
        "max_abs_grouping2": nstr(worst_g2, 12),
        "max_abs_arg_one_sub_y": nstr(worst_g1, 12),
        "the_two_agree": bool(fabs(worst_g2 - worst_g1) < mpf(10) ** -30),
        "attained_at_phi": nstr(at, 12) if at is not None else None,
        "needed_bound_3pi_over_2": nstr(3 * pi / 2, 12),
        "pass": bool(worst_g2 < 3 * pi / 2 and fabs(worst_g2 - worst_g1) < mpf(10) ** -30),
    })

    # ---- G6: where Re y > 0, and what that region is ------------------------
    re_pos = [s for s in samples if re(s["y"]) > 0]
    re_pos_cplx = [s for s in re_pos if s["disc"] < 0]
    max_c_with_re_nonpos = None
    min_c_with_re_pos = None
    for s in samples:
        if re(s["y"]) > 0:
            min_c_with_re_pos = (s["c"] if min_c_with_re_pos is None
                                 else min(min_c_with_re_pos, s["c"]))
        else:
            max_c_with_re_nonpos = (s["c"] if max_c_with_re_nonpos is None
                                    else max(max_c_with_re_nonpos, s["c"]))
    gates.append({
        "gate": "G6",
        "claim": "the region a case split would have to key on. `Re y = cos phi - t/2` at the "
                 "pair (`re_Ypair_eq`, proved), so Re y > 0 is exactly cos phi > t/2 -- an "
                 "explicit, checkable condition on phi rather than on the root. Every one of "
                 "these points has the pair GENUINELY COMPLEX, so it cannot be dodged by "
                 "restricting to the real branch of `otherRoots`",
        "checks_with_Re_y_positive": len(re_pos),
        "of_which_complex_pair": len(re_pos_cplx),
        "checks": len(samples),
        "min_cos_phi_with_Re_y_positive": (nstr(min_c_with_re_pos, 12)
                                           if min_c_with_re_pos is not None else None),
        "max_cos_phi_with_Re_y_nonpositive": (nstr(max_c_with_re_nonpos, 12)
                                              if max_c_with_re_nonpos is not None else None),
        "pass": bool(len(re_pos) > 0 and len(re_pos_cplx) == len(re_pos)),
    })

    # ---- G7: the cheap half -- where Re y <= 0 the three splits DO work -----
    easy_ok = 0
    easy_total = 0
    for s in samples:
        x, y = s["x"], s["y"]
        if re(y) > 0:
            continue
        easy_total += 1
        c1 = -pi < arg(1 - x * y) + arg(1 - y / x) <= pi
        c2 = -pi < arg(1 - y) + arg((1 - x * y) * (1 - y / x)) <= pi
        c3 = -pi < 2 * arg(-y) <= pi
        if c1 and c2 and c3:
            easy_ok += 1
    gates.append({
        "gate": "G7",
        "claim": "ON `Re y <= 0` ALL THREE SPLITS ARE LEGITIMATE, so on that part of the arc "
                 "`k = 0` follows from three `Complex.log_mul` applications and the saddle "
                 "identity, with no bounding argument at all. That is the half of the obligation "
                 "that is now an assembly of already-available lemmas; the residue is `Re y > 0`",
        "checks_with_Re_y_nonpositive": easy_total,
        "all_three_splits_legitimate": easy_ok,
        "pass": bool(easy_total > 0 and easy_ok == easy_total),
    })

    # ---- G8: the endpoint phi = pi, exactly ---------------------------------
    x = mpc(-1, 0)
    c = mpf(-1)
    t = real_root(c)
    beta = t - 2 * c
    gamma = t ** 2 - 2 * c * t + 2 * c + 1
    d = beta ** 2 - 4 * gamma
    s_ = sqrt(d) / 2
    ends = [(-beta / 2 + s_), (-beta / 2 - s_)]
    end_args = []
    for yv in ends:
        y = mpc(yv, 0)
        end_args.append({
            "y": nstr(yv, 16),
            "arg_neg_y": nstr(arg(-y), 12),
            "S": nstr(arg(1 - y) + arg(1 - x * y) + arg(1 - y / x) - 2 * arg(-y), 12),
        })
    gates.append({
        "gate": "G8",
        "claim": "the endpoint, evaluated EXACTLY at x = mpc(-1,0) rather than exp(i*pi) -- which "
                 "returns -1 + 4.1e-43j and has already produced one false pass in this lane "
                 "(Route 36 G7). At phi = pi the discriminant is POSITIVE, so the pair is real "
                 "and both roots are NEGATIVE; arg(-y) = 0 there, and the (iii) split is trivial",
        "pairDisc_at_pi": nstr(d, 12),
        "both_roots_negative": bool(ends[0] < 0 and ends[1] < 0),
        "branches": end_args,
        "pass": bool(d > 0 and ends[0] < 0 and ends[1] < 0),
    })

    # ---- G9..G15: THE CASE ANALYSIS, checked clause by clause ---------------
    # The obligation is `A + B - C = 2*pi*k` with
    #     A = arg(1-y),  B = arg(1-xy) + arg(1-y/x),  C = 2*arg(-y),
    # and `k = 0` follows as soon as the total is pinned inside (-2pi, 2pi).
    #
    # ⚠ Only ONE branch is analysed. `Ypair.2 = conj Ypair.1` (proved), and on
    # |x| = 1 conjugation swaps x*y with y/x, so S(conj y) = -S(y) and the second
    # branch is free (G14). An earlier draft of these gates tried to MIRROR each
    # inequality branch-by-branch with a sign factor and failed G10/G11: the two
    # branches are NOT related by flipping the sign of Im y in each inequality
    # separately -- `Im(x*y)` for one branch pairs with `Im(y/x)` for the other,
    # not with itself. The conjugation is the only correct symmetry.
    #
    # Writing y = p + qi with q >= 0, x = c + si with s = sin phi >= 0, the two
    # tree facts are exactly TWO inequalities, not four:
    #     c*q - s*p > 0   (unconditional)      == im_div_Ypair_fst_pos / _snd_mul_neg
    #     c*q + s*p < 0   (needs c < 0)        == im_mul_Ypair_fst_neg / _snd_div_pos
    ana = [t for t in samples if im(t["y"]) > 0 or t["disc"] >= 0]
    reg = {"cplx_re_pos": 0, "cplx_re_nonpos_c_nonpos": 0,
           "cplx_re_nonpos_c_pos": 0, "real_pair": 0}
    fail = {k: 0 for k in reg}
    worst_lo, worst_hi = None, None
    widest_lo, widest_hi = None, None
    lo_at, hi_at = None, None
    comp_fail = {}
    real_pair_both_neg = True
    sum_re_identity = mpf(0)
    for t_ in ana:
        x, y, d, ph, c = t_["x"], t_["y"], t_["disc"], t_["phi"], t_["c"]
        A, a1, a2, C = arg(1 - y), arg(1 - x * y), arg(1 - y / x), 2 * arg(-y)
        sum_re_identity = max(sum_re_identity,
                              fabs(re(x * y) + re(y / x) - 2 * c * re(y)))
        # `box` is the interval the ARGUMENT claims for each of the four
        # components. The regime's overall bound is their SUM, computed below
        # rather than asserted -- that is what G13 checks.
        if d >= 0:
            key = "real_pair"
            if not re(y) < 0:
                real_pair_both_neg = False
            box = {"A": (0, 0), "a1": (0, pi), "a2": (-pi, 0), "negC": (0, 0)}
            ok = (im(y) == 0 and im(x * y) < 0 and im(y / x) > 0)
        elif re(y) > 0:
            key = "cplx_re_pos"
            box = {"A": (-pi / 2, 0), "a1": (-pi, 0), "a2": (-pi, 0),
                   "negC": (pi, 2 * pi)}
            ok = (c > 0 and im(x * y) > 0 and im(y / x) > 0 and 0 < arg(y) < pi / 2)
        elif c <= 0:
            key = "cplx_re_nonpos_c_nonpos"
            box = {"A": (-pi / 2, 0), "a1": (0, pi), "a2": (-pi, 0),
                   "negC": (0, pi)}
            ok = (im(x * y) <= 0 and im(y / x) > 0 and pi / 2 <= arg(y) < pi)
        else:
            key = "cplx_re_nonpos_c_pos"
            if re(x * y) <= 0:                      # sub-case (a)
                box = {"A": (-pi / 2, 0), "a1": (-pi / 2, pi / 2), "a2": (-pi, 0),
                       "negC": (0, pi)}
            else:                                   # sub-case (b): Re(y/x) <= 0
                box = {"A": (-pi / 2, 0), "a1": (-pi, pi), "a2": (-pi / 2, 0),
                       "negC": (0, pi)}
            ok = (min(re(x * y), re(y / x)) <= 0 and im(y / x) > 0
                  and pi / 2 <= arg(y) < pi)
        reg[key] += 1
        if not ok:
            fail[key] += 1
        comps = {"A": A, "a1": a1, "a2": a2, "negC": -C}
        for nm, v in comps.items():
            b = box[nm]
            if not (b[0] <= v <= b[1]):
                comp_fail[key] = comp_fail.get(key, 0) + 1
                break
        lo = sum(box[nm][0] for nm in comps)
        hi = sum(box[nm][1] for nm in comps)
        widest_lo = lo if widest_lo is None else min(widest_lo, lo)
        widest_hi = hi if widest_hi is None else max(widest_hi, hi)
        if worst_lo is None or lo + 2 * pi < worst_lo:
            worst_lo, lo_at = lo + 2 * pi, (nstr(ph, 10), key)
        if worst_hi is None or 2 * pi - hi < worst_hi:
            worst_hi, hi_at = 2 * pi - hi, (nstr(ph, 10), key)
    gates.append({
        "gate": "G9",
        "claim": "REGIME 1 -- complex pair, Re y > 0. `Re y = cos phi - t/2` with t > 0, so Re y > 0 "
                 "FORCES cos phi > 0; then Im(xy) = cos(phi)*Im y + sin(phi)*Re y has both terms "
                 "positive, so arg(1-xy) < 0. This is precisely the region where the tree's "
                 "`im_mul_Ypair_fst_neg` FAILS (G3) -- and the failure is what supplies the bound. "
                 "The missing hypothesis is not a gap to fill, it is the other half of a case split",
        "checks_in_regime": reg["cplx_re_pos"], "clause_failures": fail["cplx_re_pos"],
        "bound": "(-3pi/2, 2pi)",
        "pass": bool(reg["cplx_re_pos"] > 0 and fail["cplx_re_pos"] == 0),
    })
    gates.append({
        "gate": "G10",
        "claim": "REGIME 2 -- complex pair, Re y <= 0 and cos phi <= 0. Both terms of "
                 "Im(xy) = cos(phi)*Im y + sin(phi)*Re y are now <= 0, so arg(1-xy) lands on the "
                 "OTHER side from regime 1. The upper end of the interval is 2pi and is reached "
                 "only if arg(1-y) = 0, which the strict Im y > 0 forbids -- so the bound is "
                 "strict for a reason, not by rounding",
        "checks_in_regime": reg["cplx_re_nonpos_c_nonpos"],
        "clause_failures": fail["cplx_re_nonpos_c_nonpos"],
        "bound": "(-3pi/2, 2pi)",
        "pass": bool(reg["cplx_re_nonpos_c_nonpos"] > 0
                     and fail["cplx_re_nonpos_c_nonpos"] == 0),
    })
    gates.append({
        "gate": "G11",
        "claim": "REGIME 3 -- complex pair, Re y <= 0 but cos phi > 0, where NEITHER Im-sign "
                 "argument applies. The missing pi/2 comes from an identity instead: "
                 "Re(xy) + Re(y/x) = 2*cos(phi)*Re(y) <= 0 here, so at least one of the two "
                 "factors has Re <= 0 and hence |arg| < pi/2. WHICH one is not determined and does "
                 "not need to be -- either sub-case lands inside (-2pi, 2pi)",
        "checks_in_regime": reg["cplx_re_nonpos_c_pos"],
        "clause_failures": fail["cplx_re_nonpos_c_pos"],
        "identity_residual_Re_xy_plus_Re_y_over_x": nstr(sum_re_identity, 12),
        "bound": "(-2pi, 2pi)",
        "pass": bool(reg["cplx_re_nonpos_c_pos"] > 0 and fail["cplx_re_nonpos_c_pos"] == 0
                     and sum_re_identity < mpf(10) ** -30),
    })
    gates.append({
        "gate": "G12",
        "claim": "REGIME 4 -- the REAL pair, past the discriminant crossing. Both roots are "
                 "NEGATIVE there (sum 2c - t < 0, product pairGamma > 0), so arg(1-y) = 0 and "
                 "arg(-y) = 0 outright and the whole quantity collapses to B, inside (-pi, pi) by "
                 "the two Im signs. This regime is the one that needs sin phi > 0, and it is "
                 "exactly the one that breaks at phi = pi -- where VSide breaks too (G15)",
        "checks_in_regime": reg["real_pair"], "clause_failures": fail["real_pair"],
        "both_real_roots_negative": bool(real_pair_both_neg),
        "bound": "(-pi, pi)",
        "pass": bool(reg["real_pair"] > 0 and fail["real_pair"] == 0 and real_pair_both_neg),
    })
    gates.append({
        "gate": "G13",
        "claim": "THE ARITHMETIC OF THE BOUND, not its conclusion -- and the first draft of this "
                 "gate got that wrong. It checked that A + arg(1-xy) + arg(1-y/x) - C lies inside "
                 "the regime interval, which is VACUOUS: the total is identically 0 (G1), so any "
                 "interval containing 0 passes and the gate reported a slack of exactly pi "
                 "everywhere. What is actually load-bearing is that each of the FOUR COMPONENTS "
                 "lies in the interval the argument claims for it, and that the four claimed "
                 "intervals SUM to something inside (-2pi, 2pi). Both are now checked, the sum "
                 "computed rather than asserted",
        "analysed_samples": len(ana),
        "component_interval_failures": comp_fail,
        "widest_summed_interval": [nstr(widest_lo, 12), nstr(widest_hi, 12)],
        "slack_of_summed_lower_bound_above_minus_2pi": nstr(worst_lo, 12),
        "where_lower_is_tightest": lo_at,
        "slack_of_summed_upper_bound_below_2pi": nstr(worst_hi, 12),
        "where_upper_is_tightest": hi_at,
        "pass": bool(len(comp_fail) == 0 and worst_lo >= 0 and worst_hi >= 0),
    })

    # ---- G14: the second branch is free, by conjugation --------------------
    worst_conj = mpf(0)
    pairs_checked = 0
    for i in range(0, len(samples), 2):
        f_, s_ = samples[i], samples[i + 1]
        if f_["disc"] >= 0:
            continue
        pairs_checked += 1
        x = f_["x"]
        Sf = (arg(1 - f_["y"]) + arg(1 - x * f_["y"]) + arg(1 - f_["y"] / x)
              - 2 * arg(-f_["y"]))
        Ss = (arg(1 - s_["y"]) + arg(1 - x * s_["y"]) + arg(1 - s_["y"] / x)
              - 2 * arg(-s_["y"]))
        worst_conj = max(worst_conj, fabs(Ss + Sf),
                         fabs(s_["y"] - mpc(re(f_["y"]), -im(f_["y"]))))
    gates.append({
        "gate": "G14",
        "claim": "THE SECOND BRANCH IS FREE. `Ypair.2 = conj Ypair.1` (proved), and on |x| = 1 "
                 "conjugation swaps x*y with y/x, so S(conj y) = -S(y) and k = 0 for one branch "
                 "iff for the other. This is why only Im y > 0 is analysed above. It matters: an "
                 "earlier draft mirrored each inequality separately with a sign factor and FAILED "
                 "-- Im(x*y) for one branch pairs with Im(y/x) for the OTHER, not with itself",
        "conjugate_pairs_checked": pairs_checked,
        "worst_residual": nstr(worst_conj, 12),
        "pass": bool(pairs_checked > 0 and worst_conj < mpf(10) ** -30),
    })

    # ---- G15: the endpoint FAILS, and it is the same failure as VSide's -----
    xe = mpc(-1, 0)
    ce = mpf(-1)
    te = real_root(ce)
    be = te - 2 * ce
    ge = te ** 2 - 2 * ce * te + 2 * ce + 1
    de = be ** 2 - 4 * ge
    se = sqrt(de) / 2
    end_S = []
    for yv in (-be / 2 + se, -be / 2 - se):
        y = mpc(yv, 0)
        end_S.append(arg(1 - y) + arg(1 - xe * y) + arg(1 - y / xe) - 2 * arg(-y))
    gates.append({
        "gate": "G15",
        "claim": "⚠ `S = 0` FAILS AT phi = pi, on Ypair.2, where it is 2*pi -- so k = ±1 there and "
                 "`he_j` is FALSE at the endpoint. G1 samples the OPEN interval and structurally "
                 "cannot see this, the SECOND time in this lane an endpoint has been hidden that "
                 "way (Route 36 G7 was the first). Benign for the same reason: `envelopeS_total` "
                 "needs the derivative only on `Ico 0 pi`. And the cause is identical to VSide's "
                 "endpoint failure -- x*y = 2.2469796 lands ON Li2's cut, so arg(1-xy) and "
                 "arg(1-y/x) are both pi instead of cancelling. Evaluated at x = mpc(-1,0) "
                 "exactly; exp(i*pi) returns -1 + 4.1e-43j and would report a clean 0",
        "S_at_pi_branch_1": nstr(end_S[0], 12),
        "S_at_pi_branch_2": nstr(end_S[1], 12),
        "two_pi": nstr(2 * pi, 12),
        "pass": bool(fabs(end_S[0]) < mpf(10) ** -30
                     and fabs(end_S[1] - 2 * pi) < mpf(10) ** -30),
    })

    out = {
        "probe": "qbeta_5two_route38_hej_pair_wrap",
        "bean": "qou-glbl", "dps": mp.dps,
        "pairs_with_lean": [
            "QOU/QBeta/FiveTwoRootLabelling.lean (Ypair, the four sign facts)",
            "QOU/QBeta/FiveTwoEnvelopeWiring.lean (dVdy, exists_int_dVdy_mul)",
        ],
        "gates": gates,
        "verdict": {
            "measured": "S = 0 at both pair branches on the OPEN arc, but NOT because the three "
                        "log_mul splits all hold -- split (iii) fails wherever Re y > 0. The "
                        "wraps cancel: n1 + n2 - n3 = 0 at every check.",
            "route": "a FOUR-REGIME interval argument pins k = 0 without ever needing the splits "
                     "to be individually legitimate. Writing A = arg(1-y), a1 = arg(1-xy), "
                     "a2 = arg(1-y/x), C = 2 arg(-y), the quantity A + a1 + a2 - C is 2*pi*k, and "
                     "in each regime the four components sit in intervals whose sum is strictly "
                     "inside (-2pi, 2pi). Regimes 1 and 2 split on the sign of Im(xy), which is "
                     "forced by cos phi; regime 3 has neither sign and uses the identity "
                     "Re(xy) + Re(y/x) = 2 cos(phi) Re(y) <= 0 instead; regime 4 is the real pair, "
                     "where A = C = 0 outright. Only Im y > 0 is analysed; the other branch is the "
                     "conjugate (G14).",
            "regime_sizes": {"cplx_Re_y_pos": 160, "cplx_Re_y_nonpos_cos_nonpos": 107,
                             "cplx_Re_y_nonpos_cos_pos": 40, "real_pair": 186},
            "trap": "the tree's four sign facts are NOT uniform -- two carry `cos phi < 0` and "
                    "the `fst` multiplicative one measurably fails without it (G3). The failure "
                    "region is regime 1, where the OPPOSITE sign is what supplies the bound.",
            "endpoint": "S = 2*pi at Ypair.2 when phi = pi, so `he_j` is FALSE there (G15) -- the "
                        "same endpoint, and the same cause, as VSide's failure. `envelopeS_total` "
                        "needs the derivative only on `Ico 0 pi`.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route38-hej-pair-wrap.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']:>3}  pass={g['pass']}  {g['claim'][:80]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + ("S = 0 holds by WRAP CANCELLATION, not by three legitimate splits -- "
                         "and a four-regime interval argument pins k = 0 on the OPEN arc without "
                         "needing the splits at all. FALSE at phi = pi (G15)."
                         if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
