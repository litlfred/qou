# Sidecar re-review of tonight's Lean and blocks (2026-11-16)

Scope: blocks touched by #7915, #8088, #8090, #8085 and #8087 whose
`proof-narrative-lean-equiv` (statement vs Lean) or `da-non-sequitur`
(proof vs statement) sidecar entry was stale or missing. Every verdict was
written after reading the statement, the proof and the Lean declaration that
`lean.ref` resolves to. Reviewer id `agent:sidecar-review-2026-11-15`.

Nothing in the blocks or the Lean was changed. Mismatches are recorded as
findings for the owning threads.

## Counts

| set | verdicts | pass | warn | fail | n/a |
|---|---:|---:|---:|---:|---:|
| non-mass-theory blocks (statement vs Lean, and two proofs) | 27 | 4 | 6 | 17 | 0 |
| mass-theory statements vs Lean | 48 | 7 | — | — | 0 |
| mass-theory proofs vs statements | 34 | 19 | 10 | 5 | 0 |
| conjectures (statement vs Lean not applicable) | 11 | 0 | 0 | 0 | 11 |

The mass-theory statement row is mostly fail or warn; the sidecars hold the
per-block result.

## Recurring defects in statement vs Lean

1. **Self-assuming carriers.** The Lean holds the block's own conclusion as a
   class or context field and the "theorem" projects it. Seen in
   feynman-eigenbasis, confinement, Jucys–Murphy, mass-coefficient,
   rigid-monoidal, t-beta-general, wedderburn-trace-identity, wenzl-qmn,
   q-casimir-exists/unique, categorical-reeb-exists/unique, qou-canonical-action,
   substrate-self-duality.
2. **`lean.ref` points at the wrong thing.** A `def` or `structure` instead of
   a theorem, an unrelated declaration, or nothing: cyclotomic and demazure
   (dangling), spectral-sequence-collapse, nuclear-knot-classification,
   markov-trace-product (`rfl`), markov-trace-factorization (a `def`).
3. **Empirical constants in formal statements.** binding-scale-catalan
   (m_e = 0.510999), six-term (a measured Q-value), bar-even-kernel (0.99824).

## Proof vs statement: fails and major warnings

- **binding-scale-catalan** (fail): proves only Vol(Borromean) = 8G; never
  argues |α_q(q0)| = m_e·Vol; carries an empirical error budget.
- **six-term-per-derivation-weights** (fail): built on CODATA masses,
  E_0 = 0.7823 MeV and the unproved Catalan scale.
- **nuclear-knot-classification** (fail): identifications "verified by
  comparing eigenvalue structure"; uses m_μ/m_e inside the proof.
- **quantum-dilogarithm-stratified** (fail): Step 3 is self-declared
  unestablished, and F_n(z) as written is a single monomial in z, so the
  product expansion cannot hold.
- **skein-generation** (fail): the proof shows its relation collapses the
  skein module of S³ (Hopf = unknot), so the mass-from-linking step does not
  follow; the relation also departs from the repo skein convention.
- **hecke-markov-transition** (warn, major): part (ii) is wrong as stated;
  K_i is doubly stochastic, so its stationary law is uniform, not Mallows.
- **topological-mass-formula-algebraic** (warn, major): applies Φ_q to an
  archimedean absolute value before τ_arch, and the last step uses the volume
  conjecture without saying the result is conditional.
- **spectral-decomposition-qvalue** (statement vs Lean, fail): under
  convention D the Pauli branch gives Q = 0.

## Compute- and mass-affecting findings

binding-scale-catalan, six-term-per-derivation-weights,
nuclear-knot-classification and spectral-decomposition-qvalue feed mass or
binding numbers. Each is routed to the binding/precision owner thread.

## Not done here

The six-reformulations PR from the demoted-conjectures thread was not yet
open at the time of this review.
