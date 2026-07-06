**:defterm[Rigid category]{#rigid-category}.** A :refterm[monoidal category]{#monoidal-category} in which every object has both
a :refterm[left dual]{#left-dual} and a :refterm[right dual]{#right-dual}. Equivalently, every object participates
in an :refterm[exact pairing]{#exact-pairing} on both sides.

The paper's
[Definition 1.1 (Rigid :refterm[monoidal category]{#monoidal-category})](#def:rigid-monoidal-category)
bundles a single object $V$ with its dual and the snake identities.
Mathlib's `RigidCategory` is the global statement that *all* objects
have duals.

**Mathlib reference.**
`CategoryTheory.RigidCategory` (class), extending `MonoidalCategory`.
Import: `Mathlib.CategoryTheory.Monoidal.Rigid.Basic`.
Provides: `HasLeftDual X` and `HasRightDual X` for every `X`.
