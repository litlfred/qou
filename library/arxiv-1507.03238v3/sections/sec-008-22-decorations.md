---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-008-22-decorations
section_title: "Decorations"
section_number: 2.2
pages: 6-7
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.982
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
[]{#sec:Decorations label="sec:Decorations"} Let $B\subset\mathop{\mathrm{SL}}(2,\mathbb C)$ denote the subgroup of upper triangular matrices, and $P$ the subgroup of upper triangular matrices with $1$'s on the diagonal. Let $G=\mathop{\mathrm{SL}}(2,\mathbb C)$ and let $H\subset G$ denote either $P$ or $B$.

::: definition
A $(G,H)$-representation is a representation $\pi_1(M)\to G$ taking each peripheral subgroup $\pi_1(\partial_i M)$ to a conjugate of $H$. Such are called *boundary-unipotent* for $H=P$ and *boundary-Borel* for $H=B$.
:::

::: definition
A $(G,H)$-representation is *boundary-nondegenerate* if its restriction to $\pi_1(\partial M_i)$ is non-trivial for each boundary component $\partial_i M$ of $M$.
:::

Let $I(\widetilde M)$ denote the set of ideal vertices of $\widetilde M$, i.e. vertices of $\scalerel*{\widehat{\widetilde M}}{\widetilde{M^2}}$ with the triangulation induced by $\mathcal T$. Note that each ideal point corresponds to a boundary component of $\widetilde M$, so $I(\widetilde M)$ is independent of $\mathcal T$.

::: definition
A *decoration* of a simplex $\Delta$ is an assignment of a coset $g_iH$ to each vertex $v_i$ of $\Delta$. A decoration is thus a tuple $(g_0H,g_1H,g_2H,g_3H)$, and we consider two decorations to be equal if the tuples differ by multiplication by an element in $\mathop{\mathrm{SL}}(2,\mathbb C)$. A decoration is *generic* if the cosets are distinct as $B$-cosets (distinct if $H=B$).
:::

::: definition
[]{#def:Decoration label="def:Decoration"} Let $\rho$ be a $(G,H)$-representation. A *decoration* of $\rho$ is a $\rho$-equivariant map $$\label{eq:DevelopingMap}
D\colon I(\widetilde M)\to G/H,$$ i.e. an equivariant assignment of $H$-cosets to the ideal points of $\widetilde M$. When the representation plays no role, we shall refer to a decorated representation simply as a decoration. Since $gD$ is a decoration of $g\rho g^{-1}$ if $D$ is a decoration of $\rho$, we consider two decorations to be equal if they differ by left multiplication by an element in $G$.
:::

::: remark
A boundary-unipotent representation is also boundary-Borel. We shall refer to decorations as $P$-decorations or $B$-decorations depending on context.
:::

::: definition
A decoration is *generic* if the induced decoration of each simplex of $\mathcal T$ is generic.
:::

::: remark
Every $(G,H)$-representation has a decoration, but whether a decoration is generic depends on $\mathcal T$.
:::

::: remark
A $B$-coset determines a point in $\partial\overline\mathbb H^3=\mathbb C\cup\{\infty\}$, the boundary of hyperbolic $3$-space, via $gB\leftrightarrow g\infty$. A decoration of a boundary-Borel representation thus determines a developing map (see e.g. Zickert [@ZickertDuke]) assigning ideal simplex shapes to the simplices of $\mathcal T$. A decoration is generic if and only if all shapes are non-degenerate. We shall not need this here.
:::

### Freedom in the choice of decoration {#sec:Freedom}

If we choose points $e_i\in I(\widetilde M)$, one for each boundary component $\partial_i M$ of $M$, a decoration is uniquely determined by the cosets $D(e_i)$. The freedom in the choice of $D(e_i)$ is determined by the image of the boundary components.

::: proposition
[]{#prop:Freedom label="prop:Freedom"} Let $\rho$ be a $(G,B)$-representation and let $e_i$ be as above.

1.  If $\rho(\pi_1(\partial_i M))$ is trivial, $D(e_i)$ may be chosen arbitrarily.

2.  If $\rho(\pi_1(\partial_i M))$ is non-trivial and unipotent, $D(e_i)$ is uniquely determined by $\rho$.

3.  If $\rho(\pi_1(\partial_i M))$ is non-trivial and diagonalizable, $D(e_i)$ is determined by $\rho$ up to a $\mathbb Z/2\mathbb Z$-action.0◻
:::

::: corollary
[]{#cor:Freedom label="cor:Freedom"} A boundary-nondegenerate $(G,P)$-representation has a unique $B$-decoration. A boundary-nondegenerate $(G,B)$-representation generically has $2^c$ decorations, where $c$ is the number of boundary components.
:::

::: remark
[]{#rm:Freedom label="rm:Freedom"} Different choices of $D(e_i)$ may give rise to equal decorations, i.e. decorations differing only by left multiplication by an element in $G$. Hence, even when a boundary-component is collapsed, there may be only finitely many decorations (see e.g. the example in Section [\[sub:Reducible\]](#sub:Reducible){reference-type="ref" reference="sub:Reducible"}).
:::
