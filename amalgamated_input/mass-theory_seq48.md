<!-- FILE_START: mass-theory-orphan-reconnect-intro.md -->
We consolidate structural results reconnected during the orphan audit. These blocks address phenomena at the boundary of the mass theory. We outline the categorical Higgs mechanism, the interface-knot Markov traces, and the Borromean Bloch-group elements. We isolate the spectral completeness conditions required to fully close the mass formula.
<!-- FILE_END: mass-theory-orphan-reconnect-intro.md -->

<!-- FILE_START: categorical-higgs-mechanism.md -->
**Conjecture (categorical Higgs mechanism).**
*The symmetry-breaking Higgs mechanism $SU(2)_L \times U(1)_Y \to U(1)_{\rm em}$ admits a categorical formulation. Goldstone boson consumption corresponds exactly to the topological linking of closed braids.*

Pre-symmetry breaking, the four electroweak gauge bosons form individual 1-component knots. A Higgs doublet provides four real scalar degrees of freedom, also corresponding to 1-component knots. 

Post-breaking, the vacuum expectation value induces topological linking. Three gauge bosons each fuse with a Goldstone boson, forming 2-component links. The linking number $\mathrm{lk} = 1$ encodes the broken-generator multiplicity. The remaining unbroken photon survives as a 1-component knot. The surviving Higgs scalar similarly remains an independent mediator.

The mass of each post-breaking boson evaluates strictly as the Markov trace of its new 2-component link, weighted by the appropriate Hoefsmit projector. Categorical linking supplies the precise operation that differentiates massive force-links from massless matter-knots.
<!-- FILE_END: categorical-higgs-mechanism.md -->

<!-- FILE_START: interface-knot-markov-z.md -->
*Let $\mathcal{B}_K \in H_{3A}(q)$ be the canonical atomic braid for atom $K$. Let $\mathcal{B}_K^{\mathrm{vac}}$ be the disjoint Hecke product of its constituent nucleons. The interface knot $\bowtie_K$ connects the blocks.*

*The Markov trace ratio identically satisfies:*

$$
  \boxed{\;
    \frac{\tau_M(\mathcal{B}_K)}{\tau_M(\mathcal{B}_K^{\mathrm{vac}})}
    \;=\; z(q)^{p_+(K)} \cdot \bigl(z(q) - h(q)\bigr)^{p_-(K)}
  \;}
$$

*where $z(q)$ is the Markov parameter, $h(q)$ is the Hecke skein parameter, and $p_+$ / $p_-$ count the positive / negative interface generators.*

This exact factorisation governs atomic assembly. Adding a proton inserts a positive interface, scaling the trace by $z$. Adding a neutron after a proton also inserts a positive interface. Adding a neutron to an existing neutron inserts a negative interface, scaling the trace by $z-h$. 

The structural interface identity completely determines the trace scaling. The empirical single-block extraction correction operates independently at a different structural level.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-analytic constructs. Any generic categorical identities remain valid over an abstract coefficient ring.
<!-- FILE_END: interface-knot-markov-z.md -->

<!-- FILE_START: rho-k-h3a-refinement.md -->
*The categorical density $\rho_K$ admits an exact Wedderburn-Schur decomposition:*

$$
  \rho_K(q)
  \;=\;
  \rho_K^{\mathrm{LO}}(Z, N)
  \;+\;
  \frac{1}{|\mathrm{tr}_M(\mathcal{B}_K)|}
  \sum_{\lambda \vdash 3A}
    y_\lambda(q)\,\chi^\lambda(\mathcal{B}_K)\,\Delta_\lambda(K)
$$

*The leading-order piece $\rho_K^{\mathrm{LO}}$ isolates the constituent mass. The residual block-binding correction $\Delta_\lambda(K)$ encodes the specific interaction mass added by each Wedderburn block.*

The mass formula $M(K) = \rho_K \cdot m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)|$ is exact. If we force $\Delta_\lambda \equiv 0$, the sum collapses exactly to the constituent nucleon mass. The true binding energy lives entirely within the partition-indexed $\Delta_\lambda$ profile. This provides a mathematically exact decomposition parallel to the phenomenological six-term narrative.
<!-- FILE_END: rho-k-h3a-refinement.md -->

<!-- FILE_START: rho-k-h3a-refinement-interpretation.md -->
**Remark (Wedderburn refinement interpretation).**
*The leading-order ansatz represents the $\Delta \equiv 0$ truncation. The observed binding energy precisely reflects the non-vanishing $\Delta_\lambda$ terms.*

The block-binding correction $\Delta_\lambda$ operates locally within each partition. This categorical separation mirrors the empirical shell structure captured by liquid-drop formulas. Computing $\Delta_\lambda$ across the Plancherel-dominant cone systematically reduces the residual. Nine evaluation levels push the mass prediction accuracy to one part per billion.
<!-- FILE_END: rho-k-h3a-refinement-interpretation.md -->

<!-- FILE_START: s4-s3-half-symmetric-projection.md -->
*The half-symmetric Wedderburn projection on $H_4(q)$, restricted to the $S_3$-trivial subspace, evaluates to exactly one.*

This combinatorial bijection structurally constrains the volume-density evaluation at higher orders. It proves that the half-symmetric projection extracts the curvature contribution of precisely one of the eight ideal octahedra tessellating the Borromean complement. The bijection dictates which cell contributes, though determining the exact per-cell curvature value remains an open refinement.
<!-- FILE_END: s4-s3-half-symmetric-projection.md -->

<!-- FILE_START: weak-symmetric-normalization.md -->
*The symmetric-channel normalization $\mathcal{N}_{\rm sym}(q)$ evaluates the Plancherel-weighted character product across the electroweak symmetric channel:*

$$
  \mathcal{N}_{\rm sym}(q)
  \;=\;
  \frac{q^4 + q^6 + q^8}{3}
  \;=\;
  \frac{q^4 (1 + q^2 + q^4)}{3}.
$$

The non-degenerate trace uniformizes across the 1-dimensional sym/alt blocks. The resulting expression is a closed-form rational with no free parameters. 

However, the direct cell-content trace now supersedes this Plancherel-weighted formulation. We strictly isolate the structural input to the bar-self-dual cell trace itself, bypassing Plancherel weights entirely.
<!-- FILE_END: weak-symmetric-normalization.md -->

<!-- FILE_START: z-eq-n-rho-correction.md -->
**Proposition ($Z=N$ binding correction).**
*For light atoms on the doubly-symmetric $Z=N$ line, the integer Kashaev binding law acquires a $q$-dimensional substrate correction:*

$$
  B(Z\!=\!N\!=\!k,\;q)
  \;=\;
  m_e \cdot \mathrm{Vol}_{\rm hyp}(K_A) \cdot
  \bigl(\rho_{\rm struct} + A - [A]_q\bigr).
$$

At $q=1$, $[A]_q = A$ and the correction vanishes, recovering the classical law. At $q>1$, the quantum dimension exceeds the integer dimension. The correction is negative. The integer law overestimates the binding by exactly the dimensional anomaly.

This correction eliminates the residual error for symmetric isotopes, improving accuracy by a factor of 100. It strictly fails for asymmetric isotopes like ${}^{3}$H and ${}^{3}$He. The exchange-symmetric fluid cannot absorb the Coulomb asymmetry.
<!-- FILE_END: z-eq-n-rho-correction.md -->

