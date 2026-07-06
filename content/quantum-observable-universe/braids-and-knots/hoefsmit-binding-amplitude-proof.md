**Proof.** The Hoefsmit seminormal matrix for $\sigma_2$ on $V_{(2,1)}$ has a $2 \times 2$ block with entries

$$
  a_\rho = \frac{h}{1 - q^{-2\rho}},
  \qquad
  a_{-\rho} = \frac{h}{1 - q^{2\rho}},
  \qquad
  b = \sqrt{a_\rho \cdot a_{-\rho} + 1},
$$

where $\rho = 2$ is the axial distance and $h = q - q^{-1}$. Their product is

$$
  a_\rho \cdot a_{-\rho}
  = \frac{h^2}{(1 - q^{-4})(1 - q^4)}
  = \frac{h^2}{-(h^2)(h^2 + 4)}
  = -\frac{1}{h^2 + 4}
  = -\frac{1}{[2]_q^2}.
$$

We find $b^2 = 1 - 1/[2]_q^2 = ([2]_q^2 - 1)/[2]_q^2$. Expanding the $q$-integers gives $[2]_q^2 = (q + q^{-1})^2 = h^2 + 4$ and $[3]_q = q^2 + 1 + q^{-2} = h^2 + 3 = [2]_q^2 - 1$. This implies

$$
  b^2 = \frac{[2]_q^2 - 1}{[2]_q^2} = \frac{[3]_q}{[2]_q^2}.
  \qquad\square
$$
