#!/usr/bin/env python3
"""
A(D) follow-up to the GAP-A-3 §4 flat-baseline probe: how much must P_λ deviate?

The §4 probe (`2026-06-22-gap-a3-deuteron-plambda-flat-baseline-bareven.md`,
PR #2626) computed the canonical flat baseline tr_M(β_D)=Σ_λ y_λ χ^λ(β_D)=0.38836
and noted the immediate follow-up: compare the Phase-4-DERIVED A(D) against the
A(D)=11.21 the flat baseline (P_λ≡1) would need to hit −B(D)/m_e. This runs it.

A(K) = Vol_hyp(K)/[8]_q · [3]_q^{2(Z-1)} · (q^{1/2}+q^{-1/2})^{4N}   (gap-a3 scope,
Phase-4 substrate-derived, ≤2.5% zero-parameter). For the deuteron Z=1,N=1:
[3]_q^0=1, so A(D)=Vol_hyp(D)/[8]_q·(q^{1/2}+q^{-1/2})^4 with Vol_hyp(D)=12.776
(PR #787 Phase-3, Z=1 cluster).

The closure (A factored out, gap-a3 scope) is
    Σ_λ y_λ χ^λ(β_D) P_λ = −B(D)/(m_e·A(D)).
P_λ≡1 gives tr_M(β_D); so the REQUIRED suppression is
    r := [Σ y_λ χ^λ P_λ] / tr_M = (−B(D)/m_e) / (A(D)·tr_M).

DISCIPLINE: this QUANTIFIES the redistribution magnitude (how far P_λ must move
off flat); it does NOT propose a P_λ (that is the forbidden fit / the open
derivation). The ≈2 overshoot is reported with A(D)'s ≤2.5% uncertainty band —
claiming exactly 2 would be a fit.
"""
import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Q0 = mp.mpf("1.1099785955541805")
VOL_D = mp.mpf("12.776")            # Vol_hyp(D), PR #787 Phase-3 (Z=1 cluster)
TRM_BETA_D = mp.mpf("0.38835725751524")  # canonical, GAP-A-3 §4 probe (#2626)
TARGET = mp.mpf("4.353")            # |−B(D)/m_e|
A_REL_UNC = mp.mpf("0.025")         # A(K) is ≤2.5% zero-parameter (gap-a3 scope)


def qint(m):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


def main():
    spin = (Q0 ** mp.mpf("0.5") + Q0 ** mp.mpf("-0.5")) ** 4   # (q^½+q^-½)^{4N}, N=1
    A_D = VOL_D / qint(8) * spin
    flat = A_D * TRM_BETA_D
    overshoot = flat / TARGET
    r = TARGET / flat                # required (Σ y χ P)/tr_M

    print(f"q_0 = {Q0}  |  dps = {mp.mp.dps}\n")
    print("Phase-4-derived A(D)  (Vol_hyp(D)/[8]_q · (q^½+q^-½)^4):")
    print(f"  Vol_hyp(D)        = {mp.nstr(VOL_D,8)}  (PR #787 Phase-3, Z=1 cluster)")
    print(f"  [8]_q             = {mp.nstr(qint(8),10)}")
    print(f"  (q^½+q^-½)^4       = {mp.nstr(spin,10)}")
    print(f"  ⇒ A(D)            = {mp.nstr(A_D,10)}\n")
    print("Flat baseline (P_λ≡1) vs target:")
    print(f"  A(D)·tr_M(β_D)    = {mp.nstr(flat,10)}   (tr_M = {mp.nstr(TRM_BETA_D,8)})")
    print(f"  target |−B(D)/m_e|= {mp.nstr(TARGET,6)}")
    print(f"  OVERSHOOT factor  = {mp.nstr(overshoot,8)}")
    # propagate A(D)'s ≤2.5% uncertainty
    lo, hi = overshoot * (1 - A_REL_UNC), overshoot * (1 + A_REL_UNC)
    print(f"    (A(D) ±2.5% ⇒ overshoot ∈ [{mp.nstr(lo,5)}, {mp.nstr(hi,5)}])\n")
    print("What the redistribution must do:")
    print(f"  required [Σ y_λ χ^λ P_λ]/tr_M = target/(A(D)·tr_M) = {mp.nstr(r,8)}")
    print(f"  ⇒ the bar-even P_λ must SUPPRESS the effective trace to ~{mp.nstr(r*100,4)}% of flat")
    print(f"    (i.e. the flat baseline OVERSHOOTS the deuteron binding by ~{mp.nstr(overshoot,4)}×).")
    print()
    print("Critical-distance note:")
    print(f"  overshoot ≈ {mp.nstr(overshoot,4)} is consistent with EXACTLY 2 within A(D)'s ≤2.5%")
    print( "  band, but is NOT pinned to 2. Reporting ≈2.05; claiming exactly 2 (or that")
    print( "  P_λ is a clean factor-½ suppression) would be a fit — NOT asserted.")
    print("\nA(D) FOLLOW-UP COMPLETE (overshoot quantified; no P_λ proposed; no fit)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
