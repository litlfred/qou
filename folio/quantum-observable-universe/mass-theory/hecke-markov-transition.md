The Hecke algebra $H_n(R, q)$ and the Jones-Markov trace admit a direct probabilistic interpretation: each Hecke generator acts as a stochastic transition operator. The product factorization corresponds to independent one-step expectations along a Markov chain.

**Proposition.**
*Let $H_n(R, q)$ be the Iwahori-Hecke algebra.*

**(i)** *Spectral idempotents.*
*The orthogonal idempotents*
$$
  e_+^{(i)} = \frac{\sigma_i + q^{-1}}{q + q^{-1}}, \qquad
  e_-^{(i)} = \frac{q - \sigma_i}{q + q^{-1}}
$$
*satisfy $e_+^{(i)} + e_-^{(i)} = 1$, $(e_\pm^{(i)})^2 = e_\pm^{(i)}$, and $e_+^{(i)} e_-^{(i)} = 0$. They reconstruct the generator as $\sigma_i = q \cdot e_+^{(i)} - q^{-1} \cdot e_-^{(i)}$.*

**(ii)** *Transition probabilities.*
*The symmetric and antisymmetric transition probabilities are $p_+ = q^2/(q^2 + 1)$ and $p_- = 1/(q^2 + 1)$. The stochastic transition operator at generator $i$ is $K_i = p_+ \cdot \mathrm{id} + p_- \cdot s_i$, a row-stochastic matrix. The system stays in its configuration with probability $p_+$ or transposes with probability $p_-$.*

**(iii)** *Markov property as memorylessness.*
*The Markov trace property requires the transition at generator $n$ to depend only on the eigenvalue structure of $\sigma_n$, not on the history in $H_{n-1}(q)$. The expectation value of the $i$-th crossing is $\mathbb{E}[\hat{V}_i] = z \cdot a_i + b_i = \hat{V}_i$, recovering the vertex volume.*

**(iv)** *Independence and factorization.*
*The product formula factors as independent one-step expectations only when each generator occurs at most once in the word. Then the Markov property peels one generator at a time and $\mathrm{tr}_M(\sigma_{i_1}\cdots\sigma_{i_\ell}) = z^{\ell}$. When a generator repeats the factorisation fails: for $w = \sigma_1\sigma_2\sigma_1$, $\mathrm{tr}_M(w) = h z^2 + z$ with $h = q - q^{-1}$, not $z^3$. So in general a vertex volume is not determined locally; it depends on the other generators in the word.*

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
