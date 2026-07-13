<!-- FILE_START: glossary-monoidal-intro.md -->
We define monoidal-category terminology used throughout this paper.
<!-- FILE_END: glossary-monoidal-intro.md -->

<!-- FILE_START: glossary-monoidal-category.md -->
**:defterm[Monoidal category]{#monoidal-category}.** A category $\mathbf{C}$ equipped with a bifunctor $\otimes \colon \mathbf{C} \times \mathbf{C} \to \mathbf{C}$, a distinguished unit object $\mathbf{1}$, and coherent natural isomorphisms for associativity ($\alpha$), left unitality ($\lambda$), and right unitality ($\rho$). These satisfy Mac Lane's pentagon and triangle axioms.

**Mathlib reference.**
`CategoryTheory.MonoidalCategory` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Category`.
Notation: $X \otimes Y$ for `tensorObj`, $\mathbf{1}$ for `tensorUnit`.
<!-- FILE_END: glossary-monoidal-category.md -->

<!-- FILE_START: glossary-braided-monoidal-category.md -->
**:defterm[Braided monoidal category]{#braided-monoidal-category}.** A monoidal category equipped with a natural isomorphism $\beta_{X,Y} \colon X \otimes Y \xrightarrow{\sim} Y \otimes X$ satisfying the two hexagon axioms.

**Mathlib reference.**
`CategoryTheory.BraidedCategory` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Braided.Basic`.
Notation: `β_ X Y` for `braiding X Y`.
<!-- FILE_END: glossary-braided-monoidal-category.md -->

<!-- FILE_START: glossary-symmetric-monoidal-category.md -->
**:defterm[Symmetric monoidal category]{#symmetric-monoidal-category}.** A braided monoidal category whose braiding is involutive: $\beta_{Y,X} \circ \beta_{X,Y} = \mathrm{id}_{X \otimes Y}$.

**Mathlib reference.**
`CategoryTheory.SymmetricCategory` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Braided.Basic`.
<!-- FILE_END: glossary-symmetric-monoidal-category.md -->

<!-- FILE_START: glossary-monoidal-functor.md -->
**:defterm[Monoidal functor]{#monoidal-functor}.** A functor $F \colon \mathbf{C} \to \mathbf{D}$ between monoidal categories equipped with a natural transformation $\mu_{X,Y} \colon F(X) \otimes F(Y) \to F(X \otimes Y)$ and a morphism $\epsilon \colon \mathbf{1}_{\mathbf{D}} \to F(\mathbf{1}_{\mathbf{C}})$. These are compatible with the associator and unitors.

Mathlib distinguishes lax monoidal functors (arbitrary morphisms) from strong monoidal functors (isomorphisms).

**Mathlib reference.**
`CategoryTheory.Functor.LaxMonoidal` (class).
`CategoryTheory.Functor.Monoidal` (class) for strong monoidal.
Import: `Mathlib.CategoryTheory.Monoidal.Functor`.
<!-- FILE_END: glossary-monoidal-functor.md -->
