---
doc_id: arxiv-1206.6004v2
doc_title: "Symmetry, Integrability and Geometry: Methods and Applications"
section_id: sec-005-41-introduction-to-h
section_title: "Introduction to H"
section_number: 4.1
pages: 6-9
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.904
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

## Riera and Rodrı́guez basis {#section4.2}

We start by recapitulating the hyperbolic basis of interest. Riera and Rodrı́guez begin with a simple non-canonical basis. They first define $$\begin{gathered}
  \alpha_1  = 1 + 2, \qquad
  \alpha_2  = 3 + 4
\end{gathered}$$ (in edge traversal notation, see [@rauch; @riera]) and then act on these cycles by rotations of $\frac{2\pi k}{5}$ to obtain their initial basis. So essentially $$\alpha_i = (2i-1) + (2i).$$

Next they specify (by fiat) a matrix which transforms these $\alpha_i$ into a canonical basis and proceed to derive further basis change to make use of the symmetries. The end result is the following basis-change matrix (implicit in [@riera]) $$\label{basistrans}
  \begin{pmatrix}
  1 & 0  & 0 & 0  & -2 & 0 & 1  & 0  \\
  1 & -1 & 0 & -1 & -1 & 1 & 1  & 1  \\
  1 & -1 & 0 & 0  & -1 & 2 & 1  & -1 \\
  0 & -1 & 0 & 0  & 1  & 2 & 0  & 0  \\
  1 & -1 & 1 & 0  & -1 & 1 & -1 & -1 \\
  1 & -1 & 1 & -1 & 0  & 0 & -1 & 1  \\
  1 & -1 & 1 & -1 & 0  & 1 & 0  & 1  \\
  0 & -1 & 0 & -1 & 1  & 1 & 1  & 2
  \end{pmatrix},$$ which sends the initial $\alpha_1,\dots,\alpha_{8}$ homology basis to another $\{\mathfrak{a}_i,\mathfrak{b}_i\}_{i=1}\sp{4}$, that is not only canonical but behaves well with respect to the symmetry group of the curve. Now the symmetries relate the periods $\mathcal{A}_{ij}=\int_{\mathfrak{a}_i}v_j$ and $\mathcal{B}_{ij}=\int_{\mathfrak{b}_i}v_j$ (for any basis of holomorphic differentials $v_i$). As a consequence, the period matrix $\tau=\mathcal{B}\mathcal{A}\sp{-1}$ can be written as [\[RRstau\]](#RRstau){reference-type="eqref" reference="RRstau"}, where $\tau_0 \approx -0.5+0.185576\mathrm{i}$ is defined in terms of Klein's $j$-invariants[^1] by $$\begin{gathered}
\label{deftau0}
  j(\tau_0) = -\frac{29^3\times 5}{2^5}, \qquad
  j(5\tau_0) = -\frac{25}{2}.
\end{gathered}$$

[^1]: Riera and Rodrı́guez swap these two equations. However, we believe this to be a typographical error.
