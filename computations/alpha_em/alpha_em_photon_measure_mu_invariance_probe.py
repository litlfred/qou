#!/usr/bin/env python3
"""alpha_em_photon_measure_mu_invariance_probe.py

Front-3 continuation of #3834 (`ζ_{Δ₁}(0) = −b₁`, area-free). The α_EM wall
(2026-07-14 derivability map) is precise: *why is the photon 1-loop measure the
count `b₁ = dim H¹(M_Bring) = 8`, not the Area?* — and turning "governed by b₁"
into the exact per-loop measure `1/(π b₁) = 1/(8π)` is "the RT shadow-world
1-loop determinant computation on the genus-4 Jacobian" (the multi-week item).

This probe asks the sharp question BEFORE that computation: **which part of
`1/(π b₁)` is μ-normalization-INVARIANT (hence derivable from the determinant)
and which lives in the μ-sector (hence a fitting trap on the flat torus)?**

Setup. The free 1-loop (Maxwell / scalar) fluctuation measure on the flat
Jacobian torus `J(M) = T^{b₁}` with UV normalization scale μ is

    Z_fluc(μ)  =  μ^{ ζ_{Δ}(0) } · (det' Δ)^{∓1/2} ,

because the normalized Gaussian measure `∏_k √(μ²/2π) dφ_k` contributes one
factor of `μ` per mode and the ζ-regularized mode count is `ζ_Δ(0)` (Hawking's
μ-scaling of a ζ-determinant). For the photon Hodge-1 Laplacian on `T^{b₁}`,
`ζ_{Δ₁}(0) = b₁·E_Λ(0) = −b₁` (#3834), so the μ-power is **exactly `−b₁`**,
area-free.

FINDINGS (scope-(a); C14; no α_k wired; no fit; anti-fitting per the spec):

  1. **μ-INVARIANT (derivable): the `b₁`, area-free.** The only μ-invariant place
     `b₁` enters is the anomaly coefficient `ζ_{Δ₁}(0) = −b₁` — verified area-free
     in #3834 (Epstein `E_Λ(0)=−1` ∀Λ). This IS the "why b₁ not Area" mechanism:
     the loop measure's `b₁` is the ζ-regularized scale-anomaly count, not the
     covolume. Derived.

  2. **μ-SECTOR (a fitting trap on the flat torus): the reciprocal `1/b₁` and the
     `π`.** The μ-power is `μ^{−b₁}` — *exponential* in `b₁`, NOT the reciprocal
     `1/b₁`. So the `1/(π b₁)` reciprocal form is NOT produced by the anomaly; it
     sits in the per-mode normalization / μ-choice sector. We demonstrate
     explicitly that μ absorbs any target: for ANY desired measure value `m`
     there is a μ with `Z_fluc(μ) = m` — so a flat-torus determinant cannot
     discriminate `1/(8π)` from any other constant without fixing μ externally.
     Tuning μ until `8π` appears is exactly the spec's forbidden fitting trap.

  3. **CONSEQUENCE — the flat-torus determinant route is PRUNED (scope-(a)).** The
     honest, non-fitting content extractable on `T^{b₁}` is the μ-invariant
     anomaly `−ζ_{Δ₁}(0) = b₁` (done, #3834). The reciprocal-and-`π` of
     `1/(π b₁)` is μ-normalization-dependent and therefore requires an
     **independent** μ-fixing — the categorical **RT / Reshetikhin–Turaev
     shadow-world** normalization on the genus-4 Jacobian (a TQFT-side, hence
     μ-invariant, prescription), NOT a flat-torus determinant μ-tune. This
     sharpens the wall: the residual is specifically the RT μ-prescription.

VERDICT (scope-(a) structural + route-prune): `−ζ_{Δ₁}(0)=b₁` (area-free) is the
derived μ-invariant "why b₁ not Area"; the `1/(π b₁)` reciprocal+π is μ-sector
and cannot be forced by a flat-torus determinant without the forbidden μ-tune —
so the honest closure route is the RT shadow-world normalization, not this. No
α_k wired; `1/(8π)` stays a phase-4 identification. This does NOT manufacture 8π.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

B1 = 8  # dim H¹(M_Bring) = b₁ (proven Lean, PR #2114; Jac(Bring)~E⁴, T^8)


def mu_power_of_b1(d: int) -> int:
    """The μ-exponent of the 1-loop fluctuation measure on T^d = ζ_{Δ₁}(0) = −d.
    (ζ_{Δ₁}(0) = d·E_Λ(0) = d·(−1); E_Λ(0)=−1 area-free, verified in #3834.)"""
    return -d  # = ζ_{Δ₁}(0)


def measure_at_mu(mu: mp.mpf, d: int, logdetprime: mp.mpf = mp.mpf(0)) -> mp.mpf:
    """Z_fluc(μ) = μ^{ζ(0)} · (det'Δ)^{-1/2}, ζ(0)=−d. det' folded into a constant
    (its value is μ-invariant and irrelevant to the μ-absorption point)."""
    return mu ** mu_power_of_b1(d) * mp.e ** (-mp.mpf("0.5") * logdetprime)


def main() -> int:
    print("=" * 78)
    print(" α_EM Front-3 — μ-invariance of 1/(π b₁): what is derivable vs the fitting trap")
    print("=" * 78)

    # --- 1. μ-invariant: the b₁ is the anomaly coefficient (area-free, #3834) ---
    print("\n[1] μ-INVARIANT content — the b₁ (area-free):")
    print(f"    ζ_{{Δ₁}}(0) on T^b₁ = b₁·E_Λ(0) = b₁·(−1) = −b₁ = −{B1}  (E_Λ(0)=−1 ∀ lattice, #3834)")
    print(f"    ⇒ the μ-power of the 1-loop measure is μ^(ζ(0)) = μ^(−{B1}) — a BARE b₁ count,")
    print("      area-free. This is the derived 'why b₁, not Area' mechanism.")
    mu_power = mu_power_of_b1(B1)
    invariant_is_b1 = (mu_power == -B1)

    # --- 2. μ-sector: the reciprocal 1/b₁ and π are NOT in the anomaly ---
    print("\n[2] μ-SECTOR content — the reciprocal 1/b₁ and π (the fitting trap):")
    print(f"    μ-power is μ^(−{B1}) = EXPONENTIAL in b₁, NOT the reciprocal 1/b₁.")
    print("    Demonstrate μ absorbs ANY target measure value m (⇒ 1/(8π) not discriminated):")
    target_18pi = 1 / (mp.pi * B1)            # 1/(8π), the data-selected value
    ok_absorb = True
    for m_target in (target_18pi, mp.mpf("0.001"), mp.mpf("1.0"), mp.mpf("7.3")):
        # solve μ^{-b₁}·e^{-0} = m  ⇒ μ = m^{-1/b₁}
        mu_star = m_target ** (mp.mpf(-1) / B1)
        got = measure_at_mu(mu_star, B1)
        err = abs(got - m_target)
        ok_absorb = ok_absorb and (err < mp.mpf("1e-20"))
        print(f"      target m={mp.nstr(m_target,6):>10}  ⇒  μ*={mp.nstr(mu_star,8)}  "
              f"gives Z={mp.nstr(got,6)}  (|Δ|={mp.nstr(err,2)})")
    print("    ⇒ ANY constant (incl. 1/(8π)) is reachable by choosing μ — so a flat-torus")
    print("      determinant CANNOT force 1/(π b₁) without externally fixing μ. Tuning μ")
    print("      until 8π appears is the spec's forbidden fitting trap.")

    # --- 3. consequence: prune the flat-torus route; name the real wall ---
    print("\n[3] CONSEQUENCE — flat-torus determinant route PRUNED (scope-(a)):")
    print("    Derivable here (μ-invariant): −ζ_{Δ₁}(0) = b₁, area-free (#3834). DONE.")
    print("    Residual (μ-sector): the reciprocal 1/b₁ + π of 1/(π b₁) ⇒ needs an")
    print("    INDEPENDENT μ-fixing = the categorical RT / Reshetikhin–Turaev shadow-world")
    print("    normalization on the genus-4 Jacobian (TQFT-side, μ-invariant), NOT a")
    print("    flat-torus μ-tune. The wall is specifically the RT μ-prescription.")

    wb = WitnessBuilder("alpha-em-photon-measure-mu-invariance", engine="mpmath")
    wb.set_description(
        "Front-3 continuation of #3834: decompose the target photon per-loop measure "
        "1/(π b₁)=1/(8π) into its μ-normalization-INVARIANT part (derivable from the "
        "determinant) and its μ-SECTOR part (a fitting trap on the flat torus). The "
        "1-loop fluctuation measure on the Jacobian torus T^{b₁} is "
        "Z_fluc(μ)=μ^{ζ_{Δ₁}(0)}·(det'Δ₁)^{-1/2} with ζ_{Δ₁}(0)=−b₁ (#3834). "
        "(1) μ-INVARIANT: the only place b₁ enters invariantly is the anomaly "
        "ζ_{Δ₁}(0)=−b₁, area-free — the derived 'why b₁ not Area' mechanism. "
        "(2) μ-SECTOR: the μ-power is μ^{−b₁} (exponential in b₁), NOT the reciprocal "
        "1/b₁; demonstrated that ANY target measure value (incl. 1/(8π)) is reachable "
        "by choosing μ (μ=m^{−1/b₁}), so a flat-torus determinant cannot discriminate "
        "1/(8π) — tuning μ to make 8π appear is the spec's forbidden fitting trap. "
        "(3) CONSEQUENCE: the flat-torus determinant route is PRUNED; the reciprocal+π "
        "of 1/(π b₁) requires an independent μ-fixing = the categorical RT shadow-world "
        "normalization on the genus-4 Jacobian (μ-invariant), not a flat-torus μ-tune. "
        "Scope-(a) structural + route-prune; no α_k wired; no fit; does NOT manufacture "
        "8π; 1/(8π) stays a phase-4 identification."
    )
    wb.set_content_block("prop:alpha-em-categorical-trace")
    wb.add_data("mu_invariant", {
        "b1": B1, "zeta_delta1_0": -B1, "mu_power_of_measure": mu_power,
        "reading": "b₁ enters μ-invariantly ONLY as ζ_{Δ₁}(0)=−b₁ (area-free, #3834) = the derived 'why b₁ not Area'"})
    wb.add_data("mu_sector_fitting_trap", {
        "mu_power_is_exponential_not_reciprocal": True,
        "any_constant_reachable_by_mu": bool(ok_absorb),
        "mu_for_1_over_8pi": mp.nstr(target_18pi ** (mp.mpf(-1) / B1), 10),
        "reading": "μ^{−b₁} exponential ⇒ 1/b₁ reciprocal + π live in the μ-normalization sector; "
                   "μ absorbs any constant ⇒ flat-torus determinant cannot force 1/(8π) (fitting trap)"})
    wb.add_data("consequence", {
        "flat_torus_route": "PRUNED — cannot force 1/(π b₁) without a forbidden μ-tune",
        "honest_wall": "the RT / Reshetikhin–Turaev shadow-world normalization on the genus-4 Jacobian "
                       "(μ-invariant TQFT prescription) — the multi-week item, now sharpened to the μ-fixing"})
    wb.add_assertion("mu_invariant_b1_is_neg_zeta",
                     computed=1.0 if invariant_is_b1 else 0.0, expected=1.0, tolerance=0.5,
                     source="the μ-invariant appearance of b₁ is exactly ζ_{Δ₁}(0)=−b₁ (area-free, #3834)")
    wb.add_assertion("mu_absorbs_any_constant_fitting_trap",
                     computed=1.0 if ok_absorb else 0.0, expected=1.0, tolerance=0.5,
                     source="μ=m^{−1/b₁} reproduces ANY target measure m incl 1/(8π) => flat-torus determinant "
                            "cannot discriminate 1/(π b₁); μ-tune is the forbidden fitting trap")
    wb.save()
    print("\n  RESULT: μ-invariant b₁ (area-free) DONE (#3834); the 1/(π b₁) reciprocal+π is")
    print("          μ-sector (fitting trap) ⇒ flat-torus route PRUNED; wall = the RT μ-fixing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
