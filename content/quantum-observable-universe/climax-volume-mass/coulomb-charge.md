*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $\mathfrak{H}$ be a knot composite with braid word $\beta$.  Write
$n_+(\beta)$ and $n_-(\beta)$ for the number of positive and
negative crossings in $\beta$.  The *Coulomb charge* of $\mathfrak{H}$ is

$$
  Q(\mathfrak{H}) =  \tfrac{1}{2}\bigl(n_+(\beta) - n_-(\beta)\bigr).
$$

The crossing energy ([crossing energy](#def:crossing-energy))
decomposes as

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \underbrace{\tfrac{1}{2}(n_+ + n_-)(q + q^{-1})}_{\text{baseline (strong)}}
  + 
  \underbrace{Q(\mathfrak{H}) \cdot (q - q^{-1})}_{\text{Coulomb correction}}.
$$

The first term is symmetric in $q \leftrightarrow q^{-1}$ and
represents the strong binding; the second is antisymmetric and
vanishes at $q = 1$.  The Coulomb charge $Q(\mathfrak{H})$ governs the
magnitude and sign of the electromagnetic correction:

- $Q(\mathfrak{H}) > 0$: net positive crossings, repulsive Coulomb contribution.
- $Q(\mathfrak{H}) = 0$: electromagnetically neutral.
- $Q(\mathfrak{H}) < 0$: net negative crossings, attractive Coulomb contribution.

The ratio of Coulomb to strong contributions is
$\tanh(\ln q) \approx 0.104$ at $q = q_0$.
