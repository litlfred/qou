---
doc_id: arxiv-hep-th-0006156v1
doc_title: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality"
section_id: sec-009-18-lattice-virasoro-algebra
section_title: "Lattice Virasoro algebra"
section_number: 1.8
pages: 6-7
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.879
doc_brief: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality — The quantum discrete Liouville model in the strongly cou- pled regime, 1 < c < 25, is formulated as a well"
---
[]{#sec:lva label="sec:lva"} Now we look for a generalization of this construction by natural interpretation of the "raising". So, we want the lattice Virasoro algebra actually to be a group. If that is to be, the "global" relations ought to remain the same as in the braid group $$d_1d_2\ldots d_{N-1}=d_2d_3\ldots d_N
=\cdots=d_Nd_{N+1}\ldots d_{2N-2}\;,$$ or equivalently $$\tag{\ref{cr}\(''\)}
   \hat d_n=d_{n-1}=Q^{-1}d_nQ\qquad\qquad
   Q=d_1d_2\ldots d_{N-1}\;    ,$$ but this time each generator should interfere not only with the nearest neighbours but also with the second-nearest ones $$d_md_n=d_nd_m\qquad\text{if }|m-n|
\not\equiv1\text{ and }2\pmod{N} ,$$ just like it was in bracket ([\[mb\]](#mb){reference-type="ref" reference="mb"}$'$) of course. This by itself implies $$d_{n}d_{n-2}d_{n-1}d_{n}d_{n+1}
=d_{n-2}d_{n-1}d_{n}d_{n+1}d_{n-1}$$ instead of Artin's relations, but we feel that these are not tight enough, so we voluntarily split each of them in two $$d_{n}d_{n-2}d_{n-1}d_{n}d_{n+1}=d_{n-2}
d_{n}d_{n-1}d_{n+1}=d_{n-2}d_{n-1}d_{n} d_{n+1}d_{n-1} ,$$ to end up with weird relations from [@volkov97c] $$\tag{\ref{mb}\(''\)}
   \begin{aligned}d_{n+1}d_{n-1}d_{n}d_{n+1}
     &=d_{n-1}d_{n+1}d_{n}                      \\
     d_{n}d_{n-1}d_{n+1}&=d_{n-1}d_{n}d_{n+1} d_{n-1} .
   \end{aligned}$$ This coup de force will find its justification in the treatment of the Liouville model below.
