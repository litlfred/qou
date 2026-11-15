---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-006-142-two-color-relations
section_title: "Two color relations:"
section_number: 1.4.2
pages: 7-8
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.946
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
Two color graphs and Soergel bimodules for the dihedral group are explored in detail in \cite{EDihedral}. Essentially, morphisms between Bott-Samelson bimodules in rank 2 are governed by the Temperley-Lieb algebra at a root of unity, a fact related to the (quantum) geometric Satake equivalence for $\mathfrak{sl}_2$.

The first important two color relation is the cyclicity of the $2m_{st}$-valent vertex. (There is a subtlety here if the Cartan matrix is not symmetric, which we ignore in the introduction.) This allows us to consider all morphisms as isotopy classes of diagrams. The second relation is the so-called \emph{two color associativity} (here $m = m_{{\color{red}s}{\color{blue}t}}$):
\[
\includegraphics[width=10cm]{fig/twocolorassoc}
\]
It allows one to ``pull'' a trivalent vertex through a $2m_{st}$-valent vertex.

The third relation allows one to expand the composition of a dot and a $2m_{st}$-valent vertex into a linear combination of diagrams in which the $2m_{st}$-valent vertex does not occur. This relation is best understood using Jones-Wenzl projectors, as explained in \cite{EDihedral}, and is difficult to state without developing this machinery. (For example, for a Weyl group of type $G_2$, 42 terms occur). Here we give examples for finite parabolic subgroups of types $A_1 \times A_1$, $A_2$ and $B_2$, i.e. the cases $m_{st} = 2,3,4$:
\[
\includegraphics[width=10cm]{fig/dotremoval}
\]
We hope that the reader has not missed the appearance of a 2 in the relation for $B_2$. In general, these coefficients are polynomials in the entries of the Cartan matrix of the corresponding root system.

Together, the two-color relations imply that the composition of two $2m_{st}$-valent vertices is an idempotent endomorphism (corresponding to the projection to $B_{s,t}$ inside the Bott-Samelson bimodule):
\[
\includegraphics[width=10cm]{fig/twocoloridemp}
\]
