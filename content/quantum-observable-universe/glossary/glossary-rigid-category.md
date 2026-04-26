**:defterm[Rigid category]{#rigid-category}.** A monoidal category in which every object has both
a left dual and a right dual. Equivalently, every object participates
in an exact pairing on both sides.

The paper's
[Definition 1.1 (Rigid monoidal category)](#def:rigid-monoidal-category)
bundles a single object $V$ with its dual and the snake identities.
Mathlib's `RigidCategory` is the global statement that *all* objects
have duals.

**Mathlib reference.**
`CategoryTheory.RigidCategory` (class), extending `MonoidalCategory`.
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.
Provides: `HasLeftDual X` and `HasRightDual X` for every `X`.
