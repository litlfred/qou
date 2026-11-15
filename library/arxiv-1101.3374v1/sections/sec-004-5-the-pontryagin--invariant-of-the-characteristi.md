---
doc_id: arxiv-1101.3374v1
doc_title: "Pontryagin invariants and integral formulas for Milnor's triple linking number"
section_id: sec-004-5-the-pontryagin--invariant-of-the-characteristi
section_title: "The Pontryagin -invariant of the characteristic map"
section_number: 5
pages: 25-41
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 0.983
doc_brief: "Pontryagin invariants and integral formulas for Milnor's triple linking number — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
---
[]{#sec:Aprep label="sec:Aprep"}

Fix a link $L$ in $S^3$ with three components $X$, $Y$ and $Z$ parametrized by $x=x(s)$, $y=y(t)$ and $z=z(u)$. Recalling that $S^3$ is regarded as the group of unit quaternions, the asymmetric characteristic map $h_L:T^3\to S^2$ is given by $$h_L(s,t,u) \ = \ (y_z-x_z)/|y_z-x_z|$$ where $a_z$ is an abbreviation for the vector $\mathrm{pr}_{-1}(-a\bar z)$ in pure imaginary quaternion $3\text{-space}$ $\mathbb R^3$. To carry out the proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}, we need a way to compute the absolute Pontryagin $\nu$-invariant of $h_L$. A procedure for doing so is described here.

