# Audit: meson m_K/m_π is fitted, not a derived character ratio

**Date:** 2026-05-28

## Finding

The lepton mass ratio m_μ/m_e = Vol(4₁)/ℏ² is **derived** (pure
hyperbolic-volume character invariant). The meson mass ratio
m_K/m_π is **NOT** derivable the same way.

| Sector | Ratio | Derived form | Status |
|--------|-------|--------------|--------|
| Lepton | m_μ/m_e = 206.768 | Vol(4₁)/ℏ² | **derived** |
| Meson | m_K/m_π = 3.537 | spectral phase ratio = 1.015 | **71% miss** |

## Evidence

`meson-spectral-analysis.witness.json` records the pure Hecke
character computation:

```
meson_phase = 2.1198,  kaon_phase = 2.1514
spectral_ratio = 1.015
pdg_ratio (m_K/m_π) = 3.537
miss = 71%
```

The exact χ^(std) values ARE derived (χ(L±) = −1 exactly, χ(e⁻) = 0
exactly), but their **ratio does not give the mass ratio**. The
conclusion in that witness: *"Meson mass ratio NOT from spectral
phase ratio. Different mechanism needed."*

## Why the meson ratio is structurally different

The lepton ratio works because the figure-eight 4₁ is the transition
knot between adjacent torus-knot leptons, and its hyperbolic volume
is a clean motivic period. The qq̄ meson operator rotates the V_(2,1)
eigenbasis by ≈π (near-antiparallel, θ≈2.12), not by the small angle
that makes the baryon/lepton small-angle expansion converge. The
antiquark sits in the **dual** representation, flipping χ(L+)=−1.

Per `prop:meson-scale-independence` (SDP-validated): m_π is a genuine
CAL-3 input because it carries chiral-condensate information absent
from (m_e, q₀). The Hopf-link complement has Vol = 0, so there is no
hyperbolic invariant to set the meson scale from the substrate.

## The fitted formula

The best closed form is:
```
m_K/m_π = (q⁵ − q⁻⁵) × (9/5)² × R_meson
```
where R_meson ≈ 1 + 4u² closes the 290 ppm residual to 0.6 ppm. But:

- The `(9/5)²` prefactor is a fitted ratio (torus-knot index guess,
  not derived from character theory).
- `R_meson = 1 + 4u²` is found by an **integer-coefficient scan**
  (`meson_tower_correction_probe.py`: `c_int = round(residual/pk)`),
  the same fitting pattern as the Habiro 1/30, 1/1260 corrections
  (see `2026-05-28-habiro-product-correction-7ppm.md`).

## Derived-vs-fitted accounting for the meson sector

| Component | Status |
|-----------|--------|
| pion = half-figure-eight (σ₁σ₂⁻¹) | **derived** (shared char. poly) |
| Frobenius lepton-meson bridge V_(2,1)↓H₂ | **derived** (Lean) |
| χ^(std)(L±) = −1, χ(e⁻) = 0 exact | **derived** |
| m_π scale (CAL-3) | **calibrated input** |
| m_K/m_π = (q⁵−q⁻⁵)(9/5)²R | **fitted** |
| R_meson = 1+4u², m_η = m_K·q₀ | **fitted** |

## Conclusion

The meson sector has a derived *structural* backbone (knot identity,
Frobenius bridge, exact characters) but the *mass ratio* m_K/m_π is
fitted. Like the Habiro coefficients, the fitted pieces belong in
audit docs only, not in paper content (Category J). The paper's
meson content should state only the derived structure and that m_π
is an independent CAL-3 calibration.

## Cross-references

- `meson-spectral-analysis.witness.json` (71% miss evidence)
- `meson_tower_correction_probe.py` (integer-coefficient scan)
- `prop:meson-scale-independence` (m_π independence, SDP-validated)
- `2026-05-28-habiro-product-correction-7ppm.md` (parallel fit audit)
