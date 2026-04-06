A **knot complement** $S^3 \setminus K$ is the 3-manifold obtained by
removing a tubular neighbourhood of a knot $K$ from the 3-sphere. When
$K$ is hyperbolic, the complement admits a unique complete hyperbolic
structure (by Mostow rigidity), and its volume is a topological invariant.

The SnapPea kernel (`@snappea/kernel`, compiled to WebAssembly) computes:

- **Hyperbolic volume** via ideal triangulations
- **Dehn filling** coefficients $(m, l)$ on cusps
- **Fundamental group** presentations $\pi_1(S^3 \setminus K)$
- **Homology** $H_1(S^3 \setminus K; \mathbb{Z})$ via Smith normal form
- **Chern–Simons invariant** (when defined)
- **Canonical form** for isometry detection

In the QOU particle registry, each knot $K$ (indexed by Alexander–Briggs
notation) corresponds to a particle, with the hyperbolic volume encoding
the particle's mass scale.
