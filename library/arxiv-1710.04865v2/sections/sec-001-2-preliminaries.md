---
doc_id: arxiv-1710.04865v2
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 6-12
source_pdf: 1710.04865v2.pdf
source_sha256: ac8f436173d550e8
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
duplicate_of: "cjdoubletwistfinal"
text_source: latex
latex_prose_ratio: 0.649
latex_coverage_ratio: 0.981
---
We begin by recalling the setup from [@takata]. Let $l$ and $t$ be coprime odd integers with $l > t \geq 1$ and $p^{\prime} := \frac{l-1}{2}$. For $1 \leq j \leq p^{\prime}$, define integers $r(j)$ such that $r(j) \equiv (2j-1)t \pmod{2l}$ and $-l < r(j) < l$. We put $\sigma_j := (-1)^{\lfloor \frac{(2j-1)t}{l}\rfloor}$, $r^{\prime}(j) := \frac{\mid r(j) \mid + 1}{2}$ and $i_{r^{\prime}(j)}=j$ (and thus $i_k = j$ if and only if $r^{\prime}(j)=k$). For an integer $i$, sgn($i$) denotes the sign of $i$. Let $\underline{n} = (n_1, \dotsc, n_{p^{\prime}})$ and $n_s=0$ for $s \leq 0$. Finally, define

