---
doc_id: arxiv-2512.18642v1
doc_title: "A Hidden Quantum Markov model framework for Entanglement and Topological Order in the AKLT Chain"
section_id: sec-004-hqmm-structure-of-the-aklt-state
section_title: "HQMM Structure of the AKLT State"
section_number: null
pages: 6-12
source_pdf: 2512.18642v1.pdf
source_sha256: c4c7f8b0a719aa2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 0.99
doc_brief: "A Hidden Quantum Markov model framework for Entanglement and Topological Order in the AKLT Chain — This paper introduces a hidden quantum Markov models (HQMMs) framework to the Af"
---
[]{#Sect_HQMM_AKLT label="Sect_HQMM_AKLT"} The AKLT state's unique structure can be naturally formulated as a HQMM, revealing a profound connection between topological quantum matter and quantum stochastic processes. This framework cleanly separates the system into hidden virtual degrees of freedom that encode topological information and observable physical degrees accessible to measurement.

The *Hidden Quantum Markov Model* for the AKLT chain is specified by the generative triplet $\Xi_{\mathrm{AKLT}} = (\phi_0, \mathcal{E}_H, \mathcal{E}_{O,H})$ where:

-   $\phi_0: \mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \to \mathbb{C}$ initializes the hidden system

-   $\mathcal{E}_H: \mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \otimes \mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \to \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$ governs the hidden dynamics of the spin-½ system.

-   $\mathcal{E}_{O,H}: \mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \otimes \mathcal{B}(\mathcal{H}_{1}) \to \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$ emission transition expectation that encodes the spin-1 system through the spin-½ hidden system.

The sequential structure follows quantum causality through the transition map $$\label{eq:TXY}
  E_{X_\ell,Y_\ell}(\cdot) = \mathcal{E}_H(\mathcal{E}_{O,H}(X_\ell \otimes Y_\ell) \otimes \cdot)$$ generating the complete state $$\label{eq_TXY}
 \varphi_{O,H}(X \otimes Y) = \phi_0 \circ E_{X_0,Y_0} \circ E_{X_1,Y_1} \circ \cdots \circ E_{X_n,Y_n}({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}),$$ where $X = X_1\otimes\cdots X_n\in \mathcal{B}(\mathcal{H}_{\frac{1}{2}})^{\otimes n}$ and $Y = Y_1\otimes\cdots Y_n\in \mathcal{B}(\mathcal{H}_{1})^{\otimes n}$.

This HQMM formulation provides a powerful framework for understanding how the AKLT state's topological properties emerge from the hidden quantum Markovian dynamics, which we will now analyze through the lens of symmetry protection.

::: center
:::

This HQMM formulation provides powerful quantum information tools to analyze entanglement scaling, quantum memory effects, and topological stability under decoherence, establishing fundamental connections between quantum many-body physics and quantum computational models.

In the subsequent analysis, we will explicitly derive the transition expectations governing the system's dynamics and elucidate the intricate correlation structure of the underlying hidden Markov model. This will be achieved by examining how the hidden algebra $\mathcal{B}(\mathcal{H}_{\frac{1}{2}})^{\otimes \mathbb{N}}$, which encodes the virtual spin network responsible for topological entanglement, correlates with the observation algebra $\mathcal{B}(\mathcal{H}_{1})^{\otimes \mathbb{N}}$, representing the physically measurable degrees of freedom, via the CPIP maps $\mathcal{E}_H$ and $\mathcal{E}_{O,H}$ implemented through precise virtual isometry $V$ that captures the hidden entanglement structure of the model and an observation isometry $W$, that preserves the SPT order.

The mapping $V: \mathcal{H}_{\frac{1}{2}} \to \mathcal{H}_{\frac{1}{2}} \otimes \mathcal{H}_{\frac{1}{2}}$ is a partial isometry that builds entanglement between virtual spin spaces. A specific choice of $V$ is given by: $$\label{eq:V}
  V = |\Psi^-\rangle \langle \uparrow | + |\Psi^+\rangle \langle \downarrow |,$$ where $|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$ is the singlet state forming the original AKLT valence bonds, and $|\Psi^+\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)$ is the symmetric triplet component. While this specific $V$ is a canonical choice, various other isometries can be selected to encode the system's entanglement and symmetry, each leading to a different physical state that can still saturate the maximal entanglement of the underlying virtual system.

