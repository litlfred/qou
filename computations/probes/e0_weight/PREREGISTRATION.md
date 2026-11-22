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
