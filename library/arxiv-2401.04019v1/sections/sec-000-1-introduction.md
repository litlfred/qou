---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.922
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on truncated"
---
A partition $\lambda$ of $n$ is a non-increasing sequence $\lambda= (\lambda_1, \lambda_2, \ldots, \lambda_\ell)$ of positive integers that add up to $n$. We refer to the integers $\lambda_i$ as the parts of $\lambda$. As usual, we denote by $p(n)$ the number of partitions of $n$. Since the empty partition $\emptyset$ is the only partition of $0$, we have $p(0)=1$. For a thorough introduction to the theory of partitions we refer the reader to [@A98; @AE].

We use the Pochhammer symbol: for $n \in \mathbb N_0 \cup \{\infty\}$ $$(a;q)_n := \prod_{j=0}^{n-1} (1-a q^j).$$

The generating function for the sequence $p(n)$ is given by $$\sum_{n=0}^\infty p(n)q^n=\prod_{i=1}^\infty \frac{1}{1-q^i}=\frac{1}{(q;q)_\infty}.$$ Throughout this article, we assume $q$ is a complex number with $|q|<1$ so that all products and series converge absolutely.

The earliest theta series identity is likely Euler's pentagonal number theorem [@A98 Eq. (1.3.1)]: $$\label{epnt} \sum_{j=-\infty}^\infty (-1)^jq^{j(3j-1)/2}=(q;q)_\infty.$$ Multiplying both sides in [\[epnt\]](#epnt){reference-type="eqref" reference="epnt"} by $1/(q;q)_\infty$, leads to the recurrence relation $$p(n)=  \sum_{j=1}^\infty (-1)^{j-1} p(n-j(3j\pm 1)/2)$$ for $n\geq 1$.

