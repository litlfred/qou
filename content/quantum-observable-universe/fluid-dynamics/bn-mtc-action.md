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

*Proof.*
Well-definedness of $\rho_n$ is the coherence theorem for braided
monoidal categories: the assignment $\sigma_i \mapsto c_i$ satisfies
the braid relations $\sigma_i \sigma_{i+1} \sigma_i =
\sigma_{i+1} \sigma_i \sigma_{i+1}$ by the hexagon axiom for $c$,
and $\sigma_i \sigma_j = \sigma_j \sigma_i$ for $|i - j| \geq 2$ by
the interchange law.

Non-factorisation through $S_n$: the symmetric group relation
$\sigma_i^{\,2} = e$ would force
$\rho_n(\sigma_i^{\,2}) = c_{\mathbf{V}, \mathbf{V}}^{\,2}
= \mathrm{id}_{\mathbf{V} \otimes \mathbf{V}}$
on the $i$-th factor.  But by the non-symmetric braiding clause of
[def:observable-mtc](#def:observable-mtc) there exists a simple
$\mathbf{V}$ with $c_{\mathbf{V},\mathbf{V}}^{\,2}
\neq \mathrm{id}$, which contradicts the symmetric-group relation.
$\square$

**Corollary.**  The tensor powers $\mathbf{V}^{\otimes n}$ carry
*fractional statistics*: particle exchange acts by a $B_n$-representation
that distinguishes the braid $\sigma_i$ from its inverse
$\sigma_i^{-1}$, in contrast with the symmetric-group action seen by
$q = 1$ observables ([rem:u1-phase-tube](#rem:u1-phase-tube)).
