### Proof

**Step 1 (decompose the bi-filtration cell).**  Every element
$\alpha \in \mathcal{H}_q^{(n, K)}$ admits a canonical factorisation:

$$
  \alpha \;=\; e_{\lambda_K} \cdot g(z_K)
$$

where $e_{\lambda_K} \in Z(H_{n_K}(q))$ is the central primitive
idempotent of the dominant cell
([Explicit central primitive idempotents $e_\lambda$ via Murphy elements](#prop:explicit-central-idempotent))
and $g(z_K)$ is a depth-$n$ grouplike at the shape parameter $z_K \in F^\times$.

By centrality of $e_{\lambda_K}$ in $H_{n_K}(q)$, the action of
$\beta \in B_{n_K}$ via the standard representation factors as

$$
  \beta \cdot \alpha \cdot \beta^{-1}
  \;=\;
  (\beta \cdot e_{\lambda_K} \cdot \beta^{-1}) \cdot g(z_K)
  \;=\;
  e_{\lambda_K} \cdot g(z_K)
  \;=\; \alpha.
$$

**The braid-group action is trivial on $\mathcal{H}_q^{(n, K)}$**
— it fixes both factors (centrality + grouplike-as-scalar).

**Step 2 (Galois action on the cell factorisation).**  The motivic-
Galois action $G_{\mathrm{mot}}$ acts on:
- The coefficient ring $F$ (cyclotomic Galois, bar involution etc.),
- The shape parameter $z_K \in F^\times$.

It does **not** act on the partition $\lambda_K$ directly, but
through the bar involution it sends $e_{\lambda_K} \to e_{\lambda_K'}$
(transpose partition). The factorisation transforms as:

$$
  g_{\mathrm{mot}}(\alpha)
  \;=\;
  e_{\lambda_K'} \cdot g(g_{\mathrm{mot}}(z_K)).
$$

**Step 3 (joint composition).**  Compute the two composites:

$$
  \begin{aligned}
    g_{\mathrm{mot}}(\beta \cdot \alpha)
    & \;=\; g_{\mathrm{mot}}(\alpha)
      \quad\text{(Step 1: braid trivial)} \\
    & \;=\; e_{\lambda_K'} \cdot g(g_{\mathrm{mot}}(z_K))
      \quad\text{(Step 2)} \\[4pt]
    \beta \cdot g_{\mathrm{mot}}(\alpha)
    & \;=\; \beta \cdot e_{\lambda_K'} \cdot g(g_{\mathrm{mot}}(z_K)) \cdot \beta^{-1} \\
    & \;=\; e_{\lambda_K'} \cdot g(g_{\mathrm{mot}}(z_K))
      \quad\text{(centrality of } e_{\lambda_K'}\text{).}
  \end{aligned}
$$

Both expressions equal $e_{\lambda_K'} \cdot g(g_{\mathrm{mot}}(z_K))$.
**Joint commutativity holds.** $\square$
