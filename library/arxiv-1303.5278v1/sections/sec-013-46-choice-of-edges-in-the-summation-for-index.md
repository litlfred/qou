---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-013-46-choice-of-edges-in-the-summation-for-index
section_title: "Choice of edges in the summation for index"
section_number: 4.6
pages: 20-24
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.941
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
Let $M$ be an orientable 3-manifold with $r \ge 1$ torus cusps and let $\mathcal{T}$ be an ideal triangulation of $M$ with $N$ tetrahedra and, hence, $N$ edges which we denote $e_1, \ldots, e_N$. Let $G$ be the 1-skeleton $\mathcal{T}^{(1)}$ of $\mathcal{T}$ together with one (ideal) vertex for each cusp of $M$. Note that $G$ has $r$ vertices and $N$ edges, and may contain loops (i.e. edges with both ends at a single vertex) or multiple edges between the same two vertices. The incidence matrix $C = (c_{hi})$ for $G$ is an $r \times N$ matrix whose $(h,i)$ entry gives the number of ends of edge $i$ on cusp $h$. Note that each $c_{hi} \in \{0,1,2\}$ and the sum of entries is $2$ in each column of $C$. Let $E(e_i)=E_i  \subset  \mathbb{Z}^{2N}$ be the edge equation coefficients corresponding to edge $e_i$ in $\mathcal{T}$, and let $$\Lambda = \left\{ \sum_{\boldsymbol{k}\in \mathbb{Z}^N} k_i E_i \right\} \subset  \mathbb{Z}^{2N}$$ be the lattice of all integer linear combinations of these. In other words, $E_i$ is the $i$th row of the Neumann-Zagier matrix $(\mathbf A \mid \mathbf B)$, and $\Lambda$ is the integer row space of this matrix.

From the work of Neumann and Zagier (see [@NZ] and [@Neumann-combi Thm 4.1]), the lattice $\Lambda$ has rank $N-r$ and the matrix $C$ gives the linear relations between the edge equation coefficients $E_i \in  \mathbb{Z}^{2N}$. More precisely, $$\label{cusp_relations}
\sum_i c_{hi} E_i =0 \text{ for all } h=1, \ldots, r$$ and any other linear relation between the $E_i$ arises from a real linear combination of the rows of $C$.

