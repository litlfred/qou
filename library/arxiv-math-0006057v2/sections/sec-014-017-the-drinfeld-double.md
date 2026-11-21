---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-014-017-the-drinfeld-double
section_title: "The Drinfeld double"
section_number: 0.17
pages: 19-20
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.924
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
To define the *Drinfeld double* $D(H)$ of a quantum groupoid $H$, consider on the vector space $\widehat H^{op}\otimes_k H$ an associative multiplication $$(\phi\otimes h)(\psi\otimes g) =
\psi_{(2)}\phi \otimes h_{(2)} g \langle\,S(h_{(1)}),\, \psi_{(1)}\,\rangle\langle\,h_{(3)},\, \psi_{(3)}\,\rangle,$$ where $\phi, \psi \in \widehat H^{op}$ and $h,g \in H$. Then one can verify that the linear span $J$ of the elements $$\begin{aligned}
\label{amalgamation}
\phi\otimes zh &-& (\varepsilon\leftharpoonup z)\phi \otimes h, \quad z\in H_t,\\
\phi\otimes yh &-& (y\rightharpoonup\varepsilon)\phi \otimes h, \quad y\in H_s,
\end{aligned}$$ is a two-sided ideal in $\widehat H^{op}\otimes_k H$. Let $D(H)$ be the factor-algebra $(\widehat H^{op}\otimes_k H)/J$ and let $[\phi\otimes h]$ denote the class of $\phi\otimes h$ in $D(H)$.

::: proposition
[]{#the double label="the double"} $D(H)$ is a quantum groupoid with the unit $[\varepsilon\otimes 1]$, and comultiplication, counit, and antipode given by $$\begin{aligned}
\Delta([\phi\otimes h])
&=& [\phi_{(1)} \otimes h_{(1)}] \otimes [\phi_{(2)} \otimes h_{(2)}],\\
\varepsilon([\phi\otimes h])
&=& \langle\,\varepsilon_t(a),\,\phi \,\rangle,\\
S([\phi\otimes a])
&=& [ S^{-1}(\phi_{(2)}) \otimes S(h_{(2)})] \langle\,h_{(1)},\,\phi_{(1)} \,\rangle
   \langle\,S(h_{(3)}),\,\phi_{(3)}\,\rangle.
\end{aligned}$$
:::

::: proof
*Proof.* The proof is a straightforward verification that all the structure maps are well-defined and satisfy the axioms of a quantum groupoid, which is carried out in full detail in ([@NTV], 6.1). ◻
:::

::: proposition
[]{#QT of D(H) label="QT of D(H)"} The Drinfeld double $D(H)$ has a canonical quasitriangular structure given by $$\label{R-matrix}
{\mathcal R}= \sum_i [\xi^i \otimes 1] \otimes [\varepsilon\otimes f_i],
\qquad
{\bar {\mathcal R}}= \sum_j\, [S^{-1}(\xi_j) \otimes 1] \otimes[\varepsilon\otimes f_j]$$ where $\{ f_i\}$ and $\{ \xi^i\}$ are bases in $H$ and $\widehat H$ such that $\langle\,f_i,\, \xi^j\,\rangle=\delta_{ij}$.
:::

::: proof
*Proof.* The identities $(\mbox{id}\otimes \Delta){\mathcal R}= {\mathcal R}_{13}{\mathcal R}_{12}$ and $(\Delta \otimes \mbox{id}){\mathcal R}= {\mathcal R}_{13}{\mathcal R}_{23}$ can be written as (identifying $[(\widehat H)^{op}\otimes 1]$ with $(\widehat H)^{op}$ and $[\varepsilon\otimes H]$ with $H$) : $$\begin{aligned}
\sum_i\, \xi_{(1)}^i \otimes \xi_{(1)}^i \otimes f_i &=&
\sum_{ij}\, \xi^i \otimes \xi^j \otimes f_i f_j, \\
\sum_i\, \xi^i \otimes {f_i}_{(1)}  \otimes {f_i}_{(2)} &=&
\sum_{ij}\, \xi^j \xi^i \otimes f_j \otimes f_i.
\end{aligned}$$ The above equalities can be verified, e.g., by evaluating both sides against an element $a\in H$ in the third factor (resp., against $\phi\in(\widehat H)^{op}$ in the first factor), see ([@Ma], 7.1.1). It is also straightforward to check that ${\mathcal R}$ is an intertwiner between $\Delta$ and $\Delta^{op}$ and check that ${\bar {\mathcal R}}{\mathcal R}= \Delta(1)$ and ${\mathcal R}{\bar {\mathcal R}}= \Delta^{op}(1)$, see ([@NTV], 6.2). ◻
:::

::: remark
[]{#dual double label="dual double"} The dual quantum groupoid $\widehat{D(H)}$ consists of all $\sum_k\, h_k\otimes \phi_k$ in $H\otimes_k {\widehat H}^{op}$ such that $$\sum_k\, (h_k\otimes \phi_k)|_J = 0.$$ The structure operations of $\widehat{D(H)}$ are obtained by dualizing those of $D(H)$: $$\begin{aligned}
(  \sum_k\, h_k\otimes \phi_k ) (  \sum_l\, g_l\otimes \psi_l )
&=& \sum_{kl}\, h_kg_l\otimes \phi_k \psi_l, \\
1_{\widehat{D(H)}}
&=& 1_{(2)} \otimes (\varepsilon\leftharpoonup 1_{(1)}), \\
\Delta(\sum_k\, h_k\otimes \phi_k )
&=& \sum_{ijk}\, ({h_k}_{(2)} \otimes \xi^i {\phi_k}_{(1)} \xi^j) \otimes
    (S(f_i) {h_k}_{(1)} f_j \otimes {\phi_k}_{(2)}), \\
\varepsilon(  \sum_k\, h_k\otimes \phi_k )
&=& \sum_k\,\varepsilon(h_k)\widehat\varepsilon(\phi_k),\\
S(  \sum_k\, h_k\otimes \phi_k )
&=& \sum_{ijk}\, f_i S^{-1}(h_k)S(f_j) \otimes \xi^i S(\phi)\xi^j,
\end{aligned}$$ for all $\sum_k\, h_k\otimes \phi_k,\, \sum_l\, g_l\otimes \psi_l \in
\widehat{D(H)}$, where $\{ f_i\}$ and $\{\xi^j\}$ are dual bases.
:::

::: corollary
[]{#D(H) is factorizable label="D(H) is factorizable"} The Drinfeld double $D(H)$ is factorizable in the sense of Definition [\[factorizability\]](#factorizability){reference-type="ref" reference="factorizability"}.
:::

::: proof
*Proof.* One can use the explicit form of the $R$-matrix ([\[R-matrix\]](#R-matrix){reference-type="ref" reference="R-matrix"}) of $D(H)$ and the description of the dual $\widehat{D(H)}$ to check that in this case the map $F$ from ([\[map F\]](#map F){reference-type="ref" reference="map F"}) is surjective. ◻
:::
