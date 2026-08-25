#!/usr/bin/env python3
"""alpha_em_schwinger_ladder_probe.py

The α_EM O(α²) tower at the CORRECT (proton) anchor — corrects the earlier
form-ladder which used the quadratic fixed-point and understated the accuracy.

At the proton pin (which α_EM independently prefers to 0.245 ppb — see
alpha_em_anchor_preference_probe.py), the ladder is:

  form A  (quadratic, α²H + αT − 1 = 0; NO Schwinger)        1/α resid = +1.67 ppb
  form B  (cubic, +derived Schwinger (1−h²α), RT phase 3)    1/α resid = +0.313 ppb  ≈ 2× σ_α

So α_EM with the RT-phase-3-DERIVED Schwinger self-energy factor (1−h²α) — NOT a
fitted knob — lands at +0.313 ppb = ~2× the 0.15 ppb experimental σ. This is far
closer than the 80 ppb (muon-anchor) or 1.67 ppb (proton, no-Schwinger) headlines.

The remaining +0.313 ppb is the genuine 2-loop O(α²) term, of size
  c₂ = residual/α² ≈ 8.1e-4,
which is UNCOMPUTED (the RT phase-2 EmFermionLoop program). It is NOT the Ohtsuki
2-loop κ₁ = 11√3π/108 ≈ 0.554 (a different, even-channel object in ℚ(√3); α_EM's
c₂ is ~680× smaller).

HONEST STATUS: with the correct anchor + the derived Schwinger term, α_EM misses
its 100× target by only ~2× — the closest any not-yet-met observable sits to 1 ppq.
The last factor of 2 is a small uncomputed 2-loop coefficient (plus the still-
conjectural physical coupling claim + upstream classes). No coefficient fitted here
(the Schwinger factor is derived; only q0 is the documented proton pin); scope-(a).

Companion: alpha_em_anchor_preference_probe.py, alpha_em_form_ladder_probe.py (#3612,
which used form A only), QOU/Archimedean/EmCouplingBringZeroMode.lean (#3625).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
CODATA = mp.mpf("137.035999084")
SIGMA_PPB = mp.mpf("0.15")
Q_PROTON = mp.mpf("1.109978582751380808")
KAPPA1_OHTSUKI = 11 * mp.sqrt(3) * mp.pi / 108


def qb(n, q):
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def ppb(v):
    return float((v - CODATA) / CODATA * 1e9)


def main() -> int:
    print("=" * 78)
    print(" α_EM O(α²) tower at the proton anchor — form-A → form-B(Schwinger) ladder")
    print("=" * 78)

    wb = WitnessBuilder("alpha-em-schwinger-ladder", engine="mpmath")
    wb.set_description(
        "The alpha_EM ladder at the proton pin: form A (quadratic, no Schwinger) "
        "resid +1.67 ppb -> form B (+derived Schwinger (1-h^2 alpha), RT phase 3) "
        "resid +0.313 ppb ~ 2x sigma_a. Corrects the earlier form-ladder (form A only, "
        "understated). Remaining 2-loop c2 ~ 8.1e-4 (uncomputed, NOT Ohtsuki kappa1=0.554). "
        "alpha_EM misses its 100x target by only ~2x at the correct anchor. Schwinger "
        "factor derived (not fitted); q0 = documented proton pin; scope-(a)."
    )
    wb.set_content_block("prop:em-coupling-bring-zero-mode")

    q = Q_PROTON
    h2 = (q - 1 / q) ** 2
    T = q * qb(9, q) * qb(10, q) + mp.mpf(8) / (12 * mp.pi)
    H = qb(2, q) / (8 * mp.pi)

    # form A: quadratic α²H + αT − 1 = 0
    aA = (-T + mp.sqrt(T * T + 4 * H)) / (2 * H)
    # form B: cubic, 1/α = T + αH(1 − h²α)  ⇒  −H·h²·α³ + H·α² + T·α − 1 = 0
    roots = mp.polyroots([-H * h2, H, T, -1])
    aB = min([mp.re(r) for r in roots if mp.im(r) == 0 and mp.re(r) > 0],
             key=lambda r: abs(r - mp.mpf("0.0073")))

    rA, rB = ppb(1 / aA), ppb(1 / aB)
    print(f"\n  proton pin q0 = {float(q):.12f}   h² = {mp.nstr(h2, 8)}")
    print(f"  form A (no Schwinger)   : 1/α = {mp.nstr(1/aA,15)}   resid = {rA:+.3f} ppb  ({abs(rA)/float(SIGMA_PPB):.0f}× σ)")
    print(f"  form B (+Schwinger 1−h²α): 1/α = {mp.nstr(1/aB,15)}   resid = {rB:+.3f} ppb  ({abs(rB)/float(SIGMA_PPB):.1f}× σ)")
    print(f"  Schwinger term closes {rA-rB:+.3f} ppb of the gap (derived, RT phase 3)")

    resB = 1 / aB - CODATA
    c2 = resB / aB ** 2
    print(f"\n  remaining 2-loop term: c₂ = residual/α² = {mp.nstr(c2, 6)}")
    print(f"  Ohtsuki κ₁ = 11√3π/108 = {mp.nstr(KAPPA1_OHTSUKI, 6)}  (different object; c₂ is ~{float(KAPPA1_OHTSUKI/abs(c2)):.0f}× smaller)")
    print(f"\n  HONEST HEADLINE: α_EM (proton pin + derived Schwinger) = {rB:+.3f} ppb = ~{abs(rB)/float(SIGMA_PPB):.1f}× σ_α")
    print("  => the closest any not-yet-met observable sits to its 1-ppq target.")
    print("  Remaining: a small uncomputed 2-loop c₂ + the conjectural coupling claim.")

    wb.add_data("ladder_proton", {
        "form_A_no_schwinger_ppb": rA, "form_B_schwinger_ppb": rB,
        "schwinger_shift_ppb": rA - rB,
        "form_A_sigma": abs(rA) / float(SIGMA_PPB), "form_B_sigma": abs(rB) / float(SIGMA_PPB)})
    wb.add_data("two_loop", {
        "c2": mp.nstr(c2, 12), "kappa1_ohtsuki": mp.nstr(KAPPA1_OHTSUKI, 12),
        "c2_vs_kappa1": f"c2 ~ {float(KAPPA1_OHTSUKI/abs(c2)):.0f}x smaller — different object",
        "status": "uncomputed (RT phase-2 EmFermionLoop)"})
    wb.add_assertion("schwinger_brings_alpha_within_3sigma",
                     computed=float(abs(rB) < 3 * float(SIGMA_PPB)), expected=1.0, tolerance=0.5,
                     source="form B (proton + derived Schwinger) resid +0.313 ppb < 3σ (=0.45 ppb)")
    wb.add_assertion("schwinger_improves_over_form_A",
                     computed=float(abs(rB) < abs(rA)), expected=1.0, tolerance=0.5,
                     source="Schwinger term reduces |resid| 1.67 -> 0.313 ppb")
    wb.save()

    print(f"\n  RESULT: α_EM at proton + Schwinger = {rB:+.3f} ppb (~2× σ); 2-loop c₂ uncomputed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
