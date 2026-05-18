/-!
# jet-horizon — sibling stub

The canonical Lean source for `def:jet-horizon` (and the other
content blocks that share this module — `aeon`, `big-bang-state`,
`cmb-boundary-datum`, `cmb-functor`, `horizon-functor`,
`aeon-boundary-generates-chart`, `horizon-conformal-invariance`,
`qou-is-ccc`) lives at `content/quantum-observable-universe/lean/QOU/JetHorizon.lean`,
which is Lake-built under the `qou` package.

This sibling stub exists solely to satisfy the
`lean-file-exists` constraint rule
(`folio-assistant/schemas/constraints.ts` §lean-file-exists),
which requires every `definition` block to have a sibling
`.lean` file at the same path as its `.ts` manifest.  The
re-export below keeps the declarations available under the
expected `QOU.*` qualified names without duplicating them.

Ref: [manuscript] §9
-/

import QOU.JetHorizon
