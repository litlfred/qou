# Coordination ledger — the Hecke tower and the Markov-trace parameter

**Goal.** Get `H_n(q)` and its Markov trace onto a footing where downstream
physics can cite them: genuine algebra instances at each `n`, and a *derived*
value for the trace parameter `z` rather than a chosen one.

Opened 2026-08-09 by `claude/anchor-followups-2026-08-08` under
[`local/coordinate`](../../.claude/skills/local/coordinate.md) §9, on posting
intent to [#4857](https://github.com/litlfred/qou/pull/4857).

## The seam

Two branches converged on the same object from opposite sides, and the split is
clean enough to be worth writing down rather than renegotiating each session.

| | `claude/post-drain-audit-8hj2` (#4857) | `claude/anchor-followups-2026-08-08` |
|---|---|---|
| **owns** | the algebra | the trace parameter and the weights |
| **files** | `QOU/Hecke/**`, `QOU/Machinery/MarkovTraceH4*`, `QOU/IwahoriHecke/**`, `computations/markov/**` | `QOU/QBeta/{TemperleyLiebTower,GramSignature,InterfaceScalar}.lean`, `QOU/BraidsAndKnots/ColorFlavorIsospinSelection.lean` |
| **supplies** | `HeckeAlgebra`, `IsHeckeOfFullRank`, instances at `n = 2, 3, 4`, `MarkovTraceContext` with content | what pins `z`, which Wedderburn blocks survive, `H_n/rad ≅ TL_n` |
| **needs** | a justified value for `z` | concrete instances to specialise against |

Overlap **additive**, not conflicting: no file is claimed by both.

## The composition, in one line

`z` is **free at `n = 2`** — `H₂(q)` is commutative with one generator, so every
`z` satisfies the axioms, which is why `markovTraceH2` is correctly a `def` and
not an `instance`. `z` is **forced at `n = 3`**, the moment a three-row partition
exists whose weight can be asked to vanish.

## Ledger

| Date | Branch / PR | Phase | Status | Cherry-pick |
|------|-------------|-------|--------|-------------|
| 2026-08-09 | #4857 | `IsHeckeOfFullRank` + instances `H2`/`H3` | landed | `QOU/Hecke/FullRank.lean`, `instIsHeckeOfFullRankH3` |
| 2026-08-09 | #4857 | `instHeckeAlgebraH4` via right regular rep | landed | first non-vacuous far-commutativity in the tree |
| 2026-08-09 | #4857 | `IsHeckeOfFullRank R 4` | **open** — bean `qou-awp7` | — |
| 2026-08-09 | #4857 | `MarkovTraceH2` + first `MarkovTraceContext` with content | landed | `contextH2`, `markovTraceH2` |
| 2026-08-09 | `anchor-followups` | Bratteli branching identity | landed `cf8d3bf9` | `GramSignature.mu_triplet_eq_branch`, `mu_singlet_eq_branch` |
| 2026-08-09 | `anchor-followups` | `H_n/rad ≅ TL_n`, closed-form weights | landed `1f1dbb73` | `TemperleyLiebTower.qint_three_term_pair`, `markov_branching_general` |
| 2026-08-09 | `anchor-followups` | **`z` pinned at `n = 3`** | landed `02601853f` | `y_antisym_factorisation`, `z_eq_q_forces_trivial` |
| 2026-08-09 | `anchor-followups` | pinning as an **iff**; Wenzl derived, not cited; radical is an ideal | landed `10b8dac1d` | `IsConventionD`, `conventionD_unique_nontrivial`, `traceRadical_two_sided` |

## Open asks (posted on #4857, awaiting reply)

1. **Convention-C prose in new code.** `QOU/Hecke/MarkovTraceH2.lean` calls
   `z = 1/(q^{1/2}+q^{-1/2})` "the mathematical Markov parameter". That is
   convention **C**, excised 2026-08-09 (see
   [`trace-convention-registry.md`](trace-convention-registry.md)); production is
   **D**, `z = q³/(q²+1)`. The *code* is correctly convention-agnostic — only the
   prose drifts. One-line fix, and the freshest instance of exactly the drift the
   registry exists to stop.
2. **`qou-awp7` via Wedderburn.** `c004b8f63` records that the tree already has
   H3A/H4A *and their Wedderburn isomorphisms*. If that isomorphism is a usable
   Lean equiv, `finrank H₄ = 1² + 3² + 2² + 3² + 1² = 24` follows from it
   directly, avoiding the 24 evaluation lemmas and the measured `vecCons` 30× /
   8.7 GB costs. Arithmetic half is proved here (`catalan_four`, `radical_four`).
   Not asserted — the equiv has not been read closely from this side.
3. ~~**Shape of the pinning.**~~ **ANSWERED BY BUILDING IT** (`10b8dac1d`).
   `IsConventionD q z := z(q²+1) = q³` now exists in `QOU/QBeta/`, consumable
   as-is, and `conventionD_unique_nontrivial` gives the iff
   `IsConventionD q z ↔ (y₍₁³₎ = 0 ∧ y₍₂,₁₎ ≠ 0)`. Nothing was placed in their
   territory; they take it or ignore it.

## Facts either side may cite

Everything below is sorry-free, `lake build` exit 0, axioms
`[propext, Classical.choice, Quot.sound]` or narrower.

- **`y_λ = 0` exactly when `λ` has ≥ 3 rows** under convention D, and the
  surviving `Σ dim²` is **Catalan(n)** — `2, 5, 14, 42, 132, 429` for `n = 2…7`,
  measured at 50 dps, worst residual `1.34e−51`. Hence `H_n(q)/rad ≅ TL_n(q)`:
  the radical **is** the Temperley–Lieb ideal.
- **Closed form** `y₍ₙ₋ₖ,ₖ₎ = [n−2k+1]_q / [2]_qⁿ`, everything reducible to the
  three-term recursion `[m+2] + [m] = [2]·[m+1]`.
- **The pinning.** `y₍₁³₎·(q²+1)(q⁴+q²+1) = q²(z − q)(z(q²+1) − q³)`, so for
  `q > 0` the antisymmetriser dies at exactly `z = q` (trivial: collapses the
  trace to the one-dimensional character) and `z = q³/(q²+1)` (convention D).
  **D is the unique non-trivial Markov trace on `H₃(q)` whose radical contains
  the three-strand antisymmetriser.**
- **Consequence for downstream results:** at `n ≥ 3` under D the Markov–Gram
  form is **degenerate**. Anything assuming non-degeneracy needs restating —
  `prop:markov-trace-frobenius-selection` is the known instance.

## Notes

- Nothing has been cherry-picked in either direction. This side's layer is
  instance-free by construction (`qint_three_term_pair` takes `(q r X Y : R)`
  with `q · r = 1` and no algebra structure), so it applies to `H3Alg`/`H4A`
  unchanged whenever either branch merges.
- CI status on #4857 is not readable from this side —
  `GET /commits/<sha>/status` returns `403 Resource not accessible by
  integration`. Do not record CI state here as though it had been checked.
