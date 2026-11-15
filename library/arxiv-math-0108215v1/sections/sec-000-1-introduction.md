---
doc_id: arxiv-math-0108215v1
doc_title: "arXiv:math/0108215v1 [math.GT] 30 Aug 2001"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0108215v1.pdf
source_sha256: 191784d2ccb3415a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.942
doc_brief: "arXiv:math/0108215v1 [math.GT] 30 Aug 2001 — The M¨obius energy of a knot is an energy functional for smooth curves based on an idea of self-repelling."
---
In this paper, we exhibit a bound for the Möbius energy of a knot, in terms of the amount of "rope" needed to make the knot. This is the energy introduced in [@O1] and studied extensively in [@FHW; @KS]. We follow an overall approach suggested by G. Buck for showing that any inverse-square knot energy should be bounded by the $4/3$ power of the ropelength.

We and other researchers have defined a number of different energy functions for (smooth or polygonal) knots [@O1; @FHW; @KS; @BO1; @BS; @BS2; @BS3; @DEJ; @Fu; @Lo; @O3; @O2; @O4; @Si3; @Si4; @Si2] based on the idea of inverse-square repelling energy (so these would correspond to inverse-cube "forces"). (See also [@Mo] for a different approach). Roughly, these energies are defined in terms of integrals over the curve $K$ $$\int\nolimits_{x \in K}\int\nolimits_{y \in
K}{\frac{\Box}{|x-y|^2}}\;\d x\;\d y\;\;.$$ Here $\Box$ is a placeholder for any of several kinds of terms that make the integral not give too much weight to the repelling of points that are close to each other in the sense of arclength along the knot (so the improper integral will converge). The same purpose is accomplished by defining energies as integrals of differences [@O1; @FHW], $$\int\nolimits_{x \in K}\int\nolimits_{y \in
K}{\frac1{|x-y|^2}}\;\;
-\;\;{\frac1{|s-t|^2}}\;\;\;\d x\;\d y\;.$$ Here $s,t$ lie on a line or circle used for a unit-speed parameterization of the curve $K$ with $s\mapsto x$ and $t\mapsto y$. The energy we study in this paper can be defined either way [@O1; @FHW; @KS] and we shall use the latter.

In addition to viewing a curve as self-repelling, one also can view it as self-excluding, and define the *ropelength* energy $E_L(K)$ [@BO1; @BS2; @BS3]: this is the ratio of the arclength of the curve to the maximum radius of a uniform non self-intersecting tube along the curve [@LSDR], i.e. the ratio of length to radius of the rope (see Section [\[thelemmas\]](#thelemmas){reference-type="ref" reference="thelemmas"} for precise definitions). Variations on thickness are developed in [@Mo; @devrthickness; @DEJ2; @devrthickness2; @maddocks; @KS2; @meideal; @mine].

We showed in [@BS3] that the *normal* energy $E_N(K)$, which discounts tangential self-repelling, and the *symmetric* energy $E_S(K)$, which models self-radiation of a filament [@B2], are bounded by the ropelength. These energies, in turn, dominate the number of crossings in any regular projection of the knot. The inequalities are of the form shown below in ([\[longineq\]](#longineq){reference-type="ref" reference="longineq"}). Here $\mathrm{acn}(K)$ is the *average crossing number*, that is the average, over all spatial directions, of the number of crossings seen from each direction. This, in turn, is larger than the crossing number $\mathrm{cr}(K)$, which is the minimum over all regular projections, and $\mathrm{cr}[K]$, which considers all $K$ in a given knot type.

$$4\pi\,\mathrm{cr}[K] \leq 4\pi\,
\mathrm{cr}(K)< 4
\pi\, \mathrm{acn}(K) \leq
E_S(K) \leq E_N(K) \leq c\,E_L(K)^{4/3}
\label{longineq}$$

The coefficient $c$ varies with different proofs; the exponent $4/3$ is sharp. A related idea is the *writhe* of a knot, $\mathrm{wr}(K)$, which is the average over all spatial directions of the *signed* crossing numbers. Since $\mathrm{wr}(K) \leq \mathrm{acn}(K)$, we get the same bound on $4\pi\, \mathrm{wr}(K)$. But using a different analysis of writhe, in terms of vector fields flowing in tubes around the knot, it is shown in [@CDG] that $\mathrm{wr}(K) \leq {\frac14}
E_L(K)^{4/3}$, which is a lower coefficient than we have for $\mathrm{acn}(K)$. The coefficient, approximately $5$, that we obtain in this paper is lower than in [@BS3], because we do a more subtle analysis. While coefficients might be improved, the exponent $4/3$ in inequality ([\[longineq\]](#longineq){reference-type="ref" reference="longineq"}) is sharp, because of examples [@B3; @CKS] where crossing number grows like the $4/3$ power of ropelength. Similarly, because Möbius energy also bounds crossing number [@FHW], the same examples show that the exponent $4/3$ in Theorem [\[main\]](#main){reference-type="ref" reference="main"} of this paper is sharp.

Our main result is that the Möbius energy is bounded by the $4/3$ power of the ropelength (with coefficient $\approx 5$). This and the results cited above support our belief that ropelength is the fundamental measure of knot complexity: given a bound on ropelength, one can find a bound on any other given knot invariant.

We state the theorem for the version of the energy that equals $4$ on a circle, $$E_{O4}(K) = \int\nolimits_{x \in
K}\int\nolimits_{y \in K} {  {\frac1{|x-y|^2}} - {  
{\frac1{\mathrm{arc}(x,y)^2}}   }}\;\;,$$ where $\mathrm{arc}(x,y)$ denotes the minimum arclength along the curve $K$ between $x$ and $y$.

We use one kind of analysis to bound the energy contribution coming from pairs of points $(x,y)$ where $x$ and $y$ are near each other in arclength along the knot, and a different analysis for pairs where $x$ and $y$ are relatively far apart. The analysis of proximal pairs will be special for each particular energy function, and yields typically a *linear* bound on energy in terms of ropelength. The analysis of distal pairs is identical for the various energy functions: with little work, we can get a bound on energy that is *quadratic* in ropelength; and with more work, we obtain a bound that is $4/3$ power in the ropelength. We add the proximal and distal contributions to get the overall bound.

In a recent book [@SKK], many ideas of energy and thickness for knots are discussed. Many of us interested in such ideas thought that knots should have "ideal" forms. It has turned out that the knot conformations that minimize the various ideas of energy differ from one another. The similarities and differences are equally provocative.
