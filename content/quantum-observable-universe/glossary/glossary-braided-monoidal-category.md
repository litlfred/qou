:defterm[Braided monoidal category]{#braided-monoidal-category}. A :refterm[monoidal category]{#monoidal-category} equipped with a
natural isomorphism $\beta_{X,Y} \colon X \otimes Y \xrightarrow{\sim} Y \otimes X$ (the *braiding*) satisfying the two hexagon axioms.

**Mathlib reference.**
`CategoryTheory.BraidedCategory` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Braided.Basic`.
Notation: `β_ X Y` for `BraidedCategory.braiding X Y`.
