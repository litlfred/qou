---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-007-8-construction-of-different-manifolds-sharing-th
section_title: "Construction of different manifolds sharing the same volume"
section_number: 8
pages: 21-23
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.986
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N(v) of orientable hyperbolic 3-manifolds with any given volume v."
---
[]{#const label="const"} We start with the graph with $2n$ vertices shown in Figure [1](#fig.source){reference-type="ref" reference="fig.source"}. This graph is obtained by applying the gluing move in Lemma [\[Vol\]](#Vol){reference-type="ref" reference="Vol"} $n+1$ times to $W_{2n}$.

![Starting point: graph with $2n$ vertices (represented by circles)](source1_1.eps){#fig.source}

First, we label every remaining pair of thrice punctured spheres by an element of $\{0,1\}$. For each such pair we apply Lemma [\[Vol\]](#Vol){reference-type="ref" reference="Vol"} as follows. We glue the pair of thrice punctured spheres labelled by $0$ (resp. $1$) without (resp. with) a half twist, as in Figure [\[fig.move1\]](#fig.move1){reference-type="ref" reference="fig.move1"} (left) (resp.(right)). By this construction, we get a hyperbolic link complement $M_b$ for each cyclic binary word $b$ of length $n$ and its volume is $4n V_8$.

Now we consider the decomposition of $M_b$ into isometric convex hyperbolic polyhedra with shaded faces described in section [\[polyhedral_decomp\]](#polyhedral_decomp){reference-type="ref" reference="polyhedral_decomp"}. Note that every edge lies in exactly one shaded triangular face, since the faces have a checkerboard colouring.

::: defi
*Given an edge $e$ in such a polyhedral decomposition, let $t$ be the shaded ideal triangle containing $e$. Then the *midpoint* $m$ of $e$ is the foot of the perpendicular in $t$ from the vertex of $t$ opposite $e$ to $e$.*
:::

Since isometries preserve angles, when we glue two thrice punctured sphere boundaries together by an isometry, it maps midpoints to midpoints. Moreover, for fully augmented links, we may expand horoball neighbourhoods of the cusps to find a horoball packing such that the horoballs bump together precisely at the midpoints of edges. More precisely,

::: thm
[]{#thm.packing label="thm.packing"} Let $L$ be a fully augmented link. Then there exist horoball neighbourhoods of the cusps of $S^3\setminus L$ such that the midpoint of every edge is a point of tangency of the corresponding horospherical tori.
:::

::: rmk
[]{#horo_packing_invariant label="horo_packing_invariant"} *For each $M_b$, we fix the horoball packing $\mathcal{H}_b$ given by Theorem [\[thm.packing\]](#thm.packing){reference-type="ref" reference="thm.packing"}. In fact, this horoball packing depends only on the geometry of $M_b$ and not on any choice of polyhedral decomposition for $M_b$. This follows since the horospherical tori for $\mathcal{H}_b$ can be defined as follows: For each cusp with modulus $\sqrt{-1}$ or $2\sqrt{-1}$ we choose the horospherical torus of area $2$, and for each cusp with modulus $m \sqrt{-1}$ with $m>2$ we choose the horospherical torus of area $4m$. These areas are easily calculated from the diagrams in Figures [\[fig.pack1\]](#fig.pack1){reference-type="ref" reference="fig.pack1"}--[\[fig.pack3\]](#fig.pack3){reference-type="ref" reference="fig.pack3"} and Figure [\[fig.cuspshapes\]](#fig.cuspshapes){reference-type="ref" reference="fig.cuspshapes"}, using the fact that each dotted edge in Figures 10-12 has length 1 in the horospherical tori for $\mathcal{H}_b$, (since it is a horocycle joining midpoints of edges in an ideal hyperbolic triangle).*
:::

::: thm
[]{#change_mfd label="change_mfd"} Let $b_i$ be a binary cyclic word of length $n\ge 3$ and let $M_{b_i}$ be the hyperbolic link complement obtained from $b_i$ by the above procedure for $i = 1,2$. Then $M_{b_1}$ is isometric to $M_{b_2}$ if and only if $b_1$ and $b_2$ are related by the natural action of $D_n$, the dihedral group of order $2n$.
:::

::: proof
*Proof.* Let $b$ be a binary cyclic word of length $n$. If $b$ contains $k \ge 1$ zeros, then we can split $b$ into $k$ subwords of the form $p_i =  011 \cdots  10$ with $i$ $1$'s $(i\geq 0)$ by using each zero in $b$ exactly twice.

After the gluing move in Lemma [\[Vol\]](#Vol){reference-type="ref" reference="Vol"}, each $p_{i}$ produces a torus cusp with $2i+1$ crossings, whose modulus is $m_i = 2(2i+2)\sqrt{-1} = 4(i+1)\sqrt{-1}$ (see Example [\[example\]](#example){reference-type="ref" reference="example"}). Let $\{ p_{i_1}, p_{i_2},..., p_{i_k} \}$ be the decomposition of $b$, and let $C_j$ be the cusp corresponding to the knot component produced by $p_{i_j}$. We get a cyclic sequence $\{m_{i_1}, m_{i_2}, ..., m_{i_k}\}$ of cusp moduli from $b$. Note that the total number of cusps of $M_b$ is $2n+1+k$; the crossing circle cusp $C$ at the top of Figure [1](#fig.source){reference-type="ref" reference="fig.source"} has modulus $n \sqrt{-1}$ (from the cusp diagram in Figure [\[fig.pack3\]](#fig.pack3){reference-type="ref" reference="fig.pack3"}), and the other $2n$ crossing circle cusps have modulus $\sqrt{-1}$ or $2\sqrt{-1}$ by Example [\[example\]](#example){reference-type="ref" reference="example"}.

We now only consider cusps whose modulus has norm greater than $2$. For $n \ge 3$, these are the cusps $C_1, \ldots C_k$ and $C$. From $M_b$, we will construct a labelled *cusp graph* $\mathcal{C}_b$ with vertices $\{v_1, v_2, ..., v_{k+1}\}$ as follows. We label $v_j$ by $m_{i_j}$ for $1\leq j\leq k$ and $v_{k+1}$ by $n\sqrt{-1}$, the modulus of $C$. Then join $v_i$ and $v_{i'}$ by an edge if in $\mathcal{H}_b$, horoball neighbourhoods of the cusps corresponding to $v_i$ and $v_{i'}$ are tangent to each other. In $\mathcal{H}_b$, the horoball neighbourhood of each cusp $C_j$ bumps only into $C_{j-1}$, $C_{j+1}$ (with index modulo $k$), and $C$. Therefore, the graph $\mathcal{C}_b$ consists of a cycle of length $k$ whose vertices are labelled cyclically by the $m_{i_j}$'s and one vertex labelled by $n$ joined to every vertex of the cycle.

The special case when $b=111 \cdots 1$ and $k=0$ is slightly different. Then $M_b$ has one cusp $C$ of modulus $n \sqrt{-1}$ as above, two knot components giving cusps $C_1,C_2$ of modulus $2n \sqrt{-1}$, and $2n$ cusps of modulus $\sqrt{-1}$. In this case, the cusp graph $\mathcal{C}_b$ is a 3-cycle.

Conversely given such a labelled cusp graph, we can reconstruct a binary cyclic word. Therefore given two binary cyclic words $b_1$ and $b_2$ of length $n$, the graph $\mathcal{C}_{b_1}$ is isomorphic to $\mathcal{C}_{b_2}$ as a graph with labelled vertices if and only if $b_1$ is related to $b_2$ by the natural action of $D_{n}$. Moreover, by Remark [\[horo_packing_invariant\]](#horo_packing_invariant){reference-type="ref" reference="horo_packing_invariant"}, any isometry between manifolds $M_{b_1}$ and $M_{b_2}$ takes the horoball packing $\mathcal{H}_{b_1}$ to $\mathcal{H}_{b_2}$. Hence, the manifold $M_{b_1}$ is isometric to $M_{b_2}$ if and only if the graph $\mathcal{C}_{b_1}$ is isomorphic to $\mathcal{C}_{b_2}$ as a graph with labelled vertices. This completes the proof. ◻
:::

::: thm
[]{#thm.expo label="thm.expo"} For each $n \ge 3$, there are at least $2^n/(2n)$ different hyperbolic link complements of volume $4nV_8$.
:::

::: proof
*Proof.* By theorem [\[change_mfd\]](#change_mfd){reference-type="ref" reference="change_mfd"}, there are at least as many hyperbolic link complements of volume $4nV_8$ as cyclic binary words of length $n$, up to the action of $D_n$. But there are $2^n$ based cyclic binary words of length $n$, and each orbit under the $D_n$ action has at most $2n$ elements. So the result follows. ◻
:::

::: rmk
*For the sequence $v_n = 4nV_8$, this gives a logarithmic growth rate $$\limsup_{n\to\infty} {\log  N_L(v_n) \over v_n} \ge
{\log 2 \over 4 V_8} \approx 0.0472962 .$$ Chesebro-BeBlois [@CD] construct examples of $2^n/2$ hyperbolic link complements of volume $w_n \approx 24.092184n + 2V_8$, giving a logarithmic growth rate $$\limsup_{n\to\infty} {\log  N_L(w_n) \over w_n} 
 \ge 0.0287706 .$$*
:::
