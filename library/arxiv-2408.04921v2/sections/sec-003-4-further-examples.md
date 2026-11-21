---
doc_id: arxiv-2408.04921v2
doc_title: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP"
section_id: sec-003-4-further-examples
section_title: "Further examples"
section_number: 4
pages: 13-20
source_pdf: 2408.04921v2.pdf
source_sha256: dcfe112640a8adda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.965
doc_brief: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP — The paper studies how to compute irreducible characters of the generalized symmetric group Ck ≀Sn by iterative algorithms."
---
For completeness, we first calculate the degree of any irreducible character of $C_k\wr S_n$ [@IJS]. Recall that the inner product in $V$ is given by: $$\begin{aligned}
    \langle a_{-\boldsymbol{\lambda}},a_{-\boldsymbol{\mu}} \rangle=\prod_{i=0}^{k-1}\langle a_{-\lambda^{(i)}},a_{-\mu^{(i)}}\rangle=\delta_{\boldsymbol{\lambda}\boldsymbol{\mu}}\prod_{i=0}^{k-1}z_{\lambda^{(i)}}.
\end{aligned}$$ Under this inner product the wreath Schur functions are orthonormal: $$\begin{aligned}
    \langle s_{\boldsymbol{\lambda}},s_{\boldsymbol{\mu}} \rangle=\prod_{i=0}^{k-1}\langle s_{\lambda^{(i)}},s_{\mu^{(i)}}\rangle=\delta_{\boldsymbol{\lambda}\boldsymbol{\mu}}.
\end{aligned}$$ Then we have $$\begin{aligned}
\label{e:inner}
    \langle s_{\boldsymbol{\lambda}},a_{-\boldsymbol{\mu}} \rangle=\prod_{i=0}^{k-1}\langle s_{\lambda^{(i)}},a_{-\mu^{(i)}}\rangle.
\end{aligned}$$

The following result is well-known for the wreath products and is included here using the vertex operator approach.

::: thm
[@O] For any colored partition $\boldsymbol{\lambda}=(\lambda^{(0)},\lambda^{(1)},\cdots,\lambda^{(k-1)})$ of $n$, the degree of the irreducible character $\chi^{\boldsymbol{\lambda}}$ of $C_k\wr S_n$ is given by $$\begin{aligned}
        \chi^{\boldsymbol{\lambda}}(\boldsymbol{1})=\frac{n!}{\prod_{i=0}^{k-1}h(\lambda^{(i)})},
    
\end{aligned}$$ where $\boldsymbol{1}=((1^n),\emptyset,\cdots,\emptyset)$ and $h(\lambda^{(i)})$ is the hook length of $\lambda^{(i)}$.
:::

::: proof
*Proof.* By definition, $\chi^{\boldsymbol{\lambda}}(\boldsymbol{1})=\langle s_{\boldsymbol{\lambda}}, (\widetilde{a}_{-01})^n \rangle=\langle s_{\boldsymbol{\lambda}}, (\sum_{j=0}^{k-1}a_{-j1})^n \rangle$. The non-zero items are only $$\begin{aligned}
        \langle s_{\boldsymbol{\lambda}},\prod_{j=0}^{k-1}a_{-j1}^{|\lambda^{(j)}|} \rangle=\prod_{j=0}^{k-1}\langle s_{\lambda^{(j)}},a_{-j1}^{|\lambda^{(j)}|} \rangle=\prod_{j=0}^{k-1}\frac{|\lambda^{(j)}|!}{h(\lambda^{(j)})},
    
\end{aligned}$$ where the second equality has used the degree formula of irreducible characters in $S_{\lambda^{(j)}}$. Since the coefficient of $\prod_{j=0}^{k-1}a_{-j1}^{|\lambda^{(j)}|}$ in $(\sum_{j=0}^{k-1}a_{-j1})^n$ equals to $$\begin{aligned}
        C_n^{|\lambda^{(0)}|}C_{n-|\lambda^{(0)}|}^{|\lambda^{(1)}|}\cdots=\frac{n!}{\prod_{j=0}^{k-1}|\lambda^{(j)}|!},
    
\end{aligned}$$ and the theorem is proved. ◻
:::