$$\label{kappa}
\kappa(p^{\prime})= \left\{
\begin{array}{ll}
-Nn_{p^{\prime}} & \text{if $\sigma_{p^{\prime}}=-1$,} \\
0 & \text{if $\sigma_{p^{\prime}}=1$} \\
\end{array} \right. \\$$

and

$$\label{tau}
\tau(j) = \left\{
\begin{array}{ll}
(-1)^{n_j - n_{j-1}} & \text{if $\sigma_j=-1$,} \\
q^{\binom{n_j - n_{j-1} + 1}{2}} & \text{if $\sigma_{j}=1$.} \\
\end{array} \right. \\$$

Consider the family of 2-bridge knots $\frak{b}(l,t)$ [@bz]. The main result in [@takata] is an explicit formula for the colored Jones polynomial of $\frak{b}(l,t)^{*}$.

::: theorem
[]{#takata label="takata"} We have $$\label{spt}
J_N(\frak{b}(l,t)^{*}; q) = \sum_{N-1 \geq n_{p^{\prime}} \geq \dotsc \geq n_1 \geq 0} q^{a({\underline{n}})N + b_1(\underline{n}) + b_2(\underline{n})} X(\underline{n})$$ where[^1] $$\begin{aligned}
a({\underline{n}}) & = -\frac{1}{2} \sum_{j=1}^{p^{\prime}} \Biggl( \sum_{k=r^{\prime}(j)}^{p^{\prime}} (\sigma_{i_k} + \sigma_{i_{p^{\prime} + 1 -k}})\Biggr) (n_j - n_{j-1}) - \frac{1}{2} \sum_{j=1}^{p^{\prime} - 1} (\sigma_{j+1} + \sigma_{p^{\prime} + 1 - j}) n_j \\
& - \frac{1}{2} (\sigma_{p^{\prime}} + 1) n_{p^{\prime}} - \sum_{j=1}^{p^{\prime}} \sigma_j, \\
b_1(\underline{n}) & = - a({\underline{n}}) + \sum_{k=1}^{\frac{l-t}{2}} \frac{1-\sigma_{i_k}}{2} n_{i_k - 1} - \sum_{k=\frac{l-t}{2}+1}^{p^{\prime}} n_{i_k - 1} + \sum_{k=\frac{l-t}{2}+1}^{p^{\prime}} \frac{1+\sigma_{i_k}}{2} n_{i_k} - (1+\sigma_{p^{\prime}}) n_{p^{\prime}} \\
& + \frac{1}{2} \sum_{j=1}^{p^{\prime} - 1} (\sigma_{j+1} - \sigma_j) n_j \\
& - \frac{1}{2} \sum_{k=1}^{p^{\prime} - 1} \sum_{k^{\prime} = k+1}^{p^{\prime}} \frac{1 + \operatorname{sgn}(i_k - i_{k^{\prime}})}{2}(\sigma_{i_k} - \sigma_{i_{k^{\prime}}})(n_{i_k} - n_{i_k - 1})(n_{i_{k^{\prime}}} - n_{i_{k^{\prime}} - 1}) \\
& + \sum_{j=1}^{p^{\prime}} \sigma_j \Bigl( \sum_{k=1}^{r^{\prime}(j)} (n_{i_k} - n_{i_k - 1}) \Bigr) n_{j-1}, \\
b_2(\underline{n}) & = \left\{
\begin{array}{ll}
\displaystyle \sum_{k=\frac{l-t}{2} + 1}^{\frac{t-1}{2}} \frac{1+ \sigma_{i_k}}{2} n_{i_k - 1} & \text{if $l < 2t$} \\
\displaystyle - \sum_{k=\frac{t+1}{2} + 1}^{\frac{l-t}{2}} \frac{1+ \sigma_{i_k}}{2} n_{i_k - 1} & \text{if $l > 2t,$} \\
\end{array} \right. \\
X(\underline{n}) & = (-1)^{n_{p^{\prime}}} q^{\kappa(p^{\prime})} \frac{(q)_{N-1} (q)_{n_{p^{\prime}}}}{(q)_{N-n_{p^{\prime}} - 1}} \prod_{j=1}^{p^{\prime}} \frac{\tau(j)}{(q)_{n_j - n_{j-1}}}.
\end{aligned}$$
:::

As the mirror image of the torus knots $T_{(2, 2t+1)}$ is $\frak{b}(2t+1, 1)$ (cf. [@bz; @petersen; @Tran]), one can check that Theorem [\[takata\]](#takata){reference-type="ref" reference="takata"} recovers the $q$-hypergeometric expression for $J_N(T_{(2, 2t+1)}; q)$ given in [@hikami1; @hikami2]. Our interest will be to apply Theorem [\[takata\]](#takata){reference-type="ref" reference="takata"} to the case of the double twist knots $K_{(m, p)} = \frak{b}(4mp-1, 4mp-2p-1)$ and $K_{(m,-p)}=\frak{b}(4mp+1, 4mp-2p+1)$ (cf. [@Tran]). In order to facilitate these computations, we need the following results concerning $\sigma_j$, $i_k$ and $\sigma_{i_k}$. We omit the proofs as they are straightforward generalizations of Lemmas 6--9 in [@takata].

::: lemma
[]{#l8 label="l8"} For $l=4mp-1$ and $t=4mp-2p-1$, we have\

1.  $\sigma_{j} = \left\{
    \begin{array}{ll}
    1 & \text{if $j \equiv 1, 2, \dotsc, m \pmod{2m}$} \\
    -1 & \text{if $j \equiv 0, m+1, \dotsc, 2m-1 \pmod{2m}.$} \\
    \end{array} \right.$\

2.  To compute $i_k$, apply the following algorithm. Divide the integers from $1$ to $p'$ into $2m-1$ intervals, each of length $p$, and a final interval of length $p -1$. The value of $i_k$ is $2m(p-k) + m$ in the first interval and $1- (2m(p-k) + m)$ in the second. If $j>1$ is odd, then to obtain the value of $i_k$ in the $j$th interval, add $4mp- 1$ to the formula for $i_k$ in the $(j-2)$th interval. If $j > 2$ is even, then to obtain the value of $i_k$ in the $j$th interval, subtract $4mp - 1$ from the formula for $i_k$ in the $(j-2)$th interval.\

3.  To compute $\sigma_{i_k}$, apply the following algorithm. Divide the integers from $1$ to $p'$ into $2m-1$ intervals, each of length $p$, and a final interval of length $p - 1$. The value of $\sigma_{i_k}$ alternates between $1$ and $-1$ starting with $1$ in the first interval.
:::

::: lemma
[]{#l9 label="l9"} Let $l=4mp-1$ and $t=4mp-2p-1$. Then for $1\leq k \leq p'$ and $1\leq j \leq p'-1$ we have\

1.  $\sigma_{i_k} + \sigma_{i_{p^{\prime} + 1 - k}} = \left\{
    \begin{array}{ll}
    2 & \text{if $k = p, 3p, \dotsc, (2m-1)p$} \\
    -2 & \text{if $k = 2p, \dotsc, (2m-2)p$} \\
    0 & \text{otherwise.} \\
    \end{array} \right.$\

2.  $\sigma_{j+1} + \sigma_{p^{\prime} + 1 - j} = 0$.
:::

::: lemma
[]{#l6 label="l6"} For $l=4mp + 1$ and $t=4mp - 2p + 1$, we have\

1.  $\sigma_{j} = \left\{
    \begin{array}{ll}
    1 & \text{if $j \equiv 1, 2, \dotsc, m \pmod{2m}$} \\
    -1 & \text{if $j \equiv 0, m+1, \dotsc, 2m-1 \pmod{2m}.$} \\
    \end{array} \right.$\

2.  To compute $i_k$, apply the following algorithm. Divide the integers from $1$ to $p'$ into $2m$ intervals of length $p$. The value of $i_k$ is $2m(p-k) + m + 1$ in the first interval and $1- (2m(p-k) + m + 1)$ in the second. If $j>1$ is odd, then to obtain the value of $i_k$ in the $j$th interval, add $4mp+1$ to the formula for $i_k$ in the $(j-2)$th interval. If $j > 2$ is even, then to obtain the value of $i_k$ in the $j$th interval, subtract $4mp+1$ from the formula for $i_k$ in the $(j-2)$th interval.\

3.  To compute $\sigma_{i_k}$, apply the following algorithm. Divide the integers from 1 to $p'$ into $2m$ intervals of length $p$. The value of $\sigma_{i_k}$ alternates between $-1$ and $1$ starting with $-1$ in the first interval.
:::

::: lemma
[]{#l7 label="l7"} Let $l=4mp + 1$ and $t=4mp - 2p + 1$. Then for $1\leq k \leq p'$ and $1\leq j \leq p'-1$ we have\

1.  $\sigma_{i_k} + \sigma_{i_{p^{\prime} + 1 - k}} = 0$\

2.  $\sigma_{j+1} + \sigma_{p^{\prime} + 1 - j} =  \left\{
    \begin{array}{ll}
    2 & \text{if $j \equiv 0 \pmod{2m}$} \\
    -2 & \text{if $j \equiv m \pmod{2m}$} \\
    0 & \text{otherwise.} \\
    \end{array} \right.$\
:::

We now illustrate the computation of $a({\underline{n}})$ and $b_1({\underline{n}}) + b_2({\underline{n}})$ for $l=8p-1$ and $t=6p-1$. The routine evaluation of $X(\underline{n})$ is left to the reader. First, we take $m=2$ in Lemmas [\[l8\]](#l8){reference-type="ref" reference="l8"} and [\[l9\]](#l9){reference-type="ref" reference="l9"} to obtain

$$\label{step0}
\sigma_{j} = \left\{
\begin{array}{ll}
1 & \text{if $j \equiv 1, 2 \pmod{4}$} \\
-1 & \text{if $j \equiv 0, 3 \pmod{4},$} \\
\end{array} \right. \\$$

$$\label{step1}
i_k = \left\{
\begin{array}{ll}
4(p-k) + 2 & \text{if $1 \leq k \leq p$,} \\
4(k-p) - 1 & \text{if $p+1 \leq k \leq 2p$,} \\
12p - 4k + 1 & \text{if $2p+1 \leq k \leq 3p$,} \\
 4k - 12p & \text{if $3p+1 \leq k \leq 4p-1$,} \\
\end{array} \right. \\$$

$$\label{step2}
\sigma_{i_k} = \left\{
\begin{array}{ll}
1 & \text{if $1 \leq k \leq p$,} \\
-1 & \text{if $p+1 \leq k \leq 2p$,} \\
1 & \text{if $2p+1 \leq k \leq 3p$,} \\
 -1 & \text{if $3p+1 \leq k \leq 4p-1,$} \\
\end{array} \right. \\$$

$$\label{step3}
\sigma_{i_k} + \sigma_{i_{4p-k}} = \left\{
\begin{array}{ll}
2 & \text{if $k = p, 3p$} \\
-2 & \text{if $k = 2p$} \\
0 & \text{otherwise} \\
\end{array} \right. \\$$ and $$\label{step4}
\sigma_{j+1} + \sigma_{4p - j} = 0.$$

Applying ([\[step0\]](#step0){reference-type="ref" reference="step0"}), ([\[step1\]](#step1){reference-type="ref" reference="step1"}), ([\[step3\]](#step3){reference-type="ref" reference="step3"}), ([\[step4\]](#step4){reference-type="ref" reference="step4"}) and reindexing yields

$$\label{a}
\begin{aligned}
a({\underline{n}}) & = -\frac{1}{2} \sum_{j=1}^{4p-1} \Biggl( \sum_{k=r^{\prime}(j)}^{4p-1} (\sigma_{i_k} + \sigma_{i_{4p - k}})\Biggr) (n_j - n_{j-1}) - 1 \\
& = -\frac{1}{2} \Biggl[ \sum_{j=1}^{p}  \Biggl( \sum_{k=3p-j+1}^{4p-1} (\sigma_{i_k} + \sigma_{i_{4p -k}})\Biggr) (n_{4j-3} - n_{4j-4}) \\
&  + \sum_{j=1}^{p} \Biggl( \sum_{k=p-j+1}^{4p-1} (\sigma_{i_k} + \sigma_{i_{4p -k}})\Biggr) (n_{4j-2} - n_{4j-3}) + \sum_{j=1}^{p-1} \Biggl( \sum_{k=3p+j}^{4p-1} (\sigma_{i_k} + \sigma_{i_{4p -k}})\Biggr) (n_{4j} - n_{4j-1}) \\
& + \sum_{j=1}^{p} \Biggl( \sum_{k=p+j}^{4p-1} (\sigma_{i_k} + \sigma_{i_{4p -k}})\Biggr) (n_{4j-1} - n_{4j-2}) \Biggr] - 1 \\
& = \sum_{j=1}^{2p-1} (-1)^j n_{2j} - 1.
\end{aligned}$$

By ([\[step0\]](#step0){reference-type="ref" reference="step0"}) and ([\[step2\]](#step2){reference-type="ref" reference="step2"}), the second and fifth sums in $b_1({\underline{n}})$ are zero. We then use ([\[step0\]](#step0){reference-type="ref" reference="step0"})--([\[step2\]](#step2){reference-type="ref" reference="step2"}) and reindex to obtain

$$\label{thirdpart}
\begin{aligned}
-\sum_{k=p+1}^{4p-1} n_{i_{k} - 1} & = - \Biggl( \sum_{k=p+1}^{2p} n_{i_{k} - 1} + \sum_{k=2p+1}^{3p} n_{i_{k} - 1} + \sum_{k=3p+1}^{4p-1} n_{i_{k} - 1} \Biggr) \\
& = - \Biggl( \sum_{j=1}^{p} (n_{4j-2} + n_{4j-4}) + \sum_{j-1}^{p-1} n_{4j-1} \Biggr),
\end{aligned}$$

$$\label{fourthpart}
\sum_{k=p+1}^{4p-1} \frac{1+\sigma_{i_k}}{2} n_{i_k} = \sum_{k=2p+1}^{3p} n_{i_k} = \sum_{j=1}^{p} {n_{4j-3}},$$

$$\label{sixthpart}
\frac{1}{2} \sum_{j=1}^{4p-2} (\sigma_{j+1} - \sigma_j) n_j = \sum_{j=1}^{2p-1} (-1)^j n_{2j}$$ and $$\label{b2}
b_2({\underline{n}}) = \sum_{k=p+1}^{3p-1} \frac{1+\sigma_{i_k}}{2} n_{{i_k} - 1} = \sum_{k=2p+1}^{3p-1} n_{{i_k} - 1} = \sum_{j=2}^{p} n_{4j-4}.$$ By ([\[a\]](#a){reference-type="ref" reference="a"})--([\[b2\]](#b2){reference-type="ref" reference="b2"}), the sum of $b_2({\underline{n}})$ and the first six terms in $b_1({\underline{n}})$ equals

$$\label{sixb1b2}
1 + n_{4p-1}  + \sum_{j=1}^{p} (n_{4j-3} - n_{4j-2} - n_{4j-1}).$$

To compute the seventh term in $b_1({\underline{n}})$, we use ([\[step1\]](#step1){reference-type="ref" reference="step1"}) and ([\[step2\]](#step2){reference-type="ref" reference="step2"}) to observe that $k < k^{\prime}$ and $\sigma_{i_k} \neq \sigma_{i_{k^{\prime}}}$ if and only if either $1 \leq k \leq p$ and $p+1 \leq k^{\prime} \leq 2p$ or $1 \leq k \leq p$ and $3p+1 \leq k^{\prime} \leq 4p-1$ or $p+1 \leq k \leq 2p$ and $2p+1 \leq k^{\prime} \leq 3p$ or $2p+1 \leq k \leq 3p$ and $3p+1 \leq k^{\prime} \leq 4p-1$. Also, $\operatorname{sgn}(i_k - i_{k^{\prime}}) = 1$ if and only if $i_k > i_{k^{\prime}}$ and either $i_k = 4p-4k+2$ for $1 \leq k \leq p$ and $i_{k^{\prime}} = 4k^{\prime} - 4p - 1$ for $p+1 \leq k^{\prime} \leq 2p$ or $i_k = 4p-4k+2$ for $1 \leq k \leq p$ and $i_{k^{\prime}} = 4k^{\prime} -12p$ for $3p+1 \leq k^{\prime} \leq 4p-1$ or $i_k = 4k-4p-1$ for $p+1 \leq k \leq 2p$ and $i_{k^{\prime}} = 12p - 4k^{\prime} + 1$ for $2p+1 \leq k^{\prime} \leq 3p$ or $i_k = 12p - 4k + 1$ for $2p+1 \leq k \leq 3p$ and $i_{k^{\prime}} = 4k^{\prime} - 12p$ for $3p+1 \leq k^{\prime} \leq 4p-1$. Taking these cases into account and reindexing, we have

$$\begin{aligned}
& - \frac{1}{2} \sum_{k=1}^{4p-2} \sum_{k^{\prime} = k+1}^{4p-1} \frac{1 + \operatorname{sgn}(i_k - i_{k^{\prime}})}{2}(\sigma_{i_k} - \sigma_{i_{k^{\prime}}})(n_{i_k} - n_{i_k - 1})(n_{i_{k^{\prime}}} - n_{i_{k^{\prime}} - 1}) \\
& = - \sum_{k=1}^{p} \sum_{k^{\prime} = p+1}^{2p-k} (n_{i_k} - n_{i_k - 1})(n_{i_{k^{\prime}}} - n_{i_{k^{\prime}} - 1}) - \sum_{k=1}^{p} \sum_{k^{\prime}=3p+1}^{4p-k} (n_{i_k} - n_{i_k - 1})(n_{i_{k^{\prime}}} - n_{i_{k^{\prime}} - 1}) \\
& + \sum_{k=p+1}^{2p} \sum_{k^{\prime} = 4p-k+1}^{3p} (n_{i_k} - n_{i_k - 1})(n_{i_{k^{\prime}}} - n_{i_{k^{\prime}} - 1}) - \sum_{k=2p+1}^{3p} \sum_{k^{\prime} = 3p+1}^{6p-k} (n_{i_k} - n_{i_k - 1})(n_{i_{k^{\prime}}} - n_{i_{k^{\prime}} - 1}) \\
& = - \sum_{j=1}^{p} \sum_{j^{\prime}=2}^{j} (n_{4j-2} - n_{4j-3})(n_{4j^{\prime} - 5} - n_{4j^{\prime} - 6}) - \sum_{j=1}^{p} \sum_{j^{\prime}=2}^{j} (n_{4j-2} - n_{4j-3})(n_{4j^{\prime} -4} - n_{4j^{\prime} - 5}) \\
\end{aligned}$$

$$\label{sevenb1}
\begin{aligned}
& + \sum_{j=1}^{p} \sum_{j^{\prime} = 1}^{j} (n_{4j-1} - n_{4j-2})(n_{4j^{\prime} - 3} - n_{4j^{\prime} - 4}) - \sum_{j=1}^{p} \sum_{j^{\prime}=2}^{j} (n_{4j-3} - n_{4j-4})(n_{4j^{\prime}-4} - n_{4j^{\prime} - 5}).
\end{aligned}$$

Finally, using ([\[step0\]](#step0){reference-type="ref" reference="step0"}) and ([\[step1\]](#step1){reference-type="ref" reference="step1"}), then reindexing and simplifying gives the eighth term in $b_1(\underline{n})$,

$$\label{lastb1}
\begin{aligned}
& \sum_{j=1}^{4p-1} \sigma_j \Bigl( \sum_{k=1}^{r^{\prime}(j)} (n_{i_k} - n_{i_k - 1}) \Bigr) n_{j-1} \\
& = \sum_{j=1}^{p} \sigma_{4j-3} \Bigl( \sum_{k=1}^{3p-j+1} (n_{i_k} - n_{i_k - 1}) \Bigr) n_{4j-4} +  \sum_{j=1}^{p} \sigma_{4j-2} \Bigl( \sum_{k=1}^{p-j+1} (n_{i_k} - n_{i_k - 1}) \Bigr) n_{4j-3} \\
& +  \sum_{j=1}^{p-1} \sigma_{4j} \Bigl( \sum_{k=1}^{3p+j} (n_{i_k} - n_{i_k - 1}) \Bigr) n_{4j-1} +  \sum_{j=1}^{p} \sigma_{4j-1} \Bigl( \sum_{k=1}^{p+j} (n_{i_k} - n_{i_k - 1}) \Bigr) n_{4j-2} \\
& = \sum_{j=1}^{p} \Biggl( \sum_{k=1}^{p} (n_{4p-4k+2} - n_{4p-4k+1}) + \sum_{k=p+1}^{2p} (n_{4k-4p-1} - n_{4k-4p-2}) \\
& + \sum_{k=2p+1}^{3p-j+1} (n_{12p - 4k + 1} - n_{12p - 4k}) \Biggr) n_{4j-4} + \sum_{j=1}^{p} \Biggl( \sum_{k=1}^{p-j+1} (n_{4p-4k+2} - n_{4p-4k+1}) \Biggr) n_{4j-3} \\
& - \sum_{j=1}^{p-1} \Biggl( \sum_{k=1}^{p} (n_{4p-4k+2} - n_{4p-4k+1}) + \sum_{k=p+1}^{2p} (n_{4k-4p-1} - n_{4k-4p-2}) \\
& + \sum_{k=2p+1}^{3p} (n_{12p - 4k + 1} - n_{12p - 4k}) + \sum_{k=3p+1}^{3p+j} (n_{4k-12p} - n_{4k-12p-1}) \Biggr) n_{4j-1} \\
& - \sum_{j=1}^{p} \Biggl( \sum_{k=1}^{p} (n_{4p-4k+2} - n_{4p-4k+1}) + \sum_{k=p+1}^{p+j} (n_{4k-4p-1} - n_{4k-4p-2}) \Biggr) n_{4j-2} \\
& = \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j-1} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 3}) + \sum_{j=j^{\prime}}^{p} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 4}) \Biggr) n_{4j-4} + \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime} = j}^{p} (n_{4j^{\prime} - 2} - n_{4j^{\prime} - 3} ) \Biggr) n_{4j-3} \\
& - \sum_{j=1}^{p-1} \Biggl( \sum_{j^{\prime} = j+1}^{p} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 4}) + n_{4j}\Biggr) n_{4j-1} \\
& - \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 3}) + \sum_{j^{\prime}=j+1}^{p} (n_{4j^{\prime} - 2} - n_{4j^{\prime} - 3}) \Biggr) n_{4j-2}.
\end{aligned}$$

Thus, combining ([\[a\]](#a){reference-type="ref" reference="a"})--([\[lastb1\]](#lastb1){reference-type="ref" reference="lastb1"}) implies that $b_1({\underline{n}}) + b_2({\underline{n}})$ equals

$$\begin{aligned}
& 1 + n_{4p-1}  + \sum_{j=1}^{p} (n_{4j-3} - n_{4j-2} - n_{4j-1}) \\
& - \sum_{j=1}^{p} \sum_{j^{\prime}=2}^{j} (n_{4j-2} - n_{4j-3})(n_{4j^{\prime} - 5} - n_{4j^{\prime} - 6}) - \sum_{j=1}^{p} \sum_{j^{\prime}=2}^{j} (n_{4j-2} - n_{4j-3})(n_{4j^{\prime} -4} - n_{4j^{\prime} - 5}) \\
& + \sum_{j=1}^{p} \sum_{j^{\prime} = 1}^{j} (n_{4j-1} - n_{4j-2})(n_{4j^{\prime} - 3} - n_{4j^{\prime} - 4}) - \sum_{j=1}^{p} \sum_{j^{\prime}=2}^{j} (n_{4j-3} - n_{4j-4})(n_{4j^{\prime}-4} - n_{4j^{\prime} - 5}) \\
& + \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j-1} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 3}) + \sum_{j=j^{\prime}}^{p} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 4}) \Biggr) n_{4j-4} + \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime} = j}^{p} (n_{4j^{\prime} - 2} - n_{4j^{\prime} - 3} ) \Biggr) n_{4j-3} \\
& - \sum_{j=1}^{p-1} \Biggl( \sum_{j^{\prime} = j+1}^{p} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 4}) + n_{4j}\Biggr) n_{4j-1} \\
& - \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 3}) + \sum_{j^{\prime}=j+1}^{p} (n_{4j^{\prime} - 2} - n_{4j^{\prime} - 3}) \Biggr) n_{4j-2}.
\end{aligned}$$

# Proofs of Theorems [\[main1\]](#main1){reference-type="ref" reference="main1"} and [\[main2\]](#main2){reference-type="ref" reference="main2"}

::: proof
*Proof of Theorem [\[main1\]](#main1){reference-type="ref" reference="main1"}.* As ([\[JNK-m-p\]](#JNK-m-p){reference-type="ref" reference="JNK-m-p"}) reduces to ([\[kppos\]](#kppos){reference-type="ref" reference="kppos"}) when $m=1$ and this case was proven in [@takata], we assume $m \geq 2$. Using Lemmas [\[l8\]](#l8){reference-type="ref" reference="l8"} and [\[l9\]](#l9){reference-type="ref" reference="l9"}, one can check that for $l=4mp-1$ and $t=4mp-2p-1$

$$\label{a2}
a({\underline{n}}) = \sum_{j=1}^{2p - 1} (-1)^j n_{mj} - 1$$

and $b_1({\underline{n}}) + b_2({\underline{n}})$ equals

$$\begin{aligned}
& 1 + n_{2mp - 1} + \sum_{j=1}^{p} \Biggl( \sum_{i=1}^{m-1} n_{2mj - 2m + i} - \sum_{i=m}^{2m-1} n_{2mj - 2m + i} \Biggr) \\
& + \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j} \sum_{k=1}^{m-1} \sum_{k^{\prime}=1}^{k} 
(n_{2mj - k} - n_{2mj - k - 1})(n_{2mj^{\prime} - 2m + k - k^{\prime} + 1} - n_{2mj^{\prime} - 2m + k - k^{\prime}}) \\
& - \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j} \sum_{k=1}^{m} \sum_{k^{\prime}=1}^{m-k+1} 
(n_{2mj - m - k + 1} - n_{2mj - m - k})(n_{2mj^{\prime} - 2m - k^{\prime} + 1} - n_{2mj^{\prime} - 2m - k^{\prime}}) \\
& + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime} = 1}^{j-1} (n_{2mj^{\prime} - s} - n_{2mj^{\prime} - 2m + s}) + \sum_{j^{\prime}=j}^{p} (n_{2mj^{\prime} - s} - n_{2mj^{\prime} - 2m + s-1} ) \Biggr) n_{2mj - 2m + s-1} \\
\end{aligned}$$

