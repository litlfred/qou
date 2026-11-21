---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-039-46-the-relative-case
section_title: "The relative case"
section_number: 4.6
pages: 38-40
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.894
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:relative label="sub:relative"}

The situation of Example [\[ex:projective\]](#ex:projective){reference-type="ref" reference="ex:projective"} captures a very interesting problem, namely when can we factor a map from a category to a scheme through another scheme: $$\label{eqn:iota0}
\includegraphics{4_23.png}$$ More precisely, $\iota'$ should satisfy the equations $\iota^*=\iota'^*\circ \pi^*$ and $\iota_*=\pi_*\circ \iota'_*$ and all the functors should be derived from now on. The situation we will study in this paper is when: $$Y = \mathbb{P}\mathcal{V}^{\vee} := \mathrm{Proj}_X (S^{\bullet}\mathcal{V})$$ where $\mathcal{V}$ is a coherent sheaf on $X$ of projective dimension 0 or 1. Let us first study the case of projective dimension zero, so assume that $\mathcal{V}$ is a vector bundle.

::: proposition
[]{#prop:lift0 label="prop:lift0"} Suppose that $Y=\mathbb{P}\mathcal{V}^{\vee}$ and that the map $\iota$ in [\[eqn:iota0\]](#eqn:iota0){reference-type="eqref" reference="eqn:iota0"} is constructed. The datum of the extension $\iota'$ is equivalent to an invertible object $F \in \mathcal{C}$ together with an arrow: $$\label{eqn:datum0}
\iota^*\mathcal{V}\stackrel{\alpha}\longrightarrow F$$ in $\mathcal{C}$. This gives $\mathcal{C}$ the structure of a category over $Y$ if and only if: $$\label{eqn:koszul0}
\left[ ... \stackrel{\alpha}\longrightarrow \iota^*\left(\wedge^k \mathcal{V}\right) \otimes F^{-k} \stackrel{\alpha}\longrightarrow ... \right] \stackrel{\emph{h.e.}}\cong 0 \ \in \ K^b(\mathcal{C})$$ The map $\iota'$ is birational if and only if $\iota$ satisfies: $$\label{eqn:properproj0}
S^k\mathcal{V}\cong \iota_*(F^k) \qquad \forall \ k\geq 0$$
:::

::: proof
*Proof.* All notations $\mathcal{O}$ or $\mathcal{O}(k)$ will refer to invertible sheaves on $\mathbb{P}\mathcal{V}^\vee$. If $\iota'$ exists and has all the expected properties, then set $F = {\iota'}^*(\mathcal{O}(1))$. In this case, the map [\[eqn:datum0\]](#eqn:datum0){reference-type="eqref" reference="eqn:datum0"} is simply ${\iota'}^*$ applied to the tautological morphism: $$\pi^*\mathcal{V}\longrightarrow \mathcal{O}(1)$$ on $Y$. The fact that the complex [\[eqn:koszul0\]](#eqn:koszul0){reference-type="eqref" reference="eqn:koszul0"} is quasi-isomorphic to 0 follows by applying ${\iota'}^*$ to the Koszul complex of $Y$. The birationality of $\iota'$ implies that $\iota'_*\mathbf{1} \cong \mathcal{O}$, from which the projection formula implies $\iota'_*(F^k) \cong \mathcal{O}(k)$. Applying $\pi_*$ to this relation implies precisely [\[eqn:properproj0\]](#eqn:properproj0){reference-type="eqref" reference="eqn:properproj0"}. Conversely, suppose that we are given a morphism [\[eqn:datum0\]](#eqn:datum0){reference-type="eqref" reference="eqn:datum0"} which satisfies [\[eqn:koszul0\]](#eqn:koszul0){reference-type="eqref" reference="eqn:koszul0"}, and let us construct the map $\iota'$ that makes the diagram [\[eqn:iota0\]](#eqn:iota0){reference-type="eqref" reference="eqn:iota0"} commute. Note that [\[eqn:datum0\]](#eqn:datum0){reference-type="eqref" reference="eqn:datum0"} gives us an arrow: $$\iota^*\left(\mathcal{V}^{\otimes k} \right) \longrightarrow F^k$$ for all $k\geq 0$. Because $F$ is invertible, this arrow factors through: $$\label{eqn:algebras0}
\iota^*\left(S^k\mathcal{V}\right) \longrightarrow F^k$$ for all $k\geq 0$ (since $F$ is invertible, so is $F^k$, and hence has no nontrivial endomorphisms; this implies that the anti-symmetric projector is zero, hence $S^kF = F^k)$. This allows us to define: $${\iota'}^*(M) = \left(\pi_*(M) \bigotimes_{S^{\bullet}\mathcal{V}} \bigoplus_{k=-\infty}^{\infty} F^k \right)^0$$ A priori, this only determines the functor ${\iota'}^*$ on the level of the homotopy category of coherent sheaves on $\mathbb{P}\mathcal{V}^\vee$. To check that it descends to a functor on the derived category, we must show that ${\iota'}^*$ takes quasi-isomorphic complexes to isomorphic complexes. The fact that this statement is true for the Koszul complex is precisely the assumption [\[eqn:koszul0\]](#eqn:koszul0){reference-type="eqref" reference="eqn:koszul0"}. The fact that this is sufficient is due to Theorem 2.10 of [@DanHL] (see also [@BFK]), which asserts that: $$D^b \left(\mathrm{Coh}(\mathbb{P}\mathcal{V}^\vee ) \right) \cong \text{homotopy category of complexes of} \left( \bigoplus_{i=0}^{\text{rank }\mathcal{V}-1} \mathcal{E}_i(i) \right)_{\mathcal{E}_0,\mathcal{E}_1,... \in D^b(\mathrm{Coh}(X))}$$ As for the right adjoint functor, we set: $$\iota'_*(C) = \iota_* \left( \bigoplus_{k=0}^\infty F^k \otimes C \right)$$ as a graded $\mathcal{O}_X-$module. To realize the right hand side as a sheaf on $Y$, we need to endow it with an action of $S^*\mathcal{V}$, namely with an associative homomorphism of graded algebras: $$S^*\mathcal{V}\otimes_{\mathcal{O}_X} \iota_* \left( \bigoplus_{k=0}^\infty F^k \otimes C \right) \longrightarrow \iota_* \left( \bigoplus_{k=0}^\infty F^k \otimes C \right)$$ The above morphism is obtained via adjunction and [\[eqn:algebras0\]](#eqn:algebras0){reference-type="eqref" reference="eqn:algebras0"}. ◻
:::
