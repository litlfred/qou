The **$q$-momentum** of a particle is the **braid writhe** of its *canonical* representative (the Gröbner–Shirshov normal form at the minimal level of the brane tower), weighted by the Hecke deformation parameter.

**Definition.**
Let $\beta \in B_n$ be the canonical braid representative of a particle knot $K = \hat{\beta}$ (braid closure), with generators $\sigma_{i_1}^{\epsilon_1} \cdots \sigma_{i_k}^{\epsilon_k}$ where $\epsilon_j = \pm 1$. The **$q$-momentum** is:

$$
  p_q(\beta) =  \sum_{j=1}^{k} [\epsilon_j]_q
  =  \sum_{j=1}^{k} \frac{q^{\epsilon_j} - q^{-\epsilon_j}}{q - q^{-1}}
  =  \sum_{j=1}^{k} \epsilon_j = w(\beta)
$$

where $[\epsilon]_q = (q^{\epsilon} - q^{-\epsilon})/(q - q^{-1})$ is the $q$-integer, defined for $q \neq \pm 1$ (so that $q - q^{-1} \neq 0$). On that domain, $[+1]_q = 1$ and $[-1]_q = -1$ *exactly*. Each crossing contributes precisely its sign, and the $q$-momentum coincides with the classical writhe $w(\beta)$ for all such $q$ rather than only in the limit $q \to 1$ (where the removable $0/0$ singularity of $[\pm 1]_q$ takes the same values $\pm 1$). The $q$-deformation operates trivially at single crossings; it would distinguish multi-strand contributions $|\epsilon| \geq 2$, but these do not occur in a braid word.

**Equivalently**, the $q$-momentum is the trace of the braid in the fundamental representation of $H_n(R, q)$:

$$
  p_q(\beta) =  \mathrm{tr}_{\mathrm{fund}}(\rho(\beta))
$$

where $\rho: B_n \to H_n(R, q)$ is the Hecke representation.

**Necessity of a canonical normal-form representative.**
The writhe is not a link invariant. Conjugation $\beta \mapsto \gamma\beta\gamma^{-1}$ (the horizontal direction of [the brane tower](#rem:markov-moves-brane-tower)) preserves it, but stabilisation $\beta \in B_n \mapsto \beta\sigma_n^{\pm 1} \in B_{n+1}$ presents the *same* link and shifts it by $\pm 1$. Accordingly, $p_q$ is a function of the braid word, and becomes a function of the particle only after the level is pinned; the framework pins it at the minimal level, where the surviving moves are horizontal. The single datum of the pair $(w, n)$ that survives the vertical move unaided is the parity $(w - n) \bmod 2$, which is the component parity of the closure and carries one bit, far too little to serve as $p_q$.
