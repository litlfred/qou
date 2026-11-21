---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-045-52-cohomology-of-sheaves-on-fhilb2
section_title: "Cohomology of sheaves on FHilb2"
section_number: 5.2
pages: 43-44
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.887
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:coh 2 label="sub:coh 2"}

On the projectivization [\[eqn:matrix fh 2\]](#eqn:matrix fh 2){reference-type="eqref" reference="eqn:matrix fh 2"}, the line bundles of importance for us are $\mathcal{L}_1 \cong \mathcal{O}$ and $\mathcal{L}_2 \cong \mathcal{O}(1)$, where the latter denotes the Serre twisting sheaf. Note that: $$\label{eqn:taut 2}
\mathcal{T}_2 \cong \mathcal{O}\oplus \mathcal{O}(1)$$ We will now compute the cohomology groups of certain line bundles on $\mathrm{FHilb}_2$. To simplify our computations by removing a factor of $\mathbb{C}$, we will work with the reduced version all the schemes and dg schemes in question (see Subsection [\[sub:reduced\]](#sub:reduced){reference-type="ref" reference="sub:reduced"}). Specifically, this means: $$\label{eqn:bar a}
\overline{\mathrm{FHilb}}_2 = \mathrm{Proj}(\overline{A}) \qquad \text{where } \overline{A}= \frac{\mathbb{C}[x,z,w]}{xw}$$ where we set $x_1+x_2=0$ and $x_1-x_2 = x$. The irreducible components of this variety are: $$\overline{Z}_1 = \mathbb{C}\qquad \text{and} \qquad \overline{Z}_2 = \mathbb{P}^1 = \mathrm{FHilb}_2(\mathrm{point})$$ Note that $\overline{\mathcal{T}}_2 = \mathcal{O}(1)$. The following cohomology computations are well-known: $$H^i(\overline{Z}_1,\mathcal{O}(k)) = \frac {q^{k}}{1-q} \cdot \delta_{i,0}$$ because $\overline{Z}_1 = \mathbb{C}$, while: $$H^i(\overline{Z}_2,\mathcal{O}(k))=\begin{cases}
t^k+\ldots+q^k\ & \text{if}\ i=0 \text{ and } k\ge 0\\
(qt)^{-1}(t^{k+2}+\ldots+q^{k+2})\ & \text{if}\ i=1 \text{ and } k\le -2 \\
0 & \text{otherwise}
\end{cases}$$ because $\overline{Z}_2 = \mathbb{P}^1$ with equivariant weights $q$ and $t$. Consider the short exact sequence: $$\xymatrix{
0 \ar[r] & q\mathcal{O}_{\overline{Z}_1} \ar[r]^-{x} & \mathcal{O}_{\overline{\mathrm{FHilb}}_2} \ar[r] & \mathcal{O}_{\overline{Z}_2} \ar[r] & 0}$$ which is induced by [\[eqn:irreducible components n=2\]](#eqn:irreducible components n=2){reference-type="eqref" reference="eqn:irreducible components n=2"}. Because the cohomology of sheaves on $\overline{Z}_1$ is concentrated in degree 0, we have the following equality of $(q,t)$--equivariant vector spaces: $$H^i(\overline{\mathrm{FHilb}}_2,\mathcal{O}(k)) = q H^i(\overline{Z}_1,\mathcal{O}(k)) + H^i(\overline{Z}_2,\mathcal{O}(k)) =$$ $$\label{eqn:coh n=2}
= \begin{cases}
t^k+\ldots+q^k+\frac{q^{k+1}}{1-q} & \text{if}\ i=0 \text{ and } k\ge 0\\
\frac{q^{k+1}}{1-q} & \text{if}\ i=0 \text{ and } k<0\\
(qt)^{-1}(t^{k+2}+\ldots+q^{k+2}) & \text{if}\ i=1 \text{ and } k\le -2 \\
0 & \text{otherwise}
\end{cases}$$ The analogous equalities for the non-reduced version $\mathrm{FHilb}_2$ are obtained by dividing the right hand sides of [\[eqn:coh n=2\]](#eqn:coh n=2){reference-type="eqref" reference="eqn:coh n=2"} by $1-q$.
