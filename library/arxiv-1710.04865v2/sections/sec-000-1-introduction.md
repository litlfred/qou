---
doc_id: arxiv-1710.04865v2
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 1710.04865v2.pdf
source_sha256: ac8f436173d550e8
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
duplicate_of: "cjdoubletwistfinal"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.969
---
Let $K$ be a knot and $J_{N}(K; q)$ be the usual $N$th colored Jones polynomial, normalized to be $1$ for the unknot. It is often useful to determine a $q$-hypergeometric expression for $J_{N}(K; q)$, and such expressions have been computed for a variety of knots (e.g., [@habiro; @hikami1; @hikami2; @thang; @masbaum; @walsh]). These have applications to the AJ conjecture [@hikami1], the generalized Volume conjecture [@gukov; @hikami3], the computation of WRT invariants [@bhl; @hikami4] and quantum modular and mock modular forms [@folsom; @go; @hl1; @hl2; @zagier].

Consider the family of double twist knots $K_{(m,p)}$, where $2m$ and $2p$ are nonzero integers denoting the number of half-twists in each respective region of Figure [1](#fig:dt){reference-type="ref" reference="fig:dt"}. Positive integers correspond to right-handed half-twists and negative integers correspond to left-handed half-twists.

![Double twist knots](lovejoyosburn.pdf){#fig:dt width="7.5cm" height="5.0cm"}

Using ideas of Habiro [@habiro] and Masbaum [@masbaum], Lauridsen [@La Section 6] gave the *cyclotomic expansion* of $J_N(K_{(m,p)};q)$ for all nonzero $m$ and $p$ (cf. [@gk; @walsh]). For example, when $m$ and $p$ are positive integers we have $$\label{cyclotomicmp}
J_N(K_{(m,p)}; q) = \sum_{\substack{n \geq 0 \\ n =n_m \geq n_{m-1} \geq \cdots \geq n_1 \geq 0 \\ n = s_p \geq s_{p-1} \geq \cdots \geq s_1 \geq 0}}
(q^{1+N})_{n} (q^{1-N})_n q^n \prod_{i=1}^{m-1} q^{n_i^2+n_i} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix} \prod_{j=1}^{p-1} q^{s_j^2+s_j} \begin{bmatrix} s_{j+1} \\ s_j \end{bmatrix}$$ and $$\label{cyclotomicm-p}
\begin{aligned}
& J_N(K_{(m,-p)}; q) \\
& = \sum_{\substack{n \geq 0 \\ n = n_m \geq n_{m-1} \geq \cdots \geq n_1 \geq 0 \\ n = s_p \geq s_{p-1} \geq \cdots \geq s_1 \geq 0}}
(q^{1+N})_{n} (q^{1-N})_n (-1)^nq^{-\binom{n+1}{2}} \prod_{i=1}^{m-1} q^{n_i^2+n_i} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix} \prod_{j=1}^{p-1} q^{-s_j - s_{j+1}s_j} \begin{bmatrix} s_{j+1} \\ s_j \end{bmatrix}.
\end{aligned}$$ Here we have used the usual $q$-binomial coefficient

$$\begin{bmatrix} n \\ k \end{bmatrix} = \begin{bmatrix} n \\ k \end{bmatrix}_{q} := \frac{(q)_n}{(q)_{n-k} (q)_k}$$ with the standard $q$-hypergeometric notation

$$(a)_n = (a;q)_n := \prod_{k=0}^{n-1} (1-aq^{k}).$$