$$\label{b1b2c2}  
\begin{aligned}
& + \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=j}^{p} (n_{2mj^{\prime} - m} - n_{2mj^{\prime} - m -1}) \Biggr) n_{2mj - m - 1} \\
& - \sum_{j=1}^{p - 1} \Biggl( \sum_{j^{\prime} = j+1}^{p} (n_{2mj^{\prime} - 1} - n_{2mj^{\prime} - 2m} ) + n_{2mj} \Biggr) n_{2mj - 1} \hphantom{xxxxxxxxxxxxxxxxxxxxxxxxx} \\
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j} (n_{2mj^{\prime} - m + s} - n_{2mj^{\prime} - m - s}) + \sum_{j^{\prime}=j+1}^{p} (n_{2mj^{\prime} - m + s-1} - n_{2mj^{\prime} - m - s}) \Biggr) n_{2mj - m + s - 1}.
\end{aligned}$$

Also, by ([\[kappa\]](#kappa){reference-type="ref" reference="kappa"}) and ([\[tau\]](#tau){reference-type="ref" reference="tau"})

$$\label{twist2}
\begin{aligned}
X({\underline{n}}) & = (-1)^{n_{2mp - 1}} q^{-Nn_{2mp - 1}} \frac{(q)_{N-1} (q)_{n_{2mp - 1}}}{(q)_{N - n_{2mp - 1} - 1}} \\
& \times \prod_{j=1}^{p} \frac{(-1)^{n_{2mj - 1} - n_{2mj-m}} q^{\frac{1}{2} \sum\limits_{s=1}^{m} (n_{2mj-2m+s} - n_{2mj-2m+s-1})(n_{2mj-2m+s} - n_{2mj-2m+s-1} + 1)}}{\displaystyle \prod\limits_{s=1}^{2m-1} (q)_{n_{2mj-2m+s} - n_{2mj-2m+s-1}}} \\
& \times \prod_{j=1}^{p- 1} \frac{(-1)^{n_{2mj} - n_{2mj-1}}}{(q)_{n_{2mj} - n_{2mj-1}}}.
\end{aligned}$$

Upon comparing ([\[spt\]](#spt){reference-type="ref" reference="spt"}) and ([\[a2\]](#a2){reference-type="ref" reference="a2"})--([\[twist2\]](#twist2){reference-type="ref" reference="twist2"}) with ([\[JNK-m-p\]](#JNK-m-p){reference-type="ref" reference="JNK-m-p"}) and then simplifying, it suffices to prove that for $m \geq 2$

$$\begin{aligned}
& \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j} \sum_{k=1}^{m-1} \sum_{k^{\prime}=1}^{k} 
(n_{2mj - k} - n_{2mj - k - 1})(n_{2mj^{\prime} - 2m + k - k^{\prime} + 1} - n_{2mj^{\prime} - 2m + k - k^{\prime}}) \\
& - \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j} \sum_{k=1}^{m} \sum_{k^{\prime}=1}^{m-k+1} 
(n_{2mj - m - k + 1} - n_{2mj - m - k})(n_{2mj^{\prime} - 2m - k^{\prime} + 1} - n_{2mj^{\prime} - 2m - k^{\prime}}) \\
& + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime} = 1}^{j-1} (n_{2mj^{\prime} - s} - n_{2mj^{\prime} - 2m + s}) + \sum_{j^{\prime}=j}^{p} (n_{2mj^{\prime} - s} - n_{2mj^{\prime} - 2m + s-1} ) \Biggr) n_{2mj - 2m + s-1} \\
& + \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=j}^{p} (n_{2mj^{\prime} - m} - n_{2mj^{\prime} - m -1}) \Biggr) n_{2mj - m - 1} \\
& - \sum_{j=1}^{p - 1} \Biggl( \sum_{j^{\prime} = j+1}^{p} (n_{2mj^{\prime} - 1} - n_{2mj^{\prime} - 2m} ) + n_{2mj} \Biggr) n_{2mj - 1} \\
\end{aligned}$$

