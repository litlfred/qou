**Definition (knot-indexed bi-filtration $\mathcal{H}_q^{(n, K)}$ on the substrate convolution algebra).**

*Let $\mathcal{H}_q$ be the substrate convolution Hopf algebra
([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)),
filtered by iterated-integral depth
$G^{(0)} \subseteq G^{(1)} \subseteq \cdots$
([depth correspondence](#conj:gb-depth-period-correspondence)).
For each Bring-embeddable knot/link $K$ ([Bring-embeddable
knots](#rem:bring-embeddable-knots)) with dominant cell
$\lambda_K \vdash n_K$ and central primitive idempotent
$e_{\lambda_K} \in Z(H_{n_K}(q))$
([explicit central idempotent](#prop:explicit-central-idempotent)),
the **knot-$K$-localised depth-$n$ stratum** is*

$$
  \mathcal{H}_q^{(n, K)}
  \;:=\;
  \bigl\{\, \alpha \;\in\; G^{(n)}(\mathcal{H}_q)
        \;:\; e_{\lambda_K} \cdot \alpha \cdot e_{\lambda_K} = \alpha \,\bigr\}.
$$

*The double-indexed family $\{\mathcal{H}_q^{(n, K)}\}_{n \geq 0,\;K}$
is the **bi-filtration**: a horizontal axis of iterated-integral
depth $n$ (Goncharov side) and a vertical axis of knot/braid class
$K$ (Hecke cell side).*

### Axes and refinements

**Depth axis $n$ (horizontal).** Inherited from
[GS-depth $\leftrightarrow$ Goncharov period-depth correspondence](#conj:gb-depth-period-correspondence):
$G^{(0)}$ contains $\exp_q$ and scalars; $G^{(n)}$ adjoins the
grouplikes $\log_q, \mathrm{Li}_2^q, \ldots, \mathrm{Li}_n^q$.
Compatible with $\tau_{\mathrm{arch}}$ via
$\tau_{\mathrm{arch}}(G^{(n)}) \subseteq \mathcal{P}_n$.

**Knot axis $K$ (vertical).** Refined by partition cell
$\lambda_K$. Two natural sub-axes inside the $K$-axis:

1. **Bar-class.** Self-conjugate $\lambda_K = \lambda_K'$ vs chiral
   pair $\lambda_K \neq \lambda_K'$ (cf. [Chirality structure on Goncharov period classes via the bar involution](#rem:chirality-period-pairing)).
2. **Genus.** $g(K) \leq 4$ for Bring-embeddable
   ([Bring-embeddable knots: genus-bounded table and per-knot witness targets for the depth correspondence](#rem:bring-embeddable-knots)).

### Compatibility with the Hopf and braid structures

The bi-filtration interacts with the existing structures on $\mathcal{H}_q$:

| Operation | Effect on $(n, K)$ |
|---|---|
| Convolution $*_q$ ($q$-shuffle) | $\mathcal{H}_q^{(n_1, K_1)} *_q \mathcal{H}_q^{(n_2, K_2)} \subseteq \bigoplus \mathcal{H}_q^{(n_1 + n_2, K')}$ where $K'$ ranges over cell-mergings |
| Coproduct $\Delta_q$ | $\Delta_q(\mathcal{H}_q^{(n, K)}) \subseteq \bigoplus_{n_1 + n_2 = n,\,K_1 \otimes K_2 = K} \mathcal{H}_q^{(n_1, K_1)} \otimes \mathcal{H}_q^{(n_2, K_2)}$ |
| Bar involution $* \colon q \mapsto q^{-1}$ | $* \colon \mathcal{H}_q^{(n, K)} \to \mathcal{H}_q^{(n, K^*)}$ where $K^*$ is the mirror knot |
| Markov trace $\mathrm{tr}_M$ | $\mathrm{tr}_M \colon \mathcal{H}_q^{(n, K)} \to \mathcal{P}_n / \mathcal{P}_{n-1}$ — depth-preserving, knot-evaluating |
| Braid action of $\beta \in B_{n_K}$ | $\beta \cdot \mathcal{H}_q^{(n, K)} \subseteq \mathcal{H}_q^{(n, \beta \cdot K)}$ where $\beta \cdot K$ is the conjugate braid closure |

### The grid: low-$(n, K)$ examples

| $K$ | $\lambda_K$ | Bar-class | $\mathcal{H}_q^{(0, K)}$ | $\mathcal{H}_q^{(2, K)}$ | $\mathcal{H}_q^{(3, K)}$ |
|---|---|---|---|---|---|
| trivial (unknot $0_1$) | $(1)$ | self-conj | scalars | $\mathrm{Li}_2^q(0) = 0$ | $\mathrm{Li}_3^q(0) = 0$ |
| trefoil $3_1$ | $(3)$ vs $(1,1,1)$ | chiral pair | $e_{(3)} \pm e_{(1,1,1)}$ | $\mathrm{Vol}(3_1) = 0$ (torus) | $\mathrm{CS}(3_1) = \pm \pi^2/6$ |
| figure-8 $4_1$ | $(2,2)$ | **self-conj** | $e_{(2,2)}$ | $2\,\mathrm{Cl}_2(\pi/3)$ (confirmed) | depth-3 partner (open) |
| Bring trilog input | abstract / virtual | (lifted from $\zeta_5$) | scalars | weight-2 extension | $\mathrm{Li}_3(\zeta_5)$ (confirmed) |

### The bi-filtration as a tooling unification

This is the **definition layer** for the framework the
depth correspondence implies but does not name. Three downstream conjectures
populate it:

- [Joint motivic-Galois $\times$ braid-group action on the bi-filtration $\mathcal{H}_q^{(n, K)}$](#conj:joint-galois-braid-action)
  — the symmetry group acting on $\mathcal{H}_q^{(n, K)}$.
- [Placement of paper's existing knot-indexed convolutions in the bi-filtration grid](#prop:knot-indexed-convolution-grid)
  — placement of paper's existing knot-indexed convolutions
  ($\mathrm{Lk}_R^{(k)}$, $\bowtie_K$, Markov trace, Hoefsmit pairing,
  Higgs-vev coupling) into the $(n, K)$-grid.
- [K-theory $\leftrightarrow$ depth filtration Rosetta](#rem:k-theory-period-rosetta)
  — Beilinson regulator on $K_{2n-1}^{\mathrm{ind}}(\overline{\mathbb{Q}})$
  matches the depth-$n$ axis.
