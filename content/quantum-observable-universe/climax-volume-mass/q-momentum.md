The **$q$-momentum** of a particle is the writhe of its braid representative, weighted by the Hecke deformation parameter.

**Definition.**
Let $\beta \in B_n$ be a braid representative of a particle knot $K = \hat{\beta}$ (braid closure), with generators $\sigma_{i_1}^{\epsilon_1} \cdots \sigma_{i_k}^{\epsilon_k}$ where $\epsilon_j = \pm 1$. The **$q$-momentum** is:

$$
  p_q(\beta) =  \sum_{j=1}^{k} [\epsilon_j]_q
  =  \sum_{j=1}^{k} \frac{q^{\epsilon_j} - q^{-\epsilon_j}}{q - q^{-1}}
  =  \sum_{j=1}^{k} \epsilon_j = w(\beta)
$$

where $[\epsilon]_q = (q^{\epsilon} - q^{-\epsilon})/(q - q^{-1})$ is the $q$-integer, defined for $q \neq \pm 1$ (so that $q - q^{-1} \neq 0$). On that domain, $[+1]_q = 1$ and $[-1]_q = -1$ *exactly*. Each crossing contributes precisely its sign, and the $q$-momentum coincides with the classical writhe $w(\beta)$ for all such $q$ — not only in the limit $q \to 1$ (where the removable $0/0$ singularity of $[\pm 1]_q$ takes the same values $\pm 1$). The $q$-deformation operates trivially at single crossings; it would distinguish multi-strand contributions $|\epsilon| \geq 2$, but these do not occur in a braid word.

**Equivalently**, the $q$-momentum is the trace of the braid in the fundamental representation of $H_n(R, q)$:

$$
  p_q(\beta) =  \mathrm{tr}_{\mathrm{fund}}(\rho(\beta))
$$

where $\rho: B_n \to H_n(R, q)$ is the Hecke representation.

**Building block values.**

| Knot | Braid word | Writhe $w$ | $p_q(q_0)$ |
|------|-----------|:----------:|:-------------:|
| $0_1$ (unknot) | $e$ | $0$ | $0$ |
| $3_1$ (trefoil) | $\sigma_1^3$ | $+3$ | $+3$ |
| $3_1^{\sigma}$ | $\sigma_1^{-3}$ | $-3$ | $-3$ |
| $4_1$ (figure-eight) | $\sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$ | $0$ | $0$ |
| $5_1$ (cinquefoil) | $\sigma_1^5$ | $+5$ | $+5$ |
