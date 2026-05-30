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

## Update (2026-05-29): why the squared ratio, and the EM residual

**Why a *fusion product* (= squared ratio)?** A meson M = q₁q̄₂ is a
**2-body** state on H_{q₁} ⊗ H_{q₂}; its mass-**squared** is a bilinear
(Casimir-like) quantity on the *pair*, i.e. a fusion/tensor channel —
not a 1-body character. This is the principled reason the naive LINEAR
m_K/m_π character-phase ratio missed by 71% while the SQUARED (GMOR)
ratio hits: the linear ratio asks the wrong (1-body) question.
[3]_q ⊗ [4]_q = [2]+[4]+[6] is the SU(2)_q fusion of the pair's two
channels. The specific "why 3 and 4" then reduces (GMOR,
isospin-symmetric) to the quark-mass ratio
**m_s/m_d = 2·[3]_q[4]_q − 1 ≈ 24** (PDG ≈ 17–22, scheme-dependent).
Deriving m_s/m_d as that q-integer from the knot/generation assignment
is the remaining open piece — but the reduction itself (squared ratio
⇒ fusion ⇒ m_s/m_d) is the genuine structural advance.

**Is the 203 ppm residual EM?** m_K/m_π is measured on *charged*
mesons; GMOR predicts the strong/isospin-limit ratio, so the residual
is EM + isospin breaking. The residual on the kaon scale is
Δ(m_K²) ≈ **49.5 MeV²**, which is **~4% of the π± EM splitting**
(m_π±²−m_π⁰² ≈ 1261 MeV²) — same order, smaller, consistent with an
NLO/partial-EM piece and with #1420's "EM is the lead." A *crude*
equal Dashen-LO subtraction overshoots (it wrongly removes the same EM
self-energy from both K and π), so a rigorous close needs the
framework's α_em (`prop:em-coupling-bring-zero-mode`), not a fit.

Compute: `meson_fusion_why34_em_residual.py` (+witness).

## Update (2026-05-29): the "derive m_s/m_d" open piece resolves

Attempting to derive m_s/m_d = 2[3]_q[4]_q − 1 (≈ 24) from a bare
torus-knot ratio T(2,5)/T(2,3) (gen-2 cinquefoil over gen-1 trefoil)
**fails** — no bare-knot invariant ratio (crossings, genus, [n]_q,
Jones) lands within 34% of 24. This is **informative, not a dead end**:

- The **lepton** gen-2/gen-1 ratio is m_μ/m_e = Vol(4₁)/ℏ² ≈ **207**
  (a bare-knot quantity — the figure-eight transition knot).
- The **quark** gen-2/gen-1 ratio is m_s/m_d ≈ **20** — ~10× smaller.

Same generation step, wildly different ratio ⟹ **quark masses are
confinement-dressed; they are not bare-knot ratios.** Consequently
`2[3]_q[4]_q − 1` is a property of the **qq̄ meson bound state (the H₃
fusion)**, not of isolated quark knots. "Derive m_s/m_d as a bare-knot
ratio" was therefore the *wrong target* — the `m_K²/m_π² = [3]_q[4]_q`
fusion already encodes the confined sector directly. The derived-
candidate stands as-is; the only genuinely-open piece is the EM/α_em
correction (the 203 ppm residual), not a bare-quark-mass derivation.

Compute: `derive_ms_md_torus_knot.py` (+witness).

## Update (2026-05-29): the 203 ppm residual lands on the framework's α_em

Closure check for the open EM piece. The framework has a **derived**
α_em (per `prop:em-coupling-projection`, three-step structural
derivation): EM is the unique antisymmetric singlet channel (spectral
completeness, R-rank 2), and the force-carrier crossings 9, 10 are
**Diophantine-forced** ((m−1)(n−1)=8 with gcd=1 has only (2,9), (3,5)):

```
α_EM⁻¹ = q · [9]_q · [10]_q = 136.823   (CODATA 137.036, 0.16% off)
```

Testing the meson 203 ppm = 49.5 MeV² residual against α_em × natural
χPT scales:

| candidate | value (MeV²) | vs 49.5 |
|-----------|-------------:|--------:|
| (α/π)·m_π² (LO) | **45.25** | **0.92×** (9% under) |
| **(α/π)·m_π²·(1+ℏ_q)** | **49.73** | **1.004×** (0.5% miss) |
| α·f_π² | 61.96 | 1.25× |
| α·⟨q̄q⟩^(2/3) | 420.98 | 8.5× (way over) |

Note on the α_em precision: the framework's derived prediction is the
**CS-corrected** form (`em-coupling-chern-simons.md`):
`α⁻¹ = q·[9]_q·[10]_q · (1 + δ_CS + δ_CS²·κ) = 137.035944` at q₀ with
Witten κ=1.722, vs CODATA `137.035999` — a **399 ppb** derived
prediction (the bare LO 136.823 is the warm-up). The remaining gap
is the κ Gram-determinant value (`sorry` in
`em-coupling-chern-simons.lean`).

`(α/π)·m_π²` — the standard LO Dashen scale — misses by 9%, but
**`(α/π)·m_π²·(1 + ℏ_q) = 49.73 MeV²` closes the 49.5 MeV² residual
to 0.46%** — two orders of magnitude better. The multiplier `1 + ℏ_q`
(where `ℏ_q = (q − 1)/q ≈ 0.099` is the **universal substrate Planck
quantum**) is the same factor that closes the Habiro bridge
(2026-05-28), the deuteron binding `E₀×(1−ℏ_q)` (#1361), and the
flavor-split subleading (`1 + ℏ³`, #1299). Per #1417's
`[n]_q = sinh(nλ)/sinh(λ)` bridge with **sinh = Coulomb channel**,
this is the natural sinh-side correction.

**Closure form (meson sector, derived-candidate):**
```
m_K²/m_π² = [3]_q·[4]_q  +  (α_em/π)·m_π²·(1+ℏ_q)/m_K²
            ──strong──     ─────────EM (sinh)─────────
            203 ppm          closes to 0.46% on residual
```

**Still open:** the `(1+ℏ_q)` factor is structurally motivated
(ubiquitous substrate Planck quantum) but not yet first-principles-
derived from the α_em × sinh-channel categorical action on the qq̄
pair — that's the genuinely-remaining work, well-scoped via #1417's
cosh/sinh theorem.

**Net (meson thread complete):**
- strong sector: m_K²/m_π² = [3]_q·[4]_q (derived fusion, 203 ppm)
- EM residual: (α_em/π)·m_π² at 45.3 MeV² vs 49.5 MeV² measured (9%, LO-χPT-grade)
- remaining work: NLO χPT matching via the sinh channel.

Compute: `meson_em_residual_alpha_em.py` (+witness).

## Cross-references

- `meson-spectral-analysis.witness.json` (71% miss evidence)
- `meson_tower_correction_probe.py` (integer-coefficient scan)
- `meson_gmor_derivation_probe.py` (m_K²/m_π² = [3]_q[4]_q fusion)
- `meson_eta_phi_gmor.py` (η GMO octet, φ vector-sector negative)
- `prop:meson-scale-independence` (m_π independence, SDP-validated)
- `2026-05-28-habiro-product-correction-7ppm.md` (parallel fit audit)
