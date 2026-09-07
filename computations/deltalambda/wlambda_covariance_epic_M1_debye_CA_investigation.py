#!/usr/bin/env python3
"""M_1>0 investigation: pin the TRUE asymptotic constants of the descent-DPP (CS) ingredients at
large theta (exact Bessel sums, no partitions), to decide whether a rigorous Olver/Debye C_A can
land under the target C <= 2.668 (=> N0 <= 79) -- i.e. whether M_1>0 closes outright.

Gap qou-k5r5, epic qou-x631. The rigorous bound |m(n)-m_inf| <= C n^{-1/2} closes M_1>0 for all n
if C <= m_inf*sqrt(79) = 2.668 (finite part n<=78 certified).

  *** UNITS CLARIFICATION (added 2026-09-03, PR #6528). The first paragraph above reads "whether a
  *** rigorous Olver/Debye C_A can land under the target C <= 2.668". C_A and C ARE DIFFERENT
  *** OBJECTS and must not be compared directly: C_A bounds the V_A remainder,
  *** |V_A/theta^2 - v_A| <= C_A theta^{-1/2}, while C bounds the MARGIN. The conversion is
  ***     C_margin,A = (sig_ratio_inf / (2 v_A)) * C_A = 0.41922 * C_A,
  *** so the V_A leg alone may spend C_A <= 2.6681/0.41922 = 6.3645, NOT C_A <= 2.668 -- the naive
  *** reading is 2.385x too strict. Against the C_A^emp = 0.00775 measured below that is ~821x of
  *** headroom on this leg (modulo de-poissonization, which nobody has pinned).
  *** THIS IS A PHRASING DEFECT ONLY: the VERDICT below is unit-correct, comparing the true MARGIN
  *** constant (~0.087) against 2.668, and no number in this probe is derived from the conflation.
  *** Two sibling sites made the same comparison and DID derive numbers from it; those are corrected
  *** in PRs #6500 and #6528. See wlambda_covariance_epic_M1_CA_to_margin_conversion.py. PR #5934 measured the FIXED-n margin
constant ~0.087 to n=44 (partition-limited). This probe pushes the POISSONIZED linear ingredients to
theta up to a few thousand (kernel is O(M^2), M~2 sqrt(theta)) and measures:

  - v_A = lim V_A/theta^2  (Richardson), and C_A^emp = sup |V_A/theta^2 - v_A|*sqrt(theta)
    -- the TRUE asymptotic constant the rigorous Olver/Debye bound must dominate;
  - the de-poissonized rho_P(theta) -> rho_inf and its deviation constant/exponent;
  - v_A's convergence exponent (kink => theta^{-1/2} expected as the worst case).

Reads off whether the true constants are small (so a rigorous C, typically a small multiple of the
true asymptotic coefficient for sharp Olver bounds, plausibly clears 2.668) or already large.
mpmath 40 dps; NO float64. scope-(a); no fit (limits Richardson-extrapolated, constants MEASURED,
exponents DERIVED). Gap qou-k5r5 OPEN -- this is an investigation, not a rigorous C.
"""
from __future__ import annotations
import sys
import mpmath as mp

mp.mp.dps = 40
from _m1_io_constants import RHO_INF  # merged #5901 IO leading constants -- single source, see that module


def bessel_table(theta, M):
    arg = 2 * mp.sqrt(theta)
    J = {0: mp.besselj(0, arg)}
    for x in range(1, M + 2):
        J[x] = mp.besselj(x, arg)
        J[-x] = (-1) ** x * J[x]
    return J


def _anti_abs(k):
    return mp.mpf(k * (k + 1)) / 2 if k >= 0 else -mp.mpf(k * (k + 1)) / 2


def _anti_sq(k):
    return mp.mpf(k * (k + 1) * (2 * k + 1)) / 6


