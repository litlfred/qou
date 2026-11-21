---
doc_id: arxiv-1206.6004v2
doc_title: "Symmetry, Integrability and Geometry: Methods and Applications"
section_id: sec-009-41-introduction-to-h
section_title: "Introduction to H"
section_number: 4.1
pages: 6-7
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.94
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
[]{#section4.1 label="section4.1"}

Riera and Rodrı́guez, in [@riera], give Bring's curve as a quotient, $H$, of the hyperbolic disc. They then proceed to calculate a period matrix taking account of the symmetries of the curve.

The essential features of the model can be seen in Fig. [1](#fig:bringHyperbolic){reference-type="ref" reference="fig:bringHyperbolic"}. The surface is seen to be a 20-gon with edges identified as shown in the table below the figure. (We refer, for example, to the identified edges $2$ and $9$ as $2/9$.) This leads to the polygon's vertices falling into three equivalence classes, also annotated in the figure. Naturally, this surface has genus 4.

<figure id="fig:bringHyperbolic">
<img src="hyperbolic" />
<table>
<thead>
<tr class="header">
<th colspan="10" style="text-align: center;">Edge identifications</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">1</td>
<td style="text-align: left;"><span class="math inline">↔︎</span> 14</td>
<td style="text-align: right;">5</td>
<td style="text-align: left;"><span class="math inline">↔︎</span> 18</td>
<td style="text-align: right;">9</td>
<td style="text-align: left;"><span class="math inline">↔︎</span> 2</td>
<td style="text-align: right;">13</td>
<td style="text-align: left;"><span class="math inline">↔︎</span> 6</td>
<td style="text-align: right;">17</td>
<td style="text-align: left;"><span class="math inline">↔︎</span> 10</td>
</tr>
<tr class="even">
<td style="text-align: right;">3</td>
<td style="text-align: left;"><span class="math inline">↔︎</span> 12</td>
<td style="text-align: right;">7</td>
<td style="text-align: left;"><span class="math inline">↔︎</span> 16</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;"><span class="math inline">↔︎</span> 20</td>
<td style="text-align: right;">15</td>
<td style="text-align: left;"><span class="math inline">↔︎</span> 4</td>
<td style="text-align: right;">19</td>
<td style="text-align: left;"><span class="math inline">↔︎</span> 8</td>
</tr>
</tbody>
</table>
<figcaption>Riera and Rodr<span>ı́</span>guez hyperbolic model, <span class="math inline"><em>H</em></span>, of Bring’s curve.</figcaption>
</figure>

For future calculations it will also be very useful to know the conformal structure (or equivalently, the local holomorphic coordinate) about the points $P_1$, $P_2$ and $P_3$. This can be reconstructed quite easily from Fig. [1](#fig:bringHyperbolic){reference-type="ref" reference="fig:bringHyperbolic"}. For example, start near $P_1$ in the bottom right quadrant on edge $2/9$. Make a small arc around $P_1$ proceeding anticlockwise and you will next reach edge $1/14$. Repeating at edge 14 tells us that we next meet $6/13$. If this procedure is continued we obtain Fig. [2](#fig:ptreconst){reference-type="ref" reference="fig:ptreconst"}.

![Conformal structure of $P_1$, $P_2$ and $P_3$.](vertices){#fig:ptreconst}

The polygon can be tiled by 120 double triangles (one can take a sector of the central pentagon as a fundamental domain). Now consider the automorphism group. Let $d$ be a rotation of $\frac{\pi}{2}$ about a vertex of the central pentagon and $c$ be a rotation of $\pi$ about the midpoint of an adjacent pentagon edge. Then clearly $c^2 = d^4 =
1$. But it is also easy to see that $cd$ is a rotation of $\frac{2\pi}{5}$ about the centre and hence $(cd)^5 = 1$. The rotations $c$ and $d$ are thus the classical generators of $S_5$ and this describes the entire automorphism group of Bring's curve.

Riera and Rodrı́guez give the homology basis for this model by prescribing which edges of the polygon to traverse. We are going to construct an equivalent basis for the HK curve by understanding an isomorphism $$\label{hypiso}
f : \ H \rightarrow
  \left\{(x,y,z)\in\mathbb{C}^3 : \mathcal{C}(x,y,z) = 0 \right\}$$ well enough to determine the precise values to which each edge of the polygon in Fig. [1](#fig:bringHyperbolic){reference-type="ref" reference="fig:bringHyperbolic"} maps. Once this is achieved, converting the homology basis will be a purely mechanical affair as illustrated in [@bn10] for Klein's curve. Along the way we will gain some understanding of how $f$ acts on the automorphism group by push-forwards.
