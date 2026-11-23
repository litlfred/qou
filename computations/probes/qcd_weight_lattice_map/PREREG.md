# PREREG — helon twist lattice vs our gl₃ weight map (issue #9096)

Written and pushed before the probe exists. Exact arithmetic only (sympy, ℚ and ℚ(√2,√3)); no float, no `q₀`.

## Source, and a provenance caveat

Chester, Arsiwalla, Kauffman, *Preons, Braid Topology, and Representations of Fundamental
Particles*, arXiv:2501.03260v1 ("CAK"). **The paper is NOT held in `library/`** (no
`library/arxiv-2501.03260v1/` on `main` or on this branch; measured 2026-11-22). It was read from
the arXiv HTML page through a summarising fetch, twice, the second pass to check tables. Every
number below is therefore a transcription of a summary, not of the PDF. The probe states each
CAK datum it uses so that a reader with the paper can check it line by line.

What is used from CAK:

- **§2.1–2.2** helon rules: three ribbons, per-ribbon twist in {+1, 0, −1}, no mixed signs in one
  braid; "fifteen different charges" from the patterns (000), (00±), (0±0), (±00), (0±±), (±0±),
  (±±±) plus one pattern printed as a second (±0±), read here as the typo for (±±0).
- **§3, Table 1** Lambek 4-vectors `F + aᵢ i + a_j j + a_k k`: e⁻ = 1−i−j−k, ν = 1,
  u_r = 1+j+k, u_b = 1+i+k, u_g = 1+i+j, d_r = 1−i, d_b = 1−j, d_g = 1−k, antiparticles negated;
  p⁺ = 3+i+j+k, n = 3. §3.1 Eq. (4): τ(𝒟) = F + t₁i + t₂j + t₃k.
- **§6, Eqs. (31)–(34)** weights on A₂ ⊕ A₁ written (w₁, w₂, Q); **Eq. (35)** matrix M mapping
  weight coordinates to twist coordinates; **Table 2** 5-vectors (x, y, r, g, b).

## Our candidate map

Corpus pieces: `strand-twist-datum` (free per-strand integer twist `tᵢ`, `Q_twist = T/3`);
position colour **K0** (`qcd_colour_action`, PR #9059: colour is a position label the braid does
not move); the convention-D residual `U_q(gl₂) × U(1)` with `U(1) = N₃` (`qcd_d_residual_symmetry`,
PR #9059); `U_q(gl₃)` weights on `(ℂ³)^⊗n`.

Map Φ: a three-position twist vector `t = (t₁, t₂, t₃)`, position `c` = colour `c`, goes to the
gl₃ weight `λ = Σ_c t_c ε_c`. Its sl₃ part is `μ = t − (T/3)(1,1,1)`; its centre value is
`T = t₁+t₂+t₃`; the charge candidate is `Q = T/3`; the raw D-residual charge is `N₃ = t₃`, its
traceless form `⟨λ, diag(1,1,−2)⟩`.

This is a choice (colour = position, twist = weight coordinate), not a derivation. It is the map
whose consistency is tested.

## Agreement criterion, state by state

For each first-generation fermion and antifermion (ν, e, u_{r,g,b}, d_{r,g,b} and bars), Φ agrees
with CAK iff **one** linear map L, fixed across all states, sends `(μ, Q)` to the CAK weight
`(w₁, w₂, Q)` of Eqs. (31)–(34) and to the Lambek vector, and the charges coincide. A per-state
fix is a disagreement.

## Pre-registered checks and predictions

| id | check | prediction |
|---|---|---|
| P1 | `M` invertible; `M·(w,Q)` gives the CAK twist vectors; column sums give `T = 3Q` | PASS |
| P2 | a single L (derived from `M⁻¹`) maps Φ's `μ` to CAK `(w₁,w₂)` for all states | PASS |
| P3 | Lambek: `Q = (aᵢ+a_j+a_k)/3`; the literal "the three sum to the charge" | first PASS, second FAIL (sum = 3Q) |
| P4 | the 15 twist vectors are exactly the weights of `Λ^•ℂ³ ⊕ Λ^•(ℂ³)*`, centre `±k` on `Λ^k` | PASS |
| P5 | colour multiplets: u and d triplets in one sl₃ rep, ū and d̄ in the conjugate, leptons singlets | PASS |
| P6 | Q linear in `(μ, raw N₃)`: `Q = N₃ − μ₃`; traceless `N₃` is not a function of (Q, Y) and Q is not a function of traceless `N₃` | PASS (both) |
| P7 | on `(ℂ³)^⊗n` the centre is `n`, constant; twist vectors have `T ∈ {−3,…,3}` and negative entries, so they are not weights of any single `(ℂ³)^⊗n` | PASS |
| P8 | the `N₃ = 0` (D-visible) sector of Φ excludes the electron | PASS |
| P9 | Y is not a function of the twist vector (chirality needed) | PASS |
| P10 | corpus electron σ₀σ₁σ₀ vs CAK e braid σ₁⁻¹σ₂: permutation, closure components, writhe | DIFFER |
| P11 | up quark = one unknot strand with `Q = t/3`: `Q = 2/3` needs `t = 2`, whose colour weight `2ε_c` is in `S²ℂ³` (the 6), not a triplet | conflict |
| P12 | proton uud as three strands at positions r, g, b: colour singlet iff `t₁=t₂=t₃`, so uud is not a singlet; CAK's three-braid sum is `(1,1,1)` | conflict |

A FAIL against a prediction is kept as a FAIL and reported. No check is tuned after the run.
