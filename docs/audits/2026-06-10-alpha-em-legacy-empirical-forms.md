# Legacy / obsolete α_EM empirical forms (moved out of the paper)

**Date:** 2026-06-10. **Why this doc exists:** per the owner directive
("keep the audit trail, but not in the paper — in audit docs and deprecated, so
other agents don't go down [dead-ends], or if they need to revisit they can
easily"), the obsolete empirical α_EM closed forms are recorded **here** rather
than inline in the paper block
[`rem:alpha-em-categorical-trace`](../../content/quantum-observable-universe/mass-theory/alpha-em-categorical-trace.md),
which is now a trimmed deprecation stub pointing at the canonical form.

## Canonical (current, in the paper)

- **Pre-archimedean structural form** —
  [`prop:alpha-em-categorical-trace-ratio`](../../content/quantum-observable-universe/predicted-spectra/alpha-em-categorical-trace-ratio.md):
  `α_EM = h²/(q·δ_q(T_{2,9})·δ_q(T_{3,5})) = 1/(q[9]_q[10]_q)`, in
  `R = ℤ[q^{±1/2}, h⁻¹]`, **no π** — the antisymmetric `e₋` (sinh) coupling of
  the Hopf 2-strand operation.
- **Additive Bring zero-mode correction** —
  `prop:em-coupling-bring-zero-mode` (`+2/(3π)`, archimedean side, `τ_arch` image).

## Obsolete empirical forms (DO NOT REVIVE — recorded for the audit trail)

### 1. The `45·[3]_q·(1 + δ_CS + 8q·δ_CS²)` PSLQ form

$$\frac{1}{\alpha_{EM}} = 45\,[3]_q\,\bigl(1 + \delta_{CS} + 8q\,\delta_{CS}^2\bigr), \qquad \delta_{CS} := \hbar_q^4\,[5]_q.$$

**Status: single-point PSLQ-uniqueness match at q₀, NOT a derivation.** The
100-dps extended 54-element scan ruled out the multiplicative q-rational family
entirely. Only the integer `45 = C(10,2)` had a structural derivation
(`exterior-square-borromean`); the factors `[3]_q`, `ħ_q⁴[5]_q`, `8q` were
unproved/post-hoc, and the form disagrees with the Chern–Simons form at every
`q ≠ q₀`. The earlier per-factor "forced by" table cited
`em-spectral-completeness`, `gauge-coupling-uniqueness`,
`force-carrier-bring-uniqueness`, `gram-determinant-plancherel-ratio`,
`exterior-square-borromean` — but those support only the canonical trace-ratio
form, not this empirical product.

### 2. The gluon-octet conjecture

A legacy "gluon-octet" conjecture once claimed to force the `δ_CS` / `8q`
factors. **Removed** along with the rest of the PSLQ-empirical family superseded
by `prop:alpha-em-categorical-trace-ratio`. The `δ_CS = ħ_q⁴[5]_q` and `8q`
identifications were subsumed into `gram-determinant-plancherel-ratio` as a
numerical specialisation, not separate propositions.

### Numerical record

`q[9]_q[10]_q` at q₀ (50 dps) = `136.823…`; with the archimedean `+2/(3π)` →
`137.0354…` (−4.2×10⁻⁶ vs CODATA); the further `α/(4π)` near-match → `+5.7×10⁻⁸`
(coefficient `1/(4π)` is a 1.4% near-match, π-carrying, archimedean).

**Guard:** the empirical product forms above are **PSLQ coincidences at q₀**, not
structural derivations (the residual is non-smooth in q — a zero-crossing at q₀,
not an identity). Do not re-propose them as production α_EM formulas. The
canonical, pre-archimedean source is the trace-ratio; the π-corrections are the
forced `τ_arch` archimedean shadow (see the α_{basis-knot} program,
`docs/workplans/2026-06-10-alpha-basis-knot-couplings.md`).
