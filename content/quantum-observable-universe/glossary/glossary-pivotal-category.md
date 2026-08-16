**:defterm[Pivotal category]{#pivotal-category}.** A rigid monoidal category equipped with a monoidal natural isomorphism $\delta_X \colon X \xrightarrow{\sim} X^{\vee\vee}$ between each object and its double dual.

The pivotal structure is what makes a *left* trace definable alongside the right one: without $\delta$ there is no way to close the left-hand loop back onto $X$, since evaluation lands on $X^{\vee\vee}$. A pivotal category in which the two traces then **agree** on every object is called **spherical**; pivotal alone does not force that agreement.

**Mathlib reference.** None — there is no `CategoryTheory.PivotalCategory`. Mathlib's `Mathlib.CategoryTheory.Monoidal.Rigid.Basic` lists *"Define pivotal categories (rigid categories equipped with a natural isomorphism `ᘁᘁ ≅ 𝟙 C`)"* under its **Future work** heading, and supplies only the rigid layer: `ExactPairing`, `rightAdjointMate`, `comp_rightAdjointMate`.

The classes this paper needs are therefore built in-repo, as `PivotalStructure` and `SphericalStructure` in [`QOU/BraidKnot/KeystonePivotalSpherical.lean`](../lean/QOU/BraidKnot/KeystonePivotalSpherical.lean). They are kept **separate** there for the reason above: `leftQDim` is defined with the inverse braiding and is a genuinely different morphism from `qDimObj`, so sphericality is a real hypothesis rather than a consequence of the pivotor.
