---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-004-14-statement-of-results
section_title: "Statement of results"
section_number: 1.4
pages: 3-4
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.88
latex_coverage_ratio: 0.981
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
We briefly state our main results about the triangulation independent Ptolemy varieties. A summary of their definition is given in Section [\[sec:Algorithm\]](#sec:Algorithm){reference-type="ref" reference="sec:Algorithm"}, and explicit computations are given in Section [\[sec:Examples\]](#sec:Examples){reference-type="ref" reference="sec:Examples"}. Let $M$ be a compact, orientable $3$-manifold with non-empty boundary, and let $\mathcal T$ be a topological ideal triangulation of $M$.

Any $P$-decorated boundary-unipotent representation $\rho\colon\pi_1(M)\to\mathop{\mathrm{SL}}(2,\mathbb C)$ assigns Ptolemy coordinates to the edges of $\mathcal T$ (see Section [\[sec:PtDecCocReview\]](#sec:PtDecCocReview){reference-type="ref" reference="sec:PtDecCocReview"}). If all Ptolemy coordinates are zero, we say that the decorated representation is *totally degenerate*. This notion turns out to be independent of the (ideal) triangulation and implies that the representation is reducible (see Section [\[sec:TotallyDegenerate\]](#sec:TotallyDegenerate){reference-type="ref" reference="sec:TotallyDegenerate"}).

Recall that although the set of representations of $\pi_1(M)$ is a variety, the set of representations up to conjugation is not a variety in general. The same holds for decorated representations. However, if we discard the totally degenerate decorations, we get a variety:

::: theorem
[]{#thm:MainResult label="thm:MainResult"} The conjugation action on the set of non totally degenerate decorated boundary-unipotent representations has a geometric quotient. For each triangulation $\mathcal T$ of $M$, the invariant Ptolemy variety $\overline P(\mathcal T)$ provides explicit coordinates, i.e. we have an isomorphism of varieties $$\label{eq:MainResult}
\overline P(\mathcal T)\cong\left\{\txt{Not totally degenerate, $P$-decorated, \\boundary-unipotent $\pi_1(M)\to\mathop{\mathrm{SL}}(2,\mathbb C)$}\right\}\big/\mathop{\mathrm{Conj}}.$$ In particular, $\overline P(\mathcal T)$ is independent of the triangulation. Morever, $P(\mathcal T)$ embeds in $\overline P(\mathcal T)$ as a Zariski open subset. 0◻
:::

::: definition
A representation is *boundary-nondegenerate* if its restriction to $\pi_1(\partial_i M)$ is non-trivial for each boundary component $\partial_i M$ of $M$.
:::

Theorems [\[thm:OneToOneOverNonDegenerate\]](#thm:OneToOneOverNonDegenerate){reference-type="ref" reference="thm:OneToOneOverNonDegenerate"}, [\[thm:MainThmPSL\]](#thm:MainThmPSL){reference-type="ref" reference="thm:MainThmPSL"} and [\[thm:MainThmEnhanced\]](#thm:MainThmEnhanced){reference-type="ref" reference="thm:MainThmEnhanced"} below are elementary corollaries of Theorem [\[thm:MainResult\]](#thm:MainResult){reference-type="ref" reference="thm:MainResult"} and its analogues for the modified variants. They were previously known for representations admitting a *generic* decoration (see [@PtolemyField; @GaroufalidisThurstonZickert; @ZickertEnhancedPtolemy]).

::: theorem
[]{#thm:OneToOneOverNonDegenerate label="thm:OneToOneOverNonDegenerate"} The map $$\label{eq:RedOneToOne}
\overline P(\mathcal T)_{\mathop{\mathrm{red}}}\to\left\{\txt{Boundary-unipotent\\$\pi_1(M)\to\mathop{\mathrm{SL}}(2,\mathbb C)$}\right\}\big/\mathop{\mathrm{Conj}}$$ induced from [\[eq:MainResult\]](#eq:MainResult){reference-type="eqref" reference="eq:MainResult"} by ignoring the decoration has image containing all irreducible representations and is one-to-one over the set of irreducible boundary-nondegenerate representations.0◻
:::

::: theorem
[]{#thm:MainThmPSL label="thm:MainThmPSL"} Let $k=\big\vert H^1(M,\partial M;\mathbb Z/2\mathbb Z)\big\vert$. The map $$\label{eq:RedkToOne}
\overline P^\sigma(\mathcal T)_{\mathop{\mathrm{red}}}\to\left\{\txt{Boundary-unipotent\\$\pi_1(M)\to\mathop{\mathrm{PSL}}(2,\mathbb C)$\\with obstruction class $\sigma$}\right\}\big/\mathop{\mathrm{Conj}}$$ has image containing all irreducible representations and is $k:1$ over the set of irreducible, boundary-nondegenerate representations. 0◻
:::

::: theorem
[]{#thm:MainThmEnhanced label="thm:MainThmEnhanced"} Suppose $M$ has $c$ boundary components, all of which are tori. There is a map $$\label{eq:RedTwoToOne}
\mathcal E\overline P(\mathcal T)_{\mathop{\mathrm{red}}}\to\left\{\txt{Boundary-Borel\\$\pi_1(M)\to\mathop{\mathrm{SL}}(2,\mathbb C)$}\right\}\big/\mathop{\mathrm{Conj}}$$ with image containing all irreducible representations. It is generically $2^c:1$ over the irreducible, boundary-nondegenerate representations. Moreover, the projection to the $(m_s,l_s)$ coordinates is the variety of eigenvalues of $\mu_s$ and $\lambda_s$.0◻
:::

This can be used to compute the $A$-polynomial; see Section [\[sec:Apolyexample\]](#sec:Apolyexample){reference-type="ref" reference="sec:Apolyexample"} for an example.

::: remark
The image of [\[eq:RedOneToOne\]](#eq:RedOneToOne){reference-type="eqref" reference="eq:RedOneToOne"}, [\[eq:RedkToOne\]](#eq:RedkToOne){reference-type="eqref" reference="eq:RedkToOne"}, and [\[eq:RedTwoToOne\]](#eq:RedTwoToOne){reference-type="eqref" reference="eq:RedTwoToOne"} may contain reducible representations as well (see e.g. the example in Section [\[sub:Reducible\]](#sub:Reducible){reference-type="ref" reference="sub:Reducible"}), but such are necessarily boundary-degenerate (see Proposition [\[prop:TotallyDegenerate\]](#prop:TotallyDegenerate){reference-type="ref" reference="prop:TotallyDegenerate"}). The preimage over a representation which is not boundary-nondegenerate is typically (although not always; see Remark [\[rm:Freedom\]](#rm:Freedom){reference-type="ref" reference="rm:Freedom"}) higher dimensional.
:::

::: remark
One could detect all representations (including all reducible ones) by performing a single barycentric subdivision [@GaroufalidisThurstonZickert]. The resulting variety, however, is not a topological invariant since each non-ideal vertex (generically) increases the dimension by one. The growth in the number of simplices and the expected dimension also makes computations infeasible. More importantly, invariants such as the loop invariant [@DG], important in quantum topology, are only defined when all vertices are ideal.
:::

::: remark
Our varieties are really schemes over $\mathbb Z$. They are typically not irreducible, and the coordinate rings may have nilpotents.
:::
