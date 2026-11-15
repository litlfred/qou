---
doc_id: arxiv-2109.00379v1
doc_title: "TWISTED NEUMANN–ZAGIER MATRICES"
section_id: sec-003-13-neumannzagier-matrices-and-their-twisted-vers
section_title: "Neumann–Zagier matrices and their twisted version"
section_number: 1.3
pages: 3-7
source_pdf: 2109.00379v1.pdf
source_sha256: f0c9bd89312a761c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.982
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
---
[]{#sub.tNZ label="sub.tNZ"}

Having already discussed the torsion and twisted torsion, we now recall some basic facts from ideal triangulations of 3-manifolds and their gluing equations, following [@Thurston; @NZ]. Let $M$ be an oriented hyperbolic 3-manifold with a torus boundary component (often called a one-cusped hyperbolic 3-manifold) equipped with an ideal triangulation $\mathcal T$. An Euler characteristic argument shows that the number $N$ of tetrahedra in $\mathcal T$ is equal to the number of edges. We order the edges $e_i$ and the tetrahedra $\Delta_j$ of $\mathcal T$ for $1 \leq i,j \leq N$. A quad type of a tetrahedron is a pair of opposite edges; hence each tetrahedron has three quad types. We fix an orientation and a quad type of each tetrahedron $\Delta_j$ so that each edge of $\Delta_j$ admits a shape parameter among $$z_j, \ z'_j=\frac{1}{1-z_j},\
  \textrm{or } z''_j=1- \frac{1}{z_j} \in \mathbbm C\setminus \{0,1\}$$ with opposite edges having same parameters (see Figure [1](#fig.tetrahedron){reference-type="ref" reference="fig.tetrahedron"}). We denote by $\square$ the three pairs of opposite edges of a tetrahedron, so that the edges of $\square$ are assigned the edge parameter $z^\square$.

<figure id="fig.tetrahedron">

<figcaption>An ideal tetrahedron.</figcaption>
</figure>

A complete hyperbolic structure of $M$ can be described by a special solution of the gluing equations. The latter describe the holonomy of the hyperbolic structure around each edge $e_i$ of $\mathcal T$, and have the (logarithmic) form $$\label{eqn:gluing}
\sum_{j=1}^N \left(\mathbf{G}_{ij} \log z_j +\mathbf{G}'_{ij} \log z'_j
  +\mathbf{G}''_{ij} \log z''_j\right) = 2\pi \sqrt{-1} .$$ Here $\mathbf{G}$, $\mathbf{G}'$ and $\mathbf{G}''$ are the gluing equation matrices whose rows and columns are indexed by the edges and by the tetrahedra of $\mathcal T$, respectively, such that the $(i,j)$-entry of $\mathbf{G}^\square$ is the number of edges of $\Delta_j$ with parameter $z^\square_j$ is incident to the edge $e_i$ in $\mathcal T$. It will be convenient to introduce $\zeta$-variables $$\label{eqn.zeta}
\zeta = \frac{d \log z}{dz}=\frac{1}{z}, \quad
\zeta' = \frac{d \log z'}{dz}=\frac{1}{1-z},\quad
\zeta'' = \frac{d \log z''}{dz}=\frac{1}{z(z-1)}$$ following [@siejakowski]. Note that the three shape parameters in each tetrahedron satisfy the relation $z z' z''=-1$, and this implies the linear relation $\zeta+\zeta'+\zeta''=0$. Thus one can eliminate the variable $\zeta'$ from any expression given in terms of $\zeta, \zeta'$, and $\zeta''$, arriving at the *Neumann--Zagier matrices* $$\label{AB}
\mathbf{A}:=\mathbf{G}-\mathbf{G}', \qquad
\mathbf{B}:=\mathbf{G}''-\mathbf{G}'  .$$ Note that $$\label{3GAB}
\mathbf{G}\, \mathrm{diag}(\zeta)
+\mathbf{G}' \, \mathrm{diag}(\zeta')
+ \mathbf{G}'' \, \mathrm{diag}(\zeta'')
= \mathbf{A}  \, \mathrm{diag}(\zeta) + \mathbf{B} \, \mathrm{diag}(\zeta'')$$ where $\mathrm{diag}(\zeta^\square)$ denotes the diagonal matrix with diagonal entries $\zeta^\square_1,\ldots,\zeta^\square_N$.

The NZ matrices have remarkable properties discovered in [@NZ] which is a starting point for the quantization of the gluing equations and for passing from hyperbolic geometry to quantum topology. The symplectic property of the NZ matrices implies that $$\label{eqn.sympl}
\mathbf{A} \mathbf{B}^T = \mathbf{B} \mathbf{A}^T.$$

