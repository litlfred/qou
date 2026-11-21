---
doc_id: arxiv-math-0108215v1
doc_title: "arXiv:math/0108215v1 [math.GT] 30 Aug 2001"
section_id: sec-001-2-the-lemmas
section_title: "The Lemmas"
section_number: 2
pages: 3-8
source_pdf: 0108215v1.pdf
source_sha256: 191784d2ccb3415a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.992
doc_brief: "arXiv:math/0108215v1 [math.GT] 30 Aug 2001 — The M¨obius energy of a knot is an energy functional for smooth curves based on an idea of self-repelling."
---
[]{#thelemmas label="thelemmas"}

The first lemma is a version of a theorem of Schur. This is taken from [@Ch], with the slight adjustment that we do not need to consider general planar convex curves as the reference curves, just circles.

::: lem
Let $K$ be a $C^2$ smooth curve in $\Rset^3$ whose curvature everywhere is $\leq$ some number $k$. Let $C$ be a circle of curvature $k$, i.e. of radius $r = {\frac1k}$. Let $x,y \in K$ and $s,t
\in C$ be any points such that $\mathrm{arc}(x,y)=\mathrm{arc}(s,t)
\leq \pi r$. Then the chord distances satisfy $$|x-y|
\geq |s-t|.$$ []{#schursthm label="schursthm"}
:::

::: pf
See Schur's Theorem in [@Ch]. 0◻
:::

We also will use results on thickness of knots developed in [@LSDR]. Let $K$ be a smooth knot in $\Rset^3$, a simple closed curve that is at least $C^2$ smooth. We assume $C^2$ smoothness throughout this paper, and the work in [@LSDR] assumed that as well; but in fact the definition and results there can be modified to deal with $C^{1,1}$ curves (this has been noted by R. Litherland, O. Durumeric, and [@maddocks; @cksminimum]).

For each $x \in K,$ let $D(x,r)$ denote the disk of radius $r$ centered at $x$ and orthogonal at $x$ to $K$. For sufficiently small $r>0$, the disks are pairwise disjoint, their union forming a tubular neighborhood of $K$. We define the *injectivity radius* of $K$, $R(K)$, to be the supremum of such good radii. The radius $R(K)$ measures the maximum thickness of "rope" that could be used to form the curve $K$. Of course, $R(K)$ changes with scale. We define the scale-invariant *ropelength* or *length energy* of $K$ to be

$$E_L(K) =\frac {\mathrm{arclength}(K)}{R(K)}\;\;.$$

The radius $R(K)$ is affected by curvature and by points of $K$ that are far apart in the sense of arclength but close in space. For the latter kinds of points, distances will be minimized at pairs of points $(x,y)$ that are critical points for the distance function $|x-y|$. Specifically, define the *critical self-distance* of $K$ to be the minimum of $|x-y|$ over all pairs $(x,y) \in K \times K$, $x\not = y$, for which the chord $x-y$ is perpendicular to $K$ at either or both of its endpoints. Let ${\mathrm{MinRad}}(K)$ denote the minimum radius of curvature of $K$. We then have from [@LSDR]:

::: lem
The thickness of a smooth knot is bounded by the minimum radius of curvature and half the critical self-distance. In fact, $$R(K)= \min \left\{ {\mathrm{MinRad}}(K)\;,\; \frac12\, 
\text{critical self distance}(K)\right\}.$$ []{#lsdr label="lsdr"}
:::

The next lemma is a consequence of Lemmas [\[schursthm\]](#schursthm){reference-type="ref" reference="schursthm"} and [\[lsdr\]](#lsdr){reference-type="ref" reference="lsdr"}.

::: lem
Suppose $K$ is a smooth knot of thickness $R(K)=r$. For any $x,y \in K$, such that $\mathrm{arc}(x,y) \geq \pi r$, we must have $|x-y| \geq
2 r$. []{#distancebound label="distancebound"}
:::

::: pf
Fix $x$ and consider first the two points $y
\in K$ for which $\mathrm{arc}(x,y) = \pi r$. Since, by Lemma [\[lsdr\]](#lsdr){reference-type="ref" reference="lsdr"}, the curvature of $K$ is everywhere $\leq 1/r$, and $\mathrm{arc}(x,y) = \pi r$, so in particular it is $\leq
\pi r$, we can apply Schur's Theorem to the arc from $x$ to such $y$ to conclude that $|x-y|$ is at least as large as for the corresponding points on a circle of radius $r$, i.e. $|x-y| \geq 2 r$.

Now consider the arc $Y$ of $K$ consisting of those points $y$ with $\mathrm{arc}(x,y) \geq \pi r$. Let $y_0$ be a point of $Y$ that minimizes distance to $x$. If $y_0$ is closer to $x$ than $2 r$ then, from the preceding paragraph, it cannot be an endpoint of $Y$; thus it would have to be a critical point for the function $|x-y|$. But by Lemma [\[lsdr\]](#lsdr){reference-type="ref" reference="lsdr"}, any such critical pair $(x,y)$ has distance $\geq 2 r$. 0◻
:::

In the next two lemmas, we obtain the linear bound for the energy contribution of proximal pairs, that is, points for which $\mathrm{arc}(x,y)\leq \pi R(K)$.

::: lem
For a fixed point $s$ on a circle $C$ of radius $R$, $$\int\nolimits_{t\in C} \frac{1}{|s-t|^2} -
\frac{1}{\mathrm{arc}(s,t)^2} = \frac{2}{\pi R}\;.$$ []{#circle label="circle"}
:::

::: pf
Fix $s$ on a circle $C$ of radius $R$. Note that if $\mathrm{arc}(s,t)=\theta$, then $|s-t|^2=R^2(2- 2 \cos\theta)$. Thus, $$\begin{aligned}
\int\nolimits_{t\in C} \frac{1}{|s-t|^2} -
\frac{1}{\mathrm{arc}(s,t)^2} &= 
2\int\nolimits_0^{\pi
R}\frac{1}{R^2(2-2\cos(t/R))}-\frac{1}{t^2}\,\d t \\ 
&= \frac{2}{\pi R}\;.
\end{aligned}$$ 0◻
:::

::: lem
If $K$ is a smooth knot in $\Rset^3$, then $$\int\nolimits_{x\in
K}\int\nolimits_{\mathrm{arc}(x,y)\leq \pi R(K)} 
\frac{1}{|x-y|^2} - \frac{1}{\mathrm{arc}(x,y)^2} 
\leq \frac{2}{\pi}\,E_L(K)\;.$$ []{#prox label="prox"}
:::

::: pf
We begin by rescaling $K$ to have $R(K)=1$; note this leaves each side of the inequality unchanged. Then $E_L(K)$ is just the new total arclength of $K$, which we abbreviate $L$. By Lemma [\[lsdr\]](#lsdr){reference-type="ref" reference="lsdr"}, the curvature of $K$ everywhere is $\leq \frac{1}{R(K)}=1$. For points $x,y$ on $K$ with $\mathrm{arc}(x,y) \leq \pi$, let $s,t$ be points on the circle, $C$, of radius $1=R(K)$, for which $\mathrm{arc}(s,t) = \mathrm{arc}(x,y)$. By Schur's Theorem (Lemma [\[schursthm\]](#schursthm){reference-type="ref" reference="schursthm"}), we have $|x-y| \geq |s-t|$, so $$\frac{1}{|x-y|^2}-\frac{1}{\mathrm{arc}(x,y)^2} \leq 
\frac{1}{|s-t|^2}-\frac{1}{\mathrm{arc}(x,y)^2} = 
\frac{1}{|s-t|^2}-\frac{1}{\mathrm{arc}(s,t)^2}\;.
\label{arccircles}$$ For a fixed $x$ on $K$ and a fixed $s$ on $C$, ([\[arccircles\]](#arccircles){reference-type="ref" reference="arccircles"}) and Lemma [\[circle\]](#circle){reference-type="ref" reference="circle"} give us $$\begin{aligned}
\int\nolimits_{\mathrm{arc}(x,y)\leq \pi} 
\frac{1}{|x-y|^2} - \frac{1}{\mathrm{arc}(x,y)^2} &\leq
\int\nolimits_{\mathrm{arc}(s,t)\leq \pi}
\frac{1}{|s-t|^2}-\frac{1}{\mathrm{arc}(s,t)^2} \\ 
&= \frac{2}{\pi}\,.
\end{aligned}$$ Thus, $$\int\nolimits_{x\in
K}\int\nolimits_{\mathrm{arc}(x,y)\leq \pi} 
\frac{1}{|x-y|^2} - \frac{1}{\mathrm{arc}(x,y)^2} \leq
\int\nolimits_{x\in K} \frac{2}{\pi} = \frac{2}{\pi}\,L\;.$$ 0◻
:::

Finally, we need a lemma about measurable subsets of $K$. When we talk about "measure", we mean the one-dimensional Lebesgue measure on $K$ that is just arclength when applied to intervals. We actually use only Borel sets.

We want to define subsets of $K$ of specified measure that are closest, in terms of spatial distance, to a given point $x\in K$. First we need a preliminary lemma about decomposing measurable sets.

::: lem
[]{#DecomposeASet label="DecomposeASet"} Suppose $W$ is a measurable subset of $K$ and $m_1,m_2 > 0$ are numbers with $m_1+m_2 =
\mu(W)$. Then we can partition $W$ into measurable sets $W_1,W_2$, with $\mu(W_j)=m_j\;, j=1,2$.
:::

::: pf
Orient $K$, fix a point $z_0 \in K$, and consider the intersections of $W$ with intervals $I_z =[z_0,z]$ as $z$ ranges over $K$. Since the measure of a subset of an interval is bounded by the length of the interval, the function $\mu(W\cap I_z)$ is continuous in $z$. The measure $\mu(W\cap I_z)$ is arbitrarily small when $z \approx z_0$, is monotonically nondecreasing as $z$ moves around $K$, and eventually exceeds $m_1$ as $z$ approaches $z_0$ from the "back". Thus there must be a value of $z$ for which $\mu(W\cap I_z) = m_1$. 0◻
:::

In the next lemma, and the proof of the main theorem, we use the following notation. For $x\in K$ fixed, $a \leq b$, let $S(a,b], S[a,b], S[a]$ denote spherical shells of radius from $a$ to $b$, and the sphere of radius $a$, all centered at $x$.

::: lem
[]{#ConstructWj label="ConstructWj"} Suppose $K$ is a smooth knot with $R(K)=1$. Fix $x \in K$ and let $Y$ be the subset of $K$ consisting of all points $y$ with $\mathrm{arc}(x,y) \geq \pi$. Let $\nu_1 ,\nu_2, \dots ,\nu_m > 0$ be numbers such that $\nu_1 +\nu_2 + \dots +\nu_m =
L-2\pi$ (i.e. $\mu (Y))$. Then there exists a sequence of radii $$2 \leq \rho_1 \leq \rho_2 \leq \dots \leq \rho_m$$ and a partition of $Y$ into measurable sets $W_1 , W_2 ,\dots ,W_m$ such that

\(a\) for each $j$, $\mu(W_j) = \nu_j$, and

\(b\) $W_1\subseteq Y\cap S[2,\rho_1]$ and for each $j>1$, $W_j \subseteq Y\cap
S[\rho_{j-1},\rho_j]$.
:::

::: pf
The proof is nearly straightforward. There is a slight complication because the knot $K$ might intersect some spheres $S[\rho]$ in sets of positive length.

Since $R(K)=1$ and $y\in Y$ has $\mathrm{arc}(x,y)\geq \pi$, by Lemma [\[distancebound\]](#distancebound){reference-type="ref" reference="distancebound"}, $|x-y| \geq 2$, so $Y\subseteq S[2,L/2]$. We define the radius $\rho_m\leq L/2$ to be the smallest radius $\rho$ for which $Y$ is contained in $S[2,\rho]$.

We construct radii $\rho_j$ and sets $W_j$ inductively, with a slight variation at the final step. For the degenerate case $m=1$, of course, $W_1=Y$ and $\rho_1=\rho_m$ is as above.

We now begin the induction. Suppose first that $\mu(Y\cap S[2]) \geq \nu_1$. By Lemma [\[DecomposeASet\]](#DecomposeASet){reference-type="ref" reference="DecomposeASet"}, we can partition $Y\cap S[2]$ into sets $W_1\cup V$, where $\mu(W_1)=\nu_1$; let $\rho_1=2$.

Now suppose $\mu(Y\cap S[2])< \nu_1$. Let $$R_{\text{low}}=\{\rho\,:\,\mu(Y\cap S[2,\rho])<\nu_1\}$$ and $r_1=\sup(R_{\text{low}})$. Similarly, let $$R_{\text{high}}=\{\rho\,:\,\mu(Y\cap S[2,\rho])\geq \nu_1\}$$ and let $r_1'=\inf(R_{\text{high}})$. Here $R_{\text{low}}\not = \emptyset$ because $\mu(Y\cap S[2])< \nu_1$, so $2\in R_{\text{low}}$, and $R_{\text{high}}\not = \emptyset$ because $\rho_m\in R_{\text{high}}$.

We claim $r_1=r_1'$. Each element of $R_{\text{low}}$ is $<$ each element of $R_{\text{high}}$. Thus, $r_1\leq r_1'$. If the inequality is strict, then for each $\rho\in(r_1,r_1')$, $\mu(Y\cap S[2,\rho])\geq \nu_1$, which contradicts $\rho<r_1'$.

Now define $\rho_1=r_1=r_1'$. The set $Y\cap S[2,r_1)$ is a monotone union of sets, each with measure $<\nu_1$. Thus, $\mu(Y\cap S[2,\rho_1))\leq \nu_1$. On the other hand, $Y\cap S(r_1',\infty)$ is a monotone union of sets, each with measure $< \mu(Y)-\nu_1$. Thus, $\mu(Y\cap S(\rho_1,\infty))\leq
\mu(Y)-\nu_1$, so $\mu(Y\cap S[2,\rho_1])\geq \nu_1$.

Using Lemma [\[DecomposeASet\]](#DecomposeASet){reference-type="ref" reference="DecomposeASet"}, we extract a subset of $Y\cap S[\rho_1]$ whose measure is whatever $\mu(Y\cap S[2,\rho_1))$ may lack to make $\nu_1$, and let $W_1$ be the union of this set with $Y\cap S[2,\rho_1)$.

To continue the induction, let $Y_1=Y-W_1$. Note $Y_1\subseteq Y\cap S[\rho_1,\infty)$.

Suppose $\rho_1, \cdots, \rho_{j-1}$ and $W_1, \cdots, W_{j-1}$ have been chosen as required in the statement of the lemma and the set $Y_{j-1}=Y-(W_1\cup \cdots \cup W_{j-1})\subseteq S[\rho_{j-1},\infty)$. Note that since $W_1,\cdots, W_{j-1}\subseteq Y\cap S[2,\rho_{j-1}]$, $Y\cap S(\rho_{j-1},\infty)\subseteq Y_{j-1}$. So for any $\rho,\rho'$ with $\rho_{j-1}<\rho<\rho'$, we have $Y_{j-1}\cap S[\rho,\rho']=Y\cap S[\rho,\rho']$.

Now proceed much like the initial case. If $j=m$, we finish by taking $W_j=Y_{j-1}$ and $\rho_m$ as above.

There are two cases: If $\mu(Y_{j-1}\cap S[\rho_{j-1}])\geq \nu_j$, then let $W_j$ be a subset of $Y_{j-1}\cap S[\rho_{j-1}]$ of measure $\nu_j$, $\rho_j=\rho_{j-1}$, and $Y_j=Y_{j-1}-W_j$.

Suppose now $\mu(Y_{j-1}\cap S[\rho_{j-1}])<\nu_j$. Define $$R_{\text{low}}=\{\rho\,:\,\mu(Y_{j-1}\cap S[\rho_{j-1},\rho])<\nu_j\}$$ and $r_j=\sup(R_{\text{low}})$. Similarly, let $$R_{\text{high}}=\{\rho\,:\,\mu(Y_{j-1}\cap S[\rho_{j-1},\rho])\geq \nu_j\}$$ and let $r_j'=\inf(R_{\text{high}})$. Here $R_{\text{low}}\not = \emptyset$ because $\rho_{j-1}\in R_{\text{low}}$ and $R_{\text{high}}\not = \emptyset$ because $\rho_m\in R_{\text{high}}$.

As in the initial case, we have $r_j=r_j'$, and we define $\rho_j=r_j=r_j'$. Also, $\mu(Y_{j-1}\cap S[\rho_{j-1},\rho_j))\leq \nu_j$ and $\mu(Y_{j-1}\cap S[\rho_{j-1},\rho_j]) \geq \nu_j$.

Let $W_j$ be the union of $Y_{j-1}\cap S[\rho_{j-1},\rho_j)$ with a subset of $Y_{j-1}\cap S[\rho_j]$ of however much additional measure is needed to reach $\nu_j$. Finally, let $Y_j=Y_{j-1}-W_j$. Note then $Y_j\subseteq
Y\cap S[\rho_j,\infty)$. 0◻
:::
