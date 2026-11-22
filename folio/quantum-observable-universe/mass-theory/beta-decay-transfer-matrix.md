Beta decay is mediated by the $T_{3,5}$ torus knot with $10$ crossings. The $T_{3,5}$ insertion at the converting quark produces a universal 2$\times$2 matrix-valued polynomial $\Delta_\beta(q)$ that governs every beta transition in every nucleus. The transfer matrix captures the effect of the $10$-crossing weak vertex on each nucleon pair.

## The three crossing transfer matrices

Each nucleon pair $(i, j)$ contributes a transfer matrix
$T(q) \in \mathrm{M}_2(\mathbb{Z}[\tfrac{1}{2}][q^{\pm 1}])$:

$$
  T(c, d) = 
  \begin{pmatrix}
    c(q - q^{-1}) + d & c \\
    c & d
  \end{pmatrix}
$$

with crossing coefficients $(c, d)$ depending on the pair type.
The $(1, -(q - q^{-1}))$ convention for nn crossings is the unique
convention consistent with the Hecke inverse relation
$\sigma^{-1} = \sigma - (q - q^{-1})$:

$$
  T_{pp}(q) =  T(1, 0) = 
  \begin{pmatrix}
    q - q^{-1} & 1 \\
    1 & 0
  \end{pmatrix},
  \quad
  T_{nn}(q) =  T(1, -(q - q^{-1})) = 
  \begin{pmatrix}
    0 & 1 \\
    1 & -(q - q^{-1})
  \end{pmatrix}
$$

$$
  T_{\mathrm{mix}}(q) =  T\!\left(1, -\tfrac{1}{2}(q - q^{-1})\right) = 
  \begin{pmatrix}
    \frac{1}{2}(q - q^{-1}) & 1 \\[4pt]
    1 & -\frac{1}{2}(q - q^{-1})
  \end{pmatrix}
$$

No fractional powers of $q$ appear.  $T_{pp}$ and $T_{nn}$ live in
$\mathrm{M}_2(\mathbb{Z}[q^{\pm 1}])$, but $T_{\mathrm{mix}}$ has the
entries $\pm\tfrac{1}{2}(q - q^{-1}) \notin \mathbb{Z}[q^{\pm 1}]$, so it
lives in $\mathrm{M}_2(\mathbb{Z}[\tfrac{1}{2}][q^{\pm 1}])$; the same
holds for $\Delta_\beta$ below.  The pp and nn transfer matrices
are unimodular: $\det T_{pp} = \det T_{nn} = -1$ (forced by the
Hecke eigenvalues $q \cdot (-q^{-1}) = -1$).  The mixed crossing
$\frac{1}{2}(\sigma + \sigma^{-1})$ is an algebraic average, not a
group element, so $\det T_{\mathrm{mix}} \neq -1$.

## The universal beta decay matrix

**Proposition.**
*The two elementary decay matrices $\Delta_\beta^{nn \to \mathrm{mix}}$
and $\Delta_\beta^{\mathrm{mix} \to pp}$ are identical:*

$$
  \Delta_\beta^{nn \to \mathrm{mix}}(q)
  =  T_{\mathrm{mix}}(q) - T_{nn}(q)
  =  T_{pp}(q) - T_{\mathrm{mix}}(q)
  =  \Delta_\beta^{\mathrm{mix} \to pp}(q)
$$

*There is a single universal beta decay matrix:*

$$
  \boxed{
    \Delta_\beta(q)
    = 
    \tfrac{1}{2}(q - q^{-1}) \mathbb{I}
  }
$$

*where $\mathbb{I}$ is the $2 \times 2$ identity.
The decay matrix is a scalar multiple of the identity — beta decay
uniformly scales all channels by $\frac{1}{2}(q - q^{-1})$.*
