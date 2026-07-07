**Corollary (k-factor parabolic specialisation).**
*Let $n = \sum_i n_i$. For every partition $\nu \vdash n$ and product $\beta_1 \otimes \cdots \otimes \beta_k \in H_{n_1}(R, q) \times \cdots \times H_{n_k}(R, q)$, the tensor-product Hecke character factors exactly as:*

$$
  \boxed{\;
    \chi^\nu_{H_n}(\beta_1 \otimes \cdots \otimes \beta_k)
    \;=\;
    \sum_{(\lambda_1, \ldots, \lambda_k)} c^\nu_{\lambda_1, \ldots, \lambda_k}
      \cdot \prod_{i=1}^{k} \chi^{\lambda_i}_{H_{n_i}}(\beta_i)
  \;}
$$

*where $c^\nu_{\lambda_1, \ldots, \lambda_k}$ is the iterated Littlewood–Richardson coefficient.*

This convolutional structure provides massive speedups. Computing the full atomic braid character normally requires intractable $H_{3A}$ seminormal matrices. By decomposing the canonical vacuum block into per-nucleon factors, we push the evaluation down to $H_3$ characters contracted against Schur structure constants.
