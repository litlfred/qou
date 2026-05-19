/-!
# QOU.horizon_conformal_invariance — sibling stub

The canonical Lean source for `prop:horizon-conformal-invariance`
lives in `lean/QOU/JetHorizon.lean` as `QOU.horizon_conformal_invariance`
(Lake-built under the `qou` package).  The decl declares: for any
`H : JetHorizon`, every degree-0 section coincides with
`H.algebra.zero 0` — the categorical core of Penrose's
conformal-cyclic invariance condition.

This sibling re-exports the Lake module so the content-block's
`lean.ref` URI (`qou:QOU.horizon_conformal_invariance`) resolves
cleanly through the sibling path.

LaTeX label: `prop:horizon-conformal-invariance`

## References

- [penrose2010] R. Penrose, *Cycles of Time*, Bodley Head, 2010
- [manuscript] §9 Information theory / horizon-conformal-invariance
-/

import QOU.JetHorizon
