---
doc_id: arxiv-0802.1072v2
doc_title: "A note on closed 3-braids ∗"
section_id: sec-001-solving-the-conjugacy-problem-in-b3
section_title: "Solving the conjugacy problem in B3"
section_number: null
pages: 3-4
source_pdf: 0802.1072v2.pdf
source_sha256: 6f4d93f0b7ba5cd7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.86
latex_coverage_ratio: 0.991
doc_brief: "A note on closed 3-braids ∗ — This is a review article about knots and links of braid index 3."
---
[]{#S:conjugacy label="S:conjugacy"}

As noted above, to use Theorem [\[T:topological\]](#T:topological){reference-type="ref" reference="T:topological"} the reader will need definitive tests for deciding (i) when two 3-braids are conjugate; (ii) when a conjugacy class is one of the exceptional ones which admits a non-degenerate flype; and (iii) when a conjugacy class contains $\sigma_1^k\sigma_2^{\pm 1}$ for some $k$. In this section we discuss (i).

The conjugacy problem in $B_3$ was solved long ago by O. Schreier [@Sc], making use of the fact that $B_3$ is a free product with amalgamations of cyclic groups of orders 2 and 3. His work did not generalize to $B_n, \ n>3$, where the braid groups have a more complicated structure than they do when $n=3$.

The first solution to the conjugacy decision and conjugacy search problems for all braid groups $B_n, \ n\geq 3,$ was discovered by F. Garside in 1965 [@Ga]. Garside's solution was exponential in word length and in braid index, and that fact has lead to major efforts to find a polynomial-time solution to the conjugacy decision and search problems in $B_n$, which continue at this writing. In 1992, motivated by the work of Garside [@Ga] and the later work of Birman and Menasco on 3-braids in [@BM-SLVCB-III], P.J. Xu discovered in [@Xu] a new and fast solution to the conjugacy problem in the special case of $B_3$. Her work lead naturally to an algorithm to solve the shortest word problem in $B_3$, and so (by special properties of links that are closed 3-braids, established in [@BM-SLVCB-III]) to compute the genus of a knot of braid index 3. One surprising feature of it, that was generalized later to all the groups $B_n, n\geq 2,$ in [@BKL] and thence to many Garside groups, was that it gave a 'dual' Garside structure on the braid groups. This fact played an important role in the isolation of *Garside groups* as an interesting class [@DP; @Deh]. In describing the basic theorems about 3-braids we choose Xu's work over Schreier's because it generalizes to all $n$ and so may give insights that might otherwise be missed. We also choose the band presentation (described below) and its Garside structure over the classical presentation ([\[E:classical presentation\]](#E:classical presentation){reference-type="ref" reference="E:classical presentation"}) and its Garside structure because it seems simpler, from a computational point of view. None of the solutions to the conjugacy problem in $B_3$ are particularly suited to problems (ii) and (iii) above.
