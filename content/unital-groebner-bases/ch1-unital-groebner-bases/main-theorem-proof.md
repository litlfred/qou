Let $f \in A$. The [division algorithm](#def:division-algorithm)
writes $f = r + \tilde{f}$ with $r \in O(I)$ and $\tilde{f} \in I$.
By [Lemma (generator choice)](#lem:generator-choice), we can take
$r \in \tilde{O}(G)$. As $f$ is arbitrary, $A = I + \tilde{O}(G)$.

It remains to show the sum is direct, which follows from uniqueness
of $r$. Suppose the division algorithm produces two representations:

$$
  f = \tilde{f} + r = \tilde{f}' + r'.
$$

Then $\tilde{f} - \tilde{f}' \in I$, so $r - r' \in I$. If
$r - r' \neq 0$, then by
[Lemma (generator choice)](#lem:generator-choice) there exists
$g_\gamma \in G$ with $\mathrm{LT}(g_\gamma) \mid (r - r')$.
But by construction of $r$ and $r'$, no such $g_\gamma$ exists —
contradiction. Thus $r = r'$ and the sum is direct.
