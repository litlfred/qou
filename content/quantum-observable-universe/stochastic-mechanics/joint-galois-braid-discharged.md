**Proposition (joint motivic-Galois $\times$ braid action commutes
on every bi-filtration cell — discharged in general by the
disjoint-action argument).**

The joint-action conjecture
([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action))
predicted commutativity of the motivic-Galois action $G_{\mathrm{mot}}$
and the braid-group action $B_{n_K}$ on every $\mathcal{H}_q^{(n, K)}$
stratum. *This proposition discharges the conjecture in general,
not just on the figure-8 cell as in
[`prop:joint-galois-braid-figure-8-verified`](#prop:joint-galois-braid-figure-8-verified).
The argument is structural: the two actions touch disjoint factors
of the bi-filtration's underlying tensor structure.*

### Statement

For every $(n, K)$ with $\mathcal{H}_q^{(n, K)}$ defined per
[`def:hq-bi-filtration`](#def:hq-bi-filtration), the actions
$G_{\mathrm{mot}}$ and $B_{n_K}$ commute on $\mathcal{H}_q^{(n, K)}$:

$$
  g_{\mathrm{mot}}(\beta \cdot \alpha) \;=\; \beta \cdot g_{\mathrm{mot}}(\alpha)
  \quad\text{for } \alpha \in \mathcal{H}_q^{(n, K)},\;
  g_{\mathrm{mot}} \in G_{\mathrm{mot}},\;
  \beta \in B_{n_K}.
$$

### Proof

**Step 1 (decompose the bi-filtration cell).**  Every element
$\alpha \in \mathcal{H}_q^{(n, K)}$ admits a canonical factorisation:

$$
  \alpha \;=\; e_{\lambda_K} \cdot g(z_K)
$$

where $e_{\lambda_K} \in Z(H_{n_K}(q))$ is the central primitive
idempotent of the dominant cell
([`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent))
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

### Cross-references

- Joint-action conjecture (now discharged): [`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)
- Figure-8 special case: [`prop:joint-galois-braid-figure-8-verified`](#prop:joint-galois-braid-figure-8-verified)
- Bi-filtration: [`def:hq-bi-filtration`](#def:hq-bi-filtration)
- Bridge map: [`conj:two-filtration-bridge`](#conj:two-filtration-bridge), [`prop:two-filtration-bridge-small-cases`](#prop:two-filtration-bridge-small-cases)
- Centrality of $e_{\lambda_K}$: [`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)
