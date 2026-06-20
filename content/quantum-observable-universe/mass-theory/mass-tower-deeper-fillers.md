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

## Cross-paper + uploads + wiring scans

- **`unital-groebner-bases/`** — no overlap with BlochGroup,
  Cl_2, archimedean-functor, or crystal-basis content.
- **`fred2005-formal-groups/`** — contains
  [`unit-root-F-crystal`](../../fred2005-formal-groups/formal-groups-chapter/unit-root-f-crystal.md)
  and `unit-root-iff-integrable`. *Different* notion of "crystal"
  (Berthelot-Ogus F-crystal in formal-groups context, distinct
  from Kashiwara crystal). Cross-paper integration possible at
  the level of *both being categorical / motivic objects*, but
  the math is structurally distinct — no immediate filler-sharing
  opportunity.
- **`uploads/`** — 14 PDFs present (`0008040v1.pdf`,
  `0911.4494v2.pdf`, etc.). Text-grep on the binary PDFs returned
  no hits for `Bloch | Clausen | dilog | figure-8`, so either the
  PDFs lack OCR-extracted text or the keywords are absent. A
  proper intake via `local/document-intake` skill would surface
  any relevant content; out of scope for this filler push.
- **Wiring follow-up:** `crt_markov.py` currently has no
  `solve_y_lambda` reference — the user is preparing the
  modification. Recommendation per the prior turn stands: add
  `solve_y_lambda_numerical(n, q_value)` as a *separate* function
  in `markov_weights_symbolic.py`, leave the symbolic version
  intact for `y_lambda_equivalence_proof.py:60` to consume.

## What's left after this push

The §3b-cond scaffolding is now substantially complete: every
mass-tower / α_EM open problem has a Lean class hook, an
unconditional or sign-witness instance where possible, and
explicit Mathlib-filler infrastructure where the upstream
mathematical content is established. The remaining open content
sits in three substantive places, all upstream:

1. **`BlochGroup F` formal quotient** — full free-abelian-group
   modulo 5-term pentagon construction, ~150 lines of Lean.
2. **Pentagon identity for the BW dilogarithm** — proved on the
   group quotient via the Suslin map.
3. **Faddeev-Kashaev quasi-classical limit** — uniform Tauberian
   theorem for the q-Pochhammer partial product, requires Mathlib
   asymptotic-analysis infrastructure.

Each is a substantial Mathlib-contribution-sized task. The
present infrastructure is sufficient to *state* and *use* every
result conditionally in the §3b-cond pattern, leaving the
substantive mathematical work as well-isolated future steps.