::: cor
Given colored partitions $\boldsymbol{\lambda}=(\lambda^{(0)},\lambda^{(1)},\cdots,\lambda^{(k-1)})$ of $n$, let $\boldsymbol{\kappa}^j$ be a colored partition supported only at the $j$-th constituent $(1^n)$, and $\omega$ be the $k$-th primitive root of unity. Then we have $$\begin{aligned}
        \chi^{\boldsymbol{\lambda}}_{\boldsymbol{\kappa}^j}=\frac{\omega^{-\mathrm{deg}(\boldsymbol{\lambda})j}n!}{\prod_{i=0}^{k-1}h(\lambda^{(i)})},
    
\end{aligned}$$ where $\mathrm{deg}(\boldsymbol{\lambda})$ is defined as the sum of $i |\lambda^{(i)}|$.
:::

In the dual case, one has the following result.

::: prop
Given a colored partition $\boldsymbol{\rho}=(\rho^{(0)},\rho^{(1)},\cdots,\rho^{(k-1)})$ of $n$, the irreducible character value is $$\begin{aligned}
\label{e:char-}
        \chi^{\boldsymbol{\kappa}^j}_{\boldsymbol{\rho}}=\omega^{-\eta(\boldsymbol{\rho})j}(-1)^{l(\boldsymbol{\rho})+n},
    
\end{aligned}$$ where $\boldsymbol{\kappa}^j$ is a colored partition supported only at the $j$-th constituent $(1^n)$, $\eta(\boldsymbol{\rho})$ is the weighted length $\sum_i il(\rho^{(i)})$.
:::

