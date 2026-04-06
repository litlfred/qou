*Proof of [Theorem 2](#thm:ugb-main).* Let $f$ be an element of $A$. The
division algorithm allows us to write $f = r + \tilde{f}$ with $r \in O(I)$ and
$\tilde{f} \in I$. By [Lemma 6](#lem:ugb-generator-choice) we can take
$r \in \widetilde{O}(G)$. As $f$ is arbitrary, we have:

$$A = I + \widetilde{O}(G)$$

It remains to show that this sum is direct, which follows from uniqueness of $r$.
Suppose the algorithm produces two representations:

$$f = \tilde{f} + r = \tilde{f}' + r'$$

Then $\tilde{f} - \tilde{f}' \in I$ so that $r - r' \in I$. If $r - r' \neq 0$,
then [Lemma 6](#lem:ugb-generator-choice) shows there is some $g_\gamma \in G$
with $\LT(g_\gamma) \mid (r - r')$. But by construction of $r$ and $r'$, no such
$g_\gamma$ exists — a contradiction. $\square$