Recall that $$\label{mirror}
J_{N}(K; q^{-1}) = J_{N}(K^{*}; q),$$ where $K^*$ denotes the mirror image of the knot $K$. Thus, since $K_{(m,p)} = K_{(p,m)}$ and $K_{(-m,-p)}$ is the mirror image of $K_{(m,p)}$, equations [\[cyclotomicmp\]](#cyclotomicmp){reference-type="eqref" reference="cyclotomicmp"} and [\[cyclotomicm-p\]](#cyclotomicm-p){reference-type="eqref" reference="cyclotomicm-p"} cover all of the double twist knots, up to a substitution of $q$ by $q^{-1}$.

In this paper, we use a result of Takata [@takata] to prove $q$-hypergeometric formulas for the colored Jones polynomial of the double twist knots $K_{(-m,-p)}$ and $K_{(-m,p)}$ which are different from those corresponding to [\[cyclotomicmp\]](#cyclotomicmp){reference-type="eqref" reference="cyclotomicmp"} and [\[cyclotomicm-p\]](#cyclotomicm-p){reference-type="eqref" reference="cyclotomicm-p"}. To state the first case, define the functions $\epsilon_{i,j,m}$ and $\gamma_{i,m}$ by $$\label{epsilondef}
\epsilon_{i,j,m} = 
\begin{cases}
1, &\text{if $j \equiv -i$ or $-i-1$ $\pmod{2m}$}, \\
-1, &\text{if $j \equiv i$ or $i-1$ $\pmod{2m}$}, \\
0, &\text{otherwise}
\end{cases}$$ where $1 \leq i < j \leq 2mp-1$ with $m \nmid i$ and $$\label{gammadef}
\gamma_{i,m} =
\begin{cases}
1, &\text{if $i \equiv 1,\dots, m-1 \pmod{2m}$}, \\
-1 &\text{otherwise}
\end{cases}$$ where $1 \leq i \leq 2mp-2$. Our first main result is the following.

::: theorem
[]{#main1 label="main1"} For positive integers $m$ and $p$, we have $$\label{JNK-m-p}
\begin{aligned}
J&_{N}(K_{(-m,-p)}; q) \\ 
&= q^{1-N}\sum_{N-1 \geq n_{2mp-1} \geq \cdots \geq n_1 \geq 0} (q^{1-N})_{n_{2mp-1}} (-1)^{n_{2mp-1}} q^{-\binom{n_{2mp-1} + 1}{2}} \prod_{\substack{1 \leq i < j \leq 2mp-1 \\ m \nmid i}} q^{\epsilon_{i,j,m}n_in_j} \\
&  \qquad \qquad \qquad \qquad \times \prod_{i=1}^{2p-1} (-1)^{n_{mi}} q^{(-1)^{i} N n_{mi} + \binom{n_{mi} + 1}{2}} \prod_{i=1}^{2mp - 2} q^{-n_i n_{i+1} + \gamma_{i, m} n_i}\begin{bmatrix} n_{i+1} \\ n_{i} \end{bmatrix}. 
\end{aligned}$$
:::

The case $m=1$ of Theorem [\[main1\]](#main1){reference-type="ref" reference="main1"} was proved by Takata [@takata][^1]. Here $K_{(1,p)}=K_{p>0}$, the usual $p$th twist knot. As $K_{(-1,-p)}$ is the mirror image of $K_{(1,p)}$, one recovers $J_{N}(K_{p>0}^{*}; q)$ by taking $m=1$ in [\[JNK-m-p\]](#JNK-m-p){reference-type="eqref" reference="JNK-m-p"} and simplifying. Namely, we have (cf. equation (15) in [@takata])

$$\label{kppos}
\begin{aligned}
J_{N}&(K_{p>0}^{*}; q) \\
& = q^{1-N}\sum_{N-1 \geq n_{2p-1} \geq \cdots \geq n_1 \geq 0} (q^{1-N})_{n_{2p-1}}  q^{-Nn_{2p-1}} \prod_{i=1}^{2p-2} (-1)^{n_{i}} q^{(-1)^{i} N n_{i} + \binom{n_{i}}{2} -n_i n_{i+1}} \begin{bmatrix} n_{i+1} \\ n_{i} \end{bmatrix}. 
\end{aligned}$$

For an example with $m > 1$, take $m=p=2$. Then we have $$\begin{aligned}
J_N&(K_{(-2,-2)};q) \\
 &= q^{1-N} \sum_{N-1 \geq n_7 \geq n_6 \geq n_5 \geq n_4 \geq n_3 \geq n_2 \geq n_1 \geq 0}  (q^{1-N})_{n_7} (-1)^{n_2+n_4+n_6+n_7}q^{N(-n_2+n_4-n_6)} \\
&\qquad \qquad \qquad \times q^{-\binom{n_7+1}{2} + \binom{n_6+1}{2} + \binom{n_4+1}{2} + \binom{n_2+1}{2} +n_1(n_3-n_4-n_5+n_6+n_7) + n_3(n_5-n_6-n_7) +  n_5n_7} \\
& \qquad \qquad \qquad \qquad \times q^{-n_2n_3 -n_4n_5 - n_6n_7 + n_1 - n_2 -n_3 - n_4 + n_5 - n_6}\begin{bmatrix} n_7 \\ n_6 \end{bmatrix} \begin{bmatrix} n_6 \\ n_5 \end{bmatrix} \begin{bmatrix} n_5 \\ n_4 \end{bmatrix} \begin{bmatrix} n_4 \\ n_3\end{bmatrix}  \begin{bmatrix} n_3 \\ n_2 \end{bmatrix} \begin{bmatrix} n_2 \\ n_1 \end{bmatrix}.
\end{aligned}$$

For the case of $K_{(-m,p)}$, define the functions $\Delta_{i,j,m}$ and $\beta_{i,m}$ by $$\label{Deltadef}
\Delta_{i,j,m} = 
\begin{cases}
1, &\text{if $j \equiv -i$ or $-i+1$ $\pmod{2m}$}, \\
-1, &\text{if $j \equiv i$ or $i+1$ $\pmod{2m}$}, \\
0, &\text{otherwise}
\end{cases}$$ where $1 \leq i < j \leq 2mp$ with $m \nmid i$ and $$\label{betadef}
\beta_{i,m} =
\begin{cases}
1, &\text{if $i \equiv 1,\dots, m-1 \pmod{2m}$}, \\
-1 &\text{if $i \equiv m+1,\dots, 2m-1 \pmod{2m}$}, \\
0, &\text{otherwise} 
\end{cases}$$ where $1 \leq i \leq 2mp-1$. Our second main result is the following.

::: theorem
[]{#main2 label="main2"} For positive integers $m$ and $p$, we have $$\label{JNK-mp}
\begin{aligned}
J_{N}&(K_{(-m,p)}; q) \\ 
&= \sum_{N-1 \geq n_{2mp} \geq \cdots \geq n_1 \geq 0} (q^{1-N})_{n_{2mp}}(-1)^{n_{2mp}} q^{-\binom{n_{2mp} + 1}{2}} \prod_{\substack{1 \leq i < j \leq 2mp \\ m \nmid i}} q^{\Delta_{i,j,m} n_i n_j} \\
& \qquad \qquad \qquad \qquad \times \prod_{i=1}^{2p-1} (-1)^{n_{mi}} q^{(-1)^{i+1} N n_{mi} + \binom{n_{mi} + 1}{2}} \prod_{i=1}^{2mp - 1} q^{\beta_{i,m} n_i}\begin{bmatrix} n_{i+1} \\ n_{i} \end{bmatrix}.
\end{aligned}$$
:::

Again, the case $m=1$ was established by Takata [@takata]. As $K_{(1,-p)} = K_{p<0}$ and $K_{(-1,p)}$ is the mirror image of $K_{(1,-p)}$, one recovers $J_{N}(K_{p<0}^{*}; q)$ by taking $m=1$ in ([\[JNK-mp\]](#JNK-mp){reference-type="ref" reference="JNK-mp"}) and simplifying. Namely, we have (cf. equation (14) in [@takata])

$$\label{kpneg}
\begin{aligned}
J_{N}&(K_{p<0}^{*}; q) \\
& = \sum_{N-1 \geq n_{2p} \geq \cdots \geq n_1 \geq 0} (q^{1-N})_{n_{2p}} (-1)^{n_{2p}} q^{-\binom{n_{2p} + 1}{2}} \prod_{i=1}^{2p-1} (-1)^{n_{i}} q^{(-1)^{i+1} N n_{i} + \binom{n_{i} + 1}{2}} \begin{bmatrix} n_{i+1} \\ n_{i} \end{bmatrix}. 
\end{aligned}$$

For an example with $m > 1$, take $m=3$ and $p=1$. Then we have $$\begin{aligned}
J_N&(K_{(-3,1)};q)  \\
&= \sum_{N-1 \geq n_6 \geq n_5 \geq n_4 \geq n_3 \geq n_2 \geq n_1 \geq 0} (q^{1-N})_{n_6}(-1)^{n_3+n_6}q^{Nn_3 -\binom{n_6+1}{2} + \binom{n_3+1}{2}} \\
&\qquad \qquad \qquad \qquad \times q^{n_1(-n_2 + n_5+n_6) + n_2(-n_3+n_4+n_5)  - n_4n_5 - n_5n_6} \\
& \qquad \qquad \qquad \qquad \qquad \times q^{n_1 +n_2 - n_4 -n_5} \begin{bmatrix} n_6 \\ n_5 \end{bmatrix} \begin{bmatrix} n_5 \\ n_4 \end{bmatrix} \begin{bmatrix} n_4 \\ n_3\end{bmatrix}  \begin{bmatrix} n_3 \\ n_2 \end{bmatrix} \begin{bmatrix} n_2 \\ n_1 \end{bmatrix}.
\end{aligned}$$

Motivated by the expressions in ([\[JNK-m-p\]](#JNK-m-p){reference-type="ref" reference="JNK-m-p"}) and [\[cyclotomicmp\]](#cyclotomicmp){reference-type="eqref" reference="cyclotomicmp"}, we define the $q$-series $F_{m,p}(q)$ and $U_{m,p}(x;q)$ by

$$\label{Fmp}
\begin{aligned}
F_{m,p}(q) &= q\sum_{n_{2mp-1} \geq \cdots \geq n_1 \geq 0} (q)_{n_{2mp-1}} (-1)^{n_{2mp-1}} q^{-\binom{n_{2mp-1} + 1}{2}} \prod_{\substack{1 \leq i < j \leq 2mp-1 \\ m \nmid i}} q^{\epsilon_{i,j,m}n_in_j} \\
&  \qquad \qquad \qquad \qquad \times \prod_{i=1}^{2p-1} (-1)^{n_{mi}} q^{\binom{n_{mi} + 1}{2}} \prod_{i=1}^{2mp - 2} q^{-n_i n_{i+1} + \gamma_{i, m} n_i}\begin{bmatrix} n_{i+1} \\ n_{i} \end{bmatrix}
\end{aligned}$$ and $$\label{Ump}
U_{m,p}(x; q) = \sum_{\substack{n \geq 0 \\ n =n_m \geq n_{m-1} \geq \cdots \geq n_1 \geq 0 \\ n =s_p \geq s_{p-1} \geq \cdots \geq s_1 \geq 0}}
(-xq)_{n} (-x^{-1}q)_n q^n \prod_{i=1}^{m-1} q^{n_i^2+n_i} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix} \prod_{j=1}^{p-1} q^{s_j^2+s_j} \begin{bmatrix} s_{j+1} \\ s_j \end{bmatrix}.$$

Note that if $\zeta_N$ is *any* $N$th root of unity, we have $$\label{Fatroot}
F_{m,p}(\zeta_N)  = J_N(K_{(-m,-p)};\zeta_N)$$ and $$\label{Uatroot}
U_{m,p}(-1; \zeta_N) = J_N(K_{(m,p)};\zeta_N).$$

The base case $F_{1,1}(q)$ is $q$ times the Kontsevich-Zagier series, $$\
F(q) := \sum_{n \geq 0} (q)_n,$$ one of the foundational examples of Zagier's quantum modular forms [@z-1; @zagier], while $$U_{1,1}(x;q) = q^{-1}U(x;q),$$ where $U(x;q)$ is the generating function for strongly unimodal sequences [@bopr], $$\label{u}
U(x;q) :=\sum_{n=0}^{\infty} (-xq)_n (-x^{-1}q)_n q^{n+1}.$$ For this reason, we call the series $F_{m,p}(q)$ the *generalized Kontsevich-Zagier functions for double twist knots* and the $U_{m,p}(x;q)$ the *generalized $U$-functions for double twist knots*. Note that while $U_{m,p}(x;q)$ is well-defined for $|q| <1$ and for $q$ a root of unity when $x=-1$, the generalized Kontsevich-Zagier functions $F_{m,p}(q)$ are only defined at roots of unity.

The original Kontsevich-Zagier series $F(q)$ and the generating function for strongly unimodal sequences $U(x;q)$ when $x=-1$ are *dual* at roots of unity via $$\label{fu}
F(\zeta_N^{-1}) = U(-1; \zeta_N).$$ This was first shown by Bryson, Ono, Pitman and Rhoades [@bopr]. It also follows at once from [\[mirror\]](#mirror){reference-type="eqref" reference="mirror"} and the case $m=p=1$ of [\[Fatroot\]](#Fatroot){reference-type="eqref" reference="Fatroot"} and [\[Uatroot\]](#Uatroot){reference-type="eqref" reference="Uatroot"}, which was first observed in [@hl1]. Using [\[mirror\]](#mirror){reference-type="eqref" reference="mirror"} and the general case of [\[Fatroot\]](#Fatroot){reference-type="eqref" reference="Fatroot"} and [\[Uatroot\]](#Uatroot){reference-type="eqref" reference="Uatroot"}, we immediately have the following generalization of [\[fu\]](#fu){reference-type="eqref" reference="fu"}.

::: corollary
[]{#fugeneralthm label="fugeneralthm"} If $\zeta_N$ is any $N$th root of unity, then we have $$\label{fugeneraleq}
F_{m,p}(\zeta_N) = U_{m,p}(-1; \zeta_N^{-1}).$$
:::

Next we turn our attention to [\[JNK-mp\]](#JNK-mp){reference-type="eqref" reference="JNK-mp"} and [\[cyclotomicm-p\]](#cyclotomicm-p){reference-type="eqref" reference="cyclotomicm-p"}. Motivated by these expressions, we define $\mathcal{F}_{m,p}(q)$ and $\mathcal{U}_{m,p}(x; q)$ by $$\label{calFmp}
\begin{aligned}
\mathcal{F}_{m,p} (q)
&= \sum_{n_{2mp} \geq \cdots \geq n_1 \geq 0} (q)_{n_{2mp}}(-1)^{n_{2mp}} q^{-\binom{n_{2mp} + 1}{2}} \prod_{\substack{1 \leq i < j \leq 2mp \\ m \nmid i}} q^{\Delta_{i,j,m} n_i n_j} \\
& \qquad \qquad \qquad \qquad \times \prod_{i=1}^{2p-1} (-1)^{n_{mi}} q^{\binom{n_{mi} + 1}{2}} \prod_{i=1}^{2mp - 1} q^{\beta_{i,m} n_i}\begin{bmatrix} n_{i+1} \\ n_{i} \end{bmatrix}
\end{aligned}$$ and $$\label{calUmp}
\begin{aligned}
& \mathcal{U}_{m,p}(x; q) \\
& = \sum_{\substack{n \geq 0 \\ n = n_m \geq n_{m-1} \geq \cdots \geq n_1 \geq 0 \\ n =s_p \geq s_{p-1} \geq \cdots \geq s_1 \geq 0}}
(-xq)_{n} (-x^{-1}q)_n (-1)^n q^{-\binom{n+1}{2}} \prod_{i=1}^{m-1} q^{n_i^2+n_i} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix} \prod_{j=1}^{p-1} q^{-s_j - s_{j+1}s_j} \begin{bmatrix} s_{j+1} \\ s_j \end{bmatrix}.
\end{aligned}$$ Neither $\mathcal{F}_{m,p}(q)$ nor $\mathcal{U}_{m,p}(x; q)$ is defined anywhere except at roots of unity. Note that $$\label{calFatroot}
\mathcal{F}_{m,p}(\zeta_N)  = J_N(K_{(-m,p)};\zeta_N)$$ and $$\label{calUatroot}
\mathcal{U}_{m,p}(-1; \zeta_N) = J_N(K_{(m,-p)};\zeta_N).$$ As a result of [\[mirror\]](#mirror){reference-type="eqref" reference="mirror"}, [\[calFatroot\]](#calFatroot){reference-type="eqref" reference="calFatroot"} and [\[calUatroot\]](#calUatroot){reference-type="eqref" reference="calUatroot"}, we immediately obtain the following duality at roots of unity.

::: corollary
[]{#calFcalU label="calFcalU"} If $\zeta_N$ is any $N$th root of unity, then we have $$\mathcal{F}_{m,p}(\zeta_N) = \mathcal{U}_{m,p}(-1; \zeta_N^{-1}).$$
:::

We expect ([\[JNK-m-p\]](#JNK-m-p){reference-type="ref" reference="JNK-m-p"}), ([\[JNK-mp\]](#JNK-mp){reference-type="ref" reference="JNK-mp"}) and Theorems 1.1 and 1.2 in [@lo2] to be of considerable interest to those working at the overlap of number theory, quantum topology, combinatorics and physics. Recently, Park [@park] used ([\[JNK-m-p\]](#JNK-m-p){reference-type="ref" reference="JNK-m-p"}) and ([\[JNK-mp\]](#JNK-mp){reference-type="ref" reference="JNK-mp"}) to check conjectures of Gukov and Manolescu [@gm] concerning the existence of a two-variable invariant (with origins in string theory) for knot complements. In [@lovejoyqqid], the first author initiated the study of quantum $q$-series identities with Corollary [\[fugeneralthm\]](#fugeneralthm){reference-type="ref" reference="fugeneralthm"} as a key illustration. Furthermore, we suspect that the generalized Kontsevich-Zagier series $F_{m,p}(q)$ given by ([\[Fmp\]](#Fmp){reference-type="ref" reference="Fmp"}) are quantum modular forms.

The paper is organized as follows. In Section 2, we recall Takata's main theorem and provide some preliminaries. In Section 3, we prove Theorems [\[main1\]](#main1){reference-type="ref" reference="main1"} and [\[main2\]](#main2){reference-type="ref" reference="main2"}. We conclude in Section 4 with a discussion of the generalized Kontsevich-Zagier functions and the generalized $U$-functions for the torus knots $T_{(2,2t+1)}$, along with some related questions.

[^1]: Note that Takata's $q$-hypergeometric notation differs slightly from the standard one we use here
