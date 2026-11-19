The [decomposition](#prop:crossing-energy-decomposition) separates crossing energy into two channels.

**Channel identification.**

| Channel | Weight per crossing | Under crossing reversal | Physical force |
|---------|-------------------|-----------------|----------------|
| Symmetric | $\pm\cosh(\ln q)$, signed by the crossing | negates | **Strong binding** |
| Antisymmetric | $+\sinh(\ln q)$, independent of the crossing sign | fixed | **Coulomb (electromagnetic)** |

The symmetric part binds regardless of charge. The antisymmetric part distinguishes charges. The sign-blindness of the $\sinh$ weight is what leaves a residue when a composite is paired with its mirror, and is the reason the two channel totals carry the multiplicities $p - m$ and $p + m$ respectively ([decomposition](#prop:crossing-energy-decomposition)).

**Pair creation.**

When creating an $e^- e^+$ pair, cancellation yields:

$$
  \mathfrak{E}_{\mathrm{cross}}(e^-) + \mathfrak{E}_{\mathrm{cross}}(e^+)
  = 6\sinh(\ln q)
  \approx 0.630 \quad (\text{Skein units}).
$$

Symmetric contributions cancel. The residual $6\sinh\lambda > 0$ yields pure Coulomb repulsion, separating the pair.

**Channel ratio.**

At $q = q_0$, for a positive braid closure ([ratio identity](#prop:crossing-energy-decomposition)):

$$
  \frac{E_{\mathrm{asym}}}{E_{\mathrm{sym}}} = \tanh(\ln q_0) \approx 0.104.
$$

The antisymmetric channel carries roughly $10\%$ of the symmetric channel's magnitude. This is a ratio of the two channel weights at the aether anchor rather than a running coupling ratio: no renormalisation scale is attached to it, and it should not be read as a value of $\alpha / \alpha_s$, which varies over the accessible energy range. The electromagnetic coupling proper is obtained from the antisymmetric eigenvalue by the [EM coupling projection](#prop:em-coupling-projection).

**Crossing energy table** for a particle with $n_c$ positive crossings:

| Quantity | Formula | $T_{2,3}$ ($n_c = 3$) | Value |
|----------|---------|----------------------|-------|
| Total energy | $n_cq$ | $3q$ | $3.330$ |
| Strong component | $n_c\cosh(\ln q)$ | $3\cosh(\ln q)$ | $3.015$ |
| Coulomb component | $n_c\sinh(\ln q)$ | $3\sinh(\ln q)$ | $0.315$ |
| Pair net energy | $n_c(q - q^{-1})$ | $3(q - q^{-1})$ | $0.630$ |
| Channel ratio | $\tanh(\ln q)$ | $\tanh(\ln q)$ | $0.104$ |

By [Hopf stability](#prop:torus-hopf-stability), $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$. The strong symmetric channel dominates the Coulomb antisymmetric channel, ensuring proton stability.
