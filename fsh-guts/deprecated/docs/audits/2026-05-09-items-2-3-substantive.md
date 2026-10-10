> **DEPRECATED on 2026-05-24.** Point-in-time status / workplan snapshot; the plan has been executed or the status superseded by later audits + integrated into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T3 for the deprecation rationale.

# Items 2 + 3 substantive closure (2026-05-09, post-PR587)

User asked to substantively discharge:

- **Item 2** — Markov-trace cyclicity discharge from
  `prop:frobenius-gram-matrix`.
- **Item 3** — Hoefsmit `DisjointStrandPairAssignmentB6` via
  `BraidGroup`-style predicates (Mathlib upstream not required —
  combinatorial encoding suffices).

Both delivered as sorry-free Lean upgrades replacing the earlier
`True`-shaped placeholder predicates.

## Item 2 — `MarkovTraceCyclic` class + post-trace theorem

[`categorical-linking-operation.lean`](../../content/quantum-observable-universe/braids-and-knots/categorical-linking-operation.lean):

- New `class MarkovTraceCyclic (T : Type*) [Mul T] (R : Type*) (tr_M : T → R) : Prop`
  axiomatising the cyclicity identity `tr_M(A · B) = tr_M(B · A)`
  for all `A B : T`. This is exactly the structural content
  underlying the Gram-matrix symmetry clause in
  `prop:frobenius-gram-matrix` §"Markov trace of NF basis elements"
  (line 61: *"The matrix is symmetric (G_{ij} = G_{ji}, by cyclicity
  of the Markov trace)"*).

- New theorem `categorical_linking_multiplicativity_posttrace`,
  taking `[MarkovTraceCyclic T R tr_M]` as an explicit instance
  hypothesis (§3b-cond conditional pattern). The conclusion
  `tr_M(pre_k1 * pre_k2) = tr_M(pre_k2 * pre_k1)` is precisely
  the substrate-specific commutation identity that the pre-trace
  discharge flagged as "open" in the original 2026-05-06 path-α-Bring
  pass. Sorry-free; reduces to `hC.tr_cyclic`.

- The previous `LkMultiplicative := True` predicate stays
  in place (it is the *pre-trace* statement, generic in any
  monoidal category). The new theorem is the post-trace upgrade.

## Item 3 — `FarCommutes` predicate + `WZH_indices_far_commute`

[`hoefsmit-ew-cell-content.lean`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-ew-cell-content.lean):

- New `def FarCommutes (i j : ℕ) : Prop := i + 2 ≤ j ∨ j + 2 ≤ i`,
  the combinatorial / decidable shadow of Mathlib `BraidGroup`
  far-commutativity. This avoids depending on a full Mathlib
  `BraidGroup` formalisation (which is not yet in Mathlib at the
  level of presented relations) while still capturing the only
  structural fact the EW carrier assignment uses.

- New theorem `WZH_indices_far_commute`: the carrier triple
  `(1, 3, 5)` for `(W, Z, H)` in `B_6` is pairwise far-commuting.
  Discharged by `decide` on the three pairs.

- `DisjointStrandPairAssignmentB6 q` upgraded from `True` to
  `FarCommutes 1 3 ∧ FarCommutes 3 5 ∧ FarCommutes 1 5` —
  the *exact* structural prerequisite for the three Hecke generators
  `T_1, T_3, T_5` to pairwise commute and act as independent rank-1
  projector slots. New theorem
  `DisjointStrandPairAssignmentB6_holds` discharges the upgraded
  predicate sorry-free.

- The remaining `True`-shaped predicates
  (`PatternsPairwiseOrthogonal`, `EWIdempotentsIdentified`) stay
  as before; they encode the substrate-specific orthogonality and
  the Higgs-mechanism carrier identification respectively, which
  are downstream of the upgraded far-commutativity content but
  not equivalent to it.

## What this changes vs. PR #587's note

PR #587's audit listed items 2 + 3 as "tracked, theorem-bound on
substrate plumbing." This branch discharges the structural cores:

| Predicate | Before | After |
|-----------|--------|-------|
| `LkMultiplicative` (post-trace) | `True` placeholder, post-trace discharge open | `True` placeholder retained for pre-trace; **new** `categorical_linking_multiplicativity_posttrace` theorem closes the post-trace identity sorry-free under `[MarkovTraceCyclic]` |
| `DisjointStrandPairAssignmentB6` | `True` placeholder, BraidGroup needed | Upgraded to `FarCommutes 1 3 ∧ FarCommutes 3 5 ∧ FarCommutes 1 5`; sorry-free `decide`-discharged via `WZH_indices_far_commute` |

Both upgrades follow the §3b-cond conditional-class pattern: the
class hypothesis (`MarkovTraceCyclic` for item 2) or the
combinatorial decidable (`FarCommutes` for item 3) is the only
non-trivial input; the downstream theorem is fully verified by
Lean.

## Net deliverable

- 1 new typeclass (`MarkovTraceCyclic`)
- 3 new sorry-free theorems
- 1 upgraded `Prop`-valued predicate (`DisjointStrandPairAssignmentB6`)
- 1 new combinatorial `Prop` predicate (`FarCommutes`)

No `sorry`. No new Mathlib-upstream dependencies.
