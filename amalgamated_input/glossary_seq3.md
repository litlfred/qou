<!-- FILE_START: glossary-r-linear-category.md -->
**:defterm[$R$-linear category]{#r-linear-category}.** A category whose hom-sets carry the
structure of $R$-modules (for a commutative ring $R$) such that
composition is $R$-bilinear. This is a light terminological wrapper:
the paper's "$R$-linear" is Mathlib's `Linear R` (which refines
`Preadditive`).

When $R = \mathbb{Z}$, an $R$-linear category is a preadditive
category. The quantum universe axioms
([Definition](#def:quantum-universe)) require $R$-linearity for the
hom-spaces of the underlying rigid :refterm[monoidal category]{#monoidal-category}.

**Mathlib reference.**
`CategoryTheory.Linear R` (class), for a `CommSemiring R`.
Import: `Mathlib.CategoryTheory.Linear.Basic`.
Extends: `CategoryTheory.Preadditive` (the $\mathbb{Z}$-linear case).
Import for preadditive: `Mathlib.CategoryTheory.Preadditive.Basic`.

**Note.** The paper writes "$R$-linear category" where Mathlib writes
`[Linear R C]` as a typeclass on a category `C`. No semantic
difference — only a naming convention.
<!-- FILE_END: glossary-r-linear-category.md -->

<!-- FILE_START: glossary-no-quasi-zeros.md -->
**Algebra without quasi-zeros.** Let $R$ be a commutative ring
with unity and $A$ an $R$-algebra.  An element $a \in A$ is a
**quasi-zero** if

$$
  bac = 0 \qquad \text{for all } b, c \in A \text{ not both } 1.
$$

The algebra $A$ is **:defterm[without quasi-zeros]{#no-quasi-zeros}** if no such element
exists.  Throughout this paper, whenever $\mathbf{C}$ is
$R$-linear we assume that $R$ has no quasi-zeros.  This condition
is central to the theory of unital Gröbner–Shirshov bases
\cite{leitnerpawloski2004}, where it ensures that leading-term
decompositions are well-defined and the division algorithm
terminates correctly.  In the categorical setting it guarantees
that $R$-linear hom-spaces have no phantom morphisms annihilated
by all compositions — a necessary condition for the Frobenius
pairing to be non-degenerate.
<!-- FILE_END: glossary-no-quasi-zeros.md -->

<!-- FILE_START: glossary-cemetery-group.md -->
**:refterm[Cemetery group]{#cemetery-group}.** The :refterm[cemetery group]{#cemetery-group}
$\mathcal{Z}_n \subset \mathcal{K}_n$ is the localising subcategory
of graded projective KLR modules annihilated by the fibre functor
$\tau$ (graded Euler characteristic).  See
[:refterm[cemetery group]{#cemetery-group}](#def:cemetery-group) for the formal definition and
[cemetery-group emergence](#conj:cemetery-group-emergence) for its
algorithmic role as a homological pruning filter on the
Gröbner–Shirshov reduction engine.  The terminology is
deliberately algorithmic: a state word that lands in
$\mathcal{Z}_n$ is "buried" — its image under any subsequent
observation vanishes, so the computation branch is dropped.
<!-- FILE_END: glossary-cemetery-group.md -->

