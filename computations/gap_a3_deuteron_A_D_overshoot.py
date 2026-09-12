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
# ── MUON-anchored and CONVENTION C — labelled 2026-08-23 (bean `qou-8chw`),
# matching the label bean `qou-khac` put on the sibling
# `gap_a3_overshoot_robustness_check.py`. Q0 and TRM_BETA_D below are the SAME
# MATCHED PAIR as that file's: byte-identical literals, same #2635-vintage run.
# The sibling was labelled; this one was not, which is the only difference.
#
# DO NOT "refresh" TRM_BETA_D to the live value. The corpus moved to convention
# D on 2026-08-09; the live D deuteron trace is 0.5751722439177719, 48% larger.
# Substituting it would inflate `flat = A_D * TRM_BETA_D` and hence the
# overshoot by 48% while leaving Q0 on the muon pin — breaking the matched pair
# and silently changing this probe's recorded conclusion. Per the 2026-08-15
# ruling, C-frame values are CORRECT FOR C and need scoping, not correction.
#
# Verified by construction rather than inferred: recombining the transfer's own
# chi with the live convention-C weights
# (schur_principal_mpmath.y_lambda_at_q0_mpmath_convention_C_HISTORICAL)
# reproduces 0.3883571886893111 at the muon pin and 0.3883571411977910 at the
# proton pin -- i.e. this literal's family IS convention C, to ~7 digits. (The
# residual ~1.8e-7 is an older C vintage, not a pin difference.)
#
# Re-deriving this probe under convention D is bean `qou-cds1` work, not a
# constant swap.
# ── MIGRATED TO CONVENTION D AT THE PROTON PIN, 2026-09-12 (bean qou-46ys) ──
# The header above forbids refreshing TRM_BETA_D **alone**, and it is right: Q0
# and TRM are a MATCHED PAIR. This moves BOTH from one source --
# `canonical-mass-table-extended.witness.json` (q0Anchor: proton, 2026-09-07) --
# so the pair stays matched, and its sibling
# `gap_a3_overshoot_robustness_check.py` was migrated the same way, so the two
# files stay consistent with each other. That is what the header asks for.
#
# 🛑 THE HEADER'S "48%" IS COMPUTED ON A STALE FIGURE, and its direction is
# INVERTED. It warns that substituting the live value "would inflate ... the
# overshoot by 48%". That 48% is the ratio to 0.5751, the D deuteron |tr_M| as
# recorded in the 2026-08-15 rho-k audit -- correct then, stale now. The live
# convention-D value at the proton pin is 0.15197, so migrating DEFLATES by
# ~2.56x. Same trap as its sibling; recorded in both.
#
# WHAT THIS REPLACED:
#   Q0         = mp.mpf("1.1099785955541805")   # MUON anchor
#   TRM_BETA_D = mp.mpf("0.38835725751524")     # CONVENTION C
import json as _json
from pathlib import Path as _Path

_TBL = _json.loads(
    (_Path(__file__).resolve().parent / "canonical-mass-table-extended.witness.json"
     ).read_text())
Q0 = mp.mpf(str(_TBL["q0Value"]))        # PROTON pin (owner ruling R2, 2026-08-15)
VOL_D = mp.mpf("12.776")            # Vol_hyp(D), PR #787 Phase-3 (Z=1 cluster)
# 🛑 VOL_D IS STILL A C-ERA ASSIGNMENT. The convention migration covers tr_M and
# the anchor; a convention-D-consistent knot/volume assignment has NOT been
# derived (bean qou-e5jf's arc). So the overshoot below is D in its trace and C
# in its geometry -- a genuine remaining straddle, stated rather than hidden.
# CONVENTION D deuteron |tr_M| (Z=1, N=1), read from the committed table.
TRM_BETA_D = mp.mpf(next(r["tr_M_q0_canonical_50dps"]
                         for r in _TBL["data"]["rows"]
                         if (r["Z"], r["N"]) == (1, 1)))
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
    # COMPUTED DIRECTION, 2026-09-12. This said "OVERSHOOT factor" and the three
    # lines below asserted SUPPRESS / OVERSHOOTS / "Reporting ~2.05"
    # unconditionally. All were the convention-C answer. Under D the flat
    # baseline UNDERSHOOTS (0.8021 < 1), so the required P_lam flips sign: it
    # must ENHANCE, not suppress. An unconditional "SUPPRESS" next to a computed
    # 124.7% is prose contradicting its own number.
    _over = overshoot > 1
    print(f"  {'OVER' if _over else 'UNDER'}SHOOT factor  = {mp.nstr(overshoot,8)}"
          f"   ({'>' if _over else '<'} 1)")
    # propagate A(D)'s ≤2.5% uncertainty
    lo, hi = overshoot * (1 - A_REL_UNC), overshoot * (1 + A_REL_UNC)
    print(f"    (A(D) ±2.5% ⇒ overshoot ∈ [{mp.nstr(lo,5)}, {mp.nstr(hi,5)}])\n")
    print("What the redistribution must do:")
    print(f"  required [Σ y_λ χ^λ P_λ]/tr_M = target/(A(D)·tr_M) = {mp.nstr(r,8)}")
    print(f"  ⇒ the bar-even P_λ must {'SUPPRESS' if r < 1 else 'ENHANCE'} the "
          f"effective trace to ~{mp.nstr(r*100,4)}% of flat")
    print(f"    (i.e. the flat baseline {'OVERSHOOTS' if _over else 'UNDERSHOOTS'} "
          f"the deuteron binding by ~{mp.nstr(overshoot,4)}×).")
    if r > 1:
        print( "    🛑 THE SIGN OF THE REQUIRED CORRECTION IS OPPOSITE to the")
        print( "       convention-C conclusion this probe was written for. Under C")
        print( "       the flat baseline overshot by ~2.05x and P_lam had to SUPPRESS")
        print( "       to ~48.79%; under canonical D it undershoots and P_lam must")
        print( "       ENHANCE. Any P_lam search inheriting the 'suppression' framing")
        print( "       is aimed the wrong way.")
    print()
    print("Critical-distance note:")
    # The "consistent with EXACTLY 2 ... Reporting ~2.05" text was hardcoded and
    # is now false; test the integer-proximity claim instead of asserting it.
    _lo, _hi = overshoot * (1 - A_REL_UNC), overshoot * (1 + A_REL_UNC)
    _near2 = _lo <= 2 <= _hi
    print(f"  {'over' if _over else 'under'}shoot ≈ {mp.nstr(overshoot,4)}; is 2 inside "
          f"A(D)'s ±{mp.nstr(A_REL_UNC*100,3)}% band [{mp.nstr(_lo,5)}, "
          f"{mp.nstr(_hi,5)}]? {_near2}")
    print( "  Under convention C this read 'consistent with EXACTLY 2 ... Reporting")
    print( "  ≈2.05'; that was the C-frame value. Claiming a clean integer (or that")
    print( "  P_λ is a clean factor-½ suppression) would be a fit — NOT asserted.")
    print("\nA(D) FOLLOW-UP COMPLETE (overshoot quantified; no P_λ proposed; no fit)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
