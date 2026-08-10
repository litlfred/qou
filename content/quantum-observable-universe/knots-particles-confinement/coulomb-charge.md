Let $\mathfrak{H}$ be a knot composite with braid word $\beta$. Let $n_+(\beta)$ and $n_-(\beta)$ denote the number of positive and negative crossings in $\beta$. We define the **Coulomb charge** of $\mathfrak{H}$ as:

$$
  Q(\mathfrak{H}) =  \tfrac{1}{2}\bigl(n_+(\beta) - n_-(\beta)\bigr).
$$

The crossing energy ([crossing energy](#def:crossing-energy)) decomposes into two terms:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \underbrace{\tfrac{1}{2}(n_+ + n_-)(q + q^{-1})}_{\text{baseline (strong)}}
  + 
  \underbrace{Q(\mathfrak{H}) \cdot (q - q^{-1})}_{\text{Coulomb correction}}.
$$

The first term is symmetric under $q \leftrightarrow q^{-1}$ and represents the strong binding. The second term is antisymmetric and vanishes at $q = 1$. The Coulomb charge $Q(\mathfrak{H})$ governs the magnitude and sign of the electromagnetic correction:

- $Q(\mathfrak{H}) > 0$: net positive crossings yield a repulsive Coulomb contribution.
- $Q(\mathfrak{H}) = 0$: the configuration is electromagnetically neutral.
- $Q(\mathfrak{H}) < 0$: net negative crossings yield an attractive Coulomb contribution.

The ratio of Coulomb to strong contributions evaluates to $\tanh(\ln q) \approx 0.104$ at $q = q_0$.
