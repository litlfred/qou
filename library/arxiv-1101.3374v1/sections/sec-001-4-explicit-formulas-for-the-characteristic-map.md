---
doc_id: arxiv-1101.3374v1
doc_title: "Pontryagin invariants and integral formulas for Milnor's triple linking number"
section_id: sec-001-4-explicit-formulas-for-the-characteristic-map
section_title: "Explicit formulas for the characteristic map"
section_number: 4
pages: 20-57
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.965
doc_brief: "Pontryagin invariants and integral formulas for Milnor's triple linking number — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
---
[]{#sec:characteristic label="sec:characteristic"}

In this section we give an explicit diffeomorphism from the Grassmann manifold $\mathrm{G}_2\mathbb R^4$ of oriented $2$-planes through the origin in $4$-space to a product of two $2$-spheres, and then use it to give a formula for the characteristic map $g_L:T^3\to S^2$ of a three-component link $L$ in the $3$-sphere.

We also describe an alternative form $h_L:T^3\to S^2$ of the characteristic map, homotopic to $g_L$ but more convenient for the proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} that we will give in Section [2](#sec:A){reference-type="ref" reference="sec:A"}. The formula for $h_L$ will reveal a close connection between the characteristic map and the classical Gauss map $T^2\to S^2$ for two-component links in $3$-space.

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

This formula for $g_L$ will be used in our proof of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} in Sections [4](#sec:B){reference-type="ref" reference="sec:B"} and [5](#sec:B'){reference-type="ref" reference="sec:B'"}. For Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} it will be more convenient, for the most part, to use an alternative form of the characteristic map that we introduce next.

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

# The Pontryagin $\nu$-invariant of the characteristic map {#sec:Aprep}

Fix a link $L$ in $S^3$ with three components $X$, $Y$ and $Z$ parametrized by $x=x(s)$, $y=y(t)$ and $z=z(u)$. Recalling that $S^3$ is regarded as the group of unit quaternions, the asymmetric characteristic map $h_L:T^3\to S^2$ is given by $$h_L(s,t,u) \ = \ (y_z-x_z)/|y_z-x_z|$$ where $a_z$ is an abbreviation for the vector $\mathrm{pr}_{-1}(-a\bar z)$ in pure imaginary quaternion $3\text{-space}$ $\mathbb R^3$. To carry out the proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}, we need a way to compute the absolute Pontryagin $\nu$-invariant of $h_L$. A procedure for doing so is described here.

