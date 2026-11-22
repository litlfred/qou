---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-004-5-searching-integer-layers-efficiently
section_title: "Searching Integer Layers Efficiently"
section_number: 5
pages: 11-13
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.957
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linear and integer programming problems."
---
[]{#sec:searching label="sec:searching"} The question remaining is how to test ILP-feasibility of a $c$-layer in an efficient way. Our key observation is that some optimal integral solution is close to the fixed space if the group of symmetries acts sufficiently transitive.

::: definition
Given a $c$-layer with center $z$, an integral point in the $c$-layer is a *core point* if it minimizes the distance to $z$.
:::

::: example
[]{#exmp:core label="exmp:core"} For the objective function $c=\mathbbm{1}$ and an integer $k=q n+r$ with $q\in{\mathbb{Z}}$ and $r\in\{0,1,\dots,n-1\}$, the set of core points in the $k$-th layer consists of all integer points with $r$ coefficients equal to $q+1$ and $n-r$ coefficients equal to $q$. In particular, the number of core points in this case equals $\tbinom{n}{r}$. These core points are the vertices of an $(r,n)$-hypersimplex, translated by the vector $q\mathbbm{1}$.
:::

For the algorithms below the geometric structure of the set of core points is very relevant. We therefore make a short digression: the *$(r,n)$-hypersimplex* $\Delta(r,n)$ is the $0/1$-polytope with vertices $$e_S \ = \ \sum_{i\in S} e_i \, ,$$ where $S$ ranges over all $r$-element subsets of $[n]$. The hypersimplices are highly regular structures, and this yields the following.

::: proposition
[]{#prop:mu-trs label="prop:mu-trs"} Let $\Gamma\le{\operatorname{GL}}_n{\mathbb{R}}$ be a linear group which acts $\mu$-transitively on the standard basis. Then $\Gamma$ acts transitively on the set of vertices of the $(r,n)$-hypersimplex for any $$r \in \{0,1,\dots,\mu\}\cup\{n-\mu,n-\mu+1,\dots,n\} \, .$$
:::

::: proof
*Proof.* By assumption $\Gamma$ acts transitively on the $r$-element subsets of $[n]$ for $r\le\mu$. Since $\Gamma$ is a linear group it thus acts transitively on the set of vertices of $\Delta(r,n)$. The corresponding claim for the remaining hypersimplices follows since $\Delta(r,n)$ is affinely isomorphic to $\Delta(n-r,n)$ via the map $x\mapsto \mathbbm{1}-x$. ◻
:::

Below we will apply the previous results in the special case where $\mu\ge\lfloor
n/2\rfloor$. Then the groups acts transitively on the sets of vertices of *all* hypersimplices.

::: lemma
[]{#lem:closer label="lem:closer"} Let $x\in P(A,b)$ be an LP-feasible point in the $k$-th $c$-layer, and let $\gamma\in\mathop{\mathrm{Sym}}(\operatorname{ILP}(A,b,c))$ with $\gamma x\ne x$. Then any point in the interior of the line segment $[x,\gamma x]$ is LP-feasible and closer to the center of the $k$-th $c$-layer than $x$.
:::

::: proof
*Proof.* Since $\gamma$ is an orthogonal linear map it preserves distances. The center $z$ of the $k$-th $c$-layer is fixed under $\gamma$, and this implies that $(x,z,\gamma x)$ is an isosceles triangle. We infer that $\left\lVert p-z\right\rVert<\left\lVert x-z\right\rVert$ for all points $p$ in the interior of $[x,\gamma x]$. Since $\gamma$ is an automorphism of the linear relaxation $\operatorname{LP}(A,b,c)$ the point $\gamma x$ is feasible, too. The feasible region is convex, and hence $p$ is feasible. ◻
:::

::: theorem
[]{#thm:core label="thm:core"} Suppose that $\Gamma\le\mathop{\mathrm{Sym}}(\operatorname{ILP}(A,b,\mathbbm{1}))$ acts $(\lfloor
  n/2\rfloor+1)$-transitively on the standard basis of ${\mathbb{R}}^n$, and $n\ge 2$. Then either each core point in the $k$-th $\mathbbm{1}$-layer is feasible or $H_{\mathbbm{1},k}$ does not contain any feasible point.
:::

::: proof
*Proof.* Let $x$ be a feasible integer point in the $k$-th $\mathbbm{1}$-layer which is not a core point. We will show that there is another feasible integer point which is closer to the center, and this will prove the claim.

Due to the invariance of ${\mathbb{Z}}^n$ under translation by integer vectors we may assume that $k\in\{0,1,\dots,n-1\}$. Since $x$ is not a core point, in particular, it is not the center of the $k$-th layer. Hence $x$ is not contained in the fixed space ${\mathbb{R}}\mathbbm{1}$, which means that not all coordinates of $x$ are the same. We split the set $[n]$ of coordinate directions into two subsets by considering $$\left\{i\vphantom{\text{$x_i$ is even}}\,\right.\left|\,\vphantom{i}\text{$x_i$ is even}\right\} \quad \text{and} \quad \left\{i\vphantom{\text{$x_i$ is odd}}\,\right.\left|\,\vphantom{i}\text{$x_i$ is odd}\right\} \, .$$ Then one of the sets --- denoted by $I$ --- contains at least $\lfloor (n+1)/2\rfloor$ elements, while the other set $J$ has at most $\lfloor n/2\rfloor$ elements. We will employ the $\lfloor n/2\rfloor$-transitivity of the automorphism group to control $J$, and the additional degree of freedom to produce two distinct feasible integer points. We distinguish two cases.

1.  Suppose that $x$ has two different coordinates, say $x_u$ and $x_v$, which are in the same congruence class modulo two. That is, the set $\{u,v\}$ is contained in either $I$ or $J$. Observe that this condition is satisfied whenever $x$ has at least three pairwise distinct coordinates. Due to the $(\lfloor n/2\rfloor+1)$-transitivity of $\Gamma$ there is an automorphism $\gamma\in\Gamma$ which leaves $J$ invariant and which maps $u$ to $v$. Since $J$ is invariant, its complement $I=[n]\setminus J$ is invariant, too. Notice that we do not require the set $J$ to be non-empty (if $\{u,v\}\subseteq I$).

    Letting $x'=\gamma x$ we observe that $x_i$ and $x'_i$ are congruent modulo two for all $i\in[n]$. Since $x_u\ne x_v=x_{\gamma(u)}=x'_u$ we have $x\ne x'$, and hence $$y \ = \ \frac{1}{2}(x+x') \ = \ \frac{1}{2}(x+\gamma x)$$ is an integer point in the interval $[x,\gamma x]$.

2.  Otherwise the point $x$ has exactly two different coordinates $x_u$ and $x_v$, one of them being even, the other one odd. Without loss of generality, $x_i=x_u$ for all $i\in I$ and $x_j=x_v$ for all $j\in J$. Due to the transitivity of $\Gamma$ there is an automorphism $\gamma\in\Gamma$ with $\gamma e_u=e_v$. Then $x$ and $\gamma x$ are distinct points. Consider an interior point $$y \ = \ \lambda x + (1-\lambda)\gamma x \quad \text{for } 0<\lambda<1 \label{eq:y}$$ in the line segment $[x,\gamma x]$. We want to find a parameter $\lambda$ such that $y$ is integral. As $x$ has only two distinct coordinates the $i$-th coordinate of $y$ can attain the following values only: $$\begin{aligned}
          y_i \ &= \ \lambda x_u + (1-\lambda) x_u \ = \ x_u \quad \text{or} \label{eq:yi:uu}\\
          y_i \ &= \ \lambda x_v + (1-\lambda) x_v \ = \ x_v \quad \text{or} \label{eq:yi:vv}\\
          y_i \ &= \ \lambda x_u + (1-\lambda) x_v \ = \ \lambda(x_u-x_v)+x_v \quad
          \text{or} \label{eq:yi:uv} \\
          y_i \ &= \ \lambda x_v + (1-\lambda) x_u \ = \ \lambda(x_v-x_u)+x_u \, . \label{eq:yi:vu}
        
    \end{aligned}$$ Since $x$ is integral coordinates of types [\[eq:yi:uu\]](#eq:yi:uu){reference-type="eqref" reference="eq:yi:uu"} and [\[eq:yi:vv\]](#eq:yi:vv){reference-type="eqref" reference="eq:yi:vv"} are integers for arbitrary parameters $\lambda\in(0,1)$. The coordinates of types [\[eq:yi:uv\]](#eq:yi:uv){reference-type="eqref" reference="eq:yi:uv"} and [\[eq:yi:vu\]](#eq:yi:vu){reference-type="eqref" reference="eq:yi:vu"} are integral if $\lambda\cdot|x_u-x_v|\in{\mathbb{Z}}$.

    We assumed that $x$ is contained in the $k$-th $\mathbbm{1}$-layer for some $k=0,1,\dots,n-1$ and that it is not a core point. In Example [\[exmp:core\]](#exmp:core){reference-type="ref" reference="exmp:core"} it has been observed that the core points in these layers are the vertices of a translated hypersimplex. We learned that some coordinate difference $|x_i-x_k|$ must exceed one. Since all coefficients are equal to either $x_u$ or $x_v$ it follows that $|x_u-x_v|\ge 2$. We can now set $$\lambda \ = \ \frac{1}{|x_u-x_v|}$$ in the formula [\[eq:y\]](#eq:y){reference-type="eqref" reference="eq:y"}.

In both cases we obtain an integral point $y$ in the interior of the interval $[x,\gamma
  x]$. By Lemma [\[lem:closer\]](#lem:closer){reference-type="ref" reference="lem:closer"}, such a point is always closer to the center than $x$. This shows that there exists a feasible core point in the same layer as $x$. Applying Proposition [\[prop:mu-trs\]](#prop:mu-trs){reference-type="ref" reference="prop:mu-trs"} with $\mu=\lfloor n/2\rfloor+1$ yields that then *each* core point must be feasible. ◻
:::

Now Algorithm [\[algo:reduction_to_layers\]](#algo:reduction_to_layers){reference-type="ref" reference="algo:reduction_to_layers"} can be modified in Step [\[step:reduction_to_layers:feasibility\]](#step:reduction_to_layers:feasibility){reference-type="ref" reference="step:reduction_to_layers:feasibility"} to check a single core point per layer for feasibility, provided that the group of automorphisms of the ILP acts at least $(\lfloor
n/2\rfloor+1)$-transitively. This is our *Core Point Algorithm* [\[algo:core_point\]](#algo:core_point){reference-type="ref" reference="algo:core_point"}.

::: algorithm
let $z=\zeta\mathbbm{1}$ be a symmetric optimal solution of the LP relaxation $\operatorname{LP}(A,b,\mathbbm{1})$ $d\leftarrow \lfloor n\zeta\rfloor-n\lfloor\zeta\rfloor$
:::

::: corollary
[]{#cor:core_point label="cor:core_point"} For given $A$ and $b$ such that $\mathop{\mathrm{Sym}}(\operatorname{ILP}(A,b,\mathbbm{1}))$ acts $(\lfloor
  n/2\rfloor+1)$-transitively on the standard basis the Core Point Algorithm [\[algo:core_point\]](#algo:core_point){reference-type="ref" reference="algo:core_point"} solves the integer linear program $\operatorname{ILP}(A,b,\mathbbm{1})$ in $O(mn^2)$ time.
:::

::: proof
*Proof.* The correctness follows from Theorems [\[thm:reduction_to_layers\]](#thm:reduction_to_layers){reference-type="ref" reference="thm:reduction_to_layers"} and [\[thm:core\]](#thm:core){reference-type="ref" reference="thm:core"}. The main loop of the algorithm is executed at most $n$ times. In each step the costs are dominated by checking one point in ${\mathbb{R}}^n$ for feasibility against $m$ linear inequalities. ◻
:::

::: remark
The linear search in Algorithms [\[algo:reduction_to_layers\]](#algo:reduction_to_layers){reference-type="ref" reference="algo:reduction_to_layers"} and [\[algo:core_point\]](#algo:core_point){reference-type="ref" reference="algo:core_point"} cannot be substituted by a direct bisectional approach. The reason is that the set of all $k$ in $\{0,1,\dots,\lfloor n\zeta\rfloor-n\lfloor\zeta\rfloor\}$ such that the $k$-th $\mathbbm{1}$-layer contains a feasible point is not necessarily (the set of integer points of) an interval.
:::
