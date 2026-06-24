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
$\qquad\blacksquare$
