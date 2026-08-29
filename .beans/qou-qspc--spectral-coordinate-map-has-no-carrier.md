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

---

## PARTIAL 2026-08-29 — option 1 done; the bean stays OPEN

Option 1 above is landed in `spectral-half-line.lean`, three lemmas, all
`#print axioms`-clean (`[propext, Classical.choice, Quot.sound]`), file exit 0
`lean`-direct:

- `exists_spectral_coord` — a spectral coordinate map always exists:
  `ρ := Complex.log α / Real.log q` on the principal branch gives `α = q^ρ`.
  Uses only `q > 1` and `α ≠ 0`, the latter already a field of
  `LocalQZetaFunction`.
- `spectral_coord_re_unique` — **the useful one.** Any two exponents with the
  same `q`-power share a real part. So `Re(ρᵢ) = 1/2` is a well-posed
  conclusion even though `α ↦ ρ` is not well-defined, being pinned only modulo
  `2πi / log q`. This is what makes `spectral_half_line`'s conclusion mean
  something independent of a branch convention, and it was not recorded
  anywhere before.
- `spectral_coord_re_eq` — the closed form `Re(ρ) = log‖α‖ / log q`, which with
  the previous lemma is *the* real part of any spectral coordinate for `α`.

**This does NOT close the bean, and must not be reported as closing it.** The
gap was never that no map exists — it is that nothing identifies these `ρᵢ`
with the spectrum of the Reeb derivation `ξ_q`. `spectral_coord` in
`spectral_half_line` is doing double duty: a coordinate relation (now supplied)
*and* a Reeb-eigenvalue identification (still supplied nowhere). What the three
lemmas buy is that the gap is now **isolated and named** rather than bundled
into one opaque hypothesis — the remaining work is exactly option 2, a
`HasReebSpectralCoords`-style class tying the exponents to `ξ_q`, with an
inhabited witness.

Sharpened statement of what is open: *the Frobenius eigenvalues of Bring's
curve and the Reeb spectrum are two sets of numbers that the arc requires to be
the same set, and no result in the corpus relates them.*
