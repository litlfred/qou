## Proof

By the Markov-trace factorization theorem
([nuclear Markov-trace factorization](#thm:markov-trace-factorization)),
the level-$n$ Markov trace of a product of factors decomposes as a
sum over subset structures with weights determined by the Markov
parameter $z$. For a pair $(i, j) \in \mathcal{P}_n$, the
two-factor subset contributes the weight $z^2$ (from
[all-pairs Markov-trace $z^2$ identity](#prop:markov-pair-z2): $\mathrm{tr}_M(\sigma_i \sigma_j) = z \cdot z = z^2$,
adjacent or not). The dilogarithm $\Phi_q$ applied to the absolute
value of the pair product $|\hat V_i^{(n)} \hat V_j^{(n)}|$ is the
quantum-dilogarithm regularization of the pair's contribution to the
jet-tower mass.

Pair commutativity
[traced-volume pair commutation](#lem:vhat-pair-commutation-trace)
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

## Nature of the empirical residual

The empirical table on light atoms
([jet-brane mass-tower pair comparison](#rem:mass-endomorphism-jet-tower))
shows that the all-pairs sum at jet level $0$ leaves a sub-1%
residual to CODATA — e.g., $0.57\%$ for $^6\mathrm{Li}$, $0.86\%$
for $^{16}\mathrm{O}$. The lemma above says **this residual is not
a sharpness gap in the level-$0$ pair formula** (the formula is
exact at level $0$); rather, the residual is the **level-$\ge 1$
contribution** of the brane tower not yet captured by the level-$0$
truncation.

This is consistent with the jet-tower formula
([jet-brane mass-tower formulation](#rem:mass-endomorphism-jet-tower)):

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \underbrace{\bigl|\textstyle\prod_i \hat V_i^{(0)}\bigr|}_{\text{descended (level 0)}}
  + \sum_{n=0}^{N}
      \Bigl(
        \underbrace{\textstyle\sum_i \Phi_q(|\hat V_i^{(n)}|)}_{\text{singletons}_n}
        + \underbrace{z^2 \textstyle\sum_{(i, j) \in \mathcal{P}_n}
            \Phi_q(|\hat V_i^{(n)} \hat V_j^{(n)}|)}_{\text{pairs}_n}
      \Bigr).
$$

Each term is exact at its level; the truncation error at level $N$
is bounded by
[brane-tower geometric tail bound](#prop:jet-tower-convergence) at
$\le \Delta_{\max}\,\hbar_q^{2(N+1)} / (1 - \hbar_q^2)$ once the
uniform $\Delta_{\max}$ bound is established (still open).
