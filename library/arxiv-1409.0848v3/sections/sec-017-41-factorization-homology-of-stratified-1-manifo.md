---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-017-41-factorization-homology-of-stratified-1-manifo
section_title: "Factorization homology of stratified 1-manifolds"
section_number: 4.1
pages: 42-43
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.956
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
---
When the target symmetric monoidal $\oo$-category $\cV$ is $\m_\Bbbk^\ot$, the category of $\Bbbk$-modules for some commutative algebra $\Bbbk$, then factorization homology of closed 1-manifolds gives variants of Hochschild homology.

The simplest and most fundamental example is factorization homology for framed 1-manifolds, $\mfld_1^{\fr}$. In this case, there is an equivalence between framed 1-disk algebras and associative algebras in $\cV$, $\Alg_{\disk_1^{\fr}}(\cV)\simeq \Alg(\cV)$, and we have the following immediate consequence of the excision property of factorization homology (Theorem~\ref{fact-excisive}). 

\begin{prop}\label{hochschild} For an associative algebra $A$ in $\m_d$, there is an equivalence \[\int_{S^1}A \simeq \hh_*(A)\] between the factorization homology of the circle with coefficients in $A$ and the Hochschild homology of $A$ relative $\Bbbk$.
\end{prop}

\begin{proof} We have the equivalences \[\int_{S^1}A\simeq \int_{\RR^1}A\underset{{\underset{{S^0\times\RR^1}}\int\!\! A}}\ot\int_{\RR^1}A\simeq A\underset{A\ot A^{\op}}\ot A\simeq \hh_*(A)\]using excision and a decomposition of the circle by two slightly overlapping hemispheres.\end{proof}

\begin{remark} Lurie in \S5.5.3 of ~\cite{HA} shows further that the obvious circle action by rotations on $\int_{S^1}A$ agrees with the usual simplicial circle action on the cyclic bar construction.
\end{remark}

It is interesting to probe this example slightly further and see the algebraic structure that results when one introduces marked points and singularities into the 1-manifolds. Recall the $\oo$-category $\mfld^{\fr}_{1,0}$ of framed 1-manifolds with marked points, and the $\infty$-subcategory $\sD^{\fr}_{1,0}$ of framed 1-disks with at most one marked point -- its set of objects is the two-element set $\{U^1_{\emptyset^{-1}} , U^1_{S^0}\}$ whose elements we justifiably denote as $\RR^1:= U^1_{\emptyset^{-1}}$ and $(\RR^1,\{0\}) := U^1_{S^0}$.   So $\Alg_{\disk^{\fr}_{1,0}}(\cV)$ is equivalent to the $\oo$-category whose objects are pairs $(A_1, A_{\sf b})$ consisting of an algebra $A_1$ and a unital $A_1$-bimodule $A_{\sf b}$, i.e., a bimodule with an invariant map from the unit. Specifically, $A_1 \simeq A(\RR^1)$ and $A_{\sf b}\simeq A(\RR^1, \{0\})$. The proof of the Proposition~\ref{hochschild} extends mutatis mutandis to the following.

\begin{prop} There is an equivalence \[\int_{(S^1,\ast)} A\simeq \hh_*(A_1,A_{\sf b})\] between the factorization homology of the pointed circle $(S^1,\ast)$ with coefficients in $A =(A_1,A_{\sf b})$ and the Hochschild homology of $A_1$ with coefficients in the bimodule $A_{\sf b}$.
\end{prop}

Finally, we mention the example of factorization homology for $\snglr_1^{\fr}$, the category of 1-dimensional, framed, stratified spaces. In this case, the $\oo$-category of basic opens $\bsc_1^{\fr}$ has as its set of objects $\{\RR\}\coprod \{(\sC(J), \sigma)\}$ where the latter set is indexed by finite sets $J$ together with an orientation $\sigma$ of the ordinary $1$-manifold $\bigsqcup_J \RR_{>0} = \sC(J)\smallsetminus \ast$.  

An object $A$ in $\Alg_{\disk(\bsc^{\fr}_1)}(\cV)$ is then equivalent, by evaluating on directed graphs with a single vertex, to the data of an associative algebra $A(\RR)$ in $\cV$ and for each pair $i,j\geq 0$ an object $A(i,j) \in \cV$ equipped with $i$ intercommuting left $A(\RR)$-module structures and $j$ intercommuting right compatible $A(\RR)$-module structures. One can see, for instance, that the factorization homology of a wedge of two circles with a marked point on each circle, ${(S^1\cup_{\{0\}}S^1, \{1, -1\})}$, can be calculated as \[\int_{(S^1\cup_{\{0\}}S^1, \{1, -1\})}A\simeq A(1,1)\underset{A_1\ot A_1^{\op}}\ot A(2,2)\underset{A_1\ot A_1^{\op}}\ot A(1,1)~.\]
