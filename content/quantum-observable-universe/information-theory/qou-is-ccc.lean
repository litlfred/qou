/-!
# QOU.qou_is_ccc — sibling stub

The canonical Lean source for `prop:qou-is-ccc` lives at
`content/quantum-observable-universe/lean/QOU/JetHorizon.lean:250`
(Lake-built under the `qou` package).  The decl establishes the
horizon-local form of the CCC (conformal-cyclic cosmology)
properties: degree-0 sections vanish, degree ≥ 1 data persists.

This sibling re-exports the Lake module so the content-block's
`lean.ref` URI (`qou:QOU.qou_is_ccc`) resolves cleanly through the
sibling path.

Per the in-tree decl docstring + PR #776 review notes: the *full*
narrative claim also includes CCC-2 (boundary-data inheritance / CMB
of aeon equals terminal boundary datum of predecessor), which
requires a CMB-of-aeon construction beyond `JetHorizon`'s field
structure.  CCC-1 + CCC-3 are formalised here; CCC-2 is tracked as
conditional-class follow-up.

LaTeX label: `prop:qou-is-ccc`

## References

- [penrose2010] R. Penrose, *Cycles of Time*, Bodley Head, 2010
- [manuscript] §9 Information theory / qou-is-ccc
-/

import QOU.JetHorizon
