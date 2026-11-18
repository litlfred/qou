**Proof.**
By ([Markov identification](#lem:feynman-markov-identification)), the Markov-weighted sum of seminormal block traces equals $\mathrm{tr}_M\bigl(\rho(\beta)\bigr)$. Only partitions with at most two rows carry nonzero weight, and on those $w_\lambda = \dim_q(V_\lambda)/\dim_q(V^{\otimes n})$. The partitions of $n$ with at most two rows are $(n - k, k)$ for $0 \leq k \leq \lfloor n/2 \rfloor$, so there are $\lfloor n/2 \rfloor + 1$ terms.

The rule for $\sigma_n^{-1}$ follows from the quadratic relation $\sigma_n^{-1} = \sigma_n - h$: $\mathrm{tr}_M(x\sigma_n^{-1}) = \mathrm{tr}_M(x\sigma_n) - h\,\mathrm{tr}_M(x) = (z - h)\,\mathrm{tr}_M(x)$.

By ([categorical mass as Markov trace](#prop:categorical-mass-markov)), the categorical mass at a single brane level is $|\mathrm{tr}_M(\rho(\beta))|$, which by the first step is the absolute value of the eigenbasis amplitude. $\square$
