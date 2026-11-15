---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction"
section_id: sec-014-31-rank-1-colouring-of-edges-and-the-canonical-s
section_title: "Rank-1 colouring of edges and the canonical surface"
section_number: 3.1
pages: 17-18
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.989
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low"
---
[]{#subsec:colouring label="subsec:colouring"}

We have $M= \widehat{M}\setminus \widehat{M}^{(0)},$ and thus Lefschetz duality gives a natural isomorphism $$D_M\co H_2(M; \mathbb{Z}_2) 
\cong H^1(\widehat{M}, \widehat{M}^{(0)}; \mathbb{Z}_2).$$ An element $\varphi \in H^1(\widehat{M}, \widehat{M}^{(0)}; \mathbb{Z}_2)$ can be viewed as an assignment of values $0$ or $1$ to each edge in the triangulation such that in each triangle the sum of all values at its edges equals zero modulo two. We say that the edge $e$ is *$\varphi$--even* if $\varphi(e) = 0$ and *$\varphi$--odd* if $\varphi(e) = 1.$ It follows that a tetrahedron falls into one of the following categories, which are illustrated in Figure [1](#fig:Z2-homology class){reference-type="ref" reference="fig:Z2-homology class"}:

-   Type $\Delta_{\mathfrak{q}}$: A pair of opposite edges are $\varphi$--even, all others are $\varphi$--odd.

-   Type $\Delta_{\mathfrak{t}}$: The three edges incident to a vertex are $\varphi$--odd, all others are $\varphi$--even.

-   Type $\Delta_{\emptyset}$: All edges are $\varphi$--even.

![Tetrahedra of type $\Delta_{\mathfrak{q}},$ $\Delta_{\mathfrak{t}}$ and $\Delta_{\emptyset}.$ Grey and dashed edges are $\varphi$--even. []{#fig:Z2-homology class label="fig:Z2-homology class"}](tetrahedra_1.pdf){#fig:Z2-homology class height="2.4cm"}

If $\varphi$ is non-trivial, one obtains a unique normal surface, $S_\varphi = S_\varphi(\mathcal{T}),$ with respect to $\mathcal{T}$ by introducing a single vertex on each $\varphi$--odd edge. This surface is disjoint from the tetrahedra of type $\Delta_{\emptyset};$ it meets each tetrahedron of type $\Delta_{\mathfrak{t}}$ in a single triangle meeting all $\varphi$--odd edges; and each tetrahedron of type $\Delta_{\mathfrak{q}}$ in a single quadrilateral dual to the $\varphi$--even edges. Moreover, $S_\varphi$ is Lefschetz dual to $\varphi$ and is termed the *canonical (normal) surface dual to $\varphi.$* Given $0 \neq c \in H_2(M; \mathbb{Z}_2)$ we also write $S_c = S_{D_M(c)}$ and call $S_c$ the *canonical (normal) representative* of $c.$

::: lemma
[]{#lem:chi bounds norm for canonical label="lem:chi bounds norm for canonical"} Let $M$ be a cusped hyperbolic 3--manifold with ideal triangulation $\mathcal{T}$ and $0 \neq c \in H_2(M; \mathbb{Z}_2).$ Then $|| \ c \ || \le \chi_{-} (S_c) = - \chi (S_c).$
:::

::: proof
*Proof.* It follows from the construction and definitions that $[S_c]=c$ and we need to prove the equality in the statement. For this, it suffices to show that no component of $S_\varphi$ is a sphere or a projective plane. Since $M$ is irreducible and not $\mathbb{R}P^3,$ no component can be a projective plane. Since each component of $S_\varphi$ meets some edge, and it meets each edge in at most one point, no component can be a sphere. ◻
:::