$$\label{lhs}
\begin{aligned}
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j} (n_{2mj^{\prime} - m + s} - n_{2mj^{\prime} - m - s}) + \sum_{j^{\prime}=j+1}^{p} (n_{2mj^{\prime} - m + s-1} - n_{2mj^{\prime} - m - s}) \Biggr) n_{2mj - m + s - 1} \\
& + \sum_{j=1}^{p} \Biggl[ \binom{n_{2mj-2m+1} + 1}{2} - n_{2mj-2m+1} n_{2mj-2m} + \binom{n_{2mj-m-1}}{2} - n_{2mj-m} n_{2mj-m-1} \\
& + \frac{1}{2} \sum_{s=2}^{m-1} (n_{2mj-2m+s} - n_{2mj-2m+s-1})(n_{2mj-2m+s} - n_{2mj-2m+s-1} + 1) \Biggr]
\end{aligned}$$

equals

$$\label{newrhs}
\displaystyle{\sum_{\substack{1 \leq i < j \leq 2mp-1 \\ m \nmid i}} \epsilon_{i,j,m} n_i n_j} - \displaystyle \sum_{i=1}^{2mp-2} n_i n_{i+1}$$

where $\epsilon_{i,j,m}$ is given by ([\[epsilondef\]](#epsilondef){reference-type="ref" reference="epsilondef"}). Here, we have used the fact that

$$\label{s1}
\sum_{j=1}^{p} \Biggl( \sum_{i=1}^{m-1} n_{2mj - 2m + i} - \sum_{i=m}^{2m-2} n_{2mj - 2m+i} \Biggr) - \sum_{j=1}^{p-1} n_{2mj-1} =  \sum_{i=1}^{2mp-2} \gamma_{i,m} n_i + \sum_{i=1}^{p-1} n_{2mi},$$

where $\gamma_{i,m}$ is given by ([\[gammadef\]](#gammadef){reference-type="ref" reference="gammadef"}), together with the identities

$$\label{s2}
\begin{aligned}
& \frac{1}{2} \sum_{j=1}^{p} \sum_{s=1}^{m} (n_{2mj-2m+s} - n_{2mj-2m+s-1})(n_{2mj-2m+s} - n_{2mj-2m+s-1} + 1) \\
& = \sum_{j=1}^{p} \binom{n_{2mj - 2m}}{2} + \binom{n_{2mj-m} + 1}{2} \\
& + \sum_{j=1}^{p} \Biggl[ \binom{n_{2mj-2m+1} + 1}{2} - n_{2mj-2m+1} n_{2mj-2m} + \binom{n_{2mj-m-1}}{2} - n_{2mj-m} n_{2mj-m-1} \\
& + \frac{1}{2} \sum_{s=2}^{m-1} (n_{2mj-2m+s} - n_{2mj-2m+s-1})(n_{2mj-2m+s} - n_{2mj-2m+s-1} + 1) \Biggr] \hphantom{xxxxxxxxxx}
\end{aligned}$$

and

$$\label{s3}
\sum_{j=1}^{p} \binom{n_{2mj - 2m}}{2} + \binom{n_{2mj-m} + 1}{2} + \sum_{i=1}^{p-1} n_{2mi}= \sum_{i=1}^{2p-1} \binom{n_{mi} + 1}{2}.$$

We now sketch how to proceed from [\[lhs\]](#lhs){reference-type="eqref" reference="lhs"} to [\[newrhs\]](#newrhs){reference-type="eqref" reference="newrhs"}. Let $L_{i}$ denote the $i$th line of [\[lhs\]](#lhs){reference-type="eqref" reference="lhs"}. First, note that

$$\label{l7l8}
L_7 + L_8 = \sum_{j=0}^{p-1} \sum_{i=1}^{m-1} n_{2mj+i}^2 - \sum_{j=0}^{p-1} \sum_{i=1}^{m} n_{2mj+i-1}n_{2mj+i}.$$

Next, observe that both $L_1$ and $L_2$ simplify as the sum on $k'$ telescopes in each case. Thus,

$$\label{newl1hat}
L_1 = \sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j} (n_{2mj-k} - n_{2mj-k-1})(n_{2mj' - 2m + k} - n_{2mj' - 2m})$$

$$\label{newl2hat}
L_2 = - \sum_{k=1}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j} (n_{2mj - m - k +1} - n_{2mj - m- k})(n_{2mj'-2m} - n_{2mj' - 3m + k-1}).$$

Now, splitting $L_1$ into two sums according to the second factor and then using the fact that the resulting second sum telescopes gives

$$\begin{aligned}
L_1 &= \sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j} (n_{2mj - k} - n_{2mj-k-1}) n_{2mj'-2m+k} + \sum_{j=1}^{p} \sum_{j'=1}^{j} (n_{2mj-m} - n_{2mj-1}) n_{2mj'-2m} \nonumber \\
&= \sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj - k}  n_{2mj'-2m+k} - \sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-k-1} n_{2mj'-2m+k}  \nonumber \\
& + \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-m}n_{2mj'-2m} - \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-1} n_{2mj'-2m}. \label{newl1}
\end{aligned}$$

A similar simplification for [\[newl2hat\]](#newl2hat){reference-type="eqref" reference="newl2hat"} yields

$$\begin{aligned}
L_2 &= - \sum_{j=1}^{p} \sum_{j'=1}^{j} (n_{2mj-m} - n_{2mj-2m})  n_{2mj'-2m}  \nonumber \\
&\qquad \qquad \qquad + \sum_{k=1}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j} (n_{2mj-m-k+1} - n_{2mj-m-k}) n_{2mj'-3m+k-1} \nonumber \\
&=  - \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-m}n_{2mj'-2m} + \sum_{j=1}^{p} \sum_{j'=1}^{j}n_{2mj-2m}  n_{2mj'-2m} \nonumber \\
& + \sum_{k=1}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-m-k+1}n_{2mj'-3m+k-1} - \sum_{k=1}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-m-k} n_{2mj'-3m+k-1}. 
\label{newl2}
\end{aligned}$$

Observe that the third sum in [\[newl1\]](#newl1){reference-type="eqref" reference="newl1"} cancels with the first sum in [\[newl2\]](#newl2){reference-type="eqref" reference="newl2"}. Also, if we take $s=1$ in the second triple sum of $L_3$, $$\sum_{s=1}^{m-1} \sum_{j=1}^{p}  \sum_{j^{\prime}=j}^{p} (n_{2mj^{\prime} - s} - n_{2mj^{\prime} - 2m + s-1} ) n_{2mj - 2m + s-1},$$ then this cancels with the fourth sum of [\[newl1\]](#newl1){reference-type="eqref" reference="newl1"} and the second sum of [\[newl2\]](#newl2){reference-type="eqref" reference="newl2"}. Putting all of this together and expanding sums we have that [\[lhs\]](#lhs){reference-type="eqref" reference="lhs"} equals

$$\label{newlhs}
\begin{aligned}
& \sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-k} n_{2mj' - 2m + k} - \sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-k-1} n_{2mj' - 2m + k} \\
& + \sum_{k=1}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-m-k+1}n_{2mj'-3m+k-1} - \sum_{k=1}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-m-k} n_{2mj'-3m+k-1} \\
& + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj'-s}n_{2mj-2m+s-1} - \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj'-2m+s} n_{2mj-2m+s-1} \\
& + \sum_{s=2}^{m-1} \sum_{j=1}^{p} \sum_{j'=j}^{p} n_{2mj'-s} n_{2mj-2m + s-1} - \sum_{s=2}^{m-1} \sum_{j=1}^{p} \sum_{j'=j}^{p} n_{2mj'-2m + s-1}  n_{2mj-2m + s-1} \\
& + \sum_{j=1}^{p}  \sum_{j^{\prime}=j}^{p} n_{2mj^{\prime} - m}n_{2mj - m - 1} - \sum_{j=1}^{p}  \sum_{j^{\prime}=j}^{p} n_{2mj^{\prime} - m -1}  n_{2mj - m - 1} \\
& - \sum_{j=1}^{p - 1} \sum_{j^{\prime} = j+1}^{p} n_{2mj^{\prime} - 1}n_{2mj - 1} + \sum_{j=1}^{p - 1} \sum_{j^{\prime} = j+1}^{p} n_{2mj^{\prime} - 2m}n_{2mj - 1} -  \sum_{j=1}^{p - 1}n_{2mj} n_{2mj - 1} \\
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p}  \sum_{j^{\prime}=1}^{j} n_{2mj^{\prime} - m + s}n_{2mj - m + s - 1} +  \sum_{s=1}^{m-1} \sum_{j=1}^{p}  \sum_{j^{\prime}=1}^{j} n_{2mj^{\prime} - m - s}n_{2mj - m + s - 1}  \\
&-  \sum_{s=1}^{m-1} \sum_{j=1}^{p}\sum_{j^{\prime}=j+1}^{p} n_{2mj^{\prime} - m + s-1}n_{2mj - m + s - 1} + \sum_{s=1}^{m-1} \sum_{j=1}^{p}\sum_{j^{\prime}=j+1}^{p}n_{2mj^{\prime} - m - s} n_{2mj - m + s - 1} \\
& + \sum_{j=0}^{p-1} \sum_{i=1}^{m-1} n_{2mj+i}^2 - \sum_{j=0}^{p-1} \sum_{i=1}^{m} n_{2mj+i-1}n_{2mj+i}.
\end{aligned}$$

