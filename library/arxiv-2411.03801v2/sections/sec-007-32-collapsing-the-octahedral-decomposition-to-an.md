---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-007-32-collapsing-the-octahedral-decomposition-to-an
section_title: "Collapsing the octahedral decomposition to an ideal triangulation"
section_number: 3.2
pages: 11-13
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.947
---
[]{#sec.collap label="sec.collap"}

In this section we discuss how to collapse the ideal cell decomposition $\mathcal O_D$ of $S^3\setminus (K \cup \{p,q\})$ into an ideal triangulation $\mathcal T_D$ of $S^3\setminus K$. The collapsing depends on fixing an alternating segment $s$ of $D$. By alternating we mean that we overpass the diagram at one end of $s$ and underpass at the other end. We denote by $r_1$ and $r_2$ two regions adjacent to $s$, and by $o$ and $u$ the over-arc and under-arc containing $s$, respectively (see Figure [1](#fig.region2){reference-type="ref" reference="fig.region2"}).

Recall that the octahedral decomposition $\mathcal O_D$ has four edges corresponding to the regions $r_1$, $r_2$, the over-arc $o$, and the under-arc $u$, respectively. We remove all tetrahedra of $\mathcal O_D$ that contain one of those four edges. When viewed from the top, they are represented by triangles lying in $r_1$ or $r_2$, and ones lying beside $o$ or $u$. After removing those triangles as well as dashed lines in between, we add new dashed lines or arcs in an obvious way so that every dashed line is connected, shown as in Figure [1](#fig.region2){reference-type="ref" reference="fig.region2"}. Then all faces of the remaining tetrahedra are paired along dashed lines or arcs. This results in an collapsed ideal triangulation of $S^3 \setminus K$. As the pair $(D,s)$ is determined by the open diagram $\mathring{D}$ obtained by cutting $D$ across $s$, we denote the collapsed triangulation simply by $\mathcal T_{\mathring{D}}$. Note that $s$ being alternating implies the technical assumption $(\dagger)$ on $\mathring{D}$ in Section [\[sub.OT\]](#sub.OT){reference-type="ref" reference="sub.OT"}.

<figure id="fig.region2">

<figcaption>Modified face-pairings.</figcaption>
</figure>

Suppose that the over-arc $o$, the under-arc $u$, and the regions $r_1$ and $r_2$ have $n_o$, $n_u$, $n_{r_1}$ and $n_{r_2}$ segments of $D$, respectively. When $\mathcal O_D$ collapses into $\mathcal T_{\mathring{D}}$, tetrahedra lying in $r_1$ or $r_2$, and ones lying beside $o$ or $u$ disappear: total $(n_{r_1}+n_{r_2} + 4n_u+4n_o-8)$ disappear. Therefore, if $D$ has $n$ crossings, $$\# ( \textrm{tetrahedra of } \mathcal T_{\mathring{D}}) = 4n-n_{r_1}-n_{r_2}-4n_u-4n_o+8 \,.$$

On the other hand, when $\mathcal O_D$ collapses into $\mathcal T_{\mathring{D}}$, edges of different types can be identified. In this case, we keep the bigger type according to the following order. $$C<  R < O , U \,.$$ For instance, if a C-edge and an O-edge are identified, we call the identified one an O-edge. Exceptionally, if an O-edge and a U-edge are identified, we retain both types: the identified edge is both an O-edge and a U-edge.

To describe how edges change explicitly, we denote the crossings of $u$ and $o$ by $c_1,\ldots,c_{n_u + 1}$ and $c_{n_u},\ldots, c_{n_u+n_o}$ respectively, in order so that the common ones, $c_{n_u}$ and $c_{n_u+1}$, are the crossings of $s$. We also denote a segment of $u$ or $o$ by $[c_i,c_{i+1}]$ for $1 \leq i \leq n_o+n_u-1$. When $\mathcal O_D$ collapses into $\mathcal T_{\mathring{D}}$,

-   $(n_u + n_o)$ C-edges disappear. These correspond to $c_1, \ldots, c_{n_u + n_o}$: more precisely, **(Ca)** the one corresponding to $c_1$ is identified with the U-edge corresponding to the under-arc of $c_1$; **(Cb)** the one corresponding to $c_{n_u+n_o}$ is identified with the O-edge corresponding to the over-arc of $c_{n_u+n_o}$; **(Cc)** the others disappear.

-   $(n_u+n_o+2)$ R-edges disappear. Precisely, two R-edges corresponding to regions adjacent to $[c_i,c_{i+1}]$ for $1 \leq i \leq n_u+n_o-1$: **(Ra)** disappear if $i=n_u$ (i.e., if $[c_i,c_{i+1}]=s$); **(Rb)** are identified with the O-edge corresponding to the over-arc of $c_1$ if $i=1$; **(Rc)** are identified with the U-edge corresponding to the under-arc of $c_{n_u+n_o}$ if $i=n_u + n_o -1$; **(Rd)** are identified to one R-edge, otherwise.

-   $(n_u + n_o -3)$ O-edges disappear. Precisely, **(Oa)** the O-edge corresponding to the over-arc containing $[c_i, c_{i+1}]$ vanishes for $1 < i \leq n_u$; **(Ob)** two O-edges corresponding to adjacent over-arcs at $c_i$ other than $o$ are identified for $n_u+1 < i  < n_{u} + n_{o}$.

-   $(n_u + n_o -3)$ U-edges disappear. Precisely, **(Ua)** the U-edge corresponding to the under-arc containing $[c_i, c_{i+1}]$ vanishes for $n_u < i \leq n_o+n_u$; **(Ub)** two U-edges corresponding to adjacent under-arcs at $c_i$ other than $u$ are identified for $1 < i  < n_{u}$.

In addition, for each segment $s' \neq s$ lying in $r_1$ or $r_2$, an O-edge corresponding to the over-arc containing $s'$ is identified with a U-edge corresponding to the under-arc containing $s'$. This leads to $(n_{r_1}+n_{r_2}-2)$ identifications between O-edges and U-edges. We refer to Appendix [\[sec.app\]](#sec.app){reference-type="ref" reference="sec.app"} for details. Therefore, if $D$ has $n$ crossings, $$\begin{aligned}
\# ( \textrm{edges of } \mathcal T_{\mathring{D}}) &= (4n + 2) - (n_u + n_o) - (n_u + n_o +2) \\
 & \quad \quad - (n_u + n _o -3) - (n_u + n _o -3) - (n_{r_1} + n_{r_2} -2 ) \\
&=  \, 4n  - n_{r_1} - n_{r_2}-4n_o -4n_u + 8 \, .
\end{aligned}$$ This double-checks that the number of edges is equal to the number of tetrahedra.

**Example [\[ex.61\]](#ex.61){reference-type="ref" reference="ex.61"} continued.** For the open diagram $\mathring{D}$ of Figure [\[fig.example\]](#fig.example){reference-type="ref" reference="fig.example"}, its closure $D$ is shown on the left of Figure [2](#fig.examplecc){reference-type="ref" reference="fig.examplecc"}. The diagram $D$ has six crossings, and thus the octahedral decomposition $\mathcal O_D$ has six C-edges and eight R-edges, as well as six O-edges $o_1,\ldots,o_6$ and six U-edges $u_1,\ldots , u_6$. It is convenient to label a segment of $D$ by $o_i/u_j$ where $o_i$ and $u_j$ correspond to the over and under-arcs containing the segment, respectively.

We choose an alternating segment $s$ as the one with $o_6/u_1$ (the leftmost one). Then, when $\mathcal O_D$ collapses into the collapsed triangulation $\mathcal T_{\mathring{D}}$,

-   four C-edges adjacent to the segment with $o_1/u_1$, $o_6/u_1$, or $o_6/u_6$ disappear,

-   two R-edges adjacent to the segment with $o_6/u_1$ disappear,

-   two R-edges adjacent to the segment with $o_1/u_1$ are identified with $o_1$,

-   two R-edges adjacent to the segment with $o_6/u_6$ are identified with $u_6$,

-   $o_6$ and $u_1$ disappear.

In addition, we obtain identifications $$o_4 = u_4, \quad o_1 = u_2, \quad  o_2=u_2, \quad  o_5 = u_6,
  \quad o_3 = u_3, \quad o_4=u_5$$ from segments lying in the unbounded region of $D$. It follows that the collapsed triangulation $\mathcal T_{\mathring{D}}$ has two C-edges, two R-edges, and four O or U-edges: $$\{(o_1 = o_2 = u_2), \ (o_3 = u_3), \ (o_4=u_4=u_5), \ (o_5 = u_6) \} \,.$$

To connect the 8 shape parameters of the collapsed triangulation $\mathcal T_{\mathring{D}}$ with the 3 variables of the Yokota potential of Figure [\[fig.example\]](#fig.example){reference-type="ref" reference="fig.example"}, we will eliminate five of them by solving to the gluing equations of two C-edges and two R-edges, and completeness equation of the meridian; see Section [\[sec.reduction\]](#sec.reduction){reference-type="ref" reference="sec.reduction"} for details.

<figure id="fig.examplecc">

<figcaption>Edges of <span class="math inline">𝒪<sub><em>D</em></sub></span> and <span class="math inline">𝒯<sub><em>D̊</em></sub></span>.</figcaption>
</figure>
