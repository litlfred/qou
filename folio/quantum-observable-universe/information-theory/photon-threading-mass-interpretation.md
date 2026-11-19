**Three computations of the same quantity.**

Three independent methods evaluate the mass $\mathfrak{m}_{\mathfrak{H}}$, yielding identical results:

| Method | Domain | Computes $\mathfrak{m}_{\mathfrak{H}}$ as |
|--------|--------|------------------------------|
| Yekutieli MI | Analytic | $\lVert\mathrm{MI}\int_\Sigma(\nabla_A q, L \wedge F^+)\rVert$ |
| Ribbon trace | Algebraic | $\lVert\mathrm{tr}_{\mathrm{ribbon}}(\rho(\beta_{\mathfrak{H}}))\rVert \cdot (q-1)^2$ |
| Gröbner--Shirshov reduction | Computational | $(q-1)^2 \sum \lvert c_w\rvert \cdot \lvert q - q^{-1}\rvert$ |

The first represents the definition ([mass over $\mathbb{C}$](#ex:mass-identity-su2)). The second derives from the ribbon category structure ([energy](#def:mass-energy)). The third forms the content of this proposition.

**Physical picture.**

The photon $\gamma$ ($\mathbf{1}_{B_4}$ 4-strand identity) is knot-trivial under Markov closure. It approaches the hadron $\mathfrak{H}$. To "measure" the hadron—to determine its mass—the photon must braid completely through $\mathfrak{H}$, moving from one side of the braid word to the other.

1. **Start.** The photon strand sits above the hadron braid: $\gamma \otimes \beta_{\mathfrak{H}} \in B_{n+1}$.
2. **Thread.** Braid relations move $\gamma$ downward through $\beta_{\mathfrak{H}}$. The Yang--Baxter moves ($\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1}$) and far-commutativity ($\sigma_i\sigma_j = \sigma_j\sigma_i$) are **free**. They rearrange crossings without altering the Skein weight ([Gröbner--Shirshov energy](#thm:groebner-shirshov-energy)). Only the **Hecke steps** ($\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$) cost energy. Each Hecke step resolves a double crossing into a weighted single crossing plus a resolved identity.
3. **End.** The photon strand sits below $\beta_{\mathfrak{H}}$. The total Hecke cost equals the crossing energy $E_{\mathfrak{H}} = \sum |c_w| \cdot |q - q^{-1}|$ in Skein units. Mass--energy equivalence yields the mass: $\mathfrak{m}_{\mathfrak{H}} = E_{\mathfrak{H}} \cdot (q-1)^2$.

**Measurement mechanism.**

The photon has no crossings of its own; it is topologically trivial ($K = \varnothing$). It couples to the gauge field ($F_A^+$) because it propagates as exceptional-divisor flux ([photon wavefront](#ex:photon-wavefront)). Threading it through $\mathfrak{H}$ forces it to traverse every crossing of $\beta_{\mathfrak{H}}$. Each traversed crossing forces a Hecke reduction.

The **surface** $\Sigma$ in the Yekutieli integral $\mathrm{MI}\int_\Sigma$ spans the disc swept by the photon through the hadron. The vortex boundary $\partial\Sigma = \varrho$ bounds it. The interior of $\Sigma$ tracks the trajectory of $\gamma$ through $\beta_{\mathfrak{H}}$. The multiplicative integral accumulates the connection along this trajectory, providing the analytic counterpart to the algebraic Gröbner--Shirshov reduction.

**Path independence.**

The Gröbner--Shirshov basis is confluent via the Bergman diamond lemma. The total Hecke cost remains invariant under different reduction orderings. This algebraic path independence expresses the **gauge invariance** of the mass. The Yekutieli integral is independent of the choice of surface $\Sigma$ (for fixed $\partial\Sigma = \varrho$). The Gröbner--Shirshov reduction is independent of the reduction path.

**Connection to the speed of light.**

The conversion factor $(q-1)^2$ between crossing energy and mass is $1/c_q^2$:

$$
  \mathfrak{m}_{\mathfrak{H}} =  \frac{E_{\mathfrak{H}}}{c_q^2}
  =  (q-1)^2 \cdot E_{\mathfrak{H}}.
$$

Each Hecke step costs $|q - q^{-1}|$ in Skein units (spatial information). The factor $(q-1)^2 = (q\hbar_q)^2$ converts this to mass units (temporal information). It equals the square of the ratio of temporal to spatial coupling in the $q$-connection. The photon traverses the hadron at speed $c_q = 1/(q-1)$. The total traversal cost divided by $c_q^2$ is the mass.