The second sum on the fifth line of [\[newlhs\]](#newlhs){reference-type="eqref" reference="newlhs"} can now be taken into the second sum of the fourth line, increasing the upper limit of summation there to $m$. In this sum, we can then exchange $j$ and $j'$ and reindex, giving $$-\sum_{s=2}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-2m + s-1}  n_{2mj'-2m + s-1}.$$ Now take out the term $j' = j$ and shift the indices in this term by $j \to j+1$ and $s \to s+1$ to cancel with the first sum on the last line of [\[newlhs\]](#newlhs){reference-type="eqref" reference="newlhs"}. Finally, in the second line of [\[newlhs\]](#newlhs){reference-type="eqref" reference="newlhs"}, perform the shift $j' \to j'+1$ and start the sum at $j'=1$ (as $j'=0$ gives 0) to obtain

$$\label{step}
\sum_{k=1}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj-m-k+1} n_{2mj'-m+k-1}
- \sum_{k=1}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj-m-k} n_{2mj'-m+k-1}.$$

We now remove the $k=m$ term from the second sum in [\[step\]](#step){reference-type="eqref" reference="step"} and note that what remains cancels with the second sum in the penultimate line of [\[newlhs\]](#newlhs){reference-type="eqref" reference="newlhs"}. In total, this yields that [\[lhs\]](#lhs){reference-type="eqref" reference="lhs"} equals

$$\label{newlhs1}
\begin{aligned}
& \sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-k}n_{2mj' - 2m + k} -\sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj-k-1} n_{2mj' - 2m + k} \\
& + \sum_{k=1}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj-m-k+1} n_{2mj'-m + k -1} - \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj-2m} n_{2mj'-1} \\
& + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj'-s}n_{2mj-2m+s-1} - \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj'-2m+s} n_{2mj-2m+s-1}  \\
&+ \sum_{s=2}^{m-1} \sum_{j=1}^{p} \sum_{j'=j}^{p} n_{2mj'-s} n_{2mj-2m + s-1}  - \sum_{s=2}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj-2m+s-1} n_{2mj' - 2m + s-1} \\
& + \sum_{j=1}^{p} \sum_{j'=j}^{p} n_{2mj'-m} n_{2mj-m-1} \\
& - \sum_{j=1}^{p - 1} \sum_{j^{\prime} = j+1}^{p} n_{2mj^{\prime} - 1}n_{2mj - 1} + \sum_{j=1}^{p - 1} \sum_{j^{\prime} = j+1}^{p} n_{2mj^{\prime} - 2m}n_{2mj - 1} -  \sum_{j=1}^{p - 1}n_{2mj} n_{2mj - 1}  \\
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p}  \sum_{j^{\prime}=1}^{j} n_{2mj^{\prime} - m + s}n_{2mj - m + s - 1} +  \sum_{s=1}^{m-1} \sum_{j=1}^{p}  \sum_{j^{\prime}=1}^{j} n_{2mj^{\prime} - m - s}n_{2mj - m + s - 1}  \\
&-  \sum_{s=1}^{m-1} \sum_{j=1}^{p}\sum_{j^{\prime}=j+1}^{p} n_{2mj^{\prime} - m + s-1}n_{2mj - m + s - 1}  \\ 
& - \sum_{j=0}^{p-1} \sum_{i=1}^{m} n_{2mj+i-1}n_{2mj+i}.
\end{aligned}$$

