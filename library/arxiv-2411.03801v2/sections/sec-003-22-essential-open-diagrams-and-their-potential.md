---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-003-22-essential-open-diagrams-and-their-potential
section_title: "Essential open diagrams and their potential"
section_number: 2.2
pages: 5-7
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.954
---
[]{#sub.PD label="sub.PD"}

The domain of the Ohtsuki--Takata invariant discussed below is the set of essential open diagrams of knots. An open diagram is a planar diagram of a $(1,1)$-tangle and is said to be essential if the corresponding collapsed triangulation is essential. We postpone a detailed description of the collapsed ideal triangulation to Section [\[sec.octa\]](#sec.octa){reference-type="ref" reference="sec.octa"}. Roughly, this is a story of how to pass from a planar diagram of a knot to an ideal triangulation of its complement and use it to determine the complete hyperbolic structure of a hyperbolic knot. Like so many things in hyperbolic geometry, this method goes back to Thurston.

We here recall a potential function associated to an open diagram, introduced by Yokota [@Yokota02] and motivated by the $R$-matrix state-sum formulas for the Kashaev invariant of a knot.

In what follows, we fix an open diagram $\mathring{D}$ of a hyperbolic knot $K$ in $S^3$, that is, a planar projection of a $(1,1)$-tangle whose closure is $K$. For technical reasons, we will assume that

::: center
$(\dagger)$ starting from one endpoint of $\mathring{D}$, we overpass the first crossing, and from the other endpoint, we underpass the first crossing.
:::

Viewing $\mathring{D}$ as an embedded 4-valent graph with two univalent vertices in $\mathbbm R^2$,

-   a *segment* refers to an edge of the graph that is not adjacent to a univalent vertex,

-   a *region* refers to a connected component of the complement of the graph, and

-   a *corner* refers to a fan-shaped area around a crossing separated by segments.

We assign the constant $1$ to every segment of $\mathring{D}$ adjacent to the unbounded region. Also, starting from an endpoint of $\mathring{D}$, if we underpass (resp., overpass) the first crossing, we assign the constant $\infty$ (resp., $0$) to each segment until we encounter an overpass (resp., underpass). To each segment not assigned a constant, we assign a variable so that every segment receives either a constant or a variable. For a non-alternating diagram, consecutive segments could be assigned with $\infty$. If it is the case, for each crossing lying between such segments, we set two adjacent variables, other than $\infty$, to be equal. We do the same for consecutive segments assigned with $0$.

::: example
[]{#ex.61 label="ex.61"} An essential open diagram for the $6_1$ knot, along with an assignment of variables to its segments is shown in Figure [1](#fig.example){reference-type="ref" reference="fig.example"}.
:::

<figure id="fig.example">

<figcaption>An open diagram of the knot <span class="math inline">6<sub>1</sub></span> with 3 variables <span class="math inline"><em>x</em><sub>1</sub></span>, <span class="math inline"><em>x</em><sub>2</sub></span>, <span class="math inline"><em>x</em><sub>3</sub></span> and 8 essential corners marked in red.</figcaption>
</figure>

We now define the potential function $V$ of $\mathring{D}$, following Yokota. We associate a dilogarithm function with each corner as in Figure [2](#fig.crossing){reference-type="ref" reference="fig.crossing"}. Such dilogarithms could be ill-defined or constant. This happens precisely when either $x$ or $y$ in Figure [2](#fig.crossing){reference-type="ref" reference="fig.crossing"} is $0$ or $\infty$, or when both $x$ and $y$ are $1$. We say that a corner is *essential* if it is not the case, i.e. if the associated dilogarithm is well-defined and non-constant. The *Yokota potential function* $V$ is defined as the sum of those dilogarithms over all essential corners.

<figure id="fig.crossing">

<figcaption>Dilogarithm functions associated with corners.</figcaption>
</figure>

We now discuss a key point, namely an isomorphism of the critical points of the potential function $V$ with the solutions to the gluing and completeness equations of the collapsed triangulation $\mathcal T_{\mathring{D}}$; see [@MY2018 Thm.4.1]. Here a critical point of $V$ means a point $x=(x_1,\ldots,x_n) \in \mathbbm C^n$ satisfying $$\label{eqn.crit}
\exp  \left ( x_i \, \dfrac{\partial V}{\partial x_i} \right) = 1,
\qquad i=1,\dots, n\,.$$ Under this isomorphism, the essential corners of $\mathring{D}$ are in bijection with the tetrahedra of $\mathcal T_{\mathring{D}}$, and the the variables of the Yokota potential function are related to the shapes of the tetrahedra of $\mathcal T_{\mathring{D}}$ according to Figure [3](#fig.crossing2){reference-type="ref" reference="fig.crossing2"}. In particular, if $\mathring{D}$ is essential, there is a geometric solution $x^\circ=(x^\circ_1,\ldots,x^\circ_n)$ to Equation [\[eqn.crit\]](#eqn.crit){reference-type="eqref" reference="eqn.crit"} which gives rise to the complete hyperbolic structure of $\mathcal T_{\mathring{D}}$.

<figure id="fig.crossing2">

<figcaption>An ideal tetrahedron at an essential corner.</figcaption>
</figure>

**Example [\[ex.61\]](#ex.61){reference-type="ref" reference="ex.61"} continued.** The diagram in Figure [1](#fig.example){reference-type="ref" reference="fig.example"} has 8 essential corners marked by red and the Yokota potential function is given by $$\begin{aligned}
V & =  \   \mathrm{Li}_2\left( x_1 \right) -\mathrm{Li}_2\left(\dfrac{1}{x_1} \right) + 
\mathrm{Li}_2\left(\dfrac{x_2}{x_1} \right) - \mathrm{Li}_2\left( x_2 \right) \\
& \qquad -  \mathrm{Li}_2\left(\dfrac{1}{x_2} \right) +  \mathrm{Li}_2\left(\dfrac{x_3}{x_2} \right) - 
\mathrm{Li}_2\left(x_3 \right) - \mathrm{Li}_2\left(\dfrac{1}{x_3} \right) \, .
\end{aligned}$$ The critical point equations [\[eqn.crit\]](#eqn.crit){reference-type="eqref" reference="eqn.crit"} are given by $$\frac{-x_1+x_2}{(-1+x_1)^2} =1, \, \frac{x_1(x_2-x_3)}{-x_1 + x_2} =1, \,
\frac{x_2 x_3}{-x_2 + x_3} =1 \,,$$

and equivalently, in the form $$2 - 5 x_1 + 6 x_1^2 - 3 x_1^3 + x_1^4 =0, \qquad x_2 = 1 - x_1 + x_1^2, \qquad
x_3 = \frac{1}{2}(1 + 2 x_1 - x_1^2 + x_1^3)$$ and the geometric solution is approximately $$\label{61xapp}
x^\circ \approx \,\, (0.895123 -1.552491 i , \, -1.504108 - 1.226851 i, \, 
-0.677958 -0.157779i) \, .$$
