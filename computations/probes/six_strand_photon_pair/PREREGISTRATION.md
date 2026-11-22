# Pre-registration: the γγ lepton pair on six strands, photon by photon

Written before the probe in this directory is run.

## Inputs (rulings; none chosen here)

* Photon: γ(a, b, c) = 1 + a·σ₀ + b·σ₁ + c·σ₀σ₁⁻¹ (`def:photon`, ruled 2026-11-20).
* Placement on six strands (owner card, 2026-11-22, "1 Sliding photon at each i"):
  γᵢ(a, b, c) = 1 + a·σᵢ + b·σᵢ₊₁ + c·σᵢσᵢ₊₁⁻¹, i = 0…3 (σ₀…σ₄ exist on six strands). The larger letter is inverted
  at every position (owner card 2026-11-22, "A plus right-hand closure").
* Bare γγ vertex: Vᵢ = σᵢσᵢ₊₁⁻¹ = γᵢ(0, 0, 1).
* Target link (owner card 2026-11-21, "3. Extra loop, 6 strands"): e⁻ ⊔ ν̄ ⊔ loop, i.e.
  Hopf link (lk = +1, the electron σ₀σ₁σ₀) ⊔ unknot ⊔ unknot, four components.

## Part 1: which vertex words close to the target

All words Vᵢ₁…Vᵢₘ on six strands, i ∈ {0,…,3}, m = 1…6. For each: components, pairwise
linking, self-crossing counts. For four components with linking pattern {1,0,0,0,0,0}:
the framing-corrected invariant Ĩ = q^(−2·writhe)·Tr(K^{⊗6} ρ(w)) (Jimbo R, K = diag(q, q⁻¹)),
compared exactly at q = 2 and q = 3 with Hopf ⊔ 2 unknots (σ₀σ₁σ₀ on 5 strands) and its
mirror. Two-point agreement is evidence of isotopy, not proof.

Also reported, descriptively: (i) that no target word is whole-word linking-neutral (the
Hopf pair has lk = 1); (ii) the trace restricted to the zero-charge K-weight sector
(three up, three down), at q = 2, 3, for the minimal matches.

## Part 2: how many photons does a minimal match need

For each match of the smallest vertex count m:

* Full Hecke algebra H₆(q): expand ρ(w) in the standard basis T_π and record its longest
  term. A product of k photons only reaches length 2k, so k ≥ ⌈ℓ_max/2⌉.
* Temperley–Lieb quotient (the Jimbo representation on (C²)^⊗6, faithful on TL₆ for generic
  q): solve μ·ρ(w) = γᵢ(a,b,c)·γⱼ(a′,b′,c′) for every ordered pair (i, j), exactly at
  q = 2 and q = 3 (Gröbner basis over ℚ), unknowns μ, a, b, c, a′, b′, c′.

## What is reported

The smallest vertex count; every matching word at that count; the full-H₆ lower bound on the
photon count; and every (i, j) at which a two-photon TL factorisation exists, with its
weights. Nothing is selected or scored. No Q_β value is computed.
