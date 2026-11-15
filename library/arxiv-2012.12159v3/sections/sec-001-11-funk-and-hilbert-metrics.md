---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-001-11-funk-and-hilbert-metrics
section_title: "Funk and Hilbert metrics"
section_number: 1.1
pages: 2-2
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.991
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
The Hilbert metric in the interior of a convex set $K\subset\mathbb R^n$ is given by $$d^H_K(x,y)=\frac12 \log \frac{|ay||xb|}{|ax||yb|},$$ where $a,x,y,b$ appear in that order on the line through $x,y$ with $a,b\in\partial K$. It is evidently invariant under invertible projective maps. Hilbert discovered this metric while attempting to generalize the Beltrami-Klein model of hyperbolic geometry. It is moreover a *projective* metric, meaning that straight segments are geodesic. Hilbert's fourth problem [@hilbert_problems] asks for a construction of all projective metrics.

A different example of a projective metric, which we now recall, was discovered by Funk [@funk]. It is given by the non-symmetric distance function $$d^F_K(x,y)=\log\frac{|xb|}{|yb|},$$ where $b$ is the intersection of the ray $\vv{xy}$ with $\partial K$.

Various problems in Hilbert geometry have been raised and studied, notably those of volume growth [@colbois_verovic; @vernicos_polytopes; @berck_bernig_vernicos; @tholozan] and Gromov hyperbolicity [@benoist]. The Funk metric, on the other hand, has been for the most part denied the spotlight. In this paper we attempt to argue that at least from the perspectives of convex geometry and billiard dynamics, it is the Funk metric that is most natural to study.

Let $K\subset \mathbb{R}^n$ be a convex compact set with non-empty interior, placed in the affine space $\mathbb{R}^n$. The *Funk metric* on $K$ is arguably the simplest (non-symmetric) metric one can define naturally in its interior. Indeed, it is the non-reversible Finsler metric whose tangent unit ball at $x\in \mathop{\mathrm{int}}(K)$ is $B_xK=K\subset T_x\mathbb{R}^n=\mathbb{R}^n$, namely $K$ itself with the origin fixed at $x$.

The Funk and Hilbert metrics are closely related: $$d^H_K(x,y)=\frac12(d^F_K(x,y)+d^{F}_K(y,x)).$$ It is a remarkable fact that the symmetrization of the Funk metric is already projectively invariant. This hints that the Funk metric comes close to being projectively invariant itself. We shall pursue this idea along several paths.
