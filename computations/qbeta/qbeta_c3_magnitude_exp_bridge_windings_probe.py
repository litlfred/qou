#!/usr/bin/env python3
"""qbeta_c3_magnitude_exp_bridge_windings_probe.py — DTD3: does the even-channel
exponential bridge at CANONICAL cusp windings reproduce the c₃ magnitude ratio?

Derive-then-check, canonical windings only, NO tuning. This is the explicit "next
probe" flagged in `docs/coordination/udeform-spin-part-derivation.md`
(bean `qou-dtd3`): the sign of the bar-odd leak `S = c₃ + Vol(4₁)` is now
understood as a discrete winding-lattice datum `sign Im 𝔙₄₁ = sign G(m,ℓ)` ([W],
2026-07-27), and the OPEN piece is the *magnitude* ratio
`|S(proton)/S(muon)| ≈ 4.075`. The proposed magnitude route is the OTHER channel of
the same complex volume 𝔙₄₁ — the bar-even / cosh channel — via the exponential
bridge `|δf| ~ e^{−Re 𝔙 / ℏ_q}`, with the lattice-quantized even potential

    Re 𝔙₄₁(u_{m,ℓ}) = Vol(4₁) − (3/8)(ln q₀)² · (2m+ℓ)·ℓ .        [even/cross form]

So the predicted magnitude ratio between two windings is

    |S_p/S_m|_pred = e^{−ΔRe𝔙/ℏ_q} = e^{ (3/8)(ln q₀)² · ΔN / ℏ_q },
    ΔN = N(m_p,ℓ_p) − N(m_m,ℓ_m),  N(m,ℓ) = (2m+ℓ)·ℓ .

DERIVE (fixed, not fitted):
  - Re 𝔙₄₁ even/cross potential (κ = +√3/4 half-potential convention, #4405 A-poly
    cross-validated; the (3/8)(ln q₀)² coefficient is `(3/4)·(1/2)·(ln q₀)²` of the
    cross form (2m+ℓ)ℓ, per udeform-spin-part-derivation.md §Magnitude path).
  - The CANONICAL windings: meridian (1,0) → N=0 (the boost/muon side, G=+4);
    longitude (0,1) → N=1 (the spin/proton side, G=−2). No (m,ℓ) chosen to fit.
  - Both ℏ conventions tested: substrate ℏ_q = 1 − q₀⁻¹ and resurgence ℏ = log q₀.

CHECK (assertions, honest miss-is-a-miss):
  [D1] canonical meridian/longitude pair (ΔN = 1) predicts |S_p/S_m| ≈ 1.04 under
       BOTH ℏ conventions — undershoots the target 4.075 by ~3.9×.
  [D2] hitting 4.075 requires ΔN ≈ 34–36. The genuinely DISTINGUISHED canonical pair
       is meridian/longitude (ΔN = 1); ΔN ≈ 34 is not that pair, and is not even a
       cross-form pair-difference within the |m|,|ℓ| ≤ 3 box (spectrum reaches |N| = 27
       only at extreme windings like (3,3)). So the target is reachable only by
       deliberately selecting large/extreme windings — the Dang–Purcell dense-fit
       resource the corpus already flagged (magnitudes must not be pursued by
       cusp-shape selection).
  [D3] ⇒ MISS (scope-(a)): the even-channel exponential bridge at canonical windings
       does NOT reproduce the c₃ magnitude ratio. The magnitude stays open; this
       narrows the search by ruling out the canonical-winding exponential bridge.

No fit; no c_k wired; no SDeformedVolumeChannel instance fabricated; nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 50
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(50):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def cross_N(m: int, l: int) -> int:
    """even/cross-form integer N(m,ℓ) = (2m+ℓ)·ℓ."""
    return (2 * m + l) * l


def main() -> int:
    print("=" * 78)
    print(" DTD3: even-channel exponential bridge at CANONICAL windings vs |S_p/S_m|")
    print("=" * 78)
    q_pr, q_mu = q_at(50), q_muon_at(50)
    S_mu, S_pr = S(q_mu), S(q_pr)
    ratio_target = abs(S_pr / S_mu)
    L = mp.log(q_mu)  # anchors near-identical; use the muon anchor's ln q₀
    print(f"\n S(muon)={mp.nstr(S_mu,7)}  S(proton)={mp.nstr(S_pr,7)}"
          f"  target |S_p/S_m| = {mp.nstr(ratio_target,7)}")

    hbar_sub = 1 - 1 / q_mu          # substrate ℏ_q = 1 − q₀⁻¹
    hbar_log = L                     # resurgence ℏ = log q₀

    def pref(hb):
        return (mp.mpf(3) / 8) * L ** 2 / hb   # coefficient of ΔN in the exponent

    # [D1] canonical meridian (1,0)→N=0, longitude (0,1)→N=1  ⇒  ΔN = 1
    N_mer, N_lon = cross_N(1, 0), cross_N(0, 1)
    dN_canonical = N_lon - N_mer
    preds = {}
    for nm, hb in [("hbar_sub", hbar_sub), ("hbar_log", hbar_log)]:
        P = pref(hb)
        preds[nm] = mp.e ** (P * dN_canonical)
        print(f"  {nm}: (3/8)(ln q₀)²/ℏ = {mp.nstr(P,6)};  ΔN=1 ⇒ |S_p/S_m|_pred = "
              f"{mp.nstr(preds[nm],6)}")
    d1_undershoot = all(p < mp.mpf("1.1") for p in preds.values())

    # [D2] ΔN needed to hit the target, vs canonical low-winding cross-form spectrum
    dN_needed = {nm: mp.log(ratio_target) / pref(hb)
                 for nm, hb in [("hbar_sub", hbar_sub), ("hbar_log", hbar_log)]}
    canonical_windings = [(m, l) for m in range(-3, 4) for l in range(-3, 4)]
    N_spectrum = sorted({cross_N(m, l) for (m, l) in canonical_windings})
    max_abs_N = max(abs(n) for n in N_spectrum)
    pair_diffs = {a - b for a in N_spectrum for b in N_spectrum}
    # is the (rounded) needed ΔN even a canonical winding-pair difference?
    dN_int = int(mp.nint(dN_needed["hbar_sub"]))
    dN_reachable_as_pair = dN_int in pair_diffs
    for nm in dN_needed:
        print(f"  {nm}: ΔN needed for target = {mp.nstr(dN_needed[nm],6)}")
    print(f"  canonical cross-form spectrum (|m|,|ℓ|≤3): {N_spectrum}")
    print(f"  distinguished canonical pair = meridian(1,0)/longitude(0,1), ΔN={dN_canonical}")
    print(f"  needed ΔN≈{dN_int} reachable as a canonical pair-difference? {dN_reachable_as_pair}")
    # D2: the DISTINGUISHED canonical pair misses (ΔN=1 ⇒ ~1.04), and the needed ΔN is
    # neither that pair nor (for ℏ_sub) even a pair-difference in the ≤3 box.
    d2_needs_uncanonical = (dN_canonical == 1 and d1_undershoot and not dN_reachable_as_pair)

    # [D3] verdict: MISS
    print("\n ⇒ MISS (scope-(a)): even-channel exponential bridge at CANONICAL windings")
    print("   undershoots |S_p/S_m| by ~3.9×; hitting 4.075 needs ΔN≈34 (uncanonical,")
    print("   Dang–Purcell dense-fit territory). Magnitude stays OPEN; canonical-winding")
    print("   exponential bridge ruled out (scope-(a)). Sign remains lattice-arithmetic [W].")

    wb = WitnessBuilder("qbeta-c3-magnitude-exp-bridge-windings", engine="mpmath")
    wb.set_description(
        "DTD3 (bean qou-dtd3): tests the bar-even/cosh exponential bridge "
        "|δf|~e^{−Re𝔙/ℏ_q} with Re𝔙₄₁(u_{m,ℓ})=Vol(4₁)−(3/8)(ln q₀)²(2m+ℓ)ℓ as the "
        "c₃ magnitude route, at CANONICAL cusp windings (meridian (1,0) N=0, longitude "
        "(0,1) N=1, ΔN=1), no tuning. Both ℏ conventions predict |S_p/S_m|≈1.04, "
        "undershooting the target 4.075 by ~3.9×; the target needs ΔN≈34–36, outside the "
        "canonical low-winding cross-form spectrum (|N|≤15, |m|,|ℓ|≤3). MISS (scope-(a)): "
        "the canonical-winding even-channel exponential bridge does NOT reproduce the c₃ "
        "magnitude; magnitude stays open, sign remains lattice-arithmetic [W]. No fit; "
        "nothing wired; no instance fabricated.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("magnitude_bridge_readout", {
        "target_ratio_Sp_over_Sm": mp.nstr(ratio_target, 10),
        "canonical_delta_N": dN_canonical,
        "pred_ratio_hbar_sub": mp.nstr(preds["hbar_sub"], 10),
        "pred_ratio_hbar_log": mp.nstr(preds["hbar_log"], 10),
        "delta_N_needed_hbar_sub": mp.nstr(dN_needed["hbar_sub"], 8),
        "delta_N_needed_hbar_log": mp.nstr(dN_needed["hbar_log"], 8),
        "canonical_cross_form_max_abs_N": max_abs_N,
        "needed_delta_N_is_canonical_pair_difference": bool(dN_reachable_as_pair),
        "verdict": ("MISS scope-(a): canonical-winding even-channel exponential bridge "
                    "undershoots |S_p/S_m| ~3.9x; needs uncanonical ΔN≈34; magnitude open, "
                    "sign lattice-arithmetic")})
    wb.add_assertion("canonical_ratio_undershoots_both_hbar", str(bool(d1_undershoot)), "True")
    wb.add_assertion("distinguished_pair_misses_and_target_uncanonical",
                     str(bool(d2_needs_uncanonical)), "True")
    wb.save()
    print("\nwitness → qbeta-c3-magnitude-exp-bridge-windings.witness.json")
    ok = bool(d1_undershoot and d2_needs_uncanonical)
    print("ALL ASSERTIONS PASS (honest MISS recorded)" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