::: proof
*Proof.* In view of [\[e:inner\]](#e:inner){reference-type="eqref" reference="e:inner"}, the only nonzero factor of $\langle s_{\boldsymbol{\kappa}^j}, \widetilde{a}_{\boldsymbol{\rho}} \rangle$ is $$\begin{aligned}
        \langle s_{j(1^n)}, \prod_{i=0}^{k-1}\omega^{-ij|\rho^{(i)}|}a_{-j\rho^{(i)}} \rangle
    
\end{aligned}$$ since $|\lambda^{(j)}|$ exhausts $n$. Note that $\prod_{i=0}^{k-1}a_{-j\rho^{(i)}}$ can be written as $a_{-j\rho}$, where $\rho$ is the rearrangement of $\boldsymbol{\rho}$.

For the character value $\chi^{(1^n)}_{\rho}$, we apply Theorem [\[c:3.10\]](#c:3.10){reference-type="ref" reference="c:3.10"} with induction on $n$. First $\chi^{(1)}_{(1)}=1$ is clear. The inductive hypothesis says that $$\chi^{(1^{n-1})}_{(\rho\backslash\mu)\cup\tau}=(-1)^{l(\rho)-l(\mu)+l(\tau)+n-1}.$$ Note that $$\sum_{\lambda\vdash n}\frac{1}{z_\lambda}=1.$$ Then $$\chi^{(1^n)}_{\rho}=(-1)^{l(\rho)+n-1}\sum_{\mu\vartriangleleft\rho,|\mu|\geq 1}(-1)^{l(\mu)},$$ where the sum is over all nonempty subpartitions $\mu\vartriangleleft\rho$, which is an alternating sum of binomial coefficients: $$\sum_{k=1}^{l(\rho)}(-1)^k\binom{l(\rho)}{k}=-C_{l(\rho)}^0=-1,$$ Therefore $\chi^{(1^n)}_{\rho}=(-1)^{l(\rho)+n}$. Obviously $l(\boldsymbol{\rho})=l(\rho)$, and $\prod_{i=0}^{k-1}\omega^{-ij|\rho^{(i)}|}$ equals to $\omega^{-\eta(\boldsymbol{\rho})j}$, subsequently we have shown $\chi^{\boldsymbol{\kappa}^j}_{\boldsymbol{\rho}}$ is given as stated. ◻
:::

Next we move on to study a relationship between irreducible character values of $C_k\wr S_n$ and those of $S_{kn}$ mod $k$. Note that $k$ does not have to be a prime.

Recall that the *$k$-core $\gamma_\lambda$* of partition $\lambda=(\lambda_1, \lambda_2,\cdots, \lambda_l)$ is defined by removing all $k$-rim hooks of $\lambda$. For example, let $\lambda=(4,2,1)$, $k=3$,\

::: center
$\young(~~~~,~~,~)$ $\to$ $\young(~~~~,\times\times,\times)$ $\to$ $\young(~\times\times\times,\times\times,\times)$
:::

 \
then the 3-core of $\lambda$ is $(1)$.

Let $T=T(\lambda)$ be the set of paths from partition $\lambda$ to its core $\gamma_{\lambda}$, where each path is a procedure of removing $k$-rim hooks. For each path $t\in T$, denote by $\mathrm{ht}(t)$ the sum of heights of $k$-rim hooks in path $t$. It is known that $\sigma_{\lambda}: =(-1)^{\mathrm{ht}(t)}$ is well defined and independent of the paths in $T(\lambda)$ [@MO Prop. 2.2]. For example, the 3-core of $\lambda=(5,4,3,2)$ is (2). Consider two paths $t_1, t_2\in T$ as follows. $t_1$ has $\mathrm{ht}(t_1)=5$:\

::: center
$\young(~~~~~,~~~~,~\times\times,~\times)$ $\to$ $\young(~~~\times\times,~~~\times,~\times\times,~\times)$ $\to$ $\young(~~\times\times\times,~\times\times\times,~\times\times,~\times)$ $\to$ $\young(~~\times\times\times,\times\times\times\times,\times\times\times,\times\times)$
:::

while $t_2$ has $\mathrm{ht}(t_2)=3$:\

::: center
$\young(~~~~~,~~\times\times,~~\times,~~)$ $\to$ $\young(~~~~~,~~\times\times,~\times\times,\times\times)$ $\to$ $\young(~~~~~,\times\times\times\times,\times\times\times,\times\times)$ $\to$ $\young(~~\times\times\times,\times\times\times\times,\times\times\times,\times\times)$
:::

so $\sigma_{\lambda}$ equals to $-1$.

The *$k$-quotient $\boldsymbol{\beta}_\lambda$* of $\lambda$ can be constructed as follows. Choose $m$ as a multiple of $k$ such that $m\geq l(\lambda)$, let $\delta_m=(m-1, m-2,\cdots,1,0)$, $\xi=\lambda+\delta_m$, which is a strict partition. For each $0\leq r\leq k-1$, suppose there are $m_r$ parts $\xi_i$ that are congruent to $r$ mod $k$. Each of these $\xi_i \,(1\leq i\leq m_r$) is divided by $k$ and reordered as $$\xi_i=k\cdot \xi^{(r)}_s+r$$ such that $\xi^{(r)}_1>\xi^{(r)}_2>\cdots>\xi^{(r)}_{m_r}\geq 0$. So for each $0\leq r\leq k-1$, we obtain a partition $\lambda^{(r)}=(\lambda^{(r)}_1, \lambda^{(r)}_2,\cdots,\lambda^{(r)}_{m_r})$ by letting $\lambda^{(r)}_s=\xi^{(r)}_s-m_r+s$ ($1\leq s\leq m_r$). Now the colored partition $(\lambda^{(0)}, \lambda^{(1)},\ldots, \lambda^{(k-1)})=\boldsymbol{\beta}_\lambda$ is the $k$-quotient of $\lambda$.

For example, given $\lambda=(4,2,1)$ and $k=3$ as above. Take $m=3$, then $\xi=(6,3,1)$, $m_0=2, m_1=1$ and $m_2=0$. We have $$\lambda^{(0)}_1=2-2+1=1, \quad \lambda^{(0)}_2=1-2+2=1; \quad \lambda^{(1)}_1=0-1+1=0,$$ thus the 3-quotient of $\lambda$ is $((1,1), \emptyset, \emptyset)$.

The above procedure shows that any partition $\lambda$ determines its $k$-core $\gamma_\lambda$ and $k$-quotient $\boldsymbol{\beta}_\lambda$ uniquely. Moreover, $$|\lambda|=k\cdot \Arrowvert\boldsymbol{\beta}_\lambda\Arrowvert+|\gamma_\lambda|.$$ In fact, $\lambda$ also can be determined uniquely by $\gamma_\lambda$ and $\beta_\lambda$ conversely (cf. [@Mac I.I. Ex. 8]).

For convenience, we define the *standard form* of an irreducible character value of $C_k\wr S_n$. According to Theorem [\[t:MN-gensym\]](#t:MN-gensym){reference-type="ref" reference="t:MN-gensym"}, each $\chi_{\boldsymbol{\rho}}^{\boldsymbol{\lambda}}$ can be written as $$c_0+c_1\omega+\cdots+c_{k-1}\omega^{k-1}, c_i\in \mathbb{Z}$$ since the coefficients of the recursive formula lie in $\mathbb{Z}[\omega]$. However, $k$-tuple $(c_0, c_1, \cdots, c_{k-1})$ is not unique due to $1+\omega+\cdots+\omega^{k-1}=0$. Indeed, $$c_0+c_1\omega+\cdots+c_{k-1}\omega^{k-1}=c_0'+c_1'\omega+\cdots+c_{k-1}'\omega^{k-1}$$ if and only if $c_0-c_0'=c_1-c_1'=\cdots=c_{k-1}-c_{k-1}'$. For example, the values of $\chi_{(\emptyset, (1), (1,1))}^{(\emptyset, (2), (1))}$ can be $$\begin{gathered}
\vdots\\
2+\omega+3\omega^2\\
1+2\omega^2\\
-\omega+\omega^2\\
\vdots
\end{gathered}$$ The standard form is the *unique* form such that the sum of $c_i$ lies in the color set $I=\{0, 1, \ldots, k-1\}$. We also denote by $d(\chi_{\boldsymbol{\rho}}^{\boldsymbol{\lambda}})$ the sum of $c_i$ in the standard form. Then $-\omega+\omega^2$ is the standard form in the above example, and $d(\chi_{(\emptyset, (1), (1,1))}^{(\emptyset, (2), (1))})=0$.

::: thm
(Relation between $C_k\wr{S}_n$ and $S_{kn}$) Given colored partitions $\boldsymbol{\lambda}$ and $\boldsymbol{\rho}$ of $n$. Let $\lambda$ be the partition of $kn$ with the $k$-core $\emptyset$ and $k$-quotient $\boldsymbol{\lambda}$, and let $\rho$ be the rearrangement of $k\boldsymbol{\rho}$. Then $$d(\chi_{\boldsymbol{\rho}}^{\boldsymbol{\lambda}})=\sigma_{\lambda}(\chi_{\rho}^{\lambda} \quad mod \quad k).$$
:::

::: proof
*Proof.* Let $P$ be the set of paths from $\boldsymbol{\lambda}$ to $\emptyset$ that remove colored $|\rho^{(0)}_1|$-rim hooks, colored $|\rho^{(0)}_2|$-rim hooks,\..., colored $|\rho^{(k-1)}_{l(k-1)-1}|$-rim hooks, colored $|\rho^{(k-1)}_{l(k-1)}|$-rim hooks.

By Theorem [\[t:MN-gensym\]](#t:MN-gensym){reference-type="ref" reference="t:MN-gensym"} it follows that the irreducible character value $\chi_{\boldsymbol{\rho}}^{\boldsymbol{\lambda}}$ of $C_k\wr S_n$ can be written as $$\chi_{\boldsymbol{\rho}}^{\boldsymbol{\lambda}}=\sum_{p\in P}\sigma_p\omega(p),$$ where the sum is over all paths $p\in P$ and $\sigma_p: =(-1)^{\mathrm{ht}(p)}$ with $\mathrm{ht}(p)$ being the sum of all colored rim-hook heights in path $p$. Note that $\omega(p)$ equals to some power of $\omega$ depending on $p$. Suppose the standard form of $\chi_{\boldsymbol{\rho}}^{\boldsymbol{\lambda}}$ is of the following form: $\sum_{i=0}^{k-1}c_i\omega^i$.

On the other hand, let $\tilde{P}$ be the set of paths from $\lambda$ to $\emptyset$ that remove $k|\rho_1|$-rim hooks, $k|\rho_2|$-rim hooks,\..., and $k|\rho_{l(\lambda)}|$-rim hooks. By the ordinary Murnaghan-Nakayama rule of $S_{kn}$, we have that $$\chi_{\rho}^{\lambda}=\sum_{\tilde{p}\in \tilde{P}}\sigma_{\tilde{p}},$$ where $\sigma_{\tilde{p}}=(-1)^{\mathrm{ht}(\tilde{p})}$ is defined similarly as $\sigma_p$. It is known that $\sigma_p$ and $\sigma_{\tilde{p}}$ are related by the fundamental relation [@O]: $$\begin{aligned}
\sigma_p=\sigma_{\lambda}\sigma_{\tilde{p}}.
\end{aligned}$$ and there is a bijection between the sets $P$ and $\tilde{P}$. This implies that $\sum_ic_i$ in the standard form equals to $\sigma_{\lambda}\cdot \chi_{\rho}^{\lambda}$ mod $k$, which finishes the proof. ◻
:::

Finally we discuss how to implement our iterative formulas using the SageMath program.

An algorithm design for Theorem [\[t:MN-gensym\]](#t:MN-gensym){reference-type="ref" reference="t:MN-gensym"} to display all coefficients of the MN rule is as follows:\
Step 1) Given two colored partitions of length $k$ and weight $n$, named $\boldsymbol{\lambda}$ and $\boldsymbol{\rho}$;\
Step 2) Assume the largest part (of weight $m$) in $\boldsymbol{\rho}$ be removed (to reduce the times of iterations), list all colored partitions of weight $n-m$ included in $\boldsymbol{\lambda}$;\
Step 3) Filter out colored partitions $\boldsymbol{\lambda_j}$ such that skew partition $\boldsymbol{\lambda}-\boldsymbol{\lambda_j}$ is a rim hook, and compute the corresponding coefficient.

An algorithm outline of listing all coefficients for Theorem [\[t:3.9\]](#t:3.9){reference-type="ref" reference="t:3.9"} goes as follows.\
Step 1) Given two colored partitions of length $k$ and weight $n$, named $\boldsymbol{\lambda}$ and $\boldsymbol{\rho}$;\
Step 2) Identify and remove the largest part in $\boldsymbol{\lambda}$ (of weight $s$), filter out sub-partitions $\boldsymbol{\mu}$ of $\boldsymbol{\rho}$ with weight less than or equal to $n-s$, and corresponding partitions $\tau$ of size $n-s-|\boldsymbol{\mu}|$, then compute the corresponding coefficients;\
Step 3) List all possible colored partitions $\boldsymbol{\tau}$ corresponding $\tau$, also compute each of coefficient.

