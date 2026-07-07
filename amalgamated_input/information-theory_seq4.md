<!-- FILE_START: optical-fibre-intro.md -->
We now specialize to the simplest carrier of information: a **one-dimensional channel** (physically, an optical fibre). In this context, "fibre" denotes a physical one-dimensional waveguide that transmits information, distinct from the categorical fibre functor $\tau$.

A one-dimensional channel is a bounded braid carrier. The observable universe descends to one dimension as a line along which $n$ strands (the modes of the fibre) propagate while carrying a braid word $\beta \in B_n$. The information placed on the fibre is this braid. We transmit and measure its Markov trace $\mathrm{tr}_M(\beta)$. This is the same invariant that reads out particle content throughout this paper. The **cladding** serves as a topological boundary condition. It confines $\beta$ to the strand bundle, ensuring no strand crosses the surface of the fibre.

This surface boundary renders parallel fibres non-interacting. Two cladded fibres laid side by side form a split configuration. The boundary suppresses every crossing between a strand of one fibre and a strand of the other. Thus, the joint Hecke algebra factorizes as $H_n(q) \otimes H_m(q)$, and the joint Markov trace multiplies: $\mathrm{tr}_M(\beta_A \sqcup \beta_B) = \mathrm{tr}_M(\beta_A)\mathrm{tr}_M(\beta_B)$. This product over decoupled constituents shares the structural mechanism of the Borromean composite factorization. The information capacity of a single fibre is the entropy of the reachable trace image, bounded by the substrate's operational entropy $\eta_q$.

The following sections define the channel object, prove the non-interaction of parallel fibres, establish the Markov-trace capacity, and determine the $q$-deformed dispersion of a propagating mode. We then connect the linear, high-effective-$q$ regime of a fibre to the $q$-regime map. <!-- draft; remaining blocks in progress -->
<!-- FILE_END: optical-fibre-intro.md -->

<!-- FILE_START: one-dim-qou-channel.md -->
*Lean sibling: structural, over a generic commutative ring $R$ (AGENTS.md §7c) — the carried datum is the Markov-trace value.*

**Definition.** A **one-dimensional channel** over a coefficient ring $R$ is a bounded braid carrier. Physically, it models an optical fibre as a one-dimensional waveguide (distinct from the categorical fibre functor $\tau$). It is a line along which $n$ strands, the modes of the fibre, propagate while carrying a braid word $\beta \in B_n$. Its transmitted, measurable datum is the Markov trace $\mathrm{tr}_M(\beta) \in R$. This is the same invariant that reads out particle content elsewhere in this paper.

The **cladding** is the surface of the fibre. We model it as a topological boundary condition confining $\beta$ to the strand bundle: no strand crosses the surface. A channel is thus determined by its trace value. The **vacuum channel** is the empty fibre ($\beta = \mathbf{1}$, $\mathrm{tr}_M = 1$).

The Lean sibling records this as the structure $\mathtt{OneDimChannel}\,R$ carrying its $\mathrm{trace}$. It also includes the vacuum channel and the **parallel placement** of two side-by-side fibres:

$$
  \mathcal{F}_A \parallel \mathcal{F}_B := \langle\, \mathrm{tr}_M(\mathcal{F}_A)\,\mathrm{tr}_M(\mathcal{F}_B) \,\rangle .
$$

We justify this product through the multiplicativity of the trace. The surface boundary ensures parallel fibres form a split link. We establish this in the next proposition.
<!-- FILE_END: one-dim-qou-channel.md -->

<!-- FILE_START: parallel-fibre-noninteraction.md -->
*Lean sibling: structural, over a generic commutative ring $R$ (AGENTS.md §7c).*

**Proposition.** Let $\mathcal{F}_A, \mathcal{F}_B$ be two [one-dimensional QOU channels](#def:one-dim-qou-channel) placed in parallel. The cladding bounds each channel. The joint configuration is a **split link**. The surface boundary suppresses every crossing between a strand of $\mathcal{F}_A$ and a strand of $\mathcal{F}_B$. The Markov trace is multiplicative over split links. The transmitted datum of the joint channel therefore factorises,
$$
  \mathrm{tr}_M(\mathcal{F}_A \parallel \mathcal{F}_B) \;=\; \mathrm{tr}_M(\mathcal{F}_A)\,\mathrm{tr}_M(\mathcal{F}_B).
$$

Parallel placement is **associative** and **commutative**, with the vacuum channel as the identity. Non-interacting fibres form a commutative monoid under the multiplicative trace. They compose as **independent multiplicative information sources**. This decoupling governs composite knots, which are products over decoupled constituents. It explains why parallel optical fibres carry information without cross-talk.
<!-- FILE_END: parallel-fibre-noninteraction.md -->

<!-- FILE_START: fibre-channel-capacity.md -->
*Interpretation of the [one-dimensional QOU channel](#def:one-dim-qou-channel).*

The information transmitted by a single fibre is encoded in its braid word $\beta$. The receiver reads out the Markov trace $\mathrm{tr}_M(\beta)$. The **capacity** of the channel is therefore the entropy of the reachable trace image. This counts the number of distinguishable values $\mathrm{tr}_M(\beta)$ can take as $\beta$ ranges over the admissible braids on the fibre's $n$ strands. Braid words sharing the same trace are indistinguishable to the receiver. Capacity counts trace-classes, not raw braids.

Each elementary crossing provides at most the operational entropy $\eta_q = (2q-1)/q^3$ of information. The capacity of an $n$-strand fibre carrying a length-$\ell$ braid is bounded by $\ell\,\eta_q$ $q$-bits. This realizes the one-dimensional specialisation of the Bekenstein and Bremermann limits. 

Parallel fibres do not interact. The total capacity is strictly additive. The joint Markov trace of $k$ cladded fibres multiplies, meaning their log-capacities add. A bundle of $k$ independent fibres carries $k$ times the single-fibre rate. This is the categorical analogue of the classical rule that independent channels add their capacities.
<!-- FILE_END: fibre-channel-capacity.md -->

<!-- FILE_START: photon-propagation-1d.md -->
*Interpretation of the [one-dimensional QOU channel](#def:one-dim-qou-channel).*

A photon is the trivial strand $\gamma$, making it knot-trivial under Markov closure. On a fibre, it is a propagating excitation that carries no crossings of its own as it advances along the line. The fibre's $n$ strands represent its **modes**. A bounded fibre supports exactly $n$ propagating modes. This provides the topological origin of mode quantisation in a waveguide, mirroring how a step-index fibre admits a finite, discrete mode count fixed by its cross-section.

The substrate velocity $c_q = 1/(q-1)$ governs propagation. The **dispersion** of a mode is the $q$-deformation of its propagation eigenvalue. A mode of wavenumber $k$ advances with the $q$-integer phase $[k]_q$ rather than the classical $k$. The group velocity therefore acquires $O(1 - q^{-1})$ corrections. This fractional deformation also appears in photonic-Hall quantisation. In the rigid, lossless limit of a straight fibre with no scattering, these corrections reduce to a linear dispersion. The fibre transmits each mode independently, ensuring parallel channels do not interact.

The energy dependence of the mode velocity provides the channel-level face of in-vacuo dispersion. We document its relation to doubly-special-relativity phenomenology, the gamma-ray-burst bounds on archimedean deformation residues, and the conjectural suppression scale in [the DSR remark](#rem:dsr-planck-scale-phenomenology) and [the suppression-scale conjecture](#conj:dispersion-suppression-scale).
<!-- FILE_END: photon-propagation-1d.md -->