Complementarily, the *observation isometry* $W: \mathcal{H}_{\frac{1}{2}} \to \mathcal{H}_{\frac{1}{2}} \otimes \mathcal{H}_{1}$ maps virtual states to physical spin-1 observables: $$\label{eq:W}
  W\xi = \sum_{k \in \{+,0,-\}} A_{k}\xi \otimes |k\rangle,\quad \forall \xi \in \mathcal{H}_{\frac{1}{2}}$$ where the matrices $A_{k}$ are the standard AKLT MPS tensors. This structure explicitly reveals the AKLT state as a quantum autoregressive process, where sequential application of $W$ generates the physical spin-1 chain from the virtual space evolution.

::: lemma
[]{#lem:Eh label="lem:Eh"} The map $\mathcal{E}_H: \mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \otimes \mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \to \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$ defined by the Stinespring dilation $$\label{eq:EH}
\mathcal{E}_H(X \otimes X') = V^\dagger(X \otimes X')V$$ where $V: \mathcal{H}_{\frac{1}{2}} \to \mathcal{H}_{\frac{1}{2}} \otimes \mathcal{H}_{\frac{1}{2}}$ is the partial isometry from ([\[eq:V\]](#eq:V){reference-type="ref" reference="eq:V"}), constitutes a hidden transition expectation CPIP. The dual quantum channel $\mathcal{E}_H^*: \mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \to \mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \otimes \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$, defined via the Hilbert-Schmidt adjoint, acts as: $$\label{eq:EH_dual}
\mathcal{E}_H^*(\rho) = V\rho V^\dagger.$$ This implements virtual bond preparation in the AKLT entanglement structure.
:::

::: proof
*Proof.* We first verify that $V$ is a partial isometry. From the definition ([\[eq:V\]](#eq:V){reference-type="ref" reference="eq:V"}), we compute $V^\dagger V$: $$\begin{aligned}
V^\dagger V |\uparrow\rangle &= V^\dagger\left( \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle) \right)
= \frac{1}{2}(|\uparrow\rangle + |\downarrow\rangle) - \frac{1}{2}(-|\uparrow\rangle + |\downarrow\rangle) = |\uparrow\rangle, \\
V^\dagger V |\downarrow\rangle &= V^\dagger\left( \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle) \right)
= \frac{1}{2}(|\uparrow\rangle + |\downarrow\rangle) + \frac{1}{2}(-|\uparrow\rangle + |\downarrow\rangle) = |\downarrow\rangle.
\end{aligned}$$ Hence $V^\dagger V = {\bf 1}\!\!{\rm I}$, proving $V$ is an isometry (and therefore a partial isometry).

Complete positivity of $\mathcal{E}_H$ follows from the Stinespring dilation: for any $n \in \mathbb{N}$ and $P \geq 0$ in $\mathcal{B}(\mathbb{C}^n \otimes \mathcal{H}_{\frac{1}{2}} \otimes \mathcal{H}_{\frac{1}{2}})$, $$({\bf 1}\!\!{\rm I}_n \otimes \mathcal{E}_H)(P) = ({\bf 1}\!\!{\rm I}_n \otimes V)^\dagger P ({\bf 1}\!\!{\rm I}_n \otimes V) \geq 0.$$ Unitality is immediate: $$\mathcal{E}_H({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}} \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}) = V^\dagger({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}} \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}})V = V^\dagger V = {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}.$$

