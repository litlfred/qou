**Proof.**
For $q \neq 1$, the braiding $\check{R} = \sigma \circ \mathcal{R}$
is non-trivial, and the categorical mass acquires a singular
contribution from non-adjacent strand proximity.  Concretely,
because $\mathfrak{m}(\varrho)$ depends on the $q$-Hodge star $\star_q$
([$q$-Hodge star](#def:q-hodge-star)), the cost of two non-adjacent
points $\varrho(s)$, $\varrho(t)$ approaching is governed by the
$q$-deformed commutator

$$
  [\hat{X}, \hat{P}]_q
  = 
  \hat{X}\hat{P} - q\hat{P}\hat{X}
  = 
  i\hbar_q,
$$

which replaces the classical $1/r^2$ repulsion kernel with the
strictly stronger

$$
  \frac{1}{\lvert \varrho(s) - \varrho(t) \rvert^2}
   \longmapsto 
  \frac{[2]_q}{\lvert \varrho(s) - \varrho(t) \rvert^2
  - \hbar_q^{2}},
$$

where $[2]_q = q + q^{-1}$ is the quantum integer and
$\hbar_q = 1 - q^{-1}$ is the quantum Planck constant.  This
kernel has a hard singularity at
$\lvert \varrho(s) - \varrho(t) \rvert = \hbar_q$, creating an
energy barrier of infinite height at the quantum scale.  $\square$
