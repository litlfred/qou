---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-004-14-expectations
section_title: "Expectations"
section_number: 1.4
pages: 6-6
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 1.0
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sub.ought label="sub.ought"}

We may pose some questions and conjectures about the 1-loop invariant $\tau_{\mathcal{T}}$ and the structure of the set $\mathcal X_{\rho_0}$. Let us begin with two questions whose answer is unfortunately unknown.

::: question
[]{#que.can label="que.can"} Is $\mathcal X_{\rho_0}$ connected by 2--3 moves?
:::

::: question
[]{#que.constanttau label="que.constanttau"} Is $\tau_{\mathcal{T}}$ constant on the set $\mathcal X_{\rho_0}$?
:::

Clearly, a positive answer to the first question implies a positive answer to the second.

Despite the unknown answer to the above questions, with additional effort we can still define a distinguished component of $\mathcal X_{\rho_0}$, and thus obtain a topological invariant of $M$. Namely, let $\mathcal X^{\mathrm{EP}}_M
\subset \mathcal X_{\rho_0}$ denote the subset that consists of regular refinements of the canonical (Epstein-Penner) ideal cell decomposition of $M$ [@EP]. $\mathcal X^{\mathrm{EP}}_M$ is canonically associated to a cusped hyperbolic manifold $M$. A detailed description of $\mathcal X^{\mathrm{EP}}_M$ is given in [@GHRS Sec.6]. $\mathcal X^{\mathrm{EP}}_M$ is a finite set that generically consists of a single element. In Section [\[sub.EP\]](#sub.EP){reference-type="ref" reference="sub.EP"} we will show the following.

::: proposition
[]{#prop.EP label="prop.EP"} $\mathcal X^{\mathrm{EP}}_M$ lies in a connected component of $\mathcal X_{\rho_0}$. Consequently, the value of $\tau_{\mathcal{T}}$ on $\mathcal X^{\mathrm{EP}}_M$ is a topological invariant $\tau_M$ of $M$.
:::

Admittedly, it would be more natural to show that $\tau_\mathcal{T}$ is constant on all of $\mathcal X_{\rho_0}$. Proposition [\[prop.EP\]](#prop.EP){reference-type="ref" reference="prop.EP"} appears to be an artificial way to construct a much needed topological invariant of cusped hyperbolic 3-manifolds.

Our next conjecture compares our torsion $\tau_M$ with the nonabelian Reidemeister torsion $\tau^{\mathrm{R}}_M$ of $M$ with respect to the meridian defined in [@Po; @Db].

::: conjecture
[]{#conj.1loop label="conj.1loop"} For all hyperbolic knot complements we have $\tau^{\mathrm{R}}_M=\pm \tau_{M}$.
:::

Numerical evidence for the above conjecture is presented in Appendix [\[app.compute\]](#app.compute){reference-type="ref" reference="app.compute"} using Dunfield's computation of $\tau^{\mathrm{R}}_M$ via `SnapPy` [@DFJ]. Observe that both sides of the equation in Conjecture [\[conj.1loop\]](#conj.1loop){reference-type="ref" reference="conj.1loop"} are algebraic numbers (defined up to a sign) that are elements of the invariant trace field of $M$. Moreover, if $M$ has a regular ideal triangulation with $N$ ideal tetrahedra and its fundamental group is generated with $r$ elements, then $\tau_M$ and $\tau^{\mathrm{R}}_M$ are essentially given by the determinant of square matrices of size $N$ and $3 r-3$, respectively. It is still unclear to us how to relate these two matrices or their determinants.

By definition, $\tau^{\mathrm{R}}_M \in E_M^*$. Thus, a mild but important corollary of Conjecture [\[conj.1loop\]](#conj.1loop){reference-type="ref" reference="conj.1loop"} is that $\tau_M$ is nonzero. This is a crucial ingredient, necessary for the definition of the higher loop invariants $S_{M,n}$ using perturbation theory.
