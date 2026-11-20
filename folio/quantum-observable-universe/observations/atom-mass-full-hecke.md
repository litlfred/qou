The semi-empirical mass formula $M_q$ uses the 2$\times$2 **standard** irrep of $H_3(q)$. This discards the symmetric and alternating channels, missing the dominant contribution for multi-nucleon systems.

We compute the atomic mass for $Z = 1$--$10$ using the full regular representation of $H_3(q)$.

## Three-channel decomposition

See [Table: Three-channel $H_3(q)$ decomposition](#tbl:atom-mass-full-hecke-table-data).

The full Markov trace decomposes as:

$$
  \mathrm{tr}_M^{\mathrm{full}} =
  \hat y_{\mathrm{sym}}\,\mathrm{tr}_{\mathrm{sym}} +
  \hat y_{\mathrm{std}}\,\mathrm{tr}_{\mathrm{std}} +
  \hat y_{\mathrm{alt}}\,\mathrm{tr}_{\mathrm{alt}},
$$

where $\hat y_\lambda$ are the $q$-deformed Jones--Markov weights. The classical Wedderburn--Artin values are heavily deformed.

These weights depend on the Markov parameter $z$, and the values below differ between the two conventions:

| | $\hat y_{\mathrm{sym}}$ | $\hat y_{\mathrm{std}}$ | $\hat y_{\mathrm{alt}}$ |
|:---|---:|---:|---:|
| convention D, $z = q^{3}/(q^{2}+1)$ (canonical) | $0.5054$ | $0.4946$ | $0$ |
| convention C, $z = \sqrt{q}/(q+1)$ (excised) | $0.42$ | $0.56$ | $0.02$ |

The alternating weight is **exactly zero** under the canonical convention, not merely small. Any statement that the alternating block is *suppressed* describes convention C; under convention D that channel does not contribute at all, and a nonzero $\hat y_{\mathrm{alt}}$ is itself a convention-C signature.

The convention-C row is retained because the results tabulated below were computed in it and have not been recomputed under D. They are reported as measured, in the frame that produced them.

## Mass decomposition

The mass integrand splits into:

1. **Horizontal**: $\mathfrak{E}_{\mathrm{cross}} = n_+ q - n_- q^{-1}$.
2. **Vertical**: $\mathfrak{m}_{\mathrm{vert}} = \mathrm{tr}_M^{\mathrm{full}}(\Phi_{\mathrm{mass}})$.
3. **Mixed**: $\mathfrak{m}_{\mathrm{mix}} = \mathfrak{E}_{\mathrm{cross}} \cdot (q - 1)^2$.

## Results for $Z = 1$--$10$

We evaluate the traces at $q = 111/100$.

See [Table](#tbl:atom-mass-full-hecke-table-data).

## Key observations

1. **Standard channel suppression.** The standard trace shrinks rapidly with $A$. The symmetric and alternating channels remain $O(1)$.
2. **Alternating channel sign flips.** The alternating *trace* alternates in sign with $A$, as the table shows. Its *contribution* does not: under the canonical convention the alternating block is **absent**, because its Ocneanu weight is identically zero for any partition with three or more rows (for every $n$). So the sign variation is carried by a channel that is multiplied by $\hat y_{\mathrm{alt}} = 0$ and cannot reach $\mathrm{tr}_{\mathrm{full}}$ at all. The apparent sign variation in the *total* was a classical-weighting artifact.
3. **${}^{14}\mathrm{N}$ cancellation.** The near-cancellation between symmetric and alternating traces depends entirely on classical weighting. It vanishes under canonical $q$-deformed weights.
4. **Binding energy deviations.** The semi-empirical formula undercounts the doubly-magic shell closure at ${}^4\mathrm{He}$.

No independent check of the high-$A$ traces is available.