To end this section, we list the character tables of $C_3\wr S_1$, $C_3\wr S_2$, $C_3\wr S_3$, we denote by $\omega$ the 3-rd primitive root of unity.

   $\gamma\backslash c$     $c_1$        $c_2$      $c_3$
  ---------------------- ------------ ------------ -------
        $\gamma_1$            1            1          1
        $\gamma_2$         $\omega$    $\omega^2$     1
        $\gamma_3$        $\omega^2$    $\omega$      1

  : $C_3\wr S_1$

where $\gamma_1=c_3=((1),\emptyset,\emptyset)$; $\gamma_2=c_2=(\emptyset,(1),\emptyset)$; $\gamma_3=c_1=(\emptyset,\emptyset,(1))$.

   $\gamma\backslash c$      $c_1$         $c_2$       $c_3$      $c_4$         $c_5$          $c_6$          $c_7$       $c_8$   $c_9$
  ---------------------- ------------- -------------- ------- ------------- -------------- -------------- -------------- ------- -------
        $\gamma_1$             1             1           1          1             1              1              1           1       1
        $\gamma_2$             1             -1          1          1             -1             1              1           1      -1
        $\gamma_3$         2$\omega$         0          -1     2$\omega^2$        0         \-$\omega^2$    \-$\omega$      2       0
        $\gamma_4$        2$\omega^2$        0          -1      2$\omega$         0          \-$\omega$    \-$\omega^2$     2       0
        $\gamma_5$        $\omega^2$      $\omega$       1      $\omega$      $\omega^2$      $\omega$      $\omega^2$      1       1
        $\gamma_6$        $\omega^2$     \-$\omega$      1      $\omega$     \-$\omega^2$     $\omega$      $\omega^2$      1      -1
        $\gamma_7$             2             0          -1          2             0              -1             -1          2       0
        $\gamma_8$         $\omega$      $\omega^2$      1     $\omega^2$      $\omega$      $\omega^2$      $\omega$       1       1
        $\gamma_9$         $\omega$     \-$\omega^2$     1     $\omega^2$     \-$\omega$     $\omega^2$      $\omega$       1      -1

  : $C_3\wr S_2$

