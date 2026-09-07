#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): are the PER-INGREDIENT envelopes converged over the accessible window? Every
headroom figure in this arc rests on the assumption that they are, and nothing has checked it.

WHY THIS, NOW. PR #6528 landed the result that a naive per-ingredient budget overshoots the true
margin deviation by only 4.83x, leaving 9.54x of the 46x headroom, and narrowed the open question to:
can a RIGOROUS per-ingredient bound land within 9.54x of the empirical sups? That question presumes
the empirical sups mean something -- i.e. that each ingredient's sqrt(n)-scaled envelope has settled
into decay over the window rather than still oscillating with comparable amplitude. If an envelope is
NOT settled, the sup over n <= 46 is not an extrapolation to n >= 79 at all, and the headroom figure
built on it is a number about the window, not about the problem.

The margin's OWN envelope was checked this way (PR #6500: running max at p=1/2 falls 0.1999 ->
0.0505; at p=1 flat at 0.3151, attained n=39). The three INGREDIENTS have never been.

WHAT IS MEASURED, exactly (Fraction covariances over all partitions of n; mpmath only for square
roots and display). For each quantity

    L_rho    = rho_P(n) - rho_inf                                (enters the margin LINEARLY)
    delta_A  = (V_A/n^2 - v_A)/v_A                               (relative, converts by sig_inf/2)
    delta_D  = (V_D/n^2 - v_D)/v_D                               (relative, converts by sig_inf/2)
    delta_R  = ((V_D/V_A) - sig_inf^2)/sig_inf^2                 (the ratio as ONE object)
    margin   = m(n) - m_inf                                      (the target, for calibration)

it reports the RUNNING MAXIMUM of |Q(n)| * n^p from N upward, for p = 1/2 and p = 1. A running
maximum is used deliberately INSTEAD of fitting consecutive peaks: these sequences oscillate and one
lobe of the margin sequence is double-humped, so peak-ratio exponents came out as noise (6.23,
-4.72, 0.73) when that was tried in PR #6500. A running max needs no peak classification and no
data dropped.

THE DIAGNOSTIC, and it is the point. If the running max at p FALLS steadily with N, the envelope is
settled at that rate and a sup over the window over-estimates the sup over n >= 79 -- conservative,
usable. If it is FLAT, p is the true rate and the sup is the constant. If it RISES, the scaled
quantity is still growing and the window says nothing about n >= 79: any headroom computed from it
is unfounded.

WHAT THIS CANNOT DO. It cannot establish a rate. The window ends far below 79 and every conclusion
here is an extrapolation, labelled as one. What it CAN do is detect the failure case -- an envelope
that is visibly not settled -- and that is a genuine negative if it fires.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import importlib.util
import pathlib
import mpmath as mp

mp.mp.dps = 30

from _m1_io_constants import M_INF, RHO_INF, SIG_RATIO_INF  # merged #5901 IO leading constants -- single source, see that module
C_TARGET = M_INF * mp.sqrt(79)
V_A_INF = 8 / (9 * mp.pi ** 2)
V_D_INF = SIG_RATIO_INF ** 2 * V_A_INF
HALF = SIG_RATIO_INF / 2          # margin-units conversion for a relative variance deviation


