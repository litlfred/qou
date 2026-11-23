Let $F(z, c) \in R[z, c]$ be the color-tube cubic ([color-tube cubic](#rem:color-tube-cubic)) with roots $c_1(z), c_2(z), c_3(z)$ over the categorical base ring $R$. Let $\mathrm{S}_3$ act on the three color sheets by permutation. The canonical Wedderburn decomposition is

$$
  R[\mathrm{S}_3]
  \;\cong\;
  R \oplus R \oplus R^{2 \times 2}
  \quad
  (\text{trivial} \;\oplus\; \text{sign} \;\oplus\; \text{standard}).
$$

Write $v_k := dc_k/dz$ for the color-sheet velocities. The integrand

$$
  \lambda_{\mathrm{baryon}}(z)
  \;:=\;
  \prod_{1 \leq i < j \leq 3} (v_j - v_i)
  \;=\;
  (v_2 - v_1)(v_3 - v_1)(v_3 - v_2)
$$

is the Vandermonde in the velocities. It spans the lowest-degree part of the $\mathrm{Alt}^3$ (sign) isotype of $R[v_1, v_2, v_3]$ under the $\mathrm{S}_3$ action permuting the sheets: every sign-isotypic polynomial is $\lambda_{\mathrm{baryon}}$ times a symmetric one. The sum $\sum_k v_k$ spans the degree-one part of the trivial isotype. The product $\prod_k v_k$ is symmetric under sheet exchange and lies in the trivial isotype, not the sign isotype.

The integrand is $R$-rational up to the square root of the discriminant: $\lambda_{\mathrm{baryon}} = r(z)\, V_3(c_1, c_2, c_3)$ with $r \in R(z)$, and $V_3(c_1, c_2, c_3)^2 = \Delta(z) \in R[z]$. This purely algebraic statement holds over $R$ and does not use the archimedean fibre functor $\tau \colon R \to \mathbb{R}$.

The $\mathrm{Alt}^3$ isotype is a *genuinely non-trivial* sign line, not a channel indistinguishable from the trivial one. The monodromy of the color-tube cubic around its discriminant is the full $\mathrm{S}_3$ — computed exactly over $R = \mathbb{Q}[z]$ and cross-checked at $50$ digits (six simple branch points, each a transposition, together generating $\mathrm{S}_3$; [monodromy witness](../../../computations/probes/bring-cubic-monodromy-probe.witness.json)) — so its sign character is surjective onto $\{\pm 1\}$. Fixing the baryon to this sign isotype therefore fixes the integrand up to a scalar.
