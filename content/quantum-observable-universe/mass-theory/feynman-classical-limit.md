**Proposition (conditional on [`conj:classical-limit-stpart`](#conj:classical-limit-stpart) — classical limit).**
*In the $q \to 1$ limit of the categorical trace
([Feynman transition amplitude](#prop\:feynman-categorical-trace)),
the following degenerations occur:*

1. **(Hecke $\to$ symmetric group.)**
   *The Hecke relation $(T - q)(T + q^{-1}) = 0$ becomes
   $(T - 1)(T + 1) = 0$, i.e.\ $T^2 = 1$.  The Iwahori--Hecke algebra
   $H_n(R, q)$ degenerates to the group algebra $k[S_n]$ of the symmetric
   group
   ([Hecke algebra from braiding](#rem\:hecke-algebra-from-braiding)).*

2. **(Markov trace $\to$ flat character trace.)**
   *The Jones--Markov trace parameter
   $z = (q - 1)/(q^{1/2} + q^{-1/2})^2 \to 0$
   ([Jones--Markov trace](#thm\:jones-markov-trace)),
   and the Markov trace $\mathrm{tr}_M$ on $H_n(R, q)$ degenerates to
   the augmentation map
   $\varepsilon \colon k[S_n] \to k$ sending every group element to $1$.*

3. **(Categorical action $\to$ classical action.)**
   *The categorical action
   $\mathfrak{S}_q(K) = \mathrm{tr}_M(\rho(\beta)) \to \mathfrak{S}_1(\beta)$, the
   character of the permutation $\pi(\beta) \in S_n$ obtained by
   imposing $\sigma_i^2 = 1$ on the braid word.  The $q$-energy
   reduces to $\mathfrak{E}_1 = \mathfrak{S}_1$ because the rotational and
   translational terms vanish with $\hbar_q = 1 - q^{-1} \to 0$
   ([$q$-energy](#def\:q-energy)).*

4. **(Eigenbasis collapse.)**
   *The Jones polynomial $J_K(1) = 1$ for every knot $K$, so the
   Markov trace can no longer distinguish knot types.  The eigenspace
   decomposition $V^{\otimes n} \cong \bigoplus_\lambda V_\lambda \otimes S_\lambda$
   persists, but the $S_\lambda$ become Specht modules of $S_n$ ---
   the standard angular momentum eigenbasis of quantum mechanics.
   The quantum dimensions $[2j+1]_q$ become ordinary dimensions
   $2j+1$.*

5. **(Braiding $\to$ symmetric.)**
   *The braiding $c_{V,V}$ satisfies $c_{V,V}^2 = \mathrm{id}$, so
   the :refterm[monoidal category]{#monoidal-category} becomes symmetric.  The non-trivial
   knot structure that organises the sum at $q \neq 1$ collapses:
   all braid closures yield the unknot under the symmetric quotient.*

*In this limit, the finite categorical trace
$\sum_\lambda \dim_q(V_\lambda) \cdot \mathrm{tr}_{S_\lambda}(\rho(\beta))$
becomes the standard quantum-mechanical trace
$\sum_\lambda (2j+1) \cdot \mathrm{tr}_{S_\lambda}(\pi(\beta))$
over the angular momentum eigenbasis --- precisely the finite-basis
version of the Feynman path integral.*
