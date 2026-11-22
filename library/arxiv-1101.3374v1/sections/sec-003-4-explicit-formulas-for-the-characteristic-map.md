---
doc_id: arxiv-1101.3374v1
doc_title: "Pontryagin invariants and integral formulas for Milnor's triple linking number"
section_id: sec-003-4-explicit-formulas-for-the-characteristic-map
section_title: "Explicit formulas for the characteristic map"
section_number: 4
pages: 20-25
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.951
doc_brief: "Pontryagin invariants and integral formulas for Milnor's triple linking number — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
---
[]{#sec:characteristic label="sec:characteristic"}

In this section we give an explicit diffeomorphism from the Grassmann manifold $\mathrm{G}_2\mathbb R^4$ of oriented $2$-planes through the origin in $4$-space to a product of two $2$-spheres, and then use it to give a formula for the characteristic map $g_L:T^3\to S^2$ of a three-component link $L$ in the $3$-sphere.

We also describe an alternative form $h_L:T^3\to S^2$ of the characteristic map, homotopic to $g_L$ but more convenient for the proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} that we will give in Section [\[sec:A\]](#sec:A){reference-type="ref" reference="sec:A"}. The formula for $h_L$ will reveal a close connection between the characteristic map and the classical Gauss map $T^2\to S^2$ for two-component links in $3$-space.

Throughout we regard $\mathbb R^4$ as the algebra of ***quaternions***, with orthonormal basis $1,i,j,k$ and unit sphere $S^3$ (oriented so that $i,j,k$ is a positive frame for the tangent space to $S^3$ at the point $1$), and $\mathbb R^3$ as the subspace of ***pure imaginary quaternions*** spanned by $i$, $j$ and $k$, with unit sphere $S^2$. Thus $S^3$ is viewed as the multiplicative group of unit quaternions, and $S^2$ as the subset of pure imaginary unit quaternions.

For any quaternion $q = q_0+q_1i+q_2j+q_3k$, let $\bar q$ denote its conjugate $q_0-q_1i-q_2j-q_3k$, which coincides with $q^{-1}$ when $q\in S^3$, and let $\mathrm{Re\,}(q) = q_0$ and $\mathrm{Im\,}(q)=q_1i+q_2j+q_3k$ denote its real and imaginary parts.

It is well known

that $\mathrm{G}_2\mathbb R^4$ can be identified with a product of two $2$-spheres. In particular, we will use the diffeomorphism $$\pi: \mathrm{G}_2\mathbb R^4\longrightarrow S^2\times S^2$$ that maps the oriented plane $\langle a,b\rangle$, spanned by an orthonormal $2$-frame $(a,b)$ in $\mathbb R^4$, to the point $(b\bar a,\bar ab)$ in $S^2\times S^2$. Note that both coordinates $$\pi_+\langle a,b\rangle \ = \ b\bar a \qquad\text{and}\qquad \pi_-\langle a,b\rangle \ = \ \bar ab$$ do in fact lie in $S^2$ since right and left multiplication by $\bar a$ are orthogonal transformations of $\mathbb R^4$, carrying the orthonormal frame $(a,b)$ to the orthonormal frames $(1,b\bar a)$ and $(1,\bar ab)$.

To see that $\pi$ is well-defined, consider any other orthonormal basis for the plane $\langle a,b\rangle$. It must be of the form $(ac,bc)$ for some $c$ in the circle subgroup $C_{\bar ab}$ through $\bar ab$, since this group acts on the plane by rotations. Thus it suffices to check that $bc\,\overline{ac} = b\bar a$, which is immediate, and that $\overline{ac}\, bc = \bar ab$, which is true since $c$ commutes with $\bar ab$.

To see that $\pi$ is in fact a diffeomorphism, we can simply write down the inverse. It maps a pair $(x,y)$ in $S^2\times S^2$ to the plane $\langle c,cy\rangle$ where $c$ is the midpoint of any geodesic arc from $x$ to $y$ on $S^2$. This can be verified by a straightforward calculation using the fact that conjugation by a pure imaginary quaternion rotates the $2$-sphere about that quaternion by $\pi$ radians, so $cy\bar c = x$.

Recall from the introduction that the Grassmann map $G:\mathrm{Conf}_{3}S^3\to\mathrm{G}_2\mathbb R^4$ sends a triple $(x,y,z)$ of distinct points in $S^3$ to the plane they span in $\mathbb R^4$, translated to pass through the origin, and oriented so that $$G(x,y,z) \ = \ \langle x-z,y-z\rangle.$$ We have extended notation so that for *any* two linearly independent vectors $a$ and $b$ in $\mathbb R^4$, the symbol $\langle a,b\rangle$ denotes the oriented plane they span. Then, given a three-component link $L$ in $S^3$, its characteristic map $g_L:T^3\to S^2$ is defined using the Grassmann map $G$ and the projection $\pi_+:\mathrm{G}_2\mathbb R^4\to S^2$ by the formula $$g_L(s,t,u) \ = \ \pi_+G(x,y,z) \ = \ \pi_+\langle x-z,y-z\rangle$$ where $x=x(s)$, $y=y(t)$ and $z=z(u)$ parametrize the components of $L$.

To make this explicit, and to show that using $\pi_-$ in place of $\pi_+$ in the definition would not change the homotopy class of $g_L$, we need expressions for $\pi_\pm\langle a,b\rangle$ when $a$ and $b$ are arbitrary linearly independent vectors in $\mathbb R^4$, but not necessarily orthonormal.

For example, if $a$ and $b$ are orthogonal, then $b\bar a$ and $\bar ab$ are still pure imaginary, and so need only be normalized to give $\pi_+\langle a,b\rangle$ and $\pi_-\langle a,b\rangle$.

For a general pair of linearly independent vectors $a$ and $b$, the vector $c = b-(b\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}a/a\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}a)a$, where $\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}$ is the dot product in $\mathbb R^4$, is orthogonal to $a$ and satisfies $\langle a,c\rangle = \langle a,b\rangle$. Therefore $\pi_+\langle a,b\rangle = \pi_+\langle a,c\rangle$, which equals the unit normalization of the vector $c\bar a = b\bar a - b\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}a$. But $b\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}a = \mathrm{Re\,}(b\bar a)$, and so $\pi_+\langle a,b\rangle$ is the unit normalization of $\mathrm{Im\,}(b\bar a)$. Similarly $\pi_-\langle a,b\rangle$ is the unit normalization of $\mathrm{Im\,}(\bar ab)$. Therefore, for *any* two linearly independent vectors $a$ and $b$, we have $$\pi_\pm\langle a,b\rangle \ = \ (a,b)_\pm / |(a,b)_\pm|$$ where $(\,,\,)_\pm$ are the skew symmetric bilinear forms on $\mathbb R^4$ defined by $$(a,b)_+ \ = \ \mathrm{Im\,}\,b\bar a \qquad\text{and}\qquad (a,b)_- \ = \ \mathrm{Im\,}\,\bar ab\,.$$

