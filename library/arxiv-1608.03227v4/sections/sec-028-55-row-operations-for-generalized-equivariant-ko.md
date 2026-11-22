---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-028-55-row-operations-for-generalized-equivariant-ko
section_title: "Row operations for generalized equivariant Koszul matrix factorizations"
section_number: 5.5
pages: 29-30
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.623
latex_coverage_ratio: 0.976
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
[]{#ssec: row ops label="ssec: row ops"} We use notations of the lemma [\[lem: ext MF+eq\]](#lem: ext MF+eq){reference-type="ref" reference="lem: ext MF+eq"} here and we also assume that the complex $(\calF_\bullet,d^+)$ is the Koszul complex tensored with matrix factorization $(M,D,\partial)$: $$\calF_\bullet=\tilde{M} \otimes \Lambda^\bullet V, \quad d^+=\sum_{j=1}^n f_i\theta_i,$$ where $\theta_i$ form a basis of $V$ and $f_1,\dots,f_n$ form a regular sequence in $\CC[\calZ]$. We call such matrix factorizations generalized equivariant Koszul matrix factorizations.

In these notations the corrective differentials that are computed by the iterative procedure from lemma [\[lem: ext MF+eq\]](#lem: ext MF+eq){reference-type="ref" reference="lem: ext MF+eq"} are of the form $$d^-=\sum_{\vec{i}} d^-_{\vec{i}}\frac{\partial}{\partial \theta_{\vec{i}}}, \quad \partial^-=\sum_{\vec{i}}\partial^-_{\vec{i}} \frac{\partial}{\partial \theta_{\vec{i}}},$$ where $\theta_{\vec{i}}=\theta_{i_1}\dots \theta_{i_k}$ and $d^-_{\vec{i}}\in Hom_{\CC[\calZ]}(\tilde{M},\tilde{M})$, $\partial_{\vec{i}}^-\in Hom(\Lambda^\bullet \frn,\Lambda^{<\bullet}\frn)\otimes Hom_{\CC[\calZ]}(\tilde{M},\tilde{M})$.

Let us use notation $D_{tot}:=d^++D+\partial+d^-+\partial^-+d_{ce}$. There are three types of (generalized) row transformations for the complex $(\calF_\bullet,d^++D+d^-,\partial+\partial^-)$. The first type is given by automorphism $\exp(\phi\frac{\partial}{\partial\theta_k})$, $\phi\in \Hom_{\CC[\calZ]}(\calF,\calF)$ is an odd automorphism and the affect of this automorphism on the differential is: $$\begin{gathered}
  \exp(-\phi\frac{\partial}{\partial \theta_k})\circ D_{tot}\circ \exp(\phi\frac{\partial}{\partial \theta_k})= \left(D+d_-+d_++[\phi,D]_+\frac{\partial}{\partial \theta_k}+f_k\phi\right)\\
 +d_{ce}+\partial+\partial^-+[\phi,d_{ce}+\partial+\partial_-]_+\frac{\partial}{\partial\theta_k}.
\end{gathered}$$ That is the result of the row transformation of the first type is the equivariant matrix factorization $$(\tilde{M},D+d_-+d_++[\phi,D]_+\frac{\partial}{\partial \theta_k}+f_k\phi,\partial+\partial^-+[\phi,d_{ce}+\partial+\partial_-]_+\frac{\partial}{\partial\theta_k}).$$

The second type elementary row transformation is given by conjugation by the automorphism $\exp(\phi\theta)$. The result of conjugation of $D_{tot}$ by this automorphims is the following expression $$\exp(-\phi\theta_k)\circ D_{tot}\circ\exp(\phi\theta_k)=D_{tot}+D'+\partial'.$$ $$\label{eq: sec row 1}
D'=[\phi,D]_+\theta_k+\sum_{k\in \vec{i} }d^-_{\vec{i}}\phi\frac{\partial}{\partial\widehat{\theta}_{\vec{i}}}+\theta_k\sum_{\vec{i}}[\phi,d^-_{\vec{i}}]\frac{\partial}{\partial\theta_{\vec{i}}},$$ $$\label{eq: sec row 2}
\partial'=\sum_{k\in \vec{i} }\partial^-_{\vec{i}}\phi\frac{\partial}{\partial\widehat{\theta}_{\vec{i}}}+\phi d_{ce}^k+
\theta_k(\sum_i[\phi,d_{ce}^i]\frac{\partial}{\partial\theta_i}+[\phi,\partial]_+ +\sum_{\vec{i}}[\phi,\partial^-_{\vec{i}}]\frac{\partial}{\partial\theta_{\vec{i}}}),$$ where $\partial\widehat{\theta}_{\vec{i}}=\partial \theta_{i_1}\dots \widehat{\partial\theta_k}\dots\partial_{i_m}$, $\vec{i}=(i_1,\dots,i_m)$ and $d_{ce}=\sum_i d_{ce}^i\frac{\partial}{\partial \theta_i}.$

The computation above indicates that if last summands in ([\[eq: sec row 1\]](#eq: sec row 1){reference-type="ref" reference="eq: sec row 1"}) and ([\[eq: sec row 2\]](#eq: sec row 2){reference-type="ref" reference="eq: sec row 2"}) vanish $$\label{eq: adm row tr}
\sum_{\vec{i}}[\phi,d^-_{\vec{i}}]\frac{\partial}{\partial\theta_{\vec{i}}}=0,\quad \sum_i[\phi,d_{ce}^i]\frac{\partial}{\partial\theta_i}+[\phi,\partial]_+ +\sum_{\vec{i}}[\phi,\partial^-_{\vec{i}}]\frac{\partial}{\partial\theta_{\vec{i}}}=0$$ then result of the row transformation is the equivariant matrix factorization: $$(\tilde{M},d^++D+d^-+[\phi,D]_+\theta_k+\sum_{k\in \vec{i} }d^-_{\vec{i}}\phi\frac{\partial}{\partial\widehat{\theta}_{\vec{i}}},\partial+\partial^-+\sum_{k\in \vec{i} }\partial^-_{\vec{i}}\phi\frac{\partial}{\partial\widehat{\theta}_{\vec{i}}}+\phi d_{ce}^k)$$

Finally the third type of row operation is given by automorphism $\exp(c\theta_i\frac{\partial}{\partial\theta_j})$ where $c\in \Hom_{\CC[\calZ]}(\calF,\calF)$ is an even morphism. This type of row transformation was discussed in the subsection [\[ssec: str eq Kosz\]](#ssec: str eq Kosz){reference-type="ref" reference="ssec: str eq Kosz"} for strongly equivariant matrix factorizations. We will use these type row operations only for strongly equivariant matrix factorization and omit a discussion about complications that arise for weakly equivariant generalized Koszul complexes.

The key feature of the row transformations discussed here is that differentials that encode the equivariant structure of the matrix factorization do not contribute to the change of the non-equivariant shadow of the matrix factorization. Other words, if $T$ is one the transformations discussed above then $$T(\calF)^\sharp=T(\calF^\sharp).$$

## Proof of proposition [\[prop: Knorrer factor\]](#prop: Knorrer factor){reference-type="ref" reference="prop: Knorrer factor"}

Let us expand the definition of convolution to obtain the following expression for $\pi_{12}^*(\Phi(\calF)^\sharp)\otimes\pi_{23}^*(\Phi(\calG)^\sharp)$: $$\begin{gathered}
\label{eq: long MF}
\pi_{12}^*(\bar{\pi}^*(\calF^\sharp)\otimes CC)\otimes\pi_{23}^*(\bar{\pi}^*(\calG^\sharp)\otimes CC)\\
=(\pi_{12}\circ\bar{\pi})^*(\calF^\sharp)\otimes (\pi_{23}\circ\bar{\pi})^*(\calG^\sharp)\otimes \pi_{12}^*(CC)\otimes\pi^*_{23}(CC).
\end{gathered}$$ The last factor is the Koszul complex $\begin{bmatrix} (\tilde{X}^2_{--} )& (Y_{2}-\Ad_{g_{23}}(Y_3)_{++})\end{bmatrix}$ hence we can use row transformations of second type to eliminate variables $Y_2$ from the matrix factorization ([\[eq: long MF\]](#eq: long MF){reference-type="ref" reference="eq: long MF"}). More precisely, use the row transformations of the second type to eliminate $Y_2$ from the first factor $(\pi_{12}\circ \bar{\pi})^*(\calF)$ and from the second to last factors $\pi_{12}^*(CC)$.

We can apply the second type of row transformation because $(\pi_{12}\circ \bar{\pi})^*(\calF^\sharp)$ and $\pi_{12}^*(CC)$ are the factors of $\pi^*_{12}(\Phi(\calF)^\sharp)$, thus differentials in these matrix factorizations commute with the differentials from the factor $\pi^*_{23}(\Phi(\calG)^\sharp)$ and hence the admissibility condition ([\[eq: adm row tr\]](#eq: adm row tr){reference-type="ref" reference="eq: adm row tr"}) is satisfied. On the other hand, the second factor $(\pi_{23}\circ\bar{\pi})^*(\calG^\sharp)$ has no dependence on $Y_2$.

The result of elimination of $Y_2$ from the factor before the last is $$CC_{123}=[\tilde{X}_{1,--}, Y_1-\Ad_{g_{12}}(\Ad_{g_{23}}(Y_3)_{++})_{++}]$$ and the first two factors are $$\begin{gathered}
\pi^*_{12}(\bar{\pi}^*(\calF))|_{Y_2=\Ad_{g_{23}}(Y_3)_{++}}=\calF|_{Y=\Ad_{g_{23}}(Y_3)_{++},X_+=\tilde{X}_{1,+}}=\bar{\pi}^*_{con}(\bar{\pi}_{12}^*(\calF))\\
\pi^*_{23}(\bar{\pi}^*(\calG))|_{Y_2=\Ad_{g_{23}}(Y_3)_{++}}=\calG|_{Y=Y_3,X_+=\Ad_{g_{12}}^{-1}(\tilde{X}_{1})_+},
\end{gathered}$$ where $(X_+,g_{12},g_{23},Y)$ are coordinates on $\calXr_3$. After the elimination the only term that has dependence on $Y_2$ is the Koszul complex $\begin{bmatrix} G& (Y_{2}-\Ad_{g_{23}}(Y_3)_{++})\end{bmatrix}$ and since $\pi_{13}^*(W)$ does not depend on $Y_2$ and the correction correction differentials $\partial$, which could depend on $Y_2$ does not contribute the square of the total differential, the element $G$ must vanish.

As the next step we use the complex $CC_{123}$ to eliminate dependence on $\tilde{X}_{1,--}$ from the other terms in the tensor product ([\[eq: long MF\]](#eq: long MF){reference-type="ref" reference="eq: long MF"}). For that we use the first type of row transformation and we do not need to worry about the admissibility of our eliminations. The term $\bar{\pi}^*_{con}(\bar{\pi}_{12}^*(\calF))$ has no dependence on $\tilde{X}_{1,--}$ so it is not affected by this elimination. On the other hand the second term becomes: $$\calG|_{Y=Y_3,X_+=\Ad_{g_{12}}^{-1}(\tilde{X}_{1})_+, \tilde{X}_{1,--}=0}= \calG|_{Y=Y_3,X_+=\Ad_{g_{12}}^{-1}(\tilde{X}_{1,+})_+}=\bar{\pi}^*(\bar{\pi}_{23}^*(\calG)).$$

After this round of elimination the only dependence on $\tilde{X}_{1,--}$ in ([\[eq: long MF\]](#eq: long MF){reference-type="ref" reference="eq: long MF"}) comes from the Koszul complex $[\tilde{X}_{1,--},G']$ hence $G'$ must be the derivative of $\pi_{13}^*(W)$ by $\tilde{X}_{1,--}$ that is $G'=Y_1-\Ad^{-1}_{g_{13}}(Y_3).$ That is after the eliminations $Y_2,\tilde{X}_{1,--}$ we obtain the complex $$\label{eq: last step red}
 \bar{\pi}^*\left(\bar{\pi}_{12}^*(\calF)\otimes\bar{\pi}_{23}^*(\calG)\right)\otimes [Y_2 -\Ad_{g_{23}}(Y_3)_{++},0]\otimes \pi_{13}^*(CC)$$ as we claimed in the proposition.
