**:defterm[Hom-set]{#hom-set}.** For objects $X$ and $Y$ in a category $\mathbf{C}$, the
*hom-set* $\mathrm{Hom}_{\mathbf{C}}(X, Y)$ (also written
$\mathbf{C}(X, Y)$ or $X \to Y$) is the collection of all morphisms
from $X$ to $Y$. In a *locally small* category, each hom-set is a
genuine set (as opposed to a proper class).

When $\mathbf{C}$ is $R$-linear
([§Enrichment](#rem:glossary-r-linear-category)), each hom-set carries
the structure of an $R$-module, and composition is $R$-bilinear.

**Mathlib reference.**
In Mathlib, the hom-set from `X` to `Y` is denoted `X ⟶ Y`
(using the `⟶` notation from `CategoryTheory.Category`).
Import: `Mathlib.CategoryTheory.Category.Basic`.
The type is `CategoryTheory.Category.Hom X Y`, but it is almost
always accessed via the notation `X ⟶ Y`.
