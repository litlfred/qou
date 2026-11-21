---
doc_id: arxiv-math-0408210v3
doc_title: "A simple algebraic proof of the algebraic index theorem"
section_id: sec-005-24-the-feigin-felder-shoikhet-trace-density-map
section_title: "The Feigin-Felder-Shoikhet trace density map."
section_number: 2.4
pages: 11-12
source_pdf: 0408210v3.pdf
source_sha256: 16d5ccb83a86954f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.98
doc_brief: "A simple algebraic proof of the algebraic index theorem — In math.QA/0311303 B. Feigin, G. Felder, and B."
---
Let as above $V$ be a vector bundle of rank $N$ over the symplectic manifold ${\cal M}$ and $*$ be a star-product ([\[star\]](#star){reference-type="ref" reference="star"}) in the algebra $End_V(({\hbar}))$ . Then,

::: defi
A trace density map $trd$ is a ${\Bbb C}(({\hbar}))$-linear map $$trd\,:\, End_V(({\hbar})) \mapsto H^{2n}({\cal M})(({\hbar}))$$ vanishing on commutators $$trd(a * b - b * a)=0\,,
\qquad a,b \in End_V(({\hbar}))\,.$$
:::

We will show that if the star-product $*$ in $End_V(({\hbar}))$ is obtained via the Fedosov procedure [@F1] then the Feigin-Felder-Shoikhet cocycle ([\[Te\]](#Te){reference-type="ref" reference="Te"}) provides us with a natural trace density map.

Let as above $D$ be the Fedosov connection ([\[F-conn\]](#F-conn){reference-type="ref" reference="F-conn"}) and ${\lambda}$ be the isomorphism ([\[la\]](#la){reference-type="ref" reference="la"}). Since $\Theta_{2n}^N$ ([\[Te\]](#Te){reference-type="ref" reference="Te"}) is a cocycle of ${\mathfrak{g}}= {\mathfrak{gl}}_N({\cal W})$ relative to ${\mathfrak{h}}= {\mathfrak{gl}}_N\oplus {\mathfrak{sp}}_{2n}$ , we have the following well-defined map $$\label{Psi}
\Psi_{D}\,:\, End_V(({\hbar})) \mapsto {\Omega}^{2n}({\cal M})(({\hbar}))\,,
\qquad
\Psi_{D}(a)= \frac1{{\hbar}^n}\Theta^N_{2n} (A,\dots, A,{\lambda}(a))\,,$$ where $A\in {\Omega}^1(W(End_V))$ is the one-form entering the definition of the Fedosov connection $D$ ([\[F-conn\]](#F-conn){reference-type="ref" reference="F-conn"}) .

We assemble the required properties of the map $\Psi_D$ in the following

::: teo
[]{#main label="main"} With the above notations the following statements hold:\
**i)** If $V_1$ and $V_2$ are two vector bundles over ${\cal M}$ and $D_1,~ D_2$ are Fedosov connections on $W(End_{V_1})$ and $W(End_{V_2})$, respectively, then for any $a\in End_{V_1}$ $$\Psi_{D_1\oplus D_2} (a \oplus 0) = \Psi_{D_1}(a)\,,$$ where $0$ stands for the trivial endomorphism of $V_2$ .\
**ii)** For any pair of endomorphisms $a,b \in End_V(({\hbar}))$ $$\Psi_D(a * b - b * a)\in d {\Omega}^{2n-1}({\cal M})(({\hbar}))\,,$$ where $d$ is the De Rham differential.\
**iii)** Let $D$ and $\widetilde{D}$ be two equivalent Fedosov connections and $U\in I_N \oplus {\Gamma}(W^1(End_V))$ be the element establishing their equivalence in the sense of ([\[equiv1\]](#equiv1){reference-type="ref" reference="equiv1"}). Then for any $a\in End_V(({\hbar}))$ $$\Psi_{\widetilde{D}}({\sigma}(U^{-1}\circ {\lambda}(a)\circ U))
- \Psi_D (a)
\in d {\Omega}^{2n-1}({\cal M})(({\hbar}))\,,$$ where ${\sigma}$ is the projection ([\[sigma\]](#sigma){reference-type="ref" reference="sigma"}) and ${\lambda}$ is the isomorphism ([\[la\]](#la){reference-type="ref" reference="la"}).\
**iv)** For the identity endomorphism $I_N\in End_V$ $$\Psi_D(I_N) - \frac1{{\hbar}^n}Q_n(C(A,A), \dots, C(A,A))
\in d {\Omega}^{2n-1}({\cal M})(({\hbar}))\,,$$ where $Q_n\in ((S^n{\mathfrak{h}})^*)^{{\mathfrak{h}}}$ is the $n$-th component of the adjoint invariant form ([\[Qn\]](#Qn){reference-type="ref" reference="Qn"}), $A\in {\Omega}^1(W(End_V))$ is the one-form entering the definition of the Fedosov connection $D$ ([\[F-conn\]](#F-conn){reference-type="ref" reference="F-conn"}) and $C$ is the fiberwise "curvature" ([\[curvature\]](#curvature){reference-type="ref" reference="curvature"}) of the projection ([\[pr\]](#pr){reference-type="ref" reference="pr"}) .
:::

**Proof.** Statement $i)$ is obvious from the construction of the cocycle $\Theta^N_{2n}$ ([\[phi\]](#phi){reference-type="ref" reference="phi"}), ([\[tau\]](#tau){reference-type="ref" reference="tau"}), ([\[Te\]](#Te){reference-type="ref" reference="Te"}). Statements $ii)$, $iii)$, and $iv)$ are proven in [@FFS] for the case when the bundle $V$ is trivial. Statements $ii)$ and $iii)$ follow from the fact $\Theta^N_{2n}$ is a cocycle relative to ${\mathfrak{h}}= {\mathfrak{gl}}_N\oplus {\mathfrak{sp}}_{2n}$ and statement $iv)$ is a consequence of ([\[FFS\]](#FFS){reference-type="ref" reference="FFS"}) . These results of [@FFS] are generalized to the non-trivial bundle $V$ in a straightforward manner since we always deal with the Lie algebra cochains relative to ${\mathfrak{h}}= {\mathfrak{gl}}_N\oplus {\mathfrak{sp}}_{2n}$ . $\Box$

As an immediate consequence of this theorem we get that

::: cor
If $*$ is the star-product in $End_V(({\hbar}))$ obtained via the isomorphism ${\lambda}$ ([\[la\]](#la){reference-type="ref" reference="la"}) then $$\label{trd}
trd(a) = [\Psi_D(a)] \,:\,
End_V(({\hbar})) \mapsto H^{2n}({\cal M})(({\hbar}))$$ is a trace density map.
:::

In what follows we refer to ([\[trd\]](#trd){reference-type="ref" reference="trd"}) as the Feigin-Felder-Shoikhet (FFS) trace density map.
