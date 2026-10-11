---
doc_id: arxiv-math-0502543v2
doc_title: "CONTINUITY OF VOLUMES – ON A GENERALIZATION OF A CONJECTURE OF J.W.MILNOR"
section_id: sec-001-3-convex-polytopes
section_title: "Convex polytopes"
section_number: 3
pages: 5-11
source_pdf: 0502543v2.pdf
source_sha256: 227ef8150cb08faf
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.587
doc_brief: "CONTINUITY OF VOLUMES – ON A GENERALIZATION OF A CONJECTURE OF J.W.MILNOR — In his paper [6] J."
---
[]{#convexpoly label="convexpoly"} For arbitrary convex polytopes in dimension $n > 3,$ (and convex *spherical* polytopes in all dimensions) the proof given in Section [\[simplices\]](#simplices){reference-type="ref" reference="simplices"} goes through without change, with the one proviso that it is not currently known whether the volume of a polytope is determined up to congruence by its dihedral angles. Such a uniqueness result *is* conjectured (indeed, it is conjectured that a polytope is determined up to congruence by the dihedral angles), and is easy to prove for *simple* polytopes -- those with simplicial links of vertices -- this follows in arbitrary dimension from the corresponding result in $3$ dimensions. For the $3$-dimensional result see, eg, [@thes0; @thes]. In the rest of this paper we will be concerned with the most interesting case of convex polyhedra in $\mathbb{H}^3.$

First, we recall the following result of [@thes; @thes0]:

::: theorem
[]{#annelk label="annelk"} A metric space $(M, g)$ homeomorphic to $\mathbb{S}^2$ can arise as the Gaussian image $G(P)$ of a compact convex polyhedron $P$ in $\mathbb{H}^3$ if and only if the following conditions hold:

- (a) The metric $g$ has constant curvature $1$ away from a finite collection of cone points.

- (b) The cone angle at each $c_i$ is greater than $2\pi.$

- (c) The lengths of closed geodesics of $(M, g)$ are all strictly greater than $2\pi.$
:::

Assume now, for simplicity, that the polyhedron $P$ is simple (as pointed out above, this also allows us to assume that the geometry is determined by the dihedral angles). In that case, the space of admissible metrics $\Omega_P$ (as per Theorem [\[annelk\]](#annelk){reference-type="ref" reference="annelk"}) is parametrized by the exterior dihedral angles (the cell decomposition dual to that of $P$ gives a triangulation of the Gaussian image, and the (exterior) dihedral angles are the lengths of edges of the triangulation.) Theorems [\[degenthm\]](#degenthm){reference-type="ref" reference="degenthm"},[\[quasig\]](#quasig){reference-type="ref" reference="quasig"} immediately imply the following:

::: theorem
[]{#loggrowth label="loggrowth"} There exists a constant $L_0,$ such that the maximal length $\ell_P$ of an edge of $P$ is bounded as follows: $$\ell_P \leq \max(L_0,  - 2N \log(d(P, \partial \overline{\Omega}_P)/12N)),$$ where $N$ is the number of vertices of $P.$
:::

::: proof
*Proof.* Assume the contrary. Then, there exists a sequence of polyhedra $P_1, \dots, P_n, \dots$ with diameter $\rho(P_i) \geq \ell){P_i}$ going to infnity, which are farther than $12 N  \exp(-\rho/2N).$ By choosing a subsequence, we may assume that there is a *fixed* cycle of faces $F_1, \dots, F_k$ of $P,$ such that the sum of dihedral angles along the edges $e_i = F_i \cap F_{i+1}$ is smaller than $2\pi + 12 N  \exp(-\rho/2N),$ (by Theorem [\[degenthm\]](#degenthm){reference-type="ref" reference="degenthm"}) and which are a $4N\exp(-2\rho)$ quasigeodesic (by Theorem [\[quasig\]](#quasig){reference-type="ref" reference="quasig"}). Since the limit point of the $P_i$ is not in $\Omega_P$ (by Theorem [\[annelk\]](#annelk){reference-type="ref" reference="annelk"}), the result follow. ◻
:::

The following corollary is immediate (by Schläfli, see Section [\[simplices\]](#simplices){reference-type="ref" reference="simplices"}):

::: corollary
[]{#lpest label="lpest"} The volume is in $W^{1, p}(\Omega_p)$ for *all* $p > 0.$
:::

We now have almost enough to show that volume extends to $\overline{\Omega}_p,$ except for the slight matter of not having the required (by Theorem [\[sobemb\]](#sobemb){reference-type="ref" reference="sobemb"}) regularity result for $\partial{\Omega}_P.$ Such a result seems quite non-trivial, since the length of the shortest closed geodesic is a rather badly behaved quantity. However, there are two very important special cases where $\Omega_P$ is actually a convex polytope, so this problem is finessed. The first is when we restrict the dihedral angles to be non-obtuse. This case is covered by

::: theorem
Let $C$ be an abstract polyhedron with more than $4$ faces, and suppose that *non-obtuse* angles $\alpha_i$ are given corresponding to each edge $e_i$ of $C.$ There is a compact convex hyperbolic polyhedron whose faces realize $C$ with dihedral angle $\alpha_i$ at each edge $e_i$ if and only if the following conditions hold:

1.  For each edge $e_i,$ $0 < \alpha_i \leq \pi/2.$

2.  For any three distinct edges $e_1, e_2, e_3$ meeting at a vertex, $\alpha_1 + \alpha_2 + \alpha_3 > \pi.$

3.  Whenever $\Gamma$ is a prismatic $3$-circuit intersecting edges $e_1, e_2, e_3,$ then $\alpha_1 + \alpha_2 + \alpha_3 < \pi.$

4.  Whenever $\Gamma$ is a prismatic $4$-circuit intersecting edges $e_1, e_2, e_3, e_4,$ then $\alpha_1 + \alpha_2 + \alpha_3 + \alpha_4 <2\pi.$

5.  Whenever there is a four-sided face bounded by edges $e_1, e_2, e_3, e_4$ (enumerated successively), with edges $e_{12}, e_{23}, e_{34}, e_{41}$ entering the four vertices, then: $$\begin{gather}
    \alpha_1 + \alpha_3 + \alpha_{12} + \alpha_{23} + \alpha_{34} + \alpha_{41} < 3\pi,\\
    \alpha_2 + \alpha_4 + \alpha_{12} + \alpha_{23} + \alpha_{34} + \alpha_{41} < 3\pi.
    \end{gather}$$
:::

The other special case is that of hyperideal polyhedra:

::: theorem
Let $\sigma$ be a cell decomposition of $S^2,$ and let $w: \sigma_1 \rightarrow (0, \pi)$ be a map on the set of edges of $\sigma.$ Then there exists a hyperideal polyhedron with combinatorics given by $\sigma$ and exterior dihedral angles given by $w$ if and only if:

1.  The sum of the values of $w$ on each circuit in $\sigma_1$ is not smaller than $2\pi,$ and is strictly greater if the circuit is non-elementary.

2.  The sum of values of $w$ on each simple path in $\sigma_1$ is strictly larger than $\pi.$

The hyperideal polyhedron is then unique.
:::
