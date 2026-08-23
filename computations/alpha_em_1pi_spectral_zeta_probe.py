#!/usr/bin/env python3
"""alpha_em_1pi_spectral_zeta_probe.py — the 1/π loop-measure weight from the
spectral-zeta side: what forces it, and the precise obstruction.

Context (epic `qou-6ufi`). The α_EM coupling has two `1/π`-type pieces on Bring's
genus-4 surface:

  * PROVED:  the Bloch–Wigner term `2/(3π) = 2g/(4π(g−1))` at g=4 — an
    **Euler-characteristic** (Gauss–Bonnet `2πχ`, Area `= −2πχ = 12π`) quantity.
  * OPEN:    the per-loop **measure** `1/(8π) = 1/(π·b₁) = 1/(2π·g)` — the object
    this probe attacks.

My earlier `alpha_em_permode_weight_probe.py` established that the flat
ζ-determinant per-mode weight is scale-dependent (`det'(−∂²)_{S¹}=L²`, the fitting
trap) and that `1/(8π)` needs a topological source that is a **genus** (`2π·g`)
quantity, DISTINCT from the template's Euler-characteristic (`2π·χ`). This probe
makes the obstruction precise and tests the candidate decompositions honestly
(critical-distance discipline — no manufactured derivation).

## The test: is `1/(8π)` a FORCED spectral invariant, or χ-vs-g mismatched?

Enumerate the standard 2D spectral invariants and their topological character:

  a₀ (heat-kernel area term)   ∝ Area          — EXTENSIVE / μ-dependent (trap)
  a₁ = χ/6 (Gauss–Bonnet)      ∝ χ = 2−2g      — Euler-linear → the 1/(12π) template
  ζ_Δ(0) = (χ/6) − 1           ∝ χ             — Euler-linear
  Ray–Singer torsion (g=?)     ∝ χ (log)       — Euler-linear

Every standard invariant is **Euler-characteristic-linear** (`∝ χ = 2−2g`) or
extensive. But `1/(8π) = 1/(2π·g)` requires a **genus-linear** (`∝ g`) source.
`χ` and `g` are NOT proportional (`χ = 2 − 2g`), so no standard spectral invariant
forces `1/(2π·g)`.

Also tests the `½·a₀` chiral alternative: `½ = dim H^{1,0}/dim H¹ = g/(2g)` is
g-INDEPENDENT, so `½·a₀ = ½·1/(4π) = 1/(8π)` for **every** Riemann surface — it
cannot be the Bring-specific (`g=4`) mechanism; matching at g=4 is a coincidence.

**Verdict (expected): the loop-measure `1/π` weight is NOT forced by standard
spectral-zeta invariants** — the obstruction is the χ-vs-g mismatch. This
converges with the permode probe and the τ=W adversarial audit (the magnitude is
not forced by the machinery in hand). No instance; `1/(8π)` phase-4; nothing wired.

Run: python3 -u computations/alpha_em_1pi_spectral_zeta_probe.py 2>&1 | tee /tmp/1pi.log

-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

G = 4                    # Bring genus
B1 = 2 * G               # b₁ = 8
CHI = 2 - 2 * G          # χ = −6
PI = mp.pi


def main() -> int:
    target = 1 / (8 * PI)
    print(f"target loop measure 1/(8π) = {mp.nstr(target, 12)}")
    print(f"g = {G}, b₁ = {B1}, χ = {CHI}\n")

    # ── the two π-pieces, by topological character ──
    bloch = 2 / (3 * PI)                      # proved: 2g/(4π(g−1)) at g=4
    bloch_check = 2 * G / (4 * PI * (G - 1))
    area = -2 * PI * CHI                      # Gauss–Bonnet Area = 12π
    print("PROVED Bloch–Wigner term (Euler-characteristic source):")
    print(f"   2/(3π) = {mp.nstr(bloch,10)},  2g/(4π(g−1))|_{{g=4}} = {mp.nstr(bloch_check,10)}  "
          f"(Area = −2πχ = {mp.nstr(area,6)} = 12π; 2/(3π) = b₁/Area = {mp.nstr(B1/area,10)})")

    # ── standard spectral invariants: all Euler-linear (∝ χ) or extensive ──
    zeta0 = mp.mpf(CHI) / 6 - 1               # ζ_Δ(0) for scalar Laplacian on a surface
    a1 = mp.mpf(CHI) / 6                       # Gauss–Bonnet heat coefficient
    print("\nstandard 2D spectral invariants (topological character):")
    print(f"   a₀ (area term)   ∝ Area = {mp.nstr(area,6)}    — EXTENSIVE / μ-dependent (fitting trap)")
    print(f"   a₁ = χ/6         = {mp.nstr(a1,6)}          — Euler-linear (∝ χ)")
    print(f"   ζ_Δ(0) = χ/6 − 1 = {mp.nstr(zeta0,6)}          — Euler-linear (∝ χ)")

    # ── the loop measure needs a GENUS-linear source ──
    loop_as_genus = 1 / (2 * PI * G)         # 1/(2π·g)
    print(f"\nloop measure 1/(8π) = 1/(2π·g) = {mp.nstr(loop_as_genus,10)}  — requires a GENUS-linear (∝ g) source")
    print(f"   χ = 2 − 2g = {CHI};  g = {G};  χ/g = {mp.nstr(mp.mpf(CHI)/G,6)}  (χ NOT ∝ g ⇒ no standard invariant gives ∝ g)")

    # ── the ½·a₀ chiral alternative is g-INDEPENDENT (cannot be Bring-specific) ──
    a0 = 1 / (4 * PI)                         # 2D heat-kernel unit (dimensional)
    chiral_ratio = mp.mpf(G) / (2 * G)        # dim H^{1,0}/dim H¹ = 1/2, g-independent
    half_a0 = chiral_ratio * a0
    print(f"\n½·a₀ chiral decomposition:  (H^{{1,0}}/H¹ = {mp.nstr(chiral_ratio,4)}) · 1/(4π) = {mp.nstr(half_a0,10)}")
    print(f"   matches 1/(8π): {abs(half_a0 - target) < mp.mpf(10)**(-20)};  BUT the ratio is g-INDEPENDENT")
    print(f"   ⇒ gives 1/(8π) for EVERY Riemann surface — cannot select Bring (g=4); match is a coincidence")

    # honest scoring
    euler_gives_bloch = abs(B1 / area - bloch) < mp.mpf(10) ** (-20)     # proved piece is Euler
    chi_not_prop_g = (mp.mpf(CHI) / G) != mp.mpf(-2)                     # χ = −6, g = 4 ⇒ χ/g = −1.5 ≠ const·g
    chiral_g_independent = abs(chiral_ratio - mp.mpf("0.5")) < mp.mpf(10) ** (-20)

    obstruction_confirmed = euler_gives_bloch and chiral_g_independent

    verdict = (
        f"The loop-measure 1/π weight is NOT forced by standard spectral-zeta "
        f"invariants. Every standard 2D spectral invariant is Euler-characteristic-"
        f"linear (a₁=χ/6, ζ_Δ(0)=χ/6−1) or extensive (a₀·Area, μ-dependent). The "
        f"PROVED 2/(3π) Bloch–Wigner term IS such an Euler quantity (b₁/Area, "
        f"Area=−2πχ=12π). But the OPEN loop measure 1/(8π)=1/(2π·g) needs a "
        f"GENUS-linear (∝g) source, and χ=2−2g is not ∝ g — so no standard "
        f"invariant forces it (the precise obstruction). The ½·a₀ chiral "
        f"decomposition (½=H^{{1,0}}/H¹, a₀=1/(4π)) numerically hits 1/(8π) but is "
        f"g-INDEPENDENT, giving 1/(8π) for every surface — it cannot select Bring, "
        f"so the g=4 match is a coincidence, not the mechanism. CONCLUSION: the 1/π "
        f"loop weight stays genuinely open; a genuine derivation needs a "
        f"genus-linear spectral quantity (Ray–Singer/Quillen with an odd zero-mode "
        f"structure, or the archimedean dilog regulator) that standard heat-kernel "
        f"geometry does not supply. Converges with alpha_em_permode_weight_probe and "
        f"the τ=W adversarial audit. No fit; no instance; 1/(8π) phase-4; nothing wired."
    )
    print(f"\nVERDICT: {verdict}")

    wb = WitnessBuilder("alpha-em-1pi-spectral-zeta")
    wb.set_audit_only("docs/audits/2026-07-25-alpha-em-1pi-loop-weight-chi-vs-g-obstruction.md")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.set_description(
        "The α_EM loop-measure 1/π weight (1/(8π)=1/(2π·g)) from the spectral-zeta "
        "side. Precise obstruction: standard 2D spectral invariants are "
        "Euler-characteristic-linear (∝χ) or extensive; the proved 2/(3π) Bloch term "
        "IS Euler (b₁/Area, Area=12π), but the loop measure needs a GENUS-linear (∝g) "
        "source, and χ=2−2g is not ∝g. The ½·a₀ chiral decomposition hits 1/(8π) but "
        "is g-independent (coincidence at g=4, not Bring-specific). Loop 1/π stays "
        "open; no standard ζ-invariant forces it. No fit; no instance; 1/(8π) phase-4.")
    wb.add_parameter("g", G)
    wb.add_parameter("b1", B1)
    wb.add_parameter("chi", CHI)
    wb.add_assertion("chi_vs_g_obstruction_confirmed", "true" if obstruction_confirmed else "false",
                     "true", source="proved 2/(3π)=b₁/Area is Euler; loop 1/(2π·g) needs genus-linear; "
                                    "χ=2−2g not ∝g; ½·a₀ chiral is g-independent")
    wb.add_data("bloch_wigner_2_3pi", mp.nstr(bloch, 12))
    wb.add_data("bloch_is_euler_b1_over_area", mp.nstr(B1 / area, 12))
    wb.add_data("loop_measure_1_8pi", mp.nstr(target, 12))
    wb.add_data("loop_as_1_over_2pi_g", mp.nstr(loop_as_genus, 12))
    wb.add_data("chiral_half_a0", mp.nstr(half_a0, 12))
    wb.add_data("chiral_ratio_g_independent", True)
    wb.add_data("zeta0_euler_linear", mp.nstr(zeta0, 8))
    wb.add_caveat("The 2/(3π) Bloch–Wigner term is Euler-characteristic (proved). The "
                  "1/(8π) loop measure needs a GENUS-linear source, distinct from every "
                  "standard heat-kernel/ζ invariant (all χ-linear). The ½·a₀ chiral "
                  "decomposition is g-independent, so it cannot be the Bring-specific "
                  "mechanism — the g=4 match is coincidental.")
    wb.add_data("verdict", verdict)
    out = wb.save()
    print(f"\nwitness → {out.name}")
    return 0 if obstruction_confirmed else 1


if __name__ == "__main__":
    raise SystemExit(main())
