*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (mass as a single sum over curvature-rank strata).**

*Per [spectral sequence collapse](#prop:spectral-sequence-collapse)
and [curvature-rank stratification](#prop:curvature-rank-gb-stratification),
the categorical mass of a knot $\mathcal{K}$ probed by test element
$\mathcal{T} \in A = H_n(R, q)$ decomposes as a single sum over
GB-filtration depths $k = 0, 1, \ldots, n - 1$:*

$$
  \boxed{\;
    \mathfrak{m}_{q,\mathcal{K}}(\mathcal{T})
    \;=\; \sum_{k = 0}^{n - 1} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T}),
    \qquad
    \mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T})
    \;=\; \!\!\sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}\!\!
      \tilde w_\lambda \cdot \log\Bigl|\!\int_{A_\lambda}\!\rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|
  \;}
$$

*with $\alpha_k$ stratum-dependent prefactors, $A_\lambda = e_\lambda A
e_\lambda$ the Wedderburn block, and $\tilde w_\lambda = \dim_q^2
V_\lambda / [n]_q!$ the **q-deformed Wedderburn-block weight**
([prop:wedderburn-weight-canonical](#prop:wedderburn-weight-canonical)).
The classical Plancherel measure $w_\lambda = (\dim V_\lambda)^2/n!$
([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness))
satisfies $\sum_\lambda w_\lambda = 1$ exactly; the q-deformed
analogue $\tilde w_\lambda$ has $\sum_\lambda \tilde w_\lambda$
finite but generally $\neq 1$ at $q \neq 1$ (empirically $\approx
1.51$ at $q_0, n = 12$). The two coincide at $q = 1$.*

*The total mass is the sum, with $\mathcal{T} = 1$:*
$\mathfrak{m}_{q,\mathcal{K}} := \mathfrak{m}_{q,\mathcal{K}}(1)$.
*Low-tower and high-tower partial sums are abbreviated*
$\mathfrak{m}^{<k}_{q,\mathcal{K}}(\mathcal{T})$ *and*
$\mathfrak{m}^{\geq k}_{q,\mathcal{K}}(\mathcal{T})$ *respectively.*