Throughout this section and the next, $\mathbb R^3$ is pictured in the usual way, with the $ij$-plane horizontal and the $k$-axis pointing straight up as in Figure [2](#fig:quat){reference-type="ref" reference="fig:quat"}. In particular, we view $k$ as the north pole of the unit sphere $S^2$.

<figure id="fig:quat">
<p><embed src="Figijk.pdf" style="height:2.08333in" /> (-99,40)<span><span class="math inline"><em>i</em></span></span> (-33,58)<span><span class="math inline"><em>j</em></span></span> (-89,117)<span><span class="math inline"><em>k</em></span></span></p>
<figcaption>Pure imaginary quaternion <span class="math inline">3</span>-space</figcaption>
</figure>

First, we will manipulate $L$ by a link homotopy into a favorable position -- referred to as ***generic*** below -- so that, in particular, the north pole $k$ of $S^2$ is a regular value of $h_L$.

Then we will determine the associated ***Pontryagin link*** $$\mathcal L\ = \ h_L^{-1}(k) \ \subset \ T^3$$ by giving a simple method for constructing a toral diagram for it, in the sense of Section [\[sec:pontryagin\]](#sec:pontryagin){reference-type="ref" reference="sec:pontryagin"}. Roughly speaking, our approach is as follows.

By definition of $h_L$, the Pontryagin link $\mathcal L$ consists of all $(s,t,u)\in T^3$ for which the vector in $\mathbb R^3$ from $x_z$ to $y_z$ points straight up, where $x=x(s)$, $y=y(t)$ and $z=z(u)$. The genericity of $L$ will imply that for some points $(s,t)$ in the $2$-torus $T^2$ there is a *unique* $u = u(s,t)\in S^1$ that will make this happen, while for all other points $(s,t)$, *no* $u$ will work. Furthermore, the set $\mathcal D$ of all points of the first kind, called ***isogonal points*** for reasons explained below, is a smooth $1$-dimensional submanifold of $T^2$ whose components we call ***icycles***.

Thus $$\mathcal L\ = \ \{(s,t,u)\in T^3\ | \ (s,t)\in\mathcal D\text{ and } u=u(s,t)\}\,,$$ the graph of the function $u(s,t)$ over the collection $\mathcal D$ of icycles in $T^2$. When suitably oriented and decorated with framing and vertical winding numbers, $\mathcal D$ will be the desired toral diagram of $\mathcal L$.

In particular, the icycles in $\mathcal D$ correspond to certain oriented cycles of vectors directed from $X$ to $Y$, which we call ***bicycles***, that are easily spotted from a picture of $L$. Each bicycle has a ***longitudinal*** and ***meridional degree***, recording how much it turns and spins relative to the standard open book structure on $S^3$. The framing and vertical winding number of the corresponding icycle are determined by these degrees.

Therefore a diagram for $\mathcal L$ can be constructed once we identify the bicycles in $L$. With this diagram in hand, the methods of Section [\[sec:pontryagin\]](#sec:pontryagin){reference-type="ref" reference="sec:pontryagin"} can then be used to compute $\nu(h_L)$.

We now give the details of this procedure. There are three geometries involved: spherical geometry in $S^3$, where the link $L$ lives, Euclidean geometry in $\mathbb R^3$, the setting for the asymmetric characteristic map, and hyperbolic geometry in the complex upper half plane $\mathbb H$, which turns out to be for us the natural geometry on the pages of the "standard\" open book decomposition of $\mathbb R^3$. We begin with an explicit construction of this open book, which provides a framework for the discussion that follows.

Consider the great circle $K$ in $S^3$ through $1$ and $k$, and the orthogonal great circle $C$ through $i$ and $j$. Orient both circles by left complex multiplication by $K$ (i.e. from $1$ toward $k$ on $K$, and $i$ toward $j$ on $C$) so that their linking number is $+1$.

Stereographic projection from $-1$ carries $K$

onto the $k$-axis in $\mathbb R^3$, and fixes $C$, which now appears as the unit circle in the $ij$-plane. The complement $\mathbb V$ of the $k$-axis in $\mathbb R^3$ is naturally identified with the product of a circle $S^1$ (viewed as the quotient $\mathbb R/2\pi\mathbb Z$) with the complex upper half plane $\mathbb H$ (which for later purposes will be viewed as the hyperbolic plane) via the diffeomorphism

$$\mathbb V\ \longrightarrow \ S^1 \times \mathbb H$$ with coordinates  $\ell: \mathbb V\longrightarrow S^1$  and  $m: \mathbb V\longrightarrow\mathbb H$  given by $$\ell(q) \ = \ \arg(q_1+q_2i)\qquad\text{and}\qquad m(q) \ = \ q_3 + |q_1+q_2i|i\,.$$ for $q=q_1i+q_2j+q_3k\in \mathbb V=  \mathbb R^3-k\text{-axis}$. In other words, if $q=(r,\theta,z)$ in cylindrical coordinates, then $\ell(q) = \theta$ and $m(q) = z+ri$. We call $\ell$ and $m$ the ***longitudinal*** and ***meridional projections*** in $\mathbb R^3$, and refer to $\ell(q)$ as the ***polar angle*** of $q$.

The longitudinal projection defines the ***standard open book*** in $\mathbb R^3$, with binding the $k$-axis, and with pages $P_\theta = \ell^{-1}(\theta)$ for $\theta\in S^1$. The pages are just the oriented vertical half-planes bounded by the $k$-axis, each indexed by its polar angle as shown in Figure [3](#fig:book){reference-type="ref" reference="fig:book"}. The meridional projection serves to identify each page $P_\theta$ with the hyperbolic plane $\mathbb H$, with "center\"  $i_\theta = i\,\cos\theta + j\,\sin\theta$  corresponding to $i$. The union of all the page centers is the unit circle $C$.

<figure id="fig:book">
<p><embed src="FigBook.pdf" style="height:2.36111in" /> (-113,63)<span><span class="math inline"><em>i</em></span></span> (-64,66)<span><span class="math inline"><em>i</em><sub><em>θ</em></sub></span></span> (-49,82)<span><span class="math inline"><em>j</em></span></span> (-89,114)<span><span class="math inline"><em>k</em></span></span> (-90,43)<span><span class="math inline"><em>θ</em></span></span> (-107,-10)<span>binding</span> (-145,142)<span>pages</span> (-53,10)<span><span class="math inline"><em>P</em><sub><em>θ</em></sub></span></span> (-133,62)<span><span class="math inline"><em>C</em></span></span></p>
<figcaption>The standard open book in <span class="math inline">ℝ<sup>3</sup></span></figcaption>
</figure>

The longitudinal and meridional projections in $\mathbb R^3$ lift to $S^3$ []{#longproj label="longproj"} (in the complement of $K$) by composing with stereographic projection from $-1$. Relying on the context, we continue to denote them by $\ell$ and $m$, and to refer to $\ell(q)$ as the polar angle of $q$. Explicitly $$\ell(q) \ = \ \arg(q_1+q_2i)\qquad\text{and}\qquad m(q) \ = \ \frac{q_3 + |q_1+q_2i|i}{1+q_0}\,.$$ for $q = q_0+q_1i+q_2j+q_3k\in S^3-K$. Here we are using the formula $$\mathrm{pr}_{-1}q \ =  \ (\mathrm{Im\,}q) / (1 + \mathrm{Re\,}q)  =  (q_1 i + q_2 j + q_3 k) / (1 + q_0)\,,$$ and then plugging this into the formula above for the longitudinal and meridional projections in $\mathbb R^3$.

Just as in $\mathbb R^3$, the longitudinal projection in $S^3$ defines the ***standard open book*** in $S^3$, with binding $K$, and with pages $H_\theta = \ell^{-1}(\theta)$. The pages are now open great hemispheres in $S^3$ with centers (i.e. poles) $i_\theta$ along the great circle $C$, and with $K$ as equator. By design, $\mathrm{pr}_{-1}$ maps each hemispherical page $H_\theta$ in $S^3$ onto the corresponding half-planar page $P_\theta$ in $\mathbb R^3$.

We now turn our attention back to links in the $3$-sphere.

A three-component link $L=X\,\cup\,Y\,\cup\,Z$ in $S^3$ is ***generic*** if

::: indentation
.05em1em

1.  $Z$ coincides with the oriented binding $K$ of the standard open book, and

2.  $X$ and $Y$ wind "generically\" around $Z$.
:::

More precisely, the second condition requires the restriction to $X\,\cup\,Y$ of the longitudinal projection  $\ell:S^3-K\longrightarrow S^1$, which sends each point to its polar angle, to be a Morse function with just one critical point per critical value. Geometrically, this means $X$ and $Y$ are transverse to the pages of the standard open book in $S^3$, except for finitely many pages where exactly one of them turns around at a single point. These will be called the ***critical points*** of $L$, while all other points on $X\cup Y$ will be called ***regular points***. Each regular point $w$ has a sign, denoted **$\textup{sign}(w)$**, when viewed as an intersection point of $L$ with the page containing $w$. Thus $\textup{sign}(w) = +1$ or $-1$ according to whether $L$ is oriented in the direction of increasing or decreasing polar angle near $w$.

An example of a generic link is shown in Figure [4](#fig:generic){reference-type="ref" reference="fig:generic"}. It has four critical points, two on $X$ and two on $Y$, indicated by dots in the picture.

<figure id="fig:generic">
<p><embed src="FigGeneric.pdf" style="height:2.08333in" /> (-150,110)<span><span class="math inline"><em>X</em></span></span> (-152,30)<span><span class="math inline"><em>Y</em></span></span> (-90,138)<span><span class="math inline"><em>Z</em></span></span></p>
<figcaption>A generic link</figcaption>
</figure>

Any three-component link in $S^3$ is evidently link homotopic to a generic one: first unknot the last component by a link homotopy and move it to coincide with $K$, and then adjust the first two components by a small isotopy to satisfy the genericity condition (2).

*From this point on we assume that $L$ is generic without further mention.*

As a consequence, we will show the following:

::: indentation
.05em1em

1.  The north pole $k\in S^2$ is a regular value of the characteristic map $h_L$.

2.  There is a simple method for constructing a toral diagram for the associated Pontryagin link $\mathcal L= h_L^{-1}(k)$ from a picture of $L$.
:::

This is the content of the "bicycle theorem\" below. To state it precisely, we need to introduce the key notion of a *bicycle* in $L$, and its associated *icycle* in $T^2$.

Assume, as always, that the components $X$, $Y$ and $Z$ of $L$ are parametrized by smooth functions $x=x(s)$, $y=y(t)$ and $z=z(u)$ with nowhere vanishing derivatives. In particular, points $(s,t)$ in the $2$-torus parametrize pairs of points $x\in X$ and $y\in Y$. Suppose that $x$ and $y$ have the same polar angle $\theta$, or equivalently that they lie in a common page $H_\theta$ of the standard open book in $S^3$. Then we call $(s,t)$ an ***isogonal point*** in $T^2$, and call $(x,y)$ a ***page vector*** in $L$ with polar angle $\theta$, reflecting the fact that the vector in $\mathbb R^3$ from $\mathrm{pr}_{-1}(x)$ to $\mathrm{pr}_{-1}(y)$ lies entirely on the half-planar page $P_\theta$.

A page vector $(x,y)$ will be called ***critical*** if $x$ or $y$ is a critical point of $L$, and ***regular*** if both $x$ and $y$ are regular. A regular page vector is ***positive*** if the oriented strands of $L$ through $x$ and $y$ point in the same direction, meaning $\textup{sign}(x) = \textup{sign}(y)$, and is ***negative*** if they point in opposite directions. These notions are illustrated in Figure [5](#fig:pagevectors){reference-type="ref" reference="fig:pagevectors"}, in which the vectors labeled $1$ and $2$ are positive regular page vectors, $3$ is negative regular, and $4$ is critical.

<figure id="fig:pagevectors">
<embed src="FigPageVectors2.pdf" style="height:2.36111in" />
<p>(-150,105)<span><span class="math inline">1</span></span> (-156,73)<span><span class="math inline">2</span></span> (-112,85)<span><span class="math inline">3</span></span> (-65,98)<span><span class="math inline">4</span></span> (-185,105)<span><span class="math inline"><em>X</em></span></span> (-20,102)<span><span class="math inline"><em>Y</em></span></span> (-106,18)<span><span class="math inline"><em>Z</em></span></span></p>
<figcaption>Page vectors</figcaption>
</figure>

Now consider the spaces $$\mathcal D\ = \ \{\text{isogonal points in $T^2$}\} \qquad\text{and}\qquad \mathcal P\ = \ \{\text{page vectors in $L$}\} \,.$$ By definition $\mathcal D$ parametrizes $\mathcal P$. The genericity of $L$ implies that $\mathcal P$ consists of a finite number of disjoint cycles of page vectors, and that $\mathcal D$ consists of a finite collection of smooth simple closed curves in $T^2$. Orient $\mathcal P$ so that it points to the right (meaning in the direction of increasing polar angle) at each positive regular page vector in it, and to the left at each negative regular page vector. This gives a well-defined orientation on $\mathcal P$, inducing one on $\mathcal D$ as well. We call these the ***preferred orientations*** on $\mathcal P$ and $\mathcal D$.

::: definition
A ***bicycle*** (or "bi-cycle\") in $L$ is a component $\mathcal P_i$ of $\mathcal P$, that is, an oriented cycle of page vectors. Each bicycle is parametrized by a component $\mathcal D_i$ of $\mathcal D$, which we call its associated ***icycle*** (or "i-cycle\").
:::

We first draw in Figure [6](#fig:local){reference-type="ref" reference="fig:local"} four local pictures of a bicycle near a regular page vector, and below them, their parametrizing icycles. It is understood that these pictures take place somewhere in front of the upward pointing $Z$ axis. The four cases represent the possible directions of $X$ and $Y$ relative to the page containing the vector. In each case, the orientation of the bicycle is indicated by a squiggly arrow.

<figure id="fig:local">
<p><embed src="FigLocal.pdf" style="height:2.43056in" /> (-374,146)<span><span class="math inline"><em>Y</em></span></span> (-376,96)<span><span class="math inline"><em>X</em></span></span></p>
<p>(-215,147)<span><span class="math inline"><em>Y</em></span></span> (-217,96)<span><span class="math inline"><em>X</em></span></span></p>
<p>(-115,147)<span><span class="math inline"><em>Y</em></span></span> (-171,96)<span><span class="math inline"><em>X</em></span></span></p>
<p>(-65,147)<span><span class="math inline"><em>Y</em></span></span> (-13,96)<span><span class="math inline"><em>X</em></span></span></p>
<p>(-318,3)<span><span class="math inline"><em>s</em></span></span> (-363,50)<span><span class="math inline"><em>t</em></span></span> (-216,3)<span><span class="math inline"><em>s</em></span></span> (-261,50)<span><span class="math inline"><em>t</em></span></span> (-114,2)<span><span class="math inline"><em>s</em></span></span> (-159,49)<span><span class="math inline"><em>t</em></span></span> (-12,2)<span><span class="math inline"><em>s</em></span></span> (-57,49)<span><span class="math inline"><em>t</em></span></span></p>
<figcaption>Local pictures of a bicycle and its corresponding icycle</figcaption>
</figure>

For an example of a full bicycle, consider the "clasp\" between $X$ and $Y$ pictured in Figure [7](#fig:claspbike){reference-type="ref" reference="fig:claspbike"}(a). This gives rise to the bicycle in Figure [7](#fig:claspbike){reference-type="ref" reference="fig:claspbike"}(b), passing successively through the vectors labeled $1,2,3,4$ and then back to $1$. The associated icycle is a counterclockwise circle in $T^2$, shown in Figure [7](#fig:claspbike){reference-type="ref" reference="fig:claspbike"}(c). The route taken by this bicycle is "short\" in the sense that it does not wind around the binding, although it does spin within the pages.

<figure id="fig:claspbike">
<p><embed src="FigClasp.pdf" style="height:1.11111in" /> (-280,53)<span><span class="math inline"><em>X</em></span></span> (-350,15)<span><span class="math inline"><em>Y</em></span></span> (-325,66)<span><span class="math inline"><em>Z</em></span></span> (-198,45)<span><span class="math inline">1</span></span> (-160,51)<span><span class="math inline">2</span></span> (-202,33)<span><span class="math inline">3</span></span> (-160,25)<span><span class="math inline">4</span></span> (2,6)<span><span class="math inline"><em>s</em></span></span> (-82,73)<span><span class="math inline"><em>t</em></span></span> (-42,64)<span><span class="math inline">1</span></span> (-65,40)<span><span class="math inline">2</span></span> (-42,17)<span><span class="math inline">3</span></span> (-19,40)<span><span class="math inline">4</span></span> (-340,-20)<span>(a) the clasp</span> (-215,-20)<span>(b) the bicycle</span> (-80,-20)<span>(c) the icycle</span></p>
<figcaption>Bicycle arising from a clasp</figcaption>
</figure>

As another example, the link shown in Figure [4](#fig:generic){reference-type="ref" reference="fig:generic"} and reproduced in Figure [8](#fig:icycles){reference-type="ref" reference="fig:icycles"}(a) below has three bicycles. Two of them are short, arising from the clasps as in the previous example, while the remaining long one oscillates back and forth in the longitudinal direction, eventually making one full revolution around the binding. It is an instructive exercise left to the reader to recover the plot of the associated icycles in Figure [8](#fig:icycles){reference-type="ref" reference="fig:icycles"}(b), in which the trivial circles labeled $A$ and $B$ correspond to the clasps in $L$ with the same labels, $C$ labels the icycle that parametrizes the long bicycle, and the corners of the square parametrize the pair $(x,y)$ indicated by the dots in Figure [8](#fig:icycles){reference-type="ref" reference="fig:icycles"}(a).

<figure id="fig:icycles">
<p><embed src="FigIcycles.pdf" style="height:1.73611in" /> (2,20)<span><span class="math inline"><em>s</em></span></span> (-83,104)<span><span class="math inline"><em>t</em></span></span> (-300,90)<span><span class="math inline"><em>X</em></span></span> (-295,20)<span><span class="math inline"><em>Y</em></span></span> (-238,115)<span><span class="math inline"><em>Z</em></span></span> (-248,54)<span><span class="math inline"><em>A</em></span></span> (-215,52)<span><span class="math inline"><em>B</em></span></span> (-44,53)<span><span class="math inline"><em>A</em></span></span> (-29,36)<span><span class="math inline"><em>B</em></span></span> (-27,80)<span><span class="math inline"><em>C</em></span></span> (-280,-15)<span>(a) the generic link <span class="math inline"><em>L</em></span></span> (-90,-15)<span>(b) the icycles of <span class="math inline"><em>L</em></span></span></p>
<figcaption>A generic link and its icycles</figcaption>
</figure>

Before proceeding, we remind the reader that our interest in icycles associated to $L$ stems from the fact that -- when suitably decorated -- they give a toral diagram for a Pontryagin link of the characteristic map $h_L$. This is the content of the bicycle theorem.

The longitudinal and meridional projections on $S^3-K$, defined earlier,

induce projections by the same name on the space $\mathcal P$ of page vectors, $$S^1 \, \overset{\ell}{\longleftarrow} \, \mathcal P\, \overset{m}{\longrightarrow} \, \mathbb H\,,$$ given by $\ell(x,y) = \ell(x) = \ell(y)$ and $m(x,y) = \arg(m(y)-m(x))$. In other words $\ell(x,y)$ is the polar angle that parametrizes the common hemispherical page in $S^3$ containing $x$ and $y$, and $m(x,y)$ is the argument of the vector from $m(x)$ to $m(y)$ in

$\mathbb H$.

Using these projections, we define the ***longitudinal*** and ***meridional degrees*** of a bicycle $\mathcal P_i$ in $L$ by $$\ell_i \ = \ \textup{deg}(\ell|\mathcal P_i) \qquad\text{and}\qquad  m_i \ = \ \textup{deg}(m|\mathcal P_i). \label{degrees}$$ These integer invariants record, respectively, the number of times $\mathcal P_i$ travels around the binding $Z$, and the number of times its vectors spin around in the pages as it goes.

For example, any bicycle arising from a clasp between $X$ and $Y$ has zero longitudinal degree, while its meridional degree can be $\pm1$. In particular, the one shown in Figure [7](#fig:claspbike){reference-type="ref" reference="fig:claspbike"} has meridional degree $-1$, while the ones labeled $A$ and $B$ in Figure [8](#fig:icycles){reference-type="ref" reference="fig:icycles"}(a) have degrees $1$ and $-1$, respectively. The long bicycle in Figure [8](#fig:icycles){reference-type="ref" reference="fig:icycles"}(a), labeled $C$, has longitudinal degree $2$ and meridional degree $1$.

For any icycle $\mathcal D_i$ in $T^2$, parametrizing a bicycle $\mathcal P_i$ in $L$, define the ***framing*** $n_i$ and ***vertical winding number*** $r_i$ of $\mathcal D_i$ by $$n_i \ = \ -\ell_i-m_i \qquad\text{and}\qquad r_i \ = \ m_i$$ where $\ell_i$ and $m_i$ are the longitudinal and meridional degrees of $\mathcal P_i$.

We can now state the main result of this section.

Before proving this theorem, we illustrate how it can be used to compute the Pontryagin invariant of the characteristic map of a generic link.

As a first example, again consider the link $L$ pictured in Figure [8](#fig:icycles){reference-type="ref" reference="fig:icycles"}(a). As noted above, it has three bicyles $A$, $B$, $C$, with longitudinal degrees $0,0,2$, meridional degrees $1,-1,1$, and so by definition, framings $-1,1,-3$ and vertical winding numbers $1,-1,1$.

By the bicycle theorem, the Pontryagin link for the characteristic map $h_L$ has toral diagram as shown in Figure [8](#fig:icycles){reference-type="ref" reference="fig:icycles"}(b) with vertical winding numbers $1$, $-1$ and $1$ on the icycles $A$, $B$ and $C$, and with global framing $n=-1+1-3=-3$. Thus the total vertical winding number is $r = 1-1+1=1$ and from the diagram we compute the horizontal winding numbers to be $p=-1$ and $q=-2$. (These values for the winding numbers of the diagram are confirmed by the calculations $p = \mathrm{Lk}(Y,Z)=-1$, $q = \mathrm{Lk}(X,Z)=-2$ and $r = \mathrm{Lk}(X,Y)=1$.) Thus the invariant $\nu(h_L)$ is well defined modulo $2 = 2\gcd(-1,-2,1)$.

Using a base point in the lower right corner of the diagram, and straight line paths from the icycles to the base point, the depths of the icycles $A$, $B$ and $C$ are $1$, $-1$ and $-1$. Thus by Proposition [\[prop:pontryagin\]](#prop:pontryagin){reference-type="ref" reference="prop:pontryagin"} we conclude that $$\nu(h_L) \ = \ n+pq + \textstyle\sum d_ir_i \ = \ -3+2+1  \ = \ 0 \ \in \ \mathbb Z_2.$$

Although the purpose of this example is to illustrate how the bicycle theorem is used for computations, we note that Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} (yet to be proved) yields the same result here effortlessly, since it implies that the Pontryagin invariant of the characteristic map of any three-component link in $S^3$ is even. Therefore, when the pairwise linking numbers $p$, $q$ and $r$ are relatively prime, as they are in this case, the computation is modulo $2\gcd(p, q, r)  =  2$, and so the Pontryagin invariant is zero.

For our next example we analyze the effect on $\nu(h_L)$ of changing two crossings of opposite signs between the first two components of a generic link $L=X\cup Y\cup Z$. This will be a key step in our inductive proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}.

To this end, choose a positive and a negative crossing between $X$ and $Y$ in a suitable projection of $L$, and let $(x_+,y_+)$ and $(x_-,y_-)$ be the corresponding page vectors. Changing both of the crossings yields a new link $\widehat{L}$, with the same pairwise linking numbers as $L$. This is illustrated in Figure [9](#fig:dblbor){reference-type="ref" reference="fig:dblbor"} where $L$ is the Borromean rings, shown on the left, and $\widehat{L}$ is the unlink, shown on the right.

<figure id="fig:dblbor">
<p><embed src="FigDblBor.pdf" style="height:1.875in" /> (-348,97)<span><span class="math inline"><em>X</em></span></span> (-335,17)<span><span class="math inline"><em>Y</em></span></span> (-325,125)<span><span class="math inline"><em>Z</em></span></span> (-360,-15)<span>(a) the Borromean rings <span class="math inline"><em>L</em></span></span> (-45,97)<span><span class="math inline"><em>X̂</em></span></span> (-60,17)<span><span class="math inline"><em>Ŷ</em></span></span> (-88,125)<span><span class="math inline"><em>Ẑ</em></span></span> (-115,-15)<span>(b) the unlink <span class="math inline"><em>L̂</em></span></span></p>
<figcaption>A double crossing change</figcaption>
</figure>

We then say that $\widehat{L}$ is obtained from $L$ by a ***double crossing change***, and propose to use the bicycle theorem to compute the resulting change $$\Delta\nu \ = \  \nu(h_{\widehat{L}}) - \nu(h_{L})$$ in Pontryagin invariants.

As it turns out, there is a simple formula for $\Delta\nu$ involving the link $L_0$ obtained from $L$ by "smoothing\" both crossings in the usual way: .1pt $$\includegraphics[height=20pt]{FigSmoothCrossing.pdf}$$ .1pt The smoothed link $L_0$ has three components, $P$ and $Q$ (replacing $X$ and $Y$) and $Z$. The component $P$ goes from $+$ to $-$ along $Y$, and then back from $-$ to $+$ along $X$, where we retain the $+$ and $-$ labels after smoothing, while $Q$ goes from $+$ to $-$ along $X$, and then back from $-$ to $+$ along $Y$. This is illustrated in Figure [10](#fig:smooth){reference-type="ref" reference="fig:smooth"} for the double crossing change shown in Figure [9](#fig:dblbor){reference-type="ref" reference="fig:dblbor"}, where we use $X_{+-}$ to denote the arc on $X$ from $+$ to $-$ , and so forth.

<figure id="fig:smooth">
<p><embed src="FigSmooth.pdf" style="height:1.875in" /> (-23,60)<span><span class="math inline"><em>P</em></span></span> (0,50)<span><span class="math inline"><em>Q</em></span></span> (-90,125)<span><span class="math inline"><em>Z</em></span></span> (-103,99)<span><span class="math inline"><em>X</em><sub>+−</sub></span></span> (-65,74)<span><span class="math inline"><em>X</em><sub>−+</sub></span></span> (-95,61)<span><span class="math inline"><em>Y</em><sub>+−</sub></span></span> (-67,21)<span><span class="math inline"><em>Y</em><sub>−+</sub></span></span></p>
<figcaption>The smoothed link <span class="math inline"><em>L</em><sub>0</sub> = <em>P</em> ∪ <em>Q</em> ∪ <em>Z</em></span></figcaption>
</figure>

Then we have the following consequence of the Bicycle Theorem:

::: corollary
[]{#cor:double label="cor:double"} **[(Double Crossing)]{.upright} If $L = X\cup Y\cup Z$ is transformed into $\widehat{L}$ by a double crossing change, and $P$ and $Q$ are the components of the associated smoothing of $X\cup Y$, as explained above, then the corresponding Pontryagin invariants change by $$\Delta\nu \ = \ 2\,\mathrm{Lk}(P,Z) \ = \ -2\,\mathrm{Lk}(Q,Z) \ \in \ \mathbb Z_{2\gcd(p,q,r)}$$ where $p$, $q$ and $r$ are the pairwise linking numbers of the components of $L$.**
:::

::: proof
*Proof.* First note that $$\mathrm{Lk}(P\cup Q,Z) \ = \  \mathrm{Lk}(X\cup Y,Z) \ = \ p+q \ = \ 0 \ \in \ \mathbb Z_{\gcd(p,q,r)}$$ so it suffices to establish the first equality in the corollary.

We may assume that the two page vectors $\textup{\bf v}_+ = (x_+,y_+)$ and $\textup{\bf v}_- = (x_-,y_-)$ associated with the chosen crossings lie on distinct hemispherical pages $H_+$ and $H_-$ of the standard open book in $S^3$, and that these pages contain no critical points in the link. These two page vectors may lie in distinct bicycles in $L$, or they may lie in the same bicycle.

Suppose first that $\textup{\bf v}_+$ and $\textup{\bf v}_-$ lie in distinct bicycles $\mathcal P_+$ and $\mathcal P_-$ in $L$. When we change $L$ to $\widehat{L}$, these bicycles will change, but the icycles $\mathcal D_+$ and $\mathcal D_-$ in the $2$-torus that parametrize them will stay the same. However, their vertical winding numbers $r_+$ and $r_-$ (which record the meridional degrees of $\mathcal P_+$ and $\mathcal P_-$) and their framings $n_+$ and $n_-$ (which record the negative of the sum of the meridional and longitudinal degrees of $\mathcal P_+$ and $\mathcal P_-$) will change. In particular, we claim that $$\widehat{r}_+\ = \ r_ + -1 \qquad\text{and}\qquad \widehat{r}_- \ = \ r_- + 1\,,$$ and consequently   $\widehat{n}_+ = n_+ + 1$  and  $\widehat{n}_- = n_- - 1$   since the longitudinal degrees of the bicycles clearly do not change. The figure below helps us to see this. $$\includegraphics[height=30pt]{FigVert.pdf}
\put(-212,0){\small$X$}
\put(-209,25){\small$Y$}
\put(-175,-1){\small$L$}
\put(-77,0){\small$\widehat{X}$}
\put(-75,25){\small$\widehat{Y}$}
\put(-40,-2){\small$\widehat{L}$}$$ .2pt In this figure, we start with a positive crossing in $L$ and change it to a negative crossing in $\widehat{L}$. Since the strands of $X$ and $Y$ are both pointing to the right, the bicycle $\mathcal P_+$ is moving from left to right. During this motion the page vectors in $\mathcal P_+$ undergo half a *counter-clockwise* rotation with respect to the preferred orientation on the pages. In the corresponding picture for $\widehat{L}$ , we see half a *clockwise* rotation. Therefore the bicycle in $\widehat{L}$ has one more full clockwise rotation in the pages than in $L$, and so $\widehat{r}_+ =  r_+ -1$ as claimed.

If, for example, we switched the arrow on the strand of $Y$, we would have a negative crossing, but then the corresponding bicycle would be moving from right to left, and we would see that $\widehat{r}_- = r_- +1$ as claimed. With this guidance, we leave the remaining cases to the reader.

Now suppose that the page vectors $\textup{\bf v}_+$ and $\textup{\bf v}_-$ lie in the same bicycle $\mathcal P_+ = \mathcal P_-$. Then the above changes in vertical winding number $r$ for the corresponding icycle $\mathcal D_+=\mathcal D_-$ will cancel, and so we see that neither the vertical winding number nor the framing of the icycle will change, that is $\widehat{r}_\pm = r_\pm$ and $\widehat{n}_\pm = n_\pm$.

Note that in either case, whether $\textup{\bf v}_+$ and $\textup{\bf v}_-$ lie in the same or different bicycles, the *total framing* $n$ of the diagram (the sum of the framings of the icycles) does not change.

At this point we recall Proposition [\[prop:pontryagin\]](#prop:pontryagin){reference-type="ref" reference="prop:pontryagin"}, which tells us that $$\nu(h_L)  \ = \  n  +  p q  +  \textstyle\sum d_i r_i\,.$$ In passing from $L$ to $\widehat{L}$ via the double crossing change, we have just seen that the total framing $n$ does not change, and the pairwise linking numbers $p$ and $q$ certainly do not change. We have also seen that the icycles stay the same, so their depths $d_i$ do not change. Only the winding numbers $r_+$ and $r_-$ of the (possibly equal) icycles $\mathcal D_+$ and $\mathcal D_-$ may change. In particular, they also do not change when the page vectors $$\textup{\bf v}_+ \ = \ (x(s_+), y(t_+)) \qquad\text{and}\qquad \textup{\bf v}_- \ = \ (x(s_-), y(t_-))$$ lie in the same bicycle, and so $\Delta\nu = 0$ in this case, while they change to $\widehat{r}_+ = r_+ - 1$ and $\widehat{r}_- = r_- + 1$ when $\textup{\bf v}_+$ and $\textup{\bf v}_-$ lie in distinct bicycles, in which case we have $$\begin{aligned}
\Delta\nu \ &= \  \nu(h_{\widehat{L}}) - \nu(h_L) \\
\ &= \ d_-(\widehat{r}_- - r_-) + d_+(\widehat{r}_+ - r_+) \\
\ &= \ d_- - d_+\,.
\end{aligned}$$ Thus in either case it remains to prove that $d_- - d_+ = 2\,\mathrm{Lk}(P,Z)$.

To show this, we must compute the depths $d_+$ and $d_-$ of $\mathcal D_+$ and $\mathcal D_-$. This requires a choice of base point, and then a choice of paths $\gamma_+$ and $\gamma_-$ from $\mathcal D_+$ and $\mathcal D_-$ to this base point. We let $(s_+,t_-)$ be the base point, and use the vertical path $\gamma_+$ from $(s_+,t_+)$ to $(s_+,t_-)$ and the horizontal path $\gamma_-$ from $(s_-,t_-)$ to $(s_+,t_-)$.

The depth $d_-$ of the component $\mathcal D_-$ of $\mathcal D$ counts the intersections of $\gamma_-$ with $\mathcal D$, which means that it counts the times that $(x(s),y(t_-))$ is a page vector for $s_-\le s\le s_+$, assuming parametrizations set up so that $s_-<s_+$ . Since $y(t_-)$ already lies in the page $H_-$, this means we are counting the times that $x(s)$ also lies in $H_-$ for $s_-\le s\le s_+$ . In other words we are counting the intersection number $X_{-+}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}H_-$ . Examining Figure [6](#fig:local){reference-type="ref" reference="fig:local"}, we find that the signs of the intersection points of $\gamma_-$ with $\mathcal D$ *agree* with the signs of the corresponding intersection points of $X_{-+}$ with $H_-$, and hence $$d_- \ = \ 2\, X_{-+} \raisebox{-.3ex}{\huge$\cdot$}H_- \mod{2\gcd(p,q,r)}.$$

In a similar fashion, we find that intersections of $\gamma_+$ with $\mathcal D$ correspond to intersections of $Y_{+-}$ with $H_+$, but in this case, the signs of corresponding points of intersection are *opposites*, and so the depth of $\mathcal D_+$ is $$d_+ \ = \ -2\,Y_{+-} \raisebox{-.3ex}{\huge$\cdot$}H_+\mod{2\gcd(p,q,r)}.$$

Therefore the assertion that $d_- - d_+ = 2\mathrm{Lk}(P,Z)$, which will complete the proof of the corollary, reduces to the identity $$X_{-+} \raisebox{-.3ex}{\huge$\cdot$}H_-  +  Y_{+-} \raisebox{-.3ex}{\huge$\cdot$}H_+ \ = \ \mathrm{Lk}(P,Z)\,.$$ But this follows easily from the fact that $P = X_{-+} \cup Y_{+-}$. Figure [11](#fig:linking){reference-type="ref" reference="fig:linking"} helps us to see this. In the figure, the arc $X_{-+}$ winds around the vertical $Z$ axis $k$ times and the arc $Y_{+-}$ winds around it $\ell$ times, while the entire loop $P = X_{-+} \cup Y_{+-}$ winds around it $k+\ell+1$ times. By our half-counting convention, we have $$X_{-+} \,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}H_- \ = \ 1/2 + k \qquad\text{and}\qquad Y_{+-} \,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}H_+ \ = \ 1/2 + \ell$$ and the result follows. ◻
:::

<figure id="fig:linking">
<p><embed src="FigLinking.pdf" style="height:2.63889in" /> (-132,10)<span><span class="math inline"><em>H</em><sub>−</sub></span></span> (-18,12)<span><span class="math inline"><em>H</em><sub>+</sub></span></span> (-57,27)<span><span class="math inline"><em>X</em><sub>−+</sub></span></span> (-96,155)<span><span class="math inline"><em>Y</em><sub>+−</sub></span></span> (-82,180)<span><span class="math inline"><em>Z</em></span></span> (-126,50)<span><span class="math inline"><em>k</em></span></span> (-17,135)<span><span class="math inline">ℓ</span></span> (-121,86)<span><span class="math inline">−</span></span> (-19,90)<span><span class="math inline">+</span></span></p>
<figcaption>The linking of <span class="math inline"><em>P</em> = <em>X</em><sub>−+</sub> ∪ <em>Y</em><sub>+−</sub></span> and <span class="math inline"><em>Z</em></span></figcaption>
</figure>

For the inductive step of the proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} in the next section, we will need to apply this formula for $\Delta\nu$ under the double crossing change $L\to\widehat{L}$ shown in Figure [12](#fig:double){reference-type="ref" reference="fig:double"} (which will be seen to be equivalent to a delta move). It is understood that $L$ and $\widehat{L}$ should coincide outside the picture, where in fact they can be arbitrary. Indeed, if not generic outside the ball, they can be adjusted by a link homotopy to become so, and then the methods described above apply. Since the component $Q$ of the smoothed link $L_0$ is just a meridian of $Z$ with $\mathrm{Lk}(Q,Z) = -1$, it follows that $\Delta\nu = 2$.

Thus we have proved the following: []{#double label="double"}

<figure id="fig:double">
<p><embed src="FigDouble.pdf" style="height:1.38889in" /> (-315,14)<span><span class="math inline"><em>X</em></span></span> (-203,73)<span><span class="math inline"><em>Y</em></span></span> (-267,90)<span><span class="math inline"><em>Z</em></span></span> (-300,37)<span><span class="math inline">+</span></span> (-218,37)<span><span class="math inline">−</span></span> (-100,37)<span><span class="math inline">−</span></span> (-18,37)<span><span class="math inline">+</span></span> (-285,-15)<span>(a) the link <span class="math inline"><em>L</em></span></span> (-90,-15)<span>(b) the link <span class="math inline"><em>L̂</em></span></span></p>
<figcaption>A simple double crossing change</figcaption>
</figure>

::: corollary
[]{#cor:double label="cor:double"} **If two links $L$ and $\widehat{L}$ coincide outside a $3$-ball, and appear in the ball as shown in Figure [12](#fig:double){reference-type="ref" reference="fig:double"}, then $\nu(h_{\widehat{L}}) = \nu(h_L) + 2$.**
:::

We now embark on the proof of the bicycle theorem, which will occupy us for the rest of this section.

Start with a generic link $L$ in $S^3$ where, as usual, $x=x(s)$, $y=y(t)$ and $z=z(u)$ parametrize the three components $X$, $Y$ and $Z$. Then $Z$ coincides with the binding $K$ of the standard open book, which is the circle subgroup of $S^3$ containing the quaternion $k$. Looking back at the formula for the characteristic map $$h_L(s,t,u) \ = \ (y_z-x_z)/|y_z-x_z| \quad\text{where}\quad a_z = \mathrm{pr}_{-1}(-a\bar z)\,,$$ we see that we must understand the $K$-action sending $z\in K$ to the automorphism $a\mapsto a\bar z$ of $S^3$, and the induced $K$-action on $\mathbb R^3$ via stereographic projection. Visualizing how these actions transform the pages of the standard open books will aid us in our subsequent arguments, and we do this next.

For any $z =  \cos\alpha + k\sin\alpha$ in the binding $K$, right multiplication by $\bar z=  \cos\alpha -k\sin\alpha$ is an isometry of $S^3$ that rotates $K$ by $-\alpha$ radians, likewise rotates the orthogonal great circle $C$ of page centers by $\alpha$ radians, and so advances each hemispherical page $H_\theta$ to the page $H_{\theta+\alpha}$ while simultaneously rotating the page by $-\alpha$ radians about its center $i_\theta$. Therefore, as $z$ traverses $K$, any given page turns once around $K$, successively occupying the positions vacated by the other pages. During this time, the page spins once negatively about its center, so that in total it is following a left-handed screw motion along $C$.

This turning of the hemispherical pages about $K$ in $S^3$ is transferred by stereographic projection to a turning of the half-planar pages about the $k$-axis in $\mathbb R^3$, while the *spherical* rotations of the pages in $S^3$ become *hyperbolic* rotations of the pages in $\mathbb R^3$ about their centers. This is a consequence of the conformality of stereographic projection, which implies that the page identification $H_\theta \leftrightarrow P_\theta$ is conformal. Once again, the net effect is a left-handed screw motion along $C$.

This description of the $K$-action has the following technical consequence that is critical for our study of the characteristic map of a generic link.

::: proof
*Proof.* Since the $K$-action carries pages to pages, $x$ and $y$ will lie on the same page in $S^3$ if and only if $x_z$ and $y_z$ lie on the same page in $\mathbb R^3$ for all $z\in K$. Part (a) of the lemma is now obvious. Using the meridional projection, and the description of the $K$-action above, part (b) of the lemma translates into the following statement. For any pair of distinct points $x$ and $y$ in the upper half-plane model of the hyperbolic plane $\mathbb H$, the function $$d(\alpha) \ = \ \arg(\mathrm{rot}_\alpha y-\mathrm{rot}_\alpha x)$$ is strictly increasing, where $\mathrm{rot}_\alpha:\mathbb H\to\mathbb H$ is hyperbolic rotation about $i$ by $\alpha$ radians. Since we wish to prove this for all $x$ and $y$, it suffices to show that $d'(0)>0$ (because $d'(\alpha)$ for one choice of $x$ and $y$ is equal to $d'(0)$ for some other choice of $x$ and $y$).

To prove this, we transfer the problem to the Poincaré disk $\mathbb D$ using the conformal map $$f:\mathbb D\ \longrightarrow\ \mathbb H\quad,\quad f(z) \ = \  \frac{1-z}{1+z}\ i$$ that sends $0$ to $i$. Hyperbolic rotation of $\mathbb H$ about $i$ by any angle is conjugate by $f$ to euclidean rotation of $\mathbb D$ by the same angle. Thus we must show that for any pair of distinct points $x$ and $y$ in $\mathbb D$, the function $$g(\alpha) \ = \ \arg(f(e^{i\alpha}y)-f(e^{i\alpha}x))$$ has positive derivative at $\alpha = 0$. Noting that $f(a)-f(b) = 2i(b-a)/(1+a)(1+b)$ and using the fact that the argument function converts products into sums and quotients into differences, we find that $g(\alpha)$ differs by a constant from the function $$h(\alpha) \ = \ \alpha - \arg(1+e^{i\alpha}x) - \arg(1+e^{i\alpha}y),$$ and so it remains to show that $h'(0)>0$. But a simple geometric argument using the central angle theorem from elementary plane geometry shows that, for any given $z\in \mathbb D$, the derivative of the function $\arg(1+e^{i\alpha}z)$ at $\alpha = 0$ is strictly less than $1/2$. Therefore $h'(0) > 1 - 1/2-1/2 \, = \, 0$ as desired. ◻
:::

It follows from the twist lemma that, for any point $(s,t)$ in the $2$-torus that is isogonal for our generic link $L$ (meaning that $x=x(s)$ and $y=y(t)$ have the same polar angle, and hence lie on the same page of the open book), there exists a unique $u = u(s,t)\in S^1$ for which the vector $y_z-x_z$ points straight up, namely the $u$ for which $z = z(u) = \tau(x,y)$. It follows that the link $$\mathcal L\ = \ h_L^{-1}(k) \ = \ \{(s,t,u)\in T^3\ | \ (s,t)\in\mathcal D\text{ and } u=u(s,t)\}\,, \label{pontryaginlink}$$ is the graph of the function $u(s,t)$ over the collection $\mathcal D$ of isogonal curves in $T^2$, as asserted in the introduction.

We now use the twist lemma to prove part (a) of the bicycle theorem, asserting that $k$ is a regular value of $h_L$. This will endow the components of $\mathcal L$ with orientations (and thus vertical winding numbers) and framings, as defined in Section [\[sec:pontryagin\]](#sec:pontryagin){reference-type="ref" reference="sec:pontryagin"}. The proof of the bicycle theorem will then be completed by showing that these agree with the preferred orientations, vertical winding numbers and framings of the components of $\mathcal D$, as defined earlier in this section.

Suppose that $h_L(s,t,u) = k$. This means that the vector from $x_z$ to $y_z$ points straight up, and so lies in some page $P$ of the standard open book in $\mathbb R^3$.

We must show that at $(s,t,u)$ the vectors $\partial_s h_L$, $\partial_t h_L$ and $\partial_u h_L$ span the tangent space to $S^2$ at $k$.

We are guided by Figure [13](#fig:regular){reference-type="ref" reference="fig:regular"}, depicting a neighborhood of the vertical vector $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}$ from $x_z$ to $y_z$ in $\mathbb R^3$, lying on the page $P$. In this figure, $X_z$ and $Y_z$ denote the images of $X$ and $Y$ under the $z$-action, one or both of which must be transverse to $P$ since $L$ is generic. We arbitrarily depict $X_z$ tangent to $P$ and $Y_z$ transverse to it.

<figure id="fig:regular">
<p><embed src="FigRegular.pdf" style="height:2.36111in" /> (-114,105)<span><span class="math inline"><em>y</em><sub><em>z</em></sub></span></span> (-113,66)<span><span class="math inline"><em>x</em><sub><em>z</em></sub></span></span> (-113,83)<span><span class="math inline">$\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}$</span></span> (-21,116)<span><span class="math inline"><em>Y</em><sub><em>z</em></sub></span></span> (-17,84)<span><span class="math inline"><em>X</em><sub><em>z</em></sub></span></span> (-100,120)<span><span class="math inline">∂<sub><em>u</em></sub><em>h</em><sub><em>L</em></sub></span></span> (-85,92)<span><span class="math inline">∂<sub><em>t</em></sub><em>h</em><sub><em>L</em></sub></span></span> (-120,29)<span><span class="math inline"><em>P</em></span></span> (-95,5)<span>TURN</span> (-56,158)<span>S</span> (-56.5,150)<span>P</span> (-55.5,142)<span>I</span> (-57,134)<span>N</span></p>
<figcaption><span class="math inline"><em>k</em></span> is regular</figcaption>
</figure>

The hollow arrows in the figure indicate the left-handed screw motion of the $K$-action. In particular, as the $u$ parameter increases along $K$, this action (the stereographic image of right multiplication by $-\bar z$) turns the pages in the indicated direction while spinning them in a left-handed fashion about their centers.

As the $t$ parameter along $Y$ increases, the tip of $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}$ moves to the right along $Y_z$, so that $\partial_t h_L$ also points to the right, transverse to $P$. For clarity, we draw this partial derivative vector at the tip of $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}$, even though it is really tangent to $S^2$ at its north pole $k$.

As the $u$ parameter along $Z$ increases, two things happen which affect $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}$. The page containing it turns around the binding, but such an action keeps $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}$ vertical, so has no infinitesimal effect. In addition, the page spins around its center, shifting the binding in a downward direction. Thus by the twist lemma, the vector $\partial_u h_L$ is nonzero and tangent to the page, pointing toward the binding when placed with its initial point at $y_z$.

It follows that $\partial_t h_L$ and $\partial_u h_L$ are linearly independent, confirming that $(s,t,u)$ is a regular point of the map $h_L$. Since $(s,t,u)$ was chosen arbitrarily in $h_L^{-1}(k)$, we see that $k$ is a regular value of $h_L$, proving part (a) of the Bicycle Theorem.

Starting with a three-component link $L$ in generic position in $S^3$, we have shown above that the Pontryagin link $\mathcal L$ of its characteristic map $h_L$ is given by $$\mathcal L\ = \ h_L^{-1}(k) \ = \ \{(s,t,u)\in T^3\ | \ (s,t)\in\mathcal D\text{ and } u=u(s,t)\}\,.$$ It remains to prove that the preferred orientation, vertical winding number $r_i$ and framing $n_i$ of each isogonal curve $\mathcal D_i$, as specified in Figure [6](#fig:local){reference-type="ref" reference="fig:local"} and just before the statement of the bicycle theorem, agree with the orientation, vertical winding number and framing of the component $\mathcal L_i$ of the Pontryagin link that lies over $\mathcal D_i$.

To see that the orientations agree, choose a regular page vector $(x,y)$ parametrized by an isogonal point $(s,t)$ in $\mathcal D_i$, and consider the orientation of $Y$ relative to the page containing $x$ and $y$, as recorded by the sign of $y$.

Figure [14](#fig:orientation){reference-type="ref" reference="fig:orientation"} shows the associated vertical vector $(x_z,y_z)$ in $3$-space for the case when $\textup{sign}(y) = +1$, causing the displaced link component $Y_z$ to point to the *right*. Arguing as above (see Figure [13](#fig:regular){reference-type="ref" reference="fig:regular"}) we see that $\partial_t h_L$ also points to the right, while $\partial_u h_L$ points toward the binding as always. Thus $\partial_t h_L$ and $\partial_u h_L$ form a positive basis for the tangent plane to $S^2$ at $k$. Since $\partial_s$, $\partial_t$ and $\partial_u$ form a positive basis for the tangent space to $T^3$ at each of its points, it follows that the link component $\mathcal L_i$ must be oriented in the direction of *increasing* $s$ near the associated point $(s,t,u)$ in the $3$-torus, and this agrees with the orientation assigned to $\mathcal D_i$ in Figure [6](#fig:local){reference-type="ref" reference="fig:local"}.

<figure id="fig:orientation">
<p><embed src="FigOrientation.pdf" style="height:2.36111in" /> (-100,100)<span><span class="math inline"><em>y</em><sub><em>z</em></sub></span></span> (-100,48)<span><span class="math inline"><em>x</em><sub><em>z</em></sub></span></span> (-19,110)<span><span class="math inline"><em>Y</em><sub><em>z</em></sub></span></span> (-17,50)<span><span class="math inline"><em>X</em><sub><em>z</em></sub></span></span> (-81,113)<span><span class="math inline">∂<sub><em>u</em></sub><em>h</em><sub><em>L</em></sub></span></span> (-66,79)<span><span class="math inline">∂<sub><em>t</em></sub><em>h</em><sub><em>L</em></sub></span></span></p>
<figcaption>Orientation of the Pontryagin link</figcaption>
</figure>

Similarly, if $\textup{sign}(y)=-1$ then $\mathcal L_i$ points in the direction of *decreasing* $s$ near $(s,t,u)$. Referring again to Figure [6](#fig:local){reference-type="ref" reference="fig:local"}, it is evident that this agrees with the preferred orientation on $\mathcal D_i$.

Next consider the vertical winding number $r_i$ of $\mathcal D_i$. By definition $r_i$ is equal to the meridional degree $m_i$ of the associated bicycle $\mathcal P_i$, that is, the number of times that the page vectors spin in the pages of the open book as the bicycle is traversed. By the twist lemma, this is equal to the number of times that $z$ spins around $K$, or equivalently that $u = u(s,t)$ spins around the circle as $(s,t)$ traverses $\mathcal D_i$, which is the vertical winding number of $\mathcal L_i$.

Finally consider the framing $n_i$ of $\mathcal D_i$. By definition $n_i = -\ell_i-m_i$, where $\ell_i$ and $m_i$ are the longitudinal and meridional degrees of the associated bicycle $\mathcal P_i$. This integer specifies a normal vector field $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf n}}$ to $\mathcal L_i$ by adding $n_i$ full twists (positive or negative according to the sign of $n_i$) to the lift $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf z}}$ of a normal vector field to $\mathcal D_i$ in $T^2$, the "zero\" or "blackboard\" framing.

We must show that the vector field $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf n}}$ coincides with the Pontryagin framing of $\mathcal L_i$. In other words, the differential of $h_L$ carries it onto a homotopically trivial loop of nonzero tangent vectors to $S^2$ at $k$. To see this, first note that $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf z}}$ is homotopic to the vertical vector field $\partial_u$, remaining nonzero and transverse to $\mathcal L_i$ during the homotopy. Now since $\partial_u h_L$ is always tangent to the page containing $x_z$ and $y_z$, as shown above, it is clear that each longitudinal circuit of the bicycle $\mathcal P_i$ causes $dh_L(\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf z}})$ to spin once in the same direction about the binding. By the twist lemma, each meridional spin of the bicycle also causes $dh_L(\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf z}})$ to spin once about the binding. Thus $dh_L(\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf z}})$ spins $\ell_i+m_i$ times as the bicycle is traversed. Adding $n_i= -\ell_i-m_i$ full twists to the framing negates this spinning, and so $dh_L(\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf n}})$ does not spin at all, up to isotopy, as asserted.

This completes the proof of the bicycle theorem.

# Proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} {#sec:A}

Let $L$ be a three-component link in the $3$-sphere with characteristic map $g_L:T^3\to S^2$. Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} asserts that the degrees of $g_L$ on the coordinate $2$-tori of $T^3$ are equal to the pairwise linking numbers $p$, $q$ and $r$ of the components of $L$, and that Pontryagin's absolute $\nu$-invariant of $g_L$ is equal to twice Milnor's triple linking number $\mu(L)$ mod $2\gcd(p,q,r)$.

The first statement was proved easily at the end of Section [\[sec:characteristic\]](#sec:characteristic){reference-type="ref" reference="sec:characteristic"}. We now prove the second statement by an inductive argument, relying heavily on the techniques and results of the last section. Throughout, we will use the asymmetric characteristic map $h_L:T^3\to S^2$ in place of $g_L$, since these two maps are homotopic.

In Example [\[ex:Lpqr\]](#ex:Lpqr){reference-type="ref" reference="ex:Lpqr"} we introduced the "base links\" $L_{pqr}$ with pairwise linking numbers $p$, $q$ and $r$ and $\mu(L_{pqr}) = 0$. See Figure [\[fig:Lpqr\]](#fig:Lpqr){reference-type="ref" reference="fig:Lpqr"}. We will show that Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} holds for these links.

To accomplish this, we must show that for each $p$, $q$ and $r$, the associated characteristic map $h_{L_{pqr}}$ is homotopic to the base map $f_{pqr}:T^3\to S^2$ used in Section [\[sec:pontryagin\]](#sec:pontryagin){reference-type="ref" reference="sec:pontryagin"} to convert the relative Pontryagin $\nu$-invariant to an absolute $\nu$-invariant. In other words, we must show that $\nu(h_{L_{pqr}}) = 0$.

First move $L_{pqr}$ by a link homotopy into generic position, and let $L=X\cup Y\cup Z$ be the resulting link. Then $Z$ coincides with the binding $K$ of the standard open book, while $X$ and $Y$ wind around $Z$ in a generic fashion, $q$ and $p$ times respectively, linking each other $r$ times along the way. In fact this winding can be made *monotonic*, to appear as shown in Figure [15](#fig:genericLpqr){reference-type="ref" reference="fig:genericLpqr"} for the case $(p,q,r)=(5,3,-2)$.

<figure id="fig:genericLpqr">
<p><embed src="FigLpqrGeneric.pdf" style="height:2.77778in" /> (-122,42)<span><span class="math inline"><em>q</em></span></span> (-122,133)<span><span class="math inline"><em>p</em></span></span> (-25,90)<span><span class="math inline"><em>r</em></span></span> (-1,20)<span><span class="math inline"><em>X</em></span></span> (3,157)<span><span class="math inline"><em>Y</em></span></span> (-65,180)<span><span class="math inline"><em>Z</em></span></span></p>
<figcaption>A generic link <span class="math inline"><em>L</em></span> representing <span class="math inline"><em>L</em><sub><em>p</em><em>q</em><em>r</em></sub></span></figcaption>
</figure>

Observe that one need not actually construct a link homotopy carrying $L_{pqr}$ to $L$, but need only check that the pairwise and triple linking numbers of $L_{pqr}$ and $L$ coincide, and then appeal to Milnor's classification. The verification that $\mu(L)=0$ is completely analogous to the calculation for $\mu(L_{pqr})$, using the obvious stacked disks, joined by half twisted bands, as Seifert surfaces for $X$ and $Y$, and a hemispherical page in the open book on $S^3$ as a Seifert surface for $Z$.

Now the bicycles in $L$ are easily identified. There are $d = \gcd(p,q)$ of them, all of longitudinal degree $\ell = \textup{lcm}(p,q)$, and all but one of meridional degree $0$, the remaining one being of degree $r$. The parametrizing icycles are all parallel to a $(p/d,q/d)$ torus knot in the $2$-torus, with vertical winding numbers all equal to zero, except one equal to $r$. By the bicycle theorem, these icyles form a diagram for the Pontryagin link of $h_L$, with global framing $-(pq+r)$. This is exactly the situation described in Example [\[ex:basecase\]](#ex:basecase){reference-type="ref" reference="ex:basecase"}, and so $$\nu(h_{L_{pqr}}) \ = \ \nu(h_L) \ = \ 0 \ \in \ \mathbb Z_{2\gcd(p,q,r)}$$ as asserted.

First recall from Example [\[ex:delta\]](#ex:delta){reference-type="ref" reference="ex:delta"} that any three-component link $L$ with pairwise linking numbers $p$, $q$ and $r$ is link homotopic to a link obtained from $L_{pqr}$ by a sequence of delta moves of the type shown in [Figure [\[fig:delta\]](#fig:delta){reference-type="ref" reference="fig:delta"}]{.upright} $($or its inverse$)$, by a result of Murakami and Nakanishi [@MurakamiNakanishi]. It was shown in that example that each such move increases $\mu(L)$ by $1$.

Now observe that such a delta move $\Delta:L\to\widehat{L}$ can be viewed as a double crossing change $\mathbb D$, of the kind shown in Figure [12](#fig:double){reference-type="ref" reference="fig:double"},

composed with an isotopy, as indicated in Figure [16](#fig:deltadouble){reference-type="ref" reference="fig:deltadouble"}. By Corollary [\[cor:double\]](#cor:double){reference-type="ref" reference="cor:double"}, this double crossing change increases $\nu(L)$ by $2$, and so $\Delta$ does the same.

<figure id="fig:deltadouble">
<p><embed src="FigDeltaDouble.pdf" style="height:2.5in" /> (-55,72)<span> isotopy</span> (-132,142)<span><span class="math inline">𝔻</span></span> (-210,68)<span><span class="math inline"><em>Δ</em></span></span> (-270,135)<span><span class="math inline"><em>L</em></span></span> (-255,107)<span><span class="math inline"><em>X</em></span></span> (-170,160)<span><span class="math inline"><em>Y</em></span></span> (12,135)<span><span class="math inline"><em>L̂</em></span></span> (-140,5)<span><span class="math inline"><em>L̂</em></span></span></p>
<figcaption>Another view of the delta move</figcaption>
</figure>

Since this argument applies to an arbitrary delta move, it follows that $\nu(L) = 2\mu(L)$ for *all* three component links $L$. This completes the proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}.

# Sketch of an algebraic proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} {#sec:A'}

In this section we sketch an entirely different proof of the theorem using string links and maps of the $2$-torus to the $2$-sphere. The reader is referred to our paper [@DGKMSV] for more details.

The proof is organized around the following key diagram, in which the left half, devoid of algebraic structure, represents the topological problem we are trying to solve, while the right half represents the algebraic structures that we impose on the left half via the two horizontal maps in order to solve the problem.

$$\label{eqn:keydiagram}
\begin{diagram}[size=3em]
\fbox{\parbox{0.24\linewidth}{\begin{center} \small Three-component \\ links in $S^3$ \\ up to link homotopy\end{center}}}  
&&& 
\lTo^{\text{closing up}} 
&&& 
\fbox{\parbox{0.24\linewidth}{\begin{center} \small Three-component \\ string links \\ up to link homotopy\end{center}}}    
\\ \\
\dTo^{\text{characteristic}\atop\text{maps}}_{\ g} 
&&&&&& 
\dTo_{\text{makes diagram}\atop\text{commutative}}  
\\ \\
\fbox{\parbox{0.24\linewidth}{\begin{center} 
\small Maps of $T^3$ to $S^2$ \\ up to homotopy\end{center}}}  
&&& 
\lTo_{\text{natural map}} 
&&& 
\fbox{\parbox{0.24\linewidth}{\begin{center} 
\small Fundamental groups \\ of spaces of maps \\ of $T^2$ to $S^2$\end{center}}}  \\ 
\end{diagram}$$

 

In the upper left corner of the diagram we have the set of link homotopy classes of three-component links in the $3$-sphere $S^3$, and in the lower left corner the set of homotopy classes of maps of the $3$-torus $T^3$ to the $2$-sphere $S^2$. The vertical map $g$ between them assigns to the link homotopy class of $L$ the homotopy class of its characteristic map $g_L$. Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} describes $g$ and asserts that it is one-to-one.

A $k$-component ***string link*** consists of $k$ disjoint, oriented, properly embedded arcs in a cube, with their tails on the bottom face and their tips on the top face directly above their tails. The product of two such string links with endpoints in a common position is given by stacking the second one on top of the first. When a string link moves by a link homotopy, each strand is allowed to cross itself, while different strands must remain disjoint, just as for links. Then the above product induces a group structure on the set of link homotopy classes of $k$-component string links.

In the upper right corner of the diagram we have the group of link homotopy classes of three-component string links. Following Habegger and Lin [@HabeggerLin], an explicit presentation for this group can be given in which the pairwise linking numbers and the Milnor $\mu\text{-invariant}$ figure prominently.

The upper horizontal map denotes the operation of closing up a string link to a link. It is easily shown that this map is onto, and that point inverse images are conjugacy classes of string links, a special circumstance for links with three components which fails for four or more components.

We see in the figure below that the string link on the right closes up to the Borromean rings on the left.

<figure id="fig:br">
<p><embed src="FigBR.pdf" style="height:1.52778in" /> (-136,58)<span>closes up</span></p>
<figcaption>Borromean rings as the closure of a string link</figcaption>
</figure>

Thus the Borromean rings, a "primitive example\" in the world of links, is the closure of a string link which is itself a commutator of simpler string links.

In the lower right corner of the diagram we have the union of the fundamental groups of the components of the space of continuous maps of the $2$-torus $T^2$ to the $2$-sphere $S^2$, one for each possible degree. The work of Fox [@Fox] on torus homotopy groups (the case $p = 0$) and its generalization by Larmore and Thomas [@LarmoreThomas] provide explicit presentations for these groups in which the degrees on subtori and the Pontryagin $\nu$-invariant figure prominently.

The lower horizontal map takes the homotopy class of a based loop in the space of maps of $T^2$ to $S^2$, ignores base points, and interprets this as a homotopy class of maps of $T^3$ to $S^2$ in the usual way. The resulting map is onto, and point inverse images are conjugacy classes in the various fundamental groups.

Finally, the vertical map on the right side is defined to make the diagram commute. We have a group in the upper right corner, but demote it to a union of groups to match what is below it, so that the vertical map can be regarded as a union of group homomorphisms. Using the explicit presentations of domain and range, one can determine the effects of this map on generators, and then use the commutativity of the diagram to show that the vertical map $g$ on the left is precisely as described in Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}.

# Proof of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}, formulas (1) and (2) {#sec:B}

Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} provides three formulas for Milnor's $\mu$-invariant of a three-component link $L$ in $S^3$ whose pairwise linking numbers vanish:

$(1)$ (differential forms)  $\mu(L) \ = \ \displaystyle{\frac12\, \int_{T^3} \delta(\varphi*\omega_L) \wedge \omega_L}$

$(2)$ (vector fields)  $\mu(L) \ = \ \displaystyle{\frac12\, \int_{T^3\times T^3} \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf x}) \times \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y}) \,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,
\nabla_{\!\textup{\bf y}}\,\varphi\left(\textup{\bf x}- \textup{\bf y}\right)\ d\textup{\bf x}\, d\textup{\bf y}}$

$(3)$ (Fourier series)  $\mu(L) \ = \  \displaystyle{8\pi^3 \sum_{\textup{\bf n}\ne{\bf 0}} \textup{\bf a}_\textup{\bf n}\times \textup{\bf b}_\textup{\bf n}\,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf n}/|\textup{\bf n}|^2}$

