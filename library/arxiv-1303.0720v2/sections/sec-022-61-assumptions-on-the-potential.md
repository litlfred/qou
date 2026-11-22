---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-022-61-assumptions-on-the-potential
section_title: "Assumptions on the potential"
section_number: 6.1
pages: 13-14
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.903
latex_coverage_ratio: 0.933
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
[]{#subsec-assQ label="subsec-assQ"}

We fix a $C^\infty$-smooth simply connected bounded domain $\Omega$. The potential $Q:\bar\Omega\to{\mathbb R}$ is assumed real-analytically smooth. This assumption simplifies the choice of polarization $Q(z,w)$, as there is then a unique choice which is holomorphic in $(z,\bar w)$ locally near the diagonal $z=w$.

Fix an arbitrary point $z_0 \in \Omega$. We will carryout a local analysis of the kernels $K_m(z,w)$, where $z, w \in \mathbb{D}(z_0, r)\Subset\Omega$. We will assume that the radius $r$ and the potential $Q$ meet the following additional requirements (A:i)--(A:iv):

(A:i) $Q$ is real-analytic in ${\mathbb D}(z_0,r)$ and $\varDelta Q(z) \ge \epsilon_0$ on ${\mathbb D}(z_0,r)$, for some positive constant $\epsilon_0$ (which we assume to be as big as possible).

(A:ii) There exists a local polarization of $Q$ in ${\mathbb D}(z_0,r)$, i.e. a function $Q: {\mathbb D}(z_0,r) \times {\mathbb D}(z_0,r) \to {\mathbb C}$ which is holomorphic in the first variable and conjugate-holomorphic in the second variable, with $Q(z,z)=Q(z)$.

(A:iii) For $z, w \in{\mathbb D}(z_0, r)$, we have $\partial_z \bar \partial_w Q(z,w)\neq0$ and $\bar\partial\theta(z,w)\neq0$ (this is possible because of condition (A:i)). Here, $\theta$ is the phase function, which is defined below.

(A:iv) By Taylor's formula, we have that $$2\mathop{\mathrm{Re}}Q(z,w) - Q(w)- Q(z) = -\varDelta Q(z) |w-z|^2 + 
\mathrm{O}(|z-w|^3).$$ We then pick $r>0$ so small that $$2\mathop{\mathrm{Re}}Q(z,w) - Q(w)- Q(z) \leq -\frac12 \varDelta Q(z) |w-z|^2,
\qquad z,w \in \mathbb{D}(z_0,r).
\label{Qtaylor}$$
