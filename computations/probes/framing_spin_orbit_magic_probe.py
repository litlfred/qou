#!/usr/bin/env python3
"""Framing spin-orbit -> magic numbers: SHAPE derived, SCALE not. Partial result.

The framing route is the only path to {28, 50, 82, 126} not already excluded
(the scalar q-oscillator route is a proved scope-(b) exclusion: L^2(R^3) has no
C^2 factor, so no `s` operator exists in its algebra -- 2026-07-06 audit). This
probe tests it and reports one positive and one negative.

WHAT IS DERIVED, parameter-free
-------------------------------
`def:strand-twist-datum` warns that the per-strand label T(t) is a FREE integer
label, so any coupling built on it inherits that freedom. But the same block
records that the *ribbon* twist is NOT free: on the n-th Jones-Wenzl idempotent
it acts by the scalar (-1)^n A^{n(n+2)}, whose exponent n(n+2) is the Casimir.

Spin-orbit is itself a difference of Casimirs:

    l.s = (1/2)[ C(j) - C(l) - C(s) ],   C(x) = x(x+1)

so the ribbon-twist ratio between the two j = l +/- 1/2 channels is
q^{C(j+) - C(j-)}, and that exponent is EXACTLY 2l+1 for every l >= 1
(verified symbolically over Fractions below). 2l+1 is precisely the standard
spin-orbit l-dependence -- the growth with l that pulls the high-l intruder
down and opens the 28 / 50 / 82 gaps. Nothing was chosen to obtain it.

WHAT IS NOT DERIVED, and the number that says so
------------------------------------------------
The magic ladder depends on the spin-orbit STRENGTH C relative to the
oscillator spacing hw. Taking the twist to an energy gives C ~ ln(q0) = 0.10434.
That lands inside the window that reproduces the ladder -- and the window is
useless as evidence:

    >= 6 of 7 magic numbers reached for C in [0.060, 0.195]
    width 0.135, i.e. 46.7% of the scanned range 0.005..0.30

So ~half of all plausible couplings work. ln(q0) being among them constrains
almost nothing. This is the `S_leak` precedent in AGENTS.md ("the flip is
produced by ANY constant strictly between the two values; compute that window
and report its width before claiming the feature is evidence"), and the answer
here is that the window is wide.

Verdict: the SHAPE of the spin-orbit term is a genuine parameter-free
consequence of the ribbon twist; its SCALE is not predicted. Scope (a).

A NOTE ON THE CRITERION, so 6/7 is not misread as a framework failure
---------------------------------------------------------------------
Closures are read here as the 7 largest ENERGY GAPS, with false positives
counted. That is cruder than real shell-model practice and tops out at 6 hits
/ 1 false positive ANYWHERE in the (C, D) scan -- including at couplings the
literature reproduces all 7 with. The 6/7 is a limit of this criterion, not a
measured shortfall of the framework, and must not be quoted as one.

Counting hits WITHOUT counting false positives is what makes this test
worthless: every level scheme yields dozens of cumulative sums, so "does the
magic number appear among them" scores 7/7 for essentially any coupling. That
first version was written, run, and discarded -- it is the same
selection-blindness this session documented in three other places, where the
magic set enters as an input and is presented as an output.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path
from mpmath import mp

_ROOT = Path(__file__).resolve().parents[1]
for _p in (_ROOT, _ROOT / "substrate",
           _ROOT.parent / "tools" / "qou-substrate" / "python"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
from qou_substrate.witness import WitnessBuilder   # noqa: E402

mp.dps = 40
MAGIC = [2, 8, 20, 28, 50, 82, 126]
Q0 = mp.mpf("1.1099785827513808")
N_TOP_GAPS = 7


def casimir_difference_is_2l_plus_1(lmax=12):
    """Exact, over Fractions: C(l+1/2) - C(l-1/2) == 2l+1 for l >= 1."""
    bad = []
    for l in range(1, lmax + 1):
        jp = Fraction(2 * l + 1, 2)
        jm = Fraction(2 * l - 1, 2)
        if jp * (jp + 1) - jm * (jm + 1) != 2 * l + 1:
            bad.append(l)
    return bad


def _levels(C, D, Nmax=7):
    out = []
    for N in range(Nmax + 1):
        for l in range(N % 2, N + 1, 2):
            for tj2 in ([2 * l + 1] if l == 0 else [2 * l + 1, 2 * l - 1]):
                ls = mp.mpf(l) / 2 if tj2 == 2 * l + 1 else -mp.mpf(l + 1) / 2
                out.append((mp.mpf(N) + mp.mpf(3) / 2 + D * l * (l + 1) + C * ls,
                            tj2 + 1))
    out.sort(key=lambda r: r[0])
    return out


def gap_closures(C, D, k=N_TOP_GAPS, upto=140):
    lv = _levels(C, D)
    cum, rows = 0, []
    for i, (E, deg) in enumerate(lv):
        cum += deg
        if cum > upto:
            break
        rows.append((cum, lv[i + 1][0] - E if i + 1 < len(lv) else mp.mpf(0)))
    return sorted(c for c, _ in sorted(rows, key=lambda r: -r[1])[:k])


def hits_fps(C, D):
    got = set(gap_closures(C, D))
    return len(got & set(MAGIC)), len(got - set(MAGIC)), sorted(got)


def main() -> int:
    bad = casimir_difference_is_2l_plus_1()
    lnq = mp.log(Q0)

    # genericity: how much of the coupling range reproduces the ladder?
    scanned, good = 0, set()
    for Ci in range(1, 61):
        C = -mp.mpf(Ci) * 5 / 1000
        scanned += 1
        for Di in range(0, 7):
            if hits_fps(C, -mp.mpf(Di) / 100)[0] >= 6:
                good.add(float(-C))
                break
    frac = len(good) / scanned
    lo, hi = (min(good), max(good)) if good else (0.0, 0.0)

    best = max(((hits_fps(-mp.mpf(c) * 5 / 1000, -mp.mpf(d) / 100), c, d)
                for c in range(1, 61) for d in range(0, 7)),
               key=lambda t: (t[0][0], -t[0][1]))
    at_lnq = hits_fps(-lnq, -mp.mpf(2) / 100)

    print(f"Casimir difference == 2l+1 exactly, l=1..12 : {not bad}")
    print(f"ln(q0)                                     : {mp.nstr(lnq, 8)}")
    print(f">=6-hit window in C                        : [{lo:.3f}, {hi:.3f}]")
    print(f"  width / fraction of scanned range        : {hi-lo:.3f} / {frac:.1%}")
    print(f"  ln(q0) inside                            : {lo <= float(lnq) <= hi}")
    print(f"best anywhere in scan (hits, FP)           : {best[0][0]}, {best[0][1]}")
    print(f"at C = -ln q0, D = -0.02  (hits, FP)       : {at_lnq[0]}, {at_lnq[1]}")

    w = WitnessBuilder("framing-spin-orbit-magic", engine="mpmath")
    w.set_description(
        "Framing spin-orbit route to the magic numbers. DERIVED, parameter-free: "
        "the ribbon twist acts by q^Casimir and l.s is a difference of Casimirs, "
        "so the twist ratio between j = l +/- 1/2 carries the exponent 2l+1 "
        "exactly -- the standard spin-orbit l-dependence, nothing chosen. NOT "
        "derived: the strength. ln(q0)=0.10434 lands inside the window that "
        "reproduces the ladder, but that window spans 46.7% of the scanned "
        "coupling range, so membership constrains almost nothing. Shape yes, "
        "scale no. Scope (a)."
    )
    w.add_parameter("n_top_gaps", N_TOP_GAPS)
    w.add_parameter("q0", mp.nstr(Q0, 20))
    w.add_data("casimir_diff_equals_2l_plus_1", not bad)
    w.add_data("casimir_counterexamples", bad)
    w.add_data("ln_q0", mp.nstr(lnq, 20))
    w.add_data("window_lo", f"{lo:.6f}")
    w.add_data("window_hi", f"{hi:.6f}")
    w.add_data("window_fraction_of_scanned_range", f"{frac:.6f}")
    w.add_data("ln_q0_inside_window", bool(lo <= float(lnq) <= hi))
    w.add_data("best_hits_anywhere", best[0][0])
    w.add_data("best_false_positives", best[0][1])
    w.add_data("hits_at_ln_q0", at_lnq[0])
    w.add_data("false_positives_at_ln_q0", at_lnq[1])
    w.add_data("closures_at_ln_q0", at_lnq[2])
    w.add_assertion("casimir_difference_is_exactly_2l_plus_1",
                    len(bad), 0, tolerance=0,
                    source="symbolic over Fractions, l = 1..12")
    w.add_assertion("scale_is_NOT_predicted_window_is_wide",
                    1 if frac > mp.mpf("0.25") else 0, 1, tolerance=0,
                    source=f"{frac:.1%} of the scanned coupling range works")
    w.add_caveat(
        "Closures are the 7 largest energy gaps with false positives counted. "
        "That criterion tops out at 6 hits / 1 FP anywhere in the scan, "
        "including at couplings the literature reproduces all 7 with, so the "
        "6/7 is a limit of the criterion and NOT a measured shortfall of the "
        "framework. Do not quote it as one."
    )
    w.add_caveat(
        "Scope (a): a negative about the SCALE only. The 2l+1 shape result is "
        "positive and unaffected; it says the ribbon twist supplies the right "
        "l-dependence without a parameter."
    )
    w.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
