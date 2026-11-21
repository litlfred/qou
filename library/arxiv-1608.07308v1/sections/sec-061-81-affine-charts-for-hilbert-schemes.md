---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-061-81-affine-charts-for-hilbert-schemes
section_title: "Affine charts for Hilbert schemes"
section_number: 8.1
pages: 58-59
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.878
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:affinecharts1 label="sub:affinecharts1"}

Recall the action of $\mathbb{C}^{*} \times \mathbb{C}^*$ on Hilbert schemes given by rescaling the $X$ and $Y$ matrices. The fixed points of this action on the Hilbert scheme are well-known. They are given by monomial ideals, which are indexed by partitions of $n$: $$\mathrm{Hilb}_n^{\mathbb{C}^{*} \times \mathbb{C}^*} = \{I_\lambda\}_{\lambda \vdash n}, \qquad I_\lambda = (x^{\lambda_1}, x^{\lambda_2}y,...)\subset \mathbb{C}[x,y]$$ Haiman described a set of affine charts on the Hilbert scheme, each of which is $\mathbb{C}^{*} \times \mathbb{C}^*$ invariant and contains a single fixed point: $$\label{eqn:chart0}
\mathrm{Hilb}_n = \bigcup_{\lambda \vdash n} \mathring{\mathrm{Hilb}}_\lambda$$ where: $$\label{eqn:haimanchart}
\mathring{\mathrm{Hilb}}_\lambda = \Big \{I \text{ such that } \{x^ay^b\}_{(a,b) \in \lambda} \text{ is a basis of } \mathbb{C}[x,y]/I\Big\}$$ Here and throughout this paper, we identify a partition with its Young diagram, which is the set of $1 \times 1$ boxes in the first quadrant of the plane with coordinates $(a,b) \in \mathbb{N}_0 \times \mathbb{N}_0$, $b < \lambda_{a}$:

::: picture
(100,150)(-130,-20) []{#fig0 label="fig0"}

(0,0)(1,0)160 (0,40)(1,0)160 (0,80)(1,0)120 (0,120)(1,0)40

(0,0)(0,1)120 (40,0)(0,1)120 (80,0)(0,1)80 (120,0)(0,1)80 (160,0)(0,1)40
:::

For example, the above Young diagram corresponds to the partition $\lambda = (4,3,1)$. It would be very nice to have a clear description of the algebra of functions on each affine chart [\[eqn:chart0\]](#eqn:chart0){reference-type="eqref" reference="eqn:chart0"}, but this is not at all easy. Instead, Haiman's construction gives us a set of generators: $$\{f_1,...,f_{2n} \} \in \mathfrak{m}_\lambda/\mathfrak{m}^2_\lambda$$ where $\mathfrak{m}_\lambda \in \mathbb{C}[\mathring{\mathrm{Hilb}}_\lambda]$ denotes the maximal ideal of the fixed point $I_\lambda$.
