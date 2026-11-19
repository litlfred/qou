**Conjecture (Frobenius-reciprocity ideal restriction at low curvature-rank).**

*The unified curvature-rank mass formula admits a Frobenius-reciprocity refinement at low curvature-rank $k \le 3$. The depth-$k$ Wedderburn weight restricts to the distinguished hyperbolic-knot ideal at depth $k$ via Frobenius reciprocity for the center inclusion $Z(H_3) \hookrightarrow Z(H_n)$.*

*For each low curvature-rank $k \in \{1, 2, 3\}$ there is a distinguished hyperbolic knot $K_k^*$. At $k = 3$, $K_3^* = 4_1$ gives the best variance reduction **when the partition weight is the textbook form $w_\lambda = \dim_q^2 V_\lambda / [n]_q!$**, consistent with the Fricke-trace derivation. The depth-$k$ contribution to the mass formula is*

$$
  \boxed{\;
    \Phi_k^{\mathrm{FR}}(\mathcal{K}, \mathcal{T})
     :=
    \sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}
      \widetilde{w}_\lambda^{(K_k^*)} \cdot
      \log\!\Bigl|\!\!\int_{A_\lambda}\!\! \rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|
  \;}
$$

*where the FR-restricted weight $\widetilde{w}_\lambda^{(K_k^*)}$ is the Frobenius-reciprocity pullback through the knot-ideal central projector $e_{K_k^*} \in Z(H_n)$.*

At high curvature-rank $k \ge 4$, FR is trivial and the uniform Plancherel weight is correct. Empirical tests falsified simpler weight-restriction forms that did not use the distinguished knot ideal $e_{K_k^*}$. The FR refinement breaks the Jones-only spectral degeneracy by weighting partitions through the distinguished projector. If true, this conjecture closes the variance on the unified mass formula.

**Which $K_3^*$ is best depends on the weight family.** The $k = 3$ ranking is *not* invariant across the candidate weight families for $w_\lambda$. Measured on one harness, with the same braid words and the same character inputs, changing only the partition weight: $\dim_q^2/[n]_q!$ (the form named in the statement above) ranks $4_1$ best; the self-normalised $\dim_q^2/\sum_\mu \dim_q^2$ ranks $6_1$ best; the Molien weight $f^\lambda q^{-\kappa_\lambda}\dim_q(\lambda)/[n]_q!$ ranks $5_2$ best; and under the Markov weights $y_\lambda$ the depth-3 stratum is identically zero (the $\mathrm{SU}(N)$ row cap), so the test is vacuous. Three scoreable families, three different winners. Taking the Molien weight as the canonical $\Phi_k$ family and keeping the self-normalised $\dim_q^2/\sum_\mu \dim_q^2$ as a labelled comparison arm yields $K_3^* = 5_2$. The statement's $4_1$ is therefore a result about the $\dim_q^2/[n]_q!$ family, which is not the canonical one.
