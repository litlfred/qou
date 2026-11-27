# Light-nucleus binding on the γγ chain, read in the mass chart (2026-11-27)

Owner card "Look for the missing γγ piece". Probe:
`computations/probes/gg_binding_mass_chart/gg_binding_mass_chart_probe.py`, 13/13, exact ℚ(q) then mpmath.

## Result

The ruled γγ chain is from `2026-11-22-light-nuclei-a2-a3-gg-chain.md`, with the same block traces and bond factors. The ring framing factor cancels in R = tr_atom/tr_free, for two reasons: the strand count is the same bound and free, and the vertex σᵢσᵢ₊₁⁻¹ has writhe 0.

| nucleus | R | B_log = −E₀ ln R | B_mass = (m_e/U_e)·q∂ ln R | AME / B_mass |
|---|---:|---:|---:|---:|
| ²H | 1.000611 | −2.58 keV | 6.04 keV | 368 |
| ³H | 1.001223 | −5.17 keV | 12.09 keV | 702 |
| ³He | 1.001670 | −7.05 keV | 14.79 keV | 522 |
| ⁴He | 1.002282 | −9.64 keV | 20.83 keV | 1358 |

* The mass chart (the ring energy U = −q∂ log m of PR #9789) turns every cell from unbound to bound. So the γγ bond does bind in the mass chart, with no new choice.
* It is 370 to 1360 times too small, and the ratio grows with A.
* The mirror order is wrong: ³He comes out more bound than ³H.

## Why it is small (structural)

The ruled bond is V³ = γ(0,0,qh)·γ(0,0,−h/q). At h = 0 each factor is the bare photon, which equals 1 (`QOU.StandardModel.photon_bare`). So R(1) = 1 for every word built from γγ bonds, and the binding vanishes at q = 1. The 2026-11-22 audit measures the order as y⁴ (y = q² − 1). That makes B_log of order y⁴ and B_mass of order y³. At q₀, y = 0.232, so y³ ≈ 0.012 and y⁴ ≈ 0.003 of a per-bond unit. With E₀ or m_e/U_e as the unit, the binding stays at the keV scale.

**Consequence.** Adding more bonds of the same kind (all-pairs, or more γγ vertices) cannot reach the MeV scale. They multiply the count but keep the y⁴ suppression. The all-pairs ⁴He cells change B_log only from −0.9 to −1.6 keV. A missing piece that binds ⁴He at MeV scale must survive at q = 1. It must change the closure classically, for instance by changing how many components the closed braid has or how its components link. A γγ bond, which is classically the identity, cannot do this. The per-bond table letter z − h/2 binds at MeV scale precisely because it does not vanish at q = 1: at q = 1 it equals 1/2, so ln 2 per bond.

Scope (a) for the numbers. The suppression argument rests on `photon_bare` and the measured y⁴ order. It is not a Lean theorem about every γγ word.