The notation is explained in the introduction.

In the subsections that follow, we obtain explicit expressions for the characteristic $2\textup{-form}$ $\omega_L$ and vector field $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L$, and for the fundamental solution $\varphi$ to the scalar Laplacian on $T^3$, and then establish formula (1) by making use of J. H. C. Whitehead's integral formula for the Hopf invariant. Then, we show how to obtain formula (2) from formula (1). Finally, in Section [5](#sec:B'){reference-type="ref" reference="sec:B'"} we review the calculus of differential forms and Fourier analysis on $T^3$, in order to make explicit the role and form of $\varphi$ and obtain formula (3).

Recall the formula for the characteristic map $g_L\colon T^3\to S^2$ of the link $L$ given in Proposition [\[prop:char\]](#prop:char){reference-type="ref" reference="prop:char"}, $$g_L(s,t,u) \ = \ \frac{F(x,y,z)}{| F(x,y,z)|},$$ where $x=x(s)$, $y=y(t)$ and $z=z(u)$ parametrize the components of $L$, and where $F$ was given in Section [\[sec:characteristic\]](#sec:characteristic){reference-type="ref" reference="sec:characteristic"} as $$F(x,y,z) \ = \  (ix\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}y + iy\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}z + iz\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}x \ , \  jx\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}y + jy\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}z + jz\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}x \ , \  kx\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}y + ky\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}z + kz\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}x).$$ Here we view $x$, $y$ and $z$ as quaternions for the multiplication and as vectors in $\mathbb R^4$ when performing the dot product. For simplicity, we write $g_L=F/| F|$, suppressing the appearance of the evaluation map $e_L(s,t,u)=(x(s),y(t),z(u))$.

Again let $\omega$ be the Euclidean area 2-form on the unit 2-sphere $S^2\subset\mathbb R^3$, normalized so that the total area is 1 instead of $4\pi$. If $\textup{\bf p}$ is a point of $S^2$, and $\textup{\bf a}$ and $\textup{\bf b}$ are tangent vectors to $S^2$ at $\textup{\bf p}$, then $$\omega_{\textup{\bf p}}(\textup{\bf a},\textup{\bf b}) \ = \ \frac1{4\pi}(\textup{\bf a}\times\textup{\bf b})\,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf p}.$$ This 2-form $\omega$ on $S^2$ extends to a closed 2-form $\overline\omega$ in $\mathbb R^3-{\bf 0}$ given by $$\overline\omega_{\textup{\bf p}}(\textup{\bf a},\textup{\bf b}) \ = \ {(\textup{\bf a}\times\textup{\bf b})\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf p}\over 4\pi|\textup{\bf p}|^3},$$ which is the pullback of $\omega$ from $S^2$ to $\mathbb R^3-{\bf 0}$ via the map $\textup{\bf p}\mapsto \textup{\bf p}/|\textup{\bf p}|$.

