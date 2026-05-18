/-!
# categorical-dq-squared-proof — sibling stub

The canonical Lean source for `prf:categorical-dq-squared` lives at
`content/quantum-observable-universe/lean/QOU/CategoricalDqSquared.lean`,
which is Lake-built under the `qou` package and declares
`QOU.categorical_dq_squared` (the classical-limit direction `d_q² = 0`
when `q = 1`).

This sibling stub satisfies the sibling lookup so the proof block's
`lean.ref` (`qou:QOU.categorical_dq_squared`, `validation: "leanok"`)
resolves cleanly via the Lake tree.

**Authoring note (open):** `AUDIT-REPORT.md` line 260 records that the
original `categorical_dq_squared` was renamed in
`QOU/QuantumObservableUniverse/Instanton.lean` to
`categorical_dq_squared_classical_limit` because the narrative claims
`d_q² ≠ 0` for `q ≠ 1` while the proof establishes only the
classical-limit direction.  The decl carried here from
`categorical-dq-squared-proof.lean` preserves the original name; the
non-vanishing direction remains an open formalization task
(`AUDIT-REPORT.md §P3` item 10: "Prove categorical_dq_squared
non-vanishing for q != 1").

Ref: [manuscript] §quantum-observable-universes
-/

import QOU.CategoricalDqSquared
