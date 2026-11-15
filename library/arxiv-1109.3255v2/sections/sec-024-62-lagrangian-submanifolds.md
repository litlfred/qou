---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-024-62-lagrangian-submanifolds
section_title: "Lagrangian submanifolds"
section_number: 6.2
pages: 61-62
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.989
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:other-lagrangian label="sec:other-lagrangian"}

As before, the construction of Lagrangian sections proceeds by taking paths in the base and a Lagrangian in the fiber, and sweeping out a Lagrangian in the total space by symplectic parallel transport. Potentially, we have more freedom than in the mirror to $\CP^2$.

The admissible Lagrangian submanifolds we consider have boundary conditions given by a complex curve in $\partial X(B)$ along each boundary face. This gives two complex curves $\Sigma_0$ and $\Sigma_1$ for the bottom and top horizontal boundary faces. At the vertical boundary faces, we have corresponding complex curves $M_0$ and $M_1$. These are fibers of the fibration $X(B)\to X(I)$, and to be admissible requires the Lagrangian to end on this fiber. If $B$ has a corner rather than a vertical boundary, then the fiber $M_i$ corresponds to a vertical boundary created by cutting off the corner, and the admissibility condition requires the Lagrangians to intersect this fiber in a prescribed real curve.

Thus, a Lagrangian submanifold may be constructed by taking a Lagrangian $L_0$ in $M_0$, and a path $\ell$ in the base joining $M_0$ to $M_1$, and taking the parallel transport. If $M_0$ corresponds to a corner, we have only one choice for $L_0$, and if $M_1$ corresponds to a corner, this imposes a constraint on $L_0$ and $\ell$. In order to obtain sections of the torus fibration, we choose $L_0$ to be a curve which is a section of the fibration by circles of constant $\xi$ on each fiber, and $\ell$ to be a section of the fibration of the base by circles of constant $\eta$. Thus when drawing $X(I)$ as an annulus, $\ell$ appears as a spiral.

As an example, consider the degree six del Pezzo surface $X_6$, which may be obtained from $\PP^1\times \PP^1$ by blowing up two points that do not lie on the same ruling line. The moment polytope of $\PP^1\times \PP^1$ is a rectangle. By doing toric blowups at opposite corners, we obtain $X_6$ with a toric boundary divisor consisting of six $(-1)$-curves, and the moment polytope is a hexagon. Alternatively, by doing almost toric blowups [@symington] on opposite sides of the hexagon, we obtain $X_6$ with an anticanonical divisor of four components with self-intersections $-1,0,-1,0$. The base affine manifold $B$ has four sides and two singularities with parallel monodromy invariant directions.

Passing over to the mirror side, we consider Lagrangians in the symplectic manifold $X(B)$. Then we can choose independently

1.  the number of times the initial Lagrangian $L_0$ winds around the fiber $M_0$,

2.  the number of times $\ell$ winds around the base between the $M_0$ and the first singularity,

3.  the number of times $\ell$ winds around the base between the two singularities, and

4.  the number of times $\ell$ winds around the base between the second singularity and $M_1$.

This gives rise to a $4$-parameter family of Lagrangians. Under mirror symmetry, all of them correspond to line bundles. We expect that $X(B)$ is a mirror to the degree $6$ del Pezzo surface $X_6$ with a $4$-component anticanonical divisor. The $4$ parameters correspond to $\Pic(X_6) \cong \Z^4$.

Though we can construct many Lagrangians this way, in order to compute Floer cohomology and identify the basis with $B(\frac{1}{d}\Z)$, we must choose a family of Lagrangians $\{L(d)\}_{d\in\Z}$ corresponding to the tensor powers of an ample line bundle. First we choose $\ell(0)$ as a reference path in the base, over which lies $L(0)$, a Lagrangian satisfying the boundary conditions. We take $\ell(1)$ to be a certain path in the base: the number of times that $\ell(1)$ must wind between the singularities and the vertical boundaries/corners is determined by $B$: it is essential that the number of turns $\ell(1)$ makes between two consecutive singularities (or between a boundary and the neighboring singularity) is the affine width of the corresponding portion of $B$. An equivalent condition is that the $\ell(1)$ winds at unit speed. If $B$ has a vertical boundary face rather than a corner, the intersection of $L(1)$ with the fiber at that boundary must be a curve that, relative to $L(0)$, makes a number of turns equal to the affine length of the corresponding vertical boundary face. Then we choose $\ell(d)$ to be a path in the base whose slope is $d$ times the slope of $\ell(1)$, relative to $\ell(0)$. We also make sure that in the fiber, the slope $L(d)$ is $d$ times the slope of $L(1)$ (relative to $L(0)$ in each fiber).