Throughout this section and the next, $\mathbb R^3$ is pictured in the usual way, with the $ij$-plane horizontal and the $k$-axis pointing straight up as in Figure [1](#fig:quat){reference-type="ref" reference="fig:quat"}. In particular, we view $k$ as the north pole of the unit sphere $S^2$.

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

The longitudinal projection defines the ***standard open book*** in $\mathbb R^3$, with binding the $k$-axis, and with pages $P_\theta = \ell^{-1}(\theta)$ for $\theta\in S^1$. The pages are just the oriented vertical half-planes bounded by the $k$-axis, each indexed by its polar angle as shown in Figure [2](#fig:book){reference-type="ref" reference="fig:book"}. The meridional projection serves to identify each page $P_\theta$ with the hyperbolic plane $\mathbb H$, with "center\"  $i_\theta = i\,\cos\theta + j\,\sin\theta$  corresponding to $i$. The union of all the page centers is the unit circle $C$.

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

An example of a generic link is shown in Figure [3](#fig:generic){reference-type="ref" reference="fig:generic"}. It has four critical points, two on $X$ and two on $Y$, indicated by dots in the picture.

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

A page vector $(x,y)$ will be called ***critical*** if $x$ or $y$ is a critical point of $L$, and ***regular*** if both $x$ and $y$ are regular. A regular page vector is ***positive*** if the oriented strands of $L$ through $x$ and $y$ point in the same direction, meaning $\textup{sign}(x) = \textup{sign}(y)$, and is ***negative*** if they point in opposite directions. These notions are illustrated in Figure [4](#fig:pagevectors){reference-type="ref" reference="fig:pagevectors"}, in which the vectors labeled $1$ and $2$ are positive regular page vectors, $3$ is negative regular, and $4$ is critical.

<figure id="fig:pagevectors">
<embed src="FigPageVectors2.pdf" style="height:2.36111in" />
<p>(-150,105)<span><span class="math inline">1</span></span> (-156,73)<span><span class="math inline">2</span></span> (-112,85)<span><span class="math inline">3</span></span> (-65,98)<span><span class="math inline">4</span></span> (-185,105)<span><span class="math inline"><em>X</em></span></span> (-20,102)<span><span class="math inline"><em>Y</em></span></span> (-106,18)<span><span class="math inline"><em>Z</em></span></span></p>
<figcaption>Page vectors</figcaption>
</figure>

Now consider the spaces $$\mathcal D\ = \ \{\text{isogonal points in $T^2$}\} \qquad\text{and}\qquad \mathcal P\ = \ \{\text{page vectors in $L$}\} \,.$$ By definition $\mathcal D$ parametrizes $\mathcal P$. The genericity of $L$ implies that $\mathcal P$ consists of a finite number of disjoint cycles of page vectors, and that $\mathcal D$ consists of a finite collection of smooth simple closed curves in $T^2$. Orient $\mathcal P$ so that it points to the right (meaning in the direction of increasing polar angle) at each positive regular page vector in it, and to the left at each negative regular page vector. This gives a well-defined orientation on $\mathcal P$, inducing one on $\mathcal D$ as well. We call these the ***preferred orientations*** on $\mathcal P$ and $\mathcal D$.

::: definition
A ***bicycle*** (or "bi-cycle\") in $L$ is a component $\mathcal P_i$ of $\mathcal P$, that is, an oriented cycle of page vectors. Each bicycle is parametrized by a component $\mathcal D_i$ of $\mathcal D$, which we call its associated ***icycle*** (or "i-cycle\").
:::

We first draw in Figure [5](#fig:local){reference-type="ref" reference="fig:local"} four local pictures of a bicycle near a regular page vector, and below them, their parametrizing icycles. It is understood that these pictures take place somewhere in front of the upward pointing $Z$ axis. The four cases represent the possible directions of $X$ and $Y$ relative to the page containing the vector. In each case, the orientation of the bicycle is indicated by a squiggly arrow.

<figure id="fig:local">
<p><embed src="FigLocal.pdf" style="height:2.43056in" /> (-374,146)<span><span class="math inline"><em>Y</em></span></span> (-376,96)<span><span class="math inline"><em>X</em></span></span></p>
<p>(-215,147)<span><span class="math inline"><em>Y</em></span></span> (-217,96)<span><span class="math inline"><em>X</em></span></span></p>
<p>(-115,147)<span><span class="math inline"><em>Y</em></span></span> (-171,96)<span><span class="math inline"><em>X</em></span></span></p>
<p>(-65,147)<span><span class="math inline"><em>Y</em></span></span> (-13,96)<span><span class="math inline"><em>X</em></span></span></p>
<p>(-318,3)<span><span class="math inline"><em>s</em></span></span> (-363,50)<span><span class="math inline"><em>t</em></span></span> (-216,3)<span><span class="math inline"><em>s</em></span></span> (-261,50)<span><span class="math inline"><em>t</em></span></span> (-114,2)<span><span class="math inline"><em>s</em></span></span> (-159,49)<span><span class="math inline"><em>t</em></span></span> (-12,2)<span><span class="math inline"><em>s</em></span></span> (-57,49)<span><span class="math inline"><em>t</em></span></span></p>
<figcaption>Local pictures of a bicycle and its corresponding icycle</figcaption>
</figure>

For an example of a full bicycle, consider the "clasp\" between $X$ and $Y$ pictured in Figure [6](#fig:claspbike){reference-type="ref" reference="fig:claspbike"}(a). This gives rise to the bicycle in Figure [6](#fig:claspbike){reference-type="ref" reference="fig:claspbike"}(b), passing successively through the vectors labeled $1,2,3,4$ and then back to $1$. The associated icycle is a counterclockwise circle in $T^2$, shown in Figure [6](#fig:claspbike){reference-type="ref" reference="fig:claspbike"}(c). The route taken by this bicycle is "short\" in the sense that it does not wind around the binding, although it does spin within the pages.

<figure id="fig:claspbike">
<p><embed src="FigClasp.pdf" style="height:1.11111in" /> (-280,53)<span><span class="math inline"><em>X</em></span></span> (-350,15)<span><span class="math inline"><em>Y</em></span></span> (-325,66)<span><span class="math inline"><em>Z</em></span></span> (-198,45)<span><span class="math inline">1</span></span> (-160,51)<span><span class="math inline">2</span></span> (-202,33)<span><span class="math inline">3</span></span> (-160,25)<span><span class="math inline">4</span></span> (2,6)<span><span class="math inline"><em>s</em></span></span> (-82,73)<span><span class="math inline"><em>t</em></span></span> (-42,64)<span><span class="math inline">1</span></span> (-65,40)<span><span class="math inline">2</span></span> (-42,17)<span><span class="math inline">3</span></span> (-19,40)<span><span class="math inline">4</span></span> (-340,-20)<span>(a) the clasp</span> (-215,-20)<span>(b) the bicycle</span> (-80,-20)<span>(c) the icycle</span></p>
<figcaption>Bicycle arising from a clasp</figcaption>
</figure>

As another example, the link shown in Figure [3](#fig:generic){reference-type="ref" reference="fig:generic"} and reproduced in Figure [7](#fig:icycles){reference-type="ref" reference="fig:icycles"}(a) below has three bicycles. Two of them are short, arising from the clasps as in the previous example, while the remaining long one oscillates back and forth in the longitudinal direction, eventually making one full revolution around the binding. It is an instructive exercise left to the reader to recover the plot of the associated icycles in Figure [7](#fig:icycles){reference-type="ref" reference="fig:icycles"}(b), in which the trivial circles labeled $A$ and $B$ correspond to the clasps in $L$ with the same labels, $C$ labels the icycle that parametrizes the long bicycle, and the corners of the square parametrize the pair $(x,y)$ indicated by the dots in Figure [7](#fig:icycles){reference-type="ref" reference="fig:icycles"}(a).

<figure id="fig:icycles">
<p><embed src="FigIcycles.pdf" style="height:1.73611in" /> (2,20)<span><span class="math inline"><em>s</em></span></span> (-83,104)<span><span class="math inline"><em>t</em></span></span> (-300,90)<span><span class="math inline"><em>X</em></span></span> (-295,20)<span><span class="math inline"><em>Y</em></span></span> (-238,115)<span><span class="math inline"><em>Z</em></span></span> (-248,54)<span><span class="math inline"><em>A</em></span></span> (-215,52)<span><span class="math inline"><em>B</em></span></span> (-44,53)<span><span class="math inline"><em>A</em></span></span> (-29,36)<span><span class="math inline"><em>B</em></span></span> (-27,80)<span><span class="math inline"><em>C</em></span></span> (-280,-15)<span>(a) the generic link <span class="math inline"><em>L</em></span></span> (-90,-15)<span>(b) the icycles of <span class="math inline"><em>L</em></span></span></p>
<figcaption>A generic link and its icycles</figcaption>
</figure>

Before proceeding, we remind the reader that our interest in icycles associated to $L$ stems from the fact that -- when suitably decorated -- they give a toral diagram for a Pontryagin link of the characteristic map $h_L$. This is the content of the bicycle theorem.

The longitudinal and meridional projections on $S^3-K$, defined earlier,

induce projections by the same name on the space $\mathcal P$ of page vectors, $$S^1 \, \overset{\ell}{\longleftarrow} \, \mathcal P\, \overset{m}{\longrightarrow} \, \mathbb H\,,$$ given by $\ell(x,y) = \ell(x) = \ell(y)$ and $m(x,y) = \arg(m(y)-m(x))$. In other words $\ell(x,y)$ is the polar angle that parametrizes the common hemispherical page in $S^3$ containing $x$ and $y$, and $m(x,y)$ is the argument of the vector from $m(x)$ to $m(y)$ in

$\mathbb H$.

Using these projections, we define the ***longitudinal*** and ***meridional degrees*** of a bicycle $\mathcal P_i$ in $L$ by $$\ell_i \ = \ \textup{deg}(\ell|\mathcal P_i) \qquad\text{and}\qquad  m_i \ = \ \textup{deg}(m|\mathcal P_i). \label{degrees}$$ These integer invariants record, respectively, the number of times $\mathcal P_i$ travels around the binding $Z$, and the number of times its vectors spin around in the pages as it goes.

For example, any bicycle arising from a clasp between $X$ and $Y$ has zero longitudinal degree, while its meridional degree can be $\pm1$. In particular, the one shown in Figure [6](#fig:claspbike){reference-type="ref" reference="fig:claspbike"} has meridional degree $-1$, while the ones labeled $A$ and $B$ in Figure [7](#fig:icycles){reference-type="ref" reference="fig:icycles"}(a) have degrees $1$ and $-1$, respectively. The long bicycle in Figure [7](#fig:icycles){reference-type="ref" reference="fig:icycles"}(a), labeled $C$, has longitudinal degree $2$ and meridional degree $1$.

For any icycle $\mathcal D_i$ in $T^2$, parametrizing a bicycle $\mathcal P_i$ in $L$, define the ***framing*** $n_i$ and ***vertical winding number*** $r_i$ of $\mathcal D_i$ by $$n_i \ = \ -\ell_i-m_i \qquad\text{and}\qquad r_i \ = \ m_i$$ where $\ell_i$ and $m_i$ are the longitudinal and meridional degrees of $\mathcal P_i$.

We can now state the main result of this section.

Before proving this theorem, we illustrate how it can be used to compute the Pontryagin invariant of the characteristic map of a generic link.

As a first example, again consider the link $L$ pictured in Figure [7](#fig:icycles){reference-type="ref" reference="fig:icycles"}(a). As noted above, it has three bicyles $A$, $B$, $C$, with longitudinal degrees $0,0,2$, meridional degrees $1,-1,1$, and so by definition, framings $-1,1,-3$ and vertical winding numbers $1,-1,1$.

By the bicycle theorem, the Pontryagin link for the characteristic map $h_L$ has toral diagram as shown in Figure [7](#fig:icycles){reference-type="ref" reference="fig:icycles"}(b) with vertical winding numbers $1$, $-1$ and $1$ on the icycles $A$, $B$ and $C$, and with global framing $n=-1+1-3=-3$. Thus the total vertical winding number is $r = 1-1+1=1$ and from the diagram we compute the horizontal winding numbers to be $p=-1$ and $q=-2$. (These values for the winding numbers of the diagram are confirmed by the calculations $p = \mathrm{Lk}(Y,Z)=-1$, $q = \mathrm{Lk}(X,Z)=-2$ and $r = \mathrm{Lk}(X,Y)=1$.) Thus the invariant $\nu(h_L)$ is well defined modulo $2 = 2\gcd(-1,-2,1)$.

Using a base point in the lower right corner of the diagram, and straight line paths from the icycles to the base point, the depths of the icycles $A$, $B$ and $C$ are $1$, $-1$ and $-1$. Thus by Proposition [\[prop:pontryagin\]](#prop:pontryagin){reference-type="ref" reference="prop:pontryagin"} we conclude that $$\nu(h_L) \ = \ n+pq + \textstyle\sum d_ir_i \ = \ -3+2+1  \ = \ 0 \ \in \ \mathbb Z_2.$$

Although the purpose of this example is to illustrate how the bicycle theorem is used for computations, we note that Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} (yet to be proved) yields the same result here effortlessly, since it implies that the Pontryagin invariant of the characteristic map of any three-component link in $S^3$ is even. Therefore, when the pairwise linking numbers $p$, $q$ and $r$ are relatively prime, as they are in this case, the computation is modulo $2\gcd(p, q, r)  =  2$, and so the Pontryagin invariant is zero.

For our next example we analyze the effect on $\nu(h_L)$ of changing two crossings of opposite signs between the first two components of a generic link $L=X\cup Y\cup Z$. This will be a key step in our inductive proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}.

To this end, choose a positive and a negative crossing between $X$ and $Y$ in a suitable projection of $L$, and let $(x_+,y_+)$ and $(x_-,y_-)$ be the corresponding page vectors. Changing both of the crossings yields a new link $\widehat{L}$, with the same pairwise linking numbers as $L$. This is illustrated in Figure [8](#fig:dblbor){reference-type="ref" reference="fig:dblbor"} where $L$ is the Borromean rings, shown on the left, and $\widehat{L}$ is the unlink, shown on the right.

<figure id="fig:dblbor">
<p><embed src="FigDblBor.pdf" style="height:1.875in" /> (-348,97)<span><span class="math inline"><em>X</em></span></span> (-335,17)<span><span class="math inline"><em>Y</em></span></span> (-325,125)<span><span class="math inline"><em>Z</em></span></span> (-360,-15)<span>(a) the Borromean rings <span class="math inline"><em>L</em></span></span> (-45,97)<span><span class="math inline"><em>X̂</em></span></span> (-60,17)<span><span class="math inline"><em>Ŷ</em></span></span> (-88,125)<span><span class="math inline"><em>Ẑ</em></span></span> (-115,-15)<span>(b) the unlink <span class="math inline"><em>L̂</em></span></span></p>
<figcaption>A double crossing change</figcaption>
</figure>

We then say that $\widehat{L}$ is obtained from $L$ by a ***double crossing change***, and propose to use the bicycle theorem to compute the resulting change $$\Delta\nu \ = \  \nu(h_{\widehat{L}}) - \nu(h_{L})$$ in Pontryagin invariants.

As it turns out, there is a simple formula for $\Delta\nu$ involving the link $L_0$ obtained from $L$ by "smoothing\" both crossings in the usual way: .1pt $$\includegraphics[height=20pt]{FigSmoothCrossing.pdf}$$ .1pt The smoothed link $L_0$ has three components, $P$ and $Q$ (replacing $X$ and $Y$) and $Z$. The component $P$ goes from $+$ to $-$ along $Y$, and then back from $-$ to $+$ along $X$, where we retain the $+$ and $-$ labels after smoothing, while $Q$ goes from $+$ to $-$ along $X$, and then back from $-$ to $+$ along $Y$. This is illustrated in Figure [9](#fig:smooth){reference-type="ref" reference="fig:smooth"} for the double crossing change shown in Figure [8](#fig:dblbor){reference-type="ref" reference="fig:dblbor"}, where we use $X_{+-}$ to denote the arc on $X$ from $+$ to $-$ , and so forth.

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

The depth $d_-$ of the component $\mathcal D_-$ of $\mathcal D$ counts the intersections of $\gamma_-$ with $\mathcal D$, which means that it counts the times that $(x(s),y(t_-))$ is a page vector for $s_-\le s\le s_+$, assuming parametrizations set up so that $s_-<s_+$ . Since $y(t_-)$ already lies in the page $H_-$, this means we are counting the times that $x(s)$ also lies in $H_-$ for $s_-\le s\le s_+$ . In other words we are counting the intersection number $X_{-+}\,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}H_-$ . Examining Figure [5](#fig:local){reference-type="ref" reference="fig:local"}, we find that the signs of the intersection points of $\gamma_-$ with $\mathcal D$ *agree* with the signs of the corresponding intersection points of $X_{-+}$ with $H_-$, and hence $$d_- \ = \ 2\, X_{-+} \raisebox{-.3ex}{\huge$\cdot$}H_- \mod{2\gcd(p,q,r)}.$$

In a similar fashion, we find that intersections of $\gamma_+$ with $\mathcal D$ correspond to intersections of $Y_{+-}$ with $H_+$, but in this case, the signs of corresponding points of intersection are *opposites*, and so the depth of $\mathcal D_+$ is $$d_+ \ = \ -2\,Y_{+-} \raisebox{-.3ex}{\huge$\cdot$}H_+\mod{2\gcd(p,q,r)}.$$

Therefore the assertion that $d_- - d_+ = 2\mathrm{Lk}(P,Z)$, which will complete the proof of the corollary, reduces to the identity $$X_{-+} \raisebox{-.3ex}{\huge$\cdot$}H_-  +  Y_{+-} \raisebox{-.3ex}{\huge$\cdot$}H_+ \ = \ \mathrm{Lk}(P,Z)\,.$$ But this follows easily from the fact that $P = X_{-+} \cup Y_{+-}$. Figure [10](#fig:linking){reference-type="ref" reference="fig:linking"} helps us to see this. In the figure, the arc $X_{-+}$ winds around the vertical $Z$ axis $k$ times and the arc $Y_{+-}$ winds around it $\ell$ times, while the entire loop $P = X_{-+} \cup Y_{+-}$ winds around it $k+\ell+1$ times. By our half-counting convention, we have $$X_{-+} \,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}H_- \ = \ 1/2 + k \qquad\text{and}\qquad Y_{+-} \,\raisebox{-.6ex}{\huge$\hskip-.02in\cdot$\hskip.005in}H_+ \ = \ 1/2 + \ell$$ and the result follows. ◻
:::

<figure id="fig:linking">
<p><embed src="FigLinking.pdf" style="height:2.63889in" /> (-132,10)<span><span class="math inline"><em>H</em><sub>−</sub></span></span> (-18,12)<span><span class="math inline"><em>H</em><sub>+</sub></span></span> (-57,27)<span><span class="math inline"><em>X</em><sub>−+</sub></span></span> (-96,155)<span><span class="math inline"><em>Y</em><sub>+−</sub></span></span> (-82,180)<span><span class="math inline"><em>Z</em></span></span> (-126,50)<span><span class="math inline"><em>k</em></span></span> (-17,135)<span><span class="math inline">ℓ</span></span> (-121,86)<span><span class="math inline">−</span></span> (-19,90)<span><span class="math inline">+</span></span></p>
<figcaption>The linking of <span class="math inline"><em>P</em> = <em>X</em><sub>−+</sub> ∪ <em>Y</em><sub>+−</sub></span> and <span class="math inline"><em>Z</em></span></figcaption>
</figure>

For the inductive step of the proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} in the next section, we will need to apply this formula for $\Delta\nu$ under the double crossing change $L\to\widehat{L}$ shown in Figure [11](#fig:double){reference-type="ref" reference="fig:double"} (which will be seen to be equivalent to a delta move). It is understood that $L$ and $\widehat{L}$ should coincide outside the picture, where in fact they can be arbitrary. Indeed, if not generic outside the ball, they can be adjusted by a link homotopy to become so, and then the methods described above apply. Since the component $Q$ of the smoothed link $L_0$ is just a meridian of $Z$ with $\mathrm{Lk}(Q,Z) = -1$, it follows that $\Delta\nu = 2$.

Thus we have proved the following: []{#double label="double"}

<figure id="fig:double">
<p><embed src="FigDouble.pdf" style="height:1.38889in" /> (-315,14)<span><span class="math inline"><em>X</em></span></span> (-203,73)<span><span class="math inline"><em>Y</em></span></span> (-267,90)<span><span class="math inline"><em>Z</em></span></span> (-300,37)<span><span class="math inline">+</span></span> (-218,37)<span><span class="math inline">−</span></span> (-100,37)<span><span class="math inline">−</span></span> (-18,37)<span><span class="math inline">+</span></span> (-285,-15)<span>(a) the link <span class="math inline"><em>L</em></span></span> (-90,-15)<span>(b) the link <span class="math inline"><em>L̂</em></span></span></p>
<figcaption>A simple double crossing change</figcaption>
</figure>

::: corollary
[]{#cor:double label="cor:double"} **If two links $L$ and $\widehat{L}$ coincide outside a $3$-ball, and appear in the ball as shown in Figure [11](#fig:double){reference-type="ref" reference="fig:double"}, then $\nu(h_{\widehat{L}}) = \nu(h_L) + 2$.**
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

We are guided by Figure [12](#fig:regular){reference-type="ref" reference="fig:regular"}, depicting a neighborhood of the vertical vector $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}$ from $x_z$ to $y_z$ in $\mathbb R^3$, lying on the page $P$. In this figure, $X_z$ and $Y_z$ denote the images of $X$ and $Y$ under the $z$-action, one or both of which must be transverse to $P$ since $L$ is generic. We arbitrarily depict $X_z$ tangent to $P$ and $Y_z$ transverse to it.

<figure id="fig:regular">
<p><embed src="FigRegular.pdf" style="height:2.36111in" /> (-114,105)<span><span class="math inline"><em>y</em><sub><em>z</em></sub></span></span> (-113,66)<span><span class="math inline"><em>x</em><sub><em>z</em></sub></span></span> (-113,83)<span><span class="math inline">$\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}$</span></span> (-21,116)<span><span class="math inline"><em>Y</em><sub><em>z</em></sub></span></span> (-17,84)<span><span class="math inline"><em>X</em><sub><em>z</em></sub></span></span> (-100,120)<span><span class="math inline">∂<sub><em>u</em></sub><em>h</em><sub><em>L</em></sub></span></span> (-85,92)<span><span class="math inline">∂<sub><em>t</em></sub><em>h</em><sub><em>L</em></sub></span></span> (-120,29)<span><span class="math inline"><em>P</em></span></span> (-95,5)<span>TURN</span> (-56,158)<span>S</span> (-56.5,150)<span>P</span> (-55.5,142)<span>I</span> (-57,134)<span>N</span></p>
<figcaption><span class="math inline"><em>k</em></span> is regular</figcaption>
</figure>

The hollow arrows in the figure indicate the left-handed screw motion of the $K$-action. In particular, as the $u$ parameter increases along $K$, this action (the stereographic image of right multiplication by $-\bar z$) turns the pages in the indicated direction while spinning them in a left-handed fashion about their centers.

As the $t$ parameter along $Y$ increases, the tip of $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}$ moves to the right along $Y_z$, so that $\partial_t h_L$ also points to the right, transverse to $P$. For clarity, we draw this partial derivative vector at the tip of $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}$, even though it is really tangent to $S^2$ at its north pole $k$.

As the $u$ parameter along $Z$ increases, two things happen which affect $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}$. The page containing it turns around the binding, but such an action keeps $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf v}}$ vertical, so has no infinitesimal effect. In addition, the page spins around its center, shifting the binding in a downward direction. Thus by the twist lemma, the vector $\partial_u h_L$ is nonzero and tangent to the page, pointing toward the binding when placed with its initial point at $y_z$.

It follows that $\partial_t h_L$ and $\partial_u h_L$ are linearly independent, confirming that $(s,t,u)$ is a regular point of the map $h_L$. Since $(s,t,u)$ was chosen arbitrarily in $h_L^{-1}(k)$, we see that $k$ is a regular value of $h_L$, proving part (a) of the Bicycle Theorem.

Starting with a three-component link $L$ in generic position in $S^3$, we have shown above that the Pontryagin link $\mathcal L$ of its characteristic map $h_L$ is given by $$\mathcal L\ = \ h_L^{-1}(k) \ = \ \{(s,t,u)\in T^3\ | \ (s,t)\in\mathcal D\text{ and } u=u(s,t)\}\,.$$ It remains to prove that the preferred orientation, vertical winding number $r_i$ and framing $n_i$ of each isogonal curve $\mathcal D_i$, as specified in Figure [5](#fig:local){reference-type="ref" reference="fig:local"} and just before the statement of the bicycle theorem, agree with the orientation, vertical winding number and framing of the component $\mathcal L_i$ of the Pontryagin link that lies over $\mathcal D_i$.

To see that the orientations agree, choose a regular page vector $(x,y)$ parametrized by an isogonal point $(s,t)$ in $\mathcal D_i$, and consider the orientation of $Y$ relative to the page containing $x$ and $y$, as recorded by the sign of $y$.

Figure [13](#fig:orientation){reference-type="ref" reference="fig:orientation"} shows the associated vertical vector $(x_z,y_z)$ in $3$-space for the case when $\textup{sign}(y) = +1$, causing the displaced link component $Y_z$ to point to the *right*. Arguing as above (see Figure [12](#fig:regular){reference-type="ref" reference="fig:regular"}) we see that $\partial_t h_L$ also points to the right, while $\partial_u h_L$ points toward the binding as always. Thus $\partial_t h_L$ and $\partial_u h_L$ form a positive basis for the tangent plane to $S^2$ at $k$. Since $\partial_s$, $\partial_t$ and $\partial_u$ form a positive basis for the tangent space to $T^3$ at each of its points, it follows that the link component $\mathcal L_i$ must be oriented in the direction of *increasing* $s$ near the associated point $(s,t,u)$ in the $3$-torus, and this agrees with the orientation assigned to $\mathcal D_i$ in Figure [5](#fig:local){reference-type="ref" reference="fig:local"}.

<figure id="fig:orientation">
<p><embed src="FigOrientation.pdf" style="height:2.36111in" /> (-100,100)<span><span class="math inline"><em>y</em><sub><em>z</em></sub></span></span> (-100,48)<span><span class="math inline"><em>x</em><sub><em>z</em></sub></span></span> (-19,110)<span><span class="math inline"><em>Y</em><sub><em>z</em></sub></span></span> (-17,50)<span><span class="math inline"><em>X</em><sub><em>z</em></sub></span></span> (-81,113)<span><span class="math inline">∂<sub><em>u</em></sub><em>h</em><sub><em>L</em></sub></span></span> (-66,79)<span><span class="math inline">∂<sub><em>t</em></sub><em>h</em><sub><em>L</em></sub></span></span></p>
<figcaption>Orientation of the Pontryagin link</figcaption>
</figure>

Similarly, if $\textup{sign}(y)=-1$ then $\mathcal L_i$ points in the direction of *decreasing* $s$ near $(s,t,u)$. Referring again to Figure [5](#fig:local){reference-type="ref" reference="fig:local"}, it is evident that this agrees with the preferred orientation on $\mathcal D_i$.

Next consider the vertical winding number $r_i$ of $\mathcal D_i$. By definition $r_i$ is equal to the meridional degree $m_i$ of the associated bicycle $\mathcal P_i$, that is, the number of times that the page vectors spin in the pages of the open book as the bicycle is traversed. By the twist lemma, this is equal to the number of times that $z$ spins around $K$, or equivalently that $u = u(s,t)$ spins around the circle as $(s,t)$ traverses $\mathcal D_i$, which is the vertical winding number of $\mathcal L_i$.

Finally consider the framing $n_i$ of $\mathcal D_i$. By definition $n_i = -\ell_i-m_i$, where $\ell_i$ and $m_i$ are the longitudinal and meridional degrees of the associated bicycle $\mathcal P_i$. This integer specifies a normal vector field $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf n}}$ to $\mathcal L_i$ by adding $n_i$ full twists (positive or negative according to the sign of $n_i$) to the lift $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf z}}$ of a normal vector field to $\mathcal D_i$ in $T^2$, the "zero\" or "blackboard\" framing.

We must show that the vector field $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf n}}$ coincides with the Pontryagin framing of $\mathcal L_i$. In other words, the differential of $h_L$ carries it onto a homotopically trivial loop of nonzero tangent vectors to $S^2$ at $k$. To see this, first note that $\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf z}}$ is homotopic to the vertical vector field $\partial_u$, remaining nonzero and transverse to $\mathcal L_i$ during the homotopy. Now since $\partial_u h_L$ is always tangent to the page containing $x_z$ and $y_z$, as shown above, it is clear that each longitudinal circuit of the bicycle $\mathcal P_i$ causes $dh_L(\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf z}})$ to spin once in the same direction about the binding. By the twist lemma, each meridional spin of the bicycle also causes $dh_L(\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf z}})$ to spin once about the binding. Thus $dh_L(\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf z}})$ spins $\ell_i+m_i$ times as the bicycle is traversed. Adding $n_i= -\ell_i-m_i$ full twists to the framing negates this spinning, and so $dh_L(\overset{\scriptstyle{}_\rightharpoonup}{\textup{\bf n}})$ does not spin at all, up to isotopy, as asserted.

