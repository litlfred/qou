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

## Update (2026-05-28): GMOR reframe yields a derived candidate

The 71% miss above was an **artifact of targeting the linear ratio**.
The Gell-Mann–Oakes–Renner (GMOR) relation of χPT says the natural
object is the **squared** ratio:

```
m_π² = B(m_u+m_d),  m_K² = B(m_u+m_s)  ⟹  m_K²/m_π² = (m_u+m_s)/(m_u+m_d)
```

Tested against pure q-integer forms (no fitted coefficients):

```
m_K²/m_π² = 12.51121  (measured)
[3]_q · [4]_q          = 12.50867   → 203 ppm, ZERO fitted integers
```

And [3]_q·[4]_q is a **fusion sum** by q-Clebsch-Gordan:

```
[3]_q · [4]_q = [2]_q + [4]_q + [6]_q
(spin-1 ⊗ spin-3/2 = spin-1/2 ⊕ spin-3/2 ⊕ spin-5/2)
```

This is a **derived-candidate**: m_K²/m_π² as a categorical fusion
product, 203 ppm with no rounded-to-fit integers — far cleaner than
the fitted (q⁵−q⁻⁵)(9/5)²(1+4u²) linear formula (3 fitted pieces).

**Still needed for full "derived" status:** a structural argument for
*why* the kaon/pion mass-squared ratio is the spin-1 ⊗ spin-3/2
fusion (the candidate was found by scanning q-integer products). The
residual 203 ppm is not yet a clean q-correction (residual/ℏ² ≈ 0.021,
residual/h² ≈ 0.0046 — neither integer); it is at the NLO-χPT scale.

## Conclusion

The meson sector has a derived *structural* backbone (knot identity,
Frobenius bridge, exact characters), m_π is an independent CAL-3
calibration, and the mass-**squared** ratio m_K²/m_π² is a
**derived-candidate** fusion product [3]_q[4]_q (203 ppm, no fit) —
a genuine improvement over the fitted linear formula. The remaining
work is the structural "why 3⊗4" argument plus the NLO residual.
Until that lands, the exact-precision fitted pieces stay in audit
docs (Category J); the GMOR/fusion candidate is promising enough to
pursue toward paper content.

## Update (2026-05-29): η and φ under the same squared-ratio lens

Extending the GMOR squared-ratio reframe to the other light mesons:

**η (pseudoscalar octet) — derived-candidate modulo η-η′ mixing.**
Gell-Mann–Okubo gives 3m_η² = 4m_K² − m_π², so
```
m_η²/m_π² = (4·[3]_q[4]_q − 1)/3 = 16.345   (measured 15.408, 6.1% miss)
```
The 6.1% gap is the known **η-η′ singlet mixing** — a real physical
effect absent from octet GMO. The octet part is carried by the *same*
[3]_q[4]_q fusion as the kaon. (A direct fusion [2]_q+[4]_q+[6]_q+[3]_q
fits to 0.9%, but that's a scan hit, not GMO-derived.)

**φ (vector meson, s s̄) — GMOR does NOT apply, confirmed.**
The best q-integer fusion misses m_φ²/m_π² by 3.65% (not the
sub-ppm/sub-% precision of the pseudoscalar fusions). φ is a vector
meson, not a pseudoscalar Goldstone, so the chiral-condensate scale
and GMOR/GMO don't govern it — it needs the constituent (vector)
sector. The negative result confirms the GMOR fusion is specific to
the pseudoscalar octet.

Compute: `meson_eta_phi_gmor.py`, `meson-eta-phi-gmor.witness.json`.

## Cross-references

- `meson-spectral-analysis.witness.json` (71% miss evidence)
- `meson_tower_correction_probe.py` (integer-coefficient scan)
- `meson_gmor_derivation_probe.py` (m_K²/m_π² = [3]_q[4]_q fusion)
- `meson_eta_phi_gmor.py` (η GMO octet, φ vector-sector negative)
- `prop:meson-scale-independence` (m_π independence, SDP-validated)
- `2026-05-28-habiro-product-correction-7ppm.md` (parallel fit audit)
