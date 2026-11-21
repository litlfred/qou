---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-011-31-torsions-from-lifts-of-the-holonomy-represent
section_title: "Torsions from lifts of the holonomy representation"
section_number: 3.1
pages: 16-17
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.992
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
Let $M^3$ be a closed, orientable hyperbolic 3-manifold. Its holonomy representations is unique up to conjugation: $$\operatorname{hol}\colon \pi_1 M^3\to \operatorname{Isom}^+(\mathbb H^3)\cong 
\operatorname{PSL}_2(\mathbb{C}).$$ To get a natural representation in a linear group one can lift the holonomy to $\mathrm{SL}_2(\mathbb{C})$. Such a lift always exists [@Culler86] and it depends naturally on a choice of a spin structure, because the group of isometries is naturally identified with the frame bundle of $\mathbb H^3$ and $\mathrm{SL}_2(\mathbb{C})$ with the spin bundle, cf. [@MFP14].

### Lifts of the holonomy

There is natural action of $H^1(M^3 ; \mathbb{Z}/2\mathbb{Z})$ on the set of lifts $\varrho$ to $\mathrm{SL}(2,\mathbb{C})$ of the holonomy representation: viewing $H^1(M^3 ; \mathbb{Z}/2\mathbb{Z})$ as morphisms from $\pi_1M^3$ to $\mathbb{Z}/2\mathbb{Z}$, a morphism $\epsilon\colon\pi_1M^3\to \mathbb{Z}/2\mathbb{Z}$ maps a representation $\varrho$ to $(-1)^\epsilon \varrho$.

::: prop
[]{#prop:spin label="prop:spin"}

(a) []{#item:affine label="item:affine"} There is a natural bijection between the set of lifts of the holonomy representation and the set of spin structures.

    This is an isomorphism of affine spaces on the vector space $H^1(M^3 ; \mathbb{Z}/2\mathbb{Z})$.

(b) []{#item:cplxconj label="item:cplxconj"} If $M^3$ and $\overline M^3$ are the same manifold with opposite orientations, then there is a natural bijection between spin structures on $M^3$ and on $\overline M^3$ so that lifts of the holonomy correspond to complex conjugates.
:::

Item [\[item:affine\]](#item:affine){reference-type="eqref" reference="item:affine"} can be found essentially in [@Culler86], see also [@MFP14].

A quick way of proving Item [\[item:cplxconj\]](#item:cplxconj){reference-type="eqref" reference="item:cplxconj"} is using the bijection of Item [\[item:affine\]](#item:affine){reference-type="eqref" reference="item:affine"}, knowing that complex conjugation in $\mathrm{PSL}_2(\mathbb{C})$ is the result of composing with an isometry that changes the orientation of $\mathbb H^3$. On the other hand, this bijection can be constructed explicitly from frame bundles and spin, but details are not given here.

For a spin structure $\sigma$, the corresponding lift of the holonomy, according to Proposition [\[prop:spin\]](#prop:spin){reference-type="ref" reference="prop:spin"}[\[item:affine\]](#item:affine){reference-type="eqref" reference="item:affine"}, will be denoted by $$\varrho_{\sigma}\colon \pi_1 M^3\to \mathrm{SL}_2(\mathbb{C}).$$

The behavior of torsion by mutation is also interesting. Mutation is the operation that consists in cutting along a genus two surface, applying the hyperelliptic involution and gluing again. Notice that one does do not require the surface to be essential, thus the genus two surface can be replaced by a (properly embedded) torus with one or two punctures or a sphere with three or four punctures (in particular a Conway sphere for a knot exterior). See [@DGST12].

Let $(M^3)^\mu$ denote the result of mutation, by [@Ruberman87] $(M^3)^\mu$ is hyperbolic with the same volume as $M^3$.

::: remark
[]{#rem:mutation label="rem:mutation"} There is a natural correspondence between the spin structures on $M^3$ and the spin structures on $(M^3)^\mu$.
:::

Here is an explanation of the remark, using the natural bijection between lifts of the holonomy and spin structures in Proposition [\[prop:spin\]](#prop:spin){reference-type="ref" reference="prop:spin"}. Assume that $\Sigma$ separates $M^3$ in two components $M_1$ and $M_2$. Then $$\pi_1M^3\cong \pi_1M_1 *_{\pi_1\Sigma}\pi_1 M_2.$$ If $\varrho_\sigma\colon\pi_1(M^3)\to \mathrm{SL}_2(\mathbb{C})$ is a lift of the holonomy, then $\varrho_{\sigma(\mu)}\colon\pi_1 (M^3)^\mu\to \mathrm{SL}_2(\mathbb{C})$ is defined so that $\varrho_{\sigma(\mu)}   \vert_{\pi_1 M_1}=\varrho_\sigma\vert_{\pi_1 M_1}$ and $\varrho_{\sigma(\mu)}\vert_{\pi_1 M_2}$ is conjugate to $\varrho_\sigma\vert_{\pi_1 M_2}$ by a matrix in $\mathrm{PSL}_2(\mathbb{C})$ that realizes the involution $\mu$ on $\Sigma$. When $\Sigma$ does not separate, then the construction is similar from the presentation of $\pi_1M^3$ as HNN-extension.