For the dual channel, take any $X,X',\rho \in \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$: $$\begin{aligned}
\langle \mathcal{E}_H(X \otimes X'), \rho \rangle_{\mathrm{HS}}
&= \mathrm{Tr}[(V^\dagger(X \otimes X')V)^\dagger \rho] \\
&= \mathrm{Tr}[V^\dagger(X'^\dagger \otimes X^\dagger)V\rho] \\
&= \mathrm{Tr}[(X'^\dagger \otimes X^\dagger)V\rho V^\dagger] \\
&= \langle X \otimes X', V\rho V^\dagger \rangle_{\mathrm{HS}}.
\end{aligned}$$ where we used the cyclic property of the trace. This proves $\mathcal{E}_H^*(\rho) = V\rho V^\dagger$.

For $\rho = p|\uparrow\rangle\langle\uparrow| + (1-p)|\downarrow\rangle\langle\downarrow|$, we compute: $$\begin{aligned}
\mathcal{E}_H^*(\rho) &= p \cdot V|\uparrow\rangle\langle\uparrow|V^\dagger + (1-p) \cdot V|\downarrow\rangle\langle\downarrow|V^\dagger \\
&= \frac{p}{2}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)(\langle\uparrow\downarrow| - \langle\downarrow\uparrow|) \\
&\quad + \frac{1-p}{2}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)(\langle\uparrow\downarrow| + \langle\downarrow\uparrow|) \\
&= \frac{1}{2}|\uparrow\downarrow\rangle\langle\uparrow\downarrow| + \frac{1}{2}|\downarrow\uparrow\rangle\langle\downarrow\uparrow| \\
&\quad + \frac{1-2p}{2}(|\uparrow\downarrow\rangle\langle\downarrow\uparrow| + |\downarrow\uparrow\rangle\langle\uparrow\downarrow|)
\end{aligned}$$ This expression is verified by checking the extreme cases: when $p=1$ (pure $|\uparrow\rangle$), we recover the singlet state projector (up to normalization), and when $p=0$ (pure $|\downarrow\rangle$), we obtain the triplet state projector. ◻
:::

::: remark
The hidden transition expectation $\mathcal{E}_H$ and its dual $\mathcal{E}_H^*$ link the dynamics of the AKLT chain at consecutive times. The dual channel $\mathcal{E}_H^*$ acts on density matrices, extending a state $\rho^{(n)}$ at time $n$ to an entangled bipartite state $\mathcal{E}_H^*(\rho^{(n)}) = V\rho^{(n)}V^\dagger$ at times $(n-1,n)$.

Conversely, $\mathcal{E}_H$ acts on operators. Its action on a generic operator $X$ is given by the conditional expectation: $$\mathcal{E}_H(X) = V^\dagger X V.$$ This projects the joint operator $X$ on the bipartite system $(n-1,n)$ down to an operator on the marginal system at time $n$, enforcing the Markovian structure via $\rho^{(n)} = \mathcal{E}_H(\rho^{(n-1,n)})$.

This structure reveals the AKLT chain's quantum memory: the isometry $V$ creates the virtual singlets that propagate correlations, with the virtual bond space correlating successive temporal slices.

This dual pair of operations ($\mathcal{E}_H$, $\mathcal{E}_H^*$) constitutes a consistent family of conditional expectations and state preparations that implement the quantum Markov property. The composition $\mathcal{E}_H \circ \mathcal{E}_H^* = {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}$ ensures that extending then marginalizing returns the original state, while $\mathcal{E}_H^* \circ \mathcal{E}_H$ projects onto the range of $V$, which encodes the specific entanglement structure of the AKLT virtual bonds. This mathematical structure provides a precise formulation of how the HQMM captures the temporal correlations and entanglement propagation in symmetry-protected topological phases.
:::

::: lemma
[]{#lem:emission_transition label="lem:emission_transition"} Let $W: \mathcal{H}_{\frac{1}{2}} \to \mathcal{H}_{\frac{1}{2}} \otimes \mathcal{H}_{1}$ be the partial isometry from ([\[eq:W\]](#eq:W){reference-type="ref" reference="eq:W"}). The map $\mathcal{E}_{O,H}: \mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \otimes \mathcal{B}(\mathcal{H}_{1}) \to \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$ defined by $$\label{eq:EOH}
\mathcal{E}_{O,H}(X \otimes Y) = W^{\dagger} X\otimes Y W = \sum_{k,k'} \langle k' | Y | k \rangle  A_{k} X A_{k'}^{\dagger}$$ is an emission transition expectation. Its dual channel $\mathcal{E}_{O,H}^*: \mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \to \mathcal{B}(\mathcal{H}_{\frac{1}{2}}) \otimes \mathcal{B}(\mathcal{H}_{1})$ acts as: $$\label{eq:EOH_dual}
\mathcal{E}_{O,H}^*(Z) = \sum_{k,k'} A_{k}^{\dagger} Z A_{k'} \otimes |k\rangle\langle k'|.$$
:::

::: proof
*Proof.* The proof proceeds by systematically establishing each property of the emission transition expectation and its dual channel. We begin by verifying that $W$ is indeed a partial isometry. Computing $W^\dagger W$ using the explicit form from ([\[eq:W\]](#eq:W){reference-type="ref" reference="eq:W"}) yields: Here is the paraphrased text using $A_k$ and $A_{k'}$ notation:

$$W^\dagger W = \left(\sum_k A_{k}^{\dagger} \otimes \langle k|\right)\left(\sum_{k'} A_{k'} \otimes |k'\rangle\right) = \sum_{k,k'} A_{k}^{\dagger} A_{k'} \otimes \langle k|k'\rangle = \sum_k A_k^{\dagger} A_{k} = {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}},$$ where the final equality represents the fundamental completeness relation satisfied by the AKLT MPS matrices, confirming the isometric property.

The equivalence between the Stinespring form and the explicit Kraus representation is established through direct computation: $$W^\dagger(X \otimes Y)W = \left(\sum_k A_{k}^{\dagger} \otimes \langle k|\right)(X \otimes Y)\left(\sum_{k'} A_{k'} \otimes |k'\rangle\right) = \sum_{k,k'} A_{k}^{\dagger} X A_{k'} \otimes \langle k|Y|k'\rangle = \sum_{k,k'} \langle k'|Y|k\rangle A_{k} X A_{k}^{\dagger}.$$ where the adjoint symmetry of the inner product ensures the final form matches the definition.

Complete positivity follows immediately from the Stinespring dilation: for any positive operator $P$ in the amplified space, the map $({\bf 1}\!\!{\rm I}_n \otimes \mathcal{E}_{O,H})(P)$ manifests as a conjugation by the isometric extension $({\bf 1}\!\!{\rm I}_n \otimes W)$, preserving positivity. Unitality is verified through the chain: $$\mathcal{E}_{O,H}({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}} \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}_{1}}) = W^\dagger({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}} \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}_{1}})W = W^\dagger W = {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}$$ demonstrating preservation of the identity.

The dual channel characterization emerges from the Hilbert-Schmidt adjoint relation. For arbitrary operators $X,Y,Z$, we systematically derive: $$\langle \mathcal{E}_{O,H}(X \otimes Y), Z \rangle_{\mathrm{HS}} = \mathrm{Tr}[(W^\dagger(X \otimes Y)W)^\dagger Z] = \langle X \otimes Y, W Z W^\dagger \rangle_{\mathrm{HS}},$$ establishing $\mathcal{E}_{O,H}^*(Z) = W Z W^\dagger$. The explicit Kraus form follows by expanding this expression: $$\begin{aligned}
W Z W^\dagger &= \left(\sum_k A^{[k]} \otimes |k\rangle\right) Z \left(\sum_{k'} A^{[k']\dagger} \otimes \langle k'|\right) \\
&= \sum_{k,k'} A^{[k]} Z A^{[k']\dagger} \otimes |k\rangle\langle k'|,
\end{aligned}$$ completing the demonstration of all stated properties. ◻
:::

::: theorem
[]{#thm:main1 label="thm:main1"} Let $\phi_0$ be an initial state on $\mathcal{B}(\mathcal{H}_{\frac{1}{2}})$, $\mathcal{E}_H: \mathcal{B}(\mathcal{H}_{\frac{1}{2}})\otimes \mathcal{B}(\mathcal{H}_{\frac{1}{2}})\to \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$ the hidden transition expectation ([\[eq:EH\]](#eq:EH){reference-type="ref" reference="eq:EH"}), and $\mathcal{E}_{O,H}: \mathcal{B}(\mathcal{H}_{\frac{1}{2}})\otimes \mathcal{B}(\mathcal{H}_{1})\to \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$ the emission transition expectation ([\[eq:EOH\]](#eq:EOH){reference-type="ref" reference="eq:EOH"}). For the HQMM $\varphi_{O,H}$ associated with the triple $\Xi = (\phi_0, \mathcal{E}_H, \mathcal{E}_{O,H})$ and local observables $X \otimes Y = \bigotimes_{i=1}^{n} X_i \otimes Y_i$, we have: $$\label{eq_phiOH}
\varphi_{O,H}(X \otimes Y) = \sum_{\substack{k_1,\dots,k_n \\ k'_1,\dots,k'_n}} \left( \prod_{\ell=1}^n \langle k_\ell | Y_\ell | k'_\ell \rangle \right) \varphi_{\substack{k_1,\dots,k_n \\ k'_1,\dots,k'_n}}(X),$$ where the coefficient functionals are given by the nested composition: $$\label{eq:coefE_func}
\varphi_{\substack{k_1,\dots,k_n \\ k'_1,\dots,k'_n}}(X) = \phi_0 \left( V^{\dagger} \left( A_{k_1}X_1 A_{k'_1}^\dagger \otimes  \cdots \otimes V^{\dagger}\left( A_{k_n}X_n A_{k'_n}^\dagger \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}} \right)V \cdots \right)V \right).$$
:::

::: proof
*Proof.* The fundamental building block ([\[eq:E_map\]](#eq:E_map){reference-type="ref" reference="eq:E_map"}) of the HQMMs emerges from the expression: $$E_{X_{\ell}, Y_{\ell}}(Z) = \mathcal{E}_{H}(\mathcal{E}_{O,H}(X_\ell \otimes Y_\ell) \otimes Z)

, \qquad \forall Z\in \mathcal{B}_H$$ Substituting the emission transition expectation: $$\begin{aligned}
E_{X_n,Y_n}({\bf 1}\!\!{\rm I}_{\mathcal{H}}) &= \mathcal{E}_H \left( \mathcal{E}_{O,H}(X \otimes Y) \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}} \right) \\
&\overset{(\ref{eq:EOH})}{=} \mathcal{E}_H \left( \sum_{k_n,k_n'} \langle k_n | Y_n | k_n' \rangle A_{k_n} X_n A_{k'_n}^\dagger \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}} \right) \\
&\overset{(\ref{eq:EH})}{=} \sum_{k_n,k'_n} \langle k_n | Y_n | k'_n \rangle \mathcal{E}_H \left( A_{k_n} X_n A_{k'_n}^\dagger \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}} \right)
\end{aligned}$$

We now compute the $n$-fold composition by induction. For the base case $n=1$: $$\varphi_{O,H}(X_1 \otimes Y_1) = \phi_0 \circ E_{X_1,Y_1}(\mathcal{{\bf 1}\!\!{\rm I}}_{\mathcal{H}}) = \sum_{k_1,k'_1} \langle k_1 | Y_1 | k'_1 \rangle \phi_0\left( \mathcal{E}_H(A_{k_1}X_1 A_{k'_1}^\dagger \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}) \right),$$ which matches the theorem statement. For the inductive step, assume the decomposition holds for $n-1$: $$E_{X_2,Y_2} \circ \cdots \circ E_{X_n,Y_n}(\mathcal{{\bf 1}\!\!{\rm I}}_{\mathcal{H}}) = \sum_{\substack{k_2,\dots,k_n \\ k'_2,\dots,k'_n}} \left( \prod_{\ell=2}^n \langle k_\ell | Y_\ell | k'_\ell \rangle \right) \mathcal{E}_H\left( A_{k_2}X_2 A_{k'_2}^\dagger \otimes \cdots \otimes \mathcal{E}_H\left( A_{k_n}X_n A_{k'_n}^\dagger \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}} \right) \cdots \right).$$ Applying $E_{X_1,Y_1}$ to this expression: $$\begin{aligned}
&E_{X_1,Y_1} \circ E_{X_2,Y_2} \circ \cdots \circ E_{X_n,Y_n}({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}) \\
&= \sum_{k_1,k'_1} \langle k_1 | Y_1 | k'_1 \rangle \mathcal{E}_H \left( A_{k_1}X_1 A_{k'_1}^\dagger \otimes E_{X_2,Y_2} \circ \cdots \circ E_{X_n,Y_n}({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}) \right) \\
&= \sum_{\substack{k_1,\dots,k_n \\ k'_1,\dots,k'_n}} \left( \prod_{\ell=1}^n \langle k_\ell | Y_\ell | k'_\ell \rangle \right) \mathcal{E}_H\left( A_{k_1}X_1 A_{k'_1}^\dagger \otimes \mathcal{E}_H\left( A_{k_2}X_2 A_{k'_2}^\dagger \otimes \cdots \otimes \mathcal{E}_H\left( A_{k_n}X_n A_{k'_n}^\dagger \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}} \right) \cdots \right) \right).
\end{aligned}$$ Applying the initial state $\phi_0$ yields the desired result: $$\varphi_{O, H}(X \otimes Y) = \sum_{\substack{k_1,\dots,k_n \\ k'_1,\dots,k'_n}} \left( \prod_{\ell=1}^n \langle k_\ell | Y_\ell | k'_\ell \rangle \right) \varphi_{\substack{k_1,\dots,k_n \\ k'_1,\dots,k'_n}}(X),$$ where the coefficient functionals are precisely the nested compositions in [\[eq:coefE_func\]](#eq:coefE_func){reference-type="eqref" reference="eq:coefE_func"}. This completes the proof, demonstrating how the forward transition maps naturally generate the hierarchical structure of the HQMM. ◻
:::

::: corollary
[]{#cor:extended_hidden_markov label="cor:extended_hidden_markov"} In the notation of Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"}, the HQMM structure induces two naturally defined processes with distinct mathematical characteristics:

1.  The marginal process $\varphi_H$ on the hidden algebra $\mathcal{B}(\mathcal{H}_{\frac{1}{2}})^{\otimes \mathbb{N}}$, defined by $$\varphi_H(X) = \varphi_{O,H}(X \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}_{1}}^{\otimes n}),$$ constitutes a *quantum Markov chain*. This process admits the explicit recursive representation: $$\label{eq:phiH}
    \varphi_H(X) =  \sum_{ k_1,\dots,k_n} \phi_0 \left( V^{\dagger} \left( A_{k_1}X_1 A_{k'_1}^\dagger \otimes  \cdots \otimes V^{\dagger}\left( A_{k_n}X_n A_{k'_n}^\dagger \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}} \right)V \cdots \right)V \right)$$ where $\Phi_{\mathrm{AKLT}}: \mathcal{B}(\mathcal{H}_{\frac{1}{2}})\to \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$ denotes the quantum channel associated with the AKLT model, as specified in ([\[eq:aklE_channel\]](#eq:aklE_channel){reference-type="ref" reference="eq:aklE_channel"}).

2.  The marginal process $\varphi_O$ on the observable algebra $\mathcal{B}(\mathcal{H}_{1})^{\otimes \mathbb{N}}$, obtained via $$\varphi_O(Y) = \varphi_{O,H}({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}^{\otimes n} \otimes Y),$$ exhibits *non-Markovian* behavior. Its structure is given by: $$\label{eq:phiO}
    \varphi_O(Y) = \sum_{\substack{k_1,\dots,k_n \\ k'_1,\dots,k'_n}} \left( \prod_{\ell=1}^n \langle k_\ell | Y_\ell | k'_\ell \rangle \right) \varphi_{\substack{k_1,\dots,k_n \\ k'_1,\dots,k'_n}}({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}^{\otimes n}),$$ where the coefficient functionals $\varphi_{\substack{k_1,\dots,k_n \\ k'_1,\dots,k'_n}}$ are precisely those defined in equation ([\[eq:coefE_func\]](#eq:coefE_func){reference-type="ref" reference="eq:coefE_func"})
:::

::: proof
*Proof.* **1.** To establish that $\varphi_H$ is a quantum Markov chain with the representation [\[eq:phiH\]](#eq:phiH){reference-type="eqref" reference="eq:phiH"}, we begin with the definition: $$\varphi_H(X) = \varphi_{O,H}(X \otimes {\bf 1}\!\!{\rm I}_{\mathcal{H}_{1}}^{\otimes n}).$$ Substituting into Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} with $Y_\ell = {\bf 1}\!\!{\rm I}_{\mathcal{H}_{1}}$ for all $\ell$, we observe that the matrix elements simplify as: $$\langle k_\ell | {\bf 1}\!\!{\rm I}_{\mathcal{H}_{1}} | k'_\ell \rangle = \delta_{k_\ell, k'_\ell}.$$ This diagonalization collapses the double summation in [\[eq_phiOH\]](#eq_phiOH){reference-type="eqref" reference="eq_phiOH"} to a single sum over indices $k_1, \dots, k_n$: $$\varphi_H(X) = \sum_{k_1,\dots,k_n} \varphi_{k_1,\dots,k_n \\ k_1,\dots,k_n}(X).$$ Now examining the coefficient functionals [\[eq:coefE_func\]](#eq:coefE_func){reference-type="eqref" reference="eq:coefE_func"} under this diagonal constraint, we find that at each time step $\ell$, the expression $A_{k_\ell}X_\ell A_{k_\ell}^\dagger$ appears. Crucially, summing over $k_\ell$ yields the AKLT channel: $$\sum_{k_\ell} A_{k_\ell}X_\ell A_{k_\ell}^\dagger = \Phi_{\mathrm{AKLT}}(X_\ell).$$ Substituting this into the nested structure of [\[eq:coefE_func\]](#eq:coefE_func){reference-type="eqref" reference="eq:coefE_func"} recursively yields the claimed representation [\[eq:phiH\]](#eq:phiH){reference-type="eqref" reference="eq:phiH"}. The quantum Markov property is manifest in this recursive composition structure. Indeed, we can write: $$\varphi_H(X_1 \otimes \cdots \otimes X_n) = \phi_0 \circ E_{X_1} \circ E_{X_2} \circ \cdots \circ E_{X_n}({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}})$$ where the transition maps $E_X: \mathcal{B}(\mathcal{H}_{\frac{1}{2}})\to \mathcal{B}(\mathcal{H}_{\frac{1}{2}})$ are defined by: $$E_X(\rho) = \mathcal{E}_H\left( \Phi_{\mathrm{AKLT}}(X) \otimes \rho \right).$$ This composition structure explicitly demonstrates that the process depends only on the current state, satisfying the quantum Markov property.

**1.** For the observation process, we set $X = {\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}^{\otimes n}$ in Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"}, yielding immediately: $$\varphi_O(Y) = \varphi_{O,H}({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}^{\otimes n} \otimes Y) = \sum_{\substack{k_1,\dots,k_n \\ k'_1,\dots,k'_n}} \left( \prod_{\ell=1}^n \langle k_\ell | Y_\ell | k'_\ell \rangle \right) \varphi_{\substack{k_1,\dots,k_n \\ k'_1,\dots,k'_n}}({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}^{\otimes n}),$$ which is exactly [\[eq:phiO\]](#eq:phiO){reference-type="eqref" reference="eq:phiO"}. The non-Markovian character of $\varphi_O$ follows from the fact that the coefficient functionals $\varphi_{\substack{k_1,\dots,k_n \\ k'_1,\dots,k'_n}}({\bf 1}\!\!{\rm I}_{\mathcal{H}_{\frac{1}{2}}}^{\otimes n})$ encode the full history of the hidden process through the nested composition in [\[eq:coefE_func\]](#eq:coefE_func){reference-type="eqref" reference="eq:coefE_func"}. Unlike the Markovian hidden process, the observation statistics at any time depend on the entire past history of hidden state evolution, mediated through the emission transition expectation $\mathcal{E}_{O,H}$. ◻
:::

The hidden process $\varphi_H$ (Eq. [\[eq:phiH\]](#eq:phiH){reference-type="ref" reference="eq:phiH"}) is a QMC on the infinite tensor product algebera $\mathcal{B}(\mathcal{H}_{\frac{1}{2}})^{\otimes \mathbb{N}}$, which is strongly related to the AKLT structure. Namely, its correlations are governed by the AKLT quantum channel. This means that its Markovian evolution directly reflects the physical properties of the AKLT spin chain.

This provides a concrete, physical example of a QMC, connecting an abstract stochastic process to a well-studied many-body system. This link offers a powerful new framework that allows more significant probabilistic interpretations for SPT phases.
