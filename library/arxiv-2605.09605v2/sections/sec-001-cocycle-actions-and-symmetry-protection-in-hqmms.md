---
doc_id: arxiv-2605.09605v2
doc_title: "Cocycle Actions on Hidden Quantum Markov Models:"
section_id: sec-001-cocycle-actions-and-symmetry-protection-in-hqmms
section_title: "Cocycle Actions and Symmetry Protection in HQMMs"
section_number: null
pages: 3-11
source_pdf: 2605.09605v2.pdf
source_sha256: 24496fb444a2b558
doc_brief: "Cocycle Actions on Hidden Quantum Markov Models: — We develop a symmetry action framework for hidden quantum Markov models (HQMMs) tailored to one-dimensional quantum spin systems and"
text_source: latex
latex_prose_ratio: 0.659
latex_coverage_ratio: 0.994
---
[]{#Sect_main label="Sect_main"} Let $G$ be a locally compact group. In quantum systems, symmetry actions are typically implemented by unitary representations. However, within the framework ofHQMMs, the hidden sector may carry a *projective* representation, reflecting the anomalous nature of the symmetry in the corresponding symmetry-protected topological (SPT) phase. This projective character is encoded in a $2$-cocycle, which defines an element of the second cohomology group $H^2(G, \mathrm{U}(1))$. Throughout the remainder of the paper, the notation associated with the HQMM formalism is introduced in Appendix [\[sect_prel\]](#sect_prel){reference-type="ref" reference="sect_prel"}.

A *projective unitary representation* of $G$ on a Hilbert space $\mathcal{H}$ is a map $\pi: G \to \mathcal{U}(\mathcal{H})$ such that for all $g,h \in G$, $$\pi(g)\pi(h) = \omega(g,h) \, \pi(gh),
\label{eq:proj_repr}$$ where $\omega: G \times G \to \mathrm{U}(1)$ is a measurable function satisfying the $2$-cocycle condition: $$\omega(g,h)\omega(gh,k) = \omega(g,hk)\omega(h,k), \qquad \forall g,h,k \in G.
\label{eq:cocycle_condition}$$ The cocycle $\omega$ is called the *multiplier* of the projective representation. Two projective representations $\pi$ and $\pi'$ are equivalent if there exists a function $\lambda: G \to \mathrm{U}(1)$ such that $\pi'(g) = \lambda(g)\pi(g)$, which induces a cohomologous cocycle $\omega'(g,h) = \lambda(g)\lambda(h)\overline{\lambda(gh)}\omega(g,h)$. The equivalence class $[\omega] \in H^2(G, \mathrm{U}(1))$ is a topological invariant characterizing the projective representation.

Let $\mathcal{H}$ and $\mathcal{K}$ be the separable Hilbert spaces introduced in Section 1, representing the hidden and observable degrees of freedom, respectively. Let $\pi: G \to \mathcal{U}(\mathcal{H})$ be a projective representation of $G$ on the hidden space with associated $2$-cocycle $\omega_\pi \in H^2(G, \mathrm{U}(1))$, and let $\rho: G \to \mathcal{U}(\mathcal{K})$ be an ordinary (linear) unitary representation on the observable space, corresponding to the trivial cocycle $\omega_\rho(g,h) = 1$.

The algebraic action of $G$ on the single-site algebras $\mathcal{A}_H = \mathcal{B}(\mathcal{H})$ and $\mathcal{A}_O = \mathcal{B}(\mathcal{K})$ is defined via the adjoint action: $$\alpha_g^{(H)}(X) := \pi(g) X \pi(g)^\dagger, \qquad \beta_g(Y) := \rho(g) Y \rho(g)^\dagger,
\label{eq:adjoint_actions}$$ for all $X \in \mathcal{A}_H$, $Y \in \mathcal{A}_O$, and $g \in G$. These actions extend naturally to the quasi-local algebras $\mathcal{A}_{H,\mathbb{N}_0}$ and $\mathcal{A}_{O,\mathbb{N}_0}$ via the tensor product structure, i.e., for elementary tensors, $$\alpha_g^{(H)}\Big(\bigotimes_{k=0}^n X_k\Big) = \bigotimes_{k=0}^n \pi(g) X_k \pi(g)^\dagger, \qquad
\beta_g\Big(\bigotimes_{k=0}^n Y_k\Big) = \bigotimes_{k=0}^n \rho(g) Y_k \rho(g)^\dagger.
\label{eq:tensor_actions}$$ The projective nature of $\pi$ manifests in the composition law: $$\alpha_g^{(H)} \circ \alpha_h^{(H)} = \operatorname{Ad}\bigl(\omega_\pi(g,h) \mathbb{I}_{\mathcal{H}}\bigr) \circ \alpha_{gh}^{(H)},
\label{eq:proj_composition}$$ which reflects the fact that $\alpha^{(H)}$ is an action up to inner automorphisms implemented by the scalar cocycle $\omega_\pi$. For the linear representation $\rho$, the corresponding action $\beta$ satisfies $\beta_g \circ \beta_h = \beta_{gh}$ without any phase.

We now formulate the precise symmetry requirements that define a covariant HQMM. These conditions encapsulate how the projective symmetry acts on the generative structure.

$$\phi_0\bigl( \pi(g) Z \pi(g)^\dagger \bigr) = \phi_0(Z) \qquad \forall g \in G,\; \forall Z \in \mathcal{A}_H.
\label{eq:initial_invariance}$$

$$\mathcal{E}_H\bigl( \pi(g) Z_1 \pi(g)^\dagger \otimes \pi(g) Z_2 \pi(g)^\dagger \bigr) = \pi(g) \, \mathcal{E}_H(Z_1 \otimes Z_2) \, \pi(g)^\dagger \qquad \forall g \in G,\; \forall Z_1, Z_2 \in \mathcal{A}_H.
\label{eq:Eh_equivariance}$$

$$\mathcal{E}_{H,O}\bigl( \pi(g) X \pi(g)^\dagger \otimes \rho(g) Y \rho(g)^\dagger \bigr) = \pi(g) \, \mathcal{E}_{H,O}(X \otimes Y) \, \pi(g)^\dagger \qquad \forall g \in G,\; \forall X \in \mathcal{A}_H,\; \forall Y \in \mathcal{A}_O.
\label{eq:EOH_covariance}$$

The covariance condition [\[eq:EOH_covariance\]](#eq:EOH_covariance){reference-type="eqref" reference="eq:EOH_covariance"} is the central structural relation. It states that $\mathcal{E}_{O,H}$ intertwines the projective $G$-action on $\mathcal{A}_H$ with the linear $G$-action on $\mathcal{A}_O$, i.e., $\mathcal{E}_{O,H} \circ (\alpha_g^{(H)} \otimes \beta_g) = \alpha_g^{(H)} \circ \mathcal{E}_{O,H}$. This intertwining absorbs the projective anomaly of the hidden sector, forcing the observable sector to transform under an ordinary representation.

A central extension perspective illuminates the cohomological significance of these conditions. Consider the short exact sequence $$1 \longrightarrow \mathrm{U}(1) \longrightarrow \widetilde{G} \longrightarrow G \longrightarrow 1,$$ where $\widetilde{G}$ is the central extension of $G$ by $\mathrm{U}(1)$ determined by the cocycle $\omega$. Then $\pi$ lifts to a linear representation $\widetilde{\pi}$ of $\widetilde{G}$ on $\mathcal{H}$ satisfying $\widetilde{\pi}((g,\lambda)) = \lambda \pi(g)$ for $\lambda \in \mathrm{U}(1)$. The emission map covariance condition [\[eq:EOH_covariance\]](#eq:EOH_covariance){reference-type="eqref" reference="eq:EOH_covariance"} then becomes $$\mathcal{E}_{H,O}\bigl( \widetilde{\pi}((g,\lambda)) X \widetilde{\pi}((g,\lambda))^\dagger \otimes \rho(g) Y \rho(g)^\dagger \bigr) = \widetilde{\pi}((g,\lambda)) \, \mathcal{E}_{H,O}(X \otimes Y) \, \widetilde{\pi}((g,\lambda))^\dagger,$$ where the $\mathrm{U}(1)$ phase $\lambda$ cancels on both sides. Hence the emission map provides a *cocycle intertwiner* between the centrally extended hidden dynamics and the linear observable dynamics. The existence of such an intertwiner implies that the obstruction $[\omega] \in H^2(G, \mathrm{U}(1))$ is trivialized when passing through the map $\mathcal{E}_{H,O}$, meaning that the composition $\mathcal{E}_{H,O} \circ (\cdot \otimes \operatorname{id}_{\mathcal{A}_O})$ converts the projective action on the first tensor factor into a linear action on the image.

The interplay between projective and linear representations manifests richly in the tensor product structure of the HQMM. Consider the tensor product representation $\pi \otimes \rho: G \to \mathcal{U}(\mathcal{H} \otimes \mathcal{K})$ defined by $(\pi \otimes \rho)(g) := \pi(g) \otimes \rho(g)$. Its composition law follows from [\[eq:proj_repr\]](#eq:proj_repr){reference-type="eqref" reference="eq:proj_repr"}: $$(\pi \otimes \rho)(g)(\pi \otimes \rho)(h) = \pi(g)\pi(h) \otimes \rho(g)\rho(h) = \omega(g,h) \, \pi(gh) \otimes \rho(gh) = \omega(g,h) \, (\pi \otimes \rho)(gh).$$ Thus $\pi \otimes \rho$ is a projective representation of $G$ with the same cocycle $\omega$ as $\pi$. Consequently, the composite action $\alpha_g^{(H)} \otimes \beta_g$ on $\mathcal{A}_H \otimes \mathcal{A}_O$ satisfies $$(\alpha_g^{(H)} \otimes \beta_g) \circ (\alpha_h^{(H)} \otimes \beta_h) = \operatorname{Ad}\bigl(\omega(g,h) \mathbb{I}_{\mathcal{H} \otimes \mathcal{K}}\bigr) \circ (\alpha_{gh}^{(H)} \otimes \beta_{gh}),$$ so the projective nature persists at the level of the composite system. The covariance condition [\[eq:EOH_covariance\]](#eq:EOH_covariance){reference-type="eqref" reference="eq:EOH_covariance"} exactly cancels the projective phase coming from the hidden sector. As a result, although $\alpha^{(H)}$ itself is projective, its composition with $\mathcal{E}_{O,H}$ becomes linear. This cancellation is the algebraic hallmark of a consistent, anomaly-free coupling between the hidden and observable sectors at their interface.

More generally, take two projective representations $\pi_1$ and $\pi_2$ of $G$, with cocycles $\omega_1$ and $\omega_2$ respectively. Their tensor product $\pi_1 \otimes \pi_2$ is again projective, with cocycle $\omega_1 \omega_2$ given by pointwise multiplication. Their tensor product $\pi_1 \otimes \pi_2$ satisfies $$(\pi_1 \otimes \pi_2)(g)(\pi_1 \otimes \pi_2)(h) = \omega_1(g,h)\omega_2(g,h) \, (\pi_1 \otimes \pi_2)(gh),$$ so the cocycle of the tensor product is the pointwise product $\omega_1\omega_2$. In the HQMM setting, the hidden transition map $\mathcal{E}_H$ sends the tensor product of two projective representations $\pi \otimes \pi$ (cocycle $\omega^2$) to a single copy $\pi$ (cocycle $\omega$). Equivariance [\[eq:Eh_equivariance\]](#eq:Eh_equivariance){reference-type="eqref" reference="eq:Eh_equivariance"} then forces $[\omega^2] = [\omega]$ in $H^2(G, \mathrm{U}(1))$. This holds automatically only when $\omega$ is a coboundary or $G$ has special properties; otherwise, the equivariance must be twisted. In the generic case where $[\omega]$ has order greater than $1$, this condition forces a refinement of the equivariance structure, typically implemented by a $2$-cocycle on the map itself, leading to the notion of *twisted equivariance* that we shall explore in subsequent sections.

We now turn to the analysis of the two causal structures introduced in Section 1. Recall that the conventional and causal structures are defined by [\[Tconv\]](#Tconv){reference-type="eqref" reference="Tconv"} and [\[Tcaus\]](#Tcaus){reference-type="eqref" reference="Tcaus"}, respectively in terms of the generative mappings $(\mathcal{E}_H, \mathcal{E}_{H,O})$ as:

For each structure, we define the corresponding sliced maps that propagate the hidden state forward. For the conventional structure, define $\mathcal{T}_{X,Y}^{(\text{conv})}: \mathcal{A}_H \to \mathcal{A}_H$ by $$\mathcal{T}_{X,Y}^{(\text{conv})}(Z) := \mathcal{T}^{(\text{conv})}(X \otimes Z \otimes Y) = \mathcal{E}_H\big( \mathcal{E}_{H,O}(X \otimes Y) \otimes Z \big).
\label{eq:conv_sliced}$$ For the causal structure, define $\mathcal{T}_{X,Y}^{(\text{caus})}: \mathcal{A}_H \to \mathcal{A}_H$ by $$\mathcal{T}_{X,Y}^{(\text{caus})}(Z) := \mathcal{T}^{(\text{caus})}(X \otimes Z \otimes Y) = \mathcal{E}_{H,O}\big( \mathcal{E}_H(X \otimes Z) \otimes Y \big).
\label{eq:caus_sliced}$$

These sliced maps encapsulate the sequential dynamics: given a current hidden state $Z$ and an incoming pair $(X,Y)$ representing the left neighbor hidden operator and the local observable, they produce the updated hidden state after the site.

::: lemma
[]{#lem:conv_cov label="lem:conv_cov"} Under the symmetry conditions [\[eq:Eh_equivariance\]](#eq:Eh_equivariance){reference-type="eqref" reference="eq:Eh_equivariance"} and [\[eq:EOH_covariance\]](#eq:EOH_covariance){reference-type="eqref" reference="eq:EOH_covariance"}, for all $g \in G$, $X, Z \in \mathcal{A}_H$, and $Y \in \mathcal{A}_O$, $$\mathcal{T}_{\pi(g) X \pi(g)^\dagger, \, \rho(g) Y \rho(g)^\dagger}^{(\text{conv})}\big( \pi(g) Z \pi(g)^\dagger \big) = \pi(g) \, \mathcal{T}_{X,Y}^{(\text{conv})}(Z) \, \pi(g)^\dagger.
\label{eq:conv_covariance}$$
:::

::: proof
*Proof.* The proof follows directly from the covariance property [\[eq:EOH_covariance\]](#eq:EOH_covariance){reference-type="eqref" reference="eq:EOH_covariance"} of $\mathcal{E}_{H,O}$ and the equivariance property [\[eq:Eh_equivariance\]](#eq:Eh_equivariance){reference-type="eqref" reference="eq:Eh_equivariance"} of $\mathcal{E}_H$: $$\begin{aligned}
&\mathcal{T}_{\pi(g) X \pi(g)^\dagger, \, \rho(g) Y \rho(g)^\dagger}^{(\text{conv})}\big( \pi(g) Z \pi(g)^\dagger \big) \\
&\quad = \mathcal{E}_H\Big( \mathcal{E}_{H,O}\big( \pi(g) X \pi(g)^\dagger \otimes \rho(g) Y \rho(g)^\dagger \big) \otimes \pi(g) Z \pi(g)^\dagger \Big) \\
&\quad \stackrel{ {\eqref{eq:EOH_covariance}}}{=} \mathcal{E}_H\Big( \pi(g) \mathcal{E}_{H,O}(X \otimes Y) \pi(g)^\dagger \otimes \pi(g) Z \pi(g)^\dagger \Big) \\
&\quad \stackrel{ {\eqref{eq:Eh_equivariance}}}{=} \pi(g) \, \mathcal{E}_H\big( \mathcal{E}_{H,O}(X \otimes Y) \otimes Z \big) \, \pi(g)^\dagger \\
&\quad = \pi(g) \, \mathcal{T}_{X,Y}^{(\text{conv})}(Z) \, \pi(g)^\dagger.
\end{aligned}$$ ◻
:::

::: lemma
[]{#lem:caus_cov label="lem:caus_cov"} Under the symmetry conditions [\[eq:Eh_equivariance\]](#eq:Eh_equivariance){reference-type="eqref" reference="eq:Eh_equivariance"} and [\[eq:EOH_covariance\]](#eq:EOH_covariance){reference-type="eqref" reference="eq:EOH_covariance"}, for all $g \in G$, $X, Z \in \mathcal{A}_H$, and $Y \in \mathcal{A}_O$, $$\mathcal{T}_{\pi(g) X \pi(g)^\dagger, \, \rho(g) Y \rho(g)^\dagger}^{(\text{caus})}\big( \pi(g) Z \pi(g)^\dagger \big) = \pi(g) \, \mathcal{T}_{X,Y}^{(\text{caus})}(Z) \, \pi(g)^\dagger.
\label{eq:caus_covariance}$$
:::

::: proof
*Proof.* The proof proceeds analogously, employing the equivariance property [\[eq:Eh_equivariance\]](#eq:Eh_equivariance){reference-type="eqref" reference="eq:Eh_equivariance"} of $\mathcal{E}_H$ first, followed by the covariance property [\[eq:EOH_covariance\]](#eq:EOH_covariance){reference-type="eqref" reference="eq:EOH_covariance"} of $\mathcal{E}_{H,O}$: $$\begin{aligned}
&\mathcal{T}_{\pi(g) X \pi(g)^\dagger, \, \rho(g) Y \rho(g)^\dagger}^{(\text{caus})}\big( \pi(g) Z \pi(g)^\dagger \big) \\
&\quad = \mathcal{E}_{H,O}\Big( \mathcal{E}_H\big( \pi(g) X \pi(g)^\dagger \otimes \pi(g) Z \pi(g)^\dagger \big) \otimes \rho(g) Y \rho(g)^\dagger \Big) \\
&\quad \stackrel{{\eqref{eq:Eh_equivariance}}}{=} \mathcal{E}_{H,O}\Big( \pi(g) \mathcal{E}_H(X \otimes Z) \pi(g)^\dagger \otimes \rho(g) Y \rho(g)^\dagger \Big) \\
&\quad \stackrel{{\eqref{eq:EOH_covariance}}}{=} \pi(g) \, \mathcal{E}_{H,O}\big( \mathcal{E}_H(X \otimes Z) \otimes Y \big) \, \pi(g)^\dagger \\
&\quad = \pi(g) \, \mathcal{T}_{X,Y}^{(\text{caus})}(Z) \, \pi(g)^\dagger.
\end{aligned}$$ ◻
:::

::: theorem
[]{#thm:global_invariance label="thm:global_invariance"} Let $\Xi = (\phi_0, \mathcal{E}_H, \mathcal{E}_{H,O})$ be an HQMM satisfying the symmetry conditions [\[eq:initial_invariance\]](#eq:initial_invariance){reference-type="eqref" reference="eq:initial_invariance"}, [\[eq:Eh_equivariance\]](#eq:Eh_equivariance){reference-type="eqref" reference="eq:Eh_equivariance"}, and [\[eq:EOH_covariance\]](#eq:EOH_covariance){reference-type="eqref" reference="eq:EOH_covariance"}. Let $\varphi^{(\text{conv})}$ and $\varphi^{(\text{caus})}$ be the global states on $\mathcal{A}_{\mathbb{N}_0}$ generated by the conventional and causal transition maps, respectively, via the construction of Theorem 1. Then for all $g \in G$, $A \in \mathcal{A}_{H,\mathbb{N}_0}$, and $B \in \mathcal{A}_{O,\mathbb{N}_0}$, $$\varphi^{(\text{conv})}\big( \alpha_g^{(H)}(A) \otimes \beta_g(B) \big) = \varphi^{(\text{conv})}(A \otimes B),
\label{eq:global_conv_invariance}$$ $$\varphi^{(\text{caus})}\big( \alpha_g^{(H)}(A) \otimes \beta_g(B) \big) = \varphi^{(\text{caus})}(A \otimes B).
\label{eq:global_caus_invariance}$$ In particular, both global states are invariant under the combined projective-linear action of $G$. Consequently, the hidden marginals $\varphi_H^{(\text{conv})}$ and $\varphi_H^{(\text{caus})}$ are invariant under the projective action $\alpha^{(H)}$, and the observable marginals $\varphi_O^{(\text{conv})}$ and $\varphi_O^{(\text{caus})}$ are invariant under the linear action $\beta$.
:::

::: proof
*Proof.* We present the proof for the conventional structure; the proof for the causal structure is entirely analogous, with Lemma [\[lem:caus_cov\]](#lem:caus_cov){reference-type="ref" reference="lem:caus_cov"} replacing Lemma [\[lem:conv_cov\]](#lem:conv_cov){reference-type="ref" reference="lem:conv_cov"}.

Let $A = \bigotimes_{k=0}^n X_k \in \mathcal{A}_{H,\mathbb{N}_0}$ and $B = \bigotimes_{k=0}^n Y_k \in \mathcal{A}_{O,\mathbb{N}_0}$ be elementary tensors supported on sites $0, \dots, n$. The extension to arbitrary local observables follows by linearity and continuity, and the inductive limit construction ensures the result holds for all quasi-local observables.

Recall from Theorem 1 that the finite-volume state on $\mathcal{A}_{[0,n]}$ is given by $$\varphi_n^{(\text{conv})}\!\left( \bigotimes_{k=0}^n (X_k \otimes Y_k) \right) = \phi_0 \circ \mathcal{T}_{X_0,Y_0}^{(\text{conv})} \circ \mathcal{T}_{X_1,Y_1}^{(\text{conv})} \circ \cdots \circ \mathcal{T}_{X_n,Y_n}^{(\text{conv})}(\mathbb{I}_{\mathcal{A}_H}),
\label{eq:finite_volume_conv}$$ where the composition denotes successive application of the sliced maps. In what follows, for $(\text{c})\in \{(\text{conv}), (\text{caus}) \}$ we denote the composition of the transition maps $\mathcal{T}^{(\text{c})} _{X_j,Y_j}$ by

$$\bigcirc_{k=m}^n \mathcal{T}_{X_k, Y_k} := \mathcal{T}_{X_m,Y_m}^{(\text{c})} \circ \mathcal{T}_{X_1,Y_1}^{(\text{c})} \circ \cdots \circ \mathcal{T}_{X_n,Y_n}^{(\text{c})}$$

We prove by induction on $n$ that for all $g \in G$, $$\bigcirc_{k=0}^n \mathcal{T}_{\pi(g) X_k \pi(g)^\dagger, \, \rho(g) Y_k \rho(g)^\dagger}^{(\text{conv})}(\mathbb{I}_{\mathcal{A}_H})
= \pi(g) \left( \bigcirc_{k=0}^n \mathcal{T}_{X_k,Y_k}^{(\text{conv})}(\mathbb{I}_{\mathcal{A}_H}) \right) \pi(g)^\dagger.
\label{eq:induction_claim}$$

For a single site, Lemma [\[lem:conv_cov\]](#lem:conv_cov){reference-type="ref" reference="lem:conv_cov"} with $Z = \mathbb{I}_{\mathcal{A}_H}$ together with the observation that $\pi(g) \mathbb{I}_{\mathcal{A}_H} \pi(g)^\dagger = \mathbb{I}_{\mathcal{A}_H}$ yields $$\mathcal{T}_{\pi(g) X_0 \pi(g)^\dagger, \, \rho(g) Y_0 \rho(g)^\dagger}^{(\text{conv})}(\mathbb{I}_{\mathcal{A}_H})
= \pi(g) \, \mathcal{T}_{X_0,Y_0}^{(\text{conv})}(\mathbb{I}_{\mathcal{A}_H}) \, \pi(g)^\dagger.$$

Assume the claim holds for chains of length $n$. For length $n+1$, define the composition for the last $n+1$ sites: $$\mathcal{C}_n := \bigcirc_{k=1}^{n+1} \mathcal{T}_{X_k,Y_k}^{(\text{conv})}, \qquad
\mathcal{D}_n := \bigcirc_{k=1}^{n+1} \mathcal{T}_{\pi(g) X_k \pi(g)^\dagger, \, \rho(g) Y_k \rho(g)^\dagger}^{(\text{conv})}.$$ By the induction hypothesis applied to the sites $1, \dots, n+1$, $$\mathcal{D}_n(\mathbb{I}_{\mathcal{A}_H}) = \pi(g) \, \mathcal{C}_n(\mathbb{I}_{\mathcal{A}_H}) \, \pi(g)^\dagger.
\label{eq:induction_hyp}$$

Now compute the full composition for $n+1$ sites: $$\begin{aligned}
&\bigcirc_{k=0}^{n+1} \mathcal{T}_{\pi(g) X_k \pi(g)^\dagger, \, \rho(g) Y_k \rho(g)^\dagger}^{(\text{conv})}(\mathbb{I}_{\mathcal{A}_H}) \\
&= \mathcal{T}_{\pi(g) X_0 \pi(g)^\dagger, \, \rho(g) Y_0 \rho(g)^\dagger}^{(\text{conv})}\Big( \mathcal{D}_n(\mathbb{I}_{\mathcal{A}_H}) \Big) \\
&= \mathcal{T}_{\pi(g) X_0 \pi(g)^\dagger, \, \rho(g) Y_0 \rho(g)^\dagger}^{(\text{conv})}\Big( \pi(g) \, \mathcal{C}_n(\mathbb{I}_{\mathcal{A}_H}) \, \pi(g)^\dagger \Big) \quad \text{by \eqref{eq:induction_hyp}} \\
&= \pi(g) \, \mathcal{T}_{X_0,Y_0}^{(\text{conv})}\big( \mathcal{C}_n(\mathbb{I}_{\mathcal{A}_H}) \big) \, \pi(g)^\dagger \quad \text{by Lemma \ref{lem:conv_cov}} \\
&= \pi(g) \left( \bigcirc_{k=0}^{n+1} \mathcal{T}_{X_k,Y_k}^{(\text{conv})}(\mathbb{I}_{\mathcal{A}_H}) \right) \pi(g)^\dagger.
\end{aligned}$$ This completes the induction.

Now apply the initial state $\phi_0$. By the invariance condition [\[eq:initial_invariance\]](#eq:initial_invariance){reference-type="eqref" reference="eq:initial_invariance"}, $$\begin{aligned}
\varphi_n^{(\text{conv})}\big( \alpha_g^{(H)}(A) \otimes \beta_g(B) \big)
&= \phi_0 \left( \bigcirc_{k=0}^n \mathcal{T}_{\pi(g) X_k \pi(g)^\dagger, \, \rho(g) Y_k \rho(g)^\dagger}^{(\text{conv})}(\mathbb{I}_{\mathcal{A}_H}) \right) \\
&= \phi_0 \left( \pi(g) \left( \bigcirc_{k=0}^n \mathcal{T}_{X_k,Y_k}^{(\text{conv})}(\mathbb{I}_{\mathcal{A}_H}) \right) \pi(g)^\dagger \right) \\
&= \phi_0 \left( \bigcirc_{k=0}^n \mathcal{T}_{X_k,Y_k}^{(\text{conv})}(\mathbb{I}_{\mathcal{A}_H}) \right) \\
&= \varphi_n^{(\text{conv})}(A \otimes B).
\end{aligned}$$

Since this holds for all finite $n$ and the embeddings $\iota_{m,n}$ are compatible with the group actions (i.e., $\iota_{m,n} \circ (\alpha_g^{(H)} \otimes \beta_g) = (\alpha_g^{(H)} \otimes \beta_g) \circ \iota_{m,n}$), the projective limit state $\varphi^{(\text{conv})}$ on $\mathcal{A}_{\mathbb{N}_0}$ satisfies [\[eq:global_conv_invariance\]](#eq:global_conv_invariance){reference-type="eqref" reference="eq:global_conv_invariance"}.

*Proof for the causal structure.* The proof follows exactly the same inductive structure, with $\mathcal{T}^{(\text{caus})}$ replacing $\mathcal{T}^{(\text{conv})}$ and Lemma [\[lem:caus_cov\]](#lem:caus_cov){reference-type="ref" reference="lem:caus_cov"} replacing Lemma [\[lem:conv_cov\]](#lem:conv_cov){reference-type="ref" reference="lem:conv_cov"}. The finite-volume state is $$\varphi_n^{(\text{caus})}\!\left( \bigotimes_{k=0}^n (X_k \otimes Y_k) \right) = \phi_0 \circ \mathcal{T}_{X_0,Y_0}^{(\text{caus})} \circ \mathcal{T}_{X_1,Y_1}^{(\text{caus})} \circ \cdots \circ \mathcal{T}_{X_n,Y_n}^{(\text{caus})}(\mathbb{I}_{\mathcal{A}_H}).$$ One proves by induction that $$\bigcirc_{k=0}^n \mathcal{T}_{\pi(g) X_k \pi(g)^\dagger, \, \rho(g) Y_k \rho(g)^\dagger}^{(\text{caus})}(\mathbb{I}_{\mathcal{A}_H})
= \pi(g) \left( \bigcirc_{k=0}^n \mathcal{T}_{X_k,Y_k}^{(\text{caus})}(\mathbb{I}_{\mathcal{A}_H}) \right) \pi(g)^\dagger,$$ using Lemma [\[lem:caus_cov\]](#lem:caus_cov){reference-type="ref" reference="lem:caus_cov"} at each step. Applying $\phi_0$ and its invariance [\[eq:initial_invariance\]](#eq:initial_invariance){reference-type="eqref" reference="eq:initial_invariance"} yields [\[eq:global_caus_invariance\]](#eq:global_caus_invariance){reference-type="eqref" reference="eq:global_caus_invariance"}. ◻
:::

The cohomology class $[\omega] \in H^2(G, \mathrm{U}(1))$ thus emerges as a well-defined invariant of the HQMM state. It classifies the projective nature of the hidden representation and, together with the covariance conditions [\[eq:Eh_equivariance\]](#eq:Eh_equivariance){reference-type="eqref" reference="eq:Eh_equivariance"} and [\[eq:EOH_covariance\]](#eq:EOH_covariance){reference-type="eqref" reference="eq:EOH_covariance"}, provides the algebraic characterization of the SPT order. The emission map $\mathcal{E}_{H,O}$ serves as a *cocycle intertwiner* that mediates between the projective hidden dynamics and the linear observable dynamics, effectively absorbing the anomaly at the interface.

# Application to AKLT's Symmetry-Protected Topological Order {#Sect_AKLT}

The AKLT state [@AKLT1987] stands as a paradigmatic example of a SPT phase in 1D. Its topological protection originates from a projective representation of the symmetry group on the virtual degrees of freedom---a structure that aligns naturally with the HQMM framework developed in the preceding sections. This projective character is encoded in a nontrivial $2$-cocycle $[\omega] \in H^2(\mathrm{SO}(3), \mathrm{U}(1)) \cong \mathbb{Z}_2$, which obstructs the lifting of the symmetry action on the hidden space to a linear representation. Within the HQMM formalism, this obstruction is precisely absorbed by the emission map $\mathcal{E}_{O,H}$, which acts as a *cocycle intertwiner* mediating between the projective hidden dynamics and the linear observable dynamics.

We now demonstrate how the abstract covariance conditions established earlier---specifically [\[eq:Eh_equivariance\]](#eq:Eh_equivariance){reference-type="eqref" reference="eq:Eh_equivariance"} and [\[eq:EOH_covariance\]](#eq:EOH_covariance){reference-type="eqref" reference="eq:EOH_covariance"}---manifest concretely in the AKLT construction. This reveals that SPT order is not merely a static property of the ground state but is dynamically preserved under the quantum Markov evolution generated by the HQMM. In doing so, we extend the analysis of topological order in emission transitions introduced in [@SouAndhqmm2025] to a more structural and algebraic level, grounding the classification of SPT phases within the operator-algebraic framework of quantum stochastic processes.

Let $G = \mathrm{SO}(3)$ denote the symmetry group. The physical Hilbert space is $\mathcal{K} = \mathcal{H}_1$, on which $G$ acts via the linear spin-$1$ representation $\rho: G \to \mathcal{U}(\mathcal{H}_1)$. The hidden (virtual) Hilbert space is $\mathcal{H} = \mathcal{H}_{1/2}$, where $G$ acts via the irreducible projective spin-$1/2$ representation $\pi: G \to \mathcal{U}(\mathcal{H}_{1/2})$. The projective nature of $\pi$ is captured by a $2$-cocycle $\omega: G \times G \to \mathrm{U}(1)$ satisfying the composition law $$\pi(g_1)\pi(g_2) = \omega(g_1,g_2)\,\pi(g_1g_2) \qquad \forall g_1,g_2 \in G,
\label{eq:aklt_proj_repr}$$ together with the cocycle condition [\[eq:cocycle_condition\]](#eq:cocycle_condition){reference-type="eqref" reference="eq:cocycle_condition"}. The cohomology class $[\omega] \in H^2(\mathrm{SO}(3),\mathrm{U}(1))$ is the generator of $\mathbb{Z}_2$, reflecting the double-cover relation $\mathrm{SU}(2) \to \mathrm{SO}(3)$ [@Chen2011b; @Ragone24], and serves as the topological invariant distinguishing the nontrivial SPT phase.

Let $\{|k\rangle\}_{k=+,-,0}$ denote the standard orthonormal basis of $\mathcal{H}_1$ corresponding to the eigenstates of $S^z$ with eigenvalues $+1, -1, 0$, respectively. The AKLT state is represented as a translation-invariant matrix product state with virtual dimension $2$. Its local tensors are linear operators $A_k \in \mathcal{B}(\mathcal{H}_{1/2})$ defined by $$A_+ = \frac{1}{\sqrt{2}} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix},\qquad
A_0 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},\qquad
A_- = \frac{1}{\sqrt{2}} \begin{pmatrix} 0 & 0 \\ -1 & 0 \end{pmatrix},$$ expressed in the standard basis of $\mathcal{H}_{1/2} \cong \mathbb{C}^2$. These operators satisfy the fundamental intertwining relation that encodes the SPT order [@Pollmann2010]: $$\sum_{k'} \rho(g)_{k k'} A_{k'} = \pi(g) A_k \pi(g)^\dagger \qquad \forall g \in G,\; \forall k \in \{+,0,-\},
\label{eq:aklt_covariance}$$ where $\rho(g)_{kk'} = \langle k | \rho(g) | k' \rangle$ denotes the matrix element of the physical representation. This relation asserts that a symmetry transformation applied to the physical index is equivalent to conjugation of the virtual operators by the projective representation $\pi(g)$.

The emission map $\mathcal{E}_{H,O}: \mathcal{A}_H \otimes \mathcal{A}_O \to \mathcal{A}_H$ is defined by its action on elementary tensors as $$\mathcal{E}_{H,O}(X \otimes Y) = \sum_{k,k' \in \{+,0,-\}} \langle k' | Y | k \rangle \, A_k X A_{k'}^\dagger, \qquad X \in \mathcal{A}_H,\; Y \in \mathcal{A}_O.
\label{eq:aklt_emission}$$ This map is completely positive and unital. Indeed, positivity follows from the representation $\mathcal{E}_{H,O}(X \otimes Y) = \sum_{k,k'} \langle k'|Y|k\rangle A_k X A_{k'}^\dagger = \sum_{k} A_k X A_k^\dagger$ when $Y = \mathbb{I}_{\mathcal{A}_O}$, and the general case follows from the fact that $Y$ can be diagonalized and the sum over $k,k'$ can be reorganized as a sum over $k$ with appropriate coefficients.

The hidden transition map $\mathcal{E}_H: \mathcal{A}_H \otimes \mathcal{A}_H \to \mathcal{A}_H$ for the AKLT chain is given by the multiplication map $$\mathcal{E}_H(Z_1 \otimes Z_2) = Z_1 \mathrm{Tr}(Z_2), \qquad Z_1, Z_2 \in \mathcal{A}_H.
\label{eq:aklt_transition}$$ This map is completely positive and unital, as it is the $*$-homomorphism induced by the multiplication operation on $\mathcal{B}(\mathcal{H}_{1/2})$.

We now verify that the generative triple $(\phi_0, \mathcal{E}_H, \mathcal{E}_{O,H})$ satisfies the symmetry conditions [\[eq:initial_invariance\]](#eq:initial_invariance){reference-type="eqref" reference="eq:initial_invariance"}, [\[eq:Eh_equivariance\]](#eq:Eh_equivariance){reference-type="eqref" reference="eq:Eh_equivariance"}, and [\[eq:EOH_covariance\]](#eq:EOH_covariance){reference-type="eqref" reference="eq:EOH_covariance"}. The verification proceeds through a sequence of lemmas establishing the symmetry properties at each level of the construction, culminating in Theorem [\[thm:aklt_global_invariance\]](#thm:aklt_global_invariance){reference-type="ref" reference="thm:aklt_global_invariance"}. This theorem demonstrates that the global HQMM states $\varphi^{(\text{conv})}$ and $\varphi^{(\text{caus})}$ are invariant under the combined projective-linear action of $\mathrm{SO}(3)$. Together with the nontriviality of the cocycle $[\omega]$, this invariance certifies that the AKLT state realizes a nontrivial SPT phase within the HQMM framework and that this topological protection persists under quantum Markov evolution.

The initial state $\phi_0: \mathcal{A}_H \to \mathbb{C}$ is defined as the vector state associated with the fixed point of the projective representation. Since $\pi$ is irreducible, there exists a unique (up to scalar) vector $\Omega \in \mathcal{H}_{1/2}$ satisfying $\pi(g)\Omega = \lambda(g)\Omega$ for some phase $\lambda(g)$. For the spin-$1/2$ representation, one may take $\Omega$ to be the eigenvector of $\pi(g_z)$ with eigenvalue $1$, which yields a state satisfying $$\phi_0(\pi(g) Z \pi(g)^\dagger) = \phi_0(Z) \qquad \forall g \in G,\; \forall Z \in \mathcal{A}_H,
\label{eq:aklt_initial_invariance}$$ since the phase factors cancel in the expectation value.

::: lemma
[]{#lem:aklt_emission_covariance label="lem:aklt_emission_covariance"} Let $\pi: G \to \mathcal{U}(\mathcal{H}_{1/2})$ be the projective spin-$1/2$ representation and $\rho: G \to \mathcal{U}(\mathcal{H}_1)$ the linear spin-$1$ representation. The emission map $\mathcal{E}_{H,O}$ defined in [\[eq:aklt_emission\]](#eq:aklt_emission){reference-type="eqref" reference="eq:aklt_emission"} satisfies the covariance condition $$\mathcal{E}_{H,O}\bigl( \pi(g) X \pi(g)^\dagger \otimes \rho(g) Y \rho(g)^\dagger \bigr) = \pi(g) \, \mathcal{E}_{H,O}(X \otimes Y) \, \pi(g)^\dagger
\label{eq:aklt_emission_covariance}$$ for all $g \in G$, $X \in \mathcal{A}_H$, and $Y \in \mathcal{A}_O$.
:::

::: proof
*Proof.* Fix $g \in G$, $X \in \mathcal{A}_H$, and $Y \in \mathcal{A}_O$. By definition [\[eq:aklt_emission\]](#eq:aklt_emission){reference-type="eqref" reference="eq:aklt_emission"}, $$\mathcal{E}_{H,O}\bigl( \pi(g) X \pi(g)^\dagger \otimes \rho(g) Y \rho(g)^\dagger \bigr) = \sum_{m,m'} \langle m | \rho(g) Y \rho(g)^\dagger | m' \rangle \, A_m \bigl( \pi(g) X \pi(g)^\dagger \bigr) A_{m'}^\dagger.$$ Using the resolution of the identity $\sum_{k} |k\rangle\langle k| = \mathbb{I}_{\mathcal{H}_1}$ and the unitarity of $\rho(g)$, we expand the matrix element: $$\langle m | \rho(g) Y \rho(g)^\dagger | m' \rangle = \sum_{k,k'} \langle m | \rho(g) | k \rangle \langle k | Y | k' \rangle \langle k' | \rho(g)^\dagger | m' \rangle = \sum_{k,k'} \rho(g)_{mk} \langle k | Y | k' \rangle \overline{\rho(g)_{m'k'}}.$$ Substituting this expression yields $$\mathrm{LHS} = \sum_{k,k'} \langle k | Y | k' \rangle \left( \sum_{m,m'} \rho(g)_{mk} \overline{\rho(g)_{m'k'}} \, A_m \bigl( \pi(g) X \pi(g)^\dagger \bigr) A_{m'}^\dagger \right).$$ Define $S_{k,k'}$ as the inner sum. Since the sums over $m$ and $m'$ factorize, $$S_{k,k'} = \left( \sum_{m} \rho(g)_{mk} A_m \right) \bigl( \pi(g) X \pi(g)^\dagger \bigr) \left( \sum_{m'} \overline{\rho(g)_{m'k'}} A_{m'}^\dagger \right).$$ Applying the covariance condition [\[eq:aklt_covariance\]](#eq:aklt_covariance){reference-type="eqref" reference="eq:aklt_covariance"} to the first factor gives $$\sum_{m} \rho(g)_{mk} A_m = \pi(g) A_k \pi(g)^\dagger.$$ For the third factor, take the adjoint of [\[eq:aklt_covariance\]](#eq:aklt_covariance){reference-type="eqref" reference="eq:aklt_covariance"} applied to index $k'$: $$\sum_{m'} \overline{\rho(g)_{m'k'}} A_{m'}^\dagger = \left( \sum_{m'} \rho(g)_{m'k'} A_{m'} \right)^\dagger = \bigl( \pi(g) A_{k'} \pi(g)^\dagger \bigr)^\dagger = \pi(g) A_{k'}^\dagger \pi(g)^\dagger.$$ Substituting these expressions into $S_{k,k'}$ and using $\pi(g)^\dagger \pi(g) = \mathbb{I}_{\mathcal{H}_{1/2}}$, $$S_{k,k'} = \bigl( \pi(g) A_k \pi(g)^\dagger \bigr) \bigl( \pi(g) X \pi(g)^\dagger \bigr) \bigl( \pi(g) A_{k'}^\dagger \pi(g)^\dagger \bigr) = \pi(g) A_k X A_{k'}^\dagger \pi(g)^\dagger.$$ Therefore, $$\mathrm{LHS} = \sum_{k,k'} \langle k | Y | k' \rangle \, \pi(g) A_k X A_{k'}^\dagger \pi(g)^\dagger = \pi(g) \left( \sum_{k,k'} \langle k | Y | k' \rangle A_k X A_{k'}^\dagger \right) \pi(g)^\dagger = \pi(g) \, \mathcal{E}_{H,O}(X \otimes Y) \, \pi(g)^\dagger,$$ which completes the proof. ◻
:::

::: lemma
[]{#lem:aklt_transition_equivariance label="lem:aklt_transition_equivariance"} The hidden transition map $\mathcal{E}_H$ defined in [\[eq:aklt_transition\]](#eq:aklt_transition){reference-type="eqref" reference="eq:aklt_transition"} satisfies the equivariance condition $$\mathcal{E}_H\bigl( \pi(g) Z_1 \pi(g)^\dagger \otimes \pi(g) Z_2 \pi(g)^\dagger \bigr) = \pi(g) \, \mathcal{E}_H(Z_1 \otimes Z_2) \, \pi(g)^\dagger
\label{eq:aklt_transition_equivariance}$$ for all $g \in G$ and $Z_1, Z_2 \in \mathcal{A}_H$.
:::

::: proof
*Proof.* By definition, $$\mathcal{E}_H\bigl( \pi(g) Z_1 \pi(g)^\dagger \otimes \pi(g) Z_2 \pi(g)^\dagger \bigr) = \bigl( \pi(g) Z_1 \pi(g)^\dagger \bigr) \bigl( \pi(g) Z_2 \pi(g)^\dagger \bigr) = \pi(g) Z_1 \pi(g)^\dagger \pi(g) Z_2 \pi(g)^\dagger.$$ Since $\pi(g)^\dagger \pi(g) = \mathbb{I}_{\mathcal{H}_{1/2}}$, $$\pi(g) Z_1 \pi(g)^\dagger \pi(g) Z_2 \pi(g)^\dagger = \pi(g) Z_1 Z_2 \pi(g)^\dagger = \pi(g) \, \mathcal{E}_H(Z_1 \otimes Z_2) \, \pi(g)^\dagger.$$ ◻
:::

::: lemma
[]{#lem:aklt_initial_invariance label="lem:aklt_initial_invariance"} Let $\pi: G \to \mathcal{U}(\mathcal{H}_{1/2})$ be the irreducible projective spin-$1/2$ representation of $G = \mathrm{SO}(3)$. A state $\phi_0$ on $\mathcal{A}_H = \mathcal{B}(\mathcal{H}_{1/2})$ is said to be $G$-invariant if it satisfies the invariance condition $$\phi_0\bigl( \pi(g) Z \pi(g)^\dagger \bigr) = \phi_0(Z) \qquad \forall g \in G,\; \forall Z \in \mathcal{A}_H.
\label{eq:aklt_initial_invariance}$$ For the irreducible representation $\pi$, the set of $G$-invariant states consists of a single element, namely the normalized trace $$\phi_0(Z) = \frac{1}{\dim(\mathcal{H}_{1/2})} \operatorname{Tr}_{\mathcal{H}_{1/2}}(Z) = \frac{1}{2} \operatorname{Tr}(Z), \qquad Z \in \mathcal{A}_H.$$ This state is unique and serves as the canonical initial state for the AKLT HQMM.
:::

::: proof
*Proof.* We establish the result in two parts: first, we show that the normalized trace satisfies the invariance condition; second, we prove uniqueness.

*Invariance of the normalized trace.* For any $g \in G$ and any $Z \in \mathcal{A}_H$, $$\phi_0\bigl( \pi(g) Z \pi(g)^\dagger \bigr) = \frac{1}{2} \operatorname{Tr}\bigl( \pi(g) Z \pi(g)^\dagger \bigr).$$ By the cyclicity of the trace, $\operatorname{Tr}(\pi(g) Z \pi(g)^\dagger) = \operatorname{Tr}(Z \pi(g)^\dagger \pi(g))$. Since $\pi(g)$ is unitary, $\pi(g)^\dagger \pi(g) = \mathbb{I}_{\mathcal{H}_{1/2}}$, whence $$\operatorname{Tr}(Z \pi(g)^\dagger \pi(g)) = \operatorname{Tr}(Z).$$ Therefore $\phi_0(\pi(g) Z \pi(g)^\dagger) = \frac{1}{2} \operatorname{Tr}(Z) = \phi_0(Z)$, establishing [\[eq:aklt_initial_invariance\]](#eq:aklt_initial_invariance){reference-type="eqref" reference="eq:aklt_initial_invariance"}.

*Uniqueness.* Let $\phi$ be any state on $\mathcal{B}(\mathcal{H}_{1/2})$ satisfying [\[eq:aklt_initial_invariance\]](#eq:aklt_initial_invariance){reference-type="eqref" reference="eq:aklt_initial_invariance"}. By the Riesz representation theorem for finite-dimensional Hilbert spaces, there exists a unique density operator $\rho \in \mathcal{B}(\mathcal{H}_{1/2})$ such that $\phi(Z) = \operatorname{Tr}(\rho Z)$ for all $Z \in \mathcal{A}_H$, with $\rho \ge 0$ and $\operatorname{Tr}(\rho) = 1$. The invariance condition [\[eq:aklt_initial_invariance\]](#eq:aklt_initial_invariance){reference-type="eqref" reference="eq:aklt_initial_invariance"} implies $$\operatorname{Tr}\bigl( \rho \, \pi(g) Z \pi(g)^\dagger \bigr) = \operatorname{Tr}(\rho Z) \qquad \forall g \in G,\; \forall Z \in \mathcal{A}_H.$$ Using the cyclicity of the trace on the left-hand side, $$\operatorname{Tr}\bigl( \pi(g)^\dagger \rho \pi(g) Z \bigr) = \operatorname{Tr}(\rho Z) \qquad \forall g \in G,\; \forall Z \in \mathcal{A}_H.$$ Since this holds for all $Z$, we obtain $$\pi(g)^\dagger \rho \pi(g) = \rho \qquad \forall g \in G,$$ or equivalently, $\pi(g) \rho = \rho \pi(g)$ for all $g \in G$. Thus $\rho$ belongs to the commutant of the irreducible representation $\pi$, i.e., $\rho \in \pi(G)'$. By Schur's lemma, the commutant of an irreducible representation consists of scalar multiples of the identity: $\pi(G)' = \{\lambda \mathbb{I}_{\mathcal{H}_{1/2}} : \lambda \in \mathbb{C}\}$. Hence $\rho = \lambda \mathbb{I}_{\mathcal{H}_{1/2}}$ for some $\lambda \in \mathbb{C}$. Positivity requires $\lambda \ge 0$, and the normalization condition $\operatorname{Tr}(\rho) = 1$ gives $\lambda \dim(\mathcal{H}_{1/2}) = 1$, i.e., $\lambda = 1/\dim(\mathcal{H}_{1/2}) = 1/2$. Consequently, $$\phi(Z) = \operatorname{Tr}\bigl( \tfrac{1}{2} \mathbb{I}_{\mathcal{H}_{1/2}} Z \bigr) = \frac{1}{2} \operatorname{Tr}(Z) = \phi_0(Z),$$ proving uniqueness. ◻
:::

::: remark
The uniqueness of the invariant state is a direct consequence of the irreducibility of the projective representation $\pi$. In the AKLT construction, the virtual space $\mathcal{H}_{1/2}$ carries the irreducible spin-$1/2$ representation of $\mathrm{SO}(3)$, which forces the initial state to be the maximally mixed state $\phi_0(Z) = \frac{1}{2}\operatorname{Tr}(Z)$. This state is often interpreted as the infinite-temperature state on the virtual degrees of freedom, and its uniqueness under the symmetry ensures that the resulting HQMM state inherits the topological protection without additional parameters. Were $\pi$ reducible, a convex family of invariant states would exist, potentially allowing for symmetry-preserving deformations that could trivialize the SPT order.
:::

::: theorem
[]{#thm:aklt_global_invariance label="thm:aklt_global_invariance"} Let $\Xi = (\phi_0, \mathcal{E}_H, \mathcal{E}_{H,O})$ be the HQMM defined by [\[eq:aklt_initial_invariance\]](#eq:aklt_initial_invariance){reference-type="eqref" reference="eq:aklt_initial_invariance"}, [\[eq:aklt_transition\]](#eq:aklt_transition){reference-type="eqref" reference="eq:aklt_transition"}, and [\[eq:aklt_emission\]](#eq:aklt_emission){reference-type="eqref" reference="eq:aklt_emission"}. Let $\varphi^{(\text{c})}$ with $(\text{c})\in\{ (\text{caus}), (\text{conv})\}$, be the global state on $\mathcal{A}_{\mathbb{N}_0}$ generated by $\Xi$ via the conventional causal structure [\[eq:conv_sliced\]](#eq:conv_sliced){reference-type="eqref" reference="eq:conv_sliced"} and [\[eq:caus_sliced\]](#eq:caus_sliced){reference-type="eqref" reference="eq:caus_sliced"}. Then for all $g \in G$, $A \in \mathcal{A}_{H,\mathbb{N}_0}$, and $B \in \mathcal{A}_{O,\mathbb{N}_0}$, $$\varphi^{(\text{c})}\bigl( \alpha_g^{(H)}(A) \otimes \beta_g(B) \bigr) = \varphi^{(\text{c})}(A \otimes B),
\label{eq:aklt_global_invariance}$$ where $\alpha_g^{(H)} = \operatorname{Ad}(\pi(g))$ and $\beta_g = \operatorname{Ad}(\rho(g))$.
:::

::: proof
*Proof.* Lemma [\[lem:aklt_emission_covariance\]](#lem:aklt_emission_covariance){reference-type="ref" reference="lem:aklt_emission_covariance"} and Lemma [\[lem:aklt_transition_equivariance\]](#lem:aklt_transition_equivariance){reference-type="ref" reference="lem:aklt_transition_equivariance"} together verify the hypotheses of Theorem [\[thm:global_invariance\]](#thm:global_invariance){reference-type="ref" reference="thm:global_invariance"}. The result then follows directly. ◻
:::

::: corollary
[]{#cor:aklt_spt label="cor:aklt_spt"} The global HQMM state $\varphi^{(\text{conv})}$ generated by the AKLT tensors carries a nontrivial SPT order characterized by the projective cocycle $[\omega] \in H^2(\mathrm{SO}(3),\mathrm{U}(1)) \cong \mathbb{Z}_2$. The emission map $\mathcal{E}_{O,H}$ acts as a cocycle intertwiner mediating between the projective hidden dynamics and the linear observable dynamics, thereby preserving the topological protection throughout the quantum Markov evolution.
:::

Thus, when viewed as a stationary state of a causal HQMM, the AKLT state exhibits a robust SPT order encoded in the nontrivial cohomology class $[\omega]$. This hierarchical symmetry preservation---from local tensors through the emission map and hidden transition to the global state---reveals how SPT order emerges from the consistent interplay between hidden dynamics and symmetry constraints across all scales of the system [@Pollmann2010; @Tas23].
