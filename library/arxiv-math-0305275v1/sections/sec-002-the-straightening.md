---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds"
section_id: sec-002-the-straightening
section_title: "The straightening"
section_number: null
pages: 6-9
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.99
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2, C)."
---
[]{#s due label="s due"}

A straightening of a pseudo-developing map $D$ is a map that agrees with $D$ on the ideal points and that maps each tetrahedron to a straight one. The straightening is useful to calculate the hyperbolic volume associated to a pseudo-developing map (see Section [\[s 3\]](#s 3){reference-type="ref" reference="s 3"}). A particular case is when the manifold $M$ is complete hyperbolic, because in this case the straightening descends to a map from $M$ to itself. Here we prove that such a map is onto.

Let $\Delta\subset\ensuremath{\mathbb H}^3$ be an oriented geodesic ideal tetrahedron. Since $\Delta$ is the convex hull of its vertices, then the Isom$^+(\ensuremath{\mathbb H}^3)$-class of $\Delta$ is completely determined by the Isom$^+(\ensuremath{\mathbb H}^3)$-class of the oriented set of its vertices (the orientation of the vertices is defined up to the action of ${\ensuremath{\cal A}}_4$). Such a class is completely determined by a non-real complex number called modulus, up to a three-to-one ambiguity. Such an ambiguity can be avoided by choosing a preferred pair of opposite edges of $\Delta$ (see [@BP], [@F3], [@PP], [@PW] [@Th1]). We extend the notion of modulus to the set of flat tetrahedra, that is to those whose vertices are distinct and lie on a hyperbolic plane of $\ensuremath{\mathbb H}^3$, by accepting real moduli different from 0 and 1. We want to extend this definition also to the degenerate tetrahedra, *i.e.* to those having two ore more coincident vertices. Unfortunately, for such a tetrahedron it is not possible to encode its isometry class in a complex number. Let us agree that when we use a modulus in $\{0,1,\infty\}$ for $\Delta$, we mean that $\Delta$ is a degenerate tetrahedron and that the modulus encodes the complete information on the isometry class of $\Delta$, *i.e.* who are the coincident vertices of $\Delta$.

::: defi
Let $\Delta^k$ be the standard $k$-simplex. Let $\ensuremath{\varphi}:\Delta^k\to \ensuremath{\overline{\ensuremath{\mathbb H}}}^n$ be a continuous map that maps the $0$-skeleton of $\Delta^k$ to $\partial \ensuremath{\mathbb H}^n$. Let $Q$ be the Euclidean convex hull of the $\varphi$-image of the vertices of $\Delta^k$, made in a disc model of $\ensuremath{\mathbb H}^n$. Let $\psi:\Delta^k\to Q$ be the only simplicial map that agrees with $\ensuremath{\varphi}$ on the $0$-skeleton.

We say that the map $\ensuremath{\varphi}$ is *standard* if there exist two homeomorphisms $\eta:{\rm Im}(\ensuremath{\varphi})\to Q$ and $\beta:\Delta^k\to \Delta^k$ such that $$\eta\circ\ensuremath{\varphi}\circ\beta=\psi.$$ We say that a foliation $\cal F$ of $\Delta^k$ is *standard* if there exists a standard map $\ensuremath{\varphi}:\Delta^k\to \ensuremath{\overline{\ensuremath{\mathbb H}}}^n$ such that ${\ensuremath{\cal F}}=\{\ensuremath{\varphi}^{-1}(x)\}$.
:::

::: remark
[]{#r uno label="r uno"} For any standard map $\ensuremath{\varphi}$ the dimension of ${\ensuremath{\cal F}}=\{\ensuremath{\varphi}^{-1}(x)\}$ depends only on the $\varphi$-image of the $0$-skeleton.
:::

::: remark
It is not hard to show that for a map $\varphi$ to be standard does not depend on the disc model we use. In other words $\varphi$ is standard if and only if $\gamma\ensuremath{\varphi}$ is standard for any isometry $\gamma$.
:::

Let $M$ be an ideally triangulated manifold, $\rho:\pi_1(M)\to$Isom$^+(\ensuremath{\mathbb H}^3)$ be a representation, and $D_\rho$ be a pseudo-developing map for $\rho$. Let $\Delta$ be a tetrahedron of $\tau$ and $\widetilde{\Delta}$ be one of its lifts. The vertices of $\widetilde{\Delta}$ are ideal points, so their images under $D_\rho$ lie in $\partial
\ensuremath{\mathbb H}^3$. The map $D_\rho$ determines a modulus for $\widetilde{\Delta}$ simply by considering the convex hull of the image of its vertices (the orientation is the one induced by $M$). Note that since $D_\rho$ is equivariant, then it defines a modulus for $\Delta$. For each face $\sigma$ of $\Delta$ we call ${\rm Str}_{D_\rho}(\ensuremath{\widetilde{\sigma}})$, or simply ${\rm Str}(\ensuremath{\widetilde{\sigma}})$, the straight simplex obtained as the convex hull of the $D_\rho$-image of the vertices of $\widetilde{\sigma}$.

::: defitit
Straightening[]{#d str label="d str"} A straightening of $D_\rho$ is a continuous, piecewise smooth, $\rho$-equivariant map ${\rm Str}(D_\rho):\ensuremath{\widehat{\ensuremath{\widetilde{M}}}}\to 
  \overline{\ensuremath{\mathbb H}}^3$ such that:

1.  For each simplex $\sigma$ of the triangulation, ${\rm Str}(D_\rho)$ maps $\widetilde{\sigma}$ to ${\rm Str}(\ensuremath{\widetilde{\sigma}})$.

2.  The restriction of ${\rm Str}(D_\rho)$ to any simplex $\sigma$ is standard.

3.  For each cusp $N_{\ensuremath{\widetilde{p}}}=P_{\ensuremath{\widetilde{p}}}\times[0,\infty]$ there exists $c\in\ensuremath{\mathbb R}$ such that ${\rm Str}(D_\rho)$ restricted to $P_{\ensuremath{\widetilde{p}}}\times[c,\infty]$ is a cone-map.
:::

::: lemma
[]{#l 2 label="l 2"} Let M be an ideally triangulated manifold. Let $\rho$ be a representation $\rho:\pi_1(M)\to$Isom$^+(\ensuremath{\mathbb H}^3)$ and $D_\rho$ be a pseudo-developing map. Then a straightening ${\rm Str}(D_\rho)$ of $D_\rho$ exists. Moreover ${\rm Str}(D_\rho)$ is always equivariantly homotopic to $D_\rho$ via a homotopy that fixes the ideal points.
:::

  A straightening of $D_\rho$ can be constructed with the same techniques of Lemma [\[l 1\]](#l 1){reference-type="ref" reference="l 1"}. Regarding the homotopy, since $D_\rho$ maps non-ideal points to the interior of $\ensuremath{\mathbb H}^3$, then one can use a geodesic flow with the time-parameter in $[0,\infty]$ (for example the convex combination of Definition [\[d cvxc\]](#d cvxc){reference-type="ref" reference="d cvxc"}) to construct a homotopy with the required properties.\

::: remark
A straightening in general is not a pseudo-developing map in our setting, because it can map some point of $\widetilde{M}$ to $\partial \ensuremath{\mathbb H}^3$. However, if there are no degenerate tetrahedra, then a straightening is also a pseudo-developing map, and the homotopy between $D_\rho$ and ${\rm Str}(D_\rho)$ can be made coherently with the cone structure of the cusps, *i.e.* in such a way that the intermediate maps along the homotopy between $D_\rho$ and ${\rm Str}(D_\rho)$ have the cone property on the cusps.
:::

When $M$ has a complete hyperbolic structure of finite volume, there is a natural notion of straightening of the ideal triangulation. Namely, choose the arc-length as the cone parameter on the cusps of $M$ and consider $\ensuremath{\mathbb H}^3$ as the universal cover of $M$. Then choose $\rho$ as the holonomy of the hyperbolic structure of $M$; the identity map of $\ensuremath{\mathbb H}^3$ clearly is a pseudo-developing map for $\rho$. A natural straightening map is a straightening of the identity.

::: prop
[]{#p so label="p so"} Let M be an ideally triangulated manifold equipped with a complete, finite-volume hyperbolic structure. Then any natural straightening map projects to a map ${\rm Str}:\ensuremath{\widehat{M}}\to \ensuremath{\widehat{M}}$ which is onto. Moreover ${\rm Str}(M)\supset M$.
:::

  It is easy to see that $\ensuremath{\widehat{\ensuremath{\widetilde{M}}}}=\ensuremath{\widehat{\ensuremath{\mathbb H}^3}}$ naturally embeds into $\overline{\ensuremath{\mathbb H}}^3$ and that the ideal points lie on $\partial \ensuremath{\mathbb H}^3$. Since the straightening is equivariant, then it projects to a map ${\rm Str}:\ensuremath{\widehat{M}}\to \ensuremath{\widehat{M}}$. Moreover, Str fixes the ideal points. We prove that Str is onto. One can easily prove that $H_3(\ensuremath{\widehat{M}};\ensuremath{\mathbb Z})\cong H_3(\overline M,\partial \overline M;\ensuremath{\mathbb Z})\cong\ensuremath{\mathbb Z}$. So we can define the degree of a map $f:\ensuremath{\widehat{M}}\to\ensuremath{\widehat{M}}$ by $$f_*([\ensuremath{\widehat{M}}])=\textrm{deg}(f)\cdot[\ensuremath{\widehat{M}}]$$ where $[\ensuremath{\widehat{M}}]$ is the generator of $H_3(\ensuremath{\widehat{M}};\ensuremath{\mathbb Z})$ induced by the orientation of $M$. Now note that by Lemma [\[l 2\]](#l 2){reference-type="ref" reference="l 2"} the natural straightening is homotopic to the identity via an equivariant homotopy. Because of equivariance, the homotopy projects to a homotopy between Str and the identity. It follows that ${\rm Str}_*$ and id$_*$ coincide on $H_*(\ensuremath{\widehat{M}};\ensuremath{\mathbb Z})$, so $\textrm{deg}(\textrm{Str})=\textrm{deg}(\textrm{id})=1$. Now suppose that Str is not onto and let $x$ be a point in $\ensuremath{\widehat{M}}$ outside its image. If we consider Str as a map from $\widehat{M}$ to $\ensuremath{\widehat{M}}\setminus \{x\}$, we get ${\rm Str}_*([\ensuremath{\widehat{M}}])=0\in H_3(\ensuremath{\widehat{M}}\setminus
\{x\};\ensuremath{\mathbb Z})$ simply because $H_3(\ensuremath{\widehat{M}}\setminus\{x\};\ensuremath{\mathbb Z})=0$. Then ${\rm Str}_*([\ensuremath{\widehat{M}}])$ is a boundary in $\ensuremath{\widehat{M}}\setminus \{x\}$, consequently it is a boundary also in $\widehat{M}$. It follows that ${\rm Str}_*([\ensuremath{\widehat{M}}])=0$. This implies $\textrm{deg}(\textrm{Str})=0$, that is a contradiction.

The last assertion follows because Str is onto and fixes the ideal points.\
