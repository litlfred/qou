**Proposition.** *Let $S^{+}(0)$ and $S^{-}(0)$ be the leading ($q \to 0$)
coefficient matrices of the $5_2$ Stokes sandwich, as $3 \times 3$ integer
matrices. Then*

$$
\det S^{+}(0) = \det S^{-}(0) = 1,
\qquad
\bigl(S^{+}(0)\bigr)^{\mathsf{T}} \, S^{-}(0) = I .
$$

*Moreover the leading $W_{-1}$ block, which is rational rather than integral,
has*

$$
\det W_{-1}(0) = -2 .
$$

## What the three statements do

**Unimodularity.** $\det S^{\pm}(0) = 1$ is the leading-order instance of the
$\det S^{\pm}(q) = 1$ condition that a Stokes sandwich must satisfy. It is the
algebraic expression of the fact that Stokes matrices are transition data
between asymptotic sectors: they change the basis, they do not change the
volume.

**The inversion relation.** $(S^{+})^{\mathsf{T}} S^{-} = I$ at leading order
says the two chirality blocks are not independent — one is determined by the
other, transposed. This is the sense in which $S^{+}$ and $S^{-}$ are a
*sandwich* rather than two unrelated matrices, and it holds at each of the
first several orders in $q$, not only at $q^{0}$.

Note that the inversion relation constrains the pair without collapsing it.
Transposition is not the chirality involution: it relates the blocks while
leaving the ordered pair of off-diagonal constants genuinely ordered, which is
why the split recorded in
[The $5_2$ DT spectrum $\{3,4\}$ splits across chirality](#prop:fivetwo-dt-spectrum-split) survives.

**The $W_{-1}$ determinant.** The magnitude $2$ is the "$\det \pm 2$"
phenomenon of the $W_{-1}$ block. The sign matters and is easy to get wrong:
$W_{-1}(0)$ carries denominators of $6$ from the $c$-slot subtraction, so it
is a matrix over $\mathbb{Q}$ and its determinant is $-2$. An earlier framing
assumed a fitted integer $+2$; the honest statement is the rational one.

## Why these are Lean-provable

Every assertion above is a finite decidable identity about a concrete matrix
with rational entries. There is no analysis, no limit and no convergence
argument — the content is entirely in having the *right* matrices, which come
from the derived sandwich compute rather than from a fit.

That is also the limit of what is claimed. These are statements about the
leading coefficient matrices; the corresponding all-orders statements
($\det S^{\pm}(q) = 1$ as an identity of $q$-series, and Stokes integrality)
are checked numerically in the sandwich compute and are not formalised here.
