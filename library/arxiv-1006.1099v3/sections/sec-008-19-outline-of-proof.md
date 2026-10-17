---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-008-19-outline-of-proof
section_title: "Outline of proof"
section_number: 1.9
pages: 7-9
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.988
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
As mentioned previously, our proof of Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} constructs equivalences with quasi-isomorphic images $$D^{\pi}\EuScript{F}(\Sigma) \ \hookrightarrow \ D^{\pi}\EuScript{F}(Z) \ \hookleftarrow  \ D^{\pi}\EuScript{F}(Q_0\cap Q_1;0).$$ Both $\EuScript{F}(\Sigma_g)$ and $\EuScript{F}(Q_0 \cap Q_1)$ are naturally ${\mathbb Z}_{4g-4}$-graded, but only the underlying ${\mathbb Z}_2$-graded categories are equivalent; from this perspective, that is because the intermediate category $\EuScript{F}(Z)$ only admits a ${\mathbb Z}_2$-grading. At a technical level, the proof of Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} combines five principal ingredients.

1.  *Lefschetz fibrations* provide the basic geometric setting in which all the investigations take place. Thus, a hyperelliptic curve and the relative quadric $Z$ are viewed as Lefschetz fibrations with categorically-equivalent fibres.

2.  *Eigenvalue splittings* for Fukaya categories; in particular, we derive sufficient conditions for a collection of Lagrangian spheres to split-generate a particular summand.

3.  *Quilt theory*, in the sense of Mau-Wehrheim-Woodward; specifically, we appeal to their work to construct embeddings of categories associated to (idempotent summands of) Lagrangian correspondences which arise from blowing up certain codimension two complete intersections.

4.  *Surgery* and *${\mathbb Z}$-gradings*, whereby certain holomorphic polygons are constrained by knowledge of related polygons for a Lagrange surgery at an isolated intersection point, or by their intersection numbers with divisors of poles of holomorphic volume forms.

5.  *Finite determinacy*, introduced in this setting in Seidel's beautiful paper [@Seidel:HMSgenus2], which relies on Kontsevich's formality theorem to describe certain $A_{\infty}$-structures in terms of polyvector fields. Eventually, the Fukaya categories of the curve and the relative quadric are identified by singling out a quasi-isomorphism class of $A_{\infty}$-structures on an exterior algebra with the desired Hochschild cohomology.

These ingredients are assembled as general tools in Section [\[Section:Fukaya\]](#Section:Fukaya){reference-type="ref" reference="Section:Fukaya"}, and deployed in the subsequent parts of the paper. The connection $\hookleftarrow$ between $\EuScript{F}(Z)$ and the Fukaya category of the base locus seems to be part of a wider phenomenon for blow-ups; it also makes a connection to a well-known "spinning\" construction of Lagrangian spheres, which provides a link between algebra and geometry useful for establishing Addendum [\[Thm:Action\]](#Thm:Action){reference-type="ref" reference="Thm:Action"}. The material on Fukaya categories of blow-ups should be compared to the work of Abouzaid, Auroux and Katzarkov [@AAK], who derive closely related results from the "Strominger-Yau-Zaslow\" perspective of Lagrangian torus fibrations; similar techniques are also applied in Seidel's recent [@Seidel:Flux]. These results might be viewed as an open-string counterpart to the symplectic birational geometry programme of Yongbin Ruan and his collaborators.

::: Remark
[]{#Rem:OurSpacesAreMonotone label="Rem:OurSpacesAreMonotone"} The symplectic manifolds which occur in the paper are real surfaces or Fano varieties, hence are monotone with minimal Chern number $\geq 1$, and the Lagrangian submanifolds we consider are monotone of minimal Maslov number $\geq 2$. These hypotheses considerably simplify the definition of $\EuScript{F}(\bullet; \lambda)$, which can then be constructed using essentially classical tools, and allow us to make systematic use of the quilted Floer theory of Mau, Wehrheim and Woodward [@MWW:Announce]. We emphasise that Fukaya categories enter the main argument in a rather formal manner, and the properties we require would hold independent of the finer details of the construction. That underlying construction is nonetheless a very substantial undertaking, and we are accordingly indebted to the foundational work of Fukaya-Oh-Ohta-Ono, of Seidel, and of Mau-Wehrheim-Woodward.
:::

::: small
*Organisation of the paper*. Section [\[Sec:Top\]](#Sec:Top){reference-type="ref" reference="Sec:Top"} gives background on the spaces $\EuScript{M}(\Sigma_g)$ and derives the results of Sections [\[Sec:RepVar\]](#Sec:RepVar){reference-type="ref" reference="Sec:RepVar"} and [\[Sec:InstFloer\]](#Sec:InstFloer){reference-type="ref" reference="Sec:InstFloer"}, assuming Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"}. This section is largely self-contained, though at one or two points we refer ahead for general Floer-theoretical results. Such results are collected in Section [\[Section:Fukaya\]](#Section:Fukaya){reference-type="ref" reference="Section:Fukaya"}. The proof of Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} itself takes up the remainder of the paper, Sections [\[Sec:BaseToQuadric\]](#Sec:BaseToQuadric){reference-type="ref" reference="Sec:BaseToQuadric"} and [\[Sec:CurveToQuadric\]](#Sec:CurveToQuadric){reference-type="ref" reference="Sec:CurveToQuadric"}. A low-dimensional topologist happy to take the proof of Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} on faith can stop reading at the end of Section [\[Sec:Top\]](#Sec:Top){reference-type="ref" reference="Sec:Top"}. A symplectic topologist interested in Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} but unconcerned with 3-manifolds can start reading from Section [\[Section:Fukaya\]](#Section:Fukaya){reference-type="ref" reference="Section:Fukaya"}.
:::

I am extremely indebted to Mohammed Abouzaid, Denis Auroux and Paul Seidel for all their help and their numerous patient explanations. This paper is written very much in the shadow of Seidel's [@Seidel:HMSgenus2]. Conversations with Tom Bridgeland, Alex Dimca, Tobias Dyckerhoff, Sasha Efimov, Tobias Ekholm, Rahul Pandharipande, Tim Perutz, Catharina Stroppel and Burt Totaro were also influential. Detailed and insightful comments from the anonymous referees have dramatically improved the paper, both clarifying and simplifying the exposition.

The author is partially supported by grant ERC-2007-StG-205349 from the European Research Council. Part of this work was undertaken whilst the author held a Research Professorship at the Mathematical Sciences Research Institute, Berkeley; thanks to MSRI for hospitality.
