---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-012-312-torsions-for-closed-3-manifolds
section_title: "Torsions for closed 3-manifolds"
section_number: 3.1.2
pages: 17-18
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 1.0
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
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