where $\gamma_1=c_9=((2),\emptyset,\emptyset)$; $\gamma_2=c_8=((1,1),\emptyset,\emptyset)$; $\gamma_3=c_7=((1),(1),\emptyset)$; $\gamma_4=c_6=((1),\emptyset,(1))$; $\gamma_5=c_5=(\emptyset,(2),\emptyset)$; $\gamma_6=c_4=(\emptyset,(1,1),\emptyset)$; $\gamma_7=c_3=(\emptyset,(1),(1))$; $\gamma_8=c_2=(\emptyset,\emptyset,(2))$; $\gamma_9=c_1=(\emptyset,\emptyset,(1,1))$.

where $\gamma_1=c_{22}=((3),\emptyset,\emptyset)$; $\gamma_2=c_{21}=((2,1),\emptyset,\emptyset)$; $\gamma_3=c_{20}=((1,1,1),\emptyset,\emptyset)$; $\gamma_4=c_{19}=((2),(1),\emptyset)$; $\gamma_5=c_{18}=((1,1),(1),\emptyset)$; $\gamma_6=c_{17}=((2),\emptyset,(1))$; $\gamma_7=c_{16}=((1,1),\emptyset,(1))$; $\gamma_8=c_{15}=((1),(2),\emptyset)$; $\gamma_9=c_{14}=((1),(1,1),\emptyset)$; $\gamma_{10}=c_{13}=((1),(1),(1))$; $\gamma_{11}=c_{12}=((1),\emptyset,(2))$; $\gamma_{12}=c_{11}=((1),\emptyset,(1,1))$; $\gamma_{13}=c_{10}=(\emptyset,(3),\emptyset)$; $\gamma_{14}=c_9=(\emptyset,(2,1),\emptyset)$; $\gamma_{15}=c_8=(\emptyset,(1,1,1),\emptyset)$; $\gamma_{16}=c_7=(\emptyset,(2),(1))$; $\gamma_{17}=c_6=(\emptyset,(1,1),(1))$; $\gamma_{18}=c_5=(\emptyset,(1),(2))$; $\gamma_{19}=c_4=(\emptyset,(1),(1,1))$; $\gamma_{20}=c_3=(\emptyset,\emptyset,(3))$; $\gamma_{21}=c_2=(\emptyset,\emptyset,(2,1))$; $\gamma_{22}=c_1=(\emptyset,\emptyset,(1,1,1))$.