There are two enhancements of the gluing equations and of their corresponding matrices. The first is obtained by looking at the cusp, i.e., the peripheral (also called boundary) torus of the 3-manifold. By a *peripheral curve* we mean an oriented, homotopically non-trivial, simple closed curve in the peripheral torus of $M$. A peripheral curve $\gamma$ gives a triple $(\mathbf{C}_\gamma,\mathbf{C}'_\gamma,\mathbf{C}''_\gamma)$ of row vectors in $\mathbbm Z^N$ that describe the completeness equation as $$\sum_{j=1}^N \left(\mathbf{C}_{\gamma j}\log z_j +\mathbf{C}'_{\gamma j} \log z'_j
  +\mathbf{C}''_{\gamma j} \log z''_j\right)  = 0.$$ Fixing a peripheral curve $\gamma$, let $\widehat{\mathbf{G}}^\square$ denote the matrix obtained from $\mathbf{G}^\square$ by replacing the last row by $\mathbf{C}^\square_\gamma$, and likewise for $\widehat{\mathbf{A}}$ and $\widehat{\mathbf{B}}$.

The second enhancement is a *combinatorial flattening* of $\mathcal T$, that is a triple $(f,f',f'')$ of column vectors in $\mathbbm Z^N$ such that $$\begin{aligned}
\mathbf{G} f+\mathbf{G}' f' + \mathbf{G}'' f'' & =(2,\ldots,2)^T,\\
f+ f' +  f'' & =(1,\ldots,1)^T,\\
\mathbf{C}_\gamma f+\mathbf{C}'_\gamma f' + \mathbf{C}''_\gamma f'' &=0  
\end{aligned}$$ for any peripheral curve $\gamma$. This term was introduced in [@DG1 Sec.4.4] as a necessary ingredient to define the 1-loop invariant (and there, it was called a combinatorial flattening compatible with any peripheral curve). Every ideal triangulation has combinatorial flattenings [@Neumann04 Thm.4.5].

This concludes our discussion of the NZ matrices. We now introduce a twisted version of the NZ matrices of an ideal triangulation $\mathcal T$ of a 3-manifold $M$ as above. We will fix an epimorphism $\alpha : \pi_1(M) \rightarrow \mathbbm Z$ and a peripheral curve $\mu$ satisfying $\alpha(\mu)=1$. For instance, if $M$ is a knot complement in $S^3$, then $\alpha$ is the abelianization map and $\mu$ is a meridian of the knot. Let $\widetilde M$ and $M^{(n)}$ denote the cyclic covers of $M$ corresponding to $\alpha^{-1}(0)$ and $\alpha^{-1}(n \mathbbm Z)$, respectively. The ideal triangulation $\widetilde\mathcal T$ of the infinite cyclic cover $\widetilde M$ induced from $\mathcal T$ is equipped with an action of the deck transformation group $\mathbbm Z$ (generated by the $\mu$-action), and induces an ideal triangulation $\mathcal T^{(n)}$ of the $n$-fold cyclic cover $M^{(n)}$.

We choose lifts $\widetilde e_i$ and $\widetilde\Delta_j$ of $e_i$ and $\Delta_j$ to $\widetilde\mathcal T$, respectively, and for $k \in \mathbbm Z$ let $\mathbf{G}_k^\square$ be the $N \times N$ matrix whose $(i,j)$-entry is the number of edges of $\mu^k \cdot \widetilde\Delta_j$ with parameter $z_j^\square$ is incident to the edge $\widetilde e_i$ in $\widetilde\mathcal T$. Note that $\mathbf{G}_k^\square$ is a zero matrix for all but finitely many $k$, as there are finitely many tetrahedra around $\widetilde e_i$. We define the *twisted gluing equation matrices* $\mathbf{G}^\square(t)$ of $\mathcal T$ by $$\label{Gt}
\mathbf{G}^\square(t):= \sum_{k \in \mathbbm Z} \mathbf{G}^\square_k\, t^k$$ and the *twisted Neumann--Zagier matrices* by $$\label{ABt}
\mathbf{A}(t):=\mathbf{G}(t)-\mathbf{G}'(t), \qquad
\mathbf{B}(t):=\mathbf{G}''(t)-\mathbf{G}'(t)  .$$ (More generally, if $\mathbf{X}(t)$ is a matrix with entries in $\mathbbm Z[t^{\pm1}]$, we denote by $\mathbf{X}_k$ the coefficient of $t^k$ in $\mathbf{X}(t)$.) Note that the rows and columns of these matrices are indexed by the edges and tetrahedra of $\mathcal T$, respectively, and that their entries are in the ring $\mathbbm Z[t^{\pm1}]$. Since the above matrices are well-defined after fixing lifts of each edge of $\mathcal T$, a different choice of lifts changes $\mathbf{G}^\square(t)$, $\mathbf{A}(t)$ and $\mathbf{B}(t)$ by multiplication from the left by the same diagonal matrix $\mathrm{diag}(t^{c_1},t^{c_2},\dots,t^{c_N})$ for integers $c_1,c_2,\dots,c_N$. This ambiguity propagates to any invariant constructed using these matrices.

A first property of the twisted NZ matrices $(\mathbf{A}(t) \,| \, \mathbf{B}(t))$ is that they determine the NZ matrices $(\mathbf{A}^{(n)} | \, \mathbf{B}^{(n)})$ of the cyclic covers $\mathcal T^{(n)}$ of $\mathcal T$, and moreover they do so via block circulant matrices, i.e., square matrices such that each row is obtained by its predecessor by a cyclic shift. We refer to [@Davis] and [@circulant] for details on the properties of block circulant matrices.

::: theorem
[]{#thm.NZcyclic label="thm.NZcyclic"} We have $$\label{An}
\mathbf{X}^{(n)} = 
\begin{pmatrix*}[c]
  \sum_{r \equiv 0} \mathbf{X}_r & \sum_{r \equiv 1} \mathbf{X}_r
  & \cdots & \sum_{r \equiv n-1} \mathbf{X}_r\\
  \sum_{r \equiv n-1} \mathbf{X}_r & \sum_{r \equiv 0} \mathbf{X}_r
  & \cdots & \sum_{r \equiv n-2} \mathbf{X}_r\\
  \vdots & \vdots & \ddots & \vdots \\
  \sum_{r \equiv 1} \mathbf{X}^\square_r & \sum_{r \equiv 2} \mathbf{X}_r
  & \cdots & \sum_{r \equiv 0} \mathbf{X}_r 
\end{pmatrix*}$$ for $\mathbf{X}=\mathbf{G}^\square$, $\mathbf{A}$ or $\mathbf{B}$.
:::

The twisted NZ matrices satisfy a twisted version of the symplectic property of Equation [\[eqn.sympl\]](#eqn.sympl){reference-type="eqref" reference="eqn.sympl"}.

::: theorem
[]{#thm.sympl label="thm.sympl"} We have $$\label{eqn.abba}
\mathbf{A}(t) \mathbf{B}(1/t)^T = \mathbf{B}(t) \mathbf{A}(1/t)^T.$$
:::

In other words, $\mathbf{A}(t) \mathbf{B}(1/t)^T$ is symmetric under tranposition followed by $t \mapsto 1/t$. In particular, $\mathbf{A}(\omega) \mathbf{B}(\omega)^\ast$ is Hermitian for $\omega \in \mathbbm C$ with $|\omega|=1$ and so is $\mathbf{B}(\omega)^{-1}\mathbf{A}(\omega)$ if $\mathbf{B}(\omega)$ is non-singular. Here $X^\ast$ is the complex conjugate of the transpose of a matrix $X$. Note that given any ideal triangulation, we can choose quads so that $\mathbf{B}$ (hence also $\mathbf{B}(t)$, since $\mathbf{B}(1)=\mathbf{B}$) is invertible; see [@DG1 App.A].

We now come to a conjectural property of the twisted NZ matrices, which we have checked in numerous examples.

::: conjecture
[]{#conj.ABt label="conj.ABt"} The Laurent polynomials $\det(\mathbf{A}(t))$ and $\det(\mathbf{B}(t))$ are palindromic, i.e. satisfy $p(t)=\varepsilon t^r p(1/t)$ for some $\varepsilon= \pm1$ and an integer $r$.
:::

We next discuss the behavior of the twisted NZ matrices under a 2--3 Pachner move relating an ideal triangulation $\mathcal T$ with $N$ tetrahedra to another one $\overline{\mathcal T}$ with $N+1$ tetrahedra. Recall that such a move is determined by two tetrahedra with a common face in $\mathcal T$, which become three tetrahedra with a common edge in $\overline{\mathcal T}$ as shown in Figure [\[fig.pachner\]](#fig.pachner){reference-type="ref" reference="fig.pachner"} below. Let us write the twisted NZ matrices $\mathbf{A}(t)$ and $\mathbf{B}(t)$ of the triangulation $\mathcal T$ schematically in columns as $$\mathbf{A}(t) = (a_1,\;a_2,\;a_i)\,,\quad \mathbf{B}(t) = (b_1,\;b_2,\;b_i)\,,$$ with $a_i$ meaning $(a_3,a_4,...,a_N)$ and similarly for $b_i$. Let $\overline{\mathbf{A}}(t)$ and $\overline{\mathbf{B}}(t)$ denote the corresponding twisted NZ matrices of $\overline{\mathcal T}$.

::: theorem
[]{#thm.NZpachner label="thm.NZpachner"} With the above notation, there exists a lower triangular matrix $P$ with 1's on the diagonal such that

$$\label{3AB}
P \, \overline{\mathbf{A}}(t) = \begin{pmatrix} -1 & -1 & -1  & 0 \\ 
  b_1+b_2 & a_1 & a_2 & a_i \end{pmatrix}\,,\qquad
P \, \overline{\mathbf{B}}(t) = \begin{pmatrix} -1 & -1 & -1 & 0 \\
  0 & a_2+b_1 & a_1+b_2 & b_i 
\end{pmatrix} .$$
:::

This corrects the omission of $P$ in [@DG1 Eqn.(3.27)], which does not affect the validity of the proofs in [@DG1].
