#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): the (CS) MARGIN's own envelope exponent -- correcting a claim of mine, and
measuring the headroom the crude-bound route actually has.

WHAT THIS CORRECTS. PR #6469 (merged) reported, and five other sites repeat:

    "at the theta^{-1} rate, m(n) >= m_inf - C/n > 0 needs N0 = ceil(C/m_inf) <= 78,
     i.e. C <= 23.4 -- far weaker than the C <= 2.65 a conservative n^{-1/2} reading demands."

That is WRONG, and in a way worth stating precisely because the arithmetic in it is fine:

  1. WRONG OBJECT. The theta^{-1} rate was measured on d(theta) = V_A(theta)/theta^2 - 8/pi^2, the
     remainder of the POISSONIZED Sum|c| variance. The margin is
     m(n) = rho_P(n) - sigma_D(n)/sigma_A(n) -- a RATIO OF SQUARE ROOTS of two variances plus a
     correlation. A rate on one variance's remainder is not a rate on the margin, and nobody has
     propagated the one into the other (the ratio, the square root and de-poissonization each
     contribute).
  2. MISLABELLED THE PROVED BOUND. What is actually proved (PR #5929) is |m(n) - m_inf| <=
     C n^{-1/2}, whence N0 = (C/m_inf)^2 -- SQUARED -- and the requirement is C <= m_inf*sqrt(79)
     = 2.6681. My sentence called 2.65 "a conservative reading"; it is THE requirement matching
     the bound in hand. The n^{-1} form was an assumption presented as a premise.

WHAT IS MEASURED HERE (exact Fraction covariances; mpmath only for sqrt/display; NO float64).
m(n) oscillates about m_inf with decreasing amplitude (established in
_finite_n_cs_margin.py), so the meaningful object is the ENVELOPE, not a pointwise ratio. The
envelope is probed by the RUNNING MAXIMUM of |m - m_inf| * n^p over [N, 46], which requires no peak
classification (see the note below on why peak-ratio fitting fails here):

  - the running max of |m - m_inf| * sqrt(n) over [N, 46] FALLS by ~3.4x (0.1999 -> 0.0580). A
    running max that falls means the exponent is too small: the margin decays strictly FASTER than
    n^{-1/2}, so the proved shape is not tight.
  - the running max of |m - m_inf| * n is FLAT from N=6 (0.31512, attained at n=39), i.e.
    consistent with n^{-1}.

The running maximum is used rather than a peak-ratio fit BY NECESSITY, not preference: the sign runs
are n=4..6 (-), 7..12 (+), 13..15 (-), 16..46 (+), so one local maximum (n=14) is a narrow sub-lobe
~7x below the outer envelope and the final run is double-humped (21 and 38). Fitting consecutive
peaks returns 6.2, -4.7, 0.73 -- and hand-dropping the sub-lobe to rescue that would be choosing the
data to fit.

So the n^{-1} rate I assumed is EMPIRICALLY SUPPORTED for the margin -- it is simply not proved, and
the defect was reporting the closure arithmetic as though it were. Note also what the data does NOT
establish: over n <= 46 it excludes n^{-1/2} decisively but does not cleanly separate n^{-1} from a
slightly slower power (|dev|*n drifts up ~18% across the outer peaks). An empirical envelope is not a
rigorous C; that distinction is the whole content of this gap.

WHAT THIS DOES TO THE ROUTE -- it strengthens it. Under the PROVED n^{-1/2} shape the requirement is
C <= 2.6681 while the empirical envelope over n >= 13 is C_emp = 0.0580: a headroom factor of ~46.
A rigorous constant landing within 46x of the truth closes M_1>0 for all n. That -- not the
retracted "C <= 23.4" -- is the real statement that a CRUDE bound suffices.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import importlib.util
import pathlib
import mpmath as mp

mp.mp.dps = 30
M_INF = mp.mpf('0.300186614161')          # merged #5901 IO leading (CS) margin
C_TARGET = M_INF * mp.sqrt(79)            # requirement under the PROVED n^{-1/2} shape


def _load_margin():
    """Import margin() from the C-landscape probe by explicit path.

    Deliberately NOT a bare-name import: a sibling module in a cluster subdir resolves only when
    the parent is already on sys.path, which is exactly the _path_bridge bootstrap trap. Loading by
    file path makes this probe runnable with PYTHONPATH unset.
    """
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_constant_C_landscape.py"
    spec = importlib.util.spec_from_file_location("_m1_c_landscape", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.margin


def lobe_peaks(dev):
    """Indices of local maxima of |m - m_inf| -- the envelope's lobe tops.

    dev is a list of (n, deviation). A peak is a point whose |deviation| is >= both neighbours;
    endpoints are excluded so a still-rising tail is never mistaken for a lobe top.
    """
    out = []
    for i in range(1, len(dev) - 1):
        a, b, c = abs(dev[i - 1][1]), abs(dev[i][1]), abs(dev[i + 1][1])
        if b >= a and b >= c:
            out.append(dev[i])
    return out


def main():
    nmax = 46
    margin = _load_margin()
    print(f"# (CS)-margin envelope exponent; m_inf={mp.nstr(M_INF,9)}; dps={mp.mp.dps}; NO float64")
    dev = []
    for n in range(4, nmax + 1):
        mn = margin(n)
        if mn is None:
            continue
        dev.append((n, mn - M_INF))

    peaks = lobe_peaks(dev)
    print("# LOCAL MAXIMA of |m(n) - m_inf|, for orientation only -- see the methodological note.")
    print(f"#   {'n':>4} {'|m-m_inf|':>13} {'x sqrt(n)':>12} {'x n':>12}")
    for n, d in peaks:
        a = abs(d)
        print(f"#   {n:>4} {mp.nstr(a,6):>13} {mp.nstr(a*mp.sqrt(n),6):>12} {mp.nstr(a*n,6):>12}")
    print("#")
    print("# METHODOLOGICAL NOTE -- why the exponent is NOT fitted from these peaks. The sign runs of")
    print("#   m - m_inf are n=4..6 (-), 7..12 (+), 13..15 (-), 16..46 (+), so the n=14 entry is the")
    print("#   top of a NARROW negative excursion whose amplitude is ~7x below the outer envelope,")
    print("#   and the last positive run is DOUBLE-HUMPED (peaks at 21 and 38). Peak-ratio fitting")
    print("#   therefore returns nonsense here (consecutive-peak exponents 6.2, -4.7, 0.73), and")
    print("#   hand-dropping the n=14 sub-lobe to rescue it would be choosing the data to fit. The")
    print("#   running maximum below needs no peak classification and is used instead.")
    print("#")
    print("# WHICH SHAPE? Running max of |m - m_inf| * n^p over the measured window [N, 46].")
    print("#   A DECREASING column means p is too small (the true decay is faster); a FLAT column")
    print("#   means p is consistent with the data.")
    print(f"#   {'from N':>7} {'max |dev|*sqrt(n)':>19} {'max |dev|*n':>14}")
    for N in (4, 6, 8, 10, 13, 20, 30):
        w = [(n, abs(d)) for n, d in dev if n >= N]
        if not w:
            continue
        h = max(a * mp.sqrt(n) for n, a in w)
        o = max(a * n for n, a in w)
        print(f"#   {N:>7} {mp.nstr(h,6):>19} {mp.nstr(o,6):>14}")
    print("#   => the p=1/2 column FALLS by a factor ~3.4 (0.1999 -> 0.0580): the proved n^{-1/2}")
    print("#      shape is NOT TIGHT, the margin decays strictly faster. The p=1 column is FLAT from")
    print("#      N=6 on (0.31512, attained at n=39), i.e. consistent with n^{-1}.")
    print("#   HONEST LIMIT OF THIS EVIDENCE: over n <= 46 the data decisively EXCLUDES n^{-1/2} but")
    print("#      does NOT cleanly separate n^{-1} from a slightly slower power -- |dev|*n still")
    print("#      drifts up ~18% across the outer peaks (0.261 at n=9, 0.264 at 21, 0.309 at 38),")
    print("#      and the p=1 column is flat only because its sup is attained at an interior n=39")
    print("#      inside every window. So: EMPIRICAL SUPPORT for n^{-1}, not a measurement of it,")
    print("#      and in no case a proof -- what is proved (PR #5929) is |m - m_inf| <= C n^{-1/2}.")
    print("#")

    # Headroom under the PROVED shape -- the statement that actually matters for the route.
    tail = [abs(d) * mp.sqrt(n) for n, d in dev if n >= 13]
    c_emp = max(tail)
    print("# HEADROOM UNDER THE PROVED n^{-1/2} SHAPE (this is the real 'a crude bound suffices'):")
    print(f"#   requirement           C <= m_inf*sqrt(79) = {mp.nstr(C_TARGET,6)}")
    print(f"#   empirical envelope    C_emp(n>=13)        = {mp.nstr(c_emp,6)}")
    print(f"#   headroom factor       C_target / C_emp    = {mp.nstr(C_TARGET/c_emp,5)}x")
    print(f"#   implied N0 at C_emp   (C_emp/m_inf)^2     = {mp.nstr((c_emp/M_INF)**2,4)}  (<< 79)")
    print("#   => a rigorous constant within ~46x of the truth closes M_1>0 for all n, under the")
    print("#      shape that is ALREADY PROVED. No improvement to n^{-1} is needed for closure.")
    print("#")
    print("# RETRACTED: 'at the theta^{-1} rate ... C <= 23.4 -- far weaker than the C <= 2.65 a")
    print("#   conservative n^{-1/2} reading demands' (PR #6469 and 5 further sites). The theta^{-1}")
    print("#   rate is V_A's, not the margin's; and 2.65 is the REQUIREMENT under the proved bound,")
    print("#   not a conservative reading of it.")
    print(f"RESULT: margin envelope decays faster than n^-1/2 (~n^-1 empirically, NOT proved); under "
          f"the proved n^-1/2 shape the headroom is {mp.nstr(C_TARGET/c_emp,4)}x. 'C <= 23.4' RETRACTED. "
          f"qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
