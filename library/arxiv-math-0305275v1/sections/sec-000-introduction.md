---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.875
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2, C)."
---
Let $W$ be a compact manifold and let $\rho$ be a representation of its fundamental group into PSL$(2,\ensuremath{\mathbb C})\simeq$ Isom$^+(\ensuremath{\mathbb H}^3)$. The volume of $\rho$ is defined by taking any $\rho$-equivariant map from the universal cover $\widetilde{W}$ to $\ensuremath{\mathbb H}^3$ and then by integrating the pull-back of the hyperbolic volume form on a fundamental domain. This volume does not depend on the choice of the equivariant map because two equivariant maps are always equivariantly homotopic and the cohomology-class of the pull-back of the volume form is invariant under homotopy.

In [@D] this definition is extended to the case of a non compact cusped $3$-manifold $M$ (see Definitions [\[d vdr\]](#d vdr){reference-type="ref" reference="d vdr"} and [\[d pd\]](#d pd){reference-type="ref" reference="d pd"}). When $M$ is not compact, some problems of integrability arise if one tries to use the above definition of the volume of a representation. The idea of Dunfield for overcoming these difficulties is to use a particular (and natural) class of equivariant maps, called *pseudo-developing maps* (see Definition [\[d pd\]](#d pd){reference-type="ref" reference="d pd"}), that have a nice behavior on the cusps of $M$ allowing to control their volume. Concerning the well-definition of the volume, working with non-compact manifolds, two pseudo-developing maps in general are not equivariantly homotopic and in [@D] it is not proved that the volume of a representation does not depend on the chosen pseudo-developing map.

 

In this paper we show that the volume of a representation is well-defined even in the non-compact case, and we generalize to non-compact manifolds some results know in the compact case. We restrict to the orientable case. The paper is structured as follows.

In Sections [\[s uno\]](#s uno){reference-type="ref" reference="s uno"} and [\[s due\]](#s due){reference-type="ref" reference="s due"} we introduce the notion of pseudo-developing map for a given representation $\rho:\pi_1(M)\to$ Isom$^+(\ensuremath{\mathbb H}^3)$ and the notion of straightening of such a map.

In Section [\[s 3\]](#s 3){reference-type="ref" reference="s 3"} we prove that for each orientable cusped $3$-manifold $M$ and for each representation $\rho:\pi_1(M)\to$ Isom$^+(\ensuremath{\mathbb H}^3)$, the volume of $\rho$ is well-defined and depends only on $\rho$. The main theorems are:

 \
**Theorem [\[t vndpd\]](#t vndpd){reference-type="ref" reference="t vndpd"}** *Let $D_\rho$ and $F_\rho$ be two pseudo-developing maps for $\rho$. Then ${\rm vol}(D_\rho)={\rm vol}(F_\rho)$.*

 \
**Theorem [\[t vsd\]](#t vsd){reference-type="ref" reference="t vsd"}** *For any pseudo-developing map $D_\rho$ for $\rho$ we have ${\rm vol}(D_\rho)=$ ${\rm Strvol}(D_\rho)$.*

 

Roughly speaking, Theorem [\[t vsd\]](#t vsd){reference-type="ref" reference="t vsd"} says that the volume of $\rho$ can be computed by straightening any ideal triangulation of $M$ and then summing the volume of the straight version of the tetrahedra.

In Section [\[s qua\]](#s qua){reference-type="ref" reference="s qua"}, generalizing the techniques used for the proof of Theorem [\[t vsd\]](#t vsd){reference-type="ref" reference="t vsd"}, we show that the volume of a representation $\rho$ is bounded from above by the relative simplicial volume:

 \
**Theorem [\[t sv\]](#t sv){reference-type="ref" reference="t sv"}** *For all representations $\rho:\pi_1(M)\to$ Isom$^+(\ensuremath{\mathbb H}^3)$ we have $|{\rm vol}(\rho)|<v_3\cdot||(\overline M,\partial \overline M)||$, where $v_3$ is the volume of a regular ideal tetrahedron in $\ensuremath{\mathbb H}^3$.*

 

In Section [\[s r\]](#s r){reference-type="ref" reference="s r"} we prove the following rigidity theorem for representations of the fundamental group of a hyperbolic manifold:

 \
**Theorem [\[t ug\]](#t ug){reference-type="ref" reference="t ug"}** *Let M be a non-compact, complete, orientable hyperbolic $3$-manifold of finite volume. Let $\Gamma\cong\pi_1(M)$ be the sub-group of ${\rm PSL}(2,\ensuremath{\mathbb C})$ such that $M=\ensuremath{\mathbb H}^3/\Gamma$. Let $\rho:\Gamma\to$ PSL$(2,\ensuremath{\mathbb C})$ be a representation. If $|{\rm vol}(\rho)|={\rm vol}(M)$ then $\rho$ is discrete and faithful. More precisely there exists $\ensuremath{\varphi}\in{\rm PSL}(2,\ensuremath{\mathbb C})$ such that for any $\gamma\in\Gamma$ $$\rho(\gamma)=\ensuremath{\varphi}\circ\gamma\circ\ensuremath{\varphi}^{-1}.$$*

In Section [\[s cor\]](#s cor){reference-type="ref" reference="s cor"} we give some corollaries. In particular we show how from Theorem [\[t ug\]](#t ug){reference-type="ref" reference="t ug"} one can get a proof of Mostow's rigidity for non-compact manifolds (see [@P] and [@BCS] for a more general statement and a different proof):

 \
**Theorem [\[t mstw\]](#t mstw){reference-type="ref" reference="t mstw"} (Mostow's rigidity for non-compact manifold)** *Let $f:M\to N$ be a proper map between two orientable non-compact, complete hyperbolic $3$-manifolds of finite volume. Suppose that vol(M)=deg(f)vol(N). Then $f$ is properly homotopic to a locally isometric covering with the same degree as $f$.*

Other corollaries that can be useful for checking the hyperbolicity of a $3$-manifold are also shown.

2ex I would like to thank Carlo Petronio and Joan Porti for the very many very interesting conversations about this theme.
