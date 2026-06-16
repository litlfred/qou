# Q_β precision-ladder closure path — concrete derivation roadmap

**Date:** 2026-05-19
**Branch:** `claude/track-a-b-per-isotope-and-rho-xi`
**Context:** user direction "most important to close this gap" — the derivation gap between empirically-fit c_k forms and a categorical first-principles derivation.

## State of the closure problem

| Rung | Closed form | Derivation status |
|------|-------------|-------------------|
| c_1 | b (Hoefsmit) | derived (Hoefsmit construction) |
| c_2 | −1 (factor convention) | trivial |
| c_3 | J_Hopf(q=1) = −2 | **derived** (Khovanov 2000, Jones 1985) |
| c_4 | c_3 · b⁴ = −2·b⁴ | empirical fit (0.91% residual) |
| c_5 | −(b² + 1/2) | empirical fit (sub-ppt residual) |
| c_6 | c_3² · b² = 4·b² | empirical fit |
| c_7 | c_3³ = −8 | empirical fit (residual at leverage limit) |

**Numerical pattern-matching is exhausted.** Five rungs of empirical data don't uniquely determine a generating function or operator.

## Why "find the GF directly" failed

I attempted to find F(z, b, ℏ_q) such that c_k(q) · b(q)^k · z^k are its Taylor coefficients at z = ℏ_q². The bidegrees in (b-power, z-power) space:

```
(3, 3): c_3 contribution at  −2
(8, 4): c_4 contribution at  −2  (b⁴ from c_4 = c_3·b⁴ + b⁴ from factor)
(7, 5): c_5 contribution at  −1  (b² · b⁵ term in c_5)
(5, 5): c_5 contribution at  −1/2 (1/2 · b⁵ term in c_5)
(8, 6): c_6 contribution at  +4  (c_3² · b² · b⁶)
(7, 7): c_7 contribution at  −8  (c_3³ · b⁷)
```

The b-powers are **non-monotonic** in z-power: 3, 8, 7&5, 8, 7. This rules out simple univariate generating functions F(b·z), F(b²·z), etc.

A two-variable GF F(b, z) might exist but isn't visible from these six terms.

## What additional theoretical input would close the gap

### Path 1: Identify the underlying operator

The precision-ladder factors arise from the trace of *some operator* on V_(2,1) ⊗ ... at some Hecke level. Specifically, if we knew an operator-valued ψ(q, ℏ_q) such that

$$Q_\beta^{\text{cat}}(q) = Q_\beta^A(q) \cdot \langle \psi(q, \hbar_q) \rangle$$

(with ⟨·⟩ a categorical trace), then **expanding ψ in ℏ_q would yield the c_k directly**. Candidates for ψ:

1. **Hoefsmit transfer matrix of a 3-fold Markov closure** — explicit; involves σ_1, σ_2 ∈ H_3(q).
2. **KLR canonical-basis transfer operator** — exists; not yet specialised to Q_β.
3. **Bethe-ansatz trace** — speculative but standard in q-deformed integrable systems.

**Concrete derivation attempt for Path 1:**

If ψ = exp(b · ℏ_q · X) for some operator X on V_(2,1) (a Bethe-style ansatz), then

$$\langle \psi \rangle = \langle \exp(b \hbar_q X) \rangle = \sum_k \frac{(b\hbar_q)^k}{k!} \langle X^k \rangle.$$

The c_k would then be Taylor coefficients of an exponential generating function — not a power series. Test: do the empirical c_k look like (something)/k!? At k=3, c_3/3! = -2/6 = -1/3; at k=4, c_4/4! = -2b⁴/24 ≈ -0.05; at k=5, c_5/5! = -(b²+1/2)/120 ≈ -0.01. No obvious factorial pattern.

If ψ = (1 + b·ℏ_q·X)^{-1} (rational) or some product, the GF would be rational/algebraic. Not visible from data alone.

### Path 2: Compute Khovanov-Rozansky polynomial of the relevant link projection at finite q

