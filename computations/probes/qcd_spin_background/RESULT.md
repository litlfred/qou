# RESULT: spin or background-field object for the β₀ sign

Bean `qou-bwwr`, routed to `qou-ni4b`. Pre-registration
`PREREGISTRATION-spin-background.md` (commit `0415291e97a`, pushed before any code).
Probe `qcd_spin_background_probe.py`, output `qcd_spin_background_probe.out.json`, commit
`4a21dae23ee`. **39/39 checks**: 35 pre-registered and 4 post-hoc, labelled as such. Exact
sympy over ℚ(q). mpmath is used only for display at the proton pin q₀ = 1.10997858275138….

## Claim

**MISS on S1, S2 and S3 (scope (a): not found in the searched class).** The searched class
contains no term that splits into a paramagnetic (2s)² piece and a separate N-independent
diamagnetic piece of opposite sign. Nothing gives an antiscreening sign without a sign
convention being chosen.

**The object.** The probe uses a background colour holonomy K(ε) = diag(e^{εa}) with a
traceless direction a. Acting as K^{⊗n}, it commutes with the Jimbo braiding. The
susceptibility is

χ(X) = [ε²] Tr(K^{⊗n} X) / [ε²] Tr_V K,

in units of the fundamental. For every word, χ(X) does not depend on the Cartan direction
chosen.

| | construction | exact result | verdict |
|---|---|---|---|
| S3 | χ of the N = 3 words, n = 3 | at q = 1, χ = Σ ℓᵢ² N^{#cycles−1}: 27 for 1, V³ and Δ²; 9 for σ₀σ₁ and the photon σ₀σ₁⁻¹; 15 for the electron σ₀σ₁σ₀. A strand cycle of length ℓ couples like charge ℓ. | ℓ² is a winding number, not a spin. No diamagnetic term. |
| S3 | adjoint channel P₍₂,₁₎ (rank 16) | χ_adj: 1 → 12; σ₀σ₁ → −6; photon → −6(q²−1+q⁻²) = −6 − 24ħ²; V³ → 12 at q = 1 (11.965 at q₀); electron → **0** at every q; Δ² → 12 | the sign of −6 is the 3-cycle character. No (2s)² − 1/3 structure. |
| S3 | heat kernel: per-state χ under e^{−tΔ_ξ} | 1 at t = 0, falling to **12/17** as t → ∞. The tie μ₍₂,₁₎ = μ₍₁³₎ = [2] sets the limit. d/dt at t = 0 is −5(q²+1)(q²−q+1)(q²+q+1)/(27q³) = −1.1334 at q₀. | The value falls. A real background reads this as screening and a unitary background (iε) reads it as antiscreening. **The convention decides the sign, not the construction.** |
| S2 | Hecke sign as (−1)^{2s}, n = 2 | χ(σ) = q(N+2) − q⁻¹(N−2). The q = 1 ratio χ(σ)/χ(1) = **2/N**: 1, 2/3, 1/2 at N = 2, 3, 4. | Depends on N. The value 2/3 = (2·½)² − 1/3 at N = 3 is the coincidence declared before the probe ran. |
| S1 | full twist Δ² as the spin label, n = 2 | χ(Δ²) = 2N + 8ħ + 4Nħ². The sl-framed form at N = 3 is 6 + 4ħ + 8ħ². The exponent of σ^{sl} on Sym² is 1 − 1/N. | Every coefficient is positive. The only negative constant is the framing shift −1/N. It depends on N, so it is not the Nielsen–Hughes −1/3. |

Post-hoc result (not pre-registered). The photon letter σ₀σ₁⁻¹ is the only word with a
negative ħ² term. Its ħ¹ term is 0 for N = 2, 3, 4, because the letter has writhe 0. Its ħ²
coefficient is −4, −24, −52 for N = 2, 3, 4, which is −4(N² − 3). This coefficient depends
on N, so it is not a fixed diamagnetic constant. At N = 3 all of it sits in the adjoint
channel. Recorded as an observation only.

## Corpus-grep (six paths, plus the corpus_search CLI)

- The corpus contains no background-field, Euler–Heisenberg or Nielsen–Hughes object.
- `library/` holds no Nielsen–Hughes source.
- `QOU/Hecke/TwistedChannelSplitting.lean` states that a twist acting on spin but not on
  colour is not derived anywhere. In one ribbon category the twist acts on every object.
  This is the structural reason S1 fails: in qou the twist label is the colour content
  ct(λ), not a separate spin.

## Implications

1. A qou construction from colour data alone, meaning braids on (C^N)^{⊗n}, a twist, a
   Hecke sign or a holonomy, gives either sign-definite susceptibilities or constants that
   depend on N. The 11/3 : −1/3 split needs a second factor that is not colour: a spin,
   helicity or orbital label. That requirement is exactly the open hypothesis θ_I = 1 in
   `TwistedChannelSplitting`. That hypothesis is the concrete thing for `qou-ni4b` to
   supply.
2. The N = 3 coincidences 2/N = 2/3 and 1 − 1/N = 2/3 are traps. Each equals
   (2·½)² − 1/3 at N = 3 only. Do not cite them.

## Not established

- A construction that has a separate spin factor. The corpus has none, so none was built.
- n > 3, the adjoint carried as V⊗V̄, and heat operators other than Δ_ξ.
- Whether ħ = log q is an RG scale (bean `qou-abzr`).
- No gluon is identified or selected. Step 4 of def:derived-atom stays open.
