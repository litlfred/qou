*Let $q > 0$ and let $z$ denote the Markov weight, so that on the 6-element
Gröbner–Shirshov normal-form basis
$(b_0, \dots, b_5) = (1, \sigma_0, \sigma_1, \sigma_0\sigma_1, \sigma_1\sigma_0,
\sigma_0\sigma_1\sigma_0)$ of $H_3(q)$ the Markov trace takes the values
$\mathrm{tr}_M(b_i) = (1, z, z, z^2, z^2, hz^2 + z)$ with $h = q - q^{-1}$.
Let $G(q,z)$ be the Gram matrix $G[i,j] = \mathrm{tr}_M(b_i b_j)$. Then:*

1. *$G(q,z)$ is symmetric and $G[0,0] = 1$, for every $z$.*

2. *The determinant factors as*

$$
  \det G(q,z) \;=\; -\,\frac{(z-q)^5\,(qz+1)^5\,\bigl((q^2+1)z - q^3\bigr)\,
                              (q^3 z + qz + 1)}{q^8}.
$$

3. *At the canonical Markov weight $z = q^3/(q^2+1)$ the third factor vanishes
   identically in $q$. Hence $\det G = 0$ for every $q$; the form has rank $5$,
   and its radical is spanned by $(-q^3,\, q^2,\, q^2,\, -q,\, -q,\, 1)$ — the
   three-strand $q$-antisymmetriser $\sum_i (-q^{-1})^{\ell_i} b_i$ up to scale,
   where $\ell_i$ is the word length of $b_i$. In particular $G$ is not positive
   definite.*

4. *At the Markov weight $z = \sqrt{q}/(q+1)$ one has instead
   $\det G \neq 0$ whenever $\sqrt{q} > 1$.*
