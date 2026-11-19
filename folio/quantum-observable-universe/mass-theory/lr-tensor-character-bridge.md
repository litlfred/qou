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

The bridge replaces one character computation in $H_n$ by a sum of products of characters in the parabolic factors $H_{n_i}$. For an $A$-nucleon braid that is $H_{3A}$ against $A$ copies of $H_3$, whose irreducible blocks have dimensions $1, 2, 1$; the cost of the right-hand side is then carried by the number of Littlewood–Richardson tuples contributing to $\nu$ rather than by $\dim V_\nu$. This block wires no computation, so no timing or complexity is claimed for either side.

The coefficient $c^\nu_{\lambda_1, \ldots, \lambda_k}$ enters the identity as a *count*, not as a weight supplied by hand: restricting $V_\nu$ along the parabolic chain yields one copy of $V_{\lambda_1} \otimes \cdots \otimes V_{\lambda_k}$ per Littlewood–Richardson tableau, and the character is the sum over those copies. The displayed form follows by summing a constant over each copy set, keeping the sum-over-copies decomposition distinct from the resulting multiplicity formula.
