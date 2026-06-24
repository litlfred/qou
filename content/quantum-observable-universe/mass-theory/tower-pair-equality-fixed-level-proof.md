By the Markov-trace factorization theorem
([`thm:markov-trace-factorization`](#thm\:markov-trace-factorization)),
the level-$n$ Markov trace of a product of factors decomposes as a
sum over subset structures with weights determined by the Markov
parameter $z$. For a pair $(i, j) \in \mathcal{P}_n$, the
two-factor subset contributes the weight $z^2$ (from
[`prop:markov-pair-z2`](#prop\:markov-pair-z2): $\mathrm{tr}_M(\sigma_i \sigma_j) = z \cdot z = z^2$,
adjacent or not). The dilogarithm $\Phi_q$ applied to the absolute
value of the pair product $|\hat V_i^{(n)} \hat V_j^{(n)}|$ is the
quantum-dilogarithm regularization of the pair's contribution to the
jet-tower mass.

Pair commutativity
[`lem:vhat-pair-commutation-trace`](#lem\:vhat-pair-commutation-trace)
ensures the pair index $(i, j)$ vs $(j, i)$ does not double-count
(the absolute value $|\hat V_i^{(n)} \hat V_j^{(n)}| = |\hat V_j^{(n)} \hat V_i^{(n)}|$
is symmetric). Summing over $\mathcal{P}_n$ — the set of unordered
pairs — gives the level-$n$ pair contribution

$$
  \mathrm{pairs}_n
  \;=\;
  z^2 \sum_{(i, j) \in \mathcal{P}_n}
    \Phi_q\!\bigl(\bigl|\hat V_i^{(n)} \hat V_j^{(n)}\bigr|\bigr),
$$

as an exact equality. $\square$
