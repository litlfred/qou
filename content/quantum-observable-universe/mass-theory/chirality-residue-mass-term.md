**Proposition (chirality / non-chirality split of the mass tower).**

*Per the
[unified curvature-rank mass formula](#prop:unified-curvature-rank-mass-formula),
the categorical mass of a knot $\mathcal{K}$ probed by test element
$\mathcal{T} \in A = H_n(R, q)$ decomposes as a sum over GB-filtration
strata.  This proposition refines that decomposition by splitting each
stratum into a **chirality** part (Wedderburn blocks at signed-content
zero) and a **non-chirality** part:*

$$
  \boxed{\;
    \mathfrak{m}_{q,\mathcal{K}}(\mathcal{T})
    \;=\;
    \mathfrak{m}^{\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T})
    \;+\;
    \mathfrak{m}^{\neg\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T})
  \;}
$$

*where*

$$
  \mathfrak{m}^{\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T})
  \;=\;
  \sum_{k = 0}^{n-1} \alpha_k \cdot
    \!\!\sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k \\ c_\lambda \,=\, 0}}\!\!
    w_\lambda \cdot
    \log\Bigl|\!\int_{A_\lambda}\!\rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|,
$$

*$c_\lambda := \sum_{(i, j) \in \lambda}(j - i)$ is the signed Young
content, and the chirality cells are exactly those Wedderburn blocks
satisfying $D_q^2(\lambda) = 0$ in the q-Dirac cell scanner — the
gauge-invariant background per
[confinement-categorical](#prop:confinement-categorical),
[rem:confinement-curvature-rank](#rem:confinement-curvature-rank).*

*The non-chirality contribution is defined as the remaining sum.*
