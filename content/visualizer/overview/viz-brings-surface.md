The **Bring's surface visualizer** renders quaternionic spectral resolvents as
interactive 3D surfaces. The viewport state is fully serialisable (see
`VizState` in `schemas/qou-types.ts`) and can be embedded in URLs or
Markdown to reproduce a specific view.

**Viewport parameters:**

- $q$ — torsion/chirality parameter. $q = 0$ is classical; $q > 0$
  introduces chiral twist in the colour-sector coordinates
  $(\mathfrak{r}, \mathfrak{g}, \mathfrak{b})$.
- **Mode** — `CP1` shows the $\mathbb{C}P^1$ exceptional fibre;
  `cone` shows the outgoing chiral tube cones.
- **Camera** — spherical coordinates $(\theta, \phi, r)$ with configurable
  look-at target.

$$
\rho(s) = s \cdot \ell_P \cdot \sigma \cdot \Xi_q, \qquad
\psi_i(s) = \frac{2\pi i}{3} + q \cdot 2\pi s \cdot Q \cdot \gamma
$$
