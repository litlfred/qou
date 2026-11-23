# Pre-registration: Gröbner–Shirshov reduction of the γγ lepton pair word (W5)

Written 2026-11-23, before any probe or Lean file in this directory exists. The predictions
below come from reducing the words by hand while writing this file. The probe and the Lean
files check them. Nothing is selected or scored against a measured value.

Photon (owner ruling 2026-11-20): γᵢ(φ₀, φ₁, φ₀₁) = 1 + φ₀σᵢ + φ₁σᵢ₊₁ + φ₀₁σᵢσᵢ₊₁⁻¹. The
vertex letter is Vᵢ = σᵢσᵢ₊₁⁻¹.

## The question (from the L2 1-ppQ plan, row W5)

1. Which word is the decay element: the unreduced γγ word or its reduced form?
2. What does that make the cell 2E₀·ln q ≈ 0.8735 MeV: Q_β, m_n − m_p, or neither?
3. Does any term survive at q = 1? `QBetaErrorBudget.lean` proves R(q) ≤ 3/4 for q ≥ 1, so a
   repair factor of about 2.04 must survive at q = 1.

## Closed family

The nine words that carry a two-photon factorisation in some cell, on six strands
(`PhotonPairIdleFactor.lean`, `PhotonPairNoFactorSector.lean`, the 19 factorising cells):

- three vertices: V₀V₁V₀, V₁V₂V₁, V₂V₃V₂;
- five vertices: V₀V₁V₂V₀V₃, V₀V₁V₂V₃V₀, V₂V₀V₃V₁V₀, V₂V₃V₀V₁V₀, V₀V₁V₀V₁V₂, V₁V₂V₁V₂V₃.

No other word is added after the run.

## Quantities

- **G1, the element.** Whether the reduction uses only the group relations σᵢσᵢ⁻¹ = 1 and
  far commutation σᵢσⱼ = σⱼσᵢ (|i − j| ≥ 2), or also the Hecke quadratic relation.
- **G2, the cancellation excess.** e(w) = (ℓ(w) − ℓ_min(w))/2, where ℓ is the letter count
  and ℓ_min the shortest word for the same braid. ℓ_min is bounded below by the signed crossing
  matrix c_{ab}(w): the signed number of crossings between strands a and b. It is unchanged by
  every braid relation, and it changes by ±1 in one entry per letter, so ℓ(w) ≥ Σ_{a<b} |c_{ab}|.
- **G3, the cell.** Whether the reduction alone can assign 2E₀·ln q.

## Predictions

**G1.** Every reduction uses group relations only. So the unreduced and reduced words are the
same element of the braid group B₆. Every trace, module action and energy evaluated on them
agrees for every q, including q = 1. Their difference is 0, so no term of that difference
survives at q = 1.

**G2.** Hand reductions:

| word | reduced | ℓ | ℓ_min | e |
|---|---|---|---|---|
| V₀V₁V₀ | σ₀²σ₂⁻¹σ₁⁻¹ | 6 | 4 | 1 |
| V₁V₂V₁ | σ₁²σ₃⁻¹σ₂⁻¹ | 6 | 4 | 1 |
| V₂V₃V₂ | σ₂²σ₄⁻¹σ₃⁻¹ | 6 | 4 | 1 |
| V₀V₁V₂V₀V₃ | σ₀²σ₁⁻¹σ₄⁻¹ | 10 | 4 | 3 |
| V₀V₁V₂V₃V₀ | σ₀²σ₁⁻¹σ₄⁻¹ | 10 | 4 | 3 |
| V₂V₀V₃V₁V₀ | 4 letters | 10 | 4 | 3 |
| V₂V₃V₀V₁V₀ | 4 letters | 10 | 4 | 3 |
| V₀V₁V₀V₁V₂ | σ₀²σ₂⁻¹σ₃⁻¹ | 10 | 4 | 3 |
| V₁V₂V₁V₂V₃ | σ₁²σ₃⁻¹σ₄⁻¹ | 10 | 4 | 3 |

So V₀V₁V₂V₀V₃ and V₀V₁V₂V₃V₀ are predicted to be the same braid. The crossing-matrix bound
is predicted to be attained in every row (Σ|c| = 2 + 1 + 1 = 4). Then e does not depend on the
order in which cancellations are made. Each row's e is a fact about the braid and its word,
not about a reduction strategy.

**G3.** The reduction involves no nucleon strand. It cannot by itself assign 2E₀·ln q to
Q_β or to m_n − m_p. It would need an energy per cancelled pair, and none is derived in the
corpus. Any such constant chosen to make 3 × (constant) match a target would be a fit. The
word that couples the pair to a nucleon is not fixed by the corpus. That is an owner input.

## Reporting rules

- A prediction that fails is reported as failed, with the computed value.
- Q_β, m_n − m_p and 2E₀·ln q are quoted only after G1–G3 are settled, for context, and
  nothing is chosen by them.
- Any negative is scoped (a) or (b) per AGENTS.md. A (b) claim names its invariant.
