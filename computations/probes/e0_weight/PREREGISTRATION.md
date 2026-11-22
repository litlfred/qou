# Pre-registration: is E₀'s weight ℏ_q/q² a Markov trace? (2026-11-22)

Owner, 2026-11-22: *"Try to derive the weight ℏ_q/q² from the Markov trace"*. Follows
`QOU/QBeta/E0MuonUnit.lean` (E₀ = m_e·(ℏ_q/q²)/ℏ_q²). Written and committed before any number.

## Target, and its equivalent forms
- w := ℏ_q/q² = (q − 1)/q³ = q⁻² − q⁻³.
- Equivalently E₀/m_e = w/ℏ_q² = 1/(q(q − 1)) = Σ_{k≥2} q⁻ᵏ (formal, |q| > 1).
- Corpus status: `computations/qbeta/qbeta_e0.py` records E₀ = m_e/(q(q−1)) as a definition
  ("single tick"); its tower factor 1/(1 − ℏ_q²) is an open derivation (bean qou-y3bm).

## The trace
The ruled convention-D Markov trace, z_D = q³/(q²+1), realised as the Jones quantum trace
tr(x) = Tr(K^{⊗n} x)/[2]ⁿ on (C²)^{⊗n} with the Jimbo Ř and K = diag(q, q⁻¹). (Check, done by
hand before this file: n = 2 gives tr(σ) = (q[3] − q⁻¹)/[2]² = q³/(q²+1) = z_D.)

## Candidates, fixed now (no others will be tried)
- C1. tr(σ⁻¹), n = 2. (Known by hand already: 1/(q(q²+1)). Disclosed, so it is not a finding.)
- C2. The Ocneanu weights y_(2), y_(1,1) at n = 2.
- C3. tr of the electron word σ₀σ₁σ₀, n = 3, and its inverse.
- C4. tr of the photon vertex σ₀σ₁⁻¹ and of the Borromean core (σ₀σ₁⁻¹)³, n = 3.
- C5. The same six quantities divided by ℏ_q², i.e. tested against 1/(q(q−1)).

## Verdict rule
- **Derived** only if a candidate equals w (or 1/(q(q−1)) for C5) exactly in ℚ(q).
- A match up to a monomial q^k (|k| ≤ 3) is reported as a **monomial near-match**, not a derivation.
- Otherwise: scope-(a) negative for these six objects. The weight stays open; no search beyond
  this list is run, because searching words for the target value would be selection against it.

---

# Addendum 1: is w a *tower-level* object? (owner 2026-11-22, "1 2"; written before any number)

## What is already settled, and what it implies for the tower
- Lean, `QOU/QBeta/E0WeightAllWords.lean` (this branch): for **every** braid word β on any number
  of strands, the convention-D state-sum trace T_β is continuous at q = 1 with
  T_β(1) = 2^{c−n} > 0, so T_β ≠ w. This item has been asked twice; it was answered with a proof.
- So a tower object can equal w only if it **vanishes at q = 1**, and w vanishes there to order
  exactly 1 (w/(q−1) → 1).

## The invariant used: order of vanishing at q = 1
For an object X(q), ord₁(X) := the order of its zero at q = 1. This is fixed before computing.
ord₁(w) = 1. An object with ord₁ ≠ 1 cannot be w.

## Candidates, fixed now. They are the coefficient-free tower objects the corpus defines
- T1. The brane tower (`qbeta_e0.tower_summed`, `prop:brane-tower-q-laplacian-decay`): the level
  terms (ℏ_q²λ)ⁿ for n ≥ 1, their sum ℏ_q²λ/(1 − ℏ_q²λ), and the implemented correction
  1/(1 − ℏ_q²) − 1. Here λ is any eigenvalue that is finite at q = 1.
- T2. The Markov stabilisation tower on the Hecke colimit
  (`SchurWeyl/HeckeColimitFamilyTrace.ocneanuMarkovTraceAt`): τ_D(σ₁σ₂⋯σ_n) = z_Dⁿ, and the
  series Σ_{n≥1} z_Dⁿ = z_D/(1 − z_D).
- T3. The geometric tower already in the target: E₀/m_e = Σ_{k≥2} q⁻ᵏ, read level by level as
  q⁻ᵏ, with the partial sums S_N = Σ_{k=2}^{N} q⁻ᵏ.
- T4. The skein difference τ(βσ) − τ(βσ⁻¹) = h·τ(β), h = q − q⁻¹. This is the only canonical
  operation in the Hecke tower whose output vanishes at q = 1.

## Verdict rule
- **Derived** only if a candidate equals w exactly in ℚ(q).
- If ord₁ differs from 1: excluded by the invariant. This is a scope-(b) exclusion, and the
  invariant is cited.
- If ord₁ = 1 but there is no exact equality: reported as a first-order match. That is not a
  derivation.
- **Excluded by design.** Linear combinations of traces with free coefficients, over ℤ, ℚ or
  ℤ[q^±]. Over ℤ[q^±] the trivial combination w·τ(1) already equals w, so solving for
  coefficients is selection against the target. It is not run.
