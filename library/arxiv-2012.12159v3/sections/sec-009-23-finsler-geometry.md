---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-009-23-finsler-geometry
section_title: "Finsler geometry"
section_number: 2.3
pages: 8-8
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 1.0
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
A *non-reversible Finsler manifold* $(M,\phi)$ is a smooth manifold equipped with a function $\phi :TM\setminus \underline 0\to [0,\infty)$, which restricts to a non-symmetric norm on each tangent space. The assumed smoothness of $\phi$ depends on the problem at hand.

The tangent unit ball at $x$ is $B_xM=\{v\in T_xM: \phi(x,v)\leq 1\}$, and the cotangent ball is $B_x^*M=(B_xM)^o\subset T_x^*M$. The co-ball bundle is $B^*M=\cup_{x\in M}B_x^*M$.

The *Holmes-Thompson* volume is the measure $\mu^{HT}:=\frac{1}{\omega_n}\pi_*(\mathop{\mathrm{vol}}_{2n}|_{B^*M})$, where $\mathop{\mathrm{vol}}_{2n}$ is the symplectic volume on $T^*M$, and $\pi:T^*M\to M$ the natural projection.

By $\mathop{\mathrm{Dens}}(V)$ we denote the one-dimensional real line of Lebesgue measures, or *densities*, on $V$. A measure on a manifold can be identified with a section of the line bundle $\mathop{\mathrm{Dens}}(TM)$. The Holmes-Thompson measure has $\mu^{HT}_x(B_xM)=\frac{1}{\omega_n}|B_xM||B^*_xM|$. For an illuminating discussion of the Holmes-Thompson volume in Finsler geometry, which plays a central role in this work, we refer to [@alvarez_thompson; @alvarez_berck].

Both Hilbert and Funk geometries are Finsler, and we refer to [@hilbert_handbook] for a comprehensive account. Let us quote a few facts we will use.

The Funk metric of $K\subset\mathbb{R}^n$ is given by the Finsler norm $\phi(x,v)=\|v\|_{K-x}$. The *outward ball* in the Funk geometry of $K\subset\mathbb{R}^n$, of radius $r$ and centered at $q$, is the set $$B_r^F(q, K)=\{x\in \mathop{\mathrm{int}}(K): d^F_K(q,x)\leq r.\}$$ Extrinsically, $B^F_r(q, K)=q+(1-e^{-r})(K-q)$.

Given a compact domain $\Omega\subset \mathop{\mathrm{int}}(K)$ with piecewise smooth boundary, one may, following [@gutkin_tabachnikov], consider the Funk billiard map inside $\Omega$ by requiring that whenever $x,y,z\in\partial \Omega$ are consecutive points in a billiard orbit, then $$\frac{\partial}{\partial y}(d^F(x,y)+d^F(y,z))=0.$$
