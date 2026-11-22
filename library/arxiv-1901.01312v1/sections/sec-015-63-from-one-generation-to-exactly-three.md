---
doc_id: arxiv-1901.01312v1
doc_title: "Braided fermions from Hurwitz algebras"
section_id: sec-015-63-from-one-generation-to-exactly-three
section_title: "From one generation to exactly three"
section_number: 6.3
pages: 8-9
source_pdf: 1901.01312v1.pdf
source_sha256: a480da38283622d6
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 1.0
doc_brief: "Braided fermions from Hurwitz algebras — Some curious structural similarities between a recent braid- and Hurwitz algebraic description of the unbroken internal symmetries for a single generations of"
---
There are several possibilities for extending the braid- and Hurwitz algebraic description from a single generation to exactly three generations. The algebra $C\ell(6)$ is large enough to represent three generations of fermions that transform as required under the unbroken symmetries [@furey2014generations]. It is however not yet clear how this three generation model relates to the single generation model based on minimal ideals.

A possible answer may be provided by consider the exceptional Jordan algebra. Jordan algebras arose from Jordan's 1932 attempt to reformulate quantum mechanics by identifying the minimal axioms that should be satisfied by an algebra of observables [@mccrimmon2006taste]. The classification of Jordan algebras was worked out soon after by Jordan, Wigner, and Von Neumann, and showed that all but one Jordan algebra can be represented by hermitian matrices over $\mathbb{C}$ or $\mathbb{H}$. The one curious exception is the exceptional Jordan algebra $J_3(\mathbb{O})$. An element of $J_3(\mathbb{O})$ consists of three octonions and three real numbers, and can be written as a $3\times 3$ hermitian octonionic matrix $$\begin{aligned}
\begin{pmatrix}
\alpha_1 & O_3 & \overline{O}_2 \\
\overline{O}_3 & \alpha_2 & O_1 \\
O_2 & \overline{O}_1 & \alpha_3
\end{pmatrix},\qquad \alpha_i\in\mathbb{R},\quad O_i\in \mathbb{O},
\end{aligned}$$ and where the bar indicates octonionic conjugation. This 27 dimensional exceptional Jordan algebra is the only Jordan algebra without a realization in terms of associative matrices.

One might speculate that if the unbroken SM symmetries of one generation of fermions can be described by a single copy of $\mathbb{O}$ (or rather a copy of split $\mathbb{O}$ inside $\mathbb{C}\otimes\mathbb{O}$), then three generations of fermions requires three copies. It then seems natural to embed these three copies inside the exceptional Jordan algebra. This provides an explanation why there are no more than three generations, because for $n\geq 4$, $J_n(\mathbb{O})$ are not Jordan algebras. This idea has been explored recently by [@todorov2018deducing]. There it is shown that the gauge group of the SM can be obtained via the Borel-de Siebenthal theory, which describes the maximal closed connected subgroups of a compact Lie group that have maximal rank.

The automorphism group of the exceptional Jordan algebra is the 52-dimensional exceptional Lie group $F_4$. Although the rank 4 group $F_4$ does not contain $SU(3)\times SU(2)\times U(1)$ as a subgroup, the subgroup of automorphisms which leave the three diagonal real elements in addition to one of the imaginary elements of each off-diagonal octonion invariant is exactly $SU(3)$ [@farnsworth2015standard]. The reduction from $F_4$ to $SU(3)$ therefore provides three $SU(3)$ singlets, three triplets, three antitriplets, and three antisinglets. One can likely extend this symmetry to $U(3)$ by finding a $U(1)$ generator as is done for an individual copy of the octonions [@furey2018three; @dixon2013division].

It remains to be shown how the ideas in [@todorov2018deducing] based on $J_3(\mathbb{O})$ relate to a construction of three families of fermions based on minimal left ideals. This would offer some insight into what an extension of the Helon model to exactly three generations might look like.
