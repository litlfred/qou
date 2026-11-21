---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-011-8-computational-complexity
section_title: "Computational complexity"
section_number: 8
pages: 21-22
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 1.0
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
[]{#complexsec label="complexsec"}

Consider the following two decision problems:

Problem 1

:   Let $\mathcal{T}$ be a simplicial complex, homeomorphic to a surface $S$ (possibly with boundary), and let $\alpha: V(\mathcal{T}) \rightarrow
    {\bf R}^+$ be an assignment of cone angles to the vertices of $\mathcal{T}$. Does there exist a Euclidean structure $E$ on $S$ with the prescribed cone angles, such that the Delaunay triangulation of $(S,
    E)$ is combinatorially equivalent to $\mathcal{T}$?

Problem 2

:   Let $\mathcal{T}$ be a simplicial complex, homeomorphic to a surface $S$ (possibly with boundary), and let $\Delta: E(\mathcal{T})
    \rightarrow (0, \pi]$ be an assignment of dihedral angles to the edges of $\mathcal{T}$. Does there exist a singular Euclidean structure $E$ on $S$, such that the Delaunay triangulation of $(S, E)$ is combinatorially equivalent to $\mathcal{T}$, and whose dihedral angles are given by $\Delta$.

By Theorem [\[exist\]](#exist){reference-type="ref" reference="exist"}, there are efficient algorithms for both problems, since they reduce to the linear program $L$ of section [\[oldstuff\]](#oldstuff){reference-type="ref" reference="oldstuff"}. If the angles (cone angles in problem 1, dihedral angles in problem 2) are rational multiples of $\pi$, such that the numerator and denominator are both bounded by $C$, then (by now) standard interior point methods allow us to solve the linear program $L$ using $O(n^4 (1+ \log C))$ arithmetic operation, each involving arithmetic using precision $O(n (1+\log C))$. In the case where all of the prescribed cone angles are equal to $2\pi$, the $\log C$ can be disposed with, and we wind up with an algorithm of bit-complexity $O(n^5 \log^2 n).$

*Remark.* In practice, the simplex algorithm appears much more efficient, and this has been used by M. B. Dillencourt to analyze all planar triangulations of up to $14$ vertices, and to determine which of them are combinatorially equivalent to planar Delaunay tessellations ([@Dill1; @Dillp]).

For problem 2, the network flow formulation of section [\[nflow\]](#nflow){reference-type="ref" reference="nflow"} turns out to give a markedly superior complexity. Indeed, it has been shown in [@aot] that for a network with $n$ nodes, $m$ arcs, and the (integer) capacity of each arc bounded by $U$, we can determine the maximal flow in time bounded by $O(n m
\log((n/m)(\log U)^{1/2}+2))$.

For the network $N_1$ of section [\[nflow\]](#nflow){reference-type="ref" reference="nflow"}, assuming the genus of the surface is fixed, the number of arcs and nodes in the network are both bounded by constant multiples of the number $F$ of faces in the complex $T$. If all of the dihedral angles are rational multiples of $\pi$, with numerators and denominators all bounded in absolute value by $C$, the quantity $U$ is bounded by $C^{O(F)}$ (since we need to compute the least common multiple of the denominators), giving a running time bound of $O(F^{5/2}).$ For the program $N_2$, the bound is the same, since the only difficulty consists of picking the right value of $\epsilon$, and this can be made to be $1/\mbox{least common denominator of the
dihedral angles}$.
