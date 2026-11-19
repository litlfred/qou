## Statement

*Let $H_n(q)$ denote the Iwahori-Hecke algebra of type $A_{n-1}$ with Hecke quadratic relation:*

$$
  \sigma_i^2 \;=\; h\,\sigma_i + 1, \qquad h \;=\; q - q^{-1}.
$$

*Let $\mathrm{tr}_M : \bigsqcup_n H_n(q) \to \mathbb{Q}(q)$ be the Markov trace ([categorical mass as Markov trace](#prop:categorical-mass-markov)). It is uniquely determined by:*

$$
  \mathrm{tr}_M(1) = 1, \qquad
  \mathrm{tr}_M(\alpha \sigma_n) = z \cdot \mathrm{tr}_M(\alpha) \;\text{for}\; \alpha \in H_n \subset H_{n+1}, \qquad
  \mathrm{tr}_M(\alpha\beta) = \mathrm{tr}_M(\beta\alpha),
$$

*with $z = q^{3}/(q^{2}+1)$ (**convention D**). Then for the proton's atomic-braid word $\sigma_1^7 \sigma_2^4 \in H_3(q)$, the Markov trace admits the closed-form expression:*

$$
  \mathrm{tr}_M(\sigma_1^7 \sigma_2^4)(q)
   \;=\; a_7 a_4 \, z^2 \;+\; (a_7 b_4 + b_7 a_4)\, z \;+\; b_7 b_4,
$$

*where $(a_k, b_k)$ are the polynomials in $h$ defined by the Hecke-power recurrence $a_{k+1} = h\,a_k + b_k$, $b_{k+1} = a_k$, $a_0 = 0$, $b_0 = 1$. After substituting $h = q - q^{-1}$ and $z = q^{3}/(q^{2}+1)$ and rationalising, the denominator factors as $q^{7}(q^{2}+1)^{2}$ — one factor of $q^{2}+1$ per Markov peel, which is the convention-D signature.*
