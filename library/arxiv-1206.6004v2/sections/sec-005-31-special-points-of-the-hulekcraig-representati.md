---
doc_id: arxiv-1206.6004v2
doc_title: "Symmetry, Integrability and Geometry: Methods and Applications"
section_id: sec-005-31-special-points-of-the-hulekcraig-representati
section_title: "Special points of the Hulek–Craig representation and desingularisation"
section_number: 3.1
pages: 4-4
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.924
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
[]{#section3.1 label="section3.1"}

The points at infinity for the HC curve [\[craig\]](#craig){reference-type="eqref" reference="craig"} are given by (the real points) $[0,1,0]$ and $[1,0,0]$, but the latter is singular. In fact the singularities of the HC curve are $[1,0,0]$ and $[\zeta^k,
\zeta^{2k}, 1]$ for $k\in\{0,\dots,4\}$ so we must work out expansions nearby in order to form a properly compact curve.

First the infinite singularity: consider the structure near $[1,0,0]$, say at points $[1,y,z]$ for small $y$, $z$. The curve reduces to $$y^5 + z^5 + y^2 z^2 - yz -2y^3 z^3 = 0,$$ so in the usual Puiseux construction we suppose $z = A y^{\alpha} +
\cdots$. Equating lowest order terms we get one of

-   $A^5 y^{5\alpha} - Ay^{\alpha+1} = 0$ which implies $z =
      y^{1/4}+\cdots$, that is $z\approx y^{1/4}$ near this point,

-   $y^5 - Ay^{\alpha+1} = 0$ which implies $z = y^4 + \cdots$ or $z\approx y^{4}$.

The second of these gives a single $z$ for each $y$ near 0, the first gives four different values for $z$. Together these make up the expected five sheets and so expansions after this point are unique. Thus in the vicinity of $[1,0,0]$ solutions $[1,y,z]$ of the first equation behave as $[1, t^4, t]$ where $t$ is a local parameter for the curve. Similarly the second equation has solutions behaving as $[1,t,t^4]$ in terms of a local parameter. Thus the point $[1,0,0]$ desingularises into precisely two points on the nonsingular curve: $$\begin{gathered}
  \label{eq:inftyExp}
    [1,0,0]_1  \sim \big[1,t^4,t\big], \qquad
    [1,0,0]_2  \sim \big[1,t,t^4\big],
\end{gathered}$$ where $\sim$ here indicates behaviour of a local coordinate in the vicinity of a specified point.

For the remaining singular points we only need to investigate explicitly one and then note that the automorphism $[x,y,z] \mapsto
[\zeta x, \zeta^2 y, z]$ will tell us how the other singularities behave. So we look at $[1,1,1]$. At first sight, two of the sheets come together here. Consider $[1+\epsilon,y, 1]$ near to $[1,1,1]$. To first order $$y^5- 2y^3 + y^2 - y + 1 = 0.$$ This quintic has four distinct roots: two are complex, corresponding to nonsingular points and will play no role in future developments. There is a real negative root $\alpha\sim -1.7549$ which also corresponds to a nonsingular point and will occur later. Finally, 1 is a root, which gives us the expected singularity at $[1,1,1]$.

Expanding about this singular point, at the next order we discover $$y = 1 + \epsilon\frac{-1+\sqrt{5}}{2} + \cdots, \qquad
  y = 1 + \epsilon\frac{-1-\sqrt{5}}{2} + \cdots.$$ These are clearly distinct solutions and together with the nonsingular expansions exhaust the five possible nonsingular preimages near $x=1$, so $[1,1,1]$ once again desingularises to two distinct points.
