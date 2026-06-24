**Proposition.**
Let $\mathbf{C}_{\mathrm{any}}(N)$ be the observable modular tensor
category of [def:observable-mtc](#def:observable-mtc) at level $N \geq 3$,
and let $\mathbf{V}$ be a non-trivial simple object.  For every
$n \geq 2$ the categorical braiding defines a representation

$$
  \rho_n \colon B_n  \longrightarrow
   \mathrm{Aut}_{\mathbf{C}_{\mathrm{any}}(N)}(\mathbf{V}^{\otimes n}),
  \qquad
  \sigma_i  \longmapsto
   \mathrm{id}_{\mathbf{V}^{\otimes (i-1)}}
   \otimes\, c_{\mathbf{V}, \mathbf{V}}
   \otimes\, \mathrm{id}_{\mathbf{V}^{\otimes (n - i - 1)}},
$$

of the Artin braid group $B_n$ (see
[def:braid-group](#def:braid-group)) on the tensor power of
$\mathbf{V}$.  This representation does not factor through the
symmetric-group quotient $B_n \twoheadrightarrow S_n$.

**Consequence.**  The tensor powers $\mathbf{V}^{\otimes n}$ carry
*fractional statistics*: particle exchange acts by a $B_n$-representation
that distinguishes the braid $\sigma_i$ from its inverse
$\sigma_i^{-1}$, in contrast with the symmetric-group action seen by
$q = 1$ observables ([rem:u1-phase-tube](#rem:u1-phase-tube)).