This completes the proof of the bicycle theorem.

# Proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} {#sec:A}

Let $L$ be a three-component link in the $3$-sphere with characteristic map $g_L:T^3\to S^2$. Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} asserts that the degrees of $g_L$ on the coordinate $2$-tori of $T^3$ are equal to the pairwise linking numbers $p$, $q$ and $r$ of the components of $L$, and that Pontryagin's absolute $\nu$-invariant of $g_L$ is equal to twice Milnor's triple linking number $\mu(L)$ mod $2\gcd(p,q,r)$.

The first statement was proved easily at the end of Section [\[sec:characteristic\]](#sec:characteristic){reference-type="ref" reference="sec:characteristic"}. We now prove the second statement by an inductive argument, relying heavily on the techniques and results of the last section. Throughout, we will use the asymmetric characteristic map $h_L:T^3\to S^2$ in place of $g_L$, since these two maps are homotopic.

In Example [\[ex:Lpqr\]](#ex:Lpqr){reference-type="ref" reference="ex:Lpqr"} we introduced the "base links\" $L_{pqr}$ with pairwise linking numbers $p$, $q$ and $r$ and $\mu(L_{pqr}) = 0$. See Figure [\[fig:Lpqr\]](#fig:Lpqr){reference-type="ref" reference="fig:Lpqr"}. We will show that Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} holds for these links.

To accomplish this, we must show that for each $p$, $q$ and $r$, the associated characteristic map $h_{L_{pqr}}$ is homotopic to the base map $f_{pqr}:T^3\to S^2$ used in Section [\[sec:pontryagin\]](#sec:pontryagin){reference-type="ref" reference="sec:pontryagin"} to convert the relative Pontryagin $\nu$-invariant to an absolute $\nu$-invariant. In other words, we must show that $\nu(h_{L_{pqr}}) = 0$.

First move $L_{pqr}$ by a link homotopy into generic position, and let $L=X\cup Y\cup Z$ be the resulting link. Then $Z$ coincides with the binding $K$ of the standard open book, while $X$ and $Y$ wind around $Z$ in a generic fashion, $q$ and $p$ times respectively, linking each other $r$ times along the way. In fact this winding can be made *monotonic*, to appear as shown in Figure [14](#fig:genericLpqr){reference-type="ref" reference="fig:genericLpqr"} for the case $(p,q,r)=(5,3,-2)$.

<figure id="fig:genericLpqr">
<p><embed src="FigLpqrGeneric.pdf" style="height:2.77778in" /> (-122,42)<span><span class="math inline"><em>q</em></span></span> (-122,133)<span><span class="math inline"><em>p</em></span></span> (-25,90)<span><span class="math inline"><em>r</em></span></span> (-1,20)<span><span class="math inline"><em>X</em></span></span> (3,157)<span><span class="math inline"><em>Y</em></span></span> (-65,180)<span><span class="math inline"><em>Z</em></span></span></p>
<figcaption>A generic link <span class="math inline"><em>L</em></span> representing <span class="math inline"><em>L</em><sub><em>p</em><em>q</em><em>r</em></sub></span></figcaption>
</figure>

Observe that one need not actually construct a link homotopy carrying $L_{pqr}$ to $L$, but need only check that the pairwise and triple linking numbers of $L_{pqr}$ and $L$ coincide, and then appeal to Milnor's classification. The verification that $\mu(L)=0$ is completely analogous to the calculation for $\mu(L_{pqr})$, using the obvious stacked disks, joined by half twisted bands, as Seifert surfaces for $X$ and $Y$, and a hemispherical page in the open book on $S^3$ as a Seifert surface for $Z$.

Now the bicycles in $L$ are easily identified. There are $d = \gcd(p,q)$ of them, all of longitudinal degree $\ell = \textup{lcm}(p,q)$, and all but one of meridional degree $0$, the remaining one being of degree $r$. The parametrizing icycles are all parallel to a $(p/d,q/d)$ torus knot in the $2$-torus, with vertical winding numbers all equal to zero, except one equal to $r$. By the bicycle theorem, these icyles form a diagram for the Pontryagin link of $h_L$, with global framing $-(pq+r)$. This is exactly the situation described in Example [\[ex:basecase\]](#ex:basecase){reference-type="ref" reference="ex:basecase"}, and so $$\nu(h_{L_{pqr}}) \ = \ \nu(h_L) \ = \ 0 \ \in \ \mathbb Z_{2\gcd(p,q,r)}$$ as asserted.

First recall from Example [\[ex:delta\]](#ex:delta){reference-type="ref" reference="ex:delta"} that any three-component link $L$ with pairwise linking numbers $p$, $q$ and $r$ is link homotopic to a link obtained from $L_{pqr}$ by a sequence of delta moves of the type shown in [Figure [\[fig:delta\]](#fig:delta){reference-type="ref" reference="fig:delta"}]{.upright} $($or its inverse$)$, by a result of Murakami and Nakanishi [@MurakamiNakanishi]. It was shown in that example that each such move increases $\mu(L)$ by $1$.

Now observe that such a delta move $\Delta:L\to\widehat{L}$ can be viewed as a double crossing change $\mathbb D$, of the kind shown in Figure [11](#fig:double){reference-type="ref" reference="fig:double"},

composed with an isotopy, as indicated in Figure [15](#fig:deltadouble){reference-type="ref" reference="fig:deltadouble"}. By Corollary [\[cor:double\]](#cor:double){reference-type="ref" reference="cor:double"}, this double crossing change increases $\nu(L)$ by $2$, and so $\Delta$ does the same.

<figure id="fig:deltadouble">
<p><embed src="FigDeltaDouble.pdf" style="height:2.5in" /> (-55,72)<span> isotopy</span> (-132,142)<span><span class="math inline">𝔻</span></span> (-210,68)<span><span class="math inline"><em>Δ</em></span></span> (-270,135)<span><span class="math inline"><em>L</em></span></span> (-255,107)<span><span class="math inline"><em>X</em></span></span> (-170,160)<span><span class="math inline"><em>Y</em></span></span> (12,135)<span><span class="math inline"><em>L̂</em></span></span> (-140,5)<span><span class="math inline"><em>L̂</em></span></span></p>
<figcaption>Another view of the delta move</figcaption>
</figure>

Since this argument applies to an arbitrary delta move, it follows that $\nu(L) = 2\mu(L)$ for *all* three component links $L$. This completes the proof of Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}.
