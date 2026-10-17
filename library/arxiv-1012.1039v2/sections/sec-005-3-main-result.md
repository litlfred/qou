---
doc_id: arxiv-1012.1039v2
doc_title: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS"
section_id: sec-005-3-main-result
section_title: "Main result"
section_number: 3
pages: 8-14
source_pdf: 1012.1039v2.pdf
source_sha256: acb2575050db419d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.99
doc_brief: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS — Let M be a hyperbolic n–manifold whose cusps have torus cross- sections."
---
[]{#s:main label="s:main"} In this section we prove the main result, Theorem [\[t:volumedecreases\]](#t:volumedecreases){reference-type="ref" reference="t:volumedecreases"}. The strategy is to modify an efficient relative fundamental cycle for $(M,\partial M)$ to a fundamental cycle on the filling, without increasing norm by too much.

::: lemma
[]{#l:rational label="l:rational"} Let $X$ be a topological space. Let $c\in {C_n}(X;\mathbb{R})$ be homologous to a rational chain, and let $\epsilon>0$. Then there is some $c'\in
  C_n(X;\mathbb{Q})$ homologous to $c$ so that $\|c'-c\|_1<\epsilon$. If $c$ is symmetric, $c'$ can be chosen to be symmetric.
:::

::: proof
*Proof.* By assumption, there is some $f\in C_{n+1}(X;\mathbb{R})$ so that $c+\partial f \in C_n(X;\mathbb{Q})$. Since $C_{n+1}(X;\mathbb{Q})$ is dense in $C_{n+1}(X;\mathbb{R})$, there is some $f'\in C_{n+1}(X;\mathbb{Q})$ with $\|f-f'\|<\frac{\epsilon}{n+2}$. The chain $c'=c+\partial(f-f')$ satisfies $\|c'-c\|<\epsilon$, since $\|\partial_{n+1}\|=n+2$.

If $c$ is symmetric, we can take $f$ and $f'$ to be symmetric in the above argument, and it will follow that $c'$ is symmetric. ◻
:::

::: definition
[]{#d:small label="d:small"} Let $\mathcal{T}$ be a finite triangulation of a space $X$, and let $\mathcal{T}'$ be its barycentric subdivision. The *(closed) star neighborhood* of a simplex $\tau$ of $\mathcal{T}$ is the union of those simplices of the subdivision $\mathcal{T}'$ intersecting $\tau$. A point in the interior of an $n$--simplex of $X$ lies in at least one closed star neighborhood of a vertex, and in at most $n+1$ such closed stars.

The *open star neighborhood* of a simplex is the interior of its star neighborhood. (So the open star neighborhood of a simplex does not include its proper faces.) The open star neighborhoods of the simplices of $\mathcal{T}$ form an open cover of $X$.

Let $\sigma\colon\thinspace\Delta^n\to X$ be a singular simplex. We say $\sigma$ is *small* with respect to $\mathcal{T}$ if the image of $\sigma$ is contained entirely in the open star of some vertex of $\mathcal{T}'$.

A singular chain will be called *small* if all its simplices are small.
:::

Given an order on the vertices of $\mathcal{T}$ there is a canonical way to homotope a small chain to an affine chain, as we describe in the next lemma.

::: lemma
[]{#l:affine label="l:affine"} Let $X$ be a space with a (combinatorial) triangulation $\mathcal{T}$, and let $<_\mathcal{T}$ be a total order on the vertices of $\mathcal{T}$. Canonically associated to any small singular simplex $\sigma\colon\thinspace\Delta^n\to X$ are

1.  a "straightened" affine simplex $a(\sigma)$, and

2.  a homotopy $f_t(\sigma)$ so that $f_0(\sigma)=\sigma$ and $f_1(\sigma)=a(\sigma)$,

so that if $F$ is a face of $\Delta^n$, then $a(\sigma|F)=a(\sigma)|F$ and $f_t(\sigma|F)=f_t(\sigma)|F$. (In other words, homotopies on a face depend only on that face, so a cycle remains a cycle throughout the homotopy.) Moreover, if $\sigma$ is invariant under precomposition with an affine map $\tau$, so are $a(\sigma)$ and $f_t(\sigma)$.
:::

::: proof
*Proof.* The idea is illustrated quite well by the figure given in the proof of Proposition 6.5.1 in Thurston's notes [@Th]. We give a little more detail. (The figure given there is not of a combinatorial triangulation. In that case a total order on the "corners" of the simplices must be given, rather than on the vertices. We avoid this complication here by assuming a combinatorial triangulation.)

We begin by defining the straightening $a(\sigma)$. For $x\in X$ define $n(x)$ to be the least vertex $v$ of $\mathcal{T}$ so that $x$ is in the closed star neighborhood of $v$. Let $\{v_0,\ldots,v_n\}$ be the vertices of the standard simplex $\Delta^n$. Since $\sigma$ is small, the image of $\sigma$ lies in the open star neighborhood of some simplex $\tau$ of $\mathcal{T}$. (In fact there may be several choices for $\tau$, but the maps $a(\sigma)$ and $f_t(\sigma)$ we define will not depend on the choice.) It follows that $n(\sigma(v_i))$ is a vertex of $\tau$ for each $i$. We define $a(\sigma)(v_i) = n(\sigma(v_i))$ and then extend to an affine map $a(\sigma)\colon\thinspace\Delta^n\to \tau$. It is clear that if $F$ is a face of $\Delta^n$ we have $a(\sigma|F) = a(\sigma)|F$.

We now must define the homotopies $f_t(\sigma)$. For each $x\in
  \Delta^n$, we let $\tau(x)$ be the unique simplex of $\mathcal{T}$ so that

1.  []{#containsx label="containsx"} $\sigma(x)\in \tau(x)$, and

2.  $\tau(x)$ has minimal dimension subject to [\[containsx\]](#containsx){reference-type="eqref" reference="containsx"}.

Since $\tau(x)$ lies in the open star neighborhood of $\tau$, the simplex $\tau$ is a face of $\tau(x)$. Thus both $\sigma(x)$ and $a(\sigma)(x)$ lie in $\tau(x)$. Convex combination is well-defined for points in the same simplex, so we may take, for $t\in [0,1]$, $$f_t(\sigma)(x) = (1-t)\sigma(x) + t\, a(\sigma)(x).$$ The reader may check that $f_t$ is well-defined, continuous, and satisfies the property $f_t(\sigma|F)=f_t(\sigma)|F$ for each face $F$ of $\Delta^n$.

Finally, we note that if $\tau$ is some affine map from $\Delta^n$ to itself so that $\sigma\circ \tau = \sigma$, then $a(\sigma\circ\tau) = a(\sigma)$ and therefore $f_t(\sigma\circ\tau)
  = f_t(\sigma)$ for all $t$. ◻
:::

::: lemma
[]{#l:simplicial label="l:simplicial"} Let $N$ be a manifold, and let $\mathcal{T}$ be a triangulation of $\partial N$. If $c\in {C_k}(N; \mathbb{R})$ is a relative singular cycle in $(N,\partial N)$ so that $\partial c$ is small with respect to $\mathcal{T}$, then $c$ is (relatively) homologous to $c'$ with $\|c'\|_1\leq \|c\|_1$ and $\partial c'$ an affine chain. If $c$ was symmetric, then so is $c'$.
:::

::: proof
*Proof.* The chain $c$ is a finite linear combination $c = \sum_{i=1}^{m'}\lambda_i\sigma_i$ of singular simplices $\sigma_i\colon\thinspace\Delta^k\to N$. The idea is to "preassemble" the simplices to get a map $\phi\colon\thinspace K_c \to N$ from a certain CW complex $K_c$, so that $c$ is $\phi_\sharp$ of a linear combination of characteristic maps. We can use Lemma [\[l:affine\]](#l:affine){reference-type="ref" reference="l:affine"} to homotope the "boundary" of $K_c$ to a simplicial map, and then apply the homotopy extension property of CW pairs.

More precisely, let $J = \{1,\ldots m'\}/\sim$, where $i\sim j$ if $\sigma_i = \sigma_j\circ q$ for some permutation $q$. We define $$\label{kcdef}
    K_c = \left( \coprod_{[i]\in J} \Delta^k_{[i]} \right)/\sim$$ where $x_1\sim x_2$ whenever there are $(k-1)$--dimensional faces $F_1\subset \Delta^k_{[i_1]}$ and $F_2\subset \Delta^k_{[i_2]}$ satisfying

1.  $x_j\in F_i$ for $j\in \{1,2\}$, and

2.  there is an affine map $\tau\colon\thinspace F_1\to F_2$ so that $\tau(x_1)
        = x_2$ and $\sigma_{i_1}|F_1 = \sigma_{i_2}\circ\tau$.

That is, if two singular simplices agree on a codimension $1$ face, we glue the corresponding faces together in $K_c$. Moreover, if a codimension $1$ face is unchanged by precomposing with some isometry, we identify the face to itself by the corresponding symmetry. We thus obtain a CW complex $K_c$ and a map $\phi\colon\thinspace
  K_c\to N$ given by $\phi(x) = \sigma_{i}(x)$ where $x\in
  \Delta^k_{[i]}$. In the complex $K_c$ we can canonically build a chain $\tilde{c}$ made up of "characteristic maps" $\Delta^k_{[i]}\to K_c$ so that $$c = \phi_\sharp(\tilde{c}).$$ If $c$ was symmetric, then so is $\tilde{c}$.

The boundary $\partial\tilde{c}$ is supported in some minimal subcomplex of $K_c$, which we'll refer to as $\partial K_c$. Because $c$ is a relative cycle, the map $\phi$ described in the last paragraph is really a map of pairs $$\phi \colon\thinspace(K_c,\partial K_c)\to (N,\partial N) .$$

After fixing some total order on the simplices of $\mathcal{T}$, Lemma [\[l:affine\]](#l:affine){reference-type="ref" reference="l:affine"} gives a homotopy in $\partial N$ of $\phi|\partial K_c$ to a "simplicial" map $\psi$; this map is simplicial in the sense that if $F$ is any face of one of the simplices $\Delta^k_{[i]}$ used to define $K_c$, and if $\iota_F$ is the inclusion map, then $\phi\circ \iota_F$ is affine, with image in a single simplex of $\mathcal{T}$.

By the homotopy extension property of CW pairs, the homotopy from $\phi|\partial K_c$ to $\psi$ can be extended to all of $K_c$. Let $$\Phi_t \colon\thinspace K_c \to N\mbox{, }t\in[0,1]$$ be this homotopy, with $\Phi_0 = \phi$. The chain $$c' = (\Phi_1)_\sharp(\tilde{c})$$ has all the properties we want. ◻
:::

We need to show that tori can be triangulated so that every simplex of diameter much smaller than the injectivity radius is small. Say that a triangulation of a torus is *$K$--fat* if every singular simplex of diameter less than $K$ is small with respect to that triangulation.

::: lemma
[]{#l:fattori label="l:fattori"} For each $d\geq 1$ there is a constant $0<K_d<1$ so that every flat torus of dimension $d$ with injectivity radius $R$ has a $(K_dR)$-fat triangulation with $t_d = 2^d d!$ simplices.
:::

::: proof
*Proof.* Let $T$ be a flat $d$--torus, which we can think of as $\mathbb{R}^d/\Lambda$, where $\Lambda$ is some rank $d$ lattice. Every such lattice has a Lovász--reduced basis [@LLL82] $\mathcal{B} = \{\mathbf{v}_1,\ldots,\mathbf{v}_d\}$. For $k\in \{1,\ldots,d\}$ define $\theta_k$ to be the angle made by $v_k$ with the subspace of $\mathbb{R}^d$ spanned by the rest of the basis. Babai [@Babai86] showed that, for all k, $$\sin(\theta_k)\geq\left(\frac{\sqrt{2}}{3}\right)^d.$$

Any basis $\mathcal{B}$ of $\Lambda$ gives rise in a canonical way to a triangulation $\mathcal{T}_{\mathcal{B}}$ of $T$ with $t_d$ simplices given by the first barycentric subdivision of the parallelepiped spanned by $\mathcal{B}$.

Let $V$ be the set of all ordered bases of lattices in $\mathbb{R}^d$, topologized as a subset of $\mathbb{R}^{d^2}$, and let $F\colon\thinspace V\to \mathbb{R}_+$ be the function which sends $\mathcal{B}$ to the least real $k$ so that $\mathcal{T}_{\mathcal{B}}$ is $k$--fat. The number $F(\mathcal{B})$ is also the least number $k$ so that triangulation of $\mathbb{R}^d$ covering $T_{\mathcal{B}}$ is $k$--fat. We note the following useful properties of $F$:

1.  $F$ is continuous and positive everywhere on $V$.

2.  []{#scale label="scale"} If $\lambda\in \mathbb{R}_+$ and $\mathcal{B}\in V$, then $F(\lambda \mathcal{B}) = \lambda F(\mathcal{B})$.

3.  []{#squash label="squash"} If there is a length-decreasing map from $\mathcal{B}$ to $\mathcal{B'}$ then $F(\mathcal{B})\geq F(\mathcal{B}')$.

Let $U\subset V$ be the set of bases consisting of unit vectors, any two of which make an angle $\theta$ with $\sin(\theta)\geq
  \left(\frac{\sqrt{2}}{3}\right)^d$. Since $U$ is compact, $F$ takes some minimum, positive value $L$ on $U$. We will show that every torus of injectivity radius $\geq 1/2$ has a triangulation which is $L$--fat. Linearity of $F$ (property [\[scale\]](#scale){reference-type="eqref" reference="scale"} above) then implies the lemma for $K_d = 2L$.

Let $T=\mathbb{R}^d/\Lambda$ be a torus of injectivity radius at least $1/2$. A Lovász-reduced basis $\mathcal{B}=\{\mathbf{v}_1,\ldots,\mathbf{v}_d\}$ for $\Lambda$ has all angles between basis vectors within $[\pi/3,2\pi/3]$, by Babai's result. Since the injectivity radius of $T$ is at least $1/2$, there is a distance-decreasing map from $\mathcal{B}$ to a basis in $U$, namely $$\mathcal{B}'=\left\{\frac{\mathbf{v}_1}{\|\mathbf{v}_1\|},\ldots,\frac{\mathbf{v}_d}{\|\mathbf{v}_d\|}\right\}.$$ Property [\[squash\]](#squash){reference-type="eqref" reference="squash"} above tells us that $F(\mathcal{B})\geq
  F(\mathcal{B}')\geq L$, so the triangulation $\mathcal{T}_{\mathcal{B}}$ is $L$--fat, and the proof of the lemma is completed. ◻
:::

::: lemma
[]{#l:thurstonlemma label="l:thurstonlemma"} For each $d\geq 1$ and each $s$ there is a constant $K(d,s)$ so that any null-homologous real singular $s$--cycle $z$ in a $d$--dimensional torus bounds a singular $(s+1)$--chain $c$ with $$\|c\|_1\leq K(d,s) \|z\|_1$$
:::

::: proof
*Proof.* We follow the proof of [@Th Proposition 6.5.1],which discusses the case $d=s=2$. Let $T$ be a $d$--dimensional torus, and let $z$ be an $s$--cycle. Since there are only finitely many singular simplices in $z$, their lifts to the universal cover $\mathbb{R}^d$ have diameters bounded by some $D>0$. Let $K_d$ be the constant from Lemma [\[l:fattori\]](#l:fattori){reference-type="ref" reference="l:fattori"}, and let $\tilde{T}\stackrel{\pi}{\longrightarrow} T$ be some cover of $T$ with injectivity radius bigger than $D/K_d$. By Lemma [\[l:fattori\]](#l:fattori){reference-type="ref" reference="l:fattori"}, there is a triangulation $\mathcal{T}$ of $\tilde{T}$ with $t_d$ simplices so that if $\tilde{\sigma}\colon\thinspace\Delta^s\to \tilde{T}$ is any lift of a singular simplex appearing in $z$, then $\tilde{\sigma}$ is small with respect to $\mathcal{T}$ (in the sense of Definition [\[d:small\]](#d:small){reference-type="ref" reference="d:small"}). The proof of Lemma [\[l:fattori\]](#l:fattori){reference-type="ref" reference="l:fattori"} shows that the combinatorics of this triangulation are independent of the particular chain $z$ and the cover $\tilde{T}$.

Write $C_*(X)$ for the real singular chain complex of $X$. There is a transfer map $$\mathrm{trans}\colon\thinspace C_*(T;\mathbb{R})\to C_*(\tilde{T};\mathbb{R})$$ which sends any singular simplex to the average of its lifts. The map $\mathrm{trans}$ is an isometric embedding with respect to the $l^1$ norm. The map $\pi_\sharp\colon\thinspace C_*(\tilde{T};\mathbb{R})\to C_*(T;\mathbb{R})$ induced by the covering is norm decreasing and $(\pi_\sharp\circ \mathrm{trans})$ is the identity map.

By the choice of $\tilde{T}$ and $\mathcal{T}$, the chain $\mathrm{trans}(z)$ is small. By Lemma [\[l:affine\]](#l:affine){reference-type="ref" reference="l:affine"}, the simplices of $\mathrm{trans}(z)$ can be homotoped simultaneously and consistently to the affine singular simplices making up the singular chain $a(\mathrm{trans}(z))$. Triangulating this homotopy in a standard way, we find that $\mathrm{trans}(z) - a(\mathrm{trans}(z))$ bounds an $(s+1)$--chain $c_1$ in $T$, so that $$\|c_1\|_1 \leq C_1\|z\|_1$$ for some constant $C_1$ depending on the dimension $s$ but otherwise independent of $z$. The space of affine real singular $s$--boundaries $B$ is finite dimensional, and only depends on the combinatorics of the triangulation $\mathcal{T}$.

The *affine filling norm* $\|b\|_{\mathrm{fill}}$ on $B$ is defined, for a boundary $b\in B$, to be the smallest $l^1$--norm of an affine $(s+1)$--chain bounded by $b$. Let $$C_2(d,s) = \sup \left\{\|b\|_{\mathrm{fill}}\mid b\in B \mbox{ and } \|b\|_1=1\right\},$$ and note that $C_2(d,s)$ only depends on the combinatorics of $\mathcal{T}$.

The boundary $a(\mathrm{trans}(z))$ bounds an $(s+1)$--chain $c_2$ in $T$ of $l^1$--norm at most $C_2(d,s)\|a(\mathrm{trans}(z))\|_1\leq C_2\|z\|_1$. Thus we have $$\mathrm{trans}(z) = \partial (c_1+c_2)$$ and $$z = \pi_\sharp (\partial (c_1+c_2) ) = \partial (\pi_\sharp(c_1 + c_2))$$ and $$\|\pi_\sharp(c_1 + c_2)\|_1\leq \|c_1+c_2\|_1 \leq \left(C_1(s)+ C_2(d,s)\right)\|z\|_1.$$ ◻
:::

We now prove the main theorem.

::: proof
*Proof of Theorem [\[t:volumedecreases\]](#t:volumedecreases){reference-type="ref" reference="t:volumedecreases"}.* We suppose that $M$ is a compact $n$--manifold with boundary a union of tori, so that the interior admits a complete hyperbolic metric of finite volume. We fix a $2\pi$--filling $M(T_1,\ldots,T_m)$. To prove the theorem we must show $$0< \|M(T_1,\ldots,T_m)\| \leq \frac{\mathrm{Vol}(V)}{v_n},$$ where $v_n$ is the volume of a regular ideal hyperbolic $n$--simplex.

The lower bound follows from [@MY] and is given above in Corollary [\[c:lowerbound\]](#c:lowerbound){reference-type="ref" reference="c:lowerbound"}.

We now establish the upper bound. The strategy is to first choose a symmetric representative $c_0$ for the (relative) fundamental class of $(M,\partial M)$ which is close to optimal, and then modify it to obtain a fundamental class $c_0'$ for $M(T_1,\ldots,T_m)$. If such a modification can be done in such a way that $|c_0'|_1$ is within some arbitrarily small constant of $\|M,\partial M\|$, then we will have shown: $$\|M(T_1,\ldots,T_m)\|\leq \|M,\partial M\|$$

The first step is to pass to a rational cycle. Let $\epsilon>0$. Let $c_0\in C_n(M;\mathbb{R})$ be a real symmetric singular relative cycle representing $[M,\partial M]$, and satisfying $$\|c_0\|_1<\|M,\partial M\|+\epsilon$$ By Lemma [\[l:rational\]](#l:rational){reference-type="ref" reference="l:rational"}, there is a symmetric rational singular relative cycle $c_1\in C_n(M;\mathbb{Q})$ homologous to $c_0$ with $\|c_1-c_0\|_1<\epsilon$.

We now pick a finite cover and triangulation of the boundary so that $\partial c_1$ lifts to a chain which is small with respect to that triangulation. Let $t_{n-1}
= 2^{n-1}(n-1)!$.

::: claim
[]{#claim:passtocover label="claim:passtocover"} We can choose a finite cover $\tilde{M}\stackrel{\pi}\longrightarrow M$ and a triangulation $\mathcal{T}$ of $\partial\tilde{M}$ satisfying the conditions:

1.  []{#degree label="degree"} The restriction of $\pi$ to any component of $\partial\tilde{M}$ has degree bigger than $m/\epsilon$, where $m$ is the number of cusps of $M$.

2.  []{#small label="small"} If $\mathrm{trans}\colon\thinspace C_*(M;\mathbb{R})\to
      C_*(\tilde{M};\mathbb{R})$ is the transfer map, then $\mathrm{trans}(\partial c_1)$ is small with respect to $\mathcal{T}$.

3.  []{#boundedcomb label="boundedcomb"} Each boundary component of $\tilde{M}$ is triangulated by $t_{n-1}$ $(n-1)$--simplices.
:::

::: proof
*Proof.* The compact manifold $M$ is homeomorphic to $\overline{M}$ as described in the introduction, a hyperbolic manifold minus a union of disjoint horospherical neighborhoods of its cusps. We identify $M$ with $\overline{M}$. Any simplex in the support of $\partial c_1$ therefore lifts to $\mathbb{H}^n$. Only finitely many such simplices occur, so there some number $r$ bounding the diameter of any such lift. Residual finiteness of $\pi_1M$ implies that we can pass to a finite cover $\tilde{M}\to M$ so that

1.  Every boundary component of $\tilde{M}$ has injectivity radius bigger than $r/K_{n-1}$, where $K_{n-1}$ is the constant from Lemma [\[l:fattori\]](#l:fattori){reference-type="ref" reference="l:fattori"}, and

2.  Every boundary component $N$ of $\tilde{M}$ has area at least $m/\epsilon$ times more than the area of the component of $\partial M$ covered by $N$.

Lemma [\[l:fattori\]](#l:fattori){reference-type="ref" reference="l:fattori"} implies that $\partial \tilde{M}$ admits an $r$--fat triangulation with $t_{n-1}$ $(n-1)$--simplices per component so that singular simplices lifted from $\partial c$ are all small respect to this triangulation. ◻
:::

Let $D$ be the degree of the cover coming from Claim [\[claim:passtocover\]](#claim:passtocover){reference-type="ref" reference="claim:passtocover"}. Since $c_1$ is rational and symmetric, $\mathrm{trans}(c_1)$ must also be rational and symmetric. In particular, $$\mathrm{trans}(c_1) = \frac{1}{q} c_2$$ for some integral symmetric chain $c_2\in C_*^S(\tilde{M};\mathbb{Z})$ and some positive integer $q$. Homologically $[c_2] =
\frac{q}{D}[\tilde{M},\partial\tilde{M}]$ in $H_{n}(\tilde{M},\partial\tilde{M};\mathbb{R})$. Since $\mathrm{trans}\colon\thinspace
C_*(M;\mathbb{R})\to C_*(\tilde{M};\mathbb{R})$ is isometric, $\|c_2\|_1 = q\|c_1\|_1$.

Since $\mathrm{trans}(\partial c_1)$ is small with respect to $\mathcal{T}$, the chain $\partial c_2$ is also small with respect to $\mathcal{T}$. Using Lemma [\[l:simplicial\]](#l:simplicial){reference-type="ref" reference="l:simplicial"}, we find a symmetric integral chain $c_3$ with $\|c_3\|_1\leq \|c_2\|_1$ so that $c_3$ is (relatively) homologous to $c_2$ and so that $\partial c_3$ is an affine chain, i.e., $\partial c_3\in C^{\mathcal{T}}_{n-1}(\partial
\tilde{M};\mathbb{Z})$.

Let $\tilde N_1,\ldots,\tilde N_p$ be the boundary components of $\tilde{M}$. We have $[c_3] = \frac{q}{D}[\tilde{M},\partial\tilde{M}]$ in $H_{n}(\tilde{M},\partial\tilde{M})$ and $[\partial c_3]
=\frac{q}{D}\sum_{i=1}^p[\tilde N_i]$ in $H_{n-1}(\partial\tilde M)$.

The cycle $\partial c_3$ is symmetric, affine and represents $\frac{q}{D}$ times the fundamental class of $\partial \tilde M$. By Lemma [\[l:vanish\]](#l:vanish){reference-type="ref" reference="l:vanish"}, $\partial c_3$ has no "degenerate" affine simplices in its support. It follows that $\partial c_3$ consists of exactly $\frac{q}{D}$ appropriately oriented copies of every $(n-1)$--simplex in $\mathcal{T}$.

Each of the $p$ boundary components of $\tilde{M}$ is triangulated with exactly $t_{n-1}$ simplices of dimension $n-1$. We therefore have $$\|\partial c_3\|_1 = p\, t_{n-1} \frac{q}{D}.$$ For each $i$ between $1$ and $n$, the $i$th boundary component of $M$ is covered by $p_i$ boundary components of $\tilde{M}$, so that $p=\sum_i p_i$. The degrees of these components are $d_{i1},\ldots,d_{ip_i}$, and $\sum_j p_{ij} = D$ for each $i$. Since each $d_{ij}\geq \frac{m}{\epsilon}$, we get $$D\geq p_i \frac{m}{\epsilon} \forall i,$$ which implies that $mD \geq p \frac{m}{\epsilon}$, and so $p\leq \epsilon D$. We therefore obtain $$\|\partial c_3\|_1 \leq \epsilon t_{n-1} q.$$

Projecting $c_3$ back down to $M$ gives a chain $c_4$ with $[c_4]=
q[ M,\partial M]$ in relative homology, and with $$\|c_4\|_1\leq \|c_3\|_1\leq\|c_2\|_1=
q\|c_1\|_1,$$ and with $$\|\partial c_4\|_1\leq \|\partial c_3\|_1 \leq
\epsilon t_{n-1} q.$$ Dividing by $q$ we obtain a fundamental cycle $c = \frac{1}{q}c_4$ for $[ M,\partial M]$ satisfying $\|c\|_1 \leq
\| M,\partial M\|+2\epsilon$ and $\|\partial c\|_1\leq t_{n-1}\epsilon$.

Now we will take this relative cycle $c$ for $[ M,\partial M]$, and modify it to an honest cycle in $M(T_1,\ldots,T_m)$. We start by pushing it forward from $M$ to $M(T_1,\ldots,T_m)$ by a map of pairs $$h\colon\thinspace(M,\partial M)\to
 (M(T_1,\ldots,T_m),Z),$$ where $Z$ is the singular set of $M(T_1,\ldots,T_m)$ and $h$ is the quotient map described in Definition [\[d:filling\]](#d:filling){reference-type="ref" reference="d:filling"}. (Here we are implicitly identifying $M$ with the space $\overline{M}$ described before Definition [\[d:filling\]](#d:filling){reference-type="ref" reference="d:filling"}.) Let $\partial h$ be $h$ restricted to $\partial M$. The chain $(\partial h)_\sharp(\partial c)$ is an $(n-1)$--cycle in $Z$. Lemma [\[l:thurstonlemma\]](#l:thurstonlemma){reference-type="ref" reference="l:thurstonlemma"} implies there is some $K$ depending only on $n$ so that $(\partial h)_\sharp(\partial c)$ can be filled in $Z$ with a $n$--chain $c'$ satisfying $\|c'\|_1\leq K \|(\partial h)_\sharp(\partial c)\|_1
\leq K t_{n-1}\epsilon$. It is easy to check that $h_\sharp c-c'$ is a fundamental cycle for $M(T_1,\ldots,T_m)$. Moreover, we have $$\|h_\sharp c-c'\|_1 \leq \| M,\partial M\|+(2+Kt_{n-1})\epsilon.$$ Letting $\epsilon$ tend to zero, we have established $$\|M(T_1,\ldots,T_m)\| \leq \| M,\partial M\|.$$ An application of the proportionality theorem for finite volume hyperbolic manifolds (Theorem [\[t:proportionality\]](#t:proportionality){reference-type="ref" reference="t:proportionality"}) gives the upper bound: $$\|M(T_1,\ldots,T_m)\| \leq \frac{\mathrm{Vol}(V)}{v_n}.$$ ◻
:::
