---
doc_id: arxiv-2109.00379v1
doc_title: "TWISTED NEUMANN–ZAGIER MATRICES"
section_id: sec-002-12-torsion-and-its-twisted-version
section_title: "Torsion and its twisted version"
section_number: 1.2
pages: 2-3
source_pdf: 2109.00379v1.pdf
source_sha256: f0c9bd89312a761c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.977
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
---
[]{#sub.tt label="sub.tt"}

Before discussing twisting matters further, let us recall a key motivating example. A basic invariant of a compact 3-manifold is the order of the torsion of its first homology. The behavior of this invariant for all cyclic covers of a knot complement is determined by a single Laurent polynomial, the Alexander polynomial. Explicitly, we have $$\label{TDn}
\left|\mathrm{tor}(H_1(M^{(n)};\mathbbm Z))\right| = \prod_{\omega^n=1} \Delta_K(\omega)$$

where $\Delta_K(t) \in \mathbbm Z[t^{\pm1}]$ is the Alexander polynomial of a knot $K \subset S^3$, $M^{(n)}$ is the $n$-fold cyclic cover of $M=S^3\setminus K$, and the right-hand side is the order of the torsion part of $H_1(M^{(n)};\mathbbm Z)$. This classical result connecting the torsion of the first homology to the Alexander polynomial (see e.g. [@Fox3 (6.3), p.417]) is deeply rooted in the idea that the Alexander polynomial is the torsion of the infinite cyclic cover of $M$ twisted by the abelianization map $\alpha:\pi_1(M) \rightarrow H_1(M;\mathbbm Z)=\mathbbm Z$. In other words, we have $$\boxed{
\label{basic}
\text{The twisted torsion determines the torsion of the cyclic covers} 
}$$

This idea has been extended in several directions.

Among them, one can define the torsion of a 3-manifold using interesting representations of its fundamental group. For example, when $M$ is a cusped hyperbolic 3-manifold, one can define a torsion using a (lifted) geometric $\mathrm{SL}_2(\mathbbm C)$-representation $\rho$ of its complement, or a symmetric power thereof. There are some technical difficulties that one must overcome, stemming from the fact that sometimes the corresponding chain complexes are not acyclic, hence the torsion depends on a choice of peripheral curves, as well as normalization issues, since the torsion is usually well-defined up to a sign. These issues have been addressed in detail by [@Porti:torsion; @DubYam; @Dunfield:twisted]. Among the several torsion invariants, we will be interested in the *adjoint (Reidemeister) torsion* $\tau_\gamma(M)$ of a one-cusped hyperbolic 3-manifold (such as a knot complement) using the adjoint representation $\mathrm{Ad}_\rho=\text{Sym}^2(\rho): \pi_1(M) \to \mathrm{SL}_3(\mathbbm C)$, where $\gamma$ is a fixed peripheral curve. The adjoint torsion $\tau_\gamma(M) \in F^\times/\pm$ is a nonzero element of the trace field $F$ of $M$, well-defined up to a sign [@Porti:torsion]. Just as in the case of the Alexander polynomial, there is a version of the *adjoint twisted Alexander polynomial* $\tau(M,\alpha,t) \in F[t^{\pm1}]/(\pm t^\mathbbm Z)$ (abbreviated by $\tau(M,t)$ when $\alpha$ is clear) defined in [@Wad94; @Dunfield:twisted; @DubYam] using an epimorphism $\alpha: \pi_1(M) \to \mathbbm Z$. Here, the ambiguity is given by multiplication by an element of $\pm t^\mathbbm Z:=\{\pm t^r \, | \, r \in \mathbbm Z\}$.

Two key properties of the adjoint twisted Alexander polynomial are the behavior under finite cyclic covers [@DubYam] $$\label{key1}
\tau(M^{(n)},t^n)=\prod_{\omega^n=1}\tau(M,\omega\, t)$$ and the relation with the adjoint torsion [@Yamaguchi], namely $$\label{key2}
\tau(M,1)=0, \qquad \left. \frac{d}{dt}\right|_{t=1}
\tau(M,t) = \tau_\lambda(M)$$ where $\lambda$ is the canonical longitude, i.e., the peripheral curve satisfying $\alpha(\lambda)=0$.