The 3-fold Markov closure of the Q_β-relevant braid in B_3 produces a specific link L. The Khovanov-Rozansky homology of L is a bigraded vector space Kh(L)(q, t). At t = −1 it decategorifies to V_L(q).

If we knew L explicitly, we could compute Kh(L)(q_0, t_0) and check whether its Taylor expansion in (q − 1) or (q − q_0) gives the c_k.

**Open question for Path 2:** what link L corresponds to the 3-fold Markov closure of the Q_β-prediction braid? The doc cites "Hopf-link substructure" for c_3 but doesn't identify L explicitly for higher k.

### Path 3: Spectral sequence on Wedderburn-block stratification

The 2026-05-18 cohomological-strata audit proposed:

$$c_k = \sum_{p+q=k} \text{Tr}(E^{p,q}_\infty)$$

for some spectral sequence on the Wedderburn-block stratification of H_n(q). To make this concrete:

1. **Identify the spectral sequence** by giving its E_1 page explicitly. Candidates: a filtration on the Hecke algebra by "depth in V_(2,1)", or a Hopf-algebra-style coalgebra structure.
2. **Compute differentials d_r** for r = 1, 2, ... and show they stabilise at E_∞ at finite r.
3. **Verify Tr(E^{p,q}_∞) reproduces the per-rung integer coefficients** (−2, −2, −1/2, −1, +4, −8 from the bidegree table above).

This is the most ambitious path but might be the cleanest.

## Most tractable next step

**Compute the seminormal Hoefsmit matrices for σ_1, σ_2 ∈ H_3(q) at q = q_0 in MPFR-50dps and expand the Markov trace of an explicit operator candidate (e.g. log(σ_1) · log(σ_2)) in ℏ_q²**.

If any specific operator's Taylor coefficients match the empirical c_k pattern, that operator IS the categorical source. This is a finite computation:

```python
# Pseudocode for the most tractable derivation attempt:
sigma_1 = hoefsmit_matrix(1, V_21, q)   # 2x2 mpf matrix
sigma_2 = hoefsmit_matrix(2, V_21, q)   # 2x2 mpf matrix
candidates = [
    sigma_1 * sigma_2,
    log(sigma_1 * sigma_2),
    sigma_1**2 * sigma_2**2,
    # ... other simple operator combinations
]
for psi in candidates:
    trace = markov_trace(psi)
    taylor_coeffs = expand_in_hbar_q(trace, max_order=7)
    # Check: do these match c_3, c_4, ..., c_7?
```

If a match is found, the GF is derived. If not, the operator is more complex (multi-level Hecke embedding, etc.) and the next attempt is Path 2 (Khovanov).

## Practical: what THIS branch can deliver

Closing the gap fully requires:
- ~1 day for the operator-identification compute (Path 1)
- ~1 week for Khovanov-Rozansky at finite q (Path 2)
- ~weeks-to-months for the spectral-sequence convergence theorem (Path 3)

**This branch's scope** ends with:
1. ✓ Sub-percent empirical closed forms for c_4..c_7
2. ✓ Lean axiomatised class + canonical instance
3. ✓ Honest audit documenting the derivation gap
4. ✓ Concrete closure-path roadmap (this document)

The actual closure should be a follow-up branch dedicated to one of Paths 1, 2, 3.

## Cross-references

- [`docs/audits/2026-05-19-qbeta-all-ck-categorical-extension.md`](2026-05-19-qbeta-all-ck-categorical-extension.md) — empirical pattern findings
- [`docs/audits/2026-05-18-qbeta-n5-cohomological-breakdown.md`](2026-05-18-qbeta-n5-cohomological-breakdown.md) — original cohomological-strata hypothesis
- [`content/quantum-observable-universe/braids-and-knots/q-beta-categorical-precision-ladder.{md,lean}`](../../content/quantum-observable-universe/braids-and-knots/q-beta-categorical-precision-ladder.md) — the precision-ladder content block
- [`computations/sweeps/binding_q_target_sweep.py`](../../computations/sweeps/binding_q_target_sweep.py) — sweep with N=0..7 rungs