Hence the pullback $g_L^*\omega$ of $\omega$ from $S^2$ to $T^3$ via $g_L=F/| F|$ is the same as the pullback $F^*\overline\omega$ of $\overline\omega$ from $\mathbb R^3-{\bf 0}$ to $T^3$ via $F$.

Write $$g_L^*\omega \ = \ F^*\overline\omega 
\ = \ a(s,t,u)dt\wedge du+b(s,t,u)du\wedge ds+c(s,t,u)ds\wedge dt.$$ Then we have $$\aligned
a(s,t,u)& \ = \  F^*\overline\omega({\partial_t},{\partial_u}) \ = \  \overline\omega(F_*{\partial_t}, F_*{\partial_u}) \\
& \ = \ \overline\omega(F_t,F_u) \ = \  \frac{(F_t\times F_u)\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3},
\endaligned$$ and likewise for $b(s,t,u)$ and $c(s,t,u)$, where the subscripts on $F$ denote partial derivatives.

Therefore, the characteristic 2-form of the link $L$ is $$\omega_L \ = \  g_L^*\omega \ = \ 
\frac{F_t\times F_u\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3}  \, dt\wedge du
+\frac{F_u\times F_s\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3} \, du\wedge ds
+\frac{F_s\times F_t\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3} \, ds\wedge dt,$$ and its corresponding characteristic vector field is $$\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L \ = \ 
\frac{F_t\times F_u\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3} \, \partial_s
+\frac{F_u\times F_s\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3} \, \partial_t
+\frac{F_s\times F_t\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}F}{4\pi| F|^3} \, \partial_u.$$

