---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction"
section_id: sec-016-33-combinatorial-bounds-for-triangulations
section_title: "Combinatorial bounds for triangulations"
section_number: 3.3
pages: 18-19
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.974
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low"
---
The set-up and notation of the previous subsection is continued. Let $$\begin{aligned}
n_{\mathfrak{qtt}}(\mathcal{T})&= \text{ number of tetrahedra of type } \Delta_{\mathfrak{qtt}}, \\
n_{\mathfrak{qq}}(\mathcal{T})&= \text{ number of tetrahedra of type }\Delta_{\mathfrak{qq}}, \\
n_{\mathfrak{tt}}(\mathcal{T})&= \text{ number of tetrahedra of type }\Delta_{\mathfrak{tt}}, \\
n_{\emptyset}(\mathcal{T})&= \text{ number of tetrahedra of type }\Delta_{\emptyset}, \\
n_{\mathfrak{qqq}}(\mathcal{T})&= \text{ number of tetrahedra of type }\Delta_{\mathfrak{qqq}}, \\
\mathfrak{e}(\mathcal{T})&= \text{ number of 0--even edges, }\\
\tilde{\mathfrak{e}}(\mathcal{T})&= \text{ number of preimages of 0--even edges in } \widetilde{\Delta}.
\end{aligned}$$ The number of tetrahedra in $\mathcal{T}$ is $$|\mathcal{T}| = n_{\mathfrak{qtt}}(\mathcal{T}) + n_{\mathfrak{qq}}(\mathcal{T}) + n_{\mathfrak{tt}}(\mathcal{T}) + n_{\emptyset}(\mathcal{T}) + n_{\mathfrak{qqq}}(\mathcal{T}).$$ For the remainder of this subsection, we write $n_{\mathfrak{qtt}}= n_{\mathfrak{qtt}}(\mathcal{T}),$ etc.

Let $\hat{K}$ be the complex in $\mathcal{T}$ spanned by all 0--even edges (i.e., the complex of all edges, faces and tetrahedra of $\mathcal{T}$ containing only 0--even edges) and let $K$ be the ideal complex obtained from $\hat{K}$ by removing its vertices.

Let $N$ be a small regular neighbourhood of $K.$ Then $\partial N$ is a normal surface; it meets each tetrahedron in the same number and types of normal discs as $S_{\varphi_1} \cup S_{\varphi_2}\cup S_{\varphi_3}$ except for the tetrahedra of type $\Delta_{\mathfrak{qqq}},$ which it meets in four distinct normal triangle types instead of three distinct normal quadrilateral types. The normal coordinate of $\partial N$ is thus obtained by taking the sum of the normal coordinates of $S_{\varphi_1},$ $S_{\varphi_2},$ and $S_{\varphi_3},$ and adding to this the *tetrahedral solution* of each tetrahedron of type $\Delta_{\mathfrak{qqq}}.$ (The tetrahedral solution is obtained by adding all triangle coordinates of a tetrahedron and subtracting all quadrilateral coordinates; see, for instance, [@Kang-ideal-2004 Section], or [@Tillmann-normal-2008 Section 2.8]. Each tetrahedral solution has both positive and negative coordinates.) Hence $$\chi(S_{\varphi_1}) +\chi (S_{\varphi_2}) + \chi (S_{\varphi_3}) + n_{\mathfrak{qqq}}= \chi (\partial N) = 2 \chi(N) = 2 \chi(K) = - 2 \mathfrak{e}+n_{\mathfrak{tt}}+ 2n_{\emptyset},$$ where the rightmost equality is a consequence of the following computation: By definition, the Euler characteristic of $K$ equals minus the number of 0--even edges plus the number of triangles with only 0--even edges minus the number of tetrahedra of type $\Delta_{\emptyset}$ (note that $K$ is ideal and hence has no vertices). Since every triangle occurs in exactly two tetrahedra, every tetrahedron of type $\Delta_{\mathfrak{tt}}$ accounts for one half of a triangle with 0--even edges and every tetrahedron of type $\Delta_{\emptyset}$ accounts for two triangles of 0--even edges. Hence, in total we have $$\chi (K) = - \mathfrak{e}+ \frac12 n_{\mathfrak{tt}}+ 2 n_{\emptyset}- n_{\emptyset}= -\mathfrak{e}+ \frac12 n_{\mathfrak{tt}}+ n_{\emptyset}.$$

In particular, $\chi(S_{\varphi_1}) +\chi (S_{\varphi_2}) + \chi (S_{\varphi_3}) + n_{\mathfrak{qqq}}$ is even. Rearranging the above equality gives $$\label{eq:e}
n_{\mathfrak{tt}}+ 2n_{\emptyset}-n_{\mathfrak{qqq}}= 2 \mathfrak{e}+ \chi(S_{\varphi_1}) +\chi (S_{\varphi_2}) + \chi (S_{\varphi_3}),$$

and hence: $$\begin{aligned}
\label{inequ for one vert tri gen}
\tilde{\mathfrak{e}}   &= n_{\mathfrak{qtt}}+2n_{\mathfrak{qq}}+3n_{\mathfrak{tt}}+6n_{\emptyset}\nonumber \\
        &=  2|\mathcal{T}|  -n_{\mathfrak{qtt}}+ n_{\mathfrak{tt}}+4n_{\emptyset}-2n_{\mathfrak{qqq}}\nonumber\\
        &= 2|\mathcal{T}|  - n_{\mathfrak{qtt}}- n_{\mathfrak{tt}}+4 \mathfrak{e}+ 2 (\chi(S_{\varphi_1}) +\chi (S_{\varphi_2}) + \chi (S_{\varphi_3})).
\end{aligned}$$

::: lemma
[]{#lem:formula for degree 3 edges label="lem:formula for degree 3 edges"} Let $M$ be a cusped hyperbolic 3--manifold of finite volume, and suppose that $\varphi_1, \varphi_2 \in  H^1(\widehat{M}, \widehat{M}^{(0)}; \mathbb{Z}_2)$ are non--trivial classes with $\varphi_1+\varphi_2 = \varphi_3 \neq 0.$ Let $\mathcal{T}$ be a minimal triangulation, $S_{\varphi_i}$ be the canonical surface dual to $\varphi_i,$ and let $\mathfrak{e}_d$ denote the number of 0--even edges of degree $d.$ Then $$\label{inequ for min tri general}
\mathfrak{e}_3= n_{\mathfrak{qtt}}+n_{\mathfrak{tt}}- 2 (|\mathcal{T}| + \chi(S_{\varphi_1}) +\chi (S_{\varphi_2}) +\chi (S_{\varphi_3})) + \sum_{d=5}^{\infty} (d-4) \mathfrak{e}_d.$$
:::

::: proof
*Proof.* Lemmata [\[thm:degone\]](#thm:degone){reference-type="ref" reference="thm:degone"} and [\[lem:degree two\]](#lem:degree two){reference-type="ref" reference="lem:degree two"} imply that the smallest degree of an edge in $\mathcal{T}$ is three. One has $\tilde{\mathfrak{e}} = \sum d \mathfrak{e}_d$ and $\mathfrak{e}= \sum \mathfrak{e}_d.$ Inserting this into Equation ([\[inequ for one vert tri gen\]](#inequ for one vert tri gen){reference-type="ref" reference="inequ for one vert tri gen"}) yields the desired equality. ◻
:::
