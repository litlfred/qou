**Remark (deeper §3b-cond fillers — five consolidated extensions).**

Bundles five small but focused Lean fillers into
[`mass-tower-deeper-fillers.lean`](mass-tower-deeper-fillers.lean):

| Section | Content | Status |
|---|---|---|
| (A) Height-6 partition enumeration | `HeightSixPartition n` structure with `parts : List ℕ`, `parts.length = 6` | unconditional finite-type carrier |
| (B) Demazure sub-crystal predicate | `IsDemazureSubCrystal S` typeclass | ansatz; AGENTS.md §7b item 3 hook |
| (C) Kazhdan-Lusztig classical-limit functor | `KLClassicalLimit f := f 1` | unconditional ansatz |
| (D) Minimal `BlochGroup F` carrier | `HasBlochGroupQuotient F` typeclass with two boolean fields (quotient existence + Borel regulator iso) | typeclass hypothesis |
| (E) Pentagon-identity surrogate for `Cl_2` | `Cl_2_PentagonIdentity` typeclass | typeclass hypothesis |

The five pieces deepen the mass-tower scaffolding:

- (A) makes the Term-7 reduction concrete: a finite-type
  enumeration of the height-6 partitions of $3A$ is now a Lean
  carrier downstream callers can iterate over (once the GS
  spectral-sequence weight is wired in).
- (B) adds the Demazure sub-crystal hook for resonances
  (AGENTS.md §7b item 3 — "incomplete topological states lowering
  the energy budget"), giving the structural sign argument for
  $\alpha_5 < 0$ a Lean-level handle.
- (C) provides the KL classical-limit functor as a ansatz;
  the substantive content (`b_w \to C_w \in \mathbb{Z}[S_n]`) is
  upstream conjectural.
- (D) records the `BlochGroup F` quotient as a typeclass hypothesis
  alongside Borel's regulator-isomorphism hypothesis; both are
  Mathlib-pending classical results.
- (E) records the 5-term pentagon for $\mathrm{Cl}_2$ as a
  typeclass; the full proof needs Mathlib's Fourier-series
  identities.

The synthesis class `DeeperMathlibFillers F` collects
$(B), (D), (E)$ into a single hypothesis suitable for §3b-cond
hooks, with `Cl_2_zero_consistent_with_pentagon` providing a
trivial sanity-check theorem.
