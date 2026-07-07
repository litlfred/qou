<!-- FILE_START: glossary-monoidal-intro.md -->
Glossary entries for monoidal-category terminology used in the paper.
<!-- FILE_END: glossary-monoidal-intro.md -->

<!-- FILE_START: glossary-monoidal-category.md -->
**:defterm[Monoidal category]{#monoidal-category}.** A category $\mathbf{C}$ equipped with a
bifunctor $\otimes \colon \mathbf{C} \times \mathbf{C} \to \mathbf{C}$
(the *tensor product*), a distinguished unit object $\mathbf{1}$, and
coherent natural isomorphisms for associativity ($\alpha$), left
unitality ($\lambda$), and right unitality ($\rho$), satisfying
Mac Lane's pentagon and triangle axioms.

**Mathlib reference.**
`CategoryTheory.MonoidalCategory` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Category`.
Notation: $X \otimes Y$ for `tensorObj`, $\mathbf{1}$ for `tensorUnit`
(`𝟙_ C`), $\alpha_{X,Y,Z}$ for `associator`, $\lambda_X$ for
`leftUnitor`, $\rho_X$ for `rightUnitor`.
<!-- FILE_END: glossary-monoidal-category.md -->

<!-- FILE_START: glossary-braided-monoidal-category.md -->
:defterm[Braided monoidal category]{#braided-monoidal-category}. A :refterm[monoidal category]{#monoidal-category} equipped with a
natural isomorphism $\beta_{X,Y} \colon X \otimes Y \xrightarrow{\sim} Y \otimes X$ (the *braiding*) satisfying the two hexagon axioms.

**Mathlib reference.**
`CategoryTheory.BraidedCategory` (class).
Import: `Mathlib.CategoryTheory.Monoidal.Braided.Basic`.
Notation: `β_ X Y` for `BraidedCategory.braiding X Y`.
<!-- FILE_END: glossary-braided-monoidal-category.md -->

<!-- FILE_START: glossary-symmetric-monoidal-category.md -->
**:defterm[Symmetric monoidal category]{#symmetric-monoidal-category}.** A :refterm[braided monoidal category]{#braided-monoidal-category} whose
braiding is involutive: $\beta_{Y,X} \circ \beta_{X,Y} = \mathrm{id}_{X \otimes Y}$
for all objects $X, Y$.

**Mathlib reference.**
`CategoryTheory.SymmetricCategory` (class), extending `BraidedCategory`.
Import: `Mathlib.CategoryTheory.Monoidal.Braided.Basic`.
The symmetry condition is `braiding_swap_eq_id`.
<!-- FILE_END: glossary-symmetric-monoidal-category.md -->

<!-- FILE_START: glossary-monoidal-functor.md -->
**:defterm[Monoidal functor]{#monoidal-functor}.** A functor $F \colon \mathbf{C} \to \mathbf{D}$
between monoidal categories equipped with a natural transformation
$\mu_{X,Y} \colon F(X) \otimes F(Y) \to F(X \otimes Y)$ and a
morphism $\epsilon \colon \mathbf{1}_{\mathbf{D}} \to F(\mathbf{1}_{\mathbf{C}})$,
compatible with the associator and unitors.

Mathlib distinguishes *lax* monoidal functors (where $\mu$ and
$\epsilon$ are arbitrary morphisms) from *strong* monoidal functors
(where they are isomorphisms).

**Mathlib reference.**
`CategoryTheory.Functor.LaxMonoidal` (class) — lax monoidal structure.
`CategoryTheory.Functor.OplaxMonoidal` (class) — oplax monoidal structure.
`CategoryTheory.Functor.Monoidal` (class) — strong monoidal (both lax and oplax, coherently).
Import: `Mathlib.CategoryTheory.Monoidal.Functor`.
<!-- FILE_END: glossary-monoidal-functor.md -->

