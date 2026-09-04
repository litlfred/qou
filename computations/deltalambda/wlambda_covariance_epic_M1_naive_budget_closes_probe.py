#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): DOES THE NAIVE PER-INGREDIENT BUDGET CLOSE? Turn "the cancellations eat most of
the headroom" from a qualitative worry into a number that either fits under C <= 2.6681 or does not.

WHY THIS, NOW. PR #6528 measured two cancellations in the margin -- between the legs (ratio
0.2238..1.0 over n >= 16) and inside L_sig between V_D and V_A (0.108..0.226) -- and concluded that a
budget bounding rho_P, V_D and V_A separately and adding via the triangle inequality "can overshoot by
roughly an order of magnitude, which against the 46x total headroom is most of the available room."

That sentence multiplied two worst cases and left the reader to guess whether the budget closes. It
is the wrong shape of statement for a decision: the next attempt has to know whether it may build the
EASY proof (bound the three ingredients independently) or must build the HARD one (an argument that
keeps the cancellations intact). This probe measures that directly.

WHAT IS COMPUTED, exactly (Fraction covariances over all partitions of n; mpmath only for square
roots and display).

  TRUE deviation      : |m(n) - m_inf|,          m = rho_P - sqrt(V_D/V_A)
  NAIVE bound         : |L_rho(n)| + (sig_inf/2) * (|delta_D(n)| + |delta_A(n)|)

with delta_X = (V_X/n^2 - v_X)/v_X the relative deviation of each variance, and the sig_inf/2 the
conversion PR #6528 established (a relative delta on V_X moves sqrt(V_D/V_A) by sig_inf*delta/2, hence
moves the margin by that much). The naive bound is exactly what a proof gets if it produces one
constant per ingredient and adds them.

  LOSS(n)  =  NAIVE(n) / TRUE(n)                      -- the triangle inequality's own cost
  C_true   =  max_n TRUE(n) * sqrt(n)                 -- the empirical envelope (0.0580 on record)
  C_naive  =  max_n NAIVE(n) * sqrt(n)                -- what a per-ingredient proof would report
  verdict  :  is C_naive <= m_inf * sqrt(79) = 2.6681 ?

