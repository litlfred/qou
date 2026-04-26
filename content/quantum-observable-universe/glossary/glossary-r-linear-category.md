**:defterm[$R$-linear category]{#r-linear-category}.** A category whose hom-sets carry the
structure of $R$-modules (for a commutative ring $R$) such that
composition is $R$-bilinear. This is a light terminological wrapper:
the paper's "$R$-linear" is Mathlib's `Linear R` (which refines
`Preadditive`).

When $R = \mathbb{Z}$, an $R$-linear category is simply a preadditive
category. The quantum universe axioms
([Definition](#def:quantum-universe)) require $R$-linearity for the
hom-spaces of the underlying rigid monoidal category.

**Mathlib reference.**
`CategoryTheory.Linear R` (class), for a `CommSemiring R`.
Import: `Mathlib.CategoryTheory.Linear.Basic`.
Extends: `CategoryTheory.Preadditive` (the $\mathbb{Z}$-linear case).
Import for preadditive: `Mathlib.CategoryTheory.Preadditive.Basic`.

**Note.** The paper writes "$R$-linear category" where Mathlib writes
`[Linear R C]` as a typeclass on a category `C`. No semantic
difference — only a naming convention.