We now simplify further. The $k=1$ term of the first sum in the second line cancels with the $s=1$ term of the sum in the penultimate line. The first sum on the fourth line cancels with the second sum of the first line once we remove the $k=m-1$ term. This $k=m-1$ term then cancels with the fifth line. The first sum in the sixth line is the $s=m$ term of the sum in the penultimate line. The second sum in the sixth line cancels with the second sum in the second line. The last sum in the sixth line is the $i=0$ term in the last line. Finally, we remove the $j'=j$ term from the first sum in the seventh line and write it in the last line. Thus, [\[lhs\]](#lhs){reference-type="eqref" reference="lhs"} equals

$$\begin{aligned}
& \sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj'-2m+k} n_{2mj-k} + \sum_{k=2}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj'-m+k-1} n_{2mj-m-k+1} \hphantom{xxxxxxxxxx} \\
\end{aligned}$$

$$\label{newlhs2}
\begin{aligned}
& + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj'-s} n_{2mj-2m + s-1} + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj'-m-s} n_{2mj-m + s-1} \\
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj'-2m+s} n_{2mj-2m + s-1} - \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j-1} n_{2mj'-m+s} n_{2mj-m+s-1} \\
& - \sum_{s=2}^{m} \sum_{j'=1}^{p} \sum_{j'=1}^{j-1} n_{2mj'-2m + s-1} n_{2mj-2m+s-1} - \sum_{s=2}^{m} \sum_{j=1}^{p-1} \sum_{j'=j+1}^{p} n_{2mj-m+s-1} n_{2mj'-m+s-1} \\
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p} n_{2mj-m+s} n_{2mj-m+s-1} - \sum_{j=0}^{p-1} \sum_{i=0}^{m} n_{2mj+i-1} n_{2mj+i}.
\end{aligned}$$

