---
doc_id: arxiv-2512.18642v1
doc_title: "A Hidden Quantum Markov model framework for Entanglement and Topological Order in the AKLT Chain"
section_id: sec-006-spt-order-on-the-aklts-hqmms
section_title: "SPT order on the AKLT,s HQMMs"
section_number: null
pages: 15-16
source_pdf: 2512.18642v1.pdf
source_sha256: c4c7f8b0a719aa2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.977
doc_brief: "A Hidden Quantum Markov model framework for Entanglement and Topological Order in the AKLT Chain — This paper introduces a hidden quantum Markov models (HQMMs) framework to the Af"
---
[]{#Sect_SPT_HQMM label="Sect_SPT_HQMM"} The AKLT state's remarkable robustness stems from its symmetry-protected topological (SPT) order, which manifests elegantly within its Hidden Quantum Markov Model (HQMM) description. To understand this protection mechanism, clarify how symmetries operate in the HQMM framework.

Let $G$ be a symmetry group with unitary representations $\pi: G \to \mathcal{U}(\mathcal{H}_{1/2})$ on the virtual space and $\rho: G \to \mathcal{U}(\mathcal{H}_1)$ on the physical space.

The heart of the matter lies in the *emission transition expectation* $\mathcal{E}_{O,H}$, which implements the quantum-classical interface between hidden and observable sectors. This channel is built from the AKLT tensors $A_k$ through: $$\label{eq:EOH2}
  \mathcal{E}_{O,H}(Z \otimes Y) = \sum_{k,k'} \langle k'|Y|k\rangle A_k Z A_{k'}^\dagger$$ The fundamental covariance condition [@AKLT1987; @Pollmann2010]: $$\label{eq:Cov}
    \sum_{k'} \rho(g)_{k k'} A_{k'} = \pi(g) A_k \pi(g)^\dagger$$ ensures that $\mathcal{E}_{O,H}$ transforms covariantly, meaning that symmetry transformations commute with the emission process. This covariance propagates to the composite transition map $E_{X,Y}$ that drives the HQMM dynamics: $$E_{X,Y}(Z) = \mathcal{E}_H(\mathcal{E}_{O,H}(X \otimes Y) \otimes Z)$$ The map $E_{X,Y}$ inherits the symmetry property: $$E_{\rho(g)X\rho(g)^\dagger, \rho(g)Y\rho(g)^\dagger}(\pi(g)Z\pi(g)^\dagger) = \pi(g)E_{X,Y}(Z)\pi(g)^\dagger$$

This hierarchical symmetry preservation---from individual channels to composite dynamics---ensures that the AKLT state's topological character remains protected throughout the quantum Markov process. The HQMM framework thus reveals how SPT order emerges from the consistent interplay between hidden dynamics and symmetry constraints across all scales of the system.

::: theorem
[]{#thm:EOH-sym label="thm:EOH-sym"} Let $G$ be a symmetry group with unitary representations $\rho: G \to \mathcal{U}(\mathcal{H}_{1})$ on the physical space and $\pi: G \to \mathcal{U}(\mathcal{H}_{\frac{1}{2}})$ on the virtual space. The emission transition expectation $\mathcal{E}_{O,H}: \mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \otimes \mathcal{B}(\mathcal{H}_{1}) \to \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$ defined in [\[eq:EOH2\]](#eq:EOH2){reference-type="eqref" reference="eq:EOH2"} is $G$-equivariant. That is, for all $g \in G$, $$\label{eq:equivariance_correct}
    \mathcal{E}_{O,H}\left( \pi(g) X \pi(g)^\dagger \otimes \rho(g) Y \rho(g)^\dagger \right) = \pi(g) \, \mathcal{E}_{O,H}(X \otimes Y) \, \pi(g)^\dagger,$$ for all $X \in \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$ and $Y \in \mathcal{B}(\mathcal{H}_{1})$.
:::

::: proof
*Proof.* Let $g \in G$, $X \in \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$, and $Y \in \mathcal{B}(\mathcal{H}_{1})$ be arbitrary. We compute the left-hand side of [\[eq:equivariance_correct\]](#eq:equivariance_correct){reference-type="eqref" reference="eq:equivariance_correct"}: $$\mathrm{LHS} = \mathcal{E}_{O,H}\left( \pi(g) X \pi(g)^\dagger \otimes \rho(g) Y \rho(g)^\dagger \right) = \sum_{m, m'} \langle m | \rho(g) Y \rho(g)^\dagger | m' \rangle \, A_m \left( \pi(g) X \pi(g)^\dagger \right) A_{m'}^\dagger.$$ Expanding the matrix element in the physical basis $\{|m\rangle\}$ yields: $$\langle m | \rho(g) Y \rho(g)^\dagger | m' \rangle = \sum_{k, k'} \rho(g)_{m k} \langle k | Y | k' \rangle (\rho(g)^\dagger)_{k' m'}.$$ Substituting this back into the expression for LHS and reordering the finite sums gives: $$\mathrm{LHS} = \sum_{k, k'} \langle k | Y | k' \rangle \left( \sum_{m, m'} \rho(g)_{m k} (\rho(g)^\dagger)_{k' m'} \, A_m \left( \pi(g) X \pi(g)^\dagger \right) A_{m'}^\dagger \right).$$ Let $S_{k,k'}$ denote the inner sum. We can factor it as follows: $$S_{k,k'} = \left( \sum_{m} \rho(g)_{m k} A_m \right) \left( \pi(g) X \pi(g)^\dagger \right) \left( \sum_{m'} (\rho(g)^\dagger)_{k' m'} A_{m'}^\dagger \right).$$ We now apply the covariance condition. The first factor is given directly by [\[eq:Cov\]](#eq:Cov){reference-type="eqref" reference="eq:Cov"}: $$\sum_{m} \rho(g)_{m k} A_m = \pi(g) A_k \pi(g)^\dagger.$$ The third factor is the adjoint of the covariance condition for index $k'$: $$\sum_{m'} (\rho(g)^\dagger)_{k' m'} A_{m'}^\dagger = \left( \sum_{m'} \rho(g)_{m' k'} A_{m'} \right)^\dagger = \left( \pi(g) A_{k'} \pi(g)^\dagger \right)^\dagger = \pi(g) A_{k'}^\dagger \pi(g)^\dagger.$$ Substituting these expressions into $S_{k,k'}$ and using the unitarity of $\pi(g)$ $(\pi(g)^\dagger \pi(g) = I)$ gives: $$S_{k,k'} = \left( \pi(g) A_k \pi(g)^\dagger \right) \left( \pi(g) X \pi(g)^\dagger \right) \left( \pi(g) A_{k'}^\dagger \pi(g)^\dagger \right) = \pi(g) A_k X A_{k'}^\dagger \pi(g)^\dagger.$$ Substituting $S_{k,k'}$ back into the expression for LHS yields the final result: $$\begin{aligned}
\mathrm{LHS} &= \sum_{k, k'} \langle k | Y | k' \rangle \, \pi(g) A_k X A_{k'}^\dagger \pi(g)^\dagger \\
&= \pi(g) \left( \sum_{k, k'} \langle k | Y | k' \rangle A_k X A_{k'}^\dagger \right) \pi(g)^\dagger \\
&= \pi(g) \, \mathcal{E}_{O,H}(X \otimes Y) \, \pi(g)^\dagger.
\end{aligned}$$ This completes the proof of [\[eq:equivariance_correct\]](#eq:equivariance_correct){reference-type="eqref" reference="eq:equivariance_correct"}. ◻
:::

Theorem [\[thm:EOH-sym\]](#thm:EOH-sym){reference-type="ref" reference="thm:EOH-sym"} provides a key understanding about the unique properties of AKLT state. It shows that the emission map is a perfect symmetry bridge. The equation ([\[eq:equivariance_correct\]](#eq:equivariance_correct){reference-type="ref" reference="eq:equivariance_correct"}) guarantees that the symmetry of the hidden spin-½ particles is perfectly converted into the standard symmetry of the physical spin-1 particles we observe.

The dual of this map, which governs how information flows back to the hidden level, must also respect this symmetry. The covariance implies that for a virtual density matrix $\sigma$, the dual action satisfies:

$$\mathcal{E}_{O,H}^*\left( \pi(g) \sigma \pi(g)^\dagger \right) = \left( \pi(g) \otimes \rho(g) \right) \mathcal{E}_{O,H}^*(\sigma) \left( \pi(g)^\dagger \otimes \rho(g)^\dagger \right).$$

This means that any physical process acting on the spin-1 chain---like time evolution under a symmetric Hamiltonian---will automatically induce a corresponding action on the hidden spin-½ that faithfully preserves their projective character.