It follows that $g_L(s,t,u)$ is the unit normalization of the vector $$\begin{aligned}
F(x,y,z) \ &= \ (x-z,y-z)_+ \ = \ (x,y)_+ + (y,z)_+ + (z,x)_+ \\
&= \ (ix\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}y + iy\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}z + iz\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}x \ , \  jx\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}y + jy\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}z + jz\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}x \ , \  kx\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}y + ky\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}z + kz\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}x)
\end{aligned}$$ where the last expression follows from the formula $(a,b)_+ = (ia\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b, ja\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b, ka\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b)$. This formula is seen as follows. By definition, $(a,b)_+ = \mathrm{Im\,}(b\bar a)  =  (i\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b\bar a)i + (j\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b\bar a)j + (k\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b\bar a)k$. But $q\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b\bar a = qa\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b$ for any $q$ (in particular $i$, $j$ or $k$) since right multiplication by the unit quaternion $a/|a|$ is an isometry, and so $(a,b)_+ = (ia\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b)i + (ja\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b)j + (ka\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b)k = (ia\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b, ja\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b, ka\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}b)$.

Summarizing, we have shown:

::: proposition
[]{#prop:char label="prop:char"} **The characteristic map $g_L:T^3\to S^2$ of a three-component link $L$ in $S^3$ is given by the formula $$g_L(s,t,u) \ = \ F(x,y,z)/|F(x,y,z)|$$ where $x = x(s)$, $y = y(t)$ and $z = z(u)$ parametrize the components of $L$, and $F:\mathrm{Conf}_{3}S^3\to\mathbb R^3$ is the function defined above.**
:::

This formula for $g_L$ will be used in our proof of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} in Sections [\[sec:B\]](#sec:B){reference-type="ref" reference="sec:B"} and [\[sec:B\'\]](#sec:B'){reference-type="ref" reference="sec:B'"}. For Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} it will be more convenient, for the most part, to use an alternative form of the characteristic map that we introduce next.

Given a three-component link $L$ in the $3$-sphere, we define below an asymmetric version $$h_L:T^3\longrightarrow S^2$$ of the characteristic map in which the last component of $L$ plays a distinguished role, and show that it is homotopic to the earlier defined symmetric characteristic map $g_L$. As will be seen, the map $h_L$ can be viewed as a parametrized family of Gauss maps for twisted versions of the first two components of $L$, parametrized by the third component.

For notational economy, we will use $\lceil\!\!\!\hskip.01in \lfloor q \rceil\!\!\!\hskip.01in\rfloor$ to denote the unit normalization $q/|q|$ of any nonzero quaternion $q$.

The key observation that motivates the definition of $h_L$ is that the Grassmann map $G:\mathrm{Conf}_{3}S^3\to\mathrm{G}_2\mathbb R^4$ factors up to homotopy through the ***Stiefel manifold*** $\mathrm{V}_2\mathbb R^4$ of orthonormal $2$-frames in $4$-space.

More precisely, let $\mathrm{pr}_z$ denote ***stereographic projection*** of $S^3-\{z\}$ onto $z^\perp$, the $3$-plane through the origin in $\mathbb R^4$ orthogonal to $z$. Then we define the ***Stiefel map*** $$H:\mathrm{Conf}_{3}S^3\longrightarrow\mathrm{V}_2\mathbb R^4\quad,\quad (x,y,z) \longmapsto (z,\lceil\!\!\!\hskip.01in \lfloor \mathrm{pr}_zx-\mathrm{pr}_zy \rceil\!\!\!\hskip.01in\rfloor)$$ (recall that the square brackets signify unit normalization), and will show that it is a homotopy equivalence whose composition with the canonical projection $$P:\mathrm{V}_2\mathbb R^4\longrightarrow\mathrm{G}_2\mathbb R^4\quad,\quad (z,v)\longmapsto\langle z,v\rangle$$ is homotopic to the Grassmann map $G$.

To see this, first observe that there is a deformation retraction of $\mathrm{Conf}_{3}S^3$ to its subspace $$V  \ = \ \{(v,-z,z) \ | \ v\perp z\}$$ defined as follows. Start with $(x,y,z)\in\mathrm{Conf}_{3}S^3$, and consider the points $\mathrm{pr}_zx$ and $\mathrm{pr}_zy$ in $z^\perp$. Translation in $z^\perp$ moves $\mathrm{pr}_zy$ to the origin, and then dilation in $z^\perp$ makes the translated $\mathrm{pr}_zx$ into a unit vector. Conjugating this motion by $\mathrm{pr}_z$ moves $x$ to $\lceil\!\!\!\hskip.01in \lfloor \mathrm{pr}_zx-\mathrm{pr}_zy \rceil\!\!\!\hskip.01in\rfloor$, moves $y$ to $-z$, and leaves $z$ fixed, as pictured in Figure [1](#fig:stfl){reference-type="ref" reference="fig:stfl"}, thus defining a deformation retraction of $\mathrm{Conf}_{3}S^3$ to its subspace $V$, sending $(x,y,z)$ to $(\lceil\!\!\!\hskip.01in \lfloor \mathrm{pr}_zx-\mathrm{pr}_zy \rceil\!\!\!\hskip.01in\rfloor,-z,z)$.

<figure id="fig:stfl">
<p><embed src="FigRT.pdf" style="height:2.08333in" /> (-127,136)<span><span class="math inline"><em>z</em></span></span> (-105,18)<span><span class="math inline"> − <em>z</em></span></span> (-80,103)<span><span class="math inline"><em>x</em></span></span> (-92,123)<span><span class="math inline"><em>y</em></span></span> (-40,72)<span><span class="math inline">pr<sub><em>z</em></sub><em>x</em></span></span> (-30,100)<span><span class="math inline">pr<sub><em>z</em></sub><em>y</em></span></span> (-187,45)<span><span class="math inline"><em>z</em><sup>⊥</sup></span></span> (-145,90)<span><span class="math inline"><em>S</em><sup>3</sup></span></span> (-150,0)<span><span class="math inline">$\lceil\!\!\!\hskip.01in \lfloor \mathrm{pr}_zx-\mathrm{pr}_zy \rceil\!\!\!\hskip.01in\rfloor \ = \ (\mathrm{pr}_zx-\mathrm{pr}_zy)/|\mathrm{pr}_zx-\mathrm{pr}_zy|$</span></span></p>
<figcaption>The deformation retraction <span class="math inline">Conf<sub>3</sub><em>S</em><sup>3</sup> → <em>V</em></span></figcaption>
</figure>

Identifying $V$ with $\mathrm{V}_2\mathbb R^4$ via $(v,-z,z)\leftrightarrow(z,v)$, this shows that $H$ is a homotopy equivalence with homotopy inverse $I$ given by $I(z,v) = (v,-z,z)$. The calculation $$GI(z,v) \ = \ \langle v-z,-2z\rangle \ = \ \langle z,v\rangle \ = \ P(z,v)\,,$$ shows that $GI=P$, and so $G\simeq PH$ as claimed.

Now observe that there are two natural homeomorphisms from the Stiefel manifold $\mathrm{V}_2\mathbb R^4$ to $S^3\times S^2$ that arise from viewing $S^3$ as the unit quaternions and $S^2$ as the pure imaginary unit quaternions, namely $(z,v) \mapsto (z,v\bar z)$ and $(z,v)\mapsto (z,\bar zv)$. These yield projections $\pi_\pm:\mathrm{V}_2\mathbb R^4\to S^2$ given by $$\pi_+(z,v) \ = \ v\bar z \qquad\text{and}\qquad \pi_-(z,v) =  \bar zv.$$ These are just the lifts to $\mathrm{V}_2\mathbb R^4$ of the previously defined projections $\pi_\pm:\mathrm{G}_2\mathbb R^4\to S^2$ with the same names.

Define the ***asymmetric characteristic map*** $h_L:T^3\to S^2$ to be the composition $\pi_+He_L$, that is, $$h_L(s,t,u) \ = \ \lceil\!\!\!\hskip.01in \lfloor \mathrm{pr}_zx-\mathrm{pr}_zy \rceil\!\!\!\hskip.01in\rfloor\, \bar z$$ where as usual $x=x(s)$, $y=y(t)$ and $z=z(u)$ parametrize the components of $L$, and the square brackets indicate unit normalization.

::: proposition
[]{#prop:asymmetric label="prop:asymmetric"} **The two versions $g_L$ and $h_L$ of the characteristic map of a three-component link $L$ in $S^3$ are homotopic. Furthermore, these maps are independent, up to homotopy, of the choice of projections $\pi_+$ or $\pi_-$ used in their definitions.**
:::

::: proof
*Proof.* By definition $g_L = \pi_+Ge_L$ and $h_L = \pi_+He_L$, shown in the diagram below as the maps from left to right across the bottom and top, respectively. -.1in

::: diagram
&&&& \_2R\^4&&\
&&& \^H  && \^\_+ &\
T\^3 & \_e_L &  \_3S\^3   && \_P &&  S\^2\
&&& \_G &&  \_\_+\[rightshortfall=10pt\] &\
&&&& \_2R\^4&&\
:::

.1in Here $e_L(s,t,u)=(x(s),y(t),z(u))$ records the parametrization of the link, and $G$ and $H$ are the Grassmann and Stiefel maps with their associated projections $\pi_+$. It was shown above that the left triangle in the diagram commutes up to homotopy, and the right triangle commutes on the nose. Therefore $h_L$ and $g_L$ are homotopic.

Now the same argument shows that the maps $h_L' = \pi_-He_L$ and $g_L' =  \pi_-Ge_L$ are homotopic. Hence to complete the proof, it suffices to show that $h_L$ and $h_L'$ are homotopic. To do so, view $\mathrm{V}_2\mathbb R^4$ as the unit tangent bundle of $S^3$, with projection $p$ to the base $S^3$ given by $p(z,v) = z$. Then the composition $pHe_L$ is null-homotopic, since it maps onto the third component of $L$, and so the map $He_L$ is homotopic to a map into any $S^2$-fiber of the bundle $\mathrm{V}_2\mathbb R^4\to S^3$. We choose the fiber over $z=1$, where the two projections $\pi_+(z,v) = v\bar z$ and $\pi_-(z,v) = \bar zv$ coincide. It follows that $h_L$ and $h_L'$ are homotopic. ◻
:::

The formula above for $h_L$ involves first normalizing a vector in $z^\perp$, and then multiplying by $\bar z$ to move it to the unit sphere $S^2$ in the pure imaginary quaternion $3$-space $\mathbb R^3$. We would like to express this directly as the normalization of a vector in $\mathbb R^3$.

A geometric argument shows that stereographic projection $\mathrm{pr}_a$ is given by $$\mathrm{pr}_ab \ = \ (\mathrm{Im\,}\,b\bar a)a/(1-\mathrm{Re\,}\,b\bar a)$$ and it follows that $(\mathrm{pr}_ab)c  = \mathrm{pr}_{ac}\,bc$ for any three unit quaternions $a$, $b$ and $c$ with $a\ne b$. Hence the formula $h_L(s,t,u) = \lceil\!\!\!\hskip.01in \lfloor \mathrm{pr}_zx-\mathrm{pr}_zy \rceil\!\!\!\hskip.01in\rfloor\, \bar z$ can be rewritten as $$\begin{aligned}
h_L(s,t,u) \ &= \ \lceil\!\!\!\hskip.01in \lfloor \mathrm{pr}_1\,x\bar z- \mathrm{pr}_1\,y\bar z \rceil\!\!\!\hskip.01in\rfloor \\
&= \ \lceil\!\!\!\hskip.01in \lfloor \mathrm{pr}_{-1}(-y\bar z) - \mathrm{pr}_{-1}(-x\bar z) \rceil\!\!\!\hskip.01in\rfloor
\end{aligned}$$ where, as usual, $x=x(s)$, $y=y(t)$ and $z=z(u)$ parametrize $L$, and the square brackets indicate unit normalization in $\mathbb R^3$. We favor the last expression because stereographic projection from $-1$ is orientation-preserving, while from $1$ it is orientation-reversing.

Now for any two distinct unit quaternions $a$ and $z$, introduce the abbreviation $$a_z \ = \ \mathrm{pr}_{-1}(-a\bar z) \ \in \ \mathbb R^3\,,$$ and so in particular $a_{-1} = \mathrm{pr}_{-1}\,a$. Then we can write $$h_L(s,t,u) \ = \ \lceil\!\!\!\hskip.01in \lfloor y_z-x_z \rceil\!\!\!\hskip.01in\rfloor\,.$$ For fixed $u$, this is just the classical Gauss map for the two-component link $X_z\cup Y_z \subset \mathbb R^3$ that is the image of the first two components $X\cup Y$ of $L$ under the map $a\mapsto a_z$. Thus the asymmetric characteristic map $h_L$ can be viewed as a one-parameter family of Gauss maps for images in $3$-space of $X\cup Y$. The third component $Z$ provides the parameter and determines the axes about which these images are gradually twisted.

In the next section, we will explain this perspective more carefully. But we can see right now that it yields an easy proof of the first part of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}, equating the pairwise linking numbers of the link $L$ with the degrees of the restriction of its characteristic map $g_L$ to the coordinate $2$-tori.

It can be arranged by an isotopy of $L$ that $z(0) = -1$. Then the restriction of $h_L$ to the coordinate $2$-torus $S^1\times S^1\times 0$ is precisely the Gauss map of the stereographic image $X_{-1}\cup Y_{-1}$ of $X\cup Y$, whose degree is equal to the linking number $\mathrm{Lk}(X, Y )$ since $\mathrm{pr}_{-1}$ is orientation-preserving. Since $g_L$ is homotopic to $h_L$, the same is true for $g_L$. But then it follows from the symmetry of $g_L$ that $\mathrm{Lk}(X,Z)$ and $\mathrm{Lk}(Y,Z)$ are given by the degrees of $g_L$ on $S^1\times 0\times S^1$ and on $0 \times S^1\times S^1$, respectively.

The proof of the second statement in Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} -- which relates the triple linking number of $L$ to the Pontryagin $\nu$-invariant of its characteristic map -- is more delicate. It will occupy us for the next two sections.
