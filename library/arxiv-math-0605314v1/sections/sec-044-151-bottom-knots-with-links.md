---
doc_id: arxiv-math-0605314v1
doc_title: "arXiv:math/0605314v1 [math.GT] 11 May 2006"
section_id: sec-044-151-bottom-knots-with-links
section_title: "Bottom knots with links"
section_number: 15.1
pages: 57-61
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.97
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

## Surgery along a knot with framing $1/m$ {#sec:surgery-along-knot}

Kirby and Melvin proved periodicity results for the WRT invariant of integral homology spheres obtained from $S^3$ by surgery along a knot with framings $1/m$ (Corollaries 8.15 and 8.26 of [@Kirby-Melvin]). We have the following generalization.

::: theorem
[]{#r9 label="r9"} Let $K$ be a knot in an integral homology sphere $M$. Let $M'=M_{K;1/m}$ be the result of surgery from $M$ along $K$ with framing $1/m$ with $m\in \modZ$. Then we have $$J_{M'}\equiv J_M \pmod{(q^{2m}-1)}.$$
:::

::: proof
*Proof.* One way to prove the assertion is first to prove $\tau _\zeta (M')=\tau _\zeta (M)$ for all $\zeta \in \calZ$ with $\ord(\zeta )|2m$ and then to use Section [\[sec:divis-ring-zqh\]](#sec:divis-ring-zqh){reference-type="ref" reference="sec:divis-ring-zqh"}. The former is a natural generalization of Kirby and Melvin's result, and is not difficult to prove. Here we give a direct proof.

We express $M$ as the result of surgery $S^3_{L}$ along an admissible framed link $L=L_1\cup \cdots\cup L_l$ in $S^3$, with framings $f_1,\ldots,f_l\in \{\pm 1\}$. We may assume that $K$ corresponds to a knot $K'\subset S^3\setminus L$ such that $K'\cup L$ is algebraically split. By puncturing $S^3$ at a point of $K'$, we obtain a bottom knot $T$ and a link $L$ in a cube, so that closing $T$ yields $K'\cup L$. We have $$\begin{split}
      J_{M'}-J_M
      &= J_{K\cup L^0}(\omega ^{-m},\omega ^{-f_1},\ldots,\omega ^{-f_l})
      -J_{K\cup L^0}(1,\omega ^{-f_1},\ldots,\omega ^{-f_l})\\
      &= J_{K\cup L^0}(\omega ^{-m}-1,\omega ^{-f_1},\ldots,\omega ^{-f_l})\\
      &= \trq^{\omega ^{-m}-1}(J_{T\cup L^0}(\omega ^{-f_1},\ldots,\omega ^{-f_l})),
    \end{split}$$ where $L^0$ is $L$ with $0$ framings. In view of the last subsection, we have $$J_{T\cup L^0}(\omega ^{-f_1},\ldots,\omega ^{-f_l})=\sum_{k\ge 0}a_k\sigma _k,$$ where $a_k\in \Zqh$ for $k\ge 0$. It suffices to prove that $\trq^{\omega ^{-m}-1}(\sigma _k)\in (q^{2n}-1)\Zqh$ for each $k\ge 0$. We have $$\trq^{\omega ^{-m}-1}(\sigma _k)=\langle \omega ^{-m}-1,S_k\rangle 
    =\langle \omega ^{-m}-1,\sum_{i=0}^{k}b_{k,i}\V_{2i}\rangle ,$$ where $b_{k,i}\in \Zqq$. We have $$\langle \omega ^{-m}-1,\V_{2i}\rangle =(q^{-i(i+1)m}-1)[2i+1]\in (q^{2m}-1)\Zqq.$$ Hence, the assertion follows. ◻
:::

## Cyclotomic finite type invariants of integral homology spheres {#sec:cycl-finite-type}

Kricker and Spence [@Kricker-Spence] (see also [@Ohtsuki4]) proved that for integral homology spheres the Ohtsuki series $\tau ^O(M)$ modulo $(q-1)^{k+1}$ is a finite type invariant of degree $3k$ in the sense of Ohtsuki [@Ohtsuki6]. It would be natural to ask the topological meaning of $J_M\mod \Phi _d(q)$ for $d\in \Funz$, where $\Funz$ denote the set of functions from $\modN =\{1,2,\ldots\}$ into $\modZ _+=\{0,1,\ldots\}$ vanishing for all but finitely many elements of $\modN$. $J_M\mod \Phi _d(q)$ is not an Ohtsuki finite type invariant in general. Thus it would be interesting to have a variant of the notion of Ohtsuki finite type invariants in which $J_M\mod \Phi _d(q)$ is of "finite type". In what follows, we give a conjectural definition of such a notion of finite type.

Let $\modM$ denote the set of orientation-preserving homeomorphism classes of integral homology spheres. Let $\modZ \modM$ denote the free abelian group generated by $\modM$, which has a standard ring structure with multiplication induced by connected sum. The *Ohtsuki filtration* $$\modZ \modM =F_0\supset F_1\supset F_2\supset \cdots$$ is defined as follows. For $k\ge 0$, let $F_k$ denote the $\modZ$-submodule of $\modZ \modM$ spanned by the alternating sums $$=\sum_{L'\subset \{L_1,\ldots,L_k\}}(-1)^{|L'|}M_{L'}$$ for all pairs of $M\in \modM$ and algebraically-split, $\pm 1$-framed links $L=\{L_1,\ldots,L_k\}$ in $M$. Here the sum runs over all the sublinks $L'$ of $L$, $|L'|$ denotes the number of components of $L'$, and $M_{L'}$ denotes the result from $M$ of surgery along $L'$. A $\modZ$-linear map $f\zzzcolon \modZ \modM \rightarrow A$ with $A$ an abelian group is called an *Ohtsuki invariant of type $k$* if $f|_{F_{k+1}}=0$.

Now we generalize the notion of finite type. For $d\in \Funz$, let $F_d$ denote the $\modZ$-submodule of $\modZ \modM$ generated by the alternating sums $[M;L_1,\ldots,L_k]$, where $M\in \modM$ and $L=\{L_1,\ldots,L_k\}$ is an algebraically-split framed link in $M$ with framings in $\{1/m\zzzvert m\in \modZ ,m\neq0\}$ such that for each $n\in \modN$ there is exactly $d(n)$ components of $L$ of framing $\pm n$. One sees easily that the $F_d$, $d\in \Funz$, form an inverse system of $\modZ$-submodules of $\modZ \modM$. Note that for $k\ge 0$, $F_k$ is equal to $F_{d_k}$, where $d_k(n)=k\delta _{n,1}$.

A $\modZ$-linear map $f\zzzcolon \modZ \modM \rightarrow A$ with $A$ an abelian group is said to be of *cyclotomic finite type* if $f|F_d=0$ for some $d$.

Theorem [\[r9\]](#r9){reference-type="ref" reference="r9"} implies that for all $m\in \modN$, $J_M\mod (q^m-1)$, is of cyclotomic finite type. It follows that for all $\zeta \in \calZ$, the WRT invariant $\tau _\zeta (M)$ is of cyclotomic finite type.

::: conjecture
[]{#r75 label="r75"} For each $d\in \Funz$, there is $d'\in \Funz$ such that the ring homomorphism $$J\zzzcolon \modZ \modM \rightarrow \Zqh,\quad M\mapsto J_M,$$ maps $F_{d'}$ into $\Phi _d(q)\Zqh$. Thus $J_M\mod(\Phi _d(q))$ is of cyclotomic finite type. Consequently, $J$ induces a continuous ring homomorphism $$J\zzzcolon \widehat{\modZ \modM } \rightarrow  \Zqh,$$ where $$\widehat{\modZ \modM }= \varprojlim_{d\in \Funz}\modZ \modM /F_d.$$
:::

If $M$ is an integral homology sphere and if $d\in \Funz$, then there is an integral homology sphere $M'$ not homeomorphic to $M$, such that $M-M'\in F_d$. Indeed, if $L$ is an algebraically-split, Brunnian framed link in $M$ with framings in $\{1/m\zzzvert m\in \modZ ,m\neq0\}$ such that for each $n\in \modN$ there are at least $d(n)$ components of $L$ of framings $\pm n$, then one can show that $M_L-M\in F_d$ by modifying a well-known arguments in the study of Ohtsuki finite type invariants. For a certain type of Brunnian links (e.g., iterated Bing doubles of Borromean rings), one can show that $M_L$ and $M$ are not homeomorphic, using the Le-Murakami-Ohtsuki invariant [@LMO].

Recall that for integral homology spheres $M$ the Le-Murakami-Ohtsuki invariant $Z^{\LMO}(M)$ is a "universal finite type invariant" [@Le6], i.e., every Ohtsuki finite type invariant factors through $Z^{\LMO}(M)$. It would be interesting to have a "cyclotomic finite type" version $Z^{\operatorname{cyc}}(M)$ of the Le-Murakami-Ohtsuki invariant which recovers *via ring homomorphisms* the unified $sl_2$ invariant $J_M$ (as well as the invariant for the other simple Lie algebras, see Section [\[sec:general\]](#sec:general){reference-type="ref" reference="sec:general"} below) and the Le-Murakami-Ohtsuki invariant $Z^{\LMO}(M)$. As we mentioned in the introduction, $Z^{\LMO}(M)$ determines $J_M$. However, this determination is not via a ring homomorphism, i.e., there is no natural homomorphism from the ring $\mathcal A(\emptyset)$, in which the Le-Murakami-Ohtsuki invariant takes values, into $\Zqh$.

::: remark
[]{#r38 label="r38"} Similarly to the Cochran and Melvin's generalization [@Cochran-Melvin:finitetype] of the Ohtsuki finite type invariants, one can generalize the above definition of "cyclotomic finite type" to oriented, connected $3$-manifolds by using surgeries along null-homologous, algebraically-split framed links with framings in $\{1/m\zzzvert m\in \modZ ,m\neq0\}$. It would be natural to expect that the generalization of $J_M$ to rational homology spheres defined in [@Beliakova-Blanchet-Le; @Le4] (see Section [\[sec:rati-homol-spher\]](#sec:rati-homol-spher){reference-type="ref" reference="sec:rati-homol-spher"} below) modulo $(\Phi _d(q))$, $d\in \Funz$, would be of "cyclotomic finite type" in the above-explained sense.
:::
