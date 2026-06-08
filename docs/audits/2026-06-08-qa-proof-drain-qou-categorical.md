# QA proof-drain — quantum-observable-universes categorical slice (2026-06-08)

Drains `proof-statement-integrity` fails for 5 blocks under
`content/quantum-observable-universe/quantum-observable-universes/`:

1. `categorical-action-exists` — lean.ref proves weaker Nonempty claim, not S_Phi = tr(Phi)
2. `categorical-action-unique` — lean.ref is an axiom the docstring documents as strictly false
3. `categorical-dq-squared` — lean.ref QOU.categorical_dq_squared ABSENT + file doesn't compile
4. `dq-squared` — lean.ref QOU.dq_squared ABSENT
5. `categorical-reeb-exists` — lean.ref QOU.CategoricalReeb.ofWeightDecomposition ABSENT

One slice = one PR. Pattern mirrors PR #1984 (braids proof-drain).

## Per-block resolution

(filled in as work proceeds)
