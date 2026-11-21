# Pre-registration: the lepton pair e⁻ ⊔ ν̄ from γγ production (issue #8833)

Written before the probe in this directory is run. Owner, 2026-11-21: *"Resolve the
anti-neutrino by checking the gamma gamma production to get there."*

## Inputs (rulings, none chosen here)

* γγ word: a product of vertices σᵢσᵢ₊₁⁻¹ (`GammaGammaWord`, `QOU/Mass/GammaGammaWordSelection`).
* Electron: σ₀σ₁σ₀, closure the Hopf link (lk = +1). Antineutrino: the unknot.
* Target link: Hopf ⊔ unknot, three components.

## Lean first

`QOU/QBeta/GammaGammaLeptonPair.lean`: a γγ word on n strands closes to c components with
n + c even. So e⁻ ⊔ ν̄ needs an odd number of strands; four strands is excluded.

## The closed family

All γγ words on 3 and on 5 strands, products of 1..6 vertices (vertices i = 0 on 3 strands;
i = 0, 1, 2 on 5 strands). For each word:

1. closure components (cycles of the strand permutation);
2. pairwise linking numbers and per-component self-crossing counts;
3. for words with three components and linking pattern {±1, 0, 0}: the framing-corrected
   quantum invariant Ĩ = q^(−2·writhe)·Tr(K^{⊗n} ρ(w)) (Jimbo R-matrix, K = diag(q, q⁻¹)),
   compared exactly at q = 2 and q = 3 with Hopf ⊔ unknot (σ₀σ₁σ₀ ⊗ 1) and its mirror.

Agreement at two rational points is evidence, not a proof of isotopy; it is reported as such.

## What is reported

* the smallest vertex count at which a γγ word's closure matches e⁻ ⊔ ν̄ (or its mirror), on
  3 and on 5 strands, or that none does up to six vertices;
* every matching word. None is selected or scored, and no Q_β value is computed here.
