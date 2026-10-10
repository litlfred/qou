**Theorem (conditional on the $B_3(\mathbb{C})$ $\mathcal{O}(\alpha^2)$ normalization class).**
*Let $q$ be the substrate parameter and write*

$$
  T \;=\; q\cdot[9]_q\cdot[10]_q + \frac{2}{3\pi},
  \qquad
  H \;=\; \frac{[2]_q}{8\pi},
  \qquad
  h \;=\; \frac{q-1}{q}.
$$

*Assume the typeclass [`QOU.ArchimedeanUniverse.AlphaEmFixedPointNormalization`](em-coupling-fixed-point.lean) is inhabited at $(q,\alpha)$. The exact $\mathcal{O}(\alpha^2)$ self-energy normalization of the coupling equation is $H\cdot(1-h^2\alpha)$. This is the archimedean image of a class in the Bloch group $B_3(\mathbb{C})$. Consequently, $\alpha$ solves the self-consistent fixed point:*

$$
  \frac{1}{\alpha}
  \;=\;
  T + \alpha\,H\,\bigl(1 - h^2\alpha\bigr).
$$

*Then $\alpha$ is a root of the characteristic cubic:*

$$
  P(\alpha)
  \;=\;
  -h^2 H\,\alpha^3 + H\,\alpha^2 + T\,\alpha - 1
  \;=\; 0,
$$

*and its inverse yields CODATA-consistency: $\lvert \alpha^{-1} - 137.035999177\rvert < 10^{-3}$.*
