---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-077-104-projective-dg-bundles
section_title: "Projective dg bundles"
section_number: 10.4
pages: 74-75
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.917
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:proj dg label="sub:proj dg"}

We do not wish to define projective dg schemes in complete generality, but instead focus on projectivizations of dg vector bundles $\mathcal{V}^\bullet$ on a space $X$.

::: definition
[]{#def:prog dg space label="def:prog dg space"}

A projective dg bundle is defined through its category of coherent sheaves: $$\mathrm{Coh}(\mathrm{Proj}\ S_X \mathcal{V}^\bullet) = \frac {\left\{\text{graded }S^*_X\mathcal{V}^\bullet \text{ dg modules} \right\}}{\left( S^{*}\mathcal{V}^\bullet/S^{* > 0}\mathcal{V}^\bullet \right) \cong 0}$$
:::

Let us make two remarks: first of all, an object in $\mathrm{Coh}(\mathrm{Proj}\ S_X \mathcal{V}^\bullet)$ has two gradings. The first comes from the power $*$ of the symmetric power, and the second comes from the dg grading on $\mathcal{V}^\bullet$. Secondly, the difference between a projectivization and the affine cone $\mathrm{Spec}\ S_X\mathcal{V}^\bullet$ is the same as in the classical case: there is, in the derived category of the former, an additional quasi-isomorphism between the structure sheaf of the zero section and the zero module.

::: example
[]{#ex:proj dg label="ex:proj dg"}

As in Example [\[ex:proj dg\]](#ex:proj dg){reference-type="ref" reference="ex:proj dg"}, let us study the case when $\mathcal{V}^\bullet = [\mathcal{M}\stackrel{s}\longrightarrow \mathcal{N}]$ is a two step complex of vector bundles, concentrated in degrees $-1$ and $0$. In this case, we have a map: $$\label{eqn:support}
\includegraphics{10_9.png}$$ where the map $\pi$ is an actual projective bundle since $\mathcal{N}$ is a vector bundle on $X$. The symbol $\hookrightarrow$ emulates closed embeddings of schemes, because we tautologically have: $$\label{eqn:coherent dg}
\mathrm{Coh}\left( \mathrm{Proj}\ S_X [\mathcal{M}\stackrel{s}\longrightarrow \mathcal{N}] \right) \cong$$ $$\cong \Big\{\text{coherent sheaves on }\mathrm{Proj}\ S_X  \mathcal{N}\text{ endowed with a dg action of }\wedge^\bullet[\pi^*\mathcal{M}(-1) \stackrel{s}\rightarrow \mathcal{O}_{\mathrm{Proj}\ S_X  \mathcal{N}}] \Big\}$$ With this in mind, we think of $\mathrm{Proj}\ S_X [\mathcal{M}\stackrel{s}\longrightarrow \mathcal{N}]$ as the dg subscheme of $\mathrm{Proj}\ S_X  \mathcal{N}$ cut out by the cosection $s$ of the vector bundle $\pi^*\mathcal{M}(-1)$.
:::

Our main Example [\[ex:proj dg\]](#ex:proj dg){reference-type="ref" reference="ex:proj dg"} should be interpreted as a dg version of the familiar notion of projective bundles $\mathrm{Proj}\ S_X\mathcal{V}\stackrel{\pi}\longrightarrow X$, where $\mathcal{V}$ is a rank $n$ locally free sheaf of $X$. In this case, recall the following formulas: $$\pi_*(\mathcal{O}(k)) = S^k\mathcal{V}\qquad \quad \qquad \text{ concentrated in degree 0}$$ $$\pi_*(\mathcal{O}(-k)) = S^{k-n} \mathcal{V}^\vee \otimes \wedge^{\text{top}} \mathcal{V}^\vee \quad \text{concentrated in degree }n-1$$ for all $k\in \mathbb{N}$, where $\pi_*$ denotes the derived pull-back. The second equality follows from the first one, together with **relative Serre duality**: $$\label{eqn:serre scheme}
R^\bullet \pi_*(\mathcal{A}) = R^{\bullet - n + 1} \pi_{*}(\mathcal{A}^\vee \otimes \wedge^\text{top} \mathcal{V}(-n))^\vee$$ for all $\mathcal{A}\in D^b(\mathrm{Coh}(\mathrm{Proj}\ S_X\mathcal{V}))$. We now prove a similar formula in the dg setting

::: proposition
[]{#prop:canonical label="prop:canonical"}

In the notation of Example [\[ex:proj dg\]](#ex:proj dg){reference-type="ref" reference="ex:proj dg"}, suppose $\text{rank }\mathcal{M}= m$ and $\text{rank }\mathcal{N}= n$. Then: $$\label{eqn:serre dg scheme}
R^\bullet \pi^\emph{dg}_*(\mathcal{A}) = R^{\bullet - n + m + 1} \pi^\emph{dg}_{*}\left(\mathcal{A}^\vee \otimes \frac {\wedge^\emph{top}\mathcal{N}(-n)}{\wedge^\emph{top}\mathcal{M}(-m)}\right)^\vee$$ for all $\mathcal{A}\in D^b(\mathrm{Coh}(\mathrm{Proj}\ S_X [\mathcal{M}\stackrel{s}\longrightarrow \mathcal{N}] ))$
:::

::: proof
*Proof.* Implicitly in equation [\[eqn:coherent dg\]](#eqn:coherent dg){reference-type="eqref" reference="eqn:coherent dg"}, one has the equation: $$R^\bullet \pi^\text{dg}_*(\mathcal{A}) = R^\bullet \pi_* \left(\mathcal{A}\otimes \wedge^\bullet[\pi^*\mathcal{M}(-1) \stackrel{s}\rightarrow \mathcal{O}] \right)$$ Applying [\[eqn:serre scheme\]](#eqn:serre scheme){reference-type="eqref" reference="eqn:serre scheme"} to the right hand side, we obtain $$R^\bullet \pi^\text{dg}_*(\mathcal{A}) = R^{\bullet-n+1} \pi_{*} \left(\mathcal{A}^\vee \otimes \wedge^\bullet \left[\pi^*\mathcal{M}(-1) \stackrel{s}\rightarrow \mathcal{O}\right]^\vee \otimes \wedge^\text{top} \mathcal{N}^\vee(-n) \right)^\vee$$ It is easy to see that $\wedge^\bullet \left[\pi^*\mathcal{M}(-1) \stackrel{s}\rightarrow \mathcal{O}\right]^\vee = \wedge^{\bullet+m} \left[\pi^*\mathcal{M}(-1) \stackrel{s}\rightarrow \mathcal{O}\right] \otimes \wedge^{\text{top}}\mathcal{M}^\vee(m)$, hence: $$R^\bullet \pi^\text{dg}_*(\mathcal{A}) = R^{\bullet-n+m+1} \pi_{*} \left(\mathcal{A}^\vee \otimes \wedge^\bullet \left[\pi^*\mathcal{M}(-1) \stackrel{s}\rightarrow \mathcal{O}\right] \otimes \frac {\wedge^{\text{top}}\mathcal{N}(-n)}{\wedge^{\text{top}}\mathcal{M}(-m)} \right)^\vee$$ which equals $R^{\bullet - n + m + 1} \pi^\text{dg}_{*}\left(\mathcal{A}^\vee \otimes \frac {\wedge^\text{top}\mathcal{N}(-n)}{\wedge^\text{top}\mathcal{M}(-m)}\right)^\vee$ by another application of [\[eqn:coherent dg\]](#eqn:coherent dg){reference-type="eqref" reference="eqn:coherent dg"}. ◻
:::
