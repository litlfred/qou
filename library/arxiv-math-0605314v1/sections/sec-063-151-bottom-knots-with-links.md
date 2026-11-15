---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-063-151-bottom-knots-with-links
section_title: "Bottom knots with links"
section_number: 15.1
pages: 57-59
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.949
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:bottom-knots-with label="sec:bottom-knots-with"}

Let $T=T_0\cup L_1\cup \cdots\cup L_l$ be a tangle in a cube consisting of a bottom knot $T_0$ and an algebraically-split, $0$-framed link $L_1\cup \cdots\cup L_l$, where $\lk(T_0,L_i)=0$ for $i=1,\ldots,l$. For $x_1,\ldots,x_l\in \modP$, we define $J_T(x_1,\ldots,x_l)$ as follows. Let $T'=T_0\cup T_1\cup \cdots\cup T_l$ denote an $(l+1)$-component bottom tangle such that $T$ is obtained from $T'$ by closing the components $T_1,\ldots,T_l$. Set $$J_T(x_1,\ldots,x_l) = (1\otimes \trq^{x_1}\otimes \cdots\otimes \trq^{x_l})(J_{T'}),$$ which is well-defined, i.e., does not depend on the choice of $T'$.

For $m\ge 0$, define $F_m(Z(\Uqv))$ as the $\modZ [q,q^{-1}]$-subalgebra of $Z(\Uqv)$ consisting of the elements $\sum_{k\ge 0}a_k\sigma _k$, where $a_k\in \modZ [q,q^{-1}]$ for $k\ge 0$ and if $0\le k\le m$ then $a_k$ is divisible by $\frac{\{2m+1\}_{q,m+1}}{\{2k+1\}_{q,k+1}}$. The $F_m(Z(\Uqv))$ are a descending filtration of ideals in $Z(\Uqv)$. We have a natural isomorphism $$\varprojlim_{m} Z(\Uqv)/F_{m}(Z(\Uqv)) \cong Z(\hUqv).$$ (Indeed, both are naturally isomorphic to $\varprojlim_{k,l}Z(\Uqv)/((q)_k,\sigma _l)$.)

::: proposition
[]{#r76 label="r76"} Let $T$ be as above. Let $m_1,\ldots,m_l\ge 0$. Then we have $$J_{T}(\tP'_{m_1},\ldots,\tP'_{m_l})\in  F_m(Z(\Uqv)),$$ where $m=\max(m_1,\ldots,m_l)$.
:::

::: proof
*Proof.* Let $g_k\in \modZ [q,q^{-1}]$, $k\ge 0$, be such that $\sum_{k\ge 0}g_k\sigma _k=J_T(\tP'_{m_1},\ldots,\tP'_{m_l})$. By an argument similar to the proof of Theorem [\[r18\]](#r18){reference-type="ref" reference="r18"}, we have $g_k=\trq^{P''_k}(J_T(\tP'_{m_1},\ldots,\tP'_{m_l}))$. Let $L$ denote the link obtained from $T$ by closing $K$. Then we have $$g_k=\trq^{P''_k}(J_T(\tP'_{m_1},\ldots,\tP'_{m_l}))=J_L(P''_k,\tP'_{m_1},\ldots,\tP'_{m_l}).$$ It follows from Theorem [\[r29\]](#r29){reference-type="ref" reference="r29"} that if $0\le k\le m$ then $g_k$ is divisible by $\frac{\{2m+1\}_{q,m+1}}{\{2k+1\}_{q,k+1}}$. Hence, we have the assertion. ◻
:::

::: corollary
[]{#r77 label="r77"} Let $T$ be as above. Then $J_T\zzzcolon \modP \times \cdots\times \modP \rightarrow Z(\Uqv)$, $(x_1,\ldots,x_l)\mapsto J_T(x_1,\ldots,x_l)$, induces a well-defined $\modZ [q,q^{-1}]$-multilinear map $$J_T\zzzcolon \hP\times \cdots\times \hP\rightarrow Z(\hUqv).$$
:::

Let $L=\cl(T_0)\cup L_1\cup \cdots\cup L_l$ be the link obtained from $T$ closing $T_0$. Then we set $$J_L(*,x_1,\ldots,x_l)=J_T(x_1,\ldots,x_l)\in Z(\hUqv)$$ for $x_1,\ldots,x_l\in \hP$. Thus "$*$" means "keep the element in this place".

## The invariant $J_{(M,K)}$ {#sec:invariant-jm-k}

Let $(M,K)$ be a pair of an integral homology sphere $M$ and a $0$-framed knot $K\subset M$. Choose an algebraically-split framed link $L=K'\cup L_1\cup \cdots\cup L_l$ in $S^3$ such that

1.  the framing of $L_i$ is $f_i\in \{\pm 1\}$,

2.  $(S^3,K')_{L_1\cup \cdots\cup L_l}\cong (M,K)$.

$L$ is called a *surgery presentation* for $(M,K)$.

::: theorem
[]{#r79 label="r79"} Set $$\label{e87}
    J_{(M,K)} = J_L(*,\omega ^{-f_1},\ldots,\omega ^{-f_l})\in Z(\hUqv).$$ Then $J_{(M,K)}$ is a well-defined invariant of the pair $(M,K)$.
:::

::: proof
*Proof.* (Sketch) The shortest way to prove the well-definedness of $J_{(M,K)}$ (i.e., independence from the choice of $L$) may be to consider the elements $\mods _\zeta (J_{(M,K)}(\V'_k))$ for $k\ge 0$ and $\zeta \in \calZ$, where $\V'_k=\V_k/[k+1]$. One can prove that this quantity is equal to the normalized WRT invariant of $(M,K)$ at $\zeta$ with $K$ colored by the $\V'_k$. It follows from Proposition [\[r85\]](#r85){reference-type="ref" reference="r85"} that $J_{(M,K)}(\V'_k)$ is a well-defined invariant of $(M,K)$. Therefore, $J_{(M,K)}(P''_k)$ for $k\ge 0$ are also well-defined, hence so is $J_{(M,K)}$. ◻
:::

::: remark
[]{#r78 label="r78"} Another way to prove Theorem [\[r79\]](#r79){reference-type="ref" reference="r79"} is to use a "pair version" of Theorem [\[r32\]](#r32){reference-type="ref" reference="r32"}: *Two surgery presentations (in the above sense) of pairs of integral homology spheres and knots yield orientation-preserving homeomorphic results of surgery if and only if they are related by a sequence of stabilizations and Hoste moves. Here a Hoste move is defined to be a Fenn-Rourke move (see Figure [\[fig:FR\]](#fig:FR){reference-type="ref" reference="fig:FR"}) between two surgery presentations.* (One can generalize this result to to links and tangles (in a homology ball).)

In view of this result, one has only to show that the right-hand side of [\[e87\]](#e87){reference-type="eqref" reference="e87"} is invariant under a Hoste move. To prove this invariance, one has to consider the "evaluations" at $\V_k$ for $k\ge 0$ as in the proof of Theorem [\[r79\]](#r79){reference-type="ref" reference="r79"}, but one does not have to consider the evaluations at roots of unity.
:::

::: remark
[]{#r37 label="r37"} Yet another, conceptually more interesting, way to prove Theorem [\[r79\]](#r79){reference-type="ref" reference="r79"} is to extend the domain of definition of the invariant to "bottom tangles in homology handlebodies". See Section [\[sec:homology-cylinders\]](#sec:homology-cylinders){reference-type="ref" reference="sec:homology-cylinders"} for some explanation.
:::
