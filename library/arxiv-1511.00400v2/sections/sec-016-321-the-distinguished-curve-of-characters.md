---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-016-321-the-distinguished-curve-of-characters
section_title: "The distinguished curve of characters"
section_number: 3.2.1
pages: 19-20
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 1.0
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
The variety of $\mathrm{SL}_2(\mathbb{C})$-representations of $M^3$ is the set $$\hom(\pi_1M^3,\mathrm{SL}_2(\mathbb{C})),$$ which it is an affine algebraic set: if a generating set of $\pi_1M^3$ has $k$ elements, then $\hom(\pi_1M^3,\mathrm{SL}_2(\mathbb{C}))$ embeds in $\mathrm{SL}_2(\mathbb{C})^k\subset  
\mathbb{C}^{4 k}$, by mapping a representation to the image of its generators. The algebraic equations are induced by the relations of the group.

The group $\mathrm{PSL}_2(\mathbb{C})$ acts on $\hom(\pi_1M^3,\mathrm{SL}_2(\mathbb{C}))$ by conjugation, and the affine algebraic quotient is the variety of characters $$X(M^3):= X(M^3,\mathrm{SL}_2(\mathbb{C}))=  \hom(\pi_1M^3,\mathrm{SL}_2(\mathbb{C}))/\! /  \mathrm{PSL}_2(\mathbb{C}).$$ This is defined in terms of the invariant functions: $X( M^3,\mathrm{SL}_2(\mathbb{C}))$ is the algebraic affine set whose function ring $\mathbb{C}[  X(M^3,\mathrm{SL}_2(\mathbb{C})) ]$ is the ring of invariant functions $$\mathbb{C}[ \hom(\pi_1M^3,\mathrm{SL}_2(\mathbb{C}))]^{\mathrm{PSL}_2(\mathbb{C})}.$$

By [@ThurstonBook], see also [@BoileauPorti Appendix B] each component that contains the lift of the holonomy of $M^3$ is a curve.

::: definition
An irreducible component of $X(M^3,\mathrm{SL}_2(\mathbb{C}))$ that contains a lift of the holonomy is called a *distinguished component* and it is denoted by $X_0(M^3)$.
:::

For many manifolds, e.g. for 2-bridge knot exteriors, there is a unique distinguished component. A priori there could be more components, but the definition makes sense because they would be isomorphic. More precisely, there are two characters of the holonomy representation in $\mathrm{PSL}_2(\mathbb{C})$ that are complex conjugate from each other, that correspond to the different orientations. When lifting them to $\mathrm{SL}_2(\mathbb{C})$, this gives $2 \vert   H^1(M^3;\mathbb{Z}/2\mathbb{Z}) \vert$ characters, two for each spin structure. The corresponding components $X_0(M^3)$ are isomorphic by means of the natural action of $H^1(M^3;\mathbb{Z}/2\mathbb{Z})$ and complex conjugation.

Recently, Casella, Luo, and Tillmann [@CLT] have shown an example of hyperbolic manifold with one cusp $M^3$ such that the holonomy characters of the different orientations lie in different components of $X(M^3,\mathrm{PSL}_2(\mathbb{C}))$. To my knowledge, the following question is still open:

::: question
Once $M^3$ is *oriented*, are all the lifts of the oriented holonomy contained in a single irreducible component of $X(M^3,\mathrm{SL}_2(\mathbb{C}))$?
:::

The distinguished component $X(M^3,\mathrm{SL}_2(\mathbb{C}))$ is a curve and it was studied by Thurston in his proof of the hyperbolic Dehn filling theorem [@ThurstonBook]. More precisely, in a neighborhood of the holonomy of the complete structure of $M^3$, the representations are holonomies of incomplete structures, and in some cases the completion is a Dehn filling. This is discussed in Paragraph [\[sec:Dehnfilling\]](#sec:Dehnfilling){reference-type="ref" reference="sec:Dehnfilling"}.
