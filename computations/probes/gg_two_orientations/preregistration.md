# Pre-registration — γγ words with both pair orientations

Owner 2026-11-15: "no γγ neutron ... we are missing something."

What forced "every γγ word on 3 strands is a power of V": `GammaGammaWordSelection.lean` defines the vertex as
σᵢσᵢ₊₁⁻¹ only — photon on the lower pair, anti-photon on the upper pair. The other orientation, σᵢ⁻¹σᵢ₊₁ = V̄
(photon on the upper pair), is equally a pair-production event, has writhe 0, even length and alternating character 1,
and is not included. Which orientation a photon letter has is listed as not derived (bean qou-qs1x).

Hypothesis (labelled, not adopted): γγ words are products of V = σ₀σ₁⁻¹ and V̄ = σ₀⁻¹σ₁ on 3 strands.
Then words differ by an orientation pattern, which could carry flavour.

Measure: every word in {V, V̄}^m, m = 1..6 (126 words); reading 3 at levels 1–3 alone, convention D, proton q₀,
mpmath. Also the one-photon sign ΔR of `photon_electron` for each passing word.

Derived before computing: Vᵐ and V̄ᵐ pass alone iff m ≡ 0 mod 3 (from gg_symmetry). Mixed words are new.
Outcome (i): some mixed words pass alone, giving distinct passing nucleon candidates with the same length → report them
and their ΔR. Outcome (ii): no mixed word passes. Nothing is adopted, selected or wired; changing the γγ definition is
the owner's call.
