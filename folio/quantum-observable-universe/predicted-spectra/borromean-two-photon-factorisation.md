*Let $h = q - q^{-1}$ and $V = \sigma_0\sigma_1^{-1} \in H_3(R,q)$. Then*

$$
  (\sigma_0\sigma_1^{-1})^3 = (\mathbf{1} + q h\, V)\,(\mathbf{1} - q^{-1} h\, V).
$$

*Since $\sigma_1^{-1} = \sigma_1 - h$, we have $V = \sigma_0\sigma_1 - h\,\sigma_0$. Each factor is therefore a [photon](#def:photon) with $\varphi_1 = 0$:*

$$
  \mathbf{1} + q h\, V = \gamma(-q h^2,\, 0,\, q h),
  \qquad
  \mathbf{1} - q^{-1} h\, V = \gamma(q^{-1} h^2,\, 0,\, -q^{-1} h).
$$

The two weights are $h$ times the two eigenvalues $q$ and $-q^{-1}$ of a generator $\sigma_i$.

**Proof.** In $H_3(R,q)$ the element $V$ satisfies

$$
  V^3 + h^2 V^2 - h^2 V - \mathbf{1} = (V - \mathbf{1})\bigl(V^2 + (1 + h^2)V + \mathbf{1}\bigr) = 0.
$$

To see this, write $V = \sigma_0\sigma_1 - h\sigma_0$, expand $V^2$ and $V^3$, and reduce with $\sigma_i^2 = h\sigma_i + \mathbf{1}$ and $\sigma_1\sigma_0\sigma_1 = \sigma_0\sigma_1\sigma_0$. Expanding the right-hand side with $q q^{-1} = 1$ gives $\mathbf{1} + h^2 V - h^2 V^2$, which equals $V^3$ by the cubic relation. $\square$

The two factors are polynomials in $V$, so they commute.
