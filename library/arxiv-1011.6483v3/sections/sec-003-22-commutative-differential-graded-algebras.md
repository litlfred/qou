---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS"
section_id: sec-003-22-commutative-differential-graded-algebras
section_title: "Commutative Differential Graded Algebras"
section_number: 2.2
pages: 8-8
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.982
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY, TOPOLOGICAL CHIRAL HOMOLOGY AND FACTORIZATION ALGEBRAS — We study the higher Hochschild chain functor, factorization alge- bras and their relationship with"
---
[]{#S:CDGA label="S:CDGA"} We let $CDGA$ be the category of commutative differential graded algebras (over the characteristic zero field $k$). We do not assume the underlying chain complexes of our algebras to be bounded since in practice, it happens that one has to consider the Hochschild chains of de Rham forms on a space, which is generally $\mathbb Z$-graded. We follow the approach of [@ToVe Chapter 1.1] and [@Hi] for the model category properties of $CDGA$ and modules over CDGAs. Recall from [@Ho Section 2.3], that there is a standard cofibrantly generated closed model category structure on the category of unbounded chain complexes for which fibrations are epimorphisms and (weak) equivalences are quasi-isomorphisms. It is further a symmetric monoidal model category with respect to the tensor products of chain complexes.

Since we work in characteristic zero, there is a standard closed model category structure on $CDGA$ [@Hi Theorem 4.1.1] as well, for which fibrations are epimorphisms and (weak) equivalences are quasi-isomorphisms (of CDGAs). The category $CDGA$ also has a monoidal structure given by the tensor product (over the ground field $k$) of differential graded commutative algebras, which makes $CDGA$ a symmetric monoidal model category. Note that since $k$ is assumed to be a field, this monoidal structure is given by an exact bifunctor.

Also note that $CDGA$ is simplicially enriched. Indeed, given $A,B \in CDGA$, we can form $\text{Map}_{CDGA}(A,B)$ the simplicial set of maps $[n]\mapsto \mathop{Hom}_{CDGA}(A, B\otimes \Omega^*(\Delta^n))$ (where $\Omega^*(\Delta^n)$ is the CDGA of forms on the $n$-dimensional standard simplex).

For any CDGA $A$, one can consider its category of *differential graded (left) modules*, that we will denote by $A\textit{-}Mod$. Again it has a natural model category structure with fibrations being epimorphisms and weak equivalences being quasi-isomorphisms. Further all assumptions in [@ToVe Chapter 1.1] are satisfied. In particular, the tensor product of $A$-modules makes $A\textit{-}Mod$ a symmetric monoidal model category (in the sense of [@Ho]) such that the functor $M\otimes_A -$ preserves weak equivalences when $M$ is cofibrant. Moreover, for any CDGA $A$, the category $A-CDGA$ of differential graded commutative $A$-algebra, in other words commutative monoid objects in $A\textit{-}Mod$, has a natural structure of proper model category such that, for any cofibrant $A$-algebra $B$, the base change functor $B\otimes_A -: A\textit{-}Mod \to B\textit{-}Mod$ preserves weak equivalences [@ToVe Chapter 1.1].