Let $L$ be a three-component link in the 3-sphere $S^3$ with pairwise linking numbers $p$, $q$ and $r$ all zero. By the first part of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} these numbers are the degrees of the characteristic map $g_L\colon T^3\to S^2$ on the $2$-dimensional coordinate subtori. Since these degrees are all zero, $g_L$ is homotopic to a map $g\colon T^3\to S^2$ which collapses the 2-skeleton of $T^3$ to a point: $$g_L\ \simeq \ g\colon T^3 \stackrel{\sigma}{\longrightarrow}S^3 \stackrel{f}{\longrightarrow}S^2,$$ where $\sigma$ is the collapsing map. By the second part of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}, Milnor's $\mu$-invariant of $L$ is equal to half of Pontryagin's $\nu$-invariant $\nu(g_L)$ (comparing $g_L$ to the constant map $f_{000}$ as explained in Section [\[sec:pontryagin\]](#sec:pontryagin){reference-type="ref" reference="sec:pontryagin"}), which in turn is just the Hopf invariant of $f\colon S^3\to S^2$, $$\mu(L)\ = \ {1\over 2}\nu(g_L)\ = \ {1\over 2}\mathop{\rm Hopf}\nolimits(f).$$

We can thus use J. H. C. Whitehead's integral formula for the Hopf invariant as the first ingredient in our formula for the $\mu$ invariant. Starting from Hopf's definition of his invariant of a map $f\colon S^3\to S^2$ as the linking number between the inverse images of two regular values, Whitehead [@Whitehead] found an integral formula for $\mathop{\rm Hopf}\nolimits(f)$ as follows.

Let $\omega$ be the area 2-form on $S^2$, normalized so that $\int_{S^2}
\omega=1$. Its pullback $f^*\omega$ is a closed 2-form on $S^3$, which is exact because $H^2(S^3;\mathbb R)=0$. Hence $f^*\omega=d\alpha$ for some 1-form $\alpha$ on $S^3$, and Whitehead showed that the Hopf invariant of $f$ is given by the formula $$\mathop{\rm Hopf}\nolimits(f) \ = \ \int_{S^3}\alpha\wedge f^*\omega \ 
= \ \int_{S^3}\alpha\wedge d\alpha,$$ the value of the integral being independent of the choice of $\alpha$.

To make Whitehead's formula explicit requires a way to produce a 1-form $\alpha$ whose differential $d\alpha$ is a given 2-form $f^*\omega$ on $S^3$ which is known to be exact. We give an explicit formula for this in the Appendix, since it is not needed in the body of the paper. Instead, we are going to pull the whole situation back to $T^3$ and perform our calculations there.

In particular, the formula $$\mathop{\rm Hopf}\nolimits(f) \ = \  \int_{S^3}\alpha_0\wedge f^*\omega,$$ where $\alpha_0$ is any 1-form on $S^3$ such that $d\alpha_0=f^*\omega$, pulls back to the formula $$\nu(g_L)\ = \ \int_{T^3}\overline\alpha_0\wedge g^*\omega,$$ where $\overline\alpha_0$ is any 1-form on $T^3$ such that $d\overline\alpha_0 = g^*\omega$. One such choice of $\overline\alpha_0$ would be $\overline\alpha_0 = \sigma^*\alpha_0$, with $\alpha_0$ obtained as in the Appendix. However, since we don't have an explicit analytic formula for $\sigma$, and since the formula for $\alpha_0$ is complicated, we will pursue a slightly different approach.

Taking advantage of the fact that $g_L$ is homotopic to $g$, we also have $$\nu(g_L) \ = \  \int_{T^3}\alpha\wedge g_L^*\omega \ = \ \int_{T^3}\alpha\wedge \omega_L$$ for any $1$-form $\alpha$ on $T^3$ such that $d\alpha=\omega_L$. Therefore, what we really need is a canonical way to produce a $1$-form $\alpha$ on $T^3$ whose exterior derivative is the exact 2-form $\omega_L$. We will prove in Proposition [\[prop:alp\]](#prop:alp){reference-type="ref" reference="prop:alp"} that the $1$-form $$\alpha_L \ = \ \delta(\varphi* \omega_L)$$ has the desired property that $d\alpha_L=\omega_L$. Moreover, if $\widetilde\alpha$ is any other $1$-form such that $d\widetilde\alpha=\omega_L$, then $|\alpha_L| \le |\widetilde\alpha|$ in $L^2(T^3)$, with equality if and only if $\widetilde\alpha=\alpha_L$.

We thus obtain the explicit integral formula for Milnor's $\mu$-invariant of the three component link $L$: $$\mu(L) \ = \ {1\over 2}\nu(g_L) \ = \ {1\over 2}\int_{T^3}\delta(\varphi* \omega_L)\wedge\omega_L,$$ which is formula (1) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}.

The 1-form $\delta(\varphi* \omega_L)$ on $T^3$ which appears in formula (1) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} converts to the vector field $\nabla\times(\varphi* \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L)$, which can be regarded as the magnetic field on $T^3$ due to the current flow $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L$. The customary minus sign here is now hidden in the definitions of the Laplacian and its inverse (Green's operator).

The integral formula for Milnor's $\mu$-invariant given in formula (1), $$\mu(L) \ = \ {1\over 2}\int_{T^3}\delta(\varphi* \omega_L)\wedge\omega_L\,,$$ then converts to the formula $$\mu(L) \ = \ {1\over 2}\int_{T^3}\left(\vphantom{x^2}\nabla\times(\varphi* \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L)\right)\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L\,d\mathop{\rm vol}\nolimits$$ in the language of vector fields. To obtain formula (2) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}, we first expand out the convolution integral $$(\varphi* \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L)(\textup{\bf x}) \ = \ \int_{T^3}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})\,\varphi(\textup{\bf x}-\textup{\bf y})\,d\textup{\bf y}.$$ Then we compute its curl: $$\begin{aligned}
\left(\vphantom{x^2}\nabla_{\!\textup{\bf x}}\times(\varphi* \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L)\right)(\textup{\bf x})
\ &= \  \int_{T^3}\nabla_{\!\textup{\bf x}}\times\left(\vphantom{x^2}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})\,\varphi(\textup{\bf x}-\textup{\bf y})\right)\,d\textup{\bf y}\\
\ &= \  -\int_{T^3}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})\times\nabla_{\!\textup{\bf x}}\,\varphi(\textup{\bf x}-\textup{\bf y})\,d\textup{\bf y}\,,
\end{aligned}$$ using the product formula $\nabla\times(f\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf a}})=f(\nabla\times \overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf a}})-\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf a}}\times\nabla f$. Note that $\nabla_{\!\textup{\bf x}}\times\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})={\bf 0}$ since, from the point of view of the variable $\textup{\bf x}$, the vector field $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})$ is constant.

