---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-001-2-index-structures-angle-structures-and-the-3d-i
section_title: "Index structures, angle structures and the 3D index"
section_number: 2
pages: 3-5
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.828
latex_coverage_ratio: 0.981
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sec.results label="sec.results"}

## Index structures {#sub.index}

Consider two $r \times s$ matrices $\mathbf A$ and $\mathbf B$ with integer entries and a column vector $v \in \mathbb Z^r$, and let $\mathbf M=(\mathbf A | \mathbf B | v)$.

::: definition
[]{#def.strictindex label="def.strictindex"} (a) We say that $\mathbf M$ supports an *index structure* if the rank of $(\mathbf A | \mathbf B)$ is $r$ and for every $Q: \{1,\dots,s\}\to\{1,2,3\}$ there exists $(\alpha,\beta,\gamma) \in \mathbb Q^{3s}$ that satisfies $$\label{eq.index.structure}
\mathbf A \alpha+ \mathbf B \gamma= \nu, \qquad
\alpha+\beta+\gamma=(1,\dots,1)^T$$ and $Q(\alpha,\beta,\gamma) >0$. The latter means that for every $i=1,\dots,s$ the following inequalities are satisfied: $$\label{eq.index.ineq}
\begin{cases}
\alpha_i > 0 & \text{if} \quad Q(i)=1 \\
\beta_i > 0 & \text{if} \quad Q(i)=2 \\
\gamma_i > 0 & \text{if} \quad Q(i)=3 \\
\end{cases}$$ (b) We say that $\mathbf M$ supports a *strict index structure* if the rank of $(\mathbf A | \mathbf B)$ is $r$ and there exists $(\alpha,\beta,\gamma) \in
\mathbb Q_+^{3s}$ that satisfies [\[eq.index.structure\]](#eq.index.structure){reference-type="eqref" reference="eq.index.structure"}, where $\mathbb Q^+$ is the set of positive rational numbers.
:::

It is easy to see that if $\mathbf M$ supports a strict index structure, then it supports an index structure, but not conversely. As we will see in Section [\[sub.angle\]](#sub.angle){reference-type="ref" reference="sub.angle"}, ideal triangulations $\mathcal T$ give rise to matrices $\mathbf M$, and a strict index structure on $\mathbf M$ is a strict angle structure on $\mathcal T$. On the other hand, index structures are new and motivated by Theorem [\[thm.IMconv\]](#thm.IMconv){reference-type="ref" reference="thm.IMconv"} below.

The next definition discusses two actions on $\mathbf M$: an action of $\mathrm{GL}(r,\mathbb Z)$ on the left which allows for row operations on $\mathbf M$, and a cyclic action of order three at the pair of the $i$th columns of $(\mathbf A|\mathbf B)$.

::: definition
[]{#def.GLr label="def.GLr"} (a) There is a left action of $\mathrm{GL}(r,\mathbb Z)$ on $\mathbf M$, defined by $$P  \in \mathrm{GL}(r,\mathbb Z) \qquad \mathbf M=(\mathbf A|\mathbf B|v)
\qquad P \mathbf{M}=(P \mathbf A|P \mathbf B|P v)$$ An index structure on $\mathbf M$ is also an index structure on $P \mathbf M$. (b) There is a left action of $(\mathbb Z/3)^s$ on $\mathbf M$ acting on the $i$th columns $(a_i|b_i)$ of $(\mathbf A|\mathbf B)$ (and fixing all other columns) given by $$\label{eq.Z3M}
(a_i|b_i|v) \overset{S}{\mapsto} (-b_i | a_i -b_i|v-b_i)\,,$$ where $$\label{eq.defS}
S(a|b|v)=(-b|a-b|v-b)$$ satisfies $S^3=\mathrm{Id}$. We extend $S$ to act on an index structure $(\alpha,\beta,\gamma)$ of $\mathbf M$ by $$\label{eq.Z3angle}
(\alpha_i,\beta_i,\gamma_i) \overset{S}{\mapsto} (\beta_i,\gamma_i,\alpha_i)$$ and fixing all other coordinates of $(\alpha,\beta,\gamma)$. It is easy to see that if $(\alpha,\beta,\gamma)$ is an index structure on $\mathbf M$ and $S \in (\mathbb Z/3)^s$, then $S(\alpha,\beta,\gamma)$ is an index structure of $S \mathbf M$.
:::

::: definition
[]{#def.IM label="def.IM"} Given $\mathbf M$, and $m=(m_1,\dots,m_s), e=(e_1,\dots,e_s) 
\in \mathbb Z^s$ consider the sum $$\label{eq.IM}
I_{\mathbf M}(m,e)(q)=\sum_{k \in \mathbb Z^r}
q^{\frac{1}{2} v \cdot k}
\prod_{i=1}^s I_{\Delta}(m_i-b_i \cdot k, e_i+a_i \cdot k)$$
:::

::: theorem
[]{#thm.IMconv label="thm.IMconv"} $I_{\mathbf M}(m,e)(q) \in \mathbb Z((q^{1/2}))$ is convergent for all $m, e\in \mathbb Z^s$ if and only if $\mathbf M$ supports an index structure. In that case, $I_{\mathbf M}$ is $q$-holonomic in the variables $(m,e)$.
:::

::: remark
[]{#rem.WZ label="rem.WZ"} $q$-holonomicity in Theorem [\[thm.IMconv\]](#thm.IMconv){reference-type="ref" reference="thm.IMconv"} follows immediately from [@WZ]. Convergence is the main difficulty.
:::

::: remark
[]{#rem.nahm label="rem.nahm"} By definition, $I_{\mathbf M}$ is a generalized Nahm sum in the sense of [@GL2], where the summation is over a lattice.
:::

::: corollary
[]{#cor.convP label="cor.convP"} Applying Theorem [\[thm.IMconv\]](#thm.IMconv){reference-type="ref" reference="thm.IMconv"} to the case $r=1$, $s=3$, $\mathbf M=(\mathbf A| \mathbf B|v)=(1 \, 1 \, 1|0 \, 0 \, 0|2)$ and the strict index structure $2=\frac{2}{3}\cdot 1 + \frac{2}{3}\cdot 1 +
\frac{2}{3}\cdot 1$, it follows that the right hand side of the pentagon identity [\[eq.pentagon\]](#eq.pentagon){reference-type="eqref" reference="eq.pentagon"} is convergent in $\mathbb Z((q^{1/2}))$.
:::

The next remark discusses the invariance of the index under the actions of Definition [\[def.GLr\]](#def.GLr){reference-type="ref" reference="def.GLr"}.

::: remark
[]{#rem.GLr label="rem.GLr"} Fix $\mathbf M$ that supports an index structure. Then, for $P \in \mathrm{GL}(r,\mathbb Z)$ and $S \in (\mathbb Z/3)^s$, it follows that $P \mathbf M$ and $S \mathbf M$ also supports an index structure. In that case, Theorem [\[thm.IMconv\]](#thm.IMconv){reference-type="ref" reference="thm.IMconv"} implies that $I_{\mathbf M}$, $I_{P \mathbf M}$ and $I_{S \mathbf M}$ are all convergent. We claim that $$I_{P \mathbf M} = I_{\mathbf M}, \qquad I_{S \mathbf M} = I_{\mathbf M} \,.$$ The first equality follows by changing variables $k \mapsto P k$ in the definition of $I_{\mathbf M}$ given by [\[eq.IM\]](#eq.IM){reference-type="eqref" reference="eq.IM"}. The second equality follows from the fact that the tetrahedron index $I_{\Delta}$ satisfies Equation [\[eq.Z3\]](#eq.Z3){reference-type="eqref" reference="eq.Z3"}; this is shown in part (a) of Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"}.
:::

The next corollary follows easily from Theorem [\[thm.IMconv\]](#thm.IMconv){reference-type="ref" reference="thm.IMconv"} and the definition of an index structure on $(\mathbf A|0|v_0)$.

::: corollary
[]{#cor.Aconv label="cor.Aconv"} Fix an $r \times s$ matrix $\mathbf A$ with integer entries and columns $v_i$ for $i=1,\dots,s$, and let $v_0 \in \mathbb Z^r$, and let $\mathbf M=(\mathbf A|0|v_0)$. The following are equivalent:

-   $I_{\mathbf M}(q)$ converges.

-   $\mathrm{rk}(\mathbf A)=r$ and there exist $\alpha_i >0$ for $i=1,\dots,s$ such that $v_0=\sum_{i=1}^s \alpha_i v_i$.
:::

::: question
[]{#que.compare label="que.compare"} Compare the $q$-series $I_{(\mathbf A|0|v)}$ with the vector partition functions of Sturmfels [@Sturmfels] and Brion-Vergne [@BV], and the $q$-hypergeometric systems of equations of [@SST].
:::
