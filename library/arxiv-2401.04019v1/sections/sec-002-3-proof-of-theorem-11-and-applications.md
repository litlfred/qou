---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-002-3-proof-of-theorem-11-and-applications
section_title: "Proof of Theorem 1.1 and applications"
section_number: 3
pages: 6-12
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.943
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on truncated"
---
[]{#sec-main label="sec-main"}

::: proof
*Proof of Theorem [\[main\]](#main){reference-type="ref" reference="main"}.* Let $R\geq 2$ and $0<S<R$. First we consider the case $S\neq R/2$. Recall that Conjecture [\[Conj 4.3\]](#Conj 4.3){reference-type="ref" reference="Conj 4.3"} states that, for all $k\geq 1$, the sequence $a_k(n)$ defined by [\[trunc-equiv\]](#trunc-equiv){reference-type="eqref" reference="trunc-equiv"} has non-negative terms. We prove the conjecture for $k\in \{1,2,3\}$ using combinatorial arguments.

Let $a_0(n)=\rho_R(n)$. From [\[eqn:rho\]](#eqn:rho){reference-type="eqref" reference="eqn:rho"}, we see that $$a_0(n)=\begin{cases} 1 & n=Ri(3i-1)/2 \text{ for $i$ even}\\
 -1 & n=Ri(3i-1)/2 \text{ for $i$ odd}
 \\
 0 & \text{otherwise.}\end{cases}$$

The sequence $Ri(3i-1)/2$ with $i$ even starts: $0, 5R, 7R, 22R, 26R, \ldots.$\
The sequence $Ri(3i-1)/2$ with $i$ odd starts: $R, 2R, 12R, 15R, \ldots.$

For $k\geq 0$, $$\begin{aligned}
 \notag\sum_{n=0}^\infty \big(a_k(n)+ a_{k+1}(n)\big)q^n & =\frac{q^{k(k+1)R/2-kS}}{(q^S,q^{R-S};q^R)_\infty} (1-q^{(2k+1)S})\\ \label{sum of terms} & = \frac{q^{k(k+1)R/2-kS}}{(q^{R+S},q^{R-S};q^R)_\infty} (1+q^S+q^{2S}+\cdots +q^{2kS}). 
\end{aligned}$$

The $q$-series [\[sum of terms\]](#sum of terms){reference-type="eqref" reference="sum of terms"} is the generating function for $y_k(n):=|\mathcal Y_k(n)|$, where $$\mathcal Y_k(n):=\{(\lambda, \delta_{R-S,R, k})\vdash n\mid \lambda\in \mathcal P_{\pm S,R},0\leq m_\lambda(S)\leq 2k\}.$$ Hence, for $k\geq 0$, we have $a_{k+1}(n)=y_k(n)-a_k(n)$.

**Case $k=1$:** Let $n\geq 0$. Then $a_1(n)= y_0(n)-a_0(n)$. We see that $\emptyset \in \mathcal Y_0(0)$ and if $n=mR$ with $m\geq 5$, then $\{(m-1)R+S, R-S\}\in \mathcal Y_0(n)$. Hence, $y_0(n)\geq a_0(n)$ for all $n\geq 0$ and thus $a_1(n)\geq 0$ for all $n\geq 0$.

**Case $k=2$:** We have $a_2(n)=y_1(n)-a_1(n)=y_1(n)-y_0(n)+a_0(n).$ If $n=0$, then $\mathcal Y_0(0)=\{(\emptyset, \emptyset)\}$, $\mathcal Y_1(0)=\emptyset$ and $a_0(0)=1$. Thus $a_2(0)=0$.

If $n\geq 1$ we create an injection $$\varphi_1: \mathcal Y_0(n) \to \mathcal Y_1(n)=\{(\lambda, \delta_{R-S,1})\vdash n\mid \lambda\in \mathcal P_{\pm S,R}\},   0\leq m_\lambda(S)\leq 2\}.$$ Let $(\lambda,\emptyset)\in \mathcal{Y}_0(n)$. Thus, $m_\lambda(S)=0$.

[Case I:]{.underline} $m_\lambda(R-S)\geq 1$. Define $\varphi_1(\lambda, \emptyset):=(\lambda\setminus (R-S), \delta_{R-S, 1})$.

[Case II:]{.underline} $m_\lambda(R-S)=0$. Since $n\geq 1$, we must have $\lambda\neq \emptyset$ and $$\lambda_\ell\geq \min\{R+S, 2R-S\}.$$ Define $\varphi_1(\lambda, \emptyset):=(\mu, \delta_{R-S, 1})$, where $\mu$ is the partition obtained from $\lambda$ by replacing part $\lambda_\ell$ by parts $\lambda_\ell-R, S$.

In each of Cases I and II, the transformation $\varphi_1$ is invertible on its image. Considering $m_\mu(S)$ for $(\mu, \delta_{R-S, 1})\in \varphi_1(\mathcal Y_0(n))$, we see that the image of $\varphi_1$ in Case I is disjoint from the image of $\varphi_1$ in Case II. Thus, for $n\geq 1$, $y_1(n)-y_0(n)\geq 0$.

Finally, to see that $a_2(n)\geq 0$ for all $n\geq 0$, we need to show that for each $n=Ri(3i-1)/2$ with $i$ odd, $\mathcal B_1(n):=\mathcal Y_1(n)\setminus \varphi_1\big(\mathcal Y_0(n)\big)\neq \emptyset$. Identifying partitions with their multiset of parts, we have $((S), \delta_{R-S,1})\in \mathcal B_1(R)$ and $(\{R-S,S^2\},\delta_{R-S,1}) \in \mathcal B_1(2R)$. If $n=mR$ with $m\geq 12$, then $(\{(m-3)R+S, (R-S)^2, S^2\},\delta_{R-S,1})\in \mathcal B_1(mR)$. Hence, $a_2(n)\geq 0$ for all $n\geq 0$.

**Case $k=3$:** We have $a_3(n)=y_2(n)-a_2(n)=y_2(n)-(y_1(n)-y_0(n))-a_0(n).$ Suppose $S<R/2$. First observe that

-   if $n=0$, then $\mathcal Y_0(0)=\{(\emptyset, \emptyset)\}$, $\mathcal Y_1(0)=\mathcal Y_2(0)=\emptyset$ and $a_0(0)=1$. Thus, $a_3(0)=0$.

-   if $n=R$, then $\mathcal Y_0(R)=\mathcal Y_2(R)=\emptyset$, $\mathcal Y_1(R)=\{((S), \delta_{R-S, 1})\}$ and $a_0(R)=-1$. Thus, $a_3(R)=0$.

-   If $n=2R$, then $\mathcal Y_0(2R)=\{((R+S, R-S), \emptyset)\}$, $\mathcal Y_1(2R)=\{((R+S), \delta_{R-S, 1}), ((R-S, S^2), \delta_{R-S, 1})\}$, $\mathcal Y_2(2R)=\emptyset$ and $a_0(2R)=-1$. Thus, $a_3(2R)=0$.

Let $n\not \in \{0,R, 2R\}$. We create an injection $$\varphi_2:\mathcal B_1(n)\to\mathcal Y_2(n)=\{(\lambda, \delta_{R-S,2})\vdash n \mid \lambda\in \mathcal P_{\pm S,R},   0\leq m_\lambda(S)\leq 4\}.$$ We consider several cases and in each case we describe the image of $\varphi_2$ either precisely or as a subset of a larger set. This will be sufficient to conclude that $\varphi_2$ is an injection.

Let $(\lambda, \delta_{R-S,1})\in \mathcal B_1(n)$. From Case $k=2$, $\mathcal B_1(n)$ consists of the pairs $(\mu, \delta_{R-S,1})\in \mathcal Y_1(n)$ with $\mu$ satisfying $\ell(\mu)\geq 3$, $m_\mu(S)\in \{1,2\}$, $\mu_{\ell-2}-\mu_{\ell-1}< R$.

[Case (i)]{.underline} $m_\lambda(R-S)\geq 2$. Thus, $\ell(\lambda)\geq 3$ and $\lambda_{\ell-2}-\lambda_{\ell-1}<R$. We define $\varphi_2(\lambda, \delta_{R-S,1}):=(\lambda\setminus(R-S,R-S, S), \delta_{R-S,2})$.

We obtain all pairs $(\mu, \delta_{R-S,2})\in \mathcal Y_2(n)$ with $m_\mu(S)\in \{0,1\}$

[Case (ii)]{.underline} $m_\lambda(R-S)= 0$. The condition $\lambda_{\ell-2}-\lambda_{\ell-1}< R$ implies that $m_\lambda(S)=1$. Moreover, $\lambda_{\ell-1}\geq R+S$. Define $\varphi_2(\lambda, \delta_{R-S,1}):=(\mu, \delta_{R-S, 2})$, where $\mu$ is the partition obtained from $\lambda$ by replacing parts $\lambda_{\ell-1}$ and $\lambda_{\ell-2}$ by parts $\lambda_{\ell-1}-R$ and $\lambda_{\ell-2}-R, S$.

We obtain all pairs $(\mu, \delta_{R-S, 2})\in \mathcal Y_2(n)$ satisfying all of the following conditions.

-   $\ell(\mu)\geq 4$;

-   $\mu_{\ell-4}-\mu_{\ell-3}\geq R$;

-   $\mu_{\ell-3}-\mu_{\ell-2}< R$;

-   $2\leq m_\mu(S)\leq 4$.

[Case (iii)]{.underline} $m_\lambda(R-S)= 1$.

\(a\) $m_\lambda(S)=2$. Since $n\neq 2R$, we must have $\ell(\lambda)\geq 4.$ Define $\varphi_2(\lambda, \delta_{R-S,1}):=(\mu, \delta_{R-S, 2})$, where $\mu$ is the partition obtained from $\lambda$ by replacing parts $\lambda_{\ell-3}$ and $R-S$ by part $\lambda_{\ell-3}-R$.

We obtain pairs $(\mu, \delta_{R-S, 2})\in \mathcal Y_2(n)$ satisfying all of the following conditions.

-   $\ell(\mu)\geq 3$;

-   $\mu_{\ell-3}-\mu_{\ell-2}\geq R$;

-   $2\leq m_\mu(S)\leq 3$.

\(b\) $m_\lambda(S)=1$. Then, condition $\lambda_{\ell-2}-\lambda_{\ell-1}<R$ implies that $\lambda_{\ell-2}=R+S$. First, let $\xi$ be the partition obtained from $\lambda$ by replacing parts $R+S$ and $R-S$ by a part equal to $S$. We have $m_\xi(S)=2$ and $\xi_{\ell-2}\geq R+S$.

If $\ell(\xi)=2$ or $\ell(\xi)\geq 4$ and $\xi_{\ell-i}-\xi_{\ell-i+1}<R$ for $i\in \{3,4\}$, define $\varphi_2(\lambda, \delta_{R-S, 1}):=(\xi,\delta_{R-S, 2})$.

We obtain pairs $(\mu, \delta_{R-S,2})\in\mathcal Y_2(n)$ satisfying all of the following conditions.

-   $\ell(\mu)\neq 3$;

-   if $\ell(\mu)\geq 4$, then $\mu_{\ell-4}-\mu_{\ell-3}< R$ and $\mu_{\ell-3}-\mu_{\ell-2}< R$;

-   $m_\mu(S)=2$.

Otherwise, if $\xi_{\ell-2}\leq 2R+S$, define $\varphi_2(\lambda, \delta_{R-S,1}):=(\mu, \delta_{R-S, 2})$, where $\mu$ is the partition obtained from $\xi$ by replacing part $\xi_{\ell-2}$ by parts $\xi_{\ell-2}-R, R-S, S$.

We obtain pairs $(\mu, \delta_{R-S,2})$ in $\mathcal Y_2(n)$ with

-   $\ell(\mu)\geq 5$;

-   $(m_\mu(S), m_\mu(R-S))\in \{(3,1), (3,2), (4,1)\}$;

-   $\mu_{\ell-4}-\mu_{\ell-3}<R$;

-   $\mu_{\ell-5}-\mu_{\ell-4}\geq R$.

If $\xi_{\ell-2}\geq 2R+R-S$, Define $\varphi_2(\lambda, \delta_{R-S,1}):=(\mu, \delta_{R-S, 2})$, where $\mu$ is the partition obtained from $\xi$ by replacing part $\xi_{\ell-2}$ by parts $\xi_{\ell-2}-2R, R-S,R-S, S,S$.

We obtain pairs $(\mu, \delta_{R-S,2})$ in $\mathcal Y_2(n)$ with

-   $\ell(\mu)\geq 7$;

-   $m_\mu(S)=4$ and $2 \leq m_\mu(R-S)\leq 3$;

-   $\mu_{\ell-7}-\mu_{\ell-6}\geq 2R$.

The second condition implies $\mu_{\ell-4}-\mu_{\ell-3}<R$ and $\mu_{\ell-5}-\mu_{\ell-4}<R$.

In each case, the transformation $\varphi_2$ is invertible on its image and the images in the different cases are disjoint. Thus, for $n\not \in \{0, R, 2R\}$, $y_2(n)-(y_1(n)-y_0(n))\geq 0$.

Let $n\not \in \{0, R, 2R\}$ and let $\mathcal B_2(n)=\mathcal Y_2(n)\setminus \varphi_2(\mathcal B_1(n))$. We need to show that for $n=Ri(3i-1)/2$ with $i$ even, $\mathcal B_2(n)\neq \emptyset$.

We have $(((R-S)^2, S^4), \delta_{R-S,2})\in \mathcal B_2(5R)$, $(R+S, (R-S)^3, S^4), \delta_{R-S,2})\in \mathcal B_2(7R)$, and for $m\geq 22$, $((m-8)R-S, (R+S)^2, (R-S)^3, S^4), \delta_{R-S,2})\in \mathcal B_2(mR)$.

The discussion above shows that $\varphi_2$ is an injection and thus $a_2(n)\leq y_2(n)$. Hence, $a_3(n)=y_2(n)-a_2(n)\geq 0$ for all $n\geq 0$.

Next assume $S>R/2$. Much of this case is similar to the case $S<R/2$. We highlight the differences below.

First note that if $R-S$ divides $R$ (which is equivalent to $R-S$ divides $S$), then in addition to the pairs in $\mathcal Y_i(n)$ for $0\leq i\leq 2$, $n=0,R, 2R$, listed in the case $S<R/2$, we have $$\begin{aligned}
((R-S)^{R/(R-S)}, \emptyset)&\in \mathcal Y_0(R),
\\
((R-S)^{S/(R-S)}, \delta_{R-S,1})&\in \mathcal Y_1(R),\\
((R-S)^{2R/(R-S)}, \emptyset), ((2R-S,(R-S)^{S/(R-S)}),\emptyset)&\in \mathcal Y_0(2R),\\ 
((R-S)^{(R+S)/(R-S)} \delta_{R-S,1}), ((S, (R-S)^{R/(R-S)}),\delta_{R-S,1})  &\in \mathcal Y_1(2R),
\\
((R-S)^{(2S-R)/(R-S)}, \delta_{R-S,2})&\in \mathcal Y_2(2R).
\end{aligned}$$ Thus, we still have $a_3(n)\geq 0$ for $n\in \{0, R, 2R\}$.

Let $n\not \in \{0, R, 2R\}$. The set $\mathcal B_1(n)$ consists of the pairs $(\mu, \delta_{R-S,1})\in \mathcal Y_1(n)$ with $\mu$ satisfying $\ell(\mu)\geq 3$, $m_\mu(S)\in \{1,2\}$, $(m_\mu(S), m_\mu(R-S))\neq (1,1)$, and $\mu_{\ell-2}-\mu_{\ell-1}< R$.

Let $(\lambda, \delta_{R-S,1})\in \mathcal B_1(n)$.

[Case (I)]{.underline} $m_\lambda(R-S)\geq 2$. Proceed as in Case (i) above and obtain the same image (pairs $(\mu, \delta_{R-S, 2})\in \mathcal Y_2(n)$ with $m_\mu(S)\in \{0,1\}$).

[Case (II)]{.underline} $m_\lambda(R-S)=0$ and $m_\lambda(S)=1$. Proceed as in Case (ii) above. We obtain pairs $(\mu, \delta_{R-S, 2})\in \mathcal Y_2(n)$ satisfying all of the following conditions (which are slightly different than in Case (ii) above).

-   $\ell(\mu)\geq 4$;

-   $2\leq m_\mu(S)\leq 4$ and $(m_\mu(S), m_\mu(R-S))\neq(2,1)$;

-   if $m_\mu(S)=m_\mu(R-S)=2$, then $\mu_{\ell-4}-\mu_{\ell-3}\geq 2R-2S$,\
    else $\mu_{\ell-4}-\mu_{\ell-3}\geq R$;

-   $\mu_{\ell-3}-\mu_{\ell-2}< R$.

[Case (III)]{.underline} $m_\lambda(R-S)=1$ and $m_\lambda(S)=2$. Proceed as in Case (iii)(a) above. We obtain pairs $(\mu, \delta_{R-S, 2})\in \mathcal Y_2(n)$ satisfying all of the following conditions (which are slightly different than in Case (iii)(a) above).

-   $\ell(\mu)\geq 3$;

-   $2\leq m_\mu(S)\leq 3$;

-   if $m_\mu(R-S)=1$, then $\mu_{\ell-3}-\mu_{\ell-2}\geq 2R-2S$,\
    else $\mu_{\ell-3}-\mu_{\ell-2}\geq R$.

[Case (IV)]{.underline} $m_\lambda(R-S)=0$ and $m_\lambda(S)=2$. Then, condition $\lambda_{\ell-2}-\lambda_{\ell-1}<R$ implies that $\lambda_{\ell-2}=2R-S$. First, let $\zeta$ be the partition obtained from $\lambda$ by removing one part equal to $2R-S$. We have $m_\zeta(S)=2$ and $\zeta_{\ell-2}\geq 2R-S$. In particular $m_\zeta(R-S)=0$. Now we proceed as in Case (iii)(b) with $\xi$ replaced by $\zeta$. There are again slight modifications for the conditions on the obtained pairs. They are as follows. If $\zeta_{\ell-2}\leq 2R+S$ and in the obtained pair $(\mu, \delta_{R-S, 2})$ we have $(m_\mu(S), m_\mu(R-S))\in\{(3,1), (3,2)\}$, then $\mu_{\ell-5}-\mu_{\ell-4}\geq 2R-2S$, else $\mu_{\ell-5}-\mu_{\ell-4}\geq R$. If $\zeta_{\ell-2}> 2R+S$, then $\zeta_{\ell-2}\geq 4R-S$ and in the obtained pair $(\mu, \delta_{R-S, 2})$ we have $m_\mu(R-S)=2$.

The rest of the argument is the same as in the case $S<R/2$.

If $R$ is even and $S=R/2$ then $1/(q^S,q^{R-S};q^R)_\infty=1/(q^{R/2};q^R)^2_\infty$. The proof follows in a similar manner as in the case $S<R/2$ above if instead of partitions $\lambda\in \mathcal P_{\pm S,R}$ we consider partitions $\lambda\in \mathcal P_{R/2,R}$ in two colors.

Alternatively, if $R$ is even and $S=R/2$, then [\[trunc-equiv\]](#trunc-equiv){reference-type="eqref" reference="trunc-equiv"} becomes $$\begin{aligned}
 \sum_{n=0}^\infty a_k(n)q^n:=\frac{(-1)^{k-1}}{(q^S;q^{2S})^2_\infty} 
\sum_{j=0}^{k-1} (-1)^jq^{j^2S}(1-q^{(2j+1)S}) -(-1)^{k-1}(q^{2S};q^{2S})_\infty. 
\end{aligned}$$ Replacing $q$ by $q^{1/S}$, we see that proving the non-negativity of the coefficients in the above $q$-series reduces to the case $R=2$, $S=1$ of Conjecture [\[Conj 4.3\]](#Conj 4.3){reference-type="ref" reference="Conj 4.3"}, i.e., the $q$-series $$\frac{(-1)^{k-1}}{(q;q^{2})_\infty} \left(\frac{1}{(q;q^{2})_\infty}
\sum_{j=0}^{k-1} (-1)^jq^{j^2}(1-q^{2j+1}) -(q;q)_\infty\right)$$ has non-negative coefficients. When $k=1, 2,3$, one can define simpler injections to prove the stronger Conjecture [\[Conj_2S\]](#Conj_2S){reference-type="ref" reference="Conj_2S"} below. We leave this as an exercise for the reader.

This concludes the proof of Theorem [\[main\]](#main){reference-type="ref" reference="main"}. ◻
:::

::: conjecture
[]{#Conj_2S label="Conj_2S"} Let $k$ be a positive integer. Then, the series $$\frac{(-1)^{k-1}}{(q;q^{2})_\infty}
\sum_{j=0}^{k-1} (-1)^jq^{j^2}(1-q^{2j+1}) -(-1)^{k-1}(q;q)_\infty$$ has non-negative coefficients.
:::

Next, we derive some applications of Theorem [\[main\]](#main){reference-type="ref" reference="main"}. We note that, when $(R,S)=(3,1)$, $$\frac{1}{(q^S,q^{R-S};q^R)_\infty}=\frac{1}{(q,q^2;q^3)_\infty} =\sum_{n=0}^\infty b_3(n)q^n$$ and when $(R,S)=(4,1)$,$$\frac{1}{(q^S,q^{R-S};q^R)_\infty} =\frac{1}{(q,q^2;q^4)_\infty} =\sum_{n=0}^\infty Q(n)q^n.$$ Then, Theorem [\[main\]](#main){reference-type="ref" reference="main"} leads to the following linear inequalities for $b_3(n)$ and also for $Q(n)$.

::: corollary
[]{#Cor-bQ label="Cor-bQ"} For all $n\geq 0$, $$\begin{aligned}
 b_3(n)-b_3(n-1)-\rho_3(n)& \geq 0\\ b_3(n)-b_3(n-1)-b_3(n-2)+b_3(n-5)-\rho_3(n)& \leq 0\\ b_3(n)-b_3(n-1)-b_3(n-2)+b_3(n-5)+ b_3(n-7)-b_3(n-12)-\rho_3(n)& \geq 0\\ Q(n)-Q(n-1)-\rho_4(n)& \geq 0\\ Q(n)-Q(n-1)-Q(n-3)+Q(n-6)-\rho_4(n)& \leq 0\\ Q(n)-Q(n-1)-Q(n-3)+Q(n-6)+ Q(n-10)-Q(n-15)-\rho_4(n)& \geq 0.
\end{aligned}$$
:::

We continue with another application of Theorem [\[main\]](#main){reference-type="ref" reference="main"} when $(R,S)=(4,1)$.

Given a partition $\lambda$, the minimal excludant of $\lambda$, denoted by $\textrm{mex}(\lambda)$, is the smallest positive integer that does not occur as a part of $\lambda$. For example, $$\textrm{mex}(7,7,5,3,2,2,1)=4.$$

In [@AN], Andrews and Newman define $\textrm{mex}_{A,a}(\pi)$ to be the smallest integer congruent to $a$ modulo $A$ that is not a part of the partition $\pi$. They also define $p_{A,a}(n)$ to be the number of partitions of $\pi$ of $n$ with $$\textrm{mex}_{A,a}(\pi)\equiv a\pmod{2A}$$ and $\overline p_{A,a}(n)$ to be the number of partitions $\pi$ of $n$ with $$\textrm{mex}_{A,a}(\pi)\equiv A+a\pmod{2A}.$$

As stated in the introduction, when $R=4, S=1$, Conjecture [\[Conj 4.3\]](#Conj 4.3){reference-type="ref" reference="Conj 4.3"} is equivalent to the non-negativity of the coefficients of the $q$-series $$\frac{1}{(q;q^2)_\infty}\sum_{n=0}^\infty(-1)^{T_n}q^{T_{n+2k}}.$$ From case $k=1$ of Theorem [\[main\]](#main){reference-type="ref" reference="main"}, we have that for all $n\geq 0$, $$\begin{aligned}
\label{Q-mex1} \sum_{j\geq 0}\big(Q(n-T_{4j+2})-Q(n-T_{4j+4})\big)+ \sum_{j\geq 0}\big(Q(n-T_{4j+1}) -& Q(n-T_{4j+3})\big)\\ & \notag \geq Q(n-1).
\end{aligned}$$

Since $T_{2j}=|\delta_{3,4,j}|$ the transformation $\lambda \mapsto \lambda \cup \delta_{3,4,j}$ shows that $$\begin{aligned}
    Q(n-T_{2j})& =|\{\lambda\vdash n \mid \lambda \text{ has odd parts, } \textrm{mex}_{4,3}(\lambda)\geq 4j+3\}|
\end{aligned}$$ Similarly, the transformation $\lambda \mapsto \lambda \cup \delta_{1,4,j+1}$ shows that $$\begin{aligned}
    Q(n-T_{2j+1})& =|\{\lambda\vdash n \mid \lambda \text{ has odd parts, } \textrm{mex}_{4,1}(\lambda)\geq 4j+5\}|.
\end{aligned}$$ Hence, $Q(n-T_{4j+2})-Q(n-T_{4j+4})$ is the number of partitions $\pi$ of $n$ into odd parts with $\textrm{mex}_{4,3}(\pi)=8j+7$ and $Q(n-T_{4j+1})-Q(n-T_{4j+3})$ is the number of partitions $\pi$ of $n$ into odd parts with $\textrm{mex}_{4,1}(\pi)=8j+5$.

In analogy to [@AN], we denote by $\overline Q_{A,a}(n)$ the number of partitions $\pi$ of $n$ into odd parts with $$\textrm{mex}_{A,a}(\pi)\equiv A+a\pmod{2A}.$$ Then, the discussion above leads to the following result.

::: proposition
[]{#prop-mex label="prop-mex"} For $n\geq 0$, we have $$\overline Q_{4,3}(n)+ \overline Q_{4,1}(n)\geq Q(n-1).$$
:::

# Proof of Theorems [\[thm:b3\]](#thm:b3){reference-type="ref" reference="thm:b3"}, [\[thm:b6\]](#thm:b6){reference-type="ref" reference="thm:b6"}, and [\[thm:Q\]](#thm:Q){reference-type="ref" reference="thm:Q"} {#weak-conj}