Now we see that this is equal to [\[newrhs\]](#newrhs){reference-type="eqref" reference="newrhs"} as follows. The first four lines of [\[newlhs2\]](#newlhs2){reference-type="eqref" reference="newlhs2"} correspond to the first term in [\[newrhs\]](#newrhs){reference-type="eqref" reference="newrhs"}; namely, the first line of ([\[newlhs2\]](#newlhs2){reference-type="ref" reference="newlhs2"}) corresponds to $(i,j) \equiv (i,-i) \mod{2m}$, the second line to $(i,j) \equiv (i, -i-1) \mod{2m}$, the third line to $(i,j) \equiv (i,i-1) \mod{2m}$ and the fourth line to $(i,j) \equiv (i,i) \mod{2m}$. Finally, the fifth line of ([\[newlhs2\]](#newlhs2){reference-type="ref" reference="newlhs2"}) matches the second sum of [\[newrhs\]](#newrhs){reference-type="eqref" reference="newrhs"}. Thus, we have proven that [\[lhs\]](#lhs){reference-type="eqref" reference="lhs"} equals [\[newrhs\]](#newrhs){reference-type="eqref" reference="newrhs"}. ◻
:::

::: proof
*Proof of Theorem [\[main2\]](#main2){reference-type="ref" reference="main2"}.* As ([\[JNK-mp\]](#JNK-mp){reference-type="ref" reference="JNK-mp"}) reduces to ([\[kpneg\]](#kpneg){reference-type="ref" reference="kpneg"}) when $m=1$ and this case was proven in [@takata], we assume $m \geq 2$. Using Lemmas [\[l6\]](#l6){reference-type="ref" reference="l6"} and [\[l7\]](#l7){reference-type="ref" reference="l7"}, one can check that for $l=4mp+1$ and $t=4mp-2p+1$

$$\label{a1}
a({\underline{n}}) = - \sum_{j=1}^{2p - 1} (-1)^j n_{mj}$$

and $b_1({\underline{n}}) + b_2({\underline{n}})$ equals

$$\begin{aligned}
& \sum_{j=1}^{p} \Biggl[ \sum_{i=0}^{m-1} n_{2mj - 2m + i} - \sum_{i=m+1}^{2m-1} n_{2mj-2m+i} \Biggr] \\
& + \sum_{k=1}^{m} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j} (n_{2mj-k+1} - n_{2mj-k})(n_{2mj^{\prime} - 2m + k} - n_{2mj^{\prime} - 2m})  \hphantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx} \\
& - \sum_{s=1}^{m-1} \sum_{j=2}^{p} \sum_{j^{\prime}=2}^{j} (n_{2mj - m - s +1} - n_{2mj-m-s})(n_{2mj^{\prime} - 2m} - n_{2mj^{\prime} - 3m+s}) \\
& + \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=j}^{p} (n_{2mj^{\prime}} - n_{2mj^{\prime} - 2m + 1}) + n_{2mj - 2m +1} \Biggr) n_{2mj-2m} \\
& + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j} (n_{2mj^{\prime} - s} - n_{2mj^{\prime} - 2m + s}) + \sum_{j^{\prime}=j+1}^{p} (n_{2mj^{\prime} - s} - n_{2mj^{\prime} - 2m + s + 1}) \Biggr) n_{2mj-2m+s} \\
\end{aligned}$$

$$\label{b1b2c1}
\begin{aligned}
& - \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=j}^{p} (n_{2mj^{\prime} - m + 1} - n_{2mj^{\prime} - m}) \Biggr) n_{2mj-m} \\
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j-1} (n_{2mj^{\prime} - m + s} - n_{2mj^{\prime} - m - s}) + \sum_{j^{\prime}=j}^{p} (n_{2mj^{\prime} - m + s + 1} - n_{2mj^{\prime} - m - s} ) \Biggr) n_{2mj-m+s}. 
\end{aligned}$$

Also, by ([\[kappa\]](#kappa){reference-type="ref" reference="kappa"}) and ([\[tau\]](#tau){reference-type="ref" reference="tau"})

$$\label{twist1}
\begin{aligned}
X({\underline{n}}) & = (-1)^{n_{2mp}} q^{-Nn_{2mp}} \frac{(q)_{N-1} (q)_{n_{2mp}}}{(q)_{N - n_{2mp} - 1}} \\& \times \prod_{j=1}^{p} \frac{(-1)^{n_{2mj} - n_{2mj-m}} q^{\frac{1}{2} \sum\limits_{s=1}^{m} (n_{2mj-2m+s} - n_{2mj-2m+s-1})(n_{2mj-2m+s} - n_{2mj-2m+s-1} + 1)}}{\displaystyle \prod\limits_{s=1}^{2m} (q)_{n_{2mj-2m+s} - n_{2mj-2m+s-1}}}.
\end{aligned}$$

Upon comparing ([\[spt\]](#spt){reference-type="ref" reference="spt"}) and ([\[a1\]](#a1){reference-type="ref" reference="a1"})--([\[twist1\]](#twist1){reference-type="ref" reference="twist1"}) with ([\[JNK-mp\]](#JNK-mp){reference-type="ref" reference="JNK-mp"}) and then simplifying, it suffices to prove that for $m \geq 2$

$$\begin{aligned}
& \sum_{k=1}^{m} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j} (n_{2mj-k+1} - n_{2mj-k})(n_{2mj^{\prime} - 2m + k} - n_{2mj^{\prime} - 2m}) \\
& - \sum_{s=1}^{m-1} \sum_{j=2}^{p} \sum_{j^{\prime}=2}^{j} (n_{2mj - m - s +1} - n_{2mj-m-s})(n_{2mj^{\prime} - 2m} - n_{2mj^{\prime} - 3m+s}) \\
& + \sum_{j=1}^{p} \sum_{j^{\prime}=j}^{p} (n_{2mj^{\prime}} - n_{2mj^{\prime} - 2m + 1})n_{2mj-2m} + \sum_{j=1}^{p}n_{2mj - 2m +1}n_{2mj-2m} \\
& + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j} (n_{2mj^{\prime} - s} - n_{2mj^{\prime} - 2m + s}) + \sum_{j^{\prime}=j+1}^{p} (n_{2mj^{\prime} - s} - n_{2mj^{\prime} - 2m + s + 1}) \Biggr) n_{2mj-2m+s} \\
& - \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=j}^{p} (n_{2mj^{\prime} - m + 1} - n_{2mj^{\prime} - m}) \Biggr) n_{2mj-m} \\
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j-1} (n_{2mj^{\prime} - m + s} - n_{2mj^{\prime} - m - s}) + \sum_{j^{\prime}=j}^{p} (n_{2mj^{\prime} - m + s + 1} - n_{2mj^{\prime} - m - s} ) \Biggr) n_{2mj-m+s} \\
& + \sum_{j=1}^{p} \Biggl[ \binom{n_{2mj-2m+1} + 1}{2} - n_{2mj-2m+1} n_{2mj-2m} + \binom{n_{2mj-m-1}}{2} - n_{2mj-m} n_{2mj-m-1} \\
\end{aligned}$$

$$\label{lhs2}
\begin{aligned}
& + \frac{1}{2} \sum_{s=2}^{m-1} (n_{2mj-2m+s} - n_{2mj-2m+s-1})(n_{2mj-2m+s} - n_{2mj-2m+s-1} + 1) \Biggr]
\end{aligned}$$

equals

$$\label{Deltasum}
\displaystyle \sum_{\substack{1 \leq i < j \leq 2mp \\ m \nmid i}} \Delta_{i,j,m} n_i n_j$$

