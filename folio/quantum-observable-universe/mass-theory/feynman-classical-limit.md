**Proposition (conditional on [classical limit standard-partition conjecture](#conj:classical-limit-stpart) — classical limit).**
*In the $q \to 1$ limit of the categorical trace, the following degenerations occur:*

$$
  H_n(R, q) \xrightarrow{\,q \to 1\,} k[S_n], \qquad
  \mathrm{tr}_M(w) \xrightarrow{\,q \to 1\,} 2^{-(n - c(w))}.
$$

1. **(Hecke $\to$ symmetric group.)**
   *The Hecke relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ becomes $\sigma_i^2 = 1$. The Iwahori--Hecke algebra $H_n(R, q)$ degenerates to the group algebra $k[S_n]$.*

2. **(Markov trace $\to$ flat character trace.)**
   *The Jones--Markov trace parameter $z = q^3/(q^2+1)$ tends to $z(1) = 1/2$. The Markov trace degenerates to $\mathrm{tr}_M(w) = 2^{-(n - c(w))}$ on $w \in S_n$, where $c(w)$ is the number of cycles of $w$. This is the normalised character of $w$ permuting the tensor factors of $(k^2)^{\otimes n}$. It is not the augmentation $\varepsilon$, which is the trace at $z = 1$; the limit $z \to 0$ would instead give the regular trace $w \mapsto \delta_{w,1}$.*

3. **(Categorical action $\to$ classical action.)**
   *The categorical action $\mathfrak{S}_q(K) = \mathrm{tr}_M(\rho(\beta)) \to \mathfrak{S}_1(\beta)$, the normalised character of the permutation $\pi(\beta) \in S_n$ on $(k^2)^{\otimes n}$. The $q$-energy reduces to the classical action because the rotational and translational terms vanish with $\hbar_q = 1 - q^{-1} \to 0$.*

4. **(Eigenbasis collapse.)**
   *The Jones polynomial evaluates to $J_K(1) = 1$ for every knot $K$. The Markov trace ceases to distinguish knot types. The eigenspace decomposition $V^{\otimes n} \cong \bigoplus_\lambda V_\lambda \otimes S_\lambda$ persists, but the $S_\lambda$ become Specht modules of $S_n$, forming the standard angular momentum eigenbasis. The quantum dimensions $[2j+1]_q$ become ordinary dimensions $2j+1$.*

5. **(Braiding $\to$ symmetric.)**
   *The braiding $c_{V,V}$ satisfies $c_{V,V}^2 = \mathrm{id}$, making the monoidal category symmetric. The non-trivial knot structure collapses: the trace of a braid closure depends only on its number of components $c = c(\pi(\beta))$. With the normalisation $J = z^{-(n-1)}\,\mathrm{tr}_M$, every knot gives $1$ and a $c$-component link gives $2^{c-1}$.*

*The finite categorical trace degenerates to the standard discrete trace over the finite-dimensional angular momentum eigenbasis of the symmetric group.*
