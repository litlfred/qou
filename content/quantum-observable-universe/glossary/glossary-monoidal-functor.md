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
