The semi-empirical mass formula $M_q$ uses the 2$\times$2 **standard** irrep of $H_3(q)$. This discards the symmetric and alternating channels, missing the dominant contribution for multi-nucleon systems.

We compute the atomic mass for $Z = 1$--$10$ using the full regular representation of $H_3(q)$.

## Three-channel decomposition

See [Table: Three-channel $H_3(q)$ decomposition](#tbl:atom-mass-full-hecke-table-data).

The full Markov trace decomposes as:

$$
  \mathrm{tr}_M^{\mathrm{full}}
  = \hat y_{\mathrm{sym}}\,\mathrm{tr}_{\mathrm{sym}}
  + \hat y_{\mathrm{std}}\,\mathrm{tr}_{\mathrm{std}}
  + \hat y_{\mathrm{alt}}\,\mathrm{tr}_{\mathrm{alt}},
$$

where $\hat y_\lambda$ are the $q$-deformed Jones--Markov weights. At $q \approx 1.11$, $\hat y_{\mathrm{sym}} \approx 0.42$, $\hat y_{\mathrm{std}} \approx 0.56$, and $\hat y_{\mathrm{alt}} \approx 0.02$. The classical Wedderburn--Artin values are heavily deformed.

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
2. **Alternating channel sign flips.** Under canonical $q$-deformed weights, the alternating block is suppressed. The apparent sign variation was a classical-weighting artifact.
3. **${}^{14}\mathrm{N}$ cancellation.** The near-cancellation between symmetric and alternating traces depends entirely on classical weighting. It vanishes under canonical $q$-deformed weights.
4. **Binding energy deviations.** The semi-empirical formula undercounts the doubly-magic shell closure at ${}^4\mathrm{He}$.

**Witness**: `atom-mass-full-hecke.witness.json`. We lack independent witnesses for high-$A$ traces.
