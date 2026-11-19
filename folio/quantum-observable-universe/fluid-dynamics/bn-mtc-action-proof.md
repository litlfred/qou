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
[the observable modular tensor category](#def:observable-mtc) there exists a simple
$\mathbf{V}$ with $c_{\mathbf{V},\mathbf{V}}^{\,2}
\neq \mathrm{id}$, which contradicts the symmetric-group relation.
$\square$

**Corollary.**  The tensor powers $\mathbf{V}^{\otimes n}$ carry
*fractional statistics*: particle exchange acts by a $B_n$-representation
that distinguishes the braid $\sigma_i$ from its inverse
$\sigma_i^{-1}$, in contrast with the symmetric-group action seen by
$q = 1$ observables ([the single $\mathrm{U}(1)$ phase tube](#rem:u1-phase-tube)).
