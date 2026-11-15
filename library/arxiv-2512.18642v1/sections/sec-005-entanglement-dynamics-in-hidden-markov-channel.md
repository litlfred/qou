---
doc_id: arxiv-2512.18642v1
doc_title: "A Hidden Quantum Markov model framework for Entanglement and Topological Order in the AKLT Chain"
section_id: sec-005-entanglement-dynamics-in-hidden-markov-channel
section_title: "Entanglement Dynamics in Hidden Markov Channel"
section_number: null
pages: 12-15
source_pdf: 2512.18642v1.pdf
source_sha256: c4c7f8b0a719aa2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.969
doc_brief: "A Hidden Quantum Markov model framework for Entanglement and Topological Order in the AKLT Chain — This paper introduces a hidden quantum Markov models (HQMMs) framework to the Af"
---
[]{#Sect_HiddenEntang label="Sect_HiddenEntang"}

To analyze the entanglement properties of a quantum channel $\Lambda: \mathcal{B}(\mathcal{H}_{\text{in}}) \to \mathcal{B}(\mathcal{H}_{\text{out}})$, we employ the Choi--Jamiołkowski isomorphism: $$J(\Lambda) = (\mathrm{id}_{\text{in}} \otimes \Lambda)\bigl(|\Omega\rangle\langle\Omega|\bigr),$$ where $|\Omega\rangle = \frac{1}{\sqrt{d_{\text{in}}}}\sum_{i=1}^{d_{\text{in}}} |i\rangle_{\text{ref}} \otimes |i\rangle_{\text{in}}$ is a maximally entangled state between a reference system $\mathcal{H}_{\text{ref}} \cong \mathcal{H}_{\text{in}}$ and the input system $\mathcal{H}_{\text{in}}$ [@FC2024]. This construction provides a complete characterization of the channel's ability to preserve or generate entanglement. Our primary system is the spin-½ Hilbert space $\mathcal{H}_{\frac12} \cong \mathbb{C}^2$, with the standard basis $\{|\uparrow\rangle, |\downarrow\rangle\}$ representing spin-up and spin-down states. We define two particular entangled states of two qubits: $$|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle), \qquad
|\Psi^+\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle),$$ which are two of the four Bell states. The two-dimensional subspace spanned by these states is denoted by $\mathcal{S} = \operatorname{span}\{|\Psi^-\rangle, |\Psi^+\rangle\} \subset \mathcal{H}_{\frac12} \otimes \mathcal{H}_{\frac12}$.

The isometry $V: \mathcal{H}_{\frac12} \to \mathcal{H}_{\frac12} \otimes \mathcal{H}_{\frac12}$ encodes a single spin into a specific two-spin entangled subspace: $$V = |\Psi^-\rangle\langle\uparrow| + |\Psi^+\rangle\langle\downarrow|.$$ This map satisfies $V^\dagger V = I_2$, confirming it preserves the inner product, and its image is precisely $\mathcal{S}$.

From this isometry, we naturally obtain two complementary quantum channels. The *encoding channel* $\mathcal{E}_H^*: \mathcal{B}(\mathcal{H}_{\frac12}) \to \mathcal{B}(\mathcal{H}_{\frac12} \otimes \mathcal{H}_{\frac12})$ embeds a single-qubit state into the two-qubit space: $$\mathcal{E}_H^*(\rho) = V\rho V^\dagger.$$ The adjoint channel $\mathcal{E}_H: \mathcal{B}(\mathcal{H}_{\frac12} \otimes \mathcal{H}_{\frac12}) \to \mathcal{B}(\mathcal{H}_{\frac12})$ acts as a decoder, extracting information from the two-qubit system back to a single qubit: $$\mathcal{E}_H(X) = V^\dagger X V.$$

