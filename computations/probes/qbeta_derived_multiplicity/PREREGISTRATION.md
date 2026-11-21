# Pre-registration: a derived multiplicity on the scored Q_β cell (2026-11-21)

Owner choice (card, 2026-11-21 12:30): route 1, "derived multiplicity". PR #8836, issue #8833.

## Why this is the only route left on this branch

`QOU/QBeta/PhotonVertexEigenphase.lean` (sorry-free) proves:
- every member of the γγ tower gives |1 + tr V^{3k}| ≤ 3;
- so every member, and every average over the tower whose weights sum to 1, gives
  Q_β ≤ 3h·E₀/[2]³ = 0.32607 MeV.

The scored cell is Q_β = |ε_flavour(V³)|·E₀ = 0.325434 MeV. Reaching it would need a factor of
2.404, and only a weight with total mass above 1 could supply that: a multiplicity m multiplying ε.

## Rule, fixed before any multiplied number is computed

1. A candidate m qualifies only if a corpus artifact (Lean theorem, content block, ruling) fixes
   it **without reference to Q_β**. The artifact is named below.
2. Every qualifying m is computed and reported: Q_β(m) = m·0.325434 MeV and its residual.
3. **None is selected.** Proximity to CODATA is not evidence (AGENTS.md §NO FITTING). This probe
   does not wire, score or adopt anything.
4. Candidates are listed in the table below, before any computation. None will be added after.

| id | m | what it counts | corpus source |
|---|---|---|---|
| M1 | 2 | ordered photon pairs whose product is V³: γ(0,0,qh)·γ(0,0,−q⁻¹h) and the reversed order (both factors are polynomials in V, so they commute) | `borromean-two-photon-factorisation`; `borromeanV3A_eq_switched_photon_product` |
| ~~M2~~ | — | **withdrawn before computing.** `borromeanV3A` / `borromeanV3B` are the same word V³ restricted to W_p and W_n, not two presentations; both are already inside ε_flavour. | `BorromeanRingColouredTrace.lean` lines 139-152 |
| M3 | 2 | V³ and its inverse V⁻³, with the same weight-space trace | `FlavourWeightSplit.trace_inv_V3A` |
| M4 | 4 | the orbit {V³, V⁻³, mirror, mirror⁻¹} under inverse and antipode | `trace_inv_V3A`, `trace_mirror_V3A` |
| M5 | 3 | the number of quark strands, i.e. colour labels in H₃ | three-strand nucleon word, `atom_braid_word_3A` |
| M6 | 1 | colour-singlet multiplicity of the three-quark state | singlet in V^{⊗3} |
| M7 | [2]_q | quantum dimension of the doublet V | U_q(sl₂) |
| M8 | [3]_q | quantum dimension of the spin-1 summand | U_q(sl₂) |

**Flag on M3 and M4.** The 2026-11-20 ruling makes σ₀σ₁⁻¹ the only fourth photon term. So V⁻¹ and the mirror words are not γγ products. The corpus fixes their traces, but they fail the γγ construction rule (bean `qou-ales`). They are reported anyway, with that flag.

The [2]³ normalisation is not a candidate, because ruling D1 fixes it.

**Contamination, stated plainly.** The needed factor 2.404 is already known, and so are the
values 2·0.3254 = 0.651 and 3·0.3254 = 0.976. So this is not blind. What makes it a
pre-registration is that the list is closed before the table is computed, and that nothing will
be selected from it.