In 1951, Shanks [@S1] considered a truncation of the theta series occurring in [\[epnt\]](#epnt){reference-type="eqref" reference="epnt"} and proved that $$\label{S1-trunc} \sum_{j=-k}^k(-1)^jq^{j(3j-1)/2}=\sum_{j=0}^k\frac{(-1)^j(q;q)_kq^{\binom{j+1}{2}+jk}}{(q;q)_j}.$$ With few exceptions [@S2; @A86] the subject was dormant for more than half a century. Then, in 2012, Andrews and Merca [@AM] obtained a new truncation of Euler's pentagonal number theorem. They showed that $$\label{epnt-trunc}\frac{1}{(q;q)_\infty}\sum_{j=0}^{k-1}(-1)^iq^{j(3j+1)/2}(1-q^{2j+1})=1+(-1)^{k-1}\sum_{n=1}^\infty \frac{q^{\binom{k}{2}+(k+1)n}}{(q;q)_n}
\begin{bmatrix} n-1\\k-1\end{bmatrix},$$ where $$\begin{bmatrix}
n\\k
\end{bmatrix} 
=
\begin{cases}
\dfrac{(q;q)_n}{(q;q)_k(q;q)_{n-k}} &  \text{if $0\leqslant k\leqslant n$},\\ \ \\ 
0 &\text{otherwise.}
\end{cases}$$ As explained in [@AM], combinatorially, [\[epnt-trunc\]](#epnt-trunc){reference-type="eqref" reference="epnt-trunc"} means that $$(-1)^{k-1}\sum_{j=-(k-1)}^{k}(-1)^jp(n-j(3j-1)/2)=M_k(n),$$ where $M_k(n)$ is the number of partitions of $n$ in which $k$ is the smallest integer that is not a part of the partition and there are more parts greater than $k$ than there are less than $k$.

Work of Merca [@M4 Corollary 17] shows that Shank's truncation [\[S1-trunc\]](#S1-trunc){reference-type="eqref" reference="S1-trunc"} leads to the following inequality which holds for all $n, k\geq 1$: $$\label{S1-ineq} (-1)^k \sum_{j=-k}^{k}(-1)^jp(n-j(3j-1)/2)\geq 0.$$ Xia and Zhao [@XZ] showed that the left hand side of [\[S1-ineq\]](#S1-ineq){reference-type="eqref" reference="S1-ineq"} equals the number of partitions of $n$ in which every integer less than or equal to $k$ appears as a part at least once and the first part larger than $k$ appears at least $k+1$ times.

The work of Andrews and Merca opened up the study of truncated theta series and linear partition inequalities and many articles followed. For example, Guo and Zeng [@GZ] obtained truncations of Gauss' identities [@A98 (2.2.12), (2.2.13)], and Yee [@Y] and also Wang and Yee [@WY] found a truncation of the Jacobi triple product identity $$\label{JTP_RS} \frac{1}{(q^S;q^R)_\infty(q^{R-S};q^R)_\infty(q^R;q^R)_\infty}\sum_{n=-\infty}^\infty(-1)^nq^{Rn(n-1)/2+Sn}=1,$$ where $R$ and $S$ are positive integers with $1\leq S< R/2$. Wang and Yee show explicitly that the truncations $$\begin{aligned}
\frac{1}{(q^S;q^R)_\infty(q^{R-S};q^R)_\infty(q^R;q^R)_\infty}\sum_{n=-(m-1)}^m(-1)^nq^{Rn(n-1)/2+Sn}  
\end{aligned}$$ and $$\begin{aligned}
 \frac{1}{(q^S;q^R)_\infty(q^{R-S};q^R)_\infty(q^R;q^R)_\infty}\sum_{n=-m}^m(-1)^nq^{Rn(n-1)/2+Sn},
 
\end{aligned}$$ when expanded as $q$-series, have non-negative coefficients.

Motivated by these results, Merca [@M1] investigated truncations of Jacobi's triple product written in the form $$\label{JTP_RS_M} \frac{1}{(q^S;q^R)_\infty(q^{R-S};q^R)_\infty}\sum_{n=-\infty}^\infty(-1)^nq^{Rn(n-1)/2+Sn}-(q^R;q^R)_\infty=0$$ and made a stronger conjecture.

::: conjecture
[@M1 Conjecture 4.3] []{#Conj 4.3 label="Conj 4.3"} For $1\leq S<R$, $k\geq 1$, the theta series $$\label{conj 4.3} \frac{(-1)^k}{(q^S;q^R)_\infty(q^{R-S};q^R)_\infty}\sum_{j=k}^\infty(-1)^jq^{Rj(j+1)/2-Sj}\big(1-q^{S(2j+1)}\big)$$ has non-negative coefficients.
:::

We define $$\begin{aligned}
\label{trunc-equiv} \sum_{n=0}^\infty a_{S,R,k}(n)q^n:=\frac{(-1)^{k-1}}{(q^S;q^R)_\infty(q^{R-S};q^R)_\infty}& \notag \sum_{j=0}^{k-1} (-1)^jq^{j(j+1)R/2-jS}(1-q^{(2j+1)S})\\ & -(-1)^{k-1}(q^R;q^R)_\infty, 
\end{aligned}$$ and we write $a_k(n)$ for $a_{S,R,k}(n)$ when $S$ and $R$ are clear from the context. As mentioned in [@M1], Conjecture [\[Conj 4.3\]](#Conj 4.3){reference-type="ref" reference="Conj 4.3"} is equivalent to showing $a_{S,R,k}(n)\geq 0$ for all $n\geq 0$, $k\geq 1$, $1\leq S<R$.

In this article we prove Conjecture [\[Conj 4.3\]](#Conj 4.3){reference-type="ref" reference="Conj 4.3"} for $k\in \{1,2,3\}$.

::: theorem
[]{#main label="main"} If $k\in \{1,2,3\}$ and $1\leq S<R$, then the theta series [\[conj 4.3\]](#conj 4.3){reference-type="eqref" reference="conj 4.3"} has non-negative coefficients.
:::

Let$$\label{eqn:rho}
 \rho_{R}(n):=\begin{cases}(-1)^i & \text{ if } n=Ri(3i-1)/2 \text{ for some } i\in \mathbb Z \\ 0 & \text{ otherwise.}\end{cases}$$ Then, [\[epnt\]](#epnt){reference-type="eqref" reference="epnt"} with $q$ replaced by $q^R$, implies that $(q^R;q^R)_\infty$ is the generating function for the sequence $\rho_R(n)$.

When $R=3, S=1$, for all $n\geq 0, k\geq 1$, we have $$\label{conj 4.3-b3} a_{1,3,k}(n)=(-1)^{k-1}\sum_{j=-(k-1)}^k(-1)^j b_3(n-j(3j-1)/2) - (-1)^{k-1}\rho_3(n),$$ where $b_\ell(n)$ denotes the number of $\ell$-regular partitions of $n$, i.e., partitions with no parts divisible by $\ell$.

::: remark
From [@AM Lemma 1.2] it follows that the $q$-series on the right hand side of [\[trunc-equiv\]](#trunc-equiv){reference-type="eqref" reference="trunc-equiv"} for $R=3, S=1$ equals $$(q^3;q^3)_\infty\sum_{n\geq 0}^\infty M_k(n)q^n.$$ Hence, if Conjecture [\[Conj 4.3\]](#Conj 4.3){reference-type="ref" reference="Conj 4.3"} is true for $R=3$ and $S=1$, then for $k\geq 1$, $$\sum_{j=0}^\infty (-1)^j(M_k(n-T_{3j})-M_k(n-T_{3j+2})) \geq 0,$$ where $T_j=j(j+1)/2$ is the $j$th triangular number.
:::

We prove the following related theorem, which is weaker than Conjecture [\[Conj 4.3\]](#Conj 4.3){reference-type="ref" reference="Conj 4.3"} for $R=3$, $S=1$.

::: theorem
[]{#thm:b3 label="thm:b3"} Let $k\geq 1$. Then for all $n\geq 0$, $$(-1)^{k}\sum_{j=-k}^k(-1)^j b_3(n-j(3j-1)/2) +(-1)^{k-1} \rho_{3}(n)\geq 0.$$
:::

Note that Theorem [\[thm:b3\]](#thm:b3){reference-type="ref" reference="thm:b3"} together with [\[conj 4.3-b3\]](#conj 4.3-b3){reference-type="eqref" reference="conj 4.3-b3"} shows that for all $n\geq 0$, $k\geq 1$, $$a_{1,3,k}(n)+b_3(n-k(3k-1)/2)\geq 0.$$ Following the proof of Theorem [\[thm:b3\]](#thm:b3){reference-type="ref" reference="thm:b3"} we also give a combinatorial interpretation for $a_{1,3,k}(n)+b_3(n-k(3k-1)/2)$.

Inequalities for $b_6(n)$ analogous to those in Theorem [\[thm:b3\]](#thm:b3){reference-type="ref" reference="thm:b3"} were conjectured in [@BM3]. We give a proof of the conjecture.

::: theorem
[@BM3 Conjecture 3][]{#thm:b6 label="thm:b6"} For $n\geq 0, k>0$ $$\label{eq:b6-conj}(-1)^{k-1}\left(\rho_{6}(n)-\sum_{j=-k}^k (-1)^jb_6(n-j(3j-1)/2)\right)\geq 0,$$ with strict inequality if $n\geq (k+1)(3(k+1)-1)/2$.
:::

We also give a combinatorial interpretation of the numbers on the left hand side of [\[eq:b6-conj\]](#eq:b6-conj){reference-type="eqref" reference="eq:b6-conj"}.

::: remark
In [@BM3 Conjecture 3], the inequality [\[eq:b6-conj\]](#eq:b6-conj){reference-type="eqref" reference="eq:b6-conj"} is conjectured to be strict for $n\geq k(3k+1)/2$. This is, in fact, not true as seen from the proof of Theorem [\[thm:b6\]](#thm:b6){reference-type="ref" reference="thm:b6"}.
:::

When $R=4, S=1$, by considering the parity of triangular numbers, we see that Conjecture [\[Conj 4.3\]](#Conj 4.3){reference-type="ref" reference="Conj 4.3"} is equivalent to Conjecture 4 in [@M3], which states that for $k\geq 1$ the $q$-series $$(-q;q)_\infty\sum_{n=0}^\infty(-1)^{T_n}q^{T_{n+2k}}$$ has non-negative coefficients. Here we used Euler's identity $$\frac{1}{(q;q^2)_\infty}=(-q;q)_\infty.$$

We prove that a weaker version of the conjecture is eventually true. As usual, we denote by $Q(n)$ the number of partitions of $n$ with distinct parts, which by Euler's identity is also the number of partitions of $n$ with odd parts. Let $c_1(n)=Q(n)$ and, if $k\geq 2$, let $c_k(n)$ be the sequence whose generating function is $$\label{ck} \sum_{n=0}^\infty c_k(n)q^n= (-1)^{k-1}(-q;q)_\infty\left((-1)^{k-1}q^{T_{2(k-1)}}+\sum_{j=0}^{k-2} (-1)^j(q^{T_{2j}}-q^{T_{2j+1}})\right).$$

::: theorem
[]{#thm:Q label="thm:Q"} If $k\geq 1$ there exists $N_k$ such that $c_k(n)\geq 0$ if $n\geq N_k$. Moreover, $N_k$ can be given explicitly.
:::

This article is structured as follows. In section [\[notation\]](#notation){reference-type="ref" reference="notation"}, we introduce relevant background and notation used throughout. In section [\[sec-main\]](#sec-main){reference-type="ref" reference="sec-main"}, we prove Theorem [\[main\]](#main){reference-type="ref" reference="main"} and discuss applications in the case $R=4, S=1$. In particular, in Proposition [\[prop-mex\]](#prop-mex){reference-type="ref" reference="prop-mex"} we give a connection with the odd minimal excludant of partitions into odd parts. In section [\[weak-conj\]](#weak-conj){reference-type="ref" reference="weak-conj"}, we prove Theorems [\[thm:b3\]](#thm:b3){reference-type="ref" reference="thm:b3"}, [\[thm:b6\]](#thm:b6){reference-type="ref" reference="thm:b6"}, and [\[thm:Q\]](#thm:Q){reference-type="ref" reference="thm:Q"}. In section [\[sec-JTP\]](#sec-JTP){reference-type="ref" reference="sec-JTP"} we prove combinatorially an identity related to the Jacobi Triple product identity. In particular cases, this identity reduces to identities (6.7), (6.10), (6.12), and (6.13) conjectured in [@M1]. Hence, we have combinatorial proofs of Merca's identities. In section [\[distinct-reg\]](#distinct-reg){reference-type="ref" reference="distinct-reg"}, we use the Weierstrass addition formula [@KMR Identity (8.1)] to prove an identity involving the number of $5$-regular distinct partition of $n$. Finally, in section [\[concluding\]](#concluding){reference-type="ref" reference="concluding"}, we offer some concluding remarks.
