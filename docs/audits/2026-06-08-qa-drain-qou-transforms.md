# QA proof-statement-integrity drain — quantum-observable-universes transforms slice

Branch: `claude/qa-backlog-proof-qou-transforms-2026-06-08`
Pattern: MERGED PRs #1984 / #1996 / #1997 (categorical-core slice = #1996).

## Scope — 5 blocks, all `proof-statement-integrity` = fail/critical

| Block | Mismatch (from `.qa.json` notes) |
|-------|----------------------------------|
| `categorical-dirac-operator-exists` | `lean.ref` proves `Nonempty` of a free-field struct by trivial witness, not the md's Dirac formula |
| `categorical-fourier-transform-exists` | vacuous `Nonempty` via identity projections, not the md's transform |
| `categorical-laplace-transform-unique` | `:=` an axiom the docstring flags 'too strong' (false in general) |
| `categorical-lagrangian-exists` | vacuous `Nonempty` via identity witness, not the md's Lagrangian |
| `categorical-instanton-exists` | vacuous `Nonempty` via identity witness, not a substantive self-dual instanton |

## Resolution pattern (mirrors #1996 categorical-action)

Replace trivial-witness `Nonempty (Struct)` / false `Subsingleton` axiom with:
- a `noncomputable def` constructing the actual categorical morphism from real
  Mathlib monoidal infrastructure, and
- an existence theorem `∃ S, S = <construction>` (genuine: the formula yields a
  well-defined morphism), or an honest uniqueness theorem "any two morphisms
  factoring as the construction are equal" — same proposition as the `.md`.

Stub commit; details + re-rate deltas to follow.
