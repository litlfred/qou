---
doc_id: arxiv-2512.18642v1
doc_title: "A Hidden Quantum Markov model framework for Entanglement and Topological Order in the AKLT Chain"
section_id: sec-002-hidden-quantum-markov-models
section_title: "Hidden Quantum Markov Models"
section_number: null
pages: 3-4
source_pdf: 2512.18642v1.pdf
source_sha256: c4c7f8b0a719aa2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.976
doc_brief: "A Hidden Quantum Markov model framework for Entanglement and Topological Order in the AKLT Chain — This paper introduces a hidden quantum Markov models (HQMMs) framework to the Af"
---
Let $\mathcal{H}$ and $\mathcal{K}$ be two finite-dimensional Hilbert spaces and let $\mathcal{B}(\mathcal{H})$ and $\mathcal{B}(\mathcal{K})$ be the algebras of bounded operators over the Hilbert spaces $\mathcal{H}$ and $\mathcal{K}$, respectively. A map is $\mathcal{E}$ from $\mathcal{B}(\mathcal{H})$ to $\mathcal{B}(\mathcal{K})$ is said to be *completely positive* if all its matrix amplifications $$\mathcal{E}: M_n(\mathcal{A}) \to M_n(\mathcal{B}), \quad [a_{ij}] \mapsto [\Phi(a_{ij})]$$ preserve positivity for every $n \in \mathbb{N}$. A *quantum channel* is a completely positive, trace-preserving map $\Phi: \mathcal{A} \to \mathcal{B}$ that describes general physical transformations of quantum states. The fundamental duality between state and observable evolution is encoded in the dual map $\Phi^*: \mathcal{B}^* \to \mathcal{A}^*$, defined via the relation $$\operatorname{Tr}(\Phi(\rho) X) = \operatorname{Tr}(\rho \, \Phi^*(X)) \quad \text{for all } \rho \in \mathcal{A}_*, \, X \in \mathcal{B}.$$ This establishes the precise correspondence between the Schrödinger picture (state evolution $\rho \mapsto \Phi(\rho)$) and the Heisenberg picture (observable evolution $X \mapsto \Phi^*(X)$).

A *transition expectation* $\mathcal{E}: \mathcal{A} \otimes \mathcal{B} \to \mathcal{A}$ is a completely positive, identity-preserving map that generalizes the notion of conditional expectation to open quantum systems. The duality between quantum channels and transition expectations manifests through the adjoint relationship: if $\mathcal{E}$ is a transition expectation, then its dual $\mathcal{E}^*: \mathcal{A}^* \to (\mathcal{A} \otimes \mathcal{B})^*$ defines a quantum channel when properly normalized. This framework provides the mathematical foundation for describing emission, absorption, and general interaction processes in quantum information theory.

HQMM provides a generative description of quantum stochastic processes through a bipartite structure separating hidden dynamics from observable outputs. Formally, an HQMM is defined as a state on the quasi-local algebra $\mathcal{A}_{H,O} = (\mathcal{B}(\mathcal{H}) \otimes \mathcal{B}(\mathcal{H}_{1}))^{\otimes \mathbb{N}}$, representing an infinite bipartite quantum system where $\mathcal{A}_{H} = \mathcal{B}(\mathcal{H})^{\otimes \mathbb{N}}$ describes the hidden system and $\mathcal{A}_{O} = \mathcal{B}(\mathcal{H}_{1})^{\otimes \mathbb{N}}$ represents the observable output system [@AGLS24Q]. The model is specified by a *generative triplet* $\Xi = (\phi_0, \mathcal{E}_H, \mathcal{E}_{O,H})$, where:

-   $\phi_0: \mathcal{B}(\mathcal{H})\to \mathbb{C}$ is an initial state on the hidden algebra;

-   $\mathcal{E}_{H}: \mathcal{B}(\mathcal{H}) \otimes \mathcal{B}(\mathcal{H}) \to \mathcal{B}(\mathcal{H})$ is a CPIP map governing hidden system dynamics;

-   $\mathcal{E}_{O,H}: \mathcal{B}(\mathcal{H}) \otimes \mathcal{B}(\mathcal{H}_{1})\to \mathcal{B}(\mathcal{H})$ is a CPIP map encoding observable emission.

The conventional HQMM follows quantum causality where measurement precedes state evolution. For sequences $X = \bigotimes_{m=0}^n X_m$ and $Y = \bigotimes_{m=0}^n Y_m$, the state is: $$\label{eq:standard_HQMM}
\varphi_{H,O}(X \otimes Y) = \phi_0 \circ E_{X_0,Y_0} \circ E_{X_1,Y_1} \circ \cdots \circ E_{X_n,Y_n}(h),$$ where the forward transition map is defined as: $$\label{eq:E_map}
E_{X,Y}(\cdot) := \mathcal{E}_H \big( \mathcal{E}_{O,H}(X \otimes Y) \otimes \cdot \big).$$ This structure implements the causal sequence: at each step $m$, the emission map $\mathcal{E}_{O,H}$ first processes the observable $Y_m$ with the current hidden state, followed by hidden state propagation via $\mathcal{E}_{H}$.
