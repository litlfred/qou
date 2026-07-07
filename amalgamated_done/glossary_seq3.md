<!-- FILE_START: glossary-r-linear-category.md -->
**:defterm[$R$-linear category]{#r-linear-category}.** A category whose hom-sets carry the structure of $R$-modules (for a commutative ring $R$) such that composition is $R$-bilinear.

**Mathlib reference.**
`CategoryTheory.Linear R` (class).
Import: `Mathlib.CategoryTheory.Linear.Basic`.
<!-- FILE_END: glossary-r-linear-category.md -->

<!-- FILE_START: glossary-no-quasi-zeros.md -->
**Algebra without quasi-zeros.** Let $R$ be a commutative ring with unity and $A$ an $R$-algebra. An element $a \in A$ is a **quasi-zero** if

$$
  bac = 0 \qquad \text{for all } b, c \in A \text{ not both } 1.
$$

The algebra $A$ is **without quasi-zeros** if no such element exists. We assume that $R$ has no quasi-zeros. This ensures that leading-term decompositions are well-defined and the division algorithm terminates correctly. It guarantees that $R$-linear hom-spaces have no phantom morphisms annihilated by all compositions, making the Frobenius pairing non-degenerate.
<!-- FILE_END: glossary-no-quasi-zeros.md -->

<!-- FILE_START: glossary-cemetery-group.md -->
**:refterm[Cemetery group]{#cemetery-group}.** The cemetery group $\mathcal{Z}_n \subset \mathcal{K}_n$ is the localising subcategory of graded projective KLR modules annihilated by the fibre functor $\tau$. It acts as a homological pruning filter on the Gröbner–Shirshov reduction engine. A state word that lands in $\mathcal{Z}_n$ is buried: its image under any subsequent observation vanishes, allowing the computation branch to be dropped.
<!-- FILE_END: glossary-cemetery-group.md -->
