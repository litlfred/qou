---
doc_id: arxiv-1012.1039v2
doc_title: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1012.1039v2.pdf
source_sha256: acb2575050db419d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.972
doc_brief: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS — Let M be a hyperbolic n–manifold whose cusps have torus cross- sections."
---
Simplicial volume was defined for manifolds by Gromov in [@gromov:vbc]. For an $n$-dimensional closed manifold $M$ of constant sectional curvature $K=-1$, the simplicial volume $\|M\|$ is proportional to the (Riemannian) volume $\mathrm{Vol}(M)$, and the ratio is the volume of a regular ideal hyperbolic $n$--simplex; in particular, it depends only on the dimension [@gromov:vbc 0.4]. More generally, [@gromov:vbc 0.3,0.5], for constants $a\le b< 0$, there is a constant $C=C(a,b,n)>1$ so that if the sectional curvatures $K$ satisfy $a \le K \le b$, then $$\label{propclosed}
 \mathrm{Vol}(M)/C \le \|M\| \le C\mathrm{Vol}(M).$$

This note is motivated in part by the (apparently open) question:

::: question
[]{#q:manif label="q:manif"} Fix $v>0$, and let $\mathcal{M}_{n,v}$ be the set of (homotopy classes of) closed $n$-manifolds whose sectional curvatures are all negative, and whose simplicial volume is bounded above by $v$. Is $\mathcal{M}_{n,v}$ finite whenever $n\geq 4$?
:::

Some comments, fixing $n\geq 4$ and $v>0$:

-   The set $\mathcal{M}_{n,v}$ contains only finitely many constant curvature manifolds, even up to diffeomorphism. This follows from Wang's finiteness theorem [@W] together with the proportionality of simplicial volume to hyperbolic volume for closed manifolds (see, e.g., [@BP92 C.4]).

-   Fix $b>0$. The set $\mathcal{M}_{n,v}$ contains only finitely many diffeomorphism classes of manifolds with sectional curvatures $K$ pinched between $-1$ and $b$. Indeed, as noted in the inequality [\[propclosed\]](#propclosed){reference-type="eqref" reference="propclosed"}, the curvature assumption $-1\le K \le b<0$ together with an upper bound on the simplicial volume gives an upper bound on the volume [@gromov:vbc 0.3, 1.2]. On the other hand, the condition $-1 \le K <0$ together with the upper bound on the volume gives an upper bound on the diameter [@G 1.2] and a lower bound on the volume [@G 1.3 A]. Now, Cheeger's finiteness theorem applies [@G 1.4].

    Thus if there are infinitely many diffeomorphism types of closed $n$--manifolds of bounded volume, with sectional curvatures $\le -1$, there cannot be any uniform lower bound on their sectional curvatures, so long as $n\ge 4$. So a negative answer to Question [\[q:manif\]](#q:manif){reference-type="ref" reference="q:manif"} would have to involve manifolds without uniformly pinched curvature. For $n>3$ there do exist sequences of negatively curved manifolds whose curvatures cannot be uniformly pinched. Gromov--Thurston [@GT 0.5] describe a sequence $\{V_i\}$ of negatively curved closed manifolds which are $i$-fold ramified covers of a fixed closed manifold $V$ of constant negative curvature, and show the curvatures of the $V_i$ cannot be uniformly pinched. We remark that such a sequence of ramified covers $V_i$ must satisfy $0<i\|V\| \le \|V_i\|$, so it does not imply a negative answer to Question [\[q:manif\]](#q:manif){reference-type="ref" reference="q:manif"}.

-   The sets $\mathcal{M}_{3,v}$ are infinite for large enough $v$, even if one restricts to constant curvature. This is because of Thurston's hyperbolic Dehn surgery theorem, and Thurston's theorem (which we generalize in this note) that volume decreases under hyperbolic Dehn filling.

It is easy to extend the definition of simplicial volume to closed pseudomanifolds. This is explained in Section [\[s:defs\]](#s:defs){reference-type="ref" reference="s:defs"} (cf. [@Ya97]). Pseudomanifold versions of the bounds in [\[propclosed\]](#propclosed){reference-type="eqref" reference="propclosed"} have been established by Yamaguchi [@Ya97 Theorem 0.2 and 0.5] as follows. First, if $X$ is an orientable $n$-dimensional, compact, geodesically complete (locally) CAT($-1$) pseudo-manifold, then $$\label{yamaguchilower}
\mathrm{Vol}(X)\leq  \frac{\pi}{(n-1)!} \|X\|.$$ Yamaguchi conjectures that the factor of $\frac{\pi}{(n-1)!}$ in [\[yamaguchilower\]](#yamaguchilower){reference-type="eqref" reference="yamaguchilower"} can be replaced by the volume of a regular ideal hyperbolic $n$--simplex. Second, if $X$ is an $n$-dimensional compact orientable geodesic space without boundary such that $K \ge -1$ in the sense of Alexandrov and $X$ is "locally Lipschitz contractible", then $$\|X\|\leq n!(n-1)^n\mathrm{Vol}(X),$$ where $\mathrm{Vol}(X)$ is the $n$-dimensional Hausdorff measure of $X$. Both bounds cannot be applied at once except in the manifold setting, since upper and lower curvature bounds can only coexist in a manifold. We do not use either bound in this paper, except in Remark [\[yamaguchiapp\]](#yamaguchiapp){reference-type="ref" reference="yamaguchiapp"} below.

We do not answer Question [\[q:manif\]](#q:manif){reference-type="ref" reference="q:manif"}, but we answer the analogous question for negatively curved pseudomanifolds:

::: question
[]{#q:pseud label="q:pseud"} Let $n\geq 4$. Fix $v>0$, and let $\mathcal{P}_{n,v}$ be the set of (homotopy classes of) closed locally CAT$(-1)$ $n$--pseudomanifolds whose simplicial volume is bounded above by $v$. Is $\mathcal{P}_{n,v}$ finite?
:::

Specifically, we apply a "Dehn filling" construction to give a negative answer to Question [\[q:pseud\]](#q:pseud){reference-type="ref" reference="q:pseud"}.

Let $M$ be a compact $n$--manifold with boundary a union of $m$ tori, whose interior $V = \mathrm{Int}(M)$ admits a complete hyperbolic metric of finite volume. Let $\overline{M}\cong M$ be a compact manifold obtained from $V$ by removing horospherical neighborhoods of the cusps. The manifold $\overline{M}$ has $m$ boundary components $N_1,\ldots,N_m$, each of which inherits a flat metric from the hyperbolic metric on $\mathrm{Int}(M)$. In [@FM1], we defined and studied *fillings* of $M$, which are topological spaces obtained by gluing the product of a torus with the cone on another torus to each boundary component of $\overline{M}$. Here is an equivalent definition.

::: definition
[]{#d:filling label="d:filling"} For each $i\in \{1,\ldots,m\}$, let $T_i<N_i$ be a $k_i$--dimensional submanifold which is totally geodesic in $N_i$. The $(n-1)$--torus $N_i$ is foliated by parallel copies of $T_i$, with leaf space $V_i$ homeomorphic to an $(n-1-k_i)$--dimensional torus. Let $h_i\colon\thinspace N_i\to V_i$ be the quotient map, and define $M(T_1,\ldots,T_m)$ to be the quotient $\overline{M}/\sim$, where $x\sim x'$ if $h_i(x)=h_i(x')$ for some $i$. The space $M(T_1,\ldots,T_m)$ is called a *filling of $M$*. If all of the tori $T_i$ have injectivity radius strictly larger than $\pi$, $M(T_1,\ldots,T_m)$ is called a *$2\pi$--filling of $M$*.
:::

In case $M$ is $3$--dimensional, and each $T_i$ is one-dimensional, fillings $M(T_1,\ldots,T_m)$ are the same as ordinary Dehn fillings of $M$. In [@FM1], we generalize work in [@BlHo; @Sc; @MS] (including the Gromov-Thurston $2\pi$ Theorem) to prove:

::: theorem
[]{#t:filling label="t:filling"}[@FM1] Let $M$ be an $n$--dimensional hyperbolic manifold as above. Every $2\pi$--filling $M(T_1,\ldots,T_m)$ of $M$ admits a locally CAT$(0)$ metric, so the universal cover is CAT$(0)$ with isolated flats. If every $T_i$ has dimension at least $n-2$, then $M(T_1,\ldots,T_m)$ admits a locally CAT$(-1)$ metric.
:::

Each filling of $M$ is a closed pseudomanifold with singular set equal to a disjoint union of tori of dimensions $n-(1+\dim(T_1)),\ldots
n-(1+\dim(T_m))$ (see Definition [\[d:pseudomanifold\]](#d:pseudomanifold){reference-type="ref" reference="d:pseudomanifold"} for these terms). In particular, its simplicial volume is well-defined [@Ya97]. The main result of the current paper is that these fillings have positive simplicial volume, bounded above by the simplicial volume of $M$.

::: theorem
[]{#t:volumedecreases label="t:volumedecreases"} Let $M$ be a compact $n$--manifold with boundary a union of $(n-1)$--tori, and suppose that $V=\mathrm{Int}(M)$ admits a complete hyperbolic metric of finite volume $\mathrm{Vol}(V)$. Let $M(T_1,\ldots,T_m)$ be a $2\pi$--filling of $\mathrm{Int}(M)$. Then $$0< \|M(T_1,\ldots,T_m)\| \leq \frac{\mathrm{Vol}(V)}{v_n},$$ where $v_n$ is the volume of a regular ideal hyperbolic $n$-simplex.
:::

::: corollary
The answer to Question [\[q:pseud\]](#q:pseud){reference-type="ref" reference="q:pseud"} is "no," for $v$ equal to the volume of any hyperbolic $n$--manifold with torus cusps.
:::

::: proof
*Proof.* Let $M$, $\overline{M}$, $N_1,\ldots,N_m$ be as in the discussion preceding Definition [\[d:filling\]](#d:filling){reference-type="ref" reference="d:filling"}. For each $j\in
  \{1,\ldots,m\}$, choose a sequence $\{T_i^j\}_{i\in\mathbb{N}}$ of totally geodesic codimension $1$ tori in $N_j$, all with $\mathrm{inj}>\pi$, and so that $\lim_{i\to\infty}\mathrm{inj}(T_i^j) = \infty$. Let $M_i$ be the filling $M(T_i^1,\ldots,T_i^m)$. Proposition 2.12 of [@FM1] implies that for any $i$ only finitely many $M_j$ have fundamental group isomorphic to $\pi_1M_i$, so the set $\{M_i\}_{i\in
    \mathbb{N}}$ contains infinitely many homotopy classes. Theorem [\[t:filling\]](#t:filling){reference-type="ref" reference="t:filling"} implies that $0<\|M_i\|\leq \frac{\mathrm{Vol}(V)}{v_n}$ for all $i$. ◻
:::

::: remark
In [@RT05], Ratcliffe and Tschantz describe some nonpositively curved $4$--dimensional homology spheres. These homology spheres are obtained by $2\pi$--filling of a cusped hyperbolic manifold described by Ivanšić in [@Iv]. They seem to be the first exmples of $4$--dimensional homology spheres with Riemannian metrics of non-positive sectional curvature (see the paragraph after Remark 5 in [@Na-We]). Belegradek in [@Be06] asked if these homology spheres have positive simplicial volume. Our main theorem answers this question affirmatively, but the main part of our argument is to do with the upper bound on simplicial volume. The reader primarily interested in positivity of simplicial volume can stop with Subsection [\[ss:norms\]](#ss:norms){reference-type="ref" reference="ss:norms"}. In particular, we answer Belegradek's question with Corollary [\[c:specialcase\]](#c:specialcase){reference-type="ref" reference="c:specialcase"} at the end of that subsection.
:::

It would be interesting to get some further information on the possible volumes of fillings of $M$. Hyperbolic Dehn filling of a $3$--manifold strictly decreases volume, and the volume difference goes to zero as the length of the filling slope goes to infinity (see [@Th 6.5.6] for strictness and [@NZ85; @HoKe; @FKP08] for estimates of the difference). We conjecture that similar phenomena hold in higher dimensions.

::: conjecture
The volumes $\|M(T_1,\ldots,T_m)\|$ accumulate on $\frac{\mathrm{Vol}(V)}{v_n}$ but do not attain it.
:::

::: question
Let $\epsilon>0$. Is there some $R$ so that if every torus $T_i$ has injectivity radius bigger than $R$, then $$\frac{\mathrm{Vol}(V)}{v_n}-\epsilon<\|M(T_1,\ldots,T_m)\|<\frac{\mathrm{Vol}(V)}{v_n}?$$
:::

::: question
Consider the set of fundamental groups of $2\pi$--fillings of $M$ as a subspace of the space of "marked groups" generated by some fixed set of generators of $\pi_1M$. Is the simplicial volume a continuous function on this space?
:::

::: remark
[]{#yamaguchiapp label="yamaguchiapp"} It is possible to analyze the metrics constructed in [@FM1] and apply Yamaguchi's inequality [\[yamaguchilower\]](#yamaguchilower){reference-type="eqref" reference="yamaguchilower"} to deduce that the CAT$(-1)$ fillings of a fixed $M$ have simplicial volume bounded away from zero, but this is about all we know for certain.
:::
