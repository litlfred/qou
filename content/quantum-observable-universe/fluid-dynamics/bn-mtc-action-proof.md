*Proof.*
The coherence theorem for braided monoidal categories ensures the well-definedness of $\rho_n$. The assignment $\sigma_i \mapsto c_i$ satisfies the braid relations $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ via the hexagon axiom for $c$. The interchange law yields $\sigma_i \sigma_j = \sigma_j \sigma_i$ for $|i - j| \geq 2$.

The representation does not factor through $S_n$. The symmetric group relation $\sigma_i^{\,2} = e$ forces $\rho_n(\sigma_i^{\,2}) = c_{\mathbf{V}, \mathbf{V}}^{\,2} = \mathrm{id}_{\mathbf{V} \otimes \mathbf{V}}$ on the $i$-th factor. The non-symmetric braiding clause of [def:observable-mtc](#def:observable-mtc) guarantees a simple $\mathbf{V}$ with $c_{\mathbf{V},\mathbf{V}}^{\,2} \neq \mathrm{id}$. This contradicts the symmetric-group relation. $\square$

**Corollary.** The tensor powers $\mathbf{V}^{\otimes n}$ carry *fractional statistics*. Particle exchange acts by a $B_n$-representation that distinguishes the braid $\sigma_i$ from its inverse $\sigma_i^{-1}$. This contrasts with the symmetric-group action of $q = 1$ observables ([rem:u1-phase-tube](#rem:u1-phase-tube)).
