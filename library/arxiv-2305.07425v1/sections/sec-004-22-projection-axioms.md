---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-004-22-projection-axioms
section_title: "Projection axioms"
section_number: 2.2
pages: 5-6
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.969
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a group G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
[]{#sec:projaxioms label="sec:projaxioms"} We will use the Bestvina--Bromberg--Fujiwara projection complex machinery developed in [@BBF15] to obtain actions on quasi-trees. In this section, we review this machinery.

::: defn
[]{#defn:Projectionaxioms label="defn:Projectionaxioms"}

Let $\mathbb{Y}$ be a collection of geodesic spaces equipped with projection maps $$\{\pi_{Y}\colon  \mathbb Y\setminus \{Y\}\to Y\}_{Y\in \mathbb Y}.$$ Let $d_{Y}(X,Z) = \operatorname{diam} (\pi_{Y}(X) \cup \pi_{Y}(Z))$ for $X\ne Y\ne Z \in \mathbb{Y}$. The pair $(\mathbb{Y}, \{\pi_{Y}\}_{Y\in\mathbb Y})$ satisfies the *projection axioms* for a *projection constant* $\xi \ge 0$ if

1.  []{#axiom1 label="axiom1"} $\operatorname{diam} (\pi_{Y}(X)) \le \xi$ whenever $X \neq Y$;

2.  []{#axiom2 label="axiom2"} if $X,Y,Z$ are distinct and $d_{Y}(X, Z) > \xi$, then $d_{X}(Y,Z) \le \xi$; and

3.  []{#axiom3 label="axiom3"} for $X \neq Z$, the set $\{ Y \in \mathbb{Y} \,\mid \, d_{Y}(X, Z) > \xi \}$ is finite.
:::

For a fixed $K>0$ and a pair $(\mathbb{Y}, \pi_{Y})$ satisfying the projection axioms for some constant $\xi$, Bestvina, Bromberg, and Fujiwara construct a *quasi-tree of spaces* $\mathcal C_K(\mathbb Y)$ in [@BBF15]. If $\mathbb Y$ admits an action of the group $G$ so that $\pi_{gY} (gX)=g\pi_Y(X)$ for any $g\in G$ and $X,Y\in \mathbb Y$, then $G$ acts by isometries on $\mathcal C_K(\mathbb Y)$; see Section 4.4 in [@BBF15]. Moreover, they show that if $K>4\xi$ and $\mathbb Y$ is a collection of metric spaces uniformly quasi-isometric to $\mathbb R$, then $\mathcal C_K(\mathbb Y)$ is an unbounded quasi-tree [@BBF15 Theorem 4.14].

The following is a useful example to keep in mind throughout the paper and is discussed in detail in the introduction of [@BBF15].

::: exmp
[]{#ex:linesinhypplane label="ex:linesinhypplane"} Let $G$ be a discrete group of isometries of $\mathbb H^2$ and $g_1,\dots, g_k\in G$ a finite collection of loxodromic elements with axes $\gamma_1,\dots, \gamma_k$, respectively. Let $\mathbb Y$ be the set of all $G$--translates of $\gamma_1,\dots, \gamma_k$, and given $Y\in \mathbb Y$, define $\pi_Y$ to be closest point projection in $\mathbb H^2$. Since all translates of each $\gamma_i$ are convex, this is a well-defined $1$--Lipschitz map, and it follows from hyperbolicity that the projection of one translate of an axis onto another has uniformly bounded diameter. In [@BBF15] it is verified that the pair $(\mathbb Y,\pi_Y)$ satisfies the projection axioms for some constant $\xi$.
:::

Given a pair $(\mathbb Y,\{\pi_Y\}_{Y\in\mathbb Y})$ satisfying the projection axioms and three domains $X,Y,Z\in \mathbb Y$, there is a notion of distance between a point of $X$ and a point of $Z$ from the point of view of $Y$, which we now describe. Let $x\in X$ and $z\in Z$. If $X,Y,Z$ are all distinct, then define $d_Y(x,z)\vcentcolon=d_Y(X,Z)$. If $Y=X$ and $Y\ne Z$, then define $d_Y(x,z)\vcentcolon=\operatorname{diam}(\{x\}\cup\pi_Y(z))$, where the diameter is measured in $Y$. Finally, if $X=Y=Z$, then let $d_Y(x,z)$ be the distance in $Y$ between $x$ and $z$. The spaces $Y\in \mathbb Y$ naturally embed into $\mathcal C_K(\mathbb Y)$, so the distance $d_{\mathcal C_K(\mathbb Y)}(x,z)$ is also defined.

We have the following upper bound on distance in $\mathcal C_K(\mathbb Y)$. Set $[t]_K=t$ if $t\ge K$ and $[t]_K=0$ if $t<K$.

::: prop
[]{#prop:BBFDistanceProp label="prop:BBFDistanceProp"} Let $(\mathbb Y, \pi_{Y\in \mathbb Y})$ satisfy the projection axioms with constant $\xi$. For any $K$ sufficiently large, $$d_{\mathcal C_K(\mathbb Y)}(x, z) \leq 6K + 4 \sum_{Y \in \mathbb Y} [d_Y(x,z)]_K.$$
:::

This distance formula was originally stated with a modified distance function. In [@BBF15] the distance defined above was denoted $d_Y^\pi$, and the modified distance was denoted $d_Y$. However, since $d_Y(x,z)\leq d_Y^\pi(x,z)$ for all point $x,z$, the inequality holds with the distance $d_Y^\pi$, as well. As we will not need the modified distance function in this paper, we use the simpler notation $d_Y$ for $d_Y^\pi$ and choose to state the proposition with this distance.
