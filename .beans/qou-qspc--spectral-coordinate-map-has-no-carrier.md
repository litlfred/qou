---
# qou-qspc
title: 'q-RH: the spectral coordinate map alpha_i = q^rho_i has no carrier'
status: todo
type: task
priority: high
created_at: 2026-08-29T17:00:00Z
updated_at: 2026-08-29T17:00:00Z
---

The cheapest real gap in the q-Riemann-hypothesis arc. Review:
[`docs/audits/2026-08-29-q-riemann-hypothesis-arc-gap-review.md`](../docs/audits/2026-08-29-q-riemann-hypothesis-arc-gap-review.md).

`cor:spectral-half-line` (`spectral-half-line.lean`) is genuinely proved and
`#print axioms`-clean — the best-formalised declaration in the chapter. But its
statement takes

```lean
(spectral_coord : ∀ i, Z.eigenvalues i = (Z.q : ℂ) ^ (ρ i))
```

as a **hypothesis**, and nothing in the corpus constructs that map or ties the
`ρ i` to the Reeb spectrum of `ξ_q`. As it stands the corollary says: *for any
complex exponents whose `q`-powers are the Frobenius eigenvalues, the real parts
are ½.* That is true and proved. It is not yet a statement about the Reeb
spectrum, which is what the arc needs it to be.

## The real content is the branch choice

`α = q^ρ` determines `ρ` only modulo `2πi / log q`. So:

- `Re(ρ)` **is** well-defined on the coset — which is exactly why the corollary
  is not vacuous, and worth recording as a lemma in its own right.
- but the *map* `α ↦ ρ` is not, without a branch.

Either disposition is honest; pick one and say which:

1. **Construct it.** `ρ i := Complex.log (α i) / Real.log q` with the principal
   branch, then `spectral_coord` becomes a lemma rather than a hypothesis (needs
   `α i ≠ 0`, which `LocalQZetaFunction.eigenvalues_ne_zero` already gives).
   Prove `Re(ρ)` is branch-independent separately.
2. **Name it as an assumption**, in the `IsWeilZeta` style introduced by
   `qou-hwax`: a hypothesis class `HasReebSpectralCoords Z` carrying the map and
   its compatibility with the Reeb derivation, with an inhabited witness so the
   class is not vacuous. This is the right shape if the tie to `ξ_q` is the part
   that is genuinely open — and it probably is.

Option 1 is provable today and is worth doing regardless; it does **not** close
the gap, because the identification of those `ρ` with Reeb eigenvalues is the
actual claim. Do not report option 1 as having closed this bean.
