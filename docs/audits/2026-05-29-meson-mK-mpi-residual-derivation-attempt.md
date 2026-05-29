# m_K/m_π 290 ppm residual — derivation attempt (2026-05-29)

## Context

m_K/m_π is the meson mass-ratio observable, at 290 ppm vs a 264 ppb
100× target. (Post-#1416: the dashboard is **2/7** — m_e + m_p — after
the CODATA-fitted ppb-closing towers were removed; the earlier "6/7 /
m_p 0.39 ppQ" was the pre-de-fit state. The m_K/m_π *strong-sector*
analysis below is unaffected by that de-fit.)

The canonical derivation is

    m_K/m_π = χ_{(2,1)}(σ₁⁵) · (V_Seifert(T(2,5))/V_Seifert(T(2,3)))²
            = (q₀⁵ − q₀⁻⁵) · (9/5)²
            ≈ 3.5361   (vs PDG m_K±/m_π± = 3.5371, residual ≈ 290 ppm)

The exponent on the Seifert ratio is **2** (the meson's 2-quark
structure). The residual is equivalently a Seifert-exponent
deviation `δx ≈ 4.93e-4` (i.e. the exact exponent is 2.0005, not 2)
or a multiplicative correction `C = (9/5)^δx − 1 ≈ 2.9e-4`.

Two non-fitting closure paths were tested (per owner direction
"try to derive"). **Neither yields a rigorous derivation.**

## Path 1 — structural Habiro tower: DOES NOT DERIVE

PR #1367 proposed a meson tower `R = 1 + c·u²` with `u = b·ℏ²`,
`b² = (h²+3)/(h²+4)`, and `c ≈ J² = 4`. Tested at 50 dps with the
canonical q₀ = 1.1099785955…:

| quantity | value |
|----------|-------|
| u = b·ℏ² | 0.00851724 |
| C (true residual) | 2.924e-4 |
| **C / u²** | **4.031** |
| C / (4u²) | 1.0077 |

`C/u² = 4.03`, **not** the integer J² = 4 (0.77% off). With a
slightly different q₀ input the same ratio comes out **3.99** — the
q₀-sensitivity itself shows there is no clean integer coefficient.
None of `δx/u` (0.058), `δx/u²` (6.79), `δx/h²` (0.0113),
`δx/ℏ²` (0.050) is a clean rational. The "c ≈ 4" claim is a
0.2–0.8% numerical coincidence, **not** a derivation.

**Conclusion:** wiring `c = 4` (or the `7/8` numerology in
`kaon-pion-ratio-7-8.witness.json`, 318 ppm) into production would
be a coefficient fit — forbidden by the three-calibration
discipline. Do **not** re-introduce a fitted meson tower coefficient.

Source: `meson_habiro_expansion.py` /
`meson-habiro-expansion.witness.json`.

## Path 2 — electromagnetic self-energy: RIGHT SCALE, GENUINE LEAD

The categorical derivation gives the **strong** (QCD/isospin-
symmetric) ratio and legitimately omits electromagnetism. The
charged mesons carry EM/isospin-breaking self-energies:

- π± − π⁰ = 4.59 MeV (essentially pure EM; 33 000 ppm of m_π)
- K± − K⁰ = −3.93 MeV (EM + light-quark-mass)

The 290 ppm residual corresponds to a **≈ 0.14 MeV** shift on the
m_K scale — squarely in the sub-MeV EM/isospin-breaking regime. So
the residual is the **right magnitude** to be the differential EM
self-energy that the strong-only derivation drops.

This is the physically-honest direction, but it is a real
derivation to build, not a quick win: it needs the framework's
α_em (`prop:em-coupling-bring-zero-mode`) fed into a meson EM
self-energy model (Dashen / chiral-perturbation analogue). That
construction does not yet exist in the framework.

## Recommendation

1. m_K/m_π at 290 ppm is the framework's **honest current ceiling**
   for that observable — record it as such, do not fit it.
2. The genuine closure path is the **EM/isospin-breaking
   correction** (Path 2), not an algebraic tower coefficient
   (Path 1, ruled out here).
3. m_K/m_π is the documented open frontier on the meson side; the
   overall dashboard is 2/7 post-#1416 (not 6/7).

## Corroborating merged work (2026-05-29)

- **#1396 (merged) — derived squared-ratio (GMOR reframe).** The
  *linear* m_K/m_π is the wrong target; the derived strong-sector
  leading term is `m_K²/m_π² = [3]_q·[4]_q = [2]_q + [4]_q + [6]_q`
  (203 ppm, **zero fitted integers**), a q-Clebsch–Gordan fusion. So
  Path 1's "linear tower is a fit" is right, and GMOR (squared) is the
  derived object; the residual 203 ppm ≈ the linear 290 ppm is the
  EM/NLO-χPT piece — consistent with Path 2.
- **#1417 — the EM channel is derived.** `crossing-energy-decomposition`
  identifies `sinh(ln q)` as the Coulomb/EM channel
  (`tanh(ln q) ≈ α_EM`). So the EM closure (Path 2) has a concrete
  derived term to build on: feed the framework's α_EM
  (`prop:em-coupling-bring-zero-mode`) through this sinh channel.
