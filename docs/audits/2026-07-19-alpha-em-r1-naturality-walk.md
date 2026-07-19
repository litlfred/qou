# α_EM R1 — the naturality walk, first pass (2026-07-19)

**Context:** R1 of the T5 assembly
([#4068](https://github.com/litlfred/qou/pull/4068)): *the framework's τ
restricts to the cover-monodromy functor F on the H₂-channel data* — a
corpus-internal naturality check against the brings-surface bridge. Beans
`qou-bc35`, `qou-tq20` closed (owner-authorized), T1–T4 beans completed.

**Probe:** [`computations/alpha_em/alpha_em_r1_naturality_walk_probe.py`](../../computations/alpha_em/alpha_em_r1_naturality_walk_probe.py)
→ [`alpha-em-r1-naturality-walk.witness.json`](../../computations/alpha_em/alpha-em-r1-naturality-walk.witness.json)
— 4/4 PASS, sympy-exact.

**Scope guard (STRICT):** N3 named, not derived; R2 untouched (phase-4,
owner-gated); no fit; nothing wired.

## Findings

- **N1 — F is corpus-internal (verified).** The T1 deck generator is the
  **coordinate 4-cycle in the corpus's own S₅ action**
  ([`brings-curve`](../../content/quantum-observable-universe/brings-surface/brings-curve.md)):
  `P·V = i·V`, `P·W = −i·W`, `P⁴ = 1`, with the carrier vertex
  `V = [1:i:−1:−i:0]` satisfying `Σx = Σx² = Σx³ = 0` exactly. The #3942
  Lean fact in S₅-permutation form: **F imports no new geometry** — every
  ingredient is built from the corpus's canonical automorphism data.
- **N2 — the two degree-4 covers coexist (reconciled).** The corpus's
  canonical `Σ₄ → ℙ¹`
  ([`brings-riemann-hurwitz`](../../content/quantum-observable-universe/brings-surface/brings-riemann-hurwitz.md):
  R = 14, six branch points) and T1's cyclic `Bring → E` (R = 6, two
  points) are different maps with different bases, both RH-exact for g = 4.
  No conflict: the corpus block is the linear projection; T1 is the
  ⟨U⟩-quotient.
- **N3 — the irreducible core (named).** What remains of R1 is one bounded
  computation: the corpus's explicit braid generators
  ([`braid-group-action`](../../content/quantum-observable-universe/brings-surface/braid-group-action.md):
  the affine resolvent shifts and Möbius involutions) act on
  `H^{1,0}(Bring)`; compute their action on the χ = ±i eigenlines in the
  **resolvent differential basis** (the ω_k of `H^{1,0}` in w-coordinates)
  and compare with the T2 monodromy half-twist. This needs the differential
  basis — a well-scoped next tranche.

## State of the wall after this walk

```
R1: two-thirds structural, now verified (N1 corpus-internal; N2 reconciled);
    remaining = N3, one bounded computation (resolvent differential basis).
R2: loop-weight provenance — phase-4, owner-gated, untouched.
```
