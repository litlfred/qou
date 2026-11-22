---
doc_id: arxiv-1707.06608v1
doc_title: "Fractional Hopﬁons in the Faddeev-Skyrme model with a symmetry breaking potential"
section_id: sec-002-3-initial-approximation
section_title: "Initial approximation"
section_number: 3
pages: 5-6
source_pdf: 1707.06608v1.pdf
source_sha256: 7b7db6dce87dc81e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.996
doc_brief: "Fractional Hopﬁons in the Faddeev-Skyrme model with a symmetry breaking potential — We construct new solutions of the Faddeev-Skyrme model with a symmetry breaking potential admitting S1 vacuum."
---
The peculiarity of the Faddeev-Skyrme model is that the Hopf index is not a winding number, the boundary conditions are identical for configurations in all topological sectors. As usual, the energy minimization scheme needs an appropriate initial configuration in a given sector. The most effective approach here is related with the generalization of the rational map approximation, suggested by Sutcliffe [@Sutcliffe:2007ui]. This construction can be nicely described in terms of a degree one map $\mathbb{R}^3 \mapsto S^3 \in \mathbb{C}^2$. One can consider the complex variables which parameterize the sphere $S^3$ [@Sutcliffe:2007ui] $$\left(Z_1,Z_0 \right) = \left(\sin f(r) \sin \theta e^{i\varphi};~~ \cos f(r) + i \sin f(r) \cos \theta \right)
\label{rational-Hopf}$$ where $f(r)$ is a monotonically decreasing function with the boundary values $f(0)=\pi$ and $f(\infty)=0$. Clearly, the coordinates $Z_1,Z_0$ are restricted to the unit sphere $S^3$, $|Z_1|^2 + |Z_2|^2=1$. Then a torus knot on the domain space can be described as the intersection of a curve $Q(Z_1,Z_0)$ with a unit sphere $S^3$.

Then the components of the field $\vec\phi$, which are coordinates on the Riemann sphere $S^2$, are given by the rational map $W: S^3 \in \mathbb{C}^2 \mapsto CP^1$: $$W(Z_1,Z_0) = \frac{\phi_1+i\phi_2}{1+\phi_3} = \frac{P(Z_1,Z_0)}{Q(Z_1,Z_0)} \, .
\label{rational-Hopf-2}$$ Here the polynomials $P(Z_1,Z_0)$ and $Q(Z_1,Z_0)$ have no common factors and have no common roots on the two-sphere $S^2$. Thus, the rational map ansatz ([\[rational-Hopf-2\]](#rational-Hopf-2){reference-type="ref" reference="rational-Hopf-2"}) produces a curve in $\mathbb{R}^3$ and the map $\phi: \mathbb{R}^3 \mapsto S^2$ is equivalent to the map from a three-sphere to the complex projective line, $W:S^3 \mapsto CP^1$.

According to the classification of [@Sutcliffe:2007ui], there are three different types of input configurations. The axially symmetric Hopfions are produced by the rational map $$W(Z_1,Z_0) =\frac{Z_1^n}{Z_0^m} \, ,
\label{map-unknot}$$ in this case the position curve, which is defined as solution of the equation $Z_0=0$, is just a circle in the $x$-$y$ plane centered at the origin. This Hopfion is constructed via embedding of a two-dimensional charge $n$ planar Skyrmion configuration as a slice of a circle in three-dimensional space. Since the baby Skyrmions possess an internal phase, the configuration can be twisted by the angle $2\pi m$ as it travels along the circle. Thus, the total topological charge of the three dimensional configuration is given by the product of the winding number in the plane and the number of twists: $Q=mn$. Following [@Sutcliffe:2007ui], we can label the axially symmetric Hopfions of that type as $Q \mathcal{A}_{mn}$, here the first subscript gives the number of twists and the second is the winding number of the two-dimensional planar solitons. In terms of the mathematical knot theory the axially symmetric Hopfions are trivial knots, so called unknots. They are closed field configurations with two independent winding numbers along two fundamental circles of the torus.

Note that numerical simulations reveal that in general configurations of higher degree do not possess the axial symmetry, since increase of number of twists per unit resolution may break the axial symmetry making the position curve not planar. This happened, for example, for the charge three Hopfion, the energy minimization transforms the corresponding axially symmetric initial configuration $\mathcal{A}_{31}$ into the pretzel-like loop, bending toward the third direction. It was suggested to label configurations of that type as $\widetilde{\mathcal{A}}_{31}$ to emphasize the deformation [@Sutcliffe:2007ui].

As the value of the Hopf invariant increases, some new possibilities arise. First, we can construct the Hopfions with two or more interlinked and disconnected position curves. These configurations are referred to as links. The Hopf charge of this configuration is not just a simple sum of the Hopf indexes associated with each individual unknot, it also includes in addition the sum of their secondary linking numbers due to the inter-linking with the other components. Configurations of that type are labeled as $\mathcal{L}_{a,b}^{n,m}$, here the subscripts label the Hopf indexes of the unknots and the superscript above each subscript counts the secondary linking number, which appears due to inter-linking with the other components. The total charge of the Hopfion of that type is just the sum of all four indices [@Sutcliffe:2007ui].

Rational map approximation ([\[rational-Hopf-2\]](#rational-Hopf-2){reference-type="ref" reference="rational-Hopf-2"}) can be used to produce various links in a given topological sector. Now the denominator of the map must be reducible to give rise to the linked position curves. For example, the link of the type $\mathcal{L}_{n,n}^{1,1}$ is generated by the map $$W=\frac{Z_1^{n+1}}{Z_1^2-Z_0^2} = \frac{Z_1^n}{2(Z_1-Z_0)}+\frac{Z_1^n}{2(Z_1+Z_0)} \, .
\label{map-link}$$ The Hopf index of this configuration is $Q=2n+2$, it corresponds to the two $\mathcal{A}_{n1}$ unknots linked once.

In order to construct configurations of another type, the knots, Sutcliffe suggested to consider the rational map of the following form [@Sutcliffe:2007ui] $$W(Z_1,Z_0) =\frac{Z_1^\alpha Z_0^\beta}{Z_1^a+Z_0^b}
\label{rational-Hopf-3}$$ where $\alpha$ is a positive integer and $\beta$ is a non-negative integer. This Hopfion is denoted as $\mathcal{K}_{a,b}$, in order to produce a torus knot $a$ and $b$ must be co-prime[^1] and $a>b$. Thus, this configuration possesses $a(b-1)$ crossings, for example the trefoil knot $\mathcal{K}_{3,2}$ is also the $(3,2)$ torus knot. The Hopf index is given by the crossing number and the number of times the linking curve wraps around the position curve, $$Q= \alpha b + \beta a$$ The rational map ([\[rational-Hopf-3\]](#rational-Hopf-3){reference-type="ref" reference="rational-Hopf-3"}) allows to produce knotted configurations for any value of $Q$, for example simplest $Q=1$ unknot corresponds to the setting $a=2,b=1,\alpha=1$ and $\beta=0$.

[^1]: If they are not, the rational map ([\[rational-Hopf-3\]](#rational-Hopf-3){reference-type="ref" reference="rational-Hopf-3"}) is degenerated producing a link.
