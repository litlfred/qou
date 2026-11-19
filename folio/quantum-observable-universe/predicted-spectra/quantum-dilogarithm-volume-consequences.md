## The beta-decay $Q$-value

The $Q$-value for the transition $\mathcal{N}(Z, N) \to \mathcal{N}(p\!+\!1, n\!-\!1)$ is the mass difference:

$$
  \mathfrak{Q}_\beta
  = 
  \frac{\Phi_q^{\mathrm{par}} - \Phi_q^{\mathrm{dau}}}{\hbar_q^2}
  = 
  \frac{1}{\hbar_q^2}
  \sum_{i=0}^{p}
  \log \left|
    \frac{\hat{V}_i^{\mathrm{par}}}{\hat{V}_i^{\mathrm{dau}}}
  \right|,
$$

where the sum runs only over the affected generators ($i \leq p$). For $i > p$, the generator factors agree: $\hat{V}_i^{\mathrm{par}} = \hat{V}_i^{\mathrm{dau}}$. The $Q$-value is intensive ($O(1)$ in MeV) because each log ratio is $O(1)$ and the sum contains $p + 1$ terms.

## The half-life (complete formula)

Substituting the quantum dilogarithm $Q$-value into the Fermi golden rule gives:

$$
  t_{1/2}
  = 
  \frac{\ln 2 \cdot 2N_v^4}{243\mathfrak{E}_{\times} \cdot \mu_0}
   \cdot 
  \frac{1}{[2]_q  \cdot  s^2
     \cdot  f(Z_d, Q)}
   \cdot 
  \prod_{i=0}^{p}
  \left|
    \frac{\hat{V}_i^{\mathrm{dau}}}{\hat{V}_i^{\mathrm{par}}}
  \right|^2,
$$

where $s = q^{1/2} - q^{-1/2}$ and $\mathfrak{E}_{\times} = \frac{1}{2}(q - q^{-1})$. The parameter $\mu_0$ is the single dimensional scale, and $N_v$ is the effective crossing count of the weak scale ($v = N_v\mathfrak{E}_{\times}\mu_0$). The prefactor replaces $G_F^2m_e^5/(2\pi^3)$ ([hadron half-life](#prop:hadron-half-life)). Every quantity is determined by the Iwahori–Hecke algebra computation at $q$, plus $\mu_0$ (unit choice) and $N_v$ (topological invariant of the weak scale).

## Two-level structure (cosimplicial)

The computation has two levels, corresponding to levels 0 and 1 of the cosimplicial crossed groupoid ([cosimplicial crossed groupoid](#prop:cosimplicial-crossed-groupoid)):

- **Level 0** ($B_A$, 1 strand per nucleon): The inter-nucleon crossings. The quantum dilogarithm $\Phi_q$ gives the total binding energy. (Verified: $\Delta\Phi > 0$ for all beta decays, meaning the daughter is less bound).
- **Level 1** ($B_{3A}$, 3 strands per nucleon): The intra-nucleon Borromean crossings. The crossing change $\mathfrak{d} \to \mathfrak{u}$ inside one nucleon produces the $Q$-value, which is the mass difference between parent and daughter. This splitting generates the neutron-proton mass difference $m_n - m_p = \mathcal{S}_{\mathfrak{d}\mathfrak{d}} - \mathcal{S}_{\mathfrak{u}\mathfrak{u}} \approx 1.293$ MeV.

The coface map $\delta^0 \colon \mathfrak{G}_0 \to \mathfrak{G}_1$ embeds the Level 0 computation into Level 1. The binding energy at Level 0 is the projection of the full Level 1 computation onto the inter-nucleon sector.

The factored trace $\prod_i \hat{V}_i$ applies at both levels. At Level 1, the product has $3A - 1$ factors instead of $A - 1$. The $Q$-value emerges from the log-ratio of traced volumes at the 3 quark-level generators of the converting nucleon.
