**Multi-link Jones values at $q = 1$ — values for the $c_5 / c_6$ candidate investigation.**

The $\mathfrak{Q}_\beta$ precision ladder ([$\mathfrak{Q}_\beta$ categorical-derivation precision ladder](#prop:q-beta-categorical-precision-ladder)) closed $c_1, c_2$ from Kashiwara ($b, b^2$), $c_3$ from $J_{\mathrm{Hopf}}(q{=}1) = -2$ at the 3-fold Markov closure, and $c_4$ from the mixed Kashiwara-plus-Hopf-half $b^2 + 1/2$. The simple alternating Kashiwara $\times$ Jones pattern at odd $k = 3$ suggests trying multi-link Jones values for $c_5, c_7, \ldots$ (e.g., Borromean rings, double-Hopf).

| coefficient | empirical | closest simple multi-link Jones candidate |
|:---:|---:|---:|
| $c_5$ | $\approx -395.4$ | $-J_{\mathrm{Borromean}} = +8$ (50$\times$ off in scale and sign) |
| $c_6$ | $\approx -45{,}485$ | $J_{\mathrm{Hopf}} \cdot J_{\mathrm{Borromean}} = 16$ (3000$\times$ off) |

## Contents

What follows is **infrastructure, not closure**. The following values are recorded:

1. **Three further links**: the trefoil, the Borromean rings and the double Hopf link.
2. **Their Jones values at $q = 1$**:

   | link | $J_L(q{=}1)$ | source |
   |---|---:|---|
   | trefoil | $+1$ | Jones 1985, $T(2,3)$ 1-component unnormalised |
   | Borromean rings | $-8$ | Jones 1985 / Habiro 2002, 3-component Brunnian |
   | double Hopf link | $+4$ | $J_{\mathrm{Hopf}}^2$ by disjoint-union multiplicativity |

3. **Two combination values**: $J_{\mathrm{Hopf}} \cdot J_{\mathrm{Borromean}} = 16$ and $-J_{\mathrm{Borromean}} = 8$. Both miss the empirical values in the table above. They are not closures.

## Failure of the simple multi-link pattern

We posit three structural hypotheses for the 50–3000$\times$ mismatch:

1. **Precision-ladder normalisation revision**: the $b^k$ factor multiplying $c_k$ beyond $k = 4$ may carry an extra Wedderburn-weight or coupling-constant prefactor not captured by the $(b \cdot \hbar_q^2)^k$ expansion ansatz.
2. **Sum-over-Wedderburn-blocks**: multi-link contributions enter via a non-trivial sum over $\lambda \vdash n$ rather than as a direct scalar multiple of a single Jones value. The $y_\lambda$ normalisation in the Wenzl bridge could redistribute weight in a way that magnifies single-Jones values into the empirical $c_5, c_6$ scale.
3. **New categorical input at $k \geq 5$**: a higher-rank irrep coupling, a Mostow rigidity gap correction, or a non-trivial Habiro residue contribution may enter only at orders $k \geq 5$.

We must test whether the per-Wedderburn-block contribution at $k = 5, 6$ matches the empirical values when properly weighted by the $q$-deformed dimensions $\dim_q(V_\lambda)$. This requires extending the Wenzl-bridge $y_\lambda$ infrastructure to $\varepsilon^{10}, \varepsilon^{12}$ evaluations of the $\mathrm{tr}_M$ expansion on $V_{(2,1)}, V_{(3)}, V_{(1,1,1)}$ separately.
