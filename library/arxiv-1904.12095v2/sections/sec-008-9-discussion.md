---
doc_id: arxiv-1904.12095v2
doc_title: "Veriﬁed computations for closed hyperbolic 3-manifolds"
section_id: sec-008-9-discussion
section_title: "Discussion"
section_number: 9
pages: 21-25
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
toc_source: outline
text_source: latex
latex_prose_ratio: 0.916
latex_coverage_ratio: 1.0
doc_brief: "Verified computations for closed hyperbolic 3-manifolds — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed 3-manifold using"
---
[]{#sec:discussion label="sec:discussion"}

Let $\mathcal{T}$ be a finite, orientable triangulation with $o$ vertices and $m$ edges. We have proven that $\mathcal{T}$ admits a hyperbolic structure if the checks in each step of the algorithm in Section [\[sec:algo\]](#sec:algo){reference-type="ref" reference="sec:algo"} pass. But are there hyperbolic structures which the algorithm cannot verify --- even as we increase the precision and give the algorithm better and better approximations of the edge lengths of the hyperbolic structure as input?

We conjecture that such hyperbolic structures are special and can always be avoided by a random perturbation. We state this in the following conjecture where "generic" means that a statement is true except for a closed measure zero set of hyperbolic structures on $\mathcal{T}$ (we will see later that a natural measure exists on the space of all hyperbolic structures in Theorem [\[thm:hypStructAreSubmanifold\]](#thm:hypStructAreSubmanifold){reference-type="ref" reference="thm:hypStructAreSubmanifold"}):

::: conjecture
[]{#conjecture:main label="conjecture:main"} Let $\mathcal{T}$ be a finite, orientable triangulation with $o$ vertices and $m$ edges admitting a hyperbolic structure. Then a generic hyperbolic structure on $\mathcal{T}$ gives rise to edge lengths $l_{e_1},\dots, l_{e_m}>0$ or equivalently edge parameters $\nu_{e_1},\dots,\nu_{e_m}\leq -1$ such that

1.  $M$ in [\[eqn:jacobian\]](#eqn:jacobian){reference-type="eqref" reference="eqn:jacobian"} has rank $m-3o$ and []{#subconjecture:Rank label="subconjecture:Rank"}

2.  any choice of $m-3o$ linearly independent rows from $M$ avoids gimbal lock. More precisely, for any partition $E(\mathcal{T})=E^\sim \cup E^=$ into $3o$ and $m-3o$ edges, we have that[]{#subconjecture:gimbalLock label="subconjecture:gimbalLock"}

    1.  the rows of $M$ corresponding to the edges in $E^=$ are linearly independent

    implies that

    1.  the derivative $Dg$ of the gimbal function in Definition [\[def:trigGimbalFunction\]](#def:trigGimbalFunction){reference-type="ref" reference="def:trigGimbalFunction"} is invertible.
:::

Note that if Part [\[subconjecture:gimbalLock\]](#subconjecture:gimbalLock){reference-type="eqref" reference="subconjecture:gimbalLock"} were false, the choice of the partition $E(\mathcal{T})=E^\sim\cup E^=$ made in Step [\[step:submatrix\]](#step:submatrix){reference-type="ref" reference="step:submatrix"} could be such that Step [\[step:intervalNewton\]](#step:intervalNewton){reference-type="ref" reference="step:intervalNewton"} passes but the algorithm fails later in Step [\[step:avoidGimbal\]](#step:avoidGimbal){reference-type="ref" reference="step:avoidGimbal"}.

::: remark
Numerically, we found that the converse of Part [\[subconjecture:gimbalLock\]](#subconjecture:gimbalLock){reference-type="eqref" reference="subconjecture:gimbalLock"} is not true, i.e., we found examples where the gimbal function is invertible even though the chosen rows of $M$ are linearly dependent.
:::

::: remark
Compare the conjecture to the ideal case where we do not know in general whether every cusped, finite volume hyperbolic 3-manifold has a geometric triangulation (see [@PetronioWeeks:partiallyFlatTrig; @LuoSchleimerTillmann:virtualGeometricTrig; @Goerner:DodecahedralGeometricTriangulation]).
:::

## The space of hyperbolic structures

Let $\mathcal{T}$ be a finite, orientable triangulation with $o$ vertices and $m$ edges admitting a hyperbolic structure. We are able to prove that the solution set of the edge equations has dimension $3o$. This is weaker than Part [\[subconjecture:Rank\]](#subconjecture:Rank){reference-type="eqref" reference="subconjecture:Rank"} of Conjecture [\[conjecture:main\]](#conjecture:main){reference-type="ref" reference="conjecture:main"} since it implies that the rank of $M$ is at most $m-3o$ (for example, $x^3=0$ yields a $0$-dimensional submanifold of the 1-dimensional $\mathbb R$, yet the Jacobian has rank $0$ at $0$ instead of the expected $1-0=1$).

Earlier, we defined a hyperbolic structure on $\mathcal{T}$ as a compatible assignment of an isometry class of finite simplices in $\mathbb H^3$ to each simpex in $\mathcal{T}$. The space of hyperbolic structures on $\mathcal{T}\!{}$ can be described in the following ways:

1.  $\mathrm{Sol}(\mathcal{T})\subset\mathbb R_{>0}^m$, the set of all tuples $(l_{e_1},\dots,l_{e_m})$ fulfilling the conditions of Theorem [\[thm:hypStruct\]](#thm:hypStruct){reference-type="ref" reference="thm:hypStruct"} (since the edge lengths of a hyperbolic structure yield a point in $\mathrm{Sol}(\mathcal{T})$ and determine the hyperbolic structure uniquely).

2.  The space of geodesic homeomorphisms $\mathcal{T}\to\mathcal{M}$ in a fixed homotopy class in $[\mathcal{T}\!{},\mathcal{M}]$ where $\mathcal{M}$ is a hyperbolic 3-manifold homeomorphic to $\mathcal{T}\!{}$. By Mostow rigidity, this yields all hyperbolic structures. By fixing the homotopy class, a hyperbolic structure gives a unique geodesic homeomorphism, instead of multiple related by the isometries of $\mathcal{M}$. []{#item:geodHomeo label="item:geodHomeo"}

3.  The space of all developing homeomorphisms, i.e., $\rho$-equivariant homeomorphisms $d:\tilde{\mathcal{T}}\to\mathbb H^3$ where $p$ is a fixed vertex of $\mathcal{T}\!{}$ and $\rho:\pi_1(\mathcal{T}\!{},p)\to\mathrm{PSL}_{2}(\mathbb C)$ is a fixed geometric representation. This gives the homeomorphism $\mathcal{T}\!{}\to\mathcal{M}$ in [\[item:geodHomeo\]](#item:geodHomeo){reference-type="eqref" reference="item:geodHomeo"} when letting $\mathcal{M}=\mathbb H^3/\Gamma$ where $\Gamma=\mathrm{Im}(\rho)$.

::: theorem
[]{#thm:hypStructAreSubmanifold label="thm:hypStructAreSubmanifold"} Let $\mathcal{T}$ be a finite, orientable triangulation with $o$ vertices and $m$ edges admitting a hyperbolic structure. The space $\mathrm{Sol}(\mathcal{T})$ of hyperbolic structures on $\mathcal{T}$ is a $3o$-dimensional smooth submanifold of  $\mathbb R_{>0}^m$, is (non-canonically) diffeomorphic to an open subset $U\subset \left(\mathbb H^3\right)^o$, and has a canonical measure induced from $\left(\mathbb H^3\right)^o$.
:::

::: proof
*Proof.* We call a $\rho$-equivariant geodesic map $d:\tilde{\mathcal{T}}\to\mathbb H^3$ a developing map.\
**Claim:** Fix a vertex $p$ of $\mathcal{T}\!{}$ and a geometric representation $\rho:\pi_1(\mathcal{T}\!{},p)\to\mathrm{PSL}_{2}(\mathbb C)$. Then developing maps are in 1-1 correspondence to $(\mathbb H^3)^o$.\
Pick a lift $\tilde{v_1},\dots, \tilde{v_o}$ in $\tilde{\mathcal{T}}\!{}$ of each vertex of $v_1,\dots,v_o$ of $\mathcal{T}\!{}$. By $\rho$-equivariance, the images of all vertices of $\tilde{\mathcal{T}}$ are determined by $(d(\tilde{v_1}), \dots, d(\tilde{v_o}))\in(\mathbb H^3)^o$. A geodesic map is determined uniquely by the image of all the vertices.\
**Claim:** Under the above assumptions, the homeomorphisms among the developing maps form an open subset $U\subset(\mathbb H^3)^o$. We have a bijection $l:U\to\mathrm{Sol}(\mathcal{T})$.\
By invariance of domain, a developing map is a homeomorphism if and only if it is an embedding. A developing map is an embedding if and only if the image of each simplex is positively oriented. The condition on a single simplex in $\tilde{\mathcal{T}}\!$ to be positively oriented is open in the four vertex positions of the simplex. As a function of $(x_1,\dots,x_o)\in (\mathbb H^3)^o$, each of these four vertex positions is given by some $m x_k$ where $m$ is a hyperbolic isometry in $\Gamma=\mathrm{Im}(\rho)$. Thus, the condition is also open in $(\mathbb H^3)^o$. By $\rho$-equivariance, it is sufficient to check this for one lift $\tilde{\Delta}$ of each of the finitely many simplices $\Delta$ of $\mathcal{T}\!{}$, so $U$ is open.\
**Claim:** The map $L=i\circ l: U\to\mathbb R^m_{>0}$ is smooth where $i: \mathrm{Sol}(\mathcal{T})\hookrightarrow \mathbb R^m_{>0}$ is the inclusion.\
The distance function $\mathbb H^3\times\mathbb H^3\to\mathbb R_{\geq 0}$ is smooth for all $(x,y)$ with $x\not= y$.\
**Claim:** The inverse $l^{-1}:\mathrm{Sol}(\mathcal{T})\to U$ is continuous.\
Fix a simplex $\tilde{\Delta}$ in $\tilde{\mathcal{T}}$ and $\sigma\in \mathbf{A}_4$. Given a point in $\mathrm{Sol}(\mathcal{T})$, let us consider the developing map $d':\tilde{\mathcal{T}}\to\mathbb H^3$ obtained by starting with $\tilde{\Delta}$ in $\sigma$-standard position (see Definition [\[def:standardPosSimplex\]](#def:standardPosSimplex){reference-type="ref" reference="def:standardPosSimplex"}) and developing simplex by simplex. Note that $d'$ is equivariant with respect to a conjugate but different representation $\rho':\pi_1(\mathcal{T}\!{}, p)\to\mathrm{PGL}_{2}(\mathbb C)$. In other words, there is a unique element $h\in\mathrm{PGL}_{2}(\mathbb C)$ such that $\rho(\gamma)=h\circ \rho'(\gamma)\circ h^{-1}$ for all $\gamma\in\pi_1(\mathcal{T}\!{}, p)$ and $d=h\circ d'$ is $\rho$-equivariant. We can compute $h$ as follows: fix $\gamma_1,\gamma_2,\gamma_3\in\pi_1(\mathcal{T}\!{},p)$ such that the attractive fixed points $p_i\in\partial \mathbb H^3$ of $\rho(\gamma_i)$ are distinct. Let $p'_i\in\partial\mathbb H^3$ be the attractive fixed points of $\rho'(\gamma_i)$. Then $h$ is the unique Moebius transformation with $p_i=h(p'_i)$. Note that the all $d'(\tilde{v_k})$ as well as all $\rho'(\gamma_i)$ and thus $h$ depend continuously on the point in $\mathrm{Sol}(\mathcal{T})$. Thus, $(d(\tilde{v_1}), \dots, d(\tilde{v_o}))\in U\subset (\mathbb H^3)^o$ depends continuously on the point in $\mathrm{Sol}(\mathcal{T})$.\
**Claim:** The differential $DL$ of $L: U\to\mathbb R^m_{>0}$ is injective at every point in $U$.\
Assume that $DL$ has non-trivial kernel. That is, there is a path $\gamma:(-1,1)\to U$ with $(d\gamma(t)/dt)_{|t=0}\not =0$ but $(d(L\circ\gamma)(t)/dt)_{|t=0}=0$. In other words, we have a 1-parameter family of developing maps $d:\tilde\mathcal{T}\to \mathbb H^3$ where at least one of the points $d(\tilde{v_k})$ is moving with non-zero velocity but the derivatives of all the edge lengths is zero. As we shall see, this cannot happen.\
From the edge lengths $(L\circ\gamma)(t)\in\mathrm{Sol}(\mathcal{T})$, we can construct a 1-parameter family of developing maps $d'$ as above. Since the derivatives of the lengths is zero, the vertices $d'(\tilde{v_k})$ all have velocity zero. It is not hard to see that the entries of the $h\in\mathrm{PGL}_{2}(\mathbb C)$ from above also have zero derivative. Thus, the points $d(\tilde{v_k})$ have zero velocity.\
**Claim:** The measure on $\mathrm{Sol}(\mathcal{T})$ induced from $\left(\mathbb H^3\right)^o$ is independent of the above choices.\
A different choice of lifts $\tilde{v_1},\dots,\tilde{v_o}$ of vertices corresponds to the action of $(\mathbb H^3)^o$ by an element in $\Gamma^o$ and thus does not change the induced measure. A different choice of $\rho':\pi_1(\mathcal{T}\!{},p)\to\mathrm{PGL}_{2}(\mathbb C)$ is conjugate to $\rho$ by an element $h\in\mathrm{PGL}_{2}(\mathbb C)$. The measure on $(\mathbb H^3)^o$ is invariant under the action of $h$. ◻
:::

## 1-vertex triangulations {#sec:singleVertexTrigs}

Consider a 1-vertex triangulation $\mathcal{T}$ admitting a hyperbolic structure. Let $p$ be the vertex of $\mathcal{T}$ and $\rho:\pi_1(\mathcal{T}\!{}, p)\to\mathrm{PSL}_{2}(\mathbb C)$ be a geometric representation. Note that each edge $e$ of $\mathcal{T}$ forms a loop in $\pi_1(\mathcal{T}\!{}, p)$ and denote by $F_e=\{x\in \mathbb CP^1 : x = \rho(e)(x)\}$ the set of the corresponding fixed points.

::: theorem
[]{#thm:singleVertexTriangulationGimbalLockCondition label="thm:singleVertexTriangulationGimbalLockCondition"} Let $E^\sim = \{e^\sim_1, e^\sim_2, e^\sim_3\}$ and $E^=$ be a partition of the edges of $\mathcal{T}\!{}$. Gimbal lock occurs for every hyperbolic structure on $\mathcal{T}$ if there are $i\not= j$ with $F_{e^\sim_i}=F_{e^\sim_j}$. Otherwise, gimbal lock is generically avoided.
:::

::: remark
It is imaginable that there is a 1-vertex triangulation such that $|\{F_e : e\in E(\mathcal{T})\}|=2$ and gimbal lock occurs for each choice of $E^\sim$ giving a counterexample to Conjecture [\[conjecture:main\]](#conjecture:main){reference-type="ref" reference="conjecture:main"}.
:::

<figure id="fig:edgeSingVertTrig">
<div class="center">

</div>
<figcaption>Edge in 1-vertex triangulation.<span id="fig:edgeSingVertTrig" label="fig:edgeSingVertTrig"></span></figcaption>
</figure>

::: proof
*Proof.* The edges $e^\sim_i$ become geodesics with a potential kink at the image of $p$ in $\mathcal{M}$. Let $\overrightarrow{a}_i^0$ and $\overrightarrow{a}_i^1$ be the directions (of unit length) in which the two ends of $e^\sim_i$ approach $d(p)\in\mathbb H^3$ in the developing embedding $d:\tilde{\mathcal{T}}\to\mathbb H^3$. We can identify the tangent space at $d(p)$ with Euclidean 3-space such that the gimbal matrix $m_\Gamma$ is the product of six rotations (the order depending on the choice of gimbal loop $\Gamma$) $$R_{T_1}^{\overrightarrow{a}_1^0},~R_{T_1}^{\overrightarrow{a}_1^1},~R_{T_2}^{\overrightarrow{a}_2^0},~R_{T_2}^{\overrightarrow{a}_2^1},~R_{T_3}^{\overrightarrow{a}_3^0},~\mbox{and}~R_{T_3}^{\overrightarrow{a}_3^1}$$ where $R_\omega^{\overrightarrow{v}}\in\mathrm{SO}_{3}$ denotes the rotation about $\overrightarrow{v}$ by angle $\omega$. Let $\overrightarrow{a}_{i,k}^j$ denote the $k$-th component of $\overrightarrow{a}_i^j$. At the point where all $T_i=2\pi$, we have $$\frac{\partial m_\Gamma}{\partial T_i} = \frac{R_{T_i}^{\overrightarrow{a}_i^0}}{\partial T_i} + \frac{R_{T_i}^{\overrightarrow{a}_i^1}}{\partial T_i}=
\left(\begin{array}{ccc}
0 & -\overrightarrow{a}_{i,2}^0 & \overrightarrow{a}_{i,1}^0 \\
\overrightarrow{a}_{i,2}^0 & 0 & -\overrightarrow{a}_{i,0}^0 \\
-\overrightarrow{a}_{i,1}^0 & \overrightarrow{a}_{i,0}^0 & 0
\end{array}\right) +
\left(\begin{array}{ccc}
0 & -\overrightarrow{a}_{i,2}^1 & \overrightarrow{a}_{i,1}^1 \\
\overrightarrow{a}_{i,2}^1 & 0 & -\overrightarrow{a}_{i,0}^1 \\
-\overrightarrow{a}_{i,1}^1 & \overrightarrow{a}_{i,0}^1 & 0
\end{array}\right),$$ $$\mbox{so}~\quad \frac{\partial g}{\partial T_i} = \left(-\big(\overrightarrow{a}_{i,2}^0+\overrightarrow{a}_{i,2}^1\big), \big(\overrightarrow{a}_{i,1}^0+\overrightarrow{a}_{i,1}^1\big), -\big(\overrightarrow{a}_{i,0}^0+\overrightarrow{a}_{i,0}^1\big)\right)=\left(-\overline{a}_{i,2}, \overline{a}_{i,1}, -\overline{a}_{i,0}\right)$$ where $\overline{a}_{i}=\overrightarrow{a}_i^0+\overrightarrow{a}_i^1.$ Thus, $Dg=\left(\partial g/\partial T_1, \partial g/\partial T_2, \partial g/\partial T_3\right)$ is invertible if $\overline{a}_1, \overline{a}_2,$ and $\overline{a}_3$ are linearly independent. Figure [1](#fig:edgeSingVertTrig){reference-type="ref" reference="fig:edgeSingVertTrig"} shows that $\overline{a}_i$ is pointing from $d(p)$ to the geodesic $g_i$ spanned by $F_{e^\sim_i}$ (respectively pointing to $F_{e^\sim_i}$ if $|F_{e^\sim_i}|=1$) and $\overline{a}_i=0$ if it lies on that geodesic.\
**Claim:** Given a point $x\in\mathbb H^3$, consider the directions $\overline{a}_i$ from $x$ to the point on $g_i$ closest to $x$ (respectively pointing to $F_{e^\sim_i}$ if $|F_{e^\sim_i}|=1$). The set $V$ of $x$ where these directions lie in a plane is closed and has measure zero if all sets $F_{e^\sim_i}$ are distinct. Otherwise $V=\mathbb H^3$.\
Let $f:\mathbb H^3\setminus \cup_i g_i\to \mathbb R, x\mapsto \omega(\overline{a}_1,\overline{a}_2,\overline{a}_3)$ where $\omega$ is the volume form on $\mathbb H^3$. Since $\overline{a}_i$ is the Hodge dual to the gradient of the distance of $x$ to $g_i$, $f$ is analytic. It is not hard to see that there is some $x$ with $f(x)\not = 0$ as long as no two $F_{e^\sim_i}$ and $F_{e^\sim_j}$ are equal. Thus $f^{-1}(0)$ and $V=f^{-1}(0)\cup \cup_i g_i$ have measure zero. ◻
:::
