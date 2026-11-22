---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-023-62-the-phase-function
section_title: "The phase function"
section_number: 6.2
pages: 14-14
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 1.0
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
We now introduce the *phase function*: $$\theta(z,w) = \frac{ Q(w) - Q(z,w)}{w-z},\qquad z\ne w.$$ Clearly, the phase function $\theta(z,w)$ is holomorphic in $z$ and real-analytic in $w$. We extend it by continuity to the diagonal: $\theta(z, z):=\partial_z Q(z)$. In terms of the phase function, our assumption [\[Qtaylor\]](#Qtaylor){reference-type="eqref" reference="Qtaylor"} asks that $$\begin{gathered}
 2\mathop{\mathrm{Re}}[(z-w)\theta(z,w)] =2\mathop{\mathrm{Re}}Q(z,w)-2Q(w)
\\
\leq Q(z)-Q(w)
-\frac12 \varDelta Q(z) |w-z|^2,\qquad z,w \in \mathbb{D}(z_0,r).
\label{Qtaylor2}
\end{gathered}$$

It will be convenient we record here some Taylor expansions which will be needed later on. In view of Taylor's formula, we have $$Q(w)=Q(w,w)=\sum_{j=0}^{+\infty}\frac{1}{j!}(w-z)^j\partial_z^j Q(z,w),$$ and as consequence, $$\theta(z,w) =\frac{Q(w)-Q(z,w)}{w-z}=\sum_{j=0}^{+\infty}\frac{1}{(j+1)!}
(w-z)^j\partial_z^{j+1}Q(z,w),
\label{eq-4.19}$$ so that $$\bar\partial_w\theta=
\sum_{j=0}^{+\infty}\frac{1}{(j+1)!}(w-z)^j\partial_z^{j+1}\bar\partial_w Q(z,w),
\label{eq-4.19.1}$$ and $$\partial_w\theta=
\sum_{j=0}^{+\infty}\frac{j+1}{(j+2)!}(w-z)^{j}\partial_z^{j+2} Q(z,w).
\label{eq-4.19.2}$$
