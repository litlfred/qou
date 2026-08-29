#!/usr/bin/env python3
"""M_1>0 machinery (qou-k5r5): edge-vs-bulk decomposition of the V_A remainder -- HONEST NEGATIVE.

Gap qou-k5r5. Tests the hypothesis that the theta^{-1} remainder of V_A(theta)/theta^2 -> 8/pi^2 is
EDGE-dominated (the Airy soft-edge transition) with the deep bulk converging faster. It does NOT
cleanly confirm that: the edge annulus and the deep bulk contributions COMPENSATE, so a crude split
cannot isolate which region carries the theta^{-1} remainder.

Method: V_A(theta) = (1/2) sum_{x!=y} (g(x)-g(y))^2 J(x,y;theta)^2, g=G_A(k)=+-k(k+1)/2, J the
discrete Bessel kernel. Split off the edge annulus |x| in [2sqrt(th)-K th^{1/6}, 2sqrt(th)+K th^{1/6}]
and compare V_A/theta^2 (full) to its edge-annulus contribution. NO float64 (mpmath.mpf).

FINDING (measured, theta=2000..32000, K=3):
  - full remainder theta*(V_A/theta^2 - 8/pi^2) ~ -0.067 (stable) => theta^{-1}, small (<=2%) oscillation
    (consistent with qou-tvok c_1 ~ -0.068 and the Airy-edge signature there);
  - edge-annulus contribution to V_A/theta^2 is LARGE and slowly decreasing (~0.53 -> 0.36, ~theta^{-0.14});
  - the deep-bulk share moves oppositely: the two regions COMPENSATE, so the split does NOT isolate the
    origin of the theta^{-1} remainder. A clean decomposition would need the per-region limit constants,
    which have no closed form.

CONCLUSION: the mechanism is a soft-edge double-scaling limit (Airy / Painleve II, DIK sec 11 -- the
Plancherel/Gessel/BDJ problem), NOT a fixed Fisher-Hartwig singularity; but this probe does NOT
establish edge- vs bulk-dominance of the remainder. Recorded so a later attempt does not assume it.
See docs/audits/2026-08-29-covariance-kernel-M1-k5r5-derivation-attempt-double-scaling.md.

scope-(a); NO float64; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 40
TARGET = 8 / mp.pi ** 2


def gA(k):
    return mp.mpf(k * (k + 1)) / 2 if k >= 0 else -mp.mpf(k * (k + 1)) / 2


def VA_split(theta, Kedge):
    M = int(mp.floor(2 * mp.sqrt(theta) + 14 * mp.power(theta, mp.mpf(1) / 6) + 24))
    arg = 2 * mp.sqrt(theta); st = mp.sqrt(theta)
    edge = 2 * mp.sqrt(theta); sc = mp.power(theta, mp.mpf(1) / 6)
    lo = edge - Kedge * sc; hi = edge + Kedge * sc
    J = {0: mp.besselj(0, arg)}
    for x in range(1, M + 2):
        J[x] = mp.besselj(x, arg); J[-x] = (-1) ** x * J[x]
    xs = list(range(-M, M + 1)); g = {k: gA(k) for k in xs}
    Vfull = mp.mpf(0); Vnoedge = mp.mpf(0)
    for i, x in enumerate(xs):
        gx = g[x]; xin = lo <= abs(x) <= hi
        for y in xs[i + 1:]:
            Jxy = st * (J[x] * J[y + 1] - J[x + 1] * J[y]) / (x - y)
            if Jxy == 0:
                continue
            t = (gx - g[y]) ** 2 * Jxy * Jxy
            Vfull += t
            if not (xin or lo <= abs(y) <= hi):
                Vnoedge += t
    return Vfull / theta ** 2, Vnoedge / theta ** 2


def main():
    print("# edge-vs-bulk decomposition of V_A remainder; K=3; dps=40; NO float64 -- HONEST NEGATIVE")
    print("# theta   d=V_A/th^2-8/pi^2   th*d       edge_contrib   th*edge_contrib")
    for th in (mp.mpf(2000), mp.mpf(4000), mp.mpf(8000), mp.mpf(16000), mp.mpf(32000)):
        vf, vne = VA_split(th, 3)
        d = vf - TARGET; edgec = vf - vne
        print(f"  {int(th):>6}  {mp.nstr(d,4):>12}  {mp.nstr(th*d,6):>10}  "
              f"{mp.nstr(edgec,5):>10}  {mp.nstr(th*edgec,6)}")
    print("# full remainder ~ -0.067/theta (clean theta^-1); edge annulus large & slowly decreasing")
    print("#   (~theta^-0.14); regions COMPENSATE -> split does NOT isolate the theta^-1 origin.")
    print("# => mechanism is soft-edge double-scaling (Airy/PII, DIK sec11 = Plancherel/BDJ); edge-vs-bulk")
    print("#    dominance NOT established. Honest negative.")
    print("RESULT: edge/bulk split does not isolate the theta^-1 remainder (regions compensate). qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
