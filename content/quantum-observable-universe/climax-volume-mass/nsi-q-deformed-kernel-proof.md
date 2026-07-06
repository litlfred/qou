**Proof.**
For $q \neq 1$, the braiding $\check{R} = \sigma \circ \mathcal{R}$ is non-trivial. The categorical mass acquires a singular contribution from non-adjacent strand proximity. Specifically, because $\mathfrak{m}(\varrho)$ depends on the $q$-Hodge star $\star_q$ ([Definition](#def:q-hodge-star)), the cost of two non-adjacent points $\varrho(s), \varrho(t)$ approaching is governed by the $q$-deformed commutator:

$$
  [\hat{X}, \hat{P}]_q
  = 
  \hat{X}\hat{P} - q\hat{P}\hat{X}
  = 
  i\hbar_q.
$$

This replaces the classical $1/r^2$ repulsion kernel with a strictly stronger kernel:

$$
  \frac{1}{\lvert \varrho(s) - \varrho(t) \rvert^2}
   \longmapsto 
  \frac{[2]_q}{\lvert \varrho(s) - \varrho(t) \rvert^2 - \hbar_q^{2}},
$$

where $[2]_q = q + q^{-1}$ and $\hbar_q = 1 - q^{-1}$. This kernel introduces a hard singularity at $\lvert \varrho(s) - \varrho(t) \rvert = \hbar_q$, erecting an energy barrier of infinite height at the quantum scale. $\square$
