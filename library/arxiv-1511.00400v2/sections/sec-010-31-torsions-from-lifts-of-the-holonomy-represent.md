---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-010-31-torsions-from-lifts-of-the-holonomy-represent
section_title: "Torsions from lifts of the holonomy representation"
section_number: 3.1
pages: 16-18
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.976
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

### Torsions for closed 3-manifolds

The following theorem is a particular case of Raghunathan's. With other cohomology results, it is discussed in Appendix [\[sec:cohomology\]](#sec:cohomology){reference-type="ref" reference="sec:cohomology"}. In particular the following theorem is stated in Corollary [\[cor:acyclc\]](#cor:acyclc){reference-type="ref" reference="cor:acyclc"}.

::: thm
[]{#thm:RaghunathanClosed label="thm:RaghunathanClosed"} Let $M^3$ be a closed, orientable, hyperbolic 3-manifold. Then any lift of its holonomy representation is acyclic.
:::

With Mostow rigidity, this yields immediately a topological invariant of the spin manifold.

::: definition
[]{#defn:tor2closed label="defn:tor2closed"} Let $M^3$ be a compact, oriented, hyperbolic 3-manifold with spin structure $\sigma$. The torsion of $(M^3,\sigma)$ is defined as $$\label{eqn:tau}
 \tau(M^3,\sigma):=\operatorname{tor}(M^3, \varrho_\sigma)\in \mathbb{C}^*$$ where $\varrho_\sigma=\widetilde{\mathrm{hol}}$ is the lift of the holonomy $\mathrm{hol}$ corresponding to the spin structure $\sigma$.
:::

::: remark
There is no sign indeterminacy, i.e. it is a well defined complex number, because $\varrho_\sigma$ is a representation in $\mathbb C^2$, which is even dimensional, and $\chi(M^3)=0$, see Remark [\[rem:sign\]](#rem:sign){reference-type="ref" reference="rem:sign"}.
:::

Here are some of its properties.

::: prop
[]{#prop:properties label="prop:properties"} The torsion $\tau(M^3,\sigma)$ in Definition [\[defn:tor2closed\]](#defn:tor2closed){reference-type="ref" reference="defn:tor2closed"} has the following properties:

(a) []{#item:topinvariance label="item:topinvariance"} It is a topological invariant of the spin manifold $(M^3,\sigma)$.

(b) []{#item:sensitive label="item:sensitive"} There are examples of manifolds $M^3$ with two spin structures $\sigma$ and $\sigma'$ such that $\tau(M^3,\sigma)\neq \tau(M^3,\sigma')$.

(c) []{#item:conj label="item:conj"} Let $\overline M^3$ denote the manifold $M^3$ with opposite orientation. If one changes the orientation and the spin structure accordingly as in Proposition [\[prop:spin\]](#prop:spin){reference-type="ref" reference="prop:spin"}, then the torsion is the complex conjugate $$\tau(\overline M^3,\overline \sigma)=     \overline{   \tau(M^3,\sigma)}.$$

(d) []{#item:mutation label="item:mutation"} Let $(M^3)^\mu$ denote the result of mutation. If $\sigma^\mu$ denotes the corresponding spin structure as in Remark [\[rem:mutation\]](#rem:mutation){reference-type="ref" reference="rem:mutation"}, then $$\tau((M^3)^\mu, \sigma^\mu) = \tau(M^3,\sigma).$$

(e) []{#item:dense label="item:dense"} Let $M^3$ be an oriented hyperbolic manifold with one cusp and with spin structure $\sigma$. The set of modules of the torsions obtained by Dehn filling on $M^3$, $\vert \tau(M^3_{p/q},\sigma)\vert$ so that $\sigma$ extends to $M^3_{p/q}$, is dense in the interval $$\left[ \frac14\left\vert \tau(M^3,\sigma)\right\vert,+\infty\right).$$
:::

Item [\[item:topinvariance\]](#item:topinvariance){reference-type="eqref" reference="item:topinvariance"} follows from uniqueness of the hyperbolic structure, by Mostow rigidity. To prove [\[item:sensitive\]](#item:sensitive){reference-type="eqref" reference="item:sensitive"} it suffices to compute an example, this is done in Corollary [\[cor:differentspin\]](#cor:differentspin){reference-type="ref" reference="cor:differentspin"}. Item [\[item:conj\]](#item:conj){reference-type="eqref" reference="item:conj"} is straightforward from Proposition [\[prop:spin\]](#prop:spin){reference-type="ref" reference="prop:spin"}. Item [\[item:mutation\]](#item:mutation){reference-type="eqref" reference="item:mutation"} is proved in [@MFP12c]. Finally, [\[item:dense\]](#item:dense){reference-type="eqref" reference="item:dense"} is proved later when discussing cusped manifolds, as this will follow immediately from a surgery formula.

Item [\[item:dense\]](#item:dense){reference-type="eqref" reference="item:dense"} shows that this torsion is not obviously related to the hyperbolic volume. The following theorem, a particular case of [@BV13 Thm. 4.5], finds a relation (we use the convention of torsion opposite to [@BV13]):

::: thm
[]{#thm:BV label="thm:BV"} Let $M^3$ be a compact oriented hyperbolic 3-manifold. Assume that $M_n^3\to M^3$ is a sequence of coverings such that the injectivity radius of $M_n^3$ converges to infinity. Then $$\lim_{n\to\infty} 
\frac{\log\vert \tau(M_n^3,\sigma)\vert}{ \operatorname{vol}(M_n^3) } = 
\frac{11}{12 \pi} .$$ Equivalently; $$\lim_{n\to\infty} \frac{\log\vert \tau(M_n^3,\sigma)\vert} {\deg ( M_n^3\to M^3) 
} = \frac{11}{12 \pi} \operatorname{vol}(M^3) .$$
:::

This theorem relies on analytic torsion and on $L^2$-torsion, as $\frac{-11}{12 
\pi}$ is the $L^2$-torsion of $\mathbb H^3$. The proof uses the $L^2$-Laplacian of hyperbolic space, and it is based on approximations of averages of the trace of the difference of heat kernels, see Equation [\[eqn:traceheatkernel\]](#eqn:traceheatkernel){reference-type="eqref" reference="eqn:traceheatkernel"}. They require the notion of strong acyclicity (the property in Theorem [\[thm:strong_acyclicity\]](#thm:strong_acyclicity){reference-type="ref" reference="thm:strong_acyclicity"}) to avoid eigenvalues of the Laplacian approaching to zero. This has been generalized in [@ABBGNRS], in particular without requiring that the $M_n^3$ are coverings. See also [@MuP14].
