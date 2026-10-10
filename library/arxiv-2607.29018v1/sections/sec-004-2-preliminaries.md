---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-004-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 7-8
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.753
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
[]{#sec:preliminaries label="sec:preliminaries"}

The reader is referred to [@I; @JL; @S1; @S] for general representation theory and [@Sagan] for symmetric groups and their representations. A *partition* of a positive integer $n$ is a sequence of positive integers $\gamma=(\gamma_1,\gamma_2,\ldots,\gamma_m)$ such that $\gamma_1\ge \gamma_2\ge\cdots\ge\gamma_m$ and $n=\gamma_1+\gamma_2+\cdots+\gamma_m$. We write $\gamma \vdash n$ to indicate this partition of $n$, and let $c_{i}(\gamma)$ denote the number of parts of $\gamma$ which are equal to $i$. The *sign* of a permutation $\sigma\in S_n$, denoted by $\mathrm{sgn}(\sigma)$, is defined to be $1$ if $\sigma$ is an even permutation and $-1$ if $\sigma$ is an odd permutation. Every permutation $\sigma\in S_n$ decomposes into disjoint cycles; the *cycle type* of $\sigma$ is the partition of $n$ whose parts are the lengths of these cycles. It is well known that two elements of $S_n$ are conjugate if and only if they have the same cycle type. Thus, the conjugacy classes of $S_n$ are determined by their cycle types and thus correspond to the partitions of $n$. For a partition $\gamma\vdash n$, denote by $C(S_n,\gamma)$ the corresponding conjugacy class of $S_n$. Note that $c_{1}(\gamma) = |\mathrm{fix}(\sigma)|$ is the number of fixed points of each $\sigma \in C(S_n,\gamma)$. Define $\mathrm{sgn}(\gamma)=1$ if the permutations in $C(S_n,\gamma)$ are even, and $\mathrm{sgn}(\gamma)=-1$ otherwise.

For each partition $\zeta\vdash n$, let $\rho_\zeta$ denote the corresponding Specht module in $\widehat{S_n}$. The Specht modules $\rho_{(n)}$, $\rho_{(1^n)}$ and $\rho_{(n-1,1)}$ are called the *trivial representation*, *sign representation* and *standard representation* of $S_n$, respectively. We denote the character and normalized character of $\rho_\zeta$ by $\chi_\zeta(\cdot)$ and $\tilde{\chi}_\zeta(\cdot)$, respectively. Since they are class functions on $S_n$, we write $\chi_\zeta(\gamma)$ and $\tilde{\chi}_\zeta(\gamma)$ for their values on the conjugacy class $C(S_n,\gamma)$. It is well known that $\chi_{(n)}(\sigma)=\tilde{\chi}_{(n)}(\sigma)=1$ and $\chi_{(1^n)}(\sigma)=\tilde{\chi}_{(1^n)}(\sigma)=\mathrm{sgn}(\sigma)$ for every $\sigma\in S_n$. Note that $\chi_\zeta(e)=\dim\rho_{\zeta}$ is the dimension of $\rho_\zeta\in \widehat{S_n}$ for any $\zeta\vdash n$.

In view of [\[eq:muj\]](#eq:muj){reference-type="eqref" reference="eq:muj"}, for a normal Cayley graph $\mathrm{Cay}(S_n, S)$ and a partition $\zeta \vdash n$, we use $\lambda_\zeta(\mathrm{Cay}(S_n, S))$, or $\lambda_\zeta$ for short, to denote its eigenvalue corresponding to the Specht module $\rho_\zeta$. That is, $$\begin{equation}
\label{eq:eigen-chara}
    \lambda_\zeta(\mathrm{Cay}(S_n, S)) = \sum_{\sigma \in S} \tilde{\chi}_\zeta(\sigma).
\end{equation}$$ It is known [@F] that the character of every $\rho_\zeta\in \widehat{S_n}$ on every conjugacy class of $S_n$ is an integer whose absolute value is at most the dimension of $\rho_\zeta$. Hence $\tilde{\chi}_\zeta(\gamma)$ is a rational number in the interval $[-1,1]$ for all $\zeta,\gamma\vdash n$. The following table, which is extracted from [@PP Table 1], gives the dimensions and characters of some irreducible representations of $S_n$.

::: {#tab:tab1}
   $~~~~\zeta\vdash n~~~$   $~~~~\dim \rho_\zeta=\chi_\zeta(e)~~~~$   $~~~~\chi_\zeta(\gamma)~\text{with}~c_i(\gamma)=c_i~~~~$
  ------------------------ ----------------------------------------- ----------------------------------------------------------
           $(n)$                              $1$                                               $1$
         $(n-1,1)$                           $n-1$                                            $c_1-1$
         $(n-2,2)$                    $\frac{n(n-3)}{2}$                             $\frac{c_1(c_1-3)}{2}+c_2$
        $(n-2,1,1)$                 $\frac{(n-1)(n-2)}{2}$                         $\frac{(c_1-1)(c_1-2)}{2}-c_2$
         $(n-3,3)$                  $\frac{n(n-1)(n-5)}{6}$                 $\frac{c_1(c_1-1)(c_1-5)}{6}+(c_1-1)c_2+c_3$
        $(n-3,2,1)$                 $\frac{n(n-2)(n-4)}{3}$                      $\frac{c_1(c_1-2)(c_1-4)}{3}-c_3$

  : Dimensions and characters of some irreducible representations of $S_n$
:::

The following lemma will play a crucial role in our proof of Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"}.

::: lem
[]{#PPmax label="PPmax"} There exists a positive integer $N_0$ such that for every $n\ge N_0$ and any $\gamma\vdash n$ with $|\mathrm{fix}(\gamma)| \geq 2$, we have $$\max_{\substack{\zeta\vdash n \\ \zeta \notin \{(n), (1^n)\}}} \tilde{\chi}_\zeta(\gamma)=\tilde{\chi}_{(n-1,1)}(\gamma).$$
:::
