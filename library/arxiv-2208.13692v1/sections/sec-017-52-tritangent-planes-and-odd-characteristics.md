---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-017-52-tritangent-planes-and-odd-characteristics
section_title: "Tritangent Planes and Odd Characteristics"
section_number: 5.2
pages: 31-32
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.946
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
[]{#subsec: tritangent planes label="subsec: tritangent planes"} Recall that when we consider the canonical embedding of a curve in $\mathbb{P}^{g-1}$, the intersection with a hyperplane gives an effective element of the canonical divisor class of the curve, as it corresponds to the zero-locus of a differential on the curve. A tritangent plane is a plane that intersects the curve tangentially in three points. If a hyperplane is tangent at each intersection (i.e. the intersection is of order 2) then this naturally constructs an effective theta divisor on the curve, and moreover every such theta characteristic $\theta$ gives a hyperplane [@Celik2019]. For any sextic that is the intersection of a smooth quadric and smooth quartic in $\mathbb{P}^3$, for example Bring's curve, the 120 tritangent planes are in 1-1 correspondence with the 120 odd theta characteristics [@Harris2017 Theorem 2.2].

On Bring's curve we have the following result about these planes.

::: prop
The 120 tritangent planes on Bring's curve split into two classes, 60 in each class;

1.  those where all three contact points are Weierstrass points, and

2.  those where only one contact points is a Weierstrass point.

Planes in the first and second class respectively have equations (recalling notation from §[\[subsec: Weierstrass points\]](#subsec: Weierstrass points){reference-type="ref" reference="subsec: Weierstrass points"}) $$\begin{aligned}
\Pi_{\alpha  jk }^{(1)} &:= \left\{ \frac{x_j}{\beta} - \frac{x_k}{\gamma} = 0  \right\}  , \\
\Pi_{ijk}^{(2)} &:= \left\{ (\alpha-1)(\alpha+4)x_i + (\beta-1)(\beta+4)x_j + (\gamma-1)(\gamma+4)x_k =0  \right\}  , 
\end{aligned}$$ where $[x_i] \in \mathbb{P}^4$ and $i,j,k$ distinct.
:::

To clarify the notation we have used for the planes, recall that the position of the indices on Weierstrass points $W_{ijk}$ indicates which root was equal to $x_i$. The same principle holds for $\Pi_{\alpha jk}^{(1)},  \Pi^{(1)}_{i \beta k},$ and $\Pi^{(1)}_{ij \gamma}$.

::: corollary
[]{#cor: Orbit decomposition of odd theta characteristics label="cor: Orbit decomposition of odd theta characteristics"} The orbit decomposition of odd theta characteristics on Bring's curve is $$\label{eq:oddcharacteristics}
120=20+20+20+60 .$$
:::

::: proof
*Proof.* The characteristics coming from the triangent planes are $$\begin{aligned}
T_{\alpha jk}^{(1)} &= \sum_{\substack{i=1 \\ i \neq j,k}}^5 W_{ijk}  , \\
T_{ijk}^{(2)} &= W_{ijk} + O_{ijk}^+ + O_{ijk}^-  . 
\end{aligned}$$ Here we define the points $O_{ijk}^\pm$ by, for example, $$O_{345}^\pm = \left [ \frac{1 \pm i\sqrt{15}}{2} : \frac{1 \mp i\sqrt{15}}{2} : \alpha^2 + \alpha + 1, \beta^2 + \beta + 1 , \gamma^2 + \gamma + 1 \right ] .$$ A simple orbit-stabiliser argument then gives the orbit decomposition as, for example, $T_{\alpha 45}^{(1)}$ is stabilised by the symmetric group $S_{\{ 1,2,3 \}}$ and $T_{345}^{(2)}$ is stabilised by $S_{\{1,2\}}$. ◻
:::

::: remark
While we were able to proceed analytically here characterising the orbits of the odd characteristics using the work of earlier authors who had identified the tritangent planes of the curve we also may obtain the orbit structure numerically using Sage. Given a homology representation of the automorphism group, the algorithm to compute the orbits is exact, but the current implementation in Sage requires floating point arithmetic to calculate this representation.
:::
