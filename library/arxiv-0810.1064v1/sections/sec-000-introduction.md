---
doc_id: arxiv-0810.1064v1
doc_title: "Multiple polylogarithm values at roots of unity"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 0810.1064v1.pdf
source_sha256: b2d7514c5382ceaa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 1.0
doc_brief: "Multiple polylogarithm values at roots of unity — For any positive integer N let µN be the group of the Nth roots of unity."
---
Double shuffle relations have played significant roles in the study of multiple zeta values in recent years. These relations can be easily generalized to the special values of multiple polylogarithms at roots of unity (MPV for short): $$\label{equ:seriesdefn}
Li_{s_1,\dots,s_n}(\zeta_1,\dots,\zeta_n):=\sum_{k_1>\dots>k_n>0}
\frac{\zeta_1^{k_1} \cdots \zeta_n^{k_n}}{k_1^{s_1}\cdots k_n^{s_n}},\quad(s_1,\zeta_1)\ne (1,1),$$ where $\zeta_j$ are all $N$th roots of unity for $j=1,\dots,n$. We call $N$ the *level* and $w:=s_1+\cdots+s_n$ the *weight*. One of our major interests is to find the dimension $d(w,N)$ of the $\Q$-vector space $\MPV(w,N)$ spanned by these values.

In [@Rac], Racinet listed the following relations: double shuffle relations and their regularized versions (by regularizing both the divergent integrals and divergent series representing MPVs), (regularized) distributions, and weight one relations. We will call these *standard relations*. By intensive MAPLE computation it is shown [@Zpolyrel] that in many cases these relations cannot produce all the possible $\Q$-linear relations. For example, standard relations imply only $d(3,4)\le 9$ which is one more than the bound given by [@DG 5.25]. Concretely, from standard relations MAPLE confirms the following $$\label{fact}
\aligned
 \text{Fact: }&\text{Every MPV of weight 3 and level 4 can be written explicitly} \\
 &\text{as a linear combination of the nine MPVs appearing in \eqref{equ:conj},}
\endaligned
\tag{$\ast$}$$ and no further $\Q$-linear relations between these values can be deduced from the standard relations. But by GiNac [@GiNac] and EZface [@EZface] the following is found numerically (see [@Zpolyrel Remark 10.1]) $$\begin{gathered}
\label{equ:conj}
5Li_{1,2}(-1,-i)=46Li_{1,1,1}(i,1,1)-7Li_{1,1,1}(-1,-1,i)-13Li_{1,1,1}(i,i,i) +13Li_{1,2}(-i,i)\\
-Li_{1,1,1}(-i,-1,1)+25Li_{1,1,1}(-i,1,1)-8Li_{1,1,1}(i,i,-1) +18Li_{2,1}(-i,1).
\end{gathered}$$ In this note, we shall prove [\[equ:conj\]](#equ:conj){reference-type="eqref" reference="equ:conj"} from the explicit relations in [\[fact\]](#fact){reference-type="eqref" reference="fact"} by using the octahedral symmetry of ${\mathbb P}^1-(\{0,\infty\}\cup \mmu_4)$ where $\mmu_N$ denotes the set of $N$th roots of unity. We can treat the weight 4 and level 4 case in a similar fashion.

The result above in level four case shows that the standard relations are not always sufficient to determine $d(w,N)$. On the other hand, Deligne and Goncharov [@DG] find some closed formulae for upper bounds of $d(w,N)$ for all $w$ and $N$ by studying the motivic fundamental group of ${\mathbb P}^1-(\{0,\infty\}\cup \mmu_N)$ in the framework of mixed Tate motives over the ring of $S$-integers of a number field.

::: prop
[]{#prop:DG label="prop:DG"} *([@DG 5.25])* Let $N$ be a positive integer. Let $\varphi$ be the Euler's totient function and $\nu(N)$ be the number of prime factors of $N$. Then $d(w,N)\le D(w,N)$ where $D(w,N)$ are defined by the formal power series $$1+\sum_{w=1}^\infty D(w,N)t^w=
\left\{
    \begin{array}{ll}
      (1-t^2-t^3)^{-1}, & \hbox{if $N=1$;} \\
      (1-t-t^2)^{-1}, & \hbox{if $N=2$;} \\
     \big(1-\big(\frac{\varphi(N)}2+\nu(N)\big)t+ \big(\nu(N)-1 \big)t^2 \big)^{-1}, & \hbox{if $N\ge 3$.} \\
    \end{array}
  \right.$$
:::

As an example one can find the bound $d(w,4)\le 2^w$ for all weight $w$ and by a variant of a conjecture of Grothendieck it can be deduced that for $N=4$ equality should always hold. Further, Goncharov [@DG] has defined some pro-nilpotent Lie algebra $D$ graded by weight and depth using standard relations and then related $D$ to the motivic fundamental Lie algebra in lower depth cases. Using this we shall improve the bounds in the above proposition for all levels $N=p$ and $N=p^2$ ($p\ge 5$ a prime) in the last section. From this improved bound we find that when $7<N<50$ standard relations are incomplete if $N$ is a power of 2 or 3, or $N$ has at least two prime factors, though we don't know how to find missing relations explicitly.
