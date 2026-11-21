---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-001-2-automorphisms-of-linear-programs
section_title: "Automorphisms of Linear Programs"
section_number: 2
pages: 2-7
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.989
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linear and integer programming problems."
---
[]{#sec:LP label="sec:LP"} The purpose of this section is to introduce the notation and to collect basic facts for future reference. The results of this section up to and including Corollary [\[cor:opt_sol_in_fix\]](#cor:opt_sol_in_fix){reference-type="ref" reference="cor:opt_sol_in_fix"} can be found in the literature which is why we skip some of the proofs.

We consider linear programs $\operatorname{LP}(A,b,c)$ of the form $$\label{eq:LP}
  \begin{array}{ll}
    \max & c^tx\\
    \textrm{s.t.} & Ax \le b \, , \ x \in {\mathbb{R}}^n
  \end{array}$$ where $A\in{\mathbb{R}}^{m\times n}$, $b\in{\mathbb{R}}^m$, and $c\in{\mathbb{R}}^n\setminus\{0\}$. Throughout we will assume that the set $P(A,b):=\{x\in{\mathbb{R}}^n\,|\,Ax\le b\}$ of *feasible points* is not empty, and hence it is a convex polyhedron, which may be bounded or unbounded. We will also assume that an optimal solution exists. This is to say, our linear program $\operatorname{LP}(A,b,c)$ is bounded even if the feasible region may be unbounded. In this case the set of optimal solutions forms a non-empty face of $P(A,b)$. Our final assumption $c\ne 0$ is not essential for the algorithms below, but it allows to simplify the exposition somewhat.

Each row of the matrix $A$ corresponds to one linear inequality. Suppose that one of these rows is the zero vector. Then the corresponding right hand side must be non-negative, since otherwise the linear program would be infeasible, and this was explicitly excluded above. But then this linear inequality is trivially satisfied. Therefore we will further assume that the matrix $A$ does not contain any zero rows. In this case each row defines an affine hyperplane. This way $\operatorname{LP}(A,b,c)$ gives rise to an arrangement ${\mathscr{H}}(A,b)$ of $m$ labeled affine hyperplanes in ${\mathbb{R}}^n$.

::: definition
[]{#def:automorphism label="def:automorphism"} An *automorphism* of the linear program $\operatorname{LP}(A,b,c)$ is a linear transformation in ${\operatorname{GL}}_n{\mathbb{R}}$ which induces a permutation of ${\mathscr{H}}(A,b)$, which leaves $P(A,b)$ invariant, and which does not change the objective value $c^tx$ for any feasible point $x\in P(A,b)$.
:::

The objective function is linear, and hence it follows that an automorphism of $\operatorname{LP}(A,b,c)$ does not change the objective value on the linear span $\mathop{\mathrm{lin}}(P(A,b))$ of the feasible points. One could also take more general affine transformations into account. In all what comes below this would require a number of straightforward changes. We refrain from doing so for the sake of a clearer exposition. The following examples show that the three properties to be satisfied by a linear automorphism are mutually independent.

::: example
For $m=n=1$ let $A=1$, $b=0$, and $c=1$. The feasible region is the non-positive ray ${\mathbb{R}}_{\le 0}$. Multiplication with any positive real number $\gamma$ leaves the feasible region and the hyperplane arrangement (consisting of the origin) invariant. If $\gamma\ne 1$ the objective function is not preserved.
:::

::: example
For $m=n=2$ let $$A \ = \ \begin{pmatrix} -1&0\\ 0&-1 \end{pmatrix} \, , \quad b \ = \ 0 \, , \quad c \ = \
  \begin{pmatrix}{-1}\\ {0}\end{pmatrix} \, .$$ Then $P(A,b)$ is the non-negative quadrant in ${\mathbb{R}}^2$. Now $\gamma =
  \left(\begin{smallmatrix} 1&0 \\ 0&-1 \end{smallmatrix}\right)$ leaves the coordinate hyperplane arrangement ${\mathscr{H}}(A,b)$ invariant, but it changes the feasible region. For each $x\in{\mathbb{R}}^2$ we have $c^tx=c^t\gamma x$.
:::

::: example
[]{#exmp:redundant label="exmp:redundant"} For $m=3$ and $n=2$ let $$A \ = \ \begin{pmatrix} -1 & 0\\ 0 & -1\\ -1 & -2 \end{pmatrix} \, , \quad b \ = \ 0 \, , \quad
  c \ = -\mathbbm{1}\, .$$ The feasible region is the non-negative quadrant in ${\mathbb{R}}^2$; the third inequality is redundant. The linear transformation $\gamma =\left(\begin{smallmatrix} 0 & 1 \\ 1 & 0 \end{smallmatrix}\right)$ leaves the feasible region invariant, and it satisfies $c^tx=c^t\gamma x$ for all $x\in{\mathbb{R}}$. The hyperplane arrangement ${\mathscr{H}}(A,b)$ is changed.
:::

For more examples see [@BoediGrundhoeferHerr10]. There it is also shown that each finite (permutation) group occurs as the group of automorphisms of a linear program.

::: remark
[]{#rem:scale label="rem:scale"} It is always possible to scale the rows of the extended matrix $(A|b)$ such that the leftmost non-zero coefficient is $\pm1$. This allows to remove duplicate inequalities from the input by sorting. The complexity of sorting the rows by pair-wise comparison is of order $O(mn\log m)$. This can be neglected in the asymptotic analysis of our algorithms below since it is always dominated. This way we can always assume that the hyperplanes in ${\mathscr{H}}(A,b)$, that is, the inequalities, and the rows of the extended matrix $(A|b)$ are in a one-to-one correspondence. In the rational case it is more natural to scale the inequalities to integer coefficients which are coprime. This is what we will usually do. For a more sophisticated algorithm to sort out equivalent constraints, see Bixby and Wagner [@BixbyWagner87].
:::

Since we view points in ${\mathbb{R}}^n$ as column vectors, a matrix $\gamma$ representing a linear transformation acts by multiplication on the left. The adjoint action on the row space, and thus on the set of linear inequalities, is by multiplication of the inverse transpose $\gamma^{-t}$ on the right. The set of linear transformations permuting the arrangement ${\mathscr{H}}(A,b)$ forms a closed subgroup of ${\operatorname{GL}}_n{\mathbb{R}}$, that is, a linear Lie group. Similarly, the set of linear transformations leaving the feasible region $P(A,b)$ invariant forms a linear Lie group. It follows that the set $\operatorname{Aut}(\operatorname{LP}(a,b,c))$ of automorphisms of the linear program $\operatorname{LP}(A,b,c)$ also forms a linear Lie group. For basic facts about (linear) Lie groups, see Rossmann [@Rossmann02].

::: remark
Clearly, the value and the set of optimal solutions of a linear program only depend on the non-redundant constraints. At the expense of one linear program per constraint one can get rid of the redundant ones. This obviously does not help to reduce the complexity of solving the linear program given since the linear program for a redundancy check is of the same size. However, for more costly algorithmic problems, like integer programming as is discussed below, this reduction can be useful. In particular, this will be the case when the group of automorphisms becomes larger, see Example [\[exmp:redundant\]](#exmp:redundant){reference-type="ref" reference="exmp:redundant"}. Notice that the notion of "invariance" from [@GatermannParrilo04 Definition 3.1], specialized to linear programming, implies that redundant constraints are going to be ignored.
:::

The following result is a consequence of the combinatorial properties of a convex polytope $P$: the faces of $P$ are partially ordered by inclusion, and this partially ordered set forms a lattice. The automorphisms of this lattice, the *face lattice* of $P$, are called *combinatorial automorphisms*. Each linear (or affine or projective) automorphism of $P$ induces a combinatorial automorphism, but, in general, a polytope may have many combinatorial automorphisms which are not linearly induced. See Ziegler [@Ziegler95] for the details.

::: lemma
[]{#lem:Aut_finite label="lem:Aut_finite"} If the feasible region $P(A,b)$ is bounded and full-dimensional, then the automorphism group $\operatorname{Aut}(\operatorname{LP}(A,b,c))$ is finite. Moreover, the objective function $c$ satisfies $c^t\gamma x=c^t x$ for all $x\in{\mathbb{R}}^n$ and $\gamma\in\operatorname{Aut}(\operatorname{LP}(A,b,c))$.
:::

::: proof
*Proof.* Let $v$ be a vertex of the polytope $P=P(A,b)$. Since $\dim P=n$ there are vertices $w_1,w_2,\dots,w_n$ each of which shares an edge with $v$ and such that the difference vectors $w_1-v,w_2-v,\dots,w_n-v$ form a basis of ${\mathbb{R}}^n$. This implies that each combinatorial automorphism of $P$ is induced by at most one linear automorphism. Hence the group $\operatorname{Aut}(\operatorname{LP}(A,b,c))$ is contained in the group of combinatorial automorphisms of $P$, which is finite. While Definition [\[def:automorphism\]](#def:automorphism){reference-type="ref" reference="def:automorphism"} asks that each *feasible* point is mapped to a (feasible) point with the same objective value, the additional claim deals with all points, feasible or not. However, this follows from $\mathop{\mathrm{lin}}(P(A,b))={\mathbb{R}}^n$ as $c$ is linear. ◻
:::

If the polyhedron $P(A,b)$ is not full-dimensional, then the automorphism group is a direct product of the group of automorphisms fixing the linear span of $P(A,b)$ with a full general linear group of the orthogonal complement. In the sequel we will therefore restrict our attention to the full-dimensional case.

::: definition
Given a subset $Y\subseteq {\mathbb{R}}^n$ and a group $\Gamma\le{\operatorname{GL}}_{\mathbb{R}}$ acting on $Y$, the *set of fixed points* of $Y$ with respect to an element $\gamma\in\Gamma$ is defined by $$\operatorname{Fix}_\gamma(Y) \ := \ \left\{y\in Y\vphantom{\gamma y=y}\,\right.\left|\,\vphantom{y\in Y}\gamma y=y\right\} \, .$$ Therefore, the *set of fixed points* of $Y$ with respect to $\Gamma$ is given by $$\operatorname{Fix}_\Gamma(Y) \ := \ \left\{y\in Y\vphantom{\gamma y=y \text{ for all } \gamma\in\Gamma}\,\right.\left|\,\vphantom{y\in Y}\gamma y=y \text{ for all } \gamma\in\Gamma\right\} \ = \
  \bigcap_{\gamma\in\Gamma}\operatorname{Fix}_\gamma(Y) \, .$$
:::

The set of fixed points $\operatorname{Fix}_\gamma({\mathbb{R}}^n)$ is the (possibly zero-dimensional) eigenspace $\operatorname{Eig}(\gamma,1)$ of the linear transformation $\gamma$ with respect to the eigenvalue $1$. This implies that $\operatorname{Fix}_\Gamma({\mathbb{R}}^n)$ is a linear subspace for any group $\Gamma$ of linear transformations. More generally, $\operatorname{Fix}_\Gamma(Y)$ is the intersection of this subspace with the set $Y$.

::: remark
[]{#rem:compute_fixed label="rem:compute_fixed"} If the linear group $\Gamma\le{\operatorname{GL}}_n{\mathbb{R}}$ is generated by the set $G\subset\Gamma$, then $$\operatorname{Fix}_\Gamma({\mathbb{R}}^n) \ = \ \bigcap_{\gamma\in G}\operatorname{Fix}_\gamma({\mathbb{R}}^n) \ = \
  \bigcap_{\gamma\in G}\operatorname{Eig}(\gamma,1) \, .$$ In particular, if $G$ is finite, that is, if the group $\Gamma$ is finitely generated, this leads to an algorithm to compute (a primal or dual basis of) the fixed space by solving one linear system of equations per transformation in the generating set $G$.
:::

::: remark
[]{#rem:c_one label="rem:c_one"} Let $\Gamma\le\operatorname{Aut}(\operatorname{LP}(A,b,c))$ be a group of automorphisms of the linear program $\operatorname{LP}(A,b,c)$ such that $P(A,b)$ is bounded and full-dimensional. Then, by Lemma [\[lem:Aut_finite\]](#lem:Aut_finite){reference-type="ref" reference="lem:Aut_finite"}, the set of fixed points $\operatorname{Fix}_\Gamma({\mathbb{R}}^n)$ contains the one-dimensional linear subspace spanned by the objective vector $c$.
:::

For any finite set $S\subset {\mathbb{R}}^n$ let $$\beta(S) \ := \ \frac{1}{|S|}\sum_{v\in S}v$$ be its *barycenter*. The two subsequent results are basic observations from representation theory, not restricted to applications in (linear) optimization. For a brief proof, for instance, see [@Webb Lemma 3.5].

::: lemma
[]{#lem:barycenter label="lem:barycenter"} The map $${\mathbb{R}}^n \to \operatorname{Fix}_\Gamma({\mathbb{R}}^n) \, , \ v \mapsto \beta(\Gamma v)$$ which sends a point to the barycenter of its $\Gamma$-orbit is a linear projection onto the fixed space.
:::

Let $S\subseteq {\mathbb{R}}^n$ be a finite set which is *spanning*, that is, we require $\mathop{\mathrm{lin}}(S)={\mathbb{R}}^n$. Further let $\Gamma$ be a finite subgroup of ${\operatorname{GL}}_n{\mathbb{R}}$ acting on $S$. Phrased differently, we are considering a linear representation of an abstract group $\Gamma$ on the vector space ${\mathbb{R}}^n$ which induces a permutation representation on the set $S$. In this case $\Gamma$ splits $S$ into disjoint orbits $O_1,O_2,\ldots,O_k$. In our applications below, $S$ will usually be the set of vertices of some polytope which linearly spans ${\mathbb{R}}^n$.

::: lemma
[]{#lem:fix_spanned_by_betaO label="lem:fix_spanned_by_betaO"} For the fixed space of $\Gamma$ we have $$\operatorname{Fix}_\Gamma({\mathbb{R}}^n) \ = \ \mathop{\mathrm{lin}}\{\beta(O_1),\beta(O_2),\dots,\beta(O_k)\} \, .$$ In particular, $\dim\operatorname{Fix}_\Gamma({\mathbb{R}}^n) \le k$.
:::

::: proof
*Proof.* Since $S=O_1\cup O_2\cup\dots\cup O_k$ is spanning and since the union of the orbits gives $S$ it follows that $$\label{eq:orbit_decomp}
    {\mathbb{R}}^n \ = \ \mathop{\mathrm{lin}}(O_1)+ \mathop{\mathrm{lin}}(O_2)+ \dots+ \mathop{\mathrm{lin}}(O_k) \, .$$ For $i\in\{1,2,\dots,k\}$ the linear subspace $\mathop{\mathrm{lin}}(O_i)$ is $\Gamma$-invariant. If we apply the surjective linear map $v\mapsto\beta(\Gamma v)$ from Lemma [\[lem:barycenter\]](#lem:barycenter){reference-type="ref" reference="lem:barycenter"} to the set $S$, we obtain a generating set for $\operatorname{Fix}_\Gamma({\mathbb{R}}^n)$. Applying the same map to a single orbit $O_i$ similarly yields a generating set for $\operatorname{Fix}_\Gamma(\mathop{\mathrm{lin}}(O_i))$. Now the claim follows from the equation $\Gamma O_i=O_i$. ◻
:::

Notice that the sum decomposition [\[eq:orbit_decomp\]](#eq:orbit_decomp){reference-type="eqref" reference="eq:orbit_decomp"} is not necessarily direct. We now apply the results obtained so far to a finite group of automorphisms of a linear program.

::: proposition
[]{#prop:symmetric_solution label="prop:symmetric_solution"} Let $\Gamma\le\operatorname{Aut}(\operatorname{LP}(A,b,c))$ be finite. If $x\in{\mathbb{R}}^n$ is an arbitrary point, the barycenter of its $\Gamma$-orbit satisfies $c^t \beta(\Gamma x)=c^t x$. If, moreover, $x\in P(A,b)$ is feasible, then $\beta(\Gamma x)$ is feasible, too.
:::

Geometrically this means that the points of one orbit are in the same affine hyperplane orthogonal to $c$.

::: proof
*Proof.* As the objective function is constant on the orbit $\Gamma x$ it follows that $c^t
  \beta(\Gamma x)=c^t x$. If $x$ is a feasible point, then $\gamma x$ is also feasible for all $\gamma\in\Gamma$. So the barycenter $\beta(\Gamma x)$ is a convex combination of feasible points. The claim follows as the feasible region is convex. ◻
:::

Since we assumed that $\operatorname{LP}(A,b,c)$ has an optimal solution, the following is an immediate consequence of the preceding result.

::: corollary
[]{#cor:opt_sol_in_fix label="cor:opt_sol_in_fix"} There exists an optimal solution of $\operatorname{LP}(A,b,c)$ which is a fixed point with respect to the entire automorphism group $\operatorname{Aut}(\operatorname{LP}(A,b,c))$.
:::

Up to minor technical details Theorem 3.3 of [@GatermannParrilo04] generalizes Corollary [\[cor:opt_sol_in_fix\]](#cor:opt_sol_in_fix){reference-type="ref" reference="cor:opt_sol_in_fix"} to semi-definite programming.

Let $\operatorname{LP}(A,b,c)$ be a linear program with $P(A,b)$ bounded and full-dimensional, and let $\Gamma=\langle \gamma_1,\gamma_2,\dots,\gamma_t\rangle$ be a finite subgroup of $\operatorname{Aut}(\operatorname{LP}(A,b,c))$. Following Remark [\[rem:compute_fixed\]](#rem:compute_fixed){reference-type="ref" reference="rem:compute_fixed"} we can compute a matrix $E$ such that the kernel $\{x\,|\,Ex=0\}$ is the fixed space $\operatorname{Fix}_\Gamma({\mathbb{R}}^n)$: for each $\gamma_i$ we determine a dual basis for the eigenspace $\{x\,|\,(\gamma_i-\mathop{\mathrm{id}})x=0\}$ by solving a square system of linear equations. The total number of operations to do so is of order $O(tn^3)$. Throughout this paper we measure algorithmic complexity in the RAM model; that is, we ignore the encoding lengths of real numbers, and all arithmetic operations are assumed to take constant time. The group $\Gamma$ acts on the rows of the extended matrix $(A|b)$, and we define a new extended matrix $(A'|b')$ by summing the rows of the same $\Gamma$-orbit. We have the following general result.

::: theorem
[]{#thm:barycenter_ineqs label="thm:barycenter_ineqs"} The polyhedron $$P' \ = \ \left\{x\in{\mathbb{R}}^n\vphantom{A'x\le b',\, Ex=0}\,\right.\left|\,\vphantom{x\in{\mathbb{R}}^n}A'x\le b',\, Ex=0\right\}$$ is the set $\operatorname{Fix}_\Gamma(P(A,b))$ of feasible points which is fixed under the action of $\Gamma$. In particular, $P'=\{\beta(\Gamma x)\,|\,x\in P(A,b)\}$. Each optimal solution of the linear program $$\label{eq:reduced_LP}
    \begin{array}{ll}
      \max & c^tx\\
      \textrm{s.t.} & \begin{pmatrix} A'\\ E\\ -E\end{pmatrix} x \le \begin{pmatrix}b'\\ 0\\
        0\end{pmatrix} \, , \ x \in {\mathbb{R}}^n
    \end{array}$$ is an optimal solution of $\operatorname{LP}(A,b,c)$, and the objective values are the same.
:::

::: proof
*Proof.* We constructed the matrix $E$ to guarantee that each fixed point in $P=P(A,b)$ satisfies the equation $Ex=0$. Further, each inequality of the system $A'x\le b'$ is a positive linear combination of valid inequalities. It follows that $\operatorname{Fix}_\Gamma(P)$ is contained in $P'$.

To prove the reverse inclusion consider a point $x$ which is fixed by each transformation in $\Gamma$ but which is not contained in $P$. Then for some index $i$ we have the strict inequality $a_{i,\cdot}x>b_i$. Without loss of generality we can assume that the first $k$ rows $a_{1,\cdot},a_{2,\cdot},\dots,a_{k,\cdot}$ of $A$ form the $\Gamma$-orbit of the row $a_{i,\cdot}$. It follows that $b_1=b_2=\dots=b_k=b_i$. Moreover, since $x$ is a fixed point we have $$a_{1,\cdot}x \ = \ a_{2,\cdot}x \ = \ \cdots \ = \ a_{1,\cdot}x \ = a_{i,\cdot}x \ > \
  b_i \, .$$ This implies that $(\sum_{j=1}^k a_{j,\cdot})x>kb_i$, and hence $x$ is not contained in $P'$. We conclude that $P'$ is the set of points in $P$ fixed by each transformation of $\Gamma$. Now Lemma [\[lem:barycenter\]](#lem:barycenter){reference-type="ref" reference="lem:barycenter"} says that $P'$ is the image of $P$ under the map $x\mapsto \beta(\Gamma x)$. The claim about the linear program [\[eq:reduced_LP\]](#eq:reduced_LP){reference-type="eqref" reference="eq:reduced_LP"} follows from Corollary [\[cor:opt_sol_in_fix\]](#cor:opt_sol_in_fix){reference-type="ref" reference="cor:opt_sol_in_fix"}. ◻
:::

::: remark
It has been observed by Scharlau and Schürmann[^1] that the vertices of the polyhedron $P'$ are barycenters of orbits of vertices of $P$. This is a consequence of the fact that $P'$ is the image of $P$ under the linear map $x\mapsto\beta(\Gamma x)$.
:::

Corollary [\[cor:opt_sol_in_fix\]](#cor:opt_sol_in_fix){reference-type="ref" reference="cor:opt_sol_in_fix"} and Theorem [\[thm:barycenter_ineqs\]](#thm:barycenter_ineqs){reference-type="ref" reference="thm:barycenter_ineqs"} yield a direct algorithm for solving a symmetric linear program: instead of solving $\operatorname{LP}(A,b,c)$ one can solve the linear program [\[eq:reduced_LP\]](#eq:reduced_LP){reference-type="eqref" reference="eq:reduced_LP"}. The benefit is the following: The larger the group $\Gamma\leq\operatorname{Aut}(\operatorname{LP}(A,b,c))$ the smaller the dimension of the fixed space and the number of constraints.

::: remark
Formally, the feasible points of the derived linear program live in the same space ${\mathbb{R}}^n$ as the original linear program. However, an algorithm based on the Simplex Method directly benefits if the solutions are contained in a proper subspace: the rows of the matrix $E$ describing the fixed space never have to be exchanged in a Simplex tableau. Alternatively, one can project $\operatorname{Fix}_\Gamma({\mathbb{R}}^n)$ onto a full-dimensional coordinate subspace, solve the projected linear program and lift back.
:::

In the special case where the linear program admits a group of automorphisms acting on the standard basis of ${\mathbb{R}}^n$ (that is, the groups acts by permuting the columns) it is standard optimization practice to identify variables in the same orbit, and to solve the reduced linear program. Theorem [\[thm:barycenter_ineqs\]](#thm:barycenter_ineqs){reference-type="ref" reference="thm:barycenter_ineqs"} generalizes this approach to arbitrary groups of automorphisms.

[^1]: private communication
