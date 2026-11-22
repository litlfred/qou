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

---

# Addendum 2: the exact factor beyond h/2 (owner via coordinator 2026-11-22; written before any number)

Task: start from the first-order result w ≈ h/2 and look for the exact factor from first principles, with no fitting.

## Disclosed before computing (these are rewrites, not findings)
- The corpus already derives w algebraically. From `rem:energy-scale-planck`, c_q = 1/(q−1) and ℏ_q = (q−1)/q, so
  E₀ = m_e c_q² ℏ_q. The muon pin gives m_e = m_μ ℏ_q²/Vol(4₁). Together: w = ℏ_q·(ℏ_q c_q)² = ℏ_q·q⁻²
  (Lean `E0MuonUnit.E0_eq_muon_fraction`).
- ℏ_q = h/(1+q). So "w ≈ h/2" says only that 1 + q = 2 at q = 1. The exact factor relative to h is
  1/(q²(q+1)), and the pole at q = −1 already excludes single word traces (Addendum 1).
- **Route R1 has no content.** In the symmetric Young channel, σ acts as the scalar q, so every function
  f(q) is the channel value of f(σ). In particular w = χ_(2)(σ⁻² − σ⁻³). This holds for any target
  at all, so it is not tested as evidence.

## The invariant that has content: framed link invariants and their order at q = 1
The mass of a braid class is the framed form 𝔪(β) = (1+q²)ⁿ q^{−n−2·wr(β)} τ_D(β) (`def:mass-identity`).
It is constant on link types, it lies in ℤ[q^±], and 𝔪(1) = 2^{c} > 0.
- **Prediction, stated now.** For a knot K, the excess 𝔪(K)/𝔪(O) − 1 vanishes to order ≥ 2 at q = 1,
  because a Jones-type knot polynomial has value 1 and first derivative 0 at the classical point.
  So no knot excess can equal w, which has order 1.
- **Prediction, stated now.** For a two-component link L, the excess over the 2-unlink vanishes to
  order 1 exactly when lk(L) ≠ 0. Its first-order coefficient is proportional to lk.

## Routes, fixed now (no others)
- R2, knot excess, in two normalisations: 𝔪(K)/𝔪(O) − 1 and 𝔪(K) − 𝔪(O).
  - K = 3₁ = closure of σ₁³ (n = 2).
  - K = 4₁ = closure of (σ₁σ₂⁻¹)² (n = 3); this is the muon knot.
- R3, linked-pair excess, in two normalisations: 𝔪(L)/𝔪(O⊔O) − 1 and 𝔪(L) − 𝔪(O⊔O).
  - L = Hopf⁺, closure of σ₁²; L = Hopf⁻, closure of σ₁⁻²; both with n = 2.
  - L = closure of the electron word σ₁σ₂σ₁ (n = 3; owner ruling: Hopf-link closure).

## Verdict rule
- **Derived** only if a route equals w exactly, with no extra factor.
- **First-order match only** if ord₁ = 1 and the leading coefficient is 1.
- **Excluded** if ord₁ ≠ 1 or the leading coefficient is not 1. Scope (a) for the listed objects. For
  knots, the order-≥2 statement is scope (b), by the invariant above.
- No rescaling, no powers of q, no combinations of routes. Any of those would be fitting.

---

# Addendum 3 (2026-11-22): is ℏ_q = 1 − q⁻¹ a one-sided (positive-crossing-only) object?

Owner choice, 2026-11-22 (card, option 1). Written before any computation in this addendum.

## Question
ℏ_q = 1 − q⁻¹ = h/(1+q) is the factor left over in E₀'s weight w = ℏ_q/q² (Addenda 1–2).
The skein relation σ − σ⁻¹ = h uses both crossing signs. Is there an object built from
**positive crossings only** whose value is ℏ_q (or w) exactly, with no chosen coefficient?

## What "one-sided" can mean (fixed now)
- **Not at the Hecke-algebra level.** In H₂(q), σ⁻¹ = σ − h. So every element is a polynomial in σ,
  and "uses only σ" does not single out anything. Prediction: T1 below holds, and it removes this reading.
- Also excluded as evidence: the spectral reading ℏ_q = 1 − λ₊⁻¹, with λ₊ = q the eigenvalue of σ
  on the symmetric channel. It is true by arithmetic, and any f(q) is a channel value (Addendum 2, R1).
- **Therefore one-sided means: positive braid words** (letters σᵢ only), evaluated with the same
  convention-D state-sum trace τ_D and framed mass 𝔪 as Addenda 1–2.

## Tests, fixed now (no others)
- **T1 (algebra).** In the 2-strand Jimbo representation, R⁻¹ = R − h·1; and a + b·R is a scalar
  matrix only if b = 0. Lean.
- **T2 (single-crossing increment).** For a positive word β and one more positive letter σᵢ:
  τ(βσᵢ)/τ(β) − 1, τ(βσᵢ) − τ(β), and the same two for 𝔪.
  - Prediction: all are nonzero at q = 1 (ord₁ = 0), because adding one letter changes the cycle
    count of the permutation by ±1, so τ(1) = 2^{c−n} changes by a factor 2^{±1}.
  - Enumerated: n = 2, 3; every positive β of length ≤ 3; every i.
- **T3 (two-crossing increment).** β → βσᵢσⱼ (both positive), the same four normalisations.
  - Enumerated: n = 2, 3; every positive β of length ≤ 2; every (i, j).
  - Prediction: ord₁ ≥ 1 when the cycle count returns to its old value; leading coefficient tied to
    the linking change (Addendum 2 found ±3 for Hopf⁺).

## Verdict rule (same as Addendum 2)
- **Derived** only if an enumerated object equals w or ℏ_q exactly.
- **Monomial match**, reported separately, if it equals q^k·ℏ_q for an integer k. It counts only if
  k equals −2·(writhe added), the framing factor already in 𝔪. Any other k would be a chosen power.
- **First-order match only** if ord₁ = 1 with leading coefficient 1.
- Otherwise **excluded**, scope (a) for the enumerated objects; T2 is scope (b) for all positive words
  if the parity argument is proved.
- Every enumerated object is reported. No selection, no combinations, no rescaling.