Inserting the expression for the curl of $\varphi*\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L$ into the formula for $\mu(L)$, we get $$\aligned
\mu(L)
&\ = \ -\frac12\int_{T^3\times T^3}\left(\vphantom{x^2}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})\times\nabla_{\!\textup{\bf x}}\,\varphi(\textup{\bf x}-\textup{\bf y})\right)\,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,
\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf x})\,d\textup{\bf x}\,d\textup{\bf y}\\
&\ = \ -\frac12\int_{T^3\times T^3}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf x})\times\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})\,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,\nabla_{\!\textup{\bf x}}\,\varphi(\textup{\bf x}-\textup{\bf y})\,d\textup{\bf x}\,d\textup{\bf y}\\
&\ = \ \frac12\int_{T^3\times T^3}\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf x})\times\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}_L(\textup{\bf y})\,\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\,\nabla_{\!\textup{\bf y}}\,\varphi(\textup{\bf x}-\textup{\bf y})\,d\textup{\bf x}\,d\textup{\bf y}\,,
\endaligned$$ where at the last step we hid the minus sign by taking the gradient of $\varphi$ with respect to $\textup{\bf y}$ instead of $\textup{\bf x}$, and obtained formula (2) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}.

# Fourier series and the Proof of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}, formula (3) {#sec:B'}

-.2in -.2in

In the proofs of formulas (1) and (2) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}, we needed to find a 1-form $\alpha$ on $T^3$ whose exterior derivative is the exact 2-form $\omega_L$ associated with the three-component link $L$ in $S^3$. We asserted that we can choose $\alpha=\delta(\varphi* \omega_L)$, where $\varphi$ is the fundamental solution of the scalar Laplacian on $T^3$. Furthermore, we asserted that this choice of $\alpha$ is canonical in the sense that it has the smallest $L^2$ norm among all possible choices. We justify these assertions in this section and lay the groundwork for the proof of formula (3) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} by studying the calculus of differential forms on $T^3=(\mathbb R/2\pi\mathbb Z)^3$ in terms of their Fourier series.

