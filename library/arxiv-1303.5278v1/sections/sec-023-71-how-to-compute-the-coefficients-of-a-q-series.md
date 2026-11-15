---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-023-71-how-to-compute-the-coefficients-of-a-q-series
section_title: "How to compute the coefficients of a q-series"
section_number: 7.1
pages: 43-44
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.945
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sub.overview.compute label="sub.overview.compute"}

In this section we will explain a general method to compute the coefficients of a $q$-series which is given by a multi-dimensional sum of some basic $q$-series. The idea is simple, but the effective aspects of it are tricky and were explained to the first author by D. Zagier. The method is applied in forthcoming work [@GV] which computes the coefficients of the stabilization of the coloured Jones polynomial of an alternating knot [@GL2].

Fix a 1-efficient ideal triangulation $\mathcal{T}$ with $n$ tetrahedra of a 1-cusped hyperbolic manifold $M$ and an oriented multi-curve $\varpi$ on $\partial M$. The index $I_{\mathcal{T}}(\varpi)(q) \in \mathbb Z((q^{1/2}))$ is given by a convergent $(n-1)$-dimensional sum over the integers of a summand that depends on the angle structure equation matrices of $\mathcal{T}$; see Equation [\[eq.indT\]](#eq.indT){reference-type="eqref" reference="eq.indT"}. The summand of $I_{\mathcal{T}}(\varpi)$ is a product of tetrahedron indices (one per tetrahedron of $\mathcal{T}$) of linear forms in $\boldsymbol{k}=(k_1, \ldots, k_{n-1}) \in \mathbb Z^{n-1}$ and the turning number vectors $(a_{\varpi}|b_{\varpi})$ of $\varpi$.

The building block of the summand is the tetrahedron index $I_\Delta$, whose degree (i.e., minimum degree with respect to $q$) is a piecewise quadratic function on $\mathbb{R}^2$; see Section [\[sub.degI\]](#sub.degI){reference-type="ref" reference="sub.degI"}. By a *piecewise quadratic function* on $\mathbb R^m$, we mean that there exists a partition $\mathcal F$ of $\mathbb R^{m}$ into a finite number of chambers whose boundaries are rational polyhedral cones such that the restriction of the function to each chamber is given by a quadratic polynomial. It follows that for fixed $\varpi$, the degree $\delta(\varpi,\boldsymbol{k})$ of the summand in [\[eq.indT\]](#eq.indT){reference-type="eqref" reference="eq.indT"} is a piecewise quadratic function defined on a partition $\mathcal F_{\mathcal{T}}$ of $\mathbb R^{n-1}$. In a later publication, we will explain how to compute $\mathcal F_{\mathcal{T}}$ directly from $\mathcal{T}$. A priori, $\mathcal F_{\mathcal{T}}$ need not be a fan in $\mathbb R^{n-1}$ as the cones in the partition may not be convex.

Since $\mathcal{T}$ is 1-efficient, it follows that its index $I_{\mathcal{T}}(\varpi)(q)$ is a convergent series. In other words, the degree of the summand is a proper function on $\mathbb Z^{n-1}$. Thus, for fixed $\varpi$ and every half-integer $N$, the set $\{\boldsymbol{k}\in \mathbb Z^{n-1} \,: \delta(\varpi,\boldsymbol{k}) \leq N \}$ is finite. To compute the index of $\mathcal{T}$, we need to compute bounds on this finite set. Since $\delta$ is convex and piecewise quadratic, it follows that to bound $\delta(\varpi,\boldsymbol{k})$, it suffices to bound the restriction of $\delta(\varpi,\boldsymbol{k})$ to an arbitrary ray $\rho = \{ k' \rho_0: k' \in \mathbb N\}$ of $\mathcal F_T$. Now $\delta(\varpi,k' \rho_0)$ is a quadratic function of $k' \in \mathbb N$, and we obtain sharp bounds for $k_i$ typically of the form $k_i=O(\sqrt{N})$ and *exceptionally* of the form $k_i=O(N)$. The latter happens when $\delta$ has linear growth on some ray of $\mathcal F_T$. These directions of linear growth (also observed in [@GL2] in the context of stabilization of the coloured Jones function) are computationally costly. For an example, see the case of the knot $6_1$ discussed below.

The bounds for $k_i$ discussed above are rigorous and sharp, and work well for $n=2$ and $n=3$ tetrahedra. However, they quickly become inefficient when $n$ increases (e.g. $n=9$). The better way to proceed for larger $n$, as was explained to us by D. Zagier and is applied successfully in [@GV], is to use *iterated summation*. In the examples shown below for $n=2$ and $n=3$ iterated summation is not needed. For simplicity, we focus on 1-cusped manifolds and their index for $[\varpi]=0 \in H_1(\partial M;\mathbb{Z})$. The data presented below are available from [@Ga:data].

::: rmk
[]{#rem.same.index label="rem.same.index"} If two 1-cusped hyperbolic 3-manifolds $M$ and $M'$ have 1-efficient ideal triangulations $\mathcal{T}$ and $\mathcal{T}'$ with equal angle structure matrices, then $I_{\mathcal{T}}(0)(q)=I_{\mathcal{T}'}(0)(q)$. For example, $M$ and $-M$ have such triangulations, where $-M$ denotes the orientation reversed cusped hyperbolic manifold. Also, $M_{\phi}$ and $M_{-\phi}$ have such triangulations for a pseudo-Anosov homeomorphism $\phi$ of a once punctured torus, where $M_{\phi}$ denotes the mapping torus of $\phi$.
:::
