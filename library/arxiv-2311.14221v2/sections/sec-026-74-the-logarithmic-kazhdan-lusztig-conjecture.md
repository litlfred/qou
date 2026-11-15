---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-026-74-the-logarithmic-kazhdan-lusztig-conjecture
section_title: "The logarithmic Kazhdan Lusztig conjecture"
section_number: 7.4
pages: 45-47
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.957
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
In conformal field theory, there is in good situations a modular tensor category of  representations of a vertex algebra $\mathcal{V}$, which reflects the analytic properties for example of solution spaces to certain differential equations (e.g. the braiding reflects the monodromy around the singularity $z=0$). One is often confronted with the very difficult question to determine the representation category of representations of a vertex subalgebra  $\mathcal{W}\subset \mathcal{V}$ if the representation theory of $\mathcal{V}$ is known, for example being a free-field realization. A brief introduction, references and an account for the statements below can be found in \cite{CLR}. \\

Categorically, one can understand as $\Rep(\mathcal{W})$ being a modular tensor category and $A=\mathcal{V}$ being a commutative  algebra in this category and $\vc=\Rep(\mathcal{V})$ is the category of local $A$-modules $\Rep^{loc}(A)$. Then by the results in \cite{CLR} Section $3$ we have under suitable conditions that $\Rep(\mathcal{W})$ is a relative Drinfeld center of $\Rep(A)$ with respect to the subcategory $\vc=\Rep^{loc}(A)$. In the cases relevant to logarithmic (i.e. nonsemisimple) conformal field theory, it is often the case that all \emph{simple} modules in $\Rep(A)$ are already in $\Rep^{loc}(A)$. This gives rise via the socle filtration to a monoidal section functor, see \cite{CLR} Section 4 $$\Rep^{loc}(A)\rightleftarrows \Rep^{loc}(A)$$
Then the results in our paper produce a Hopf algebra $R^*$, such that 
$$\Rep(A)={^{R^{*}}}\vc$$
and in this case the mentioned equivalence to the relative Drinfeld center means explicitly (see Section \ref{Section_YD})
$$\Rep(\mathcal{W})
\cong {^R_R}\YD(\vc)$$
For example the celebrated and notoriously difficult \emph{logarithmic Kazhdan Lusztig conjecture} considers the lattice vertex algebra $\mathcal{V}_\Lambda$ of the root lattice of a semisimple complex finite dimensional Lie algebra $\mathfrak{g}$ rescaled by an integer $p$, whose category of representations is the category of vector spaces graded by an abelian group 
$$\Rep(\mathcal{V}_\Lambda)=\Vect_{\Lambda^*/\Lambda}$$  Then it asserts that $\mathcal{V}_\Lambda$ contains as kernel of screening operators a certain vertex algebra $\mathcal{W}_p(\mathfrak{g})\subset \mathcal{V}_\Lambda$, whose category of representation is conjectured to be equivalent to the category of representations of the small quantum group $u_q(\mathfrak{g})$ for $q=e^{\pi i / p}$. In the first authors paper \cite{CLR} the approach is to view the small quantum group category as a category of Yetter-Drinfeld modules over the Nichols algebra $\mathcal{N}$
$$\Rep(u_q(\mathfrak{g}))\cong {^\mathcal{N}_\mathcal{N}}\YD(\Vect_{\Lambda^*/\Lambda})$$
and develop the categorical tools above to reduce the equivalence in question to proving that 
$$\Rep(A)\cong {_\mathcal{N}}\Vect_{\Lambda^*/\Lambda}$$
In the case $\mathfrak{sl}_2$ the abelian category could be determined and this gives a systematic proof of the conjecture in this case (initially we have used more complicated proof methods for the case $\mathfrak{sl}_2,p=2$ in \cite{CLR}, while \cite{GN} have used very different arguments for $\mathfrak{sl}_2,p$). A main motivation for writing the present paper is that now we have the clear statement that the category $\Rep(A)$ is for abstract reasons given as category of representations of a Hopf algebra $\mathcal{N}$ in $\vc$, and it now remains to determine that $\mathcal{N}$ is indeed the expected Nichols algebra, namely the Nichols algebra of screenings.
