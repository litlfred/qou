#!/usr/bin/env python3
"""qbeta_c3_deformed_median_discontinuity_probe.py — the DIRECT median/lateral-
Borel test the corpus inferred but never computed, for the deformed (u≠0) Φ_b
odd tower. Settles the "try deformed median resummation" fork branch.

Context: the bar-odd c₃ S (~0.0097/−0.0395) needs an ANCHOR-DEPENDENT datum
(S swings 2.44% while q₀ moves ~1e-8). The u=0 4₁ index has CS=0 (amphichiral)
so carries no bar-odd real; the proposed rescue is a median/Borel resummation of
the DEFORMED (u≠0) state integral. The corpus already showed (three ways) the
perturbative deformed κ̃-tower is ξ-frame-real (phase law κ̃_n/ξⁿ ∈ (−i)ⁿ·ℝ,
residual 6e-20) and its Borel singularity sits 88° off the substrate ray, and
INFERRED "single-valued, no median split" — but never directly computed the
lateral sums S_±. This probe computes them.

What it does (Borel–Padé[2/2] of the committed κ̃₁..κ̃₄ at the substrate
meridian, cited from qbeta-c3-borel-pade-deformed-meridian.witness.json):
  1. on-ray Laplace along x = i·t → reproduces Im 𝔙̃_b ≈ 0.0585 (the smooth scale);
  2. LATERAL sums S_± along x = i·t·e^{±iδ} (δ within the 88° margin) and the
     discontinuity S_+ − S_− → DIRECTLY confirms single-valued (disc ≈ 0), the
     result the corpus only inferred;
  3. the ACROSS-singularity Stokes discontinuity via the Padé residue at the
     Borel pole ξ₀ → the tower's Stokes-constant magnitude (anchor-blind, and
     only ~2 sig figs from 4 rungs, per the modular-resurgence T3 result).

VERDICT (scope-(a), reinforcing the proved prune): the physical resummation is
single-valued on the substrate ray (disc ≈ 0, now directly computed), so the
deformed median resummation is anchor-BLIND — it cannot supply S's swing. This
is subsumed by the Lean-proved `QOU.QBeta.SRigidity.no_anchor_invariant_realizes
_swing` (any anchor-invariant datum, incl. a fixed Stokes constant, cannot
realize an anchor-swinging S). The swing is the 1/u³ ladder-inversion of a
smooth numerator N_odd = S·u³ (BarOddLadderShape), whose geometric origin
(Im 𝔙_q → N_odd) is the open capstone — NOT a resummation. No c_k; no fit.

Run: python3 -u computations/probes/qbeta_c3_deformed_median_discontinuity_probe.py \\
       2>&1 | tee /tmp/qbeta_c3_deformed_median.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

set_compute_dps()

# Committed deformed κ̃_n(u_substrate) at the proton meridian (conf digits re/im),
# cited from computations/qbeta/qbeta-c3-borel-pade-deformed-meridian.witness.json
# (produced by docs/audits/scripts/qbeta_ohtsuki_deformed_kappa3_tall_ladder.py).
KAPPA_TILDE = [
    mp.mpc("0.58734338731121242885", "-0.019507249622872478038"),   # n=1
    mp.mpc("0.91213672160598223175", "-0.060655923702509204149"),   # n=2
    mp.mpc("3.9562908021323882106", "-0.39536049609981547201"),     # n=3
    mp.mpc("24.780232535481186432", "-3.3103459615937492858"),      # n=4
]
IM_V_ONRAY_REF = mp.mpf("0.0585499951473")   # committed on-ray resummation


def main() -> int:
    from qou_substrate.constants import q_at
    t = mp.log(q_at(50))          # substrate log-modulus; ℏ direction is x = i·t

    # Borel–Padé[2/2] of the tower: b_n = κ̃_n/(n+1)!, B(ξ) = Padé of Σ b_n ξ^{n+1}
    b = [KAPPA_TILDE[n] / mp.factorial(n + 1) for n in range(4)]
    c = [mp.mpc(0)] + b
    p, qq = mp.pade(c, 2, 2)

    def B(xi):
        return mp.polyval(p[::-1], xi) / mp.polyval(qq[::-1], xi)

    def laplace(xdir):
        # ∫_0^∞ e^{-s} B(xdir · s) ds along the ray x = xdir
        return mp.quad(lambda s: mp.e ** (-s) * B(xdir * s), [0, 5, 20, 60])

    print("=" * 78)
    print(" Deformed median / lateral-Borel discontinuity — DIRECT test (try-1)")
    print("=" * 78)
    print(f"  substrate t = ln q0 = {mp.nstr(t, 12)}   physical ray x = i·t (arg π/2)")

    # ---- 1. on-ray resummation (reproduce the committed 0.0585) ----
    x0 = mp.mpc(0, 1) * t
    S_on = laplace(x0)
    print(f"\n[1] on-ray Laplace  Im 𝔙̃_b = {mp.nstr(mp.im(S_on), 8)}  "
          f"(committed ref {mp.nstr(IM_V_ONRAY_REF, 8)})")
    onray_ok = abs(mp.im(S_on) - IM_V_ONRAY_REF) / IM_V_ONRAY_REF < mp.mpf("0.02")

    # ---- 2. LATERAL sums around the physical ray — SMOOTH vs JUMP ----
    # A genuine Stokes jump is CONSTANT as the straddle δ→0 (the rays keep
    # straddling the singularity); smooth angular variation scales LINEARLY with
    # δ (disc ≈ 2δ·|d Im/dθ| → 0). The physical ray (arg π/2) sits 88° from the
    # only Borel singularity, so no straddle occurs — expect linear (smooth).
    def disc_at(delta):
        Sp = laplace(x0 * mp.e ** (mp.mpc(0, 1) * delta))
        Sm = laplace(x0 * mp.e ** (mp.mpc(0, 1) * (-delta)))
        return abs(Sp - Sm)
    d1, d2, d3 = mp.mpf("0.30"), mp.mpf("0.15"), mp.mpf("0.075")
    D1, D2, D3 = disc_at(d1), disc_at(d2), disc_at(d3)
    # linear-scaling ratios (≈2 per halving ⇒ smooth, no jump)
    r12 = float(D1 / D2) if D2 else 0.0
    r23 = float(D2 / D3) if D3 else 0.0
    print(f"\n[2] lateral discontinuity vs straddle δ (SMOOTH ⇒ ∝δ ⇒ ratio≈2; "
          f"JUMP ⇒ constant ⇒ ratio≈1):")
    print(f"    |S_+−S_−|(δ=0.300) = {mp.nstr(D1,6)}")
    print(f"    |S_+−S_−|(δ=0.150) = {mp.nstr(D2,6)}   ratio D1/D2 = {r12:.4f}")
    print(f"    |S_+−S_−|(δ=0.075) = {mp.nstr(D3,6)}   ratio D2/D3 = {r23:.4f}")
    smooth = abs(r12 - 2) < 0.25 and abs(r23 - 2) < 0.25
    print(f"    ⇒ physical resummation is {'SMOOTH (no Stokes jump: disc∝δ→0)' if smooth else 'JUMP-LIKE'} "
          f"on the substrate ray")
    single_valued = smooth
    disc_phys = D3               # smallest-straddle residual, for the witness

    # ---- 3. across-singularity Stokes discontinuity (Padé residue at ξ₀) ----
    # The Borel pole ξ₀ (root of the [2/2] denominator). The lateral discontinuity
    # of the Laplace across the ray THROUGH ξ₀ is 2πi·Res_{ξ₀}(B)·(1/x)e^{−ξ₀/x}.
    den = qq[::-1]
    poles = mp.polyroots(den)
    xi0 = min(poles, key=lambda z: abs(z))     # nearest Borel singularity
    # residue of B = p/qq at simple root ξ₀:  p(ξ₀)/qq'(ξ₀)
    dq = [den[i] * (len(den) - 1 - i) for i in range(len(den) - 1)]  # derivative coeffs
    res = mp.polyval(p[::-1], xi0) / mp.polyval(dq, xi0)
    # Stokes-constant magnitude (normalization-free): |2πi·Res|
    stokes_mag = abs(2 * mp.pi * res)
    print(f"\n[3] across-singularity Stokes structure (Padé residue at ξ₀):")
    print(f"    nearest Borel pole ξ₀ = {mp.nstr(xi0, 8)}  |ξ₀| = {mp.nstr(abs(xi0),6)}"
          f"  arg = {mp.nstr(mp.arg(xi0),5)} rad ({mp.nstr(mp.arg(xi0)*180/mp.pi,4)}°)")
    Vol41 = 2 * mp.clsin(2, mp.pi / 3)
    print(f"    |2πi·Res_{{ξ₀}}(B)| = {mp.nstr(stokes_mag, 6)}   "
          f"(tower Stokes-constant magnitude; ANCHOR-BLIND, ~2 sig figs from 4 rungs)")
    print(f"    cf. action Vol(4₁)/π = {mp.nstr(Vol41/mp.pi, 6)} — consistent "
          f"(|ξ₀|≈action), NOT a new identification (T3: not identifiable to precision)")

    # anchor targets + named comparators (declared; NOT fitted)
    S_muon, S_proton = mp.mpf("0.00968298"), mp.mpf("-0.03945936")
    print(f"\n  reference: |S(muon)| = {mp.nstr(abs(S_muon),6)}  |S(proton)| = "
          f"{mp.nstr(abs(S_proton),6)}  Vol(4₁)/π = {mp.nstr(Vol41/mp.pi,6)}  "
          f"classical Stokes int = 3")
    print(f"  → on-ray Im 𝔙̃ ≈ {mp.nstr(mp.im(S_on),4)} is the |S|-SCALE but a SINGLE "
          f"smooth number — reproduces neither anchor (anchor-blind).")

    wb = WitnessBuilder("qbeta-c3-deformed-median-discontinuity", engine="mpmath")
    wb.set_description(
        "DIRECT lateral-Borel/median test of the deformed (u≠0) Φ_b odd tower — "
        "the computation the corpus inferred but never ran. Borel–Padé[2/2] of "
        "committed κ̃₁..κ̃₄ at the substrate meridian: (1) on-ray Laplace "
        "reproduces Im 𝔙̃_b≈0.0585; (2) lateral sums S_± around the physical ray "
        "give |S_+−S_−|≈0 — DIRECTLY confirms single-valued (no Stokes jump on "
        "the substrate ray); (3) across-singularity residue gives the tower's "
        "Stokes-constant magnitude (anchor-blind, ~2 sig figs). VERDICT scope-(a): "
        "the deformed median resummation is anchor-BLIND, cannot supply S's swing "
        "— subsumed by the Lean-proved no_anchor_invariant_realizes_swing. The "
        "swing is the 1/u³ inversion of a smooth N_odd=S·u³ (BarOddLadderShape); "
        "its geometric origin (Im 𝔙_q→N_odd) is the open capstone, not a "
        "resummation. No c_k; no fit.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("onray_reproduces_committed_resummation",
                     computed=abs(mp.im(S_on) - IM_V_ONRAY_REF) / IM_V_ONRAY_REF,
                     expected=0.0, tolerance=0.02,
                     source="on-ray Laplace Im 𝔙̃_b matches the committed 0.05855")
    wb.add_assertion("physical_ray_smooth_no_jump",
                     computed=abs(r23 - 2), expected=0.0, tolerance=0.25,
                     source="lateral discontinuity scales LINEARLY with straddle δ "
                            "(ratio D(δ)/D(δ/2)≈2 as δ→0): the physical-ray "
                            "resummation is SMOOTH, no Stokes jump — a genuine jump "
                            "would give ratio≈1 (constant). Directly computed, not "
                            "inferred from the off-ray argument")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("onray_Im_V", mp.nstr(mp.im(S_on), 12))
    wb.add_data("physical_lateral_discontinuity", mp.nstr(disc_phys, 8))
    wb.add_data("nearest_borel_pole", mp.nstr(xi0, 10))
    wb.add_data("tower_stokes_magnitude_anchor_blind", mp.nstr(stokes_mag, 8))
    wb.add_data("anchor_invariance_prune",
                "Lean-proved QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing "
                "(sorry-free): any anchor-invariant datum g(datum) with datum "
                "constant across anchors cannot equal an S that swings. The "
                "deformed tower + its Stokes constant are anchor-blind (proton-"
                "extracted, blind to 7.9e-9), hence excluded as the swing carrier.")
    wb.add_data("verdict",
                ("DEFORMED MEDIAN RESUMMATION IS ANCHOR-BLIND (try-1 settled, "
                 "directly). On-ray reproduces the committed 0.0585 |S|-scale; "
                 "lateral sums around the physical ray give |S_+−S_−|≈0 — the "
                 "physical resummation is single-valued (no Stokes jump), now "
                 "DIRECTLY computed, not inferred. The tower's across-singularity "
                 "Stokes magnitude is a fixed anchor-blind number. Excluded as the "
                 "swing carrier by the Lean-proved no_anchor_invariant_realizes_"
                 "swing. The swing is the 1/u³ inversion of a smooth N_odd "
                 "(BarOddLadderShape); geometric origin (Im 𝔙_q→N_odd) is the open "
                 "capstone — not a resummation, not a fixed knot's CS. No c_k; no fit."
                 if ok else "INCONCLUSIVE — an assertion failed; inspect output."))
    wb.save()
    print(f"\n  assertions passed: {ok}")
    print("  witness -> computations/probes/qbeta-c3-deformed-median-discontinuity.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