where $\Delta_{i,j,m}$ is given by ([\[Deltadef\]](#Deltadef){reference-type="ref" reference="Deltadef"}). Here, we have used ([\[s2\]](#s2){reference-type="ref" reference="s2"}), ([\[s3\]](#s3){reference-type="ref" reference="s3"}) and the fact that

$$\sum_{j=1}^{p} \Biggl[ \sum_{i=0}^{m-1} n_{2mj - 2m + i} - \sum_{i=m+1}^{2m-1} n_{2mj-2m+i} \Biggr] = \sum_{i=1}^{2mp-1} \beta_{i,m} n_i + \sum_{i=1}^{p-1} n_{2mi}$$

where $\beta_{i,m}$ is given by ([\[betadef\]](#betadef){reference-type="ref" reference="betadef"}).

We now sketch how to go from [\[lhs2\]](#lhs2){reference-type="eqref" reference="lhs2"} to [\[Deltasum\]](#Deltasum){reference-type="eqref" reference="Deltasum"}. Let $\hat{L}_i$ denote the $i$th line of [\[lhs2\]](#lhs2){reference-type="eqref" reference="lhs2"}. We first split $\hat{L}_1$ into two parts according to the second factor and note that the sum on $k$ in the second part telescopes. Thus,

$$\label{l1}
\hat{L}_1 = \sum_{k=1}^{m} \sum_{j=1}^{p} \sum_{j'=1}^{j} (n_{2mj-k+1} - n_{2mj-k}) n_{2mj' - 2m + k} + \sum_{j=1}^{p} \sum_{j'=1}^{j} (n_{2mj-m} - n_{2mj}) n_{2mj'-2m}.$$

Similarly, we split $\hat{L}_2$ into two parts according to the second factor and note that the sum on $s$ in the first part telescopes. Thus,

$$\label{l2}
\begin{aligned}
\hat{L}_2 = - \sum_{j=1}^{p} \sum_{j'=1}^{j}  (n_{2mj-m} - n_{2mj-2m+1}) & n_{2mj' - 2m} \\
& + \sum_{s=1}^{m-1} \sum_{j=2}^{p} \sum_{j'=2}^{j} (n_{2mj-m-s+1} - n_{2mj-m-s}) n_{2mj-3m+s}.
\end{aligned}$$

Here, we have used the fact that $n_0:=0$. Now, the $k=m$ term of the first sum in ([\[l1\]](#l1){reference-type="ref" reference="l1"}) cancels with $\hat{L}_5$. If we combine the double sum of ([\[l1\]](#l1){reference-type="ref" reference="l1"}) with the double sum in $\hat{L}_3$, then the resulting sum cancels with the first sum in ([\[l2\]](#l2){reference-type="ref" reference="l2"}). Note that $\hat{L}_i = L_i$ for $i=7$ and $8$. Hence, the single sum in $\hat{L}_3$ cancels with the $i=1$ term of the second sum in ([\[l7l8\]](#l7l8){reference-type="ref" reference="l7l8"}). Putting this together and expanding sums we now have that [\[lhs2\]](#lhs2){reference-type="eqref" reference="lhs2"} equals

$$\label{lhs2new}
\begin{aligned}
& \sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j} n_{2mj-k+1}n_{2mj^{\prime} - 2m + k} -\sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j} n_{2mj-k}n_{2mj^{\prime} - 2m + k}
\\
& + \sum_{s=1}^{m-1} \sum_{j=2}^{p} \sum_{j^{\prime}=2}^{j} n_{2mj - m - s +1}n_{2mj^{\prime} - 3m+s} - \sum_{s=1}^{m-1} \sum_{j=2}^{p} \sum_{j^{\prime}=2}^{j}n_{2mj-m-s} n_{2mj^{\prime} - 3m+s} \\
& + \sum_{s=1}^{m-1} \sum_{j=1}^{p}  \sum_{j^{\prime}=1}^{j} n_{2mj^{\prime} - s}n_{2mj-2m+s} - \sum_{s=1}^{m-1} \sum_{j=1}^{p}  \sum_{j^{\prime}=1}^{j} n_{2mj^{\prime} - 2m + s}n_{2mj-2m+s} \\ 
&+ \sum_{s=1}^{m-1} \sum_{j=1}^{p}\sum_{j^{\prime}=j+1}^{p} n_{2mj^{\prime} - s}n_{2mj-2m+s} - \sum_{s=1}^{m-1} \sum_{j=1}^{p}\sum_{j^{\prime}=j+1}^{p}n_{2mj^{\prime} - 2m + s + 1} n_{2mj-2m+s} \\
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j-1} n_{2mj^{\prime} - m + s}n_{2mj-m+s} + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j-1} n_{2mj^{\prime} - m - s}n_{2mj-m+s} \\
&- \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=j}^{p} n_{2mj^{\prime} - m + s + 1}n_{2mj-m+s} + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=j}^{p}n_{2mj^{\prime} - m - s}n_{2mj-m+s} \\
& + \sum_{j=0}^{p-1} \sum_{i=1}^{m-1} n_{2mj+i}^2 - \sum_{j=0}^{p-1} \sum_{i=2}^{m} n_{2mj+i-1}n_{2mj+i}.
\end{aligned}$$

We combine the $j'=j$ term from the first sum of the third line in ([\[lhs2new\]](#lhs2new){reference-type="ref" reference="lhs2new"}) with the first sum on the fourth line, and then cancel this with the second sum in the first line. Next, the $j'=j$ term in the second sum of the third line cancels with the first sum in the last line. Thus, [\[lhs2\]](#lhs2){reference-type="eqref" reference="lhs2"} equals

$$\begin{aligned}
& \sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j} n_{2mj-k+1}n_{2mj^{\prime} - 2m + k}
\\
& + \sum_{s=1}^{m-1} \sum_{j=2}^{p} \sum_{j^{\prime}=2}^{j} n_{2mj - m - s +1}n_{2mj^{\prime} - 3m+s} - \sum_{s=1}^{m-1} \sum_{j=2}^{p} \sum_{j^{\prime}=2}^{j}n_{2mj-m-s} n_{2mj^{\prime} - 3m+s} \\
& + \sum_{s=1}^{m-1} \sum_{j=1}^{p}  \sum_{j^{\prime}=1}^{j-1} n_{2mj^{\prime} - s}n_{2mj-2m+s} - \sum_{s=1}^{m-1} \sum_{j=1}^{p}  \sum_{j^{\prime}=1}^{j-1} n_{2mj^{\prime} - 2m + s}n_{2mj-2m+s} \\ 
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p}\sum_{j^{\prime}=j+1}^{p}n_{2mj^{\prime} - 2m + s + 1} n_{2mj-2m+s} \\
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j-1} n_{2mj^{\prime} - m + s}n_{2mj-m+s} + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j-1} n_{2mj^{\prime} - m - s}n_{2mj-m+s} \\
\end{aligned}$$

$$\label{lhs2new2}
\begin{aligned}
&- \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=j}^{p} n_{2mj^{\prime} - m + s + 1}n_{2mj-m+s} + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=j}^{p}n_{2mj^{\prime} - m - s}n_{2mj-m+s} \\
& - \sum_{j=0}^{p-1} \sum_{i=2}^{m} n_{2mj+i-1}n_{2mj+i}.
\end{aligned}$$

Now, the last line of ([\[lhs2new2\]](#lhs2new2){reference-type="ref" reference="lhs2new2"}) is just the $j'=j$ term of the fourth line. In the second line, perform the shift $j' \to j'+1$ and start the sum at $j=1$. The second sum on this line then cancels with the second sum of penultimate line, except for the $j'=j$ term. But this term now becomes the $j'=j$ term for the second sum in the fifth line. After simplifying and gathering terms, we have

$$\label{lhs2new4}
\begin{aligned}
& \sum_{k=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j} n_{2mj^{\prime} - 2m + k}n_{2mj-k+1} + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j-1} n_{2mj^{\prime} - m+s}n_{2mj - m - s +1} \\
& + \sum_{s=1}^{m-1} \sum_{j=1}^{p}  \sum_{j^{\prime}=1}^{j-1} n_{2mj^{\prime} - s}n_{2mj-2m+s} + \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j'=1}^{j} n_{2mj^{\prime} - m - s}n_{2mj-m+s} \\
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j-1} n_{2mj^{\prime} - 2m + s}n_{2mj-2m+s} - \sum_{s=1}^{m-1} \sum_{j=1}^{p} \sum_{j^{\prime}=1}^{j-1} n_{2mj^{\prime} - m + s}n_{2mj-m+s} \\
& - \sum_{s=1}^{m-1} \sum_{j=1}^{p}   \sum_{j^{\prime}=1}^{j} n_{2mj^{\prime}-2m+s} n_{2mj - 2m + s + 1}  - \sum_{s=1}^{m-1} \sum_{j=1}^{p}  \sum_{j^{\prime}=1}^{j} n_{2mj^{\prime}-m+s} n_{2mj - m + s + 1} .
\end{aligned}$$

Now we see that this is equal to [\[Deltasum\]](#Deltasum){reference-type="eqref" reference="Deltasum"} as follows. Namely, the first line of ([\[lhs2new4\]](#lhs2new4){reference-type="ref" reference="lhs2new4"}) corresponds to $(i,j) \equiv (i,-i+1)$ mod $2m$, the second line to $(i,j) \equiv (i,-i)$ mod $2m$, the third line to $(i,j) \equiv (i,i)$ mod $2m$ and the fourth line to $(i,j) \equiv (i,i+1)$ mod $2m$. This completes the proof that [\[lhs2\]](#lhs2){reference-type="eqref" reference="lhs2"} is equal to [\[Deltasum\]](#Deltasum){reference-type="eqref" reference="Deltasum"}. ◻
:::

[^1]: Note that there is a misprint in the definition of $X(\underline{n})$ in [@takata]. Each $\overline{q}$ in the prefactor should be $q$.
