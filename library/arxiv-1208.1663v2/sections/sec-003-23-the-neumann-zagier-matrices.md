---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-003-23-the-neumann-zagier-matrices
section_title: "The Neumann-Zagier matrices"
section_number: 2.3
pages: 5-7
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.959
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sub.NZ label="sub.NZ"}

Fix is an oriented ideal triangulation $\mathcal T$ with $N$ tetrahedra of a 3-manifold $M$ with torii boundary components. Sssign variables $Z_i,Z'_i,Z''_i$ at the opposite edges of each tetrahedron $\Delta_i$ respecting its orientation as in Figure [1](#fig.tetZZZ){reference-type="ref" reference="fig.tetZZZ"}.

<figure id="fig.tetZZZ">
<div class="center">
<embed src="draws/tetrahedronZZZ.pdf" />
</div>
<figcaption>Shapes of a tetrahedron.</figcaption>
</figure>

Then we can read off matrices $N\times N$ matrices $\bar{\mathbf A}$, $\bar{\mathbf B}$ and $\bar{\mathbf C}$ whose rows are indexed by the $N$ edges of $\mathcal T$ and whose columns are indexed by the $Z_i,Z'_i,Z''_i$ variables. These are the so-called *Neumann-Zagier matrices* that encode the exponents of the *gluing equations* of $\mathcal T$, originally introduced by Thurston [@NZ; @Th]. In terms of these matrices, a generalized angle structure is a triple of vectors $\alpha,\beta,\gamma\in \mathbb R^N$ that satisfy the equations $$\label{eq.angle}
\bar{\mathbf A} \alpha+ \bar{\mathbf B} \beta+ \bar{\mathbf C} \gamma= (2,\dots,2)^T, 
\qquad \alpha+\beta+\gamma=(1,\dots,1)^T \,.$$ A *quad* $Q$ for $\mathcal T$ is a choice of pair of opposite edges at each tetrahedron $\Delta_i$ for $i=1,\dots,N$. $Q$ can be used to eliminate one of the three variables $\alpha_i,\beta_i,\gamma_i$ at each tetrahedron using the relation $\alpha_i+\beta_i+\gamma_i=1$. Doing so, Equations [\[eq.angle\]](#eq.angle){reference-type="eqref" reference="eq.angle"} take the form $$\mathbf A \alpha+ \mathbf B \gamma= \nu \,.$$ The matrices $(\mathbf A|\mathbf B)$ have some key *symplectic properties*, discovered by Neumann-Zagier when $M$ is a hyperbolic 3-manifold (and $\mathcal T$ is well-adapted to the hyperbolic structure) [@NZ], and later generalized to the case of arbitrary 3-manifolds in [@Neumann-combi]. Neumann-Zagier show that the rank of $(\mathbf A|\mathbf B)$ is $N-r$, where $r$ is the number of boundary components of $M$; all assumed torii. If we choose $N-r$ linearly independent rows of $(\mathbf A|\mathbf B)$, then we obtain matrices $(\mathbf A'|\mathbf B')$ and a vector $\nu'$, which combine to $\mathbf M=(\mathbf A'|\mathbf B'|\nu')$. In addition, the exponents of meridian and longitude loops at each boundary torus give additional matrices $(a^T,b^T)$ and $(c^T,d^T)$ of size $r \times 2N$.

::: definition
[]{#def.indexT label="def.indexT"} The 3D index of $\mathcal T$ is defined by $$\label{eq.index2}
I_{\mathcal T}(m,e)(q)=I_{\mathbf M}(d m - b e, -c m + a e)(q)$$
:::

Implicit in the above definition is a choice of quad $Q$ and a choice of rows to remove. However, the index is independent of these choices; see Remark [\[rem.GLr\]](#rem.GLr){reference-type="ref" reference="rem.GLr"}. Keep in mind the action of $(\mathbb Z/3)^N$ given by acting on the $i$th columns $\bar a_i$, $\bar b_i$ and $\bar c_i$ of $\bar{\mathbf A}$, $\bar{\mathbf B}$ and $\bar{\mathbf C}$ by $$S(\bar a_i |\bar b_i |\bar c_i)=(\bar b_i |\bar c_i |\bar a_i), \qquad$$ (and fixing all other columns) and on the $i$th coordinates of an angle structure by $$S(\alpha_i,\beta_i,\gamma_i)=(\beta_i,\gamma_i,\alpha_i)$$ (and fixing all other coordinates) and on the $i$th columns $a_i$ and $b_i$ of $\mathbf A$ and $\mathbf B$ by $$S(a_i|b_i|\nu)=(-b_i |a_i-b_i|\nu-b_i) \,.$$ (and fixing all other columns). Since the rank of $(\mathbf A|\mathbf B)$ is $N-r$ and $\mathbf A, \mathbf B$ are $(N-r)\times N$ matrices, it follows that $\mathbf M$ admits a strict structure if and only $\mathcal T$ admits a strict angle structure. In addition, $\mathcal T$ admits an index structure if for every choice of quad $Q$ there exist a solution $(\alpha,\beta,\gamma)$ of Equations [\[eq.angle\]](#eq.angle){reference-type="eqref" reference="eq.angle"} that satisfies the inequalities [\[eq.index.ineq\]](#eq.index.ineq){reference-type="eqref" reference="eq.index.ineq"}. Theorem [\[thm.IMconv\]](#thm.IMconv){reference-type="ref" reference="thm.IMconv"} implies the following.

::: theorem
[]{#thm.3 label="thm.3"} The index $I_{\mathcal T}: \mathbb Z^r \times \mathbb Z^r \longrightarrow\mathbb Z((q^{1/2}))$ is well-defined if and only if $\mathcal T$ admits an index structure. In particular, $I_{\mathcal T}$ exists if $\mathcal T$ admits a strict angle structure.
:::

See Section [\[sub.m136\]](#sub.m136){reference-type="ref" reference="sub.m136"} for an example of an ideal triangulation $\mathcal T$ of the census manifold `m136` [@census] which admits a semi-strict angle structure (i.e., angles are nonnegative real numbers), does not admit a strict angle structure, and which has a solution of the gluing equations that recover the complete hyperbolic structure. A case-by-case analysis shows that this example admits an index structure, thus the index $I_{\mathcal T}$ exists. This example appears in [@HRS Example 7.7]. We thank H. Segerman for a detailed analysis of this example.