def ingredients(theta, M):
    """Poissonized descent-DPP VA=Var(Sum|c|), VW=Var(Sum c^2), P=Cov, VN=Var(n), CAN, CWN
    via the projection formula (1/2) Sum_{x!=y}(g-g)^2 J^2; de-poissonized rho_P by conditioning."""
    Jt = bessel_table(theta, M)
    st = mp.sqrt(theta)
    xs = list(range(-M, M + 1))
    gA = {k: _anti_abs(k) for k in xs}
    gW = {k: _anti_sq(k) for k in xs}
    gN = {k: mp.mpf(k) for k in xs}
    VA = VW = P = VN = CAN = CWN = mp.mpf(0)
    for i, x in enumerate(xs):
        aX, wX, nX = gA[x], gW[x], gN[x]
        for y in xs[i + 1:]:
            J = st * (Jt[x] * Jt[y + 1] - Jt[x + 1] * Jt[y]) / (x - y)
            if J == 0:
                continue
            J2 = J * J
            dA = aX - gA[y]; dW = wX - gW[y]; dN = nX - gN[y]
            VA += dA * dA * J2; VW += dW * dW * J2; P += dA * dW * J2
            VN += dN * dN * J2; CAN += dA * dN * J2; CWN += dW * dN * J2
    cond = lambda cXY, cXN, cYN: cXY - cXN * cYN / VN
    VA_n = cond(VA, CAN, CAN); VW_n = cond(VW, CWN, CWN); P_n = cond(P, CAN, CWN)
    rho = P_n / mp.sqrt(VA_n * VW_n)
    return VA, VW, P, rho   # VA poissonized (for the Debye target); rho de-poissonized


def main():
    thetas = [int(t) for t in (sys.argv[1:] or ["80", "160", "320", "640", "1280", "2560"])]
    print(f"# large-theta asymptotic constants of the descent-DPP; dps={mp.mp.dps}; NO float64")
    print(f"# {'theta':>6} {'M':>4} {'VA/theta^2':>16} {'rho_P(n)':>14} {'rho-RHOinf':>13}")
    rows = []
    for th in thetas:
        thm = mp.mpf(th)
        M = int(mp.floor(2 * mp.sqrt(thm) + 10 * mp.power(thm, mp.mpf(1) / 6) + 12))
        VA, VW, P, rho = ingredients(thm, M)
        sA = VA / thm ** 2
        rows.append((thm, sA, rho))
        print(f"  {th:>6} {M:>4} {mp.nstr(sA,12):>16} {mp.nstr(rho,10):>14} "
              f"{mp.nstr(rho - RHO_INF, 4):>13}")
    print()
    # Richardson: v_A = lim VA/theta^2; assume VA/theta^2 = v_A + c*theta^{-a}. Estimate a and v_A.
    if len(rows) >= 3:
        (t0, s0, _), (t1, s1, _), (t2, s2, _) = rows[-3], rows[-2], rows[-1]
        # exponent from three points (geometric theta): a = log((s0-s1)/(s1-s2))/log(t1/t0)
        d01 = s0 - s1; d12 = s1 - s2
        if d01 != 0 and d12 != 0 and (d01 / d12) > 0:
            a = mp.log(d01 / d12) / mp.log(t1 / t0)
            # v_A extrapolation: s2 - d12 * (1/(r^a -1)) with r=t2/t1
            r = t2 / t1
            vA = s2 - d12 / (r ** a - 1)
            print(f"# V_A/theta^2 fit:  exponent a = {mp.nstr(a,4)}  (kink worst-case 0.5)")
            print(f"#   v_A (extrapolated limit) = {mp.nstr(vA,10)}")
            CA = max(abs(s - vA) * mp.sqrt(t) for t, s, _ in rows)
            print(f"#   C_A^emp = max |V_A/theta^2 - v_A|*sqrt(theta) = {mp.nstr(CA,6)}"
                  "   (the constant Olver/Debye must dominate)")
    # rho_P deviation exponent
    print()
    print("# rho_P(n) -> RHO_inf deviation, |rho-RHOinf|*theta^b:")
    for b in (mp.mpf('0.5'), mp.mpf('1')):
        vals = [abs(rw[2] - RHO_INF) * rw[0] ** b for rw in rows]
        print(f"#   b={mp.nstr(b,2)}: " + " ".join(mp.nstr(v, 4) for v in vals)
              + ("  (flat => that IS the exponent)" if b == 1 else ""))
    print()
    print("# VERDICT INPUTS: if v_A converges at ~theta^-1/2 with a SMALL C_A^emp and rho_P even")
    print("#   faster, the true margin constant (~0.087, PR #5934) is tiny vs the 2.668 target.")
    print("#   A rigorous Olver/Debye C_A is a small multiple of the true coefficient (Olver bounds")
    print("#   are sharp), so closing (C<=2.668) is PLAUSIBLE -- but the verified number still needs")
    print("#   the multi-page constant-tracking; this probe does not produce it.")
    print("RESULT: true asymptotic constants pinned at large theta; feasibility assessed. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
