---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-003-4-layers-of-integer-points
section_title: "Layers of Integer Points"
section_number: 4
pages: 9-11
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.94
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linear and integer programming problems."
---
[]{#sec:layers label="sec:layers"} Our goal is to describe an algorithm for the efficient solution of a highly symmetric integer linear program. Again we consider $\operatorname{ILP}(A,b,c)$ with a group $\Gamma$ of automorphisms as above.

Let us assume that the objective function $c\ne 0$ is *projectively rational*. This means that we require $c$ to be a constant real multiple of a rational vector. For such a vector $c$ let $\operatorname{coprime}(c)$ be the unique integral vector with coprime coefficients such that $c=\rho\operatorname{coprime}(c)$ for some positive real $\rho$. If $c$ is a multiple of a standard basis vector, the single non-zero coefficient of $\operatorname{coprime}(c)$ is defined to be $\pm 1$. For an integer $k$ the *$k$-th $c$-layer* is the affine hyperplane $$H_{c,k} \ = \ \ker\ (x\mapsto c^tx)+\frac{k}{\left\lVert\operatorname{coprime}(c)\right\rVert^2}\operatorname{coprime}(c) \, .$$ We have $H_{c,k}=H_{\rho c,k}$ for all $\rho>0$, and $H_{-c,k}=-H_{c,k}=H_{c,-k}$. All points in $H_{c,k}$ attain the same value $k$ with respect to the rescaled objective function $\operatorname{coprime}(c)$. We call $k$ the *number* of the $c$-layer $H_{c,k}$. The intersection of $H_{c,k}$ with the line ${\mathbb{R}}c$ is called the *center*.

::: lemma
[]{#lem:layer label="lem:layer"} If $c\ne 0$ is projectively rational, the integral point $x\in{\mathbb{Z}}^n$ is contained in the $c$-layer with number $\operatorname{coprime}(c)^tx$.
:::

::: proof
*Proof.* The number $k=\operatorname{coprime}(c)^tx$ is an integer. We abbreviate $d=\operatorname{coprime}(c)$ and compute $$c^t\bigl(\frac{k}{\left\lVert d\right\rVert^2}d\bigr) \ = \ c^t\bigl(\frac{d^txd}{\left\lVert d\right\rVert^2}\bigr) \ = \ \frac{d^td}{\left\lVert d\right\rVert^2}c^tx \ = \ c^tx \, .$$ Hence $x-(k/\left\lVert d\right\rVert^2)d$ is contained in the kernel of the linear form $c^t$, that is, the point $x$ lies in the affine hyperplane $H_{c,k}$. ◻
:::

For the following result it is crucial that the coefficients of $\operatorname{coprime}(c)$ are coprime.

::: proposition
[]{#prop:partition label="prop:partition"} If $c\ne 0$ is projectively rational, the $c$-layers $H_{c,k}$ for $k\in{\mathbb{Z}}$ partition the set ${\mathbb{Z}}^n$ of all integral points.
:::

::: proof
*Proof.* From Lemma [\[lem:layer\]](#lem:layer){reference-type="ref" reference="lem:layer"} is clear that each integral point is contained in some $c$-layer. By construction it is also obvious that the $c$-layers are pairwise disjoint. It remains to show that $H_{c,k}\cap{\mathbb{Z}}^n$ is non-empty for all $k\in{\mathbb{Z}}$.

Let $d=\operatorname{coprime}(c)$. Since the coefficients $d_1,d_2,\dots,d_n$ are coprime there are integral coefficients $x_1,x_2,\dots,x_n$ such that $$x_1 d_1 + x_2 d_2 + \dots + x_n d_n \ = \ \gcd(d_1,d_2,\dots,d_n) \ = \ 1 \, .$$ However, the left side of this equation equals $c^t x$, whence the point $x$ is contained in the first $c$-layer $H_{c,1}$. Now $c^t(kx)=kc^t(x)=k$ implies that the $k$-th layer contains the integral point $kx$ for arbitrary $k\in{\mathbb{Z}}$. ◻
:::

Another way of putting the statement above is that $\operatorname{coprime}(c)$ is the unique generator of the unique minimal Hilbert basis of the one-dimensional pointed cone ${\mathbb{R}}_{\ge 0}c$.

::: remark
An important consequence of Proposition [\[prop:partition\]](#prop:partition){reference-type="ref" reference="prop:partition"} is that for any given bounds $\ell,u\in{\mathbb{R}}$ there are only finitely many $c$-layers with feasible integral points whose objective values lie between $\ell$ and $u$. This does not hold if the objective function is not projectively rational.
:::

::: algorithm
let $z=\zeta\mathbbm{1}$ be a symmetric optimal solution of the LP relaxation $\operatorname{LP}(A,b,\mathbbm{1})$ $k\leftarrow \lfloor n\zeta\rfloor$
:::

::: theorem
[]{#thm:reduction_to_layers label="thm:reduction_to_layers"} For given $A$ and $b$ such that $\mathop{\mathrm{Sym}}(\operatorname{ILP}(A,b,\mathbbm{1}))$ acts transitively on the standard basis the Algorithm [\[algo:reduction_to_layers\]](#algo:reduction_to_layers){reference-type="ref" reference="algo:reduction_to_layers"} solves the integer linear program $\operatorname{ILP}(A,b,\mathbbm{1})$.
:::

::: proof
*Proof.* Recall that throughout we assumed that the set of feasible points of the linear relaxation is bounded. Hence it cannot occur that the integer linear program is unbounded.

Let $\Gamma\le\mathop{\mathrm{Sym}}(\operatorname{ILP}(A,b,\mathbbm{1}))$ be a transitive group of automorphisms. The fixed space is spanned by $\mathbbm{1}$. If $z$ is an optimal solution of the relaxation $\operatorname{LP}(A,b\mathbbm{1})$, then, by Proposition [\[prop:symmetric_solution\]](#prop:symmetric_solution){reference-type="ref" reference="prop:symmetric_solution"}, the barycenter $\beta(\Gamma z)=\zeta\mathbbm{1}$ for $\zeta=1/n(z_1+z_2+\dots+z_n)$ is also an optimal solution. Now $\lfloor\zeta\rfloor\mathbbm{1}$ is an integral point in the fixed space with an objective value not exceeding the optimal value of the linear programming relaxation. Each $\mathbbm{1}$-layer with a feasible integral point meets the one-dimensional polyhedron $P'=\{\beta(\Gamma x)\,|\,x\in P(A,b)\}$. We infer that no integral optimal solution of $\operatorname{ILP}(A,b,\mathbbm{1})$ can have an objective value strictly less than $n\lfloor\zeta\rfloor$.

Due to Proposition [\[prop:partition\]](#prop:partition){reference-type="ref" reference="prop:partition"} the $\mathbbm{1}$-layers partition ${\mathbb{Z}}^n$, and so the feasible points of $\operatorname{ILP}(A,b,c)$ are contained in the set $$\bigcup_{k=n\lfloor\zeta\rfloor}^{\lfloor n\zeta\rfloor} H_{\mathbbm{1},k} \, .$$ ◻
:::

The benefit of Algorithm [\[algo:reduction_to_layers\]](#algo:reduction_to_layers){reference-type="ref" reference="algo:reduction_to_layers"} is that it reduces a (symmetric) $n$-dimensional integer linear programming problem to $n$ integer feasibility problems in one dimension below. Since the latter is still an NP-complete problem not much is gained, in general. The situation changes, however, if we assume higher degrees of transitivity for the action of the group of automorphisms.

::: remark
Searching a family of parallel affine hyperplanes for integer points as in Algorithm [\[algo:reduction_to_layers\]](#algo:reduction_to_layers){reference-type="ref" reference="algo:reduction_to_layers"} also plays a key role in Lenstra's algorithm for integer linear programming which requires polynomial time in fixed dimension [@Lenstra83].
:::
