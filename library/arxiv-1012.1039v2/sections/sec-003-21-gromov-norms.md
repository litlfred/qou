---
doc_id: arxiv-1012.1039v2
doc_title: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS"
section_id: sec-003-21-gromov-norms
section_title: "Gromov norms"
section_number: 2.1
pages: 4-6
source_pdf: 1012.1039v2.pdf
source_sha256: acb2575050db419d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.99
doc_brief: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS — Let M be a hyperbolic n–manifold whose cusps have torus cross- sections."
---
[]{#ss:norms label="ss:norms"} Let $X$ be any space, and let $\omega \in H_*(X;\mathbb{R})$ or $\omega \in
H_*(X,Y;\mathbb{R})$ for some $Y\subset X$. The *Gromov norm of $\omega$* is the smallest $l^1$--norm of a real singular chain representing $\omega$, $$\|\omega\| = \inf\left\{\sum_{i=1}^k
|\alpha_i|\ \right|\ \left. \left[\sum_{i=1}^k\alpha_i\sigma_i \right]
 = \omega \right\}.$$ (Since this infimum may be zero, the "Gromov norm" is only a seminorm in general.) This quantity only depends on $\omega$ and the homotopy type of the pair $(X,Y)$. In the absolute case, we can use it to define the Gromov norm of any $\omega\in H_*(G)$, where $G$ is a discrete group, by choosing $X$ to be a $K(G,1)$.

If $\omega$ is an integral cycle and $\eta$ is the canonical map from integral to real homology, then we set $\|\omega\| = \|\eta(\omega)\|$.

The Gromov norm of a cycle can be computed via the pairing between bounded cohomology and $l^1$ homology: If $\omega\in H_k(X)$ and $H_b^k(X;\mathbb{R})$ is the $k$--dimensional bounded cohomology of $X$, then $$\label{duality}
 \|\omega\| = \sup\left(\left.\left\{\frac{1}{\|\phi\|_\infty}\ \right| \phi\in
H_b^k(X;\mathbb{R}),\langle \phi,\omega\rangle = 1\right\}\cup\{0\}\right).$$ See [@BP92 Proposition F.2.2] for a proof.

For $M$ a closed orientable $n$--manifold, Gromov defined the *simplicial volume* $\|M\|$ to be the Gromov norm of the fundamental class in $H_n(M;\mathbb{R})$. For a manifold with boundary, it is natural to define $\|M,\partial M\|$ to be the Gromov norm of the fundamental class in $H_n(M,\partial M;\mathbb{R})$. It is clear from the definition that this volume only depends on the homotopy type of $(M,\partial M)$. For closed hyperbolic manifolds the simplicial volume is proportional to the volume. More generally, if $M$ is compact, and the interior of $M$ admits a complete finite volume hyperbolic metric of volume $\mathrm{Vol}$, then $$\|M,\partial M\| = \frac{1}{v_n} \mathrm{Vol},$$ where $v_n$ is the volume of a hyperbolic regular ideal simplex of dimension $n$. (See [@BP92 C.4] for the closed case; we show how to extend to the finite volume case in Appendix [\[s:prop\]](#s:prop){reference-type="ref" reference="s:prop"}.)

In [@Ya97], Yamaguchi extended the notion of simplicial volume to orientable pseudomanifolds, defined as follows.

::: definition
[@Ya97 Definition 2.1][]{#d:pseudomanifold label="d:pseudomanifold"} A locally compact, Hausdorff, locally homologically $n$--connected space $X$ is called an *oriented $n$--pseudomanifold* if it contains a closed subset $S$ (the *singular set*) so that:

1.  $X\smallsetminus S$ is an orientable $n$--manifold,

2.  $\dim(S)\leq n-1$, and

3.  $\dim(S\cap\overline{X\smallsetminus S}) \leq n-2$.
:::

::: remark
In this definition, we allow the possibility that $S$ is not "really" singular. For example, $X$ could be a manifold and $S$ a codimension $2$ submanifold. This is important in applying Proposition [\[p:nonzero\]](#p:nonzero){reference-type="ref" reference="p:nonzero"} to $2\pi$--fillings which happen to be manifolds, as in Corollary [\[c:specialcase\]](#c:specialcase){reference-type="ref" reference="c:specialcase"} below.
:::

In [@Ya97 Proposition 2.2], Yamaguchi shows that an oriented $n$--pseudomanifold $X$ has a fundamental class $[X]$ in $H_n(X) = H_n(\pi_1(X))$ so that the orientation cocycle $\beta \in H^n(X)$ is dual to this class. For such a pseudomanifold $X$, the *simplicial volume* of $X$ is defined to be the Gromov norm of $[X]$, and written $\|X\|$.

If $X$ is compact with CAT$(-1)$ universal cover, then $X$ is aspherical and $\pi_1(X)$ is (word) hyperbolic [@gromov:hg]. In this case the orientation cocycle is cohomologous to a bounded cocycle by the main theorem of [@min:bcchg], and so $\|X\|>0$ by the duality equation [\[duality\]](#duality){reference-type="eqref" reference="duality"}.

If $X$ is compact and the universal cover is CAT$(0)$ with isolated flats, then $X$ is again aspherical, but $\pi_1(X)$ is only relatively hyperbolic, relative to fundamental groups of images of flats in $X$ [@HK]. In this case, we will need the following corollary of a theorem of Mineyev--Yaman:

::: proposition
[]{#p:nonzero label="p:nonzero"} Let $M$ be a closed orientable aspherical $n$--dimensional pseudomanifold with singular set $V\subset M$ which is a disjoint union of aspherical components $V
  = \cup_{i=1}^mV_i$. Suppose that $\pi_1(M)$ is hyperbolic relative to the collection of subgroups $\left\{\pi_1(V_i)\mid i\in \{1,\ldots,n\}\right\}$. Then $\|M\|>0$.
:::

::: proof
*Proof.* The inclusion of pairs $(M,\emptyset)\to (M,V)$ gives a natural map $$H^n(M,V;\mathbb{R})\to H^n(M;\mathbb{R}).$$ Since $\dim(V\cap \overline{M\smallsetminus V})\leq n-2$, the Mayer--Vietoris exact sequence shows this map to be an isomorphism (cf. [@Ya97 Proposition 2.2]). The main result of Mineyev--Yaman [@MY] implies that the map $$H_b^n(\pi_1(M),\{\pi_1(V_i)\}_{i=1}^m;\mathbb{R}) \to
    H^n(\pi_1(M),\{\pi_1(V_i)\}_{i=1}^m;\mathbb{R})$$ is surjective, since $\pi_1(M)$ is hyperbolic relative to the fundamental groups of the components of $V$. Since $M$ and the components of $V$ are aspherical, this is the same as saying that the map $$\label{allbounded}
    H^n_b(M,V;\mathbb{R}) \to H^n(M,V;\mathbb{R}) = H^n(M;\mathbb{R})$$ is surjective. It follows that the orientation cocycle of $M$ is cohomologous to a bounded cocycle $\alpha$. (The cocycle moreover can be chosen to vanish on chains in $V$, but we don't use this.) Equation [\[duality\]](#duality){reference-type="eqref" reference="duality"} gives $\|M\| \geq \frac{1}{\| \alpha\|_\infty} > 0 .$ ◻
:::

Applying Theorem [\[t:filling\]](#t:filling){reference-type="ref" reference="t:filling"}, we immediately obtain the lower bound of Theorem [\[t:volumedecreases\]](#t:volumedecreases){reference-type="ref" reference="t:volumedecreases"}.

::: corollary
[]{#c:lowerbound label="c:lowerbound"} If $M(T_1,\ldots,T_m)$ is a $2\pi$--filling as in Theorem [\[t:volumedecreases\]](#t:volumedecreases){reference-type="ref" reference="t:volumedecreases"}, then $$\|M(T_1,\ldots,T_m)\|>0.$$
:::

The special case of nonpositively curved *manifolds* obtained by $2\pi$--filling of $\geq 4$--dimensional hyperbolic manifolds has been studied before us by Schroeder, Anderson and others [@Sc; @An]. Ivanšić describes in [@Iv] a particular cusped hyperbolic manifold which is the complement of five linked $2$--tori in the $4$--sphere. Ratcliffe and Tschantz point out in [@RT05] that appropriately chosen $2\pi$--fillings of this hyperbolic manifold are homology $4$--spheres. In [@Be06 Question 7.2], Belegradek asked if such fillings have positive simplicial volume. As a special case of [\[c:lowerbound\]](#c:lowerbound){reference-type="ref" reference="c:lowerbound"} above, we give an affirmative answer.

::: corollary
[]{#c:specialcase label="c:specialcase"} Every manifold obtained by $2\pi$--filling of an orientable hyperbolic $n$--manifold with torus cusps has positive simplicial volume. In particular, the aspherical homology $4$--spheres constructed by Ratcliffe and Tschantz have positive simplicial volume.
:::

Theorem [\[t:volumedecreases\]](#t:volumedecreases){reference-type="ref" reference="t:volumedecreases"} gives further information (an upper bound) on the simplicial volume.
