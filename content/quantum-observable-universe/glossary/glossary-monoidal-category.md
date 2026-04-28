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
