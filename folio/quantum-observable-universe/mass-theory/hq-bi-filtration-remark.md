#### Axes and refinements

**Depth axis $n$ (horizontal).** Inherited from
[gb depth period correspondence](#conj:gb-depth-period-correspondence):
$G^{(0)}$ contains $\exp_q$ and scalars; $G^{(n)}$ adjoins the
grouplikes $\log_q, \mathrm{Li}_2^q, \ldots, \mathrm{Li}_n^q$.
Compatible with $\tau_{\mathrm{arch}}$ via
$\tau_{\mathrm{arch}}(G^{(n)}) \subseteq \mathcal{P}_n$.

**Knot axis $K$ (vertical).** Refined by partition cell
$\lambda_K$. Two natural sub-axes inside the $K$-axis:

1. **Bar-class.** Self-conjugate $\lambda_K = \lambda_K'$ vs chiral
   pair $\lambda_K \neq \lambda_K'$ (cf. [chirality period pairing](#rem:chirality-period-pairing)).
2. **Genus.** $g(K) \leq 4$ for Bring-embeddable
   ([bring embeddable knots](#rem:bring-embeddable-knots)).

#### Compatibility with the Hopf and braid structures

The bi-filtration interacts with the existing structures on $\mathcal{H}_q$:

| Operation | Effect on $(n, K)$ |
|---|---|
| Convolution $*_q$ ($q$-shuffle) | $\mathcal{H}_q^{(n_1, K_1)} *_q \mathcal{H}_q^{(n_2, K_2)} \subseteq \bigoplus \mathcal{H}_q^{(n_1 + n_2, K')}$ where $K'$ ranges over cell-mergings |
| Coproduct $\Delta_q$ | $\Delta_q(\mathcal{H}_q^{(n, K)}) \subseteq \bigoplus_{n_1 + n_2 = n,\,K_1 \otimes K_2 = K} \mathcal{H}_q^{(n_1, K_1)} \otimes \mathcal{H}_q^{(n_2, K_2)}$ |
| Bar involution $* \colon q \mapsto q^{-1}$ | $* \colon \mathcal{H}_q^{(n, K)} \to \mathcal{H}_q^{(n, K^*)}$ where $K^*$ is the mirror knot |
| Markov trace $\mathrm{tr}_M$ | $\mathrm{tr}_M \colon \mathcal{H}_q^{(n, K)} \to \mathcal{P}_n / \mathcal{P}_{n-1}$ — depth-preserving, knot-evaluating |
| Braid action of $\beta \in B_{n_K}$ | $\beta \cdot \mathcal{H}_q^{(n, K)} \subseteq \mathcal{H}_q^{(n, \beta \cdot K)}$ where $\beta \cdot K$ is the conjugate braid closure |

#### The bi-filtration as a tooling unification

This is the **definition layer** for the framework the
depth correspondence implies but does not name. Three downstream conjectures
populate it:

- [joint galois braid action](#conj:joint-galois-braid-action)
  — the symmetry group acting on $\mathcal{H}_q^{(n, K)}$.
- [knot indexed convolution grid](#prop:knot-indexed-convolution-grid)
  — placement of paper's existing knot-indexed convolutions
  ($\mathrm{Lk}_R^{(k)}$, $\bowtie_K$, Markov trace, Hoefsmit pairing,
  Higgs-vev coupling) into the $(n, K)$-grid.
- [k theory period rosetta](#rem:k-theory-period-rosetta)
  — Beilinson regulator on $K_{2n-1}^{\mathrm{ind}}(\overline{\mathbb{Q}})$
  matches the depth-$n$ axis.
