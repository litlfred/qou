The quark-gluon plasma (QGP) deconfinement transition corresponds to the **golden ratio degeneration** of the Descartes elliptic curve ([golden ratio threshold](#rem:golden-ratio-degeneration)). Hadrons dissolve into free quarks and gluons.

**Deconfinement mechanism.**
Color confinement in QOU is enforced by the $S_5$-invariance of the Skein module on Bring's surface ([chromaticity](#rem:q-chromaticity)). Only $S_5$-invariant combinations of knots in the three color tubes yield positive $\tau$-evaluation. This $S_5$-invariance is a property of the **smooth elliptic fiber** $\mathcal{E}_q$. The fiber relates the three color tubes.

At $q_{\mathrm{gold}} = 1/\varphi^2 \approx 0.382$, the elliptic fiber degenerates. $\mathcal{E}_q$ acquires a node. Two roots of the Weierstrass equation coincide. The three color tubes collapse to a degenerate configuration. At this point:
1. The $S_5$ symmetry that enforces color neutrality **breaks**.
2. The $q$-chromaticity gamut **expands to fill the entire triangle**.
3. Individual quarks acquire **positive probability**. They are no longer confined.

This is deconfinement. It is a **topological phase transition** where the fiber that enforces confinement ceases to exist.

**First-order character.**
The QGP transition in QCD lattice simulations is first-order for three or more light quark flavors. In QOU, the first-order character is visible algebraically.
1. **Discriminant crossing.** The discriminant of $\mathcal{E}_q$ crosses zero at $q_{\mathrm{gold}}$. For $q > q_{\mathrm{gold}}$, $\Delta < 0$ (smooth curve, one real component). At $q = q_{\mathrm{gold}}$, $\Delta = 0$ (nodal curve). Below, $\Delta > 0$ (two real components, then degenerate). The topology of the real locus changes discontinuously.
2. **Latent heat.** The energy difference between the confined phase and the deconfined phase is finite. In crossing-energy units, the latent heat per baryon is
$$
  \mathcal{L}
   \sim 
  \tfrac{1}{2}(n_+ + n_-)\bigl[(q + q^{-1}) -
  (q_{\mathrm{gold}} + q_{\mathrm{gold}}^{-1})\bigr]
$$
   This is nonzero for $q \neq q_{\mathrm{gold}}$.
3. **Order parameter.** The order parameter is the **$j$-invariant** of the elliptic fiber. $j(q)$ is finite and continuous for $q > q_{\mathrm{gold}}$. It diverges as $q \to q_{\mathrm{gold}}$ ($j \to \infty$ at the node). The divergence of $j$ signals the breakdown of the elliptic structure. The Polyakov loop jumps from zero (confined) to nonzero (deconfined) at the transition.

**Effective $q$ at finite temperature.**
The physical aether has $q = q_0$. Temperature changes the **effective crossing energy** available to disrupt the Borromean structure. At temperature $T$, thermal fluctuations supply energy $\sim k_B T$ per degree of freedom. Deconfinement occurs when thermal energy matches the Hopf binding energy per baryon:

$$
  k_B T_c
   \sim 
  |\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p})|
   \sim 
  \tfrac{1}{2}(q + q^{-1}) \cdot n_{\mathrm{link}},
$$

where $n_{\mathrm{link}}$ is the number of Hopf-link crossings in the Borromean triple. The effective $q$ at which the **chiral structure of the fiber is thermally disrupted** is $q_{\mathrm{gold}}$.

This identifies the QGP transition temperature with the stability margin:

$$
  \frac{k_B T_c}{\Lambda_{\mathrm{QCD}}}
   \sim 
  \frac{q - q_{\mathrm{gold}}}{q}
  = 
  \frac{q_0 - 0.382}{q_0}
   \approx  0.656.
$$

**Golden ratio threshold.**
The QGP phase transition is not at a new scale or coupling constant. It is the same golden ratio that appears in the chiral degeneration, the Penrose tiling, and the $E_8$ McKay correspondence. Its appearance as the deconfinement boundary is forced by the $S_5$ symmetry of Bring's surface. The minimal polynomial $s^2 + s - 1 = 0$ governs both the chiral fiber structure and the confinement mechanism. When the fiber degenerates, confinement breaks.

**Phase diagram.**
| $q_{\mathrm{eff}}$ | Phase | Fiber | Color | Hadrons |
|---------------------|-------|-------|-------|---------|
| $q > 1$ (low $T$) | Confined hadronic | Smooth, $\Delta < 0$ | Confined ($S_5$-inv only) | Stable baryons, mesons |
| $q_{\mathrm{gold}} < q < 1$ | Intermediate | Smooth, $\Delta > 0$ | Partially confined | Unstable resonances |
| $q = q_{\mathrm{gold}}$ | Critical | Nodal | Deconfining | QGP onset |
| $q < q_{\mathrm{gold}}$ | Deconfined QGP | Degenerate | Free quarks | No stable hadrons |
