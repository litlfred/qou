---
doc_id: arxiv-0805.1447v2
doc_title: "Braid ordering and the geometry of closed braid"
section_id: sec-005-3-braid-foliation
section_title: "Braid Foliation"
section_number: 3
pages: 8-9
source_pdf: 0805.1447v2.pdf
source_sha256: b7ee20b0a7f5f3da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.894
latex_coverage_ratio: 0.989
doc_brief: "Braid ordering and the geometry of closed braid — The relationships between braid ordering and the ge- ometry of its closure is studied."
---
In this section, we summarize basic machinery of Birman-Menasco's braid foliation theory in case of an embedded essential surface. For details of these techniques, see [@bf] or [@bm2].

Fix an unknot $A \in S^{3}$, called *axis* and choose a meridian fibration $H = \{ H_{\theta}| \theta \in [0,2\pi]\}$ of the solid torus $S^{3} \backslash A$. A link $L$ in $S^{3} \backslash A$ is called *closed braid* with axis $A$ if $L$ intersects every fiber $H_{\theta}$ transversely and each fiber is oriented so that all intersections of $L$ are positive. It is easy to see closed braid $L$ intersects every fiber $H_{\theta}$ in the same number of points, and we call this number *braid index* of $L$. Note that closed braids $\widehat{\beta}$ obtained by a braid $\beta\in B_{n}$ as described in section 2 is indeed closed braid with $z-$axis and braid index is $n$. Conversely, if we cut solid torus $S^{3}\backslash A$ along the fiber $H_{0}$, we obtain a braid $\beta$. It is known that isotopy in $S^{3}\backslash A$ does not change conjugacy class of $\beta$ and if the isotopy fixes $H_{0}\cap \widehat{\beta}$, obtained braid $\beta$ does not change as a element of braid group though geometrical configuration of strands are varied.

A closed embedded surface $F$ in $S^{3} \backslash A$ is called *essential* if $F$ is incompressible and non-boundary parallel. Let $F$ be a essential closed surface in $S^{3} \backslash L$. Then the intersections of fiber $\{H_{\theta}\}$ with $F$ induce a singular foliation of $F$. Leaves of this foliation are connected components of intersection with fiber. Braid foliation techniques are, in short, changing this foliation simpler as possible and obtain standard and simple position of the surface and braids. By the argument in [@bf], $F$ can be isotoped to \"general\" position with respect to the fibration satisfying:

\(1\)

:   Axis $A$ pierces $F$ transversely in finitely many points.

\(2\)

:   For each point $v \in A\cap F$, there exists neighborhood $N_{v}$ of $v$ such that $F\cap N_{v}$ is radially foliated disc.

\(3\)

:   All but finitely many fibers $H_{\theta}$ intersect $F$ transversely, and each of the exceptional fiber is tangent to $F$ exactly one point. Moreover, each point of tangency is saddle tangency and lies in the interior of $F \cap H_{\theta}$.

Notice that the condition above is a bit stronger than usual general position arguments, since usual general position arguments only tell us that each tangency is local minimum, maximum, or saddle. In fact, this strong sense of general position is achieved from usual general position by deleting local minimum or maximum tangency.

We say fiber $H_{\theta}$ *regular* if $H_{\theta}$ transverse $F$ and *singular* if $H_{\theta}$ tangent to $F$. In the foliation of $F$, every non-singular leaf of induced foliation is either simple closed curve or arc which has both endpoints on axis $A$. We call former *c-circle* and the latter *b-arc*. Each b-arc in a fiber $H_{\theta}$ separates $H_{\theta}$ to two components, and we say b-arc is *essential* if both of these components are pierced at least once by $L$. For c-circle in a fiber $H_{\theta}$, c-circle bound a disc $D$ in $H_{\theta}$ and we say c-circle is *essential* if $D$ is pierced at least once by $L$. As shown in [@bf], we can assume further more condition about foliation of $F$.

\(4\)

:   every fiber is essential.

\(5\)

:   every c-circle is homotopically non-trivial.

This condition is achieved by deleting all inessential leaves or homotopically trivial c-circle. From now on, we always assume that $F$ satisfies condition (1)$-$(5).

We call an intersection point of $A$ with $F$ *vertex*. For each vertex $p$, the valance of vertex $p$ is, by definition, the number of singular leaves which pass $p$. We say singular point is $bb-singularity$ if the singular point derived from two b-arcs. $bc-singularity$ and $cc-singularity$ are defined by the same way. Each type of singularity has a neighborhood in $F$ as shown in figure [1](#fig:regions){reference-type="ref" reference="fig:regions"}, and we say such a neighborhood *regions*.

A foliation of $F$ is classified into following three types according to its containing leaves; We say $F$ is *tiled* if $F$ is foliated entirely b-arc and *circular* if $F$ is foliated entirely c-circle. The remaining case, if $F$ is foliated by both b-arcs and c-circles, we say $F$ is *mixed*. In tiled surface, there are only bb-singularity and circular surface has only cc-singularity. Mixed foliation might have all types of singularity and always contains bc-singularity.

<figure id="fig:regions">
<div class="center">
<embed src="tile.eps" style="width:120mm" />
</div>
<figcaption>bb-tile,bc-annulus,cc-pants</figcaption>
</figure>

# Proof of theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"}

Now we are ready to prove theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"}. From now on, we always assume $F$ satisfies all conditions (1)-(5) described in section 3. First we consider the case $g=0$. In this case, $F$ is never circular foliated. The main result of [@bm1] shows in this case $\widehat{\beta}$ admit exchange move if $F$ is tiled and $\beta$ has word representatives which contains no $\sigma_{k}^{\pm1}$ for some $k$, so $[\beta]_{D}=0$. Thus, in this case theorem holds. Thus, we always assume $g>0$.