We will prove the following two results:

::: proposition
[]{#prop:fs label="prop:fs"} **  The fundamental solution of the scalar Laplacian on the\
$3$-torus $T^3 = (\mathbb R/2\pi\mathbb Z)^3$ is given by the formula $$\varphi(\textup{\bf x}) \ = \
{1\over 8\pi^3}\sum_{\textup{\bf n}\ne{\bf 0}}
e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}} / |\textup{\bf n}|^2.$$ The function $\varphi$ is $C^\infty$ at all points $\textup{\bf x}\in T^3$ except ${\bf 0}$, where it becomes infinite.**
:::

::: proposition
[]{#prop:alp label="prop:alp"} **If $\omega$ is any exact differential form on $T^3$ with $C^\infty$ coefficients, then $$\alpha \ = \ \delta(\varphi* \omega)$$ is a $C^\infty$ differential form satisfying $d\alpha=\omega$. Furthermore, if $d\widetilde\alpha=\omega$ as well, then $|\alpha|_{L^2}\le|\widetilde\alpha|_{L^2}$, with equality if and only if $\widetilde\alpha=\alpha$.**
:::

Before diving into calculations, we pause for some words of explanation: We write $\Omega^k(T^3)$ for the space of $C^\infty$ $k$-forms on $T^3$. With $d$ as the exterior differentiation operator taking $\Omega^k(T^3)$ to $\Omega^{k+1}(T^3)$, and $\delta$ the co-differentiation map adjoint to $d$ in the $L^2$ sense, the Laplacian of a $k$-form $\alpha$ is $$\Delta\alpha \ = \ (d\delta+\delta d)\alpha.$$ This definition gives us the "geometer's sign convention" for the Laplacian on functions (0-forms): $$\Delta f \ = \  -\left({\partial^2 f\over\partial x_1^2}+{\partial^2 f\over\partial x_2^2} +
{\partial^2 f\over\partial x_3^2}\right).$$

The *fundamental solution of the scalar Laplacian is a function $\varphi$, convolution with which "inverts" the Laplacian to the extent that this is possible. On $T^3$, only functions that integrate to zero are in the range of the Laplacian, and so "the" fundamental solution of $\Delta$ on $T^3$ is the function $\varphi$ which satisfies $$\int_{T^3}\varphi\,d\!\mathop{\rm vol}\nolimits\ = \  0
\qquad\textup{and}\qquad 
\Delta(\varphi * f) \ = \ f$$ for all $f\in C^\infty(T^3)$ such that $\displaystyle{\int_{T^3}f\,d\!\mathop{\rm vol}\nolimits=0}$.*

Even though we have expressed $\varphi$ in terms of complex exponentials, the value of $\varphi$ is real for real values of $\textup{\bf x}$ because of the symmetry of the coefficients.

Figure [18](#fig:fundsol){reference-type="ref" reference="fig:fundsol"} shows the graph of the corresponding fundamental solution $$\varphi(\textup{\bf x}) \ = \
{1\over 4\pi^2}\sum_{\textup{\bf n}\ne{\bf 0}} e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}} /  |\textup{\bf n}|^2$$ of the scalar Laplacian on the 2-torus $S^1 \times S^1$, summed for $|\textup{\bf n}| \leq 10$, and displayed over the range $[-3\pi,3\pi]\times[-3\pi,3\pi]$.

![Fundamental solution of the scalar Laplacian on $S^1 \times S^1$](FigFundSolDennis.pdf){#fig:fundsol height="260pt"}

With respect to the $L^2$ inner product $$\langle f,g\rangle \ = \  \int_{T^3}f(\textup{\bf x})\,\overline{g(\textup{\bf x})}\,d\textup{\bf x}\,,$$ the set of complex exponentials $\{e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}} \ | \ \textup{\bf n}\in\mathbb Z^3\}$ is an orthogonal set, and for all $\textup{\bf n}$, we have $\langle e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}},e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\rangle = 8\pi^3$.

Any function $f$ in $L^2(T^3)$ can be expanded into a Fourier series $$f\ \sim \ \sum_{\textup{\bf n}\in\mathbb Z^3} c_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}$$ where $$c_\textup{\bf n}\ = \ {1\over 8\pi^3}\langle f,e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\rangle \ = \  {1\over 8\pi^3}\int_{T^3} f(\textup{\bf x})\,e^{-i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,d\textup{\bf x}.$$ Moreover, by Plancharel's theorem, the $L^2(T^3)$-norm of $f$ is equal to the $\ell^2$-norm of the sequence of coefficients: $$|f|_{L^2} \ = \  \int_{T^3}|f(x)|^2\,d\textup{\bf x}\ = \  \sum_{\textup{\bf n}\in\mathbb Z^3} 8\pi^3|c_\textup{\bf n}|^2.$$ This shows that the function $\varphi$ of Proposition [\[prop:fs\]](#prop:fs){reference-type="ref" reference="prop:fs"} is in $L^2(T^3)$, since $|c_\textup{\bf n}|^2$ is of order $1/|\textup{\bf n}|^4$, while the number of lattice points at distance $|\textup{\bf n}|$ from ${\bf 0}$ is of order $|\textup{\bf n}|^2$.

Because the range of the scalar Laplacian is the (closed) subspace of functions $f$ for which $$\int_{T^3} f(\textup{\bf x})\,d\textup{\bf x}\ = \ 0\,,$$ we will denote this subspace of $L^2(T^3)$ by $L^2_0(T^3)$, and similarly for other function spaces, where a zero subscript will indicate that all functions in the space have average value zero. In terms of Fourier coefficients, $f\in L^2_0(T^3)$ if and only if the Fourier coefficient $c_{\bf 0}=c_{(0,0,0)}=0$.

For functions $f$ and $g$ in $C^\infty(T^3)$, their ***convolution*** $f*g$ is defined by $$\left(\vphantom{x^2}f*g\right)(\textup{\bf x})\ = \ \int_{T^3}f(\textup{\bf y})\,g(\textup{\bf x}-\textup{\bf y})\,d\textup{\bf y}\,,$$ and also lies in $C^\infty(T^3)$. One checks easily that $e^{i\textup{\bf m}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}*e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}} = 0$ if $\textup{\bf m}\neq \textup{\bf n}$, and $$e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}*e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\ = \ 8\pi^3 e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}.$$ Therefore, if $f$ and $g$ have Fourier series $\sum c_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}$ and $\sum d_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}$ respectively, then the Fourier series of $f*g$ is $$8\pi^3\sum_{\textup{\bf n}\in\mathbb Z^3}c_{\textup{\bf n}}d_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}.$$

From this it follows that the operation of convolution satisfies $f*g=g*f$ and $(f*g)*h=f*(g*h)$ whenever all the convolutions are defined. Furthermore, $${\partial\over \partial x_k}(f*g)\ = \ {\partial f\over \partial x_k}*g \ = \  f*{\partial g\over \partial x_k}.$$

For $u\in C^\infty(T^3)$, with $$u(\textup{\bf x})\ = \ \sum_{\textup{\bf n}\in\mathbb Z^3} b_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,,$$ we have $$\Delta u(\textup{\bf x})\ = \ \sum_{\textup{\bf n}\neq{\bf 0}}|\textup{\bf n}|^2b_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}.$$ Because the $(0,0,0)$-coefficient of $\Delta u$ is zero, this shows why in order to solve $\Delta u=f$ we must restrict $f$ to be in $C^\infty_0(T^3)$. And for $f\in C^\infty_0(T^3)$, with $$f(\textup{\bf x})\ = \ \sum_{\textup{\bf n}\neq{\bf 0}}c_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}},$$ the unique solution $u\in C^\infty_0(T^3)$ of $\Delta u=f$ has $b_{\textup{\bf n}}= c_\textup{\bf n}/|\textup{\bf n}|^2$, and so, since $$\varphi(\textup{\bf x})\ = \ \frac{1}{8\pi^3}\sum_{\textup{\bf n}\ne{\bf 0}}{e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}}/{|\textup{\bf n}|^2}\,,$$ we conclude that $u=\varphi * f$. This completes the proof of Proposition [\[prop:fs\]](#prop:fs){reference-type="ref" reference="prop:fs"} except for the assertion about the smoothness of $\varphi$ away from its singularity, which follows from well-known local regularity theorems for elliptic partial differential equations (see, for example, Folland [@Folland], Theorem 6.33).

To prove Proposition [\[prop:alp\]](#prop:alp){reference-type="ref" reference="prop:alp"}, we express the calculus of differential forms on $T^3$ in terms of Fourier series. Except for the fundamental solution $\varphi$ of the (scalar) Laplacian on $T^3$, we will assume all functions and forms are $C^\infty$.

We continue to express functions (0-forms) as Fourier series: for $\textup{\bf x}=(s,t,u)$ and $\textup{\bf n}=(n_1,n_2,n_3)$, we write $$f(\textup{\bf x}) \ = \ \sum_{\textup{\bf n}\in\mathbb Z^3}c_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\ \in\ \Omega^0(T^3).$$ Likewise, we employ the notation described in the introduction and express 1-forms using $\textup{\bf c}_{\textup{\bf n}}=(c_\textup{\bf n}^{s},c_\textup{\bf n}^{t},c_\textup{\bf n}^{u})$ and $d\textup{\bf x}=(ds,dt,du)$. We write $$\alpha(\textup{\bf x}) \ = \ \sum_{\textup{\bf n}\in\mathbb Z^3}\textup{\bf c}_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}d\textup{\bf x}\ \in\ \Omega^1(T^3).$$ With $\star d\textup{\bf x}=(dt\wedge du,du\wedge ds,ds\wedge dt)$ as before, we can express a 2-form as $$\beta(\textup{\bf x}) \ = \ \sum_{\textup{\bf n}\in\mathbb Z^3}\textup{\bf c}_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\star d\textup{\bf x}\ \in\ \Omega^2(T^3).$$ Finally, with $dV=ds\wedge dt\wedge du$, a 3-form can be written as $$\gamma(\textup{\bf x}) \ = \ \sum_{n\in\mathbb Z^3}c_{\textup{\bf n}}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}dV\ \in\ \Omega^3(T^3).$$

It is straightforward to express both the exterior derivative $d$ and the codifferential $\delta$ in terms of Fourier coefficients. With $f$, $\alpha$, $\beta$ and $\gamma$ as above, we have $$\begin{array}{lll}
\displaystyle{df \ = \ \sum ic_{\textup{\bf n}}\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}d\textup{\bf x}} &
\mbox{\rm\ and\ } & \delta f \ = \ 0,\\[0.3cm]
\displaystyle{d\alpha \ = \ \sum i\textup{\bf n}\times \textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\star d\textup{\bf x}} &
\mbox{\rm\ and\ } & \displaystyle{\delta\alpha \ = \ -\sum i\textup{\bf n}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}},\\[0.3cm]
\displaystyle{d\beta \ = \ \sum i\textup{\bf n}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}dV} &
\mbox{\rm\ and\ } & \displaystyle{\delta\beta \ = \ \sum i\textup{\bf n}\times\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}
\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}d\textup{\bf x},}\\[0.3cm]
d\gamma \ = \ 0 & \mbox{\rm\ and\ } & 
\displaystyle{\delta\gamma \ = \ -\sum ic_\textup{\bf n}\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\star d\textup{\bf x}}.
\end{array}$$ Thus, exterior differentiation and co-differentiation are expressed in terms of vector algebraic operations on the Fourier coefficients. From these expressions, we conclude the following about the kernel and image of $d$ and $\delta$:

-   For 0-forms, $$\begin{aligned}
    \ker d &\ = \ \{f \ | \ c_\textup{\bf n}=0\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},
    \mbox{\rm\ while\ }
    \ c_{\bf 0}
    \ \mbox{\rm is arbitrary}\} \ \ \ \\[0.2cm]
    \mathrm{im\,}d\, &\ = \  \{0\} \\[0.2cm]
    \ker \delta &\ = \  \{\mbox{\rm all}\ f\} \\[0.2cm]
    \mathrm{im\,}\delta\, &\ = \  \{f \ | \ c_{\bf 0}=0\}
    \end{aligned}$$

-   For 1-forms, $$\begin{aligned}
    \ker d &\ = \  \{\alpha \ | \ \textup{\bf c}_\textup{\bf n}=\lambda_\textup{\bf n}\textup{\bf n}\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},
    \mbox{\rm\ while\ }\textup{\bf c}_{\bf 0}
    \ \mbox{\rm is arbitrary}\} \\[0.2cm] 
    \mathrm{im\,}d\, &\ = \  \{\alpha \ | \ \textup{\bf c}_\textup{\bf n}=\lambda_\textup{\bf n}\textup{\bf n}\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},\ \textup{\bf c}_{\bf 0}={\bf 0}\} \\[0.2cm]
    \ker \delta &\ = \  \{\alpha \ | \ \textup{\bf c}_\textup{\bf n}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf n}=0\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},
    \mbox{\rm\ while\ }\textup{\bf c}_{\bf 0}\ \mbox{\rm is arbitrary}\} \\[0cm]

    \mathrm{im\,}\delta\, &\ = \  \{\alpha \ | \ \textup{\bf c}_\textup{\bf n}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf n}=0\ \mbox{\rm for}
    \ \textup{\bf n}\ne{\bf 0},\ \textup{\bf c}_{\bf 0}={\bf 0}\}
    \end{aligned}$$

