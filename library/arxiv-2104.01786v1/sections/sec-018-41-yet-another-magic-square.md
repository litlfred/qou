---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-018-41-yet-another-magic-square
section_title: "Yet another magic square"
section_number: 4.1
pages: 16-17
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
toc_source: outline
text_source: latex
latex_prose_ratio: 0.725
latex_coverage_ratio: 0.989
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a single real"
---
There is an octonionic model for the exceptional Lie groups, which is obtained by considering $3\times 3$ matrices with entries in ${\mathbb X}\otimes{\mathbb Y}$, where ${\mathbb X},{\mathbb Y}$ are division algebras, see [@Barton:2000ki]. This leads to what in the literature is known as the \"magic square\" construction. These authors also describe the $2\times 2$ matrix version of the magic square. This gives a set of octonionic models for groups the largest of which is ${\rm Spin}(12,4)$. We describe a very closely related construction, which effectively forgets two of the corresponding Clifford generators, to produce models with the largest covered group being ${\rm Spin}(11,3)$. The difference between our construction and that in [@Barton:2000ki], see also [@Dray:2014mba], is that in our case the semi-spinor is the space ${\mathbb X}\otimes{\mathbb Y}$, while in the former case the semi-spinor is twice that $({\mathbb X}\otimes{\mathbb Y})^2$.

We now work out a table of cases that are covered by the construction of Theorem 1. There are two tables that can be produced. One corresponds to taking ${\mathbb X}$ to be a division algebra, and ${\mathbb Y}$ to be a split (i.e. just composition) algebra. This produces the most interesting \"magic square\". The largest group covered by this construction is ${\rm Spin}(11,3)$. $$\begin{aligned}
\label{table}
\begin{tabular}{c | ccc}
 & ${\mathbb C}$ & ${\mathbb H}$ & ${\mathbb O}$ \\
 \hline
 $\tilde{{\mathbb C}}$ & (2,0) & (4,0) & (8,0) \\
 $\tilde{{\mathbb H}}$ & (3,1) & (5,1) & (9,1) \\
 $\tilde{{\mathbb O}}$ & (5,3) & (7,3) & (11,3)
 \end{tabular}\qquad
 \begin{tabular}{c | ccc}
 & ${\mathbb C}$ & ${\mathbb H}$ & ${\mathbb O}$ \\
 \hline
 ${\mathbb C}$ & (1,1) & (3,1) & (7,1) \\
 ${\mathbb H}$ & (1,3) & (3,3) & (7,3) \\
 ${\mathbb O}$ & (1,7) & (3,7) & (7,7)
 \end{tabular}
 
\end{aligned}$$ What is indicated in these tables is the signature of the arising pseudo-orthogonal group.

The second table is the case when ${\mathbb X},{\mathbb Y}$ are either both division, or both split. These two possibilities give the same groups. The diagonal in this case gives the split signature pseudo-orthogonal groups ${\rm Spin}(1,1), {\rm Spin}(3,3)$ and ${\rm Spin}(7,7)$. The only other case that is not covered by the first table is that of ${\rm Spin}(7,1)$.

It is clear that adding $(1,1)$ to every entry of the first table reproduces the $2\times 2$ tables in [@Barton:2000ki], [@Dray:2014mba]. However, it is not so easy to go from the construction of Theorem 1 to that in [@Barton:2000ki], [@Dray:2014mba] because these references describe a model for the Lie algebra of the relevant groups as the algebra of $2\times 2$ matrices with entries in ${\mathbb X}\otimes {\mathbb Y}$. The corresponding $\gamma$-matrices are then $4\times 4$ such matrices. So, giving a model for the Clifford algebra requires one higher level of complexity. This can be done, but is not relevant for our purposes. We refer to [@Dray:2014mba] for details.

## Lie algebra

Taking the commutators of the $\Gamma$-matrices ([\[Gammas\]](#Gammas){reference-type="ref" reference="Gammas"}), or simply the products of distinct $\Gamma$-matrices, we get the following description of the Lie algebra of the groups that our construction covers. The Lie algebra is given by the following endomorphisms of ${\mathbb X}\otimes {\mathbb Y}$ $$\begin{aligned}
{\mathfrak so}({\rm Im}({\mathbb X}))\otimes {\mathbb I}+ {\mathbb I}\otimes {\mathfrak so}({\rm Im}({\mathbb Y})) + L_x \otimes L_y, \qquad x\in{\rm Im}({\mathbb X}), y\in{\rm Im}({\mathbb Y}).
\end{aligned}$$ For the case of ${\mathfrak so}(11,3)$ that is of most interest for us we can give a more explicit description $$\begin{aligned}
\label{lie-11-3}
X_{{\mathfrak so}(11,3)}= \sum_{i<j} \omega_{ij} E^i E^j \otimes {\mathbb I}+ {\mathbb I}\otimes \sum_{i<j} \tilde{\omega}_{ij} \tilde{E}^i \tilde{E}^j  + \sum_{i,j} a_{ij} E^i \otimes \tilde{E}^j.
\end{aligned}$$ Thus, there is the Lie algebra ${\mathfrak so}(7)$ acting on the ${\mathbb O}$ factor in ${\mathbb O}\otimes\tilde{{\mathbb O}}$, the algebra ${\mathfrak so}(4,3)$ acting on the $\tilde{{\mathbb O}}$ factor, and the terms that mix the first and second sets of directions in $(11,3)=(7,0) + (4,3)$. All the blocks here are constructed from $8\times 8$ matrices $E^i,\tilde{E}^i$, see ([\[Es\]](#Es){reference-type="ref" reference="Es"}), ([\[E-split\]](#E-split){reference-type="ref" reference="E-split"}). This gives a very explicit description of the Lie algebra.
