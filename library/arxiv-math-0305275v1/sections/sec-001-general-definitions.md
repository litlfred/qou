---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds"
section_id: sec-001-general-definitions
section_title: "General definitions"
section_number: null
pages: 3-6
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.991
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2, C)."
---
[]{#s uno label="s uno"} We fix here the class of manifolds we consider, namely the class of ideally triangulated cusped manifolds. Since we work with cusped manifolds, we want to fix a structure on the cusps.

::: defitit
Cusped manifold An orientable manifold $M$ is called *cusped manifold* if it is diffeomorphic to the interior of a compact manifold with boundary $\ensuremath{\overline{M}}$. A *cusp* of $M$ is a closed regular neighborhood of a component of $\partial
 \overline M$. In the following we require $M$ to have dimension $3$ and $\partial \overline M$ to be a union of tori, so each cusp is homeomorphic to $T^2\times[0,\infty)$.

We define $\ensuremath{\widehat{M}}$ as the compactification of $M$ obtained by adding one point for each cusp of $M$. Called $\ensuremath{\widetilde{M}}$ the universal cover of $M$, we call $\ensuremath{\widehat{\ensuremath{\widetilde{M}}}}$ the space obtained by adding to $\ensuremath{\widetilde{M}}$ one point for each lift of each cusp of $M$.

We call the points added to $M$ (or $\ensuremath{\widetilde{M}}$) *ideal points* of $M$ (or $\widetilde{M}$). For each ideal point $p$ of $M$, we fix a smooth product structure $T_p\times[0,\infty)$ on the cusp relative to $p$. Such a structure induces a cone structure, obtained from $T_p\times[0,\infty]$ by collapsing $T_p\times\{\infty\}$ to $p$, on a neighborhood $C_p$ of $p$ in $\ensuremath{\widehat{M}}$.

We lift such structures to the universal cover. Let $\widetilde{p}$ be an ideal point of $\widetilde{M}$ that projects to the ideal point $p$ of $M$. We denote by $N_{\ensuremath{\widetilde{p}}}$ the cone at $\widetilde{p}$. The cone $N_{\ensuremath{\widetilde{p}}}$ is homeomorphic to $P_{\ensuremath{\widetilde{p}}}\times[0,\infty]$ where $P_{\ensuremath{\widetilde{p}}}$ covers the torus $T_p$ and $P_{\ensuremath{\widetilde{p}}}\times\{\infty\}$ is collapsed to $\widetilde{p}$.
:::

::: remark
In the definition of cusped manifold we have included a fixed product structure on the cusps. This is for technical reasons, however we will show that the results about the volume of representations do not depend on the chosen structure.
:::

::: remark
Let $\widetilde{M}$ be the universal cover of $M$. In the following, when we speak about $\pi_1(M)$, we tacitly assume that a base-point and one of its lifts have been fixed. If $p$ is an ideal point of $M$, then $\pi_1(T_p)$ is well-defined only up to conjugation. Called $\{\ensuremath{\widetilde{p}}_i\}$ the set of the lifts of $p$, there is a one-to-one correspondence between the stabilizers Stab$(\ensuremath{\widetilde{p}}_i)$ of $\ensuremath{\widetilde{p}}_i$ in the group of deck transformations of $\ensuremath{\widetilde{M}}\to M$ and the conjugates of $\pi_1(T_p)$ in $\pi_1(M)$. Such a correspondence is uniquely determined once the base-points have been fixed.
:::

To avoid pathologies, since we are working with cusped manifolds, we need that the maps we use have a nice behavior "at infinity." Namely, we will often require that a map from a cusp to $\ensuremath{\mathbb H}^3$ is a cone-map in the following sense.

::: defitit
Cone-map Let $A$ be a set, $c\in\ensuremath{\mathbb R}$ and $C$ be the cone obtained from $A\times[c,\infty]$ by collapsing $A\times\{\infty\}$ to a point, which we call $\infty$. A map $f:C\to\ensuremath{\overline{\ensuremath{\mathbb H}}}^n$ is a *cone-map* if:

-   $f(C)\cap\partial \ensuremath{\mathbb H}^n=\{f(\infty)\}$;

-   $\forall a\in A$ the map $f_{|a\times[c,\infty]}$ is either the constant to $f(\infty)$ or the geodesic ray from $f(a,c)$ to $f(\infty)$, parametrized in such a way that the parameter $(t-c),\ t\in[c,\infty]$, is the arc-length.
:::

We recall here the definition of pseudo-developing map for a representation (see [@D]).

::: defitit
Pseudo-developing map[]{#d pd label="d pd"} Let $M$ be a cusped manifold and let $\rho:\pi_1(M)\to{\rm Isom}^+(\ensuremath{\mathbb H}^3)$ be a representation. A *pseudo-developing map* for $\rho$ is a piecewise smooth map $D_\rho:\ensuremath{\widetilde{M}}\to \ensuremath{\mathbb H}^3$ which is equivariant w.r.t. the actions of $\pi_1(M)$ on $\widetilde{M}$ via deck transformations and on $\ensuremath{\mathbb H}^3$ via $\rho$. Moreover we require $D_\rho$ to extend to a continuous map, which we still call $D_\rho$, from $\ensuremath{\widehat{\ensuremath{\widetilde{M}}}}$ to $\overline{\ensuremath{\mathbb H}}^3$ that maps the ideal points to $\partial \ensuremath{\mathbb H}^3$ (see Remark [\[r die\]](#r die){reference-type="ref" reference="r die"} for comments on this property). Finally we require that there exists $t_{D_\rho}\in \ensuremath{\mathbb R}^+$ such that for each cusp $N_p=P_p\times[0,\infty]$ of $\widetilde{M}$, the restriction of $D_\rho$ to $P_p\times[t_{D_\rho},\infty]$ is a cone-map.
:::

Let $\gamma\neq{\rm id}$ be an isometry of $\ensuremath{\mathbb H}^3$ and let Fix$(\gamma)$ be the set of fixed points of $\gamma$. Then Fix$(\gamma)\cap\partial\ensuremath{\mathbb H}^3$ consists of either one or two points. Moreover, if $\gamma_1$ and $\gamma_2$ commute, then Fix$(\gamma_1)$ is $\gamma_2$-invariant. It follows that if $\Gamma$ is an Abelian subgroup of orientation-preserving isometries and $\gamma\in\Gamma$, then Fix$(\gamma)$ is $\Gamma$-invariant. Actually, for almost all Abelian $\Gamma$ and for any $\gamma_1,
\gamma_2\in\Gamma\setminus\{{\rm id}\}$ we have $$\textrm{Fix}(\gamma_1)= \textrm{Fix}(\gamma_2).$$

The only cases in which this is not true are when $\Gamma$ is a dihedral group generated by two rotations of angle $\pi$ around orthogonal axes. Such a group is isomorphic to $\ensuremath{\mathbb Z}_2\times \ensuremath{\mathbb Z}_2$ and its unique fixed point is the intersection of the axes. It follows that any Abelian group $\Gamma$ of orientation-preserving isometries has a fixed point in $\ensuremath{\overline{\ensuremath{\mathbb H}}}^3$ and, if $\Gamma$ is not dihedral, then it has a fixed point in $\partial \ensuremath{\mathbb H}^3$.

Let now $p$ be an ideal point of $\ensuremath{\widehat{\ensuremath{\widetilde{M}}}}$. Since Stab$(p)$ is Abelian, then either it is dihedral or it has a fixed point in $\partial\ensuremath{\mathbb H}^3$. If $\rho$ is a representation of $\pi_1(M)$ and $D_\rho$ is a pseudo-developing map for $\rho$, then $D_\rho(p)$ is a fixed point of $\rho($Stab$(p))$. It follows that, using Definition [\[d pd\]](#d pd){reference-type="ref" reference="d pd"}, in order for a pseudo-developing map to exist, $\rho($Stab$(p))$ must have a fixed point in $\partial \ensuremath{\mathbb H}^3$.

::: remark
 []{#r die label="r die"} We included in Definition [\[d pd\]](#d pd){reference-type="ref" reference="d pd"} the requirement that $D_\rho$ maps ideal points to $\partial \ensuremath{\mathbb H}^3$ only for simplicity. No pathologies do occur if some ideal point is mapped to the interior of $\ensuremath{\mathbb H}^3$. Coherently with this fact, from now on we suppose that:

-   For each boundary torus $T$, the group $\rho(\pi_1(T))$ is not dihedral.

As above we notice that this is only for simplicity and one can easily check that all the results of this paper remain true, *mutatis mutandis*, without this assumption.
:::

::: lemma
[]{#l 1 label="l 1"} Let M be a cusped manifold and let $\rho:\pi_1(M)\to$ Isom$^+(\ensuremath{\mathbb H}^3)$ be a representation. Then a pseudo-developing map $D_\rho$ exists.
:::

 The proof is the same as in [@D], we recall it by completeness. We construct a pseudo-developing map inductively on the $n$-skeleta. Let $p$ be an ideal point of $\widetilde{M}$. Since Stab$(p)$ is Abelian and not dihedral, then its $\rho$-image has at least one fixed point $q\in\partial \ensuremath{\mathbb H}^3$. We define $D_\rho(p)=q$ and, for all $\alpha\in\pi_1(M)$ we set $D_\rho(\alpha(p))=\rho(\alpha)(q)$. We do the same for the other ideal points. Now for each ideal point $p$ we define $D_\rho$ on $P_p\times\{0\}$ in any Stab$(p)$-equivariant way and then we make the cone over $D_\rho(p)$ in such a way that $D_\rho$ has the cone property. Then we extend $D_\rho$ in any equivariant way. The extension is possible because $\ensuremath{\mathbb H}^3$ is contractible.\

::: remark
[]{#r pip label="r pip"} Let $p$ be an ideal point of $\ensuremath{\widehat{\ensuremath{\widetilde{M}}}}$. If $\rho($Stab$(p))$ is a parabolic non-trivial group, then it has a unique fixed point. It follows that $D_\rho(p)$ is uniquely determined. Thus, if all the $\rho$-images of the stabilizers of the ideal points are parabolic, then the $D_\rho$-images of all the ideal points are uniquely determined.
:::

::: defitit
Ideally triangulated manifold Let $M$ be a cusped manifold. An ideal triangulation of $M$ is a triangulation of $\ensuremath{\widehat{M}}$ having the set of ideal points as $0$-skeleton. An *ideally triangulated manifold* is a cusped manifold equipped with a finite smooth ideal triangulation $\tau$. We require the triangulation to be compatible with the product structure. That is, for each cusp $N_p$ we require $\tau\cap (T_p\times\{0\})$ to be a triangulation of $T_p$ and the restriction to $N_p$ of $\tau$ to be the product triangulation.
:::

We will often consider the simplices of an ideal triangulation of a manifold $M$ as subsets of $\ensuremath{\widehat{M}}$.

::: remark
[]{#r acmcbid label="r acmcbid"} It is well-known that any cusped manifold can be ideally triangulated (see for example [@BP]).
:::
