**Proposition (conditional on [`conj:classical-limit-stpart`](#conj:classical-limit-stpart) — classical limit).**
*In the $q \to 1$ limit of the categorical trace, the following degenerations occur:*

1. **(Hecke $\to$ symmetric group.)**
   *The Hecke relation $(T - q)(T + q^{-1}) = 0$ becomes $T^2 = 1$. The Iwahori--Hecke algebra $H_n(R, q)$ degenerates to the group algebra $k[S_n]$.*

2. **(Markov trace $\to$ flat character trace.)**
   *The Jones--Markov trace parameter $z \to 0$. The Markov trace $\mathrm{tr}_M$ on $H_n(R, q)$ degenerates to the augmentation map $\varepsilon \colon k[S_n] \to k$ sending every group element to $1$.*

3. **(Categorical action $\to$ classical action.)**
   *The categorical action $\mathfrak{S}_q(K) = \mathrm{tr}_M(\rho(\beta)) \to \mathfrak{S}_1(\beta)$, the character of the permutation $\pi(\beta) \in S_n$. The $q$-energy reduces to the classical action because the rotational and translational terms vanish with $\hbar_q = 1 - q^{-1} \to 0$.*

4. **(Eigenbasis collapse.)**
   *The Jones polynomial evaluates to $J_K(1) = 1$ for every knot $K$. The Markov trace ceases to distinguish knot types. The eigenspace decomposition $V^{\otimes n} \cong \bigoplus_\lambda V_\lambda \otimes S_\lambda$ persists, but the $S_\lambda$ become Specht modules of $S_n$, forming the standard angular momentum eigenbasis. The quantum dimensions $[2j+1]_q$ become ordinary dimensions $2j+1$.*

5. **(Braiding $\to$ symmetric.)**
   *The braiding $c_{V,V}$ satisfies $c_{V,V}^2 = \mathrm{id}$, making the monoidal category symmetric. The non-trivial knot structure collapses, reducing all braid closures to the unknot.*

*The finite categorical trace degenerates to the standard discrete trace over the finite-dimensional angular momentum eigenbasis of the symmetric group.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