-   For 2-forms, $$\begin{aligned}
    \ker d &\ = \  \{\beta \ | \ \textup{\bf c}_\textup{\bf n}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf n}=0\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},
    \mbox{\rm\ while\ }\textup{\bf c}_{\bf 0}
    \ \mbox{\rm is arbitrary}\} \\[0.01cm]
    \mathrm{im\,}d\, &\ = \  \{\beta \ | \ \textup{\bf c}_\textup{\bf n}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\textup{\bf n}=0\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},\ \textup{\bf c}_{\bf 0}={\bf 0}\} \\[0cm]
    \ker \delta &\ = \  \{\beta \ | \ \textup{\bf c}_\textup{\bf n}=\lambda_\textup{\bf n}\textup{\bf n}\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},
    \mbox{\rm\ while\ }\textup{\bf c}_{\bf 0}\ \mbox{\rm is arbitrary}\} \\[0cm]
    \mathrm{im\,}\delta\, &\ = \  \{\beta \ | \ \textup{\bf c}_\textup{\bf n}=\lambda_\textup{\bf n}\textup{\bf n}\ \mbox{\rm for}
    \ \textup{\bf n}\ne{\bf 0},\ \textup{\bf c}_{\bf 0}={\bf 0}\}
    \end{aligned}$$

-   For 3-forms, $$\begin{aligned}
    \ker d&\ = \ \{\mbox{\rm all}\ \gamma\}\\[0.15cm]
    \mathrm{im\,}d\, &\ = \  \{\gamma \ | \ c_{\bf 0}=0\} \\[0.2cm]
    \ker \delta &\ = \  \{\gamma \ | \ c_\textup{\bf n}=0\ \mbox{\rm for}\ \textup{\bf n}\ne{\bf 0},
    \mbox{\rm\ while\ }\ c_{\bf 0}
    \ \mbox{\rm is arbitrary}\} \\[0.1cm]
    \mathrm{im\,}\delta\, &\ = \ \{0\}
    \end{aligned}$$

Therefore $\mathrm{im\,}d\subset\ker d$ and $\mathrm{im\,}\delta\subset\ker\delta$, and the following orthogonal (with respect to the $L^2$ inner product) decompositions hold: $$\Omega^k(T^3)\ = \ \ker\delta\oplus\mathrm{im\,}d \ = \ \mathrm{im\,}\delta\oplus\ker d$$ for $k=0,\ldots,3$. The $k$-forms in $\ker d\cap\ker\delta$ are the forms whose Fourier series contain only constant terms. These are called *harmonic $k$-forms because they are in the kernel of the Laplacian $\Delta=d\delta+\delta d$, so we write $\mathop{\rm Har}\nolimits^k(T^3)=\ker d\cap\ker\delta$. We then have the Hodge decomposition $$\Omega^k(T^3)\ = \ \mathrm{im\,}\delta\oplus\mathop{\rm Har}\nolimits^k(T^3)\oplus \mathrm{im\,}d.$$ The Laplacian $\Delta\colon\Omega^k(T^3)\to\Omega^k(T^3)$ preserves this Hodge decomposition, taking $\mathrm{im\,}\delta$ bijectively to itself, killing $\mathop{\rm Har}\nolimits^k(T^3)$, and taking $\mathrm{im\,}d$ bijectively to itself.*

We must show that if $\omega$ is any $C^\infty$ exact differential $k$-form on $T^3$, then the $(k-1)$-form $\alpha=\delta(\varphi*\omega)$ is $C^\infty$ and satisfies $d\alpha=\omega$, and that if $d\widetilde\alpha=\omega$ as well, then $|\alpha|_{L^2}
\le|\widetilde\alpha|_{L^2}$, with equality if and only if $\widetilde\alpha=\alpha$.

Because it is the case we use in Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}, we will carry this out specifically for 2-forms. The proofs for 1-forms and 3-forms are essentially the same.

For a 2-form $$\beta\ = \ \sum_{\textup{\bf n}\in\mathbb Z^3}\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\star d\textup{\bf x}\,,$$ its Laplacian is given by $$\Delta\beta\ = \ \sum_{\textup{\bf n}\ne{\bf 0}}|\textup{\bf n}|^2\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\star d\textup{\bf x}.$$ We can use convolution with the fundamental solution $\varphi$ of the scalar Laplacian to express the Green's operator, $$\mathop{\rm Gr}\nolimits(\beta)\ = \ \varphi* \beta \ = \  \sum_{\textup{\bf n}\ne {\bf 0}}{\textup{\bf c}_\textup{\bf n}\over|\textup{\bf n}|^2}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}\star d\textup{\bf x}.$$ Clearly the Laplacian $\Delta$ and the Green's operator are inverses of one another when applied to 2-forms $\beta$ with $\textup{\bf c}_{\bf 0}={\bf 0}$, equivalently, to 2-forms $\beta$ orthogonal to $\mathop{\rm Har}\nolimits^2(T^3)$.

To prove Proposition [\[prop:alp\]](#prop:alp){reference-type="ref" reference="prop:alp"}, assume that $\beta$ is exact, that is, $\beta\in\mathrm{im\,}d$. Then $\mathop{\rm Gr}\nolimits(\beta)$ is also exact, hence certainly closed, and therefore $$\beta\ = \ \Delta\mathop{\rm Gr}\nolimits(\beta)\ = \ (d\delta+\delta d)\mathop{\rm Gr}\nolimits(\beta)\ = \ d\delta\mathop{\rm Gr}\nolimits(\beta)\ = \ d\delta(\varphi*\beta).$$ Thus $\alpha=\delta(\varphi*\beta)$ satisfies $d\alpha=\beta$.

If $\widetilde\alpha$ is any other 2-form satisfying $d\widetilde\alpha=\beta$, then $\widetilde\alpha$ differs from $\alpha$ by some closed 2-form, which must be $L^2$-orthogonal to $\alpha$ since $\alpha\in\mathrm{im\,}\delta$. Thus, $|\alpha|_{L^2}\le|\widetilde\alpha|_{L^2}$ by the Pythagorean theorem.

Since the Fourier coefficients of a $C^\infty$ 2-form decrease faster than any negative power of $|\textup{\bf n}|$, we have that $\mathop{\rm Gr}\nolimits(\beta)$ and $\delta\mathop{\rm Gr}\nolimits(\beta)$ will be $C^\infty$ if $\beta$ is. This completes the proof of Proposition [\[prop:alp\]](#prop:alp){reference-type="ref" reference="prop:alp"}.

This formula expresses Milnor's invariant $\mu(L)$ in terms of the Fourier coefficients of $\omega_L$: $$\mu(L)\ = \ 8\pi^3\sum_{\textup{\bf n}\ne{\bf 0}}\frac{\textup{\bf a}_\textup{\bf n}\times\textup{\bf b}_\textup{\bf n}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf n}}{|\textup{\bf n}|^2}$$ where $$\omega_L\ = \ \sum_{\textup{\bf n}\ne{\bf 0}}\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\star d\textup{\bf x}$$ with $\textup{\bf c}_\textup{\bf n}=\textup{\bf a}_\textup{\bf n}+i\textup{\bf b}_\textup{\bf n}$ and with $\textup{\bf a}_\textup{\bf n}$ and $\textup{\bf b}_\textup{\bf n}$ real.

The formula for $\omega_L$ is summed over $\textup{\bf n}\ne{\bf 0}$ because the hypothesis of pairwise linking numbers zero is equivalent to the vanishing of the harmonic component of $\omega_L$, which in turn is equivalent to the vanishing of its Fourier coefficient $\textup{\bf c}_{\bf 0}$.

We begin with formula (1) of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} for $\mu(L)$: $$\mu(L)\ = \ {1\over 2}\int_{T^3}\delta(\varphi*\omega_L)\wedge\omega_L.$$ We have $$\varphi*\omega_L\ = \ \sum_{\textup{\bf n}\ne{\bf 0}}\frac{\textup{\bf c}_\textup{\bf n}e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}}{|\textup{\bf n}|^2}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\star d\textup{\bf x}\,,$$ and hence, from our table of derivatives and co-derivatives in terms of Fourier series, $$\delta(\varphi*\omega_L)\ = \ \sum_{\textup{\bf n}\ne{\bf 0}} \frac{(\textup{\bf n}\times\textup{\bf c}_\textup{\bf n})\,i\,e^{i\textup{\bf n}\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}}{|\textup{\bf n}|^2}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,d\textup{\bf x}.$$ To compute $\delta(\varphi*\omega_L)\wedge\omega_L$, we use the fact that if $\textup{\bf v}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,d\textup{\bf x}$ is a 1-form and $\textup{\bf w}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\! \star \!d\textup{\bf x}$ is a 2-form, then $$(\textup{\bf v}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,d\textup{\bf x})\wedge(\textup{\bf w}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\! \star\!d\textup{\bf x})\ = \ (\textup{\bf v}\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf w})\,dV.$$ Thus $$\delta(\varphi*\omega_L)\wedge\omega_L\ = \ \sum_{\textup{\bf m}\ne{\bf 0}}\sum_{\textup{\bf n}\ne{\bf 0}}
\frac{(\textup{\bf n}\times\textup{\bf c}_\textup{\bf n})\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf c}_\textup{\bf m}\,ie^{i(\textup{\bf m}+\textup{\bf n})\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}}{|\textup{\bf n}|^2}\,dV.$$ When we insert this double sum into the integral $\mu(L)={1\over 2}\int_{T^3}\delta(\varphi*\omega_L)\wedge\omega_L,$ most of the terms in the summation will integrate to zero, leaving only the terms where $\textup{\bf m}+\textup{\bf n}={\bf 0}$. In those cases, $e^{i(\textup{\bf m}+\textup{\bf n})\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\textup{\bf x}}=e^0=1$ integrates to $8\pi^3$, the volume of $T^3$.

Thus $$\begin{aligned}
\mu(L)&\ = \ 4\pi^3\sum_{\textup{\bf n}\ne{\bf 0}}\frac{i(\textup{\bf n}\times\textup{\bf c}_\textup{\bf n})\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf c}_{-\textup{\bf n}}}{|\textup{\bf n}|^2} \\
&\ = \ 4\pi^3\sum_{\textup{\bf n}\ne{\bf 0}}\frac{i(\textup{\bf c}_\textup{\bf n}\times\textup{\bf c}_{-\textup{\bf n}})\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf n}}{|\textup{\bf n}|^2}
\end{aligned}$$ and it remains to simplify this last series.

Since $\textup{\bf c}_\textup{\bf n}=\textup{\bf a}_\textup{\bf n}+i\textup{\bf b}_\textup{\bf n}$ and since $\omega_L$ is real-valued, we have $\textup{\bf c}_{-\textup{\bf n}} = \overline\textup{\bf c}_\textup{\bf n} = \textup{\bf a}_\textup{\bf n}-i\textup{\bf b}_\textup{\bf n}.$ Hence $$\textup{\bf c}_\textup{\bf n}\times\textup{\bf c}_{-\textup{\bf n}}\ = \ (\textup{\bf a}_\textup{\bf n}+i\textup{\bf b}_\textup{\bf n})\times(\textup{\bf a}_\textup{\bf n}-i\textup{\bf b}_\textup{\bf n})\ = \ 
-2i\,\textup{\bf a}_\textup{\bf n}\times\textup{\bf b}_\textup{\bf n},$$ and therefore $$\begin{aligned}
\mu(L)&\ = \ 4\pi^3\sum_{\textup{\bf n}\ne{\bf 0}}\frac{i(\textup{\bf c}_\textup{\bf n}\times\textup{\bf c}_{-\textup{\bf n}})\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf n}}{|\textup{\bf n}|^2}\\
&\ = \ 8\pi^3\sum_{\textup{\bf n}\ne{\bf 0}}\frac{(\textup{\bf a}_\textup{\bf n}\times\textup{\bf b}_\textup{\bf n})\,\,\raisebox{-.3ex}{\Large$\hskip-.02in\cdot$\hskip.005in}\,\textup{\bf n}}{|\textup{\bf n}|^2}\,,
\end{aligned}$$ completing the proof of formula (3) and, with it, that of Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}.

We used Maple and Matlab to calculate an approximation to Milnor's $\mu$-invariant for the three-component link $L$ in $S^3$ given by $$\aligned
x(s)&\ = \ [\textstyle{4\over 5}\sin s,\cos s,\textstyle{3\over 5}\sin s,0], \\
y(t)&\ = \ [\textstyle{4\over 5}\sin t,0,\cos t,\textstyle{3\over 5}\sin t], \\
z(u)&\ = \ [\textstyle{4\over 5}\sin u,\textstyle{3\over 5}\sin u,0,\cos u],
\endaligned$$ for $s\in[0,2\pi]$, $t\in[0,2\pi]$ and $u\in[0,2\pi]$, which is a concrete realization of the Borromean rings with $\mu=-1$.

![Borromean rings](FigBorRafal.pdf){#fig:bor height="130pt"}

Maple gave the (long, ugly) formula for $\omega_L$ obtained from Proposition [\[prop:char\]](#prop:char){reference-type="ref" reference="prop:char"}, and we used Matlab to calculate approximations to its Fourier coefficients $\textup{\bf c}_\textup{\bf n}$ for divisions of the $s$, $t$ and $u$ intervals into 60 subintervals and for $\textup{\bf n}\in[-15,15]^3$. The approximation of $\mu$ we obtained in this way was $-0.97$.
