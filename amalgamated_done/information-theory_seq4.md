<!-- FILE_START: optical-fibre-intro.md -->
To model the physical transmission of information, we introduce the **one-dimensional channel**. This construct represents an optical fibre acting as a one-dimensional waveguide. We emphasize that this physical "fibre" is distinct from the categorical fibre functor $\tau$.

A channel transmits information by carrying a braid word $\beta \in B_n$ along its length. The measurable output of this transmission is the Markov trace $\mathrm{tr}_M(\beta)$. The fibre is bounded by its **cladding**, a topological boundary that prevents strands from crossing the surface. This boundary strictly isolates the interior braid. Consequently, adjacent fibres decouple into a split configuration. The joint Markov trace of parallel fibres factorizes into the product of their individual traces. The total information capacity thus derives from the operational entropy of the substrate.
<!-- FILE_END: optical-fibre-intro.md -->

<!-- FILE_START: one-dim-qou-channel.md -->
*Lean sibling: structural, over a generic commutative ring $R$ (AGENTS.md §7c).*

**Definition.** A **one-dimensional channel** over a commutative ring $R$ is a bounded braid carrier along a line, conveying a braid word $\beta \in B_n$. The transmitted datum is the Markov trace $\mathrm{tr}_M(\beta) \in R$. 

The **cladding** is a topological boundary condition that confines $\beta$ so that no strand crosses the boundary surface. A channel is determined by its trace value. The **vacuum channel** is the empty fibre with $\beta = \mathbf{1}$ and $\mathrm{tr}_M(\mathbf{1}) = 1$.

The Lean formalization records this as the structure $\mathtt{OneDimChannel}\,R$. It includes the vacuum channel and the **parallel placement** of two side-by-side fibres:

$$
  \mathcal{F}_A \parallel \mathcal{F}_B := \langle\, \mathrm{tr}_M(\mathcal{F}_A)\,\mathrm{tr}_M(\mathcal{F}_B) \,\rangle .
$$

This product relies on the multiplicativity of the Markov trace over split links, as parallel cladded fibres decouple.
<!-- FILE_END: one-dim-qou-channel.md -->

<!-- FILE_START: parallel-fibre-noninteraction.md -->
*Lean sibling: structural, over a generic commutative ring $R$ (AGENTS.md §7c).*

**Proposition.** Let $\mathcal{F}_A$ and $\mathcal{F}_B$ be two one-dimensional channels placed in parallel. The cladding bounds each channel, rendering the joint configuration a **split link**. The boundary suppresses all crossings between the strands of $\mathcal{F}_A$ and those of $\mathcal{F}_B$. Because the Markov trace is multiplicative over split links, the transmitted datum of the joint channel factorizes:

$$
  \mathrm{tr}_M(\mathcal{F}_A \parallel \mathcal{F}_B) \;=\; \mathrm{tr}_M(\mathcal{F}_A)\,\mathrm{tr}_M(\mathcal{F}_B).
$$

Parallel placement is associative and commutative. The vacuum channel serves as the identity. Non-interacting fibres thus form a commutative monoid under the multiplicative trace. They act as independent multiplicative information sources. This topological decoupling guarantees that parallel fibres carry information without cross-talk.
<!-- FILE_END: parallel-fibre-noninteraction.md -->

<!-- FILE_START: fibre-channel-capacity.md -->
*Interpretation of the one-dimensional channel.*

Information is encoded in the braid word $\beta$ and read out via the Markov trace $\mathrm{tr}_M(\beta)$. Braid words sharing the same trace are indistinguishable to the receiver. The **capacity** of the channel is the entropy of the reachable trace image. It counts the distinguishable values of $\mathrm{tr}_M(\beta)$ rather than the raw braids.

An elementary crossing provides at most the operational entropy $\eta_q = (2q-1)/q^3$. The capacity of an $n$-strand fibre carrying a length-$\ell$ braid is bounded by $\ell\,\eta_q$ $q$-bits. This bound constitutes a one-dimensional analogue of the Bekenstein and Bremermann limits. 

Because parallel fibres do not interact, their joint Markov trace multiplies and their capacities add. A bundle of $k$ independent fibres carries exactly $k$ times the single-fibre capacity. This mirrors the classical additivity of independent information channels.
<!-- FILE_END: fibre-channel-capacity.md -->

<!-- FILE_START: photon-propagation-1d.md -->
*Interpretation of the one-dimensional channel.*

A photon is a trivial strand $\gamma$, knot-trivial under Markov closure. In a fibre, it is a propagating excitation that carries no crossings as it advances. The $n$ strands of the fibre represent its **modes**. A bounded fibre supports exactly $n$ propagating modes. This gives a topological origin to waveguide mode quantization, directly analogous to the discrete mode count of a step-index fibre.

Propagation is governed by the substrate velocity $c_q = 1/(q-1)$. The **dispersion** of a mode is the $q$-deformation of its propagation eigenvalue. A mode of wavenumber $k$ advances with the $q$-integer phase $[k]_q$ rather than the classical $k$. The group velocity thus acquires $O(1 - q^{-1})$ corrections. In the rigid, lossless limit of a straight fibre, these corrections reduce to linear dispersion. 

This energy-dependent mode velocity manifests in-vacuo dispersion at the channel level. It aligns with doubly-special-relativity phenomenology and is constrained by gamma-ray-burst bounds on archimedean deformation residues.
<!-- FILE_END: photon-propagation-1d.md -->
