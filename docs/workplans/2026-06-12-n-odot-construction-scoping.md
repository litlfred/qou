# Workplan: constructing N_⊙(A, d) — staged plan for the Casimir mode-count object

**Date.** 2026-06-12
**Blocks.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md),
[`conj:casimir-first-q-correction`](../../content/quantum-observable-universe/appendix-surreals/casimir-first-q-correction.md)
**Builds on.**
[`2026-05-31-casimir-n-unknot-construction.md`](../audits/2026-05-31-casimir-n-unknot-construction.md) (n-stability selection),
[`2026-06-01-casimir-free-field-disjoint-grounding.md`](../audits/2026-06-01-casimir-free-field-disjoint-grounding.md) (identification grounded),
[`2026-06-01-casimir-first-qcorrection-figure8.md`](../audits/2026-06-01-casimir-first-qcorrection-figure8.md) (4₁ carrier).

## Goal

The single genuine blocker of both Casimir conjectures is the explicit
categorical object `N_⊙(A, d)` — a surreal-valued, plate-conditioned
disjoint-unknot density whose archimedean shadow is the standard mode
count. The selection principle (n-stability) and the photon
representation already pin down *what the object must reduce to*; this
plan stages *building it*. Each stage has a deliverable that is
independently committable and falsifiable.

## Stage A — finite-cutoff combinatorial model (session-sized)

Define the regulated model: plate geometry `(A, d)`, cutoff `Λ`; mode
lattice `k_z = nπ/d` (n ≤ Λ) × transverse continuum; configuration
space = finite multisets of disjoint unknots, one per occupied mode;
mode functional = bare count (n-stability lemma). Compute the regulated
in−out difference symbolically and verify the `A/d³` scaling and the
`(π²/6)·|ζ(−3)| = π²/720` coefficient against the witness pipeline.

- **Deliverable:** compute script + witness
  (extends `casimir_n_unknot_construction.py`); closes sub-problem 2
  at model level.
- **Physics input (transported, declared):** per-level degeneracy
  `∝ n³` and dispersion — standard free-field mode counting. This is
  the layer a fully internal derivation must eventually replace
  (same seam as the `conj:e-hartree-categorical-derivation`
  archimedean-unit gap).
- **Effort:** 1 session.

## Stage B — surreal lift of the regulated tower (session-sized)

Identify cutoff index with birthday grading: the divergent tower is an
ω-indexed surreal; the regulated value is a Conway-normal-form
coefficient; prove the standard-part identity
`st(ε · N_diff) = finite Casimir energy` against
[`conj:archimedean-stpart`](../../content/quantum-observable-universe/appendix-surreals/archimedean-stpart.md)
and [`def:standard-part-functor`](../../content/quantum-observable-universe/appendix-surreals/classical-limit-stpart.md).

- **Deliverable:** narrative + Lean conditional (the st-arithmetic side
  is already class-axiomatised in `CasimirEpsilonVacuum.lean`; this
  stage replaces the `PlateModeCount` class fields with the Stage-A
  model's values). Mathlib has `riemannZeta` values at negative
  integers via Bernoulli numbers — the `ζ(−3) = 1/120` input can be a
  cited Mathlib fact rather than an axiom.
- **Effort:** 1–2 sessions.

## Stage C — the categorical object (research-grade)

The Yekutieli-homotopy lift proper: a functor from plate-bounded
ambient-isotopy classes to surreal-valued counts, functorial in
`(A, d)`, natural in the in/out comparison, reducing to the Stage-A/B
model via the n-stability selection (Lean:
`CasimirNStability.lean`) and the free-field ↔ disjoint-unknot
identification (grounded in
`rem:trivial-knot-photon-interpretation` /
`prop:recursive-atom-knot-atlas` /
`lem:degree-one-braid-trivial-volume`, per the 2026-06-01 audit).

- **Deliverable:** definition block + functoriality proposition;
  upgrades both conjectures' conditional chains to unconditional
  modulo the declared physics input.
- **Risk:** the lift may require substrate-conformal boundary data not
  yet formalised anywhere in the corpus; if so, split out that
  definition first.
- **Effort:** research-grade; do not time-box to a session.

## Stage D — interacting sector and the 1/d power (research-grade)

Extend the Stage-C functor to degree-≥2 closures, weighting each mode
by its Markov trace `J_K(q)` gated on `Vol(K) ≠ 0`. The first
contribution is 4₁ with weight `1 + (3/4)h² + O(h⁴)` (Lean-proved,
`FigureEightCasimirWeight.lean`). Derive the `1/d` power of the
correction — settling whether the radiative-correction expectation
`1/d⁶` is right — and the absolute coefficient.

- **Deliverable:** closes `conj:casimir-first-q-correction` (or
  refutes the 4₁-carrier identification per its falsification path).
- **Effort:** research-grade; depends on Stage C.

## Falsification hooks (carried from the blocks)

- Stage A/B: if the regulated surreal coefficient does not match
  `−π²A/(720 d³ ε)`, the parent conjecture is refuted.
- Stage D: if the first non-vanishing substrate correction is not
  `J_{4₁}`-weighted, the first-q-correction conjecture is refuted.

## Non-goals

- No new probe sweeps for the π²/720 prefactor: six fitting routes are
  already null-resulted
  ([investigation audit](../audits/2026-05-30-casimir-epsilon-vacuum-investigation.md));
  formalize-first applies.
- No claim that Stages A–B make the chain "internal": the per-level
  degeneracy stays transported until Stage C+ replaces it.
