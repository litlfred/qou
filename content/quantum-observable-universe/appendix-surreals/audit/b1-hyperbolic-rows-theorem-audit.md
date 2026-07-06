# Audit: Per-row computations for B1 hyperbolic rows

This block records explicit cell pairing and Volume Conjecture discharge steps for the Borromean rings and Whitehead link. This supports the conditional reduction of B1 at these rows.

## Borromean rings row

**Step 1 (Bloch–Suslin depth-2 ID).** Over $F = \mathbb{Q}(i)$: we have $\dim_\mathbb{Q} K_3^{\mathrm{ind}}(\mathbb{Q}(i)) \otimes \mathbb{Q} = 1$ ([`prop:borel-partial-resolution`](#prop:borel-partial-resolution)), because $\mathbb{Q}(i)$ has $r_1 = 0$ and $r_2 = 1$. The image of the Bloch–Suslin regulator is the line spanned by $D(i) = \mathrm{Cl}_2(\pi/2) = G$, which is Catalan's constant.

**Step 2 (cell pairing).** The Borromean rings have braid representation $(\sigma_1 \sigma_2^{-1})^3 \in B_3$ closure. The dominant cell in $H_3(q)$ pairs with $\mathrm{Li}_2^q(i)$ via Markov trace. This produces $8 \cdot D(i) = 8 G = \mathrm{Vol}(L_{6a4})$. This matches the Lobachevsky decomposition of the Borromean rings complement into 8 ideal regular octahedra, each contributing $G$.

**Step 3 (VC discharge).** We apply van der Veen (2008). This asymptotic analysis of the coloured Jones polynomial of the Borromean rings yields:

$$
  \lim_{N \to \infty} \frac{2 \pi}{N} \log\bigl|J_{L_{6a4}}^{(N)}(e^{2 \pi i / N})\bigr|
  \;=\;
  \mathrm{Vol}(L_{6a4})
  \;=\;
  8\,\mathrm{Cl}_2(\pi/2).
$$

## Whitehead link row

**Steps 1–2 (Bloch–Suslin + cell pairing).** We work over $\mathbb{Q}(i)$. The Whitehead link complement decomposes into 4 ideal regular octahedra. This yields a volume of $4 G = 4\,\mathrm{Cl}_2(\pi/2) \approx 3.66386$.

**Step 3 (VC discharge).** We apply Murakami (2002). This analysis generalises the figure-8 calculation to the coloured Jones polynomial of the Whitehead link, proving the asymptotic match.
