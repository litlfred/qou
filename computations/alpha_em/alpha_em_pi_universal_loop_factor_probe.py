#!/usr/bin/env python3
"""alpha_em_pi_universal_loop_factor_probe.py

π-DECOMPOSITION of the α_EM per-loop measure `1/(π b₁) = 1/(8π)`.

Bounded STRUCTURAL probe (scope-(a); NOT a fit, NOT a derivation): decide
**where the `π` comes from** in the data-selected photon per-loop measure
`1/(π b₁) = 1/(8π)`, `b₁ = dim H¹(M_Bring) = 8`. Two hypotheses:

  (U) the `π` is the UNIVERSAL 1-loop factor — the loop-momentum angular
      integration `∫d^d k/(2π)^d` and/or the Schwinger `∫ds/s` heat-kernel
      Gaussian normalization `(4πs)^{-d/2}`; or
  (G) the `π` is a GEOMETRIC / categorical constant — a Gauss-Bonnet Area
      factor, a period, or a single archimedean π multiplying the topological
      count `b₁`.

The lever is the ONE **proved** α_EM π-template in the corpus: the photon IR
zero-mode (`QOU.Archimedean.PhotonIRZeroMode`, PR #2114),

    δ(1/α_EM)_IR = b₁ / Area = b₁ / (4π(g-1)) = 8/(12π) = 2/(3π)   (g = 4).

In THAT proved form the `π` is unambiguously GEOMETRIC: it is the Gauss-Bonnet
hyperbolic area `Area = -2πχ = 4π(g-1)`. The zero-mode is the kernel of the
1-form Laplacian Δ₁ (harmonic forms, NO momentum integration) normalized by the
surface area — a ratio of two geometric quantities, so its π is the area's π.

KEY STRUCTURAL FACT this probe computes exactly:

  * the proved zero-mode π-home is `Area = 12π`;
  * the self-energy per-loop π-home is `π·b₁ = 8π`;
  * they DIFFER — exactly — by the pure topological ratio
        Area / (π·b₁) = 4π(g-1) / (π·2g) = 2(g-1)/g = 3/2   (g = 4),
    i.e. `12π / 8π = 3/2`.

So the self-energy `π` is NOT the proved geometric Gauss-Bonnet `π`: if it were,
the denominator would be the Area `12π`, and `D = Area/π = 12` is the corpus's
9500σ / −1419 ppb FALSIFICATION (`alpha_em_perloop_integer_forcedness`,
`2026-07-17-...`). The one π we have PROVED to be geometric is demonstrably a
DIFFERENT π from the self-energy's. Hypothesis (G)-as-Area is therefore excluded
by the precedent + data.

What remains for the self-energy `π` (a genuine n=2 loop, the `α·H` term in
`1/α = T + α·H`) is the UNIVERSAL 1-loop family. The probe tabulates the
universal d-dim loop constants and shows `8π = 2·(4π)` factors cleanly with the
2D heat-kernel Gaussian normalization `(4π)^{d/2}|_{d=2} = 4π` (the photon loop
lives strictly on the 2-surface — the zero-mode doc's own dimensional-reduction
argument), the residual `2` a symmetry/mode-multiplicity factor — whereas the
momentum measure `(2π)^d|_{d=2} = 4π²` carries `π²`, not `π`, and the Schwinger
`∫ds/s` carries no π. The universal 2D heat-kernel factor is the only universal
constant of the right shape (a single `π`).

VERDICT (scope-(a) structural, leaning-UNIVERSAL, residual OPEN):
  * The proved precedent's π is geometric (Gauss-Bonnet Area) and — computed
    exactly here — is a DIFFERENT π from the self-energy's (they differ by the
    topological factor 2(g-1)/g = 3/2; the Area value 12π is data-FALSIFIED).
    So hypothesis (G) read as "the same geometric Area π" is EXCLUDED.
  * The self-energy is a genuine 1-loop diagram, so by universality its π is the
    loop-integration factor; `8π = 2·(4π)` matches the universal 2D heat-kernel
    Gaussian normalization `(4π)^{d/2}|_{d=2}`. This SUPPORTS hypothesis (U).
  * RESIDUAL OPEN (STRICT — not manufactured): the EXACT bare-π reciprocal
    normalization is not derived. `8π` is compatible with both `(4π)·2`
    [universal loop × symmetry-2] and `(π)·(b₁=8)` [one loop-π × an 8-mode
    trace over the b₁ harmonic sectors] — both are UNIVERSAL-loop-family
    readings, but which multiplicity (2 vs b₁) and why the reciprocal form is
    the open wall. No `8π` is manufactured; no α_k wired; no fit; `1/(8π)` stays
    a phase-4 identification.
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


def gauss_bonnet_area(g: int) -> mp.mpf:
    """Hyperbolic area at curvature −1: Area = −2πχ = 4π(g−1) (Gauss–Bonnet)."""
    return 4 * mp.pi * (g - 1)


def heat_kernel_gaussian_norm(d: int) -> mp.mpf:
    """Universal small-s heat-kernel Gaussian normalization (4π)^{d/2} — the π
    factor of the free-field 1-loop measure on a d-manifold. d=2 → 4π."""
    return (4 * mp.pi) ** (mp.mpf(d) / 2)


def momentum_measure_norm(d: int) -> mp.mpf:
    """Loop-momentum angular measure (2π)^d from ∫d^d k/(2π)^d. d=2 → 4π²."""
    return (2 * mp.pi) ** d


def main() -> int:
    print("=" * 78)
    print(" α_EM π-decomposition — is the π in 1/(π b₁)=1/(8π) the UNIVERSAL")
    print(" 1-loop factor, or the GEOMETRIC Gauss–Bonnet π?")
    print("=" * 78)

    g = 4                       # Bring genus
    b1 = 2 * g                  # = 8 = dim H¹(M_Bring)
    assert b1 == 8

    # ---- (1) The PROVED geometric-π template: photon IR zero-mode -----------
    Area = gauss_bonnet_area(g)                 # = 12π
    zero_mode = mp.mpf(b1) / Area               # b₁/Area = 8/(12π) = 2/(3π)
    two_thirds_pi = 2 / (3 * mp.pi)
    zm_ok = abs(zero_mode - two_thirds_pi) < mp.mpf("1e-30")
    print("\n [PROVED template — photon IR zero-mode, PhotonIRZeroMode.lean]")
    print(f"   Area = 4π(g−1) = {mp.nstr(Area, 12)}  = 12π   (Gauss–Bonnet, GEOMETRIC π)")
    print(f"   b₁/Area = {mp.nstr(zero_mode, 12)}   2/(3π) = {mp.nstr(two_thirds_pi, 12)}"
          f"   match={zm_ok}")
    print("   ⇒ here the π IS geometric: it is the hyperbolic Area's π.")

    # ---- (2) The self-energy per-loop π-home vs the geometric Area ----------
    self_energy_pi_home = mp.pi * b1            # = 8π  (the 1/(π b₁) denominator)
    area_over_pib1 = Area / self_energy_pi_home # = 12π/8π = 3/2, exactly
    topo_ratio = mp.mpf(2 * (g - 1)) / g        # = 2(g−1)/g = 3/2
    ratio_ok = abs(area_over_pib1 - topo_ratio) < mp.mpf("1e-30")
    print("\n [SEPARATION — the two π-homes are DIFFERENT, by a pure topological ratio]")
    print(f"   self-energy π-home  π·b₁ = {mp.nstr(self_energy_pi_home, 12)}  = 8π")
    print(f"   geometric π-home    Area = {mp.nstr(Area, 12)}  = 12π")
    print(f"   Area/(π·b₁) = {mp.nstr(area_over_pib1, 12)}   2(g−1)/g = "
          f"{mp.nstr(topo_ratio, 12)}   match={ratio_ok}")
    print("   ⇒ 8π ≠ 12π: the self-energy π is NOT the proved geometric Area π")
    print("     (the Area reading D=Area/π=12 is the corpus's 9500σ / −1419 ppb FALSIFICATION).")

    # ---- (3) Universal 1-loop constants (photon loop lives on the 2-surface) --
    hk2 = heat_kernel_gaussian_norm(2)          # = 4π
    mom2 = momentum_measure_norm(2)             # = 4π²
    eight_pi = mp.pi * b1                        # = 8π
    mult_hk = eight_pi / hk2                     # = 8π/4π = 2
    mult_mom = eight_pi / mom2                   # = 8π/4π² = 2/π (non-integer, π-laden)
    hk_clean = abs(mult_hk - 2) < mp.mpf("1e-30")
    print("\n [UNIVERSAL 1-loop candidates on the 2-surface (d=2)]")
    print(f"   heat-kernel (4π)^(d/2)|_(d=2) = {mp.nstr(hk2, 12)} = 4π   →  8π/4π = "
          f"{mp.nstr(mult_hk, 8)}  (clean ×2, single π: match={hk_clean})")
    print(f"   momentum   (2π)^d|_(d=2)      = {mp.nstr(mom2, 12)} = 4π²  →  8π/4π² = "
          f"{mp.nstr(mult_mom, 8)}  (2/π: π² measure, WRONG shape)")
    print("   Schwinger  ∫ds/s                = dimensionless          →  carries no π")
    print("   ⇒ only the 2D heat-kernel factor 4π has the single-π shape; 8π = 2·(4π).")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "-" * 78)
    print(" VERDICT (scope-(a), leaning-UNIVERSAL, residual OPEN):")
    print("  • proved zero-mode π = geometric Gauss–Bonnet Area π, and it is a DIFFERENT π")
    print("    from the self-energy's (differ by 2(g−1)/g = 3/2; Area=12π is data-falsified);")
    print("  • the n=2 self-energy is a genuine 1-loop diagram ⇒ by universality its π is the")
    print("    loop-integration factor; 8π = 2·(4π) matches the universal 2D heat-kernel norm;")
    print("  • RESIDUAL OPEN: exact reciprocal normalization (2 vs b₁ multiplicity) not derived.")
    print("  No 8π manufactured; no α_k wired; no fit; 1/(8π) stays a phase-4 identification.")

    all_exact = zm_ok and ratio_ok and hk_clean

    wb = WitnessBuilder("alpha-em-pi-decomposition", engine="mpmath")
    wb.set_description(
        "π-decomposition of the α_EM per-loop measure 1/(π b₁)=1/(8π), b₁=dim H¹(M_Bring)=8. "
        "STRUCTURAL probe (scope-(a), NOT a fit/derivation) deciding whether the π is the "
        "UNIVERSAL 1-loop factor or a GEOMETRIC/categorical π, using the ONE proved α_EM "
        "π-template — the photon IR zero-mode δ(1/α)_IR=b₁/Area=8/(12π)=2/(3π) (PhotonIRZeroMode, "
        "PR #2114), whose π is unambiguously the Gauss–Bonnet Area 4π(g−1). Exact finding: the "
        "proved geometric π-home is Area=12π while the self-energy π-home is π·b₁=8π, and they "
        "DIFFER by the pure topological ratio Area/(π·b₁)=2(g−1)/g=3/2 (12π/8π). So the "
        "self-energy π is NOT the proved geometric Area π — the Area reading D=Area/π=12 is the "
        "corpus's 9500σ/−1419 ppb falsification — which EXCLUDES the 'same geometric Area π' "
        "reading. Since the n=2 self-energy is a genuine 1-loop diagram, by universality its π is "
        "the loop-integration factor; among universal 2D constants only the heat-kernel Gaussian "
        "norm (4π)^{d/2}|_{d=2}=4π has the single-π shape, and 8π=2·(4π) (momentum (2π)^2=4π² is "
        "π², Schwinger ∫ds/s is π-free). SUPPORTS the universal-loop reading. RESIDUAL OPEN "
        "(STRICT): the exact bare-π reciprocal normalization is not derived — 8π is compatible "
        "with (4π)·2 [universal×symmetry-2] and (π)·(b₁=8) [loop-π × 8-mode trace], both "
        "universal-loop-family; which multiplicity and why the reciprocal form is the open wall. "
        "No 8π manufactured; no α_k wired; no fit; 1/(8π) stays a phase-4 identification."
    )
    wb.set_content_block("prop:alpha-em-categorical-trace")
    wb.add_data("proved_zero_mode_template", {
        "genus_g": g, "b1_dim_H1": b1,
        "Area_gauss_bonnet": mp.nstr(Area, 16), "Area_as_pi_multiple": "12*pi",
        "zero_mode_b1_over_Area": mp.nstr(zero_mode, 16),
        "closed_form_2_over_3pi": mp.nstr(two_thirds_pi, 16), "match": bool(zm_ok),
        "pi_role": "GEOMETRIC — the Gauss–Bonnet hyperbolic Area 4π(g−1); no loop integration"})
    wb.add_data("pi_home_separation", {
        "self_energy_pi_home_pi_b1": mp.nstr(self_energy_pi_home, 16), "as_pi_multiple": "8*pi",
        "geometric_pi_home_Area": mp.nstr(Area, 16), "as_pi_multiple_2": "12*pi",
        "ratio_Area_over_pi_b1": mp.nstr(area_over_pib1, 16),
        "topological_2_g_minus_1_over_g": mp.nstr(topo_ratio, 16), "match": bool(ratio_ok),
        "reading": "8π ≠ 12π: the self-energy π is a DIFFERENT π from the proved geometric one; "
                   "the Area reading (12π, D=Area/π=12) is the 9500σ/−1419 ppb falsification"})
    wb.add_data("universal_loop_candidates_d2", {
        "heat_kernel_4pi_dhalf_d2": mp.nstr(hk2, 16), "as_pi_multiple": "4*pi",
        "eight_pi_over_heat_kernel": mp.nstr(mult_hk, 12), "clean_times_2": bool(hk_clean),
        "momentum_2pi_d_d2": mp.nstr(mom2, 16), "as_pi_multiple_2": "4*pi^2 (pi-squared, wrong shape)",
        "eight_pi_over_momentum": mp.nstr(mult_mom, 12),
        "schwinger_ds_over_s": "dimensionless (carries no pi)",
        "reading": "only 2D heat-kernel norm 4π has single-π shape; 8π = 2·(4π)"})
    wb.add_data("verdict", {
        "scope": "a", "leaning": "UNIVERSAL 1-loop factor",
        "excluded": "the self-energy π is the SAME geometric Gauss–Bonnet Area π "
                    "(would give 12π=Area, data-falsified at 9500σ/−1419 ppb)",
        "supported": "the self-energy π is the universal 2D heat-kernel loop factor "
                     "(4π)^{d/2}|_{d=2}=4π, with 8π=2·(4π)",
        "residual_open": "exact bare-π reciprocal normalization (2 vs b₁ multiplicity; why the "
                         "reciprocal form) not derived — the open wall",
        "discipline": "no 8π manufactured; no α_k wired; no fit; 1/(8π) stays phase-4"})

    wb.add_assertion("zero_mode_pi_is_geometric_area",
                     computed=1.0 if zm_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="b₁/Area=8/(12π)=2/(3π) exactly (PhotonIRZeroMode): the proved α_EM π "
                            "is the Gauss–Bonnet Area 4π(g−1) — geometric, no loop")
    wb.add_assertion("self_energy_pi_home_differs_from_geometric_by_topology",
                     computed=float(area_over_pib1), expected=1.5, tolerance=1e-9,
                     source="Area/(π·b₁)=12π/8π=2(g−1)/g=3/2: the self-energy π-home (8π) is a "
                            "DIFFERENT π from the proved geometric one (Area=12π), excluding the "
                            "same-geometric-π reading (Area value data-falsified)")
    wb.add_assertion("eight_pi_matches_universal_2d_heat_kernel_factor",
                     computed=float(mult_hk), expected=2.0, tolerance=1e-9,
                     source="8π = 2·(4π), (4π)^{d/2}|_{d=2}=4π the universal 2D heat-kernel loop "
                            "norm; only universal constant of single-π shape (momentum is 4π², "
                            "Schwinger π-free) — supports the universal-loop reading of the π")
    wb.save()
    print("\n  RESULT: the self-energy π is NOT the proved geometric Gauss–Bonnet π; it is")
    print("          structurally the universal 2D 1-loop heat-kernel factor (8π=2·4π).")
    print("          Exact bare-π reciprocal normalization remains the open wall.")
    return 0 if all_exact else 1


if __name__ == "__main__":
    raise SystemExit(main())