::: defn
[]{#maximal tree with cycle label="maximal tree with cycle"} A subset of the edges of a graph $\Gamma$ is a *maximal tree with 1- or 3-cycle* in $\Gamma$ if (together with the vertices) it consists of any maximal tree $T$ together with one additional edge that either (1) is a loop at one vertex, or (2) forms a 3-cycle together with two edges in $T$.
:::

::: thm
[]{#pick_edges label="pick_edges"} There exists an integer basis for $\Lambda$ consisting of $N-r$ of the edge equation coefficients $E_1, \ldots, E_n$. In fact, we can choose such a basis by omitting $r$ edge equations corresponding to a maximal tree with 1- or 3-cycle in $G$.
:::

::: rmk
In other words, we can choose any maximal tree with 1- or 3- cycle for our set $\mathcal X$ of excluded edges, and hence choose the remaining edges as our set $\mathcal B$ of basic edges.
:::

This result and its proof were inspired by Jeff Weeks' argument in [@Weeks:thesis pp. 35--36].

::: proof
*Proof.* First we show that we can find a maximal tree with 1- or 3-cycle. If there exists a loop in $G$ we use this loop together with any maximal tree. If not, any face of the triangulation has its ideal vertices on 3 distinct cusps. Pick two edges of this face and extend these to a maximal tree $T \subset G$. Adding the third edge of the face gives the desired subgraph.

Now let $S$ be a maximal tree with 1- or 3-cycle. Next we show that the $N-r$ equations $E(e)$ corresponding to the edges $e \notin S$ give an integer basis for $\Lambda$. We show that for each $s\in S,$ the equation $E(s)$ can be written as an integer linear combination of the equations $E(e)$ with $e \notin S$. Given this, the $N-r$ equations $E(e)$ with $e \notin S$ form an integer spanning set for $\Lambda$. The work of Neumann and Zagier ([@NZ] and [@Neumann-combi Thm 4.1]), implies that these equations are also linearly independent, hence form an integer basis for $\Lambda$, and we are done.

So, we have to show that every $E(s)$ can be written as an integer linear combination of the $E(e)$ for $e\notin S$. To organise the construction, we use the following sequence of *decorated graphs*. At each step we have a graph $G_k$ whose edges are labelled by names of edges of $G$. We decorate each end of each edge of $G_k$ with a sign. Each vertex $v$ of $G_k$ is then incident to a set of ends of edges with signs. We list the names of the edges, together with the sign associated to this end: $\{ (e_{i_v(1)}, \epsilon_v(1)), (e_{i_v(2)}, \epsilon_v(2)), \ldots, (e_{i_v(d)}, \epsilon_v(d))\}$. Here $d$ is the degree of the vertex $v$. To this vertex we associate the equation $$R_k(v) = \sum_{l=1}^d \epsilon_v(l) E(e_{i_v(l)})=0.$$

For each $G_k$ we have a subset $S_k$ of the edges of $G_k$ which is a maximal tree with 1-or 3-cycle in $G_k$. We set $G_0=G$ and $S_0=S$, with all signs set to $+$. Note that the equations associated to the vertices of $G_0$ are then the same as those given by [\[cusp_relations\]](#cusp_relations){reference-type="eqref" reference="cusp_relations"}.

We obtain the graph and edge subset $(G_{k+1},S_{k+1})$ from $(G_{k},S_{k})$ as follows. We arbitrarily choose a vertex $v$ of $G_k$ that has only one end of one edge $s$ of $S_k$ incident. If there are no such vertices then the sequence ends at $(G_k,S_k)$. Let $w$ be the other end of $s$, which by assumption is distinct from $v$. The graph $G_{k+1}$ is the result of collapsing the edge $s$ of $G_k$; the two ends of $s$, $v$ and $w$, are identified in $G_{k+1}$. We label the edges of $G_{k+1}$ with the same names as in $G_k$ and set $S_{k+1}=S_k \setminus \{s\}.$ All of the signs decorating $G_{k+1}$ are the same as in $G_k$, except that the ends of edges that were incident to $v$ have their signs flipped. See Figure [1](#collapse_edge){reference-type="ref" reference="collapse_edge"}.

<figure id="collapse_edge">
<p><span class="math inline"><em>v</em></span> at 82 170 <span class="math inline"><em>w</em></span> at 82 80 <span class="math inline"><em>s</em></span> at 66 125 <span class="math inline">+</span> at 66 155 <span class="math inline">+</span> at 46 169 <span class="math inline">−</span> at 58 188 <span class="math inline">+</span> at 79 188 <span class="math inline">−</span> at 96 155</p>
<p><span class="math inline">+</span> at 66 95 <span class="math inline">+</span> at 96 95 <span class="math inline">+</span> at 46 74 <span class="math inline">+</span> at 57 54 <span class="math inline">+</span> at 80 54</p>
<p><span class="math inline">+</span> at 227 110 <span class="math inline">+</span> at 241 92 <span class="math inline">+</span> at 265 92 <span class="math inline">+</span> at 280 102 <span class="math inline">+</span> at 280 135 <span class="math inline">−</span> at 264 141 <span class="math inline">+</span> at 243 141 <span class="math inline">−</span> at 227 125</p>
<img src="draws_eps/collapse_edge" style="width:60.0%" />
<figcaption>Collapsing the edge <span class="math inline"><em>s</em></span> flips the signs on the ends of the edges incident to <span class="math inline"><em>v</em></span>. Edges in <span class="math inline"><em>S</em></span> are drawn dashed.</figcaption>
</figure>

Note that at each step of the sequence, both ends of each element of $S_k$ have a $+$ sign, since they do in $G_0$ and we never collapse an edge from a vertex with more than one incident edge end in $S$. Consider the equations associated to the vertices of $G_k$ and $G_{k+1}$. We have

$$R_k(v) = +E(s) + \sum_{l, e_{i_v(l)} \neq s} \epsilon_v(l) E(e_{i_v(l)})=0, \quad R_k(w) = +E(s) + \sum_{m, e_{i_w(m)} \neq s} \epsilon_w(m) E(e_{i_w(m)})=0.$$

If we use $R_k(v)$ to solve for $E(s)$ we get

$$E(s) = \sum_{l, e_{i_v(l)} \neq s} -\epsilon_v(l) E(e_{i_v(l)}).$$

Substituting this into $R_k(w)$ gives

$$\sum_{l, e_{i_v(l)} \neq s} -\epsilon_v(l) E(e_{i_v(l)}) + \sum_{m, e_{i_w(m)} \neq s} \epsilon_w(m) E(e_{i_w(m)})=0.$$

This is the equation associated to the vertex of $G_{k+1}$ formed by the identification of $v$ with $w$. Thus, the sequence of graphs gives an expression for $E(s)$ for each edge $s\in S$ which is removed.

This expression is an integer linear combination of the $E(e)$ for $e \notin S$. The sequence ends, at $G_K$ say. By construction $G_K$ has no vertices for which only one end of an edge of $S$ is incident. If we are in case (1) of Definition [\[maximal tree with cycle\]](#maximal tree with cycle){reference-type="ref" reference="maximal tree with cycle"} then $G_K$ has one vertex, $S_K$ has one edge and $G_K$ looks like Figure [2](#collapse_edge_endgame){reference-type="ref" reference="collapse_edge_endgame"} (left). If we are in case (2) then $G_K$ has three vertices, $S_K$ has three edges, and $G_K$ looks like Figure [2](#collapse_edge_endgame){reference-type="ref" reference="collapse_edge_endgame"} (right).

<figure id="collapse_edge_endgame">

<figcaption>The last graph in the sequence has one of these two forms.</figcaption>
</figure>

In the first case, the equation from the last vertex is of the form $$2E(s) + \sum_{l, e_i(l) \neq s} \epsilon(l) E(e_{i(l)}) = 0.$$ Notice that since all edges are now loops, each $E(e_i)$ appears with total coefficient either $-2,0$ or $2$. So we can divide the entire equation by $2$, and get $E(s)$ as an integer linear combination of the $E(e_i)$.

The second case is slightly more complicated. We have three vertices $x,y,z$, with three edges $s_x,s_y,s_z\in S$ connecting the vertices into a triangle. The three vertices give equations of the form

$$E(s_y) + E(s_z) + X = 0, \quad E(s_z) + E(s_x) + Y = 0, \quad E(s_x) + E(s_y) + Z= 0,$$ where $X,Y,Z$ are terms coming from the edges not in $S$. We can solve these equations for $E(s_z)$ as $$2E(s_z) = -X-Y+Z,$$ and the other two expressions similarly. We just have to show that $-X-Y+Z$ has even coefficients, and then we will be done. As before, any loops contribute a coefficient in $\{-2,0,2\}$ to one of $X,Y$ or $Z$. For edges with the same endpoints as one of $s_x,s_y$ or $s_z$, their coefficients are $1$ or $-1$ at two of $X,Y$ and $Z$ and $0$ at the third. Thus their contribution to $-X-Y+Z$ is also in $\{-2,0,2\}$, and so $-X-Y+Z$ has even coefficients, as required. ◻
:::

::: ex
The following example shows that the edges omitted must be chosen carefully in the multi-cusped case. Let $M$ be the Whitehead link complement (with the triangulation given by m129 in SnapPy notation). Then the matrix of edge equations is $$(\mathbf A \mid \mathbf B) = 
\begin{pmatrix}
2 & -1 & 1 & 1 & \vline & 1 & -2 &  0 & 0 \\
-1 & 0 & 0 & 0  & \vline & -1 & 1 & 1 & 1 \\
0 & 1 & -1 & -1 & \vline & 1 & 0 & -2 & -2 \\
-1 & 0 & 0 & 0 & \vline & -1 & 1 & 1 & 1
\end{pmatrix}$$

The cusp incidence matrix is $$C = \begin{pmatrix} 1 & 2 & 1 & 0 \\ 1 & 0 & 1 & 2 \end{pmatrix}$$ and the corresponding graph $G$ is shown in Figure [3](#wh_link_edges_and_cusps){reference-type="ref" reference="wh_link_edges_and_cusps"}.

<figure id="wh_link_edges_and_cusps">
<p><span class="math inline"><em>e</em><sub>1</sub></span> at -5 20 <span class="math inline"><em>e</em><sub>3</sub></span> at 168 20 <span class="math inline"><em>e</em><sub>0</sub></span> at 81.5 44 <span class="math inline"><em>e</em><sub>2</sub></span> at 81.5 -5 <span class="math inline"><em>c</em><sub>0</sub></span> at 49 30 <span class="math inline"><em>c</em><sub>1</sub></span> at 114 30</p>
<img src="draws_eps/wh_link_edges_and_cusps" style="width:36.0%" />
<figcaption>The graph of edges and cusps for the Whitehead link.</figcaption>
</figure>

The rows $E_0, E_1, E_2, E_3$ of $(\mathbf A \mid \mathbf B)$ satisfy the relations: $$E_0 + 2 E_1 + E_2   = 0 \text{ (from cusp 0)}$$ and $$E_0 + E_2  + 2 E_3  = 0 \text{ (from cusp 1)},$$ which imply that $E_1=E_3$.\
It follows that $E_0, E_1$ are linearly independent and form an integer basis for the $\mathbb{Z}$-span of $\{ E_0,E_1,E_ 2,E_3 \}$. (This basis corresponds to removing the edge $e_2$ in a maximal tree and an additional loop $e_3$.)

On the other hand, $E_0$, $E_2$ are also linearly independent and $2E_1$ is in the $\mathbb{Z}$-span of $\{ E_0,E_2 \}$ but $E_1$ is not in $\mathbb{Z}$-span of $\{ E_0,E_ 2 \}$. So $\mathbb{Z}\text{-span} \{ E_0,E_2 \}$ is an index 2 subgroup in $\mathbb{Z}\text{-span} \{ E_0,E_1 \}$. Thus, a summation using $E_0, E_2$ will most likely give a different result for the index than using $E_0, E_1$.
:::