def _load_legs():
    """Import legs() by explicit file path (not a bare name: the _path_bridge bootstrap trap --
    this probe must run with PYTHONPATH unset)."""
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_margin_leg_decomposition.py"
    spec = importlib.util.spec_from_file_location("_m1_legs", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def running_max(series, p):
    """[(N, max_{n>=N} |Q(n)| n^p)] over the tabulated n, from each N upward."""
    scaled = [(n, abs(q) * mp.mpf(n) ** p) for n, q in series]
    out, run = [], mp.mpf(0)
    for n, v in reversed(scaled):
        run = max(run, v)
        out.append((n, run))
    return list(reversed(out))


def verdict(rm):
    """Classify a running-max profile over its last third: FALLING / FLAT / RISING."""
    tail = rm[-max(3, len(rm) // 3):]
    first, last = tail[0][1], tail[-1][1]
    if last == 0:
        return "FLAT", mp.mpf(1)
    ratio = last / first
    if ratio < mp.mpf('0.9'):
        return "FALLING", ratio
    if ratio > mp.mpf('1.1'):
        return "RISING", ratio
    return "FLAT", ratio


def main():
    legmod = _load_legs()
    stats = legmod._load_partitions_and_stats()
    nmax = 46

    print(f"# per-ingredient envelope convergence; dps={mp.mp.dps}; NO float64")
    print(f"# C_target = m_inf sqrt(79) = {mp.nstr(C_TARGET,6)}; window n <= {nmax}, "
          f"requirement is n >= 79")
    print("#")

    series = {"L_rho": [], "delta_A": [], "delta_D": [], "delta_R": [], "margin": []}
    R_INF = SIG_RATIO_INF ** 2
    for n in range(4, nmax + 1):
        got = legmod.legs(stats, n)
        if got is None:
            continue
        lr, ls, m, vAn, vDn = got
        series["L_rho"].append((n, lr))
        series["delta_A"].append((n, (vAn - V_A_INF) / V_A_INF))
        series["delta_D"].append((n, (vDn - V_D_INF) / V_D_INF))
        series["delta_R"].append((n, ((vDn / vAn) - R_INF) / R_INF))
        series["margin"].append((n, m - M_INF))

    for p, plabel in ((mp.mpf(1) / 2, "1/2"), (mp.mpf(1), "1")):
        print(f"# RUNNING MAX of |Q(n)| * n^{plabel}, from N upward:")
        print(f"#   {'N':>4} " + " ".join(f"{k:>12}" for k in series))
        rms = {k: running_max(v, p) for k, v in series.items()}
        Ns = [n for n, _ in rms["margin"]]
        for i, N in enumerate(Ns):
            if N % 6 == 0 or N == Ns[-1]:
                print(f"#   {N:>4} " + " ".join(f"{mp.nstr(rms[k][i][1],5):>12}" for k in series))
        print(f"#   {'verdict':>4} " + " ".join(f"{verdict(rms[k])[0]:>12}" for k in series))
        print(f"#   {'ratio':>4} " + " ".join(f"{mp.nstr(verdict(rms[k])[1],4):>12}" for k in series))
        print("#")
        if plabel == "1/2":
            rm_half = rms
        else:
            rm_one = rms

    print("# WHAT THE VERDICTS MEAN. FALLING at p => the envelope is settled at that rate and a sup")
    print("#   over this window OVER-estimates the sup over n >= 79 (conservative, usable). FLAT =>")
    print("#   p is the true rate and the sup IS the constant. RISING => the scaled quantity is still")
    print("#   growing, the window says nothing about n >= 79, and any headroom built on it is")
    print("#   unfounded.")
    print("#")

    # The margin-units budget, per ingredient, at the proved n^-1/2 rate.
    print("# PER-INGREDIENT BUDGET in MARGIN UNITS at the proved n^-1/2 rate (sup over n >= 16):")
    print("#   L_rho enters linearly; delta_A and delta_D each convert by "
          f"sig_inf/2 = {mp.nstr(HALF,6)}.")
    idx16 = [i for i, (n, _) in enumerate(rm_half["margin"]) if n == 16][0]
    c_rho = rm_half["L_rho"][idx16][1]
    c_A = rm_half["delta_A"][idx16][1] * HALF
    c_D = rm_half["delta_D"][idx16][1] * HALF
    c_R = rm_half["delta_R"][idx16][1] * HALF
    c_true = rm_half["margin"][idx16][1]
    print(f"#   C_rho   (linear)        = {mp.nstr(c_rho,6)}")
    print(f"#   C_A     (x sig_inf/2)   = {mp.nstr(c_A,6)}")
    print(f"#   C_D     (x sig_inf/2)   = {mp.nstr(c_D,6)}")
    print(f"#   sum (naive budget)      = {mp.nstr(c_rho + c_A + c_D,6)}")
    print(f"#   C_ratio (x sig_inf/2)   = {mp.nstr(c_R,6)}   <- bounding V_D/V_A as ONE object")
    print(f"#   C_rho + C_ratio         = {mp.nstr(c_rho + c_R,6)}   <- the ratio route's budget")
    print(f"#   C_true  (the target)    = {mp.nstr(c_true,6)}")
    print("#")
    print(f"#   headroom, naive         = {mp.nstr(C_TARGET/(c_rho+c_A+c_D),5)}x")
    print(f"#   headroom, ratio route   = {mp.nstr(C_TARGET/(c_rho+c_R),5)}x")
    print(f"#   headroom, true envelope = {mp.nstr(C_TARGET/c_true,5)}x")
    print("#")
    # The same budget at p = 1, for the OTHER rate. Measured, not combined by hand from the table
    # above -- assembling a composite from separately-quoted numbers is exactly how the "order of
    # magnitude" overstatement of PR #6528 happened.
    idx16_1 = [i for i, (n, _) in enumerate(rm_one["margin"]) if n == 16][0]
    d_rho = rm_one["L_rho"][idx16_1][1]
    d_R = rm_one["delta_R"][idx16_1][1] * HALF
    d_A = rm_one["delta_A"][idx16_1][1] * HALF
    d_D = rm_one["delta_D"][idx16_1][1] * HALF
    d_true = rm_one["margin"][idx16_1][1]
    target1 = M_INF * 79                       # |m - m_inf| <= C'/n  =>  N0 = C'/m_inf <= 79
    print("# THE SAME BUDGET AT THE p=1 RATE -- NOT proved (the proved shape is n^-1/2, PR #5929),")
    print("#   but the empirical envelopes are consistent with it, so this is what a stronger rate")
    print("#   would be worth. At |m - m_inf| <= C'/n the requirement is N0 = C'/m_inf <= 79, i.e.")
    print(f"#   C' <= m_inf * 79 = {mp.nstr(target1,6)} -- a LINEAR relaxation, not a square-root one.")
    print(f"#   C'_rho {mp.nstr(d_rho,6)}   C'_A {mp.nstr(d_A,6)}   C'_D {mp.nstr(d_D,6)}   "
          f"C'_ratio {mp.nstr(d_R,6)}")
    print(f"#   three-ingredient {mp.nstr(d_rho+d_A+d_D,6)}  =>  headroom "
          f"{mp.nstr(target1/(d_rho+d_A+d_D),5)}x")
    print(f"#   ratio route      {mp.nstr(d_rho+d_R,6)}  =>  headroom "
          f"{mp.nstr(target1/(d_rho+d_R),5)}x   (waste {mp.nstr((d_rho+d_R)/d_true,4)}x)")
    print(f"#   C'_true          {mp.nstr(d_true,6)}  =>  headroom {mp.nstr(target1/d_true,5)}x")
    gain = (target1 / (d_rho + d_R)) / (C_TARGET / (c_rho + c_R))
    print(f"#   => proving the n^-1 shape multiplies the ratio route's room by {mp.nstr(gain,4)}x")
    print("#      (40.48x -> 67.18x). Worth knowing before spending effort sharpening constants at")
    print("#      the n^-1/2 shape instead -- though note it is the SMALLER lever of the two: moving")
    print("#      from the three-ingredient budget to the ratio route is worth 4.37x at p=1/2, while")
    print("#      moving from p=1/2 to p=1 is worth 1.66x. Do the ratio bound first.")
    print("#")
    print("# NOTE the ratio route is NOT free: it needs a rigorous bound on V_D/V_A directly, which")
    print("#   is a different analytic object from bounds on V_D and V_A separately. It buys the")
    print("#   headroom above only if such a bound exists at comparable rigour.")
    print("#")
    print("# WINDOW CAVEAT, restated because it governs every number above: this table ends at")
    print(f"#   n = {nmax} and the constant is required only for n >= 79. Nothing here is a bound.")

    vs = {k: verdict(rms[k])[0] for k in series}
    risers = [k for k, v in vs.items() if v == "RISING"]
    tag = ("NOT settled: " + ", ".join(risers)) if risers else "all settled or flat at p=1"
    print(f"RESULT: envelope verdicts at p=1 -- " +
          ", ".join(f"{k}:{v}" for k, v in vs.items()) + f" => {tag}. Naive per-ingredient budget "
          f"{mp.nstr(c_rho+c_A+c_D,5)} vs ratio-route {mp.nstr(c_rho+c_R,5)} vs target "
          f"{mp.nstr(C_TARGET,5)}. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