::: theorem
[]{#thm:entropy label="thm:entropy"} Consider the encoding channel $\mathcal{E}_H^*$ defined above. Its Choi--Jamiołkowski state $J(\mathcal{E}_H^*)$ is a pure state exhibiting maximal entanglement between the reference system and the output subsystem. Concretely, $$J(\mathcal{E}_H^*) = |\Psi_{\mathrm{Choi}}\rangle\langle\Psi_{\mathrm{Choi}}|,
\quad
|\Psi_{\mathrm{Choi}}\rangle = \frac{1}{\sqrt{2}}\bigl( |\uparrow\rangle_R \otimes |\Psi^-\rangle_B + |\downarrow\rangle_R \otimes |\Psi^+\rangle_B \bigr),$$ where $R$ labels the reference qubit and $B$ the output two-qubit system. The entanglement entropy across the $R|B$ partition is $$S\bigl(\rho_R\bigr) = S\bigl(\rho_B\bigr) = 1 \; \text{ebit},$$ with $\rho_R = \operatorname{Tr}_B J(\mathcal{E}_H^*)$ and $\rho_B = \operatorname{Tr}_R J(\mathcal{E}_H^*)$. This shows that $\mathcal{E}_H^*$ perfectly preserves one ebit of entanglement with a reference system, achieving the theoretical maximum for an encoding from one qubit to two qubits restricted to the Bell subspace $\mathcal{S}$.
:::

::: proof
*Proof.* We proceed through a systematic construction and analysis of the Choi state. Since $\mathcal{E}_H^*$ takes a single qubit as input, we have $d_{\text{in}}=2$. We identify the reference system basis with the input basis: $|\uparrow\rangle_R$ corresponds to $|\uparrow\rangle_{\text{in}}$ and $|\downarrow\rangle_R$ to $|\downarrow\rangle_{\text{in}}$. The maximally entangled state between reference and input is therefore $$|\Omega\rangle = \frac{1}{\sqrt{2}}\bigl(|\uparrow\rangle_R|\uparrow\rangle_{\text{in}} + |\downarrow\rangle_R|\downarrow\rangle_{\text{in}}\bigr).$$ Applying the identity on the reference and the channel on the input gives: $$J(\mathcal{E}_H^*) = \frac{1}{2}\sum_{i,j \in \{\uparrow,\downarrow\}} |i\rangle\langle j|_R \otimes V|i\rangle\langle j|_{\text{in}} V^\dagger.$$ Using the defining action of $V$, namely $V|\uparrow\rangle = |\Psi^-\rangle$ and $V|\downarrow\rangle = |\Psi^+\rangle$, we obtain: $$J(\mathcal{E}_H^*) = \frac{1}{2}\Bigl( |\uparrow\rangle\langle\uparrow|_R \otimes |\Psi^-\rangle\langle\Psi^-|_B + |\uparrow\rangle\langle\downarrow|_R \otimes |\Psi^-\rangle\langle\Psi^+|_B + |\downarrow\rangle\langle\uparrow|_R \otimes |\Psi^+\rangle\langle\Psi^-|_B + |\downarrow\rangle\langle\downarrow|_R \otimes |\Psi^+\rangle\langle\Psi^+|_B \Bigr).$$ This operator is precisely the projector onto the pure state $|\Psi_{\mathrm{Choi}}\rangle$ as stated in the theorem.

Since $|\Psi_{\mathrm{Choi}}\rangle$ is pure, we can compute the reduced states by partial tracing. For the reference system: $$\begin{aligned}
\rho_R &= \operatorname{Tr}_B |\Psi_{\mathrm{Choi}}\rangle\langle\Psi_{\mathrm{Choi}}|\\
&= \frac{1}{2}\bigl(\langle\Psi^-|\Psi^-\rangle |\uparrow\rangle\langle\uparrow| + \langle\Psi^-|\Psi^+\rangle|\uparrow\rangle\langle\downarrow| + \langle\Psi^+|\Psi^-\rangle|\downarrow\rangle\langle\uparrow| + \langle\Psi^+|\Psi^+\rangle|\downarrow\rangle\langle\downarrow| \bigr)
\end{aligned}$$

The Bell states are orthonormal: $\langle\Psi^\pm|\Psi^\pm\rangle=1$ and $\langle\Psi^-|\Psi^+\rangle=0$. Thus, $$\rho_R = \frac{1}{2}\bigl(|\uparrow\rangle\langle\uparrow| + |\downarrow\rangle\langle\downarrow|\bigr) = \frac{I_2}{2}.$$ The von Neumann entropy of this completely mixed qubit state is $S(\rho_R) = -\operatorname{Tr}(\rho_R \log_2 \rho_R) = 1$ ebit.

For the output system $B$: $$\rho_B = \operatorname{Tr}_R |\Psi_{\mathrm{Choi}}\rangle\langle\Psi_{\mathrm{Choi}}|
= \frac{1}{2}\bigl( |\Psi^-\rangle\langle\Psi^-| + |\Psi^+\rangle\langle\Psi^+| \bigr).$$ To express this in the computational basis, we write: $$|\Psi^-\rangle = \frac{|\uparrow\downarrow\rangle-|\downarrow\uparrow\rangle}{\sqrt{2}}, \qquad
|\Psi^+\rangle = \frac{|\uparrow\downarrow\rangle+|\downarrow\uparrow\rangle}{\sqrt{2}}.$$ Then, $$|\Psi^-\rangle\langle\Psi^-| = \frac{1}{2}\bigl(|\uparrow\downarrow\rangle\langle\uparrow\downarrow| - |\uparrow\downarrow\rangle\langle\downarrow\uparrow| - |\downarrow\uparrow\rangle\langle\uparrow\downarrow| + |\downarrow\uparrow\rangle\langle\downarrow\uparrow|\bigr),$$ $$|\Psi^+\rangle\langle\Psi^+| = \frac{1}{2}\bigl(|\uparrow\downarrow\rangle\langle\uparrow\downarrow| + |\uparrow\downarrow\rangle\langle\downarrow\uparrow| + |\downarrow\uparrow\rangle\langle\uparrow\downarrow| + |\downarrow\uparrow\rangle\langle\downarrow\uparrow|\bigr).$$ Adding these and dividing by 2 yields: $$\rho_B = \frac{1}{2}\bigl( |\uparrow\downarrow\rangle\langle\uparrow\downarrow| + |\downarrow\uparrow\rangle\langle\downarrow\uparrow| \bigr).$$ This density matrix has eigenvalues $\{\tfrac12, \tfrac12, 0, 0\}$, giving $S(\rho_B) = 1$ ebit as well.

For a pure bipartite state, the entanglement entropy is given by the von Neumann entropy of either reduced density matrix. Here, $S(\rho_R) = S(\rho_B) = 1$. Since the reference system is a single qubit, the maximum possible entanglement entropy is $\log_2 2 = 1$ ebit. Our calculated value saturates this bound, confirming that $|\Psi_{\mathrm{Choi}}\rangle$ is maximally entangled across the $R|B$ partition given the dimension constraints. ◻
:::

::: remark
The encoding channel $\mathcal{E}_H^*$ maps a single qubit isometrically into the two-dimensional Bell subspace $\mathcal{S}$ of two qubits. The fact that its Choi state carries exactly one ebit of entanglement means that the channel can perfectly transmit one qubit of quantum information---its coherent information is maximal. Moreover, it preserves the maximum possible entanglement with a reference system, which is the hallmark of an optimal quantum encoding. The corresponding decoding channel $\mathcal{E}_H$ reverses this process on the subspace $\mathcal{S}$, and both channels share the same entanglement capacity as quantified by their Choi states. This structure reflects the essential role of such encodings in valence-bond solid models and quantum error correction schemes.
:::
