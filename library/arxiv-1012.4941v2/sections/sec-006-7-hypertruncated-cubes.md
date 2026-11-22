---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-006-7-hypertruncated-cubes
section_title: "Hypertruncated Cubes"
section_number: 7
pages: 16-18
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.959
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linear and integer programming problems."
---
[]{#sec:hypertruncated label="sec:hypertruncated"} In this section we will construct a specific class of highly symmetric convex polytopes among which one can find examples of rather high Gomory-Chvátal rank. The motivation for this construction is rooted in the systematic study of Gomory-Chvátal cuts and cutting-plane proof systems. Pokutta and Stauffer [@PokuttaStauffer10] propose a new method for computing lower bounds on the Gomory-Chvátal rank for polytopes contained in the $0/1$-cube, and the polytopes constructed here provide examples which asymptotically almost attain the bounds obtained. The subsequent section on computational experiments also contains results about these polytopes.

Our construction starts out with the unit cube $C=[0,1]^n$. Intersecting $C$ with the hyperplane defined by $\sum x_i=r$ for $r\in\{2,3,\dots,n-1\}$ gives the hypersimplex $\Delta(r,n)$ which already appeared in Example [\[exmp:core\]](#exmp:core){reference-type="ref" reference="exmp:core"}. Here we are interested in the *$(r,n)$-truncated cube* $C' = \{x\in [0,1]^n\,|\,\sum x_i\le r\}$. We make one more modification to the cube $C$ by defining the polytope $$\label{eq:hypertruncated}
  C'' \ = \ \mathop{\mathrm{conv}}(C'\cup\lambda\mathbbm{1}) \quad \text{for $\lambda>r/n$}$$ which we call the *$(r,n;\lambda)$-hypertruncated cube*. Notice that the full group $\mathop{\mathrm{Sym}}(n)$ acts on the cube $C$ as well as on the truncated cube $C'$ as well as on the hypertruncated cube $C''$. Hence our algorithms above can be applied. Our next goal is to describe the vertices and the facets of $C''$.

::: proposition
Let $n\ge 2$, $r\in\{2,3,\dots,n-1\}$, and $r/n<\lambda<1$. The vertices of the $(r,n;\lambda)$-hypertruncated cube $C''$ are $$e_S \quad \text{for all $S\subset[n]$ with $\#S\le r$} \qquad \text{and} \qquad
  \lambda\mathbbm{1}\, .$$
:::

::: proof
*Proof.* The points $e_S$, for $S\subset[n]$ and $\#S\le r$, are the vertices of the $(r,n)$-truncated cube $C'$. They are also vertices of $C''$. Since $n\lambda$ exceeds $r$, the hyperplane $\sum x_i=n\lambda$ does not separate $C''$, and its intersection with $C''$ only contains the point $\lambda\mathbbm{1}$. Hence the latter is a vertex, too. Looking at the defining Equation [\[eq:hypertruncated\]](#eq:hypertruncated){reference-type="eqref" reference="eq:hypertruncated"} shows that there cannot be any other vertices. ◻
:::

Of course, the vertices determine the facets completely. In this case, it is particularly easy to read off the facets of $C''$ by looking at the facets of $C'$ and analyzing what changes in case the point $\lambda\mathbbm{1}$ is added as a generator. This proves the claim in [@PokuttaStauffer10 Remark 3.3].

::: proposition
[]{#prop:hypertruncated_facets label="prop:hypertruncated_facets"} Let $n\ge 2$, $r\in\{2,3,\dots,n-1\}$, and $\lambda>r/n$. The facets of the $(r,n;\lambda)$-hypertruncated cube $C''$ are $$\begin{aligned}
    & x_i \ \ge \ 0 \ , \quad x_i \ \le \ 1 \label{eq:hypertruncated_facets:cube}\\
    & \bigl(1-n+\frac{r}{\lambda}\bigr) x_i + \sum_{k\ne i} x_k \ \ge \ r  \label{eq:hypertruncated_facets:deletion}\\
    & \bigl(1-r+\lambda(n-1)\bigr) x_i + (1-\lambda) \sum_{k\ne i} x_k \ \le \
    \lambda(n-r) \label{eq:hypertruncated_facets:contraction}
  
\end{aligned}$$ for $i\in[n]$. In particular, $C''$ has precisely $4n$ facets.
:::

::: proof
*Proof.* The facets of type [\[eq:hypertruncated_facets:cube\]](#eq:hypertruncated_facets:cube){reference-type="eqref" reference="eq:hypertruncated_facets:cube"} are the facets of the unit cube $C$. Together with the truncating inequality $\sum x_i\le r$ they also form the facets of the truncated cube $C'$. The remaining facets of $C''$ are the facets through the vertex $\lambda\mathbbm{1}$. Each of them is the convex hull of $\lambda\mathbbm{1}$ and a ridge of $C'$ contained in the truncating facet. A *ridge* is a face of codimension $2$, that is, a facet of a facet. As pointed out above the truncating facet is the hypersimplex $\Delta(r,n)$. Its facets arise from the intersection with the cube facets. A hypersimplex facet of type $\{x\in\Delta(r,n)\,|\,x_i=0\}$ is a *deletion facet*, and a hypersimplex facet of type $\{x\in\Delta(r,n)\,|\,x_i=1\}$ is a *contraction facet*. The $n-1$ points $r e_k$ for $k\ne i$ span an $(n-2)$-dimensional affine subspace ${\mathscr{A}}$ containing the $i$-th deletion facet. However, these points are not contained in $\Delta(r,n)$. Looking for an affine hyperplane containing ${\mathscr{A}}$ and $\lambda\mathbbm{1}$ results in a rank-$1$ system of linear equations. This way we obtain the $n$ linear inequalities of type [\[eq:hypertruncated_facets:deletion\]](#eq:hypertruncated_facets:deletion){reference-type="eqref" reference="eq:hypertruncated_facets:deletion"}. Similarly, the affine span of a contraction ridge is generated by the $n-1$ points $e_i+(r-1)e_k$ for $k\ne i$. Via the same approach we arrive at the $n$ linear inequalities of type [\[eq:hypertruncated_facets:contraction\]](#eq:hypertruncated_facets:contraction){reference-type="eqref" reference="eq:hypertruncated_facets:contraction"}. ◻
:::

::: remark
[]{#rem:hypertruncated:parameters label="rem:hypertruncated:parameters"} Pokutta and Stauffer [@PokuttaStauffer10] show that the Gomory-Chvátal ranks of the $(r,n;\lambda)$-hypertruncated cubes for $r=\lfloor n/e\rfloor$, where $e=2.7172\ldots$ is Euler's constant, and $\lambda=(m-1)/m$ approach $n/e - o(1)$ as $m\in{\mathbb{N}}$ goes to infinity. In our experiments below we look at the case $r=\lfloor
  n/e\rfloor$ and $\lambda=1/2$, that is, $m=2$.
:::