WHAT THIS DOES AND DOES NOT SETTLE.

  * It settles the TRIANGLE INEQUALITY's cost, exactly, at every n in the window. That cost is
    independent of how a rigorous argument is built -- any proof that reports three constants and
    adds them pays it.
  * It does NOT settle whether a rigorous proof closes. A rigorous per-ingredient constant is
    LARGER than the empirical one measured here (an empirical sup over a finite window is a lower
    bound on what a proof must state). So C_naive here is a FLOOR on what the easy route reports:
    if the floor already exceeds 2.6681 the easy route is dead, and if it does not, the easy route
    is merely not-yet-excluded.
  * WINDOW CAVEAT. The exact table reaches n = 40, while the constant is only required to control
    n >= 79 (n <= 78 is covered by exhaustive verification). The sqrt(n)-scaled envelopes DECREASE
    over the window (the margin's own falls 0.1999 -> 0.0505, PR #6500), so a sup taken over
    [16, 40] OVER-estimates the sup over n >= 79 -- conservative in the safe direction, but an
    extrapolation and labelled as one. LOSS(n) itself is pointwise-exact and needs no extrapolation.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import importlib.util
import pathlib
import mpmath as mp

mp.mp.dps = 30

M_INF = mp.mpf('0.300186614161')            # merged #5901 IO leading (CS) margin
SIG_RATIO_INF = mp.mpf('0.679609581496')    # merged #5901 sigma_D/sigma_A limit
C_TARGET = M_INF * mp.sqrt(79)              # margin-level requirement (PR #5929 n^-1/2 shape)
V_A_INF = 8 / (9 * mp.pi ** 2)              # de-poissonized V_A/n^2 limit, PR #5969
V_D_INF = SIG_RATIO_INF ** 2 * V_A_INF      # forced by sig_ratio_inf = sqrt(v_D/v_A)


def _load_legs():
    """Import legs() from the leg-decomposition probe by explicit file path.

    By path, not by bare name: a sibling in a cluster subdir resolves only when the parent is already
    on sys.path (the _path_bridge bootstrap trap), and this probe must run with PYTHONPATH unset.
    """
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_margin_leg_decomposition.py"
    spec = importlib.util.spec_from_file_location("_m1_legs", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    legmod = _load_legs()
    stats = legmod._load_partitions_and_stats()
    nmax = 40
    half = SIG_RATIO_INF / 2

    print(f"# does the naive per-ingredient budget close? dps={mp.mp.dps}; NO float64")
    print(f"# C_target = m_inf*sqrt(79) = {mp.nstr(C_TARGET,6)}   (PR #5929 n^-1/2 shape)")
    print(f"# conversion per variance leg: sig_inf/2 = {mp.nstr(half,6)}")
    print(f"# v_A = 8/(9 pi^2) = {mp.nstr(V_A_INF,9)}   v_D = sig_inf^2 v_A = {mp.nstr(V_D_INF,9)}")
    print("#")
    print(f"#   {'n':>3} {'TRUE':>12} {'|L_rho|':>12} {'|dD|':>12} {'|dA|':>12} "
          f"{'NAIVE':>12} {'LOSS':>8}")

    rows = []
    for n in range(4, nmax + 1):
        got = legmod.legs(stats, n)
        if got is None:
            continue
        lr, ls, m, vAn, vDn = got
        true = abs(m - M_INF)
        dA = (vAn - V_A_INF) / V_A_INF
        dD = (vDn - V_D_INF) / V_D_INF
        naive = abs(lr) + half * (abs(dD) + abs(dA))
        loss = naive / true if true != 0 else mp.mpf('inf')
        rows.append((n, true, naive, loss, abs(lr), abs(dD), abs(dA)))
        if n <= 10 or n % 4 == 0:
            print(f"#   {n:>3} {mp.nstr(true,5):>12} {mp.nstr(abs(lr),5):>12} "
                  f"{mp.nstr(abs(dD),5):>12} {mp.nstr(abs(dA),5):>12} "
                  f"{mp.nstr(naive,5):>12} {mp.nstr(loss,4):>8}")
    print("#")

    tail = [r for r in rows if r[0] >= 16]
    lmin = min(r[3] for r in tail)
    lmax = max(r[3] for r in tail)
    n_at_max = [r[0] for r in tail if r[3] == lmax][0]
    print("# LOSS = NAIVE/TRUE, the triangle inequality's own cost. Pointwise-exact, no extrapolation.")
    print(f"#   over n >= 16: min {mp.nstr(lmin,4)}, max {mp.nstr(lmax,4)} (at n = {n_at_max})")
    print("#")

    c_true = max(r[1] * mp.sqrt(r[0]) for r in tail)
    c_naive = max(r[2] * mp.sqrt(r[0]) for r in tail)
    n_true = [r[0] for r in tail if r[1] * mp.sqrt(r[0]) == c_true][0]
    n_naive = [r[0] for r in tail if r[2] * mp.sqrt(r[0]) == c_naive][0]
    print("# ENVELOPES at the proved n^-1/2 rate, sup over the window n in [16, 40]:")
    print(f"#   C_true  = max TRUE  * sqrt(n) = {mp.nstr(c_true,6)}  (at n = {n_true})")
    print(f"#   C_naive = max NAIVE * sqrt(n) = {mp.nstr(c_naive,6)}  (at n = {n_naive})")
    print(f"#   ratio C_naive / C_true        = {mp.nstr(c_naive/c_true,5)}")
    print("#")
    print(f"#   headroom, true envelope       = C_target / C_true  = {mp.nstr(C_TARGET/c_true,5)}x")
    print(f"#   headroom, naive budget        = C_target / C_naive = {mp.nstr(C_TARGET/c_naive,5)}x")
    print("#")

    closes = c_naive <= C_TARGET
    print("# VERDICT on the EASY route (bound the three ingredients separately, add):")
    if closes:
        print(f"#   C_naive = {mp.nstr(c_naive,5)} <= {mp.nstr(C_TARGET,5)} -- the triangle inequality")
        print(f"#   alone does NOT kill the easy route; it leaves {mp.nstr(C_TARGET/c_naive,4)}x for the")
        print("#   gap between an EMPIRICAL per-ingredient sup and a RIGOROUS one. The easy route is")
        print("#   not excluded, and the burden moves to how lossy the rigorous constants are.")
    else:
        print(f"#   C_naive = {mp.nstr(c_naive,5)} > {mp.nstr(C_TARGET,5)} -- the easy route is DEAD on")
        print("#   the triangle inequality alone, before any rigorous-vs-empirical looseness. Any")
        print("#   proof must preserve the cancellations.")
    print("#")
    print("# WHAT THIS IS NOT. C_naive is a FLOOR on what a per-ingredient proof reports: it is built")
    print("#   from EMPIRICAL sups over a finite window, and a rigorous constant is necessarily larger")
    print("#   (it must hold for all n, not just the ones tabulated). So 'closes' above means NOT-YET-")
    print("#   EXCLUDED, never proved; 'dead' would be a genuine exclusion, since a floor exceeding the")
    print("#   target excludes everything above it.")
    print("#   WINDOW: the exact table reaches n=40 and the constant is required only for n >= 79. The")
    print("#   sqrt(n)-scaled envelopes DECREASE across the window, so these sups over-estimate the")
    print("#   sup over n >= 79 -- safe direction, but an extrapolation.")
    verdict = "NOT-YET-EXCLUDED" if closes else "DEAD on the triangle inequality alone"
    print(f"RESULT: triangle-inequality LOSS over n>=16 is {mp.nstr(lmin,4)}..{mp.nstr(lmax,4)}x; "
          f"C_naive = {mp.nstr(c_naive,5)} vs C_target = {mp.nstr(C_TARGET,5)} => the easy "
          f"per-ingredient route is {verdict} (C_naive is a FLOOR built from empirical sups over "
          f"n<=40, not a rigorous constant). qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
