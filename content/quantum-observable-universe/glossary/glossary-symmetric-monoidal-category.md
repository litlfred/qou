**:defterm[Symmetric monoidal category]{#symmetric-monoidal-category}.** A braided monoidal category whose
braiding is involutive: $\beta_{Y,X} \circ \beta_{X,Y} = \mathrm{id}_{X \otimes Y}$
for all objects $X, Y$.

**Mathlib reference.**
`CategoryTheory.SymmetricCategory` (class), extending `BraidedCategory`.
Import: `Mathlib.CategoryTheory.Monoidal.Braided.Basic`.
The symmetry condition is `braiding_swap_eq_id`.