Moreover, by Theorem 4.4, one has

::: center
   $\lambda\backslash c$   $(9)$   $(6,3)$   $(3,3,3)$
  ----------------------- ------- --------- -----------
         $(7,1,1)$           1        1          1
      $(4,1,1,1,1,1)$        2        0          2
   $(1,1,1,1,1,1,1,1,1)$     1        2          1
         $(4,3,2)$           0        2          0
      $(2,2,2,1,1,1)$        0        2          0
         $(4,4,1)$           0        1          0
      $(3,2,1,1,1,1)$        0        1          0
         $(5,2,2)$           0        1          0
       $(2,2,2,2,1)$         0        1          0
         $(3,3,3)$           0        0          0
         $(6,2,1)$           0        2          0
        $(3,2,2,2)$          0        2          0
          $(8,1)$            2        2          2
       $(5,1,1,1,1)$         1        0          1
    $(2,1,1,1,1,1,1,1)$      2        1          2
          $(5,4)$            0        2          0
       $(3,3,1,1,1)$         0        2          0
          $(6,3)$            0        1          0
        $(3,3,2,1)$          0        1          0
           $(9)$             1        1          1
        $(6,1,1,1)$          2        0          2
     $(3,1,1,1,1,1,1)$       1        2          1

  : $S_9$ mod 3
:::

where $\lambda$ corresponds to $\gamma_1\sim \gamma_{22}$. They are consistient with the elements in the character table of $S_9$ mod 3.

**Acknowledgments**

The work is supported in part by the Simons Foundation grant no. MP-TSM-00002518 and the National Natural Science Foundation of China grant nos. 12171303.
