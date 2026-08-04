*Let $G \in \mathbb{R}^{6 \times 6}$ be the Gram matrix of $H_3(q)$ at $q = q_0$. Consider the linear program:*

$$
  \min_{x \in \mathbb{R}^6} \;
  \sum_{i=1}^{6} t_i x_i
  \qquad
  \text{s.t.} \quad
  \mathbf{1}^\top x = n_{\mathrm{target}},
  \quad
  Gx \geq 0
$$

*where $t_i = \mathrm{tr}_M(b_i)$ are the Markov traces of the NF basis elements. Then:*

1. *The LP has optimal value $\mathrm{tr}_M^* = 0$, achieved by exploiting the negative eigenvalue $\lambda_{\min}(G) < 0$.*
2. *The LP optimum $x^*$ has $|x_i^*| \gg 1$ for some components. It is not in the image of the braid group representation $\rho \colon B_3 \to H_3(q)$.*
3. *Among all elements $\Phi \in H_3(q)$ that are images of braid group elements of length $\leq 6$, $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the unique element with $|\mathrm{net}(\Phi \cdot \mathrm{crossings}) - n_{\mathrm{target}}| = 0$ for both proton and neutron typed crossings.*
