---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-041-a1-introductory-remarks
section_title: "A.1. Introductory remarks"
section_number: null
pages: 36-37
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
Before starting formal definitions in the next subsection we  consider here a slightly simplified situation which should help to make the general picture clearer. Let $(\Gamma,Z,\Omega)$ be a BPS structure. Given a basis $(\gamma_1,\cdots,\gamma_n)\subset \Gamma$ there is a corresponding cone
\[\Gamma^\oplus=\big\{\gamma =\sum  d_i \gamma_i \text{ with }  d_i\in \bZ_{\geq 0}\big\}\subset \Gamma,\]
whose elements we call positive. We call a class $\gamma\in \Gamma$ negative if $-\gamma$ is positive.

Let us  assume that we can find a basis such that every active class  is either positive or negative, and further that all positive classes $\gamma\in \Gamma$ satisfy $\Im Z(\gamma)>0$. These assumptions are always satisfied  for BPS structures arising from stability conditions on quivers.
 Let us also temporarily ignore the difference between the tori $\bT_\pm$.

The co-ordinate ring $\bC[\bT]$ can be identified with the algebra of Laurent polynomials
\[\bC[\bT]=\bC[y_1^{\pm 1}, \cdots, y_n^{\pm n}],\]
and a regular automorphism of $\bT$ corresponds to an automorphism of this algebra. The element $\DT(\ell)$ corresponding to an active ray $\ell\subset \bC^*$ does not  in general define an element of $\bC[\bT]$ however,  since it could an infinite sum of characters.
If a ray $\ell\subset \bC^*$ lies in the upper half-plane, the series $\DT(\ell)$  defines an element of the power series ring
\[\bC[[\bT]]=\bC[[y_1, \cdots, y_n]],\]
which is a Poisson algebra in  the same way as $\bC[\bT]$. 
We can then  define an algebra automorphism
\[\bS(\ell)^*=\exp \{\DT(\ell),-\}\in \Aut  \bC[[\bT]],\]
and  interpret the wall-crossing formula \eqref{wcw} in the group of  automorphisms of  $\bC[[\bT]]$, at least for sectors $\Delta\subset \bC^*$ contained in the upper half-plane.

In what follows we will modify this  procedure  in two ways. Firstly, to avoid the assumption on active classes we will work with completions of $\bC[\bT]$ defined by more general cones in $\Gamma$. Secondly, note that if the form $\<-,-\>=0$ is trivial, the  automorphisms $\bS(\ell)^*$ as defined above will all be identity maps, and the wall-crossing formula will become vacuous. One way to  avoid this problem would be to force the form $\<-,-\>$ to be non-degenerate by  passing to the double BPS structure as in Section \ref{double}.  Instead, we will  formulate the wall-crossing formula in a group defined abstractly by using the Baker-Campbell-Hausdorff formula to formally exponentiate elements of $\bC[[\bT]]$.
