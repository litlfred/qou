# α_EM F-construction T3 — deck reality forces the ρ-equivariance (2026-07-19)

**Bean:** `qou-yop7` (T3) of milestone `qou-a46k`. Upstream: T1
([#4039](https://github.com/litlfred/qou/pull/4039)), T2
([#4040](https://github.com/litlfred/qou/pull/4040)) merged.

**Lean (this PR):** [`QOU/Archimedean/DeckRealityEquivariance.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/DeckRealityEquivariance.lean)
— sorry-free, `lean`-direct exit 0 with Mathlib.

**Scope guard (STRICT):** no axiom; no instance fabricated; nothing wired;
`1/(8π)` stays phase-4.

## The theorem

The functor's required equivariance `F∘ρ = conj∘F` — conjugation exchanges
the χ = ±i deck eigenspaces anti-linearly — is **forced by deck reality**,
proved in Mathlib generality:

- `mulVec_map_star` — entrywise conjugation intertwines matrix action.
- `conj_eigenvector_of_real` — a real operator's complex eigenspaces come in
  conjugate pairs: `U real, U·v = μ·v ⟹ U·(star v) = μ̄·(star v)`.
- `deck_eigenspace_exchange` — at the T1 deck eigenvalues ±i: the
  i-eigenspace and the (−i)-eigenspace are exchanged by conjugation, both
  directions. This **is** the B1 dictionary's demanded intertwining
  (#3955), realized on the geometric side.

Instantiation is automatic: the deck generator U of the T1 cover acts on
`H¹(Bring, ℝ)` (an automorphism of the real manifold), so its matrix on the
complexification is real — the hypothesis `U.map star = U` holds by
construction.

## One lemma, three hats

This is the third appearance of the same mechanism: reality of the
**Laplacian** forced the ½ split (B4b #3977); reality of the **loop
operator** constructed the lift (#3999); reality of the **deck action**
forces the ρ-equivariance (this). The equivariance costs nothing once the
T1 cover exists — which is exactly why the McMullen route dissolves the
holo/anti-holo obstruction that blocked the original τ-correspondence
attack (`a6d522e0a`).

## Plan state (milestone `qou-a46k`)

```
T1 cover structure                     MERGED #4039
T2 local monodromy = H₂(i) module      MERGED #4040
T3 ρ-equivariance (deck reality)       THIS — proved sorry-free
T4 weight-value transport (¾,¼)        next — the derivation leg
T5 assembly + F = framework-τ residual open
```
